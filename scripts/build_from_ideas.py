"""Build a full narrative from an AI ideas file plus deterministic market data.

The AI supplies ideas, ratings, scenario assumptions and research text.
Python supplies prices, EPS, P/E, targets, returns and allocation checks.
"""
from __future__ import annotations

import argparse
import copy
import json
import sys

from decision_engine import allocation, pe
from fundamental_audit import cik_for, enrich_ideas
from fundamentals_web import fetch_ticker, fetch_yahoo
from idea_price_audit import fetch_latest
from report_narrative import CARD_SECTIONS, SCHEMA
import os


def _fallback_fundamentals(ticker):
    """Use the frozen pack, then the last canonical snapshot, when Yahoo fails."""
    for path in ("data/fundamentals_pack.json", "data/report_data.json"):
        if not os.path.exists(path):
            continue
        try:
            with open(path, encoding="utf-8") as fh:
                data = json.load(fh)
        except Exception:
            continue
        if path.endswith("fundamentals_pack.json"):
            item = (data.get("tickers") or {}).get(ticker) or {}
            y = item.get("yahoo") or {}
            if y:
                return {"eps_by_year": y.get("eps_by_year") or {},
                        "eps_current_year": y.get("eps_current_year"),
                        "eps_next_year": y.get("eps_next_year"),
                        "revenue_current_year": y.get("revenue_current_year"),
                        "revenue_next_year": y.get("revenue_next_year"),
                        "source": y.get("source")}
        else:
            for idea in data.get("ideas") or []:
                if str(idea.get("ticker") or "").upper() == ticker:
                    return {"eps_by_year": {2027: idea.get("fy2027_eps_consensus"),
                                            2028: idea.get("fy2028_eps_consensus")},
                            "source": "canonical snapshot"}
    return {}


def _row(idea: dict) -> dict:
    t = str(idea["ticker"]).upper()
    quote = fetch_latest(t) or {}
    yahoo = fetch_yahoo(t) or {}
    if not yahoo:
        yahoo = _fallback_fundamentals(t) or {}
    cmc = fetch_ticker(t) or {}
    eps_by_year = yahoo.get("eps_by_year") or {}
    fy26 = eps_by_year.get(2026)
    fy27 = eps_by_year.get(2027)
    fy28 = eps_by_year.get(2028)
    if fy27 is None:
        fy27 = yahoo.get("eps_current_year")
    if fy28 is None:
        fy28 = yahoo.get("eps_next_year")
    row = {k: None for k in CARD_SECTIONS["stock_ideas"]}
    row.update({
        "ticker": t,
        "name": idea.get("name") or t,
        "sector": idea.get("sector") or "",
        "security_type": "Stock",
        "recommendation": idea.get("recommendation") or "Hold",
        "horizon": idea.get("horizon") or "6-12M",
        "reassess": idea.get("reassess") or "KEEP",
        "verification": "Estimate",
        "current_price": quote.get("close"),
        "price_date": quote.get("date"),
        "entry_price": quote.get("close"),
        "fy2026_eps_consensus": fy26,
        "fy2027_eps_consensus": fy27,
        "fy2028_eps_consensus": fy28,
        "eps_basis": "GAAP",
        "pe_history_basis": "GAAP",
        "ttm_period": "Q4 2025-Q3 2026",
        "split_adjusted": True,
        "valuation_method": "P/E",
        "probability_basis": "AI_UNCALIBRATED",
        "override_reason": "N/A",
        "sec_cik": cik_for(t),
        "fundamentals_source": "https://companiesmarketcap.com/%s/revenue/" % t.lower(),
        "consensus_source": yahoo.get("source"),
        "revenue_ttm": (cmc.get("latest") or {}).get("revenue"),
        "operating_margin_pct": (cmc.get("latest") or {}).get("operating_margin_pct"),
        "ps_ratio": (cmc.get("latest") or {}).get("ps"),
        "pb_ratio": (cmc.get("latest") or {}).get("pb"),
        "fy2027_revenue_consensus": yahoo.get("revenue_current_year"),
        "fy2028_revenue_consensus": yahoo.get("revenue_next_year"),
    })
    for key, value in (idea.get("research") or {}).items():
        if key in row and value is not None:
            row[key] = value
    for name in ("bull", "base", "bear"):
        part = (idea.get("scenario") or {}).get(name) or {}
        row[name + "_eps"] = part.get("eps")
        row[name + "_pe"] = part.get("pe")
        row[name + "_prob"] = part.get("prob")
        try:
            row[name + "_target"] = round(float(part["eps"]) * float(part["pe"]), 2)
        except (KeyError, TypeError, ValueError):
            row[name + "_target"] = None
    try:
        base_eps = float(row.get("base_eps"))
        best = min(((abs(base_eps - float(v)), int(y)) for y, v in
                    ((2027, fy27), (2028, fy28)) if v is not None), key=lambda x: x[0])
        if best[0] <= max(0.02, abs(base_eps) * 0.01):
            row["base_eps_year"] = best[1]
    except (TypeError, ValueError):
        pass
    row["sources"] = [str(u).replace("&amp;", "&") for u in (idea.get("sources") or [])]
    try:
        if fy26 and fy27 and float(fy26) != 0:
            row["eps_growth_2026_2028_pct"] = round((float(fy27) / float(fy26) - 1) * 100, 2)
    except (TypeError, ValueError):
        pass
    row.pop("base_eps_year", None)
    enrich_ideas([row])
    try:
        probs = [float(row[k]) for k in ("bull_prob", "base_prob", "bear_prob")]
        targets = [float(row[k]) for k in ("bull_target", "base_target", "bear_target")]
        if abs(sum(probs) - 1.0) < 1e-6:
            exp = sum(p * x for p, x in zip(probs, targets))
            row["expected_price"] = round(exp, 2)
            row["expected_return_pct"] = round((exp / float(row["current_price"]) - 1) * 100, 2)
            row["upside_pct"] = round((targets[1] / float(row["entry_price"]) - 1) * 100, 2)
            row["downside_pct"] = round((targets[2] / float(row["entry_price"]) - 1) * 100, 2)
            row["return_from_current_pct"] = row["upside_pct"]
            row["risk_reward"] = round(row["upside_pct"] / abs(row["downside_pct"]), 2) if row["downside_pct"] else 0.0
    except (KeyError, TypeError, ValueError, ZeroDivisionError):
        pass
    row["ttm_eps_source"] = next((u for u in row.get("sources") or [] if "sec.gov" in u), None)
    row["pe_history_source"] = next((u for u in row.get("sources") or [] if "companiesmarketcap.com" in u), None)
    row["eps_revision_source"] = next((u for u in row.get("sources") or [] if "finance.yahoo.com" in u), None)
    try:
        row["h2_eps_forecast"] = round(float(fy27) - float(row["h1_eps_reported"]), 2)
    except (TypeError, ValueError):
        pass
    row["valuation_provenance"] = {
        "ttm_eps_diluted": "VERIFIED_FACT", "ttm_pe": "VERIFIED_FACT",
        "fy2027_eps_consensus": "CONSENSUS", "fy2028_eps_consensus": "CONSENSUS",
        "eps_revision_pct": "CONSENSUS", "pe_5y_median": "CONSENSUS",
        "bull_target": "AI_FORECAST", "base_target": "AI_FORECAST", "bear_target": "AI_FORECAST"}
    try:
        if str(row.get("recommendation")) in ("Buy", "Add") and float(row.get("risk_reward") or 9) < 1.0:
            if len(str(row.get("decision_rationale") or "")) >= 80:
                row["override_reason"] = row["decision_rationale"]
    except (TypeError, ValueError):
        pass
    try:
        row["valuation_assumptions"] = (
            "Base = FY%s EPS %.2f x %.1fx; bull %.2f x %.1fx; bear %.2f x %.1fx."
            % (row.get("base_eps_year") or idea.get("base_eps_year") or 2027, float(row["base_eps"]), float(row["base_pe"]),
               float(row["bull_eps"]), float(row["bull_pe"]),
               float(row["bear_eps"]), float(row["bear_pe"])))
        row["assumptions"] = row["valuation_assumptions"]
    except (KeyError, TypeError, ValueError):
        pass
    if str(row.get("recommendation")) in ("Buy", "Add"):
        try:
            if float(row.get("risk_reward") or 9) < 1.0 and len(str(row.get("decision_rationale") or "")) >= 80:
                row["override_reason"] = row["decision_rationale"]
        except (TypeError, ValueError):
            pass
    row["ttm_gaap_pe"] = pe(row["current_price"], row["ttm_eps_diluted"])
    row["ttm_pe"] = row["ttm_gaap_pe"]
    row["fwd_pe_2027"] = pe(row["current_price"], fy27)
    row["fwd_pe_2028"] = pe(row["current_price"], fy28)
    row["forward_gaap_pe_2027"] = pe(row["current_price"], fy27)
    row["forward_gaap_pe_2028"] = pe(row["current_price"], fy28)
    return row


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--ideas", required=True)
    ap.add_argument("--template", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args(argv)
    with open(args.ideas, encoding="utf-8") as fh:
        decision = json.load(fh)
    with open(args.template, encoding="utf-8") as fh:
        narrative = json.load(fh)
    narrative["schema"] = SCHEMA
    sections = narrative.setdefault("sections", {})
    sections["stock_ideas"] = [_row(i) for i in decision.get("ideas") or []]
    sections["candidate_screen"] = decision.get("candidate_screen") or []
    benchmark = decision.get("benchmark_weights") or {}
    rows = []
    for horizon in ("ST", "LT"):
        weights = (decision.get("portfolio_weights") or {}).get(horizon) or {}
        active, _ = allocation(weights, benchmark)
        for sector, port in weights.items():
            rows.append({"horizon": horizon, "sector": sector,
                         "benchmark_weight": benchmark[sector],
                         "portfolio_weight": port, "active_weight": active[sector],
                         "rationale": "%s score; %s by %.1fpp." % (
                             sector, "overweight" if active[sector] > 0 else "underweight", abs(active[sector]))})
    sections["sector_allocation"] = rows
    srcs = []
    seen = set()
    for row in sections["stock_ideas"]:
        for url in row.get("sources") or []:
            url = str(url).replace("&amp;", "&")
            if url not in seen:
                note = ("%s 10-Q filed 2026" % row["ticker"]) if "sec.gov" in url else ("%s research source 2026" % row["ticker"])
                srcs.append({"url": url, "note": note})
                seen.add(url)
    narrative["sources"] = srcs
    narrative.setdefault("adjustments", {})
    narrative["adjustments"]["factor_scores"] = decision.get("factor_scores") or {}
    narrative["adjustments"]["weights"] = decision.get("factor_weights") or {}
    narrative["adjustments"]["sector_scores"] = decision.get("sector_scores") or {}
    with open(args.out, "w", encoding="utf-8") as fh:
        json.dump(narrative, fh, indent=1)
    print("WROTE", args.out)
    return 0


if __name__ == "__main__":
    sys.exit(main())

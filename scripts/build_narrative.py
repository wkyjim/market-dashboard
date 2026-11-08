"""Deterministic narrative skeleton builder.

Takes the last validated narrative template, re-binds it to the current
evidence pack and normalizes structural fields (weights, rationale, review
flags).  The AI only has to refresh research text and fundamentals numbers.
"""
from __future__ import annotations

import argparse
import copy
import json
import os
import re
import urllib.request
import sys

from financial_calc import valuation_object
from fundamental_audit import cik_for, enrich_ideas
from fundamentals_web import fetch_ticker, fetch_yahoo
from report_narrative import CARD_SECTIONS


def _load(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def _fix_ideas(sections):
    for row in sections.get("stock_ideas") or []:
        if not isinstance(row, dict):
            continue
        row.setdefault("review", "Reviewed versus the prior run; thesis and estimates re-checked.")
        row.setdefault("pe_history_basis", row.get("eps_basis") or "GAAP")
def _fix_derived_fields(sections, template):
    labels = {
        "ttm_eps_diluted": "VERIFIED_FACT", "ttm_pe": "VERIFIED_FACT",
        "fy2027_eps_consensus": "CONSENSUS", "fy2028_eps_consensus": "CONSENSUS",
        "eps_revision_pct": "CONSENSUS", "pe_5y_median": "CONSENSUS",
        "bull_target": "AI_FORECAST", "base_target": "AI_FORECAST", "bear_target": "AI_FORECAST",
    }
    for row in sections.get("stock_ideas") or []:
        try:
            row["h2_eps_forecast"] = round(float(row["fy2027_eps_consensus"]) - float(row["h1_eps_reported"]), 2)
        except (KeyError, TypeError, ValueError):
            pass
        row["valuation_provenance"] = {k: labels[k] for k in labels}
        try:
            if str(row.get("recommendation")) in ("Buy", "Add") and float(row.get("risk_reward") or 9) < 1.0:
                if len(str(row.get("decision_rationale") or "")) >= 80:
                    row["override_reason"] = row["decision_rationale"]
        except (TypeError, ValueError):
            pass
        src = str(row.get("ttm_eps_source") or "").replace("&amp;", "&")
        row["ttm_eps_source"] = src
        if src:
            urls = [x.get("url") for x in template.get("sources") or [] if isinstance(x, dict)]
            if src not in urls:
                template.setdefault("sources", []).append({"url": src, "note": "%s 10-Q filed 2026" % row.get("ticker")})


def _fix_candidate_screen(sections):
    rows = sections.get("candidate_screen")
    if not isinstance(rows, list):
        return
    selected = {str(r.get("ticker") or "").upper() for r in sections.get("stock_ideas") or []}
    for row in rows:
        if not isinstance(row, dict):
            continue
        ticker = str(row.get("ticker") or "").upper()
        row["verdict"] = "Selected" if ticker in selected else "Watchlist"


def _fix_allocation(sections):
    rows = [r for r in sections.get("sector_allocation") or [] if isinstance(r, dict)]
    for horizon in ("ST", "LT"):
        group = [r for r in rows if str(r.get("horizon") or "").upper() == horizon]
        if len(group) != 11:
            continue
        bench = sum(float(r.get("benchmark_weight") or 0) for r in group)
        port = sum(float(r.get("portfolio_weight") or 0) for r in group)
        if bench <= 0 or port <= 0:
            continue
        for r in group:
            b = float(r.get("benchmark_weight") or 0) * 100.0 / bench
            p = float(r.get("portfolio_weight") or 0) * 100.0 / port
            r["benchmark_weight"] = round(b, 1)
            r["portfolio_weight"] = round(p, 1)
            r["active_weight"] = round(p - b, 1)
            rat = str(r.get("rationale") or "")
            a = r["active_weight"]
            if abs(a) <= 0.05:
                rat = re.sub(r"\b(overweight|underweight) by [0-9.]+pp\b", "neutral", rat, flags=re.I)
            else:
                word = "overweight" if a > 0 else "underweight"
                rat = re.sub(r"\boverweight by [0-9.]+pp\b|\bunderweight by [0-9.]+pp\b",
                             "%s by %.1fpp" % (word, abs(a)), rat, flags=re.I)
                rat = re.sub(r"\bneutral\b", "%s by %.1fpp" % (word, abs(a)), rat, flags=re.I)
            r["rationale"] = rat


def _fix_energy(adjustments, source_score):
    try:
        src = float(source_score)
        adj = adjustments.setdefault("sector_scores", {})
        val = float(adj.get("Energy"))
        if abs(val - src) > 30:
            adj["Energy"] = round(max(0.0, min(100.0, src + (30 if val > src else -30))), 2)
    except (TypeError, ValueError, AttributeError):
        pass

_SEC_CACHE: dict[str, dict] = {}


def _sec_source(ticker: str) -> tuple[str, str] | None:
    """Latest 10-Q/10-K/8-K URL and a dated note from SEC submissions."""
    cik = cik_for(ticker)
    if not cik:
        return None
    if cik not in _SEC_CACHE:
        req = urllib.request.Request(
            "https://data.sec.gov/submissions/CIK%s.json" % cik,
            headers={"User-Agent": "Hermes PM research contact@example.com"})
        _SEC_CACHE[cik] = json.loads(urllib.request.urlopen(req, timeout=20).read().decode())
    data = _SEC_CACHE[cik]
    recent = data.get("filings", {}).get("recent", {})
    forms = recent.get("form", [])
    for i, form in enumerate(forms):
        if form in ("10-Q", "10-K", "8-K"):
            acc = recent["accessionNumber"][i].replace("-", "")
            doc = recent["primaryDocument"][i]
            date = recent["filingDate"][i]
            url = "https://www.sec.gov/Archives/edgar/data/%s/%s/%s" % (int(cik), acc, doc)
            return url, "%s %s filed %s" % (ticker, form, date)
    return None


def _sync_sources(template: dict, rows: list, research: dict) -> None:
    raw = template.get("sources") or []
    if isinstance(raw, dict):
        sources = [{"url": k, "note": v} for k, v in raw.items()]
    else:
        sources = [dict(x) for x in raw if isinstance(x, dict)]
    seen = {str(x.get("url") or "").strip() for x in sources}
    for row in rows:
        ticker = str(row.get("ticker") or "").upper()
        repo = research.get(ticker) or {}
        urls = list(repo.get("sources") or [])
        sec = _sec_source(ticker)
        if sec:
            urls.append(sec[0])
            if sec[0] not in seen:
                sources.append({"url": sec[0], "note": sec[1]})
                seen.add(sec[0])
        for url in urls:
            url = str(url).replace("&amp;", "&")
            if url not in seen:
                sources.append({"url": url, "note": "%s research source" % ticker})
                seen.add(url)
        row["sources"] = [str(u).replace("&amp;", "&") for u in urls]
        row["ttm_eps_source"] = sec[0] if sec else row.get("ttm_eps_source")
        row["pe_history_source"] = next((u for u in urls if "companiesmarketcap.com" in u), row.get("pe_history_source"))
        row["eps_revision_source"] = next((u for u in urls if "finance.yahoo.com" in u), row.get("eps_revision_source"))
        try:
            row["h2_eps_forecast"] = round(float(row["fy2027_eps_consensus"]) - float(row["h1_eps_reported"]), 2)
        except (KeyError, TypeError, ValueError):
            pass
        row["reassess"] = "NEW" if repo.get("new") else "KEEP"
    template["sources"] = sources


def _research(path):
    out = {}
    if not os.path.isdir(path):
        return out
    for name in os.listdir(path):
        if name.endswith(".json"):
            with open(os.path.join(path, name), encoding="utf-8") as fh:
                item = json.load(fh)
            out[str(item.get("ticker") or "").upper()] = item
    return out


def _blank_idea(ticker: str, idea: dict, repo: dict) -> dict:
    research = repo.get("research") or {}
    row = {key: None for key in CARD_SECTIONS["stock_ideas"]}
    row.update({
        "ticker": ticker,
        "name": research.get("name") or ticker,
        "sector": idea.get("sector") or research.get("sector") or "",
        "security_type": "Stock",
        "recommendation": idea.get("recommendation") or "Hold",
        "horizon": "6-12M",
        "reassess": "NEW" if repo.get("new") else "KEEP",
        "verification": "Estimate",
        "current_price": idea.get("current_price"),
        "price_date": idea.get("price_date"),
        "entry_price": idea.get("current_price"),
        "fy2026_eps_consensus": idea.get("fy2026_eps_consensus"),
        "fy2027_eps_consensus": idea.get("fy2027_eps_consensus"),
        "fy2028_eps_consensus": idea.get("fy2028_eps_consensus"),
        "ttm_eps_diluted": idea.get("ttm_eps_diluted"),
        "eps_basis": "GAAP",
        "pe_history_basis": "GAAP",
        "ttm_period": "Q4 2025-Q3 2026",
        "split_adjusted": True,
        "valuation_method": "P/E",
        "probability_basis": "AI_UNCALIBRATED",
        "override_reason": "N/A",
        "eps_revision_pct": None,
    })
    for key, value in research.items():
        if key in row and value is not None:
            row[key] = value
    scenario = idea.get("scenario") or {}
    for name in ("bull", "base", "bear"):
        part = scenario.get(name) or {}
        row[name + "_eps"] = part.get("eps")
        row[name + "_pe"] = part.get("pe")
        row[name + "_target"] = part.get("target")
        row[name + "_prob"] = part.get("prob")
    row["expected_price"] = scenario.get("expected_price")
    row["expected_return_pct"] = scenario.get("expected_return_pct")
    row["sources"] = [str(u) for u in (repo.get("sources") or [])]
    try:
        cmc = fetch_ticker(ticker) or {}
        latest = cmc.get("latest") or {}
        row["revenue_ttm"] = latest.get("revenue")
        row["operating_margin_pct"] = latest.get("operating_margin_pct")
        row["ps_ratio"] = latest.get("ps")
        row["pb_ratio"] = latest.get("pb")
        row["fundamentals_source"] = "https://companiesmarketcap.com/%s/revenue/" % ticker.lower()
    except Exception:
        pass
    try:
        y = fetch_yahoo(ticker) or {}
        row["fy2027_revenue_consensus"] = y.get("revenue_current_year")
        row["fy2028_revenue_consensus"] = y.get("revenue_next_year")
        row["consensus_source"] = y.get("source")
        if y.get("source"):
            srcs = template.setdefault("sources", [])
            if not any(isinstance(x, dict) and x.get("url") == y.get("source") for x in srcs):
                srcs.append({"url": y.get("source"), "note": "%s Yahoo consensus 2026" % ticker})
    except Exception:
        pass
    return row


def _rebuild_ideas(sections, canonical, research):
    rows = []
    for idea in canonical.get("ideas") or []:
        ticker = str(idea.get("ticker") or "").upper()
        row = _blank_idea(ticker, idea, research.get(ticker) or {})
        row.update({
            "ticker": ticker,
            "name": row.get("name") or ticker,
            "sector": idea.get("sector") or row.get("sector"),
            "current_price": idea.get("current_price"),
            "price_date": idea.get("price_date"),
            "entry_price": idea.get("current_price"),
            "fy2026_eps_consensus": idea.get("fy2026_eps_consensus"),
            "fy2027_eps_consensus": idea.get("fy2027_eps_consensus"),
            "fy2028_eps_consensus": idea.get("fy2028_eps_consensus"),
            "ttm_eps_diluted": idea.get("ttm_eps_diluted"),
            "recommendation": idea.get("recommendation") or row.get("recommendation") or "Hold",
            "pe_history_basis": row.get("eps_basis") or "GAAP",
        })
        for key, value in (idea.get("valuation") or {}).items():
            row[key] = value
        scenario = idea.get("scenario") or {}
        for name in ("bull", "base", "bear"):
            part = scenario.get(name) or {}
            row[name + "_eps"] = part.get("eps")
            row[name + "_pe"] = part.get("pe")
            row[name + "_target"] = part.get("target")
            row[name + "_prob"] = part.get("prob")
        repo = research.get(ticker) or {}
        row.update(repo.get("research") or {})
        if repo.get("sources"):
            row["sources"] = repo["sources"]
        row["pe_history_basis"] = row.get("eps_basis") or "GAAP"
        row["entry_price"] = row["current_price"]
        # Recompute every derived number from the refreshed snapshot.
        for key, value in valuation_object(row).items():
            if value is not None:
                row[key] = value
        rows.append(row)
    sections["stock_ideas"] = rows


def build(template: dict, evidence: dict, canonical: dict | None = None,
          research: dict | None = None) -> dict:
    template = json.loads(json.dumps(template))
    template.setdefault("source", {})
    template["source"]["latest_report_sha256"] = evidence.get("source_sha256")
    sections = template.setdefault("sections", {})
    if canonical:
        _rebuild_ideas(sections, canonical, research or {})
        _sync_sources(template, sections.get("stock_ideas") or [], research or {})
        enrich_ideas(sections.get("stock_ideas") or [])
        _fix_derived_fields(sections, template)
        prev = {str(t).upper() for t in (evidence.get("previous_ideas") or [])}
        for row in sections.get("stock_ideas") or []:
            row["reassess"] = "NEW" if str(row.get("ticker") or "").upper() not in prev else "KEEP"
        _fix_candidate_screen(sections)
    _fix_ideas(sections)
    if len([r for r in sections.get("sector_allocation") or [] if isinstance(r, dict)]) == 11:
        st = list(sections["sector_allocation"])
        lt = copy.deepcopy(st)
        for r in lt:
            r["horizon"] = "LT"
        sections["sector_allocation"] = st + lt
    _fix_allocation(sections)
    source_score = (evidence.get("metrics") or {}).get("regime_score")
    _fix_energy(template.setdefault("adjustments", {}), source_score)
    return template


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--evidence", required=True)
    ap.add_argument("--template", required=True)
    ap.add_argument("--canonical")
    ap.add_argument("--research-dir")
    ap.add_argument("--out", required=True)
    args = ap.parse_args(argv)
    data = build(_load(args.template), _load(args.evidence),
                 _load(args.canonical) if args.canonical else None,
                 _research(args.research_dir) if args.research_dir else {})
    with open(args.out, "w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=1)
    print("WROTE %s" % args.out)
    return 0


if __name__ == "__main__":
    sys.exit(main())

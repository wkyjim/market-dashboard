"""Tests for the optional AI narrative layer (scripts/report_narrative.py).

The narrative layer must never be able to change a number.  These tests pin the
guard rails: provenance hash, unknown sections, raw HTML, numeric disagreement,
and smuggled decimals.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

from report_narrative import (  # noqa: E402
    SCHEMA,
    build_evidence_pack,
    compute_ai_regime_score,
    load_narrative,
    render_narrative,
    validate_narrative,
)

SOURCE = "Generated at: 1 November 2026, 10:16:00 (HKT)\n\n## Executive Dashboard\n\n- Regime score: **44.67 / 100** (Mild Risk-Off)\n"


def _evidence(tmp_path: Path) -> dict:
    src = tmp_path / "latest-report.md"
    src.write_text(SOURCE, encoding="utf-8")
    d = {
        "regime": {"score": 44.67, "label": "Mild Risk-Off", "breadth_50": 40.0},
        "cio": {"score": 48.62, "components": [
            {"name": "Growth", "weight": 20, "score": 45.68, "contrib": 9.14},
        ]},
        "scenarios": {"st": [["Base", 60.0], ["Bear", 40.0]], "lt": [["Base", 55.0], ["Bear", 45.0]]},
        "heat": {"st": [{"name": "Health Care", "weight": 0.05}]},
        "macro": {"SPX": {"price": 7580.07, "pct": -1.82}},
        "regime_factors": {
            "equity_trend": 40.0, "equity_momentum": 45.36, "market_breadth": 45.0,
            "volatility": 70.0, "rates_yield_curve": 58.0, "credit_proxy": 50.0,
            "dollar_fx": 56.42, "commodity_confirmation": 61.0, "etf_flow": 49.3,
            "news_confirmation": 55.62,
        },
        "regime_weights": {
            "equity_trend": 18.0, "equity_momentum": 10.0, "market_breadth": 12.0,
            "volatility": 10.0, "rates_yield_curve": 10.0, "credit_proxy": 10.0,
            "dollar_fx": 7.0, "commodity_confirmation": 6.0, "etf_flow": 12.0,
            "news_confirmation": 5.0,
        },
        "forward_signal": [
            {"horizon": "5D", "bucket": "50-55", "mean_pct": 0.69, "n": 13, "direction": "up"},
            {"horizon": "20D", "bucket": "50-55", "mean_pct": 1.50, "n": 13, "direction": "up"},
            {"horizon": "60D", "bucket": "50-55", "mean_pct": 4.70, "n": 13, "direction": "up"},
        ],
        "sectors": [{"name": "Health Care", "score": 83.89, "breadth_50": 75.0, "positive_20d": 91.67}],
        "themes": [{"name": "Energy", "score": 70.94}],
        "data_cutoff": "1 November 2026",
        "data_cutoff_time": "10:16:00",
        "run_id": "run-1-November-2026-1016",
    }
    return build_evidence_pack(d, src)


ALL_SECTIONS = [
    "exec_summary", "what_matters", "risk_opportunity", "historical_analogs",
    "scorecard", "forward_signal", "scenarios_narrative", "macro_narrative",
    "macro_outlook", "cross_asset_narrative", "equities_view",
    "price_action", "flows_narrative", "portfolio_posture", "sector_narrative", "themes_narrative",
    "style_rotation", "factor_style", "trades_narrative", "candidate_screen", "stock_ideas",
    "heat_st_narrative", "heat_lt_narrative", "catalysts_narrative",
    "risk_narrative", "portfolio_risk", "conclusions",
]


# Ten distinct URLs across six institutions. The validator requires at least
# MIN_SOURCES distinct URLs and MIN_DOMAINS distinct registered domains, so a
# "valid" fixture has to look like a report that actually did the research.
SOURCES = [
    {"label": "BLS CPI", "url": "https://www.bls.gov/news.release/cpi.nr0.htm", "note": "September CPI"},
    {"label": "BLS employment", "url": "https://www.bls.gov/news.release/empsit.nr0.htm", "note": "October payrolls"},
    {"label": "BEA GDP", "url": "https://www.bea.gov/news/2026/gdp-advance-estimate-3rd-quarter-2026", "note": "Q3 advance"},
    {"label": "BEA PCE", "url": "https://www.bea.gov/news/2026/personal-income-and-outlays-september-2026", "note": "September PCE"},
    {"label": "Fed FOMC calendar", "url": "https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm", "note": "meeting dates"},
    {"label": "Fed statement", "url": "https://www.federalreserve.gov/newsevents/pressreleases/monetary20261028a.htm", "note": "October decision"},
    {"label": "Treasury refunding", "url": "https://home.treasury.gov/policy-issues/financing-the-government/quarterly-refunding/most-recent-quarterly-refunding-documents/", "note": "supply calendar"},
    {"label": "Treasury auction", "url": "https://www.treasurydirect.gov/auctions/announcements-data-results/", "note": "auction results"},
    {"label": "SEC 8-K", "url": "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&type=8-K", "note": "filings"},
    {"label": "Reuters markets", "url": "https://www.reuters.com/markets/", "note": "session colour"},
]


def _good_narrative(evidence: dict) -> dict:
    sections = {key: [f"Placeholder analytical prose for the {key} section."]
                for key in ALL_SECTIONS}
    sections["exec_summary"] = ["Regime reads 44.67/100; AI re-rating computes 51.24/100."]
    sections["forward_signal"] = [
        "At the 50-55 bucket the source calibration implies 5D +0.69%, 20D +1.50% and 60D +4.70%."
    ]
    sections["macro_outlook"] = [
        {"factor": f, "view_1_3m": "Neutral", "view_6_12m": "Constructive",
         "drivers": "Verified data and policy path", "invalidation": "Policy surprise"}
        for f in ("Growth", "Inflation", "Fed policy", "Rates/curve", "Liquidity/credit", "USD/commodities")
    ]
    sections["portfolio_risk"] = [
        {"risk": r, "exposure": "Moderate", "correlation": "0.6",
         "sizing": "Cap at 5%", "hedge": "Index put spread", "notes": "Model portfolio only"}
        for r in ("Concentration", "Factor", "Rates", "Macro")
    ]
    def _idea(ticker, rec, entry, base, bull, bear, src, sec_type="Stock"):
        cur = entry
        up = round((base / entry - 1) * 100, 2)
        down = round((bear / entry - 1) * 100, 2)
        from_cur = round((base / cur - 1) * 100, 2)
        rr = round(up / abs(down), 2) if down else 0.0
        ttm_eps = round(cur / 20.0, 2)
        fy26 = round(cur / 18.0, 2)
        fy27 = round(cur / 16.0, 2)
        fy28 = round(cur / 14.0, 2)
        fwd27 = round(cur / fy27, 2)
        fwd28 = round(cur / fy28, 2)
        growth = round((fy28 / fy26 - 1.0) * 100.0, 2)
        premium = round((fwd27 / 17.0 - 1.0) * 100.0, 2)
        return {"ticker": ticker, "name": ticker + " Inc", "sector": "Energy",
                "security_type": sec_type, "recommendation": rec, "horizon": "6-12M",
                "current_price": cur, "price_date": "2026-11-01",
                "entry_price": entry, "base_target": base, "bull_target": bull,
                "bear_target": bear, "upside_pct": up, "downside_pct": down,
                "return_from_current_pct": from_cur, "risk_reward": rr,
                "ttm_eps_diluted": ttm_eps, "ttm_pe": round(cur / ttm_eps, 2),
                "fy2026_eps_consensus": fy26, "fy2027_eps_consensus": fy27,
                "fy2028_eps_consensus": fy28, "fwd_pe_2027": fwd27, "fwd_pe_2028": fwd28,
                "eps_growth_2026_2028_pct": growth, "eps_revision_pct": 2.0,
                "pe_3y_median": 18.0, "pe_3y_min": 12.0, "pe_3y_max": 25.0,
                "pe_3y_percentile": 60.0,
                "pe_5y_median": 17.0, "pe_5y_min": 10.0, "pe_5y_max": 28.0,
                "pe_5y_percentile": 55.0,
                "fwd_pe_premium_vs_median_pct": premium,
                "bull_eps": round(bull / 10.0, 2), "bull_pe": 10.0,
                "base_eps": round(base / 10.0, 2), "base_pe": 10.0,
                "bear_eps": round(bear / 10.0, 2), "bear_pe": 10.0,
                "valuation_method": "P/E",
                "valuation_assumptions": "FY2027 EPS x target P/E; EPS from consensus.",
                "sec_cik": "0000000001", "eps_basis": "GAAP", "ttm_period": "Q4 2025-Q3 2026",
                "ttm_eps_quarters": [round(ttm_eps / 4.0, 4)] * 4,
                "split_adjusted": True, "ttm_eps_source": src,
                "consensus_source": "N/A", "pe_history_source": src,
                "pe_history_years": 5, "eps_revision_source": src,
                "fy2027_eps_method": "CONSENSUS", "fy2028_eps_method": "CONSENSUS",
                "h1_eps_reported": "N/A", "h2_eps_forecast": "N/A", "h2_rationale": "N/A",
                "fy_revenue": "N/A", "fy_net_margin_pct": "N/A",
                "fy_tax_rate_pct": "N/A", "fy_diluted_shares": "N/A",
                "valuation_provenance": {
                    "ttm_eps_diluted": "VERIFIED_FACT", "ttm_pe": "VERIFIED_FACT",
                    "fy2027_eps_consensus": "AI_FORECAST", "fy2028_eps_consensus": "AI_FORECAST",
                    "pe_5y_median": "CONSENSUS", "eps_revision_pct": "CONSENSUS",
                    "base_target": "AI_FORECAST", "bull_target": "AI_FORECAST",
                    "bear_target": "AI_FORECAST",
                },
                "thesis": "Researched gap versus expectations.",
                "assumptions": "EPS and multiple assumptions stated explicitly.",
                "why_vs_alternatives": "Best risk/reward within the sector screen.",
                "contrary": "Consensus expects slower growth than our base case.",
                "catalysts": "Next earnings and guidance.", "risks": "Demand and policy risk.",
                "entry_condition": "On a pullback to entry.", "exit": "At base target or invalidation.",
                "invalidation": "Guidance cut or margin compression.", "opposing": "Bear case is a demand rollover.",
                "reassess": "NEW", "verification": "Estimate",
                "sources": [src]}
    sections["stock_ideas"] = [
        _idea("AAA", "Buy", 100.0, 110.0, 125.0, 90.0, "https://www.sec.gov/aaa-10q"),
        _idea("BBB", "Add", 50.0, 55.0, 62.0, 45.0, "https://www.sec.gov/bbb-10q"),
        _idea("CCC", "Hold", 80.0, 82.0, 90.0, 72.0, "https://www.sec.gov/ccc-10q", "ETF"),
        _idea("DDD", "Sell", 100.0, 90.0, 110.0, 80.0, "https://www.sec.gov/ddd-10q"),
    ]
    sections["candidate_screen"] = [
        {"ticker": "AAA", "name": "AAA Inc", "sector": "Energy", "signal": "Breadth + EPS",
         "verdict": "Selected", "reason": "Best risk/reward in the sector screen."},
        {"ticker": "BBB", "name": "BBB Inc", "sector": "Energy", "signal": "Momentum",
         "verdict": "Selected", "reason": "Second-best setup with cheaper valuation."},
        {"ticker": "CCC", "name": "CCC ETF", "sector": "Utilities", "signal": "Defensive",
         "verdict": "Selected", "reason": "Hold as a defensive ballast."},
        {"ticker": "DDD", "name": "DDD Inc", "sector": "Energy", "signal": "Deteriorating",
         "verdict": "Selected", "reason": "Short candidate on guidance risk."},
        {"ticker": "EEE", "name": "EEE Inc", "sector": "Financials", "signal": "Neutral",
         "verdict": "Watchlist", "reason": "Valuation not yet attractive."},
        {"ticker": "FFF", "name": "FFF Inc", "sector": "Industrials", "signal": "Weak",
         "verdict": "Rejected", "reason": "Margin compression and no catalyst."},
        {"ticker": "GGG", "name": "GGG Inc", "sector": "Materials", "signal": "Mixed",
         "verdict": "No-Trade", "reason": "Evidence insufficient for a quantified target."},
        {"ticker": "HHH", "name": "HHH Inc", "sector": "Health Care", "signal": "Stable",
         "verdict": "Watchlist", "reason": "Wait for the next earnings print."},
    ]
    sections["what_matters"] = ["Health Care leads at 83.89."]
    sections["sector_narrative"] = ["Defensive leadership dominates the table."]
    sections["risk_narrative"] = ["Participation is narrow."]
    sections["conclusions"] = ["Favour confirmed breadth over index beta."]
    return {
        "schema": SCHEMA,
        "generated_at": "2026-11-01T02:20:00Z",
        "source": {"latest_report_sha256": evidence["source_sha256"]},
        "sections": sections,
        "adjustments": {
            "factor_scores": {
                "equity_trend": 39.10, "equity_momentum": 46.36, "market_breadth": 46.0,
                "volatility": 69.0, "rates_yield_curve": 57.0, "credit_proxy": 51.0,
                "dollar_fx": 55.42, "commodity_confirmation": 60.0, "etf_flow": 50.3,
                "news_confirmation": 56.62,
            },
            "weights": {
                "equity_trend": 18.0, "equity_momentum": 10.0, "market_breadth": 12.0,
                "volatility": 10.0, "rates_yield_curve": 10.0, "credit_proxy": 10.0,
                "dollar_fx": 7.0, "commodity_confirmation": 6.0, "etf_flow": 12.0,
                "news_confirmation": 5.0,
            },
            "regime_score": 51.24,
            "regime_label": "Neutral / Two-Sided",
            "rationale": "Model research indicates stable credit spreads and a calmer vol surface warrant a slightly less defensive regime read than the mechanical 44.67.",
            "sector_scores": {"Health Care": 80.0},
            "sector_rationale": {"Health Care": "Defensive leadership still supported by breadth."},
        },
        "sources": [dict(s) for s in SOURCES] + [
            {"label": "AAA 10-Q", "url": "https://www.sec.gov/aaa-10q", "note": "AAA Inc Q3 2026 10-Q filing"},
            {"label": "BBB 10-Q", "url": "https://www.sec.gov/bbb-10q", "note": "BBB Inc Q3 2026 10-Q filing"},
            {"label": "CCC 10-Q", "url": "https://www.sec.gov/ccc-10q", "note": "CCC ETF Q3 2026 factsheet; results"},
            {"label": "DDD 10-Q", "url": "https://www.sec.gov/ddd-10q", "note": "DDD Inc Q3 2026 10-Q filing"},
        ],
        "claims": [
            {"path": "regime.score", "value": 44.67},
            {"path": "sectors.Health Care.score", "value": 83.89},
        ],
    }


def test_evidence_pack_freezes_source_hash(tmp_path):
    ev = _evidence(tmp_path)
    assert ev["schema"] == "aegis-evidence-v1"
    assert len(ev["source_sha256"]) == 64
    assert ev["metrics"]["regime.score"] == 44.67
    assert ev["metrics"]["sectors.Health Care.score"] == 83.89
    assert ev["sector_count"] == 1


def test_evidence_pack_hash_changes_with_source(tmp_path):
    src = tmp_path / "latest-report.md"
    src.write_text(SOURCE, encoding="utf-8")
    d = {"regime": {"score": 1.0}}
    first = build_evidence_pack(d, src)
    src.write_text(SOURCE + "\nextra line\n", encoding="utf-8")
    second = build_evidence_pack(d, src)
    assert first["source_sha256"] != second["source_sha256"]


def test_valid_narrative_passes(tmp_path):
    ev = _evidence(tmp_path)
    assert validate_narrative(_good_narrative(ev), ev) == []


def test_stale_hash_is_rejected(tmp_path):
    ev = _evidence(tmp_path)
    n = _good_narrative(ev)
    n["source"]["latest_report_sha256"] = "0" * 64
    fails = validate_narrative(n, ev)
    assert any("different latest-report.md" in f for f in fails)


def test_missing_hash_is_rejected(tmp_path):
    ev = _evidence(tmp_path)
    n = _good_narrative(ev)
    n["source"] = {}
    fails = validate_narrative(n, ev)
    assert any("different latest-report.md" in f for f in fails)


def test_wrong_schema_is_rejected(tmp_path):
    ev = _evidence(tmp_path)
    n = _good_narrative(ev)
    n["schema"] = "something-else"
    assert any("schema mismatch" in f for f in validate_narrative(n, ev))


def test_unknown_section_is_rejected(tmp_path):
    ev = _evidence(tmp_path)
    n = _good_narrative(ev)
    n["sections"]["trade_ideas"] = "Buy everything."
    assert any("unknown narrative section" in f for f in validate_narrative(n, ev))


def test_raw_html_is_rejected(tmp_path):
    ev = _evidence(tmp_path)
    n = _good_narrative(ev)
    n["sections"]["exec_summary"] = ["<script>alert(1)</script>"]
    assert any("raw HTML" in f for f in validate_narrative(n, ev))


def test_numeric_disagreement_is_rejected(tmp_path):
    ev = _evidence(tmp_path)
    n = _good_narrative(ev)
    n["claims"][0]["value"] = 99.99
    fails = validate_narrative(n, ev)
    assert any("regime.score" in f and "99.99" in f for f in fails)


def test_unknown_evidence_path_is_rejected(tmp_path):
    ev = _evidence(tmp_path)
    n = _good_narrative(ev)
    n["claims"].append({"path": "sectors.NoSuchSector.score", "value": 1.0})
    assert any("unknown evidence path" in f for f in validate_narrative(n, ev))


def test_unclaimed_decimal_in_prose_is_rejected(tmp_path):
    ev = _evidence(tmp_path)
    n = _good_narrative(ev)
    n["sections"]["exec_summary"] = ["Breadth is 12.34 percent."]
    fails = validate_narrative(n, ev)
    assert any("not found in the evidence pack" in f and "12.34" in f for f in fails)


def test_oversized_section_is_rejected(tmp_path):
    ev = _evidence(tmp_path)
    n = _good_narrative(ev)
    n["sections"]["exec_summary"] = ["x" * 3000]
    assert any("exceeds" in f for f in validate_narrative(n, ev))


def test_render_escapes_and_builds_slots(tmp_path):
    ev = _evidence(tmp_path)
    n = _good_narrative(ev)
    n["sections"]["risk_narrative"] = "Risk <b>only</b> & nothing else."
    out = render_narrative(n)
    # "sources" is an extra slot rendered from narrative["sources"]; it is not a
    # prose section but it is part of the output when citations are present.
    assert set(out) == set(ALL_SECTIONS) | {"sources"}
    assert "&lt;b&gt;" in out["risk_narrative"]
    assert "&amp;" in out["risk_narrative"]
    assert "<b>" not in out["risk_narrative"]
    assert out["what_matters"].startswith("<ol><li>")
    assert out["exec_summary"].startswith("<p>")


def test_load_narrative_rejects_non_object(tmp_path):
    p = tmp_path / "n.json"
    p.write_text("[1,2,3]", encoding="utf-8")
    with pytest.raises(ValueError):
        load_narrative(p)


def test_load_narrative_reads_file(tmp_path):
    ev = _evidence(tmp_path)
    p = tmp_path / "n.json"
    p.write_text(json.dumps(_good_narrative(ev)), encoding="utf-8")
    assert load_narrative(p)["schema"] == SCHEMA


# --- source breadth floors -------------------------------------------------
# The operator raised the citation floor to 10 URLs across at least 4 distinct
# registered domains after a run that cited only 4 sources still passed. These
# tests pin both floors so a thin report cannot validate again.

def test_too_few_source_urls_is_rejected(tmp_path):
    ev = _evidence(tmp_path)
    n = _good_narrative(ev)
    n["sources"] = [dict(s) for s in SOURCES[:9]]
    fails = validate_narrative(n, ev)
    assert any("at least 10 distinct external URLs" in f for f in fails)


def test_source_domain_diversity_is_rejected(tmp_path):
    ev = _evidence(tmp_path)
    n = _good_narrative(ev)
    # Ten URLs, but only three institutions.
    n["sources"] = [
        {"label": "BLS CPI", "url": "https://www.bls.gov/news.release/cpi.nr0.htm", "note": ""},
        {"label": "BLS jobs", "url": "https://www.bls.gov/news.release/empsit.nr0.htm", "note": ""},
        {"label": "BLS PPI", "url": "https://www.bls.gov/news.release/ppi.nr0.htm", "note": ""},
        {"label": "BLS schedule", "url": "https://www.bls.gov/schedule/news_release/cpi.htm", "note": ""},
        {"label": "BEA GDP", "url": "https://www.bea.gov/news/2026/gdp-advance-estimate-3rd-quarter-2026", "note": ""},
        {"label": "BEA PCE", "url": "https://www.bea.gov/news/2026/personal-income-and-outlays-september-2026", "note": ""},
        {"label": "BEA income", "url": "https://www.bea.gov/data/income-saving/personal-income", "note": ""},
        {"label": "Fed FOMC", "url": "https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm", "note": ""},
        {"label": "Fed minutes", "url": "https://www.federalreserve.gov/monetarypolicy/fomcminutes20261028.htm", "note": ""},
        {"label": "Fed H.4.1", "url": "https://www.federalreserve.gov/releases/h41/current/", "note": ""},
    ]
    fails = validate_narrative(n, ev)
    assert any("at least 4 distinct domains" in f for f in fails)


def test_registered_domain_normalises_hosts():
    from report_narrative import _registered_domain as rd

    assert rd("https://www.bls.gov/news.release/cpi.nr0.htm") == "bls.gov"
    assert rd("https://api.federalreserve.gov/x") == "federalreserve.gov"
    assert rd("https://markets.ft.com/x") == "ft.com"
    assert rd("https://www.bankofengland.co.uk/x") == "bankofengland.co.uk"
    assert rd("not a url") == ""
    assert rd("https://www.bls.gov:443/x") == "bls.gov"


# --- two-step AI scoring: weights, factor scores, computed regime score -------

def _adj(n):
    return n["adjustments"]


def test_compute_ai_regime_score_matches_weighted_sum(tmp_path):
    ev = _evidence(tmp_path)
    n = _good_narrative(ev)
    # 39.10*18 + 46.36*10 + 46*12 + 69*10 + 57*10 + 51*10
    # + 55.42*7 + 60*6 + 50.3*12 + 56.62*5 = 5124.04 -> 51.24
    assert compute_ai_regime_score(_adj(n)) == 51.24
    assert compute_ai_regime_score({"factor_scores": {"a": 1}, "weights": {"b": 2}}) is None


def test_weights_must_sum_to_100(tmp_path):
    ev = _evidence(tmp_path)
    n = _good_narrative(ev)
    _adj(n)["weights"]["equity_trend"] = 20.0  # 18 + 2 -> total 102
    fails = validate_narrative(n, ev)
    assert any("weights sum to 102.00" in f for f in fails)


def test_weight_deviation_beyond_10_points_rejected(tmp_path):
    ev = _evidence(tmp_path)
    n = _good_narrative(ev)
    # move 11 points from market_breadth to equity_trend: 18+11=29, 12-11=1
    _adj(n)["weights"]["equity_trend"] = 29.0
    _adj(n)["weights"]["market_breadth"] = 1.0
    fails = validate_narrative(n, ev)
    assert any("more than 10 points from source weight" in f for f in fails)


def test_factor_score_deviation_beyond_30_points_rejected(tmp_path):
    ev = _evidence(tmp_path)
    n = _good_narrative(ev)
    _adj(n)["factor_scores"]["equity_trend"] = 71.0  # source 40.0 -> +31
    fails = validate_narrative(n, ev)
    assert any("more than 30 points from source" in f for f in fails)


def test_computed_regime_score_beyond_25_points_rejected(tmp_path):
    ev = _evidence(tmp_path)
    n = _good_narrative(ev)
    # +29 on every factor keeps each factor legal but pushes the weighted result
    # far past the 25-point anchor.
    for name, src in ev["metrics"].items():
        if name.startswith("regime_factors."):
            _adj(n)["factor_scores"][name.split(".", 1)[1]] = min(100.0, float(src) + 29.0)
    _adj(n).pop("regime_score", None)
    fails = validate_narrative(n, ev)
    assert any("computed AI regime score" in f and "more than 25 points" in f for f in fails)


def test_claimed_regime_score_must_match_computation(tmp_path):
    ev = _evidence(tmp_path)
    n = _good_narrative(ev)
    _adj(n)["regime_score"] = 60.0  # computed is 51.24
    fails = validate_narrative(n, ev)
    assert any("the AI score must be computed" in f for f in fails)


def test_forward_signal_requires_all_three_horizons(tmp_path):
    ev = _evidence(tmp_path)
    n = _good_narrative(ev)
    n["sections"]["forward_signal"] = ["5D +0.69% and 20D +1.50% only."]
    fails = validate_narrative(n, ev)
    assert any("forward_signal must cite 60D" in f for f in fails)


def test_forward_signal_requires_percentages(tmp_path):
    ev = _evidence(tmp_path)
    n = _good_narrative(ev)
    n["sections"]["forward_signal"] = ["5D 0.69, 20D 1.50, 60D 4.70 in the 50-55 bucket."]
    fails = validate_narrative(n, ev)
    assert sum("forward_signal must give a percentage" in f for f in fails) == 3


def test_sector_rationale_is_optional_but_validated(tmp_path):
    ev = _evidence(tmp_path)
    n = _good_narrative(ev)
    _adj(n)["sector_rationale"] = {"No Such Sector": "x"}
    fails = validate_narrative(n, ev)
    assert any("unknown sector 'No Such Sector'" in f for f in fails)


def test_duplicate_sector_rationale_rejected(tmp_path):
    ev = _evidence(tmp_path)
    n = _good_narrative(ev)
    _adj(n)["sector_rationale"] = {"Health Care": "A" * 50}
    # duplicate under a second known sector
    n["sections"]["sector_narrative"] = ["x"]
    # add a second sector to the evidence via a fresh pack
    d = {"regime": {"score": 44.67}, "sectors": [
        {"name": "Health Care", "score": 83.89},
        {"name": "Energy", "score": 72.38},
    ]}
    src = tmp_path / "latest-report.md"
    src.write_text(SOURCE, encoding="utf-8")
    ev2 = build_evidence_pack(d, src)
    _adj(n)["sector_rationale"] = {"Health Care": "A" * 50, "Energy": "A" * 50}
    _adj(n)["sector_scores"] = {"Health Care": 80.0, "Energy": 70.0}
    fails = validate_narrative(n, ev2)
    assert any("duplicates" in f for f in fails)


def test_short_sector_rationale_rejected(tmp_path):
    ev = _evidence(tmp_path)
    n = _good_narrative(ev)
    _adj(n)["sector_rationale"] = {"Health Care": "Too short."}
    fails = validate_narrative(n, ev)
    assert any("40-300 chars" in f for f in fails)


def test_uniform_sector_offset_rejected(tmp_path):
    ev = _evidence(tmp_path)
    n = _good_narrative(ev)
    d = {"regime": {"score": 44.67}, "sectors": [
        {"name": "Health Care", "score": 83.89},
        {"name": "Energy", "score": 72.38},
        {"name": "Utilities", "score": 76.34},
    ]}
    src = tmp_path / "latest-report.md"
    src.write_text(SOURCE, encoding="utf-8")
    ev2 = build_evidence_pack(d, src)
    _adj(n)["sector_scores"] = {"Health Care": 81.89, "Energy": 70.38, "Utilities": 74.34}
    _adj(n)["sector_rationale"] = {
        "Health Care": "Defensive cash flows hold up but reimbursement risk caps upside." * 1,
        "Energy": "Oil below 100 and HY divergence argue for a smaller overweight than source." * 1,
        "Utilities": "Rate sensitivity offsets defensive appeal; trim versus the source score." * 1,
    }
    fails = validate_narrative(n, ev2)
    assert any("uniform" in f for f in fails)


# --- AEGIS research sections: stock ideas, macro outlook, portfolio risk ------

def test_stock_idea_arithmetic_mismatch_rejected(tmp_path):
    ev = _evidence(tmp_path)
    n = _good_narrative(ev)
    n["sections"]["stock_ideas"][0]["upside_pct"] += 5.0
    fails = validate_narrative(n, ev)
    assert any("upside_pct" in f for f in fails)


def test_stock_ideas_require_a_bearish_idea(tmp_path):
    ev = _evidence(tmp_path)
    n = _good_narrative(ev)
    for idea in n["sections"]["stock_ideas"]:
        if idea["recommendation"] in ("Sell", "Reduce", "Hold"):
            idea["recommendation"] = "Buy"
    fails = validate_narrative(n, ev)
    assert any("at least one Sell, Reduce or Hold" in f for f in fails)


def test_stock_idea_sources_must_be_in_global_sources(tmp_path):
    ev = _evidence(tmp_path)
    n = _good_narrative(ev)
    n["sections"]["stock_ideas"][0]["sources"] = ["https://example.com/not-cited"]
    fails = validate_narrative(n, ev)
    assert any("not in the global sources list" in f for f in fails)


def test_stock_ideas_require_three_to_five(tmp_path):
    ev = _evidence(tmp_path)
    n = _good_narrative(ev)
    n["sections"]["stock_ideas"] = n["sections"]["stock_ideas"][:2]
    fails = validate_narrative(n, ev)
    assert any("3-5 ideas" in f for f in fails)


def test_macro_outlook_and_portfolio_risk_are_required(tmp_path):
    ev = _evidence(tmp_path)
    n = _good_narrative(ev)
    n["sections"]["macro_outlook"] = []
    n["sections"]["portfolio_risk"] = []
    fails = validate_narrative(n, ev)
    assert any("macro_outlook" in f for f in fails)
    assert any("portfolio_risk" in f for f in fails)


def test_stock_ideas_need_at_least_three_individual_stocks(tmp_path):
    ev = _evidence(tmp_path)
    n = _good_narrative(ev)
    for idea in n["sections"]["stock_ideas"][:2]:
        idea["security_type"] = "ETF"
    fails = validate_narrative(n, ev)
    assert any("at least 3 individual stocks" in f for f in fails)


def test_candidate_screen_selected_must_match_ideas(tmp_path):
    ev = _evidence(tmp_path)
    n = _good_narrative(ev)
    n["sections"]["candidate_screen"][0]["ticker"] = "ZZZ"
    fails = validate_narrative(n, ev)
    assert any("do not match stock_ideas tickers" in f for f in fails)


def test_candidate_screen_requires_eight_to_fifteen(tmp_path):
    ev = _evidence(tmp_path)
    n = _good_narrative(ev)
    n["sections"]["candidate_screen"] = n["sections"]["candidate_screen"][:5]
    fails = validate_narrative(n, ev)
    assert any("8-15 candidates" in f for f in fails)


def test_stale_price_date_rejected(tmp_path):
    ev = _evidence(tmp_path)
    n = _good_narrative(ev)
    n["sections"]["stock_ideas"][0]["price_date"] = "2020-01-01"
    fails = validate_narrative(n, ev)
    assert any("price_date is stale" in f for f in fails)


def test_return_from_current_mismatch_rejected(tmp_path):
    ev = _evidence(tmp_path)
    n = _good_narrative(ev)
    n["sections"]["stock_ideas"][0]["return_from_current_pct"] += 5.0
    fails = validate_narrative(n, ev)
    assert any("return_from_current_pct" in f for f in fails)


def test_idea_needs_company_specific_source(tmp_path):
    ev = _evidence(tmp_path)
    n = _good_narrative(ev)
    # swap in a global source whose note does not name the ticker
    n["sections"]["stock_ideas"][0]["sources"] = [SOURCES[0]["url"]]
    fails = validate_narrative(n, ev)
    assert any("dated, company-specific filing/results source" in f for f in fails)


def test_reassess_and_verification_enums(tmp_path):
    ev = _evidence(tmp_path)
    n = _good_narrative(ev)
    n["sections"]["stock_ideas"][0]["reassess"] = "MAYBE"
    n["sections"]["stock_ideas"][1]["verification"] = "Probably"
    fails = validate_narrative(n, ev)
    assert any("reassess must be one of" in f for f in fails)
    assert any("verification must be one of" in f for f in fails)


def test_idea_requires_explicit_valuation_basis(tmp_path):
    ev = _evidence(tmp_path)
    n = _good_narrative(ev)
    n["sections"]["stock_ideas"][0]["assumptions"] = "The stock looks cheap."
    fails = validate_narrative(n, ev)
    assert any("explicit valuation basis" in f for f in fails)


def test_recycled_idea_cannot_be_marked_new(tmp_path):
    ev = _evidence(tmp_path)
    ev["previous_ideas"] = ["AAA"]
    n = _good_narrative(ev)
    fails = validate_narrative(n, ev)
    assert any("was in the previous report" in f for f in fails)


def test_new_idea_must_be_marked_new(tmp_path):
    ev = _evidence(tmp_path)
    ev["previous_ideas"] = ["AAA"]
    n = _good_narrative(ev)
    n["sections"]["stock_ideas"][1]["reassess"] = "KEEP"  # BBB is not in previous ideas
    fails = validate_narrative(n, ev)
    assert any("is new; reassess must be NEW" in f for f in fails)


def test_price_audit_rejects_stale_and_invented_prices():
    from idea_price_audit import audit_ideas
    idea = {"ticker": "XOM", "current_price": 120.0, "price_date": "2026-11-02",
            "entry_price": 120.0}
    lookup = lambda t: {"close": 100.0, "date": "2026-10-30"}
    fails = audit_ideas([idea], lookup=lookup)
    assert any("current_price" in f and "verified close" in f for f in fails)
    assert any("price_date" in f and "verified close date" in f for f in fails)


def test_price_audit_accepts_verified_close():
    from idea_price_audit import audit_ideas
    idea = {"ticker": "XOM", "current_price": 101.0, "price_date": "2026-10-30",
            "entry_price": 100.0}
    lookup = lambda t: {"close": 100.0, "date": "2026-10-30"}
    assert audit_ideas([idea], lookup=lookup) == []


def test_price_audit_fails_closed_when_api_unavailable():
    from idea_price_audit import audit_ideas
    idea = {"ticker": "XOM", "current_price": 100.0, "price_date": "2026-10-30",
            "entry_price": 100.0}
    fails = audit_ideas([idea], lookup=lambda t: None)
    assert any("no verified latest price" in f for f in fails)


def test_api_spec_is_not_a_fundamental_source(tmp_path):
    ev = _evidence(tmp_path)
    n = _good_narrative(ev)
    api = "https://api.138.2.69.165.sslip.io/openapi.json"
    n["sources"].append({"label": "API", "url": api, "note": "AAA Inc quote"})
    n["sections"]["stock_ideas"][0]["sources"] = [api]
    fails = validate_narrative(n, ev)
    assert any("dated, company-specific filing/results source" in f for f in fails)


def test_generic_ir_homepage_rejected(tmp_path):
    ev = _evidence(tmp_path)
    n = _good_narrative(ev)
    url = "https://investor.example.com/"
    n["sources"].append({"label": "IR", "url": url, "note": "AAA Inc investor relations 2026"})
    n["sections"]["stock_ideas"][0]["sources"] = [url]
    fails = validate_narrative(n, ev)
    assert any("dated, company-specific filing/results source" in f for f in fails)


def test_at_least_two_selected_ideas_must_be_new(tmp_path):
    ev = _evidence(tmp_path)
    ev["previous_ideas"] = ["AAA", "BBB", "CCC", "DDD"]
    n = _good_narrative(ev)
    for idea in n["sections"]["stock_ideas"]:
        idea["reassess"] = "KEEP"
    fails = validate_narrative(n, ev)
    assert any("at least 2 selected ideas must be new" in f for f in fails)


def test_valuation_target_must_equal_eps_times_pe(tmp_path):
    ev = _evidence(tmp_path)
    n = _good_narrative(ev)
    n["sections"]["stock_ideas"][0]["base_pe"] = 12.0  # 6.0 x 12 = 72 != 110
    fails = validate_narrative(n, ev)
    assert any("EPS x" in f and "!= target" in f for f in fails)


def test_ttm_pe_must_match_price_over_eps(tmp_path):
    ev = _evidence(tmp_path)
    n = _good_narrative(ev)
    n["sections"]["stock_ideas"][0]["ttm_pe"] = 35.0
    fails = validate_narrative(n, ev)
    assert any("ttm_pe" in f and "current_price/TTM EPS" in f for f in fails)


def test_forward_pe_must_match_price_over_eps(tmp_path):
    ev = _evidence(tmp_path)
    n = _good_narrative(ev)
    n["sections"]["stock_ideas"][0]["fwd_pe_2027"] = 30.0
    fails = validate_narrative(n, ev)
    assert any("fwd_pe_2027" in f and "current_price/FY2027 EPS" in f for f in fails)


def test_eps_growth_must_match_fy26_fy28(tmp_path):
    ev = _evidence(tmp_path)
    n = _good_narrative(ev)
    n["sections"]["stock_ideas"][0]["eps_growth_2026_2028_pct"] = 99.0
    fails = validate_narrative(n, ev)
    assert any("eps_growth_2026_2028_pct" in f for f in fails)


def test_pe_range_must_be_ordered(tmp_path):
    ev = _evidence(tmp_path)
    n = _good_narrative(ev)
    n["sections"]["stock_ideas"][0]["pe_3y_min"] = 30.0  # > median 18
    fails = validate_narrative(n, ev)
    assert any("pe_3y range" in f for f in fails)


def test_nonpositive_ttm_eps_requires_nm(tmp_path):
    ev = _evidence(tmp_path)
    n = _good_narrative(ev)
    n["sections"]["stock_ideas"][0]["ttm_eps_diluted"] = -1.0
    n["sections"]["stock_ideas"][0]["ttm_pe"] = 20.0
    fails = validate_narrative(n, ev)
    assert any("nonpositive TTM EPS" in f for f in fails)


def test_ttm_eps_must_equal_four_quarters(tmp_path):
    ev = _evidence(tmp_path)
    n = _good_narrative(ev)
    n["sections"]["stock_ideas"][0]["ttm_eps_diluted"] = 18.45
    n["sections"]["stock_ideas"][0]["ttm_eps_quarters"] = [17.0, 18.0, 18.45, 19.0]
    fails = validate_narrative(n, ev)
    assert any("sum(ttm_eps_quarters)" in f for f in fails)


def test_single_quarter_period_rejected(tmp_path):
    ev = _evidence(tmp_path)
    n = _good_narrative(ev)
    n["sections"]["stock_ideas"][0]["ttm_period"] = "Q3 2026"
    fails = validate_narrative(n, ev)
    assert any("not a single quarter" in f for f in fails)


def test_split_adjusted_false_rejected(tmp_path):
    ev = _evidence(tmp_path)
    n = _good_narrative(ev)
    n["sections"]["stock_ideas"][0]["split_adjusted"] = False
    fails = validate_narrative(n, ev)
    assert any("split_adjusted must be true" in f for f in fails)


def test_fy_eps_must_equal_h1_plus_h2(tmp_path):
    ev = _evidence(tmp_path)
    n = _good_narrative(ev)
    n["sections"]["stock_ideas"][0]["h1_eps_reported"] = 4.85
    n["sections"]["stock_ideas"][0]["h2_eps_forecast"] = 0.20
    fails = validate_narrative(n, ev)
    assert any("H1 reported" in f and "H2 forecast" in f for f in fails)


def test_verified_requires_verified_provenance(tmp_path):
    ev = _evidence(tmp_path)
    n = _good_narrative(ev)
    n["sections"]["stock_ideas"][0]["verification"] = "Verified"
    n["sections"]["stock_ideas"][0]["valuation_provenance"]["ttm_eps_diluted"] = "AI_FORECAST"
    fails = validate_narrative(n, ev)
    assert any("verification=Verified but provenance" in f for f in fails)


def test_ttm_eps_source_required(tmp_path):
    ev = _evidence(tmp_path)
    n = _good_narrative(ev)
    n["sections"]["stock_ideas"][0]["ttm_eps_source"] = "N/A"
    fails = validate_narrative(n, ev)
    assert any("ttm_eps_source" in f for f in fails)


def test_h2_collapse_requires_rationale(tmp_path):
    ev = _evidence(tmp_path)
    n = _good_narrative(ev)
    idea = n["sections"]["stock_ideas"][0]
    idea["h1_eps_reported"] = 4.85
    idea["h2_eps_forecast"] = 0.65
    idea["fy2027_eps_consensus"] = 5.50
    idea["h2_rationale"] = ""
    fails = validate_narrative(n, ev)
    assert any("h2_rationale" in f for f in fails)


def _facts_regn():
    q = [
        ("2025-01-01", "2025-03-31", 7.27), ("2025-04-01", "2025-06-30", 12.81),
        ("2025-07-01", "2025-09-30", 13.62), ("2026-01-01", "2026-03-31", 6.75),
        ("2026-04-01", "2026-06-30", 12.23), ("2026-07-01", "2026-09-30", 18.45),
    ]
    return {"quarters": [{"start": s, "end": e, "val": v} for s, e, v in q],
            "annual": [{"start": "2025-01-01", "end": "2025-12-31", "val": 41.48}]}


def test_sec_ttm_mismatch_blocks():
    from fundamental_audit import audit_fundamentals
    idea = {"ticker": "REGN", "sec_cik": "0000872589", "ttm_eps_diluted": 38.0}
    fails = audit_fundamentals([idea], lookup=lambda c: _facts_regn())
    assert any("TTM EPS" in f and "SEC XBRL" in f for f in fails)


def test_sec_ttm_match_passes():
    from fundamental_audit import audit_fundamentals
    idea = {"ticker": "REGN", "sec_cik": "0000872589", "ttm_eps_diluted": 45.21}
    assert audit_fundamentals([idea], lookup=lambda c: _facts_regn()) == []


def test_sec_h1_mismatch_blocks():
    from fundamental_audit import audit_fundamentals
    facts = {"quarters": [
        {"start": "2026-01-26", "end": "2026-04-26", "val": 2.39},
        {"start": "2026-04-27", "end": "2026-07-26", "val": 2.46},
    ], "annual": []}
    idea = {"ticker": "NVDA", "sec_cik": "0001045810", "h1_eps_reported": 2.1}
    fails = audit_fundamentals([idea], lookup=lambda c: facts)
    assert any("H1 EPS" in f and "SEC XBRL" in f for f in fails)


def test_sec_unavailable_blocks():
    from fundamental_audit import audit_fundamentals
    idea = {"ticker": "X", "sec_cik": "0000000001", "ttm_eps_diluted": 1.0}
    fails = audit_fundamentals([idea], lookup=lambda c: None)
    assert any("SEC XBRL unavailable" in f for f in fails)


def test_nm_ttm_with_four_quarters_rejected(tmp_path):
    ev = _evidence(tmp_path)
    n = _good_narrative(ev)
    idea = n["sections"]["stock_ideas"][0]
    idea["ttm_eps_diluted"] = "N/M"
    idea["ttm_pe"] = "N/M"
    fails = validate_narrative(n, ev)
    assert any("must be numeric when four quarters are provided" in f for f in fails)


def test_sec_ttm_nm_is_blocked():
    from fundamental_audit import audit_fundamentals
    idea = {"ticker": "REGN", "sec_cik": "0000872589", "ttm_eps_diluted": "N/M"}
    fails = audit_fundamentals([idea], lookup=lambda c: _facts_regn())
    assert any("N/M is not accepted" in f for f in fails)


def test_pe_history_must_match_cmc():
    from fundamentals_web import audit_pe_history
    stats = {"median": 29.6, "min": 21.6, "max": 39.5, "percentile": 80.0}
    idea = {"ticker": "AAPL", "pe_5y_median": 22.0, "pe_5y_min": 21.6,
            "pe_5y_max": 39.5, "pe_5y_percentile": 80.0,
            "pe_history_source": "https://companiesmarketcap.com/apple/pe-ratio/"}
    fails = audit_pe_history([idea], lookup=lambda t: stats)
    assert any("CMC median" in f for f in fails)


def test_pe_history_source_must_be_cmc():
    from fundamentals_web import audit_pe_history
    stats = {"median": 29.6, "min": 21.6, "max": 39.5, "percentile": 80.0}
    idea = {"ticker": "AAPL", "pe_5y_median": 29.6, "pe_history_source": "https://example.com"}
    fails = audit_pe_history([idea], lookup=lambda t: stats)
    assert any("companiesmarketcap.com" in f for f in fails)


def test_consensus_label_requires_source(tmp_path):
    ev = _evidence(tmp_path)
    n = _good_narrative(ev)
    idea = n["sections"]["stock_ideas"][0]
    idea["valuation_provenance"]["fy2027_eps_consensus"] = "CONSENSUS"
    idea["consensus_source"] = "N/A"
    fails = validate_narrative(n, ev)
    assert any("labelled CONSENSUS" in f for f in fails)

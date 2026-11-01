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
        "regime_factors": {"equity_trend": 40.0},
        "sectors": [{"name": "Health Care", "score": 83.89, "breadth_50": 75.0, "positive_20d": 91.67}],
        "themes": [{"name": "Energy", "score": 70.94}],
        "data_cutoff": "1 November 2026",
        "data_cutoff_time": "10:16:00",
        "run_id": "run-1-November-2026-1016",
    }
    return build_evidence_pack(d, src)


ALL_SECTIONS = [
    "exec_summary", "cio_dashboard", "what_matters", "risk_opportunity", "historical_analogs",
    "scorecard", "scenarios_narrative", "macro_narrative", "cross_asset_narrative", "equities_view",
    "price_action", "flows_narrative", "portfolio_posture", "sector_narrative", "themes_narrative",
    "style_rotation", "factor_style", "trades_narrative", "heat_st_narrative", "heat_lt_narrative",
    "catalysts_narrative", "risk_narrative", "conclusions",
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
    sections["exec_summary"] = ["Regime reads 44.67/100 with a CIO composite of 48.62/100."]
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
            "regime_score": 50.0,
            "regime_label": "Neutral / Two-Sided",
            "rationale": "Model research indicates stable credit spreads and a calmer vol surface warrant a less defensive regime read than the mechanical 44.67.",
            "sector_scores": {"Health Care": 80.0},
        },
        "sources": [dict(s) for s in SOURCES],
        "claims": [
            {"path": "regime.score", "value": 44.67},
            {"path": "cio.score", "value": 48.62},
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

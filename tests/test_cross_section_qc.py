"""Cross-section contradiction checks (no network)."""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "scripts"))

import cross_section_qc

CARD = '<div class="idea-card"><h3>MSFT &mdash; Microsoft <span>Stock &middot; Reduce</span></h3></div>'


def test_regime_number_must_match_canonical():
    html = CARD + '<p>AI regime score: 41.71 / 100</p><p>AI score 39.4 vs source 39.58</p>'
    fails = cross_section_qc.check(html, {}, ai_score=41.71)
    assert any("39.4" in f for f in fails)


def test_ticker_action_contradiction():
    html = CARD + "<p>Buy NVDA, COP, MSFT on pullback.</p>"
    fails = cross_section_qc.check(html, {}, ai_score=None)
    assert any("MSFT" in f and "Reduce" in f for f in fails)


def test_heatmap_must_match_allocation():
    html = CARD + '<h2 id="heat-st">Heat</h2><table><tr><td>Information Technology</td><td class="neg">-4.0%</td></tr></table>'
    narrative = {"sections": {"sector_allocation": [
        {"horizon": "ST", "sector": "Information Technology", "active_weight": -5.0}]}}
    fails = cross_section_qc.check(html, narrative, ai_score=None)
    assert any("heat map" in f for f in fails)


def test_wrong_calendar_date():
    html = CARD + "<p>December FOMC is Dec 10.</p>"
    fails = cross_section_qc.check(html, {}, ai_score=None)
    assert any("Dec 8-9" in f for f in fails)


def test_ai_disclosure_must_match_canonical():
    html = '<p>Source rule-based: 40.12 | AI: 38.10</p>'
    fails = cross_section_qc.check(html, {}, ai_score=42.96)
    assert any("AI: 38.10" in f for f in fails)


def test_wti_range_must_contain_snapshot():
    html = "<p>WTI 90.34</p><p>WTI likely trades $75-80.</p>"
    fails = cross_section_qc.check(html, {}, ai_score=None)
    assert any("WTI" in f and "90.34" in f for f in fails)


def test_nasdaq_identifiers_must_not_mix():
    html = "<p>Nasdaq Composite 24579</p><p>Nasdaq 100 20000</p>"
    fails = cross_section_qc.check(html, {}, ai_score=None)
    assert any("Nasdaq" in f for f in fails)


def test_energy_overweight_needs_valuation_reason():
    html = "<p>Energy</p>"
    narrative = {
        "adjustments": {"sector_scores": {"Energy": 22.0}},
        "sections": {"sector_allocation": [
            {"horizon": "ST", "sector": "Energy", "active_weight": 2.0,
             "rationale": "Sector score 22.0; active weight +2 pp."}]},
    }
    fails = cross_section_qc.check(html, narrative, ai_score=None)
    assert any("Energy active +2.0pp" in f for f in fails)


def test_bare_nasdaq_is_ambiguous():
    fails = cross_section_qc.check("<p>Nasdaq 24579.42</p>", {}, ai_score=None)
    assert any("bare 'Nasdaq'" in f for f in fails)


def test_labeled_nasdaq_composite_passes():
    fails = cross_section_qc.check("<p>Nasdaq Composite 24579.42</p>", {}, ai_score=None)
    assert not any("Nasdaq" in f for f in fails)


def test_iso_cpi_date_must_be_nov_10():
    fails = cross_section_qc.check("<p>BLS releases 2026-11-12 CPI.</p>", {}, ai_score=None)
    assert any("2026-11-12" in f for f in fails)


def test_iso_fomc_date_must_be_dec_8_or_9():
    fails = cross_section_qc.check("<p>FOMC policy 2026-11-05, 2026-12-16.</p>", {}, ai_score=None)
    assert any("2026-12-16" in f for f in fails)

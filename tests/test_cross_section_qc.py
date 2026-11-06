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

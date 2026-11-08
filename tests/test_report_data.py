"""Canonical report-data object tests."""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "scripts"))

import report_data


def _fixtures():
    d = {
        "run_id": "run-test-0001",
        "regime": {"score": 40.0, "label": "Neutral"},
        "regime_factors": {"equity_trend": 50.0},
        "regime_weights": {"equity_trend": 100.0},
        "sectors": [{"name": "Energy", "score": 20.0}],
    }
    adj = {
        "factor_scores": {"equity_trend": 60.0},
        "weights": {"equity_trend": 100.0},
        "sector_scores": {"Energy": 40.0},
        "regime_score": 60.0,
    }
    row = {
        "ticker": "X", "recommendation": "Buy", "current_price": 100.0,
        "ttm_eps_diluted": 5.0, "fy2026_eps_consensus": 5.0,
        "fy2027_eps_consensus": 5.5, "fy2028_eps_consensus": 6.0,
        "entry_price": 100.0, "bull_eps": 6.5, "bull_pe": 20.0,
        "base_eps": 6.0, "base_pe": 18.0, "bear_eps": 5.0, "bear_pe": 15.0,
        "bull_prob": 0.25, "base_prob": 0.50, "bear_prob": 0.25,
    }
    nv = {"source": {"latest_report_sha256": "abc"},
          "sections": {"stock_ideas": [row],
                       "sector_allocation": [{"horizon": "ST", "sector": "Energy",
                                              "benchmark_weight": 4, "portfolio_weight": 4,
                                              "active_weight": 0}]}}
    return d, nv, adj


def test_build_is_versioned_and_consistent():
    d, nv, adj = _fixtures()
    data = report_data.build(d, nv, adj)
    assert data.ai_score == 60.0
    assert data.source_score == 40.0
    assert len(data.version) == 16
    assert data.run_id == "run-test-0001"
    assert data.source_sha == "abc"


def test_normalize_narrative_uses_canonical_valuation():
    d, nv, adj = _fixtures()
    data = report_data.build(d, nv, adj)
    out = report_data.normalize_narrative(nv, data)
    assert out["sections"]["stock_ideas"][0]["ttm_pe"] == 20.0


def test_version_is_stable_for_same_inputs():
    d, nv, adj = _fixtures()
    assert report_data.build(d, nv, adj).version == report_data.build(d, nv, adj).version


def test_strict_pe_fields():
    d, nv, adj = _fixtures()
    data = report_data.build(d, nv, adj)
    pe = data.ideas[0]["pe"]
    assert pe["ttm_gaap_pe"] == 20.0
    assert pe["forward_gaap_pe_2027"] == round(100.0 / 5.5, 4)
    assert pe["ttm_adjusted_pe"] == "N/A"


def test_markdown_mirrors_json(tmp_path):
    d, nv, adj = _fixtures()
    data = report_data.build(d, nv, adj)
    out = tmp_path / "report-data.md"
    report_data.write_markdown(str(out), data)
    text = out.read_text()
    assert "TTM GAAP P/E" in text
    assert "| X | Buy |" in text

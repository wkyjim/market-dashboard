"""One regression test per mandatory QC item (1-12)."""
import pathlib
import sys
import tempfile
from pathlib import Path

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT / "tests"))

from financial_calc import attribution, qc_probabilities, qc_target, ttm_eps
from official_calendar import verify
from report_narrative import validate_narrative
from test_report_narrative import _evidence, _good_narrative


def _narrative():
    return _good_narrative(_evidence(Path(tempfile.mkdtemp())))


def test_qc01_eps_periods_and_basis():
    assert ttm_eps([1, 1, 1, 1]) == 4
    assert ttm_eps([1, 1, 1]) is None
    n = _narrative()
    n["sections"]["stock_ideas"][0]["pe_history_basis"] = "non-GAAP"
    assert any("pe_history_basis" in f for f in validate_narrative(n, _evidence(Path(tempfile.mkdtemp()))))


def test_qc02_pe_and_target_math():
    assert "target" in qc_target(6.50, 30, 560)
    assert "target" in qc_target(4.50, 35, 185)
    assert qc_target(5.0, 20, 100) is None


def test_qc03_consensus_vs_ai_label():
    from fundamentals_web import audit_consensus
    idea = {"ticker": "AAPL", "fy2027_eps_consensus": 8.0,
            "consensus_source": "N/A",
            "valuation_provenance": {"fy2027_eps_consensus": "CONSENSUS"}}
    fails = audit_consensus([idea], lookup=lambda t: {"eps_current_year": 9.31, "eps_next_year": 10.0})
    assert any("Yahoo" in f or "consensus_source" in f for f in fails)


def test_qc04_price_entry_target_exit_are_separate():
    idea = _narrative()["sections"]["stock_ideas"][0]
    values = {idea["current_price"], idea["entry_price"], idea["base_target"], idea["realized_exit"] if "realized_exit" in idea else idea["exit"]}
    assert len(values) >= 3


def test_qc05_action_matches_valuation():
    n = _narrative()
    idea = n["sections"]["stock_ideas"][0]
    idea["base_target"] = 95.0
    idea["base_eps"] = 9.5
    fails = validate_narrative(n, _evidence(Path(tempfile.mkdtemp())))
    assert any("must exceed current" in f for f in fails)


def test_qc06_scenario_probabilities():
    assert qc_probabilities([0.25, 0.5, 0.25]) is None
    assert "sum to 100" in qc_probabilities([0.2, 0.3, 0.4])


def test_qc07_eleven_unique_sectors():
    n = _narrative()
    assert len(n["sections"]["sector_allocation"]) == 22
    assert len([r for r in n["sections"]["sector_allocation"] if r["horizon"] == "ST"]) == 11
    n["sections"]["sector_allocation"][0]["sector"] = n["sections"]["sector_allocation"][1]["sector"]
    fails = validate_narrative(n, _evidence(Path(tempfile.mkdtemp())))
    assert any("11 unique GICS" in f for f in fails)


def test_qc08_portfolio_weights_and_active_sum():
    n = _narrative()
    n["sections"]["sector_allocation"][0]["portfolio_weight"] += 5
    fails = validate_narrative(n, _evidence(Path(tempfile.mkdtemp())))
    assert any("portfolio weights must sum to 100" in f for f in fails)


def test_qc09_timestamp_and_units():
    from idea_price_audit import audit_ideas
    idea = {"ticker": "AAPL", "current_price": 100, "price_date": "", "entry_price": 100}
    fails = audit_ideas([idea], lookup=lambda t: {"close": 100, "date": "2026-11-04"})
    assert any("missing or invalid" in f for f in fails)


def test_qc10_official_calendar_dates():
    assert verify("FOMC", "2026-12-08") and verify("FOMC", "2026-12-09")
    assert not verify("FOMC", "2026-12-10")
    assert verify("CPI", "2026-11-10")


def test_qc11_material_claims_have_sources():
    n = _narrative()
    n["sections"]["stock_ideas"][0]["sources"] = []
    fails = validate_narrative(n, _evidence(Path(tempfile.mkdtemp())))
    assert any("sources" in f for f in fails)


def test_qc12_ai_score_reconciles():
    py_scores = {"a": 50, "b": 60}
    py_w = {"a": 0.5, "b": 0.5}
    ai_scores = {"a": 55, "b": 65}
    ai_w = {"a": 0.6, "b": 0.4}
    out = attribution(py_scores, py_w, ai_scores, ai_w)
    assert abs(out["residual"]) < 1e-12
    assert out["ai_final"] - out["python_baseline"] == out["explained"] or abs(
        (out["ai_final"] - out["python_baseline"]) - out["explained"]) < 1e-12

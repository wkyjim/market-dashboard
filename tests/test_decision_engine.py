"""Decision-engine math tests."""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "scripts"))

import decision_engine as de


def test_regime_score_is_weighted_average():
    assert de.regime_score({"a": 60, "b": 40}, {"a": 50, "b": 50}) == 50.0


def test_pe_handles_zero_and_missing():
    assert de.pe(100, 5) == 20.0
    assert de.pe(100, 0) == "N/M"
    assert de.pe(100, None) == "N/A"


def test_valuation_uses_base_year_eps():
    out = de.valuation(100, 5.0, 5.5, 6.0, 2028, 18.0)
    assert out["base_eps"] == 6.0
    assert out["base_target"] == 108.0
    assert out["forward_gaap_pe_2027"] == round(100 / 5.5, 4)


def test_allocation_must_sum_to_100_100_0():
    active, sums = de.allocation({"A": 60, "B": 40}, {"A": 55, "B": 45})
    assert active == {"A": 5.0, "B": -5.0}
    assert sums["active_sum"] == 0.0
    try:
        de.allocation({"A": 60, "B": 30}, {"A": 55, "B": 45})
    except ValueError as exc:
        assert "100/100/0" in str(exc)
    else:
        raise AssertionError("expected ValueError")

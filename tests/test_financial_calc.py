"""Unit tests for the deterministic financial calculation engine."""
import math
import pathlib
import sys

import pytest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "scripts"))

from financial_calc import (
    active_return, active_weight, attribution, beta, beta_neutral_short_weight,
    revenue_growth,
    correlation, covariance, diluted_eps, dv01_neutral_short_notional, enterprise_value,
    eps_growth, ev_to_ebitda, excess_return, expected_return, expected_shortfall,
    fcf_margin, fcf_yield, forward_pe, free_cash_flow, gross_exposure, hit, hit_rate,
    historical_var, information_ratio, max_drawdown, net_exposure, net_margin,
    operating_margin, pair_return, pair_volatility, pe_premium, peg, portfolio_beta,
    portfolio_return, portfolio_variance, portfolio_volatility, position_weight,
    price_to_book, price_to_sales, probability_weighted_return,
    probability_weighted_target, qc_probabilities, qc_sectors, qc_target, reward_risk,
    risk_based_notional, score_adjustment_effect, score_change_attribution,
    sector_return, sharpe, spearman_rho, target_price, tracking_error, ttm_eps, ttm_pe,
    weight_adjustment_effect, weighted_score,
)


def test_statement_formulas():
    assert revenue_growth(110, 100) == pytest.approx(0.10)
    assert operating_margin(25, 100) == pytest.approx(0.25)
    assert net_margin(10, 100) == pytest.approx(0.10)
    assert diluted_eps(10_000_000, 5_000_000) == pytest.approx(2.0)
    assert free_cash_flow(100, 40) == pytest.approx(60)
    assert fcf_margin(60, 100) == pytest.approx(0.60)


def test_eps_growth_only_for_positive_comparable():
    assert eps_growth(5, 4) == pytest.approx(0.25)
    assert eps_growth(5, -4) is None
    assert eps_growth(0, 4) is None
    assert eps_growth(None, 4) is None


def test_ttm_eps_requires_four_quarters():
    assert ttm_eps([1, 2, 3, 4]) == pytest.approx(10)
    assert ttm_eps([1, 2, 3]) is None
    assert ttm_eps([1, 2, 3, None]) is None


def test_pe_uses_nm_for_nonpositive_eps():
    assert ttm_pe(100, 5) == pytest.approx(20)
    assert ttm_pe(100, 0) == "N/M"
    assert ttm_pe(100, -2) == "N/M"
    assert forward_pe(100, 4) == pytest.approx(25)


def test_target_and_premium():
    assert target_price(5, 20) == pytest.approx(100)
    assert target_price(-1, 20) is None
    assert pe_premium(25, 20) == pytest.approx(0.25)
    assert peg(20, 10) == pytest.approx(2.0)
    assert peg(20, 0) is None


def test_ps_pb_ev_fcf_yield():
    assert price_to_sales(1000, 100) == pytest.approx(10)
    assert price_to_book(1000, 200) == pytest.approx(5)
    assert enterprise_value(1000, 200, 10, 5, 50) == pytest.approx(1165)
    assert ev_to_ebitda(1165, 100) == pytest.approx(11.65)
    assert fcf_yield(60, 1000) == pytest.approx(0.06)


def test_scenario_math():
    assert expected_return(110, 100) == pytest.approx(0.10)
    assert expected_return(110, 100, dividends=2) == pytest.approx(0.12)
    assert reward_risk(0.10, -0.10) == pytest.approx(1.0)
    assert probability_weighted_target([120, 100, 80], [0.25, 0.5, 0.25]) == pytest.approx(100)
    assert probability_weighted_return([0.2, 0.0, -0.2], [0.25, 0.5, 0.25]) == pytest.approx(0.0)


def test_attribution_identity_is_exact():
    py_scores = {"a": 50, "b": 60}
    py_w = {"a": 0.5, "b": 0.5}
    ai_scores = {"a": 55, "b": 65}
    ai_w = {"a": 0.6, "b": 0.4}
    out = attribution(py_scores, py_w, ai_scores, ai_w)
    assert out["python_baseline"] == pytest.approx(55)
    assert out["ai_final"] == pytest.approx(59)
    assert out["score_effect"] == pytest.approx(5)
    assert out["weight_effect"] == pytest.approx(-1)
    assert out["residual"] == pytest.approx(0, abs=1e-12)


def test_score_change_attribution_identity():
    prev_s = {"a": 50, "b": 60}
    prev_w = {"a": 0.5, "b": 0.5}
    cur_s = {"a": 60, "b": 50}
    cur_w = {"a": 0.5, "b": 0.5}
    out = score_change_attribution(prev_s, prev_w, cur_s, cur_w)
    assert out["total_change"] == pytest.approx(0)
    assert out["factor_effect"] == pytest.approx(0)
    assert out["weight_effect"] == pytest.approx(0)
    assert out["residual"] == pytest.approx(0, abs=1e-12)


def test_spearman_and_hit_rate():
    assert spearman_rho([1, 2, 3, 4], [-0.02, -0.01, 0.01, 0.02]) == pytest.approx(1.0)
    assert spearman_rho([1, 2, 3, 4], [0.02, 0.01, -0.01, -0.02]) == pytest.approx(-1.0)
    assert hit_rate([("OW", 0.01), ("UW", -0.02), ("OW", -0.01)]) == pytest.approx(2 / 3)
    assert hit("OW", 0.0) is False


def test_sector_and_active_return():
    assert sector_return(110, 100) == pytest.approx(0.10)
    assert excess_return(0.10, 0.08) == pytest.approx(0.02)
    assert active_weight(0.30, 0.25) == pytest.approx(0.05)
    assert active_return([0.02, -0.01], [0.05, 0.02], costs=0.001) == pytest.approx(-0.0002)


def test_portfolio_risk():
    cov = [[0.04, 0.01], [0.01, 0.09]]
    assert portfolio_variance([0.5, 0.5], cov) == pytest.approx(0.0375)
    assert portfolio_volatility([0.5, 0.5], cov) == pytest.approx(0.193649, rel=1e-4)
    assert beta([0.01, 0.02, 0.03], [0.005, 0.01, 0.015]) == pytest.approx(2.0)
    assert correlation([0.01, 0.02, 0.03], [0.005, 0.01, 0.015]) == pytest.approx(1.0)
    assert covar_is_close(covariance([0.01, 0.02, 0.03], [0.005, 0.01, 0.015]), 0.00005)


def covar_is_close(value, expected):
    return value == pytest.approx(expected, rel=1e-6)


def test_tracking_error_information_ratio_sharpe():
    assert tracking_error([0.01, 0.02, 0.03], [0.005, 0.01, 0.015]) == pytest.approx(0.07937, rel=1e-3)
    assert information_ratio(0.03, 0.02) == pytest.approx(1.5)
    assert sharpe(0.08, 0.16) == pytest.approx(0.5)


def test_drawdown_var_es():
    assert max_drawdown([100, 120, 90, 110]) == pytest.approx(-0.25)
    pnl = [-0.05, -0.02, 0.0, 0.01, 0.03]
    assert historical_var(pnl) == pytest.approx(0.043, abs=0.002)
    assert expected_shortfall(pnl) == pytest.approx(0.05)


def test_position_sizing_and_exposure():
    assert risk_based_notional(1_000_000, 0.01, 0.05) == pytest.approx(200_000)
    assert position_weight(200_000, 1_000_000) == pytest.approx(0.2)
    assert gross_exposure([100, -50], 1000) == pytest.approx(0.15)
    assert net_exposure([100, -50], 1000) == pytest.approx(0.05)


def test_pair_trades():
    assert pair_return(0.10, -0.05, costs=0.002) == pytest.approx(0.148)
    assert beta_neutral_short_weight(1.0, 1.2, 0.8) == pytest.approx(1.5)
    assert dv01_neutral_short_notional(1_000_000, 100, 80) == pytest.approx(1_250_000)
    assert pair_volatility(1, 1, 0.04, 0.09, 0.01) == pytest.approx(math.sqrt(0.11))


def test_known_failures_block():
    # AMD $6.50 x 30x != $560; NVDA $4.50 x 35x != $185.
    assert "target" in qc_target(6.50, 30, 560)
    assert "target" in qc_target(4.50, 35, 185)
    assert qc_target(5.0, 20, 100) is None
    assert qc_probabilities([0.25, 0.5, 0.25]) is None
    assert "sum to 100" in qc_probabilities([0.2, 0.3, 0.4])
    assert qc_sectors(["A"] * 11) is not None
    assert qc_sectors([str(i) for i in range(11)]) is None


def test_regn_ttm_and_wmt_split():
    # REGN Q4'25 7.78 + Q1 6.75 + Q2 12.23 + Q3 18.45 = 45.21
    assert ttm_eps([7.78, 6.75, 12.23, 18.45]) == pytest.approx(45.21)
    # A single quarter (18.45) or a stale 38.0 must not be accepted as TTM.
    assert ttm_eps([18.45, 18.45, 18.45, 18.45]) != pytest.approx(45.21)
    # WMT split-adjusted TTM 2.76; the pre-split 6.80 is not comparable.
    assert ttm_eps([0.66, 0.68, 0.70, 0.72]) == pytest.approx(2.76)

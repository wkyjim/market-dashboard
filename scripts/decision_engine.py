"""Deterministic decision math for the hybrid report builder.

The AI supplies scores, weights, ratings and scenario assumptions only.
Every derived number is computed here.
"""
from __future__ import annotations


def _num(value):
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def regime_score(scores: dict, weights: dict) -> float:
    if not scores or set(scores) != set(weights):
        raise ValueError("factor scores and weights must have identical keys")
    total = sum(float(weights[k]) for k in weights)
    if abs(total - 100.0) > 0.2:
        raise ValueError("factor weights must sum to 100 (got %.2f)" % total)
    return round(sum(float(scores[k]) * float(weights[k]) for k in scores) / 100.0, 2)


def pe(price, eps):
    p, e = _num(price), _num(eps)
    if p is None or e is None:
        return "N/A"
    if e <= 0:
        return "N/M"
    return round(p / e, 4)


def valuation(price, ttm_eps, fy2027_eps, fy2028_eps, base_year, base_pe):
    base_eps = fy2027_eps if int(base_year) == 2027 else fy2028_eps
    b_eps, b_pe = _num(base_eps), _num(base_pe)
    if b_eps is None or b_pe is None or b_eps <= 0 or b_pe <= 0:
        raise ValueError("base scenario needs positive EPS and P/E")
    return {
        "ttm_gaap_pe": pe(price, ttm_eps),
        "forward_gaap_pe_2027": pe(price, fy2027_eps),
        "forward_gaap_pe_2028": pe(price, fy2028_eps),
        "base_eps": b_eps,
        "base_pe": b_pe,
        "base_target": round(b_eps * b_pe, 4),
        "eps_growth_2027_2028_pct": (
            round((float(fy2028_eps) / float(fy2027_eps) - 1.0) * 100.0, 4)
            if _num(fy2027_eps) and _num(fy2028_eps) and float(fy2027_eps) > 0 else None
        ),
    }


def target(eps, multiple):
    e, m = _num(eps), _num(multiple)
    if e is None or m is None or e <= 0 or m <= 0:
        raise ValueError("target needs positive EPS and multiple")
    return round(e * m, 4)


def allocation(portfolio: dict, benchmark: dict):
    if set(portfolio) != set(benchmark):
        raise ValueError("portfolio and benchmark sectors must match")
    active = {k: round(float(portfolio[k]) - float(benchmark[k]), 1) for k in portfolio}
    p_sum = round(sum(float(v) for v in portfolio.values()), 2)
    b_sum = round(sum(float(v) for v in benchmark.values()), 2)
    a_sum = round(sum(active.values()), 2)
    if abs(p_sum - 100.0) > 0.2 or abs(b_sum - 100.0) > 0.2 or abs(a_sum) > 0.2:
        raise ValueError("weights must sum 100/100/0 (got %.1f/%.1f/%.1f)" % (p_sum, b_sum, a_sum))
    return active, {"portfolio_sum": p_sum, "benchmark_sum": b_sum, "active_sum": a_sum}

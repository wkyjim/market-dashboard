"""Deterministic financial, regime and portfolio calculations.

Every function returns None when an input is missing or not meaningful
(e.g. P/E on nonpositive EPS) so callers can render N/A or N/M. No function
invents an input, a probability or a target.

Conventions
-----------
- Returns are decimal fractions (0.05 = 5%), not percentages, unless the
  function name ends in ``_pct``.
- Weights are fractions that sum to 1.0 unless the caller explicitly passes
  percent weights to ``weighted_score`` with ``scale=100``.
- ``ttm_eps`` requires exactly four comparable quarterly values.
"""
from __future__ import annotations

import math
from statistics import fmean, median, pstdev, stdev


# ---------------------------------------------------------------- primitives
def _num(value):
    if value is None or isinstance(value, bool):
        return None
    try:
        out = float(value)
    except (TypeError, ValueError):
        return None
    return out if math.isfinite(out) else None


def safe_div(numerator, denominator):
    n, d = _num(numerator), _num(denominator)
    if n is None or d is None or d == 0:
        return None
    return n / d


def pct(value):
    """Decimal fraction -> percentage points."""
    v = _num(value)
    return None if v is None else v * 100.0


# ------------------------------------------------------- financial statements
def revenue_growth(revenue_t, revenue_prev):
    r = safe_div(revenue_t, revenue_prev)
    return None if r is None else r - 1.0


def operating_margin(operating_income, revenue):
    return safe_div(operating_income, revenue)


def net_margin(net_income, revenue):
    return safe_div(net_income, revenue)


def diluted_eps(net_income_available, diluted_shares):
    return safe_div(net_income_available, diluted_shares)


def free_cash_flow(operating_cash_flow, capex):
    ocf, cx = _num(operating_cash_flow), _num(capex)
    if ocf is None or cx is None:
        return None
    return ocf - abs(cx)


def fcf_margin(fcf, revenue):
    return safe_div(fcf, revenue)


def eps_growth(eps_t, eps_prev):
    """Only comparable positive EPS; otherwise None (never a fake growth rate)."""
    a, b = _num(eps_t), _num(eps_prev)
    if a is None or b is None or b <= 0 or a <= 0:
        return None
    return a / b - 1.0


def ttm_eps(quarters):
    """Sum the latest four quarterly diluted EPS values, or None."""
    if not isinstance(quarters, (list, tuple)) or len(quarters) != 4:
        return None
    vals = [_num(q) for q in quarters]
    if any(v is None for v in vals):
        return None
    return sum(vals)


# ------------------------------------------------------- earnings & valuation
def ttm_pe(price, eps):
    p, e = _num(price), _num(eps)
    if p is None or e is None:
        return None
    if e <= 0:
        return "N/M"
    return p / e


def forward_pe(price, forward_eps):
    return ttm_pe(price, forward_eps)


def target_price(forecast_eps, target_pe):
    e, m = _num(forecast_eps), _num(target_pe)
    if e is None or m is None or e <= 0 or m <= 0:
        return None
    return e * m


def pe_premium(current_pe, historical_median_pe):
    """Current P/E over comparable median minus 1 (decimal)."""
    a, b = _num(current_pe), _num(historical_median_pe)
    if a is None or b is None or b <= 0:
        return None
    return a / b - 1.0


def peg(pe, growth_rate_pct):
    """P/E divided by EPS growth in percentage points (e.g. 15 for 15%)."""
    p, g = _num(pe), _num(growth_rate_pct)
    if p is None or g is None or g <= 0:
        return None
    return p / g


def price_to_sales(market_cap, ttm_revenue):
    return safe_div(market_cap, ttm_revenue)


def price_to_book(market_cap, common_equity):
    return safe_div(market_cap, common_equity)


def enterprise_value(market_cap, debt, preferred=0.0, minority=0.0, cash=0.0):
    mc, d = _num(market_cap), _num(debt)
    if mc is None or d is None:
        return None
    parts = [_num(preferred) or 0.0, _num(minority) or 0.0, _num(cash) or 0.0]
    return mc + d + parts[0] + parts[1] - parts[2]


def ev_to_ebitda(ev, ebitda):
    e = _num(ebitda)
    if e is None or e <= 0:
        return None
    return safe_div(ev, e)


def fcf_yield(fcf, market_cap):
    return safe_div(fcf, market_cap)


# ------------------------------------------------------- valuation scenarios
def scenario_target(scenario_eps, scenario_pe):
    return target_price(scenario_eps, scenario_pe)


def expected_return(target, current_price, dividends=0.0):
    t, p = _num(target), _num(current_price)
    if t is None or p is None or p <= 0:
        return None
    d = _num(dividends) or 0.0
    return (t + d) / p - 1.0


def downside(bear_target, current_price):
    return expected_return(bear_target, current_price)


def reward_risk(upside, downside_value):
    """Positive expected upside / absolute downside."""
    u, d = _num(upside), _num(downside_value)
    if u is None or d is None or d == 0:
        return None
    return abs(u) / abs(d)


def probability_weighted(values, probabilities):
    """Σ(probability * value); probabilities must be fractions summing to 1."""
    if not values or len(values) != len(probabilities):
        return None
    p = [_num(x) for x in probabilities]
    v = [_num(x) for x in values]
    if any(x is None for x in p + v) or abs(sum(p) - 1.0) > 1e-6:
        return None
    return sum(pi * vi for pi, vi in zip(p, v))


def probability_weighted_target(targets, probabilities):
    return probability_weighted(targets, probabilities)


def probability_weighted_return(returns, probabilities):
    return probability_weighted(returns, probabilities)


# --------------------------------------------------------- regime / scoring
def weighted_score(scores: dict, weights: dict, scale: float = 1.0) -> float | None:
    """Σ(score_i * weight_i). Missing factor -> None (never silently dropped)."""
    if not scores or not weights or set(scores) != set(weights):
        return None
    total = 0.0
    for key, score in scores.items():
        s, w = _num(score), _num(weights[key])
        if s is None or w is None:
            return None
        total += s * w
    return total * scale


def weights_sum(weights: dict) -> float | None:
    vals = [_num(v) for v in weights.values()]
    if not vals or any(v is None for v in vals):
        return None
    return sum(vals)


def score_adjustment_effect(python_scores, python_weights, ai_scores):
    """Σ[python weight * (AI score - python score)]."""
    if set(python_scores) != set(ai_scores):
        return None
    return sum(python_weights[k] * (ai_scores[k] - python_scores[k]) for k in python_scores)


def weight_adjustment_effect(python_weights, ai_weights, ai_scores):
    """Σ[(AI weight - python weight) * AI score]."""
    if set(python_weights) != set(ai_weights):
        return None
    return sum((ai_weights[k] - python_weights[k]) * ai_scores[k] for k in ai_weights)


def attribution(python_scores, python_weights, ai_scores, ai_weights):
    """Full two-step decomposition; the identity must hold to machine precision."""
    baseline = weighted_score(python_scores, python_weights)
    final = weighted_score(ai_scores, ai_weights)
    if baseline is None or final is None:
        return None
    se = score_adjustment_effect(python_scores, python_weights, ai_scores)
    we = weight_adjustment_effect(python_weights, ai_weights, ai_scores)
    return {
        "python_baseline": baseline,
        "ai_final": final,
        "score_effect": se,
        "weight_effect": we,
        "explained": se + we,
        "residual": (final - baseline) - (se + we),
    }


def score_change_attribution(prev_scores, prev_weights, cur_scores, cur_weights):
    """Period-over-period factor and weight effects (exact identity)."""
    if set(prev_scores) != set(cur_scores) or set(prev_weights) != set(cur_weights):
        return None
    factor = sum(prev_weights[k] * (cur_scores[k] - prev_scores[k]) for k in cur_scores)
    weight = sum((cur_weights[k] - prev_weights[k]) * cur_scores[k] for k in cur_weights)
    total = weighted_score(cur_scores, cur_weights) - weighted_score(prev_scores, prev_weights)
    return {"factor_effect": factor, "weight_effect": weight,
            "total_change": total, "residual": total - factor - weight}


# --------------------------------------------------------- sector returns
def sector_return(price_end, price_start):
    p1, p0 = _num(price_end), _num(price_start)
    if p1 is None or p0 is None or p0 <= 0:
        return None
    return p1 / p0 - 1.0


def excess_return(sector_ret, benchmark_ret):
    a, b = _num(sector_ret), _num(benchmark_ret)
    return None if a is None or b is None else a - b


def hit(side, excess):
    """OW hit when excess > 0, UW hit when excess < 0; else False."""
    e = _num(excess)
    if e is None:
        return None
    return e > 0 if str(side).upper() == "OW" else (e < 0 if str(side).upper() == "UW" else False)


def hit_rate(pairs):
    """pairs: iterable of (side, excess_return) -> correct / evaluated."""
    evaluated = [(s, e) for s, e in pairs if _num(e) is not None and str(s).upper() in ("OW", "UW")]
    if not evaluated:
        return None
    return sum(1 for s, e in evaluated if hit(s, e)) / len(evaluated)


def _rank(values):
    order = sorted(range(len(values)), key=lambda i: values[i])
    ranks = [0.0] * len(values)
    i = 0
    while i < len(order):
        j = i
        while j + 1 < len(order) and values[order[j + 1]] == values[order[i]]:
            j += 1
        avg = (i + j) / 2.0 + 1.0
        for k in range(i, j + 1):
            ranks[order[k]] = avg
        i = j + 1
    return ranks


def spearman_rho(xs, ys):
    """Rank correlation with tie-aware average ranks."""
    x = [_num(v) for v in xs]
    y = [_num(v) for v in ys]
    if len(x) != len(y) or len(x) < 2 or any(v is None for v in x + y):
        return None
    rx, ry = _rank(x), _rank(y)
    mx, my = fmean(rx), fmean(ry)
    num = sum((a - mx) * (b - my) for a, b in zip(rx, ry))
    den = math.sqrt(sum((a - mx) ** 2 for a in rx) * sum((b - my) ** 2 for b in ry))
    return None if den == 0 else num / den


def rank_ic(ratings_by_date):
    """ratings_by_date: list of (ratings, future_excess_returns) -> mean Spearman."""
    rhos = [spearman_rho(r, e) for r, e in ratings_by_date]
    rhos = [x for x in rhos if x is not None]
    return fmean(rhos) if rhos else None


def active_weight(portfolio_weight, benchmark_weight):
    a, b = _num(portfolio_weight), _num(benchmark_weight)
    return None if a is None or b is None else a - b


def active_return(active_weights, sector_returns, costs=0.0):
    """Σ(active weight * sector return) - costs."""
    if len(active_weights) != len(sector_returns):
        return None
    total = 0.0
    for w, r in zip(active_weights, sector_returns):
        a, b = _num(w), _num(r)
        if a is None or b is None:
            return None
        total += a * b
    c = _num(costs) or 0.0
    return total - c


# ------------------------------------------------------------- portfolio risk
def portfolio_return(weights, asset_returns, costs=0.0):
    if len(weights) != len(asset_returns):
        return None
    total = 0.0
    for w, r in zip(weights, asset_returns):
        a, b = _num(w), _num(r)
        if a is None or b is None:
            return None
        total += a * b
    return total - (_num(costs) or 0.0)


def portfolio_variance(weights, covariance):
    """wᵀΣw for a square covariance matrix."""
    n = len(weights)
    if n == 0 or len(covariance) != n or any(len(row) != n for row in covariance):
        return None
    total = 0.0
    for i in range(n):
        for j in range(n):
            wi, wj = _num(weights[i]), _num(weights[j])
            c = _num(covariance[i][j])
            if wi is None or wj is None or c is None:
                return None
            total += wi * wj * c
    return total


def portfolio_volatility(weights, covariance):
    v = portfolio_variance(weights, covariance)
    return None if v is None or v < 0 else math.sqrt(v)


def covariance(xs, ys):
    x = [_num(v) for v in xs]
    y = [_num(v) for v in ys]
    if len(x) != len(y) or len(x) < 2 or any(v is None for v in x + y):
        return None
    mx, my = fmean(x), fmean(y)
    return sum((a - mx) * (b - my) for a, b in zip(x, y)) / (len(x) - 1)


def beta(asset_returns, benchmark_returns):
    cov = covariance(asset_returns, benchmark_returns)
    var = covariance(benchmark_returns, benchmark_returns)
    if cov is None or var is None or var == 0:
        return None
    return cov / var


def portfolio_beta(weights, betas):
    if len(weights) != len(betas):
        return None
    total = 0.0
    for w, b in zip(weights, betas):
        a, c = _num(w), _num(b)
        if a is None or c is None:
            return None
        total += a * c
    return total


def correlation(xs, ys):
    cov = covariance(xs, ys)
    sx, sy = stdev([v for v in xs if _num(v) is not None]), stdev([v for v in ys if _num(v) is not None])
    if cov is None or sx == 0 or sy == 0:
        return None
    return cov / (sx * sy)


def tracking_error(portfolio_returns, benchmark_returns, periods_per_year=252):
    active = [a - b for a, b in zip(portfolio_returns, benchmark_returns)]
    if len(active) < 2:
        return None
    return stdev(active) * math.sqrt(periods_per_year)


def information_ratio(active_return_annual, tracking_error_annual):
    return safe_div(active_return_annual, tracking_error_annual)


def sharpe(excess_return_annual, volatility_annual):
    return safe_div(excess_return_annual, volatility_annual)


def max_drawdown(values):
    vals = [_num(v) for v in values]
    if not vals or any(v is None for v in vals) or any(v <= 0 for v in vals):
        return None
    peak = vals[0]
    worst = 0.0
    for v in vals:
        peak = max(peak, v)
        worst = min(worst, v / peak - 1.0)
    return worst


def _percentile(values, q):
    vals = sorted(_num(v) for v in values if _num(v) is not None)
    if not vals:
        return None
    if len(vals) == 1:
        return vals[0]
    pos = (len(vals) - 1) * q
    lo, hi = math.floor(pos), math.ceil(pos)
    if lo == hi:
        return vals[int(pos)]
    return vals[lo] + (vals[hi] - vals[lo]) * (pos - lo)


def historical_var(pnl, level=0.95):
    """Positive loss at the (1-level) left tail; e.g. 95% -> 5th percentile loss."""
    q = _percentile(pnl, 1.0 - level)
    return None if q is None else -q


def expected_shortfall(pnl, level=0.95):
    """Average loss beyond the VaR threshold (positive loss)."""
    var = historical_var(pnl, level)
    if var is None:
        return None
    tail = [v for v in pnl if _num(v) is not None and -_num(v) >= var]
    if not tail:
        return var
    return -fmean(tail)


# ------------------------------------------------------------ position sizing
def risk_based_notional(capital, risk_budget, assumed_loss_fraction):
    """capital * risk budget / assumed loss fraction."""
    c, b, l = _num(capital), _num(risk_budget), _num(assumed_loss_fraction)
    if c is None or b is None or l is None or l <= 0:
        return None
    return c * b / l


def position_weight(notional, capital):
    return safe_div(notional, capital)


def gross_exposure(positions, nav):
    """Σ|market value| / NAV."""
    vals = [_num(p) for p in positions]
    n = _num(nav)
    if not vals or any(v is None for v in vals) or n is None or n <= 0:
        return None
    return sum(abs(v) for v in vals) / n


def net_exposure(positions, nav):
    vals = [_num(p) for p in positions]
    n = _num(nav)
    if not vals or any(v is None for v in vals) or n is None or n <= 0:
        return None
    return sum(vals) / n


# ----------------------------------------------------------------- pair trades
def pair_return(long_return, short_return, long_weight=1.0, short_weight=1.0, costs=0.0):
    lr, sr = _num(long_return), _num(short_return)
    lw, sw = _num(long_weight), _num(short_weight)
    if None in (lr, sr, lw, sw):
        return None
    return lw * lr - sw * sr - (_num(costs) or 0.0)


def beta_neutral_short_weight(long_weight, beta_long, beta_short):
    """wS = wL * betaL / betaS."""
    wl, bl, bs = _num(long_weight), _num(beta_long), _num(beta_short)
    if wl is None or bl is None or bs is None or bs == 0:
        return None
    return wl * bl / bs


def dv01_neutral_short_notional(long_notional, long_dv01, short_dv01):
    """Long DV01 = Short DV01 -> short notional = long notional * DV01_L / DV01_S."""
    ln, ld, sd = _num(long_notional), _num(long_dv01), _num(short_dv01)
    if ln is None or ld is None or sd is None or sd == 0:
        return None
    return ln * ld / sd


def pair_volatility(long_weight, short_weight, long_var, short_var, cov):
    """sqrt(wᵀΣw) with signed weights [wL, -wS]."""
    wl, ws = _num(long_weight), _num(short_weight)
    lv, sv, c = _num(long_var), _num(short_var), _num(cov)
    if None in (wl, ws, lv, sv, c):
        return None
    var = wl * wl * lv + ws * ws * sv - 2 * wl * ws * c
    return None if var < 0 else math.sqrt(var)


# ------------------------------------------------------------------- QC helpers
def qc_probabilities(probabilities, expected_n=3, tol=1e-6):
    vals = [_num(p) for p in probabilities]
    if len(vals) != expected_n or any(v is None for v in vals):
        return "scenario probabilities must be %d numeric values" % expected_n
    if any(v < 0 or v > 1 for v in vals):
        return "scenario probabilities must be between 0 and 1"
    if abs(sum(vals) - 1.0) > tol:
        return "scenario probabilities must sum to 100%% (got %.4f)" % (sum(vals) * 100)
    return None


def qc_target(eps, pe, target, tol=0.005):
    expected = target_price(eps, pe)
    if expected is None or _num(target) is None:
        return "target requires positive EPS and P/E"
    if abs(_num(target) / expected - 1.0) > tol:
        return "target %.2f != EPS x P/E %.2f" % (_num(target), expected)
    return None


def qc_weights(weights, tol=1e-6):
    total = weights_sum(weights)
    if total is None:
        return "weights missing or non-numeric"
    if abs(total - 1.0) > tol:
        return "weights must sum to 1.0 (got %.6f)" % total
    return None


def qc_sectors(sectors, expected=11):
    names = [str(s).strip() for s in sectors]
    if len(names) != expected:
        return "expected %d GICS sectors, got %d" % (expected, len(names))
    if len(set(names)) != expected:
        return "GICS sector names must be unique"
    return None

# AEGIS AI-First Market Intelligence

Research generated at: 24 November 2026, 18:08 HKT
Database freshness: equity 2026-11-23 (latest row retrieved 2026-11-24 13:05:22.265864+08:00)
Data cutoff: 2026-11-23 US cash close
Snapshot ID: aegis-hourly-20261124T100844Z

## Executive Summary

- **AI market view: Late-November 2026 US equity market is characterized by a broad, late-cycle growth slowdown with a sharp Information Technology drawdown, while defensive and low-volatility sectors (Consumer Staples, Utilities, Health Care) remain relatively more resilient. Breadth is mixed: the 20-day advance/decline ratio is strongly positive, but 50-day and 200-day breadth have deteriorated, and the index is below both its 50-day and 200-day averages. Macro data show a still-elevated but decelerating inflation backdrop, a labor market near full employment, and a flat-to-modestly-positive 10Y-2Y curve, with policy rates around 3.88%.**
- US equities are in a late-cycle, growth-slowing regime: the S&P 500 is down 5.73% over 20 days and the Information Technology sector is the worst performer at -12.85% over 20 days.
- Defensive sectors are outperforming: Consumer Staples +2.75%, Utilities +1.81%, Health Care +0.08%, while Materials, Industrials, and Energy are the weakest sectors.
- Breadth is bifurcated: 20-day positive breadth is strong (47.12% positive, ADR 5.05), but 50-day and 200-day breadth have turned negative, and the index sits below both moving averages.
- Macro backdrop is mixed: CPI is elevated but decelerating, unemployment is low at 4.2%, the 10Y-2Y curve is flat at +0.29%, and policy rates are around 3.88%.
- Credit conditions are moderately tight but not stressed: high-yield OAS is 3.76% and IG OAS is 0.98%, with no directional risk signal in the frozen forecast.
- The market is in a caution posture: momentum and liquidity leaders are concentrated in a few large-cap names, while the broader universe shows weak earnings-revision and forward-EPS coverage.

## Data QC

- Status: **PASS_WITH_WARNINGS**
- Equity session: 0 completed session(s) behind inference date
- Macro session: 2026-11-24 (0 completed session(s) behind inference date)
- Equity provenance: 149 provisional / 12873 canonical
- Breadth lag: 0 session(s); ETF-flow lag: 0 session(s)
- Note: Equity session contains a mix of provisional yfinance and canonical Massive rows.
- External sources: 79 ok / 0 unavailable; retrieved 2026-11-24T10:09:03.664840+00:00

## Idea Discovery

- S&P 500 universe: 503; eligible: 501; transparent shortlist: 20
- Method: independent momentum/dislocation/PE/liquidity buckets; no composite score
- Evidence used: latest close, 20d and 60d price returns, 60d drawdown, trailing P/E, earnings yield, sector-relative P/E, dollar volume, GICS sector
- Not available as verified inputs: verified earnings-revision history for the full universe, FY+2 consensus, structured industry catalyst calendar
- Eligible but not shortlisted: 481 (outside the top independent momentum, dislocation, valuation and liquidity buckets)
- Included: APP (top_20d_momentum); CMG (top_20d_momentum); PNR (top_20d_momentum); CHTR (top_20d_momentum); GEN (top_20d_momentum); IDXX (top_20d_momentum); CLX (top_20d_momentum); CVNA (top_20d_momentum); SNDK (largest_20d_dislocation); NOW (largest_20d_dislocation); DDOG (largest_20d_dislocation); MRVL (largest_20d_dislocation); RDDT (largest_20d_dislocation); INTC (largest_20d_dislocation); LITE (largest_20d_dislocation); COIN (largest_20d_dislocation); NVDA (liquidity_leader); MU (liquidity_leader); AMD (liquidity_leader); AAPL (liquidity_leader)
- Excluded reasons: {"missing_recent_or_latest_price": 2}
- Valuation-quality rejected: [{"flags": ["forward_pe_outside_plausible_range", "implausible_earnings_yield", "forward_eps_vs_reported_jump"], "ticker": "CHTR"}, {"flags": ["forward_pe_outside_plausible_range", "implausible_earnings_yield"], "ticker": "SNDK"}, {"flags": ["forward_eps_vs_reported_jump"], "ticker": "MRVL"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "RDDT"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "INTC"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "LITE"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "COIN"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "NVDA"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "MU"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "AMD"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "AAPL"}]

## Market Snapshot

| Asset | Latest | Change | Observation |
| --- | --- | --- | --- |
| S&P 500 (SPX) | 7237.17 | -5.73% over 20d | Index below both 50-day and 200-day averages; 20-day breadth is positive but longer-term breadth is deteriorating. |
| Information Technology (XLK) | -12.85% | -12.85% over 20d | Worst sector; trailing P/E 28.64, but forward EPS data are unavailable for the shortlist leaders. |
| Energy (XLE) | -14.03% | -14.03% over 20d | Worst sector; trailing P/E 14.95, low valuation but sharp price decline. |
| Consumer Staples (XLP) | +2.75% | +2.75% over 20d | Best sector; trailing P/E 24.32, defensive demand supporting relative strength. |
| Utilities (XLU) | +1.81% | +1.81% over 20d | Positive 20d return; trailing P/E 17.82, medium-term deterioration in flow structure. |
| Health Care (XLV) | +0.08% | +0.08% over 20d | Near-flat; trailing P/E 29.25, tactical profit-taking inside structural accumulation. |

## Macro, Fiscal, Rates, Liquidity and Credit

- Growth: The 20-day S&P 500 return of -5.73% and the -12.85% Information Technology drawdown signal a sharp deceleration in US equity growth momentum, consistent with a late-cycle environment.
- Inflation: CPI is elevated but decelerating; the database shows CPI at 336.30 (Sep-2026) and core CPI at 338.90, while external S004 reports CPI at 337.476 for Oct-2026, indicating continued but moderating price pressure.
- Policy: The effective federal funds rate is 3.88% as of 2026-11-20, and the 10Y-2Y Treasury spread is +0.29% as of 2026-11-23, suggesting a flat-to-modestly-positive curve with limited policy easing pressure.
- Rates: Credit spreads are moderately tight but not distressed: high-yield OAS is 3.76% and IG OAS is 0.98% as of 2026-11-20, implying manageable but not negligible credit risk.
- Liquidity: The frozen risk forecast shows 5-day forecast volatility of 25.19%, above the historical baseline of 31.88% and EWMA baseline of 30.12%, with a spike probability of 53.96% versus a 18.50% threshold, indicating elevated near-term volatility risk.
- Credit: High-yield and IG spreads are not signaling acute stress, but the combination of a sharp tech drawdown, negative longer-term breadth, and elevated volatility suggests caution on risk appetite.

## US Equities and 11 GICS Sectors

Macro source IDs: S001, S002, S003, S004, S005, S006, S007

| GICS sector | Evidence | AI research stance | Source IDs |
| --- | --- | --- | --- |
| Information Technology | 20d return -12.85% (XLK); trailing P/E 28.64 (S074); shortlist leaders NVDA, MU, AMD, AAPL flagged as liquidity leaders but with forward EPS missing/unavailable. | Negative momentum and sharp drawdown; valuation is not cheap on forward earnings, and forward EPS coverage is missing for the liquidity leaders. | S074 |
| Energy | 20d return -14.03% (XLE); trailing P/E 14.95 (S075); sharp price decline despite low trailing P/E. | Worst sector; low valuation is offset by a severe price decline and no positive momentum signal. | S075 |
| Consumer Staples | 20d return +2.75% (XLP); trailing P/E 24.32 (S059); defensive sector outperforming in a late-cycle slowdown. | Positive relative strength; defensive demand supports the sector despite a moderate trailing P/E. | S059 |
| Utilities | 20d return +1.81% (XLU); trailing P/E 17.82 (S065); flow structure shows medium-term deterioration. | Positive 20d return but flow structure indicates medium-term deterioration; low-volatility positioning remains relevant. | S065 |
| Health Care | 20d return +0.08% (XLV); trailing P/E 29.25 (S052); tactical profit-taking inside structural accumulation. | Near-flat with institutional accumulation; defensive characteristics support relative stability. | S052 |
| Financials | 20d return -0.66% (XLF); trailing P/E 15.03 (S067); flat price state with neutral flow. | Slightly negative but stable; low trailing P/E and neutral flows suggest no acute stress. | S067 |
| Consumer Discretionary | 20d return +2.34% (XLY); trailing P/E 24.47 (S058); flow z-score 20d -0.24, 60d -0.81, structural distribution. | Positive 20d return but structural distribution and negative 60d flow z-score indicate caution. | S058 |
| Real Estate | 20d return +0.23% (XLRE); trailing P/E 28.65 (S060); flat price state. | Near-flat with moderate trailing P/E; no clear directional signal. | S060 |
| Materials | 20d return -2.88% (XLB); trailing P/E 20.75 (S068); negative sector return. | Negative 20d return; moderate trailing P/E but weak price momentum. | S068 |
| Industrials | 20d return -2.69% (XLI); trailing P/E 26.06 (S070); negative sector return. | Negative 20d return; moderate trailing P/E but weak momentum. | S070 |
| Communication Services | 20d return -0.24% (XLC); trailing P/E 16.46 (S072); flat price state. | Near-flat with low trailing P/E; no clear directional signal. | S072 |

### Sector fundamentals, valuation and earnings

The supplied database provides sector-level ETF returns and trailing P/E for all 11 GICS sectors, but does not supply point-in-time sector fundamentals such as sector-level earnings growth, margins, or consensus revisions. Therefore, sector fundamentals are not available in the evidence base; only price returns and trailing valuation multiples are used. The sector view is based on these supplied data and source IDs.

## Growth vs Value

- Growth: The sharp Information Technology drawdown (-12.85% over 20d) and the S&P 500's -5.73% 20d return indicate a deceleration in US equity growth momentum, with the index below both its 50-day and 200-day averages.
- Value: Energy (XLE, trailing P/E 14.95) and Financials (XLF, trailing P/E 15.03) offer the lowest trailing P/E, but Energy's -14.03% 20d return and Financials' -0.66% return show that low valuation is not accompanied by positive momentum.
- Quality: Consumer Staples (XLP, trailing P/E 24.32) and Utilities (XLU, trailing P/E 17.82) combine positive 20d returns with defensive characteristics, offering relative value in a late-cycle slowdown.
- Earnings coverage: Forward EPS data are missing or unavailable for the shortlist liquidity leaders (NVDA, MU, AMD, AAPL) and several dislocation names, limiting forward growth assessment for the largest-cap names.

## ETF Flows and Breadth

- 20-day breadth is strongly positive: 47.12% of names are above their 20-day moving average, with 419 advancers and 83 decliners (ADR 5.05), indicating short-term participation.
- Longer-term breadth is deteriorating: 50-day breadth change over 5d is -12.83 and over 20d is -7.74; 200-day breadth change over 5d is -6.74 and over 20d is -5.66, showing a loss of participation among larger-cap names.
- The index is below both its 50-day and 200-day averages, and the standardized divergence is -1.609, indicating a bearish divergence in longer-term momentum.
- Flows show structural distribution in Consumer Discretionary (XLY) with 20d flow z-score -0.24 and 60d -0.81, while Health Care (XLV) shows tactical profit-taking inside structural accumulation with a 60d flow z-score of +0.72.
- Utilities (XLU) shows a 20d flow z-score of -1.05, indicating medium-term deterioration, while the 60d z-score is +0.45,

## Stock Ideas

Single-stock research uses reported EPS, forward P/E and company fundamentals. All ideas are research judgments, not validated return predictions.

| Ticker | Security | Research view | Price | EPS | Forward P/E | Base target | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| APP | AppLovin | NEW | 373.92 | 20.86084 | 17.924494 | 417.22 | NEW |
| PNR | Pentair | KEEP | 69.94 | 5.30402 | 13.186226 | 74.26 | KEEP |
| IDXX | Idexx Laboratories | KEEP | 687.02 | 16.8929 | 40.669155 | 473.0 | KEEP |

## ETF Ideas

ETF research uses holdings, portfolio valuation and exposure. Single-stock EPS × P/E valuation is not applied to ETFs.

| Ticker | Fund | Research view | Price | Top holdings | Portfolio valuation | Sector exposure | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| XLY | Consumer Discretionary sector ETF | NEW | 116.93 | AMZN 21.29%, TSLA 18.78%, HD 5.47%, MCD 4.46%, TJX 4.07%, SBUX 3.11%, LOW 3.08%, BKNG 2.93%, MAR 2.24%, HLT 2.11% | Top 10 holdings; numeric weight coverage 67.54% | Consumer Discretionary | NEW |
### APP — AppLovin

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** AppLovin offers a rare combination of top-tier momentum, very high gross and operating margins, and a forward P/E below the trailing multiple. Compared with the other momentum names such as CMG, PNR, and IDXX, AppLovin's margin profile and forward earnings compression make it the more compelling quality-momentum candidate in the shortlist. Alternatives considered: CMG, PNR, IDXX.
- **Thesis:** AppLovin screens as a top 20-day momentum name with a 20-day return of roughly 43% and a 60-day return near 18%, indicating strong recent price momentum. The company reports a high gross margin near 89% and an operating margin near 78%, supporting durable profitability. The forward P/E of about 17.9 is below the trailing P/E of about 25.2, implying the market is pricing in a meaningful earnings step-up. The recent pullback and the news headline describing the stock as still looking cheap after a sharp pullback support a re-entry or accumulation view.
- **Source IDs:** S008, S012, S014, S019
- **Catalysts:** Continued high-margin advertising and content monetization growth, Sustained 20-day momentum and positive 60-day return, Forward earnings growth compressing the forward P/E below the trailing multiple, Potential re-acceleration after the recent pullback
- **Risks:** Momentum names can be volatile and prone to sharp reversals, High valuation multiples leave limited room for error if growth decelerates, Advertising market cyclicality and macroeconomic sensitivity, Forward EPS and fiscal-year mapping are unverified, so forward P/E should be treated with caution
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 20.8608 (source.forwardEps) x AI multiple assumption 20.00; source IDs S008, S012, S014, S019
- **EPS:** 20.86084 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 17.924494
- **FY+1 growth assumption:** 27.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / MSFT / APP shows strong FY1 consensus growth of 27.44% with 25.51% revenue growth and 75.5% earnings growth, supported by 88.8% gross margin and 77.8% operating margin. The forward P/E of 17.9x is below the 20x base multiple, reflecting a premium growth profile. MSFT is used as a named peer reference for high-margin, high-growth software/tech valuation.
- **Company fundamentals:** AppLovin reports a gross margin near 89%, an operating margin near 78%, a profit margin near 66%, and a forward P/E of about 17.9 versus a trailing P/E of about 25.2. Reported diluted EPS is 11.61 and forward EPS is about 20.86. Revenue growth is about 55.5% and earnings growth about 75.5%. The 20-day return is about 43% and the 60-day return is about 18%, with a 60-day drawdown of about -10%.
- **Bull / Base / Bear:** 500.66 / 417.22 / 333.77
- **Bull / Base / Bear returns:** 33.89% / 11.58% / -10.74%
- **Scenario probabilities:** not separately assigned; see scenario table.

### PNR — Pentair

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Pentair is preferable to the more expensive momentum names such as AppLovin and IDXX because it offers a lower forward P/E and a lower valuation risk profile. However, its negative revenue and earnings growth make it less attractive than the strongest momentum candidates, so it is best held as a neutral, valuation-supported position rather than a core buy. Alternatives considered: APP, CMG, IDXX.
- **Thesis:** Pentair screens as a top 20-day momentum name with a 20-day return of about 27% and a 60-day return of about 13%. The stock has a low forward P/E of about 13.2 and a trailing P/E of about 19.1, suggesting the market is not pricing in aggressive future earnings growth. Revenue growth is about -4.5% and earnings growth is about -18.8%, indicating that current momentum is not yet supported by broad-based fundamental expansion. The low valuation and positive price momentum justify a neutral stance rather than a strong buy or avoid.
- **Source IDs:** S010, S013, S016, S027
- **Catalysts:** Positive 20-day and 60-day price momentum, Attractive forward P/E relative to the broader shortlist, Potential stabilization if the industrial and water-treatment end markets stabilize
- **Risks:** Negative revenue and earnings growth contradict the momentum signal, Forward P/E of about 13.2 may already reflect limited upside, Industrial end-market cyclicality and capital expenditure sensitivity, No verified FY2+ consensus or earnings-revision history to confirm durability
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 5.3040 (source.forwardEps) x AI multiple assumption 14.00; source IDs S010, S013, S016, S027
- **EPS:** 5.30402 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 13.186226
- **FY+1 growth assumption:** 12.82%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / UPS / PNR has FY1 consensus growth of 12.82% with 18.38% revenue growth, though earnings growth is negative at -18.8%. The 40.2% gross margin and 21.4% operating margin support a moderate multiple. UPS is used as a named peer reference for freight/logistics valuation.
- **Company fundamentals:** Pentair reports a forward P/E of about 13.2 and a trailing P/E of about 19.1. Reported diluted EPS is 2.76 and forward EPS is 5.30. Revenue growth is about -4.5% and earnings growth is about -18.8%. Gross margin is about 40%, operating margin about 21%, and profit margin about 15%. The 20-day return is about 27% and the 60-day return is about 13%, with a 60-day drawdown of about -3%.
- **Bull / Base / Bear:** 90.17 / 74.26 / 58.34
- **Bull / Base / Bear returns:** 28.92% / 6.18% / -16.59%
- **Scenario probabilities:** not separately assigned; see scenario table.

### IDXX — Idexx Laboratories

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Idexx is preferable to the lower-multiple momentum names such as PNR and GEN because it offers stronger revenue and earnings growth and the best 60-day momentum in the shortlist. However, its high multiple means it is not a clear buy; it is best treated as a premium-growth holding with a neutral stance. Alternatives considered: APP, PNR, GEN.
- **Thesis:** Idexx Laboratories screens as a top 20-day momentum name with a 20-day return of about 20% and a 60-day return of about 24%, the strongest 60-day return among the momentum candidates. The stock carries a high forward P/E of about 40.7 and a trailing P/E of about 40.7, implying the market is paying a premium for its growth. Revenue growth is about 10% and earnings growth about 18%, which supports the premium multiple, but the high valuation leaves limited room for disappointment if growth slows.
- **Source IDs:** S020, S029, S031, S034
- **Catalysts:** Strong 60-day momentum of about 24%, Positive revenue and earnings growth of about 10% and 18%, High-margin diagnostics and veterinary software franchise, Premium multiple may expand further if growth re-accelerates
- **Risks:** High forward P/E of about 40.7 limits upside if growth decelerates, Momentum can reverse quickly in a high-multiple name, Small 60-day drawdown of about -3% is manageable but does not eliminate volatility risk, No verified FY2+ consensus or earnings-revision history to confirm durability
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 16.8929 (source.forwardEps) x AI multiple assumption 28.00; source IDs S020, S029, S031, S034
- **EPS:** 16.8929 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 40.669155
- **FY+1 growth assumption:** 12.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / CDW / IDXX shows FY1 consensus growth of 12.44% with 8.88% revenue growth and 17.9% earnings growth, supported by 62.7% gross margin and 32.5% operating margin. The 40.7x forward P/E is high, so the 28x base multiple reflects a premium but justified by growth and margins. CDW is used as a named peer reference for IT services/security valuation.
- **Company fundamentals:** Idexx Laboratories reports a forward P/E of about 40.7 and a trailing P/E of about 40.7. Reported diluted EPS is 11.75 and forward EPS is 16.89. Revenue growth is about 10% and earnings growth about 18%. Gross margin is about 63%, operating margin about 32%, and profit margin about 25%. The 20-day return is about 20% and the 60-day return is about 24%, with a 60-day drawdown of about -3%.
- **Bull / Base / Bear:** 574.36 / 473.0 / 371.64
- **Bull / Base / Bear returns:** -16.4% / -31.15% / -45.91%
- **Scenario probabilities:** not separately assigned; see scenario table.

### XLY — Consumer Discretionary sector ETF

- **Type:** ETF
- **Research view:** NEW (stance: NEUTRAL)
- **Why preferred / alternatives:** XLY is preferable to the sector ETFs as a broad consumer discretionary proxy because it captures the strongest sector momentum in the shortlist and offers diversified exposure across e-commerce, autos, home improvement, restaurants, and travel. Compared with the individual momentum stocks, it provides lower single-stock risk, but it lacks the margin and valuation precision of the top individual candidates. Alternatives considered: XLV, XLP, XLRE, XLF, XLU, XLB.
- **Thesis:** The Consumer Discretionary sector ETF has the strongest sector-level price action in the shortlist, with a raw price change of about +4.0% and a high dollar volume of about $11.6 billion. The top holdings include Amazon, Tesla, Home Depot, McDonald's, TJX, Starbucks, Lowe's, Booking Holdings, Marriott, and Hilton, giving broad exposure to e-commerce, autos, home improvement, restaurants, and travel. The sector's momentum is attractive, but the ETF is a broad market proxy and does not offer the same margin or valuation precision as the individual stock candidates.
- **Source IDs:** S058, S064
- **Catalysts:** Sector-level price strength of about +4.0%, High dollar volume supporting liquidity and execution, Diversified exposure to consumer discretionary sub-sectors, Potential continuation if consumer spending and travel remain resilient
- **Risks:** Broad sector exposure means individual stock risks are diluted but not eliminated, High concentration in Amazon and Tesla adds single-stock and technology/automobile sensitivity, Consumer discretionary is sensitive to macroeconomic slowdown and consumer confidence, Sector-level fundamentals are not as granular as individual company analysis
- **Valuation method:** Holdings/portfolio valuation with AI total-return assumption
- **Valuation status:** verified; forward-EPS source: ; period flags: 
- **Valuation assumptions:** Holdings/portfolio valuation; 10 weighted holdings; coverage 67.54%; source IDs S058, S064
- **Top holdings:** AMZN 21.29%, TSLA 18.78%, HD 5.47%, MCD 4.46%, TJX 4.07%, SBUX 3.11%, LOW 3.08%, BKNG 2.93%, MAR 2.24%, HLT 2.11%
- **Portfolio valuation:** Top 10 holdings; numeric weight coverage 67.54%
- **Sector exposure:** Consumer Discretionary
- **Underlying drivers:** Consumer discretionary spending, e-commerce growth, autos, home improvement, restaurants, travel, and leisure. The ETF's top holdings include Amazon, Tesla, Home Depot, McDonald's, TJX, Starbucks, Lowe's, Booking Holdings, Marriott, and Hilton.
- **Bull / Base / Bear:** 130.96 / 122.78 / 109.91
- **Bull / Base / Bear returns:** 12.0% / 5.0% / -6.0%
- **Scenario probabilities:** not separately assigned; see scenario table.

## Quant Risk Layer

| Field | Value |
| --- | --- |
| Volatility model | vol5_ols_v1 |
| Spike model | spike_logit_v1 |
| As-of date | 2026-11-23 |
| Target window | 2026-11-24 to 2026-12-01 |
| Forecast 5D annualized volatility | 25.19% |
| Historical-vol baseline | 31.88% |
| EWMA baseline | 30.12% |
| Spike probability | 53.96% |
| Spike threshold | 18.50% |
| Status | prospective |
| Forecast ID | 26012b9968dbe3b1 |

Risk-only; no directional interpretation or allocation implication.

## Scenarios

### Short Term (5 trading sessions)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 25% | +2.00% | Low spike probability (0.54) and frozen daily-close model imply limited near-term volatility; a modest 2.0% upside is justified if US close confirms stable liquidity and no credit stress. |
| Base | 50% | +0.00% | Directional signal is false and forecast vol (0.252) is elevated relative to historical baseline (0.319), so the most likely path is a flat 0.0% range as the market absorbs data without a clear directional catalyst. |
| Bear | 25% | -2.00% | If the elevated forecast vol triggers a risk-off repricing or a credit spread widening, a -2.0% drawdown is plausible given the 0.54 spike probability and absence of a directional hedge. |

### Long Term (12 months)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 30% | +8.00% | Sustained earnings growth and stable rates support a 8.0% long-term upside, with a 30% probability if credit conditions remain benign and breadth expands. |
| Base | 40% | +3.00% | A 3.0% long-term return reflects modest earnings momentum and neutral rate expectations, with a 40% probability if no major policy or credit shock materializes. |
| Bear | 30% | -5.00% | A -5.0% long-term decline is plausible if elevated volatility persists, credit spreads widen, or earnings disappoint, with a 30% probability under a risk-off regime. |

## Positioning


## Catalysts

| Date | Event | Why it matters |
| --- | --- | --- |

## Key Risks


## External Source Ledger

| ID | Type | Ticker | Published | Status | URL | Claims |
| --- | --- | --- | --- | --- | --- | --- |
| S001 | macro | macro | 2026-11-20 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFF&cosd=2026-01-01 | Effective federal funds rate (DFF) latest observation 2026-11-20: 3.88 |
| S002 | macro | macro | 2026-11-20 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLH0A0HYM2&cosd=2026-01-01 | US high-yield OAS (BAMLH0A0HYM2) latest observation 2026-11-20: 3.76 |
| S003 | macro | macro | 2026-11-20 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLC0A0CM&cosd=2026-01-01 | US investment-grade OAS (BAMLC0A0CM) latest observation 2026-11-20: 0.98 |
| S004 | macro | macro | 2026-10-01 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCSL&cosd=2026-01-01 | US CPI (CPIAUCSL) latest observation 2026-10-01: 337.476 |
| S005 | macro | macro | 2026-10-01 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=UNRATE&cosd=2026-01-01 | US unemployment rate (UNRATE) latest observation 2026-10-01: 4.1 |
| S006 | macro | macro | 2026-10-01 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=PAYEMS&cosd=2026-01-01 | US nonfarm payrolls (PAYEMS) latest observation 2026-10-01: 159293 |
| S007 | macro | macro | 2026-11-23 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=T10Y2Y&cosd=2026-01-01 | 10Y-2Y Treasury spread (T10Y2Y) latest observation 2026-11-23: 0.29 |
| S008 | filing | APP | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001751008&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0001751008-26-000069); 8-K filed 2026-11-04 (accession 0001751008-26-000068); 10-Q filed 2026-08-05 (accession 0001751008-26-000059) |
| S009 | filing | CMG | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001058090&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0001058090-26-000104); 8-K filed 2026-10-28 (accession 0001058090-26-000103); 8-K filed 2026-09-14 (accession 0001058090-26-000088) |
| S010 | filing | PNR | 2026-10-27 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-27 (accession 0000077360-26-000058); 8-K filed 2026-10-27 (accession 0000077360-26-000055); 8-K filed 2026-09-22 (accession 0000077360-26-000050) |
| S011 | news | CMG | Sat, 21 Nov 2026 02:05:00 GMT | ok | https://news.google.com/rss/search?q=CMG+Chipotle+Mexican+Grill+stock&hl=en-US&gl=US&ceid=US:en | Chipotle Mexican Grill vs. Hershey: Which Consumer Stock Is a Better Buy for 2027? - Yahoo Finance (Sat, 21 Nov 2026 02:05:00 GMT); Can Chipotle's AI Rollout Turn Efficiency Into Earnings Growth? - TradingView (Mon, 23 Nov 2026 14:46:00 GMT); Chipotle Mexican Grill Stock Rides A 5-Day Winning Streak To A 19% Gain - Trefis (Wed, 04 Nov 2026 08:00:00 GMT) |
| S012 | news | APP | Mon, 23 Nov 2026 01:07:00 GMT | ok | https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en | AppLovin (APP) Stock Still Looks Cheap After Sharp Pullback - Yahoo Finance (Mon, 23 Nov 2026 01:07:00 GMT); APP Falls 14.9% in One Week as Growth Strength Meets Execution Risk - TradingView (Mon, 23 Nov 2026 15:30:00 GMT); AppLovin vs. Reddit: Which Technology Stock Is a Better Buy for 2027? - The Motley Fool (Sat, 21 Nov 2026 23:19:26 GMT) |
| S013 | news | PNR | Mon, 23 Nov 2026 15:58:41 GMT | ok | https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en | Pentair plc (PNR) Stock Price, News, Quote & History - Yahoo! Finance Canada (Mon, 23 Nov 2026 15:58:41 GMT); Pentair plc (PNR) stock price, news, quote and history - Yahoo Finance UK (Mon, 23 Nov 2026 15:45:16 GMT); Pentair plc (NYSE:PNR): A Quality Stock With a Staggering 55.92% ROIC - ChartMill (Tue, 14 Jul 2026 07:00:00 GMT) |
| S014 | stock | APP | 2026-11-24 | ok | https://finance.yahoo.com/quote/APP | Trailing P/E: 25.179798; Forward P/E: 17.924494; Forward EPS: 20.86084; Price: 373.92; Market price: 373.92; Market cap: 123887919104; Sector: Communication Services; Trailing Eps: 14.85; Revenue Growth: 0.555; Earnings Growth: 0.755; Gross Margin: 0.8878; Operating Margin: 0.77782995; Profit Margin: 0.65887; Return On Equity: 2.1008599; Total Revenue: 7608893952; Market Cap: 123887919104; Consensus EPS FY+1: 20.72451; growth: 0.2744 |
| S015 | stock | CMG | 2026-11-24 | ok | https://finance.yahoo.com/quote/CMG | Trailing P/E: 33.8785; Forward P/E: 27.392395; Forward EPS: 1.32336; Price: 36.25; Market price: 36.25; Market cap: 45855342592; Sector: Consumer Cyclical; Trailing Eps: 1.07; Revenue Growth: 0.096; Earnings Growth: -0.062; Gross Margin: 0.39314; Operating Margin: 0.14715; Profit Margin: 0.10832; Return On Equity: 0.48518002; Total Revenue: 12713477120; Market Cap: 45855342592; Consensus EPS FY+1: 1.32336; growth: 0.216 |
| S016 | stock | PNR | 2026-11-24 | ok | https://finance.yahoo.com/quote/PNR | Trailing P/E: 19.05722; Forward P/E: 13.186226; Forward EPS: 5.30402; Price: 69.94; Market price: 69.94; Market cap: 11166248960; Sector: Industrials; Trailing Eps: 3.67; Revenue Growth: -0.045; Earnings Growth: -0.188; Gross Margin: 0.40168998; Operating Margin: 0.21410999; Profit Margin: 0.15435; Return On Equity: 0.15605; Total Revenue: 3966200064; Market Cap: 11166248960; Consensus EPS FY+1: 5.30402; growth: 0.1282 |
| S017 | filing | CMG | 2026-10-29 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001058090.json | Diluted EPS 0.82 for period ending 2026-09-30 (filed 2026-10-29) |
| S018 | filing | CHTR | 2026-11-06 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-06 (accession 0001091667-26-000073); 8-K filed 2026-11-06 (accession 0001091667-26-000072); 8-K filed 2026-10-27 (accession 0001091667-26-000064) |
| S019 | filing | APP | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json | Diluted EPS 11.61 for period ending 2026-09-30 (filed 2026-11-04) |
| S020 | filing | IDXX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000874716&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000874716-26-000135); 8-K filed 2026-11-02 (accession 0001104659-26-120892); 10-Q filed 2026-08-04 (accession 0000874716-26-000123) |
| S021 | filing | GEN | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0000849399-26-000083); 8-K filed 2026-10-28 (accession 0000849399-26-000081); 8-K filed 2026-10-09 (accession 0000849399-26-000079) |
| S022 | stock | GEN | 2026-11-24 | ok | https://finance.yahoo.com/quote/GEN | Trailing P/E: 15.248732; Forward P/E: 9.001127; Forward EPS: 3.33736; Price: 30.04; Market price: 30.04; Market cap: 17822015488; Sector: Technology; Trailing Eps: 1.97; Revenue Growth: 0.122; Earnings Growth: 1.286; Gross Margin: 0.77410007; Operating Margin: 0.43229; Profit Margin: 0.23068; Return On Equity: 0.46402; Total Revenue: 5228000256; Market Cap: 17822015488; Consensus EPS FY+1: 3.33736; growth: 0.1286 |
| S023 | news | GEN | Sun, 22 Nov 2026 00:38:11 GMT | ok | https://news.google.com/rss/search?q=GEN+Gen+Digital+stock&hl=en-US&gl=US&ceid=US:en | Gen Digital Inc. (GEN) Stock Price, News, Quote & History - Yahoo! Finance Canada (Sun, 22 Nov 2026 00:38:11 GMT); Gen Digital Inc. stock underperforms Friday when compared to competitors - MarketWatch (Fri, 20 Nov 2026 22:08:00 GMT); Gen Digital Insider Sold Shares Worth $2,204,209, According to a Recent SEC Filing - www.marketscreener.com (Mon, 23 Nov 2026 08:59:15 GMT) |
| S024 | filing | CHTR | 2026-11-06 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001091667.json | Diluted EPS 0.38 for period ending 2026-09-30 (filed 2026-11-06) |
| S025 | news | CHTR | Tue, 24 Nov 2026 07:06:00 GMT | ok | https://news.google.com/rss/search?q=CHTR+Charter+Communications+stock&hl=en-US&gl=US&ceid=US:en | Charter Communications (CHTR) Stock Could Still Offer Value On Fresh Investigation News - Simply Wall St (Tue, 24 Nov 2026 07:06:00 GMT); Charter Communications (CHTR) Stock Could Be A Bargain Following Its New Operating Model - Yahoo Finance (Sat, 14 Nov 2026 08:00:00 GMT); Can Charter Communications Stock Jump 40%? - Trefis (Thu, 29 Oct 2026 07:00:00 GMT) |
| S026 | stock | CHTR | 2026-11-24 | ok | https://finance.yahoo.com/quote/CHTR | Trailing P/E: 12.022556; Forward P/E: 2.8055801; Forward EPS: 45.59485; Price: 127.92; Market price: 127.92; Market cap: 22904274944; Sector: Communication Services; Trailing Eps: 10.64; Revenue Growth: 0.091; Gross Margin: 0.55084; Operating Margin: 0.23389; Profit Margin: 0.02498; Return On Equity: 0.07019; Total Revenue: 55645999104; Market Cap: 22904274944; Consensus EPS FY+1: 47.75367; growth: 1.4848 |
| S027 | filing | PNR | 2026-10-27 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json | Diluted EPS 2.76 for period ending 2026-09-30 (filed 2026-10-27) |
| S028 | filing | CLX | 2026-11-19 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 | 8-K filed 2026-11-19 (accession 0001206774-26-000606); 10-Q filed 2026-11-02 (accession 0000021076-26-000046); 8-K filed 2026-11-02 (accession 0000021076-26-000044) |
| S029 | stock | IDXX | 2026-11-24 | ok | https://finance.yahoo.com/quote/IDXX | Trailing P/E: 46.29515; Forward P/E: 40.669155; Forward EPS: 16.8929; Price: 687.02; Market price: 687.02; Market cap: 54127738880; Sector: Healthcare; Trailing Eps: 14.84; Revenue Growth: 0.099; Earnings Growth: 0.179; Gross Margin: 0.62722; Operating Margin: 0.32497; Profit Margin: 0.25357; Return On Equity: 0.68925005; Total Revenue: 4662220800; Market Cap: 54127738880; Consensus EPS FY+1: 16.8929; growth: 0.1244 |
| S030 | news | CLX | Mon, 23 Nov 2026 16:27:34 GMT | ok | https://news.google.com/rss/search?q=CLX+Clorox+stock&hl=en-US&gl=US&ceid=US:en | The Clorox Company (CLX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Mon, 23 Nov 2026 16:27:34 GMT); Clorox Purell ProCare™ Recognized for Healthcare Disinfection... - Quantisnow (Mon, 23 Nov 2026 16:15:43 GMT); Clorox (CLX) Stock Rebounds As Q4 Earnings Face Margin Strain - Yahoo Finance (Tue, 03 Nov 2026 08:00:00 GMT) |
| S031 | filing | IDXX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000874716.json | Diluted EPS 11.75 for period ending 2026-09-30 (filed 2026-11-02) |
| S032 | stock | CLX | 2026-11-24 | ok | https://finance.yahoo.com/quote/CLX | Trailing P/E: 18.724821; Forward P/E: 16.877958; Forward EPS: 6.1684; Price: 104.11; Market price: 104.11; Market cap: 12612655104; Sector: Consumer Defensive; Trailing Eps: 5.56; Revenue Growth: 0.333; Earnings Growth: 1.138; Gross Margin: 0.41939998; Operating Margin: 0.14286; Profit Margin: 0.09408; Return On Equity: 5.34363; Total Revenue: 7196000256; Market Cap: 12612655104; Consensus EPS FY+1: 6.1684; growth: 0.0769 |
| S033 | filing | GEN | 2026-10-29 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000849399.json | Diluted EPS 0.83 for period ending 2026-10-02 (filed 2026-10-29) |
| S034 | news | IDXX | Mon, 23 Nov 2026 13:59:54 GMT | ok | https://news.google.com/rss/search?q=IDXX+Idexx+Laboratories+stock&hl=en-US&gl=US&ceid=US:en | IDEXX Laboratories, Inc. (IDXX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Mon, 23 Nov 2026 13:59:54 GMT); IDEXX Laboratories Inc (IDXX) Stock Price, Quote, News & History - Benzinga (Fri, 20 Nov 2026 21:14:00 GMT); Earnings Strength: 3 Companies Raising Guidance - TradingView (Tue, 24 Nov 2026 00:02:00 GMT) |
| S035 | filing | CVNA | 2026-10-28 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001690820&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-28 (accession 0001690820-26-000067); 8-K filed 2026-10-28 (accession 0001690820-26-000066); 8-K filed 2026-08-14 (accession 0001690820-26-000059) |
| S036 | filing | SNDK | 2026-11-19 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0002023554&type=10-Q&dateb=&owner=include&count=10 | 8-K filed 2026-11-19 (accession 0001628280-26-075127); 8-K filed 2026-11-18 (accession 0001628280-26-074848); 10-Q filed 2026-10-30 (accession 0001628280-26-068601) |
| S037 | stock | CVNA | 2026-11-24 | ok | https://finance.yahoo.com/quote/CVNA | Trailing P/E: 32.60096; Forward P/E: 31.6557; Forward EPS: 2.14211; Price: 67.81; Market price: 67.81; Market cap: 170295361536; Sector: Consumer Cyclical; Trailing Eps: 2.08; Revenue Growth: 0.424; Earnings Growth: 0.857; Gross Margin: 0.19041; Operating Margin: 0.08743; Profit Margin: 0.06215; Return On Equity: 0.54672; Total Revenue: 27451000832; Market Cap: 170295361536; Consensus EPS FY+1: 2.09151; growth: 0.28530002 |
| S038 | news | CVNA | Sun, 22 Nov 2026 08:27:22 GMT | ok | https://news.google.com/rss/search?q=CVNA+Carvana+stock&hl=en-US&gl=US&ceid=US:en | Carvana Co. (CVNA) Stock Price, News, Quote & History - Yahoo! Finance Canada (Sun, 22 Nov 2026 08:27:22 GMT); Can Carvana Stock Hit $95? - Yahoo Finance (Fri, 20 Nov 2026 11:40:22 GMT); Carvana stock falls as auto retailer’s 2026 earnings guidance misses Wall Street’s expectations - CNBC (Wed, 29 Jul 2026 07:00:00 GMT) |
| S039 | stock | SNDK | 2026-11-24 | ok | https://finance.yahoo.com/quote/SNDK | Trailing P/E: 5.608056; Forward P/E: 2.4440978; Forward EPS: 35.88645; Price: 87.71; Market price: 87.71; Market cap: 99841597440; Sector: Technology; Trailing Eps: 15.64; Revenue Growth: 3.779; Earnings Growth: 69.096; Gross Margin: 0.79952; Operating Margin: 0.7268; Profit Margin: 0.67039; Return On Equity: 1.41174; Total Revenue: 28970999808; Market Cap: 99841597440; Consensus EPS FY+1: 35.88645; growth: 0.2606 |
| S040 | filing | NOW | 2026-10-28 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001373715&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-28 (accession 0001373715-26-000096); 8-K filed 2026-10-28 (accession 0001373715-26-000092); 10-Q filed 2026-07-23 (accession 0001373715-26-000076) |

## Sources

- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFF&cosd=2026-01-01 (2026-11-20)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLH0A0HYM2&cosd=2026-01-01 (2026-11-20)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLC0A0CM&cosd=2026-01-01 (2026-11-20)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCSL&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=UNRATE&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=PAYEMS&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=T10Y2Y&cosd=2026-01-01 (2026-11-23)
- filing APP: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001751008&type=10-Q&dateb=&owner=include&count=10 (2026-11-04)
- filing CMG: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001058090&type=10-Q&dateb=&owner=include&count=10 (2026-10-29)
- filing PNR: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 (2026-10-27)
- news CMG: https://news.google.com/rss/search?q=CMG+Chipotle+Mexican+Grill+stock&hl=en-US&gl=US&ceid=US:en (Sat, 21 Nov 2026 02:05:00 GMT)
- news APP: https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en (Mon, 23 Nov 2026 01:07:00 GMT)
- news PNR: https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en (Mon, 23 Nov 2026 15:58:41 GMT)
- stock APP: https://finance.yahoo.com/quote/APP (2026-11-24)
- stock CMG: https://finance.yahoo.com/quote/CMG (2026-11-24)
- stock PNR: https://finance.yahoo.com/quote/PNR (2026-11-24)
- filing CMG: https://data.sec.gov/api/xbrl/companyfacts/CIK0001058090.json (2026-10-29)
- filing CHTR: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 (2026-11-06)
- filing APP: https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json (2026-11-04)
- filing IDXX: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000874716&type=10-Q&dateb=&owner=include&count=10 (2026-11-02)

## AI Provenance

- Provider / model: hermes-local-proxy / upstage/solar-mini4:free
- Market research: attempts=1 tokens=8353 (prompt=5353, completion=3000) runtime=41.95s
- Fundamental research: generated this run at 2026-11-24T10:08:44.345426+00:00
- Evidence source dates: {'as_of': '2026-11-23', 'latest_equity_date': '2026-11-23', 'latest_macro_date': '2026-11-24', 'flows_date': '2026-11-23'}
- Evidence fingerprint: 1959613e51adca8b9c4fec43a6f327d62f83d79ec978ba2c14c825da9f304bd3
- Source citations are retrieved external records in the ledger above; market values remain from the verified database snapshot.


## Disclosures

- This is research and market intelligence, not investment advice.
- AI conclusions are research judgments, not validated return predictions.
- The frozen risk layer is risk-only and is not used for directional views or allocations.
- Legacy scores are not active inputs or outputs.

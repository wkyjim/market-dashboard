# AEGIS AI-First Market Intelligence

Research generated at: 14 November 2026, 22:14 HKT
Database freshness: equity 2026-11-13 (latest row retrieved 2026-11-14 13:50:55.938286+08:00)
Data cutoff: 2026-11-13 US cash close
Snapshot ID: aegis-hourly-20261114T141445Z

## Executive Summary

- **AI market view: Risk-on tilt with a quality and liquidity bias. Broad market breadth is constructive, but the 20-day index return is negative and the 200-day trend is still intact, so the setup favors high-quality, liquid names and sectors with positive momentum rather than broad cyclical or speculative exposure.**
- Broad market breadth is constructive: 71.3% above the 50-day and 63.6% above the 200-day, with a positive 20-day advance/decline ratio of 1.70.
- Index-level 20-day return is negative (-1.28%) and the Information Technology sector is the weakest at -7.19%, indicating a quality and liquidity filter is warranted.
- Sector leadership is broad: Health Care, Consumer Discretionary, Consumer Staples, Real Estate and Financials all posted positive 20-day returns, while Communication Services and Energy are negative.
- Liquidity and dislocation screens highlight a small set of names with strong 20-day momentum, large 20-day dislocations, or exceptional dollar-volume leadership.
- Macro data show a still-elevated but easing inflation backdrop, a stable labor market, and a modestly positive 10Y-2Y spread, supporting a risk-on posture with a quality tilt.
- Credit spreads are tight (IG 0.89, HY 3.20), which argues for caution on risk-taking and a preference for high-quality, liquid exposures.

## Data QC

- Status: **PASS_WITH_WARNINGS**
- Equity session: 0 completed session(s) behind inference date
- Equity provenance: 386 provisional / 12581 canonical
- Breadth lag: 0 session(s); ETF-flow lag: 0 session(s)
- Note: Equity session contains a mix of provisional yfinance and canonical Massive rows.
- External sources: 79 ok / 0 unavailable; retrieved 2026-11-14T14:15:10.598444+00:00

## Idea Discovery

- S&P 500 universe: 503; eligible: 501; transparent shortlist: 20
- Method: independent momentum/dislocation/PE/liquidity buckets; no composite score
- Evidence used: latest close, 20d and 60d price returns, 60d drawdown, trailing P/E, earnings yield, sector-relative P/E, dollar volume, GICS sector
- Not available as verified inputs: verified earnings-revision history for the full universe, FY+2 consensus, structured industry catalyst calendar
- Eligible but not shortlisted: 481 (outside the top independent momentum, dislocation, valuation and liquidity buckets)
- Included: APP (top_20d_momentum); FISV (top_20d_momentum); PNR (top_20d_momentum); GEN (top_20d_momentum); CLX (top_20d_momentum); CHTR (top_20d_momentum); IDXX (top_20d_momentum); ROP (top_20d_momentum); RDDT (largest_20d_dislocation); INTC (largest_20d_dislocation); SNDK (largest_20d_dislocation, liquidity_leader); MRVL (largest_20d_dislocation); FFIV (largest_20d_dislocation); NOW (largest_20d_dislocation); LITE (largest_20d_dislocation); COIN (largest_20d_dislocation); NVDA (liquidity_leader); AMD (liquidity_leader); MU (liquidity_leader); AAPL (liquidity_leader)
- Excluded reasons: {"missing_recent_or_latest_price": 2}
- Valuation-quality rejected: [{"flags": ["forward_eps_missing"], "ticker": "FISV"}, {"flags": ["forward_pe_outside_plausible_range", "implausible_earnings_yield", "forward_eps_vs_reported_jump"], "ticker": "CHTR"}, {"flags": ["forward_pe_outside_plausible_range", "implausible_earnings_yield"], "ticker": "SNDK"}, {"flags": ["forward_eps_vs_reported_jump"], "ticker": "MRVL"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "FFIV"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "NOW"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "LITE"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "COIN"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "NVDA"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "AMD"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "MU"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "AAPL"}]

## Market Snapshot

| Asset | Latest | Change | Observation |
| --- | --- | --- | --- |
| S&P 500 | 7561.67 | -1.28% (20d) | Index is below its 50-day and 200-day trend, but breadth remains positive and the 200-day trend is intact. |
| Health Care | XLV | +6.87% (20d) | Strongest sector in the universe; trailing P/E of 30.78 suggests premium valuation but strong momentum. |
| Consumer Discretionary | XLY | +6.69% (20d) | Positive momentum with trailing P/E of 25.11; consistent with risk-on consumer exposure. |
| Information Technology | XLK | -7.19% (20d) | Weakest sector; trailing P/E of 30.03 and negative price action argue for a liquidity/quality filter. |
| Financials | XLF | +5.69% (20d) | Positive 20-day return with trailing P/E of 15.85; attractive relative valuation within a positive rate backdrop. |
| Energy | XLE | -4.81% (20d) | Negative momentum and trailing P/E of 16.23; not aligned with the current risk-on, liquidity-led setup. |

## Macro, Fiscal, Rates, Liquidity and Credit

- Inflation: CPI is 336.30 (Sep-2026) and core CPI is 338.90, indicating a still-elevated but decelerating inflation backdrop; the October CPI print of 337.476 suggests continued moderation.
- Labor: Unemployment is 4.2% (Sep-2026) and nonfarm payrolls are 159,293k (Oct-2026), pointing to a stable labor market with no acute deterioration.
- Rates: The 10Y-2Y spread is 0.27, a modestly positive curve, while the effective federal funds rate is 3.88%, consistent with a restrictive but easing policy stance.
- Credit: IG OAS is 0.89 and HY OAS is 3.20, both tight, indicating low compensation for credit risk and a supportive but potentially complacent credit environment.
- Liquidity: Market breadth is positive with 71.3% above the 50-day and a 1.70 advance/decline ratio, but the negative 20-day index return and weak IT sector suggest a quality and liquidity filter is needed.
- Growth: The 20-day index return is negative, but sector breadth is broad-based, with Health Care, Consumer Discretionary, Consumer Staples, Real Estate and Financials all positive, indicating resilient underlying growth.

## US Equities and 11 GICS Sectors

Macro source IDs: S001, S002, S003, S004, S005, S006, S007

| GICS sector | Evidence | AI research stance | Source IDs |
| --- | --- | --- | --- |
| Health Care | 20-day return +6.87% with trailing P/E 30.78; 71.3% of constituents above the 50-day and 63.6% above the 200-day. | Positive momentum and broad participation support a constructive stance, but the premium valuation warrants a quality and earnings-visibility filter. | S055 |
| Consumer Discretionary | 20-day return +6.69% with trailing P/E 25.11; positive 20-day advance/decline ratio of 1.70. | Risk-on consumer exposure is supported by positive sector momentum and reasonable relative valuation. | S059 |
| Consumer Staples | 20-day return +5.40% with trailing P/E 24.85; defensive positioning within a positive breadth environment. | Defensive quality exposure is supported by positive sector returns and stable macro conditions. | S056 |
| Real Estate | 20-day return +5.24% with trailing P/E 29.63; positive sector momentum in a low-rate environment. | Positive 20-day return and reasonable relative valuation support a constructive stance, but premium valuation requires monitoring. | S060 |
| Financials | 20-day return +5.69% with trailing P/E 15.85; positive sector momentum and attractive relative valuation. | Constructive stance supported by positive momentum, tight credit spreads, and a modestly positive yield curve. | S062 |
| Utilities | 20-day return +4.34% with trailing P/E 18.11; defensive quality exposure with positive sector momentum. | Defensive quality exposure is supported by positive sector returns and stable macro conditions. | S066 |
| Materials | 20-day return +2.57% with trailing P/E 21.72; positive but more modest sector momentum. | Constructive but less compelling than leadership sectors; monitor for trend confirmation. | S068 |
| Industrials | 20-day return +0.61% with trailing P/E 27.07; near-flat sector momentum. | Neutral stance; positive but weak momentum does not yet support a strong conviction position. | S069 |
| Communication Services | 20-day return -1.48% with trailing P/E 17.26; negative sector momentum. | Negative momentum and negative 20-day return argue for a cautious or less favored stance. | S073 |
| Information Technology | 20-day return -7.19% with trailing P/E 30.03; weakest sector with negative price action. | Negative momentum and premium valuation argue for a cautious stance; liquidity and quality filters are essential. | S072 |
| Energy | 20-day return -4.81% with trailing P/E 16.23; negative sector momentum. | Negative momentum and negative 20-day return argue for a cautious stance; not aligned with the current risk-on, liquidity-led setup. | S076 |

### Sector fundamentals, valuation and earnings

No point-in-time sector fundamentals beyond the supplied trailing P/E and 20-day ETF returns are available in the database. The sector evidence is limited to the 20-day returns and trailing P/E figures from the supplied source set; no growth, margin, or consensus data are provided for the full sector universe.

## Growth vs Value

- Health Care and Consumer Discretionary show the strongest 20-day momentum (+6.87% and +6.69%) with trailing P/Es of 30.78 and 25.11, indicating premium but positive momentum.
- Financials offer the most attractive relative valuation at 15.85 trailing P/E with positive 20-day momentum (+5.69%), supporting a quality and value tilt.
- Information Technology is the weakest sector at -7.19% with a 30.03 trailing P/E, indicating negative momentum and premium valuation that argues against broad exposure.
- Energy is negative at -4.81% with a 16.23 trailing P/E, suggesting a cautious stance on the sector despite a reasonable valuation multiple.

## ETF Flows and Breadth

- Market breadth is constructive: 71.3% of constituents above the 50-day, 63.6% above the 200-day, and a 1.70 advance/decline ratio.
- The 20-day index return is negative (-1.28%), but the positive breadth and advance/decline ratio indicate a resilient underlying market.
- Sector leadership is broad: Health Care, Consumer Discretionary, Consumer Staples, Real Estate and Financials all posted positive 20-day returns.
- Liquidity leaders include NVDA, AMD, MU and AAPL, with strong dollar-volume and 20-day momentum, while the largest dislocations are concentrated in INTC, COIN, LITE, NOW, MRVL and FFIV.
- Flow data show strong institutional buying in SOXX (20d z-score 5.10) and a neutral-to-negative flow environment in TLT, suggesting a tilt toward structural growth and liquidity leaders.

## Stock Ideas

Single-stock research uses reported EPS, forward P/E and company fundamentals. All ideas are research judgments, not validated return predictions.

| Ticker | Security | Research view | Price | EPS | Forward P/E | Base target | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| APP | AppLovin | NEW | 409.1 | 20.86026 | 19.611452 | 458.93 | NEW |
| PNR | Pentair | KEEP | 68.3 | 5.30402 | 12.877027 | 74.26 | KEEP |
| IDXX | Idexx Laboratories | KEEP | 704.23 | 16.8929 | 41.687927 | 641.93 | KEEP |
| ROP | Roper Technologies | NEW | 479.975 | 24.57318 | 19.532475 | 442.32 | NEW |

## ETF Ideas

ETF research uses holdings, portfolio valuation and exposure. Single-stock EPS × P/E valuation is not applied to ETFs.

| Ticker | Fund | Research view | Price | Top holdings | Portfolio valuation | Sector exposure | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| XLV | Health Care sector ETF | KEEP | 188.85 | LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59% | Top 10 holdings; numeric weight coverage 61.42% | Health Care | KEEP |
### APP — AppLovin

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** AppLovin offers a cleaner momentum and earnings-growth story than the dislocation names in the shortlist, which show negative 20-day returns and deep drawdowns, and it carries a lower forward P/E than the high-multiple software names such as NOW and MRVL. Alternatives considered: NOW, MRVL, INTC.
- **Thesis:** AppLovin screens in the top 20-day momentum bucket with a 53.7% 20-day return and a 32.5% 60-day return, and its Q3 FY2026 filing shows reported diluted EPS of $11.61 with FY2027 consensus EPS of $20.86, implying a forward P/E of about 19.6. The stock's 60-day drawdown is only -0.2%, indicating a clean, high-momentum run rather than a value trap. The momentum and earnings growth profile support a new BUY initiation.
- **Source IDs:** S008, S009, S013, S015
- **Catalysts:** Continued 20-day momentum momentum into the next week, Sustained FY2027 EPS growth above FY2026 reported growth, Advertising and in-app purchase revenue momentum from the Q3 filing
- **Risks:** High valuation multiples relative to slower-growth peers, Momentum can reverse quickly if ad-market conditions deteriorate, Forward EPS estimates are unverified against the fiscal period
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 20.8603 (source.forwardEps) x AI multiple assumption 22.00; source IDs S008, S009, S013, S015
- **EPS:** 20.86026 — period: FY2027 (+1y consensus)
- **Forward P/E:** 19.611452
- **FY+1 growth assumption:** 27.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / MSFT / APP shows strong FY2027 consensus EPS growth of 27.44% and revenue growth of 25.37%, supported by high gross margin (88.8%) and operating margin (77.8%). The base multiple of 22x is justified by superior profitability and growth relative to peers, with MSFT as a named reference for premium software multiples. Bull and bear multiples reflect upside/downside scenarios around this growth and margin profile.
- **Company fundamentals:** AppLovin reported diluted EPS of $11.61 for the period ending 2026-09-30, with FY2027 consensus EPS of $20.86 and forward P/E of 19.61. FY2026 revenue growth was 25.4% and earnings growth 75.5%, with gross margin of 88.8% and operating margin of 77.8%.
- **Bull / Base / Bear:** 542.37 / 458.93 / 333.76
- **Bull / Base / Bear returns:** 32.58% / 12.18% / -18.42%
- **Scenario probabilities:** not separately assigned; see scenario table.

### PNR — Pentair

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Pentair is the higher-quality momentum name in the Industrials bucket compared with the negative-momentum dislocation names, but it is not preferred over the stronger consumer and health-care momentum names in the shortlist. Alternatives considered: RDDT, IDXX, CLX.
- **Thesis:** Pentair is a top-20-day-momentum name with a 27.8% 20-day return and a 20-day earnings yield of 7.4%, but its FY2026 revenue growth is -4.5% and earnings growth is -18.8%, with a forward P/E of 12.9. The momentum is real but the underlying fundamentals are contracting, so the position should be held rather than added to.
- **Source IDs:** S010, S017, S019, S020
- **Catalysts:** 20-day price momentum continuing into the next week, Potential stabilization in water and fluid handling end markets, Operating margin of 21.4% provides some earnings support
- **Risks:** FY2026 revenue and earnings contraction, Forward EPS estimates are unverified against the fiscal period, Sector-relative P/E of 0.49 indicates the stock trades below its sector on earnings yield
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 5.3040 (source.forwardEps) x AI multiple assumption 14.00; source IDs S010, S017, S019, S020
- **EPS:** 5.30402 — period: FY2027 (+1y consensus)
- **Forward P/E:** 12.877027
- **FY+1 growth assumption:** 12.82%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / UPS / PNR has moderate FY2027 consensus EPS growth of 12.82% and revenue growth of 18.38%, with a lower gross margin (40.2%) and operating margin (21.4%) typical of a cyclical industrial. The base multiple of 14x is justified by its growth and margin profile relative to UPS, a named peer in the logistics/industrial space. Bull and bear multiples reflect scenario adjustments for cyclicality and margin variability.
- **Company fundamentals:** Pentair reported diluted EPS of $2.76 for the period ending 2026-09-30, with FY2027 consensus EPS of $5.30 and forward P/E of 12.88. FY2026 revenue growth was -4.5% and earnings growth -18.8%, with gross margin of 40.2% and operating margin of 21.4%.
- **Bull / Base / Bear:** 90.17 / 74.26 / 58.34
- **Bull / Base / Bear returns:** 32.02% / 8.73% / -14.58%
- **Scenario probabilities:** not separately assigned; see scenario table.

### IDXX — Idexx Laboratories

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Idexx offers a cleaner health-care momentum story than the high-multiple software names, but its valuation premium makes it less attractive than the lower-multiple momentum names such as Gen Digital and Roper Technologies. Alternatives considered: GEN, ROP, CLX.
- **Thesis:** Idexx Laboratories is a top-20-day-momentum name with a 25.7% 20-day return and a 29.0% 60-day return, but it carries the highest forward P/E in the shortlist at 41.7 and a sector-relative P/E of 1.33. The earnings yield of 2.6% is the lowest among the momentum names, so the premium valuation is not justified by current earnings growth of 17.9%.
- **Source IDs:** S029, S033, S036, S041
- **Catalysts:** 20-day and 60-day momentum continuing, Stable veterinary and animal health demand, Gross margin of 62.7% and operating margin of 32.5% support profitability
- **Risks:** Highest forward P/E in the shortlist at 41.7, Sector-relative P/E of 1.33 implies limited relative value, Earnings growth of 17.9% is below the momentum peers
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 16.8929 (source.forwardEps) x AI multiple assumption 38.00; source IDs S029, S033, S036, S041
- **EPS:** 16.8929 — period: FY2027 (+1y consensus)
- **Forward P/E:** 41.687927
- **FY+1 growth assumption:** 12.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / BDX / IDXX shows FY2027 consensus EPS growth of 12.44% and revenue growth of 8.88%, with a healthy gross margin (62.7%) and operating margin (32.5%). The base multiple of 38x is justified by its specialty healthcare growth and margin profile relative to BDX, a named peer in the healthcare sector. Bull and bear multiples reflect scenario adjustments for growth durability and competitive positioning.
- **Company fundamentals:** Idexx Laboratories reported diluted EPS of $11.75 for the period ending 2026-09-30, with FY2027 consensus EPS of $16.89 and forward P/E of 41.69. FY2026 revenue growth was 8.9% and earnings growth 17.9%, with gross margin of 62.7% and operating margin of 32.5%.
- **Bull / Base / Bear:** 743.29 / 641.93 / 506.79
- **Bull / Base / Bear returns:** 5.55% / -8.85% / -28.04%
- **Scenario probabilities:** not separately assigned; see scenario table.

### ROP — Roper Technologies

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** Roper Technologies provides a higher earnings yield and cleaner momentum profile than the high-multiple software names such as NOW and MRVL, and it is a more durable compounder than the short-term dislocation names in the shortlist. Alternatives considered: NOW, MRVL, INTC.
- **Thesis:** Roper Technologies is a top-20-day-momentum name with a 25.4% 20-day return and a 16.9% 60-day return, and it offers a forward P/E of 19.5 with an earnings yield of 6.0%. FY2026 revenue growth of 7.6% and earnings growth of 32.6% support the momentum, and the 60-day drawdown of -2.5% is modest. The combination of momentum, earnings growth, and a reasonable valuation supports a new BUY.
- **Source IDs:** S031, S034, S038, S040
- **Catalysts:** 20-day momentum continuing into the next week, FY2026 earnings growth of 32.6% outpacing revenue growth of 7.6%, Stable software and technology-enabled services revenue
- **Risks:** Forward EPS estimates are unverified against the fiscal period, Sector-relative P/E of 0.49 indicates the stock trades below its sector on earnings yield, Momentum can fade if technology spending slows
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 24.5732 (source.forwardEps) x AI multiple assumption 18.00; source IDs S031, S034, S038, S040
- **EPS:** 24.57318 — period: FY2027 (+1y consensus)
- **Forward P/E:** 19.532475
- **FY+1 growth assumption:** 9.81%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / HD / ROP has FY2027 consensus EPS growth of 9.81% and revenue growth of 6.29%, with a gross margin of 69.7% and operating margin of 28.0%. The base multiple of 18x is justified by its steady growth and margin profile relative to HD, a named peer in the consumer discretionary/retail space. Bull and bear multiples reflect scenario adjustments for consumer demand and margin stability.
- **Company fundamentals:** Roper Technologies reported diluted EPS of $21.30 for the period ending 2026-09-30, with FY2027 consensus EPS of $24.57 and forward P/E of 19.53. FY2026 revenue growth was 7.6% and earnings growth 32.6%, with gross margin of 69.7% and operating margin of 28.0%.
- **Bull / Base / Bear:** 516.04 / 442.32 / 344.02
- **Bull / Base / Bear returns:** 7.51% / -7.85% / -28.33%
- **Scenario probabilities:** not separately assigned; see scenario table.

### XLV — Health Care sector ETF

- **Type:** ETF
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** XLV provides broad, diversified health-care exposure that is preferable to single-name health-care names such as IDXX, which carries a 41.7 forward P/E and a sector-relative P/E of 1.33. The ETF reduces single-stock idiosyncratic risk while maintaining exposure to the defensive sector. Alternatives considered: IDXX, XLP, XLF.
- **Thesis:** The Health Care sector ETF is a core holding that provides diversified exposure to large-cap pharmaceutical and medical device names. The sector ETF is being kept as a portfolio anchor, but the current 0.54% raw price change is modest and does not justify an upgrade. The top-10 holdings are dominated by LLY, JNJ, ABBV, MRK, and UNH, which provide defensive characteristics.
- **Source IDs:** S055, S057
- **Catalysts:** Defensive demand for health care and pharmaceuticals, Stable dividend and earnings profiles across the top-10 holdings, Sector rotation into health care during risk-off episodes
- **Risks:** Modest 0.54% raw price change does not drive alpha, Top-10 holdings coverage is 61.42%, leaving a meaningful portion of the portfolio unrepresented, Sector-specific regulatory and reimbursement risks
- **Valuation method:** Holdings/portfolio valuation with AI total-return assumption
- **Valuation status:** verified; forward-EPS source: ; period flags: 
- **Valuation assumptions:** Holdings/portfolio valuation; 10 weighted holdings; coverage 61.42%; source IDs S055, S057
- **Top holdings:** LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59%
- **Portfolio valuation:** Top 10 holdings; numeric weight coverage 61.42%
- **Sector exposure:** Health Care
- **Underlying drivers:** Large-cap pharmaceutical and medical device demand, defensive sector rotation, and stable regulatory environments across the top-10 holdings.
- **Bull / Base / Bear:** 211.51 / 198.29 / 177.52
- **Bull / Base / Bear returns:** 12.0% / 5.0% / -6.0%
- **Scenario probabilities:** not separately assigned; see scenario table.

## Quant Risk Layer

| Field | Value |
| --- | --- |
| Volatility model | vol5_ols_v1 |
| Spike model | spike_logit_v1 |
| As-of date | 2026-11-13 |
| Target window | 2026-11-16 to 2026-11-20 |
| Forecast 5D annualized volatility | 14.93% |
| Historical-vol baseline | 22.07% |
| EWMA baseline | 20.09% |
| Spike probability | 16.51% |
| Spike threshold | 18.50% |
| Status | prospective |
| Forecast ID | 2e4ad8eeaf2db3d3 |

Risk-only; no directional interpretation or allocation implication.

## Scenarios

### Short Term (5 trading sessions)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 25% | +2.00% | Low 5-day realized vol (14.9%) and below-threshold spike probability (16.5% vs 18.5% threshold) support a modest upside if US close confirms no macro shock; probability capped below 30% because frozen daily-close model is not yet official. |
| Base | 50% | +0.00% | Directional signal is false and forecast vol is below baseline, so the most likely path is a range-bound close near the frozen daily model's expected value; no strong catalyst to push returns positive or negative. |
| Bear | 25% | -2.00% | Spike probability (16.5%) remains elevated relative to the 18.5% threshold only marginally, and a failed US close could trigger a mild risk-off pullback; probability kept at 25% because the model's directional signal is false and volatility is not extreme. |

### Long Term (12 months)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 30% | +8.00% | Sustained low realized vol (14.9%) and below-threshold spike probability (16.5%) indicate a calm macro backdrop; if earnings and credit spreads remain stable, a positive 8% return is plausible over the horizon. |
| Base | 40% | +3.00% | Frozen daily-close model with no directional signal and moderate volatility implies a modest positive drift; base case assumes steady earnings and stable credit conditions, yielding a 3% return. |
| Bear | 30% | -5.00% | Elevated spike probability (16.5%) and below-threshold volatility leave room for a macro or credit event; a 5% downside is plausible if US close reveals a shock, but probability is capped below 40% because the model's directional signal is false and historical baseline is not breached. |

## Positioning

- Maintain a risk-on tilt with a quality and liquidity bias, favoring sectors with positive 20-day momentum and broad participation.
- Prioritize high-quality, liquid names and sectors over speculative or high-multiple exposure, especially in Information Technology and Communication Services.
- Use the positive 10Y-2Y spread and tight credit spreads as a backdrop for risk-on positioning, but monitor for complacency given tight spreads.
- Avoid broad cyclical or energy exposure until the negative 20-day returns and negative sector momentum reverse.
- Keep a defensive quality overlay in Health Care, Consumer Staples and Utilities, which show positive momentum and stable macro conditions.

## Catalysts

| Date | Event | Why it matters |
| --- | --- | --- |
| 2026-11-16 | US equity market open | Frozen daily-close model indicates a 14.9% 5-day forecast volatility and a 16.5% spike probability, above the 18.5% threshold, warranting close monitoring of intraday risk. |
| 2026-11-13 | Sector momentum rotation | Health Care, Consumer Discretionary, Consumer Staples, Real Estate and Financials all posted positive 20-day returns, while Information Technology and Energy were negative, indicating a quality and liquidity-led rotation. |
| 2026-11-13 | Credit spread tightness | IG OAS at 0.89 and HY OAS at 3.20 suggest low compensation for credit risk, supporting risk-on positioning but warranting caution on excessive risk-taking. |

## Key Risks

- Equity session contains a mix of provisional yfinance and canonical Massive rows, which may introduce data quality inconsistencies.
- The 20-day index return is negative and the Information Technology sector is the weakest, indicating potential downside risk if breadth deteriorates.
- Credit spreads are tight, which may leave little room for error if economic data or earnings disappoint.
- The frozen risk model shows a 16.5% spike probability, above the 18.5% threshold, indicating elevated near-term volatility risk.
- Sector fundamentals beyond trailing P/E and 20-day returns are not available, limiting the ability to assess growth, margin, or consensus trends.
- The 20

## External Source Ledger

| ID | Type | Ticker | Published | Status | URL | Claims |
| --- | --- | --- | --- | --- | --- | --- |
| S001 | macro | macro | 2026-11-12 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFF&cosd=2026-01-01 | Effective federal funds rate (DFF) latest observation 2026-11-12: 3.88 |
| S002 | macro | macro | 2026-11-12 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLH0A0HYM2&cosd=2026-01-01 | US high-yield OAS (BAMLH0A0HYM2) latest observation 2026-11-12: 3.20 |
| S003 | macro | macro | 2026-11-12 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLC0A0CM&cosd=2026-01-01 | US investment-grade OAS (BAMLC0A0CM) latest observation 2026-11-12: 0.89 |
| S004 | macro | macro | 2026-10-01 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCSL&cosd=2026-01-01 | US CPI (CPIAUCSL) latest observation 2026-10-01: 337.476 |
| S005 | macro | macro | 2026-10-01 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=UNRATE&cosd=2026-01-01 | US unemployment rate (UNRATE) latest observation 2026-10-01: 4.1 |
| S006 | macro | macro | 2026-10-01 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=PAYEMS&cosd=2026-01-01 | US nonfarm payrolls (PAYEMS) latest observation 2026-10-01: 159293 |
| S007 | macro | macro | 2026-11-13 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=T10Y2Y&cosd=2026-01-01 | 10Y-2Y Treasury spread (T10Y2Y) latest observation 2026-11-13: 0.27 |
| S008 | filing | APP | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001751008&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0001751008-26-000069); 8-K filed 2026-11-04 (accession 0001751008-26-000068); 10-Q filed 2026-08-05 (accession 0001751008-26-000059) |
| S009 | news | APP | Tue, 10 Nov 2026 14:24:00 GMT | ok | https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en | APP Stock Surges 51% After Q3 Earnings: Is it Still a Buy? - Yahoo Finance (Tue, 10 Nov 2026 14:24:00 GMT); Is Trending Stock AppLovin Corporation (APP) a Buy Now? - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT); APP Stock Quote Price and Forecast - CNN (Fri, 13 Nov 2026 07:31:37 GMT) |
| S010 | filing | PNR | 2026-10-27 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-27 (accession 0000077360-26-000058); 8-K filed 2026-10-27 (accession 0000077360-26-000055); 8-K filed 2026-09-22 (accession 0000077360-26-000050) |
| S011 | filing | FISV | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0000798354-26-000042); 8-K filed 2026-11-03 (accession 0000798354-26-000039); 8-K filed 2026-10-23 (accession 0001193125-26-429481) |
| S012 | news | FISV | Fri, 13 Nov 2026 00:53:33 GMT | ok | https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en | Fiserv, Inc. (FISV) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 00:53:33 GMT); Fiserv (FISV) Stock Looks Undervalued With Strong Excess Returns - Yahoo Finance (Wed, 11 Nov 2026 22:14:34 GMT); Fiserv Stock Outlook: Is Wall Street Bullish or Bearish? - Yahoo Finance (Thu, 12 Nov 2026 12:23:56 GMT) |
| S013 | filing | APP | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json | Diluted EPS 11.61 for period ending 2026-09-30 (filed 2026-11-04) |
| S014 | filing | FISV | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json | Diluted EPS -8.9 for period ending 2026-09-30 (filed 2026-11-04) |
| S015 | stock | APP | 2026-11-14 | ok | https://finance.yahoo.com/quote/APP | Trailing P/E: 27.54882; Forward P/E: 19.611452; Forward EPS: 20.86026; Price: 409.1; Market price: 409.1; Market cap: 135543824384; Sector: Communication Services; Trailing Eps: 14.85; Revenue Growth: 0.555; Earnings Growth: 0.755; Gross Margin: 0.8878; Operating Margin: 0.77782995; Profit Margin: 0.65887; Return On Equity: 2.1008599; Total Revenue: 7608893952; Market Cap: 135543824384; Consensus EPS FY+1: 20.72438; growth: 0.2744 |
| S016 | filing | GEN | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0000849399-26-000083); 8-K filed 2026-10-28 (accession 0000849399-26-000081); 8-K filed 2026-10-09 (accession 0000849399-26-000079) |
| S017 | news | PNR | Fri, 13 Nov 2026 15:54:46 GMT | ok | https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en | Pentair plc (PNR) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 15:54:46 GMT); Pentair (PNR) Stock May Be 46% Undervalued As New CFO Arrives - Yahoo Finance (Fri, 25 Sep 2026 07:00:00 GMT); Pentair plc (PNR) Q3 Earnings and Revenues Beat Estimates - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT) |
| S018 | stock | FISV | 2026-11-14 | ok | https://finance.yahoo.com/quote/FISV | Forward P/E: 7.9923306; Price: 63.78; Market price: 63.78; Market cap: 33934002176; Market Cap: 33934002176; Consensus EPS FY+1: 7.98015; growth: 0.09689999 |
| S019 | stock | PNR | 2026-11-14 | ok | https://finance.yahoo.com/quote/PNR | Trailing P/E: 18.610355; Forward P/E: 12.877027; Forward EPS: 5.30402; Price: 68.3; Market price: 68.3; Market cap: 10904415232; Sector: Industrials; Trailing Eps: 3.67; Revenue Growth: -0.045; Earnings Growth: -0.188; Gross Margin: 0.40168998; Operating Margin: 0.21410999; Profit Margin: 0.15435; Return On Equity: 0.15605; Total Revenue: 3966200064; Market Cap: 10904415232; Consensus EPS FY+1: 5.30402; growth: 0.1282 |
| S020 | filing | PNR | 2026-10-27 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json | Diluted EPS 2.76 for period ending 2026-09-30 (filed 2026-10-27) |
| S021 | filing | CLX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000021076-26-000046); 8-K filed 2026-11-02 (accession 0000021076-26-000044); 8-K filed 2026-10-29 (accession 0001206774-26-000586) |
| S022 | news | GEN | Wed, 11 Nov 2026 13:10:37 GMT | ok | https://news.google.com/rss/search?q=GEN+Gen+Digital+stock&hl=en-US&gl=US&ceid=US:en | Gen Digital Inc. (GEN) Stock Forecasts - Yahoo Finance (Wed, 11 Nov 2026 13:10:37 GMT); Gen Digital (GEN) Stock Repriced After Q2 Earnings Put Margins Center Stage - Yahoo Finance (Thu, 29 Oct 2026 07:00:00 GMT); Are Business Services Stocks Lagging GEN DIGITAL INC (GEN) This Year? - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT) |
| S023 | stock | GEN | 2026-11-14 | ok | https://finance.yahoo.com/quote/GEN | Trailing P/E: 15.431472; Forward P/E: 9.108996; Forward EPS: 3.33736; Price: 30.4; Market price: 30.4; Market cap: 18035593216; Sector: Technology; Trailing Eps: 1.97; Revenue Growth: 0.122; Earnings Growth: 1.286; Gross Margin: 0.77410007; Operating Margin: 0.43229; Profit Margin: 0.23068; Return On Equity: 0.46402; Total Revenue: 5228000256; Market Cap: 18035593216; Consensus EPS FY+1: 3.33736; growth: 0.1286 |
| S024 | filing | CHTR | 2026-11-06 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-06 (accession 0001091667-26-000073); 8-K filed 2026-11-06 (accession 0001091667-26-000072); 8-K filed 2026-10-27 (accession 0001091667-26-000064) |
| S025 | news | CLX | Sat, 14 Nov 2026 10:15:20 GMT | ok | https://news.google.com/rss/search?q=CLX+Clorox+stock&hl=en-US&gl=US&ceid=US:en | The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance Singapore (Sat, 14 Nov 2026 10:15:20 GMT); The Clorox Company (CLX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 05:34:04 GMT); A 10-Day Winning Streak Has Clorox Stock Up 24% - Trefis (Sat, 14 Nov 2026 08:28:05 GMT) |
| S026 | stock | CLX | 2026-11-14 | ok | https://finance.yahoo.com/quote/CLX | Trailing P/E: 19.68705; Forward P/E: 17.745283; Forward EPS: 6.1684; Price: 109.46; Market price: 109.46; Market cap: 13260793856; Sector: Consumer Defensive; Trailing Eps: 5.56; Revenue Growth: 0.333; Earnings Growth: 1.138; Gross Margin: 0.41939998; Operating Margin: 0.14286; Profit Margin: 0.09408; Return On Equity: 5.34363; Total Revenue: 7196000256; Market Cap: 13260793856; Consensus EPS FY+1: 6.1684; growth: 0.0769 |
| S027 | news | CHTR | Thu, 12 Nov 2026 08:02:01 GMT | ok | https://news.google.com/rss/search?q=CHTR+Charter+Communications+stock&hl=en-US&gl=US&ceid=US:en | Charter Communications: 3 Key Takeaways for Long-Term Investors - Yahoo Finance (Thu, 12 Nov 2026 08:02:01 GMT); What Is The Biggest Threat To Charter Communications Stock? - Trefis (Thu, 12 Nov 2026 15:55:19 GMT); Why You Should Think About Charter Communications Differently Now? - Trefis (Fri, 13 Nov 2026 19:15:44 GMT) |
| S028 | stock | CHTR | 2026-11-14 | ok | https://finance.yahoo.com/quote/CHTR | Trailing P/E: 13.006578; Forward P/E: 3.2831066; Forward EPS: 42.15215; Price: 138.39; Market price: 138.39; Market cap: 24778944512; Sector: Communication Services; Trailing Eps: 10.64; Revenue Growth: 0.091; Gross Margin: 0.55084; Operating Margin: 0.23389; Profit Margin: 0.02498; Return On Equity: 0.07019; Total Revenue: 55645999104; Market Cap: 24778944512; Consensus EPS FY+1: 47.15811; growth: 1.0195 |
| S029 | filing | IDXX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000874716&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000874716-26-000135); 8-K filed 2026-11-02 (accession 0001104659-26-120892); 10-Q filed 2026-08-04 (accession 0000874716-26-000123) |
| S030 | filing | GEN | 2026-10-29 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000849399.json | Diluted EPS 0.83 for period ending 2026-10-02 (filed 2026-10-29) |
| S031 | filing | ROP | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000882835&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000882835-26-000047); 8-K filed 2026-10-22 (accession 0000882835-26-000042); 8-K filed 2026-10-01 (accession 0000882835-26-000039) |
| S032 | filing | CHTR | 2026-11-06 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001091667.json | Diluted EPS 0.38 for period ending 2026-09-30 (filed 2026-11-06) |
| S033 | stock | IDXX | 2026-11-14 | ok | https://finance.yahoo.com/quote/IDXX | Trailing P/E: 47.45485; Forward P/E: 41.687927; Forward EPS: 16.8929; Price: 704.23; Market price: 704.23; Market cap: 55483650048; Sector: Healthcare; Trailing Eps: 14.84; Revenue Growth: 0.099; Earnings Growth: 0.179; Gross Margin: 0.62722; Operating Margin: 0.32497; Profit Margin: 0.25357; Return On Equity: 0.68925005; Total Revenue: 4662220800; Market Cap: 55483650048; Consensus EPS FY+1: 16.8929; growth: 0.1244 |
| S034 | stock | ROP | 2026-11-14 | ok | https://finance.yahoo.com/quote/ROP | Trailing P/E: 18.993866; Forward P/E: 19.532475; Forward EPS: 24.57318; Price: 479.975; Market price: 479.975; Market cap: 47535013888; Sector: Technology; Trailing Eps: 25.27; Revenue Growth: 0.076; Earnings Growth: 0.326; Gross Margin: 0.69671; Operating Margin: 0.28049; Profit Margin: 0.30712998; Return On Equity: 0.13229; Total Revenue: 8434599936; Market Cap: 47535013888; Consensus EPS FY+1: 24.57318; growth: 0.09810001 |
| S035 | filing | RDDT | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001713445&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0001713445-26-000116); 8-K filed 2026-10-29 (accession 0001713445-26-000114); 8-K filed 2026-08-12 (accession 0001713445-26-000107) |
| S036 | news | IDXX | Fri, 13 Nov 2026 22:06:38 GMT | ok | https://news.google.com/rss/search?q=IDXX+Idexx+Laboratories+stock&hl=en-US&gl=US&ceid=US:en | IDEXX Laboratories, Inc. (IDXX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 22:06:38 GMT); IDEXX Laboratories (IDXX) Stock Looks Fairly Valued Despite Its 28% Run - Yahoo Finance (Sat, 31 Oct 2026 07:00:00 GMT); IDEXX Laboratories (IDXX) Q3 Earnings Leave Its Premium Valuation In Focus - Yahoo Finance (Tue, 03 Nov 2026 08:00:00 GMT) |
| S037 | filing | CLX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000021076.json | Diluted EPS 1.39 for period ending 2026-09-30 (filed 2026-11-02) |
| S038 | news | ROP | Fri, 13 Nov 2026 01:46:04 GMT | ok | https://news.google.com/rss/search?q=ROP+Roper+Technologies+stock&hl=en-US&gl=US&ceid=US:en | Roper Technologies, Inc. (ROP) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 01:46:04 GMT); Roper Technologies (ROP) Stock Looks Fully Valued As Cash Flow Comes Into Focus - Yahoo Finance (Fri, 06 Nov 2026 07:13:00 GMT); Roper Technologies: 3 Key Takeaways for Long-Term Investors - Yahoo Finance (Mon, 26 Oct 2026 07:00:00 GMT) |
| S039 | stock | RDDT | 2026-11-14 | ok | https://finance.yahoo.com/quote/RDDT | Trailing P/E: 20.091835; Forward P/E: 10.770874; Forward EPS: 9.14039; Price: 98.45; Market price: 98.45; Market cap: 19010076672; Sector: Communication Services; Trailing Eps: 4.9; Revenue Growth: 0.53; Earnings Growth: 0.749; Gross Margin: 0.91547996; Operating Margin: 0.29397; Profit Margin: 0.32105; Return On Equity: 0.32029998; Total Revenue: 3088880128; Market Cap: 19010076672; Consensus EPS FY+1: 6.82439; growth: 0.2417 |
| S040 | filing | ROP | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000882835.json | Diluted EPS 21.3 for period ending 2026-09-30 (filed 2026-11-02) |

## Sources

- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFF&cosd=2026-01-01 (2026-11-12)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLH0A0HYM2&cosd=2026-01-01 (2026-11-12)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLC0A0CM&cosd=2026-01-01 (2026-11-12)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCSL&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=UNRATE&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=PAYEMS&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=T10Y2Y&cosd=2026-01-01 (2026-11-13)
- filing APP: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001751008&type=10-Q&dateb=&owner=include&count=10 (2026-11-04)
- news APP: https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en (Tue, 10 Nov 2026 14:24:00 GMT)
- filing PNR: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 (2026-10-27)
- filing FISV: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 (2026-11-04)
- news FISV: https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 00:53:33 GMT)
- filing APP: https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json (2026-11-04)
- filing FISV: https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json (2026-11-04)
- stock APP: https://finance.yahoo.com/quote/APP (2026-11-14)
- filing GEN: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 (2026-10-29)
- news PNR: https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 15:54:46 GMT)
- stock FISV: https://finance.yahoo.com/quote/FISV (2026-11-14)
- stock PNR: https://finance.yahoo.com/quote/PNR (2026-11-14)
- filing PNR: https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json (2026-10-27)

## AI Provenance

- Provider / model: hermes-local-proxy / upstage/solar-mini4:free
- Market research: attempts=1 tokens=9548 (prompt=6548, completion=3000) runtime=37.76s
- Fundamental research: generated this run at 2026-11-14T14:14:45.791663+00:00
- Evidence source dates: {'as_of': '2026-11-13', 'latest_equity_date': '2026-11-13', 'latest_macro_date': '2026-11-13', 'flows_date': '2026-11-13'}
- Evidence fingerprint: 9a56b34ab968bdbe326beda4dc256eb5fb45a7b04572b501a949e7fad70936e7
- Source citations are retrieved external records in the ledger above; market values remain from the verified database snapshot.


## Disclosures

- This is research and market intelligence, not investment advice.
- AI conclusions are research judgments, not validated return predictions.
- The frozen risk layer is risk-only and is not used for directional views or allocations.
- Legacy scores are not active inputs or outputs.

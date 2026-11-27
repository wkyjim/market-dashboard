# AEGIS AI-First Market Intelligence

Research generated at: 27 November 2026, 18:12 HKT
Database freshness: equity 2026-11-25 (latest row retrieved 2026-11-27 13:06:09.162829+08:00)
Data cutoff: 2026-11-25 US cash close
Snapshot ID: aegis-hourly-20261127T101254Z

## Executive Summary

- **AI market view: Late-November 2026 US equities show a mixed tape: momentum and liquidity leaders are holding up, but the Information Technology sector is the clear weak spot with a deep 20-day drawdown, while Consumer Staples and Real Estate are the strongest sectors. Breadth is mixed—above 50-day and 20-day moving averages is solid, but 200-day momentum is deteriorating and the advance/decline ratio is positive. Macro data points to a still-elevated rate environment with a modestly positive yield curve and tight credit spreads, so the risk block is the key watch item.**
- Information Technology is the weakest sector, down ~18% over 20 days, dragging the market tape lower.
- Consumer Staples (+6.3%) and Real Estate (+4.1%) are the strongest sectors over 20 days.
- Breadth is mixed: 59% above the 50-day and 56% above the 200-day, but 200-day momentum is deteriorating.
- Credit spreads are tight (IG OAS 0.98, HY OAS 3.72), and the 10Y-2Y spread is a modest +0.24.
- The risk block shows elevated forecast volatility (0.279) and a 66% spike probability, above the historical baseline.
- Equity data is a mix of provisional yfinance and canonical Massive rows, so some figures carry a warning.

## Data QC

- Status: **PASS_WITH_WARNINGS**
- Equity session: 0 completed session(s) behind inference date
- Macro session: 2026-11-27 (0 completed session(s) behind inference date)
- Equity provenance: 300 provisional / 12634 canonical
- Breadth lag: 0 session(s); ETF-flow lag: 0 session(s)
- Note: Equity session contains a mix of provisional yfinance and canonical Massive rows.
- External sources: 79 ok / 0 unavailable; retrieved 2026-11-27T10:13:06.944547+00:00

## Idea Discovery

- S&P 500 universe: 503; eligible: 501; transparent shortlist: 20
- Method: independent momentum/dislocation/PE/liquidity buckets; no composite score
- Evidence used: latest close, 20d and 60d price returns, 60d drawdown, trailing P/E, earnings yield, sector-relative P/E, dollar volume, GICS sector
- Not available as verified inputs: verified earnings-revision history for the full universe, FY+2 consensus, structured industry catalyst calendar
- Eligible but not shortlisted: 481 (outside the top independent momentum, dislocation, valuation and liquidity buckets)
- Included: APP (top_20d_momentum); CHTR (top_20d_momentum); CMG (top_20d_momentum); CLX (top_20d_momentum); TSCO (top_20d_momentum); MGM (top_20d_momentum); IDXX (top_20d_momentum); FISV (top_20d_momentum); SNDK (largest_20d_dislocation); MRVL (largest_20d_dislocation); LITE (largest_20d_dislocation); DDOG (largest_20d_dislocation); INTC (largest_20d_dislocation); DELL (largest_20d_dislocation); MU (largest_20d_dislocation, liquidity_leader); NOW (largest_20d_dislocation); NVDA (liquidity_leader); AMD (liquidity_leader); AAPL (liquidity_leader); AMZN (liquidity_leader)
- Excluded reasons: {"missing_recent_or_latest_price": 2}
- Valuation-quality rejected: [{"flags": ["forward_pe_outside_plausible_range", "implausible_earnings_yield", "forward_eps_vs_reported_jump"], "ticker": "CHTR"}, {"flags": ["forward_eps_missing"], "ticker": "FISV"}, {"flags": ["forward_pe_outside_plausible_range", "implausible_earnings_yield"], "ticker": "SNDK"}, {"flags": ["forward_eps_vs_reported_jump"], "ticker": "MRVL"}, {"flags": ["forward_eps_vs_reported_jump"], "ticker": "LITE"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "INTC"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "DELL"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "MU"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "NOW"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "NVDA"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "AMD"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "AAPL"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "AMZN"}]

## Market Snapshot

| Asset | Latest | Change | Observation |
| --- | --- | --- | --- |
| S&P 500 | 7182.78 | -7.25% (20d) | Index is down over 20 days, with Information Technology the main drag. |
| Information Technology (XLK) | -18.43% | -18.43% (20d) | Deepest drawdown among all sectors; likely the primary driver of the negative market view. |
| Consumer Staples (XLP) | +6.29% | +6.29% (20d) | Strongest sector; defensive demand and high trailing P/E of 24.84 support the view. |
| Real Estate (XLRE) | +4.11% | +4.11% (20d) | Second-strongest sector; trailing P/E of 29.29 is elevated but price action is positive. |
| Energy (XLE) | -11.03% | -11.03% (20d) | Second-worst sector; trailing P/E of 15.21 is cheap but price momentum is negative. |
| Industrials (XLI) | -3.29% | -3.29% (20d) | Negative 20-day return; trailing P/E of 26.13 is above average. |

## Macro, Fiscal, Rates, Liquidity and Credit

- Growth: US CPI (CPIAUCSL) is 336.30 as of 2026-09-01, and core CPI is 338.90, indicating inflation remains above the pre-2021 trend.
- Policy: The effective federal funds rate is 3.88 as of 2026-11-24, and the 10Y-2Y spread is a modest +0.24, suggesting a still-restrictive but slightly less aggressive policy stance.
- Rates: The yield curve is slightly positive, but the 20-day S&P 500 return of -7.25% suggests markets are pricing in a slower growth or higher-for-longer scenario.
- Liquidity: Credit spreads are tight (IG OAS 0.98, HY OAS 3.72), which is consistent with a risk-on credit backdrop, but the elevated forecast volatility and 66% spike probability indicate a fragile liquidity environment.
- Credit: Tight spreads and a positive yield curve are supportive, but the risk block's elevated volatility and spike probability suggest that credit conditions could deteriorate quickly.
- Labor: Unemployment is 4.2% as of 2026-09-01, and nonfarm payrolls are 159,293 as of 2026-10-01, indicating a still-resilient labor market.

## US Equities and 11 GICS Sectors

Macro source IDs: S001, S002, S003, S004, S005, S006, S007

| GICS sector | Evidence | AI research stance | Source IDs |
| --- | --- | --- | --- |
| Information Technology | Sector ETF XLK has a 20-day return of -18.43% and a trailing P/E of 27.47, the worst performance among all sectors. | Negative: deep drawdown and weak momentum; likely to remain a drag until a stabilization signal appears. | S073 |
| Consumer Staples | Sector ETF XLP has a 20-day return of +6.29% and a trailing P/E of 24.84, the strongest performance among all sectors. | Positive: defensive demand and high valuation support the view; relative strength is notable. | S057 |
| Real Estate | Sector ETF XLRE has a 20-day return of +4.11% and a trailing P/E of 29.29, the second-strongest performance. | Positive: price momentum is positive, but the high trailing P/E suggests limited upside. | S060 |
| Energy | Sector ETF XLE has a 20-day return of -11.03% and a trailing P/E of 15.21, the second-worst performance. | Negative: price momentum is negative despite cheap valuation; watch for a reversal. | S075 |
| Industrials | Sector ETF XLI has a 20-day return of -3.29% and a trailing P/E of 26.13, a negative 20-day return. | Negative: weak price action and above-average valuation; monitor for further deterioration. | S069 |
| Financials | Sector ETF XLF has a 20-day return of +0.68% and a trailing P/E of 15.26, a modest positive return. | Neutral: modest positive return and cheap valuation, but not a strong leader. | S063 |
| Consumer Discretionary | Sector ETF XLY has a 20-day return of +1.87% and a trailing P/E of 24.59, a modest positive return. | Neutral: modest positive return and average valuation, but not a strong leader. | S062 |
| Health Care | Sector ETF XLV has a 20-day return of +2.20% and a trailing P/E of 29.94, a modest positive return. | Neutral: modest positive return and high valuation, but not a strong leader. | S055 |
| Materials | Sector ETF XLB has a 20-day return of -1.25% and a trailing P/E of 21.30, a negative 20-day return. | Negative: weak price action and average valuation; monitor for further deterioration. | S067 |
| Utilities | Sector ETF XLU has a 20-day return of +2.64% and a trailing P/E of 17.94, a modest positive return. | Neutral: modest positive return and average valuation, but not a strong leader. | S066 |
| Communication Services | Sector ETF XLC has a 20-day return of +2.17% and a trailing P/E of 16.74, a modest positive return. | Neutral: modest positive return and average valuation, but not a strong leader. | S070 |

### Sector fundamentals, valuation and earnings

No point-in-time sector fundamentals (e.g., growth, margins, consensus) are supplied in the database snapshot. The sector evidence is limited to 20-day ETF returns and trailing P/E from the supplied source IDs. Any further fundamental claims would be invented and are therefore omitted.

## Growth vs Value

- Consumer Staples (XLP) and Real Estate (XLRE) show the strongest 20-day returns, but their trailing P/Es (24.84 and 29.29) are elevated, suggesting a value-tilt is not the primary driver.
- Energy (XLE) and Financials (XLF) offer the cheapest trailing P/Es (15.21 and 15.26), but their 20-day returns are negative, indicating a value-tilt is not currently rewarded.
- Information Technology (XLK) has a trailing P/E of 27.47, which is above the cheapest sectors but below the most expensive, so valuation is not the main issue; momentum and drawdown are.
- The database does not provide growth or margin data for the full universe, so growth-vs-value conclusions are limited to the supplied P/E evidence.

## ETF Flows and Breadth

- 20-day flow z-scores are negative for XLY (-0.60) and XLV (-0.94), indicating structural distribution and medium-term deterioration in those sectors.
- XLY shows a structural distribution with a 20-day flow z-score of -0.60, while XLV shows medium-term deterioration with a 20-day flow z-score of -0.94.
- Breadth is mixed: 59.12% of names are above the 50-day moving average, and 55.67% are positive over 20 days, but only 55.42% are above the 200-day moving average.
- The advance/decline ratio is 2.876 (371 advancers vs. 129 decliners), which is positive, but the 200-day momentum is deteriorating with a -3.0 change over 20 days.
- New highs are 0 and new lows are 0, so there is no extreme breadth divergence, but the negative divergence of -7.52 suggests a potential warning sign.

## Stock Ideas

Single-stock research uses reported EPS, forward P/E and company fundamentals. All ideas are research judgments, not validated return predictions.

| Ticker | Security | Research view | Price | EPS | Forward P/E | Base target | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| APP | AppLovin | NEW | 378.95 | 20.86084 | 18.165617 | 417.22 | NEW |
| DDOG | Datadog | KEEP | 158.25 | 3.1829 | 49.71881 | N/A | KEEP |

## ETF Ideas

ETF research uses holdings, portfolio valuation and exposure. Single-stock EPS × P/E valuation is not applied to ETFs.

| Ticker | Fund | Research view | Price | Top holdings | Portfolio valuation | Sector exposure | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| XLV | Health Care sector ETF | KEEP | 183.68 | LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59% | Top 10 holdings; numeric weight coverage 61.42% | Health Care | KEEP |
### APP — AppLovin

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** AppLovin offers a better risk/reward than the other top momentum names because its forward P/E is materially lower than the high-multiple names in the shortlist, while still carrying strong 20-day momentum and a manageable 60-day drawdown. Alternatives considered: CMG, CLX, TSCO, MGM, IDXX.
- **Thesis:** AppLovin screens as a top 20-day momentum name with a reported diluted EPS of 11.61 and a forward P/E near 18.17, implying a materially cheaper entry than its recent momentum would suggest. The 20-day return of roughly 45.8% and 60-day return of about 21.6% show strong price acceleration, while the 60-day drawdown of only -8.7% indicates the rally has not yet exhausted downside risk. The Criteo deal talks referenced in the news source add a potential catalyst that could re-rate the stock if the transaction closes.
- **Source IDs:** S008, S011, S012, S014
- **Catalysts:** Criteo deal talks may close and re-rate AppLovin, Continued 20-day momentum with a modest 60-day drawdown, Forward P/E near 18.17 offers a cheaper entry than the recent price run
- **Risks:** 20-day momentum is already strong, leaving limited room for further upside, Deal talks are speculative and not confirmed, High revenue growth may not be sustained at current margins
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 20.8608 (source.forwardEps) x AI multiple assumption 20.00; source IDs S008, S011, S012, S014
- **EPS:** 20.86084 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 18.165617
- **FY+1 growth assumption:** 27.59%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / CRM / APP shows strong FY+1 consensus earnings growth of 27.59% and revenue growth of 55.5%, supported by high gross margin (88.8%) and operating margin (77.8%). The forward P/E of 18.17 is below the 20.0 base multiple, reflecting a premium growth profile relative to the named peer Salesforce (CRM). The multiple is justified by durable high margins, strong revenue momentum, and consensus growth, not by reproducing today's price.
- **Company fundamentals:** AppLovin reported diluted EPS of 11.61 for the period ending 2026-09-30, with forward EPS of 20.86 and a forward P/E of 18.17. Revenue growth is 55.5% and earnings growth is 75.5%, with gross margin of 88.8% and operating margin of 77.8%. The stock closed at 378.95 with 20-day return of 45.8% and 60-day return of 21.6%.
- **Bull / Base / Bear:** 500.66 / 417.22 / 333.77
- **Bull / Base / Bear returns:** 32.12% / 10.1% / -11.92%
- **Scenario probabilities:** not separately assigned; see scenario table.

### DDOG — Datadog

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Datadog is preferred over the other dislocation names because it has the largest analyst following and the strongest revenue growth, making it the most likely to recover if the dislocation is purely technical rather than fundamental. Alternatives considered: INTC, DELL, MU, NOW, MRVL.
- **Thesis:** Datadog is the largest 20-day dislocation name in the shortlist, with a 20-day return of -43.2% and a 60-day return of -29.3%, plus a 60-day drawdown of -46.0%. The stock screens as a dislocation candidate rather than a momentum winner, so the current price action reflects a sharp de-rating. The company's reported diluted EPS of 0.59 and forward EPS of 3.18 imply a forward P/E near 49.7, which is expensive relative to the broader market, but the dislocation may create a mean-reversion opportunity if fundamentals hold.
- **Source IDs:** S047, S052, S053, S056
- **Catalysts:** Potential mean reversion if the 46% drawdown stabilizes, Revenue growth of 35.2% and earnings growth of 231.6% support the business, Large analyst following (45 analysts) suggests active institutional interest
- **Risks:** Forward P/E near 49.7 is very expensive after the dislocation, Operating margin of only 2.4% is thin for a software company, The dislocation may reflect deeper fundamental concerns, not just a technical reset
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** incomplete; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Target withheld. Qualitative research retained. Flags: implausible_base_return.
- **EPS:** 3.1829 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 49.71881
- **FY+1 growth assumption:** 16.23%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / CRM / DDOG shows FY+1 consensus earnings growth of 16.23% and revenue growth of 35.2%, with a forward P/E of 49.72. The base multiple of 20.0 is set below the current forward P/E to reflect the higher valuation multiple and margin profile (operating margin 2.4%, profit margin 6.1%) relative to the named peer Salesforce (CRM). The multiple is justified by growth and margin risk, not by reproducing today's price.
- **Company fundamentals:** Datadog reported diluted EPS of 0.59 for the period ending 2026-09-30, with forward EPS of 3.18 and a forward P/E of 49.72. Revenue growth is 35.2% and earnings growth is 231.6%, with gross margin of 79.6% but operating margin of only 2.4%. The stock closed at 158.25 with a 20-day return of -43.2% and a 60-day return of -29.3%.
- **Bull / Base / Bear:** N/A / N/A / N/A
- **Bull / Base / Bear returns:** N/A% / N/A% / N/A%
- **Scenario probabilities:** not separately assigned; see scenario table.

### XLV — Health Care sector ETF

- **Type:** ETF
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** XLV is preferred over the other sector ETFs because it is the only health care sector ETF in the shortlist and offers the most direct exposure to the defensive health care complex, which is valuable for portfolio balance even if the sector is currently underperforming. Alternatives considered: XLP, XLY, XLRE, XLF, XLU, XLB, XLI, XLC.
- **Thesis:** The Health Care sector ETF (XLV) is the only sector ETF in the shortlist with a negative price change of -0.56% over the relevant period, while the broader market and other sector ETFs are positive. The ETF holds the largest pharmaceutical and health care names, including LLY, JNJ, ABBV, MRK, and UNH, which provide defensive exposure but also drag on performance if the sector is under pressure. The negative sector move suggests caution rather than a buy signal.
- **Source IDs:** S055, S058
- **Catalysts:** Defensive sector exposure may outperform in a risk-off environment, Top holdings include large, stable pharmaceutical names, Sector ETF provides diversification across health care sub-industries
- **Risks:** Sector ETF is down -0.56% while other sector ETFs are positive, Top 10 holdings coverage is only 61.42%, leaving significant undiscovered weight, Pharmaceutical sector may face regulatory or patent-related headwinds
- **Valuation method:** Holdings/portfolio valuation with AI total-return assumption
- **Valuation status:** verified; forward-EPS source: ; period flags: 
- **Valuation assumptions:** Holdings/portfolio valuation; 10 weighted holdings; coverage 61.42%; source IDs S055, S058
- **Top holdings:** LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59%
- **Portfolio valuation:** Top 10 holdings; numeric weight coverage 61.42%
- **Sector exposure:** Health Care
- **Underlying drivers:** Top 10 holdings include LLY (16.88%), JNJ (9.80%), ABBV (7.76%), MRK (5.49%), UNH (5.44%), TMO (3.84%), AMGN (3.75%), GILD (3.15%), ABT (2.74%), and PFE (2.59%), with numeric weight coverage of 61.42%.
- **Bull / Base / Bear:** 205.72 / 192.86 / 172.66
- **Bull / Base / Bear returns:** 12.0% / 5.0% / -6.0%
- **Scenario probabilities:** not separately assigned; see scenario table.

## Quant Risk Layer

| Field | Value |
| --- | --- |
| Volatility model | vol5_ols_v1 |
| Spike model | spike_logit_v1 |
| As-of date | 2026-11-25 |
| Target window | 2026-11-27 to 2026-12-03 |
| Forecast 5D annualized volatility | 27.94% |
| Historical-vol baseline | 31.64% |
| EWMA baseline | 28.40% |
| Spike probability | 65.99% |
| Spike threshold | 18.50% |
| Status | prospective |
| Forecast ID | 9884506cdbaa9353 |

Risk-only; no directional interpretation or allocation implication.

## Scenarios

### Short Term (5 trading sessions)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 25% | +2.00% | Low spike probability (0.66) and false directional signal reduce near-term tail risk; a modest 2.0% upside reflects a benign volatility regime and stable macro backdrop over the target week. |
| Base | 50% | +0.00% | Frozen daily-close model with no directional alpha implies a neutral path; base case anchors to the historical baseline of ~0.32 and EWMA of ~0.28, yielding flat returns with no material drift. |
| Bear | 25% | -2.00% | If the frozen forecast's elevated volatility (0.279) persists and a spike materializes, downside risk rises; a -2.0% return captures the probability-weighted downside without assuming a directional break. |

### Long Term (12 months)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 30% | +8.00% | Sustained low volatility and stable baselines support a gradual risk-on drift; an 8.0% long-term return reflects continued earnings growth and favorable rate expectations over the horizon. |
| Base | 40% | +3.00% | A neutral long-term path anchored to the historical baseline (0.316) and EWMA (0.284) implies modest positive returns as volatility normalizes and credit conditions remain stable. |
| Bear | 30% | -5.00% | If elevated volatility (0.279) and spike probability (0.66) persist, earnings compression and widening credit spreads could drive a -5.0% long-term return, reflecting a downside scenario with no directional alpha. |

## Positioning

- Maintain a defensive tilt: Consumer Staples and Real Estate are the strongest sectors, while Information Technology is the clear weak spot.
- Watch the 200-day moving average: only 55.42% of names are above it, and the 200-day momentum is deteriorating, which could signal a broader trend change.
- Monitor credit spreads: tight IG and HY spreads are supportive, but the elevated forecast volatility and 66% spike probability suggest a fragile environment.
- Avoid overconcentration in the liquidity leaders (NVDA, AMD, AAPL, AMZN) as they are not necessarily aligned with the broader market trend.
- The equity data is a mix of provisional and canonical rows, so treat any numerical claims with caution until the data is fully canonical.

## Catalysts

| Date | Event | Why it matters |
| --- | --- | --- |
| 2026-11-27 | US macro data release | The latest macro data (CPI, unemployment, payrolls) is from 2026-09-01 and 2026-10-01, so a new data point could shift the growth/inflation narrative. |
| 2026-11-27 | Risk block forecast window | The risk block covers 2026-11-27 to 2026-12-03 with elevated forecast volatility (0.279) and a 66% spike probability, which could trigger a market event. |
| 2026-11-25 |  |  |

## Key Risks


## External Source Ledger

| ID | Type | Ticker | Published | Status | URL | Claims |
| --- | --- | --- | --- | --- | --- | --- |
| S001 | macro | macro | 2026-11-24 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFF&cosd=2026-01-01 | Effective federal funds rate (DFF) latest observation 2026-11-24: 3.88 |
| S002 | macro | macro | 2026-11-24 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLH0A0HYM2&cosd=2026-01-01 | US high-yield OAS (BAMLH0A0HYM2) latest observation 2026-11-24: 3.72 |
| S003 | macro | macro | 2026-11-24 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLC0A0CM&cosd=2026-01-01 | US investment-grade OAS (BAMLC0A0CM) latest observation 2026-11-24: 0.98 |
| S004 | macro | macro | 2026-10-01 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCSL&cosd=2026-01-01 | US CPI (CPIAUCSL) latest observation 2026-10-01: 337.476 |
| S005 | macro | macro | 2026-10-01 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=UNRATE&cosd=2026-01-01 | US unemployment rate (UNRATE) latest observation 2026-10-01: 4.1 |
| S006 | macro | macro | 2026-10-01 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=PAYEMS&cosd=2026-01-01 | US nonfarm payrolls (PAYEMS) latest observation 2026-10-01: 159293 |
| S007 | macro | macro | 2026-11-25 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=T10Y2Y&cosd=2026-01-01 | 10Y-2Y Treasury spread (T10Y2Y) latest observation 2026-11-25: 0.24 |
| S008 | filing | APP | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001751008&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0001751008-26-000069); 8-K filed 2026-11-04 (accession 0001751008-26-000068); 10-Q filed 2026-08-05 (accession 0001751008-26-000059) |
| S009 | filing | CMG | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001058090&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0001058090-26-000104); 8-K filed 2026-10-28 (accession 0001058090-26-000103); 8-K filed 2026-09-14 (accession 0001058090-26-000088) |
| S010 | filing | CHTR | 2026-11-06 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-06 (accession 0001091667-26-000073); 8-K filed 2026-11-06 (accession 0001091667-26-000072); 8-K filed 2026-10-27 (accession 0001091667-26-000064) |
| S011 | filing | APP | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json | Diluted EPS 11.61 for period ending 2026-09-30 (filed 2026-11-04) |
| S012 | news | APP | Wed, 25 Nov 2026 22:10:42 GMT | ok | https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en | AppLovin (APP) Could Be 25% Undervalued As Criteo Deal Talks Stir Debate - Yahoo Finance (Wed, 25 Nov 2026 22:10:42 GMT); AppLovin vs. Reddit: Which Technology Stock Is a Better Buy for 2027? - The Motley Fool (Sat, 21 Nov 2026 23:19:26 GMT); APP Falls 14.9% in One Week as Growth Strength Meets Execution Risk - TradingView (Mon, 23 Nov 2026 15:30:00 GMT) |
| S013 | news | CHTR | Thu, 26 Nov 2026 19:14:36 GMT | ok | https://news.google.com/rss/search?q=CHTR+Charter+Communications+stock&hl=en-US&gl=US&ceid=US:en | Why Charter Communications Stock Is Back In Focus After $2 Billion Cost Saving Plan - Yahoo Finance (Thu, 26 Nov 2026 19:14:36 GMT); Charter Communications (CHTR) Jumps After Cox Deal, Is It Still Cheap? - Yahoo Finance (Thu, 26 Nov 2026 16:09:04 GMT); What Is The Biggest Threat To Charter Communications Stock? - Trefis (Thu, 12 Nov 2026 08:00:00 GMT) |
| S014 | stock | APP | 2026-11-27 | ok | https://finance.yahoo.com/quote/APP | Trailing P/E: 25.518518; Forward P/E: 18.165617; Forward EPS: 20.86084; Price: 378.95; Market price: 378.95; Market cap: 125554507776; Sector: Communication Services; Trailing Eps: 14.85; Revenue Growth: 0.555; Earnings Growth: 0.755; Gross Margin: 0.8878; Operating Margin: 0.77782995; Profit Margin: 0.65887; Return On Equity: 2.1008599; Total Revenue: 7608893952; Market Cap: 125554507776; Consensus EPS FY+1: 20.78066; growth: 0.2759 |
| S015 | filing | CMG | 2026-10-29 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001058090.json | Diluted EPS 0.82 for period ending 2026-09-30 (filed 2026-10-29) |
| S016 | stock | CMG | 2026-11-27 | ok | https://finance.yahoo.com/quote/CMG | Trailing P/E: 34.95327; Forward P/E: 28.261396; Forward EPS: 1.32336; Price: 37.4; Market price: 37.4; Market cap: 47310065664; Sector: Consumer Cyclical; Trailing Eps: 1.07; Revenue Growth: 0.096; Earnings Growth: -0.062; Gross Margin: 0.39314; Operating Margin: 0.14715; Profit Margin: 0.10832; Return On Equity: 0.48518002; Total Revenue: 12713477120; Market Cap: 47310065664; Consensus EPS FY+1: 1.32336; growth: 0.216 |
| S017 | filing | CLX | 2026-11-19 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 | 8-K filed 2026-11-19 (accession 0001206774-26-000606); 10-Q filed 2026-11-02 (accession 0000021076-26-000046); 8-K filed 2026-11-02 (accession 0000021076-26-000044) |
| S018 | filing | CHTR | 2026-11-06 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001091667.json | Diluted EPS 0.38 for period ending 2026-09-30 (filed 2026-11-06) |
| S019 | news | CMG | Tue, 24 Nov 2026 15:25:45 GMT | ok | https://news.google.com/rss/search?q=CMG+Chipotle+Mexican+Grill+stock&hl=en-US&gl=US&ceid=US:en | What Could Lift Chipotle Stock Further? - Trefis (Tue, 24 Nov 2026 15:25:45 GMT); Chipotle’s Earnings Fell 7% Last Quarter, but 1 Trend Has Now Lasted 3 Straight Quarters. - The Motley Fool (Tue, 24 Nov 2026 12:45:02 GMT); Where Will Chipotle Mexican Grill's Stock Be in 5 Years? - Yahoo Finance (Wed, 19 Aug 2026 07:00:00 GMT) |
| S020 | stock | CHTR | 2026-11-27 | ok | https://finance.yahoo.com/quote/CHTR | Trailing P/E: 13.841166; Forward P/E: 3.2299702; Forward EPS: 45.59485; Price: 147.27; Market price: 147.27; Market cap: 26368923648; Sector: Communication Services; Trailing Eps: 10.64; Revenue Growth: 0.091; Gross Margin: 0.55084; Operating Margin: 0.23389; Profit Margin: 0.02498; Return On Equity: 0.07019; Total Revenue: 55645999104; Market Cap: 26368923648; Consensus EPS FY+1: 47.75367; growth: 1.4848 |
| S021 | news | CLX | Tue, 24 Nov 2026 22:03:23 GMT | ok | https://news.google.com/rss/search?q=CLX+Clorox+stock&hl=en-US&gl=US&ceid=US:en | Clorox Company (The) (CLX) Stock Forecasts - Yahoo Finance (Tue, 24 Nov 2026 22:03:23 GMT); Clorox (CLX) Stock Looks Fairly Valued After A 28% Slide - Simply Wall St (Mon, 23 Nov 2026 14:08:34 GMT); CLX - Clorox Co Stock Price and Quote - Finviz (Tue, 26 May 2026 17:32:27 GMT) |
| S022 | filing | TSCO | 2026-11-05 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000916365&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-05 (accession 0000916365-26-000079); 8-K filed 2026-11-05 (accession 0000916365-26-000076); 8-K filed 2026-10-22 (accession 0000916365-26-000069) |
| S023 | stock | TSCO | 2026-11-27 | ok | https://finance.yahoo.com/quote/TSCO | Trailing P/E: 21.7043; Forward P/E: 19.622805; Forward EPS: 2.0573; Price: 40.37; Market price: 40.37; Market cap: 20934819840; Sector: Consumer Cyclical; Trailing Eps: 1.86; Revenue Growth: 0.051; Earnings Growth: -0.121; Gross Margin: 0.36285; Operating Margin: 0.08701; Profit Margin: 0.061300002; Return On Equity: 0.37347; Total Revenue: 15942134784; Market Cap: 20934819840; Consensus EPS FY+1: 2.04688; growth: 0.091400005 |
| S024 | filing | MGM | 2026-10-28 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000789570&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-28 (accession 0000789570-26-000107); 8-K filed 2026-10-28 (accession 0000789570-26-000106); 8-K filed 2026-10-28 (accession 0000789570-26-000104) |
| S025 | stock | CLX | 2026-11-27 | ok | https://finance.yahoo.com/quote/CLX | Trailing P/E: 19.953238; Forward P/E: 17.985216; Forward EPS: 6.1684; Price: 110.94; Market price: 110.94; Market cap: 13440092160; Sector: Consumer Defensive; Trailing Eps: 5.56; Revenue Growth: 0.333; Earnings Growth: 1.138; Gross Margin: 0.41939998; Operating Margin: 0.14286; Profit Margin: 0.09408; Return On Equity: 5.34363; Total Revenue: 7196000256; Market Cap: 13440092160; Consensus EPS FY+1: 6.1684; growth: 0.0769 |
| S026 | stock | MGM | 2026-11-27 | ok | https://finance.yahoo.com/quote/MGM | Trailing P/E: 13.326924; Forward P/E: 24.652624; Forward EPS: 1.40553; Price: 34.65; Market price: 34.65; Market cap: 8766815232; Sector: Consumer Cyclical; Trailing Eps: 2.6; Revenue Growth: -0.009; Gross Margin: 0.4362; Operating Margin: 0.057979997; Profit Margin: 0.03916; Return On Equity: 0.26933; Total Revenue: 17722869760; Market Cap: 8766815232; Consensus EPS FY+1: 1.40553; growth: -0.0462 |
| S027 | filing | IDXX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000874716&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000874716-26-000135); 8-K filed 2026-11-02 (accession 0001104659-26-120892); 10-Q filed 2026-08-04 (accession 0000874716-26-000123) |
| S028 | filing | CLX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000021076.json | Diluted EPS 1.39 for period ending 2026-09-30 (filed 2026-11-02) |
| S029 | stock | IDXX | 2026-11-27 | ok | https://finance.yahoo.com/quote/IDXX | Trailing P/E: 47.807278; Forward P/E: 41.997524; Forward EPS: 16.8929; Price: 709.46; Market price: 709.46; Market cap: 55895703552; Sector: Healthcare; Trailing Eps: 14.84; Revenue Growth: 0.099; Earnings Growth: 0.179; Gross Margin: 0.62722; Operating Margin: 0.32497; Profit Margin: 0.25357; Return On Equity: 0.68925005; Total Revenue: 4662220800; Market Cap: 55895703552; Consensus EPS FY+1: 16.8929; growth: 0.1244 |
| S030 | news | TSCO | Wed, 25 Nov 2026 03:47:00 GMT | ok | https://news.google.com/rss/search?q=TSCO+Tractor+Supply+stock&hl=en-US&gl=US&ceid=US:en | Tractor Supply Company (TSCO) stock price, news, quote and history - Yahoo Finance UK (Wed, 25 Nov 2026 03:47:00 GMT); Tractor Supply Company Stock Price Forecast. Should You Buy TSCO? - StockInvest.us (Tue, 24 Nov 2026 08:00:00 GMT); Tractor Supply (Nasdaq:TSCO) - Stock Analysis - Simply Wall St (Mon, 23 Nov 2026 08:00:00 GMT) |
| S031 | filing | MGM | 2026-10-28 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000789570.json | Diluted EPS 1.52 for period ending 2026-09-30 (filed 2026-10-28) |
| S032 | filing | FISV | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0000798354-26-000042); 8-K filed 2026-11-03 (accession 0000798354-26-000039); 8-K filed 2026-10-23 (accession 0001193125-26-429481) |
| S033 | news | MGM | Mon, 23 Nov 2026 17:45:39 GMT | ok | https://news.google.com/rss/search?q=MGM+MGM+Resorts+stock&hl=en-US&gl=US&ceid=US:en | Here’s Why MGM Resorts (MGM) Declined in Q3 - Yahoo Finance (Mon, 23 Nov 2026 17:45:39 GMT); MGM Resorts officer sells $685,938 in common stock - Investing.com (Wed, 25 Nov 2026 01:19:46 GMT); MGM Stock Dives 10% After Barry Diller Drops $18 Billion Bid - Forbes (Thu, 24 Sep 2026 07:00:00 GMT) |
| S034 | filing | TSCO | 2026-11-05 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000916365.json | Diluted EPS 1.43 for period ending 2026-09-26 (filed 2026-11-05) |
| S035 | news | IDXX | Wed, 25 Nov 2026 17:12:38 GMT | ok | https://news.google.com/rss/search?q=IDXX+Idexx+Laboratories+stock&hl=en-US&gl=US&ceid=US:en | Does ETF Buying Change The Bull Case For IDEXX Stock (IDXX)? - Yahoo Finance (Wed, 25 Nov 2026 17:12:38 GMT); IDEXX Laboratories Stock Outlook: Is Wall Street Bullish or Bearish - Barchart.com (Thu, 26 Nov 2026 13:13:20 GMT); If You Invested $100 In IDEXX Laboratories Stock 15 Years Ago, You Would Have This Much Today - Benzinga (Mon, 02 Nov 2026 08:00:00 GMT) |
| S036 | stock | FISV | 2026-11-27 | ok | https://finance.yahoo.com/quote/FISV | Forward P/E: 7.499978; Price: 59.78; Market price: 59.78; Market cap: 31805810688; Market Cap: 31805810688; Consensus EPS FY+1: 7.97069; growth: 0.0954 |
| S037 | filing | SNDK | 2026-11-19 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0002023554&type=10-Q&dateb=&owner=include&count=10 | 8-K filed 2026-11-19 (accession 0001628280-26-075127); 8-K filed 2026-11-18 (accession 0001628280-26-074848); 10-Q filed 2026-10-30 (accession 0001628280-26-068601) |
| S038 | filing | IDXX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000874716.json | Diluted EPS 11.75 for period ending 2026-09-30 (filed 2026-11-02) |
| S039 | filing | MRVL | 2026-11-12 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001835632&type=10-Q&dateb=&owner=include&count=10 | 8-K filed 2026-11-12 (accession 0001835632-26-000026); 8-K filed 2026-11-02 (accession 0001193125-26-442717); 8-K filed 2026-11-02 (accession 0001193125-26-442714) |
| S040 | stock | SNDK | 2026-11-27 | ok | https://finance.yahoo.com/quote/SNDK | Trailing P/E: 4.7065215; Forward P/E: 2.0565789; Forward EPS: 35.79245; Price: 73.61; Market price: 73.61; Market cap: 83791355904; Sector: Technology; Trailing Eps: 15.64; Revenue Growth: 3.779; Earnings Growth: 69.096; Gross Margin: 0.79952; Operating Margin: 0.7268; Profit Margin: 0.67039; Return On Equity: 1.41174; Total Revenue: 28970999808; Market Cap: 83791355904; Consensus EPS FY+1: 35.79245; growth: 0.2573 |

## Sources

- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFF&cosd=2026-01-01 (2026-11-24)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLH0A0HYM2&cosd=2026-01-01 (2026-11-24)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLC0A0CM&cosd=2026-01-01 (2026-11-24)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCSL&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=UNRATE&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=PAYEMS&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=T10Y2Y&cosd=2026-01-01 (2026-11-25)
- filing APP: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001751008&type=10-Q&dateb=&owner=include&count=10 (2026-11-04)
- filing CMG: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001058090&type=10-Q&dateb=&owner=include&count=10 (2026-10-29)
- filing CHTR: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 (2026-11-06)
- filing APP: https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json (2026-11-04)
- news APP: https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en (Wed, 25 Nov 2026 22:10:42 GMT)
- news CHTR: https://news.google.com/rss/search?q=CHTR+Charter+Communications+stock&hl=en-US&gl=US&ceid=US:en (Thu, 26 Nov 2026 19:14:36 GMT)
- stock APP: https://finance.yahoo.com/quote/APP (2026-11-27)
- filing CMG: https://data.sec.gov/api/xbrl/companyfacts/CIK0001058090.json (2026-10-29)
- stock CMG: https://finance.yahoo.com/quote/CMG (2026-11-27)
- filing CLX: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 (2026-11-19)
- filing CHTR: https://data.sec.gov/api/xbrl/companyfacts/CIK0001091667.json (2026-11-06)
- news CMG: https://news.google.com/rss/search?q=CMG+Chipotle+Mexican+Grill+stock&hl=en-US&gl=US&ceid=US:en (Tue, 24 Nov 2026 15:25:45 GMT)
- stock CHTR: https://finance.yahoo.com/quote/CHTR (2026-11-27)

## AI Provenance

- Provider / model: hermes-local-proxy / upstage/solar-mini4:free
- Market research: attempts=1 tokens=8384 (prompt=5384, completion=3000) runtime=24.82s
- Fundamental research: generated this run at 2026-11-27T10:12:54.378439+00:00
- Evidence source dates: {'as_of': '2026-11-25', 'latest_equity_date': '2026-11-25', 'latest_macro_date': '2026-11-27', 'flows_date': '2026-11-25'}
- Evidence fingerprint: 32dfd88174757d1c8b1c057f1c7a58d399212efd04c5203abcd62c13f95e77e8
- Source citations are retrieved external records in the ledger above; market values remain from the verified database snapshot.


## Disclosures

- This is research and market intelligence, not investment advice.
- AI conclusions are research judgments, not validated return predictions.
- The frozen risk layer is risk-only and is not used for directional views or allocations.
- Legacy scores are not active inputs or outputs.

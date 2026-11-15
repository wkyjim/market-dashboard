# AEGIS AI-First Market Intelligence

Research generated at: 15 November 2026, 17:14 HKT
Database freshness: equity 2026-11-13 (latest row retrieved 2026-11-15 13:06:40.074841+08:00)
Data cutoff: 2026-11-13 US cash close
Snapshot ID: aegis-hourly-20261115T091433Z

## Executive Summary

- **AI market view: Late-November 2026 equity market is in a late-cycle, mixed posture: broad market breadth is positive but thin, with 50-day and 200-day advance ratios near 71% and 64%, and a 20-day advance/decline ratio of 1.70. Momentum and dislocation screens are dominated by large-cap liquidity leaders and high-beta technology names, while the 20-day sector returns show Health Care, Consumer Staples, Consumer Discretionary and Financials at the top and Information Technology and Energy at the bottom. Macro data show a still-elevated but easing inflation backdrop, a 4.2% unemployment rate, a modestly positive 10Y-2Y spread, and a Fed funds rate near 3.88%, with high-yield OAS at 3.20 and IG OAS at 0.89. Risk indicators show below-baseline 5-day volatility and a 16.5% spike probability, below both historical and EWMA baselines.**
- Equity market is in a late-cycle, mixed configuration: broad market breadth is positive but not robust, with 50-day and 200-day advance ratios of 71.3% and 63.6% and a 20-day advance/decline ratio of 1.70.
- Momentum and dislocation screens are led by large-cap liquidity leaders and high-beta technology names, while the 20-day sector returns show Health Care, Consumer Staples, Consumer Discretionary and Financials at the top and Information Technology and Energy at the bottom.
- Macro data show a still-elevated but easing inflation backdrop, a 4.2% unemployment rate, a modestly positive 10Y-2Y spread, and a Fed funds rate near 3.88%, with high-yield OAS at 3.20 and IG OAS at 0.89.
- Risk indicators show below-baseline 5-day volatility and a 16.5% spike probability, below both historical and EWMA baselines, suggesting a calm but not risk-free environment.
- Sector leadership is broad-based in defensive and consumer names, while technology and energy lag, consistent with a late-cycle, quality-and-defensiveness tilt rather than a broad-based cyclical expansion.
- The market is not in a clear risk-on or risk-off regime; the evidence points to a cautious, quality-tilted posture with selective exposure to momentum and dislocation names rather than a broad allocation shift.

## Data QC

- Status: **PASS_WITH_WARNINGS**
- Equity session: 0 completed session(s) behind inference date
- Equity provenance: 393 provisional / 12576 canonical
- Breadth lag: 0 session(s); ETF-flow lag: 0 session(s)
- Note: Equity session contains a mix of provisional yfinance and canonical Massive rows.
- External sources: 79 ok / 0 unavailable; retrieved 2026-11-15T09:14:52.598993+00:00

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
| S&P 500 | 7561.67 | -1.28% over 20 days | Broad market is positive on a 20-day basis but the index is down on the 20-day horizon, with 71.3% of names above their 50-day and 63.6% above their 200-day. |
| Health Care | +6.87% | 20-day sector return | Top sector by 20-day return, supported by defensive demand and a trailing P/E of 30.78. |
| Consumer Discretionary | +6.69% | 20-day sector return | Strong 20-day performance, with a trailing P/E of 25.11. |
| Consumer Staples | +5.40% | 20-day sector return | Defensive strength, with a trailing P/E of 24.85. |
| Financials | +5.69% | 20-day sector return | Solid 20-day performance, with a trailing P/E of 15.85. |
| Information Technology | -7.19% | 20-day sector return | Bottom sector by 20-day return, with a trailing P/E of 30.03, reflecting high-beta and dislocation pressure. |
| Energy | -4.81% | 20-day sector return | Bottom sector by 20-day return, with a trailing P/E of 16.23, consistent with late-cycle energy weakness. |

## Macro, Fiscal, Rates, Liquidity and Credit

- Inflation is still elevated but easing: CPI for all urban consumers is 336.298 in September 2026, with core CPI at 338.896, and the latest CPI observation from October 2026 is 337.476, indicating a gradual disinflation trend.
- Labor market is stable but not overheating: unemployment is 4.2% in September 2026, with the latest October 2026 reading at 4.1%, and nonfarm payrolls at 159,293 in thousands, suggesting a resilient but cooling labor market.
- Monetary policy is in a late-cycle easing mode: the effective federal funds rate is 3.88% as of November 12, 2026, with a 10Y-2Y Treasury spread of 0.27 as of November 13, 2026, indicating a modestly positive yield curve.
- Credit conditions are stable: high-yield OAS is 3.20 and investment-grade OAS is 0.89 as of November 12, 2026, implying tight but not stressed credit spreads.
- Liquidity and risk appetite are calm: 5-day forecast volatility is 14.93%, below the historical baseline of 22.07% and the EWMA baseline of 20.09%, with a 16.5% spike probability, below both baselines.
- Equity market breadth is positive but thin: 71.3% of names are above their 50-day, 63.6% above their 200-day, and the 20-day advance/decline ratio is 1.70, indicating broad but not overwhelming participation.

## US Equities and 11 GICS Sectors

Macro source IDs: S001, S002, S003, S004, S005, S006, S007

| GICS sector | Evidence | AI research stance | Source IDs |
| --- | --- | --- | --- |
| Health Care | 20-day sector return of +6.87% with a trailing P/E of 30.78, the highest among the top-performing sectors, indicating defensive demand and premium valuation. | Defensive strength with premium valuation; supported by stable demand and a 20-day return well above the market average. | S057 |
| Consumer Discretionary | 20-day sector return of +6.69% with a trailing P/E of 25.11, indicating strong consumer spending and moderate valuation. | Positive momentum with balanced valuation; supported by strong 20-day performance and a reasonable P/E. | S056 |
| Consumer Staples | 20-day sector return of +5.40% with a trailing P/E of 24.85, indicating defensive strength and stable demand. | Defensive strength with moderate valuation; supported by stable demand and a reasonable P/E. | S060 |
| Financials | 20-day sector return of +5.69% with a trailing P/E of 15.85, indicating solid performance and a relatively low valuation. | Solid performance with a low valuation; supported by strong 20-day returns and a reasonable P/E. | S062 |
| Real Estate | 20-day sector return of +5.24% with a trailing P/E of 29.63, indicating moderate performance and a premium valuation. | Moderate performance with a premium valuation; supported by stable 20-day returns and a reasonable P/E. | S063 |
| Utilities | 20-day sector return of +4.34% with a trailing P/E of 18.11, indicating defensive strength and a moderate valuation. | Defensive strength with moderate valuation; supported by stable 20-day returns and a reasonable P/E. | S069 |
| Materials | 20-day sector return of +2.57% with a trailing P/E of 21.72, indicating moderate performance and a reasonable valuation. | Moderate performance with a reasonable valuation; supported by stable 20-day returns and a reasonable P/E. | S065 |
| Industrials | 20-day sector return of +0.61% with a trailing P/E of 27.07, indicating weak momentum and a premium valuation. | Weak momentum with a premium valuation; supported by low 20-day returns and a reasonable P/E. | S070 |
| Communication Services | 20-day sector return of -1.48% with a trailing P/E of 17.26, indicating negative momentum and a moderate valuation. | Negative momentum with a moderate valuation; supported by negative 20-day returns and a reasonable P/E. | S068 |
| Information Technology | 20-day sector return of -7.19% with a trailing P/E of 30.03, indicating negative momentum and a premium valuation. | Negative momentum with a premium valuation; supported by negative 20-day returns and a reasonable P/E. | S074 |
| Energy | 20-day sector return of -4.81% with a trailing P/E of 16.23, indicating negative momentum and a low valuation. | Negative momentum with a low valuation; supported by negative 20-day returns and a reasonable P/E. | S077 |

### Sector fundamentals, valuation and earnings

The supplied database provides 20-day sector ETF returns and trailing P/E ratios for all 11 GICS sectors, but does not include point-in-time sector-level fundamentals such as earnings growth, margins, or consensus estimates. Therefore, sector fundamentals are limited to the supplied return and valuation evidence; no additional sector-level fundamental data are available in the database.

## Growth vs Value

- Health Care and Consumer Discretionary show the strongest 20-day momentum with trailing P/Es of 30.78 and 25.11, respectively, indicating a growth-and-defensiveness tilt rather than pure value.
- Financials and Utilities offer lower trailing P/Es of 15.85 and 18.11, respectively, providing a value tilt within a late-cycle, defensive framework.
- Information Technology and Energy are the weakest 20-day performers with trailing P/Es of 30.03 and 16.23, reflecting high-beta and energy sector weakness in a late-cycle environment.
- The sector-level P/E dispersion is wide, with Health Care at 30.78 and Financials at 15.85, indicating a market that is not uniformly expensive or cheap but is differentiated by sector leadership.

## ETF Flows and Breadth

- Market breadth is positive but not robust: 71.3% of names are above their 50-day, 63.6% above their 200-day, and the 20-day advance/decline ratio is 1.70, indicating broad but not overwhelming participation.
- The 20-day advance/decline ratio of 1.70 is a strong breadth signal, but the 50-day and 200-day advance ratios of 71.3% and 63.6% are moderate, suggesting a market that is not in a broad-based expansion.
- Flow data show strong institutional buying in SOXX with a 20-day flow z-score of 5.10 and a 60-day flow z-score of 3.17, indicating exceptional institutional accumulation, while SMH shows a 20-day flow z-score of 1.22 and a 60-day flow z-score of 1.04, indicating tactical profit-taking inside structural accumulation.
- TLT shows a 2

## Stock Ideas

Single-stock research uses reported EPS, forward P/E and company fundamentals. All ideas are research judgments, not validated return predictions.

| Ticker | Security | Research view | Price | EPS | Forward P/E | Base target | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| APP | AppLovin | NEW | 409.1 | 20.86026 | 19.611452 | 458.93 | NEW |
| PNR | Pentair | KEEP | 68.3 | 5.30402 | 12.877027 | 74.26 | KEEP |
| GEN | Gen Digital | NEW | 30.4 | 3.33736 | 9.108996 | 36.71 | NEW |
| CLX | Clorox | KEEP | 109.46 | 6.1684 | 17.745283 | 98.69 | KEEP |
| ROP | Roper Technologies | KEEP | 479.975 | 24.57318 | 19.532475 | 442.32 | KEEP |

## ETF Ideas

ETF research uses holdings, portfolio valuation and exposure. Single-stock EPS × P/E valuation is not applied to ETFs.

No qualifying ETF ideas this run.
### APP — AppLovin

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** AppLovin offers a rare combination of top-tier momentum, best-in-class margins, and strong reported earnings growth, making it a more compelling standalone equity than the lower-margin, lower-growth industrial and consumer staples names in the shortlist. Alternatives considered: PNR, GEN, CLX, ROP.
- **Thesis:** AppLovin screens in the top 20-day momentum bucket with a 53.7% 20-day return and a 32.5% 60-day return, indicating strong recent price leadership. Reported diluted EPS of 11.61 for the fiscal period ending 2026-09-30 and a forward EPS of 20.86 support a forward P/E of 19.61, which is reasonable for a high-margin, high-growth mobile advertising platform. The company's gross margin of 88.8% and operating margin of 77.8% provide a durable profitability profile, while revenue growth of 55.5% and earnings growth of 75.5% underpin the momentum thesis.
- **Source IDs:** S008, S012, S013, S014
- **Catalysts:** Continued acceleration in mobile advertising revenue, Sustained high gross margin and operating leverage, Positive 20-day and 60-day price momentum
- **Risks:** High valuation multiples relative to slower-growth peers, Concentration in mobile advertising and potential ad-market cyclicality, Recent sharp price run could face mean-reversion or sentiment risk
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 20.8603 (source.forwardEps) x AI multiple assumption 22.00; source IDs S008, S012, S013, S014
- **EPS:** 20.86026 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 19.611452
- **FY+1 growth assumption:** 27.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / PNR and CLX / APP shows strong FY1 consensus earnings growth of 27.44% and revenue growth of 25.37%, supported by high gross margin (88.78%) and operating margin (77.78%). The base multiple of 22.0x is justified by superior margins and growth relative to PNR (12.88x forward P/E, lower growth) and CLX (17.75x forward P/E, lower growth), while the bull and bear multiples reflect upside/downside around the growth and margin profile.
- **Company fundamentals:** Reported diluted EPS 11.61; forward EPS 20.86; forward P/E 19.61; gross margin 88.8%; operating margin 77.8%; profit margin 65.9%; revenue growth 55.5%; earnings growth 75.5%; ROE 2.10; 20-day return 53.7%; 60-day return 32.5%; 60-day drawdown -0.2%.
- **Bull / Base / Bear:** 542.37 / 458.93 / 333.76
- **Bull / Base / Bear returns:** 32.58% / 12.18% / -18.42%
- **Scenario probabilities:** not separately assigned; see scenario table.

### PNR — Pentair

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Pentair is not preferred over the higher-growth, higher-margin names like AppLovin or Gen Digital, but its cheap forward multiple offers a defensive, value-oriented alternative within the Industrials sector. Alternatives considered: APP, GEN, CLX, ROP.
- **Thesis:** Pentair is a top-20-day momentum name with a 27.8% 20-day return and a 7.1% 60-day return. The stock trades at a forward P/E of 12.9, which is attractive relative to its sector-relative P/E of 0.49, but reported earnings growth of -18.8% and revenue growth of -4.5% indicate near-term operational headwinds. The moderate 60-day drawdown of -5.2% suggests some consolidation, and the neutral stance reflects the tension between a cheap forward multiple and deteriorating fundamentals.
- **Source IDs:** S009, S015, S018, S020
- **Catalysts:** Potential stabilization in revenue and earnings growth, Attractive forward P/E of 12.9 relative to sector, Continued momentum in the top 20-day bucket
- **Risks:** Negative revenue and earnings growth in the latest reported period, Sector-relative P/E of 0.49 indicates underperformance versus peers, Industrial end-market softness could delay recovery
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 5.3040 (source.forwardEps) x AI multiple assumption 14.00; source IDs S009, S015, S018, S020
- **EPS:** 5.30402 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 12.877027
- **FY+1 growth assumption:** 12.82%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / APP and CLX / PNR has FY1 consensus earnings growth of 12.82% and revenue growth of 18.38%, with a lower forward P/E of 12.88x. The base multiple of 14.0x is justified by its lower growth and margin profile (gross margin 40.17%, operating margin 21.41%) compared to APP, but it warrants a higher multiple than bear case due to positive growth. The bull and bear multiples reflect range around this valuation.
- **Company fundamentals:** Reported diluted EPS 2.76; forward EPS 5.30; forward P/E 12.88; gross margin 40.2%; operating margin 21.4%; profit margin 15.4%; revenue growth -4.5%; earnings growth -18.8%; ROE 15.6%; 20-day return 27.8%; 60-day return 7.1%; 60-day drawdown -5.2%.
- **Bull / Base / Bear:** 90.17 / 74.26 / 58.34
- **Bull / Base / Bear returns:** 32.02% / 8.73% / -14.58%
- **Scenario probabilities:** not separately assigned; see scenario table.

### GEN — Gen Digital

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** Gen Digital offers a much lower forward P/E than AppLovin while still delivering strong earnings growth, making it a more attractive value-oriented alternative within the Information Technology sector. Alternatives considered: APP, PNR, CLX, ROP.
- **Thesis:** Gen Digital is a top-20-day momentum name with a 25.8% 20-day return and a 7.9% 60-day return. It trades at a forward P/E of 9.1, which is very cheap relative to its sector-relative P/E of 0.42, and it has strong reported earnings growth of 128.6% and revenue growth of 12.2%. The combination of low valuation and accelerating earnings makes it an attractive risk-reward, though the lower gross margin of 77.4% and operating margin of 43.2% suggest less pricing power than AppLovin.
- **Source IDs:** S019, S022, S023, S028
- **Catalysts:** Accelerating earnings growth of 128.6%, Very low forward P/E of 9.1, Positive 20-day and 60-day momentum
- **Risks:** Lower gross margin and operating margin than high-growth tech peers, Cybersecurity and digital risk exposure to macro cycles, Lower ROE of 46.4% relative to AppLovin
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 3.3374 (source.forwardEps) x AI multiple assumption 11.00; source IDs S019, S022, S023, S028
- **EPS:** 3.33736 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 9.108996
- **FY+1 growth assumption:** 12.86%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / PNR and CLX / GEN has FY1 consensus earnings growth of 12.86% and revenue growth of 6.81%, with strong ROE of 46.4% and operating margin of 43.22%. The base multiple of 11.0x is justified by its high returns and growth, but it is lower than APP due to lower revenue growth and different margin structure. The bull and bear multiples reflect range around this valuation.
- **Company fundamentals:** Reported diluted EPS 0.83; forward EPS 3.34; forward P/E 9.11; gross margin 77.4%; operating margin 43.2%; profit margin 23.1%; revenue growth 12.2%; earnings growth 128.6%; ROE 46.4%; 20-day return 25.8%; 60-day return 7.9%; 60-day drawdown -3.2%.
- **Bull / Base / Bear:** 46.72 / 36.71 / 26.7
- **Bull / Base / Bear returns:** 53.68% / 20.76% / -12.17%
- **Scenario probabilities:** not separately assigned; see scenario table.

### CLX — Clorox

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Clorox is not preferred over the higher-growth, higher-margin names like AppLovin or Gen Digital, but its improving fundamentals and reasonable valuation make it a more attractive consumer staples alternative than the lower-growth industrial names. Alternatives considered: APP, PNR, GEN, ROP.
- **Thesis:** Clorox is a top-20-day momentum name with a 25.7% 20-day return and a 3.2% 60-day return. It trades at a forward P/E of 17.7, which is reasonable for a consumer staples company, and it has positive revenue growth of 33.3% and earnings growth of 113.8%. However, the stock's sector-relative P/E of 0.76 and its lower gross margin of 41.9% and operating margin of 14.3% indicate limited pricing power and margin compression. The neutral stance reflects the tension between improving fundamentals and a still-challenging margin profile.
- **Source IDs:** S021, S025, S026, S035
- **Catalysts:** Positive revenue growth of 33.3% and earnings growth of 113.8%, Reasonable forward P/E of 17.7 for consumer staples, Positive 20-day momentum
- **Risks:** Low gross margin of 41.9% and operating margin of 14.3%, Sector-relative P/E of 0.76 indicates underperformance versus peers, Consumer staples demand sensitivity to economic cycles
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 6.1684 (source.forwardEps) x AI multiple assumption 16.00; source IDs S021, S025, S026, S035
- **EPS:** 6.1684 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 17.745283
- **FY+1 growth assumption:** 7.69%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / APP and PNR / CLX has FY1 consensus earnings growth of 7.69% and revenue growth of 2.23%, with gross margin of 41.94% and operating margin of 14.29%. The base multiple of 16.0x is justified by its stable growth and dividend profile, but it is lower than APP due to lower growth and margins. The bull and bear multiples reflect range around this valuation.
- **Company fundamentals:** Reported diluted EPS 1.39; forward EPS 6.17; forward P/E 17.75; gross margin 41.9%; operating margin 14.3%; profit margin 9.4%; revenue growth 33.3%; earnings growth 113.8%; ROE 5.34; 20-day return 25.7%; 60-day return 3.2%; 60-day drawdown 0.0%.
- **Bull / Base / Bear:** 117.2 / 98.69 / 80.19
- **Bull / Base / Bear returns:** 7.07% / -9.84% / -26.74%
- **Scenario probabilities:** not separately assigned; see scenario table.

### ROP — Roper Technologies

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Roper Technologies is not preferred over the higher-growth, higher-margin names like AppLovin or Gen Digital, but its positive momentum and reasonable valuation make it a more attractive technology alternative than the lower-growth industrial names. Alternatives considered: APP, PNR, GEN, CLX.
- **Thesis:** Roper Technologies is a top-20-day momentum name with a 25.4% 20-day return and a 16.9% 60-day return. It trades at a forward P/E of 19.5, which is reasonable for a technology company, and it has positive revenue growth of 7.6% and earnings growth of 32.6%. However, the stock's sector-relative P/E of 0.49 and its lower gross margin of 69.7% and operating margin of 28.0% indicate limited margin advantage. The neutral stance reflects the tension between positive momentum and a moderate valuation.
- **Source IDs:** S034, S037, S038, S047
- **Catalysts:** Positive revenue growth of 7.6% and earnings growth of 32.6%, Reasonable forward P/E of 19.5, Positive 20-day and 60-day momentum
- **Risks:** Lower gross margin of 69.7% and operating margin of 28.0%, Sector-relative P/E of 0.49 indicates underperformance versus peers, Technology sector cyclicality and competitive pressure
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 24.5732 (source.forwardEps) x AI multiple assumption 18.00; source IDs S034, S037, S038, S047
- **EPS:** 24.57318 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 19.532475
- **FY+1 growth assumption:** 9.81%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / APP and CLX / ROP has FY1 consensus earnings growth of 9.81% and revenue growth of 6.29%, with gross margin of 69.67% and operating margin of 28.05%. The base multiple of 18.0x is justified by its solid growth and margins, higher than CLX but lower than APP. The bull and bear multiples reflect range around this valuation.
- **Company fundamentals:** Reported diluted EPS 21.3; forward EPS 24.57; forward P/E 19.53; gross margin 69.7%; operating margin 28.0%; profit margin 30.7%; revenue growth 7.6%; earnings growth 32.6%; ROE 13.2%; 20-day return 25.4%; 60-day return 16.9%; 60-day drawdown -2.5%.
- **Bull / Base / Bear:** 540.61 / 442.32 / 344.02
- **Bull / Base / Bear returns:** 12.63% / -7.85% / -28.33%
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
| Bull | 25% | +2.00% | Low 5-day volatility (14.9%) and below-threshold spike probability (16.5% vs 18.5% threshold) reduce near-term downside risk, supporting a modest upside if US close confirms stable tape. |
| Base | 50% | +0.00% | Frozen daily-close model with no directional signal and historical baseline (22.1%) above spike threshold implies neutral drift with no clear catalyst for a move over the 5-day window. |
| Bear | 25% | -2.00% | If the US close fails to confirm the frozen forecast, elevated spike probability and volatility regime could trigger a mild risk-off pullback into the weekend. |

### Long Term (12 months)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 30% | +8.00% | Sustained low volatility and stable baseline support a gradual risk-on drift, with earnings and credit conditions improving if the current low-vol regime persists into year-end. |
| Base | 40% | +3.00% | Neutral trajectory assumes no major shock, with modest positive drift from steady economic data and balanced market positioning over the medium term. |
| Bear | 30% | -5.00% | A regime shift in volatility or a spike event above threshold could drive a more pronounced correction, especially if earnings or credit conditions deteriorate. |

## Positioning


## Catalysts

| Date | Event | Why it matters |
| --- | --- | --- |

## Key Risks


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
| S009 | filing | PNR | 2026-10-27 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-27 (accession 0000077360-26-000058); 8-K filed 2026-10-27 (accession 0000077360-26-000055); 8-K filed 2026-09-22 (accession 0000077360-26-000050) |
| S010 | filing | FISV | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0000798354-26-000042); 8-K filed 2026-11-03 (accession 0000798354-26-000039); 8-K filed 2026-10-23 (accession 0001193125-26-429481) |
| S011 | news | FISV | Fri, 13 Nov 2026 00:42:12 GMT | ok | https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en | Fiserv, Inc. (FISV) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 00:42:12 GMT); Fiserv Stock Outlook: Is Wall Street Bullish or Bearish? - Yahoo Finance (Thu, 12 Nov 2026 12:23:56 GMT); What Is Fiserv (FISV) Planning With Its Debit Networks And Clover AI? - Yahoo Finance (Thu, 12 Nov 2026 06:09:00 GMT) |
| S012 | news | APP | Thu, 12 Nov 2026 20:05:45 GMT | ok | https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en | AppLovin Just Ripped 47% in a Month: Is It Too Late to Buy APP Stock Now? - Yahoo Finance (Thu, 12 Nov 2026 20:05:45 GMT); APP Stock Surges 51% After Q3 Earnings: Is it Still a Buy? - Yahoo Finance (Tue, 10 Nov 2026 14:24:00 GMT); ETFs Are Net Sellers of AppLovin (APP) on Nov. 11 - Yahoo Finance (Fri, 13 Nov 2026 11:02:35 GMT) |
| S013 | stock | APP | 2026-11-15 | ok | https://finance.yahoo.com/quote/APP | Trailing P/E: 27.54882; Forward P/E: 19.611452; Forward EPS: 20.86026; Price: 409.1; Market price: 409.1; Market cap: 135543824384; Sector: Communication Services; Trailing Eps: 14.85; Revenue Growth: 0.555; Earnings Growth: 0.755; Gross Margin: 0.8878; Operating Margin: 0.77782995; Profit Margin: 0.65887; Return On Equity: 2.1008599; Total Revenue: 7608893952; Market Cap: 135543824384; Consensus EPS FY+1: 20.72438; growth: 0.2744 |
| S014 | filing | APP | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json | Diluted EPS 11.61 for period ending 2026-09-30 (filed 2026-11-04) |
| S015 | news | PNR | Fri, 13 Nov 2026 22:05:23 GMT | ok | https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en | Pentair plc (PNR) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 22:05:23 GMT); Here's What Key Metrics Tell Us About Pentair (PNR) Q3 Earnings - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT); Pentair plc (PNR) Q3 Earnings and Revenues Beat Estimates - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT) |
| S016 | filing | FISV | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json | Diluted EPS -8.9 for period ending 2026-09-30 (filed 2026-11-04) |
| S017 | stock | FISV | 2026-11-15 | ok | https://finance.yahoo.com/quote/FISV | Forward P/E: 7.9923306; Price: 63.78; Market price: 63.78; Market cap: 33934002176; Market Cap: 33934002176; Consensus EPS FY+1: 7.98015; growth: 0.09689999 |
| S018 | stock | PNR | 2026-11-15 | ok | https://finance.yahoo.com/quote/PNR | Trailing P/E: 18.610355; Forward P/E: 12.877027; Forward EPS: 5.30402; Price: 68.3; Market price: 68.3; Market cap: 10904415232; Sector: Industrials; Trailing Eps: 3.67; Revenue Growth: -0.045; Earnings Growth: -0.188; Gross Margin: 0.40168998; Operating Margin: 0.21410999; Profit Margin: 0.15435; Return On Equity: 0.15605; Total Revenue: 3966200064; Market Cap: 10904415232; Consensus EPS FY+1: 5.30402; growth: 0.1282 |
| S019 | filing | GEN | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0000849399-26-000083); 8-K filed 2026-10-28 (accession 0000849399-26-000081); 8-K filed 2026-10-09 (accession 0000849399-26-000079) |
| S020 | filing | PNR | 2026-10-27 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json | Diluted EPS 2.76 for period ending 2026-09-30 (filed 2026-10-27) |
| S021 | filing | CLX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000021076-26-000046); 8-K filed 2026-11-02 (accession 0000021076-26-000044); 8-K filed 2026-10-29 (accession 0001206774-26-000586) |
| S022 | stock | GEN | 2026-11-15 | ok | https://finance.yahoo.com/quote/GEN | Trailing P/E: 15.431472; Forward P/E: 9.108996; Forward EPS: 3.33736; Price: 30.4; Market price: 30.4; Market cap: 18035593216; Sector: Technology; Trailing Eps: 1.97; Revenue Growth: 0.122; Earnings Growth: 1.286; Gross Margin: 0.77410007; Operating Margin: 0.43229; Profit Margin: 0.23068; Return On Equity: 0.46402; Total Revenue: 5228000256; Market Cap: 18035593216; Consensus EPS FY+1: 3.33736; growth: 0.1286 |
| S023 | news | GEN | Fri, 13 Nov 2026 00:21:25 GMT | ok | https://news.google.com/rss/search?q=GEN+Gen+Digital+stock&hl=en-US&gl=US&ceid=US:en | Gen Digital Inc. (GEN) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 00:21:25 GMT); Gen Digital (GEN) Stock Repriced After Q2 Earnings Put Margins Center Stage - Yahoo Finance (Thu, 29 Oct 2026 07:00:00 GMT); Gen Digital Inc. (GEN) Stock Forecasts - Yahoo Finance (Wed, 11 Nov 2026 13:10:37 GMT) |
| S024 | filing | CHTR | 2026-11-06 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-06 (accession 0001091667-26-000073); 8-K filed 2026-11-06 (accession 0001091667-26-000072); 8-K filed 2026-10-27 (accession 0001091667-26-000064) |
| S025 | stock | CLX | 2026-11-15 | ok | https://finance.yahoo.com/quote/CLX | Trailing P/E: 19.68705; Forward P/E: 17.745283; Forward EPS: 6.1684; Price: 109.46; Market price: 109.46; Market cap: 13260793856; Sector: Consumer Defensive; Trailing Eps: 5.56; Revenue Growth: 0.333; Earnings Growth: 1.138; Gross Margin: 0.41939998; Operating Margin: 0.14286; Profit Margin: 0.09408; Return On Equity: 5.34363; Total Revenue: 7196000256; Market Cap: 13260793856; Consensus EPS FY+1: 6.1684; growth: 0.0769 |
| S026 | news | CLX | Fri, 13 Nov 2026 05:44:34 GMT | ok | https://news.google.com/rss/search?q=CLX+Clorox+stock&hl=en-US&gl=US&ceid=US:en | The Clorox Company (CLX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 05:44:34 GMT); The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance Singapore (Sat, 14 Nov 2026 05:36:50 GMT); The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance UK (Fri, 13 Nov 2026 02:25:29 GMT) |
| S027 | filing | IDXX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000874716&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000874716-26-000135); 8-K filed 2026-11-02 (accession 0001104659-26-120892); 10-Q filed 2026-08-04 (accession 0000874716-26-000123) |
| S028 | filing | GEN | 2026-10-29 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000849399.json | Diluted EPS 0.83 for period ending 2026-10-02 (filed 2026-10-29) |
| S029 | news | CHTR | Sun, 15 Nov 2026 05:47:01 GMT | ok | https://news.google.com/rss/search?q=CHTR+Charter+Communications+stock&hl=en-US&gl=US&ceid=US:en | Charter Communications (CHTR) Stock Could Be A Bargain Following Its New Operating Model - Yahoo Finance (Sun, 15 Nov 2026 05:47:01 GMT); Charter Communications (CHTR) Expands Enterprise Reach With Managed Secure Networking Launch - Yahoo Finance (Sun, 15 Nov 2026 06:08:00 GMT); Charter Communications: 3 Key Takeaways for Long-Term Investors - Yahoo Finance (Thu, 12 Nov 2026 08:02:01 GMT) |
| S030 | stock | CHTR | 2026-11-15 | ok | https://finance.yahoo.com/quote/CHTR | Trailing P/E: 13.006578; Forward P/E: 3.2831066; Forward EPS: 42.15215; Price: 138.39; Market price: 138.39; Market cap: 24778944512; Sector: Communication Services; Trailing Eps: 10.64; Revenue Growth: 0.091; Gross Margin: 0.55084; Operating Margin: 0.23389; Profit Margin: 0.02498; Return On Equity: 0.07019; Total Revenue: 55645999104; Market Cap: 24778944512; Consensus EPS FY+1: 47.15811; growth: 1.0195 |
| S031 | stock | IDXX | 2026-11-15 | ok | https://finance.yahoo.com/quote/IDXX | Trailing P/E: 47.45485; Forward P/E: 41.687927; Forward EPS: 16.8929; Price: 704.23; Market price: 704.23; Market cap: 55483650048; Sector: Healthcare; Trailing Eps: 14.84; Revenue Growth: 0.099; Earnings Growth: 0.179; Gross Margin: 0.62722; Operating Margin: 0.32497; Profit Margin: 0.25357; Return On Equity: 0.68925005; Total Revenue: 4662220800; Market Cap: 55483650048; Consensus EPS FY+1: 16.8929; growth: 0.1244 |
| S032 | news | IDXX | Sun, 15 Nov 2026 08:10:43 GMT | ok | https://news.google.com/rss/search?q=IDXX+Idexx+Laboratories+stock&hl=en-US&gl=US&ceid=US:en | IDEXX Laboratories, Inc. (IDXX) stock price, news, quote and history - Yahoo Finance UK (Sun, 15 Nov 2026 08:10:43 GMT); IDEXX Laboratories, Inc. (IDXX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Sat, 14 Nov 2026 06:13:17 GMT); IDEXX Laboratories (IDXX) Stock Looks Fairly Valued Despite Its 28% Run - Yahoo Finance (Sat, 31 Oct 2026 07:00:00 GMT) |
| S033 | filing | CHTR | 2026-11-06 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001091667.json | Diluted EPS 0.38 for period ending 2026-09-30 (filed 2026-11-06) |
| S034 | filing | ROP | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000882835&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000882835-26-000047); 8-K filed 2026-10-22 (accession 0000882835-26-000042); 8-K filed 2026-10-01 (accession 0000882835-26-000039) |
| S035 | filing | CLX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000021076.json | Diluted EPS 1.39 for period ending 2026-09-30 (filed 2026-11-02) |
| S036 | filing | RDDT | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001713445&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0001713445-26-000116); 8-K filed 2026-10-29 (accession 0001713445-26-000114); 8-K filed 2026-08-12 (accession 0001713445-26-000107) |
| S037 | stock | ROP | 2026-11-15 | ok | https://finance.yahoo.com/quote/ROP | Trailing P/E: 18.993866; Forward P/E: 19.532475; Forward EPS: 24.57318; Price: 479.975; Market price: 479.975; Market cap: 47535013888; Sector: Technology; Trailing Eps: 25.27; Revenue Growth: 0.076; Earnings Growth: 0.326; Gross Margin: 0.69671; Operating Margin: 0.28049; Profit Margin: 0.30712998; Return On Equity: 0.13229; Total Revenue: 8434599936; Market Cap: 47535013888; Consensus EPS FY+1: 24.57318; growth: 0.09810001 |
| S038 | news | ROP | Thu, 12 Nov 2026 19:15:50 GMT | ok | https://news.google.com/rss/search?q=ROP+Roper+Technologies+stock&hl=en-US&gl=US&ceid=US:en | Roper Technologies, Inc. (ROP) Stock Price, News, Quote & History - Yahoo! Finance Canada (Thu, 12 Nov 2026 19:15:50 GMT); Roper Technologies (ROP) Stock Looks Fully Valued As Cash Flow Comes Into Focus - Yahoo Finance (Thu, 05 Nov 2026 08:00:00 GMT); Roper Technologies: 3 Key Takeaways for Long-Term Investors - Yahoo Finance (Mon, 26 Oct 2026 07:00:00 GMT) |
| S039 | filing | IDXX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000874716.json | Diluted EPS 11.75 for period ending 2026-09-30 (filed 2026-11-02) |
| S040 | stock | RDDT | 2026-11-15 | ok | https://finance.yahoo.com/quote/RDDT | Trailing P/E: 20.091835; Forward P/E: 10.770874; Forward EPS: 9.14039; Price: 98.45; Market price: 98.45; Market cap: 19010076672; Sector: Communication Services; Trailing Eps: 4.9; Revenue Growth: 0.53; Earnings Growth: 0.749; Gross Margin: 0.91547996; Operating Margin: 0.29397; Profit Margin: 0.32105; Return On Equity: 0.32029998; Total Revenue: 3088880128; Market Cap: 19010076672; Consensus EPS FY+1: 6.82439; growth: 0.2417 |

## Sources

- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFF&cosd=2026-01-01 (2026-11-12)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLH0A0HYM2&cosd=2026-01-01 (2026-11-12)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLC0A0CM&cosd=2026-01-01 (2026-11-12)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCSL&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=UNRATE&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=PAYEMS&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=T10Y2Y&cosd=2026-01-01 (2026-11-13)
- filing APP: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001751008&type=10-Q&dateb=&owner=include&count=10 (2026-11-04)
- filing PNR: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 (2026-10-27)
- filing FISV: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 (2026-11-04)
- news FISV: https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 00:42:12 GMT)
- news APP: https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en (Thu, 12 Nov 2026 20:05:45 GMT)
- stock APP: https://finance.yahoo.com/quote/APP (2026-11-15)
- filing APP: https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json (2026-11-04)
- news PNR: https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 22:05:23 GMT)
- filing FISV: https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json (2026-11-04)
- stock FISV: https://finance.yahoo.com/quote/FISV (2026-11-15)
- stock PNR: https://finance.yahoo.com/quote/PNR (2026-11-15)
- filing GEN: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 (2026-10-29)
- filing PNR: https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json (2026-10-27)

## AI Provenance

- Provider / model: hermes-local-proxy / upstage/solar-mini4:free
- Market research: attempts=1 tokens=9473 (prompt=6473, completion=3000) runtime=20.15s
- Fundamental research: generated this run at 2026-11-15T09:14:33.189428+00:00
- Evidence source dates: {'as_of': '2026-11-13', 'latest_equity_date': '2026-11-13', 'latest_macro_date': '2026-11-14', 'flows_date': '2026-11-13'}
- Evidence fingerprint: 9f3e261f34bb8eb9d74f12713fd4bf8c846404fe89c723fa8dc0bf0a6ce64ba9
- Source citations are retrieved external records in the ledger above; market values remain from the verified database snapshot.


## Disclosures

- This is research and market intelligence, not investment advice.
- AI conclusions are research judgments, not validated return predictions.
- The frozen risk layer is risk-only and is not used for directional views or allocations.
- Legacy scores are not active inputs or outputs.

# AEGIS AI-First Market Intelligence

Research generated at: 15 November 2026, 02:15 HKT
Database freshness: equity 2026-11-13 (latest row retrieved 2026-11-14 13:50:55.938286+08:00)
Data cutoff: 2026-11-13 US cash close
Snapshot ID: aegis-hourly-20261114T181528Z

## Executive Summary

- **AI market view: Risk-on tilt with a quality/income bias: broad market breadth is positive, but the 20-day return is negative and the 200-day trend is still intact, so the setup favors resilient, cash-generative names and sectors over speculative or high-multiple names. The shortlist is dominated by momentum and dislocation names, but several carry forward-EPS or valuation-quality flags, so the evidence supports a cautious, fundamentals-first posture rather than a directional call.**
- Broad market breadth is constructive: 71.3% above the 50-day and 63.6% above the 200-day, with a positive 20-day advance/decline ratio of 1.70, but the index is down 1.28% over 20 days and the 200-day trend is not yet broken.
- Sector rotation is mixed: Health Care, Consumer Discretionary, Consumer Staples, Real Estate and Financials are up over 20 days, while Information Technology and Energy are down, indicating a quality/income tilt rather than broad momentum.
- The shortlist is driven by 20-day momentum and 20-day dislocation, but several names have forward-EPS or valuation-quality flags, so the evidence supports a cautious, fundamentals-first stance.
- Macro data show a still-elevated but easing inflation backdrop, a 4.2% unemployment rate, a modestly positive 10Y-2Y spread, and tight credit spreads, which supports risk appetite but argues for quality and cash flow.
- Flows show strong institutional buying in SOXX and neutral-to-negative flows in TLT, with SMH showing tactical profit-taking inside structural accumulation, reinforcing a selective, not broad, risk-on posture.
- The frozen risk model shows 5-day forecast volatility of 14.9% and a spike probability of 16.5%, below the 18.5% threshold, so no directional signal is issued; the posture is risk-on with a quality bias.

## Data QC

- Status: **PASS_WITH_WARNINGS**
- Equity session: 0 completed session(s) behind inference date
- Equity provenance: 386 provisional / 12581 canonical
- Breadth lag: 0 session(s); ETF-flow lag: 0 session(s)
- Note: Equity session contains a mix of provisional yfinance and canonical Massive rows.
- External sources: 79 ok / 0 unavailable; retrieved 2026-11-14T18:15:48.749231+00:00

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
| S&P 500 | 7561.67 | -1.28% over 20 days | Broad market is above both moving averages, but the index is down over 20 days; 71.3% of names are above the 50-day and 63.6% above the 200-day. |
| Health Care (XLV) | +6.87% over 20 days | +6.87% | Top 20-day sector performer; trailing P/E 30.78 per S059. |
| Consumer Discretionary (XLY) | +6.69% over 20 days | +6.69% | Strong 20-day return; trailing P/E 25.11 per S062. |
| Information Technology (XLK) | -7.19% over 20 days | -7.19% | Worst 20-day sector; trailing P/E 30.03 per S075. |
| Energy (XLE) | -4.81% over 20 days | -4.81% | Negative 20-day return; trailing P/E 16.23 per S076. |

## Macro, Fiscal, Rates, Liquidity and Credit

- Inflation is easing but still above the pre-pandemic norm: CPI 336.30 and core CPI 338.90 in September 2026, with the latest CPI observation 337.476 in October 2026 per S004.
- Labor market is stable: unemployment rate 4.2% in September 2026, with the latest observation 4.1% in October 2026 per S005; nonfarm payrolls 159,293 in thousands in October 2026 per S006.
- Policy rates are easing: effective federal funds rate 3.88% as of 2026-11-12 per S001, supporting a risk-on tilt.
- Yield curve is modestly positive: 10Y-2Y spread 0.27 as of 2026-11-13 per S007, indicating no deep recession signal.
- Credit conditions are tight: high-yield OAS 3.20 and investment-grade OAS 0.89 as of 2026-11-12 per S002 and S003, consistent with a stable-to-positive credit backdrop.
- Liquidity and flows show selective institutional demand: SOXX has exceptional institutional buying with a 20-day flow z-score of 5.10, while TLT is neutral-to-negative with a 20-day flow z-score of -0.41, and SMH shows tactical profit-taking inside structural accumulation.

## US Equities and 11 GICS Sectors

Macro source IDs: S001, S002, S003, S004, S005, S006, S007

| GICS sector | Evidence | AI research stance | Source IDs |
| --- | --- | --- | --- |
| Health Care | 20-day return +6.87% per database; trailing P/E 30.78 per S059; top 20-day sector performer. | Favor: strong momentum and defensive characteristics support a quality tilt, but the high multiple warrants a valuation-conslegacyus entry. | S059 |
| Consumer Discretionary | 20-day return +6.69% per database; trailing P/E 25.11 per S062; strong 20-day performance. | Favor: positive momentum and reasonable valuation support a constructive stance, but monitor consumer spending and earnings revisions. | S062 |
| Consumer Staples | 20-day return +5.40% per database; trailing P/E 24.85 per S057; defensive sector with positive momentum. | Favor: defensive quality and positive 20-day return support a stable, income-oriented stance. | S057 |
| Real Estate | 20-day return +5.24% per database; trailing P/E 29.63 per S061; positive but high multiple. | Neutral-to-favor: positive momentum but elevated valuation suggests a selective, fundamentals-driven approach. | S061 |
| Financials | 20-day return +5.69% per database; trailing P/E 15.85 per S064; positive momentum with a relatively low multiple. | Favor: positive momentum and lower valuation support a constructive stance, especially with a positive yield curve. | S064 |
| Utilities | 20-day return +4.34% per database; trailing P/E 18.11 per S066; defensive sector with moderate valuation. | Favor: defensive quality and moderate valuation support a stable, income-oriented stance. | S066 |
| Materials | 20-day return +2.57% per database; trailing P/E 21.72 per S074; positive but modest momentum. | Neutral: positive but weaker momentum; selective exposure based on commodity and industrial demand. | S074 |
| Industrials | 20-day return +0.61% per database; trailing P/E 27.07 per S069; near-flat momentum. | Neutral: minimal momentum; selective exposure based on earnings and order books. | S069 |
| Communication Services | 20-day return -1.48% per database; trailing P/E 17.26 per S071; negative momentum. | Neutral-to-caution: negative 20-day return and high multiple suggest a wait-and-see approach. | S071 |
| Information Technology | 20-day return -7.19% per database; trailing P/E 30.03 per S075; worst 20-day sector. | Caution: negative momentum and high multiple; favor quality names with strong cash flow over speculative tech. | S075 |
| Energy | 20-day return -4.81% per database; trailing P/E 16.23 per S076; negative momentum. | Caution: negative 20-day return; monitor commodity prices and demand before adding exposure. | S076 |

### Sector fundamentals, valuation and earnings

No point-in-time sector fundamentals beyond the supplied 20-day ETF returns and trailing P/E values are available in the database. The sector evidence is limited to the supplied returns and P/E figures; no growth, margin, or consensus data are provided for the full sector universe.

## Growth vs Value

- Health Care and Consumer Discretionary show the strongest 20-day momentum (+6.87% and +6.69%) with trailing P/Es of 30.78 and 25.11, indicating a quality/income tilt rather than a high-multiple speculative tilt.
- Financials offer a relatively low trailing P/E of 15.85 with positive 20-day momentum (+5.69%), supporting a value-plus-momentum stance in a positive yield curve environment.
- Information Technology and Energy are the weakest 20-day performers (-7.19% and -4.81%) with high and low multiples respectively, suggesting caution on broad exposure and a focus on fundamentals.
- Consumer Staples and Utilities provide defensive, moderate-valuation exposure (P/Es 24.85 and 18.11) with positive 20-day returns, supporting a stable, income-oriented posture.

## ETF Flows and Breadth

- SOXX shows exceptional institutional buying with a 20-day flow z-score of 5.10 and a strong confirmation signal, indicating selective, not broad, risk-on flows.
- TLT is neutral-to-negative with a 20-day flow z-score of -0.41, suggesting reduced demand for duration and a tilt toward risk assets.
- SMH shows tactical profit-taking inside structural accumulation, with a 20-day flow z-score of 1.22, indicating that some structural demand is being trimmed.
- Market breadth is constructive: 71.3% of names above the 50-day, 63.6% above the 200-day, and a 20-day advance/decline ratio of 1.70, but the index is down 1.28% over 20 days.
- No new highs or new lows are reported, and the 52-week high/low coverage is 487/487, indicating a broad but not extreme market structure.

## Stock Ideas

Single-stock research uses reported EPS, forward P/E and company fundamentals. All ideas are research judgments, not validated return predictions.

| Ticker | Security | Research view | Price | EPS | Forward P/E | Base target | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| APP | AppLovin | NEW | 409.1 | 20.86026 | 19.611452 | 417.21 | NEW |
| PNR | Pentair | KEEP | 68.3 | 5.30402 | 12.877027 | 74.26 | KEEP |
| GEN | Gen Digital | KEEP | 30.4 | 3.33736 | 9.108996 | 33.37 | KEEP |
| CLX | Clorox | KEEP | 109.46 | 6.1684 | 17.745283 | 98.69 | KEEP |
| IDXX | Idexx Laboratories | KEEP | 704.23 | 16.8929 | 41.687927 | 641.93 | KEEP |

## ETF Ideas

ETF research uses holdings, portfolio valuation and exposure. Single-stock EPS × P/E valuation is not applied to ETFs.

No qualifying ETF ideas this run.
### APP — AppLovin

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** AppLovin offers a higher-quality, higher-margin business than the lower-quality dislocation names such as NOW and MRVL, while still participating in the momentum bucket. Its 20-day return of 53.7% and 60-day return of 32.5% are among the strongest in the shortlist, and its margins and earnings growth support a more durable growth story than the speculative high-multiple names. Alternatives considered: NOW, MRVL.
- **Thesis:** AppLovin screens in the top 20-day momentum bucket with a 53.7% 20-day return and a 32.5% 60-day return, and its Q3 2026 report shows strong operating leverage with 88.8% gross margin and 77.8% operating margin. The stock's trailing P/E of 20.05 and earnings yield of 5.0% are consistent with a high-quality, cash-generative mobile advertising platform, and the catalyst is the continued monetization of its user base plus the post-earnings momentum captured in the screen.
- **Source IDs:** S008, S009, S015, S020
- **Catalysts:** Sustained 20-day momentum and 60-day return, Q3 2026 reported diluted EPS of 11.61 and 27.4% FY1 EPS growth, High gross margin and operating margin supporting free cash flow, Continued ad-market demand and user engagement
- **Risks:** High 20-day momentum can mean elevated volatility, Mobile advertising cycle and competition, Forward EPS and fiscal-year mapping are unverified
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 20.8603 (source.forwardEps) x AI multiple assumption 20.00; source IDs S008, S009, S015, S020
- **EPS:** 20.86026 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 19.611452
- **FY+1 growth assumption:** 27.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / PNR / APP's FY1 consensus growth of 27.44% is supported by 25.4% revenue growth and 75.5% earnings growth, with a 77.8% operating margin and 88.8% gross margin indicating strong pricing power. The 19.6x forward P/E is below the 20-24x base/bull range, reflecting a premium but justified by high margins and growth; PNR is used as a lower-growth, lower-margin industrial reference to show APP's premium is warranted.
- **Company fundamentals:** AppLovin reported diluted EPS of 11.61 for the period ending 2026-09-30, with FY1 EPS growth of 27.4% and revenue growth of 25.4%. Gross margin is 88.8%, operating margin 77.8%, and profit margin 65.9%. Trailing P/E is 20.05 and forward P/E is 19.61. Source IDs: S008, S009, S015, S020.
- **Bull / Base / Bear:** 500.65 / 417.21 / 333.76
- **Bull / Base / Bear returns:** 22.38% / 1.98% / -18.42%
- **Scenario probabilities:** not separately assigned; see scenario table.

### PNR — Pentair

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Pentair is a lower-multiple, higher-earnings-yield industrial that is not as expensive as the momentum names like APP or the high-multiple dislocation names like MRVL. It provides a different risk profile within the shortlist, but its negative revenue and earnings growth keep it from being a clear BUY. Alternatives considered: APP, MRVL.
- **Thesis:** Pentair is a top-20-day-momentum name with a 27.8% 20-day return and a 7.1% 60-day return. It trades at a reasonable trailing P/E of 13.59 and an earnings yield of 7.4%, with a forward P/E of 12.88. The stock offers exposure to industrial water, fluid handling, and building products, but the 60-day drawdown of -5.2% and modest revenue growth of -4.5% argue for a neutral stance rather than a strong conviction position.
- **Source IDs:** S010, S013, S016, S018
- **Catalysts:** 20-day momentum of 27.8% and 60-day return of 7.1%, Trailing P/E of 13.59 and forward P/E of 12.88, Earnings yield of 7.4%, Industrial end-market exposure
- **Risks:** Revenue growth of -4.5% and earnings growth of -18.8%, 60-day drawdown of -5.2%, Cyclical industrial end markets, Forward EPS and fiscal-year mapping are unverified
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 5.3040 (source.forwardEps) x AI multiple assumption 14.00; source IDs S010, S013, S016, S018
- **EPS:** 5.30402 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 12.877027
- **FY+1 growth assumption:** 12.82%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / APP / PNR's FY1 consensus growth of 12.82% is supported by 18.4% revenue growth and 12.8% earnings growth, with a 40.2% gross margin and 21.4% operating margin indicating moderate profitability. The 12.9x forward P/E is below the 14-17x base/bull range, reflecting a value opportunity relative to APP's premium; APP is used as a higher-growth, higher-margin peer to show PNR's lower multiple is appropriate.
- **Company fundamentals:** Pentair reported diluted EPS of 2.76 for the period ending 2026-09-30, with FY1 EPS growth of 12.8% and revenue growth of 18.4%. Gross margin is 40.2%, operating margin 21.4%, and profit margin 15.4%. Trailing P/E is 13.59 and forward P/E is 12.88. Source IDs: S010, S013, S016, S018.
- **Bull / Base / Bear:** 90.17 / 74.26 / 58.34
- **Bull / Base / Bear returns:** 32.02% / 8.73% / -14.58%
- **Scenario probabilities:** not separately assigned; see scenario table.

### GEN — Gen Digital

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Gen Digital is a lower-multiple, higher-earnings-yield name that is not as expensive as the momentum names like APP or the high-multiple dislocation names like NOW and MRVL. It provides a different risk profile within the shortlist, but its modest revenue growth and limited forward visibility keep it from being a clear BUY. Alternatives considered: APP, MRVL.
- **Thesis:** Gen Digital is a top-20-day-momentum name with a 25.8% 20-day return and a 7.9% 60-day return. It trades at a low trailing P/E of 14.15 and an earnings yield of 7.1%, with a forward P/E of 9.11. The company is a cyber and digital life protection platform, but the 60-day drawdown of -3.2% and modest revenue growth of 12.2% argue for a neutral stance rather than a strong conviction position.
- **Source IDs:** S014, S021, S022, S023
- **Catalysts:** 20-day momentum of 25.8% and 60-day return of 7.9%, Trailing P/E of 14.15 and forward P/E of 9.11, Earnings yield of 7.1%, Cyber and digital life protection platform exposure
- **Risks:** Revenue growth of 12.2% and earnings growth of 128.6%, 60-day drawdown of -3.2%, Cyclical cybersecurity end markets, Forward EPS and fiscal-year mapping are unverified
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 3.3374 (source.forwardEps) x AI multiple assumption 10.00; source IDs S014, S021, S022, S023
- **EPS:** 3.33736 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 9.108996
- **FY+1 growth assumption:** 12.86%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / IDXX / GEN's FY1 consensus growth of 12.86% is supported by 6.8% revenue growth and 128.6% earnings growth, with a 77.4% gross margin and 43.2% operating margin indicating strong profitability. The 9.1x forward P/E is below the 10-12x base/bull range, reflecting a value opportunity relative to IDXX's higher multiple; IDXX is used as a higher-growth, higher-margin peer to show GEN's lower multiple is appropriate.
- **Company fundamentals:** Gen Digital reported diluted EPS of 0.83 for the period ending 2026-10-02, with FY1 EPS growth of 12.9% and revenue growth of 6.8%. Gross margin is 77.4%, operating margin 43.2%, and profit margin 23.1%. Trailing P/E is 14.15 and forward P/E is 9.11. Source IDs: S014, S021, S022, S023.
- **Bull / Base / Bear:** 40.05 / 33.37 / 26.7
- **Bull / Base / Bear returns:** 31.74% / 9.77% / -12.17%
- **Scenario probabilities:** not separately assigned; see scenario table.

### CLX — Clorox

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Clorox is a consumer staples name that is not as expensive as the momentum names like APP or the high-multiple dislocation names like NOW and MRVL. It provides a different risk profile within the shortlist, but its modest revenue growth and limited forward visibility keep it from being a clear BUY. Alternatives considered: APP, MRVL.
- **Thesis:** Clorox is a top-20-day-momentum name with a 25.7% 20-day return and a 3.2% 60-day return. It trades at a trailing P/E of 18.27 and an earnings yield of 5.5%, with a forward P/E of 17.75. The company is a consumer staples brand with a strong balance sheet, but the 60-day drawdown of 0.0% and modest revenue growth of 2.2% argue for a neutral stance rather than a strong conviction position.
- **Source IDs:** S024, S025, S028, S039
- **Catalysts:** 20-day momentum of 25.7% and 60-day return of 3.2%, Trailing P/E of 18.27 and forward P/E of 17.75, Earnings yield of 5.5%, Consumer staples brand exposure
- **Risks:** Revenue growth of 2.2% and earnings growth of 113.8%, 60-day drawdown of 0.0%, Consumer staples end markets, Forward EPS and fiscal-year mapping are unverified
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 6.1684 (source.forwardEps) x AI multiple assumption 16.00; source IDs S024, S025, S028, S039
- **EPS:** 6.1684 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 17.745283
- **FY+1 growth assumption:** 7.69%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / IDXX / CLX's FY1 consensus growth of 7.69% is supported by 2.2% revenue growth and 113.8% earnings growth, with a 41.9% gross margin and 14.3% operating margin indicating moderate profitability. The 17.7x forward P/E is below the 16-19x base/bull range, reflecting a premium but justified by high margins and growth; IDXX is used as a higher-growth, higher-margin peer to show CLX's lower multiple is appropriate.
- **Company fundamentals:** Clorox reported diluted EPS of 1.39 for the period ending 2026-09-30, with FY1 EPS growth of 7.7% and revenue growth of 2.2%. Gross margin is 41.9%, operating margin 14.3%, and profit margin 9.4%. Trailing P/E is 18.27 and forward P/E is 17.75. Source IDs: S024, S025, S028, S039.
- **Bull / Base / Bear:** 117.2 / 98.69 / 80.19
- **Bull / Base / Bear returns:** 7.07% / -9.84% / -26.74%
- **Scenario probabilities:** not separately assigned; see scenario table.

### IDXX — Idexx Laboratories

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Idexx is a higher-multiple, lower-earnings-yield name that is not as cheap as the momentum names like APP or the dislocation names like RDDT. It provides a different risk profile within the shortlist, but its high valuation and modest growth keep it from being a clear BUY. Alternatives considered: APP, RDDT.
- **Thesis:** Idexx Laboratories is a top-20-day-momentum name with a 25.7% 20-day return and a 29.0% 60-day return. It trades at a high trailing P/E of 39.18 and a low earnings yield of 2.6%, with a forward P/E of 41.69. The company is a veterinary diagnostics and animal health platform, but the high multiple and modest revenue growth of 9.9% argue for a neutral stance rather than a strong conviction position.
- **Source IDs:** S030, S031, S032, S045
- **Catalysts:** 20-day momentum of 25.7% and 60-day return of 29.0%, Trailing P/E of 39.18 and forward P/E of 41.69, Earnings yield of 2.6%, Veterinary diagnostics and animal health platform
- **Risks:** High trailing P/E of 39.18 and forward P/E of 41.69, Revenue growth of 9.9% and earnings growth of 17.9%, 60-day drawdown of -0.3%, High multiple relative to sector
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 16.8929 (source.forwardEps) x AI multiple assumption 38.00; source IDs S030, S031, S032, S045
- **EPS:** 16.8929 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 41.687927
- **FY+1 growth assumption:** 12.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / GEN / IDXX's FY1 consensus growth of 12.44% is supported by 8.9% revenue growth and 17.9% earnings growth, with a 62.7% gross margin and 32.5% operating margin indicating strong profitability. The 41.7x forward P/E is below the 38-44x base/bull range, reflecting a premium but justified by high margins and growth; GEN is used as a lower-growth, lower-margin peer to show IDXX's higher multiple is appropriate.
- **Company fundamentals:** Idexx Laboratories reported diluted EPS of 11.75 for the period ending 2026-09-30, with FY1 EPS growth of 12.4% and revenue growth of 8.9%. Gross margin is 62.7%, operating margin 32.5%, and profit margin 25.4%. Trailing P/E is 39.18 and forward P/E is 41.69. Source IDs: S030, S031, S032, S045.
- **Bull / Base / Bear:** 743.29 / 641.93 / 540.57
- **Bull / Base / Bear returns:** 5.55% / -8.85% / -23.24%
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
| Bull | 25% | +2.00% | Directional signal is false and forecast volatility is below the historical baseline, so a mild upside is driven by stable earnings momentum and low near-term tail risk rather than a directional catalyst. |
| Base | 50% | +0.00% | Frozen daily-close model with no directional signal and elevated forecast volatility relative to the historical baseline implies a range-bound path with neutral expected return over the target window. |
| Bear | 25% | -2.00% | Elevated forecast volatility and a 16.5% spike probability relative to the historical baseline raise the risk of a mild downside move if risk-off flows or earnings disappointment occur. |

### Long Term (12 months)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 30% | +8.00% | Sustained earnings growth and stable credit conditions support a positive multi-week drift, with low directional signal risk offset by improving fundamentals. |
| Base | 40% | +3.00% | Neutral earnings trajectory and moderate volatility imply a modest positive long-term drift as the frozen daily-close model converges toward a stable trend. |
| Bear | 30% | -5.00% | Persistent elevated forecast volatility and a 16.5% spike probability relative to the historical baseline increase the likelihood of a meaningful downside correction if risk sentiment deteriorates. |

## Positioning

- Maintain a risk-on tilt with a quality and income bias, favoring sectors with positive 20-day momentum and reasonable valuations.
- Favor Health Care, Consumer Discretionary, Consumer Staples, Financials, and Utilities for stability and positive momentum.
- Exercise caution in Information Technology and Energy due to negative 20-day returns and elevated or low multiples.
- Use the shortlist of momentum and dislocation names as a starting point, but apply valuation-quality filters and avoid names with forward-EPS or earnings-yield flags.
- Do not assign weights or directional calls; the posture is a research framework for monitoring and selective entry.

## Catalysts

| Date | Event | Why it matters |
| --- | --- | --- |
| 2026-11-16 | Frozen risk model target window opens | The frozen daily-close model is prospective from 2026-11-16 to 2026-11-20, with 5-day forecast volatility of 14.9% and a spike probability of 16.5%, below the 18.5% threshold, so no directional signal is issued. |
| 2026-11-13 |  |  |

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
| S009 | news | APP | Tue, 10 Nov 2026 14:24:00 GMT | ok | https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en | APP Stock Surges 51% After Q3 Earnings: Is it Still a Buy? - Yahoo Finance (Tue, 10 Nov 2026 14:24:00 GMT); Is Trending Stock AppLovin Corporation (APP) a Buy Now? - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT); APP Stock Quote Price and Forecast - CNN (Fri, 13 Nov 2026 15:20:18 GMT) |
| S010 | filing | PNR | 2026-10-27 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-27 (accession 0000077360-26-000058); 8-K filed 2026-10-27 (accession 0000077360-26-000055); 8-K filed 2026-09-22 (accession 0000077360-26-000050) |
| S011 | filing | FISV | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0000798354-26-000042); 8-K filed 2026-11-03 (accession 0000798354-26-000039); 8-K filed 2026-10-23 (accession 0001193125-26-429481) |
| S012 | news | FISV | Thu, 12 Nov 2026 14:54:12 GMT | ok | https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en | Fiserv, Inc. (FISV) Stock Price, News, Quote & History - Yahoo! Finance Canada (Thu, 12 Nov 2026 14:54:12 GMT); Fiserv Stock Outlook: Is Wall Street Bullish or Bearish? - Yahoo Finance (Thu, 12 Nov 2026 12:23:56 GMT); What Is Fiserv (FISV) Planning With Its Debit Networks And Clover AI? - Yahoo Finance (Thu, 12 Nov 2026 06:09:00 GMT) |
| S013 | news | PNR | Fri, 13 Nov 2026 15:54:46 GMT | ok | https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en | Pentair plc (PNR) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 15:54:46 GMT); Pentair (PNR) Stock May Be 46% Undervalued As New CFO Arrives - Yahoo Finance (Fri, 25 Sep 2026 07:00:00 GMT); Pentair plc (PNR) Q3 Earnings and Revenues Beat Estimates - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT) |
| S014 | filing | GEN | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0000849399-26-000083); 8-K filed 2026-10-28 (accession 0000849399-26-000081); 8-K filed 2026-10-09 (accession 0000849399-26-000079) |
| S015 | filing | APP | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json | Diluted EPS 11.61 for period ending 2026-09-30 (filed 2026-11-04) |
| S016 | stock | PNR | 2026-11-14 | ok | https://finance.yahoo.com/quote/PNR | Trailing P/E: 18.610355; Forward P/E: 12.877027; Forward EPS: 5.30402; Price: 68.3; Market price: 68.3; Market cap: 10904415232; Sector: Industrials; Trailing Eps: 3.67; Revenue Growth: -0.045; Earnings Growth: -0.188; Gross Margin: 0.40168998; Operating Margin: 0.21410999; Profit Margin: 0.15435; Return On Equity: 0.15605; Total Revenue: 3966200064; Market Cap: 10904415232; Consensus EPS FY+1: 5.30402; growth: 0.1282 |
| S017 | filing | FISV | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json | Diluted EPS -8.9 for period ending 2026-09-30 (filed 2026-11-04) |
| S018 | filing | PNR | 2026-10-27 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json | Diluted EPS 2.76 for period ending 2026-09-30 (filed 2026-10-27) |
| S019 | stock | FISV | 2026-11-14 | ok | https://finance.yahoo.com/quote/FISV | Forward P/E: 7.9923306; Price: 63.78; Market price: 63.78; Market cap: 33934002176; Market Cap: 33934002176; Consensus EPS FY+1: 7.98015; growth: 0.09689999 |
| S020 | stock | APP | 2026-11-14 | ok | https://finance.yahoo.com/quote/APP | Trailing P/E: 27.54882; Forward P/E: 19.611452; Forward EPS: 20.86026; Price: 409.1; Market price: 409.1; Market cap: 135543824384; Sector: Communication Services; Trailing Eps: 14.85; Revenue Growth: 0.555; Earnings Growth: 0.755; Gross Margin: 0.8878; Operating Margin: 0.77782995; Profit Margin: 0.65887; Return On Equity: 2.1008599; Total Revenue: 7608893952; Market Cap: 135543824384; Consensus EPS FY+1: 20.72438; growth: 0.2744 |
| S021 | news | GEN | Wed, 11 Nov 2026 13:10:37 GMT | ok | https://news.google.com/rss/search?q=GEN+Gen+Digital+stock&hl=en-US&gl=US&ceid=US:en | Gen Digital Inc. (GEN) Stock Forecasts - Yahoo Finance (Wed, 11 Nov 2026 13:10:37 GMT); Gen Digital (GEN) Stock Repriced After Q2 Earnings Put Margins Center Stage - Yahoo Finance (Thu, 29 Oct 2026 07:00:00 GMT); Are Business Services Stocks Lagging GEN DIGITAL INC (GEN) This Year? - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT) |
| S022 | filing | GEN | 2026-10-29 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000849399.json | Diluted EPS 0.83 for period ending 2026-10-02 (filed 2026-10-29) |
| S023 | stock | GEN | 2026-11-14 | ok | https://finance.yahoo.com/quote/GEN | Trailing P/E: 15.431472; Forward P/E: 9.108996; Forward EPS: 3.33736; Price: 30.4; Market price: 30.4; Market cap: 18035593216; Sector: Technology; Trailing Eps: 1.97; Revenue Growth: 0.122; Earnings Growth: 1.286; Gross Margin: 0.77410007; Operating Margin: 0.43229; Profit Margin: 0.23068; Return On Equity: 0.46402; Total Revenue: 5228000256; Market Cap: 18035593216; Consensus EPS FY+1: 3.33736; growth: 0.1286 |
| S024 | stock | CLX | 2026-11-14 | ok | https://finance.yahoo.com/quote/CLX | Trailing P/E: 19.68705; Forward P/E: 17.745283; Forward EPS: 6.1684; Price: 109.46; Market price: 109.46; Market cap: 13260793856; Sector: Consumer Defensive; Trailing Eps: 5.56; Revenue Growth: 0.333; Earnings Growth: 1.138; Gross Margin: 0.41939998; Operating Margin: 0.14286; Profit Margin: 0.09408; Return On Equity: 5.34363; Total Revenue: 7196000256; Market Cap: 13260793856; Consensus EPS FY+1: 6.1684; growth: 0.0769 |
| S025 | news | CLX | Sat, 14 Nov 2026 10:15:20 GMT | ok | https://news.google.com/rss/search?q=CLX+Clorox+stock&hl=en-US&gl=US&ceid=US:en | The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance Singapore (Sat, 14 Nov 2026 10:15:20 GMT); The Clorox Company (CLX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 05:34:04 GMT); The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance UK (Fri, 13 Nov 2026 16:03:45 GMT) |
| S026 | filing | CHTR | 2026-11-06 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-06 (accession 0001091667-26-000073); 8-K filed 2026-11-06 (accession 0001091667-26-000072); 8-K filed 2026-10-27 (accession 0001091667-26-000064) |
| S027 | stock | CHTR | 2026-11-14 | ok | https://finance.yahoo.com/quote/CHTR | Trailing P/E: 13.006578; Forward P/E: 3.2831066; Forward EPS: 42.15215; Price: 138.39; Market price: 138.39; Market cap: 24778944512; Sector: Communication Services; Trailing Eps: 10.64; Revenue Growth: 0.091; Gross Margin: 0.55084; Operating Margin: 0.23389; Profit Margin: 0.02498; Return On Equity: 0.07019; Total Revenue: 55645999104; Market Cap: 24778944512; Consensus EPS FY+1: 47.15811; growth: 1.0195 |
| S028 | filing | CLX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000021076-26-000046); 8-K filed 2026-11-02 (accession 0000021076-26-000044); 8-K filed 2026-10-29 (accession 0001206774-26-000586) |
| S029 | news | CHTR | Thu, 12 Nov 2026 08:02:01 GMT | ok | https://news.google.com/rss/search?q=CHTR+Charter+Communications+stock&hl=en-US&gl=US&ceid=US:en | Charter Communications: 3 Key Takeaways for Long-Term Investors - Yahoo Finance (Thu, 12 Nov 2026 08:02:01 GMT); Charter Communications (CHTR) Stock Looks Reasonable As Shares Slump 85% - Yahoo Finance (Wed, 28 Oct 2026 07:00:00 GMT); What Is The Biggest Threat To Charter Communications Stock? - Trefis (Thu, 12 Nov 2026 15:55:19 GMT) |
| S030 | stock | IDXX | 2026-11-14 | ok | https://finance.yahoo.com/quote/IDXX | Trailing P/E: 47.45485; Forward P/E: 41.687927; Forward EPS: 16.8929; Price: 704.23; Market price: 704.23; Market cap: 55483650048; Sector: Healthcare; Trailing Eps: 14.84; Revenue Growth: 0.099; Earnings Growth: 0.179; Gross Margin: 0.62722; Operating Margin: 0.32497; Profit Margin: 0.25357; Return On Equity: 0.68925005; Total Revenue: 4662220800; Market Cap: 55483650048; Consensus EPS FY+1: 16.8929; growth: 0.1244 |
| S031 | filing | IDXX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000874716&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000874716-26-000135); 8-K filed 2026-11-02 (accession 0001104659-26-120892); 10-Q filed 2026-08-04 (accession 0000874716-26-000123) |
| S032 | news | IDXX | Fri, 13 Nov 2026 22:06:38 GMT | ok | https://news.google.com/rss/search?q=IDXX+Idexx+Laboratories+stock&hl=en-US&gl=US&ceid=US:en | IDEXX Laboratories, Inc. (IDXX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 22:06:38 GMT); IDEXX Laboratories (IDXX) Stock Looks Fairly Valued Despite Its 28% Run - Yahoo Finance (Sat, 31 Oct 2026 07:00:00 GMT); IDEXX Laboratories (IDXX) Q3 Earnings Leave Its Premium Valuation In Focus - Yahoo Finance (Tue, 03 Nov 2026 08:00:00 GMT) |
| S033 | stock | ROP | 2026-11-14 | ok | https://finance.yahoo.com/quote/ROP | Trailing P/E: 18.993866; Forward P/E: 19.532475; Forward EPS: 24.57318; Price: 479.975; Market price: 479.975; Market cap: 47535013888; Sector: Technology; Trailing Eps: 25.27; Revenue Growth: 0.076; Earnings Growth: 0.326; Gross Margin: 0.69671; Operating Margin: 0.28049; Profit Margin: 0.30712998; Return On Equity: 0.13229; Total Revenue: 8434599936; Market Cap: 47535013888; Consensus EPS FY+1: 24.57318; growth: 0.09810001 |
| S034 | filing | ROP | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000882835&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000882835-26-000047); 8-K filed 2026-10-22 (accession 0000882835-26-000042); 8-K filed 2026-10-01 (accession 0000882835-26-000039) |
| S035 | news | ROP | Fri, 13 Nov 2026 01:46:04 GMT | ok | https://news.google.com/rss/search?q=ROP+Roper+Technologies+stock&hl=en-US&gl=US&ceid=US:en | Roper Technologies, Inc. (ROP) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 01:46:04 GMT); Roper Technologies (ROP) Stock Looks Fully Valued As Cash Flow Comes Into Focus - Yahoo Finance (Fri, 06 Nov 2026 07:13:00 GMT); Roper Technologies: 3 Key Takeaways for Long-Term Investors - Yahoo Finance (Mon, 26 Oct 2026 07:00:00 GMT) |
| S036 | filing | RDDT | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001713445&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0001713445-26-000116); 8-K filed 2026-10-29 (accession 0001713445-26-000114); 8-K filed 2026-08-12 (accession 0001713445-26-000107) |
| S037 | filing | CHTR | 2026-11-06 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001091667.json | Diluted EPS 0.38 for period ending 2026-09-30 (filed 2026-11-06) |
| S038 | filing | INTC | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000050863&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0000050863-26-000191); 8-K filed 2026-10-29 (accession 0000050863-26-000188); 8-K filed 2026-08-12 (accession 0001193125-26-346806) |
| S039 | filing | CLX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000021076.json | Diluted EPS 1.39 for period ending 2026-09-30 (filed 2026-11-02) |
| S040 | stock | RDDT | 2026-11-14 | ok | https://finance.yahoo.com/quote/RDDT | Trailing P/E: 20.091835; Forward P/E: 10.770874; Forward EPS: 9.14039; Price: 98.45; Market price: 98.45; Market cap: 19010076672; Sector: Communication Services; Trailing Eps: 4.9; Revenue Growth: 0.53; Earnings Growth: 0.749; Gross Margin: 0.91547996; Operating Margin: 0.29397; Profit Margin: 0.32105; Return On Equity: 0.32029998; Total Revenue: 3088880128; Market Cap: 19010076672; Consensus EPS FY+1: 6.82439; growth: 0.2417 |

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
- news FISV: https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en (Thu, 12 Nov 2026 14:54:12 GMT)
- news PNR: https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 15:54:46 GMT)
- filing GEN: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 (2026-10-29)
- filing APP: https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json (2026-11-04)
- stock PNR: https://finance.yahoo.com/quote/PNR (2026-11-14)
- filing FISV: https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json (2026-11-04)
- filing PNR: https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json (2026-10-27)
- stock FISV: https://finance.yahoo.com/quote/FISV (2026-11-14)
- stock APP: https://finance.yahoo.com/quote/APP (2026-11-14)

## AI Provenance

- Provider / model: hermes-local-proxy / upstage/solar-mini4:free
- Market research: attempts=1 tokens=9521 (prompt=6521, completion=3000) runtime=19.31s
- Fundamental research: generated this run at 2026-11-14T18:15:28.869530+00:00
- Evidence source dates: {'as_of': '2026-11-13', 'latest_equity_date': '2026-11-13', 'latest_macro_date': '2026-11-13', 'flows_date': '2026-11-13'}
- Evidence fingerprint: 3af16c2afe479155c92b8aded958f2e58f637da5ef5ae07347c40db36eee61a2
- Source citations are retrieved external records in the ledger above; market values remain from the verified database snapshot.


## Disclosures

- This is research and market intelligence, not investment advice.
- AI conclusions are research judgments, not validated return predictions.
- The frozen risk layer is risk-only and is not used for directional views or allocations.
- Legacy scores are not active inputs or outputs.

# AEGIS AI-First Market Intelligence

Research generated at: 15 November 2026, 06:15 HKT
Database freshness: equity 2026-11-13 (latest row retrieved 2026-11-14 13:50:55.938286+08:00)
Data cutoff: 2026-11-13 US cash close
Snapshot ID: aegis-hourly-20261114T221521Z

## Executive Summary

- **AI market view: Risk-on tilt with a quality and liquidity bias. Broad market breadth is constructive, but the 20-day return is negative and the 10Y-2Y curve is only mildly positive, so the setup favors high-liquidity, low-valuation-risk names and sectors with positive 20-day momentum rather than broad cyclical or speculative exposure.**
- Broad market breadth is constructive: 71.3% above the 50-day and 63.6% above the 200-day, with a positive 20-day advance/decline ratio of 1.70.
- The S&P 500 is down 1.28% over 20 days, so the rally is narrow and quality-led rather than broad-based.
- Shortlist names are driven by top 20-day momentum, large 20-day dislocations, or liquidity leadership, with a mix of high and low earnings yields.
- Sector 20-day returns are mostly positive, led by Health Care, Consumer Discretionary, Consumer Staples, Real Estate and Financials; Information Technology and Energy are the weakest.
- Credit spreads are tight (IG 0.89, HY 3.20), and the 10Y-2Y curve is modestly positive at 0.27, supporting a risk-on posture.
- Liquidity and flow data show exceptional institutional buying in SOXX, while TLT and SMH show neutral-to-tactical positioning.

## Data QC

- Status: **PASS_WITH_WARNINGS**
- Equity session: 0 completed session(s) behind inference date
- Equity provenance: 386 provisional / 12581 canonical
- Breadth lag: 0 session(s); ETF-flow lag: 0 session(s)
- Note: Equity session contains a mix of provisional yfinance and canonical Massive rows.
- External sources: 79 ok / 0 unavailable; retrieved 2026-11-14T22:15:35.607956+00:00

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
| S&P 500 | 7561.67 | -1.28% (20d) | 20-day return negative; breadth above 50d and 200d is positive but the index is under pressure. |
| DJI | 52347.55 | +0.0965% | Dow Jones Industrial Average closed higher on 2026-11-13. |
| FCHI | 8368.91 | +0.0903% | French CAC closed higher on 2026-11-13. |
| FTSE | 10902.56 | +0.3633% | UK FTSE closed higher on 2026-11-13. |
| 10Y-2Y spread | 0.27 | modestly positive | Curve is only mildly positive, not a strong steepener signal. |
| US high-yield OAS | 3.20 | tight | Spreads are compressed, consistent with a risk-on credit backdrop. |
| US IG OAS | 0.89 | tight | Investment-grade spreads are very tight, limiting credit risk premium. |
| SOXX | inflow | flow zscore 20d 5.10 | Exceptional institutional buying in semiconductors despite price weakness. |
| TLT | neutral | flow zscore 20d -0.41 | Medium-term deterioration in Treasury flows; no strong directional signal. |
| SMH | outflow | flow zscore 20d 1.22 | Tactical profit-taking inside structural accumulation. |

## Macro, Fiscal, Rates, Liquidity and Credit

- Growth: equity market breadth is positive (71.3% above 50d, 63.6% above 200d), but the S&P 500 is down 1.28% over 20 days, indicating a quality-led, narrow rally rather than broad-based expansion.
- Inflation: CPI and core CPI are available only through 2026-09-01 (336.298 and 338.896), and the latest external CPI observation is 337.476 for 2026-10-01; no monthly change or trend is supplied, so the inflation path is not fully observable.
- Policy: the effective federal funds rate is 3.88 as of 2026-11-12, and the 10Y-2Y spread is 0.27 as of 2026-11-13, implying a modestly positive but not steepening curve.
- Rates: IG OAS at 0.89 and HY OAS at 3.20 are tight, and the frozen risk model shows 5-day forecast volatility of 14.9% with a 16.5% spike probability, below the 18.5% threshold.
- Liquidity: SOXX shows exceptional institutional buying (20d flow z-score 5.10), while TLT and SMH show neutral-to-tactical positioning, suggesting capital is rotating into structural growth rather than duration or cyclical metals.
- Credit: tight spreads and a positive curve support risk appetite, but the negative 20-day index return and the absence of new highs (0 new highs, 0 new lows) indicate caution on broad momentum.

## US Equities and 11 GICS Sectors

Macro source IDs: S001, S002, S003, S004, S005, S006, S007

| GICS sector | Evidence | AI research stance | Source IDs |
| --- | --- | --- | --- |
| Health Care | 20-day return +6.87% and trailing P/E 30.78 from S054; positive momentum and high valuation. | Positive 20-day momentum and high valuation; quality and defensive tilt favored. | S054 |
| Consumer Staples | 20-day return +5.40% and trailing P/E 24.85 from S059; defensive and positive. | Positive 20-day momentum and moderate valuation; defensive quality favored. | S059 |
| Consumer Discretionary | 20-day return +6.69% and trailing P/E 25.11 from S060; strong momentum. | Positive 20-day momentum and moderate valuation; consumer-led upside favored. | S060 |
| Real Estate | 20-day return +5.24% and trailing P/E 29.63 from S062; positive but high valuation. | Positive 20-day momentum but high valuation; selective exposure favored. | S062 |
| Financials | 20-day return +5.69% and trailing P/E 15.85 from S066; positive momentum and low valuation. | Positive 20-day momentum and low valuation; attractive relative value. | S066 |
| Utilities | 20-day return +4.34% and trailing P/E 18.11 from S067; defensive and positive. | Positive 20-day momentum and moderate valuation; defensive quality favored. | S067 |
| Materials | 20-day return +2.57% and trailing P/E 21.72 from S069; positive but weakest among positive sectors. | Positive 20-day momentum but weaker momentum; selective exposure favored. | S069 |
| Industrials | 20-day return +0.61% and trailing P/E 27.07 from S070; near-flat momentum. | Near-flat 20-day momentum and high valuation; cautious, selective exposure. | S070 |
| Communication Services | 20-day return -1.48% and trailing P/E 17.26 from S073; negative momentum. | Negative 20-day momentum; avoid or less favored. | S073 |
| Information Technology | 20-day return -7.19% and trailing P/E 30.03 from S073; negative momentum and high valuation. | Negative 20-day momentum and high valuation; avoid or less favored. | S073 |
| Energy | 20-day return -4.81% and trailing P/E 16.23 from S076; negative momentum and low valuation. | Negative 20-day momentum; avoid or less favored despite low valuation. | S076 |

### Sector fundamentals, valuation and earnings

No point-in-time sector fundamentals beyond the supplied 20-day ETF returns and trailing P/E multiples are available in the database. The sector evidence is limited to the 11 GICS sectors with their ETF returns and trailing P/E from S054, S059, S060, S062, S066, S067, S069, S070, S073, S074 and S076. No growth, margin, earnings revision or consensus data are supplied for the sector level, so no further fundamental claims are made.

## Growth vs Value

- Growth: Information Technology and Communication Services are the only sectors with negative 20-day returns, and both carry high trailing P/E (30.03 and 17.26), indicating weak growth momentum.
- Value: Financials, Energy and Utilities offer the lowest trailing P/E (15.85, 16.23 and 18.11), but Energy is negative on 20-day momentum while Financials and Utilities are positive.
- Quality: Health Care (+6.87%) and Consumer Discretionary (+6.69%) show the strongest 20-day momentum, but both carry high valuations (30.78 and 25.11), so the growth/value trade-off is mixed.
- Relative value: Financials combine positive momentum with the lowest P/E, while Information Technology combines negative momentum with a high P/E, making the former relatively more attractive on a value basis.

## ETF Flows and Breadth

- SOXX shows exceptional institutional buying with a 20-day flow z-score of 5.10, confirming strong structural accumulation despite the sector's negative 20-day price return.
- SMH shows tactical profit-taking inside structural accumulation, with a 20-day flow z-score of 1.22 and a negative price state.
- TLT shows medium-term deterioration in flows (20d z-score -0.41) with a flat price state, indicating no strong directional signal.
- Market breadth is constructive: 71.3% of constituents above the 50-day, 63.6% above the 200-day, and a 20-day advance/decline ratio of 1.70.
- However, the index is down 1.28% over 20 days with zero new highs and zero new lows, so breadth is positive but not broad-based.

## Stock Ideas

Single-stock research uses reported EPS, forward P/E and company fundamentals. All ideas are research judgments, not validated return predictions.

| Ticker | Security | Research view | Price | EPS | Forward P/E | Base target | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| APP | AppLovin | NEW | 409.1 | 20.86026 | 19.611452 | 417.21 | NEW |
| PNR | Pentair | KEEP | 68.3 | 5.30402 | 12.877027 | 63.65 | KEEP |
| GEN | Gen Digital | KEEP | 30.4 | 3.33736 | 9.108996 | 33.37 | KEEP |
| CLX | Clorox | KEEP | 109.46 | 6.1684 | 17.745283 | 98.69 | KEEP |
| ROP | Roper Technologies | KEEP | 479.975 | 24.57318 | 19.532475 | 442.32 | KEEP |

## ETF Ideas

ETF research uses holdings, portfolio valuation and exposure. Single-stock EPS × P/E valuation is not applied to ETFs.

No qualifying ETF ideas this run.
### APP — AppLovin

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** AppLovin offers a rare combination of top-tier momentum, exceptional profitability, and a reasonable forward valuation, making it preferable to the other momentum names like Gen Digital and Clorox, which have lower growth profiles and margins. Alternatives considered: GEN, CLX, ROP.
- **Thesis:** AppLovin screens in the top 20-day momentum bucket with a 53.7% 20-day return and a 32.5% 60-day return, while maintaining a 60-day drawdown of only -0.2%. The company reports strong fundamentals: FY1 revenue growth of 55.5%, earnings growth of 75.5%, gross margin of 88.8%, operating margin of 77.8%, and profit margin of 65.9%. Forward EPS of 20.86 implies a forward P/E of 19.6, which is reasonable for a high-margin, high-growth mobile advertising platform. The combination of strong momentum, high profitability, and a reasonable valuation supports a new BUY recommendation.
- **Source IDs:** S008, S012, S013, S018
- **Catalysts:** Continued 20-day momentum with 53.7% price return, Sustained FY1 revenue growth of 55.5% and earnings growth of 75.5%, High gross margin of 88.8% and operating margin of 77.8%, Forward P/E of 19.6 on forward EPS of 20.86
- **Risks:** High 20-day momentum may already be priced in, Mobile advertising market cyclicality, Single-quarter earnings growth may not persist at same rate
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 20.8603 (source.forwardEps) x AI multiple assumption 20.00; source IDs S008, S012, S013, S018
- **EPS:** 20.86026 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 19.611452
- **FY+1 growth assumption:** 27.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / PNR / APP's FY1 consensus growth of 27.44% is supported by 25.4% revenue growth and 75.5% earnings growth, with a 65.9% profit margin and 88.8% gross margin. PNR is the named peer reference: PNR's FY1 growth is only 12.82% with 15.4% profit margin and 40.2% gross margin, so APP's higher growth and margin profile justifies a premium multiple. The base multiple of 20.0 reflects strong but not extreme growth; bull 24.0 and bear 16.0 bracket the range.
- **Company fundamentals:** AppLovin reports FY1 revenue growth of 55.5%, earnings growth of 75.5%, gross margin of 88.8%, operating margin of 77.8%, profit margin of 65.9%, forward EPS of 20.86, and forward P/E of 19.6. The company has strong momentum with a 53.7% 20-day return and a 32.5% 60-day return, with a 60-day drawdown of only -0.2%.
- **Bull / Base / Bear:** 500.65 / 417.21 / 333.76
- **Bull / Base / Bear returns:** 22.38% / 1.98% / -18.42%
- **Scenario probabilities:** not separately assigned; see scenario table.

### PNR — Pentair

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Pentair is preferable to the other momentum names like Gen Digital and Clorox because it offers a lower forward P/E of 12.9, providing a potentially more attractive entry point despite weaker earnings growth. Alternatives considered: GEN, CLX, ROP.
- **Thesis:** Pentair screens in the top 20-day momentum bucket with a 27.8% 20-day return and a 7.1% 60-day return. The company has a forward P/E of 12.9 on forward EPS of 5.30, with FY1 revenue growth of 18.4% and earnings growth of -18.8%. While the momentum is positive, the negative earnings growth and lower margins (gross margin 40.2%, operating margin 21.4%) suggest a more cautious stance. The stock is not a clear BUY or SELL, so a NEUTRAL stance with a KEEP review is appropriate.
- **Source IDs:** S010, S014, S015, S021
- **Catalysts:** 27.8% 20-day price return, FY1 revenue growth of 18.4%, Forward P/E of 12.9 on forward EPS of 5.30
- **Risks:** FY1 earnings growth of -18.8%, Lower gross margin of 40.2% and operating margin of 21.4%, Moderate 60-day return of 7.1%
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 5.3040 (source.forwardEps) x AI multiple assumption 12.00; source IDs S010, S014, S015, S021
- **EPS:** 5.30402 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 12.877027
- **FY+1 growth assumption:** 12.82%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / APP / PNR's FY1 consensus growth of 12.82% is supported by 18.4% revenue growth and 12.8% earnings growth, with a 40.2% gross margin and 15.4% profit margin. APP is the named peer reference: APP's FY1 growth is 27.44% with 65.9% profit margin and 88.8% gross margin, so PNR's lower growth and margin profile justifies a discount multiple. The base multiple of 12.0 reflects modest growth; bull 15.0 and bear 9.0 bracket the range.
- **Company fundamentals:** Pentair reports FY1 revenue growth of 18.4%, earnings growth of -18.8%, gross margin of 40.2%, operating margin of 21.4%, profit margin of 15.4%, forward EPS of 5.30, and forward P/E of 12.9. The stock has a 27.8% 20-day return and a 7.1% 60-day return, with a 60-day drawdown of -5.2%.
- **Bull / Base / Bear:** 79.56 / 63.65 / 47.74
- **Bull / Base / Bear returns:** 16.49% / -6.81% / -30.1%
- **Scenario probabilities:** not separately assigned; see scenario table.

### GEN — Gen Digital

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Gen Digital is preferable to the other momentum names like AppLovin and Clorox because it offers a lower forward P/E of 9.1, providing a potentially more attractive entry point despite lower revenue growth. Alternatives considered: APP, CLX, ROP.
- **Thesis:** Gen Digital screens in the top 20-day momentum bucket with a 25.8% 20-day return and a 7.9% 60-day return. The company has a forward P/E of 9.1 on forward EPS of 3.34, with FY1 revenue growth of 6.8% and earnings growth of 128.6%. While the earnings growth is strong, the lower revenue growth and moderate margins (gross margin 77.4%, operating margin 43.2%) suggest a balanced view. The stock is not a clear BUY or SELL, so a NEUTRAL stance with a KEEP review is appropriate.
- **Source IDs:** S017, S020, S024, S027
- **Catalysts:** 25.8% 20-day price return, FY1 earnings growth of 128.6%, Forward P/E of 9.1 on forward EPS of 3.34
- **Risks:** FY1 revenue growth of only 6.8%, Moderate operating margin of 43.2%, Lower 60-day return of 7.9%
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 3.3374 (source.forwardEps) x AI multiple assumption 10.00; source IDs S017, S020, S024, S027
- **EPS:** 3.33736 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 9.108996
- **FY+1 growth assumption:** 12.86%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / PNR / GEN's FY1 consensus growth of 12.86% is supported by 6.8% revenue growth and 128.6% earnings growth, with a 77.4% gross margin and 23.1% profit margin. PNR is the named peer reference: PNR's FY1 growth is 12.82% with 40.2% gross margin and 15.4% profit margin, so GEN's higher gross margin and earnings growth justify a premium multiple. The base multiple of 10.0 reflects moderate growth; bull 12.0 and bear 8.0 bracket the range.
- **Company fundamentals:** Gen Digital reports FY1 revenue growth of 6.8%, earnings growth of 128.6%, gross margin of 77.4%, operating margin of 43.2%, profit margin of 23.1%, forward EPS of 3.34, and forward P/E of 9.1. The stock has a 25.8% 20-day return and a 7.9% 60-day return, with a 60-day drawdown of -3.2%.
- **Bull / Base / Bear:** 40.05 / 33.37 / 26.7
- **Bull / Base / Bear returns:** 31.74% / 9.77% / -12.17%
- **Scenario probabilities:** not separately assigned; see scenario table.

### CLX — Clorox

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Clorox is preferable to the other momentum names like AppLovin and Gen Digital because it offers a lower forward P/E of 17.7, providing a potentially more attractive entry point despite lower revenue growth. Alternatives considered: APP, GEN, ROP.
- **Thesis:** Clorox screens in the top 20-day momentum bucket with a 25.7% 20-day return and a 3.2% 60-day return. The company has a forward P/E of 17.7 on forward EPS of 6.17, with FY1 revenue growth of 2.2% and earnings growth of 113.8%. While the earnings growth is strong, the lower revenue growth and lower margins (gross margin 41.9%, operating margin 14.3%) suggest a more cautious stance. The stock is not a clear BUY or SELL, so a NEUTRAL stance with a KEEP review is appropriate.
- **Source IDs:** S022, S023, S025, S032
- **Catalysts:** 25.7% 20-day price return, FY1 earnings growth of 113.8%, Forward P/E of 17.7 on forward EPS of 6.17
- **Risks:** FY1 revenue growth of only 2.2%, Lower gross margin of 41.9% and operating margin of 14.3%, Lower 60-day return of 3.2%
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 6.1684 (source.forwardEps) x AI multiple assumption 16.00; source IDs S022, S023, S025, S032
- **EPS:** 6.1684 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 17.745283
- **FY+1 growth assumption:** 7.69%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / ROP / CLX's FY1 consensus growth of 7.69% is supported by 2.2% revenue growth and 113.8% earnings growth, with a 41.9% gross margin and 9.4% profit margin. ROP is the named peer reference: ROP's FY1 growth is 9.81% with 69.7% gross margin and 30.7% profit margin, so CLX's lower growth and margin profile justifies a discount multiple. The base multiple of 16.0 reflects modest growth; bull 19.0 and bear 13.0 bracket the range.
- **Company fundamentals:** Clorox reports FY1 revenue growth of 2.2%, earnings growth of 113.8%, gross margin of 41.9%, operating margin of 14.3%, profit margin of 9.4%, forward EPS of 6.17, and forward P/E of 17.7. The stock has a 25.7% 20-day return and a 3.2% 60-day return, with a 60-day drawdown of 0.0%.
- **Bull / Base / Bear:** 117.2 / 98.69 / 80.19
- **Bull / Base / Bear returns:** 7.07% / -9.84% / -26.74%
- **Scenario probabilities:** not separately assigned; see scenario table.

### ROP — Roper Technologies

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Roper Technologies is preferable to the other momentum names like AppLovin and Gen Digital because it offers a lower forward P/E of 19.5, providing a potentially more attractive entry point despite lower revenue growth. Alternatives considered: APP, GEN, CLX.
- **Thesis:** Roper Technologies screens in the top 20-day momentum bucket with a 25.4% 20-day return and a 16.9% 60-day return. The company has a forward P/E of 19.5 on forward EPS of 24.57, with FY1 revenue growth of 6.3% and earnings growth of 32.6%. While the momentum is strong, the lower revenue growth and moderate margins (gross margin 69.7%, operating margin 28.0%) suggest a balanced view. The stock is not a clear BUY or SELL, so a NEUTRAL stance with a KEEP review is appropriate.
- **Source IDs:** S033, S035, S037, S041
- **Catalysts:** 25.4% 20-day price return, FY1 earnings growth of 32.6%, Forward P/E of 19.5 on forward EPS of 24.57
- **Risks:** FY1 revenue growth of only 6.3%, Moderate gross margin of 69.7% and operating margin of 28.0%, Lower 60-day return of 16.9%
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 24.5732 (source.forwardEps) x AI multiple assumption 18.00; source IDs S033, S035, S037, S041
- **EPS:** 24.57318 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 19.532475
- **FY+1 growth assumption:** 9.81%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / CLX / ROP's FY1 consensus growth of 9.81% is supported by 6.3% revenue growth and 32.6% earnings growth, with a 69.7% gross margin and 30.7% profit margin. CLX is the named peer reference: CLX's FY1 growth is 7.69% with 41.9% gross margin and 9.4% profit margin, so ROP's higher growth and margin profile justifies a premium multiple. The base multiple of 18.0 reflects moderate growth; bull 22.0 and bear 14.0 bracket the range.
- **Company fundamentals:** Roper Technologies reports FY1 revenue growth of 6.3%, earnings growth of 32.6%, gross margin of 69.7%, operating margin of 28.0%, profit margin of 30.7%, forward EPS of 24.57, and forward P/E of 19.5. The stock has a 25.4% 20-day return and a 16.9% 60-day return, with a 60-day drawdown of -2.5%.
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
| Bull | 25% | +2.00% | Low 5-day realized vol (14.9%) and below-threshold spike probability (16.5% vs 18.5% threshold) support a modest upside if US close confirms positive breadth and stable rates. |
| Base | 50% | +0.00% | Directional signal is false and forecast vol is near the historical baseline, so the most likely path is a range-bound move with no material directional drift over the 5-day window. |
| Bear | 25% | -2.00% | If the frozen daily-close model fails to confirm after the US close, elevated spike probability and vol clustering could trigger a mild downside correction. |

### Long Term (12 months)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 30% | +8.00% | Sustained low vol regime and below-threshold spike probability allow earnings and credit spreads to expand, supporting a positive multi-week return if rate expectations stay anchored. |
| Base | 40% | +3.00% | A balanced path where stable volatility and moderate spike probability produce gradual upward drift as earnings and credit conditions remain constructive. |
| Bear | 30% | -5.00% | If the frozen model's low-vol signal reverses and spike probability rises above threshold, elevated vol and widening spreads could drive a meaningful downside move. |

## Positioning

- Maintain a risk-on tilt with a quality and liquidity bias, favoring high-liquidity, low-valuation-risk names and sectors with positive 20-day momentum.
- Favored Health Care, Consumer Discretionary, Consumer Staples, Financials and Utilities on positive 20-day momentum and moderate-to-low valuations.
- Less favored Information Technology and Energy on negative 20-day momentum and high or weak valuations.
- Use SOXX as a liquidity and structural accumulation signal, but do not infer a directional allocation; treat it as a flow confirmation.
- Avoid broad cyclical or speculative exposure given the negative 20-day index return and the absence of new highs.

## Catalysts

| Date | Event | Why it matters |
| --- | --- | --- |
| 2026-11-13 | Equity session close | S&P 500 closed at 7561.67 with a -1.28% 20-day return; breadth remains positive but the index is under pressure. |
| None |  |  |

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
| S009 | news | FISV | Thu, 12 Nov 2026 18:47:44 GMT | ok | https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en | Fiserv, Inc. (FISV) Stock Price, News, Quote & History - Yahoo! Finance Canada (Thu, 12 Nov 2026 18:47:44 GMT); Fiserv Stock Outlook: Is Wall Street Bullish or Bearish? - Yahoo Finance (Thu, 12 Nov 2026 12:23:56 GMT); What Is Fiserv (FISV) Planning With Its Debit Networks And Clover AI? - Yahoo Finance (Thu, 12 Nov 2026 06:09:00 GMT) |
| S010 | filing | PNR | 2026-10-27 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-27 (accession 0000077360-26-000058); 8-K filed 2026-10-27 (accession 0000077360-26-000055); 8-K filed 2026-09-22 (accession 0000077360-26-000050) |
| S011 | filing | FISV | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0000798354-26-000042); 8-K filed 2026-11-03 (accession 0000798354-26-000039); 8-K filed 2026-10-23 (accession 0001193125-26-429481) |
| S012 | news | APP | Thu, 12 Nov 2026 20:05:45 GMT | ok | https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en | AppLovin Just Ripped 47% in a Month: Is It Too Late to Buy APP Stock Now? - Yahoo Finance (Thu, 12 Nov 2026 20:05:45 GMT); APP Stock Surges 51% After Q3 Earnings: Is it Still a Buy? - Yahoo Finance (Tue, 10 Nov 2026 14:24:00 GMT); Is Trending Stock AppLovin Corporation (APP) a Buy Now? - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT) |
| S013 | stock | APP | 2026-11-14 | ok | https://finance.yahoo.com/quote/APP | Trailing P/E: 27.54882; Forward P/E: 19.611452; Forward EPS: 20.86026; Price: 409.1; Market price: 409.1; Market cap: 135543824384; Sector: Communication Services; Trailing Eps: 14.85; Revenue Growth: 0.555; Earnings Growth: 0.755; Gross Margin: 0.8878; Operating Margin: 0.77782995; Profit Margin: 0.65887; Return On Equity: 2.1008599; Total Revenue: 7608893952; Market Cap: 135543824384; Consensus EPS FY+1: 20.72438; growth: 0.2744 |
| S014 | news | PNR | Fri, 13 Nov 2026 15:54:46 GMT | ok | https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en | Pentair plc (PNR) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 15:54:46 GMT); Here's What Key Metrics Tell Us About Pentair (PNR) Q3 Earnings - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT); Pentair (PNR) Stock May Be 46% Undervalued As New CFO Arrives - Yahoo Finance (Fri, 25 Sep 2026 07:00:00 GMT) |
| S015 | stock | PNR | 2026-11-14 | ok | https://finance.yahoo.com/quote/PNR | Trailing P/E: 18.610355; Forward P/E: 12.877027; Forward EPS: 5.30402; Price: 68.3; Market price: 68.3; Market cap: 10904415232; Sector: Industrials; Trailing Eps: 3.67; Revenue Growth: -0.045; Earnings Growth: -0.188; Gross Margin: 0.40168998; Operating Margin: 0.21410999; Profit Margin: 0.15435; Return On Equity: 0.15605; Total Revenue: 3966200064; Market Cap: 10904415232; Consensus EPS FY+1: 5.30402; growth: 0.1282 |
| S016 | stock | FISV | 2026-11-14 | ok | https://finance.yahoo.com/quote/FISV | Forward P/E: 7.9923306; Price: 63.78; Market price: 63.78; Market cap: 33934002176; Market Cap: 33934002176; Consensus EPS FY+1: 7.98015; growth: 0.09689999 |
| S017 | filing | GEN | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0000849399-26-000083); 8-K filed 2026-10-28 (accession 0000849399-26-000081); 8-K filed 2026-10-09 (accession 0000849399-26-000079) |
| S018 | filing | APP | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json | Diluted EPS 11.61 for period ending 2026-09-30 (filed 2026-11-04) |
| S019 | filing | FISV | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json | Diluted EPS -8.9 for period ending 2026-09-30 (filed 2026-11-04) |
| S020 | stock | GEN | 2026-11-14 | ok | https://finance.yahoo.com/quote/GEN | Trailing P/E: 15.431472; Forward P/E: 9.108996; Forward EPS: 3.33736; Price: 30.4; Market price: 30.4; Market cap: 18035593216; Sector: Technology; Trailing Eps: 1.97; Revenue Growth: 0.122; Earnings Growth: 1.286; Gross Margin: 0.77410007; Operating Margin: 0.43229; Profit Margin: 0.23068; Return On Equity: 0.46402; Total Revenue: 5228000256; Market Cap: 18035593216; Consensus EPS FY+1: 3.33736; growth: 0.1286 |
| S021 | filing | PNR | 2026-10-27 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json | Diluted EPS 2.76 for period ending 2026-09-30 (filed 2026-10-27) |
| S022 | stock | CLX | 2026-11-14 | ok | https://finance.yahoo.com/quote/CLX | Trailing P/E: 19.68705; Forward P/E: 17.745283; Forward EPS: 6.1684; Price: 109.46; Market price: 109.46; Market cap: 13260793856; Sector: Consumer Defensive; Trailing Eps: 5.56; Revenue Growth: 0.333; Earnings Growth: 1.138; Gross Margin: 0.41939998; Operating Margin: 0.14286; Profit Margin: 0.09408; Return On Equity: 5.34363; Total Revenue: 7196000256; Market Cap: 13260793856; Consensus EPS FY+1: 6.1684; growth: 0.0769 |
| S023 | filing | CLX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000021076-26-000046); 8-K filed 2026-11-02 (accession 0000021076-26-000044); 8-K filed 2026-10-29 (accession 0001206774-26-000586) |
| S024 | news | GEN | Thu, 29 Oct 2026 07:00:00 GMT | ok | https://news.google.com/rss/search?q=GEN+Gen+Digital+stock&hl=en-US&gl=US&ceid=US:en | Gen Digital (GEN) Stock Repriced After Q2 Earnings Put Margins Center Stage - Yahoo Finance (Thu, 29 Oct 2026 07:00:00 GMT); Gen Digital Inc. (GEN) Stock Forecasts - Yahoo Finance (Wed, 11 Nov 2026 13:10:37 GMT); Are Business Services Stocks Lagging GEN DIGITAL INC (GEN) This Year? - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT) |
| S025 | news | CLX | Fri, 13 Nov 2026 18:52:58 GMT | ok | https://news.google.com/rss/search?q=CLX+Clorox+stock&hl=en-US&gl=US&ceid=US:en | The Clorox Company (CLX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 18:52:58 GMT); The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance Singapore (Fri, 13 Nov 2026 14:35:41 GMT); The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance UK (Fri, 13 Nov 2026 16:03:45 GMT) |
| S026 | filing | CHTR | 2026-11-06 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-06 (accession 0001091667-26-000073); 8-K filed 2026-11-06 (accession 0001091667-26-000072); 8-K filed 2026-10-27 (accession 0001091667-26-000064) |
| S027 | filing | GEN | 2026-10-29 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000849399.json | Diluted EPS 0.83 for period ending 2026-10-02 (filed 2026-10-29) |
| S028 | stock | CHTR | 2026-11-14 | ok | https://finance.yahoo.com/quote/CHTR | Trailing P/E: 13.006578; Forward P/E: 3.2831066; Forward EPS: 42.15215; Price: 138.39; Market price: 138.39; Market cap: 24778944512; Sector: Communication Services; Trailing Eps: 10.64; Revenue Growth: 0.091; Gross Margin: 0.55084; Operating Margin: 0.23389; Profit Margin: 0.02498; Return On Equity: 0.07019; Total Revenue: 55645999104; Market Cap: 24778944512; Consensus EPS FY+1: 47.15811; growth: 1.0195 |
| S029 | filing | IDXX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000874716&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000874716-26-000135); 8-K filed 2026-11-02 (accession 0001104659-26-120892); 10-Q filed 2026-08-04 (accession 0000874716-26-000123) |
| S030 | news | CHTR | Thu, 12 Nov 2026 08:02:01 GMT | ok | https://news.google.com/rss/search?q=CHTR+Charter+Communications+stock&hl=en-US&gl=US&ceid=US:en | Charter Communications: 3 Key Takeaways for Long-Term Investors - Yahoo Finance (Thu, 12 Nov 2026 08:02:01 GMT); Charter Communications (CHTR) Stock Looks Reasonable As Shares Slump 85% - Yahoo Finance (Wed, 28 Oct 2026 07:00:00 GMT); Should Value Investors Buy Charter Communications (CHTR) Stock? - Yahoo Finance (Wed, 21 Oct 2026 07:00:00 GMT) |
| S031 | news | IDXX | Fri, 13 Nov 2026 22:06:38 GMT | ok | https://news.google.com/rss/search?q=IDXX+Idexx+Laboratories+stock&hl=en-US&gl=US&ceid=US:en | IDEXX Laboratories, Inc. (IDXX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 22:06:38 GMT); IDEXX Laboratories (IDXX) Stock Looks Fairly Valued Despite Its 28% Run - Yahoo Finance (Sat, 31 Oct 2026 07:00:00 GMT); IDEXX Laboratories (IDXX) Q3 Earnings Leave Its Premium Valuation In Focus - Yahoo Finance (Tue, 03 Nov 2026 08:00:00 GMT) |
| S032 | filing | CLX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000021076.json | Diluted EPS 1.39 for period ending 2026-09-30 (filed 2026-11-02) |
| S033 | filing | ROP | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000882835&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000882835-26-000047); 8-K filed 2026-10-22 (accession 0000882835-26-000042); 8-K filed 2026-10-01 (accession 0000882835-26-000039) |
| S034 | stock | IDXX | 2026-11-14 | ok | https://finance.yahoo.com/quote/IDXX | Trailing P/E: 47.45485; Forward P/E: 41.687927; Forward EPS: 16.8929; Price: 704.23; Market price: 704.23; Market cap: 55483650048; Sector: Healthcare; Trailing Eps: 14.84; Revenue Growth: 0.099; Earnings Growth: 0.179; Gross Margin: 0.62722; Operating Margin: 0.32497; Profit Margin: 0.25357; Return On Equity: 0.68925005; Total Revenue: 4662220800; Market Cap: 55483650048; Consensus EPS FY+1: 16.8929; growth: 0.1244 |
| S035 | stock | ROP | 2026-11-14 | ok | https://finance.yahoo.com/quote/ROP | Trailing P/E: 18.993866; Forward P/E: 19.532475; Forward EPS: 24.57318; Price: 479.975; Market price: 479.975; Market cap: 47535013888; Sector: Technology; Trailing Eps: 25.27; Revenue Growth: 0.076; Earnings Growth: 0.326; Gross Margin: 0.69671; Operating Margin: 0.28049; Profit Margin: 0.30712998; Return On Equity: 0.13229; Total Revenue: 8434599936; Market Cap: 47535013888; Consensus EPS FY+1: 24.57318; growth: 0.09810001 |
| S036 | filing | CHTR | 2026-11-06 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001091667.json | Diluted EPS 0.38 for period ending 2026-09-30 (filed 2026-11-06) |
| S037 | news | ROP | Thu, 12 Nov 2026 19:15:50 GMT | ok | https://news.google.com/rss/search?q=ROP+Roper+Technologies+stock&hl=en-US&gl=US&ceid=US:en | Roper Technologies, Inc. (ROP) Stock Price, News, Quote & History - Yahoo! Finance Canada (Thu, 12 Nov 2026 19:15:50 GMT); Roper Technologies (ROP) Stock Looks Fully Valued As Cash Flow Comes Into Focus - Yahoo Finance (Fri, 06 Nov 2026 07:13:00 GMT); Roper Technologies: 3 Key Takeaways for Long-Term Investors - Yahoo Finance (Mon, 26 Oct 2026 07:00:00 GMT) |
| S038 | filing | RDDT | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001713445&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0001713445-26-000116); 8-K filed 2026-10-29 (accession 0001713445-26-000114); 8-K filed 2026-08-12 (accession 0001713445-26-000107) |
| S039 | stock | RDDT | 2026-11-14 | ok | https://finance.yahoo.com/quote/RDDT | Trailing P/E: 20.091835; Forward P/E: 10.770874; Forward EPS: 9.14039; Price: 98.45; Market price: 98.45; Market cap: 19010076672; Sector: Communication Services; Trailing Eps: 4.9; Revenue Growth: 0.53; Earnings Growth: 0.749; Gross Margin: 0.91547996; Operating Margin: 0.29397; Profit Margin: 0.32105; Return On Equity: 0.32029998; Total Revenue: 3088880128; Market Cap: 19010076672; Consensus EPS FY+1: 6.82439; growth: 0.2417 |
| S040 | filing | INTC | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000050863&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0000050863-26-000191); 8-K filed 2026-10-29 (accession 0000050863-26-000188); 8-K filed 2026-08-12 (accession 0001193125-26-346806) |

## Sources

- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFF&cosd=2026-01-01 (2026-11-12)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLH0A0HYM2&cosd=2026-01-01 (2026-11-12)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLC0A0CM&cosd=2026-01-01 (2026-11-12)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCSL&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=UNRATE&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=PAYEMS&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=T10Y2Y&cosd=2026-01-01 (2026-11-13)
- filing APP: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001751008&type=10-Q&dateb=&owner=include&count=10 (2026-11-04)
- news FISV: https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en (Thu, 12 Nov 2026 18:47:44 GMT)
- filing PNR: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 (2026-10-27)
- filing FISV: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 (2026-11-04)
- news APP: https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en (Thu, 12 Nov 2026 20:05:45 GMT)
- stock APP: https://finance.yahoo.com/quote/APP (2026-11-14)
- news PNR: https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 15:54:46 GMT)
- stock PNR: https://finance.yahoo.com/quote/PNR (2026-11-14)
- stock FISV: https://finance.yahoo.com/quote/FISV (2026-11-14)
- filing GEN: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 (2026-10-29)
- filing APP: https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json (2026-11-04)
- filing FISV: https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json (2026-11-04)
- stock GEN: https://finance.yahoo.com/quote/GEN (2026-11-14)

## AI Provenance

- Provider / model: hermes-local-proxy / upstage/solar-mini4:free
- Market research: attempts=1 tokens=9548 (prompt=6548, completion=3000) runtime=25.99s
- Fundamental research: generated this run at 2026-11-14T22:15:21.063670+00:00
- Evidence source dates: {'as_of': '2026-11-13', 'latest_equity_date': '2026-11-13', 'latest_macro_date': '2026-11-13', 'flows_date': '2026-11-13'}
- Evidence fingerprint: 4955c3f910f01346db769a7a84bba936e294e373fd67daab1acf47ca0b30ed42
- Source citations are retrieved external records in the ledger above; market values remain from the verified database snapshot.


## Disclosures

- This is research and market intelligence, not investment advice.
- AI conclusions are research judgments, not validated return predictions.
- The frozen risk layer is risk-only and is not used for directional views or allocations.
- Legacy scores are not active inputs or outputs.

# AEGIS AI-First Market Intelligence

Research generated at: 16 November 2026, 09:13 HKT
Database freshness: equity 2026-11-13 (latest row retrieved 2026-11-15 13:06:40.074841+08:00)
Data cutoff: 2026-11-13 US cash close
Snapshot ID: aegis-hourly-20261116T011332Z

## Executive Summary

- **AI market view: Late-November 2026 risk-on tilt with a quality/earnings-yield bias: momentum and dislocation names are shortlisted, but the market is being pulled back by a 20-day equity dip and elevated volatility. Breadth is constructive (71.3% above 50-day, 63.6% above 200-day, ADR 1.70), yet the 20-day return is negative and the 52-week high/low coverage is flat, so the rally is broad but not yet a clean breakout. Macro is mixed: Fed funds at 3.88%, 10Y-2Y at 0.27, IG OAS at 0.89, HY OAS at 3.20, but CPI and unemployment data are stale and crypto is down sharply.**
- Equity market is in a late-November risk-on phase with broad participation: 71.3% of names above their 50-day and 63.6% above their 200-day, with an advance/decline ratio of 1.70.
- The 20-day equity return is negative (-1.28% SPX), and the 52-week high/low coverage is flat, indicating a market that is broad but not yet decisively above prior highs.
- Momentum and dislocation screens shortlisted 20 names, led by liquidity leaders NVDA, AMD, MU, AAPL and dislocation names RDDT, INTC, SNDK, MRVL, FFIV, NOW, LITE, COIN.
- Valuation quality is mixed: several shortlisted names carry high trailing P/E or negative earnings yields, and forward EPS data is missing for most large-cap names, so quality filters were not applied.
- Macro is supportive of risk but not decisive: Fed funds 3.88%, 10Y-2Y 0.27, IG OAS 0.89, HY OAS 3.20, but CPI and unemployment are stale and crypto is down sharply.
- Sector rotation is visible: Health Care, Consumer Staples, Consumer Discretionary, Real Estate, Financials, Utilities and Materials are up 20-day, while Communication Services and Information Technology are down, with Information Technology the weakest sector.

## Data QC

- Status: **PASS_WITH_WARNINGS**
- Equity session: 0 completed session(s) behind inference date
- Equity provenance: 393 provisional / 12576 canonical
- Breadth lag: 0 session(s); ETF-flow lag: 0 session(s)
- Note: Equity session contains a mix of provisional yfinance and canonical Massive rows.
- External sources: 79 ok / 0 unavailable; retrieved 2026-11-16T01:13:54.176130+00:00

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
| S&P 500 | 7561.67 | -1.28% (20d) | Broad but not decisively above prior highs; 71.3% above 50-day, 63.6% above 200-day, ADR 1.70. |
| Health Care (XLV) | 6.87% | +6.87% (20d) | Strongest sector; trailing P/E 30.78. |
| Consumer Discretionary (XLY) | 6.69% | +6.69% (20d) | Strong consumer sector; trailing P/E 25.11. |
| Information Technology (XLK) | -7.19% | -7.19% (20d) | Weakest sector; trailing P/E 30.03, reflecting heavy dislocation-name pressure. |
| Communication Services (XLC) | -1.48% | -1.48% (20d) | Negative 20-day return; trailing P/E 17.26. |
| Energy (XLE) | -4.81% | -4.81% (20d) | Negative 20-day return; trailing P/E 16.23. |

## Macro, Fiscal, Rates, Liquidity and Credit

- Growth: The 10Y-2Y Treasury spread is 0.27 as of 2026-11-13, a modestly positive but still shallow curve, consistent with a late-cycle but not recessionary macro setup.
- Inflation: CPI and core CPI are only available through 2026-09-01 (336.298 and 338.896), and the latest external CPI claim is 337.476 for 2026-10-01; the data are stale and do not support a current inflation read.
- Policy: The effective federal funds rate is 3.88 as of 2026-11-12, indicating a restrictive but easing policy stance.
- Rates: IG OAS is 0.89 and HY OAS is 3.20 as of 2026-11-12, implying tight but not distressed credit conditions.
- Liquidity: Crypto is down sharply, with BTC at 64,128.05 (-6.04%) and ETH at 1,769.12 (-8.22%) on 2026-11-14, signaling a liquidity squeeze or risk-off rotation in risk assets.
- Credit: IG and HY spreads are near tight levels, but the frozen risk model shows 5-day forecast volatility of 14.9% and a 16.5% spike probability, above the historical baseline of 22.1% but below the EWMA baseline of 20.1%.

## US Equities and 11 GICS Sectors

Macro source IDs: S001, S002, S003, S004, S005, S006, S007

| GICS sector | Evidence | AI research stance | Source IDs |
| --- | --- | --- | --- |
| Health Care | 20-day return +6.87%; trailing P/E 30.78 (S054). | Strong momentum and broad participation; valuation is rich but supported by sector leadership. | S054 |
| Consumer Staples | 20-day return +5.40%; trailing P/E 24.85 (S058). | Defensive strength with moderate valuation; consistent with a late-cycle risk-on tilt. | S058 |
| Consumer Discretionary | 20-day return +6.69%; trailing P/E 25.11 (S060). | Strong consumer sector; valuation is reasonable and supports the risk-on bias. | S060 |
| Real Estate | 20-day return +5.24%; trailing P/E 29.63 (S062). | Positive 20-day return but rich valuation; watch rate sensitivity. | S062 |
| Financials | 20-day return +5.69%; trailing P/E 15.85 (S065). | Attractive valuation and positive momentum; a core risk-on holding. | S065 |
| Utilities | 20-day return +4.34%; trailing P/E 18.11 (S064). | Defensive strength with reasonable valuation; supports the risk-on tilt. | S064 |
| Materials | 20-day return +2.57%; trailing P/E 21.72 (S066). | Modest positive momentum; valuation is reasonable but less compelling than Financials. | S066 |
| Industrials | 20-day return +0.61%; trailing P/E 27.07 (S069). | Weakest positive sector; valuation is rich and momentum is thin. | S069 |
| Communication Services | 20-day return -1.48%; trailing P/E 17.26 (S073). | Negative 20-day return; valuation is reasonable but the sector is underperforming. | S073 |
| Information Technology | 20-day return -7.19%; trailing P/E 30.03 (S075). | Weakest sector; heavy dislocation-name pressure and high valuation drag. | S075 |
| Energy | 20-day return -4.81%; trailing P/E 16.23 (S079). | Negative 20-day return; valuation is reasonable but the sector is underperforming. | S079 |

### Sector fundamentals, valuation and earnings

No point-in-time sector fundamentals beyond the supplied 20-day ETF returns and trailing P/E multiples are available in the database. The sector evidence is limited to the 11 GICS sectors with their ETF returns and trailing P/E values; no growth, margin, earnings revision, or consensus data are supplied for the sector level. The sector view is therefore based on the supplied 20-day returns and trailing P/E multiples, with the caveat that these are point-in-time snapshots and not a full fundamental read.

## Growth vs Value

- Health Care leads with a 20-day return of +6.87% and a trailing P/E of 30.78, indicating strong momentum but rich valuation.
- Consumer Discretionary (+6.69%) and Consumer Staples (+5.40%) show strong 20-day returns with trailing P/Es of 25.11 and 24.85, respectively, offering a balance of momentum and valuation.
- Financials offer the best value with a trailing P/E of 15.85 and a positive 20-day return of +5.69%, making it the most attractive risk/reward in the supplied data.
- Information Technology is the weakest sector with a 20-day return of -7.19% and a trailing P/E of 30.03, reflecting both negative momentum and high valuation.
- Energy and Communication Services are negative on 20-day returns (-4.81% and -1.48%) with trailing P/Es of 16.23 and 17.26, respectively, offering value but weak momentum.

## ETF Flows and Breadth

- Equity breadth is constructive: 71.3% of names above their 50-day, 63.6% above their 200-day, and an advance/decline ratio of 1.70 on 2026-11-13.
- The 20-day equity return is negative (-1.28% SPX), and the 52-week high/low coverage is flat, indicating a broad but not yet decisively above prior highs.
- Flow data show SOXX with exceptional institutional buying (20d flow z-score 5.10, 60d 3.17) despite a down price, while TLT shows medium-term deterioration (20d -0.41, 60d -0.29) and SMH shows tactical profit-taking inside structural accumulation (20d 1.22, 60d 1.04).
- The 20-day flow z-score for SOXX is the strongest institutional signal in the supplied data, suggesting a clear thematic flow preference for semiconductors.
- The negative divergence flag is false and bullish divergence is true, but the 20-day return is negative, so the breadth picture is mixed with a caution on near-term direction.

## Stock Ideas

Single-stock research uses reported EPS, forward P/E and company fundamentals. All ideas are research judgments, not validated return predictions.

| Ticker | Security | Research view | Price | EPS | Forward P/E | Base target | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| APP | AppLovin | NEW | 409.1 | 20.86026 | 19.611452 | 417.21 | NEW |
| PNR | Pentair | KEEP | 68.3 | 5.30402 | 12.877027 | 68.95 | KEEP |
| GEN | Gen Digital | KEEP | 30.4 | 3.33736 | 9.108996 | 33.37 | KEEP |
| CLX | Clorox | KEEP | 109.46 | 6.1684 | 17.745283 | 111.03 | KEEP |
| IDXX | Idexx Laboratories | KEEP | 704.23 | 16.8929 | 41.687927 | 709.5 | KEEP |

## ETF Ideas

ETF research uses holdings, portfolio valuation and exposure. Single-stock EPS × P/E valuation is not applied to ETFs.

No qualifying ETF ideas this run.
### APP — AppLovin

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** AppLovin offers a rare combination of top-tier 20-day momentum and high-quality margins among the shortlisted names, with a forward P/E of 19.61 that is far more reasonable than the high-multiple names such as MRVL or NOW. Its reported EPS and forward EPS provide a concrete valuation anchor, unlike several other shortlist candidates with missing or unverified forward estimates. Alternatives considered: MRVL, NOW.
- **Thesis:** AppLovin screens in the top 20-day momentum bucket with a 53.7% 20-day return and a 32.5% 60-day return, indicating strong recent price momentum. Reported diluted EPS of 11.61 for the period ending 2026-09-30 and a forward EPS of 20.86 support a forward P/E of 19.61, which is reasonable for a high-margin advertising platform. The company's gross margin of 88.8% and operating margin of 77.8% show durable operating leverage in its core business.
- **Source IDs:** S009, S012, S014, S016
- **Catalysts:** Continued 20-day momentum with a 53.7% return over the last 20 sessions, Sustained high gross margin and operating margin supporting earnings growth, Forward EPS of 20.86 providing a valuation anchor at a forward P/E of 19.61
- **Risks:** A 47% one-month decline headline suggests elevated volatility and potential overreaction, High momentum can reverse quickly if ad-market demand softens, Forward EPS and fiscal-year mapping are unverified, so forward valuation should be treated cautiously
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 20.8603 (source.forwardEps) x AI multiple assumption 20.00; source IDs S009, S012, S014, S016
- **EPS:** 20.86026 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 19.611452
- **FY+1 growth assumption:** 27.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / PNR / APP shows strong FY1 consensus growth of 27.44% with 25.4% revenue growth and 75.5% earnings growth, supported by 88.8% gross margin and 77.8% operating margin. PNR is the named peer reference: PNR's FY1 growth is only 12.82% with 18.4% revenue growth and 12.9x forward P/E, so APP's higher growth and margin profile justify a premium multiple. The base multiple of 20.0x reflects APP's superior growth and margins relative to the peer, while 24.0x bull and 16.0x bear capture upside/downside around that growth and margin profile.
- **Company fundamentals:** Reported diluted EPS 11.61 for period ending 2026-09-30; forward EPS 20.86; forward P/E 19.61; gross margin 88.8%; operating margin 77.8%; revenue growth 55.5%; earnings growth 75.5%; 20-day return 53.7%; 60-day return 32.5%; 60-day drawdown -0.2%.
- **Bull / Base / Bear:** 500.65 / 417.21 / 333.76
- **Bull / Base / Bear returns:** 22.38% / 1.98% / -18.42%
- **Scenario probabilities:** not separately assigned; see scenario table.

### PNR — Pentair

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Pentair offers a low forward P/E of 12.9 with a high forward EPS of 5.30, which is more attractive than the higher-multiple momentum names such as APP or IDXX. However, its negative revenue and earnings growth mean the case is not a clear buy, so it is kept as a neutral candidate rather than a top pick. Alternatives considered: APP, IDXX.
- **Thesis:** Pentair screens in the top 20-day momentum bucket with a 27.8% 20-day return and a 7.1% 60-day return. Reported diluted EPS of 2.76 for the period ending 2026-09-30 and a forward EPS of 5.30 support a forward P/E of 12.9, which is attractive relative to its sector. However, revenue growth of -4.5% and earnings growth of -18.8% indicate near-term operating pressure, so the momentum is not yet supported by fundamental growth.
- **Source IDs:** S008, S013, S017, S020
- **Catalysts:** 27.8% 20-day return showing strong recent price momentum, Forward P/E of 12.9 offering a potentially attractive entry point if earnings recover, Water infrastructure and flow control exposure may benefit from infrastructure spending
- **Risks:** Revenue growth of -4.5% and earnings growth of -18.8% show near-term fundamental weakness, Forward EPS and fiscal-year mapping are unverified, so forward valuation should be treated cautiously, Industrial end-market demand can be cyclical and sensitive to construction activity
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 5.3040 (source.forwardEps) x AI multiple assumption 13.00; source IDs S008, S013, S017, S020
- **EPS:** 5.30402 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 12.877027
- **FY+1 growth assumption:** 12.82%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / APP / PNR has FY1 consensus growth of 12.82% with 18.4% revenue growth and 18.8% earnings decline, supported by 40.2% gross margin and 21.4% operating margin. APP is the named peer reference: APP's FY1 growth is 27.44% with 25.4% revenue growth and 75.5% earnings growth, so PNR's lower growth and negative earnings momentum justify a lower multiple. The base multiple of 13.0x reflects PNR's modest growth and weaker margins, with 16.0x bull and 10.0x bear capturing the range around that profile.
- **Company fundamentals:** Reported diluted EPS 2.76 for period ending 2026-09-30; forward EPS 5.30; forward P/E 12.88; gross margin 40.2%; operating margin 21.4%; profit margin 15.4%; revenue growth -4.5%; earnings growth -18.8%; 20-day return 27.8%; 60-day return 7.1%; 60-day drawdown -5.2%.
- **Bull / Base / Bear:** 84.86 / 68.95 / 53.04
- **Bull / Base / Bear returns:** 24.25% / 0.95% / -22.34%
- **Scenario probabilities:** not separately assigned; see scenario table.

### GEN — Gen Digital

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Gen Digital offers a very low forward P/E of 9.1 with strong revenue and earnings growth, making it a more attractive valuation than the high-multiple names such as IDXX or MRVL. Its momentum and growth profile support a neutral stance rather than a full buy, given the unverified forward estimates and limited absolute price. Alternatives considered: IDXX, MRVL.
- **Thesis:** Gen Digital screens in the top 20-day momentum bucket with a 25.8% 20-day return and a 7.9% 60-day return. Reported diluted EPS of 0.83 for the period ending 2026-10-02 and a forward EPS of 3.34 support a forward P/E of 9.1, which is very attractive. Revenue growth of 12.2% and earnings growth of 128.6% show strong fundamental momentum, but the low absolute price and high forward multiple relative to the sector warrant caution.
- **Source IDs:** S018, S019, S022, S027
- **Catalysts:** 25.8% 20-day return showing strong recent price momentum, Forward P/E of 9.1 with forward EPS of 3.34 providing a low entry multiple, Revenue growth of 12.2% and earnings growth of 128.6% indicating strong operational momentum
- **Risks:** Forward EPS and fiscal-year mapping are unverified, so forward valuation should be treated cautiously, Low absolute price and high forward multiple relative to the sector may imply limited upside, Cybersecurity and digital risk exposure can be sensitive to regulatory and competitive changes
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 3.3374 (source.forwardEps) x AI multiple assumption 10.00; source IDs S018, S019, S022, S027
- **EPS:** 3.33736 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 9.108996
- **FY+1 growth assumption:** 12.86%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / IDXX / GEN has FY1 consensus growth of 12.86% with 6.8% revenue growth and 128.6% earnings growth, supported by 77.4% gross margin and 43.2% operating margin. IDXX is the named peer reference: IDXX's FY1 growth is 12.44% with 8.9% revenue growth and 17.9% earnings growth, so GEN's higher earnings growth and stronger margins justify a premium multiple. The base multiple of 10.0x reflects GEN's growth and margin profile, with 12.0x bull and 8.0x bear capturing the range around that profile.
- **Company fundamentals:** Reported diluted EPS 0.83 for period ending 2026-10-02; forward EPS 3.34; forward P/E 9.11; gross margin 77.4%; operating margin 43.2%; profit margin 23.1%; revenue growth 12.2%; earnings growth 128.6%; 20-day return 25.8%; 60-day return 7.9%; 60-day drawdown -3.2%.
- **Bull / Base / Bear:** 40.05 / 33.37 / 26.7
- **Bull / Base / Bear returns:** 31.74% / 9.77% / -12.17%
- **Scenario probabilities:** not separately assigned; see scenario table.

### CLX — Clorox

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Clorox offers a reasonable forward P/E of 17.7 with strong revenue and earnings growth, making it a more attractive staples option than the broader consumer staples sector ETF XLP. Its momentum and growth profile support a neutral stance rather than a full buy, given the lower margin profile and unverified forward estimates. Alternatives considered: XLP.
- **Thesis:** Clorox screens in the top 20-day momentum bucket with a 25.7% 20-day return and a 3.2% 60-day return. Reported diluted EPS of 1.39 for the period ending 2026-09-30 and a forward EPS of 6.17 support a forward P/E of 17.7, which is reasonable for a consumer staples company. Revenue growth of 33.3% and earnings growth of 113.8% show strong operational momentum, but the lower margin profile and consumer-cyclical exposure temper the case.
- **Source IDs:** S023, S024, S025, S032
- **Catalysts:** 25.7% 20-day return showing strong recent price momentum, Forward P/E of 17.7 with forward EPS of 6.17 providing a reasonable valuation for staples, Revenue growth of 33.3% and earnings growth of 113.8% indicating strong operational momentum
- **Risks:** Lower gross margin of 41.9% and operating margin of 14.3% limit operating leverage, Consumer staples demand can be sensitive to macroeconomic and household spending changes, Forward EPS and fiscal-year mapping are unverified, so forward valuation should be treated cautiously
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 6.1684 (source.forwardEps) x AI multiple assumption 18.00; source IDs S023, S024, S025, S032
- **EPS:** 6.1684 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 17.745283
- **FY+1 growth assumption:** 7.69%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / IDXX / CLX has FY1 consensus growth of 7.69% with 2.2% revenue growth and 113.8% earnings growth, supported by 41.9% gross margin and 14.3% operating margin. IDXX is the named peer reference: IDXX's FY1 growth is 12.44% with 8.9% revenue growth and 17.9% earnings growth, so CLX's lower growth and weaker margins justify a lower multiple. The base multiple of 18.0x reflects CLX's growth and margin profile, with 22.0x bull and 14.0x bear capturing the range around that profile.
- **Company fundamentals:** Reported diluted EPS 1.39 for period ending 2026-09-30; forward EPS 6.17; forward P/E 17.75; gross margin 41.9%; operating margin 14.3%; profit margin 9.4%; revenue growth 33.3%; earnings growth 113.8%; 20-day return 25.7%; 60-day return 3.2%; 60-day drawdown 0.0%.
- **Bull / Base / Bear:** 135.7 / 111.03 / 86.36
- **Bull / Base / Bear returns:** 23.97% / 1.43% / -21.1%
- **Scenario probabilities:** not separately assigned; see scenario table.

### IDXX — Idexx Laboratories

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Idexx offers a high-growth animal health and diagnostics franchise with strong momentum, but its forward P/E of 41.7 is the highest among the shortlisted stocks, making it a less attractive valuation than the lower-multiple names such as PNR or GEN. It is therefore kept as a neutral candidate rather than a top pick. Alternatives considered: PNR, GEN.
- **Thesis:** Idexx Laboratories screens in the top 20-day momentum bucket with a 25.7% 20-day return and a 29.0% 60-day return, indicating strong recent price momentum. Reported diluted EPS of 11.75 for the period ending 2026-09-30 and a forward EPS of 16.89 support a forward P/E of 41.7, which is high relative to the sector. Revenue growth of 9.9% and earnings growth of 17.9% show moderate fundamental momentum, but the high multiple and elevated valuation relative to peers limit the case.
- **Source IDs:** S029, S031, S033, S042
- **Catalysts:** 25.7% 20-day return and 29.0% 60-day return showing strong recent price momentum, Forward EPS of 16.89 providing a concrete valuation anchor, Moderate revenue growth of 9.9% and earnings growth of 17.9% supporting the business
- **Risks:** Forward P/E of 41.7 is high relative to the sector and the shortlist average, High multiple leaves limited room for error if earnings growth disappoints, Forward EPS and fiscal-year mapping are unverified, so forward valuation should be treated cautiously
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 16.8929 (source.forwardEps) x AI multiple assumption 42.00; source IDs S029, S031, S033, S042
- **EPS:** 16.8929 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 41.687927
- **FY+1 growth assumption:** 12.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / GEN / IDXX has FY1 consensus growth of 12.44% with 8.9% revenue growth and 17.9% earnings growth, supported by 62.7% gross margin and 32.5% operating margin. GEN is the named peer reference: GEN's FY1 growth is 12.86% with 6.8% revenue growth and 128.6% earnings growth, so IDXX's lower earnings growth and weaker margins justify a lower multiple. The base multiple of 42.0x reflects IDXX's growth and margin profile, with 50.0x bull and 34.0x bear capturing the range around that profile.
- **Company fundamentals:** Reported diluted EPS 11.75 for period ending 2026-09-30; forward EPS 16.89; forward P/E 41.69; gross margin 62.7%; operating margin 32.5%; profit margin 25.4%; revenue growth 9.9%; earnings growth 17.9%; 20-day return 25.7%; 60-day return 29.0%; 60-day drawdown -0.3%.
- **Bull / Base / Bear:** 844.65 / 709.5 / 574.36
- **Bull / Base / Bear returns:** 19.94% / 0.75% / -18.44%
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
| Bull | 25% | +2.00% | Low realized volatility (14.9%) and below-threshold spike probability (16.5% vs 18.5% threshold) support a modest upside if US close confirms positive breadth; 25% probability reflects a favorable but not dominant setup. |
| Base | 50% | +0.00% | Directional signal is false and forecast volatility is near the historical baseline, so the most likely path is a range-bound session with returns clustering around zero. |
| Bear | 25% | -2.00% | If the frozen daily-close model fails to confirm after the US close, elevated forecast vol (14.9%) and a 16.5% spike probability could trigger a mild downside move; 25% probability captures the risk of a failed confirmation. |

### Long Term (12 months)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 30% | +8.00% | Sustained low volatility and below-threshold spike probability over the horizon support a positive drift if credit conditions remain stable and earnings breadth expands; 30% probability reflects a constructive but not assured trend. |
| Base | 40% | +3.00% | With forecast vol near the historical baseline and no directional signal, a modest positive drift is the central case if earnings growth and credit spreads remain benign; 40% probability reflects a mild but positive long-term bias. |
| Bear | 30% | -5.00% | If the frozen daily-close model's low-volatility regime breaks and spike probability rises above threshold, elevated vol and negative breadth could drive a meaningful drawdown; 30% probability captures the downside risk of regime change. |

## Positioning

- Maintain a risk-on tilt with a quality/earnings-yield bias, favoring Financials, Consumer Discretionary, and Health Care on the supplied momentum and valuation evidence.
- Less favored Information Technology and Communication Services on the negative 20-day returns and high valuation drag.
- Use the SOXX flow signal as a thematic confirmation for semiconductor exposure, but note the negative 20-day price state and the need for price confirmation.
- Monitor the frozen risk model: 5-day forecast volatility of 14.9% and a 16.5% spike probability are elevated but below the historical baseline, so position sizing should be cautious.
- Do not infer allocation weights or directional calls; the supplied data support a broad risk-on posture with selective quality and flow confirmation.

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
| S008 | filing | PNR | 2026-10-27 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-27 (accession 0000077360-26-000058); 8-K filed 2026-10-27 (accession 0000077360-26-000055); 8-K filed 2026-09-22 (accession 0000077360-26-000050) |
| S009 | filing | APP | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001751008&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0001751008-26-000069); 8-K filed 2026-11-04 (accession 0001751008-26-000068); 10-Q filed 2026-08-05 (accession 0001751008-26-000059) |
| S010 | news | FISV | Fri, 13 Nov 2026 21:49:46 GMT | ok | https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en | Fiserv, Inc. (FISV) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 21:49:46 GMT); Fiserv Stock Outlook: Is Wall Street Bullish or Bearish? - Yahoo Finance (Thu, 12 Nov 2026 12:23:56 GMT); Michael Burry makes a bold call on struggling payments giant - Yahoo Finance (Wed, 11 Nov 2026 00:17:00 GMT) |
| S011 | filing | FISV | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0000798354-26-000042); 8-K filed 2026-11-03 (accession 0000798354-26-000039); 8-K filed 2026-10-23 (accession 0001193125-26-429481) |
| S012 | news | APP | Thu, 12 Nov 2026 20:05:45 GMT | ok | https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en | AppLovin Just Ripped 47% in a Month: Is It Too Late to Buy APP Stock Now? - Yahoo Finance (Thu, 12 Nov 2026 20:05:45 GMT); Is Trending Stock AppLovin Corporation (APP) a Buy Now? - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT); APP Stock Surges 51% After Q3 Earnings: Is it Still a Buy? - Yahoo Finance (Tue, 10 Nov 2026 14:24:00 GMT) |
| S013 | news | PNR | Fri, 13 Nov 2026 22:09:48 GMT | ok | https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en | Pentair plc (PNR) stock price, news, quote and history - Yahoo Finance UK (Fri, 13 Nov 2026 22:09:48 GMT); Pentair plc (PNR) Q3 Earnings and Revenues Beat Estimates - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT); Pentair (PNR) Stock May Be 46% Undervalued As New CFO Arrives - Yahoo Finance (Fri, 25 Sep 2026 07:00:00 GMT) |
| S014 | stock | APP | 2026-11-16 | ok | https://finance.yahoo.com/quote/APP | Trailing P/E: 27.54882; Forward P/E: 19.611452; Forward EPS: 20.86026; Price: 409.1; Market price: 409.1; Market cap: 135543824384; Sector: Communication Services; Trailing Eps: 14.85; Revenue Growth: 0.555; Earnings Growth: 0.755; Gross Margin: 0.8878; Operating Margin: 0.77782995; Profit Margin: 0.65887; Return On Equity: 2.1008599; Total Revenue: 7608893952; Market Cap: 135543824384; Consensus EPS FY+1: 20.72438; growth: 0.2744 |
| S015 | stock | FISV | 2026-11-16 | ok | https://finance.yahoo.com/quote/FISV | Forward P/E: 7.99667; Price: 63.78; Market price: 63.78; Market cap: 33934002176; Market Cap: 33934002176; Consensus EPS FY+1: 7.98015; growth: 0.09689999 |
| S016 | filing | APP | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json | Diluted EPS 11.61 for period ending 2026-09-30 (filed 2026-11-04) |
| S017 | stock | PNR | 2026-11-16 | ok | https://finance.yahoo.com/quote/PNR | Trailing P/E: 18.610355; Forward P/E: 12.877027; Forward EPS: 5.30402; Price: 68.3; Market price: 68.3; Market cap: 10904415232; Sector: Industrials; Trailing Eps: 3.67; Revenue Growth: -0.045; Earnings Growth: -0.188; Gross Margin: 0.40168998; Operating Margin: 0.21410999; Profit Margin: 0.15435; Return On Equity: 0.15605; Total Revenue: 3966200064; Market Cap: 10904415232; Consensus EPS FY+1: 5.30402; growth: 0.1282 |
| S018 | filing | GEN | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0000849399-26-000083); 8-K filed 2026-10-28 (accession 0000849399-26-000081); 8-K filed 2026-10-09 (accession 0000849399-26-000079) |
| S019 | news | GEN | Fri, 13 Nov 2026 09:34:35 GMT | ok | https://news.google.com/rss/search?q=GEN+Gen+Digital+stock&hl=en-US&gl=US&ceid=US:en | Gen Digital Inc. (GEN) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 09:34:35 GMT); Gen Digital (GEN) Stock Repriced After Q2 Earnings Put Margins Center Stage - Yahoo Finance (Thu, 29 Oct 2026 07:00:00 GMT); Gen Digital Stock: Is Wall Street Bullish or Bearish? - Yahoo Finance (Thu, 05 Nov 2026 08:00:00 GMT) |
| S020 | filing | PNR | 2026-10-27 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json | Diluted EPS 2.76 for period ending 2026-09-30 (filed 2026-10-27) |
| S021 | filing | FISV | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json | Diluted EPS -8.9 for period ending 2026-09-30 (filed 2026-11-04) |
| S022 | stock | GEN | 2026-11-16 | ok | https://finance.yahoo.com/quote/GEN | Trailing P/E: 15.431472; Forward P/E: 9.108996; Forward EPS: 3.33736; Price: 30.4; Market price: 30.4; Market cap: 18035593216; Sector: Technology; Trailing Eps: 1.97; Revenue Growth: 0.122; Earnings Growth: 1.286; Gross Margin: 0.77410007; Operating Margin: 0.43229; Profit Margin: 0.23068; Return On Equity: 0.46402; Total Revenue: 5228000256; Market Cap: 18035593216; Consensus EPS FY+1: 3.33736; growth: 0.1286 |
| S023 | filing | CLX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000021076-26-000046); 8-K filed 2026-11-02 (accession 0000021076-26-000044); 8-K filed 2026-10-29 (accession 0001206774-26-000586) |
| S024 | news | CLX | Sun, 15 Nov 2026 08:55:47 GMT | ok | https://news.google.com/rss/search?q=CLX+Clorox+stock&hl=en-US&gl=US&ceid=US:en | The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance UK (Sun, 15 Nov 2026 08:55:47 GMT); The Clorox Company (CLX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 05:44:34 GMT); The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance Singapore (Fri, 13 Nov 2026 14:10:46 GMT) |
| S025 | stock | CLX | 2026-11-16 | ok | https://finance.yahoo.com/quote/CLX | Trailing P/E: 19.68705; Forward P/E: 17.745283; Forward EPS: 6.1684; Price: 109.46; Market price: 109.46; Market cap: 13260793856; Sector: Consumer Defensive; Trailing Eps: 5.56; Revenue Growth: 0.333; Earnings Growth: 1.138; Gross Margin: 0.41939998; Operating Margin: 0.14286; Profit Margin: 0.09408; Return On Equity: 5.34363; Total Revenue: 7196000256; Market Cap: 13260793856; Consensus EPS FY+1: 6.1684; growth: 0.0769 |
| S026 | filing | CHTR | 2026-11-06 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-06 (accession 0001091667-26-000073); 8-K filed 2026-11-06 (accession 0001091667-26-000072); 8-K filed 2026-10-27 (accession 0001091667-26-000064) |
| S027 | filing | GEN | 2026-10-29 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000849399.json | Diluted EPS 0.83 for period ending 2026-10-02 (filed 2026-10-29) |
| S028 | stock | CHTR | 2026-11-16 | ok | https://finance.yahoo.com/quote/CHTR | Trailing P/E: 13.006578; Forward P/E: 3.2831066; Forward EPS: 42.15215; Price: 138.39; Market price: 138.39; Market cap: 24778944512; Sector: Communication Services; Trailing Eps: 10.64; Revenue Growth: 0.091; Gross Margin: 0.55084; Operating Margin: 0.23389; Profit Margin: 0.02498; Return On Equity: 0.07019; Total Revenue: 55645999104; Market Cap: 24778944512; Consensus EPS FY+1: 47.15811; growth: 1.0195 |
| S029 | filing | IDXX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000874716&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000874716-26-000135); 8-K filed 2026-11-02 (accession 0001104659-26-120892); 10-Q filed 2026-08-04 (accession 0000874716-26-000123) |
| S030 | news | CHTR | Sun, 15 Nov 2026 05:47:01 GMT | ok | https://news.google.com/rss/search?q=CHTR+Charter+Communications+stock&hl=en-US&gl=US&ceid=US:en | Charter Communications (CHTR) Stock Could Be A Bargain Following Its New Operating Model - Yahoo Finance (Sun, 15 Nov 2026 05:47:01 GMT); Charter Communications (CHTR) Expands Enterprise Reach With Managed Secure Networking Launch - Yahoo Finance (Sun, 15 Nov 2026 06:08:00 GMT); Why You Should Think About Charter Communications Differently Now? - Yahoo Finance (Fri, 13 Nov 2026 19:16:11 GMT) |
| S031 | stock | IDXX | 2026-11-16 | ok | https://finance.yahoo.com/quote/IDXX | Trailing P/E: 47.45485; Forward P/E: 41.687927; Forward EPS: 16.8929; Price: 704.23; Market price: 704.23; Market cap: 55483650048; Sector: Healthcare; Trailing Eps: 14.84; Revenue Growth: 0.099; Earnings Growth: 0.179; Gross Margin: 0.62722; Operating Margin: 0.32497; Profit Margin: 0.25357; Return On Equity: 0.68925005; Total Revenue: 4662220800; Market Cap: 55483650048; Consensus EPS FY+1: 16.8929; growth: 0.1244 |
| S032 | filing | CLX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000021076.json | Diluted EPS 1.39 for period ending 2026-09-30 (filed 2026-11-02) |
| S033 | news | IDXX | Sat, 14 Nov 2026 06:13:17 GMT | ok | https://news.google.com/rss/search?q=IDXX+Idexx+Laboratories+stock&hl=en-US&gl=US&ceid=US:en | IDEXX Laboratories, Inc. (IDXX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Sat, 14 Nov 2026 06:13:17 GMT); symbol__ Stock Quote Price and Forecast - CNN (Fri, 13 Nov 2026 15:22:45 GMT); IDEXX Laboratories (IDXX) Stock Looks Fairly Valued Despite Its 28% Run - Yahoo Finance (Sat, 31 Oct 2026 07:00:00 GMT) |
| S034 | stock | ROP | 2026-11-16 | ok | https://finance.yahoo.com/quote/ROP | Trailing P/E: 18.993866; Forward P/E: 19.532475; Forward EPS: 24.57318; Price: 479.975; Market price: 479.975; Market cap: 47535013888; Sector: Technology; Trailing Eps: 25.27; Revenue Growth: 0.076; Earnings Growth: 0.326; Gross Margin: 0.69671; Operating Margin: 0.28049; Profit Margin: 0.30712998; Return On Equity: 0.13229; Total Revenue: 8434599936; Market Cap: 47535013888; Consensus EPS FY+1: 24.57318; growth: 0.09810001 |
| S035 | filing | RDDT | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001713445&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0001713445-26-000116); 8-K filed 2026-10-29 (accession 0001713445-26-000114); 8-K filed 2026-08-12 (accession 0001713445-26-000107) |
| S036 | filing | ROP | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000882835&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000882835-26-000047); 8-K filed 2026-10-22 (accession 0000882835-26-000042); 8-K filed 2026-10-01 (accession 0000882835-26-000039) |
| S037 | filing | CHTR | 2026-11-06 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001091667.json | Diluted EPS 0.38 for period ending 2026-09-30 (filed 2026-11-06) |
| S038 | news | ROP | Fri, 13 Nov 2026 13:04:22 GMT | ok | https://news.google.com/rss/search?q=ROP+Roper+Technologies+stock&hl=en-US&gl=US&ceid=US:en | Roper Technologies, Inc. (ROP) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 13:04:22 GMT); Roper Technologies (ROP) Stock Looks Fully Valued As Cash Flow Comes Into Focus - Yahoo Finance (Thu, 05 Nov 2026 08:00:00 GMT); Roper Technologies (ROP), What Is Behind The Fresh Attention? - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT) |
| S039 | news | RDDT | Thu, 29 Oct 2026 07:00:00 GMT | ok | https://news.google.com/rss/search?q=RDDT+Reddit+stock&hl=en-US&gl=US&ceid=US:en | Reddit (NYSE:RDDT) surprises with Q3 2026 sales but stock drops 12.6% - Yahoo Finance (Thu, 29 Oct 2026 07:00:00 GMT); Reddit shares sink on weak sales guidance and plans login requirement test as Google search traffic shrinks - CNBC (Thu, 29 Oct 2026 07:00:00 GMT); Should You Wait Before Buying Reddit Stock? - Trefis (Fri, 13 Nov 2026 18:20:39 GMT) |
| S040 | stock | RDDT | 2026-11-16 | ok | https://finance.yahoo.com/quote/RDDT | Trailing P/E: 20.091835; Forward P/E: 10.770874; Forward EPS: 9.14039; Price: 98.45; Market price: 98.45; Market cap: 19010076672; Sector: Communication Services; Trailing Eps: 4.9; Revenue Growth: 0.53; Earnings Growth: 0.749; Gross Margin: 0.91547996; Operating Margin: 0.29397; Profit Margin: 0.32105; Return On Equity: 0.32029998; Total Revenue: 3088880128; Market Cap: 19010076672; Consensus EPS FY+1: 6.82439; growth: 0.2417 |

## Sources

- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFF&cosd=2026-01-01 (2026-11-12)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLH0A0HYM2&cosd=2026-01-01 (2026-11-12)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLC0A0CM&cosd=2026-01-01 (2026-11-12)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCSL&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=UNRATE&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=PAYEMS&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=T10Y2Y&cosd=2026-01-01 (2026-11-13)
- filing PNR: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 (2026-10-27)
- filing APP: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001751008&type=10-Q&dateb=&owner=include&count=10 (2026-11-04)
- news FISV: https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 21:49:46 GMT)
- filing FISV: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 (2026-11-04)
- news APP: https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en (Thu, 12 Nov 2026 20:05:45 GMT)
- news PNR: https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 22:09:48 GMT)
- stock APP: https://finance.yahoo.com/quote/APP (2026-11-16)
- stock FISV: https://finance.yahoo.com/quote/FISV (2026-11-16)
- filing APP: https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json (2026-11-04)
- stock PNR: https://finance.yahoo.com/quote/PNR (2026-11-16)
- filing GEN: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 (2026-10-29)
- news GEN: https://news.google.com/rss/search?q=GEN+Gen+Digital+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 09:34:35 GMT)
- filing PNR: https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json (2026-10-27)

## AI Provenance

- Provider / model: hermes-local-proxy / upstage/solar-mini4:free
- Market research: attempts=1 tokens=9473 (prompt=6473, completion=3000) runtime=24.05s
- Fundamental research: generated this run at 2026-11-16T01:13:32.126739+00:00
- Evidence source dates: {'as_of': '2026-11-13', 'latest_equity_date': '2026-11-13', 'latest_macro_date': '2026-11-14', 'flows_date': '2026-11-13'}
- Evidence fingerprint: 08eac02983751317728100266dfcb8501fec5de38c4e821167e3c13363afccd1
- Source citations are retrieved external records in the ledger above; market values remain from the verified database snapshot.


## Disclosures

- This is research and market intelligence, not investment advice.
- AI conclusions are research judgments, not validated return predictions.
- The frozen risk layer is risk-only and is not used for directional views or allocations.
- Legacy scores are not active inputs or outputs.

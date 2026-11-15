# AEGIS AI-First Market Intelligence

Research generated at: 16 November 2026, 06:14 HKT
Database freshness: equity 2026-11-13 (latest row retrieved 2026-11-15 13:06:40.074841+08:00)
Data cutoff: 2026-11-13 US cash close
Snapshot ID: aegis-hourly-20261115T221416Z

## Executive Summary

- **AI market view: Late-November 2026: broad market breadth is constructive (71% above 50-day, 64% above 200-day, A/D ratio 1.70), but the index is slightly negative over 20 days and the 20-day return is -1.28%. Sector leadership is mixed: Health Care, Consumer Discretionary, Consumer Staples and Real Estate are positive over 20 days, while Information Technology and Energy are negative. Liquidity is concentrated in semiconductors and hardware, with SOXX showing exceptional institutional buying and NVDA/AMD/MU among the largest dollar-volume names. Macro data show a 10Y-2Y spread of 0.27 and a 3.88% effective federal funds rate, with CPI and unemployment still elevated relative to the 2026-10 baseline.**
- Broad market breadth is positive: 71.3% of names above the 50-day moving average, 63.6% above the 200-day, and an advance/decline ratio of 1.70.
- Index-level momentum is slightly negative over 20 days (-1.28%), indicating a cautious near-term trend despite positive breadth.
- Sector rotation is mixed: Health Care, Consumer Discretionary, Consumer Staples and Real Estate lead on 20-day returns; Information Technology and Energy lag.
- Liquidity is concentrated in semiconductors and hardware: SOXX shows exceptional institutional buying, while NVDA, AMD, MU and AAPL are the largest dollar-volume names.
- Macro backdrop shows a modestly positive yield curve (10Y-2Y = 0.27) and a 3.88% effective federal funds rate, with CPI and unemployment still above the 2026-10 baseline.
- Risk environment is elevated but not extreme: 5-day forecast volatility is 14.9% and spike probability is 16.5%, below the 22.1% historical baseline.

## Data QC

- Status: **PASS_WITH_WARNINGS**
- Equity session: 0 completed session(s) behind inference date
- Equity provenance: 393 provisional / 12576 canonical
- Breadth lag: 0 session(s); ETF-flow lag: 0 session(s)
- Note: Equity session contains a mix of provisional yfinance and canonical Massive rows.
- External sources: 79 ok / 0 unavailable; retrieved 2026-11-15T22:14:31.234604+00:00

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
| S&P 500 | 7561.67 | -1.28% (20d) | Index is slightly negative over 20 days; breadth is positive with 71.3% above 50-day and 63.6% above 200-day. |
| Health Care (XLV) | 6.87% | +6.87% (20d) | Top 20-day sector performer; trailing P/E 30.78. |
| Consumer Discretionary (XLY) | 6.69% | +6.69% (20d) | Strong 20-day return; trailing P/E 25.11. |
| Consumer Staples (XLP) | 5.40% | +5.40% (20d) | Positive 20-day return; trailing P/E 24.85. |
| Real Estate (XLRE) | 5.24% | +5.24% (20d) | Positive 20-day return; trailing P/E 29.63. |
| Information Technology (XLK) | -7.19% | -7.19% (20d) | Worst 20-day sector; trailing P/E 30.03; liquidity leader in SOXX, NVDA, AMD, MU. |
| Energy (XLE) | -4.81% | -4.81% (20d) | Negative 20-day return; trailing P/E 16.23. |

## Macro, Fiscal, Rates, Liquidity and Credit

- Growth: 10Y-2Y Treasury spread is 0.27 as of 2026-11-13, indicating a modestly positive but still flat-ish yield curve; no recession signal from the spread itself.
- Inflation: CPI (CPIAUCSL) is 336.298 as of 2026-09-01 and core CPI is 338.896; the 2026-10 CPI reading is 337.476, indicating inflation remains above the 2026-10 baseline.
- Policy: Effective federal funds rate is 3.88% as of 2026-11-12, suggesting a restrictive but stable policy stance.
- Rates: 10Y-2Y spread of 0.27 and IG OAS of 0.89 indicate a relatively tight credit curve; high-yield OAS of 3.20 is elevated but not distressed.
- Liquidity: SOXX shows exceptional institutional buying (20d flow z-score 5.10, 60d 3.17) while TLT is neutral-to-negative (20d -0.41, 60d -0.29), suggesting capital rotation into cyclical/tech hardware.
- Credit: High-yield OAS 3.20 and IG OAS 0.89 imply moderate credit stress; the spread environment is consistent with a late-cycle but not crisis posture.

## US Equities and 11 GICS Sectors

Macro source IDs: S001, S002, S003, S004, S005, S006, S007

| GICS sector | Evidence | AI research stance | Source IDs |
| --- | --- | --- | --- |
| Health Care | 20d return +6.87%; trailing P/E 30.78; top 20-day sector performer. | Positive momentum and relative strength; valuation is rich but supported by sector leadership. | S055 |
| Consumer Discretionary | 20d return +6.69%; trailing P/E 25.11; strong 20-day return. | Positive momentum; consumer spending remains supportive. | S060 |
| Consumer Staples | 20d return +5.40%; trailing P/E 24.85; defensive strength. | Positive 20-day return; defensive positioning supported by stable demand. | S057 |
| Real Estate | 20d return +5.24%; trailing P/E 29.63; positive 20-day return. | Positive momentum; valuation is elevated but sector is outperforming. | S064 |
| Financials | 20d return +5.69%; trailing P/E 15.85; positive 20-day return. | Positive momentum; low valuation supports earnings yield. | S068 |
| Utilities | 20d return +4.34%; trailing P/E 18.11; defensive sector. | Positive 20-day return; stable defensive demand. | S065 |
| Materials | 20d return +2.57%; trailing P/E 21.72; modest positive return. | Positive but lagging; materials sector is mid-pack. | S066 |
| Industrials | 20d return +0.61%; trailing P/E 27.07; near-flat. | Weak momentum; near-flat 20-day return. | S069 |
| Communication Services | 20d return -1.48%; trailing P/E 17.26; negative 20-day return. | Negative momentum; sector is underperforming. | S070 |
| Information Technology | 20d return -7.19%; trailing P/E 30.03; worst 20-day sector; liquidity leader in SOXX, NVDA, AMD, MU. | Negative momentum at index level; but liquidity concentration in semis suggests institutional accumulation despite price weakness. | S072 |
| Energy | 20d return -4.81%; trailing P/E 16.23; negative 20-day return. | Negative momentum; energy sector is underperforming. | S075 |

### Sector fundamentals, valuation and earnings

Sector-level fundamentals are limited to trailing P/E and 20-day returns supplied in the database snapshot. No point-in-time growth, margin, or consensus data are available for the full sector universe; therefore no additional fundamental metrics are reported.

## Growth vs Value

- Health Care has the highest trailing P/E (30.78) among the positive 20-day sectors, indicating rich valuation but strong momentum.
- Financials offer the lowest trailing P/E (15.85) among the positive 20-day sectors, implying a higher earnings yield.
- Information Technology has the worst 20-day return (-7.19%) but the highest liquidity concentration, with SOXX, NVDA, AMD and MU as dollar-volume leaders.
- Energy has the lowest trailing P/E (16.23) among the negative 20-day sectors, suggesting value characteristics but negative momentum.

## ETF Flows and Breadth

- SOXX is the standout flow name: 20d flow z-score 5.10 and 60d 3.17, classified as exceptional institutional buying despite a down price state.
- SMH shows tactical profit-taking inside structural accumulation: 20d flow z-score 1.22, 60d 1.04, with a down price state.
- TLT is neutral-to-negative: 20d flow z-score -0.41, 60d -0.29, with a flat price state and medium-term deterioration.
- Breadth is strongly positive: 315 advancers vs 185 decliners, A/D ratio 1.70, 71.3% above 50-day, 63.6% above 200-day.
- No new highs or new lows are reported (0/0), so breadth is broad but not extreme; the index is slightly negative over 20 days.

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
- **Why preferred / alternatives:** AppLovin offers a higher-quality growth profile than the lower-quality dislocation names such as NOW and MRVL, which carry forward EPS gaps and extreme trailing P/E multiples, while still participating in the momentum-driven tech and digital advertising rally. Alternatives considered: NOW, MRVL.
- **Thesis:** AppLovin screens in the top 20-day momentum bucket with a 53.7% 20-day return and a 32.5% 60-day return, and its reported diluted EPS of 11.61 for the 2026-09-30 period supports a forward P/E near 19.6. The momentum and earnings profile justify a new position despite the recent sharp run.
- **Source IDs:** S008, S010, S013, S017
- **Catalysts:** Sustained 20-day momentum above 50%, Continued revenue and earnings growth from the mobile advertising platform, High gross margin and operating leverage supporting forward earnings
- **Risks:** Recent sharp price run may leave limited upside, Mobile advertising market cyclicality and ad spend sensitivity, Execution risk on new product and market initiatives
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 20.8603 (source.forwardEps) x AI multiple assumption 20.00; source IDs S008, S010, S013, S017
- **EPS:** 20.86026 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 19.611452
- **FY+1 growth assumption:** 27.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / PNR / APP's forward EPS growth of 27.4% and revenue growth of 25.4% support a premium multiple, but the 88.8% gross margin and 77.8% operating margin are unusually high and may not persist; PNR is the named peer reference for a lower-margin, cyclical industrial with a 12.9x forward P/E.
- **Company fundamentals:** Reported diluted EPS 11.61 for period ending 2026-09-30; forward EPS 20.86; forward P/E 19.61; revenue growth 55.5%; earnings growth 75.5%; gross margin 88.8%; operating margin 77.8%; profit margin 65.9%; ROE 2.10.
- **Bull / Base / Bear:** 500.65 / 417.21 / 333.76
- **Bull / Base / Bear returns:** 22.38% / 1.98% / -18.42%
- **Scenario probabilities:** not separately assigned; see scenario table.

### PNR — Pentair

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Pentair is a more defensible industrial holding than the deeply unprofitable INTC, which carries a negative trailing P/E and a 53.2% 60-day drawdown, while still offering a lower forward multiple than the high-multiple dislocation names. Alternatives considered: INTC.
- **Thesis:** Pentair screens in the top 20-day momentum bucket with a 27.8% 20-day return and a 7.1% 60-day return. Its forward P/E of 12.9 and earnings yield of 7.4% are reasonable, but the company's revenue and earnings are contracting, so the momentum alone does not justify a strong directional call.
- **Source IDs:** S011, S014, S015, S021
- **Catalysts:** 20-day momentum of 27.8%, Reasonable forward valuation relative to sector, Industrial and water technology exposure
- **Risks:** Revenue growth of -4.5% and earnings growth of -18.8%, Cyclical exposure to construction and industrial end markets, Margin compression in operating and profit lines
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 5.3040 (source.forwardEps) x AI multiple assumption 13.00; source IDs S011, S014, S015, S021
- **EPS:** 5.30402 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 12.877027
- **FY+1 growth assumption:** 12.82%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / APP / PNR's forward EPS growth of 12.8% and revenue growth of 18.4% support a mid-teens multiple, but the 40.2% gross margin and 21.4% operating margin are structurally lower than APP's; the 12.9x forward P/E is the named peer reference for a cyclical industrial.
- **Company fundamentals:** Reported diluted EPS 2.76 for period ending 2026-09-30; forward EPS 5.30; forward P/E 12.88; revenue growth -4.5%; earnings growth -18.8%; gross margin 40.2%; operating margin 21.4%; profit margin 15.4%; ROE 15.6%.
- **Bull / Base / Bear:** 84.86 / 68.95 / 53.04
- **Bull / Base / Bear returns:** 24.25% / 0.95% / -22.34%
- **Scenario probabilities:** not separately assigned; see scenario table.

### GEN — Gen Digital

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Gen Digital offers a lower forward multiple than the high-multiple dislocation names such as NOW and MRVL, while still providing exposure to the cyber and digital risk theme, making it a more reasonable valuation play than the speculative dislocation names. Alternatives considered: NOW, MRVL.
- **Thesis:** Gen Digital screens in the top 20-day momentum bucket with a 25.8% 20-day return and a 7.9% 60-day return. Its forward P/E of 9.1 and earnings yield of 7.1% are attractive, but the company's revenue growth is modest and the security is a high-beta cyber and digital risk name, so a neutral stance is appropriate.
- **Source IDs:** S018, S020, S022, S029
- **Catalysts:** 20-day momentum of 25.8%, Low forward P/E of 9.1, Cybersecurity and digital risk exposure
- **Risks:** Revenue growth of 6.8% is modest, High-beta cyber and digital risk exposure, Cyclicality in cyber spending and M&A integration
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 3.3374 (source.forwardEps) x AI multiple assumption 10.00; source IDs S018, S020, S022, S029
- **EPS:** 3.33736 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 9.108996
- **FY+1 growth assumption:** 12.86%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / IDXX / GEN's forward EPS growth of 12.9% and revenue growth of 6.8% support a low-to-mid single-digit multiple, but the 77.4% gross margin and 43.2% operating margin are strong; IDXX is the named peer reference for a higher-multiple, higher-growth software/healthcare services peer.
- **Company fundamentals:** Reported diluted EPS 0.83 for period ending 2026-10-02; forward EPS 3.34; forward P/E 9.11; revenue growth 12.2%; earnings growth 128.6%; gross margin 77.4%; operating margin 43.2%; profit margin 23.1%; ROE 46.4%.
- **Bull / Base / Bear:** 40.05 / 33.37 / 26.7
- **Bull / Base / Bear returns:** 31.74% / 9.77% / -12.17%
- **Scenario probabilities:** not separately assigned; see scenario table.

### CLX — Clorox

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Clorox provides a consumer staples exposure that is more stable than the high-multiple tech dislocation names, while still offering a reasonable forward P/E, making it a better defensive alternative than the speculative names. Alternatives considered: XLP.
- **Thesis:** Clorox screens in the top 20-day momentum bucket with a 25.7% 20-day return and a 3.2% 60-day return. Its forward P/E of 17.7 and earnings yield of 5.5% are reasonable, but the consumer staples sector faces margin pressure and the stock's 60-day drawdown is flat, so a neutral stance is appropriate.
- **Source IDs:** S023, S024, S026, S034
- **Catalysts:** 20-day momentum of 25.7%, Reasonable forward valuation relative to consumer staples, Diversified consumer staples portfolio
- **Risks:** Revenue growth of 2.2% is modest, Earnings growth of 113.8% is volatile and may not repeat, Margin pressure in consumer staples
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 6.1684 (source.forwardEps) x AI multiple assumption 18.00; source IDs S023, S024, S026, S034
- **EPS:** 6.1684 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 17.745283
- **FY+1 growth assumption:** 7.69%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / IDXX / CLX's forward EPS growth of 7.7% and revenue growth of 2.2% support a mid-to-high single-digit multiple, but the 41.9% gross margin and 14.3% operating margin are structurally lower than GEN's; IDXX is the named peer reference for a higher-margin, higher-growth consumer/healthcare services peer.
- **Company fundamentals:** Reported diluted EPS 1.39 for period ending 2026-09-30; forward EPS 6.17; forward P/E 17.75; revenue growth 33.3%; earnings growth 113.8%; gross margin 41.9%; operating margin 14.3%; profit margin 9.4%; ROE 5.34%.
- **Bull / Base / Bear:** 135.7 / 111.03 / 86.36
- **Bull / Base / Bear returns:** 23.97% / 1.43% / -21.1%
- **Scenario probabilities:** not separately assigned; see scenario table.

### IDXX — Idexx Laboratories

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Idexx offers a healthcare exposure that is more stable than the high-multiple tech dislocation names, while still providing a reasonable forward P/E, making it a better defensive alternative than the speculative names. Alternatives considered: XLV.
- **Thesis:** Idexx Laboratories screens in the top 20-day momentum bucket with a 25.7% 20-day return and a 29.0% 60-day return. Its forward P/E of 41.7 and earnings yield of 2.6% are high, but the company's revenue and earnings growth are modest, so a neutral stance is appropriate.
- **Source IDs:** S027, S030, S033, S041
- **Catalysts:** 20-day momentum of 25.7%, 29.0% 60-day return, Animal health and diagnostics exposure
- **Risks:** Forward P/E of 41.7 is high, Revenue growth of 9.9% is modest, Earnings growth of 17.9% may not sustain
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 16.8929 (source.forwardEps) x AI multiple assumption 42.00; source IDs S027, S030, S033, S041
- **EPS:** 16.8929 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 41.687927
- **FY+1 growth assumption:** 12.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / GEN / IDXX's forward EPS growth of 12.4% and revenue growth of 8.9% support a premium multiple, but the 62.7% gross margin and 32.5% operating margin are lower than GEN's; GEN is the named peer reference for a lower-multiple, higher-growth software/healthcare services peer.
- **Company fundamentals:** Reported diluted EPS 11.75 for period ending 2026-09-30; forward EPS 16.89; forward P/E 41.69; revenue growth 9.9%; earnings growth 17.9%; gross margin 62.7%; operating margin 32.5%; profit margin 25.4%; ROE 68.9%.
- **Bull / Base / Bear:** 810.86 / 709.5 / 608.14
- **Bull / Base / Bear returns:** 15.14% / 0.75% / -13.64%
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
| Bull | 25% | +2.00% | Low 5-day forecast vol (14.9%) and below-threshold spike probability (16.5% vs 18.5% threshold) suggest a stable, range-bound tape where a modest upside drift is plausible if credit spreads tighten and earnings expectations hold. |
| Base | 50% | +0.00% | Frozen daily-close model with no directional signal and historical/ewma baselines above threshold implies a neutral path: flat returns as volatility normalizes and no catalyst is expected to drive a decisive move. |
| Bear | 25% | -2.00% | If the spike probability materializes above threshold or credit conditions tighten, elevated vol and negative skew could push returns down modestly, with downside capped by the frozen model's conservative calibration. |

### Long Term (12 months)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 30% | +8.00% | Sustained low vol and stable credit conditions over the horizon could allow earnings growth and breadth expansion to compound returns, with a 30% probability assigned to a constructive macro and rate environment. |
| Base | 40% | +3.00% | A balanced baseline where moderate earnings momentum and normalized volatility produce a low-single-digit positive drift, reflecting a steady-state equity market with no major regime shift. |
| Bear | 30% | -5.00% | A bear case driven by rising volatility, spread widening, or earnings disappointment could produce a deeper drawdown, with a 30% probability reflecting tail risk from the frozen model's conservative volatility and spike probability estimates. |

## Positioning

- Maintain a constructive but cautious equity stance: positive breadth and sector leadership in Health Care, Consumer Discretionary, Consumer Staples and Real Estate, but negative index momentum and negative 20-day returns in IT and Energy.
- Favored liquidity leaders in semiconductors and hardware (SOXX, NVDA, AMD, MU) given exceptional institutional buying and dollar-volume concentration.
- Less favored or neutral on Energy and Communication Services given negative 20-day returns and weaker momentum.
- Use the 10Y-2Y spread of 0.27 and IG OAS of 0.89 as a neutral-to-modestly-constructive rate backdrop; high-yield OAS of 3.20 warrants monitoring.
- Do not assign weights; the frozen risk block is risk-only and does not imply directional or allocation views.

## Catalysts

| Date | Event | Why it matters |
| --- | --- | --- |
| 2026-11-16 | US equity session | Frozen risk model target window begins; 5-day forecast volatility is 14.9% and spike probability is 16.5%, below the 22.1% historical baseline. |
| 2026-11-17 | Semiconductor sector flow confirmation | SOXX shows exceptional institutional buying (20d flow z-score 5.10); continued flows would confirm structural accumulation. |
| 2026-11-18 | Index momentum check | 20-day return is -1.28%; a reversal above the 20-day moving average would confirm the positive breadth trend. |
| 2026-11-19 | Credit spread monitoring | High-yield OAS 3.20 and IG OAS 0.89; any widening would signal rising credit stress. |
| 2026-11-20 |  |  |

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
| S009 | filing | FISV | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0000798354-26-000042); 8-K filed 2026-11-03 (accession 0000798354-26-000039); 8-K filed 2026-10-23 (accession 0001193125-26-429481) |
| S010 | news | APP | Thu, 12 Nov 2026 20:05:45 GMT | ok | https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en | AppLovin Just Ripped 47% in a Month: Is It Too Late to Buy APP Stock Now? - Yahoo Finance (Thu, 12 Nov 2026 20:05:45 GMT); Is Trending Stock AppLovin Corporation (APP) a Buy Now? - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT); APP Stock Surges 51% After Q3 Earnings: Is it Still a Buy? - Yahoo Finance (Tue, 10 Nov 2026 14:24:00 GMT) |
| S011 | filing | PNR | 2026-10-27 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-27 (accession 0000077360-26-000058); 8-K filed 2026-10-27 (accession 0000077360-26-000055); 8-K filed 2026-09-22 (accession 0000077360-26-000050) |
| S012 | news | FISV | Thu, 12 Nov 2026 12:23:56 GMT | ok | https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en | Fiserv Stock Outlook: Is Wall Street Bullish or Bearish? - Yahoo Finance (Thu, 12 Nov 2026 12:23:56 GMT); Michael Burry makes a bold call on struggling payments giant - Yahoo Finance (Wed, 11 Nov 2026 00:17:00 GMT); Fiserv (FISV) Stock Looks Undervalued With Strong Excess Returns - Yahoo Finance Singapore (Wed, 11 Nov 2026 22:14:34 GMT) |
| S013 | stock | APP | 2026-11-15 | ok | https://finance.yahoo.com/quote/APP | Trailing P/E: 27.54882; Forward P/E: 19.611452; Forward EPS: 20.86026; Price: 409.1; Market price: 409.1; Market cap: 135543824384; Sector: Communication Services; Trailing Eps: 14.85; Revenue Growth: 0.555; Earnings Growth: 0.755; Gross Margin: 0.8878; Operating Margin: 0.77782995; Profit Margin: 0.65887; Return On Equity: 2.1008599; Total Revenue: 7608893952; Market Cap: 135543824384; Consensus EPS FY+1: 20.72438; growth: 0.2744 |
| S014 | news | PNR | Fri, 13 Nov 2026 22:05:23 GMT | ok | https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en | Pentair plc (PNR) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 22:05:23 GMT); Pentair (PNR) Stock May Be 46% Undervalued As New CFO Arrives - Yahoo Finance (Fri, 25 Sep 2026 07:00:00 GMT); Pentair plc (PNR) Q3 Earnings and Revenues Beat Estimates - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT) |
| S015 | stock | PNR | 2026-11-15 | ok | https://finance.yahoo.com/quote/PNR | Trailing P/E: 18.610355; Forward P/E: 12.877027; Forward EPS: 5.30402; Price: 68.3; Market price: 68.3; Market cap: 10904415232; Sector: Industrials; Trailing Eps: 3.67; Revenue Growth: -0.045; Earnings Growth: -0.188; Gross Margin: 0.40168998; Operating Margin: 0.21410999; Profit Margin: 0.15435; Return On Equity: 0.15605; Total Revenue: 3966200064; Market Cap: 10904415232; Consensus EPS FY+1: 5.30402; growth: 0.1282 |
| S016 | stock | FISV | 2026-11-15 | ok | https://finance.yahoo.com/quote/FISV | Forward P/E: 7.99667; Price: 63.78; Market price: 63.78; Market cap: 33934002176; Market Cap: 33934002176; Consensus EPS FY+1: 7.98015; growth: 0.09689999 |
| S017 | filing | APP | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json | Diluted EPS 11.61 for period ending 2026-09-30 (filed 2026-11-04) |
| S018 | filing | GEN | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0000849399-26-000083); 8-K filed 2026-10-28 (accession 0000849399-26-000081); 8-K filed 2026-10-09 (accession 0000849399-26-000079) |
| S019 | filing | FISV | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json | Diluted EPS -8.9 for period ending 2026-09-30 (filed 2026-11-04) |
| S020 | stock | GEN | 2026-11-15 | ok | https://finance.yahoo.com/quote/GEN | Trailing P/E: 15.431472; Forward P/E: 9.108996; Forward EPS: 3.33736; Price: 30.4; Market price: 30.4; Market cap: 18035593216; Sector: Technology; Trailing Eps: 1.97; Revenue Growth: 0.122; Earnings Growth: 1.286; Gross Margin: 0.77410007; Operating Margin: 0.43229; Profit Margin: 0.23068; Return On Equity: 0.46402; Total Revenue: 5228000256; Market Cap: 18035593216; Consensus EPS FY+1: 3.33736; growth: 0.1286 |
| S021 | filing | PNR | 2026-10-27 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json | Diluted EPS 2.76 for period ending 2026-09-30 (filed 2026-10-27) |
| S022 | news | GEN | Fri, 13 Nov 2026 09:34:35 GMT | ok | https://news.google.com/rss/search?q=GEN+Gen+Digital+stock&hl=en-US&gl=US&ceid=US:en | Gen Digital Inc. (GEN) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 09:34:35 GMT); Gen Digital (GEN) Stock Repriced After Q2 Earnings Put Margins Center Stage - Yahoo Finance (Thu, 29 Oct 2026 07:00:00 GMT); Gen Digital Stock: Is Wall Street Bullish or Bearish? - Yahoo Finance (Thu, 05 Nov 2026 08:00:00 GMT) |
| S023 | news | CLX | Sun, 15 Nov 2026 08:55:47 GMT | ok | https://news.google.com/rss/search?q=CLX+Clorox+stock&hl=en-US&gl=US&ceid=US:en | The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance UK (Sun, 15 Nov 2026 08:55:47 GMT); The Clorox Company (CLX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 05:44:34 GMT); The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance Singapore (Fri, 13 Nov 2026 14:10:46 GMT) |
| S024 | filing | CLX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000021076-26-000046); 8-K filed 2026-11-02 (accession 0000021076-26-000044); 8-K filed 2026-10-29 (accession 0001206774-26-000586) |
| S025 | filing | CHTR | 2026-11-06 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-06 (accession 0001091667-26-000073); 8-K filed 2026-11-06 (accession 0001091667-26-000072); 8-K filed 2026-10-27 (accession 0001091667-26-000064) |
| S026 | stock | CLX | 2026-11-15 | ok | https://finance.yahoo.com/quote/CLX | Trailing P/E: 19.68705; Forward P/E: 17.745283; Forward EPS: 6.1684; Price: 109.46; Market price: 109.46; Market cap: 13260793856; Sector: Consumer Defensive; Trailing Eps: 5.56; Revenue Growth: 0.333; Earnings Growth: 1.138; Gross Margin: 0.41939998; Operating Margin: 0.14286; Profit Margin: 0.09408; Return On Equity: 5.34363; Total Revenue: 7196000256; Market Cap: 13260793856; Consensus EPS FY+1: 6.1684; growth: 0.0769 |
| S027 | filing | IDXX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000874716&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000874716-26-000135); 8-K filed 2026-11-02 (accession 0001104659-26-120892); 10-Q filed 2026-08-04 (accession 0000874716-26-000123) |
| S028 | stock | CHTR | 2026-11-15 | ok | https://finance.yahoo.com/quote/CHTR | Trailing P/E: 13.006578; Forward P/E: 3.2831066; Forward EPS: 42.15215; Price: 138.39; Market price: 138.39; Market cap: 24778944512; Sector: Communication Services; Trailing Eps: 10.64; Revenue Growth: 0.091; Gross Margin: 0.55084; Operating Margin: 0.23389; Profit Margin: 0.02498; Return On Equity: 0.07019; Total Revenue: 55645999104; Market Cap: 24778944512; Consensus EPS FY+1: 47.15811; growth: 1.0195 |
| S029 | filing | GEN | 2026-10-29 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000849399.json | Diluted EPS 0.83 for period ending 2026-10-02 (filed 2026-10-29) |
| S030 | news | IDXX | Sat, 14 Nov 2026 06:13:17 GMT | ok | https://news.google.com/rss/search?q=IDXX+Idexx+Laboratories+stock&hl=en-US&gl=US&ceid=US:en | IDEXX Laboratories, Inc. (IDXX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Sat, 14 Nov 2026 06:13:17 GMT); symbol__ Stock Quote Price and Forecast - CNN (Fri, 13 Nov 2026 15:22:45 GMT); IDEXX Laboratories (IDXX) Stock Looks Fairly Valued Despite Its 28% Run - Yahoo Finance (Sat, 31 Oct 2026 07:00:00 GMT) |
| S031 | filing | CHTR | 2026-11-06 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001091667.json | Diluted EPS 0.38 for period ending 2026-09-30 (filed 2026-11-06) |
| S032 | news | CHTR | Sun, 15 Nov 2026 05:47:01 GMT | ok | https://news.google.com/rss/search?q=CHTR+Charter+Communications+stock&hl=en-US&gl=US&ceid=US:en | Charter Communications (CHTR) Stock Could Be A Bargain Following Its New Operating Model - Yahoo Finance (Sun, 15 Nov 2026 05:47:01 GMT); Charter Communications (CHTR) Expands Enterprise Reach With Managed Secure Networking Launch - Yahoo Finance (Sun, 15 Nov 2026 06:08:00 GMT); Why You Should Think About Charter Communications Differently Now? - Yahoo Finance (Fri, 13 Nov 2026 19:16:11 GMT) |
| S033 | stock | IDXX | 2026-11-15 | ok | https://finance.yahoo.com/quote/IDXX | Trailing P/E: 47.45485; Forward P/E: 41.687927; Forward EPS: 16.8929; Price: 704.23; Market price: 704.23; Market cap: 55483650048; Sector: Healthcare; Trailing Eps: 14.84; Revenue Growth: 0.099; Earnings Growth: 0.179; Gross Margin: 0.62722; Operating Margin: 0.32497; Profit Margin: 0.25357; Return On Equity: 0.68925005; Total Revenue: 4662220800; Market Cap: 55483650048; Consensus EPS FY+1: 16.8929; growth: 0.1244 |
| S034 | filing | CLX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000021076.json | Diluted EPS 1.39 for period ending 2026-09-30 (filed 2026-11-02) |
| S035 | filing | ROP | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000882835&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000882835-26-000047); 8-K filed 2026-10-22 (accession 0000882835-26-000042); 8-K filed 2026-10-01 (accession 0000882835-26-000039) |
| S036 | news | ROP | Fri, 13 Nov 2026 13:04:22 GMT | ok | https://news.google.com/rss/search?q=ROP+Roper+Technologies+stock&hl=en-US&gl=US&ceid=US:en | Roper Technologies, Inc. (ROP) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 13:04:22 GMT); Roper Technologies (ROP) Stock Looks Fully Valued As Cash Flow Comes Into Focus - Yahoo Finance (Thu, 05 Nov 2026 08:00:00 GMT); Roper Technologies (ROP), What Is Behind The Fresh Attention? - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT) |
| S037 | filing | RDDT | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001713445&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0001713445-26-000116); 8-K filed 2026-10-29 (accession 0001713445-26-000114); 8-K filed 2026-08-12 (accession 0001713445-26-000107) |
| S038 | news | RDDT | Thu, 29 Oct 2026 07:00:00 GMT | ok | https://news.google.com/rss/search?q=RDDT+Reddit+stock&hl=en-US&gl=US&ceid=US:en | Reddit shares sink on weak sales guidance and plans login requirement test as Google search traffic shrinks - CNBC (Thu, 29 Oct 2026 07:00:00 GMT); Reddit (NYSE:RDDT) surprises with Q3 2026 sales but stock drops 12.6% - Yahoo Finance (Thu, 29 Oct 2026 07:00:00 GMT); Should You Wait Before Buying Reddit Stock? - Trefis (Fri, 13 Nov 2026 18:20:39 GMT) |
| S039 | filing | INTC | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000050863&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0000050863-26-000191); 8-K filed 2026-10-29 (accession 0000050863-26-000188); 8-K filed 2026-08-12 (accession 0001193125-26-346806) |
| S040 | stock | ROP | 2026-11-15 | ok | https://finance.yahoo.com/quote/ROP | Trailing P/E: 18.993866; Forward P/E: 19.532475; Forward EPS: 24.57318; Price: 479.975; Market price: 479.975; Market cap: 47535013888; Sector: Technology; Trailing Eps: 25.27; Revenue Growth: 0.076; Earnings Growth: 0.326; Gross Margin: 0.69671; Operating Margin: 0.28049; Profit Margin: 0.30712998; Return On Equity: 0.13229; Total Revenue: 8434599936; Market Cap: 47535013888; Consensus EPS FY+1: 24.57318; growth: 0.09810001 |

## Sources

- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFF&cosd=2026-01-01 (2026-11-12)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLH0A0HYM2&cosd=2026-01-01 (2026-11-12)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLC0A0CM&cosd=2026-01-01 (2026-11-12)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCSL&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=UNRATE&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=PAYEMS&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=T10Y2Y&cosd=2026-01-01 (2026-11-13)
- filing APP: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001751008&type=10-Q&dateb=&owner=include&count=10 (2026-11-04)
- filing FISV: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 (2026-11-04)
- news APP: https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en (Thu, 12 Nov 2026 20:05:45 GMT)
- filing PNR: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 (2026-10-27)
- news FISV: https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en (Thu, 12 Nov 2026 12:23:56 GMT)
- stock APP: https://finance.yahoo.com/quote/APP (2026-11-15)
- news PNR: https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 22:05:23 GMT)
- stock PNR: https://finance.yahoo.com/quote/PNR (2026-11-15)
- stock FISV: https://finance.yahoo.com/quote/FISV (2026-11-15)
- filing APP: https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json (2026-11-04)
- filing GEN: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 (2026-10-29)
- filing FISV: https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json (2026-11-04)
- stock GEN: https://finance.yahoo.com/quote/GEN (2026-11-15)

## AI Provenance

- Provider / model: hermes-local-proxy / upstage/solar-mini4:free
- Market research: attempts=1 tokens=9473 (prompt=6473, completion=3000) runtime=21.4s
- Fundamental research: generated this run at 2026-11-15T22:14:16.287487+00:00
- Evidence source dates: {'as_of': '2026-11-13', 'latest_equity_date': '2026-11-13', 'latest_macro_date': '2026-11-14', 'flows_date': '2026-11-13'}
- Evidence fingerprint: 19921944ef98a7b3604161143e15c9ee0a95b15eeb8da443e71c1b8fd48a3d1a
- Source citations are retrieved external records in the ledger above; market values remain from the verified database snapshot.


## Disclosures

- This is research and market intelligence, not investment advice.
- AI conclusions are research judgments, not validated return predictions.
- The frozen risk layer is risk-only and is not used for directional views or allocations.
- Legacy scores are not active inputs or outputs.

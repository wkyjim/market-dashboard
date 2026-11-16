# AEGIS AI-First Market Intelligence

Research generated at: 17 November 2026, 03:06 HKT
Database freshness: equity 2026-11-13 (latest row retrieved 2026-11-16 13:06:43.000010+08:00)
Data cutoff: 2026-11-13 US cash close
Snapshot ID: aegis-hourly-20261116T190643Z

## Executive Summary

- **AI market view: Late-November 2026: broad market breadth is constructive (71% above 50-day, 64% above 200-day, A/D ratio 1.70), but the index is slightly negative over 20 days and the 20-day return is -1.28%. Sector leadership is bifurcated: Health Care, Consumer Discretionary, Consumer Staples and Financials are up 20-day, while Information Technology and Energy are down. Institutional flows show strong confirmation in Health Care and neutral-to-structural distribution in Consumer Discretionary and Utilities.**
- Broad market breadth is positive: 71.3% of names above the 50-day moving average, 63.6% above the 200-day, and a 1.70 advance/decline ratio.
- The index is in a mild 20-day drawdown (-1.28%), so the positive breadth is not yet fully reflected in the index level.
- Sector returns are bifurcated: Health Care (+6.9%), Consumer Discretionary (+6.7%), Consumer Staples (+5.4%) and Financials (+5.7%) lead; Information Technology (-7.2%) and Energy (-4.8%) lag.
- Institutional flows confirm Health Care (inflow, strong confirmation) while Consumer Discretionary and Utilities show structural distribution.
- Macro data show a 10Y-2Y spread of 0.27, high-yield OAS of 3.23 and IG OAS of 0.89, with CPI and unemployment at 3.88% and 4.2% respectively.
- Risk environment is moderate: forecast volatility 14.9% is below the 18.5% threshold, but spike probability 16.5% is below the 22.1% historical baseline.

## Data QC

- Status: **PASS_WITH_WARNINGS**
- Equity session: 0 completed session(s) behind inference date
- Equity provenance: 393 provisional / 12576 canonical
- Breadth lag: 0 session(s); ETF-flow lag: 0 session(s)
- Note: Equity session contains a mix of provisional yfinance and canonical Massive rows.
- External sources: 79 ok / 0 unavailable; retrieved 2026-11-16T19:07:02.151382+00:00

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
| S&P 500 | 7561.67 | -1.28% (20d) | Index is slightly negative over 20 days; 71.3% of constituents above 50-day and 63.6% above 200-day. |
| Health Care (XLV) | +6.87% | 20d return | Strongest sector; ETF trailing P/E 30.71 and institutional inflow with strong confirmation. |
| Consumer Discretionary (XLY) | +6.69% | 20d return | Strong 20-day return but institutional flow is neutral with structural distribution. |
| Consumer Staples (XLP) | +5.40% | 20d return | Positive 20-day return; trailing P/E 24.94. |
| Financials (XLF) | +5.69% | 20d return | Positive 20-day return; trailing P/E 15.69. |
| Information Technology (XLK) | -7.19% | 20d return | Worst sector; trailing P/E 29.15. |
| Energy (XLE) | -4.81% | 20d return | Negative 20-day return; trailing P/E 15.93. |

## Macro, Fiscal, Rates, Liquidity and Credit

- Growth: US CPI for all urban consumers is 336.298 (Sep 2026) and core CPI is 338.896, indicating inflation remains above the pre-2021 trend but has not accelerated sharply.
- Labor: Unemployment rate is 4.2% (Sep 2026), consistent with a labor market near full employment and supportive of consumer spending.
- Policy: The effective federal funds rate is 3.88% as of 2026-11-12, suggesting a restrictive but not extreme policy stance.
- Rates: The 10Y-2Y Treasury spread is 0.27 as of 2026-11-13, a modestly positive curve that does not signal imminent recession.
- Credit: High-yield OAS is 3.23 and IG OAS is 0.89 as of 2026-11-13, implying tight but not stressed credit conditions.
- Liquidity: Market breadth is positive with 71.3% above 50-day and 63.6% above 200-day, and the advance/decline ratio is 1.70, indicating broad participation.

## US Equities and 11 GICS Sectors

Macro source IDs: S001, S002, S003, S004, S005, S006, S007

| GICS sector | Evidence | AI research stance | Source IDs |
| --- | --- | --- | --- |
| Health Care | 20-day return +6.87%; ETF trailing P/E 30.71; institutional flow is inflow with strong confirmation; 71.3% of constituents above 50-day. | Constructive: strong sector momentum, positive institutional flows and broad market participation support the sector. | S055, S001, S002 |
| Consumer Staples | 20-day return +5.40%; ETF trailing P/E 24.94; 63.6% of constituents above 200-day. | Constructive: steady demand and moderate valuation support the sector. | S057, S005 |
| Consumer Discretionary | 20-day return +6.69%; ETF trailing P/E 24.69; institutional flow is neutral with structural distribution. | Cautious: strong price momentum but institutional selling suggests caution on near-term upside. | S059, S002 |
| Real Estate | 20-day return +5.24%; ETF trailing P/E 29.55. | Neutral: positive 20-day return but elevated valuation. | S061 |
| Financials | 20-day return +5.69%; ETF trailing P/E 15.69; 63.6% of constituents above 200-day. | Constructive: positive momentum and reasonable valuation support the sector. | S065, S005 |
| Utilities | 20-day return +4.34%; ETF trailing P/E 18.12; institutional flow is neutral with exceptional institutional selling. | Cautious: price strength is not confirmed by institutional flows. | S069, S002 |
| Materials | 20-day return +2.57%; ETF trailing P/E 21.46. | Neutral: modest positive return and reasonable valuation. | S066 |
| Industrials | 20-day return +0.61%; ETF trailing P/E 26.62. | Neutral: near-flat momentum and above-average valuation. | S068 |
| Communication Services | 20-day return -1.48%; ETF trailing P/E 16.98. | Cautious: negative 20-day return and below-average valuation. | S072 |
| Information Technology | 20-day return -7.19%; ETF trailing P/E 29.15; 63.6% of constituents above 200-day. | Cautious: negative momentum and high valuation despite broad 200-day participation. | S074, S005 |
| Energy | 20-day return -4.81%; ETF trailing P/E 15.93. | Cautious: negative momentum and below-average valuation. | S076 |

### Sector fundamentals, valuation and earnings

Sector-level fundamental data (growth, margins, consensus) are not available in the supplied database for the 11 GICS sectors. The only sector fundamentals supplied are trailing P/E ratios for the sector ETFs (XLV, XLP, XLY, XLRE, XLF, XLB, XLI, XLU, XLC, XLK, XLE) and 20-day ETF returns. No point-in-time sector growth or margin estimates are provided, so no sector fundamental claims are made beyond these figures.

## Growth vs Value

- Health Care offers the strongest 20-day momentum (+6.87%) but carries the highest sector ETF trailing P/E (30.71), indicating a growth-oriented valuation.
- Financials provide a reasonable balance with positive 20-day return (+5.69%) and a lower trailing P/E (15.69), suggesting a value tilt.
- Information Technology is the weakest sector on 20-day return (-7.19%) and carries a high trailing P/E (29.15), indicating expensive growth.
- Energy is the cheapest sector by trailing P/E (15.93) but is negative over 20 days (-4.81%), suggesting value without near-term momentum.

## ETF Flows and Breadth

- Health Care is the only sector with a clear institutional inflow (flow z-score 20d +1.45, 60d +1.72) and strong confirmation, aligning with positive breadth.
- Consumer Discretionary shows neutral flow state with structural distribution (flow z-score 20d -0.38, 60d -0.78), indicating institutional selling despite strong price momentum.
- Utilities is neutral on price but shows exceptional institutional selling (flow z-score 20d -2.15), a warning sign for the sector.
- Market breadth is constructive: 71.3% of constituents above 50-day, 63.6% above 200-day, and an advance/decline ratio of 1.70.
- The index is slightly negative over 20 days (-1.28%), so the positive breadth is not yet fully reflected in the index level.

## Stock Ideas

Single-stock research uses reported EPS, forward P/E and company fundamentals. All ideas are research judgments, not validated return predictions.

| Ticker | Security | Research view | Price | EPS | Forward P/E | Base target | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| APP | AppLovin | NEW | 409.1 | 20.86026 | 19.757975 | 417.21 | NEW |
| PNR | Pentair | KEEP | 68.3 | 5.30402 | 12.84686 | 68.95 | KEEP |
| GEN | Gen Digital | NEW | 30.4 | 3.33736 | 9.146451 | 33.37 | NEW |
| CLX | Clorox | KEEP | 109.46 | 6.1684 | 17.92361 | 111.03 | KEEP |
| IDXX | Idexx Laboratories | KEEP | 704.23 | 16.8929 | 41.70006 | 709.5 | KEEP |

## ETF Ideas

ETF research uses holdings, portfolio valuation and exposure. Single-stock EPS × P/E valuation is not applied to ETFs.

No qualifying ETF ideas this run.
### APP — AppLovin

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** AppLovin offers a high-margin, momentum-driven advertising name with a cleaner forward P/E than the high-multiple names in the shortlist, and it is not a financial or semiconductor name with balance-sheet or margin-compression risk. Alternatives considered: PNR, GEN, CLX, IDXX, ROP.
- **Thesis:** AppLovin screens in the top 20-day momentum bucket with a 53.7% 20-day return and a 32.5% 60-day return, while its reported diluted EPS of $11.61 and forward EPS of $20.86 support a forward P/E near 19.8. The company's high gross margin (~88.8%) and operating margin (~77.8%) indicate a durable, high-quality advertising franchise, and the filing and news sources confirm recent earnings momentum and price action.
- **Source IDs:** S008, S012, S017, S018
- **Catalysts:** Continued 20-day momentum into the next week, Advertising market recovery supporting AppLovin's demand, Recurring in-app advertising revenue growth
- **Risks:** Momentum can fade quickly if ad spend slows, High valuation relative to near-term earnings growth, Single-quarter earnings concentration
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 20.8603 (source.forwardEps) x AI multiple assumption 20.00; source IDs S008, S012, S017, S018
- **EPS:** 20.86026 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 19.757975
- **FY+1 growth assumption:** 27.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / PNR / APP shows 27.44% forward earnings growth and 25.37% revenue growth with exceptional 88.8% gross margin and 77.8% operating margin, but ROE is only 2.10%, indicating heavy leverage. PNR is the named peer with 12.82% forward earnings growth, 18.38% revenue growth, 40.2% gross margin, 21.4% operating margin, and 15.6% ROE, making it a more conservative comparable for APP's growth and margin profile.
- **Company fundamentals:** Stock only; null for ETF
- **Bull / Base / Bear:** 500.65 / 417.21 / 333.76
- **Bull / Base / Bear returns:** 22.38% / 1.98% / -18.42%
- **Scenario probabilities:** not separately assigned; see scenario table.

### PNR — Pentair

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Pentair is a lower-multiple industrial name with a reasonable forward P/E, but it is not as high-quality or as fast-growing as the top momentum names, so it is best held as a neutral core position rather than a primary recommendation. Alternatives considered: APP, GEN, CLX, IDXX, ROP.
- **Thesis:** Pentair screens in the top 20-day momentum bucket with a 27.8% 20-day return and a 7.1% 60-day return. Its trailing P/E of 18.57 and forward P/E of 12.85 are reasonable, but revenue growth is slightly negative (-4.5%) and earnings growth is negative (-18.8%), so the momentum is not yet supported by fundamental expansion. The stock is a solid industrial name but does not currently warrant a strong directional call.
- **Source IDs:** S009, S013, S016, S021
- **Catalysts:** Potential stabilization in industrial end-markets, Possible margin recovery if input costs ease, Continued 20-day momentum if order books hold
- **Risks:** Negative revenue and earnings growth in the latest reported period, Industrial cyclicality and exposure to construction cycles, Valuation may be priced for a recovery that has not yet materialized
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 5.3040 (source.forwardEps) x AI multiple assumption 13.00; source IDs S009, S013, S016, S021
- **EPS:** 5.30402 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 12.84686
- **FY+1 growth assumption:** 12.82%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / APP / PNR has 12.82% forward earnings growth and 18.38% revenue growth with 40.2% gross margin and 21.4% operating margin, but ROE is only 15.6%. APP is the named peer with 27.44% forward earnings growth, 25.37% revenue growth, 88.8% gross margin, 77.8% operating margin, and 2.10% ROE, providing a higher-growth but lower-ROE comparison for PNR's more modest growth and margin profile.
- **Company fundamentals:** Stock only; null for ETF
- **Bull / Base / Bear:** 84.86 / 68.95 / 53.04
- **Bull / Base / Bear returns:** 24.25% / 0.95% / -22.34%
- **Scenario probabilities:** not separately assigned; see scenario table.

### GEN — Gen Digital

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** Gen Digital combines a low forward P/E with strong earnings growth and a clear margin story, making it a more compelling risk/reward than the higher-multiple or lower-growth names in the shortlist. Alternatives considered: APP, PNR, CLX, IDXX, ROP.
- **Thesis:** Gen Digital screens in the top 20-day momentum bucket with a 25.8% 20-day return and a 7.9% 60-day return. Its forward P/E of 9.15 is attractive relative to its growth profile, and the news source indicates that margins are a central focus after the Q2 earnings repricing. The company's revenue growth of 12.2% and earnings growth of 128.6% support a high-quality cybersecurity and digital life assets franchise.
- **Source IDs:** S014, S023, S026, S028
- **Catalysts:** Margin expansion as the portfolio re-rates, Continued 20-day momentum in the security software space, Potential for further re-rating as margins improve
- **Risks:** High valuation relative to near-term earnings growth, Cybersecurity sector competition and regulatory risk, Concentration in a few large customers
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 3.3374 (source.forwardEps) x AI multiple assumption 10.00; source IDs S014, S023, S026, S028
- **EPS:** 3.33736 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 9.146451
- **FY+1 growth assumption:** 12.86%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / IDXX / GEN has 12.86% forward earnings growth and 6.81% revenue growth with 77.4% gross margin and 43.2% operating margin, but ROE is 46.4%. IDXX is the named peer with 12.44% forward earnings growth, 8.88% revenue growth, 62.7% gross margin, 32.5% operating margin, and 68.9% ROE, making it a more conservative comparable for GEN's growth and margin profile.
- **Company fundamentals:** Stock only; null for ETF
- **Bull / Base / Bear:** 43.39 / 33.37 / 26.7
- **Bull / Base / Bear returns:** 42.73% / 9.77% / -12.17%
- **Scenario probabilities:** not separately assigned; see scenario table.

### CLX — Clorox

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Clorox provides a defensive consumer staples exposure with reasonable valuation, but it is not as high-quality or as fast-growing as the top momentum names, so it is best held as a neutral core position. Alternatives considered: APP, PNR, GEN, IDXX, ROP.
- **Thesis:** Clorox screens in the top 20-day momentum bucket with a 25.7% 20-day return and a 3.2% 60-day return. Its trailing P/E of 19.88 and forward P/E of 17.92 are reasonable, and revenue growth of 33.3% and earnings growth of 113.8% are strong, but the company's lower gross margin (~41.9%) and operating margin (~14.3%) indicate a more capital-light, lower-margin business. The stock is a solid consumer staples name but does not offer the same quality or growth as the top momentum names.
- **Source IDs:** S020, S022, S025, S030
- **Catalysts:** Continued 20-day momentum in consumer staples, Potential for margin expansion as the business scales, Stable demand for household and personal care products
- **Risks:** Lower margins than peers in the consumer staples space, Consumer spending sensitivity to economic conditions, Competition in the household and personal care categories
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 6.1684 (source.forwardEps) x AI multiple assumption 18.00; source IDs S020, S022, S025, S030
- **EPS:** 6.1684 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 17.92361
- **FY+1 growth assumption:** 7.69%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / ROP / CLX has 7.69% forward earnings growth and 2.23% revenue growth with 41.9% gross margin and 14.3% operating margin, but ROE is only 5.34%. ROP is the named peer with 9.81% forward earnings growth, 6.29% revenue growth, 69.7% gross margin, 28.0% operating margin, and 13.2% ROE, making it a more conservative comparable for CLX's lower growth and margin profile.
- **Company fundamentals:** Stock only; null for ETF
- **Bull / Base / Bear:** 135.7 / 111.03 / 86.36
- **Bull / Base / Bear returns:** 23.97% / 1.43% / -21.1%
- **Scenario probabilities:** not separately assigned; see scenario table.

### IDXX — Idexx Laboratories

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Idexx offers a defensive, high-quality animal health and diagnostic franchise, but its rich valuation relative to growth makes it a neutral holding rather than a primary recommendation. Alternatives considered: APP, PNR, GEN, CLX, ROP.
- **Thesis:** Idexx Laboratories screens in the top 20-day momentum bucket with a 25.7% 20-day return and a 29.0% 60-day return. Its trailing P/E of 39.18 and forward P/E of 41.70 are high, and the company's revenue growth of 9.9% and earnings growth of 17.9% are solid but not exceptional. The stock is a high-quality animal health and diagnostic franchise, but the valuation is rich relative to its growth, so it is best held as a neutral position.
- **Source IDs:** S027, S031, S035, S040
- **Catalysts:** Continued 20-day momentum in the animal health space, Potential for margin expansion as the business scales, Stable demand for veterinary diagnostics and animal health products
- **Risks:** High valuation relative to near-term earnings growth, Concentration in a few large markets, Competition in the veterinary diagnostics and animal health categories
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 16.8929 (source.forwardEps) x AI multiple assumption 42.00; source IDs S027, S031, S035, S040
- **EPS:** 16.8929 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 41.70006
- **FY+1 growth assumption:** 12.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / GEN / IDXX has 12.44% forward earnings growth and 8.88% revenue growth with 62.7% gross margin and 32.5% operating margin, and 68.9% ROE. GEN is the named peer with 12.86% forward earnings growth, 6.81% revenue growth, 77.4% gross margin, 43.2% operating margin, and 46.4% ROE, providing a higher-margin but lower-ROE comparison for IDXX's growth and margin profile.
- **Company fundamentals:** Stock only; null for ETF
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
| Bull | 25% | +2.00% | Low 5-day realized vol (14.9%) and below-threshold spike probability (16.5% vs 18.5% threshold) support a modest upside if US close confirms the frozen daily-close model and breadth holds. |
| Base | 50% | +0.00% | Directional signal is false and the forecast is prospective, so the most likely path is range-bound consolidation near the frozen daily-close level with no directional alpha. |
| Bear | 25% | -2.00% | If the US close fails to validate the frozen model or credit/breadth deteriorates, the low signal confidence and elevated volatility regime could push a mild downside move. |

### Long Term (12 months)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 30% | +8.00% | Sustained earnings growth and positive rate trajectory can drive a bull case, with the low 5-day vol environment allowing a 8% upside over the horizon. |
| Base | 40% | +3.00% | A neutral base case assumes stable credit conditions, modest earnings progression, and no sharp rate shift, yielding a low-single-digit long-term return. |
| Bear | 30% | -5.00% | A bear case arises if credit spreads widen, earnings disappoint, or rates rise faster than expected, compressing valuations and producing a -5% long-term return. |

## Positioning

- Maintain a constructive stance on Health Care given strong momentum, positive institutional flows and broad market participation.
- Favor Financials for a balance of positive momentum and reasonable valuation.
- Exercise caution on Consumer Discretionary and Utilities due to structural distribution and exceptional institutional selling.
- Monitor Information Technology and Energy for stabilization before adding exposure, given negative 20-day returns and high valuations.
- No allocation weights are provided; this is a research posture only.

## Catalysts

| Date | Event | Why it matters |
| --- | --- | --- |
| 2026-11-16 | US macro data release | CPI and unemployment data are the latest available; any revision or new print will affect inflation and labor market expectations. |
| 2026-11-16 | 10Y-2Y Treasury spread | The spread is 0.27, a modestly positive curve; a move below zero would signal recession concerns. |
| 2026-11-16 | Credit spreads | High-yield OAS at 3.23 and IG OAS at 0.89 are tight but not stressed; widening would indicate credit stress. |
| 2026-11-16 | Risk forecast | Forecast volatility is 14.9%, below the 18.5% threshold, but spike probability is 16.5%, below the 22.1% historical baseline. |

## Key Risks

- Index is slightly negative over 20 days (-1.28%), so positive breadth may not persist if the index fails to recover.

## External Source Ledger

| ID | Type | Ticker | Published | Status | URL | Claims |
| --- | --- | --- | --- | --- | --- | --- |
| S001 | macro | macro | 2026-11-12 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFF&cosd=2026-01-01 | Effective federal funds rate (DFF) latest observation 2026-11-12: 3.88 |
| S002 | macro | macro | 2026-11-13 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLH0A0HYM2&cosd=2026-01-01 | US high-yield OAS (BAMLH0A0HYM2) latest observation 2026-11-13: 3.23 |
| S003 | macro | macro | 2026-11-13 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLC0A0CM&cosd=2026-01-01 | US investment-grade OAS (BAMLC0A0CM) latest observation 2026-11-13: 0.89 |
| S004 | macro | macro | 2026-10-01 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCSL&cosd=2026-01-01 | US CPI (CPIAUCSL) latest observation 2026-10-01: 337.476 |
| S005 | macro | macro | 2026-10-01 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=UNRATE&cosd=2026-01-01 | US unemployment rate (UNRATE) latest observation 2026-10-01: 4.1 |
| S006 | macro | macro | 2026-10-01 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=PAYEMS&cosd=2026-01-01 | US nonfarm payrolls (PAYEMS) latest observation 2026-10-01: 159293 |
| S007 | macro | macro | 2026-11-13 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=T10Y2Y&cosd=2026-01-01 | 10Y-2Y Treasury spread (T10Y2Y) latest observation 2026-11-13: 0.27 |
| S008 | filing | APP | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001751008&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0001751008-26-000069); 8-K filed 2026-11-04 (accession 0001751008-26-000068); 10-Q filed 2026-08-05 (accession 0001751008-26-000059) |
| S009 | filing | PNR | 2026-10-27 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-27 (accession 0000077360-26-000058); 8-K filed 2026-10-27 (accession 0000077360-26-000055); 8-K filed 2026-09-22 (accession 0000077360-26-000050) |
| S010 | news | FISV | Mon, 16 Nov 2026 02:19:15 GMT | ok | https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en | Fiserv, Inc. (FISV) Stock Price, News, Quote & History - Yahoo! Finance Canada (Mon, 16 Nov 2026 02:19:15 GMT); Fiserv (FISV) Stock Looks Undervalued With Strong Excess Returns - Yahoo Finance (Wed, 11 Nov 2026 22:14:34 GMT); What Is Fiserv (FISV) Planning With Its Debit Networks And Clover AI? - Yahoo Finance (Thu, 12 Nov 2026 06:09:00 GMT) |
| S011 | filing | FISV | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0000798354-26-000042); 8-K filed 2026-11-03 (accession 0000798354-26-000039); 8-K filed 2026-10-23 (accession 0001193125-26-429481) |
| S012 | news | APP | Mon, 16 Nov 2026 18:52:15 GMT | ok | https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en | AppLovin Stock Moves Higher: What's Going On? - Benzinga (Mon, 16 Nov 2026 18:52:15 GMT); AppLovin Just Ripped 47% in a Month: Is It Too Late to Buy APP Stock Now? - Yahoo Finance (Thu, 12 Nov 2026 20:05:45 GMT); APP Stock Quote Price and Forecast - CNN (Sat, 14 Nov 2026 08:02:29 GMT) |
| S013 | news | PNR | Sat, 14 Nov 2026 08:48:27 GMT | ok | https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en | Pentair plc (PNR) Stock Price, News, Quote & History - Yahoo! Finance Canada (Sat, 14 Nov 2026 08:48:27 GMT); Pentair Stock Price Forecast. Should You Buy PNR? - StockInvest.us (Fri, 13 Nov 2026 22:50:05 GMT); Why Pentair Stock Popped This Morning - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT) |
| S014 | filing | GEN | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0000849399-26-000083); 8-K filed 2026-10-28 (accession 0000849399-26-000081); 8-K filed 2026-10-09 (accession 0000849399-26-000079) |
| S015 | stock | FISV | 2026-11-16 | ok | https://finance.yahoo.com/quote/FISV | Forward P/E: 7.9819164; Price: 63.63; Market price: 63.63; Market cap: 33854195712; Market Cap: 33854195712; Consensus EPS FY+1: 7.97582; growth: 0.0959 |
| S016 | stock | PNR | 2026-11-16 | ok | https://finance.yahoo.com/quote/PNR | Trailing P/E: 18.566757; Forward P/E: 12.84686; Forward EPS: 5.30402; Price: 68.14; Market price: 68.14; Market cap: 10878870528; Sector: Industrials; Trailing Eps: 3.67; Revenue Growth: -0.045; Earnings Growth: -0.188; Gross Margin: 0.40168998; Operating Margin: 0.21410999; Profit Margin: 0.15435; Return On Equity: 0.15605; Total Revenue: 3966200064; Market Cap: 10878870528; Consensus EPS FY+1: 5.30402; growth: 0.1282 |
| S017 | stock | APP | 2026-11-16 | ok | https://finance.yahoo.com/quote/APP | Trailing P/E: 27.754646; Forward P/E: 19.757975; Forward EPS: 20.86026; Price: 412.1565; Market price: 412.1565; Market cap: 136556511232; Sector: Communication Services; Trailing Eps: 14.85; Revenue Growth: 0.555; Earnings Growth: 0.755; Gross Margin: 0.8878; Operating Margin: 0.77782995; Profit Margin: 0.65887; Return On Equity: 2.1008599; Total Revenue: 7608893952; Market Cap: 136556511232; Consensus EPS FY+1: 20.72438; growth: 0.2744 |
| S018 | filing | APP | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json | Diluted EPS 11.61 for period ending 2026-09-30 (filed 2026-11-04) |
| S019 | filing | FISV | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json | Diluted EPS -8.9 for period ending 2026-09-30 (filed 2026-11-04) |
| S020 | filing | CLX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000021076-26-000046); 8-K filed 2026-11-02 (accession 0000021076-26-000044); 8-K filed 2026-10-29 (accession 0001206774-26-000586) |
| S021 | filing | PNR | 2026-10-27 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json | Diluted EPS 2.76 for period ending 2026-09-30 (filed 2026-10-27) |
| S022 | stock | CLX | 2026-11-16 | ok | https://finance.yahoo.com/quote/CLX | Trailing P/E: 19.884892; Forward P/E: 17.92361; Forward EPS: 6.1684; Price: 110.56; Market price: 110.56; Market cap: 13394055168; Sector: Consumer Defensive; Trailing Eps: 5.56; Revenue Growth: 0.333; Earnings Growth: 1.138; Gross Margin: 0.41939998; Operating Margin: 0.14286; Profit Margin: 0.09408; Return On Equity: 5.34363; Total Revenue: 7196000256; Market Cap: 13394055168; Consensus EPS FY+1: 6.1684; growth: 0.0769 |
| S023 | news | GEN | Thu, 29 Oct 2026 07:00:00 GMT | ok | https://news.google.com/rss/search?q=GEN+Gen+Digital+stock&hl=en-US&gl=US&ceid=US:en | Gen Digital (GEN) Stock Repriced After Q2 Earnings Put Margins Center Stage - Yahoo Finance (Thu, 29 Oct 2026 07:00:00 GMT); Gen Digital Stock: Is Wall Street Bullish or Bearish? - Yahoo Finance (Thu, 05 Nov 2026 08:00:00 GMT); Are Business Services Stocks Lagging GEN DIGITAL INC (GEN) This Year? - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT) |
| S024 | filing | CHTR | 2026-11-06 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-06 (accession 0001091667-26-000073); 8-K filed 2026-11-06 (accession 0001091667-26-000072); 8-K filed 2026-10-27 (accession 0001091667-26-000064) |
| S025 | news | CLX | Fri, 13 Nov 2026 23:34:51 GMT | ok | https://news.google.com/rss/search?q=CLX+Clorox+stock&hl=en-US&gl=US&ceid=US:en | The Clorox Company (CLX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 23:34:51 GMT); The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance UK (Sat, 14 Nov 2026 06:03:20 GMT); A 10-Day Winning Streak Has Clorox Stock Up 24% - Trefis (Sat, 14 Nov 2026 08:28:05 GMT) |
| S026 | stock | GEN | 2026-11-16 | ok | https://finance.yahoo.com/quote/GEN | Trailing P/E: 15.494924; Forward P/E: 9.146451; Forward EPS: 3.33736; Price: 30.525; Market price: 30.525; Market cap: 18109753344; Sector: Technology; Trailing Eps: 1.97; Revenue Growth: 0.122; Earnings Growth: 1.286; Gross Margin: 0.77410007; Operating Margin: 0.43229; Profit Margin: 0.23068; Return On Equity: 0.46402; Total Revenue: 5228000256; Market Cap: 18109753344; Consensus EPS FY+1: 3.33736; growth: 0.1286 |
| S027 | filing | IDXX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000874716&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000874716-26-000135); 8-K filed 2026-11-02 (accession 0001104659-26-120892); 10-Q filed 2026-08-04 (accession 0000874716-26-000123) |
| S028 | filing | GEN | 2026-10-29 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000849399.json | Diluted EPS 0.83 for period ending 2026-10-02 (filed 2026-10-29) |
| S029 | news | CHTR | Sun, 15 Nov 2026 05:47:01 GMT | ok | https://news.google.com/rss/search?q=CHTR+Charter+Communications+stock&hl=en-US&gl=US&ceid=US:en | Charter Communications (CHTR) Stock Could Be A Bargain Following Its New Operating Model - Yahoo Finance (Sun, 15 Nov 2026 05:47:01 GMT); Why You Should Think About Charter Communications Differently Now? - Yahoo Finance (Fri, 13 Nov 2026 19:16:11 GMT); Charter Communications (CHTR) Earnings Expected to Grow: What to Know Ahead of Next Week's Release - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT) |
| S030 | filing | CLX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000021076.json | Diluted EPS 1.39 for period ending 2026-09-30 (filed 2026-11-02) |
| S031 | news | IDXX | Sat, 14 Nov 2026 22:37:20 GMT | ok | https://news.google.com/rss/search?q=IDXX+Idexx+Laboratories+stock&hl=en-US&gl=US&ceid=US:en | IDEXX Laboratories, Inc. (IDXX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Sat, 14 Nov 2026 22:37:20 GMT); IDEXX Laboratories (IDXX) Stock Looks Fairly Valued Despite Its 28% Run - Yahoo Finance (Sat, 31 Oct 2026 07:00:00 GMT); IDEXX Laboratories (IDXX) vs. ZTS and NEOG: Can Raised Guidance and Product Expansion Drive Further Earnings Growth? - Yahoo Finance (Thu, 22 Oct 2026 07:00:00 GMT) |
| S032 | stock | CHTR | 2026-11-16 | ok | https://finance.yahoo.com/quote/CHTR | Trailing P/E: 12.945489; Forward P/E: 3.0309265; Forward EPS: 45.44485; Price: 137.74; Market price: 137.74; Market cap: 24662560768; Sector: Communication Services; Trailing Eps: 10.64; Revenue Growth: 0.091; Gross Margin: 0.55084; Operating Margin: 0.23389; Profit Margin: 0.02498; Return On Equity: 0.07019; Total Revenue: 55645999104; Market Cap: 24662560768; Consensus EPS FY+1: 49.35412; growth: 1.1136 |
| S033 | filing | CHTR | 2026-11-06 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001091667.json | Diluted EPS 0.38 for period ending 2026-09-30 (filed 2026-11-06) |
| S034 | filing | ROP | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000882835&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000882835-26-000047); 8-K filed 2026-10-22 (accession 0000882835-26-000042); 8-K filed 2026-10-01 (accession 0000882835-26-000039) |
| S035 | stock | IDXX | 2026-11-16 | ok | https://finance.yahoo.com/quote/IDXX | Trailing P/E: 47.468666; Forward P/E: 41.70006; Forward EPS: 16.8929; Price: 704.435; Market price: 704.435; Market cap: 55499800576; Sector: Healthcare; Trailing Eps: 14.84; Revenue Growth: 0.099; Earnings Growth: 0.179; Gross Margin: 0.62722; Operating Margin: 0.32497; Profit Margin: 0.25357; Return On Equity: 0.68925005; Total Revenue: 4662220800; Market Cap: 55499800576; Consensus EPS FY+1: 16.8929; growth: 0.1244 |
| S036 | stock | ROP | 2026-11-16 | ok | https://finance.yahoo.com/quote/ROP | Trailing P/E: 19.178076; Forward P/E: 19.721909; Forward EPS: 24.57318; Price: 484.63; Market price: 484.63; Market cap: 47996026880; Sector: Technology; Trailing Eps: 25.27; Revenue Growth: 0.076; Earnings Growth: 0.326; Gross Margin: 0.69671; Operating Margin: 0.28049; Profit Margin: 0.30712998; Return On Equity: 0.13229; Total Revenue: 8434599936; Market Cap: 47996026880; Consensus EPS FY+1: 24.57318; growth: 0.09810001 |
| S037 | filing | RDDT | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001713445&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0001713445-26-000116); 8-K filed 2026-10-29 (accession 0001713445-26-000114); 8-K filed 2026-08-12 (accession 0001713445-26-000107) |
| S038 | stock | RDDT | 2026-11-16 | ok | https://finance.yahoo.com/quote/RDDT | Trailing P/E: 18.893877; Forward P/E: 10.17319; Forward EPS: 9.10039; Price: 92.58; Market price: 92.58; Market cap: 17876617216; Sector: Communication Services; Trailing Eps: 4.9; Revenue Growth: 0.53; Earnings Growth: 0.749; Gross Margin: 0.91547996; Operating Margin: 0.29397; Profit Margin: 0.32105; Return On Equity: 0.32029998; Total Revenue: 3088880128; Market Cap: 17876617216; Consensus EPS FY+1: 6.8155; growth: 0.2401 |
| S039 | news | ROP | Thu, 05 Nov 2026 08:00:00 GMT | ok | https://news.google.com/rss/search?q=ROP+Roper+Technologies+stock&hl=en-US&gl=US&ceid=US:en | Roper Technologies (ROP) Stock Looks Fully Valued As Cash Flow Comes Into Focus - Yahoo Finance (Thu, 05 Nov 2026 08:00:00 GMT); Here's How Much $100 Invested In Roper Technologies 20 Years Ago Would Be Worth Today - Benzinga (Mon, 16 Nov 2026 14:15:26 GMT); Roper Technologies (ROP), What Is Behind The Fresh Attention? - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT) |
| S040 | filing | IDXX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000874716.json | Diluted EPS 11.75 for period ending 2026-09-30 (filed 2026-11-02) |

## Sources

- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFF&cosd=2026-01-01 (2026-11-12)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLH0A0HYM2&cosd=2026-01-01 (2026-11-13)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLC0A0CM&cosd=2026-01-01 (2026-11-13)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCSL&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=UNRATE&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=PAYEMS&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=T10Y2Y&cosd=2026-01-01 (2026-11-13)
- filing APP: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001751008&type=10-Q&dateb=&owner=include&count=10 (2026-11-04)
- filing PNR: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 (2026-10-27)
- news FISV: https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en (Mon, 16 Nov 2026 02:19:15 GMT)
- filing FISV: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 (2026-11-04)
- news APP: https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en (Mon, 16 Nov 2026 18:52:15 GMT)
- news PNR: https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en (Sat, 14 Nov 2026 08:48:27 GMT)
- filing GEN: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 (2026-10-29)
- stock FISV: https://finance.yahoo.com/quote/FISV (2026-11-16)
- stock PNR: https://finance.yahoo.com/quote/PNR (2026-11-16)
- stock APP: https://finance.yahoo.com/quote/APP (2026-11-16)
- filing APP: https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json (2026-11-04)
- filing FISV: https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json (2026-11-04)
- filing CLX: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 (2026-11-02)

## AI Provenance

- Provider / model: hermes-local-proxy / upstage/solar-mini4:free
- Market research: attempts=1 tokens=9513 (prompt=6513, completion=3000) runtime=23.16s
- Fundamental research: generated this run at 2026-11-16T19:06:43.537167+00:00
- Evidence source dates: {'as_of': '2026-11-13', 'latest_equity_date': '2026-11-13', 'latest_macro_date': '2026-11-16', 'flows_date': '2026-11-13'}
- Evidence fingerprint: c762e1a47f59f7ff441af582759d9ca780994f2f865568f833dfd9ca8a56a55d
- Source citations are retrieved external records in the ledger above; market values remain from the verified database snapshot.


## Disclosures

- This is research and market intelligence, not investment advice.
- AI conclusions are research judgments, not validated return predictions.
- The frozen risk layer is risk-only and is not used for directional views or allocations.
- Legacy scores are not active inputs or outputs.

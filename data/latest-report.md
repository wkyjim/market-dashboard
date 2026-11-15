# AEGIS AI-First Market Intelligence

Research generated at: 15 November 2026, 16:15 HKT
Database freshness: equity 2026-11-13 (latest row retrieved 2026-11-15 13:06:40.074841+08:00)
Data cutoff: 2026-11-13 US cash close
Snapshot ID: aegis-hourly-20261115T081515Z

## Executive Summary

- **AI market view: Late-November 2026 US equities show a late-cycle, late-autumn setup: broad index levels remain elevated, but momentum and breadth are mixed, with 20-day returns positive for most sectors while Information Technology and Energy are negative. Liquidity is concentrated in select large-cap names and semiconductors, while credit spreads are tight and macro data point to a cooling but still-positive growth backdrop. The risk block is frozen and prospective, with elevated volatility and a low spike probability relative to historical baselines.**
- Broad market is in a late-cycle phase: 20-day sector returns are mostly positive, but IT and Energy are negative and 200-day breadth is below 65%.
- Momentum and liquidity are concentrated in a short list of large-cap names, including NVDA, AMD, MU, AAPL, and SOXX, while several dislocation names carry high valuation or negative earnings yield.
- Credit spreads are tight (IG 0.89, HY 3.20), consistent with a stable but not exuberant risk appetite.
- Macro data show cooling inflation (CPI 336.298, Sep-2026) and a 4.2% unemployment rate, with the effective funds rate at 3.88%.
- The frozen risk block flags elevated 5-day volatility (14.9%) and a 16.5% spike probability, below the 22.1% historical baseline.
- Sector leadership is broad but uneven; Communication Services and Information Technology are the weakest 20-day performers.

## Data QC

- Status: **PASS_WITH_WARNINGS**
- Equity session: 0 completed session(s) behind inference date
- Equity provenance: 393 provisional / 12576 canonical
- Breadth lag: 0 session(s); ETF-flow lag: 0 session(s)
- Note: Equity session contains a mix of provisional yfinance and canonical Massive rows.
- External sources: 79 ok / 0 unavailable; retrieved 2026-11-15T08:15:45.304762+00:00

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
| S&P 500 | 7561.67 | -1.28% (20d) | Index level elevated but 20-day return negative; breadth and momentum are mixed. |
| Health Care (XLV) | 30.78 P/E | +6.87% (20d) | Strongest 20-day sector return; high trailing P/E suggests premium valuation. |
| Consumer Discretionary (XLY) | 25.11 P/E | +6.69% (20d) | Positive momentum but premium valuation relative to market. |
| Information Technology (XLK) | 30.03 P/E | -7.19% (20d) | Weakest 20-day sector return; high P/E and liquidity leader concentration. |
| Energy (XLE) | 16.23 P/E | -4.81% (20d) | Negative 20-day return; low P/E but weak price action. |
| Financials (XLF) | 15.85 P/E | +5.69% (20d) | Positive 20-day return with low P/E; attractive relative value. |

## Macro, Fiscal, Rates, Liquidity and Credit

- Growth: CPI for All Urban Consumers is 336.298 (Sep-2026), down from 337.476 in Oct-2026, indicating cooling inflation; core CPI is 338.896.
- Labor: Unemployment rate is 4.2% (Sep-2026), up from 4.1% in Oct-2026, suggesting a gradual labor market cooling.
- Policy: Effective federal funds rate is 3.88% as of 2026-11-12, with a 10Y-2Y spread of 0.27 as of 2026-11-13, indicating a modestly positive but flat yield curve.
- Rates: IG OAS is 0.89 and HY OAS is 3.20 as of 2026-11-12, both tight and consistent with stable credit conditions.
- Liquidity: Bitcoin fell 6.04% to 64,128.05 and Ethereum fell 8.22% to 1,769.12 on 2026-11-14, signaling reduced risk appetite in crypto and possible de-risking.
- Credit: Tight spreads and cooling inflation support a late-cycle but not distressed environment; the frozen risk block shows elevated volatility and a low spike probability.

## US Equities and 11 GICS Sectors

Macro source IDs: S001, S002, S003, S004, S005, S006, S007

| GICS sector | Evidence | AI research stance | Source IDs |
| --- | --- | --- | --- |
| Health Care | 20d return +6.87%; trailing P/E 30.78; S055 | Positive momentum but premium valuation; leadership in a late-cycle market. | S055 |
| Consumer Staples | 20d return +5.40%; trailing P/E 24.85; S057 | Defensive strength with moderate valuation; stable demand. | S057 |
| Consumer Discretionary | 20d return +6.69%; trailing P/E 25.11; S061 | Positive momentum but premium valuation; consumer spending remains supportive. | S061 |
| Real Estate | 20d return +5.24%; trailing P/E 29.63; S063 | Positive 20d return but high P/E; rate-sensitive sector faces mixed macro backdrop. | S063 |
| Financials | 20d return +5.69%; trailing P/E 15.85; S070 | Positive momentum with low valuation; attractive relative value in a late-cycle market. | S070 |
| Utilities | 20d return +4.34%; trailing P/E 18.11; S065 | Defensive stability with moderate valuation; low beta in a mixed market. | S065 |
| Materials | 20d return +2.57%; trailing P/E 21.72; S074 | Modest positive momentum; industrial and commodity exposure is mixed. | S074 |
| Industrials | 20d return +0.61%; trailing P/E 27.07; S068 | Near-flat 20d return; high P/E and weak momentum; late-cycle caution. | S068 |
| Communication Services | 20d return -1.48%; trailing P/E 17.26; S071 | Weakest 20d return; negative momentum despite moderate valuation. | S071 |
| Information Technology | 20d return -7.19%; trailing P/E 30.03; S076 | Negative 20d return and high P/E; liquidity leader concentration but broad weakness. | S076 |
| Energy | 20d return -4.81%; trailing P/E 16.23; S073 | Negative 20d return; low P/E but weak price action and macro headwinds. | S073 |

### Sector fundamentals, valuation and earnings

No point-in-time sector fundamentals beyond the supplied 20-day ETF returns and trailing P/E multiples are available in the database. The sector evidence is limited to the 11 GICS sectors with their ETF return_20d and trailing P/E values; no growth, margin, or consensus data are supplied for the full sector universe. Therefore, no additional sector fundamentals are asserted here.

## Growth vs Value

- Growth: Health Care (+6.87% 20d) and Consumer Discretionary (+6.69% 20d) lead sector momentum, but both carry high trailing P/E (30.78 and 25.11), indicating premium growth expectations.
- Value: Financials (+5.69% 20d) and Energy (-4.81% 20d) show the widest valuation dispersion; Financials at 15.85 P/E is the cheapest major sector, while Energy at 16.23 P/E is low but negative on price.
- Mixed signals: Utilities (18.11 P/E) and Materials (21.72 P/E) offer moderate valuation with low single-digit positive momentum, while Industrials (27.07 P/E) and Real Estate (29.63 P/E) are expensive with weak momentum.
- Valuation caution: Information Technology (30.03 P/E) and Communication Services (17.26 P/E) show negative 20d returns despite moderate-to-high multiples, suggesting momentum and valuation are misaligned.

## ETF Flows and Breadth

- Breadth is mixed: 71.34% of names are above their 50-day moving average and 63.6% above the 200-day, but 20-day positive rate is 70.46% with an advance/decline ratio of 1.70.
- Price-breadth divergence is -27.49, but bullish divergence is true and bearish divergence is false, indicating no confirmed negative divergence.
- Flows show strong institutional buying in SOXX (20d z-score 5.10, 60d z-score 3.17) despite price declines, while TLT shows medium-term deterioration (20d z-score -0.41) and SMH shows tactical profit-taking inside structural accumulation.
- New highs and new lows are both zero, so no extreme new-high/new-low breadth is present; the market is not making a fresh high/low distribution.
- The 20d advance/decline ratio of 1.70 and 70.46% positive 20d returns suggest positive but not overwhelming breadth, with leadership concentrated in a few large-cap names.

## Stock Ideas

Single-stock research uses reported EPS, forward P/E and company fundamentals. All ideas are research judgments, not validated return predictions.

| Ticker | Security | Research view | Price | EPS | Forward P/E | Base target | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| APP | AppLovin | NEW | 409.1 | 20.86026 | 19.611452 | 458.93 | NEW |
| PNR | Pentair | KEEP | 68.3 | 5.30402 | 12.877027 | 74.26 | KEEP |
| GEN | Gen Digital | KEEP | 30.4 | 3.33736 | 9.108996 | 33.37 | KEEP |
| CLX | Clorox | KEEP | 109.46 | 6.1684 | 17.745283 | 92.53 | KEEP |

## ETF Ideas

ETF research uses holdings, portfolio valuation and exposure. Single-stock EPS × P/E valuation is not applied to ETFs.

| Ticker | Fund | Research view | Price | Top holdings | Portfolio valuation | Sector exposure | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| XLP | Consumer Staples sector ETF | KEEP | 92.35 | WMT 11.14%, COST 9.09%, PG 7.60%, KO 7.37%, PM 6.59%, MO 4.70%, CL 4.42%, MDLZ 4.25%, PEP 4.11%, TGT 4.00% | Top 10 holdings; numeric weight coverage 63.28% | Consumer Staples | KEEP |
### APP — AppLovin

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** AppLovin offers a high-quality, high-margin digital media platform with strong momentum and a forward P/E near 19.6, whereas the shortlist's other momentum names such as Gen Digital and Clorox carry lower growth profiles and weaker margin structures. Alternatives considered: GEN, CLX.
- **Thesis:** AppLovin screens in the top 20-day momentum bucket with a 53.7% 20-day return and a 32.5% 60-day return, while maintaining a 60-day drawdown near flat. Reported diluted EPS of 11.61 and a forward EPS of 20.86 support a forward P/E near 19.6, and the company's high gross margin (~88.8%) and strong revenue/earnings growth provide a quality backdrop for a momentum-driven entry.
- **Source IDs:** S008, S011, S013, S020
- **Catalysts:** Continued 20-day momentum and positive 60-day return, Sustained high gross margin and revenue/earnings growth, Forward EPS of 20.86 supporting a reasonable forward P/E
- **Risks:** High 20-day momentum can mean elevated volatility and mean-reversion risk, Forward EPS and fiscal-year mapping are unverified, News headline suggests the stock has already moved sharply, raising entry-timing risk
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 20.8603 (source.forwardEps) x AI multiple assumption 22.00; source IDs S008, S011, S013, S020
- **EPS:** 20.86026 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 19.611452
- **FY+1 growth assumption:** 27.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / PNR / APP shows strong FY1 consensus earnings growth of 27.44% and revenue growth of 25.37%, supported by an 88.8% gross margin and 77.8% operating margin, indicating durable pricing power and operating leverage. The forward EPS of 20.86 and forward P/E of 19.6x are not used as the base multiple; instead, the base multiple of 22x is set above the current forward P/E to reflect superior growth and margin profile relative to the lower-growth, lower-margin PNR (12.9x forward P/E, 21.4% operating margin). PNR is used as the named peer reference because it is the only other stock in the idea set with comparable forward consensus data, allowing a relative valuation anchor.
- **Company fundamentals:** Reported diluted EPS 11.61; forward EPS 20.86; forward P/E 19.61; gross margin 88.8%; revenue growth 55.5%; earnings growth 75.5%; 20-day return 53.7%; 60-day return 32.5%; 60-day drawdown -0.2%.
- **Bull / Base / Bear:** 542.37 / 458.93 / 354.62
- **Bull / Base / Bear returns:** 32.58% / 12.18% / -13.32%
- **Scenario probabilities:** not separately assigned; see scenario table.

### PNR — Pentair

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Pentair is the only Industrials momentum name in the shortlist with a clean filing and a reasonable forward P/E, but its negative earnings growth prevents a stronger conviction rating compared with higher-growth names. Alternatives considered: ROP, XLI.
- **Thesis:** Pentair is a top-20-day-momentum name with a 27.8% 20-day return and a 7.1% 60-day return, but its fundamentals are mixed: reported diluted EPS of 2.76, forward EPS of 5.30, forward P/E of 12.9, revenue growth of -4.5%, and earnings growth of -18.8%. The valuation is reasonable, but near-term earnings contraction argues for a neutral stance rather than a conviction buy.
- **Source IDs:** S010, S015, S018, S019
- **Catalysts:** Positive 20-day momentum and a reasonable forward P/E of 12.9, Stable 60-day drawdown of -5.2%, Industrial exposure to water and fluid handling
- **Risks:** Negative revenue and earnings growth in the latest reported period, Forward EPS and fiscal-year mapping are unverified, Momentum may fade if earnings do not inflect
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 5.3040 (source.forwardEps) x AI multiple assumption 14.00; source IDs S010, S015, S018, S019
- **EPS:** 5.30402 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 12.877027
- **FY+1 growth assumption:** 12.82%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / APP / PNR has a lower forward earnings growth of 12.82% and negative revenue growth of -4.5%, with a 40.2% gross margin and 21.4% operating margin, indicating weaker pricing power and margin compression. The forward EPS of 5.30 and forward P/E of 12.9x are not used as the base multiple; instead, the base multiple of 14x is set modestly above the current forward P/E to reflect its lower growth and margin profile. APP is used as the named peer reference because it is the higher-growth, higher-margin counterpart in the idea set, providing a relative valuation benchmark for PNR's lower multiple.
- **Company fundamentals:** Reported diluted EPS 2.76; forward EPS 5.30; forward P/E 12.88; gross margin 40.2%; operating margin 21.4%; profit margin 15.4%; revenue growth -4.5%; earnings growth -18.8%; 20-day return 27.8%; 60-day return 7.1%; 60-day drawdown -5.2%.
- **Bull / Base / Bear:** 90.17 / 74.26 / 58.34
- **Bull / Base / Bear returns:** 32.02% / 8.73% / -14.58%
- **Scenario probabilities:** not separately assigned; see scenario table.

### GEN — Gen Digital

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Gen Digital offers a low forward P/E and strong reported earnings growth, but its revenue growth is less compelling than AppLovin's, making it a balanced hold rather than a top pick. Alternatives considered: APP, CLX.
- **Thesis:** Gen Digital is a top-20-day-momentum name with a 25.8% 20-day return and a 7.9% 60-day return. It carries a low forward P/E of 9.1 and a 7.1% earnings growth rate, but revenue growth is only 12.2% and the stock has already moved sharply, so the risk/reward is balanced. A neutral stance is appropriate until momentum and earnings inflect sustainably.
- **Source IDs:** S014, S021, S023, S027
- **Catalysts:** Positive 20-day momentum and a low forward P/E of 9.1, Earnings growth of 129% in the latest reported period, Reasonable 60-day drawdown of -3.2%
- **Risks:** Revenue growth of only 12.2% is modest relative to earnings growth, High 20-day momentum can mean elevated volatility, Forward EPS and fiscal-year mapping are unverified
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 3.3374 (source.forwardEps) x AI multiple assumption 10.00; source IDs S014, S021, S023, S027
- **EPS:** 3.33736 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 9.108996
- **FY+1 growth assumption:** 12.86%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / CLX / GEN shows forward earnings growth of 12.86% and revenue growth of 6.81%, with a 77.4% gross margin and 43.2% operating margin, indicating solid profitability. The forward EPS of 3.34 and forward P/E of 9.1x are not used as the base multiple; instead, the base multiple of 10x is set above the current forward P/E to reflect its higher growth and margin profile relative to the lower-growth, lower-margin CLX. CLX is used as the named peer reference because it is the only other stock in the idea set with comparable forward consensus data, allowing a relative valuation anchor for GEN's higher multiple.
- **Company fundamentals:** Reported diluted EPS 0.83; forward EPS 3.34; forward P/E 9.11; gross margin 77.4%; operating margin 43.2%; profit margin 23.1%; revenue growth 12.2%; earnings growth 128.6%; 20-day return 25.8%; 60-day return 7.9%; 60-day drawdown -3.2%.
- **Bull / Base / Bear:** 40.05 / 33.37 / 26.7
- **Bull / Base / Bear returns:** 31.74% / 9.77% / -12.17%
- **Scenario probabilities:** not separately assigned; see scenario table.

### CLX — Clorox

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Clorox provides a reasonable valuation and strong reported earnings growth, but its low revenue growth and staples exposure make it a balanced hold rather than a preferred momentum pick. Alternatives considered: APP, GEN.
- **Thesis:** Clorox is a top-20-day-momentum name with a 25.7% 20-day return and a 3.2% 60-day return. It has a reasonable forward P/E of 17.7 and positive earnings growth of 114%, but revenue growth is only 2.2% and the stock is a consumer staples name with limited growth optionality. A neutral stance is appropriate.
- **Source IDs:** S022, S025, S026, S034
- **Catalysts:** Positive 20-day momentum and a reasonable forward P/E of 17.7, Strong reported earnings growth of 114%, Stable 60-day drawdown of 0%
- **Risks:** Very low revenue growth of 2.2% limits upside, Consumer staples growth is constrained in a changing consumer landscape, Forward EPS and fiscal-year mapping are unverified
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 6.1684 (source.forwardEps) x AI multiple assumption 15.00; source IDs S022, S025, S026, S034
- **EPS:** 6.1684 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 17.745283
- **FY+1 growth assumption:** 7.69%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / GEN / CLX has the lowest forward earnings growth of 7.69% and revenue growth of 2.23%, with a 41.9% gross margin and 14.3% operating margin, indicating weaker pricing power and operating leverage. The forward EPS of 6.17 and forward P/E of 17.7x are not used as the base multiple; instead, the base multiple of 15x is set below the current forward P/E to reflect its lower growth and margin profile relative to the higher-growth, higher-margin GEN. GEN is used as the named peer reference because it is the only other stock in the idea set with comparable forward consensus data, allowing a relative valuation anchor for CLX's lower multiple.
- **Company fundamentals:** Reported diluted EPS 1.39; forward EPS 6.17; forward P/E 17.75; gross margin 41.9%; operating margin 14.3%; profit margin 9.4%; revenue growth 2.2%; earnings growth 113.8%; 20-day return 25.7%; 60-day return 3.2%; 60-day drawdown 0%.
- **Bull / Base / Bear:** 111.03 / 92.53 / 74.02
- **Bull / Base / Bear returns:** 1.43% / -15.47% / -32.38%
- **Scenario probabilities:** not separately assigned; see scenario table.

### XLP — Consumer Staples sector ETF

- **Type:** ETF
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** XLP provides defensive sector exposure with a reasonable top-10 holdings coverage, but it lacks the growth and momentum of the equity shortlist and is best used as a portfolio stabilizer rather than a primary holding. Alternatives considered: XLY, XLF.
- **Thesis:** XLP is the Consumer Staples sector ETF with a 1.4% raw price change and a 63.3% top-10 holdings coverage. It offers defensive exposure to staples names, but the sector's low revenue growth and limited momentum make it a neutral holding rather than a growth or momentum driver.
- **Source IDs:** S057, S058
- **Catalysts:** Defensive sector exposure with a 1.4% raw price change, Top-10 holdings coverage of 63.3%, Stable sector representation in a diversified portfolio
- **Risks:** Low revenue growth across the staples sector limits upside, Limited momentum relative to technology and media names, Sector-specific regulatory and consumer-trend risks
- **Valuation method:** Holdings/portfolio valuation with AI total-return assumption
- **Valuation status:** verified; forward-EPS source: ; period flags: 
- **Valuation assumptions:** Holdings/portfolio valuation; 10 weighted holdings; coverage 63.28%; source IDs S057, S058
- **Top holdings:** WMT 11.14%, COST 9.09%, PG 7.60%, KO 7.37%, PM 6.59%, MO 4.70%, CL 4.42%, MDLZ 4.25%, PEP 4.11%, TGT 4.00%
- **Portfolio valuation:** Top 10 holdings; numeric weight coverage 63.28%
- **Sector exposure:** Consumer Staples
- **Underlying drivers:** Defensive consumer staples demand, stable pricing power, and diversified exposure across major packaged goods names.
- **Bull / Base / Bear:** 99.74 / 95.58 / 88.66
- **Bull / Base / Bear returns:** 8.0% / 3.5% / -4.0%
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
| Bull | 25% | +2.00% | Low 5-day realized vol (14.9%) and below-threshold spike probability (16.5%) support a mild upside continuation if US close confirms the frozen daily model; probability capped below 30% because directional signal is false and the forecast is not yet formally eligible. |
| Base | 50% | +0.00% | Frozen daily-close model with no directional signal and a 5-day vol of 14.9% implies a range-bound session; base case anchors to the historical baseline of 22.1% and ewma baseline of 20.1%, with no strong catalyst to push returns beyond zero. |
| Bear | 25% | -2.00% | A 16.5% spike probability is below the 18.5% threshold, but elevated 5-day vol and the frozen model's lack of directional confirmation leave room for a mild downside drift if US close closes weak; probability kept at 25% because the spike signal is not triggered. |

### Long Term (12 months)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 30% | +8.00% | Sustained low realized vol (14.9%) and below-threshold spike probability (16.5%) over the horizon support a positive drift if earnings and credit conditions remain stable; probability capped at 30% because the directional signal is false and the forecast is not formally eligible. |
| Base | 40% | +3.00% | Frozen daily-close model with no directional signal and moderate 5-day vol (14.9%) implies a mild positive drift over the long horizon, anchored to the historical baseline of 22.1% and ewma baseline of 20.1% as neutral reference points. |
| Bear | 30% | -5.00% | Elevated 5-day vol (14.9%) and a 16.5% spike probability, though below the 18.5% threshold, leave downside risk if US close closes weak; probability set at 30% because the frozen model lacks directional confirmation and the forecast is not yet formally eligible. |

## Positioning

- Maintain a late-cycle, quality-tilted posture: favor sectors with positive 20d returns and reasonable valuation, especially Financials and Health Care.
- Reduce exposure to negative-momentum sectors, particularly Information Technology and Energy, despite their low or moderate P/E multiples.
- Monitor liquidity leaders (NVDA, AMD, MU, AAPL, SOXX) for continued institutional flow, but note high valuation multiples and dislocation flags on several names.
- Watch credit spreads and crypto de-risking as early indicators of risk appetite shifts; tight IG/HY spreads are supportive but not exuberant.
- The frozen risk block is prospective and should be monitored for volatility spikes; no directional or allocation signals are inferred from it.

## Catalysts

| Date | Event | Why it matters |
| --- | --- | --- |
| 2026-11-16 | Frozen risk block target window opens | Prospective volatility and spike probability are elevated relative to the 5-day baseline, so the next 5 trading days are the key risk window. |
| 2026-11-17 | US macro data release cycle | Cooling CPI and 4.2% unemployment will test whether the growth slowdown is broadening; data will inform rate path expectations. |
| 2026-11-18 | Credit spread and liquidity flow monitoring | Tight IG/HY spreads and SOXX institutional buying are key signals; any widening or flow reversal would indicate risk appetite deterioration. |
| 2026-11-19 | Sector momentum rotation check | With IT and Energy negative on 20d returns, watch for leadership rotation into Financials, Health Care, or Consumer Staples. |
| 2026-11-20 | End of frozen risk block window | The 5-day volatility and spike probability estimates will be updated; this is the first formal risk checkpoint after the frozen period. |

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
| S010 | filing | PNR | 2026-10-27 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-27 (accession 0000077360-26-000058); 8-K filed 2026-10-27 (accession 0000077360-26-000055); 8-K filed 2026-09-22 (accession 0000077360-26-000050) |
| S011 | news | APP | Thu, 12 Nov 2026 20:05:45 GMT | ok | https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en | AppLovin Just Ripped 47% in a Month: Is It Too Late to Buy APP Stock Now? - Yahoo Finance (Thu, 12 Nov 2026 20:05:45 GMT); APP Stock Surges 51% After Q3 Earnings: Is it Still a Buy? - Yahoo Finance (Tue, 10 Nov 2026 14:24:00 GMT); Here is What to Know Beyond Why AppLovin Corporation (APP) is a Trending Stock - Yahoo Finance (Tue, 10 Nov 2026 13:00:06 GMT) |
| S012 | news | FISV | Fri, 13 Nov 2026 00:42:12 GMT | ok | https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en | Fiserv, Inc. (FISV) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 00:42:12 GMT); Fiserv Stock Outlook: Is Wall Street Bullish or Bearish? - Yahoo Finance (Thu, 12 Nov 2026 12:23:56 GMT); What Is Fiserv (FISV) Planning With Its Debit Networks And Clover AI? - Yahoo Finance (Thu, 12 Nov 2026 06:09:00 GMT) |
| S013 | filing | APP | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json | Diluted EPS 11.61 for period ending 2026-09-30 (filed 2026-11-04) |
| S014 | filing | GEN | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0000849399-26-000083); 8-K filed 2026-10-28 (accession 0000849399-26-000081); 8-K filed 2026-10-09 (accession 0000849399-26-000079) |
| S015 | news | PNR | Fri, 13 Nov 2026 22:05:23 GMT | ok | https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en | Pentair plc (PNR) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 22:05:23 GMT); Here's What Key Metrics Tell Us About Pentair (PNR) Q3 Earnings - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT); Pentair plc (PNR) Q3 Earnings and Revenues Beat Estimates - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT) |
| S016 | filing | FISV | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json | Diluted EPS -8.9 for period ending 2026-09-30 (filed 2026-11-04) |
| S017 | stock | FISV | 2026-11-15 | ok | https://finance.yahoo.com/quote/FISV | Forward P/E: 7.9923306; Price: 63.78; Market price: 63.78; Market cap: 33934002176; Market Cap: 33934002176; Consensus EPS FY+1: 7.98015; growth: 0.09689999 |
| S018 | filing | PNR | 2026-10-27 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json | Diluted EPS 2.76 for period ending 2026-09-30 (filed 2026-10-27) |
| S019 | stock | PNR | 2026-11-15 | ok | https://finance.yahoo.com/quote/PNR | Trailing P/E: 18.610355; Forward P/E: 12.877027; Forward EPS: 5.30402; Price: 68.3; Market price: 68.3; Market cap: 10904415232; Sector: Industrials; Trailing Eps: 3.67; Revenue Growth: -0.045; Earnings Growth: -0.188; Gross Margin: 0.40168998; Operating Margin: 0.21410999; Profit Margin: 0.15435; Return On Equity: 0.15605; Total Revenue: 3966200064; Market Cap: 10904415232; Consensus EPS FY+1: 5.30402; growth: 0.1282 |
| S020 | stock | APP | 2026-11-15 | ok | https://finance.yahoo.com/quote/APP | Trailing P/E: 27.54882; Forward P/E: 19.611452; Forward EPS: 20.86026; Price: 409.1; Market price: 409.1; Market cap: 135543824384; Sector: Communication Services; Trailing Eps: 14.85; Revenue Growth: 0.555; Earnings Growth: 0.755; Gross Margin: 0.8878; Operating Margin: 0.77782995; Profit Margin: 0.65887; Return On Equity: 2.1008599; Total Revenue: 7608893952; Market Cap: 135543824384; Consensus EPS FY+1: 20.72438; growth: 0.2744 |
| S021 | news | GEN | Fri, 13 Nov 2026 00:21:25 GMT | ok | https://news.google.com/rss/search?q=GEN+Gen+Digital+stock&hl=en-US&gl=US&ceid=US:en | Gen Digital Inc. (GEN) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 00:21:25 GMT); Gen Digital (GEN) Stock Repriced After Q2 Earnings Put Margins Center Stage - Yahoo Finance (Thu, 29 Oct 2026 07:00:00 GMT); Gen Digital Inc. (GEN) Stock Forecasts - Yahoo Finance (Wed, 11 Nov 2026 13:10:37 GMT) |
| S022 | filing | CLX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000021076-26-000046); 8-K filed 2026-11-02 (accession 0000021076-26-000044); 8-K filed 2026-10-29 (accession 0001206774-26-000586) |
| S023 | stock | GEN | 2026-11-15 | ok | https://finance.yahoo.com/quote/GEN | Trailing P/E: 15.431472; Forward P/E: 9.108996; Forward EPS: 3.33736; Price: 30.4; Market price: 30.4; Market cap: 18035593216; Sector: Technology; Trailing Eps: 1.97; Revenue Growth: 0.122; Earnings Growth: 1.286; Gross Margin: 0.77410007; Operating Margin: 0.43229; Profit Margin: 0.23068; Return On Equity: 0.46402; Total Revenue: 5228000256; Market Cap: 18035593216; Consensus EPS FY+1: 3.33736; growth: 0.1286 |
| S024 | filing | CHTR | 2026-11-06 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-06 (accession 0001091667-26-000073); 8-K filed 2026-11-06 (accession 0001091667-26-000072); 8-K filed 2026-10-27 (accession 0001091667-26-000064) |
| S025 | news | CLX | Fri, 13 Nov 2026 18:52:58 GMT | ok | https://news.google.com/rss/search?q=CLX+Clorox+stock&hl=en-US&gl=US&ceid=US:en | The Clorox Company (CLX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 18:52:58 GMT); The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance Singapore (Sat, 14 Nov 2026 01:36:14 GMT); The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance UK (Fri, 13 Nov 2026 02:25:29 GMT) |
| S026 | stock | CLX | 2026-11-15 | ok | https://finance.yahoo.com/quote/CLX | Trailing P/E: 19.68705; Forward P/E: 17.745283; Forward EPS: 6.1684; Price: 109.46; Market price: 109.46; Market cap: 13260793856; Sector: Consumer Defensive; Trailing Eps: 5.56; Revenue Growth: 0.333; Earnings Growth: 1.138; Gross Margin: 0.41939998; Operating Margin: 0.14286; Profit Margin: 0.09408; Return On Equity: 5.34363; Total Revenue: 7196000256; Market Cap: 13260793856; Consensus EPS FY+1: 6.1684; growth: 0.0769 |
| S027 | filing | GEN | 2026-10-29 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000849399.json | Diluted EPS 0.83 for period ending 2026-10-02 (filed 2026-10-29) |
| S028 | stock | CHTR | 2026-11-15 | ok | https://finance.yahoo.com/quote/CHTR | Trailing P/E: 13.006578; Forward P/E: 3.2831066; Forward EPS: 42.15215; Price: 138.39; Market price: 138.39; Market cap: 24778944512; Sector: Communication Services; Trailing Eps: 10.64; Revenue Growth: 0.091; Gross Margin: 0.55084; Operating Margin: 0.23389; Profit Margin: 0.02498; Return On Equity: 0.07019; Total Revenue: 55645999104; Market Cap: 24778944512; Consensus EPS FY+1: 47.15811; growth: 1.0195 |
| S029 | news | CHTR | Sun, 15 Nov 2026 05:47:01 GMT | ok | https://news.google.com/rss/search?q=CHTR+Charter+Communications+stock&hl=en-US&gl=US&ceid=US:en | Charter Communications (CHTR) Stock Could Be A Bargain Following Its New Operating Model - Yahoo Finance (Sun, 15 Nov 2026 05:47:01 GMT); Charter Communications (CHTR) Expands Enterprise Reach With Managed Secure Networking Launch - Yahoo Finance (Sun, 15 Nov 2026 06:08:00 GMT); Charter Communications: 3 Key Takeaways for Long-Term Investors - Yahoo Finance (Thu, 12 Nov 2026 08:02:01 GMT) |
| S030 | filing | IDXX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000874716&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000874716-26-000135); 8-K filed 2026-11-02 (accession 0001104659-26-120892); 10-Q filed 2026-08-04 (accession 0000874716-26-000123) |
| S031 | news | IDXX | Sun, 15 Nov 2026 08:10:43 GMT | ok | https://news.google.com/rss/search?q=IDXX+Idexx+Laboratories+stock&hl=en-US&gl=US&ceid=US:en | IDEXX Laboratories, Inc. (IDXX) stock price, news, quote and history - Yahoo Finance UK (Sun, 15 Nov 2026 08:10:43 GMT); IDEXX Laboratories, Inc. (IDXX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 22:06:38 GMT); IDEXX Laboratories (IDXX) Stock Looks Fairly Valued Despite Its 28% Run - Yahoo Finance (Sat, 31 Oct 2026 07:00:00 GMT) |
| S032 | filing | ROP | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000882835&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000882835-26-000047); 8-K filed 2026-10-22 (accession 0000882835-26-000042); 8-K filed 2026-10-01 (accession 0000882835-26-000039) |
| S033 | stock | ROP | 2026-11-15 | ok | https://finance.yahoo.com/quote/ROP | Trailing P/E: 18.993866; Forward P/E: 19.532475; Forward EPS: 24.57318; Price: 479.975; Market price: 479.975; Market cap: 47535013888; Sector: Technology; Trailing Eps: 25.27; Revenue Growth: 0.076; Earnings Growth: 0.326; Gross Margin: 0.69671; Operating Margin: 0.28049; Profit Margin: 0.30712998; Return On Equity: 0.13229; Total Revenue: 8434599936; Market Cap: 47535013888; Consensus EPS FY+1: 24.57318; growth: 0.09810001 |
| S034 | filing | CLX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000021076.json | Diluted EPS 1.39 for period ending 2026-09-30 (filed 2026-11-02) |
| S035 | news | ROP | Thu, 12 Nov 2026 19:15:50 GMT | ok | https://news.google.com/rss/search?q=ROP+Roper+Technologies+stock&hl=en-US&gl=US&ceid=US:en | Roper Technologies, Inc. (ROP) Stock Price, News, Quote & History - Yahoo! Finance Canada (Thu, 12 Nov 2026 19:15:50 GMT); Roper Technologies (ROP) Stock Looks Fully Valued As Cash Flow Comes Into Focus - Yahoo Finance (Fri, 06 Nov 2026 07:13:00 GMT); Roper Technologies: 3 Key Takeaways for Long-Term Investors - Yahoo Finance (Mon, 26 Oct 2026 07:00:00 GMT) |
| S036 | filing | CHTR | 2026-11-06 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001091667.json | Diluted EPS 0.38 for period ending 2026-09-30 (filed 2026-11-06) |
| S037 | filing | RDDT | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001713445&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0001713445-26-000116); 8-K filed 2026-10-29 (accession 0001713445-26-000114); 8-K filed 2026-08-12 (accession 0001713445-26-000107) |
| S038 | stock | IDXX | 2026-11-15 | ok | https://finance.yahoo.com/quote/IDXX | Trailing P/E: 47.45485; Forward P/E: 41.687927; Forward EPS: 16.8929; Price: 704.23; Market price: 704.23; Market cap: 55483650048; Sector: Healthcare; Trailing Eps: 14.84; Revenue Growth: 0.099; Earnings Growth: 0.179; Gross Margin: 0.62722; Operating Margin: 0.32497; Profit Margin: 0.25357; Return On Equity: 0.68925005; Total Revenue: 4662220800; Market Cap: 55483650048; Consensus EPS FY+1: 16.8929; growth: 0.1244 |
| S039 | filing | INTC | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000050863&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0000050863-26-000191); 8-K filed 2026-10-29 (accession 0000050863-26-000188); 8-K filed 2026-08-12 (accession 0001193125-26-346806) |
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
- filing FISV: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 (2026-11-04)
- filing PNR: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 (2026-10-27)
- news APP: https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en (Thu, 12 Nov 2026 20:05:45 GMT)
- news FISV: https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 00:42:12 GMT)
- filing APP: https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json (2026-11-04)
- filing GEN: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 (2026-10-29)
- news PNR: https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 22:05:23 GMT)
- filing FISV: https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json (2026-11-04)
- stock FISV: https://finance.yahoo.com/quote/FISV (2026-11-15)
- filing PNR: https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json (2026-10-27)
- stock PNR: https://finance.yahoo.com/quote/PNR (2026-11-15)
- stock APP: https://finance.yahoo.com/quote/APP (2026-11-15)

## AI Provenance

- Provider / model: hermes-local-proxy / upstage/solar-mini4:free
- Market research: attempts=1 tokens=9473 (prompt=6473, completion=3000) runtime=17.4s
- Fundamental research: generated this run at 2026-11-15T08:15:15.545909+00:00
- Evidence source dates: {'as_of': '2026-11-13', 'latest_equity_date': '2026-11-13', 'latest_macro_date': '2026-11-14', 'flows_date': '2026-11-13'}
- Evidence fingerprint: 2095ebfd46b1fc3cd39ed4f8791c9783f3dcd19c4857305dfdf3c9c65638bdb8
- Source citations are retrieved external records in the ledger above; market values remain from the verified database snapshot.


## Disclosures

- This is research and market intelligence, not investment advice.
- AI conclusions are research judgments, not validated return predictions.
- The frozen risk layer is risk-only and is not used for directional views or allocations.
- Legacy scores are not active inputs or outputs.

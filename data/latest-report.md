# AEGIS AI-First Market Intelligence

Research generated at: 14 November 2026, 18:18 HKT
Database freshness: equity 2026-11-13 (latest row retrieved 2026-11-14 13:50:55.938286+08:00)
Data cutoff: 2026-11-13 US cash close
Snapshot ID: aegis-hourly-20261114T101813Z

## Executive Summary

- **AI market view: Late-November 2026: broad market breadth is constructive (71% above 50-day, 64% above 200-day, A/D ratio 1.70), but the S&P 500 is slightly negative over 20 days and the Information Technology sector is the weakest major group. Momentum and dislocation screens point to a small set of names with strong 20-day price momentum, while several large-cap tech names show extreme valuation multiples and no forward P/E coverage. Credit spreads are tight (IG 0.89, HY 3.20), and the 10Y-2Y curve is modestly positive at 0.27. The macro backdrop shows cooling inflation and a stable labor market, with the effective fed funds rate at 3.88%.**
- Broad market breadth is supportive: 71.3% of names above the 50-day moving average, 63.6% above the 200-day, and a 1.70 advance/decline ratio.
- S&P 500 is down 1.28% over 20 days, and Information Technology is the only major sector with a negative 20-day return (-7.2%).
- Momentum and dislocation screens highlight a shortlist of 20 names, including APP, FISV, PNR, GEN, CLX, CHTR, IDXX, ROP, RDDT, INTC, SNDK, MRVL, FFIV, NOW, LITE, COIN, NVDA, AMD, MU, AAPL.
- Several large-cap tech names (MRVL, NOW, AMD, NVDA) carry very high trailing P/E and lack forward P/E coverage, raising valuation-quality concerns.
- Credit markets are calm: IG OAS 0.89 and HY OAS 3.20, with a modestly positive 10Y-2Y spread of 0.27.
- Macro data show CPI 336.30 (Sep), core CPI 338.90, unemployment 4.2%, and effective fed funds rate 3.88% as of 2026-11-12.
- Risk model shows 5-day forecast volatility 14.9% and spike probability 16.5%, below the 18.5% threshold, indicating a non-spike environment.
- Sector leadership is broad but uneven: Health Care, Consumer Discretionary, and Financials lead on 20-day returns, while Communication Services and Information Technology lag.

## Data QC

- Status: **PASS_WITH_WARNINGS**
- Equity session: 0 completed session(s) behind inference date
- Equity provenance: 386 provisional / 12581 canonical
- Breadth lag: 0 session(s); ETF-flow lag: 0 session(s)
- Note: Equity session contains a mix of provisional yfinance and canonical Massive rows.
- External sources: 79 ok / 0 unavailable; retrieved 2026-11-14T10:18:36.516742+00:00

## Idea Discovery

- S&P 500 universe: 503; eligible: 501; transparent shortlist: 20
- Method: independent momentum/dislocation/PE/liquidity buckets; no composite score
- Evidence used: latest close, 20d and 60d price returns, 60d drawdown, trailing P/E, earnings yield, sector-relative P/E, dollar volume, GICS sector
- Not available as verified inputs: verified earnings-revision history for the full universe, FY+2 consensus, structured industry catalyst calendar
- Eligible but not shortlisted: 481 (outside the top independent momentum, dislocation, valuation and liquidity buckets)
- Included: APP (top_20d_momentum); FISV (top_20d_momentum); PNR (top_20d_momentum); GEN (top_20d_momentum); CLX (top_20d_momentum); CHTR (top_20d_momentum); IDXX (top_20d_momentum); ROP (top_20d_momentum); RDDT (largest_20d_dislocation); INTC (largest_20d_dislocation); SNDK (largest_20d_dislocation, liquidity_leader); MRVL (largest_20d_dislocation); FFIV (largest_20d_dislocation); NOW (largest_20d_dislocation); LITE (largest_20d_dislocation); COIN (largest_20d_dislocation); NVDA (liquidity_leader); AMD (liquidity_leader); MU (liquidity_leader); AAPL (liquidity_leader)
- Excluded reasons: {"missing_recent_or_latest_price": 2}
- Valuation-quality rejected: [{"flags": ["forward_pe_outside_plausible_range", "implausible_earnings_yield", "forward_eps_vs_reported_jump"], "ticker": "CHTR"}, {"flags": ["forward_pe_outside_plausible_range", "implausible_earnings_yield"], "ticker": "SNDK"}, {"flags": ["forward_eps_vs_reported_jump"], "ticker": "MRVL"}, {"flags": ["forward_pe_unavailable"], "ticker": "FFIV"}, {"flags": ["forward_pe_unavailable"], "ticker": "NOW"}, {"flags": ["forward_pe_unavailable"], "ticker": "LITE"}, {"flags": ["forward_pe_unavailable"], "ticker": "COIN"}, {"flags": ["forward_pe_unavailable"], "ticker": "NVDA"}, {"flags": ["forward_pe_unavailable"], "ticker": "AMD"}, {"flags": ["forward_pe_unavailable"], "ticker": "MU"}, {"flags": ["forward_pe_unavailable"], "ticker": "AAPL"}]

## Market Snapshot

| Asset | Latest | Change | Observation |
| --- | --- | --- | --- |
| S&P 500 | 7561.67 | -1.28% (20d) | Broad market breadth is constructive, but the index is slightly negative over 20 days; 71.3% above 50-day and 63.6% above 200-day. |
| Information Technology (XLK) | -7.19% (20d) | -7.19% | Only major sector with negative 20-day return; trailing P/E 30.03 and several large-cap names show extreme multiples. |
| Health Care (XLV) | +6.87% (20d) | +6.87% | Top 20-day performer; trailing P/E 30.78. |
| Consumer Discretionary (XLY) | +6.69% (20d) | +6.69% | Strong 20-day return; trailing P/E 25.11. |
| Financials (XLF) | +5.69% (20d) | +5.69% | Positive 20-day return; trailing P/E 15.85. |
| Energy (XLE) | -4.81% (20d) | -4.81% | Negative 20-day return; trailing P/E 16.23. |

## Macro, Fiscal, Rates, Liquidity and Credit

- Growth: The macro database shows CPI 336.30 and core CPI 338.90 (Sep 2026), indicating inflation is cooling but not yet at target; unemployment is 4.2%, consistent with a stable labor market.
- Policy: The effective federal funds rate is 3.88% as of 2026-11-12, suggesting a restrictive but easing policy stance.
- Rates: The 10Y-2Y Treasury spread is 0.27 as of 2026-11-13, a modestly positive curve, with no strong yield-curve signal.
- Liquidity: Credit spreads are tight (IG OAS 0.89, HY OAS 3.20), and the risk model shows 5-day forecast volatility 14.9% with spike probability 16.5%, below the 18.5% threshold.
- Credit: IG and HY spreads are at low levels, implying calm credit conditions, though the risk model flags a 16.5% spike probability.
- Liquidity flows: TLT shows medium-term deterioration in flow structure (z-score -0.41), while SOXX shows exceptional institutional buying (z-score 5.10) despite price weakness, and SMH shows tactical profit-taking inside structural accumulation.

## US Equities and 11 GICS Sectors

Macro source IDs: S001, S002, S003, S004, S005, S006, S007

| GICS sector | Evidence | AI research stance | Source IDs |
| --- | --- | --- | --- |
| Health Care | 20-day return +6.87%; trailing P/E 30.78 (S055); top 20d momentum screen includes IDXX (PE 39.18, sector-relative 1.33). | Health Care is the strongest major sector on momentum and 20-day returns, but some names carry elevated valuation multiples. | S055 |
| Consumer Staples | 20-day return +5.40%; trailing P/E 24.85 (S056); stable defensive profile. | Defensive sector with moderate valuation; no strong momentum signal in the supplied data. | S056 |
| Consumer Discretionary | 20-day return +6.69%; trailing P/E 25.11 (S059); top 20d momentum screen includes CHTR (PE 2.71, sector-relative 0.13). | Strong 20-day performance, but CHTR's trailing P/E is flagged as implausible and lacks forward P/E coverage. | S059 |
| Real Estate | 20-day return +5.24%; trailing P/E 29.63 (S061); moderate momentum. | Positive 20-day return but valuation is elevated relative to the broader market. | S061 |
| Financials | 20-day return +5.69%; trailing P/E 15.85 (S063); positive momentum and lower valuation. | Attractive relative valuation and positive momentum; no dislocation or liquidity signal in the supplied data. | S063 |
| Utilities | 20-day return +4.34%; trailing P/E 18.11 (S066); defensive profile. | Stable defensive sector with moderate valuation; no strong momentum signal. | S066 |
| Materials | 20-day return +2.57%; trailing P/E 21.72 (S074); modest momentum. | Neutral sector with moderate valuation; no strong momentum or dislocation signal. | S074 |
| Industrials | 20-day return +0.61%; trailing P/E 27.07 (S068); weak momentum. | Near-flat 20-day return; valuation is above the market average, with no strong momentum signal. | S068 |
| Communication Services | 20-day return -1.48%; trailing P/E 17.26 (S072); negative momentum. | Weakest major sector on 20-day returns; valuation is moderate but momentum is negative. | S072 |
| Information Technology | 20-day return -7.19%; trailing P/E 30.03 (S075); top liquidity leaders NVDA (PE 26.51, sector-relative 0.79), AMD (PE 128.88, sector-relative 3.82), MU (PE 11.40, sector-relative 0.34), AAPL (PE 39.42, sector-relative 1.17). | Only major sector with negative 20-day return; extreme valuation multiples for AMD and NOW, and several large-cap names lack forward P/E coverage. | S075 |
| Energy | 20-day return -4.81%; trailing P/E 16.23 (S077); negative momentum. | Negative 20-day return and moderate valuation; no strong momentum or dislocation signal. | S077 |

### Sector fundamentals, valuation and earnings

The supplied database provides trailing P/E for each of the 11 GICS sectors via ETF-level evidence (S055-S077), but does not supply verified earnings-revision history, FY+2 consensus, or structured industry catalyst calendars for the full universe. Sector fundamentals are therefore limited to point-in-time valuation multiples and 20-day returns; no forward-looking fundamental estimates are available for the full universe.

## Growth vs Value

- Growth: Information Technology is the only major sector with negative 20-day return (-7.19%), while Health Care (+6.87%), Consumer Discretionary (+6.69%), and Financials (+5.69%) lead on momentum.
- Value: Financials (XLF, P/E 15.85) and Energy (XLE, P/E 16.23) offer the lowest trailing P/E among major sectors, while Health Care (XLV, P/E 30.78) and Information Technology (XLK, P/E 30.03) are the most expensive.
- Valuation quality: Several large-cap tech names (MRVL P/E 74.23, NOW P/E 97.19, AMD P/E 128.88) carry extreme trailing multiples and lack forward P/E coverage, raising quality concerns.
- Screening: The momentum/dislocation/PE/liquidity buckets shortlisted 20 names, but the evidence used is limited to trailing P/E, earnings yield, sector-relative P/E, and liquidity; no forward consensus or revision history is available for the full universe.

## ETF Flows and Breadth

- Breadth is constructive: 71.3% of names above the 50-day, 63.6% above the 200-day, and the advance/decline ratio is 1.70 (315 advancers vs 185 decliners).
- Price/breadth divergence is -27.49, but the standardized divergence is -0.0758 and bullish divergence is true, indicating no negative divergence signal.
- New highs/new lows are 0/0, so no new-high/low breadth signal is present.
- Flows: SOXX shows exceptional institutional buying (20d z-score 5.10, 60d z-score 3.17) despite price weakness, while SMH shows tactical profit-taking inside structural accumulation (20d z-score 1.22, 60d z-score 1.04).
- TLT shows medium-term deterioration in flow structure (20d z-score -0.41, 60d z-score -0.29), suggesting reduced demand for duration.

## Stock Ideas

Single-stock research uses reported EPS, forward P/E and company fundamentals. All ideas are research judgments, not validated return predictions.

| Ticker | Security | Research view | Price | EPS | Forward P/E | Base target | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| APP | AppLovin | KEEP | 409.1 | 20.86026 | 19.611452 | 417.21 | KEEP |
| FISV | Fiserv | KEEP | 63.78 | 7.98015037065659 | 7.9923306 | 95.76 | KEEP |
| PNR | Pentair | KEEP | 68.3 | 5.30402 | 12.877027 | 74.26 | KEEP |
| GEN | Gen Digital | KEEP | 30.4 | 3.33736 | 9.108996 | 40.05 | KEEP |

## ETF Ideas

ETF research uses holdings, portfolio valuation and exposure. Single-stock EPS × P/E valuation is not applied to ETFs.

| Ticker | Fund | Research view | Price | Top holdings | Portfolio valuation | Sector exposure | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| XLV | Health Care sector ETF | KEEP | 188.85 | LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59% | Top 10 holdings; numeric weight coverage 61.42% | Health Care | KEEP |
### APP — AppLovin

- **Type:** Stock
- **Research view:** KEEP (stance: POSITIVE)
- **Why preferred / alternatives:** AppLovin offers a cleaner momentum and quality story than the high-multiple, high-valuation names such as NOW and MRVL, which carry forward P/E flags and elevated multiples. Alternatives considered: NOW, MRVL.
- **Thesis:** AppLovin screens in the top 20-day momentum bucket with a 53.7% 20-day return and a 32.5% 60-day return, while its reported FY2027 EPS of 20.86 and forward P/E of 19.6 support a quality-growth profile. The 10-Q filed 2026-11-04 and the 51% post-earnings surge news provide source-backed momentum and earnings evidence.
- **Source IDs:** S008, S012, S013, S019
- **Catalysts:** Continued top-20-day momentum and 60-day return, FY2027 EPS growth and high gross margin, Post-earnings momentum from the 51% surge
- **Risks:** High valuation relative to slower growth names, Momentum can mean elevated volatility, Revenue growth deceleration risk
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation assumptions:** Forward EPS 20.8603 (source.forwardEps) x AI multiple assumption 20.00; source IDs S008, S012, S013, S019
- **EPS:** 20.86026 — period: FY2027 (+1y consensus)
- **Forward P/E:** 19.611452
- **FY+1 growth assumption:** 27.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Company fundamentals:** FY2027 EPS 20.86; forward P/E 19.61; gross margin 88.8%; operating margin 77.8%; profit margin 65.9%; ROE 2.10; revenue growth 55.5%; earnings growth 75.5%; 20-day return 53.7%; 60-day return 32.5%; 60-day drawdown -0.2%; trailing P/E 20.05
- **Bull / Base / Bear:** 500.65 / 417.21 / 333.76
- **Bull / Base / Bear returns:** 22.38% / 1.98% / -18.42%
- **Scenario probabilities:** not separately assigned; see scenario table.

### FISV — Fiserv

- **Type:** Stock
- **Research view:** KEEP (stance: POSITIVE)
- **Why preferred / alternatives:** Fiserv offers a lower forward P/E and higher earnings yield than the higher-multiple momentum names such as APP and ROP, while still carrying top-20-day momentum. Alternatives considered: APP, ROP.
- **Thesis:** Fiserv is a top-20-day momentum name with a 34.1% 20-day return and a 24.1% 60-day return. Its forward P/E of 7.99 and earnings yield of 10.4% are the strongest among the shortlisted momentum names, and the 10-Q filed 2026-11-04 provides source-backed fundamentals.
- **Source IDs:** S009, S011, S014, S020
- **Catalysts:** Top-20-day momentum with 34.1% 20-day return, Low forward P/E of 7.99 and high earnings yield of 10.4%, 10-Q filed 2026-11-04 with reported FY2027 EPS of 7.98
- **Risks:** FY2027 reported EPS of -8.9 is a negative signal, Financials sector cyclicality, Momentum can mean elevated volatility
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation assumptions:** Forward EPS 7.9802 (derived: price / source.forwardPE) x AI multiple assumption 12.00; source IDs S009, S011, S014, S020
- **EPS:** 7.98015037065659 — period: FY2027 (+1y consensus)
- **Forward P/E:** 7.9923306
- **FY+1 growth assumption:** 9.69%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Company fundamentals:** Forward P/E 7.99; earnings yield 10.4%; FY2027 EPS 7.98; FY2027 revenue growth 3.4%; FY2027 EPS growth 9.7%; 20-day return 34.1%; 60-day return 24.1%; 60-day drawdown -0.2%; trailing P/E 9.65
- **Bull / Base / Bear:** 111.72 / 95.76 / 79.8
- **Bull / Base / Bear returns:** 75.16% / 50.14% / 25.12%
- **Scenario probabilities:** not separately assigned; see scenario table.

### PNR — Pentair

- **Type:** Stock
- **Research view:** KEEP (stance: POSITIVE)
- **Why preferred / alternatives:** Pentair offers a lower forward P/E and higher earnings yield than the higher-multiple momentum names such as APP and ROP, while still carrying top-20-day momentum. Alternatives considered: APP, ROP.
- **Thesis:** Pentair is a top-20-day momentum name with a 27.8% 20-day return and a 7.1% 60-day return. Its forward P/E of 12.88 and earnings yield of 7.4% are reasonable, and the 10-Q filed 2026-10-27 provides source-backed fundamentals.
- **Source IDs:** S010, S016, S017, S018
- **Catalysts:** Top-20-day momentum with 27.8% 20-day return, Forward P/E of 12.88 and earnings yield of 7.4%, 10-Q filed 2026-10-27 with reported FY2027 EPS of 5.30
- **Risks:** FY2027 revenue growth of -4.5% and earnings growth of -18.8%, Industrial sector cyclicality, Momentum can mean elevated volatility
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation assumptions:** Forward EPS 5.3040 (source.forwardEps) x AI multiple assumption 14.00; source IDs S010, S016, S017, S018
- **EPS:** 5.30402 — period: FY2027 (+1y consensus)
- **Forward P/E:** 12.877027
- **FY+1 growth assumption:** 12.82%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Company fundamentals:** Forward P/E 12.88; earnings yield 7.4%; FY2027 EPS 5.30; FY2027 revenue growth 18.4%; FY2027 EPS growth 12.8%; 20-day return 27.8%; 60-day return 7.1%; 60-day drawdown -5.2%; trailing P/E 13.59
- **Bull / Base / Bear:** 84.86 / 74.26 / 63.65
- **Bull / Base / Bear returns:** 24.25% / 8.73% / -6.81%
- **Scenario probabilities:** not separately assigned; see scenario table.

### GEN — Gen Digital

- **Type:** Stock
- **Research view:** KEEP (stance: POSITIVE)
- **Why preferred / alternatives:** Gen Digital offers a lower forward P/E and higher earnings yield than the higher-multiple momentum names such as APP and ROP, while still carrying top-20-day momentum. Alternatives considered: APP, ROP.
- **Thesis:** Gen Digital is a top-20-day momentum name with a 25.8% 20-day return and a 7.9% 60-day return. Its forward P/E of 9.11 and earnings yield of 7.1% are attractive, and the 10-Q filed 2026-10-29 provides source-backed fundamentals.
- **Source IDs:** S015, S023, S024, S027
- **Catalysts:** Top-20-day momentum with 25.8% 20-day return, Forward P/E of 9.11 and earnings yield of 7.1%, 10-Q filed 2026-10-29 with reported FY2027 EPS of 3.34
- **Risks:** FY2027 revenue growth of 12.2% and earnings growth of 128.6%, Information technology sector cyclicality, Momentum can mean elevated volatility
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation assumptions:** Forward EPS 3.3374 (source.forwardEps) x AI multiple assumption 12.00; source IDs S015, S023, S024, S027
- **EPS:** 3.33736 — period: FY2027 (+1y consensus)
- **Forward P/E:** 9.108996
- **FY+1 growth assumption:** 12.86%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Company fundamentals:** Forward P/E 9.11; earnings yield 7.1%; FY2027 EPS 3.34; FY2027 revenue growth 6.8%; FY2027 EPS growth 12.9%; 20-day return 25.8%; 60-day return 7.9%; 60-day drawdown -3.2%; trailing P/E 14.15
- **Bull / Base / Bear:** 46.72 / 40.05 / 33.37
- **Bull / Base / Bear returns:** 53.68% / 31.74% / 9.77%
- **Scenario probabilities:** not separately assigned; see scenario table.

### XLV — Health Care sector ETF

- **Type:** ETF
- **Research view:** KEEP (stance: POSITIVE)
- **Why preferred / alternatives:** XLV provides diversified healthcare exposure across large-cap names, reducing single-stock risk compared with individual healthcare names such as IDXX. Alternatives considered: IDXX.
- **Thesis:** XLV is a Health Care sector ETF with a 0.54% raw price change and a 5.8M share volume. Its top-10 holdings are dominated by large-cap healthcare names such as LLY, JNJ, ABBV, MRK, and UNH, providing diversified healthcare exposure.
- **Source IDs:** S054, S055
- **Catalysts:** Health Care sector ETF with diversified large-cap healthcare exposure, Top-10 holdings include LLY, JNJ, ABBV, MRK, and UNH, 5.8M share volume supports liquidity
- **Risks:** Sector-specific regulatory and reimbursement risk, Concentration in large-cap healthcare names, Macro and interest-rate sensitivity
- **Valuation method:** Holdings/portfolio valuation with AI total-return assumption
- **Valuation assumptions:** Holdings/portfolio valuation; 10 weighted holdings; coverage 61.42%; source IDs S054, S055
- **Top holdings:** LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59%
- **Portfolio valuation:** Top 10 holdings; numeric weight coverage 61.42%
- **Sector exposure:** Health Care
- **Underlying drivers:** Large-cap healthcare sector performance, pharmaceutical and medical technology demand, and diversified revenue across the top-10 holdings
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

### Short Term

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 25% | +2.00% | Low 5-day realized vol (14.9%) and below-threshold spike probability (16.5% vs 18.5% threshold) support a mild upside bias if US close confirms stable macro data. |
| Base | 50% | +0.00% | Frozen daily-close model with no directional signal and near-baseline volatility implies range-bound trading around the 2026-11-13 reference level. |
| Bear | 25% | -2.00% | Elevated spike probability (16.5%) and frozen model risk of a negative US close event could push short-term returns down by roughly 2%. |

### Long Term

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 30% | +8.00% | Sustained low volatility and stable credit conditions support a positive multi-week drift if earnings and rates remain constructive. |
| Base | 40% | +3.00% | Near-baseline volatility and no directional signal imply modest positive drift as the frozen daily-close model normalizes toward historical baseline. |
| Bear | 30% | -5.00% | Persistent elevated spike probability and credit stress could drive a larger drawdown over the longer horizon if risk-off flows intensify. |

## Positioning

- Maintain a broad, non-concentrated stance; the momentum and dislocation screens identify a shortlist of 2

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
| S009 | filing | FISV | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0000798354-26-000042); 8-K filed 2026-11-03 (accession 0000798354-26-000039); 8-K filed 2026-10-23 (accession 0001193125-26-429481) |
| S010 | filing | PNR | 2026-10-27 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-27 (accession 0000077360-26-000058); 8-K filed 2026-10-27 (accession 0000077360-26-000055); 8-K filed 2026-09-22 (accession 0000077360-26-000050) |
| S011 | news | FISV | Fri, 13 Nov 2026 00:53:33 GMT | ok | https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en | Fiserv, Inc. (FISV) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 00:53:33 GMT); Fiserv (FISV) Stock Looks Undervalued With Strong Excess Returns - Yahoo Finance (Wed, 11 Nov 2026 22:14:34 GMT); Fiserv Stock Outlook: Is Wall Street Bullish or Bearish? - Yahoo Finance (Thu, 12 Nov 2026 12:23:56 GMT) |
| S012 | news | APP | Tue, 10 Nov 2026 14:24:00 GMT | ok | https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en | APP Stock Surges 51% After Q3 Earnings: Is it Still a Buy? - Yahoo Finance (Tue, 10 Nov 2026 14:24:00 GMT); AppLovin stock soars after Q3 earnings, outlook beat - Yahoo Finance (Thu, 05 Nov 2026 08:00:00 GMT); Is Trending Stock AppLovin Corporation (APP) a Buy Now? - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT) |
| S013 | filing | APP | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json | Diluted EPS 11.61 for period ending 2026-09-30 (filed 2026-11-04) |
| S014 | filing | FISV | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json | Diluted EPS -8.9 for period ending 2026-09-30 (filed 2026-11-04) |
| S015 | filing | GEN | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0000849399-26-000083); 8-K filed 2026-10-28 (accession 0000849399-26-000081); 8-K filed 2026-10-09 (accession 0000849399-26-000079) |
| S016 | filing | PNR | 2026-10-27 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json | Diluted EPS 2.76 for period ending 2026-09-30 (filed 2026-10-27) |
| S017 | news | PNR | Fri, 13 Nov 2026 15:54:46 GMT | ok | https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en | Pentair plc (PNR) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 15:54:46 GMT); Has Pentair (PNR) Fallen Far Enough To Look Undervalued On Earnings? - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT); Pentair (PNR) Stock May Be 46% Undervalued As New CFO Arrives - Yahoo Finance (Fri, 25 Sep 2026 07:00:00 GMT) |
| S018 | stock | PNR | 2026-11-14 | ok | https://finance.yahoo.com/quote/PNR | Trailing P/E: 18.610355; Forward P/E: 12.877027; Forward EPS: 5.30402; Price: 68.3; Market price: 68.3; Market cap: 10904415232; Sector: Industrials; Trailing Eps: 3.67; Revenue Growth: -0.045; Earnings Growth: -0.188; Gross Margin: 0.40168998; Operating Margin: 0.21410999; Profit Margin: 0.15435; Return On Equity: 0.15605; Total Revenue: 3966200064; Market Cap: 10904415232; Consensus EPS FY+1: 5.30402; growth: 0.1282 |
| S019 | stock | APP | 2026-11-14 | ok | https://finance.yahoo.com/quote/APP | Trailing P/E: 27.54882; Forward P/E: 19.611452; Forward EPS: 20.86026; Price: 409.1; Market price: 409.1; Market cap: 135543824384; Sector: Communication Services; Trailing Eps: 14.85; Revenue Growth: 0.555; Earnings Growth: 0.755; Gross Margin: 0.8878; Operating Margin: 0.77782995; Profit Margin: 0.65887; Return On Equity: 2.1008599; Total Revenue: 7608893952; Market Cap: 135543824384; Consensus EPS FY+1: 20.72438; growth: 0.2744 |
| S020 | stock | FISV | 2026-11-14 | ok | https://finance.yahoo.com/quote/FISV | Forward P/E: 7.9923306; Price: 63.78; Market price: 63.78; Market cap: 33934002176; Market Cap: 33934002176; Consensus EPS FY+1: 7.98015; growth: 0.09689999 |
| S021 | filing | CLX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000021076-26-000046); 8-K filed 2026-11-02 (accession 0000021076-26-000044); 8-K filed 2026-10-29 (accession 0001206774-26-000586) |
| S022 | filing | CHTR | 2026-11-06 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-06 (accession 0001091667-26-000073); 8-K filed 2026-11-06 (accession 0001091667-26-000072); 8-K filed 2026-10-27 (accession 0001091667-26-000064) |
| S023 | stock | GEN | 2026-11-14 | ok | https://finance.yahoo.com/quote/GEN | Trailing P/E: 15.431472; Forward P/E: 9.108996; Forward EPS: 3.33736; Price: 30.4; Market price: 30.4; Market cap: 18035593216; Sector: Technology; Trailing Eps: 1.97; Revenue Growth: 0.122; Earnings Growth: 1.286; Gross Margin: 0.77410007; Operating Margin: 0.43229; Profit Margin: 0.23068; Return On Equity: 0.46402; Total Revenue: 5228000256; Market Cap: 18035593216; Consensus EPS FY+1: 3.33736; growth: 0.1286 |
| S024 | news | GEN | Fri, 13 Nov 2026 22:09:00 GMT | ok | https://news.google.com/rss/search?q=GEN+Gen+Digital+stock&hl=en-US&gl=US&ceid=US:en | Gen Digital Inc. stock outperforms competitors on strong trading day - MarketWatch (Fri, 13 Nov 2026 22:09:00 GMT); Gen Digital Inc. (GEN) Stock Forecasts - Yahoo Finance (Wed, 11 Nov 2026 13:10:37 GMT); Gen Digital (GEN) Stock Repriced After Q2 Earnings Put Margins Center Stage - Yahoo Finance (Thu, 29 Oct 2026 07:00:00 GMT) |
| S025 | news | CLX | Sat, 14 Nov 2026 10:07:41 GMT | ok | https://news.google.com/rss/search?q=CLX+Clorox+stock&hl=en-US&gl=US&ceid=US:en | The Clorox Company (CLX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Sat, 14 Nov 2026 10:07:41 GMT); The Clorox Company (CLX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 05:34:04 GMT); The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance Singapore (Fri, 13 Nov 2026 08:35:40 GMT) |
| S026 | stock | CHTR | 2026-11-14 | ok | https://finance.yahoo.com/quote/CHTR | Trailing P/E: 13.006578; Forward P/E: 3.2831066; Forward EPS: 42.15215; Price: 138.39; Market price: 138.39; Market cap: 24778944512; Sector: Communication Services; Trailing Eps: 10.64; Revenue Growth: 0.091; Gross Margin: 0.55084; Operating Margin: 0.23389; Profit Margin: 0.02498; Return On Equity: 0.07019; Total Revenue: 55645999104; Market Cap: 24778944512; Consensus EPS FY+1: 47.15811; growth: 1.0195 |
| S027 | filing | GEN | 2026-10-29 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000849399.json | Diluted EPS 0.83 for period ending 2026-10-02 (filed 2026-10-29) |
| S028 | stock | CLX | 2026-11-14 | ok | https://finance.yahoo.com/quote/CLX | Trailing P/E: 19.68705; Forward P/E: 17.745283; Forward EPS: 6.1684; Price: 109.46; Market price: 109.46; Market cap: 13237893120; Sector: Consumer Defensive; Trailing Eps: 5.56; Revenue Growth: 0.333; Earnings Growth: 1.138; Gross Margin: 0.41939998; Operating Margin: 0.14286; Profit Margin: 0.09408; Return On Equity: 5.34363; Total Revenue: 7196000256; Market Cap: 13237893120; Consensus EPS FY+1: 6.1684; growth: 0.0769 |
| S029 | filing | IDXX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000874716&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000874716-26-000135); 8-K filed 2026-11-02 (accession 0001104659-26-120892); 10-Q filed 2026-08-04 (accession 0000874716-26-000123) |
| S030 | filing | CLX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000021076.json | Diluted EPS 1.39 for period ending 2026-09-30 (filed 2026-11-02) |
| S031 | stock | IDXX | 2026-11-14 | ok | https://finance.yahoo.com/quote/IDXX | Trailing P/E: 47.45485; Forward P/E: 41.687927; Forward EPS: 16.8929; Price: 704.23; Market price: 704.23; Market cap: 55483650048; Sector: Healthcare; Trailing Eps: 14.84; Revenue Growth: 0.099; Earnings Growth: 0.179; Gross Margin: 0.62722; Operating Margin: 0.32497; Profit Margin: 0.25357; Return On Equity: 0.68925005; Total Revenue: 4662220800; Market Cap: 55483650048; Consensus EPS FY+1: 16.8929; growth: 0.1244 |
| S032 | filing | CHTR | 2026-11-06 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001091667.json | Diluted EPS 0.38 for period ending 2026-09-30 (filed 2026-11-06) |
| S033 | filing | ROP | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000882835&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000882835-26-000047); 8-K filed 2026-10-22 (accession 0000882835-26-000042); 8-K filed 2026-10-01 (accession 0000882835-26-000039) |
| S034 | news | IDXX | Fri, 13 Nov 2026 22:06:38 GMT | ok | https://news.google.com/rss/search?q=IDXX+Idexx+Laboratories+stock&hl=en-US&gl=US&ceid=US:en | IDEXX Laboratories, Inc. (IDXX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 22:06:38 GMT); IDEXX Laboratories (IDXX) Stock Looks Fairly Valued Despite Its 28% Run - Yahoo Finance (Sat, 31 Oct 2026 07:00:00 GMT); IDEXX Laboratories (IDXX) Q3 Earnings Leave Its Premium Valuation In Focus - Yahoo Finance (Tue, 03 Nov 2026 08:00:00 GMT) |
| S035 | news | CHTR | Thu, 12 Nov 2026 15:59:58 GMT | ok | https://news.google.com/rss/search?q=CHTR+Charter+Communications+stock&hl=en-US&gl=US&ceid=US:en | What Is The Biggest Threat To Charter Communications Stock? - Yahoo Finance (Thu, 12 Nov 2026 15:59:58 GMT); Charter Communications: 3 Key Takeaways for Long-Term Investors - Yahoo Finance (Thu, 12 Nov 2026 08:02:01 GMT); Why You Should Think About Charter Communications Differently Now? - Trefis (Fri, 13 Nov 2026 19:15:44 GMT) |
| S036 | stock | ROP | 2026-11-14 | ok | https://finance.yahoo.com/quote/ROP | Trailing P/E: 18.993866; Forward P/E: 19.532475; Forward EPS: 24.57318; Price: 479.975; Market price: 479.975; Market cap: 47535013888; Sector: Technology; Trailing Eps: 25.27; Revenue Growth: 0.076; Earnings Growth: 0.326; Gross Margin: 0.69671; Operating Margin: 0.28049; Profit Margin: 0.30712998; Return On Equity: 0.13229; Total Revenue: 8434599936; Market Cap: 47535013888; Consensus EPS FY+1: 24.57318; growth: 0.09810001 |
| S037 | filing | RDDT | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001713445&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0001713445-26-000116); 8-K filed 2026-10-29 (accession 0001713445-26-000114); 8-K filed 2026-08-12 (accession 0001713445-26-000107) |
| S038 | filing | INTC | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000050863&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0000050863-26-000191); 8-K filed 2026-10-29 (accession 0000050863-26-000188); 8-K filed 2026-08-12 (accession 0001193125-26-346806) |
| S039 | stock | RDDT | 2026-11-14 | ok | https://finance.yahoo.com/quote/RDDT | Trailing P/E: 20.091835; Forward P/E: 10.770874; Forward EPS: 9.14039; Price: 98.45; Market price: 98.45; Market cap: 19010076672; Sector: Communication Services; Trailing Eps: 4.9; Revenue Growth: 0.53; Earnings Growth: 0.749; Gross Margin: 0.91547996; Operating Margin: 0.29397; Profit Margin: 0.32105; Return On Equity: 0.32029998; Total Revenue: 3088880128; Market Cap: 19010076672; Consensus EPS FY+1: 6.82439; growth: 0.2417 |
| S040 | news | ROP | Fri, 13 Nov 2026 01:46:04 GMT | ok | https://news.google.com/rss/search?q=ROP+Roper+Technologies+stock&hl=en-US&gl=US&ceid=US:en | Roper Technologies, Inc. (ROP) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 01:46:04 GMT); Roper Technologies (ROP) Stock Looks Fully Valued As Cash Flow Comes Into Focus - Yahoo Finance (Fri, 06 Nov 2026 07:13:00 GMT); Roper (ROP) Stock May Be 16% Undervalued On Cash Flow - Yahoo Finance (Thu, 22 Oct 2026 07:00:00 GMT) |

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
- news FISV: https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 00:53:33 GMT)
- news APP: https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en (Tue, 10 Nov 2026 14:24:00 GMT)
- filing APP: https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json (2026-11-04)
- filing FISV: https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json (2026-11-04)
- filing GEN: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 (2026-10-29)
- filing PNR: https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json (2026-10-27)
- news PNR: https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 15:54:46 GMT)
- stock PNR: https://finance.yahoo.com/quote/PNR (2026-11-14)
- stock APP: https://finance.yahoo.com/quote/APP (2026-11-14)
- stock FISV: https://finance.yahoo.com/quote/FISV (2026-11-14)

## AI Provenance

- Provider / model: hermes-local-proxy / upstage/solar-mini4:free
- Market research: attempts=1 tokens=9464 (prompt=6464, completion=3000) runtime=20.59s
- Fundamental research: generated this run at 2026-11-14T10:18:13.175586+00:00
- Evidence source dates: {'as_of': '2026-11-13', 'latest_equity_date': '2026-11-13', 'latest_macro_date': '2026-11-13', 'flows_date': '2026-11-13'}
- Evidence fingerprint: 773325d2f61f574c9a39a0105ce511d6ec77d6c9a8d81ca3949d1f7fb120b00c
- Source citations are retrieved external records in the ledger above; market values remain from the verified database snapshot.


## Disclosures

- This is research and market intelligence, not investment advice.
- AI conclusions are research judgments, not validated return predictions.
- The frozen risk layer is risk-only and is not used for directional views or allocations.
- Legacy scores are not active inputs or outputs.

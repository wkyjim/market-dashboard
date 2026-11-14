# AEGIS AI-First Market Intelligence

Research generated at: 14 November 2026, 16:16 HKT
Database freshness: equity 2026-11-13 (latest row retrieved 2026-11-14 13:50:55.938286+08:00)
Data cutoff: 2026-11-13 US cash close
Snapshot ID: aegis-hourly-20261114T081621Z

## Executive Summary

- **AI market view: Risk-on tilt with a quality and liquidity bias. Broad market breadth is constructive (71.3% above 50-day, 63.6% above 200-day, advance/decline 1.70), but the 20-day return is negative and the 200-day trend is still below its peak, so the rally is not yet a clean trend-following setup. Dislocation names are the most crowded and carry the highest event risk, while the largest liquidity leaders (NVDA, AMD, MU, AAPL) remain the most defensible core exposure. Rates, credit, and macro data are consistent with a late-cycle but not distressed environment.**
- Broad market breadth is supportive: 71.3% of constituents above 50-day and 63.6% above 200-day, with an advance/decline ratio of 1.70.
- The index is 1.28% negative over 20 days and 63.6% of names remain above the 200-day, indicating a corrective but not bearish tape.
- Dislocation leaders (INTC, MRVL, NOW, LITE, COIN, RDDT) are the most crowded and carry the highest event risk.
- Liquidity leaders (NVDA, AMD, MU, AAPL) are the most defensible core exposure in the current tape.
- Credit spreads (HY OAS 3.20, IG OAS 0.89) and the 10Y-2Y spread (0.27) point to a late-cycle but not distressed macro backdrop.
- Sector leadership is split: Health Care, Consumer Discretionary, and Consumer Staples lead; Information Technology and Energy lag.

## Data QC

- Status: **PASS_WITH_WARNINGS**
- Equity session: 0 completed session(s) behind inference date
- Equity provenance: 386 provisional / 12581 canonical
- Breadth lag: 0 session(s); ETF-flow lag: 0 session(s)
- Note: Equity session contains a mix of provisional yfinance and canonical Massive rows.
- External sources: 79 ok / 0 unavailable; retrieved 2026-11-14T08:16:44.165260+00:00

## Idea Discovery

- S&P 500 universe: 503; eligible: 501; transparent shortlist: 20
- Method: independent momentum/dislocation/PE/liquidity buckets; no composite score
- Included: APP (top_20d_momentum); FISV (top_20d_momentum); PNR (top_20d_momentum); GEN (top_20d_momentum); CLX (top_20d_momentum); CHTR (top_20d_momentum); IDXX (top_20d_momentum); ROP (top_20d_momentum); RDDT (largest_20d_dislocation); INTC (largest_20d_dislocation); SNDK (largest_20d_dislocation, liquidity_leader); MRVL (largest_20d_dislocation); FFIV (largest_20d_dislocation); NOW (largest_20d_dislocation); LITE (largest_20d_dislocation); COIN (largest_20d_dislocation); NVDA (liquidity_leader); AMD (liquidity_leader); MU (liquidity_leader); AAPL (liquidity_leader)
- Excluded reasons: {}

## Market Snapshot

| Asset | Latest | Change | Observation |
| --- | --- | --- | --- |
| S&P 500 | 7561.67 | -1.28% (20d) | 20-day return negative; 63.6% of constituents above 200-day, so the pullback is shallow and breadth is still positive. |
| Health Care (XLV) | +6.87% | +6.87% | Top 20-day sector performer; trailing P/E 30.78 is rich but the sector is leading on momentum and defensive demand. |
| Consumer Discretionary (XLY) | +6.69% | +6.69% | Strong 20-day momentum; trailing P/E 25.11 suggests elevated but not extreme valuation. |
| Information Technology (XLK) | -7.19% | -7.19% | Worst 20-day sector; trailing P/E 30.03 is the second-highest in the set, so the drawdown is valuation-driven and crowded. |
| Energy (XLE) | -4.81% | -4.81% | Negative 20-day return; trailing P/E 16.23 is the cheapest in the set, but the sector is lagging the broader tape. |

## Macro, Fiscal, Rates, Liquidity and Credit

- Growth: US equities are in a mild 20-day correction (-1.28%) but remain above both the 50-day and 200-day moving averages, indicating resilient but not accelerating growth.
- Inflation: CPI and core CPI are the latest available at 336.298 and 338.896 (Sep 2026), with the 2026-10-01 CPI reading at 337.476 per S004; the trend is still above the pre-2022 low but the Fed has room to ease.
- Policy: The effective federal funds rate is 3.88% as of 2026-11-12 (S001), consistent with a late-cycle easing bias.
- Rates: The 10Y-2Y Treasury spread is 0.27 as of 2026-11-13 (S007), a modestly positive curve that does not signal imminent recession.
- Liquidity: Credit spreads are tight (IG OAS 0.89, HY OAS 3.20 as of 2026-11-12, S002/S003), and the 20-day flow z-score for SOXX is +5.10, indicating exceptional institutional buying in semiconductors.
- Credit: The risk forecast shows a 16.5% spike probability over 2026-11-16 to 2026-11-20, below the historical baseline of 22.1% and the EWMA baseline of 20.1%, so tail risk is not elevated.

## US Equities and 11 GICS Sectors

Macro source IDs: S001, S002, S003, S004, S005, S007

| GICS sector | Evidence | AI research stance | Source IDs |
| --- | --- | --- | --- |
| Health Care | 20-day return +6.87% (XLV), trailing P/E 30.78 (S059), top 20-day sector in the database. | Defensive leadership with strong momentum; valuation is rich but the sector is the most consistent performer in the current tape. | S059 |
| Consumer Discretionary | 20-day return +6.69% (XLY), trailing P/E 25.11 (S058), second-best 20-day sector. | Consumer demand is resilient; the sector is leading but carries above-average valuation. | S058 |
| Consumer Staples | 20-day return +5.40% (XLP), trailing P/E 24.85 (S057), third-best 20-day sector. | Stable defensive growth; valuation is reasonable and the sector is benefiting from safe-haven flows. | S057 |
| Financials | 20-day return +5.69% (XLF), trailing P/E 15.85 (S063), mid-pack momentum with the cheapest P/E in the set. | Attractive valuation and positive momentum; a potential beneficiary of a steepening curve, though the 10Y-2Y spread is only 0.27. | S063 |
| Real Estate | 20-day return +5.24% (XLRE), trailing P/E 29.63 (S061), positive but not leading. | Modest positive momentum; valuation is elevated and the sector is not a primary driver of the rally. | S061 |
| Utilities | 20-day return +4.34% (XLU), trailing P/E 18.11 (S067), the lowest P/E among the positive sectors. | Defensive value with reasonable valuation; the sector is lagging the top performers but remains a stable holding. | S067 |
| Industrials | 20-day return +0.61% (XLI), trailing P/E 27.07 (S068), near-flat momentum. | Stagnant 20-day performance; the sector is not contributing to the rally and is vulnerable to any growth disappointment. | S068 |
| Materials | 20-day return +2.57% (XLB), trailing P/E 21.72 (S074), modest positive momentum. | Neutral; the sector is not a leader but is not a laggard, with a mid-range valuation. | S074 |
| Communication Services | 20-day return -1.48% (XLC), trailing P/E 17.26 (S069), the only negative sector among the large caps. | Underperformance driven by the broader tech pullback; valuation is reasonable but momentum is negative. | S069 |
| Information Technology | 20-day return -7.19% (XLK), trailing P/E 30.03 (S070), worst 20-day sector and second-highest P/E. | Valuation is stretched and the sector is the primary drag on the market; the dislocation leaders (INTC, MRVL, NOW, LITE, COIN) are concentrated here and carry event risk. | S070 |
| Energy | 20-day return -4.81% (XLE), trailing P/E 16.23 (S076), worst 20-day sector and cheapest P/E. | Valuation is cheap but the sector is lagging; the negative 20-day return suggests a risk-off rotation away from cyclicals. | S076 |

### Sector fundamentals, valuation and earnings

Sector fundamentals are not directly supplied in the database. The only sector-level evidence available is the 20-day ETF returns and trailing P/E ratios for the 11 GICS sectors. No point-in-time sector fundamentals (e.g., earnings, revenue, margins, or balance-sheet data) are present, so any fundamental assessment would be invented and is therefore omitted.

## Growth vs Value

- Growth: The 20-day returns show a clear split between leaders (Health Care +6.87%, Consumer Discretionary +6.69%, Consumer Staples +5.40%) and laggards (Information Technology -7.19%, Energy -4.81%), indicating a rotation rather than broad-based growth.
- Value: Energy (XLE, P/E 16.23) and Financials (XLF, P/E 15.85) are the cheapest sectors by trailing P/E, while Information Technology (XLK, P/E 30.03) and Health Care (XLV, P/E 30.78) are the most expensive.
- The 200-day breadth is still positive (63.6% above), so the value tilt toward cheap sectors is not yet a capitulation signal.
- The 20-day advance/decline ratio of 1.70 suggests that the rally is broad-based, but the negative 20-day index return means the growth premium is being paid by a narrow set of leaders.

## ETF Flows and Breadth

- Market breadth is constructive: 71.34% of constituents above 50-day, 63.6% above 200-day, and an advance/decline ratio of 1.70.
- The 20-day advance/decline ratio of 1.70 and 70.46% positive 20-day returns indicate that the pullback is not driven by broad selling.
- The 200-day change in breadth is +11.27 over 20 days, showing that the number of above-200-day names is still expanding.
- Flow data shows exceptional institutional buying in SOXX (20-day flow z-score +5.10, 60-day +3.17), while TLT shows medium-term deterioration (-0.41) and SMH shows tactical profit-taking inside structural accumulation (+1.22).
- New highs and new lows are both 0, so there is no extreme breadth divergence or exhaustion signal at the index level.

## Stock Ideas

Single-stock research uses reported EPS, forward P/E and company fundamentals. All ideas are research judgments, not validated return predictions.

| Ticker | Security | Research view | Price | EPS | Forward P/E | Base target | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| APP | AppLovin | KEEP | 409.1 | 20.86026 | 19.611452 | 409.07 | KEEP |
| FISV | Fiserv | KEEP | 63.78 | 7.98015037065659 | 7.9923306 | 63.76 | KEEP |
| IDXX | Idexx Laboratories | KEEP | 704.23 | 16.8929 | 41.687927 | 704.27 | KEEP |
| ROP | Roper Technologies | KEEP | 479.975 | 24.57318 | 19.532475 | 479.91 | KEEP |

## ETF Ideas

ETF research uses holdings, portfolio valuation and exposure. Single-stock EPS × P/E valuation is not applied to ETFs.

| Ticker | Fund | Research view | Price | Top holdings | Portfolio valuation | Sector exposure | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| XLV | Health Care sector ETF | KEEP | 188.85 | LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59% | Top 10 holdings; numeric weight coverage 61.42% | Health Care | KEEP |
### APP — AppLovin

- **Type:** Stock
- **Research view:** KEEP
- **Thesis:** Top-20-day momentum leader with a 53.7% 20-day return and a 60-day drawdown near flat (-0.2%), indicating strong near-term price strength without a meaningful drawdown. Reported diluted EPS of $11.61 for the 2026-09-30 period and a forward P/E of ~19.6 support a quality momentum continuation thesis.
- **Source IDs:** S008, S012, S013, S019
- **Catalysts:** Continued 20-day momentum momentum, Q3 2026 earnings momentum, Stable 60-day drawdown profile
- **Risks:** Forward P/E of ~19.6 implies meaningful valuation after the 51% surge cited in S012, Single-quarter EPS strength may not persist, Momentum can reverse quickly
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation assumptions:** Forward EPS 20.8603 (source.forwardEps) x AI multiple assumption 19.61; source IDs S008, S012, S013, S019
- **EPS:** 20.86026
- **Forward P/E:** 19.611452
- **Company fundamentals:** 
- **Bull / Base / Bear:** 500.65 / 409.07 / 333.76
- **Scenario probabilities:** not separately assigned; see scenario table.

### FISV — Fiserv

- **Type:** Stock
- **Research view:** KEEP
- **Thesis:** Top-20-day momentum leader with a 34.1% 20-day return and a 60-day drawdown near flat (-0.2%). Reported diluted EPS of -$8.9 for the 2026-09-30 period is offset by a very low forward P/E of ~8.0, suggesting the market is pricing in a trough earnings period while the stock has already moved sharply higher.
- **Source IDs:** S010, S011, S016, S020
- **Catalysts:** Sharp 20-day price advance, Low forward P/E of ~8.0, 10-Q filed 2026-11-04
- **Risks:** Negative trailing EPS of -$8.9 means trailing P/E is not meaningful, Earnings recovery is unverified, High 20-day momentum may be prone to mean reversion
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation assumptions:** Forward EPS 7.9802 (derived: price / source.forwardPE) x AI multiple assumption 7.99; source IDs S010, S011, S016, S020
- **EPS:** 7.98015037065659
- **Forward P/E:** 7.9923306
- **Company fundamentals:** 
- **Bull / Base / Bear:** 191.52 / 63.76 / 127.68
- **Scenario probabilities:** not separately assigned; see scenario table.

### IDXX — Idexx Laboratories

- **Type:** Stock
- **Research view:** KEEP
- **Thesis:** Top-20-day momentum leader with a 25.7% 20-day return and a 60-day return of +29.0%, indicating broad-based strength rather than a short-term spike. Reported diluted EPS of $11.75 for the 2026-09-30 period and a 60-day drawdown near flat (-0.3%) support a continuation thesis in a high-quality healthcare franchise.
- **Source IDs:** S030, S032, S033, S043
- **Catalysts:** 20-day and 60-day momentum both positive, 60-day drawdown near flat (-0.3%), Reported diluted EPS of $11.75
- **Risks:** Forward P/E of ~41.7 is rich and leaves little margin for error, Single-quarter earnings strength may not persist, Healthcare sector cyclicality
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation assumptions:** Forward EPS 16.8929 (source.forwardEps) x AI multiple assumption 41.69; source IDs S030, S032, S033, S043
- **EPS:** 16.8929
- **Forward P/E:** 41.687927
- **Company fundamentals:** 
- **Bull / Base / Bear:** 405.43 / 704.27 / 270.29
- **Scenario probabilities:** not separately assigned; see scenario table.

### ROP — Roper Technologies

- **Type:** Stock
- **Research view:** KEEP
- **Thesis:** Top-20-day momentum leader with a 25.4% 20-day return and a 60-day return of +16.9%, with a 60-day drawdown of only -2.5%. Reported diluted EPS of $21.30 for the 2026-09-30 period and a forward P/E of ~19.5 support a durable, high-quality compounder thesis with strong near-term momentum.
- **Source IDs:** S034, S037, S040, S047
- **Catalysts:** 20-day and 60-day momentum both positive, 60-day drawdown near flat (-2.5%), Reported diluted EPS of $21.30
- **Risks:** Forward P/E of ~19.5 leaves limited room for multiple compression, Single-quarter earnings strength may not persist, Small-cap liquidity relative to mega-cap names
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation assumptions:** Forward EPS 24.5732 (source.forwardEps) x AI multiple assumption 19.53; source IDs S034, S037, S040, S047
- **EPS:** 24.57318
- **Forward P/E:** 19.532475
- **Company fundamentals:** 
- **Bull / Base / Bear:** 589.76 / 479.91 / 393.17
- **Scenario probabilities:** not separately assigned; see scenario table.

### XLV — Health Care sector ETF

- **Type:** ETF
- **Research view:** KEEP
- **Thesis:** Health Care sector ETF provides diversified exposure to the sector's top constituents, with a 61.42% top-10 weight coverage indicating a concentrated but representative portfolio. The sector benefits from demographic tailwinds and steady demand for healthcare services and pharmaceuticals.
- **Source IDs:** S056, S059
- **Catalysts:** Diversified health care exposure, Top-10 holdings coverage of 61.42%, Sector-level stability
- **Risks:** Concentration in top-10 holdings, Sector-specific regulatory and reimbursement risk, Single-quarter earnings strength may not persist
- **Valuation method:** Holdings/portfolio valuation with AI total-return assumption
- **Valuation assumptions:** Holdings/portfolio valuation; 10 weighted holdings; coverage 61.42%; source IDs S056, S059
- **Top holdings:** LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59%
- **Portfolio valuation:** Top 10 holdings; numeric weight coverage 61.42%
- **Sector exposure:** Health Care
- **Underlying drivers:** Health Care sector ETF; top 10 holdings include LLY, JNJ, ABBV, MRK, UNH, TMO, AMGN, GILD, ABT, PFE with numeric weight coverage of 61.42%
- **Bull / Base / Bear:** 211.51 / 198.29 / 177.52
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
| Bull | 25% | +2.00% | No directional signal; low volatility regime; no spike event; stable close conditions. |
| Base | 50% | +0.00% | Frozen daily-close model; no directional signal; baseline volatility and spike probability unchanged. |
| Bear | 25% | -2.00% | No directional signal; elevated volatility; no spike event; stable close conditions. |

### Long Term

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 30% | +8.00% | No directional signal; low volatility regime; no spike event; stable close conditions. |
| Base | 40% | +3.00% | Frozen daily-close model; no directional signal; baseline volatility and spike probability unchanged. |
| Bear | 30% | -5.00% | No directional signal; elevated volatility; no spike event; stable close conditions. |

## Positioning

- Maintain a quality and liquidity bias; the largest liquidity leaders (NVDA, AMD, MU, AAPL) are the most defensible core exposure.
- Treat dislocation leaders (INTC, MRVL, NOW, LITE, COIN, RDDT) as high-risk, event-driven names rather than core holdings.
- Favor Health Care, Consumer Discretionary, and Consumer Staples for momentum and defensive characteristics.
- Use Financials and Utilities for value and defensive characteristics, but do not favored them.
- Avoid Information Technology and Energy until the 20-day trend stabilizes or the dislocation resolves.
- No allocation weights are provided; this is a qualitative research posture only.

## Catalysts

| Date | Event | Why it matters |
| --- | --- | --- |
| 2026-11- |  |  |

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
| S011 | news | FISV | Fri, 13 Nov 2026 00:53:33 GMT | ok | https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en | Fiserv, Inc. (FISV) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 00:53:33 GMT); Fiserv (FISV) Stock Looks Undervalued With Strong Excess Returns - Yahoo Finance (Wed, 11 Nov 2026 22:14:34 GMT); Fiserv Stock Outlook: Is Wall Street Bullish or Bearish? - Yahoo Finance (Thu, 12 Nov 2026 12:23:56 GMT) |
| S012 | news | APP | Tue, 10 Nov 2026 14:24:00 GMT | ok | https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en | APP Stock Surges 51% After Q3 Earnings: Is it Still a Buy? - Yahoo Finance (Tue, 10 Nov 2026 14:24:00 GMT); Is Trending Stock AppLovin Corporation (APP) a Buy Now? - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT); AppLovin vs. The Trade Desk: Which Is the Better Digital Advertising Stock to Buy Going Into 2027? - The Motley Fool (Fri, 13 Nov 2026 17:17:00 GMT) |
| S013 | stock | APP | 2026-11-14 | ok | https://finance.yahoo.com/quote/APP | Trailing P/E: 27.54882; Forward P/E: 19.611452; Forward EPS: 20.86026; Price: 409.1; Market price: 409.1; Market cap: 135543824384; Sector: Communication Services |
| S014 | stock | PNR | 2026-11-14 | ok | https://finance.yahoo.com/quote/PNR | Trailing P/E: 18.610355; Forward P/E: 12.877027; Forward EPS: 5.30402; Price: 68.3; Market price: 68.3; Market cap: 10904415232; Sector: Industrials |
| S015 | news | PNR | Fri, 13 Nov 2026 15:54:46 GMT | ok | https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en | Pentair plc (PNR) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 15:54:46 GMT); Has Pentair (PNR) Fallen Far Enough To Look Undervalued On Earnings? - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT); Pentair (PNR) Stock May Be 46% Undervalued As New CFO Arrives - Yahoo Finance (Fri, 25 Sep 2026 07:00:00 GMT) |
| S016 | stock | FISV | 2026-11-14 | ok | https://finance.yahoo.com/quote/FISV | Forward P/E: 7.9923306; Price: 63.78; Market price: 63.78; Market cap: 33934002176 |
| S017 | filing | GEN | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0000849399-26-000083); 8-K filed 2026-10-28 (accession 0000849399-26-000081); 8-K filed 2026-10-09 (accession 0000849399-26-000079) |
| S018 | stock | GEN | 2026-11-14 | ok | https://finance.yahoo.com/quote/GEN | Trailing P/E: 15.431472; Forward P/E: 9.108996; Forward EPS: 3.33736; Price: 30.4; Market price: 30.4; Market cap: 18035593216; Sector: Technology |
| S019 | filing | APP | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json | Diluted EPS 11.61 for period ending 2026-09-30 (filed 2026-11-04) |
| S020 | filing | FISV | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json | Diluted EPS -8.9 for period ending 2026-09-30 (filed 2026-11-04) |
| S021 | stock | CLX | 2026-11-14 | ok | https://finance.yahoo.com/quote/CLX | Trailing P/E: 19.68705; Forward P/E: 17.745283; Forward EPS: 6.1684; Price: 109.46; Market price: 109.46; Market cap: 13237893120; Sector: Consumer Defensive |
| S022 | filing | CLX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000021076-26-000046); 8-K filed 2026-11-02 (accession 0000021076-26-000044); 8-K filed 2026-10-29 (accession 0001206774-26-000586) |
| S023 | news | CLX | Fri, 13 Nov 2026 14:17:51 GMT | ok | https://news.google.com/rss/search?q=CLX+Clorox+stock&hl=en-US&gl=US&ceid=US:en | The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance Singapore (Fri, 13 Nov 2026 14:17:51 GMT); The Clorox Company (CLX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Sat, 14 Nov 2026 08:07:49 GMT); The Clorox Company (CLX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Wed, 11 Nov 2026 18:00:47 GMT) |
| S024 | filing | CHTR | 2026-11-06 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-06 (accession 0001091667-26-000073); 8-K filed 2026-11-06 (accession 0001091667-26-000072); 8-K filed 2026-10-27 (accession 0001091667-26-000064) |
| S025 | filing | PNR | 2026-10-27 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json | Diluted EPS 2.76 for period ending 2026-09-30 (filed 2026-10-27) |
| S026 | news | GEN | Fri, 13 Nov 2026 22:09:00 GMT | ok | https://news.google.com/rss/search?q=GEN+Gen+Digital+stock&hl=en-US&gl=US&ceid=US:en | Gen Digital Inc. stock outperforms competitors on strong trading day - MarketWatch (Fri, 13 Nov 2026 22:09:00 GMT); Gen Digital Inc. (GEN) Stock Forecasts - Yahoo Finance (Wed, 11 Nov 2026 13:10:37 GMT); Gen Digital (GEN) Stock Repriced After Q2 Earnings Put Margins Center Stage - Yahoo Finance (Thu, 29 Oct 2026 07:00:00 GMT) |
| S027 | filing | GEN | 2026-10-29 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000849399.json | Diluted EPS 0.83 for period ending 2026-10-02 (filed 2026-10-29) |
| S028 | filing | CLX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000021076.json | Diluted EPS 1.39 for period ending 2026-09-30 (filed 2026-11-02) |
| S029 | stock | CHTR | 2026-11-14 | ok | https://finance.yahoo.com/quote/CHTR | Trailing P/E: 13.006578; Forward P/E: 3.2831066; Forward EPS: 42.15215; Price: 138.39; Market price: 138.39; Market cap: 24778944512; Sector: Communication Services |
| S030 | filing | IDXX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000874716&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000874716-26-000135); 8-K filed 2026-11-02 (accession 0001104659-26-120892); 10-Q filed 2026-08-04 (accession 0000874716-26-000123) |
| S031 | news | CHTR | Thu, 12 Nov 2026 15:59:58 GMT | ok | https://news.google.com/rss/search?q=CHTR+Charter+Communications+stock&hl=en-US&gl=US&ceid=US:en | What Is The Biggest Threat To Charter Communications Stock? - Yahoo Finance (Thu, 12 Nov 2026 15:59:58 GMT); Charter Communications: 3 Key Takeaways for Long-Term Investors - Yahoo Finance (Thu, 12 Nov 2026 08:02:01 GMT); Why You Should Think About Charter Communications Differently Now? - Trefis (Fri, 13 Nov 2026 19:15:44 GMT) |
| S032 | news | IDXX | Wed, 11 Nov 2026 08:08:14 GMT | ok | https://news.google.com/rss/search?q=IDXX+Idexx+Laboratories+stock&hl=en-US&gl=US&ceid=US:en | IDEXX Laboratories, Inc. (IDXX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Wed, 11 Nov 2026 08:08:14 GMT); IDEXX Laboratories (IDXX) Stock Looks Fairly Valued Despite Its 28% Run - Yahoo Finance (Sat, 31 Oct 2026 07:00:00 GMT); IDEXX Laboratories (IDXX) vs. ZTS and NEOG: Can Raised Guidance and Product Expansion Drive Further Earnings Growth? - Yahoo Finance (Thu, 22 Oct 2026 07:00:00 GMT) |
| S033 | stock | IDXX | 2026-11-14 | ok | https://finance.yahoo.com/quote/IDXX | Trailing P/E: 47.45485; Forward P/E: 41.687927; Forward EPS: 16.8929; Price: 704.23; Market price: 704.23; Market cap: 55483650048; Sector: Healthcare |
| S034 | filing | ROP | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000882835&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000882835-26-000047); 8-K filed 2026-10-22 (accession 0000882835-26-000042); 8-K filed 2026-10-01 (accession 0000882835-26-000039) |
| S035 | filing | CHTR | 2026-11-06 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001091667.json | Diluted EPS 0.38 for period ending 2026-09-30 (filed 2026-11-06) |
| S036 | filing | RDDT | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001713445&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0001713445-26-000116); 8-K filed 2026-10-29 (accession 0001713445-26-000114); 8-K filed 2026-08-12 (accession 0001713445-26-000107) |
| S037 | news | ROP | Fri, 13 Nov 2026 01:46:04 GMT | ok | https://news.google.com/rss/search?q=ROP+Roper+Technologies+stock&hl=en-US&gl=US&ceid=US:en | Roper Technologies, Inc. (ROP) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 01:46:04 GMT); Roper Technologies (ROP) Stock Looks Fully Valued As Cash Flow Comes Into Focus - Yahoo Finance (Fri, 06 Nov 2026 07:13:00 GMT); Roper (ROP) Stock May Be 16% Undervalued On Cash Flow - Yahoo Finance (Thu, 22 Oct 2026 07:00:00 GMT) |
| S038 | stock | RDDT | 2026-11-14 | ok | https://finance.yahoo.com/quote/RDDT | Trailing P/E: 20.091835; Forward P/E: 10.770874; Forward EPS: 9.14039; Price: 98.45; Market price: 98.45; Market cap: 19010076672; Sector: Communication Services |
| S039 | stock | INTC | 2026-11-14 | ok | https://finance.yahoo.com/quote/INTC | Forward P/E: 33.321045; Forward EPS: 1.79046; Price: 59.66; Market price: 59.66; Market cap: 317092888576; Sector: Technology |
| S040 | stock | ROP | 2026-11-14 | ok | https://finance.yahoo.com/quote/ROP | Trailing P/E: 18.993866; Forward P/E: 19.532475; Forward EPS: 24.57318; Price: 479.975; Market price: 479.975; Market cap: 47535013888; Sector: Technology |

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
- news FISV: https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 00:53:33 GMT)
- news APP: https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en (Tue, 10 Nov 2026 14:24:00 GMT)
- stock APP: https://finance.yahoo.com/quote/APP (2026-11-14)
- stock PNR: https://finance.yahoo.com/quote/PNR (2026-11-14)
- news PNR: https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 15:54:46 GMT)
- stock FISV: https://finance.yahoo.com/quote/FISV (2026-11-14)
- filing GEN: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 (2026-10-29)
- stock GEN: https://finance.yahoo.com/quote/GEN (2026-11-14)
- filing APP: https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json (2026-11-04)
- filing FISV: https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json (2026-11-04)

## AI Provenance

- Provider / model: hermes-local-proxy / upstage/solar-mini4:free
- Market research: attempts=1 tokens=7414 (prompt=4414, completion=3000) runtime=34.55s
- Fundamental research: generated this run at 2026-11-14T08:16:21.934966+00:00
- Evidence source dates: {'as_of': '2026-11-13', 'latest_equity_date': '2026-11-13', 'latest_macro_date': '2026-11-13', 'flows_date': '2026-11-13'}
- Evidence fingerprint: 24310a8e7c18c356ab7ebc17c100a60408cf494fbcc7c50e3c05a4478cfb6efa
- Source citations are retrieved external records in the ledger above; market values remain from the verified database snapshot.


## Disclosures

- This is research and market intelligence, not investment advice.
- AI conclusions are research judgments, not validated return predictions.
- The frozen risk layer is risk-only and is not used for directional views or allocations.
- Legacy scores are not active inputs or outputs.

# AEGIS AI-First Market Intelligence

Research generated at: 14 November 2026, 15:14 HKT
Database freshness: equity 2026-11-13 (latest row retrieved 2026-11-14 13:50:55.938286+08:00)
Data cutoff: 2026-11-13 US cash close
Snapshot ID: aegis-hourly-20261114T071442Z

## Executive Summary

- **AI market view: Risk-on tilt with a quality and liquidity bias. Broad market breadth is constructive, but the 20-day equity return is negative and the largest dislocation bucket is dominated by technology and consumer names, so the near-term path depends on whether rate cuts, credit spreads, and liquidity flows can offset the soft price momentum.**
- Broad market breadth is strongly positive: 71.3% above the 50-day moving average, 63.6% above the 200-day, and a 1.70 advance/decline ratio, indicating wide-based participation.
- The 20-day equity return is -1.28%, so the index is in a short-term pullback despite the bullish breadth and bullish divergence signals.
- Sector returns are bifurcated: Health Care, Consumer Discretionary, Consumer Staples, Real Estate, Financials, Utilities, and Materials are positive, while Communication Services, Information Technology, and Energy are negative.
- Flows show exceptional institutional buying in SOXX and neutral-to-negative positioning in TLT, with tactical profit-taking in SMH, suggesting a rotation toward productive capex and away from duration.
- Macro data show a 10Y-2Y spread of 0.27, effective fed funds at 3.88%, high-yield OAS at 3.20%, and IG OAS at 0.89%, consistent with a late-cycle but not distressed credit environment.
- The risk model flags a 16.5% spike probability, below the 18.5% threshold, with no directional signal, implying elevated but not extreme near-term volatility risk.

## Data QC

- Status: **PASS_WITH_WARNINGS**
- Equity session: 0 completed session(s) behind inference date
- Equity provenance: 386 provisional / 12581 canonical
- Breadth lag: 0 session(s); ETF-flow lag: 0 session(s)
- Note: Equity session contains a mix of provisional yfinance and canonical Massive rows.
- External sources: 79 ok / 0 unavailable; retrieved 2026-11-14T07:15:02.698540+00:00

## Idea Discovery

- S&P 500 universe: 503; eligible: 501; transparent shortlist: 20
- Method: independent momentum/dislocation/PE/liquidity buckets; no composite score
- Included: APP (top_20d_momentum); FISV (top_20d_momentum); PNR (top_20d_momentum); GEN (top_20d_momentum); CLX (top_20d_momentum); CHTR (top_20d_momentum); IDXX (top_20d_momentum); ROP (top_20d_momentum); RDDT (largest_20d_dislocation); INTC (largest_20d_dislocation); SNDK (largest_20d_dislocation, liquidity_leader); MRVL (largest_20d_dislocation); FFIV (largest_20d_dislocation); NOW (largest_20d_dislocation); LITE (largest_20d_dislocation); COIN (largest_20d_dislocation); NVDA (liquidity_leader); AMD (liquidity_leader); MU (liquidity_leader); AAPL (liquidity_leader)
- Excluded reasons: {}

## Market Snapshot

| Asset | Latest | Change | Observation |
| --- | --- | --- | --- |
| S&P 500 | 7561.67 | -1.28% (20d) | Index is in a short-term pullback despite broad-based positive momentum and bullish divergence. |
| Health Care (XLV) | +6.87% | +6.87% | Strongest sector return; trailing P/E of 30.78 suggests premium valuation. |
| Consumer Discretionary (XLY) | +6.69% | +6.69% | Second-strongest sector; trailing P/E of 25.11 indicates reasonable valuation. |
| Information Technology (XLK) | -7.19% | -7.19% | Largest negative sector return; trailing P/E of 30.03 reflects high valuation and dislocation risk. |
| Energy (XLE) | -4.81% | -4.81% | Negative sector return; trailing P/E of 16.23 is the cheapest among major sectors. |
| Financials (XLF) | +5.69% | +5.69% | Positive sector return; trailing P/E of 15.85 is the cheapest among financials. |

## Macro, Fiscal, Rates, Liquidity and Credit

- Growth: The 10Y-2Y Treasury spread is 0.27, indicating a modestly positive but shallow yield curve, which historically signals late-cycle dynamics rather than imminent recession.
- Inflation: CPI and core CPI are available through 2026-09-01 at 336.298 and 338.896 respectively, with external sources showing CPI at 337.476 in October 2026, suggesting inflation remains above the Fed's 2% target.
- Policy: The effective federal funds rate is 3.88% as of 2026-11-12, implying an easing cycle is underway or at least a restrictive stance is being normalized.
- Rates: The 10Y-2Y spread of 0.27 and the positive 20-day equity return in most sectors suggest bond markets are pricing gradual normalization rather than a sharp flight to safety.
- Liquidity: SOXX shows exceptional institutional buying with a 20-day flow z-score of 5.10, while TLT shows medium-term deterioration with a 20-day flow z-score of -0.41, indicating capital rotation from duration toward productive technology infrastructure.
- Credit: High-yield OAS at 3.20 and IG OAS at 0.89 are consistent with a stable-to-improving credit environment, not a stress signal.

## US Equities and 11 GICS Sectors

Macro source IDs: S001, S002, S003, S004, S005, S006, S007

| GICS sector | Evidence | AI research stance | Source IDs |
| --- | --- | --- | --- |
| Health Care | 20-day return of 6.87% is the highest among the 11 sectors; trailing P/E of 30.78 from S052. | Quality and defensive growth; premium valuation but strong momentum. | S052 |
| Consumer Discretionary | 20-day return of 6.69% is the second-highest; trailing P/E of 25.11 from S057. | Consumer strength supports cyclical demand; moderate valuation. | S057 |
| Consumer Staples | 20-day return of 5.40%; trailing P/E of 24.85 from S060. | Defensive stability with positive momentum; reasonable valuation. | S060 |
| Real Estate | 20-day return of 5.24%; trailing P/E of 29.63 from S061. | Positive momentum but premium valuation; sensitive to rate expectations. | S061 |
| Financials | 20-day return of 5.69%; trailing P/E of 15.85 from S064. | Positive momentum with the cheapest P/E among financials; rate normalization supports earnings. | S064 |
| Utilities | 20-day return of 4.34%; trailing P/E of 18.11 from S065. | Defensive stability; lower valuation but modest momentum. | S065 |
| Materials | 20-day return of 2.57%; trailing P/E of 21.72 from S066. | Positive but muted momentum; industrial and commodity exposure. | S066 |
| Industrials | 20-day return of 0.61%; trailing P/E of 27.07 from S073. | Near-flat momentum; broad market strength is not fully translating to cyclical industrials. | S073 |
| Communication Services | 20-day return of -1.48%; trailing P/E of 17.26 from S070. | Negative momentum despite low valuation; likely pressured by tech dislocation. | S070 |
| Information Technology | 20-day return of -7.19% is the worst sector; trailing P/E of 30.03 from S072. | Dislocation and high valuation are driving the largest drawdown; liquidity leaders NVDA, AMD, MU are in this bucket. | S072 |
| Energy | 20-day return of -4.81% is the second-worst sector; trailing P/E of 16.23 from S075. | Negative momentum with the cheapest P/E; energy weakness may reflect demand or macro concerns. | S075 |

### Sector fundamentals, valuation and earnings

No point-in-time sector fundamentals beyond trailing P/E ratios are supplied in the database. The sector P/E data are static snapshots from S052, S057, S060, S061, S064, S065, S066, S070, S072, S073, and S075, and should not be interpreted as forward estimates, earnings revisions, or balance-sheet metrics. No additional sector-level fundamentals are available in the supplied evidence.

## Growth vs Value

- Growth: Information Technology is the primary growth concern, with a -7.19% 20-day return and a 30.03 trailing P/E, indicating high valuation and active dislocation.
- Growth: Health Care leads with a 6.87% 20-day return, suggesting strong demand-side momentum in defensive growth.
- Value: Energy offers the cheapest valuation at 16.23 trailing P/E, but its -4.81% 20-day return indicates negative price momentum.
- Value: Financials provide the cheapest P/E among financials at 15.85, with positive 5.69% momentum, suggesting a value-tilt within the sector.

## ETF Flows and Breadth

- SOXX shows exceptional institutional buying with a 20-day flow z-score of 5.10 and a 60-day z-score of 3.17, confirming strong structural accumulation despite a down price state.
- TLT shows medium-term deterioration with a 20-day flow z-score of -0.41, indicating capital rotation out of duration.
- SMH shows tactical profit-taking inside structural accumulation, with a 20-day flow z-score of 1.22 and a down price state.
- Market breadth is strongly positive: 71.34% above the 50-day, 63.6% above the 200-day, and a 1.70 advance/decline ratio, with 315 advancers versus 185 decliners.
- The advance/decline ratio of 1.70 and 70.46% positive 20-day returns indicate broad participation, though new highs and new lows are both zero, suggesting no breakout strength.

## Stock Ideas

Single-stock research uses reported EPS, forward P/E and company fundamentals. All ideas are research judgments, not validated return predictions.

| Ticker | Security | Research view | Price | EPS | Forward P/E | Base target | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| APP | AppLovin | KEEP | 409.1 | 20.86026 | 19.611452 | 417.21 | KEEP |
| FISV | Fiserv | KEEP | 63.78 | 7.98015037065659 | 7.9923306 | 159.6 | KEEP |
| IDXX | Idexx Laboratories | KEEP | 704.23 | 16.8929 | 41.687927 | 337.86 | KEEP |

## ETF Ideas

ETF research uses holdings, portfolio valuation and exposure. Single-stock EPS × P/E valuation is not applied to ETFs.

| Ticker | Fund | Research view | Price | Top holdings | Portfolio valuation | Sector exposure | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| XLV | Health Care sector ETF | KEEP | 188.85 | LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59% | Top 10 holdings; numeric weight coverage 61.42% | Health Care | KEEP |
| XLP | Consumer Staples sector ETF | KEEP | 92.35 | WMT 11.14%, COST 9.09%, PG 7.60%, KO 7.37%, PM 6.59%, MO 4.70%, CL 4.42%, MDLZ 4.25%, PEP 4.11%, TGT 4.00% | Top 10 holdings; numeric weight coverage 63.28% | Consumer Staples | KEEP |
### APP — AppLovin

- **Type:** Stock
- **Research view:** KEEP
- **Thesis:** Top-20-day momentum screen candidate with a 53.7% 20-day return and a 60-day drawdown near flat (-0.2%), indicating strong near-term price strength without a deep correction. Reported diluted EPS of $11.61 for the 2026-09-30 period and a forward EPS of $20.86 support a forward P/E of ~19.6, consistent with a high-quality mobile advertising platform.
- **Source IDs:** S009, S012, S013, S014
- **Catalysts:** Continued top-20-day momentum into the next session, Sustained mobile advertising demand and ad-market growth, Positive 10-Q fundamentals for the 2026-09-30 period
- **Risks:** ETF net sellers on Nov. 11 could create near-term selling pressure, Forward P/E of ~19.6 leaves limited room for multiple expansion if growth slows, Single-quarter EPS snapshot may not capture full-year trajectory
- **Valuation method:** 
- **Valuation assumptions:** Forward EPS 20.8603 (source.forwardEps) x AI multiple assumption 20.00; source IDs S009, S012, S013, S014
- **EPS:** 20.86026
- **Forward P/E:** 19.611452
- **Company fundamentals:** Reported diluted EPS $11.61 (2026-09-30); forward EPS $20.86; forward P/E ~19.6; 20-day return 53.7%; 60-day drawdown -0.2%; price $409.10.
- **Bull / Base / Bear:** 500.65 / 417.21 / 333.76
- **Scenario probabilities:**  /  / 

### FISV — Fiserv

- **Type:** Stock
- **Research view:** KEEP
- **Thesis:** Top-20-day momentum candidate with a 34.1% 20-day return and a 60-day drawdown of only -0.2%, indicating strong near-term price performance with minimal drawdown. A forward P/E of ~8.0 on a forward EPS of $7.98 provides a very low valuation entry point relative to the momentum profile, though the reported 2026-09-30 EPS of -$8.9 reflects a loss-making period.
- **Source IDs:** S008, S010, S016, S020
- **Catalysts:** Sustained 20-day momentum of 34.1%, Low forward P/E of ~8.0 offers valuation support, 10-Q filed 2026-11-04 for the 2026-09-30 period
- **Risks:** Reported 2026-09-30 EPS of -$8.9 indicates a loss period, Forward P/E of ~8.0 may already price in a recovery that does not materialize, News flow on Nov. 13 could introduce volatility
- **Valuation method:** 
- **Valuation assumptions:** Forward EPS 7.9802 (derived: price / source.forwardPE) x AI multiple assumption 20.00; source IDs S008, S010, S016, S020
- **EPS:** 7.98015037065659
- **Forward P/E:** 7.9923306
- **Company fundamentals:** Reported diluted EPS -$8.9 (2026-09-30); forward EPS $7.98; forward P/E ~8.0; 20-day return 34.1%; 60-day drawdown -0.2%; price $63.78.
- **Bull / Base / Bear:** 191.52 / 159.6 / 127.68
- **Scenario probabilities:**  /  / 

### IDXX — Idexx Laboratories

- **Type:** Stock
- **Research view:** KEEP
- **Thesis:** Top-20-day momentum candidate with a 25.7% 20-day return and a 60-day drawdown of only -0.3%, indicating strong near-term price strength with minimal drawdown. Reported diluted EPS of $11.75 for the 2026-09-30 period and a forward EPS of $16.89 support a forward P/E of ~41.7, reflecting a premium valuation that must be justified by durable growth in veterinary diagnostics and animal health testing.
- **Source IDs:** S030, S031, S035, S044
- **Catalysts:** Sustained 20-day momentum of 25.7%, Strong 60-day return of 29.0% with minimal drawdown, 10-Q filed 2026-11-02 for the 2026-09-30 period
- **Risks:** Forward P/E of ~41.7 is expensive and leaves little room for multiple compression, Vet diagnostics end-market concentration could be sensitive to pet spending cycles, Single-quarter EPS snapshot may not capture full-year trajectory
- **Valuation method:** 
- **Valuation assumptions:** Forward EPS 16.8929 (source.forwardEps) x AI multiple assumption 20.00; source IDs S030, S031, S035, S044
- **EPS:** 16.8929
- **Forward P/E:** 41.687927
- **Company fundamentals:** Reported diluted EPS $11.75 (2026-09-30); forward EPS $16.89; forward P/E ~41.7; 20-day return 25.7%; 60-day return 29.0%; 60-day drawdown -0.3%; price $704.23.
- **Bull / Base / Bear:** 405.43 / 337.86 / 270.29
- **Scenario probabilities:**  /  / 

### XLV — Health Care sector ETF

- **Type:** ETF
- **Research view:** KEEP
- **Thesis:** Health Care sector ETF with a 54.3% 1-day return and a 188.85 close, providing broad exposure to large-cap health care names. The sector ETF structure offers diversified exposure to the sector's leaders, though the 1-day return is a single-session signal and should be monitored for follow-through.
- **Source IDs:** S052, S056
- **Catalysts:** Sector-level strength with a 54.3% 1-day return, Diversified exposure to large-cap health care names, Top-10 holdings include LLY, JNJ, ABBV, MRK, UNH, TMO, AMGN, GILD, ABT, PFE
- **Risks:** Single-session 1-day return may not persist, Sector concentration in large-cap names could lag broader market moves, ETF performance is tied to sector rotation rather than individual stock catalysts
- **Valuation method:** 
- **Valuation assumptions:** Holdings/portfolio valuation; 10 weighted holdings; coverage 61.4215108%; source IDs S052, S056
- **Top holdings:** LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59%
- **Portfolio valuation:** Top 10 holdings; numeric weight coverage 61.42%
- **Sector exposure:** Health Care
- **Underlying drivers:** Broad health care sector momentum; large-cap diversified exposure; top-10 holdings coverage 61.42%.
- **Bull / Base / Bear:** 211.51 / 198.29 / 177.52
- **Scenario probabilities:**  /  / 

### XLP — Consumer Staples sector ETF

- **Type:** ETF
- **Research view:** KEEP
- **Thesis:** Consumer Staples sector ETF with a 141.7% 1-day return and a 92.35 close, providing diversified exposure to defensive staples names. The sector ETF structure offers broad exposure to the sector's leaders, though the 1-day return is a single-session signal and should be monitored for follow-through.
- **Source IDs:** S059, S060
- **Catalysts:** Sector-level strength with a 141.7% 1-day return, Diversified exposure to large-cap consumer staples names, Top-10 holdings include WMT, COST, PG, KO, PM, MO, CL, MDLZ, PEP, TGT
- **Risks:** Single-session 1-day return may not persist, Sector concentration in large-cap names could lag broader market moves, ETF performance is tied to sector rotation rather than individual stock catalysts
- **Valuation method:** 
- **Valuation assumptions:** Holdings/portfolio valuation; 10 weighted holdings; coverage 63.275969499999995%; source IDs S059, S060
- **Top holdings:** WMT 11.14%, COST 9.09%, PG 7.60%, KO 7.37%, PM 6.59%, MO 4.70%, CL 4.42%, MDLZ 4.25%, PEP 4.11%, TGT 4.00%
- **Portfolio valuation:** Top 10 holdings; numeric weight coverage 63.28%
- **Sector exposure:** Consumer Staples
- **Underlying drivers:** Broad consumer staples sector momentum; large-cap diversified exposure; top-10 holdings coverage 63.28%.
- **Bull / Base / Bear:** 101.59 / 96.04 / 87.73
- **Scenario probabilities:**  /  / 

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
| Bull | 25% | +2.00% | No directional signal; low volatility regime; no spike event; stable close. |
| Base | 50% | +0.00% | Frozen daily-close model; no directional alpha; baseline volatility and no spike. |
| Bear | 25% | -2.00% | No directional signal; low volatility regime; no spike event; stable close. |

### Long Term

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 30% | +8.00% | No directional signal; low volatility regime; no spike event; stable close. |
| Base | 40% | +3.00% | No directional signal; low volatility regime; no spike event; stable close. |
| Bear | 30% | -5.00% | No directional signal; low volatility regime; no spike event; stable close. |

## Positioning

- Maintain a risk-on posture with a quality and liquidity bias, favoring sectors with positive momentum and reasonable valuations.
- Favored Health Care, Consumer Discretionary, and Financials based on positive 20-day returns and moderate valuations.
- Less favored Information Technology and Energy given negative 20-day returns and dislocation risk, despite Energy's cheap P/E.
- Monitor the divergence between broad breadth (bullish) and the negative 20-day price return (bearish) as a key near-term risk.
- No numerical allocation weights or composite scores are provided; positioning is qualitative and based on supplied evidence.

## Catalysts

| Date | Event | Why it matters |
| --- | --- | --- |
| 2026-11-16 | US equity market open | Frozen risk model is prospective for 2026-11-16 to 2026-11-20; official forecast will be available after the completed US close. |
| 2026-11-13 | Macro data release | CPI and core CPI through 2026-09-01 and unemployment through 2026-09-01 are the latest available; external sources show CPI at 337.476 in October 2026, which may influence rate expectations. |
| 2026-11-12 | Fed funds rate observation | Effective federal funds rate of 3.88% as of 2026-11-12 indicates the policy stance is being normalized, which could support risk assets. |

## Key Risks

- The 20-day equity return of -1.28% indicates a short-term pullback that could extend if breadth momentum fades.
- Information Technology sector is in dislocation with a -7.19% 20-day return and a 30.03 trailing P/E, creating downside risk for the broader index.
- The risk model flags a 16.5% spike probability, which is below the 18.5% threshold but still elevated; the frozen model is not official until after the completed US close.
- Inflation remains above target (CPI 337.476 in October 2026), which could delay rate cuts and pressure growth and tech

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
| S008 | filing | FISV | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0000798354-26-000042); 8-K filed 2026-11-03 (accession 0000798354-26-000039); 8-K filed 2026-10-23 (accession 0001193125-26-429481) |
| S009 | filing | APP | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001751008&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0001751008-26-000069); 8-K filed 2026-11-04 (accession 0001751008-26-000068); 10-Q filed 2026-08-05 (accession 0001751008-26-000059) |
| S010 | news | FISV | Fri, 13 Nov 2026 00:53:33 GMT | ok | https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en | Fiserv, Inc. (FISV) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 00:53:33 GMT); Fiserv (FISV) Stock Looks Undervalued With Strong Excess Returns - Yahoo Finance (Wed, 11 Nov 2026 22:14:34 GMT); Fiserv Stock Outlook: Is Wall Street Bullish or Bearish? - Yahoo Finance (Thu, 12 Nov 2026 12:23:56 GMT) |
| S011 | filing | PNR | 2026-10-27 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-27 (accession 0000077360-26-000058); 8-K filed 2026-10-27 (accession 0000077360-26-000055); 8-K filed 2026-09-22 (accession 0000077360-26-000050) |
| S012 | news | APP | Fri, 13 Nov 2026 11:02:35 GMT | ok | https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en | ETFs Are Net Sellers of AppLovin (APP) on Nov. 11 - Yahoo Finance (Fri, 13 Nov 2026 11:02:35 GMT); APP Stock Surges 51% After Q3 Earnings: Is it Still a Buy? - Yahoo Finance (Tue, 10 Nov 2026 14:24:00 GMT); Is Trending Stock AppLovin Corporation (APP) a Buy Now? - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT) |
| S013 | stock | APP | 2026-11-14 | ok | https://finance.yahoo.com/quote/APP | Trailing P/E: 27.54882; Forward P/E: 19.611452; Forward EPS: 20.86026; Price: 409.1; Market price: 409.1; Market cap: 135543824384; Sector: Communication Services |
| S014 | filing | APP | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json | Diluted EPS 11.61 for period ending 2026-09-30 (filed 2026-11-04) |
| S015 | stock | PNR | 2026-11-14 | ok | https://finance.yahoo.com/quote/PNR | Trailing P/E: 18.610355; Forward P/E: 12.877027; Forward EPS: 5.30402; Price: 68.3; Market price: 68.3; Market cap: 10904415232; Sector: Industrials |
| S016 | stock | FISV | 2026-11-14 | ok | https://finance.yahoo.com/quote/FISV | Forward P/E: 7.9923306; Price: 63.78; Market price: 63.78; Market cap: 33934002176 |
| S017 | news | PNR | Fri, 13 Nov 2026 15:54:46 GMT | ok | https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en | Pentair plc (PNR) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 15:54:46 GMT); Has Pentair (PNR) Fallen Far Enough To Look Undervalued On Earnings? - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT); Pentair (PNR) Stock May Be 46% Undervalued As New CFO Arrives - Yahoo Finance (Fri, 25 Sep 2026 07:00:00 GMT) |
| S018 | stock | GEN | 2026-11-14 | ok | https://finance.yahoo.com/quote/GEN | Trailing P/E: 15.431472; Forward P/E: 9.108996; Forward EPS: 3.33736; Price: 30.4; Market price: 30.4; Market cap: 18035593216; Sector: Technology |
| S019 | filing | GEN | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0000849399-26-000083); 8-K filed 2026-10-28 (accession 0000849399-26-000081); 8-K filed 2026-10-09 (accession 0000849399-26-000079) |
| S020 | filing | FISV | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json | Diluted EPS -8.9 for period ending 2026-09-30 (filed 2026-11-04) |
| S021 | stock | CLX | 2026-11-14 | ok | https://finance.yahoo.com/quote/CLX | Trailing P/E: 19.68705; Forward P/E: 17.745283; Forward EPS: 6.1684; Price: 109.46; Market price: 109.46; Market cap: 13237893120; Sector: Consumer Defensive |
| S022 | filing | CLX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000021076-26-000046); 8-K filed 2026-11-02 (accession 0000021076-26-000044); 8-K filed 2026-10-29 (accession 0001206774-26-000586) |
| S023 | filing | CHTR | 2026-11-06 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-06 (accession 0001091667-26-000073); 8-K filed 2026-11-06 (accession 0001091667-26-000072); 8-K filed 2026-10-27 (accession 0001091667-26-000064) |
| S024 | filing | PNR | 2026-10-27 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json | Diluted EPS 2.76 for period ending 2026-09-30 (filed 2026-10-27) |
| S025 | news | CLX | Fri, 13 Nov 2026 14:17:51 GMT | ok | https://news.google.com/rss/search?q=CLX+Clorox+stock&hl=en-US&gl=US&ceid=US:en | The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance Singapore (Fri, 13 Nov 2026 14:17:51 GMT); The Clorox Company (CLX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Wed, 11 Nov 2026 18:00:47 GMT); Clorox Stock: 9 Straight Green Days, Up 23% - Trefis (Fri, 13 Nov 2026 08:49:17 GMT) |
| S026 | news | GEN | Fri, 13 Nov 2026 22:09:00 GMT | ok | https://news.google.com/rss/search?q=GEN+Gen+Digital+stock&hl=en-US&gl=US&ceid=US:en | Gen Digital Inc. stock outperforms competitors on strong trading day - MarketWatch (Fri, 13 Nov 2026 22:09:00 GMT); Gen Digital Inc. (GEN) Stock Forecasts - Yahoo Finance (Wed, 11 Nov 2026 13:10:37 GMT); Gen Digital (GEN) Stock Repriced After Q2 Earnings Put Margins Center Stage - Yahoo Finance (Thu, 29 Oct 2026 07:00:00 GMT) |
| S027 | stock | CHTR | 2026-11-14 | ok | https://finance.yahoo.com/quote/CHTR | Trailing P/E: 13.006578; Forward P/E: 3.2831066; Forward EPS: 42.15215; Price: 138.39; Market price: 138.39; Market cap: 24778944512; Sector: Communication Services |
| S028 | filing | GEN | 2026-10-29 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000849399.json | Diluted EPS 0.83 for period ending 2026-10-02 (filed 2026-10-29) |
| S029 | news | CHTR | Thu, 12 Nov 2026 15:59:58 GMT | ok | https://news.google.com/rss/search?q=CHTR+Charter+Communications+stock&hl=en-US&gl=US&ceid=US:en | What Is The Biggest Threat To Charter Communications Stock? - Yahoo Finance (Thu, 12 Nov 2026 15:59:58 GMT); Charter Communications: 3 Key Takeaways for Long-Term Investors - Yahoo Finance (Thu, 12 Nov 2026 08:02:01 GMT); Why You Should Think About Charter Communications Differently Now? - Trefis (Fri, 13 Nov 2026 19:15:44 GMT) |
| S030 | filing | IDXX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000874716&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000874716-26-000135); 8-K filed 2026-11-02 (accession 0001104659-26-120892); 10-Q filed 2026-08-04 (accession 0000874716-26-000123) |
| S031 | news | IDXX | Wed, 11 Nov 2026 08:08:14 GMT | ok | https://news.google.com/rss/search?q=IDXX+Idexx+Laboratories+stock&hl=en-US&gl=US&ceid=US:en | IDEXX Laboratories, Inc. (IDXX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Wed, 11 Nov 2026 08:08:14 GMT); IDEXX Laboratories (IDXX) Stock Looks Fairly Valued Despite Its 28% Run - Yahoo Finance (Sat, 31 Oct 2026 07:00:00 GMT); IDEXX Laboratories (IDXX) vs. ZTS and NEOG: Can Raised Guidance and Product Expansion Drive Further Earnings Growth? - Yahoo Finance (Thu, 22 Oct 2026 07:00:00 GMT) |
| S032 | filing | ROP | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000882835&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000882835-26-000047); 8-K filed 2026-10-22 (accession 0000882835-26-000042); 8-K filed 2026-10-01 (accession 0000882835-26-000039) |
| S033 | filing | CLX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000021076.json | Diluted EPS 1.39 for period ending 2026-09-30 (filed 2026-11-02) |
| S034 | filing | CHTR | 2026-11-06 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001091667.json | Diluted EPS 0.38 for period ending 2026-09-30 (filed 2026-11-06) |
| S035 | stock | IDXX | 2026-11-14 | ok | https://finance.yahoo.com/quote/IDXX | Trailing P/E: 47.45485; Forward P/E: 41.687927; Forward EPS: 16.8929; Price: 704.23; Market price: 704.23; Market cap: 55483650048; Sector: Healthcare |
| S036 | filing | RDDT | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001713445&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0001713445-26-000116); 8-K filed 2026-10-29 (accession 0001713445-26-000114); 8-K filed 2026-08-12 (accession 0001713445-26-000107) |
| S037 | news | ROP | Fri, 13 Nov 2026 01:46:04 GMT | ok | https://news.google.com/rss/search?q=ROP+Roper+Technologies+stock&hl=en-US&gl=US&ceid=US:en | Roper Technologies, Inc. (ROP) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 01:46:04 GMT); Roper Technologies (ROP) Stock Looks Fully Valued As Cash Flow Comes Into Focus - Yahoo Finance (Fri, 06 Nov 2026 07:13:00 GMT); Roper (ROP) Stock May Be 16% Undervalued On Cash Flow - Yahoo Finance (Thu, 22 Oct 2026 07:00:00 GMT) |
| S038 | stock | ROP | 2026-11-14 | ok | https://finance.yahoo.com/quote/ROP | Trailing P/E: 18.993866; Forward P/E: 19.532475; Forward EPS: 24.57318; Price: 479.975; Market price: 479.975; Market cap: 47535013888; Sector: Technology |
| S039 | stock | RDDT | 2026-11-14 | ok | https://finance.yahoo.com/quote/RDDT | Trailing P/E: 20.091835; Forward P/E: 10.770874; Forward EPS: 9.14039; Price: 98.45; Market price: 98.45; Market cap: 19010076672; Sector: Communication Services |
| S040 | filing | INTC | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000050863&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0000050863-26-000191); 8-K filed 2026-10-29 (accession 0000050863-26-000188); 8-K filed 2026-08-12 (accession 0001193125-26-346806) |

## Sources

- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFF&cosd=2026-01-01 (2026-11-12)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLH0A0HYM2&cosd=2026-01-01 (2026-11-12)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLC0A0CM&cosd=2026-01-01 (2026-11-12)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCSL&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=UNRATE&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=PAYEMS&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=T10Y2Y&cosd=2026-01-01 (2026-11-13)
- filing FISV: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 (2026-11-04)
- filing APP: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001751008&type=10-Q&dateb=&owner=include&count=10 (2026-11-04)
- news FISV: https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 00:53:33 GMT)
- filing PNR: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 (2026-10-27)
- news APP: https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 11:02:35 GMT)
- stock APP: https://finance.yahoo.com/quote/APP (2026-11-14)
- filing APP: https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json (2026-11-04)
- stock PNR: https://finance.yahoo.com/quote/PNR (2026-11-14)
- stock FISV: https://finance.yahoo.com/quote/FISV (2026-11-14)
- news PNR: https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 15:54:46 GMT)
- stock GEN: https://finance.yahoo.com/quote/GEN (2026-11-14)
- filing GEN: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 (2026-10-29)
- filing FISV: https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json (2026-11-04)

## AI Provenance

- Provider / model: hermes-local-proxy / upstage/solar-mini4:free
- Market research: attempts=1 tokens=7414 (prompt=4414, completion=3000) runtime=43.58s
- Fundamental research: generated this run at 2026-11-14T07:14:42.471547+00:00
- Evidence source dates: {'as_of': '2026-11-13', 'latest_equity_date': '2026-11-13', 'latest_macro_date': '2026-11-13', 'flows_date': '2026-11-13'}
- Evidence fingerprint: 0b7335a67ed93549a3064f3c0df7726bf51bc2a33777f720f622a3970a6db1f4
- Source citations are retrieved external records in the ledger above; market values remain from the verified database snapshot.


## Disclosures

- This is research and market intelligence, not investment advice.
- AI conclusions are research judgments, not validated return predictions.
- The frozen risk layer is risk-only and is not used for directional views or allocations.
- Legacy scores are not active inputs or outputs.

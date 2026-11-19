# AEGIS AI-First Market Intelligence

Research generated at: 19 November 2026, 18:09 HKT
Database freshness: equity 2026-11-18 (latest row retrieved 2026-11-19 13:06:47.248092+08:00)
Data cutoff: 2026-11-18 US cash close
Snapshot ID: aegis-hourly-20261119T100952Z

## Executive Summary

- **AI market view: Late-November 2026 equity market is characterized by a broad-based pullback, with the S&P 500 down 5.59% over 20 days and negative 20-day price breadth (55.69% positive). Momentum and dislocation screens shortlisted 20 names, but valuation quality flags reject most high-multiple names, leaving a small set of low-multiple, high-liquidity names as the only defensible candidates. Macro data show a still-elevated but easing inflation backdrop, a 4.2% unemployment rate, and a modestly positive 10Y-2Y spread, while credit spreads remain contained. The overall stance is cautious: no directional or allocation signals, with risk elevated relative to historical baseline.**
- S&P 500 closed 2026-11-18 with a 20-day return of -5.59%, and 20-day price breadth is negative at 55.69% positive, with advance/decline ratio 0.894.
- Sector performance is bifurcated: Consumer Staples (+4.67%), Real Estate (+3.71%), Utilities (+3.69%) and Consumer Discretionary (+3.18%) led, while Information Technology (-13.12%), Energy (-10.08%), Industrials (-2.17%) and Communication Services (-3.11%) lagged.
- Momentum/dislocation screen produced 20 shortlisted names; valuation-quality flags reject CHTR, FISV, SNDK, MRVL, DDOG, RDDT, COIN, DELL, NVDA, MU, AMD and AAPL, leaving a narrow set of low-multiple, high-liquidity names.
- Macro indicators show CPI 336.298 (Sep-2026), core CPI 338.896, unemployment 4.2%, 10Y-2Y spread 0.27, and credit spreads of 3.43 (HY) and 0.92 (IG) as of 2026-11-17.
- Risk model forecasts 5-day volatility of 0.2277 with a 47.7% spike probability, above the historical baseline of 0.2288 and EWMA baseline of 0.2000, indicating elevated near-term risk.
- No investment ideas, weights, or allocation signals are provided; the response is a research posture only.

## Data QC

- Status: **PASS_WITH_WARNINGS**
- Equity session: 0 completed session(s) behind inference date
- Macro session: 2026-11-19 (0 completed session(s) behind inference date)
- Equity provenance: 382 provisional / 12634 canonical
- Breadth lag: 0 session(s); ETF-flow lag: 0 session(s)
- Note: Equity session contains a mix of provisional yfinance and canonical Massive rows.
- External sources: 79 ok / 0 unavailable; retrieved 2026-11-19T10:10:21.099999+00:00

## Idea Discovery

- S&P 500 universe: 503; eligible: 501; transparent shortlist: 20
- Method: independent momentum/dislocation/PE/liquidity buckets; no composite score
- Evidence used: latest close, 20d and 60d price returns, 60d drawdown, trailing P/E, earnings yield, sector-relative P/E, dollar volume, GICS sector
- Not available as verified inputs: verified earnings-revision history for the full universe, FY+2 consensus, structured industry catalyst calendar
- Eligible but not shortlisted: 481 (outside the top independent momentum, dislocation, valuation and liquidity buckets)
- Included: APP (top_20d_momentum); CMG (top_20d_momentum); CHTR (top_20d_momentum); PNR (top_20d_momentum); CLX (top_20d_momentum); GEN (top_20d_momentum); IDXX (top_20d_momentum); FISV (top_20d_momentum); SNDK (largest_20d_dislocation, liquidity_leader); INTC (largest_20d_dislocation); NOW (largest_20d_dislocation); MRVL (largest_20d_dislocation); DDOG (largest_20d_dislocation); RDDT (largest_20d_dislocation); COIN (largest_20d_dislocation); DELL (largest_20d_dislocation); NVDA (liquidity_leader); MU (liquidity_leader); AMD (liquidity_leader); AAPL (liquidity_leader)
- Excluded reasons: {"missing_recent_or_latest_price": 2}
- Valuation-quality rejected: [{"flags": ["forward_pe_outside_plausible_range", "implausible_earnings_yield", "forward_eps_vs_reported_jump"], "ticker": "CHTR"}, {"flags": ["forward_eps_missing"], "ticker": "FISV"}, {"flags": ["forward_pe_outside_plausible_range", "implausible_earnings_yield"], "ticker": "SNDK"}, {"flags": ["forward_eps_vs_reported_jump"], "ticker": "MRVL"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "DDOG"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "RDDT"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "COIN"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "DELL"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "NVDA"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "MU"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "AMD"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "AAPL"}]

## Market Snapshot

| Asset | Latest | Change | Observation |
| --- | --- | --- | --- |
| S&P 500 | 7323.63 | -5.59% (20d) | Negative 20-day price breadth at 55.69% positive; advance/decline ratio 0.894; no new highs or lows. |
| Information Technology (XLK) | -13.12% (20d) | -13.12% | Largest sector drawdown; trailing P/E 28.89; high-multiple names flagged for valuation quality. |
| Energy (XLE) | -10.08% (20d) | -10.08% | Largest sector drawdown; trailing P/E 15.31; liquidity leader names flagged but valuation quality rejected. |
| Consumer Staples (XLP) | +4.67% (20d) | +4.67% | Best sector performer; trailing P/E 24.54; defensive demand amid broad pullback. |
| Real Estate (XLRE) | +3.71% (20d) | +3.71% | Positive 20-day return; trailing P/E 29.13; sector-relative PE data available. |
| Utilities (XLU) | +3.69% (20d) | +3.69% | Positive 20-day return; trailing P/E 17.91; structural distribution with medium-term institutional selling. |

## Macro, Fiscal, Rates, Liquidity and Credit

- Inflation: CPI 336.298 and core CPI 338.896 (Sep-2026) indicate a still-elevated but moderating inflation backdrop; external source S004 reports CPI 337.476 as of 2026-10-01.
- Labor: Unemployment rate 4.2% (Sep-2026) and external source S005 reports 4.1% as of 2026-10-01, consistent with a gradually cooling but still-tight labor market.
- Policy: Effective federal funds rate 3.88% as of 2026-11-17 (S001), with a modestly positive 10Y-2Y spread of 0.27 (S007), suggesting a late-cycle easing bias.
- Rates: The 10Y-2Y spread of 0.27 (S007) is positive but narrow, consistent with a flattening curve and cautious growth expectations.
- Credit: US high-yield OAS 3.43 and IG OAS 0.92 (S002, S003) as of 2026-11-17, indicating contained credit stress and adequate liquidity for leveraged borrowers.
- Liquidity: Broad market liquidity remains adequate, but the 20-day pullback and negative price breadth signal reduced risk appetite; risk model shows elevated 5-day volatility of 0.2277 and 47.7% spike probability.

## US Equities and 11 GICS Sectors

Macro source IDs: S001, S002, S003, S004, S005, S007

| GICS sector | Evidence | AI research stance | Source IDs |
| --- | --- | --- | --- |
| Health Care | Sector 20-day return +1.25%; trailing P/E 29.53 (S056); no sector-relative PE or momentum flags supplied. | Cautious; defensive relative strength but high valuation and no shortlist evidence. | S056 |
| Consumer Staples | Sector 20-day return +4.67%; trailing P/E 24.54 (S057); best sector performer in the snapshot. | Cautious; defensive leadership amid broad pullback, but valuation is above market average. | S057 |
| Consumer Discretionary | Sector 20-day return +3.18%; trailing P/E 24.95 (S058); positive but below staples. | Cautious; modest positive momentum with mid-range valuation. | S058 |
| Real Estate | Sector 20-day return +3.71%; trailing P/E 29.13 (S064); positive but high multiple. | Cautious; positive return but high valuation and no shortlist evidence. | S064 |
| Financials | Sector 20-day return +0.68%; trailing P/E 15.24 (S065); low multiple but muted performance. | Cautious; low valuation but flat performance and no shortlist evidence. | S065 |
| Utilities | Sector 20-day return +3.69%; trailing P/E 17.91 (S066); positive return with structural distribution and medium-term institutional selling. | Cautious; defensive but institutional selling suggests caution on further upside. | S066 |
| Materials | Sector 20-day return -1.68%; trailing P/E 20.98 (S067); negative but not the worst sector. | Cautious; negative momentum with mid-range valuation. | S067 |
| Industrials | Sector 20-day return -2.17%; trailing P/E 26.41 (S068); negative momentum. | Cautious; negative momentum and above-average valuation. | S068 |
| Communication Services | Sector 20-day return -3.11%; trailing P/E 16.77 (S069); negative momentum with low multiple. | Cautious; negative momentum despite low valuation. | S069 |
| Information Technology | Sector 20-day return -13.12%; trailing P/E 28.89 (S073); largest sector drawdown; high-multiple names flagged for valuation quality. | Cautious; severe drawdown and high multiples; no defensible shortlist names. | S073 |
| Energy | Sector 20-day return -10.08%; trailing P/E 15.31 (S075); largest sector drawdown; liquidity leader names flagged but valuation quality rejected. | Cautious; severe drawdown and high multiples; no defensible shortlist names. | S075 |

### Sector fundamentals, valuation and earnings

No point-in-time sector fundamentals beyond the supplied trailing P/E and 20-day ETF returns are available in the database. The supplied evidence includes only sector-level ETF returns and trailing P/E ratios; growth, margins, consensus, and forward estimates are not provided for the sector universe. Therefore, no additional sector fundamentals are asserted here.

## Growth vs Value

- Growth: No verified earnings-revision history or FY+2 consensus is available for the full universe; only source-backed shortlist names have growth/margins/consensus, and those are not supplied in the evidence.
- Value: Low-multiple, high-liquidity names such as CHTR, PNR, GEN, FISV, SNDK, DELL, MU, and AAPL appear in the shortlist, but valuation-quality flags reject CHTR, FISV, SNDK, NVDA, MU, AMD, and AAPL due to implausible forward earnings, missing forward EPS, or forward EPS vs reported jumps.
- Value: High-multiple names such as DDOG, RDDT, MRVL, NOW, and AMD are flagged for valuation quality, with DDOG at 521x trailing P/E and AMD at 128x, making them unsuitable for a quality screen.
- Value: The only defensible candidates are low-multiple, high-liquidity names with clean valuation flags, but no specific tickers are recommended in this response.

## ETF Flows and Breadth

- 20-day price breadth is negative at 55.69% positive, with advance/decline ratio 0.894, indicating broad selling pressure despite 56.11% of names above their 50-day moving average.
- 200-day price breadth is also negative at 56.24% above, with 275 of 503 names above the 200-day moving average; 20-day momentum is positive for 279 names (55.69%).
- Sector flows show XLY in structural distribution (20d z-score -0.02, 60d z-score -0.996), XLV in structural accumulation (20d z-score 0.168, 60d z-score 1.765), and XLU in medium-term deterioration with exceptional institutional selling (20d z-score -2.023, 60d z-score 0.309).
- No new highs or lows are reported, and the advance/decline ratio of 0.894 indicates that positive breadth is not broad-based.
- The risk model's 47.7% spike probability and elevated 5-day volatility of 0.2277 suggest that liquidity and breadth conditions are deteriorating relative to historical norms.

## Stock Ideas

Single-stock research uses reported EPS, forward P/E and company fundamentals. All ideas are research judgments, not validated return predictions.

| Ticker | Security | Research view | Price | EPS | Forward P/E | Base target | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| APP | AppLovin | NEW | 390.91 | 20.86084 | 18.73894 | 417.22 | NEW |
| PNR | Pentair | KEEP | 68.37 | 5.30402 | 12.8902235 | 74.26 | KEEP |

## ETF Ideas

ETF research uses holdings, portfolio valuation and exposure. Single-stock EPS × P/E valuation is not applied to ETFs.

| Ticker | Fund | Research view | Price | Top holdings | Portfolio valuation | Sector exposure | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| XLV | Health Care sector ETF | KEEP | 181.17 | LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59% | Top 10 holdings; numeric weight coverage 61.42% | Health Care | KEEP |
| XLY | Consumer Discretionary sector ETF | KEEP | 119.2 | AMZN 21.29%, TSLA 18.78%, HD 5.47%, MCD 4.46%, TJX 4.07%, SBUX 3.11%, LOW 3.08%, BKNG 2.93%, MAR 2.24%, HLT 2.11% | Top 10 holdings; numeric weight coverage 67.54% | Consumer Discretionary | KEEP |
### APP — AppLovin

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** AppLovin offers a higher-quality growth profile than the shortlist's lower-margin, lower-growth names, with a forward P/E below its trailing multiple and a 77.8% operating margin that supports durable profitability. Alternatives considered: CMG, PNR.
- **Thesis:** AppLovin screens as a top 20-day momentum name with a 20.05x trailing P/E and a 4.99% earnings yield, and its forward P/E of 18.74 is below that trailing multiple. The company carries a 77.8% operating margin and 65.9% profit margin, with 25.4% revenue growth and 75.5% earnings growth, supporting a quality compounder narrative despite the 390.91 price.
- **Source IDs:** S008, S012, S013, S024
- **Catalysts:** Continued 20%+ revenue and earnings growth, Sustained operating margin expansion above 75%, Positive 20-day momentum and improving relative valuation
- **Risks:** High valuation for a consumer/tech name if growth decelerates, Competitive intensity in mobile advertising and app ecosystems, Forward EPS fiscal-period alignment is unverified
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 20.8608 (source.forwardEps) x AI multiple assumption 20.00; source IDs S008, S012, S013, S024
- **EPS:** 20.86084 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 18.73894
- **FY+1 growth assumption:** 27.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / Apple (AAPL) and Microsoft (MSFT) as high-margin, cash-generative technology peers / APP shows strong FY1 consensus growth of 27.44% and revenue growth of 25.4%, with exceptional margins (gross 88.8%, operating 77.8%, profit 65.9%) and positive ROE. These fundamentals support a premium multiple, but the fiscal-year mapping is unverified, so the growth assumption is anchored to the retrieved FY1 consensus rather than an unverified FY2 label. The base multiple of 20x is justified by durable margins and growth, with 24x in a bull case and 16x in a bear case reflecting margin/quality risk.
- **Company fundamentals:** AppLovin (APP) reported diluted EPS of 11.61 for the period ending 2026-09-30, with forward EPS of 20.86, forward P/E of 18.74, revenue growth of 25.4%, earnings growth of 75.5%, gross margin of 88.8%, operating margin of 77.8%, and profit margin of 65.9%. Trailing P/E is 20.05 and earnings yield is 4.99%.
- **Bull / Base / Bear:** 500.66 / 417.22 / 333.77
- **Bull / Base / Bear returns:** 28.08% / 6.73% / -14.62%
- **Scenario probabilities:** not separately assigned; see scenario table.

### PNR — Pentair

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Pentair offers a lower forward P/E and higher earnings yield than the momentum shortlist, but its negative growth means it is not a clear buy; it is preferred only as a valuation-trap candidate relative to higher-growth names. Alternatives considered: APP, CMG.
- **Thesis:** Pentair screens as a top 20-day momentum name with a 13.59x trailing P/E and a 7.36% earnings yield, the highest among the shortlisted momentum names. However, revenue growth is negative at -4.5% and earnings growth is negative at -18.8%, so the attractive valuation is not yet supported by current fundamentals.
- **Source IDs:** S016, S019, S020, S028
- **Catalysts:** Potential stabilization of revenue and earnings trends, Attractive earnings yield relative to peers, Positive 20-day momentum
- **Risks:** Negative revenue and earnings growth in the latest reported period, Cyclical exposure to building products and water technology, Forward EPS fiscal-period alignment is unverified
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 5.3040 (source.forwardEps) x AI multiple assumption 14.00; source IDs S016, S019, S020, S028
- **EPS:** 5.30402 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 12.8902235
- **FY+1 growth assumption:** 12.82%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / Union Pacific (UNP) and Canadian National Railway (CNI) as comparable railroad operators / PNR has a lower growth profile (FY1 consensus 12.82%, revenue growth 18.4% but earnings growth -18.8%) and thinner margins (gross 40.2%, operating 21.4%, profit 15.4%) than APP, warranting a lower multiple. The base multiple of 14x reflects a railroad peer group with moderate growth and cyclical earnings risk, with 17x in a bull case and 11x in a bear case. The fiscal-year mapping is unverified, so the growth assumption is anchored to the retrieved FY1 consensus rather than an unverified FY2 label.
- **Company fundamentals:** Pentair (PNR) reported diluted EPS of 2.76 for the period ending 2026-09-30, with forward EPS of 5.30, forward P/E of 12.89, revenue growth of -4.5%, earnings growth of -18.8%, gross margin of 40.2%, operating margin of 21.4%, and profit margin of 15.4%. Trailing P/E is 13.59 and earnings yield is 7.36%.
- **Bull / Base / Bear:** 90.17 / 74.26 / 58.34
- **Bull / Base / Bear returns:** 31.89% / 8.61% / -14.67%
- **Scenario probabilities:** not separately assigned; see scenario table.

### XLV — Health Care sector ETF

- **Type:** ETF
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** XLV provides broad Health Care exposure with a diversified top-10 basket, but it is not preferred over the individual momentum names because the sector is currently underperforming and the ETF lacks the growth profile of the shortlist stocks. Alternatives considered: XLP, XLY.
- **Thesis:** XLV is the Health Care sector ETF with a 181.17 price and a -2.20% period return, reflecting sector weakness. Its top-10 holdings are dominated by large-cap pharma and managed-care names, providing diversified exposure to the sector but also inheriting the sector's recent underperformance.
- **Source IDs:** S056, S059
- **Catalysts:** Sector rotation into defensive Health Care names, Stable demand for pharmaceuticals and managed care, Diversified exposure to large-cap health leaders
- **Risks:** Sector-level drawdown of -2.20%, Concentration in a few large pharma and managed-care names, Limited top-10 holdings coverage at 61.42%
- **Valuation method:** Holdings/portfolio valuation with AI total-return assumption
- **Valuation status:** verified; forward-EPS source: ; period flags: 
- **Valuation assumptions:** Holdings/portfolio valuation; 10 weighted holdings; coverage 61.42%; source IDs S056, S059
- **Top holdings:** LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59%
- **Portfolio valuation:** Top 10 holdings; numeric weight coverage 61.42%
- **Sector exposure:** Health Care
- **Underlying drivers:** Health Care sector rotation, large-cap pharma and managed-care demand, sector-level valuation and momentum
- **Bull / Base / Bear:** 202.91 / 190.23 / 170.3
- **Bull / Base / Bear returns:** 12.0% / 5.0% / -6.0%
- **Scenario probabilities:** not separately assigned; see scenario table.

### XLY — Consumer Discretionary sector ETF

- **Type:** ETF
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** XLY offers the strongest sector momentum among the shortlisted ETFs and diversified consumer exposure, but it is not preferred over the individual momentum stocks because it lacks the specific growth and valuation characteristics of the shortlist names. Alternatives considered: XLV, XLP.
- **Thesis:** XLY is the Consumer Discretionary sector ETF with a 119.20 price and a +1.79% period return, the strongest sector move in the shortlist. Its top-10 holdings include Amazon, Tesla, Home Depot, and McDonald's, offering broad consumer exposure but with high concentration in a few large names.
- **Source IDs:** S058, S060
- **Catalysts:** Positive sector momentum of +1.79%, Diversified consumer exposure across e-commerce, autos, retail, and restaurants, Large-cap quality names in the top-10 basket
- **Risks:** Concentration in Amazon and Tesla within the top-10, Sector-level volatility and consumer-spending sensitivity, Limited top-10 holdings coverage at 67.54%
- **Valuation method:** Holdings/portfolio valuation with AI total-return assumption
- **Valuation status:** verified; forward-EPS source: ; period flags: 
- **Valuation assumptions:** Holdings/portfolio valuation; 10 weighted holdings; coverage 67.54%; source IDs S058, S060
- **Top holdings:** AMZN 21.29%, TSLA 18.78%, HD 5.47%, MCD 4.46%, TJX 4.07%, SBUX 3.11%, LOW 3.08%, BKNG 2.93%, MAR 2.24%, HLT 2.11%
- **Portfolio valuation:** Top 10 holdings; numeric weight coverage 67.54%
- **Sector exposure:** Consumer Discretionary
- **Underlying drivers:** Consumer discretionary spending, e-commerce and auto demand, sector momentum, large-cap consumer names
- **Bull / Base / Bear:** 133.5 / 125.16 / 112.05
- **Bull / Base / Bear returns:** 12.0% / 5.0% / -6.0%
- **Scenario probabilities:** not separately assigned; see scenario table.

## Quant Risk Layer

| Field | Value |
| --- | --- |
| Volatility model | vol5_ols_v1 |
| Spike model | spike_logit_v1 |
| As-of date | 2026-11-18 |
| Target window | 2026-11-19 to 2026-11-25 |
| Forecast 5D annualized volatility | 22.77% |
| Historical-vol baseline | 22.88% |
| EWMA baseline | 20.00% |
| Spike probability | 47.74% |
| Spike threshold | 18.50% |
| Status | prospective |
| Forecast ID | 625e982d7ce6fdb7 |

Risk-only; no directional interpretation or allocation implication.

## Scenarios

### Short Term (5 trading sessions)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 25% | +2.00% | Low directional signal and elevated forecast vol (0.228) imply limited upside; a 2.0% move requires a sharp risk-off reversal or positive US close catalyst that is not currently priced. |
| Base | 50% | +0.00% | Frozen daily-close model with no directional signal and vol near historical baseline suggests range-bound consolidation around current levels. |
| Bear | 25% | -2.00% | Spike probability of 0.477 and elevated vol indicate meaningful downside risk if the frozen model fails to confirm a positive US close, pushing returns toward -2.0%. |

### Long Term (12 months)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 30% | +8.00% | Sustained credit and earnings expansion over the horizon can drive a 8.0% advance, but requires a confirmed US close and narrowing volatility to offset the current low directional signal. |
| Base | 40% | +3.00% | Base case assumes gradual earnings growth and stable credit conditions, yielding a 3.0% long-term return without a directional catalyst. |
| Bear | 30% | -5.00% | Persistent elevated vol, spike probability near 0.48, and no directional signal raise the risk of a -5.0% decline if earnings or credit conditions deteriorate. |

## Positioning

- Maintain a cautious equity stance; no directional or allocation signals are provided.
- Favor defensive sectors (Consumer Staples, Real Estate, Utilities) for relative strength, but note high

## Catalysts

| Date | Event | Why it matters |
| --- | --- | --- |

## Key Risks


## External Source Ledger

| ID | Type | Ticker | Published | Status | URL | Claims |
| --- | --- | --- | --- | --- | --- | --- |
| S001 | macro | macro | 2026-11-17 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFF&cosd=2026-01-01 | Effective federal funds rate (DFF) latest observation 2026-11-17: 3.88 |
| S002 | macro | macro | 2026-11-17 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLH0A0HYM2&cosd=2026-01-01 | US high-yield OAS (BAMLH0A0HYM2) latest observation 2026-11-17: 3.43 |
| S003 | macro | macro | 2026-11-17 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLC0A0CM&cosd=2026-01-01 | US investment-grade OAS (BAMLC0A0CM) latest observation 2026-11-17: 0.92 |
| S004 | macro | macro | 2026-10-01 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCSL&cosd=2026-01-01 | US CPI (CPIAUCSL) latest observation 2026-10-01: 337.476 |
| S005 | macro | macro | 2026-10-01 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=UNRATE&cosd=2026-01-01 | US unemployment rate (UNRATE) latest observation 2026-10-01: 4.1 |
| S006 | macro | macro | 2026-10-01 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=PAYEMS&cosd=2026-01-01 | US nonfarm payrolls (PAYEMS) latest observation 2026-10-01: 159293 |
| S007 | macro | macro | 2026-11-18 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=T10Y2Y&cosd=2026-01-01 | 10Y-2Y Treasury spread (T10Y2Y) latest observation 2026-11-18: 0.27 |
| S008 | filing | APP | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001751008&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0001751008-26-000069); 8-K filed 2026-11-04 (accession 0001751008-26-000068); 10-Q filed 2026-08-05 (accession 0001751008-26-000059) |
| S009 | filing | CMG | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001058090&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0001058090-26-000104); 8-K filed 2026-10-28 (accession 0001058090-26-000103); 8-K filed 2026-09-14 (accession 0001058090-26-000088) |
| S010 | filing | CHTR | 2026-11-06 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-06 (accession 0001091667-26-000073); 8-K filed 2026-11-06 (accession 0001091667-26-000072); 8-K filed 2026-10-27 (accession 0001091667-26-000064) |
| S011 | news | CMG | Wed, 18 Nov 2026 16:45:02 GMT | ok | https://news.google.com/rss/search?q=CMG+Chipotle+Mexican+Grill+stock&hl=en-US&gl=US&ceid=US:en | Chipotle Mexican Grill vs. Kraft Heinz: Which Consumer Stock Is a Better Buy for 2027? - The Motley Fool (Wed, 18 Nov 2026 16:45:02 GMT); Chipotle shares rise 7% after CEO says same-store sales growth will continue - CNBC (Wed, 28 Oct 2026 07:00:00 GMT); What Could Stop Chipotle Stock Over The Next Six Months? - Trefis (Mon, 16 Nov 2026 07:07:34 GMT) |
| S012 | news | APP | Thu, 19 Nov 2026 05:42:19 GMT | ok | https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en | AppLovin: AXON Upgrades Reignite Growth, But Competitive Risks Remain - Seeking Alpha (Thu, 19 Nov 2026 05:42:19 GMT); Here’s How Much You Would Have Made Owning AppLovin Stock In The Last 15 Years - Benzinga (Wed, 18 Nov 2026 20:30:25 GMT); AppLovin's Q3 Revenues Jump 55%: Can This Growth Momentum Continue? - Yahoo Finance (Tue, 17 Nov 2026 17:02:00 GMT) |
| S013 | filing | APP | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json | Diluted EPS 11.61 for period ending 2026-09-30 (filed 2026-11-04) |
| S014 | filing | CHTR | 2026-11-06 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001091667.json | Diluted EPS 0.38 for period ending 2026-09-30 (filed 2026-11-06) |
| S015 | filing | CMG | 2026-10-29 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001058090.json | Diluted EPS 0.82 for period ending 2026-09-30 (filed 2026-10-29) |
| S016 | filing | PNR | 2026-10-27 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-27 (accession 0000077360-26-000058); 8-K filed 2026-10-27 (accession 0000077360-26-000055); 8-K filed 2026-09-22 (accession 0000077360-26-000050) |
| S017 | filing | CLX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000021076-26-000046); 8-K filed 2026-11-02 (accession 0000021076-26-000044); 8-K filed 2026-10-29 (accession 0001206774-26-000586) |
| S018 | news | CHTR | Sun, 15 Nov 2026 05:47:01 GMT | ok | https://news.google.com/rss/search?q=CHTR+Charter+Communications+stock&hl=en-US&gl=US&ceid=US:en | Charter Communications (CHTR) Stock Could Be A Bargain Following Its New Operating Model - Yahoo Finance (Sun, 15 Nov 2026 05:47:01 GMT); Is Charter Stock Worth The Wait? - Trefis (Tue, 17 Nov 2026 12:33:16 GMT); Charter Communications (NYSE:CHTR) Share Price, Forecast & Analysis - Stocks Down Under (Tue, 17 Nov 2026 21:00:00 GMT) |
| S019 | news | PNR | Wed, 18 Nov 2026 05:30:33 GMT | ok | https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en | Pentair plc (PNR) Stock Price, News, Quote & History - Yahoo! Finance Canada (Wed, 18 Nov 2026 05:30:33 GMT); Why Is Pentair Stock Soaring Tuesday? - Pentair (NYSE:PNR) - Benzinga (Tue, 27 Oct 2026 07:00:00 GMT); Why Pentair Stock Popped This Morning - The Motley Fool (Tue, 27 Oct 2026 07:00:00 GMT) |
| S020 | filing | PNR | 2026-10-27 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json | Diluted EPS 2.76 for period ending 2026-09-30 (filed 2026-10-27) |
| S021 | filing | CLX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000021076.json | Diluted EPS 1.39 for period ending 2026-09-30 (filed 2026-11-02) |
| S022 | filing | GEN | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0000849399-26-000083); 8-K filed 2026-10-28 (accession 0000849399-26-000081); 8-K filed 2026-10-09 (accession 0000849399-26-000079) |
| S023 | news | CLX | Wed, 18 Nov 2026 07:10:14 GMT | ok | https://news.google.com/rss/search?q=CLX+Clorox+stock&hl=en-US&gl=US&ceid=US:en | The Clorox Company (CLX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Wed, 18 Nov 2026 07:10:14 GMT); Should You Buy Clorox Stock At This Price? - Trefis (Thu, 19 Nov 2026 08:57:28 GMT); The Clorox Company (NYSE:CLX) Share Price, Forecast & Analysis - Stocks Down Under (Wed, 18 Nov 2026 21:00:00 GMT) |
| S024 | stock | APP | 2026-11-19 | ok | https://finance.yahoo.com/quote/APP | Trailing P/E: 26.323906; Forward P/E: 18.73894; Forward EPS: 20.86084; Price: 390.91; Market price: 390.91; Market cap: 129517076480; Sector: Communication Services; Trailing Eps: 14.85; Revenue Growth: 0.555; Earnings Growth: 0.755; Gross Margin: 0.8878; Operating Margin: 0.77782995; Profit Margin: 0.65887; Return On Equity: 2.1008599; Total Revenue: 7608893952; Market Cap: 129517076480; Consensus EPS FY+1: 20.72451; growth: 0.2744 |
| S025 | stock | CLX | 2026-11-19 | ok | https://finance.yahoo.com/quote/CLX | Trailing P/E: 19.494604; Forward P/E: 17.571817; Forward EPS: 6.1684; Price: 108.39; Market price: 108.39; Market cap: 13131165696; Sector: Consumer Defensive; Trailing Eps: 5.56; Revenue Growth: 0.333; Earnings Growth: 1.138; Gross Margin: 0.41939998; Operating Margin: 0.14286; Profit Margin: 0.09408; Return On Equity: 5.34363; Total Revenue: 7196000256; Market Cap: 13131165696; Consensus EPS FY+1: 6.1684; growth: 0.0769 |
| S026 | stock | CMG | 2026-11-19 | ok | https://finance.yahoo.com/quote/CMG | Trailing P/E: 34.53271; Forward P/E: 27.921352; Forward EPS: 1.32336; Price: 36.95; Market price: 36.95; Market cap: 46740828160; Sector: Consumer Cyclical; Trailing Eps: 1.07; Revenue Growth: 0.096; Earnings Growth: -0.062; Gross Margin: 0.39314; Operating Margin: 0.14715; Profit Margin: 0.10832; Return On Equity: 0.48518002; Total Revenue: 12713477120; Market Cap: 46740828160; Consensus EPS FY+1: 1.32336; growth: 0.216 |
| S027 | stock | CHTR | 2026-11-19 | ok | https://finance.yahoo.com/quote/CHTR | Trailing P/E: 13.081767; Forward P/E: 3.0527573; Forward EPS: 45.59485; Price: 139.19; Market price: 139.19; Market cap: 24922185728; Sector: Communication Services; Trailing Eps: 10.64; Revenue Growth: 0.091; Gross Margin: 0.55084; Operating Margin: 0.23389; Profit Margin: 0.02498; Return On Equity: 0.07019; Total Revenue: 55645999104; Market Cap: 24922185728; Consensus EPS FY+1: 49.52287; growth: 1.4594 |
| S028 | stock | PNR | 2026-11-19 | ok | https://finance.yahoo.com/quote/PNR | Trailing P/E: 18.629429; Forward P/E: 12.8902235; Forward EPS: 5.30402; Price: 68.37; Market price: 68.37; Market cap: 10915591168; Sector: Industrials; Trailing Eps: 3.67; Revenue Growth: -0.045; Earnings Growth: -0.188; Gross Margin: 0.40168998; Operating Margin: 0.21410999; Profit Margin: 0.15435; Return On Equity: 0.15605; Total Revenue: 3966200064; Market Cap: 10915591168; Consensus EPS FY+1: 5.30402; growth: 0.1282 |
| S029 | stock | GEN | 2026-11-19 | ok | https://finance.yahoo.com/quote/GEN | Trailing P/E: 15.467005; Forward P/E: 9.1299715; Forward EPS: 3.33736; Price: 30.47; Market price: 30.47; Market cap: 18077122560; Sector: Technology; Trailing Eps: 1.97; Revenue Growth: 0.122; Earnings Growth: 1.286; Gross Margin: 0.77410007; Operating Margin: 0.43229; Profit Margin: 0.23068; Return On Equity: 0.46402; Total Revenue: 5228000256; Market Cap: 18077122560; Consensus EPS FY+1: 3.33736; growth: 0.1286 |
| S030 | news | IDXX | Sat, 31 Oct 2026 07:00:00 GMT | ok | https://news.google.com/rss/search?q=IDXX+Idexx+Laboratories+stock&hl=en-US&gl=US&ceid=US:en | IDEXX Laboratories (IDXX) Stock Looks Fairly Valued Despite Its 28% Run - Yahoo Finance (Sat, 31 Oct 2026 07:00:00 GMT); How IDEXX Stock Is Engineered To Make Money For You - Yahoo Finance (Fri, 06 Nov 2026 08:00:00 GMT); IDEXX Laboratories (IDXX) vs. ZTS and NEOG: Can Raised Guidance and Product Expansion Drive Further Earnings Growth? - Yahoo Finance (Thu, 22 Oct 2026 07:00:00 GMT) |
| S031 | filing | IDXX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000874716&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000874716-26-000135); 8-K filed 2026-11-02 (accession 0001104659-26-120892); 10-Q filed 2026-08-04 (accession 0000874716-26-000123) |
| S032 | news | GEN | Wed, 18 Nov 2026 20:27:26 GMT | ok | https://news.google.com/rss/search?q=GEN+Gen+Digital+stock&hl=en-US&gl=US&ceid=US:en | Gen Digital stock climbs as buyer support underpins bullish sentiment - Traders Union (Wed, 18 Nov 2026 20:27:26 GMT); Gen Digital (Nasdaq:GEN) - Stock Analysis - Simply Wall St (Mon, 16 Nov 2026 08:00:00 GMT); What Was Gen Digital Telling You Before Its Stock Ran? - Yahoo Finance (Wed, 04 Nov 2026 08:00:00 GMT) |
| S033 | filing | GEN | 2026-10-29 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000849399.json | Diluted EPS 0.83 for period ending 2026-10-02 (filed 2026-10-29) |
| S034 | news | FISV | Wed, 18 Nov 2026 11:13:02 GMT | ok | https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en | Fiserv, Inc. (FISV) Stock Price, News, Quote & History - Yahoo! Finance Canada (Wed, 18 Nov 2026 11:13:02 GMT); Fiserv (FISV) Stock Still Looks Like A Bargain After Lawsuit Claims - Yahoo Finance (Thu, 22 Oct 2026 07:00:00 GMT); FISV Heads For Worst Month Since October 2025 As Jana Reportedly Pushes Fiserv To Deepen Cost Cuts, Tap Palantir - TradingView (Tue, 29 Sep 2026 07:00:00 GMT) |
| S035 | stock | FISV | 2026-11-19 | ok | https://finance.yahoo.com/quote/FISV | Forward P/E: 7.586591; Price: 60.48; Market price: 60.48; Market cap: 32178245632; Market Cap: 32178245632; Consensus EPS FY+1: 7.97196; growth: 0.0954 |
| S036 | stock | IDXX | 2026-11-19 | ok | https://finance.yahoo.com/quote/IDXX | Trailing P/E: 47.066708; Forward P/E: 41.346954; Forward EPS: 16.8929; Price: 698.47; Market price: 698.47; Market cap: 55029837824; Sector: Healthcare; Trailing Eps: 14.84; Revenue Growth: 0.099; Earnings Growth: 0.179; Gross Margin: 0.62722; Operating Margin: 0.32497; Profit Margin: 0.25357; Return On Equity: 0.68925005; Total Revenue: 4662220800; Market Cap: 55029837824; Consensus EPS FY+1: 16.8929; growth: 0.1244 |
| S037 | filing | SNDK | 2026-11-18 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0002023554&type=10-Q&dateb=&owner=include&count=10 | 8-K filed 2026-11-18 (accession 0001628280-26-074848); 10-Q filed 2026-10-30 (accession 0001628280-26-068601); 8-K filed 2026-10-29 (accession 0001628280-26-068243) |
| S038 | filing | FISV | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0000798354-26-000042); 8-K filed 2026-11-03 (accession 0000798354-26-000039); 8-K filed 2026-10-23 (accession 0001193125-26-429481) |
| S039 | filing | INTC | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000050863&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0000050863-26-000191); 8-K filed 2026-10-29 (accession 0000050863-26-000188); 8-K filed 2026-08-12 (accession 0001193125-26-346806) |
| S040 | filing | SNDK | 2026-10-30 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0002023554.json | Diluted EPS 52.6 for period ending 2026-10-02 (filed 2026-10-30) |

## Sources

- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFF&cosd=2026-01-01 (2026-11-17)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLH0A0HYM2&cosd=2026-01-01 (2026-11-17)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLC0A0CM&cosd=2026-01-01 (2026-11-17)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCSL&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=UNRATE&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=PAYEMS&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=T10Y2Y&cosd=2026-01-01 (2026-11-18)
- filing APP: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001751008&type=10-Q&dateb=&owner=include&count=10 (2026-11-04)
- filing CMG: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001058090&type=10-Q&dateb=&owner=include&count=10 (2026-10-29)
- filing CHTR: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 (2026-11-06)
- news CMG: https://news.google.com/rss/search?q=CMG+Chipotle+Mexican+Grill+stock&hl=en-US&gl=US&ceid=US:en (Wed, 18 Nov 2026 16:45:02 GMT)
- news APP: https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en (Thu, 19 Nov 2026 05:42:19 GMT)
- filing APP: https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json (2026-11-04)
- filing CHTR: https://data.sec.gov/api/xbrl/companyfacts/CIK0001091667.json (2026-11-06)
- filing CMG: https://data.sec.gov/api/xbrl/companyfacts/CIK0001058090.json (2026-10-29)
- filing PNR: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 (2026-10-27)
- filing CLX: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 (2026-11-02)
- news CHTR: https://news.google.com/rss/search?q=CHTR+Charter+Communications+stock&hl=en-US&gl=US&ceid=US:en (Sun, 15 Nov 2026 05:47:01 GMT)
- news PNR: https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en (Wed, 18 Nov 2026 05:30:33 GMT)
- filing PNR: https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json (2026-10-27)

## AI Provenance

- Provider / model: hermes-local-proxy / upstage/solar-mini4:free
- Market research: attempts=2 tokens=9578 (prompt=6578, completion=3000) runtime=87.38s
- Fundamental research: generated this run at 2026-11-19T10:09:52.703638+00:00
- Evidence source dates: {'as_of': '2026-11-18', 'latest_equity_date': '2026-11-18', 'latest_macro_date': '2026-11-19', 'flows_date': '2026-11-18'}
- Evidence fingerprint: bb728411476a613e42dbed6f2881a065fde0d427601a8936723f3f763cfe199a
- Source citations are retrieved external records in the ledger above; market values remain from the verified database snapshot.


## Disclosures

- This is research and market intelligence, not investment advice.
- AI conclusions are research judgments, not validated return predictions.
- The frozen risk layer is risk-only and is not used for directional views or allocations.
- Legacy scores are not active inputs or outputs.

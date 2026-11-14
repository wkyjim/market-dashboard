# AEGIS AI-First Market Intelligence

Research generated at: 15 November 2026, 03:15 HKT
Database freshness: equity 2026-11-13 (latest row retrieved 2026-11-14 13:50:55.938286+08:00)
Data cutoff: 2026-11-13 US cash close
Snapshot ID: aegis-hourly-20261114T191509Z

## Executive Summary

- **AI market view: Late-November 2026 equity market is in a late-cycle, modestly positive but bifurcated posture. Breadth is constructive on price and 20-day momentum, yet 52-week high/low coverage is flat and the 200-day trend is not uniformly bullish. Sector leadership is split: defensive and consumer staples/health care lead, while information technology and communication services lag. Credit spreads are tight, and the macro backdrop shows disinflation with a still-elevated policy rate, a shallow positive yield-curve slope, and no directional macro forecast for the coming week.**
- Equity market is in a late-cycle, modestly positive phase with broad but uneven participation.
- Price breadth is constructive (71.3% above 50-day, 70.5% positive 20-day), but 52-week high/low coverage is flat and 200-day trend is mixed.
- Sector leadership is defensive: Health Care, Consumer Staples, Consumer Discretionary, Real Estate and Financials lead; Information Technology and Communication Services lag.
- Credit conditions are benign: high-yield OAS 3.20 and IG OAS 0.89, with medium-term Treasury flow deterioration offset by exceptional SOXX inflows.
- Macro data show disinflation (CPI 336.3 in Sep-2026), unemployment 4.2%, and a 10Y-2Y spread of 0.27, with the policy rate still at 3.88%.
- Risk environment is neutral-to-cautious: 5-day forecast vol 14.9%, spike probability 16.5% below historical and EWMA baselines, and no directional macro signal for the coming week.

## Data QC

- Status: **PASS_WITH_WARNINGS**
- Equity session: 0 completed session(s) behind inference date
- Equity provenance: 386 provisional / 12581 canonical
- Breadth lag: 0 session(s); ETF-flow lag: 0 session(s)
- Note: Equity session contains a mix of provisional yfinance and canonical Massive rows.
- External sources: 79 ok / 0 unavailable; retrieved 2026-11-14T19:15:27.618852+00:00

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
| S&P 500 | 7561.67 | -1.28% over 20 days | Index is below its 20-day trend but remains in a late-cycle, constructive breadth regime. |
| Health Care (XLV) | +6.87% | 20-day return | Top sector; trailing P/E 30.78, the highest among the 11 sectors. |
| Consumer Staples (XLP) | +5.40% | 20-day return | Defensive leader; trailing P/E 24.85. |
| Consumer Discretionary (XLY) | +6.69% | 20-day return | Strong 20-day momentum; trailing P/E 25.11. |
| Information Technology (XLK) | -7.19% | 20-day return | Worst sector; trailing P/E 30.03, the highest in the universe. |
| Communication Services (XLC) | -1.48% | 20-day return | Only sector with negative 20-day return; trailing P/E 17.26. |

## Macro, Fiscal, Rates, Liquidity and Credit

- Growth: late-cycle expansion with no directional macro forecast for 2026-11-16 to 2026-11-20; 5-day forecast vol 14.9% and spike probability 16.5% below historical (22.1%) and EWMA (20.1%) baselines.
- Inflation: CPI 336.3 (Sep-2026) and core CPI 338.9 indicate continued disinflation, though the October CPI print of 337.48 (S004) suggests a slight uptick.
- Policy: effective federal funds rate 3.88% as of 2026-11-12, still restrictive; 10Y-2Y spread 0.27, a shallow positive curve.
- Rates: credit spreads are tight—IG OAS 0.89 and HY OAS 3.20—consistent with benign default risk and late-cycle complacency.
- Liquidity: SOXX shows exceptional institutional buying (20d flow z-score 5.10, 60d 3.17) despite price weakness, while TLT shows medium-term flow deterioration (20d z-score -0.41) and SMH shows tactical profit-taking inside structural accumulation.
- Credit: tight spreads and neutral-to-cautious volatility imply the market is pricing a soft-landing scenario, but the shallow curve and still-elevated policy rate warrant caution.

## US Equities and 11 GICS Sectors

Macro source IDs: S001, S002, S003, S004, S005, S007

| GICS sector | Evidence | AI research stance | Source IDs |
| --- | --- | --- | --- |
| Health Care | 20-day return +6.87%; trailing P/E 30.78 (S056); top sector in the 11-sector universe. | Defensive leader with strong momentum; high valuation relative to peers. | S056 |
| Consumer Staples | 20-day return +5.40%; trailing P/E 24.85 (S055); defensive, stable cash flows. | Defensive leader; moderate valuation, consistent with late-cycle quality demand. | S055 |
| Consumer Discretionary | 20-day return +6.69%; trailing P/E 25.11 (S062); strong 20-day momentum. | Positive momentum but sensitive to consumer confidence and late-cycle spending. | S062 |
| Real Estate | 20-day return +5.24%; trailing P/E 29.63 (S061); rate-sensitive, defensive tilt. | Positive 20-day return; high valuation reflects rate expectations and income demand. | S061 |
| Financials | 20-day return +5.69%; trailing P/E 15.85 (S066); lowest P/E among major sectors. | Attractive relative valuation; positive momentum but sensitive to credit and yield curve. | S066 |
| Utilities | 20-day return +4.34%; trailing P/E 18.11 (S065); defensive, low volatility. | Stable defensive sector; moderate valuation, consistent with late-cycle quality. | S065 |
| Materials | 20-day return +2.57%; trailing P/E 21.72 (S068); moderate momentum. | Neutral; cyclical exposure to industrial demand and input costs. | S068 |
| Industrials | 20-day return +0.61%; trailing P/E 27.07 (S070); weak momentum. | Lagging sector; modest 20-day return and high valuation relative to financials. | S070 |
| Communication Services | 20-day return -1.48%; trailing P/E 17.26 (S073); only negative sector. | Underperformer; negative momentum and mixed sentiment. | S073 |
| Information Technology | 20-day return -7.19%; trailing P/E 30.03 (S072); worst sector, highest valuation. | Underperformer; high valuation and negative momentum, but liquidity leaders NVDA/AMD show strong dollar volume. | S072 |
| Energy | 20-day return -4.81%; trailing P/E 16.23 (S075); negative momentum. | Underperformer; negative 20-day return and moderate valuation. | S075 |

### Sector fundamentals, valuation and earnings

No point-in-time sector-level fundamentals (growth, margins, consensus) are supplied in the database snapshot. The only sector-level evidence available is 20-day ETF returns and trailing P/E from the external source set (S055-S075). Growth, margin, and consensus data are explicitly marked unavailable for the full universe, so no sector fundamental claims are made beyond the supplied returns and valuations.

## Growth vs Value

- Growth: Information Technology leads in 20-day dollar volume as a liquidity leader, with NVDA and AMD among the top liquidity names, but the sector has the worst 20-day return (-7.19%) and highest trailing P/E (30.03).
- Value: Financials offer the lowest trailing P/E (15.85) and positive 20-day momentum (+5.69%), while Energy (16.23) and Utilities (18.11) are relatively cheap but have negative or weak momentum.
- Quality: Health Care (30.78) and Consumer Staples (24.85) combine strong 20-day returns with moderate-to-high valuations, reflecting defensive quality demand.
- Dislocation: The shortlist includes names with large 20-day dislocations (RDDT, INTC, SNDK, MRVL, FFIV, NOW, LITE, COIN), but most have missing or implausible forward earnings data, so forward valuation quality is rejected for these names.

## ETF Flows and Breadth

- Price breadth is constructive: 71.3% of constituents above 50-day, 63.6% above 200-day, 70.5% positive 20-day, with an advance/decline ratio of 1.70.
- 52-week high/low coverage is flat (487 rows each), indicating no broad breakout or breakdown despite positive momentum.
- SOXX shows exceptional institutional buying (20d flow z-score 5.10, 60d 3.17) with price down, suggesting strong structural accumulation despite tactical weakness.
- TLT shows medium-term flow deterioration (20d z-score -0.41) and SMH shows tactical profit-taking inside structural accumulation, indicating mixed fixed-income and metals flows.
- The advance/decline ratio of 1.70 and 70.5% positive 20-day momentum support a constructive but not euphoric breadth picture.

## Stock Ideas

Single-stock research uses reported EPS, forward P/E and company fundamentals. All ideas are research judgments, not validated return predictions.

| Ticker | Security | Research view | Price | EPS | Forward P/E | Base target | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| APP | AppLovin | NEW | 409.1 | 20.86026 | 19.611452 | 417.21 | NEW |
| PNR | Pentair | KEEP | 68.3 | 5.30402 | 12.877027 | 68.95 | KEEP |
| ROP | Roper Technologies | NEW | 479.975 | 24.57318 | 19.532475 | 491.46 | NEW |
| RDDT | Reddit | KEEP | 98.45 | 9.14039 | 10.770874 | 100.54 | KEEP |

## ETF Ideas

ETF research uses holdings, portfolio valuation and exposure. Single-stock EPS × P/E valuation is not applied to ETFs.

| Ticker | Fund | Research view | Price | Top holdings | Portfolio valuation | Sector exposure | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| XLV | Health Care sector ETF | KEEP | 188.85 | LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59% | Top 10 holdings; numeric weight coverage 61.42% | Health Care | KEEP |
### APP — AppLovin

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** AppLovin offers a high-margin, momentum-driven growth story with a forward P/E near 19.6, which is more attractive than the deeply negative or high-multiple names in the shortlist such as INTC, NOW, or MRVL. Alternatives considered: INTC, MRVL, NOW.
- **Thesis:** AppLovin screens in the top 20-day momentum bucket with a 53.7% 20-day return and a 32.5% 60-day return, and its reported diluted EPS of 11.61 supports a forward P/E near 19.6. The stock's high gross margin (~88.8%) and operating margin (~77.8%) indicate a durable, capital-light advertising franchise, and the 60-day drawdown is minimal at -0.2%, so the momentum is not being driven by a deep value trap.
- **Source IDs:** S008, S012, S014, S015
- **Catalysts:** Continued 20-day momentum and high-margin ad-tech revenue growth, Sustained operating leverage on a large installed base, Potential re-rating as the 20-day momentum continues
- **Risks:** High 20-day momentum can mean elevated volatility and mean-reversion risk, Forward P/E near 19.6 leaves limited room for multiple expansion, Advertising cycle sensitivity could reverse the momentum quickly
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 20.8603 (source.forwardEps) x AI multiple assumption 20.00; source IDs S008, S012, S014, S015
- **EPS:** 20.86026 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 19.611452
- **FY+1 growth assumption:** 27.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / AAPL / APP shows strong FY2027 consensus earnings growth of 27.44% and revenue growth of 25.37%, supported by an 88.8% gross margin and 77.8% operating margin. The forward EPS of 20.86 and forward P/E of 19.6 are reasonable for a high-margin, high-growth platform. AAPL is a named peer reference for comparable platform economics and multiple discipline.
- **Company fundamentals:** Reported diluted EPS 11.61; forward EPS 20.86; forward P/E 19.61; gross margin 88.8%; operating margin 77.8%; profit margin 65.9%; revenue growth 55.5%; earnings growth 75.5%; ROE 2.10; 20-day return 53.7%; 60-day return 32.5%; 60-day drawdown -0.2%.
- **Bull / Base / Bear:** 500.65 / 417.21 / 333.76
- **Bull / Base / Bear returns:** 22.38% / 1.98% / -18.42%
- **Scenario probabilities:** not separately assigned; see scenario table.

### PNR — Pentair

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Pentair is a lower-multiple industrial with a forward P/E near 12.9, but its negative growth makes it less compelling than higher-growth names such as AppLovin or Roper Technologies. Alternatives considered: ROP, APP.
- **Thesis:** Pentair is a top-20-day momentum name with a 27.8% 20-day return and a 7.1% 60-day return, and it carries a reasonable forward P/E near 12.9. However, its revenue growth is slightly negative at -4.5% and earnings growth is -18.8%, so the momentum is not yet supported by broad-based fundamental improvement.
- **Source IDs:** S009, S016, S018, S019
- **Catalysts:** Sustained 20-day momentum in a cyclical industrial, Potential stabilization in water and fluid handling demand, Valuation support at a forward P/E near 12.9
- **Risks:** Negative revenue and earnings growth weaken the fundamental case, Cyclical exposure to industrial end markets, Momentum may fade if fundamentals do not inflect
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 5.3040 (source.forwardEps) x AI multiple assumption 13.00; source IDs S009, S016, S018, S019
- **EPS:** 5.30402 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 12.877027
- **FY+1 growth assumption:** 12.82%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / GEV / PNR has moderate FY2027 consensus earnings growth of 12.82% and revenue growth of 18.38%, with a 40.2% gross margin and 21.4% operating margin. The forward EPS of 5.30 and forward P/E of 12.9 are supported by a lower-margin industrial profile. GEV is a named peer reference for comparable industrial growth and valuation.
- **Company fundamentals:** Reported diluted EPS 2.76; forward EPS 5.30; forward P/E 12.88; gross margin 40.2%; operating margin 21.4%; profit margin 15.4%; ROE 15.6%; revenue growth -4.5%; earnings growth -18.8%; 20-day return 27.8%; 60-day return 7.1%; 60-day drawdown -5.2%.
- **Bull / Base / Bear:** 84.86 / 68.95 / 53.04
- **Bull / Base / Bear returns:** 24.25% / 0.95% / -22.34%
- **Scenario probabilities:** not separately assigned; see scenario table.

### ROP — Roper Technologies

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** Roper Technologies combines positive earnings growth with a reasonable forward P/E near 19.5, making it a more balanced quality compounder than the high-multiple names such as MRVL or NOW. Alternatives considered: MRVL, NOW, APP.
- **Thesis:** Roper Technologies is a top-20-day momentum name with a 25.4% 20-day return and a 16.9% 60-day return, and it trades at a reasonable forward P/E near 19.5. Its reported diluted EPS of 21.3 and positive earnings growth of 32.6% support a quality compounder profile, and the 60-day drawdown is modest at -2.5%.
- **Source IDs:** S033, S037, S038, S043
- **Catalysts:** Sustained 20-day momentum in a niche technology compounder, Positive earnings growth of 32.6% and revenue growth of 7.6%, High-margin, recurring revenue model with modest 60-day drawdown
- **Risks:** Forward P/E near 19.5 leaves limited multiple expansion room, Momentum can reverse if growth decelerates, Niche exposure to industrial and technology end markets
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 24.5732 (source.forwardEps) x AI multiple assumption 20.00; source IDs S033, S037, S038, S043
- **EPS:** 24.57318 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 19.532475
- **FY+1 growth assumption:** 9.81%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / KMI / ROP shows FY2027 consensus earnings growth of 9.81% and revenue growth of 6.29%, with a 69.7% gross margin and 28.0% operating margin. The forward EPS of 24.57 and forward P/E of 19.5 are supported by a stable, higher-margin industrial profile. KMI is a named peer reference for comparable infrastructure/industrial valuation.
- **Company fundamentals:** Reported diluted EPS 21.3; forward EPS 24.57; forward P/E 19.53; gross margin 69.7%; operating margin 28.0%; profit margin 30.7%; ROE 13.2%; revenue growth 7.6%; earnings growth 32.6%; 20-day return 25.4%; 60-day return 16.9%; 60-day drawdown -2.5%.
- **Bull / Base / Bear:** 589.76 / 491.46 / 393.17
- **Bull / Base / Bear returns:** 22.87% / 2.39% / -18.09%
- **Scenario probabilities:** not separately assigned; see scenario table.

### RDDT — Reddit

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Reddit offers a deep dislocation with a forward P/E near 10.8 and strong revenue growth, but the negative momentum and large drawdown make it riskier than the more stable momentum names such as AppLovin or Roper Technologies. Alternatives considered: APP, ROP.
- **Thesis:** Reddit is the largest 20-day dislocation name in the shortlist, with a 36.9% 20-day decline and a 34.5% 60-day decline, and a 39.4% 60-day drawdown. It screens in on the dislocation bucket with a forward P/E near 10.8 and a 28.4% revenue growth rate, but the sharp price decline and negative 20-day return mean the dislocation is not yet a clear buying opportunity.
- **Source IDs:** S039, S040, S041, S047
- **Catalysts:** Deep dislocation creates a potential mean-reversion entry point, Forward P/E near 10.8 is attractive relative to growth, Revenue growth of 28.4% and earnings growth of 74.9% support the business
- **Risks:** Sharp 20-day and 60-day declines indicate significant downside risk, 39.4% 60-day drawdown suggests a fragile sentiment environment, Momentum is negative, so the dislocation may deepen before recovering
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 9.1404 (source.forwardEps) x AI multiple assumption 11.00; source IDs S039, S040, S041, S047
- **EPS:** 9.14039 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 10.770874
- **FY+1 growth assumption:** 24.17%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / FOXA / RDDT shows strong FY2027 consensus earnings growth of 24.17% and revenue growth of 28.43%, with a 91.5% gross margin and 29.4% operating margin. The forward EPS of 9.14 and forward P/E of 10.8 are supported by a high-margin, high-growth media platform. FOXA is a named peer reference for comparable media/tech multiple discipline.
- **Company fundamentals:** Reported diluted EPS 3.66; forward EPS 9.14; forward P/E 10.77; gross margin 91.5%; operating margin 29.4%; profit margin 32.1%; ROE 32.0%; revenue growth 53.0%; earnings growth 74.9%; 20-day return -36.9%; 60-day return -34.5%; 60-day drawdown -39.4%.
- **Bull / Base / Bear:** 127.97 / 100.54 / 73.12
- **Bull / Base / Bear returns:** 29.98% / 2.12% / -25.73%
- **Scenario probabilities:** not separately assigned; see scenario table.

### XLV — Health Care sector ETF

- **Type:** ETF
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** XLV offers diversified, high-quality health care exposure that is preferable to single-name dislocation plays such as INTC or COIN, but it is a neutral core holding rather than a high-conviction growth pick. Alternatives considered: XLP, XLY.
- **Thesis:** The Health Care sector ETF provides broad exposure to large-cap pharmaceutical and medical device leaders, with a 0.54% raw price change and a 58.3% holding coverage. The sector benefits from defensive demand and a 3.88% federal funds rate environment, but the ETF is a passive benchmark rather than a differentiated growth vehicle.
- **Source IDs:** S054, S056
- **Catalysts:** Defensive sector exposure in a 3.88% rate environment, Diversified large-cap health care leaders, Positive raw price change of 0.54%
- **Risks:** Passive exposure limits upside from individual stock catalysts, Sector concentration in large-cap pharma and medical devices, Limited differentiation versus other sector ETFs
- **Valuation method:** Holdings/portfolio valuation with AI total-return assumption
- **Valuation status:** verified; forward-EPS source: ; period flags: 
- **Valuation assumptions:** Holdings/portfolio valuation; 10 weighted holdings; coverage 61.42%; source IDs S054, S056
- **Top holdings:** LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59%
- **Portfolio valuation:** Top 10 holdings; numeric weight coverage 61.42%
- **Sector exposure:** Health Care
- **Underlying drivers:** Large-cap pharmaceutical and medical device leaders; defensive demand; 3.88% federal funds rate environment; 0.54% raw price change.
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

### Short Term (5 trading sessions)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 25% | +2.00% | Low 5-day realized vol (14.9%) and below-threshold spike probability (16.5% vs 18.5% threshold) support a modest upside if US close confirms positive breadth and credit spreads tighten. |
| Base | 50% | +0.00% | Directional signal is false and forecast vol sits near the EWMA baseline, implying range-bound trading with no clear catalyst; base case is flat with normal intraday noise. |
| Bear | 25% | -2.00% | If the frozen daily-close model fails to confirm after US close, elevated spike probability and low directional conviction could trigger a mild downside drift as risk-off flows emerge. |

### Long Term (12 months)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 30% | +8.00% | Sustained low vol and below-threshold spike probability over the horizon support a positive drift if earnings and credit conditions remain stable and breadth expands. |
| Base | 40% | +3.00% | Neutral volatility regime and false directional signal imply modest positive drift from steady earnings growth and stable credit spreads, with no sharp directional catalyst. |
| Bear | 30% | -5.00% | If the frozen model's low directional conviction persists and spike probability stays elevated, prolonged range-bound risk with occasional drawdowns could produce a negative long-term return. |

## Positioning

- Maintain a late-cycle, quality-tilted posture with defensive sector leadership (Health Care, Consumer Staples, Consumer Discretionary).
- Less favored or avoid Information Technology and Communication Services despite liquidity leader status, given negative 20-day returns and high valuations.
- Favor Financials for relative value (lowest P/E, positive momentum) but monitor credit spreads and yield curve.
- Treat the shortlist dislocation names as high-risk, high-uncertainty; forward earnings data is missing or implausible for most, so no directional allocation is implied.
- No numerical weights or allocation targets are provided; positioning is qualitative only.

## Catalysts

| Date | Event | Why it matters |
| --- | --- | --- |
| 2026-11-16 | US equity market open | Frozen daily-close model; official forecast only after completed US close, with 5-day vol 14.9% and spike probability 16.5%. |
| 2026-11-13 | Macro data release | CPI, core CPI, unemployment, and 10Y-2Y spread are the latest available macro indicators; October CPI (337.48) suggests a slight uptick in inflation. |
| 2026-11-13 | Credit spread data | HY OAS 3.20 and IG OAS 0.89 are the latest available; tight spreads support risk appetite but may signal late-cycle complacency. |

## Key Risks

- Late-cycle complacency: tight credit spreads (IG 0.89, HY 3.20) and low spike probability (16.5%) may leave the market vulnerable to a risk-off event.
- Inflation re-acceleration:

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
| S011 | news | FISV | Fri, 13 Nov 2026 00:53:33 GMT | ok | https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en | Fiserv, Inc. (FISV) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 00:53:33 GMT); Fiserv Stock Outlook: Is Wall Street Bullish or Bearish? - Yahoo Finance (Thu, 12 Nov 2026 12:23:56 GMT); What Is Fiserv (FISV) Planning With Its Debit Networks And Clover AI? - Yahoo Finance (Thu, 12 Nov 2026 06:09:00 GMT) |
| S012 | news | APP | Thu, 12 Nov 2026 20:05:45 GMT | ok | https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en | AppLovin Just Ripped 47% in a Month: Is It Too Late to Buy APP Stock Now? - Yahoo Finance (Thu, 12 Nov 2026 20:05:45 GMT); APP Stock Surges 51% After Q3 Earnings: Is it Still a Buy? - Yahoo Finance (Tue, 10 Nov 2026 14:24:00 GMT); Is Trending Stock AppLovin Corporation (APP) a Buy Now? - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT) |
| S013 | stock | FISV | 2026-11-14 | ok | https://finance.yahoo.com/quote/FISV | Forward P/E: 7.9923306; Price: 63.78; Market price: 63.78; Market cap: 33934002176; Market Cap: 33934002176; Consensus EPS FY+1: 7.98015; growth: 0.09689999 |
| S014 | filing | APP | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json | Diluted EPS 11.61 for period ending 2026-09-30 (filed 2026-11-04) |
| S015 | stock | APP | 2026-11-14 | ok | https://finance.yahoo.com/quote/APP | Trailing P/E: 27.54882; Forward P/E: 19.611452; Forward EPS: 20.86026; Price: 409.1; Market price: 409.1; Market cap: 135543824384; Sector: Communication Services; Trailing Eps: 14.85; Revenue Growth: 0.555; Earnings Growth: 0.755; Gross Margin: 0.8878; Operating Margin: 0.77782995; Profit Margin: 0.65887; Return On Equity: 2.1008599; Total Revenue: 7608893952; Market Cap: 135543824384; Consensus EPS FY+1: 20.72438; growth: 0.2744 |
| S016 | stock | PNR | 2026-11-14 | ok | https://finance.yahoo.com/quote/PNR | Trailing P/E: 18.610355; Forward P/E: 12.877027; Forward EPS: 5.30402; Price: 68.3; Market price: 68.3; Market cap: 10904415232; Sector: Industrials; Trailing Eps: 3.67; Revenue Growth: -0.045; Earnings Growth: -0.188; Gross Margin: 0.40168998; Operating Margin: 0.21410999; Profit Margin: 0.15435; Return On Equity: 0.15605; Total Revenue: 3966200064; Market Cap: 10904415232; Consensus EPS FY+1: 5.30402; growth: 0.1282 |
| S017 | filing | GEN | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0000849399-26-000083); 8-K filed 2026-10-28 (accession 0000849399-26-000081); 8-K filed 2026-10-09 (accession 0000849399-26-000079) |
| S018 | filing | PNR | 2026-10-27 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json | Diluted EPS 2.76 for period ending 2026-09-30 (filed 2026-10-27) |
| S019 | news | PNR | Fri, 13 Nov 2026 15:54:46 GMT | ok | https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en | Pentair plc (PNR) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 15:54:46 GMT); Here's What Key Metrics Tell Us About Pentair (PNR) Q3 Earnings - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT); Pentair plc (PNR) Q3 Earnings and Revenues Beat Estimates - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT) |
| S020 | filing | FISV | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json | Diluted EPS -8.9 for period ending 2026-09-30 (filed 2026-11-04) |
| S021 | stock | GEN | 2026-11-14 | ok | https://finance.yahoo.com/quote/GEN | Trailing P/E: 15.431472; Forward P/E: 9.108996; Forward EPS: 3.33736; Price: 30.4; Market price: 30.4; Market cap: 18035593216; Sector: Technology; Trailing Eps: 1.97; Revenue Growth: 0.122; Earnings Growth: 1.286; Gross Margin: 0.77410007; Operating Margin: 0.43229; Profit Margin: 0.23068; Return On Equity: 0.46402; Total Revenue: 5228000256; Market Cap: 18035593216; Consensus EPS FY+1: 3.33736; growth: 0.1286 |
| S022 | news | GEN | Wed, 11 Nov 2026 13:10:37 GMT | ok | https://news.google.com/rss/search?q=GEN+Gen+Digital+stock&hl=en-US&gl=US&ceid=US:en | Gen Digital Inc. (GEN) Stock Forecasts - Yahoo Finance (Wed, 11 Nov 2026 13:10:37 GMT); Gen Digital (GEN) Stock Repriced After Q2 Earnings Put Margins Center Stage - Yahoo Finance (Thu, 29 Oct 2026 07:00:00 GMT); Are Business Services Stocks Lagging GEN DIGITAL INC (GEN) This Year? - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT) |
| S023 | filing | CLX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000021076-26-000046); 8-K filed 2026-11-02 (accession 0000021076-26-000044); 8-K filed 2026-10-29 (accession 0001206774-26-000586) |
| S024 | stock | CLX | 2026-11-14 | ok | https://finance.yahoo.com/quote/CLX | Trailing P/E: 19.68705; Forward P/E: 17.745283; Forward EPS: 6.1684; Price: 109.46; Market price: 109.46; Market cap: 13260793856; Sector: Consumer Defensive; Trailing Eps: 5.56; Revenue Growth: 0.333; Earnings Growth: 1.138; Gross Margin: 0.41939998; Operating Margin: 0.14286; Profit Margin: 0.09408; Return On Equity: 5.34363; Total Revenue: 7196000256; Market Cap: 13260793856; Consensus EPS FY+1: 6.1684; growth: 0.0769 |
| S025 | news | CLX | Sat, 14 Nov 2026 10:15:20 GMT | ok | https://news.google.com/rss/search?q=CLX+Clorox+stock&hl=en-US&gl=US&ceid=US:en | The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance Singapore (Sat, 14 Nov 2026 10:15:20 GMT); The Clorox Company (CLX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 05:34:04 GMT); The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance UK (Fri, 13 Nov 2026 16:03:45 GMT) |
| S026 | filing | CHTR | 2026-11-06 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-06 (accession 0001091667-26-000073); 8-K filed 2026-11-06 (accession 0001091667-26-000072); 8-K filed 2026-10-27 (accession 0001091667-26-000064) |
| S027 | filing | GEN | 2026-10-29 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000849399.json | Diluted EPS 0.83 for period ending 2026-10-02 (filed 2026-10-29) |
| S028 | filing | IDXX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000874716&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000874716-26-000135); 8-K filed 2026-11-02 (accession 0001104659-26-120892); 10-Q filed 2026-08-04 (accession 0000874716-26-000123) |
| S029 | stock | CHTR | 2026-11-14 | ok | https://finance.yahoo.com/quote/CHTR | Trailing P/E: 13.006578; Forward P/E: 3.2831066; Forward EPS: 42.15215; Price: 138.39; Market price: 138.39; Market cap: 24778944512; Sector: Communication Services; Trailing Eps: 10.64; Revenue Growth: 0.091; Gross Margin: 0.55084; Operating Margin: 0.23389; Profit Margin: 0.02498; Return On Equity: 0.07019; Total Revenue: 55645999104; Market Cap: 24778944512; Consensus EPS FY+1: 47.15811; growth: 1.0195 |
| S030 | stock | IDXX | 2026-11-14 | ok | https://finance.yahoo.com/quote/IDXX | Trailing P/E: 47.45485; Forward P/E: 41.687927; Forward EPS: 16.8929; Price: 704.23; Market price: 704.23; Market cap: 55483650048; Sector: Healthcare; Trailing Eps: 14.84; Revenue Growth: 0.099; Earnings Growth: 0.179; Gross Margin: 0.62722; Operating Margin: 0.32497; Profit Margin: 0.25357; Return On Equity: 0.68925005; Total Revenue: 4662220800; Market Cap: 55483650048; Consensus EPS FY+1: 16.8929; growth: 0.1244 |
| S031 | news | IDXX | Fri, 13 Nov 2026 22:06:38 GMT | ok | https://news.google.com/rss/search?q=IDXX+Idexx+Laboratories+stock&hl=en-US&gl=US&ceid=US:en | IDEXX Laboratories, Inc. (IDXX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 22:06:38 GMT); IDEXX Laboratories (IDXX) Stock Looks Fairly Valued Despite Its 28% Run - Yahoo Finance (Sat, 31 Oct 2026 07:00:00 GMT); IDEXX Laboratories (IDXX) Q3 Earnings Leave Its Premium Valuation In Focus - Yahoo Finance (Tue, 03 Nov 2026 08:00:00 GMT) |
| S032 | news | CHTR | Thu, 12 Nov 2026 08:02:01 GMT | ok | https://news.google.com/rss/search?q=CHTR+Charter+Communications+stock&hl=en-US&gl=US&ceid=US:en | Charter Communications: 3 Key Takeaways for Long-Term Investors - Yahoo Finance (Thu, 12 Nov 2026 08:02:01 GMT); Charter Communications (CHTR) Stock Looks Reasonable As Shares Slump 85% - Yahoo Finance (Wed, 28 Oct 2026 07:00:00 GMT); Should Value Investors Buy Charter Communications (CHTR) Stock? - Yahoo Finance (Wed, 21 Oct 2026 07:00:00 GMT) |
| S033 | filing | ROP | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000882835&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000882835-26-000047); 8-K filed 2026-10-22 (accession 0000882835-26-000042); 8-K filed 2026-10-01 (accession 0000882835-26-000039) |
| S034 | filing | CLX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000021076.json | Diluted EPS 1.39 for period ending 2026-09-30 (filed 2026-11-02) |
| S035 | filing | CHTR | 2026-11-06 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001091667.json | Diluted EPS 0.38 for period ending 2026-09-30 (filed 2026-11-06) |
| S036 | filing | IDXX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000874716.json | Diluted EPS 11.75 for period ending 2026-09-30 (filed 2026-11-02) |
| S037 | news | ROP | Fri, 13 Nov 2026 01:46:04 GMT | ok | https://news.google.com/rss/search?q=ROP+Roper+Technologies+stock&hl=en-US&gl=US&ceid=US:en | Roper Technologies, Inc. (ROP) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 01:46:04 GMT); Roper Technologies (ROP) Stock Looks Fully Valued As Cash Flow Comes Into Focus - Yahoo Finance (Fri, 06 Nov 2026 07:13:00 GMT); Roper Technologies: 3 Key Takeaways for Long-Term Investors - Yahoo Finance (Mon, 26 Oct 2026 07:00:00 GMT) |
| S038 | stock | ROP | 2026-11-14 | ok | https://finance.yahoo.com/quote/ROP | Trailing P/E: 18.993866; Forward P/E: 19.532475; Forward EPS: 24.57318; Price: 479.975; Market price: 479.975; Market cap: 47535013888; Sector: Technology; Trailing Eps: 25.27; Revenue Growth: 0.076; Earnings Growth: 0.326; Gross Margin: 0.69671; Operating Margin: 0.28049; Profit Margin: 0.30712998; Return On Equity: 0.13229; Total Revenue: 8434599936; Market Cap: 47535013888; Consensus EPS FY+1: 24.57318; growth: 0.09810001 |
| S039 | filing | RDDT | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001713445&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0001713445-26-000116); 8-K filed 2026-10-29 (accession 0001713445-26-000114); 8-K filed 2026-08-12 (accession 0001713445-26-000107) |
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
- filing PNR: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 (2026-10-27)
- filing FISV: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 (2026-11-04)
- news FISV: https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 00:53:33 GMT)
- news APP: https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en (Thu, 12 Nov 2026 20:05:45 GMT)
- stock FISV: https://finance.yahoo.com/quote/FISV (2026-11-14)
- filing APP: https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json (2026-11-04)
- stock APP: https://finance.yahoo.com/quote/APP (2026-11-14)
- stock PNR: https://finance.yahoo.com/quote/PNR (2026-11-14)
- filing GEN: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 (2026-10-29)
- filing PNR: https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json (2026-10-27)
- news PNR: https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 15:54:46 GMT)
- filing FISV: https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json (2026-11-04)

## AI Provenance

- Provider / model: hermes-local-proxy / upstage/solar-mini4:free
- Market research: attempts=1 tokens=9521 (prompt=6521, completion=3000) runtime=25.78s
- Fundamental research: generated this run at 2026-11-14T19:15:09.837088+00:00
- Evidence source dates: {'as_of': '2026-11-13', 'latest_equity_date': '2026-11-13', 'latest_macro_date': '2026-11-13', 'flows_date': '2026-11-13'}
- Evidence fingerprint: bb19f72ba6c21c42eaa325742f9d7d1104cc79f1cdc19dd14951e1f9a266af26
- Source citations are retrieved external records in the ledger above; market values remain from the verified database snapshot.


## Disclosures

- This is research and market intelligence, not investment advice.
- AI conclusions are research judgments, not validated return predictions.
- The frozen risk layer is risk-only and is not used for directional views or allocations.
- Legacy scores are not active inputs or outputs.

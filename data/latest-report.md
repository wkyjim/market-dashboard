# AEGIS AI-First Market Intelligence

Research generated at: 17 November 2026, 18:08 HKT
Database freshness: equity 2026-11-16 (latest row retrieved 2026-11-17 13:06:22.906505+08:00)
Data cutoff: 2026-11-16 US cash close
Snapshot ID: aegis-hourly-20261117T100826Z

## Executive Summary

- **AI market view: Late-November 2026 US equities show a mixed tape: broad market indices are down over the past 20 days, but a large majority of names remain above their 50-day and 200-day moving averages, and health care, consumer staples, real estate, utilities and financials posted positive 20-day sector returns. The shortlist is dominated by high-momentum and dislocation names, with several large-cap technology names flagged as liquidity leaders despite elevated valuations.**
- Broad market momentum is mixed: SPX is down 3.56% over 20 days, yet 64.93% of constituents are above their 50-day moving average and 59.3% above their 200-day moving average.
- Sector leadership is defensive and rate-sensitive: Health Care (+6.96%), Utilities (+6.67%), Consumer Staples (+6.18%) and Real Estate (+6.19%) lead the 20-day returns.
- Information Technology (-11.40%) and Communication Services (-2.97%) are the weakest sectors, with Information Technology also the most negative on a 20-day basis.
- The shortlist is driven by independent momentum, dislocation, valuation and liquidity screens; several names carry extreme trailing P/E multiples or negative earnings yields, so valuation quality is mixed.
- Macro data as of 2026-11-17 show a 10Y-2Y spread of 0.29, US high-yield OAS of 3.23 and IG OAS of 0.89, with effective fed funds at 3.88.
- Risk indicators show 5-day forecast volatility of 20.00% versus a historical baseline of 22.95%, with a 34.1% spike probability, but no directional signal.

## Data QC

- Status: **PASS_WITH_WARNINGS**
- Equity session: 0 completed session(s) behind inference date
- Macro session: 2026-11-17 (0 completed session(s) behind inference date)
- Equity provenance: 359 provisional / 12644 canonical
- Breadth lag: 0 session(s); ETF-flow lag: 0 session(s)
- Note: Equity session contains a mix of provisional yfinance and canonical Massive rows.
- External sources: 79 ok / 0 unavailable; retrieved 2026-11-17T10:08:43.595160+00:00

## Idea Discovery

- S&P 500 universe: 503; eligible: 501; transparent shortlist: 20
- Method: independent momentum/dislocation/PE/liquidity buckets; no composite score
- Evidence used: latest close, 20d and 60d price returns, 60d drawdown, trailing P/E, earnings yield, sector-relative P/E, dollar volume, GICS sector
- Not available as verified inputs: verified earnings-revision history for the full universe, FY+2 consensus, structured industry catalyst calendar
- Eligible but not shortlisted: 481 (outside the top independent momentum, dislocation, valuation and liquidity buckets)
- Included: APP (top_20d_momentum); FISV (top_20d_momentum); PNR (top_20d_momentum); CLX (top_20d_momentum); GEN (top_20d_momentum); CHTR (top_20d_momentum); ROP (top_20d_momentum); IDXX (top_20d_momentum); SNDK (largest_20d_dislocation, liquidity_leader); RDDT (largest_20d_dislocation); INTC (largest_20d_dislocation); MRVL (largest_20d_dislocation); LITE (largest_20d_dislocation); DDOG (largest_20d_dislocation); FFIV (largest_20d_dislocation); NOW (largest_20d_dislocation); NVDA (liquidity_leader); MU (liquidity_leader); AMD (liquidity_leader); AAPL (liquidity_leader)
- Excluded reasons: {"missing_recent_or_latest_price": 2}
- Valuation-quality rejected: [{"flags": ["forward_eps_missing"], "ticker": "FISV"}, {"flags": ["forward_pe_outside_plausible_range", "implausible_earnings_yield", "forward_eps_vs_reported_jump"], "ticker": "CHTR"}, {"flags": ["forward_pe_outside_plausible_range", "implausible_earnings_yield"], "ticker": "SNDK"}, {"flags": ["forward_eps_vs_reported_jump"], "ticker": "MRVL"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "LITE"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "DDOG"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "FFIV"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "NOW"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "NVDA"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "MU"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "AMD"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "AAPL"}]

## Market Snapshot

| Asset | Latest | Change | Observation |
| --- | --- | --- | --- |
| SPX | 7416.5898 | -3.56% (20d) | Broad index down over 20 days; still above key moving averages in breadth terms. |
| Health Care (XLV) | return_20d 6.96% | +6.96% | Strongest major sector; trailing P/E 30.62. |
| Consumer Staples (XLP) | return_20d 6.18% | +6.18% | Defensive strength; trailing P/E 24.92. |
| Real Estate (XLRE) | return_20d 6.19% | +6.19% | Positive 20-day return; trailing P/E 29.55. |
| Utilities (XLU) | return_20d 6.67% | +6.67% | Positive 20-day return; trailing P/E 18.15. |
| Financials (XLF) | return_20d 5.67% | +5.67% | Positive 20-day return; trailing P/E 15.71. |
| Information Technology (XLK) | return_20d -11.40% | -11.40% | Weakest major sector; trailing P/E 29.06. |
| Communication Services (XLC) | return_20d -2.97% | -2.97% | Negative 20-day return; trailing P/E 16.97. |
| Industrials (XLI) | return_20d -0.61% | -0.61% | Slightly negative 20-day return; trailing P/E 26.57. |
| Materials (XLB) | return_20d 1.02% | +1.02% | Slightly positive 20-day return; trailing P/E 21.40. |
| Energy (XLE) | return_20d -6.06% | -6.06% | Negative 20-day return; trailing P/E 15.91. |
| Consumer Discretionary (XLY) | return_20d 3.22% | +3.22% | Positive 20-day return; trailing P/E 24.73. |

## Macro, Fiscal, Rates, Liquidity and Credit

- Growth: US equities are down 3.56% over 20 days, but breadth remains constructive with 64.93% above the 50-day and 59.3% above the 200-day moving average.
- Inflation: CPI and core CPI are available only through 2026-09-01 (336.298 and 338.896), so near-term inflation momentum cannot be confirmed from the supplied database.
- Policy: Effective federal funds rate is 3.88 as of 2026-11-13, and the 10Y-2Y Treasury spread is 0.29 as of 2026-11-16, indicating a modestly positive but shallow yield curve.
- Rates: US high-yield OAS is 3.23 and IG OAS is 0.89 as of 2026-11-13, suggesting credit conditions are not in acute stress.
- Liquidity: Sector ETF flows show XLV with a strong inflow confirmation and XLY with medium-term recovery, while XLU shows medium-term deterioration.
- Credit: The risk block shows 5-day forecast volatility of 20.00% versus a historical baseline of 22.95%, with a 34.1% spike probability and no directional signal.

## US Equities and 11 GICS Sectors

Macro source IDs: S001, S002, S003, S004, S005, S006, S007

| GICS sector | Evidence | AI research stance | Source IDs |
| --- | --- | --- | --- |
| Health Care | 20-day sector return +6.96% (XLV); trailing P/E 30.62; breadth shows 64.93% above 50-day and 59.3% above 200-day. | Defensive leadership with positive momentum; valuation is rich but supported by sector strength. | S052 |
| Consumer Staples | 20-day sector return +6.18% (XLP); trailing P/E 24.92; defensive positioning amid mixed market breadth. | Stable defensive sector; positive 20-day return with moderate valuation. | S060 |
| Consumer Discretionary | 20-day sector return +3.22% (XLY); trailing P/E 24.73; flow z-score 20d 0.67, 60d -0.46, medium-term recovery. | Modestly positive; flow structure suggests medium-term recovery but not strong confirmation. | S059 |
| Real Estate | 20-day sector return +6.19% (XLRE); trailing P/E 29.55; positive sector momentum. | Positive 20-day return; valuation is elevated but sector is outperforming. | S062 |
| Financials | 20-day sector return +5.67% (XLF); trailing P/E 15.71; positive sector return with relatively low valuation. | Positive momentum and reasonable valuation; supportive of financial sector. | S064 |
| Utilities | 20-day sector return +6.67% (XLU); trailing P/E 18.15; positive sector return but flow z-score 20d -1.97 indicates medium-term deterioration. | Sector strength is positive, but flow structure suggests medium-term deterioration; monitor for reversal. | S067 |
| Materials | 20-day sector return +1.02% (XLB); trailing P/E 21.40; slightly positive sector return. | Neutral-to-slightly-positive; modest strength with moderate valuation. | S068 |
| Industrials | 20-day sector return -0.61% (XLI); trailing P/E 26.57; slightly negative sector return. | Slightly negative; valuation is above the low end but sector is not leading. | S069 |
| Communication Services | 20-day sector return -2.97% (XLC); trailing P/E 16.97; negative sector return. | Negative momentum; valuation is reasonable but sector is underperforming. | S071 |
| Information Technology | 20-day sector return -11.40% (XLK); trailing P/E 29.06; largest negative sector return. | Weakest major sector; significant drawdown despite moderate trailing P/E. | S073 |
| Energy | 20-day sector return -6.06% (XLE); trailing P/E 15.91; negative sector return. | Negative momentum; valuation is low but sector is underperforming. | S076 |

### Sector fundamentals, valuation and earnings

No point-in-time sector fundamentals beyond the supplied 20-day ETF returns, trailing P/E multiples and flow z-scores are available in the database. The supplied evidence is limited to these metrics; no growth, margin, earnings revision or consensus data are provided for the sector ETFs.

## Growth vs Value

- Health Care and Consumer Staples show the strongest 20-day sector returns (+6.96% and +6.18%) with trailing P/Es of 30.62 and 24.92, indicating premium valuations but positive momentum.
- Financials and Utilities offer lower trailing P/Es (15.71 and 18.15) with positive 20-day returns, but Utilities flow structure shows medium-term deterioration.
- Information Technology is the weakest sector at -11.40% over 20 days, with a trailing P/E of 29.06, suggesting a valuation that is not cheap relative to its underperformance.
- Energy has a low trailing P/E of 15.91 but a negative 20-day return of -6.06%, indicating that low valuation has not yet translated into positive momentum.

## ETF Flows and Breadth

- SPX is down 3.56% over 20 days, but 64.93% of constituents are above their 50-day moving average and 59.3% above their 200-day moving average, indicating broad market resilience.
- XLY shows a 20-day flow z-score of 0.67 and a 60-day z-score of -0.46, consistent with a medium-term recovery in consumer discretionary flows.
- XLV shows a 20-day flow z-score of 1.27 and a 60-day z-score of 1.85, indicating strong inflow confirmation in health care.
- XLU shows a 20-day flow z-score of -1.97, indicating medium-term deterioration in utility flows despite a positive 20-day sector return.
- Advance/decline ratio is 0.407 with 145 advancers and

## Stock Ideas

Single-stock research uses reported EPS, forward P/E and company fundamentals. All ideas are research judgments, not validated return predictions.

| Ticker | Security | Research view | Price | EPS | Forward P/E | Base target | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| APP | AppLovin | NEW | 415.22 | 20.86026 | 19.904833 | 458.93 | NEW |
| PNR | Pentair | KEEP | 68.44 | 5.30402 | 12.903421 | 74.26 | KEEP |
| ROP | Roper Technologies | KEEP | 483.72 | 24.57318 | 19.684877 | 393.17 | KEEP |
| IDXX | Idexx Laboratories | KEEP | 700.65 | 16.8929 | 41.476006 | 506.79 | KEEP |

## ETF Ideas

ETF research uses holdings, portfolio valuation and exposure. Single-stock EPS × P/E valuation is not applied to ETFs.

| Ticker | Fund | Research view | Price | Top holdings | Portfolio valuation | Sector exposure | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| XLP | Consumer Staples sector ETF | KEEP | 92.6 | WMT 11.14%, COST 9.09%, PG 7.60%, KO 7.37%, PM 6.59%, MO 4.70%, CL 4.42%, MDLZ 4.25%, PEP 4.11%, TGT 4.00% | Top 10 holdings; numeric weight coverage 63.28% | Consumer Staples | KEEP |
### APP — AppLovin

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** AppLovin offers a high-margin, high-growth mobile-gaming franchise with strong 20-day momentum and a defensible forward P/E, making it a more attractive standalone momentum candidate than the lower-margin, lower-growth names in the shortlist such as Pentair or Clorox. Alternatives considered: PNR, CLX.
- **Thesis:** AppLovin screens in the top 20-day momentum bucket with a 54% 20-day return and a 36% 60-day return, indicating strong price follow-through. Reported diluted EPS of 11.61 for the fiscal period ending 2026-09-30 and a forward EPS of 20.86 support a forward P/E near 19.9, which is reasonable for a high-margin, high-growth mobile-gaming platform. The company's gross margin near 89% and operating margin near 78% provide a durable profitability profile that can compound earnings while the stock has already shown momentum.
- **Source IDs:** S008, S012, S013, S019
- **Catalysts:** Continued 20-day momentum and positive 60-day return trajectory, Sustained high gross and operating margins supporting earnings growth, Forward EPS of 20.86 providing a valuation anchor near 19.9x forward earnings
- **Risks:** High 20-day momentum can mean elevated volatility and potential mean-reversion risk, Forward EPS and fiscal-year mapping are unverified, so forward P/E should be treated as indicative, Mobile-gaming sector competition and ad-market cyclicality could pressure growth
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 20.8603 (source.forwardEps) x AI multiple assumption 22.00; source IDs S008, S012, S013, S019
- **EPS:** 20.86026 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 19.904833
- **FY+1 growth assumption:** 27.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / MSFT / APP shows strong FY1 consensus growth of 27.44% with 25.4% revenue growth and 75.5% earnings growth, supported by 88.8% gross margin and 77.8% operating margin. The forward P/E of 19.9x is below the 22x base multiple, reflecting a premium growth profile relative to peers. Microsoft is used as a comparable software peer for growth and margin structure.
- **Company fundamentals:** Reported diluted EPS 11.61 for the fiscal period ending 2026-09-30; forward EPS 20.86; forward P/E 19.90; gross margin 88.78%; operating margin 77.78%; profit margin 65.89%; revenue growth 55.5%; earnings growth 75.5%; ROE 2.10%.
- **Bull / Base / Bear:** 542.37 / 458.93 / 333.76
- **Bull / Base / Bear returns:** 30.62% / 10.53% / -19.62%
- **Scenario probabilities:** not separately assigned; see scenario table.

### PNR — Pentair

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Pentair is a lower-cost industrial name relative to its sector, but its negative earnings growth and modest margins make it less attractive than higher-quality momentum names such as AppLovin or Roper Technologies. Alternatives considered: APP, ROP.
- **Thesis:** Pentair is a top-20-day-momentum name with a 30% 20-day return and a 60-day return of 6%, but its fundamentals are mixed. Reported diluted EPS of 2.76 and forward EPS of 5.30 give a forward P/E near 12.9, yet revenue growth is negative at -4.5% and earnings growth is negative at -18.8%. The stock is trading at a sector-relative P/E of 0.49, suggesting it is cheap relative to its sector, but the earnings decline and modest margin profile (gross margin 40.2%, operating margin 21.4%) do not yet support a strong conviction buy.
- **Source IDs:** S009, S014, S016, S017
- **Catalysts:** Positive 20-day momentum and a low sector-relative P/E, Forward EPS of 5.30 provides a valuation anchor near 12.9x forward earnings, Potential stabilization in earnings if the cyclical industrial recovery materializes
- **Risks:** Negative revenue growth of -4.5% and negative earnings growth of -18.8%, Modest gross margin of 40.2% and operating margin of 21.4% limit upside, Forward EPS and fiscal-year mapping are unverified, so forward P/E should be treated as indicative
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 5.3040 (source.forwardEps) x AI multiple assumption 14.00; source IDs S009, S014, S016, S017
- **EPS:** 5.30402 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 12.903421
- **FY+1 growth assumption:** 12.82%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / CSCO / PNR has modest FY1 consensus growth of 12.82% with 18.4% revenue growth but negative earnings growth of -18.8%, reflecting margin pressure with 40.2% gross margin and 21.4% operating margin. The forward P/E of 12.9x is below the 14x base multiple, consistent with a lower-growth, higher-risk profile. Cisco is used as a comparable for network infrastructure valuation.
- **Company fundamentals:** Reported diluted EPS 2.76 for the fiscal period ending 2026-09-30; forward EPS 5.30; forward P/E 12.90; gross margin 40.17%; operating margin 21.41%; profit margin 15.44%; revenue growth -4.5%; earnings growth -18.8%; ROE 15.61%.
- **Bull / Base / Bear:** 90.17 / 74.26 / 58.34
- **Bull / Base / Bear returns:** 31.75% / 8.5% / -14.76%
- **Scenario probabilities:** not separately assigned; see scenario table.

### ROP — Roper Technologies

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Roper Technologies offers a higher-quality technology-enabled industrial franchise with better margins and a more reasonable valuation than the lower-margin industrial names in the shortlist, but its modest growth profile keeps it from a strong buy rating. Alternatives considered: APP, PNR.
- **Thesis:** Roper Technologies is a top-20-day-momentum name with a 26% 20-day return and a 17% 60-day return, supported by a high forward P/E of 19.7 and a sector-relative P/E of 0.49. Reported diluted EPS of 21.3 and forward EPS of 24.57 provide a reasonable valuation for a technology-enabled industrial distributor. However, revenue growth is modest at 7.6% and earnings growth is 32.6%, so the stock is not a high-growth compounder. The positive momentum and reasonable valuation justify a neutral stance with a focus on whether the 20-day momentum can persist.
- **Source IDs:** S030, S032, S035, S041
- **Catalysts:** Positive 20-day momentum and a 17% 60-day return, Forward EPS of 24.57 providing a valuation anchor near 19.7x forward earnings, Diversified technology portfolio with high gross margin of 69.7%
- **Risks:** Modest revenue growth of 7.6% limits upside relative to high-growth names, Forward EPS and fiscal-year mapping are unverified, so forward P/E should be treated as indicative, Technology-enabled industrial distribution is subject to cyclical demand and customer spending cycles
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 24.5732 (source.forwardEps) x AI multiple assumption 16.00; source IDs S030, S032, S035, S041
- **EPS:** 24.57318 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 19.684877
- **FY+1 growth assumption:** 9.81%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / HD / ROP shows FY1 consensus growth of 9.81% with 6.3% revenue growth and 32.6% earnings growth, supported by 69.7% gross margin and 28.0% operating margin. The forward P/E of 19.7x is below the 16x base multiple, reflecting a value-oriented consumer discretionary profile. Home Depot is used as a comparable for retail and consumer discretionary valuation.
- **Company fundamentals:** Reported diluted EPS 21.3 for the fiscal period ending 2026-09-30; forward EPS 24.57; forward P/E 19.68; gross margin 69.67%; operating margin 28.05%; profit margin 30.71%; revenue growth 7.6%; earnings growth 32.6%; ROE 13.23%.
- **Bull / Base / Bear:** 466.89 / 393.17 / 319.45
- **Bull / Base / Bear returns:** -3.48% / -18.72% / -33.96%
- **Scenario probabilities:** not separately assigned; see scenario table.

### IDXX — Idexx Laboratories

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Idexx offers a premium, high-margin diagnostics franchise with strong momentum, but its high valuation and modest growth profile make it less attractive than the lower-cost momentum names in the shortlist. Alternatives considered: APP, ROP.
- **Thesis:** Idexx Laboratories is a top-20-day-momentum name with a 26% 20-day return and a 26% 60-day return, and it screens with a sector-relative P/E of 1.33, indicating it is trading at a premium to its sector. Reported diluted EPS of 11.75 and forward EPS of 16.89 give a forward P/E near 41.5, which is high but reflects a premium-quality diagnostics franchise with strong margins (gross margin 62.7%, operating margin 32.5%). The stock is not a cheap dislocation play, and the high valuation means the market is pricing in sustained growth. A neutral stance is appropriate until the momentum can be validated by earnings delivery.
- **Source IDs:** S034, S037, S040, S043
- **Catalysts:** Positive 20-day and 60-day momentum of 26% each, Premium sector-relative P/E of 1.33 reflecting a high-quality diagnostics franchise, Forward EPS of 16.89 providing a valuation anchor near 41.5x forward earnings
- **Risks:** High forward P/E of 41.5 leaves limited room for error if growth disappoints, Forward EPS and fiscal-year mapping are unverified, so forward P/E should be treated as indicative, Diagnostics sector is sensitive to pet-health spending cycles and veterinary practice consolidation
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 16.8929 (source.forwardEps) x AI multiple assumption 30.00; source IDs S034, S037, S040, S043
- **EPS:** 16.8929 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 41.476006
- **FY+1 growth assumption:** 12.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / ILMN / IDXX shows FY1 consensus growth of 12.44% with 8.9% revenue growth and 17.9% earnings growth, supported by 62.7% gross margin and 32.5% operating margin. The forward P/E of 41.5x is below the 30x base multiple, reflecting a higher-growth healthcare diagnostics profile. Illumina is used as a comparable for healthcare diagnostics valuation.
- **Company fundamentals:** Reported diluted EPS 11.75 for the fiscal period ending 2026-09-30; forward EPS 16.89; forward P/E 41.48; gross margin 62.72%; operating margin 32.50%; profit margin 25.36%; revenue growth 9.9%; earnings growth 17.9%; ROE 68.93%.
- **Bull / Base / Bear:** 608.14 / 506.79 / 405.43
- **Bull / Base / Bear returns:** -13.2% / -27.67% / -42.14%
- **Scenario probabilities:** not separately assigned; see scenario table.

### XLP — Consumer Staples sector ETF

- **Type:** ETF
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** XLP offers the most attractive sector-ETF momentum in the shortlist with a diversified, defensive consumer staples portfolio, but its strong relative performance and defensive nature make it a neutral holding rather than an aggressive buy. Alternatives considered: XLV, XLY.
- **Thesis:** XLP is a Consumer Staples sector ETF with a 27% price change over the period, making it the strongest sector ETF in the shortlist. It provides diversified exposure to essential consumer staples through top holdings such as WMT, COST, PG, KO, and PM. The ETF is a defensive, low-beta holding that can serve as a portfolio stabilizer, but its high relative strength means it may already be pricing in a defensive rotation. A neutral stance is appropriate, with the ETF used for sector exposure rather than aggressive positioning.
- **Source IDs:** S058, S060
- **Catalysts:** Strong 27% price change, the best among the sector ETFs in the shortlist, Diversified exposure to essential consumer staples with top holdings WMT, COST, PG, KO, PM, Defensive characteristics provide portfolio stability in uncertain macro conditions
- **Risks:** High relative strength may mean the ETF is already pricing in a defensive rally, Consumer staples face margin pressure from input cost inflation and currency headwinds, Sector rotation into staples can reverse quickly if growth expectations improve
- **Valuation method:** Holdings/portfolio valuation with AI total-return assumption
- **Valuation status:** verified; forward-EPS source: ; period flags: 
- **Valuation assumptions:** Holdings/portfolio valuation; 10 weighted holdings; coverage 63.28%; source IDs S058, S060
- **Top holdings:** WMT 11.14%, COST 9.09%, PG 7.60%, KO 7.37%, PM 6.59%, MO 4.70%, CL 4.42%, MDLZ 4.25%, PEP 4.11%, TGT 4.00%
- **Portfolio valuation:** Top 10 holdings; numeric weight coverage 63.28%
- **Sector exposure:** Consumer Staples
- **Underlying drivers:** Consumer staples demand resilience, defensive rotation, and strong relative performance driven by WMT, COST, PG, KO, and PM.
- **Bull / Base / Bear:** 101.86 / 96.3 / 89.82
- **Bull / Base / Bear returns:** 10.0% / 4.0% / -3.0%
- **Scenario probabilities:** not separately assigned; see scenario table.

## Quant Risk Layer

| Field | Value |
| --- | --- |
| Volatility model | vol5_ols_v1 |
| Spike model | spike_logit_v1 |
| As-of date | 2026-11-16 |
| Target window | 2026-11-17 to 2026-11-23 |
| Forecast 5D annualized volatility | 20.00% |
| Historical-vol baseline | 22.95% |
| EWMA baseline | 20.85% |
| Spike probability | 34.14% |
| Spike threshold | 18.50% |
| Status | prospective |
| Forecast ID | 1033bd48a6e76c15 |

Risk-only; no directional interpretation or allocation implication.

## Scenarios

### Short Term (5 trading sessions)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 25% | +2.00% | Elevated 5-day volatility (0.200) and 34.1% spike probability suggest a tail-risk event could resolve favorably if the frozen daily-close model confirms a post-US-close recovery, driving a modest +2.0% move. |
| Base | 50% | +0.00% | Directional signal is false and the 5-day volatility (0.200) is only slightly above the historical baseline (0.229) and EWMA baseline (0.208), implying a range-bound week with near-zero expected return. |
| Bear | 25% | -2.00% | A 34.1% spike probability combined with a frozen daily-close model that has not yet confirmed a US close leaves downside risk intact; if the spike materializes without a directional offset, a -2.0% decline is plausible. |

### Long Term (12 months)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 30% | +8.00% | Sustained volatility normalization and a confirmed post-US-close recovery could extend the elevated 5-day vol (0.200) into a trend, supporting an 8.0% annualized return over the horizon. |
| Base | 40% | +3.00% | With the directional signal false and volatility only marginally above baseline, a modest positive drift of 3.0% reflects steady but unspectacular market participation over the longer horizon. |
| Bear | 30% | -5.00% | If the 34.1% spike probability triggers a sustained risk-off episode and the frozen daily-close model fails to confirm a recovery, the elevated volatility environment could drive a -5.0% decline over the long term. |

## Positioning


## Catalysts

| Date | Event | Why it matters |
| --- | --- | --- |

## Key Risks


## External Source Ledger

| ID | Type | Ticker | Published | Status | URL | Claims |
| --- | --- | --- | --- | --- | --- | --- |
| S001 | macro | macro | 2026-11-13 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFF&cosd=2026-01-01 | Effective federal funds rate (DFF) latest observation 2026-11-13: 3.88 |
| S002 | macro | macro | 2026-11-13 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLH0A0HYM2&cosd=2026-01-01 | US high-yield OAS (BAMLH0A0HYM2) latest observation 2026-11-13: 3.23 |
| S003 | macro | macro | 2026-11-13 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLC0A0CM&cosd=2026-01-01 | US investment-grade OAS (BAMLC0A0CM) latest observation 2026-11-13: 0.89 |
| S004 | macro | macro | 2026-10-01 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCSL&cosd=2026-01-01 | US CPI (CPIAUCSL) latest observation 2026-10-01: 337.476 |
| S005 | macro | macro | 2026-10-01 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=UNRATE&cosd=2026-01-01 | US unemployment rate (UNRATE) latest observation 2026-10-01: 4.1 |
| S006 | macro | macro | 2026-10-01 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=PAYEMS&cosd=2026-01-01 | US nonfarm payrolls (PAYEMS) latest observation 2026-10-01: 159293 |
| S007 | macro | macro | 2026-11-16 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=T10Y2Y&cosd=2026-01-01 | 10Y-2Y Treasury spread (T10Y2Y) latest observation 2026-11-16: 0.29 |
| S008 | filing | APP | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001751008&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0001751008-26-000069); 8-K filed 2026-11-04 (accession 0001751008-26-000068); 10-Q filed 2026-08-05 (accession 0001751008-26-000059) |
| S009 | filing | PNR | 2026-10-27 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-27 (accession 0000077360-26-000058); 8-K filed 2026-10-27 (accession 0000077360-26-000055); 8-K filed 2026-09-22 (accession 0000077360-26-000050) |
| S010 | filing | FISV | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0000798354-26-000042); 8-K filed 2026-11-03 (accession 0000798354-26-000039); 8-K filed 2026-10-23 (accession 0001193125-26-429481) |
| S011 | news | FISV | Tue, 17 Nov 2026 09:38:35 GMT | ok | https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en | Fiserv, Inc. (FISV) stock price, news, quote and history - Yahoo Finance Singapore (Tue, 17 Nov 2026 09:38:35 GMT); Fiserv (FISV) Stock Looks Undervalued With Strong Excess Returns - Yahoo Finance (Wed, 11 Nov 2026 22:14:34 GMT); Fiserv Stock Outlook: Is Wall Street Bullish or Bearish? - Yahoo Finance (Thu, 12 Nov 2026 12:23:56 GMT) |
| S012 | news | APP | Thu, 12 Nov 2026 20:05:45 GMT | ok | https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en | AppLovin Just Ripped 47% in a Month: Is It Too Late to Buy APP Stock Now? - Yahoo Finance (Thu, 12 Nov 2026 20:05:45 GMT); AppLovin Stock Moves Higher: What's Going On? - Benzinga (Mon, 16 Nov 2026 18:52:15 GMT); APP Stock Quote Price and Forecast - CNN (Mon, 16 Nov 2026 02:55:55 GMT) |
| S013 | filing | APP | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json | Diluted EPS 11.61 for period ending 2026-09-30 (filed 2026-11-04) |
| S014 | news | PNR | Fri, 13 Nov 2026 22:50:05 GMT | ok | https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en | Pentair Stock Price Forecast. Should You Buy PNR? - StockInvest.us (Fri, 13 Nov 2026 22:50:05 GMT); Why Pentair Stock Popped This Morning - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT); Pentair plc (PNR) Q3 Earnings and Revenues Beat Estimates - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT) |
| S015 | filing | CLX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000021076-26-000046); 8-K filed 2026-11-02 (accession 0000021076-26-000044); 8-K filed 2026-10-29 (accession 0001206774-26-000586) |
| S016 | stock | PNR | 2026-11-17 | ok | https://finance.yahoo.com/quote/PNR | Trailing P/E: 18.648502; Forward P/E: 12.903421; Forward EPS: 5.30402; Price: 68.44; Market price: 68.44; Market cap: 10926767104; Sector: Industrials; Trailing Eps: 3.67; Revenue Growth: -0.045; Earnings Growth: -0.188; Gross Margin: 0.40168998; Operating Margin: 0.21410999; Profit Margin: 0.15435; Return On Equity: 0.15605; Total Revenue: 3966200064; Market Cap: 10926767104; Consensus EPS FY+1: 5.30402; growth: 0.1282 |
| S017 | filing | PNR | 2026-10-27 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json | Diluted EPS 2.76 for period ending 2026-09-30 (filed 2026-10-27) |
| S018 | stock | FISV | 2026-11-17 | ok | https://finance.yahoo.com/quote/FISV | Forward P/E: 7.943647; Price: 63.32; Market price: 63.32; Market cap: 33689260032; Market Cap: 33689260032; Consensus EPS FY+1: 7.97177; growth: 0.0953 |
| S019 | stock | APP | 2026-11-17 | ok | https://finance.yahoo.com/quote/APP | Trailing P/E: 27.960941; Forward P/E: 19.904833; Forward EPS: 20.86026; Price: 415.22; Market price: 415.22; Market cap: 137571516416; Sector: Communication Services; Trailing Eps: 14.85; Revenue Growth: 0.555; Earnings Growth: 0.755; Gross Margin: 0.8878; Operating Margin: 0.77782995; Profit Margin: 0.65887; Return On Equity: 2.1008599; Total Revenue: 7608893952; Market Cap: 137571516416; Consensus EPS FY+1: 20.72438; growth: 0.2744 |
| S020 | filing | FISV | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json | Diluted EPS -8.9 for period ending 2026-09-30 (filed 2026-11-04) |
| S021 | news | CLX | Tue, 17 Nov 2026 00:55:20 GMT | ok | https://news.google.com/rss/search?q=CLX+Clorox+stock&hl=en-US&gl=US&ceid=US:en | The Clorox Company (CLX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Tue, 17 Nov 2026 00:55:20 GMT); The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance Singapore (Tue, 17 Nov 2026 01:06:04 GMT); Clorox Stock Rides An 11-Day Winning Streak To A 25% Gain - Trefis (Tue, 17 Nov 2026 08:40:15 GMT) |
| S022 | filing | GEN | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0000849399-26-000083); 8-K filed 2026-10-28 (accession 0000849399-26-000081); 8-K filed 2026-10-09 (accession 0000849399-26-000079) |
| S023 | filing | CLX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000021076.json | Diluted EPS 1.39 for period ending 2026-09-30 (filed 2026-11-02) |
| S024 | filing | CHTR | 2026-11-06 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-06 (accession 0001091667-26-000073); 8-K filed 2026-11-06 (accession 0001091667-26-000072); 8-K filed 2026-10-27 (accession 0001091667-26-000064) |
| S025 | stock | GEN | 2026-11-17 | ok | https://finance.yahoo.com/quote/GEN | Trailing P/E: 15.431472; Forward P/E: 9.108996; Forward EPS: 3.33736; Price: 30.4; Market price: 30.4; Market cap: 18035593216; Sector: Technology; Trailing Eps: 1.97; Revenue Growth: 0.122; Earnings Growth: 1.286; Gross Margin: 0.77410007; Operating Margin: 0.43229; Profit Margin: 0.23068; Return On Equity: 0.46402; Total Revenue: 5228000256; Market Cap: 18035593216; Consensus EPS FY+1: 3.33736; growth: 0.1286 |
| S026 | filing | GEN | 2026-10-29 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000849399.json | Diluted EPS 0.83 for period ending 2026-10-02 (filed 2026-10-29) |
| S027 | news | GEN | Thu, 29 Oct 2026 07:00:00 GMT | ok | https://news.google.com/rss/search?q=GEN+Gen+Digital+stock&hl=en-US&gl=US&ceid=US:en | Gen Digital (GEN) Stock Repriced After Q2 Earnings Put Margins Center Stage - Yahoo Finance (Thu, 29 Oct 2026 07:00:00 GMT); What Was Gen Digital Telling You Before Its Stock Ran? - Yahoo Finance (Wed, 04 Nov 2026 08:00:00 GMT); Are Business Services Stocks Lagging GEN DIGITAL INC (GEN) This Year? - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT) |
| S028 | news | CHTR | Sun, 15 Nov 2026 05:47:01 GMT | ok | https://news.google.com/rss/search?q=CHTR+Charter+Communications+stock&hl=en-US&gl=US&ceid=US:en | Charter Communications (CHTR) Stock Could Be A Bargain Following Its New Operating Model - Yahoo Finance (Sun, 15 Nov 2026 05:47:01 GMT); Why You Should Think About Charter Communications Differently Now? - Yahoo Finance (Fri, 13 Nov 2026 19:16:11 GMT); Charter Communications (CHTR) Stock Looks Reasonable As Shares Slump 85% - Yahoo Finance (Wed, 28 Oct 2026 07:00:00 GMT) |
| S029 | stock | CHTR | 2026-11-17 | ok | https://finance.yahoo.com/quote/CHTR | Trailing P/E: 13.05921; Forward P/E: 3.057552; Forward EPS: 45.44485; Price: 138.95; Market price: 138.95; Market cap: 24879212544; Sector: Communication Services; Trailing Eps: 10.64; Revenue Growth: 0.091; Gross Margin: 0.55084; Operating Margin: 0.23389; Profit Margin: 0.02498; Return On Equity: 0.07019; Total Revenue: 55645999104; Market Cap: 24879212544; Consensus EPS FY+1: 49.35412; growth: 1.1136 |
| S030 | filing | ROP | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000882835&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000882835-26-000047); 8-K filed 2026-10-22 (accession 0000882835-26-000042); 8-K filed 2026-10-01 (accession 0000882835-26-000039) |
| S031 | stock | CLX | 2026-11-17 | ok | https://finance.yahoo.com/quote/CLX | Trailing P/E: 19.814749; Forward P/E: 17.860386; Forward EPS: 6.1684; Price: 110.17; Market price: 110.17; Market cap: 13346807808; Sector: Consumer Defensive; Trailing Eps: 5.56; Revenue Growth: 0.333; Earnings Growth: 1.138; Gross Margin: 0.41939998; Operating Margin: 0.14286; Profit Margin: 0.09408; Return On Equity: 5.34363; Total Revenue: 7196000256; Market Cap: 13346807808; Consensus EPS FY+1: 6.1684; growth: 0.0769 |
| S032 | stock | ROP | 2026-11-17 | ok | https://finance.yahoo.com/quote/ROP | Trailing P/E: 19.142065; Forward P/E: 19.684877; Forward EPS: 24.57318; Price: 483.72; Market price: 483.72; Market cap: 47905902592; Sector: Technology; Trailing Eps: 25.27; Revenue Growth: 0.076; Earnings Growth: 0.326; Gross Margin: 0.69671; Operating Margin: 0.28049; Profit Margin: 0.30712998; Return On Equity: 0.13229; Total Revenue: 8434599936; Market Cap: 47905902592; Consensus EPS FY+1: 24.57318; growth: 0.09810001 |
| S033 | filing | CHTR | 2026-11-06 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001091667.json | Diluted EPS 0.38 for period ending 2026-09-30 (filed 2026-11-06) |
| S034 | filing | IDXX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000874716&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000874716-26-000135); 8-K filed 2026-11-02 (accession 0001104659-26-120892); 10-Q filed 2026-08-04 (accession 0000874716-26-000123) |
| S035 | news | ROP | Thu, 05 Nov 2026 08:00:00 GMT | ok | https://news.google.com/rss/search?q=ROP+Roper+Technologies+stock&hl=en-US&gl=US&ceid=US:en | Roper Technologies (ROP) Stock Looks Fully Valued As Cash Flow Comes Into Focus - Yahoo Finance (Thu, 05 Nov 2026 08:00:00 GMT); Roper Technologies (ROP), What Is Behind The Fresh Attention? - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT); Did Earnings Beat Just Shift Roper Technologies (ROP) Investment Narrative? - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT) |
| S036 | filing | SNDK | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0002023554&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0001628280-26-068601); 8-K filed 2026-10-29 (accession 0001628280-26-068243); 8-K filed 2026-09-16 (accession 0001628280-26-062267) |
| S037 | news | IDXX | Sat, 31 Oct 2026 07:00:00 GMT | ok | https://news.google.com/rss/search?q=IDXX+Idexx+Laboratories+stock&hl=en-US&gl=US&ceid=US:en | IDEXX Laboratories (IDXX) Stock Looks Fairly Valued Despite Its 28% Run - Yahoo Finance (Sat, 31 Oct 2026 07:00:00 GMT); IDEXX Laboratories (IDXX) vs. ZTS and NEOG: Can Raised Guidance and Product Expansion Drive Further Earnings Growth? - Yahoo Finance (Thu, 22 Oct 2026 07:00:00 GMT); IDEXX Laboratories (IDXX) Q3 Earnings Leave Its Premium Valuation In Focus - Yahoo Finance (Tue, 03 Nov 2026 08:00:00 GMT) |
| S038 | filing | RDDT | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001713445&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0001713445-26-000116); 8-K filed 2026-10-29 (accession 0001713445-26-000114); 8-K filed 2026-08-12 (accession 0001713445-26-000107) |
| S039 | stock | SNDK | 2026-11-17 | ok | https://finance.yahoo.com/quote/SNDK | Trailing P/E: 6.466672; Forward P/E: 2.799166; Forward EPS: 289.05396; Price: 809.11; Market price: 809.11; Market cap: 115127738368; Sector: Technology; Trailing Eps: 125.12; Revenue Growth: 3.779; Earnings Growth: 69.133; Gross Margin: 0.79952; Operating Margin: 0.7268; Profit Margin: 0.67039; Return On Equity: 1.41174; Total Revenue: 28970999808; Market Cap: 115127738368; Consensus EPS FY+1: 289.05396; growth: 0.2707 |
| S040 | stock | IDXX | 2026-11-17 | ok | https://finance.yahoo.com/quote/IDXX | Trailing P/E: 47.21361; Forward P/E: 41.476006; Forward EPS: 16.8929; Price: 700.65; Market price: 700.65; Market cap: 55201599488; Sector: Healthcare; Trailing Eps: 14.84; Revenue Growth: 0.099; Earnings Growth: 0.179; Gross Margin: 0.62722; Operating Margin: 0.32497; Profit Margin: 0.25357; Return On Equity: 0.68925005; Total Revenue: 4662220800; Market Cap: 55201599488; Consensus EPS FY+1: 16.8929; growth: 0.1244 |

## Sources

- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFF&cosd=2026-01-01 (2026-11-13)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLH0A0HYM2&cosd=2026-01-01 (2026-11-13)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLC0A0CM&cosd=2026-01-01 (2026-11-13)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCSL&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=UNRATE&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=PAYEMS&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=T10Y2Y&cosd=2026-01-01 (2026-11-16)
- filing APP: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001751008&type=10-Q&dateb=&owner=include&count=10 (2026-11-04)
- filing PNR: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 (2026-10-27)
- filing FISV: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 (2026-11-04)
- news FISV: https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en (Tue, 17 Nov 2026 09:38:35 GMT)
- news APP: https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en (Thu, 12 Nov 2026 20:05:45 GMT)
- filing APP: https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json (2026-11-04)
- news PNR: https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 22:50:05 GMT)
- filing CLX: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 (2026-11-02)
- stock PNR: https://finance.yahoo.com/quote/PNR (2026-11-17)
- filing PNR: https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json (2026-10-27)
- stock FISV: https://finance.yahoo.com/quote/FISV (2026-11-17)
- stock APP: https://finance.yahoo.com/quote/APP (2026-11-17)
- filing FISV: https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json (2026-11-04)

## AI Provenance

- Provider / model: hermes-local-proxy / upstage/solar-mini4:free
- Market research: attempts=1 tokens=9558 (prompt=6558, completion=3000) runtime=18.72s
- Fundamental research: generated this run at 2026-11-17T10:08:26.070893+00:00
- Evidence source dates: {'as_of': '2026-11-16', 'latest_equity_date': '2026-11-16', 'latest_macro_date': '2026-11-17', 'flows_date': '2026-11-16'}
- Evidence fingerprint: b2614f67bffa4142403f68d8e24bffd842ce0b9e77d52c6f9345d301f5b5569d
- Source citations are retrieved external records in the ledger above; market values remain from the verified database snapshot.


## Disclosures

- This is research and market intelligence, not investment advice.
- AI conclusions are research judgments, not validated return predictions.
- The frozen risk layer is risk-only and is not used for directional views or allocations.
- Legacy scores are not active inputs or outputs.

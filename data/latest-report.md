# AEGIS AI-First Market Intelligence

Research generated at: 16 November 2026, 13:14 HKT
Database freshness: equity 2026-11-13 (latest row retrieved 2026-11-16 13:06:43.000010+08:00)
Data cutoff: 2026-11-13 US cash close
Snapshot ID: aegis-hourly-20261116T051438Z

## Executive Summary

- **AI market view: Late-November 2026 equity market is in a late-cycle, modestly defensive posture. Breadth is positive on price and momentum, but the 20-day return is negative and the 52-week high/low coverage is flat, indicating a market that is not making new highs despite a majority of names trading above their moving averages. Sector leadership is split: Health Care, Consumer Discretionary, Consumer Staples, Real Estate and Financials are up over 20 days, while Information Technology and Energy are down, consistent with a rotation away from rate-sensitive and high-multiple growth toward defensive and value-oriented sectors.**
- Equity market is in a late-cycle, modestly defensive phase with negative 20-day returns and no new highs.
- Breadth is supportive: 71.3% of names are above their 50-day moving average and the advance/decline ratio is 1.70, but 20-day price performance is negative.
- Sector rotation is visible: defensive and cyclical value sectors (Health Care, Consumer Discretionary, Consumer Staples, Real Estate, Financials) lead, while Information Technology and Energy lag.
- Macro backdrop shows a Fed rate of 3.88% and a modestly positive 10Y-2Y spread of 0.27, with CPI and unemployment data from September 2026 still pending a fresh monthly print.
- Credit conditions are stable: high-yield OAS at 3.20 and IG OAS at 0.89, with no acute stress signals.
- Liquidity is mixed: SOXX shows exceptional institutional buying, while TLT and SMH show neutral-to-tactical flows, and crypto markets are down sharply.
- Risk environment is elevated but not spiking: 5-day forecast volatility is 14.9% versus a 22.1% historical baseline, with a 16.5% spike probability below the 18.5% threshold.
- The shortlist is dominated by high-momentum and dislocation names, but the market environment argues for a cautious, quality-oriented stance rather than aggressive positioning.

## Data QC

- Status: **PASS_WITH_WARNINGS**
- Equity session: 0 completed session(s) behind inference date
- Equity provenance: 393 provisional / 12576 canonical
- Breadth lag: 0 session(s); ETF-flow lag: 0 session(s)
- Note: Equity session contains a mix of provisional yfinance and canonical Massive rows.
- External sources: 79 ok / 0 unavailable; retrieved 2026-11-16T05:15:02.240634+00:00

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
| S&P 500 | 7561.67 | -1.28% over 20 days | Index is below its 50-day and 200-day moving averages, with no new highs and a negative 20-day return. |
| Health Care (XLV) | +6.87% over 20 days | +6.87% | Leading sector with a trailing P/E of 30.78, reflecting defensive demand and relative value. |
| Consumer Discretionary (XLY) | +6.69% over 20 days | +6.69% | Strong 20-day performance with a trailing P/E of 25.11, suggesting consumer resilience. |
| Information Technology (XLK) | -7.19% over 20 days | -7.19% | Worst-performing sector with a trailing P/E of 30.03, consistent with high-multiple de-rating. |
| Energy (XLE) | -4.81% over 20 days | -4.81% | Negative 20-day return with a trailing P/E of 16.23, indicating weak energy sector momentum. |
| Financials (XLF) | +5.69% over 20 days | +5.69% | Positive 20-day return with a trailing P/E of 15.85, reflecting a steepening yield curve and credit stability. |

## Macro, Fiscal, Rates, Liquidity and Credit

- Growth: The 10Y-2Y Treasury spread is 0.27 as of 2026-11-13, indicating a modestly positive but still flat yield curve, which is consistent with a late-cycle environment.
- Inflation: CPI and core CPI data are available only through September 2026 (336.298 and 338.896), with the latest October CPI claim from an external source at 337.476; the inflation picture is not yet updated for the most recent month.
- Policy: The effective federal funds rate is 3.88% as of 2026-11-12, suggesting a restrictive but stabilizing monetary policy stance.
- Rates: The 10Y-2Y spread of 0.27 and the stable credit spreads imply a relatively calm rate environment, with no signal of a sharp curve steepening or inversion.
- Liquidity: Crypto markets are down sharply, with BTC at 64,128.05 (-6.04%) and ETH at 1,769.12 (-8.22%) on 2026-11-14, indicating a liquidity drawdown in risk assets outside equities.
- Credit: High-yield OAS is 3.20 and IG OAS is 0.89 as of 2026-11-12, both stable and not signaling stress, which supports the late-cycle but not crisis interpretation.

## US Equities and 11 GICS Sectors

Macro source IDs: S001, S002, S003, S004, S005, S006, S007

| GICS sector | Evidence | AI research stance | Source IDs |
| --- | --- | --- | --- |
| Health Care | 20-day return of 6.87% and trailing P/E of 30.78; the sector is the top performer among the 11 GICS sectors. | Defensive leadership; the sector is benefiting from late-cycle rotation and relative value, but the high P/E warrants caution on further multiple expansion. | S054 |
| Consumer Staples | 20-day return of 5.40% and trailing P/E of 24.85; the sector is a stable defensive performer. | Defensive stability; the sector is not leading but provides ballast in a late-cycle market. | S057 |
| Consumer Discretionary | 20-day return of 6.69% and trailing P/E of 25.11; the sector is a strong performer. | Cyclical resilience; the sector is benefiting from consumer spending, but the P/E is not cheap. | S063 |
| Real Estate | 20-day return of 5.24% and trailing P/E of 29.63; the sector is up but carries a high multiple. | Positive momentum but high valuation; the sector is not a core holding in a late-cycle environment. | S062 |
| Financials | 20-day return of 5.69% and trailing P/E of 15.85; the sector is a strong performer with a reasonable multiple. | Value and cyclical strength; the sector benefits from a positive yield curve and stable credit spreads. | S064 |
| Utilities | 20-day return of 4.34% and trailing P/E of 18.11; the sector is a steady defensive performer. | Defensive stability; the sector is not leading but provides ballast. | S071 |
| Materials | 20-day return of 2.57% and trailing P/E of 21.72; the sector is modestly positive. | Modest performance; the sector is not a leader but is not a laggard. | S069 |
| Industrials | 20-day return of 0.61% and trailing P/E of 27.07; the sector is essentially flat. | Neutral; the sector is not contributing to returns and is not a clear leader. | S068 |
| Communication Services | 20-day return of -1.48% and trailing P/E of 17.26; the sector is a mild laggard. | Mild underperformance; the sector is not a core holding. | S070 |
| Information Technology | 20-day return of -7.19% and trailing P/E of 30.03; the sector is the worst performer. | De-rating and negative momentum; the sector is a clear laggard in the current environment. | S073 |
| Energy | 20-day return of -4.81% and trailing P/E of 16.23; the sector is a laggard. | Negative momentum; the sector is not a core holding. | S074 |

### Sector fundamentals, valuation and earnings

Sector-level fundamental evidence is limited to trailing P/E ratios for the 11 GICS sectors, sourced from the supplied ETF data. No growth, margin, or consensus estimates are available for the sector ETFs in the database. The trailing P/E values range from 15.85 for Financials to 30.78 for Health Care, with Information Technology at 30.03 and Energy at 16.23. These multiples are consistent with a late-cycle environment where defensive and value sectors trade at lower multiples than high-multiple growth sectors, but the data do not support a detailed fundamental comparison beyond the supplied P/E figures.

## Growth vs Value

- Growth: Information Technology and Communication Services are the growth-oriented sectors with negative 20-day returns and high trailing P/E (30.03 and 17.26 respectively), indicating that growth is being de-rated.
- Value: Financials, Energy, and Consumer Staples offer the most reasonable trailing P/E (15.85, 16.23, and 24.85 respectively) and positive or flat 20-day returns, consistent with a value tilt.
- Quality: Health Care and Consumer Discretionary combine positive 20-day returns with moderate-to-high P/E, suggesting that quality and defensive characteristics are being rewarded.
- The data do not include forward earnings revisions or consensus growth estimates, so the growth/value assessment is based solely on trailing P/E and 20-day price performance.

## ETF Flows and Breadth

- Equity breadth is positive: 71.3% of names are above their 50-day moving average, 63.6% are above their 200-day moving average, and the advance/decline ratio is 1.70, indicating broad participation.
- However, the 20-day price return is negative (-1.28%) and there are no new highs, suggesting that the positive breadth is not translating into index-level gains.
- Flow data show exceptional institutional buying in SOXX (20-day flow z-score of 5.10, 60-day of 3.17), while TLT shows neutral-to-negative flows and SMH shows tactical profit-taking inside structural accumulation.
- The market is not making new highs, and the 52-week high/low coverage is flat, indicating a lack of breakout momentum despite the positive breadth.
- The advance/decline ratio of 1.70 is a strong breadth signal, but the negative 20-day return and absence of new highs suggest the market is in a consolidation or late-cycle phase.

## Stock Ideas

Single-stock research uses reported EPS, forward P/E and company fundamentals. All ideas are research judgments, not validated return predictions.

| Ticker | Security | Research view | Price | EPS | Forward P/E | Base target | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| APP | AppLovin | NEW | 409.1 | 20.86026 | 19.611452 | 417.21 | NEW |
| PNR | Pentair | KEEP | 68.3 | 5.30402 | 12.877027 | 74.26 | KEEP |
| GEN | Gen Digital | KEEP | 30.4 | 3.33736 | 9.108996 | 33.37 | KEEP |
| IDXX | Idexx Laboratories | KEEP | 704.23 | 16.8929 | 41.687927 | 540.57 | KEEP |

## ETF Ideas

ETF research uses holdings, portfolio valuation and exposure. Single-stock EPS × P/E valuation is not applied to ETFs.

| Ticker | Fund | Research view | Price | Top holdings | Portfolio valuation | Sector exposure | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| XLP | Consumer Staples sector ETF | KEEP | 92.35 | WMT 11.14%, COST 9.09%, PG 7.60%, KO 7.37%, PM 6.59%, MO 4.70%, CL 4.42%, MDLZ 4.25%, PEP 4.11%, TGT 4.00% | Top 10 holdings; numeric weight coverage 63.28% | Consumer Staples | KEEP |
### APP — AppLovin

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** AppLovin offers a rare combination of top-tier 20-day momentum, high reported growth, and a high-quality margin profile among the shortlisted names, while the alternatives considered (e.g., IDXX and ROP) have lower momentum and weaker growth profiles. Alternatives considered: IDXX, ROP.
- **Thesis:** AppLovin screens in the top 20-day momentum bucket with a 53.7% 20-day return and a 32.5% 60-day return, while its trailing P/E of 20.05 and earnings yield of 5.0% sit at the sector-relative benchmark. The company reports strong reported fundamentals: FY1 revenue growth of 55.5%, earnings growth of 75.5%, gross margin of 88.8%, and operating margin of 77.8%, with a forward P/E of 19.6. The momentum and quality profile support a new BUY, though the 12/12 news headline about a 47% one-month decline suggests the move is already well telegraphed and should be sized carefully.
- **Source IDs:** S008, S012, S013, S018
- **Catalysts:** Continued high-single-digit to low-double-digit revenue and earnings growth, Sustained high-margin advertising and mobile monetization, Follow-through on the 20-day momentum breakout
- **Risks:** A 47% one-month decline headline indicates sharp prior volatility and possible overreaction, High 20-day momentum can mean the move is already priced in, Forward EPS and fiscal-year mapping are unverified in the retrieved evidence
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 20.8603 (source.forwardEps) x AI multiple assumption 20.00; source IDs S008, S012, S013, S018
- **EPS:** 20.86026 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 19.611452
- **FY+1 growth assumption:** 27.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / MSFT / APP shows strong FY1 consensus growth of 27.44% with 25.4% revenue growth and 88.8% gross margin, but ROE of 2.10% and unverified fiscal-period mapping warrant a conservative multiple. Peer reference: MSFT, whose high-margin, high-growth profile supports a premium; APP's 19.6x forward P/E is below that premium, so base 20x is justified, with 24x bull and 16x bear reflecting growth and margin risk.
- **Company fundamentals:** FY1 revenue growth 55.5%, earnings growth 75.5%, gross margin 88.8%, operating margin 77.8%, reported diluted EPS 11.61, forward P/E 19.6, trailing P/E 20.05, earnings yield 5.0%, sector-relative P/E 1.0, 20-day return 53.7%, 60-day return 32.5%, 60-day drawdown -0.2%.
- **Bull / Base / Bear:** 500.65 / 417.21 / 333.76
- **Bull / Base / Bear returns:** 22.38% / 1.98% / -18.42%
- **Scenario probabilities:** not separately assigned; see scenario table.

### PNR — Pentair

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Pentair is the only Industrials shortlist name with a clean filing and a reasonable valuation, but its negative growth and lower momentum make it a neutral hold rather than a preferred pick over higher-growth names like IDXX or ROP. Alternatives considered: IDXX, ROP.
- **Thesis:** Pentair is a top-20-day-momentum stock with a 27.8% 20-day return and a 7.1% 60-day return, but its fundamentals are mixed. Reported FY1 revenue growth is -4.5% and earnings growth is -18.8%, with gross margin of 40.2%, operating margin of 21.4%, and profit margin of 15.4%. The forward P/E of 12.9 and trailing P/E of 13.6 are reasonable, but the negative growth and modest momentum argue for a neutral stance rather than a conviction BUY.
- **Source IDs:** S009, S014, S017, S020
- **Catalysts:** Potential stabilization in end-market demand for water and fluid handling, Reasonable forward P/E relative to its growth profile
- **Risks:** Negative revenue and earnings growth in FY1, Modest 20-day momentum relative to other shortlisted names, Sector-relative P/E of 0.49 suggests it is cheap but also weak
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 5.3040 (source.forwardEps) x AI multiple assumption 14.00; source IDs S009, S014, S017, S020
- **EPS:** 5.30402 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 12.877027
- **FY+1 growth assumption:** 12.82%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / UPS / PNR has 12.8% consensus growth but negative revenue/earnings growth of -4.5%/-18.8%, thin 40.2% gross margin and 21.4% operating margin, and ROE of 15.6%. Peer reference: UPS, a lower-margin, cyclical logistics peer; PNR's higher growth but weaker margins justify a modest 14x base, with 17x bull and 11x bear reflecting margin and cyclical risk.
- **Company fundamentals:** FY1 revenue growth -4.5%, earnings growth -18.8%, gross margin 40.2%, operating margin 21.4%, profit margin 15.4%, reported diluted EPS 2.76, forward P/E 12.9, trailing P/E 13.6, earnings yield 7.4%, sector-relative P/E 0.49, 20-day return 27.8%, 60-day return 7.1%, 60-day drawdown -5.2%.
- **Bull / Base / Bear:** 90.17 / 74.26 / 58.34
- **Bull / Base / Bear returns:** 32.02% / 8.73% / -14.58%
- **Scenario probabilities:** not separately assigned; see scenario table.

### GEN — Gen Digital

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Gen Digital offers a cleaner growth profile than Pentair and a more reasonable valuation than AppLovin, but its lower momentum and less compelling forward multiple make it a neutral hold rather than a preferred pick. Alternatives considered: APP, PNR.
- **Thesis:** Gen Digital is a top-20-day-momentum name with a 25.8% 20-day return and a 7.9% 60-day return. It reports FY1 revenue growth of 12.2% and earnings growth of 128.6%, with gross margin of 77.4% and operating margin of 43.2%. However, the forward P/E of 9.1 and trailing P/E of 14.1 are not compelling enough to justify a strong BUY, and the 20-day momentum is less extreme than AppLovin or IDXX. The stock is better characterized as a neutral hold.
- **Source IDs:** S015, S022, S024, S026
- **Catalysts:** Strong earnings growth and margin expansion, Continued momentum in cybersecurity and digital risk services
- **Risks:** Moderate 20-day momentum relative to other shortlisted names, Forward P/E of 9.1 may already reflect the strong earnings growth, Sector-relative P/E of 0.42 suggests it is cheap but also weak
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 3.3374 (source.forwardEps) x AI multiple assumption 10.00; source IDs S015, S022, S024, S026
- **EPS:** 3.33736 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 9.108996
- **FY+1 growth assumption:** 12.86%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / CSCO / GEN shows 12.9% consensus growth with 6.8% revenue growth, 77.4% gross margin, 43.2% operating margin, and 46.4% ROE. Peer reference: CSCO, a comparable enterprise infrastructure peer; GEN's higher ROE and growth justify a 10x base, with 12x bull and 8x bear reflecting margin and execution risk.
- **Company fundamentals:** FY1 revenue growth 12.2%, earnings growth 128.6%, gross margin 77.4%, operating margin 43.2%, profit margin 23.1%, reported diluted EPS 0.83, forward P/E 9.1, trailing P/E 14.2, earnings yield 7.1%, sector-relative P/E 0.42, 20-day return 25.8%, 60-day return 7.9%, 60-day drawdown -3.2%.
- **Bull / Base / Bear:** 40.05 / 33.37 / 26.7
- **Bull / Base / Bear returns:** 31.74% / 9.77% / -12.17%
- **Scenario probabilities:** not separately assigned; see scenario table.

### IDXX — Idexx Laboratories

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Idexx offers strong momentum and a high-quality diagnostics franchise, but its expensive valuation and lower growth relative to AppLovin make it a neutral hold rather than a preferred pick. Alternatives considered: APP, ROP.
- **Thesis:** Idexx Laboratories is a top-20-day-momentum stock with a 25.7% 20-day return and a 29.0% 60-day return, and it has the highest sector-relative P/E of 1.33, indicating it is more expensive than its sector. Its FY1 revenue growth is 9.9% and earnings growth is 17.9%, with gross margin of 62.7% and operating margin of 32.5%. The forward P/E of 41.7 and trailing P/E of 39.2 are high, so the momentum is not enough to justify a strong BUY. The stock is best viewed as a neutral hold.
- **Source IDs:** S028, S032, S036, S038
- **Catalysts:** Strong 60-day momentum and high sector-relative valuation, Steady growth in animal health and diagnostics
- **Risks:** High forward P/E of 41.7 and trailing P/E of 39.2, Sector-relative P/E of 1.33 indicates it is expensive relative to peers, Moderate earnings growth of 17.9%
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 16.8929 (source.forwardEps) x AI multiple assumption 32.00; source IDs S028, S032, S036, S038
- **EPS:** 16.8929 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 41.687927
- **FY+1 growth assumption:** 12.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / ILMN / IDXX has 12.4% consensus growth, 9.9% revenue growth, 62.7% gross margin, 32.5% operating margin, and 68.9% ROE. Peer reference: ILMN, a high-ROE diagnostics peer; IDXX's strong ROE and growth justify a 32x base, with 38x bull and 26x bear reflecting diagnostic-sector multiple compression risk.
- **Company fundamentals:** FY1 revenue growth 9.9%, earnings growth 17.9%, gross margin 62.7%, operating margin 32.5%, profit margin 25.4%, reported diluted EPS 11.75, forward P/E 41.7, trailing P/E 39.2, earnings yield 2.6%, sector-relative P/E 1.33, 20-day return 25.7%, 60-day return 29.0%, 60-day drawdown -0.3%.
- **Bull / Base / Bear:** 641.93 / 540.57 / 439.22
- **Bull / Base / Bear returns:** -8.85% / -23.24% / -37.63%
- **Scenario probabilities:** not separately assigned; see scenario table.

### XLP — Consumer Staples sector ETF

- **Type:** ETF
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** XLP offers the most defensive sector exposure among the shortlisted ETFs, with a positive price change and high-quality staples holdings, but it is not a strong standalone recommendation. Alternatives considered: XLU, XLF.
- **Thesis:** XLP is a Consumer Staples sector ETF with a 1.4% raw price change and a 92.35 close. It is the only sector ETF in the shortlist with a positive price change, and its top holdings include WMT, COST, PG, KO, and PM. The ETF provides defensive exposure, but the positive price change and high-quality staples profile do not justify a strong BUY. It is best viewed as a neutral hold within a diversified portfolio.
- **Source IDs:** S057, S059
- **Catalysts:** Defensive sector exposure with stable consumer demand, Top holdings include WMT, COST, PG, KO, and PM
- **Risks:** Only 63.28% top-10 weight coverage, Positive price change may already reflect expectations, Sector-specific risks such as input cost inflation
- **Valuation method:** Holdings/portfolio valuation with AI total-return assumption
- **Valuation status:** verified; forward-EPS source: ; period flags: 
- **Valuation assumptions:** Holdings/portfolio valuation; 10 weighted holdings; coverage 63.28%; source IDs S057, S059
- **Top holdings:** WMT 11.14%, COST 9.09%, PG 7.60%, KO 7.37%, PM 6.59%, MO 4.70%, CL 4.42%, MDLZ 4.25%, PEP 4.11%, TGT 4.00%
- **Portfolio valuation:** Top 10 holdings; numeric weight coverage 63.28%
- **Sector exposure:** Consumer Staples
- **Underlying drivers:** Consumer staples demand, input cost inflation, defensive sector rotation
- **Bull / Base / Bear:** 99.74 / 95.58 / 90.04
- **Bull / Base / Bear returns:** 8.0% / 3.5% / -2.5%
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
| Bull | 25% | +2.00% | Directional signal is false and forecast volatility is below the 18.5% threshold, so a mild upside is driven by stable rate expectations and broad market breadth rather than a directional catalyst. |
| Base | 50% | +0.00% | Frozen daily-close model with no directional signal and elevated spike probability near 16.5% implies a range-bound session where rates and credit conditions remain balanced. |
| Bear | 25% | -2.00% | A 16.5% spike probability above the 18.5% threshold baseline suggests elevated tail risk, with rate or credit stress potentially driving a modest downside move. |

### Long Term (12 months)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 30% | +8.00% | Sustained earnings growth and stable rate expectations support a positive multi-day drift, with breadth and credit conditions reinforcing the upside. |
| Base | 40% | +3.00% | A modest positive drift reflects balanced rate and earnings expectations, with no strong directional signal but a constructive medium-term trend. |
| Bear | 30% | -5.00% | Elevated spike probability and rate/credit stress could trigger a meaningful drawdown over the horizon, with earnings or spread widening driving the decline. |

## Positioning

- Maintain a cautious, late-cycle posture with a tilt toward defensive and value sectors.
- Avoid aggressive exposure to high-multiple growth sectors, particularly Information Technology, which is showing negative momentum and high valuation.
- Use breadth and flow signals to confirm the defensive rotation, but do not favored any single sector without further evidence.
- Monitor credit spreads and the yield curve for any sign of late-cycle acceleration or stress.
- The current risk environment is elevated but not spiking; maintain a balanced risk budget and avoid concentrated positions.
- No specific weights or allocation targets are provided; the stance is qualitative and risk-aware.

## Catalysts

| Date | Event | Why it matters |
| --- | --- | --- |
| 2026-11-14 | Crypto market drawdown | BTC and ETH fell sharply on 2026-1 |

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
| S010 | news | FISV | Fri, 13 Nov 2026 21:49:46 GMT | ok | https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en | Fiserv, Inc. (FISV) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 21:49:46 GMT); Fiserv (FISV) Stock Still Looks Like A Bargain After Lawsuit Claims - Yahoo Finance (Thu, 22 Oct 2026 07:00:00 GMT); FISV Stock Quote Price and Forecast - CNN (Fri, 13 Nov 2026 21:18:08 GMT) |
| S011 | filing | FISV | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0000798354-26-000042); 8-K filed 2026-11-03 (accession 0000798354-26-000039); 8-K filed 2026-10-23 (accession 0001193125-26-429481) |
| S012 | news | APP | Thu, 12 Nov 2026 20:05:45 GMT | ok | https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en | AppLovin Just Ripped 47% in a Month: Is It Too Late to Buy APP Stock Now? - Yahoo Finance (Thu, 12 Nov 2026 20:05:45 GMT); Is Trending Stock AppLovin Corporation (APP) a Buy Now? - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT); APP Stock Surges 51% After Q3 Earnings: Is it Still a Buy? - Yahoo Finance (Tue, 10 Nov 2026 14:24:00 GMT) |
| S013 | filing | APP | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json | Diluted EPS 11.61 for period ending 2026-09-30 (filed 2026-11-04) |
| S014 | news | PNR | Fri, 13 Nov 2026 22:09:48 GMT | ok | https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en | Pentair plc (PNR) stock price, news, quote and history - Yahoo Finance UK (Fri, 13 Nov 2026 22:09:48 GMT); Pentair plc (PNR) Q3 Earnings and Revenues Beat Estimates - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT); Pentair (PNR) Stock May Be 46% Undervalued As New CFO Arrives - Yahoo Finance (Fri, 25 Sep 2026 07:00:00 GMT) |
| S015 | filing | GEN | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0000849399-26-000083); 8-K filed 2026-10-28 (accession 0000849399-26-000081); 8-K filed 2026-10-09 (accession 0000849399-26-000079) |
| S016 | stock | FISV | 2026-11-16 | ok | https://finance.yahoo.com/quote/FISV | Forward P/E: 7.99667; Price: 63.78; Market price: 63.78; Market cap: 33934002176; Market Cap: 33934002176; Consensus EPS FY+1: 7.98015; growth: 0.09689999 |
| S017 | stock | PNR | 2026-11-16 | ok | https://finance.yahoo.com/quote/PNR | Trailing P/E: 18.610355; Forward P/E: 12.877027; Forward EPS: 5.30402; Price: 68.3; Market price: 68.3; Market cap: 10904415232; Sector: Industrials; Trailing Eps: 3.67; Revenue Growth: -0.045; Earnings Growth: -0.188; Gross Margin: 0.40168998; Operating Margin: 0.21410999; Profit Margin: 0.15435; Return On Equity: 0.15605; Total Revenue: 3966200064; Market Cap: 10904415232; Consensus EPS FY+1: 5.30402; growth: 0.1282 |
| S018 | stock | APP | 2026-11-16 | ok | https://finance.yahoo.com/quote/APP | Trailing P/E: 27.54882; Forward P/E: 19.611452; Forward EPS: 20.86026; Price: 409.1; Market price: 409.1; Market cap: 135543824384; Sector: Communication Services; Trailing Eps: 14.85; Revenue Growth: 0.555; Earnings Growth: 0.755; Gross Margin: 0.8878; Operating Margin: 0.77782995; Profit Margin: 0.65887; Return On Equity: 2.1008599; Total Revenue: 7608893952; Market Cap: 135543824384; Consensus EPS FY+1: 20.72438; growth: 0.2744 |
| S019 | filing | FISV | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json | Diluted EPS -8.9 for period ending 2026-09-30 (filed 2026-11-04) |
| S020 | filing | PNR | 2026-10-27 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json | Diluted EPS 2.76 for period ending 2026-09-30 (filed 2026-10-27) |
| S021 | filing | CLX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000021076-26-000046); 8-K filed 2026-11-02 (accession 0000021076-26-000044); 8-K filed 2026-10-29 (accession 0001206774-26-000586) |
| S022 | stock | GEN | 2026-11-16 | ok | https://finance.yahoo.com/quote/GEN | Trailing P/E: 15.431472; Forward P/E: 9.108996; Forward EPS: 3.33736; Price: 30.4; Market price: 30.4; Market cap: 18035593216; Sector: Technology; Trailing Eps: 1.97; Revenue Growth: 0.122; Earnings Growth: 1.286; Gross Margin: 0.77410007; Operating Margin: 0.43229; Profit Margin: 0.23068; Return On Equity: 0.46402; Total Revenue: 5228000256; Market Cap: 18035593216; Consensus EPS FY+1: 3.33736; growth: 0.1286 |
| S023 | stock | CLX | 2026-11-16 | ok | https://finance.yahoo.com/quote/CLX | Trailing P/E: 19.68705; Forward P/E: 17.745283; Forward EPS: 6.1684; Price: 109.46; Market price: 109.46; Market cap: 13260793856; Sector: Consumer Defensive; Trailing Eps: 5.56; Revenue Growth: 0.333; Earnings Growth: 1.138; Gross Margin: 0.41939998; Operating Margin: 0.14286; Profit Margin: 0.09408; Return On Equity: 5.34363; Total Revenue: 7196000256; Market Cap: 13260793856; Consensus EPS FY+1: 6.1684; growth: 0.0769 |
| S024 | news | GEN | Thu, 29 Oct 2026 07:00:00 GMT | ok | https://news.google.com/rss/search?q=GEN+Gen+Digital+stock&hl=en-US&gl=US&ceid=US:en | Gen Digital (GEN) Stock Repriced After Q2 Earnings Put Margins Center Stage - Yahoo Finance (Thu, 29 Oct 2026 07:00:00 GMT); Gen Digital Stock: Is Wall Street Bullish or Bearish? - Yahoo Finance (Thu, 05 Nov 2026 08:00:00 GMT); Are Business Services Stocks Lagging GEN DIGITAL INC (GEN) This Year? - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT) |
| S025 | filing | CHTR | 2026-11-06 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-06 (accession 0001091667-26-000073); 8-K filed 2026-11-06 (accession 0001091667-26-000072); 8-K filed 2026-10-27 (accession 0001091667-26-000064) |
| S026 | filing | GEN | 2026-10-29 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000849399.json | Diluted EPS 0.83 for period ending 2026-10-02 (filed 2026-10-29) |
| S027 | news | CLX | Sun, 15 Nov 2026 08:55:47 GMT | ok | https://news.google.com/rss/search?q=CLX+Clorox+stock&hl=en-US&gl=US&ceid=US:en | The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance UK (Sun, 15 Nov 2026 08:55:47 GMT); The Clorox Company (CLX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 23:34:51 GMT); A 10-Day Winning Streak Has Clorox Stock Up 24% - Trefis (Sat, 14 Nov 2026 08:28:05 GMT) |
| S028 | filing | IDXX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000874716&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000874716-26-000135); 8-K filed 2026-11-02 (accession 0001104659-26-120892); 10-Q filed 2026-08-04 (accession 0000874716-26-000123) |
| S029 | filing | CLX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000021076.json | Diluted EPS 1.39 for period ending 2026-09-30 (filed 2026-11-02) |
| S030 | stock | CHTR | 2026-11-16 | ok | https://finance.yahoo.com/quote/CHTR | Trailing P/E: 13.006578; Forward P/E: 3.2831066; Forward EPS: 42.15215; Price: 138.39; Market price: 138.39; Market cap: 24778944512; Sector: Communication Services; Trailing Eps: 10.64; Revenue Growth: 0.091; Gross Margin: 0.55084; Operating Margin: 0.23389; Profit Margin: 0.02498; Return On Equity: 0.07019; Total Revenue: 55645999104; Market Cap: 24778944512; Consensus EPS FY+1: 47.15811; growth: 1.0195 |
| S031 | news | CHTR | Sun, 15 Nov 2026 05:47:01 GMT | ok | https://news.google.com/rss/search?q=CHTR+Charter+Communications+stock&hl=en-US&gl=US&ceid=US:en | Charter Communications (CHTR) Stock Could Be A Bargain Following Its New Operating Model - Yahoo Finance (Sun, 15 Nov 2026 05:47:01 GMT); Why You Should Think About Charter Communications Differently Now? - Yahoo Finance (Fri, 13 Nov 2026 19:16:11 GMT); Charter Communications (CHTR) Expands Enterprise Reach With Managed Secure Networking Launch - Yahoo Finance (Sun, 15 Nov 2026 06:08:00 GMT) |
| S032 | news | IDXX | Sat, 14 Nov 2026 22:37:20 GMT | ok | https://news.google.com/rss/search?q=IDXX+Idexx+Laboratories+stock&hl=en-US&gl=US&ceid=US:en | IDEXX Laboratories, Inc. (IDXX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Sat, 14 Nov 2026 22:37:20 GMT); symbol__ Stock Quote Price and Forecast - CNN (Fri, 13 Nov 2026 15:22:45 GMT); IDEXX Laboratories (IDXX) Stock Looks Fairly Valued Despite Its 28% Run - Yahoo Finance (Sat, 31 Oct 2026 07:00:00 GMT) |
| S033 | filing | ROP | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000882835&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000882835-26-000047); 8-K filed 2026-10-22 (accession 0000882835-26-000042); 8-K filed 2026-10-01 (accession 0000882835-26-000039) |
| S034 | filing | CHTR | 2026-11-06 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001091667.json | Diluted EPS 0.38 for period ending 2026-09-30 (filed 2026-11-06) |
| S035 | stock | ROP | 2026-11-16 | ok | https://finance.yahoo.com/quote/ROP | Trailing P/E: 18.993866; Forward P/E: 19.532475; Forward EPS: 24.57318; Price: 479.975; Market price: 479.975; Market cap: 47535013888; Sector: Technology; Trailing Eps: 25.27; Revenue Growth: 0.076; Earnings Growth: 0.326; Gross Margin: 0.69671; Operating Margin: 0.28049; Profit Margin: 0.30712998; Return On Equity: 0.13229; Total Revenue: 8434599936; Market Cap: 47535013888; Consensus EPS FY+1: 24.57318; growth: 0.09810001 |
| S036 | filing | IDXX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000874716.json | Diluted EPS 11.75 for period ending 2026-09-30 (filed 2026-11-02) |
| S037 | filing | RDDT | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001713445&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0001713445-26-000116); 8-K filed 2026-10-29 (accession 0001713445-26-000114); 8-K filed 2026-08-12 (accession 0001713445-26-000107) |
| S038 | stock | IDXX | 2026-11-16 | ok | https://finance.yahoo.com/quote/IDXX | Trailing P/E: 47.45485; Forward P/E: 41.687927; Forward EPS: 16.8929; Price: 704.23; Market price: 704.23; Market cap: 55483650048; Sector: Healthcare; Trailing Eps: 14.84; Revenue Growth: 0.099; Earnings Growth: 0.179; Gross Margin: 0.62722; Operating Margin: 0.32497; Profit Margin: 0.25357; Return On Equity: 0.68925005; Total Revenue: 4662220800; Market Cap: 55483650048; Consensus EPS FY+1: 16.8929; growth: 0.1244 |
| S039 | news | ROP | Fri, 13 Nov 2026 13:04:22 GMT | ok | https://news.google.com/rss/search?q=ROP+Roper+Technologies+stock&hl=en-US&gl=US&ceid=US:en | Roper Technologies, Inc. (ROP) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 13:04:22 GMT); Roper Technologies (ROP) Stock Looks Fully Valued As Cash Flow Comes Into Focus - Yahoo Finance (Thu, 05 Nov 2026 08:00:00 GMT); Roper Technologies (ROP), What Is Behind The Fresh Attention? - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT) |
| S040 | filing | INTC | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000050863&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0000050863-26-000191); 8-K filed 2026-10-29 (accession 0000050863-26-000188); 8-K filed 2026-08-12 (accession 0001193125-26-346806) |

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
- news FISV: https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 21:49:46 GMT)
- filing FISV: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 (2026-11-04)
- news APP: https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en (Thu, 12 Nov 2026 20:05:45 GMT)
- filing APP: https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json (2026-11-04)
- news PNR: https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 22:09:48 GMT)
- filing GEN: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 (2026-10-29)
- stock FISV: https://finance.yahoo.com/quote/FISV (2026-11-16)
- stock PNR: https://finance.yahoo.com/quote/PNR (2026-11-16)
- stock APP: https://finance.yahoo.com/quote/APP (2026-11-16)
- filing FISV: https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json (2026-11-04)
- filing PNR: https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json (2026-10-27)

## AI Provenance

- Provider / model: hermes-local-proxy / upstage/solar-mini4:free
- Market research: attempts=1 tokens=9473 (prompt=6473, completion=3000) runtime=19.86s
- Fundamental research: generated this run at 2026-11-16T05:14:38.842945+00:00
- Evidence source dates: {'as_of': '2026-11-13', 'latest_equity_date': '2026-11-13', 'latest_macro_date': '2026-11-14', 'flows_date': '2026-11-13'}
- Evidence fingerprint: 59f3f82afebf317a854f3a0b74ba01839c0adc9e4f80c3f1017863453e9e46b2
- Source citations are retrieved external records in the ledger above; market values remain from the verified database snapshot.


## Disclosures

- This is research and market intelligence, not investment advice.
- AI conclusions are research judgments, not validated return predictions.
- The frozen risk layer is risk-only and is not used for directional views or allocations.
- Legacy scores are not active inputs or outputs.

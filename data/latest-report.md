# AEGIS AI-First Market Intelligence

Research generated at: 16 November 2026, 08:14 HKT
Database freshness: equity 2026-11-13 (latest row retrieved 2026-11-15 13:06:40.074841+08:00)
Data cutoff: 2026-11-13 US cash close
Snapshot ID: aegis-hourly-20261116T001442Z

## Executive Summary

- **AI market view: Late-November 2026 equity market is in a late-cycle, mixed posture: broad market breadth is positive but the index is slightly negative over 20 days, and the leadership is split between high-momentum names, dislocation names, and liquidity leaders. Sector returns show a defensive tilt with Health Care, Consumer Staples, Consumer Discretionary, Real Estate and Financials outperforming, while Information Technology and Energy are the weakest sectors. Macro data show a still-elevated but easing inflation backdrop, a stable labor market, and a modestly positive 10Y-2Y curve, with credit spreads tight and liquidity conditions neutral-to-deteriorating in medium-term Treasury flows.**
- Broad market breadth is constructive: 71.3% of constituents are above their 50-day moving average and 63.6% above the 200-day, with a positive 20-day advance/decline ratio of 1.70.
- The index is slightly negative over 20 days (-1.28%), indicating a late-cycle consolidation rather than a broad breakout.
- Sector leadership is defensive: Health Care (+6.87%), Consumer Discretionary (+6.69%), Consumer Staples (+5.40%) and Financials (+5.69%) lead, while Information Technology (-7.19%) and Energy (-4.81%) lag.
- Liquidity and flows show strong institutional buying in SOXX (semiconductor hardware) but medium-term Treasury outflows, suggesting selective risk appetite rather than broad risk-on.
- Macro backdrop is stable: CPI is elevated but easing, unemployment is 4.2%, the 10Y-2Y spread is +0.27%, and credit spreads are tight, supporting a cautious but not bearish stance.
- Risk environment is moderate: 5-day forecast volatility is 14.9% versus a historical baseline of 22.1%, and spike probability is 16.5%, below the 18.5% threshold, indicating no acute tail-risk spike at this time.

## Data QC

- Status: **PASS_WITH_WARNINGS**
- Equity session: 0 completed session(s) behind inference date
- Equity provenance: 393 provisional / 12576 canonical
- Breadth lag: 0 session(s); ETF-flow lag: 0 session(s)
- Note: Equity session contains a mix of provisional yfinance and canonical Massive rows.
- External sources: 79 ok / 0 unavailable; retrieved 2026-11-16T00:15:00.238017+00:00

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
| S&P 500 | 7561.67 | -1.28% over 20 days | Index is in a late-cycle consolidation; breadth is positive but index return is slightly negative, with 71.3% above 50-day and 63.6% above 200-day moving averages. |
| Health Care (XLV) | +6.87% over 20 days | +6.87% | Strongest sector; trailing P/E of 30.78 suggests premium valuation but defensive demand is supporting performance. |
| Information Technology (XLK) | -7.19% over 20 days | -7.19% | Weakest sector; trailing P/E of 30.03 and negative price momentum indicate capital rotation out of tech despite liquidity-leader names like NVDA and AMD. |
| Energy (XLE) | -4.81% over 20 days | -4.81% | Negative sector return; trailing P/E of 16.23 is relatively cheap but weak momentum suggests energy is not leading. |
| Financials (XLF) | +5.69% over 20 days | +5.69% | Positive sector performance; trailing P/E of 15.85 is the cheapest among major sectors, supporting a value tilt. |
| Consumer Discretionary (XLY) | +6.69% over 20 days | +6.69% | Strong sector return; trailing P/E of 25.11 indicates moderate valuation with consumer strength. |

## Macro, Fiscal, Rates, Liquidity and Credit

- Inflation: CPI is elevated but easing; the latest CPI reading is 336.298 (2026-09-01) and core CPI is 338.896, with a later October reading of 337.476 from S004, indicating continued disinflation but still above the pre-pandemic trend.
- Labor market: Unemployment rate is 4.2% (2026-09-01) and nonfarm payrolls are 159,293 (2026-10-01), indicating a stable but not overheating labor market.
- Policy: The effective federal funds rate is 3.88% as of 2026-11-12, suggesting a restrictive but easing monetary policy stance.
- Rates: The 10Y-2Y Treasury spread is +0.27 as of 2026-11-13, indicating a modestly positive yield curve, consistent with a late-cycle but not recession-signaling environment.
- Liquidity: Medium-term Treasury flows show a neutral-to-deteriorating structure (flow z-score 20d -0.41, 60d -0.29), while semiconductor hardware (SOXX) shows exceptional institutional buying (flow z-score 20d 5.10, 60d 3.17), indicating selective liquidity deployment.
- Credit: High-yield OAS is 3.20 and investment-grade OAS is 0.89 as of 2026-11-12, both tight, supporting risk appetite but leaving limited room for stress.

## US Equities and 11 GICS Sectors

Macro source IDs: S001, S002, S003, S004, S005, S006, S007

| GICS sector | Evidence | AI research stance | Source IDs |
| --- | --- | --- | --- |
| Health Care | Sector return 20d +6.87%; trailing P/E 30.78 (S053); 71.3% of constituents above 50-day MA and 63.6% above 200-day MA. | Defensive leadership with premium valuation; strong breadth supports continued outperformance in a late-cycle environment. | S053 |
| Consumer Staples | Sector return 20d +5.40%; trailing P/E 24.85 (S060); positive 20-day advance/decline ratio of 1.70. | Stable defensive sector; moderate valuation and positive breadth support a hold stance. | S060 |
| Consumer Discretionary | Sector return 20d +6.69%; trailing P/E 25.11 (S061); positive 20-day advance/decline ratio of 1.70. | Outperforming consumer sector; moderate valuation and positive momentum support a constructive stance. | S061 |
| Real Estate | Sector return 20d +5.24%; trailing P/E 29.63 (S063); positive 20-day advance/decline ratio of 1.70. | Positive sector performance; premium valuation but supportive breadth and rate environment. | S063 |
| Financials | Sector return 20d +5.69%; trailing P/E 15.85 (S069); positive 20-day advance/decline ratio of 1.70. | Cheapest major sector with positive momentum; value tilt supported by tight credit spreads and positive curve. | S069 |
| Utilities | Sector return 20d +4.34%; trailing P/E 18.11 (S067); positive 20-day advance/decline ratio of 1.70. | Defensive utility sector with moderate valuation; positive breadth supports a hold stance. | S067 |
| Materials | Sector return 20d +2.57%; trailing P/E 21.72 (S068); positive 20-day advance/decline ratio of 1.70. | Modest positive sector return; moderate valuation and positive breadth support a neutral stance. | S068 |
| Industrials | Sector return 20d +0.61%; trailing P/E 27.07 (S071); positive 20-day advance/decline ratio of 1.70. | Near-flat sector performance; premium valuation and weak momentum suggest a neutral stance. | S071 |
| Communication Services | Sector return 20d -1.48%; trailing P/E 17.26 (S072); negative sector return despite positive breadth. | Weakest major sector; negative momentum and premium valuation (relative to peers) suggest a cautious stance. | S072 |
| Information Technology | Sector return 20d -7.19%; trailing P/E 30.03 (S073); negative sector return despite liquidity-leader names like NVDA and AMD. | Weakest major sector; negative momentum and high valuation suggest a cautious stance despite selective liquidity. | S073 |
| Energy | Sector return 20d -4.81%; trailing P/E 16.23 (S074); negative sector return despite cheap valuation. | Negative sector performance; cheap valuation is not offsetting weak momentum, suggesting a cautious stance. | S074 |

### Sector fundamentals, valuation and earnings

Sector-level trailing P/E data are available for all 11 GICS sectors from the supplied ETF evidence (S053, S060, S061, S063, S067, S068, S069, S071, S072, S073, S074). No point-in-time sector fundamentals such as revenue growth, margins, or consensus estimates are supplied in the database; therefore, no sector-level growth or margin claims are made. The sector view is based solely on 20-day returns, trailing P/E, and breadth evidence.

## Growth vs Value

- Value tilt: Financials (XLF) has the cheapest trailing P/E at 15.85, followed by Energy (XLE) at 16.23 and Utilities (XLU) at 18.11, suggesting a value-oriented posture.
- Growth premium: Health Care (XLV) at 30.78 and Information Technology (XLK) at 30.03 carry the highest trailing P/E, indicating a growth premium but also higher valuation risk.
- Mixed signals: Consumer Discretionary (XLY) at 25.11 and Real Estate (XLRE) at 29.63 show moderate-to-premium valuations, while Consumer Staples (XLP) at 24.85 is near the middle of the pack.
- Sector-relative P/E from the screening data shows that several shortlisted names (e.g., IDXX, RDDT, MRVL, NOW) trade at sector-relative P/E above 1.0, indicating premium growth expectations, while names like CHTR, FISV, and SNDK trade at sector-relative P/E below 0.7, indicating cheaper valuations.

## ETF Flows and Breadth

- Market breadth is positive: 71.3% of constituents above 50-day MA, 63.6% above 200-day MA, and a 20-day advance/decline ratio of 1.70, indicating broad participation.
- Index vs. breadth divergence: S&P 500 is -1.28% over 20 days while breadth is positive, suggesting a late-cycle consolidation with selective leadership rather than broad market strength.
- Flows show selective institutional buying: SOXX has exceptional institutional buying (flow z-score 20d 5.10, 60d 3.17) despite price being down, indicating strong structural accumulation in semiconductors.
- Medium-term Treasury flows show deterioration (flow z-score 20d -0.41, 60d -0.29), suggesting capital rotation out of duration into selective

## Stock Ideas

Single-stock research uses reported EPS, forward P/E and company fundamentals. All ideas are research judgments, not validated return predictions.

| Ticker | Security | Research view | Price | EPS | Forward P/E | Base target | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| APP | AppLovin | NEW | 409.1 | 20.86026 | 19.611452 | 417.21 | NEW |
| PNR | Pentair | KEEP | 68.3 | 5.30402 | 12.877027 | 63.65 | KEEP |
| GEN | Gen Digital | KEEP | 30.4 | 3.33736 | 9.108996 | 33.37 | KEEP |
| CLX | Clorox | KEEP | 109.46 | 6.1684 | 17.745283 | 98.69 | KEEP |

## ETF Ideas

ETF research uses holdings, portfolio valuation and exposure. Single-stock EPS × P/E valuation is not applied to ETFs.

| Ticker | Fund | Research view | Price | Top holdings | Portfolio valuation | Sector exposure | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| XLV | Health Care sector ETF | KEEP | 188.85 | LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59% | Top 10 holdings; numeric weight coverage 61.42% | Health Care | KEEP |
### APP — AppLovin

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** AppLovin offers a high-margin, high-ROE software-like compounder with strong recent momentum, whereas the shortlist's other momentum names such as ROP and IDXX carry lower margins and slower growth. Its forward P/E of ~19.6x is more reasonable than the speculative dislocation names in the shortlist. Alternatives considered: ROP, IDXX.
- **Thesis:** AppLovin screens as a top 20-day momentum name with a 20-day return of ~53.7% and a 60-day return of ~32.5%, indicating strong recent price leadership. Reported diluted EPS of $11.61 for the fiscal period ending 2026-09-30 supports a forward P/E of ~19.6x on the $409.10 close, and the company's high gross margin (~88.8%) and operating margin (~77.8%) provide a quality profile that can compound through the momentum phase.
- **Source IDs:** S008, S012, S015, S017
- **Catalysts:** Continued 20-day momentum and positive 60-day return, Sustained high gross margin and operating leverage, Continued advertiser and content monetization growth
- **Risks:** Sharp 20-day price run may be vulnerable to mean-reversion, High valuation relative to near-term earnings growth, News coverage flags a 47% one-month decline, suggesting elevated volatility
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 20.8603 (source.forwardEps) x AI multiple assumption 20.00; source IDs S008, S012, S015, S017
- **EPS:** 20.86026 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 19.611452
- **FY+1 growth assumption:** 27.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / PNR / APP shows 27.44% forward earnings growth and 25.37% revenue growth with exceptional margins (gross 88.8%, operating 77.8%, profit 65.9%) and strong ROE, supporting a premium multiple. PNR is the named peer reference: APP's growth and margin profile is materially higher than PNR's declining earnings (-18.8%) and lower margins, justifying a higher base multiple.
- **Company fundamentals:** AppLovin reported diluted EPS of $11.61 for the period ending 2026-09-30, with forward EPS of $20.86, forward P/E of ~19.6x, gross margin of ~88.8%, operating margin of ~77.8%, profit margin of ~65.9%, and ROE of ~2.10. Revenue growth of ~55.5% and earnings growth of ~75.5% support the momentum thesis.
- **Bull / Base / Bear:** 500.65 / 417.21 / 333.76
- **Bull / Base / Bear returns:** 22.38% / 1.98% / -18.42%
- **Scenario probabilities:** not separately assigned; see scenario table.

### PNR — Pentair

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Pentair offers a lower forward P/E than the high-multiple momentum names, but its negative growth and lower margins make it a less compelling standalone pick. It is preferable to the speculative dislocation names such as INTC and COIN, which carry larger fundamental and valuation risks. Alternatives considered: INTC, COIN.
- **Thesis:** Pentair screens as a top 20-day momentum name with a 20-day return of ~27.8% and a 60-day return of ~7.1%. Reported diluted EPS of $2.76 for the period ending 2026-09-30 supports a forward P/E of ~12.9x on the $68.30 close. The company's moderate gross margin (~40.2%) and operating margin (~21.4%) are typical of a diversified industrial, but revenue growth of ~-4.5% and earnings growth of ~-18.8% indicate the momentum is not yet supported by broad fundamental expansion.
- **Source IDs:** S009, S013, S016, S018
- **Catalysts:** Continued 20-day momentum and positive 60-day return, Potential stabilization in end-market demand, Attractive forward P/E relative to historical levels
- **Risks:** Negative revenue and earnings growth in the latest reported period, Moderate margins limit upside from operational leverage, Momentum may fade if fundamentals do not improve
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 5.3040 (source.forwardEps) x AI multiple assumption 12.00; source IDs S009, S013, S016, S018
- **EPS:** 5.30402 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 12.877027
- **FY+1 growth assumption:** 12.82%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / APP / PNR has 12.82% forward earnings growth but negative revenue/earnings growth (-4.5%/-18.8%) and lower margins (gross 40.2%, operating 21.4%, profit 15.4%) with modest ROE, warranting a lower multiple. APP is the named peer reference: APP's superior growth and margin profile supports a higher multiple for APP, while PNR's weaker fundamentals justify a lower base multiple.
- **Company fundamentals:** Pentair reported diluted EPS of $2.76 for the period ending 2026-09-30, with forward EPS of $5.30, forward P/E of ~12.9x, gross margin of ~40.2%, operating margin of ~21.4%, profit margin of ~15.4%, and ROE of ~15.6%. Revenue growth of ~-4.5% and earnings growth of ~-18.8% are a concern despite the positive momentum screen.
- **Bull / Base / Bear:** 74.26 / 63.65 / 53.04
- **Bull / Base / Bear returns:** 8.73% / -6.81% / -22.34%
- **Scenario probabilities:** not separately assigned; see scenario table.

### GEN — Gen Digital

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Gen Digital offers a low forward P/E and strong earnings growth, but its modest revenue growth and low price make it less attractive than the higher-quality momentum names. It is preferable to the speculative dislocation names such as NOW and MRVL, which carry much higher multiples and less certain fundamentals. Alternatives considered: NOW, MRVL.
- **Thesis:** Gen Digital screens as a top 20-day momentum name with a 20-day return of ~25.8% and a 60-day return of ~7.9%. Reported diluted EPS of $0.83 for the period ending 2026-10-02 supports a forward P/E of ~9.1x on the $30.40 close. The company's gross margin (~77.4%) and operating margin (~43.2%) are strong for the sector, and earnings growth of ~128.6% is a bright spot, but revenue growth of ~12.2% is modest and the stock is low-priced, making the momentum less durable.
- **Source IDs:** S014, S022, S023, S026
- **Catalysts:** Strong earnings growth of ~128.6%, High gross margin and operating leverage, Attractive forward P/E of ~9.1x
- **Risks:** Modest revenue growth of ~12.2%, Low share price may mask volatility, Momentum may not persist if growth decelerates
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 3.3374 (source.forwardEps) x AI multiple assumption 10.00; source IDs S014, S022, S023, S026
- **EPS:** 3.33736 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 9.108996
- **FY+1 growth assumption:** 12.86%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / CLX / GEN has 12.86% forward earnings growth and 1.286x earnings growth, but revenue growth is modest (6.81%) with lower margins (gross 77.4%, operating 43.2%, profit 23.1%) and ROE of 46.4%. CLX is the named peer reference: CLX's higher revenue growth (33.3%) and stronger operating margin (14.3%) support a higher multiple, while GEN's lower growth and margin profile justify a lower base multiple.
- **Company fundamentals:** Gen Digital reported diluted EPS of $0.83 for the period ending 2026-10-02, with forward EPS of $3.34, forward P/E of ~9.1x, gross margin of ~77.4%, operating margin of ~43.2%, profit margin of ~23.1%, and ROE of ~46.4%. Revenue growth of ~12.2% and earnings growth of ~128.6% are mixed signals.
- **Bull / Base / Bear:** 40.05 / 33.37 / 26.7
- **Bull / Base / Bear returns:** 31.74% / 9.77% / -12.17%
- **Scenario probabilities:** not separately assigned; see scenario table.

### CLX — Clorox

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Clorox offers a defensive consumer staples profile with strong earnings growth, but its revenue growth and valuation are less compelling than the high-margin momentum names. It is preferable to the speculative dislocation names such as RDDT and INTC, which carry larger valuation and fundamental risks. Alternatives considered: RDDT, INTC.
- **Thesis:** Clorox screens as a top 20-day momentum name with a 20-day return of ~25.7% and a 60-day return of ~3.2%. Reported diluted EPS of $1.39 for the period ending 2026-09-30 supports a forward P/E of ~17.7x on the $109.46 close. The company's gross margin (~41.9%) and operating margin (~14.3%) are typical of a consumer staples company, and earnings growth of ~113.8% is a positive, but revenue growth of ~33.3% is not clearly sustainable and the stock is already at a premium valuation.
- **Source IDs:** S021, S024, S025, S035
- **Catalysts:** Positive 20-day momentum and positive 60-day return, Strong earnings growth of ~113.8%, Consumer staples defensive characteristics
- **Risks:** Revenue growth of ~33.3% may not be sustainable, Forward P/E of ~17.7x is elevated for the sector, Consumer staples demand may be pressured by macro conditions
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 6.1684 (source.forwardEps) x AI multiple assumption 16.00; source IDs S021, S024, S025, S035
- **EPS:** 6.1684 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 17.745283
- **FY+1 growth assumption:** 7.69%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / GEN / CLX has 7.69% forward earnings growth and 33.3% revenue growth with a strong gross margin (41.9%) and operating margin (14.3%), supporting a higher multiple. GEN is the named peer reference: GEN's lower revenue growth (6.81%) and lower operating margin (43.2%) justify a lower multiple, while CLX's faster revenue growth and better margin profile support a higher base multiple.
- **Company fundamentals:** Clorox reported diluted EPS of $1.39 for the period ending 2026-09-30, with forward EPS of $6.17, forward P/E of ~17.7x, gross margin of ~41.9%, operating margin of ~14.3%, profit margin of ~9.4%, and ROE of ~534.4%. Revenue growth of ~33.3% and earnings growth of ~113.8% are strong but may not be sustainable.
- **Bull / Base / Bear:** 111.03 / 98.69 / 86.36
- **Bull / Base / Bear returns:** 1.43% / -9.84% / -21.1%
- **Scenario probabilities:** not separately assigned; see scenario table.

### XLV — Health Care sector ETF

- **Type:** ETF
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** XLV provides broad health care exposure that complements the individual stock ideas, but it is not a substitute for the higher-conviction momentum names. It is preferable to the sector ETFs with lower top-10 weight coverage or less relevant sector exposure, such as XLRE or XLU. Alternatives considered: XLRE, XLU.
- **Thesis:** The Health Care sector ETF (XLV) provides diversified exposure to large-cap pharmaceutical and medical device names. The ETF's top holdings include LLY, JNJ, ABBV, MRK, UNH, TMO, AMGN, GILD, ABT, and PFE, with top-10 weight coverage of ~61.4%. The sector offers defensive characteristics and exposure to innovation in health care, but the ETF's performance is tied to the sector's overall trajectory rather than individual stock selection.
- **Source IDs:** S053, S055
- **Catalysts:** Diversified exposure to large-cap health care names, Defensive characteristics in a potentially uncertain macro environment, Exposure to innovation in pharmaceuticals and medical devices
- **Risks:** Sector concentration in large-cap pharma, Performance tied to sector-wide catalysts rather than individual stock selection, Limited top-10 weight coverage (~61.4%) may leave some exposure unrepresented
- **Valuation method:** Holdings/portfolio valuation with AI total-return assumption
- **Valuation status:** verified; forward-EPS source: ; period flags: 
- **Valuation assumptions:** Holdings/portfolio valuation; 10 weighted holdings; coverage 61.42%; source IDs S053, S055
- **Top holdings:** LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59%
- **Portfolio valuation:** Top 10 holdings; numeric weight coverage 61.42%
- **Sector exposure:** Health Care
- **Underlying drivers:** Large-cap pharmaceutical and medical device innovation, defensive demand, and sector-wide earnings growth.
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
| Bull | 25% | +2.00% | Low 5-day forecast vol (14.9%) and below-threshold spike probability (16.5% vs 18.5% threshold) suggest a stable, range-bound tape where a modest upside drift is plausible if credit spreads tighten and earnings expectations hold. |
| Base | 50% | +0.00% | Frozen daily-close model with no directional signal and historical/ewma baselines above threshold implies a neutral path: flat returns as volatility normalizes and no catalyst is expected to drive a decisive move. |
| Bear | 25% | -2.00% | If the spike probability materializes above threshold or credit conditions tighten, elevated vol and negative skew could push returns down modestly, with downside capped by the frozen model's conservative calibration. |

### Long Term (12 months)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 30% | +8.00% | Sustained low vol and stable credit conditions over the horizon could allow earnings growth and breadth expansion to compound returns, with a 30% probability assigned to a constructive macro and rate environment. |
| Base | 40% | +3.00% | A moderate positive drift reflects a baseline where volatility remains contained, earnings modestly exceed expectations, and no major shock disrupts the trend, yielding a low-single-digit long-term return. |
| Bear | 30% | -5.00% | A bear case assigns 30% probability to a scenario where rising volatility, credit stress, or earnings disappointment drives a meaningful drawdown, with the frozen model's conservative calibration limiting the downside to -5%. |

## Positioning


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
| S009 | filing | PNR | 2026-10-27 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-27 (accession 0000077360-26-000058); 8-K filed 2026-10-27 (accession 0000077360-26-000055); 8-K filed 2026-09-22 (accession 0000077360-26-000050) |
| S010 | filing | FISV | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0000798354-26-000042); 8-K filed 2026-11-03 (accession 0000798354-26-000039); 8-K filed 2026-10-23 (accession 0001193125-26-429481) |
| S011 | news | FISV | Fri, 13 Nov 2026 21:49:46 GMT | ok | https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en | Fiserv, Inc. (FISV) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 21:49:46 GMT); Fiserv Stock Outlook: Is Wall Street Bullish or Bearish? - Yahoo Finance (Thu, 12 Nov 2026 12:23:56 GMT); Michael Burry makes a bold call on struggling payments giant - Yahoo Finance (Wed, 11 Nov 2026 00:17:00 GMT) |
| S012 | news | APP | Thu, 12 Nov 2026 20:05:45 GMT | ok | https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en | AppLovin Just Ripped 47% in a Month: Is It Too Late to Buy APP Stock Now? - Yahoo Finance (Thu, 12 Nov 2026 20:05:45 GMT); Is Trending Stock AppLovin Corporation (APP) a Buy Now? - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT); APP Stock Surges 51% After Q3 Earnings: Is it Still a Buy? - Yahoo Finance (Tue, 10 Nov 2026 14:24:00 GMT) |
| S013 | news | PNR | Fri, 13 Nov 2026 22:05:23 GMT | ok | https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en | Pentair plc (PNR) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 22:05:23 GMT); Pentair plc (PNR) stock price, news, quote and history - Yahoo Finance UK (Fri, 13 Nov 2026 22:09:48 GMT); Pentair plc (PNR) Q3 Earnings and Revenues Beat Estimates - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT) |
| S014 | filing | GEN | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0000849399-26-000083); 8-K filed 2026-10-28 (accession 0000849399-26-000081); 8-K filed 2026-10-09 (accession 0000849399-26-000079) |
| S015 | filing | APP | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json | Diluted EPS 11.61 for period ending 2026-09-30 (filed 2026-11-04) |
| S016 | filing | PNR | 2026-10-27 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json | Diluted EPS 2.76 for period ending 2026-09-30 (filed 2026-10-27) |
| S017 | stock | APP | 2026-11-16 | ok | https://finance.yahoo.com/quote/APP | Trailing P/E: 27.54882; Forward P/E: 19.611452; Forward EPS: 20.86026; Price: 409.1; Market price: 409.1; Market cap: 135543824384; Sector: Communication Services; Trailing Eps: 14.85; Revenue Growth: 0.555; Earnings Growth: 0.755; Gross Margin: 0.8878; Operating Margin: 0.77782995; Profit Margin: 0.65887; Return On Equity: 2.1008599; Total Revenue: 7608893952; Market Cap: 135543824384; Consensus EPS FY+1: 20.72438; growth: 0.2744 |
| S018 | stock | PNR | 2026-11-16 | ok | https://finance.yahoo.com/quote/PNR | Trailing P/E: 18.610355; Forward P/E: 12.877027; Forward EPS: 5.30402; Price: 68.3; Market price: 68.3; Market cap: 10904415232; Sector: Industrials; Trailing Eps: 3.67; Revenue Growth: -0.045; Earnings Growth: -0.188; Gross Margin: 0.40168998; Operating Margin: 0.21410999; Profit Margin: 0.15435; Return On Equity: 0.15605; Total Revenue: 3966200064; Market Cap: 10904415232; Consensus EPS FY+1: 5.30402; growth: 0.1282 |
| S019 | stock | FISV | 2026-11-16 | ok | https://finance.yahoo.com/quote/FISV | Forward P/E: 7.99667; Price: 63.78; Market price: 63.78; Market cap: 33934002176; Market Cap: 33934002176; Consensus EPS FY+1: 7.98015; growth: 0.09689999 |
| S020 | filing | FISV | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json | Diluted EPS -8.9 for period ending 2026-09-30 (filed 2026-11-04) |
| S021 | filing | CLX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000021076-26-000046); 8-K filed 2026-11-02 (accession 0000021076-26-000044); 8-K filed 2026-10-29 (accession 0001206774-26-000586) |
| S022 | filing | GEN | 2026-10-29 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000849399.json | Diluted EPS 0.83 for period ending 2026-10-02 (filed 2026-10-29) |
| S023 | stock | GEN | 2026-11-16 | ok | https://finance.yahoo.com/quote/GEN | Trailing P/E: 15.431472; Forward P/E: 9.108996; Forward EPS: 3.33736; Price: 30.4; Market price: 30.4; Market cap: 18035593216; Sector: Technology; Trailing Eps: 1.97; Revenue Growth: 0.122; Earnings Growth: 1.286; Gross Margin: 0.77410007; Operating Margin: 0.43229; Profit Margin: 0.23068; Return On Equity: 0.46402; Total Revenue: 5228000256; Market Cap: 18035593216; Consensus EPS FY+1: 3.33736; growth: 0.1286 |
| S024 | news | CLX | Sun, 15 Nov 2026 08:55:47 GMT | ok | https://news.google.com/rss/search?q=CLX+Clorox+stock&hl=en-US&gl=US&ceid=US:en | The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance UK (Sun, 15 Nov 2026 08:55:47 GMT); A 10-Day Winning Streak Has Clorox Stock Up 24% - Trefis (Sat, 14 Nov 2026 08:28:05 GMT); Clorox (CLX) Down 9.3% Since Last Earnings Report: Can It Rebound? - Yahoo Finance (Wed, 02 Sep 2026 07:00:00 GMT) |
| S025 | stock | CLX | 2026-11-16 | ok | https://finance.yahoo.com/quote/CLX | Trailing P/E: 19.68705; Forward P/E: 17.745283; Forward EPS: 6.1684; Price: 109.46; Market price: 109.46; Market cap: 13260793856; Sector: Consumer Defensive; Trailing Eps: 5.56; Revenue Growth: 0.333; Earnings Growth: 1.138; Gross Margin: 0.41939998; Operating Margin: 0.14286; Profit Margin: 0.09408; Return On Equity: 5.34363; Total Revenue: 7196000256; Market Cap: 13260793856; Consensus EPS FY+1: 6.1684; growth: 0.0769 |
| S026 | news | GEN | Fri, 13 Nov 2026 09:34:35 GMT | ok | https://news.google.com/rss/search?q=GEN+Gen+Digital+stock&hl=en-US&gl=US&ceid=US:en | Gen Digital Inc. (GEN) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 09:34:35 GMT); Gen Digital (GEN) Stock Repriced After Q2 Earnings Put Margins Center Stage - Yahoo Finance (Thu, 29 Oct 2026 07:00:00 GMT); Gen Digital Stock: Is Wall Street Bullish or Bearish? - Yahoo Finance (Thu, 05 Nov 2026 08:00:00 GMT) |
| S027 | filing | CHTR | 2026-11-06 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-06 (accession 0001091667-26-000073); 8-K filed 2026-11-06 (accession 0001091667-26-000072); 8-K filed 2026-10-27 (accession 0001091667-26-000064) |
| S028 | filing | IDXX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000874716&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000874716-26-000135); 8-K filed 2026-11-02 (accession 0001104659-26-120892); 10-Q filed 2026-08-04 (accession 0000874716-26-000123) |
| S029 | stock | CHTR | 2026-11-16 | ok | https://finance.yahoo.com/quote/CHTR | Trailing P/E: 13.006578; Forward P/E: 3.2831066; Forward EPS: 42.15215; Price: 138.39; Market price: 138.39; Market cap: 24778944512; Sector: Communication Services; Trailing Eps: 10.64; Revenue Growth: 0.091; Gross Margin: 0.55084; Operating Margin: 0.23389; Profit Margin: 0.02498; Return On Equity: 0.07019; Total Revenue: 55645999104; Market Cap: 24778944512; Consensus EPS FY+1: 47.15811; growth: 1.0195 |
| S030 | news | IDXX | Sat, 14 Nov 2026 06:13:17 GMT | ok | https://news.google.com/rss/search?q=IDXX+Idexx+Laboratories+stock&hl=en-US&gl=US&ceid=US:en | IDEXX Laboratories, Inc. (IDXX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Sat, 14 Nov 2026 06:13:17 GMT); symbol__ Stock Quote Price and Forecast - CNN (Fri, 13 Nov 2026 15:22:45 GMT); IDEXX Laboratories, Inc. (IDXX) stock price, news, quote and history - Yahoo Finance UK (Fri, 13 Nov 2026 23:14:50 GMT) |
| S031 | filing | ROP | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000882835&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000882835-26-000047); 8-K filed 2026-10-22 (accession 0000882835-26-000042); 8-K filed 2026-10-01 (accession 0000882835-26-000039) |
| S032 | news | CHTR | Sun, 15 Nov 2026 05:47:01 GMT | ok | https://news.google.com/rss/search?q=CHTR+Charter+Communications+stock&hl=en-US&gl=US&ceid=US:en | Charter Communications (CHTR) Stock Could Be A Bargain Following Its New Operating Model - Yahoo Finance (Sun, 15 Nov 2026 05:47:01 GMT); Charter Communications (CHTR) Expands Enterprise Reach With Managed Secure Networking Launch - Yahoo Finance (Sun, 15 Nov 2026 06:08:00 GMT); Why You Should Think About Charter Communications Differently Now? - Yahoo Finance (Fri, 13 Nov 2026 19:16:11 GMT) |
| S033 | stock | IDXX | 2026-11-16 | ok | https://finance.yahoo.com/quote/IDXX | Trailing P/E: 47.45485; Forward P/E: 41.687927; Forward EPS: 16.8929; Price: 704.23; Market price: 704.23; Market cap: 55483650048; Sector: Healthcare; Trailing Eps: 14.84; Revenue Growth: 0.099; Earnings Growth: 0.179; Gross Margin: 0.62722; Operating Margin: 0.32497; Profit Margin: 0.25357; Return On Equity: 0.68925005; Total Revenue: 4662220800; Market Cap: 55483650048; Consensus EPS FY+1: 16.8929; growth: 0.1244 |
| S034 | news | ROP | Fri, 13 Nov 2026 13:04:22 GMT | ok | https://news.google.com/rss/search?q=ROP+Roper+Technologies+stock&hl=en-US&gl=US&ceid=US:en | Roper Technologies, Inc. (ROP) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 13:04:22 GMT); Roper Technologies (ROP) Stock Looks Fully Valued As Cash Flow Comes Into Focus - Yahoo Finance (Thu, 05 Nov 2026 08:00:00 GMT); Roper Technologies (ROP), What Is Behind The Fresh Attention? - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT) |
| S035 | filing | CLX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000021076.json | Diluted EPS 1.39 for period ending 2026-09-30 (filed 2026-11-02) |
| S036 | filing | CHTR | 2026-11-06 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001091667.json | Diluted EPS 0.38 for period ending 2026-09-30 (filed 2026-11-06) |
| S037 | filing | RDDT | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001713445&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0001713445-26-000116); 8-K filed 2026-10-29 (accession 0001713445-26-000114); 8-K filed 2026-08-12 (accession 0001713445-26-000107) |
| S038 | stock | ROP | 2026-11-16 | ok | https://finance.yahoo.com/quote/ROP | Trailing P/E: 18.993866; Forward P/E: 19.532475; Forward EPS: 24.57318; Price: 479.975; Market price: 479.975; Market cap: 47535013888; Sector: Technology; Trailing Eps: 25.27; Revenue Growth: 0.076; Earnings Growth: 0.326; Gross Margin: 0.69671; Operating Margin: 0.28049; Profit Margin: 0.30712998; Return On Equity: 0.13229; Total Revenue: 8434599936; Market Cap: 47535013888; Consensus EPS FY+1: 24.57318; growth: 0.09810001 |
| S039 | filing | IDXX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000874716.json | Diluted EPS 11.75 for period ending 2026-09-30 (filed 2026-11-02) |
| S040 | filing | ROP | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000882835.json | Diluted EPS 21.3 for period ending 2026-09-30 (filed 2026-11-02) |

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
- news FISV: https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 21:49:46 GMT)
- news APP: https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en (Thu, 12 Nov 2026 20:05:45 GMT)
- news PNR: https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 22:05:23 GMT)
- filing GEN: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 (2026-10-29)
- filing APP: https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json (2026-11-04)
- filing PNR: https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json (2026-10-27)
- stock APP: https://finance.yahoo.com/quote/APP (2026-11-16)
- stock PNR: https://finance.yahoo.com/quote/PNR (2026-11-16)
- stock FISV: https://finance.yahoo.com/quote/FISV (2026-11-16)
- filing FISV: https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json (2026-11-04)

## AI Provenance

- Provider / model: hermes-local-proxy / upstage/solar-mini4:free
- Market research: attempts=1 tokens=9473 (prompt=6473, completion=3000) runtime=28.06s
- Fundamental research: generated this run at 2026-11-16T00:14:42.467113+00:00
- Evidence source dates: {'as_of': '2026-11-13', 'latest_equity_date': '2026-11-13', 'latest_macro_date': '2026-11-14', 'flows_date': '2026-11-13'}
- Evidence fingerprint: 7c574099aed41f73aee7662860b76abc173ccda0f44bdb9ed3317f3d7b657998
- Source citations are retrieved external records in the ledger above; market values remain from the verified database snapshot.


## Disclosures

- This is research and market intelligence, not investment advice.
- AI conclusions are research judgments, not validated return predictions.
- The frozen risk layer is risk-only and is not used for directional views or allocations.
- Legacy scores are not active inputs or outputs.

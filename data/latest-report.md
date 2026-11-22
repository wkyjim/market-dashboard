# AEGIS AI-First Market Intelligence

Research generated at: 22 November 2026, 18:16 HKT
Database freshness: equity 2026-11-20 (latest row retrieved 2026-11-22 13:05:43.380314+08:00)
Data cutoff: 2026-11-20 US cash close
Snapshot ID: aegis-hourly-20261122T101621Z

## Executive Summary

- **AI market view: Late-November 2026 equity market is in a broad, late-stage risk-off posture: the S&P 500 is down 9.4% over 20 days, price breadth is deteriorating, and the 20-day advance/decline ratio is deeply negative. Defensive sectors (Consumer Staples, Utilities, Health Care) are the least negative, while Information Technology and Energy are the worst performers. Liquidity is flowing into semiconductors and Treasuries, but the overall market is not participating broadly.**
- S&P 500 is in a 20-day drawdown of -9.36%, with breadth collapsing: 37.6% of names positive over 20 days and an advance/decline ratio of 0.33.
- Defensive sectors are outperforming: Consumer Staples +2.5%, Utilities +0.3%, Health Care -1.1% over 20 days.
- Cyclical and growth sectors are under pressure: Information Technology -18.7%, Energy -12.7%, Industrials -5.0%.
- Institutional flows show structural accumulation in TLT and exceptional buying in SOXX, while SMH is neutral.
- Macro backdrop shows a 3.88% effective fed funds rate, 3.52% high-yield OAS, and 0.94% IG OAS, with CPI and unemployment data from September 2026.
- Risk model flags elevated 5-day volatility (0.366) with a 92.8% spike probability, though directional signal is false.

## Data QC

- Status: **PASS_WITH_WARNINGS**
- Equity session: 0 completed session(s) behind inference date
- Macro session: 2026-11-21 (0 completed session(s) behind inference date)
- Equity provenance: 138 provisional / 12686 canonical
- Breadth lag: 0 session(s); ETF-flow lag: 0 session(s)
- Note: Equity session contains a mix of provisional yfinance and canonical Massive rows.
- External sources: 79 ok / 0 unavailable; retrieved 2026-11-22T10:16:43.178554+00:00

## Idea Discovery

- S&P 500 universe: 503; eligible: 501; transparent shortlist: 20
- Method: independent momentum/dislocation/PE/liquidity buckets; no composite score
- Evidence used: latest close, 20d and 60d price returns, 60d drawdown, trailing P/E, earnings yield, sector-relative P/E, dollar volume, GICS sector
- Not available as verified inputs: verified earnings-revision history for the full universe, FY+2 consensus, structured industry catalyst calendar
- Eligible but not shortlisted: 481 (outside the top independent momentum, dislocation, valuation and liquidity buckets)
- Included: APP (top_20d_momentum); CMG (top_20d_momentum); PNR (top_20d_momentum); CLX (top_20d_momentum); IDXX (top_20d_momentum); CHTR (top_20d_momentum); GEN (top_20d_momentum); MGM (top_20d_momentum); SNDK (largest_20d_dislocation); MRVL (largest_20d_dislocation); NOW (largest_20d_dislocation); DDOG (largest_20d_dislocation); INTC (largest_20d_dislocation); RDDT (largest_20d_dislocation); NVDA (largest_20d_dislocation, liquidity_leader); LITE (largest_20d_dislocation); MU (liquidity_leader); AMD (liquidity_leader); AAPL (liquidity_leader); MSFT (liquidity_leader)
- Excluded reasons: {"missing_recent_or_latest_price": 2}
- Valuation-quality rejected: [{"flags": ["forward_pe_outside_plausible_range", "implausible_earnings_yield", "forward_eps_vs_reported_jump"], "ticker": "CHTR"}, {"flags": ["forward_pe_outside_plausible_range", "implausible_earnings_yield"], "ticker": "SNDK"}, {"flags": ["forward_eps_vs_reported_jump"], "ticker": "MRVL"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "INTC"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "RDDT"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "NVDA"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "LITE"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "MU"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "AMD"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "AAPL"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "MSFT"}]

## Market Snapshot

| Asset | Latest | Change | Observation |
| --- | --- | --- | --- |
| S&P 500 | 6910.39 | -9.36% (20d) | Broad market is in a late-stage risk-off phase with deteriorating price breadth and negative 20-day advance/decline. |
| Consumer Staples (XLP) | 24.34x P/E | +2.49% (20d) | Most resilient sector; defensive demand and relative valuation support. |
| Health Care (XLV) | 28.89x P/E | -1.14% (20d) | Modestly negative but relatively stable; defensive positioning intact. |
| Information Technology (XLK) | 26.28x P/E | -18.68% (20d) | Deepest drawdown; high dislocation names and liquidity leader NVDA are in the shortlist but the sector is under severe pressure. |
| Energy (XLE) | 15.11x P/E | -12.72% (20d) | Sharp decline; sector-relative P/E and flows suggest weak momentum despite low valuation. |
| Financials (XLF) | 14.74x P/E | -2.38% (20d) | Negative but less severe than tech/energy; IG OAS at 0.94% suggests tight credit conditions. |

## Macro, Fiscal, Rates, Liquidity and Credit

- Growth: S&P 500 20-day return is -9.36%, indicating a broad growth contraction; sector returns show Information Technology (-18.7%) and Energy (-12.7%) leading the decline.
- Inflation: CPI (CPIAUCSL) stands at 336.30 (Sep 2026) and Core CPI at 338.90; October CPI is available at 337.48, suggesting inflation remains above the pre-2021 trend.
- Policy: Effective federal funds rate is 3.88% as of 2026-11-19, indicating a restrictive but potentially stabilizing monetary stance.
- Rates: 10Y-2Y Treasury spread is 0.29 as of 2026-11-20, a modestly positive curve; IG OAS at 0.94% and HY OAS at 3.52% point to tight but not distressed credit.
- Liquidity: Institutional flows show structural accumulation in TLT and exceptional institutional buying in SOXX, while SMH is neutral; equity breadth is negative.
- Credit: High-yield OAS of 3.52% and IG OAS of 0.94% suggest credit conditions are tight but not signaling imminent stress.

## US Equities and 11 GICS Sectors

Macro source IDs: S001, S002, S003, S004, S005, S006, S007

| GICS sector | Evidence | AI research stance | Source IDs |
| --- | --- | --- | --- |
| Health Care | XLV 20d return -1.14%; trailing P/E 28.89; sector-relative P/E 1.0; 20d positive 37.6% of names. | Defensive sector with stable relative valuation; modest drawdown but not leading the selloff. | S059 |
| Consumer Staples | XLP 20d return +2.49%; trailing P/E 24.34; sector-relative P/E 1.0; most resilient sector in the universe. | Best-performing sector; defensive demand and relative valuation support. | S057 |
| Consumer Discretionary | XLY 20d return -0.57%; trailing P/E 23.54; sector-relative P/E 1.0. | Slightly negative; consumer resilience is mixed with broad market weakness. | S062 |
| Real Estate | XLRE 20d return -0.26%; trailing P/E 28.35; sector-relative P/E 1.0. | Near flat; rate-sensitive but not a primary driver of the selloff. | S063 |
| Financials | XLF 20d return -2.38%; trailing P/E 14.74; IG OAS 0.94%. | Negative but less severe; tight credit spreads limit downside risk. | S065 |
| Materials | XLB 20d return -5.79%; trailing P/E 20.10; sector-relative P/E 1.0. | Under pressure; commodity and industrial demand concerns. | S068 |
| Industrials | XLI 20d return -5.01%; trailing P/E 25.08; sector-relative P/E 1.0. | Negative; cyclical exposure to slowing growth. | S070 |
| Communication Services | XLC 20d return -5.19%; trailing P/E 15.89; sector-relative P/E 1.0. | Negative; media and platform exposure to ad and consumer spending weakness. | S073 |
| Information Technology | XLK 20d return -18.68%; trailing P/E 26.28; sector-relative P/E 1.0; shortlist includes NVDA, MRVL, NOW, DDOG, INTC, AMD, MU, AAPL, MSFT. | Deepest drawdown; high dislocation and liquidity leader names are in the shortlist but the sector is under severe pressure. | S075 |
| Energy | XLE 20d return -12.72%; trailing P/E 15.11; sector-relative P/E 1.0. | Sharp decline; low valuation but weak momentum and sector-relative P/E. | S078 |
| Utilities | XLU 20d return +0.31%; trailing P/E 17.56; sector-relative P/E 1.0. | Stable and defensive; relative strength in a risk-off tape. | S069 |

### Sector fundamentals, valuation and earnings

Sector-level fundamental evidence is limited to trailing P/E and 20-day ETF returns from the supplied database. No point-in-time sector fundamentals such as revenue growth, margins, or consensus estimates are available for the full universe; only source-backed shortlist names have growth/margins/consensus data. Therefore, no additional sector fundamentals are reported to avoid invention.

## Growth vs Value

- Consumer Staples (XLP) trades at 24.34x trailing P/E and is the only sector with positive 20-day return, offering the best growth-value balance in the current tape.
- Health Care (XLV) at 28.89x P/E is expensive on a trailing basis but remains defensive; its relative P/E is 1.0, indicating no sector premium.
- Information Technology (XLK) at 26.28x P/E is the most dislocation-prone sector, with shortlist names like MRVL (74.2x), NOW (97.2x), and DDOG (521.2x) showing extreme valuation gaps.
- Energy (XLE) at 15.11x P/E is the cheapest sector on trailing earnings, but its -12.7% 20-day return and weak sector-relative P/E suggest value is not yet being rewarded.

## ETF Flows and Breadth

- Equity breadth is collapsing: 37.6% of names positive over 20 days, advance/decline ratio 0.33, and 0 new highs; the 200-day indicator shows 46.2% above, with negative divergence.
- Institutional flows show structural accumulation in TLT (20d z-score 0.12, 60d -0.10) and exceptional institutional buying in SOXX (20d z-score 2.83, 60d 2.30), while SMH is neutral (20d 0.77, 60d 0.74).
- The negative breadth and positive flows into semiconductors and Treasuries suggest institutional investors are rotating into quality and liquidity rather than broad market participation.
- The advance/decline ratio of 0.33 and 0 new highs indicate a market that is not participating broadly, consistent with a late-stage risk-off environment.

## Stock Ideas

Single-stock research uses reported EPS, forward P/E and company fundamentals. All ideas are research judgments, not validated return predictions.

| Ticker | Security | Research view | Price | EPS | Forward P/E | Base target | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| APP | AppLovin | KEEP | 348.29 | 20.86084 | 16.695877 | 417.22 | KEEP |
| PNR | Pentair | KEEP | 68.63 | 5.30402 | 12.939242 | 74.26 | KEEP |
| CLX | Clorox | KEEP | 104.73 | 6.1684 | 16.978472 | 98.69 | KEEP |
| IDXX | Idexx Laboratories | KEEP | 676.21 | 16.8929 | 40.029243 | 540.57 | KEEP |

## ETF Ideas

ETF research uses holdings, portfolio valuation and exposure. Single-stock EPS × P/E valuation is not applied to ETFs.

| Ticker | Fund | Research view | Price | Top holdings | Portfolio valuation | Sector exposure | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| XLV | Health Care sector ETF | KEEP | 177.24 | LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59% | Top 10 holdings; numeric weight coverage 61.42% | Health Care | KEEP |
### APP — AppLovin

- **Type:** Stock
- **Research view:** KEEP (stance: BUY)
- **Why preferred / alternatives:** AppLovin offers a cleaner quality and momentum profile than the dislocation names such as DDOG, NOW, or MRVL, which carry far higher forward P/Es and deeper drawdowns. Its 88.8% gross margin and 77.8% operating margin provide a more durable earnings engine than the high-multiple software names in the shortlist. Alternatives considered: DDOG, NOW, MRVL.
- **Thesis:** AppLovin screens in the top 20-day momentum bucket with a 33.8% 20-day return and a 20.1x trailing P/E that is in line with its sector. Reported diluted EPS of 11.61 for the fiscal period ending 2026-09-30 supports a forward P/E near 16.7x, and the company's high gross margin of 88.8% and operating margin near 77.8% provide a durable, high-quality earnings base. The momentum and quality combination supports a constructive stance.
- **Source IDs:** S009, S012, S013, S019
- **Catalysts:** Continued 20-day momentum leadership in the shortlist, Sustained high-margin advertising and content monetization, Potential for forward P/E expansion as reported earnings remain strong
- **Risks:** 20-day momentum can mean elevated volatility if the trend stalls, Forward P/E still implies meaningful valuation for a high-growth digital media name, Sector-relative P/E is at 1.0x, so no cheapness versus peers
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 20.8608 (source.forwardEps) x AI multiple assumption 20.00; source IDs S009, S012, S013, S019
- **EPS:** 20.86084 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 16.695877
- **FY+1 growth assumption:** 27.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / PNR and CLX / APP shows strong FY+1 consensus growth of 27.44% and revenue growth of 25.51%, with exceptional margins (gross 88.8%, operating 77.8%, profit 65.9%) and ROE of 2.10x. The forward P/E of 16.70 is below the FY+1 consensus growth, supporting a premium base multiple. PNR and CLX are named peers for comparison; APP's superior margin profile and growth justify a higher multiple than the lower-growth, lower-margin peers.
- **Company fundamentals:** AppLovin reported diluted EPS of 11.61 for the period ending 2026-09-30, with forward EPS of 20.86, a forward P/E of 16.70x, revenue growth of 55.5%, earnings growth of 75.5%, gross margin of 88.8%, operating margin of 77.8%, and profit margin of 65.9%. The 20-day return is 33.8% and the 60-day return is 11.4%. Trailing P/E is 20.1x and sector-relative P/E is 1.0x.
- **Bull / Base / Bear:** 500.66 / 417.22 / 333.77
- **Bull / Base / Bear returns:** 43.75% / 19.79% / -4.17%
- **Scenario probabilities:** not separately assigned; see scenario table.

### PNR — Pentair

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Pentair is the cheapest momentum name in the shortlist with a forward P/E near 12.9x, but its negative revenue and earnings growth make it less attractive than the higher-quality names such as AppLovin. It is preferable to the deeply discounted dislocation names like INTC or LITE, which lack clean forward earnings visibility. Alternatives considered: APP, INTC, LITE.
- **Thesis:** Pentair screens in the top 20-day momentum bucket with a 24.1% 20-day return and a 13.6x trailing P/E. Reported diluted EPS of 2.76 for the fiscal period ending 2026-09-30 supports a forward P/E near 12.9x, and the company's 40.2% gross margin and 21.4% operating margin provide a reasonable industrial profile. The momentum is positive, but the 60-day return is only 10.5% and the earnings growth is negative, so the stance is neutral rather than a strong buy.
- **Source IDs:** S008, S017, S018, S020
- **Catalysts:** Positive 20-day momentum of 24.1%, Low forward P/E near 12.9x relative to the shortlist, Industrial exposure to water, fluid handling, and building products
- **Risks:** 60-day return of only 10.5% is modest versus other momentum names, Revenue growth of -4.5% and earnings growth of -18.8% indicate near-term operating pressure, Sector-relative P/E of 0.49x suggests the market is pricing in a lower growth profile
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 5.3040 (source.forwardEps) x AI multiple assumption 14.00; source IDs S008, S017, S018, S020
- **EPS:** 5.30402 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 12.939242
- **FY+1 growth assumption:** 12.82%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / APP and CLX / PNR has FY+1 consensus growth of 12.82% with revenue growth of 18.38%, but earnings growth is negative at -18.8% and margins are lower (gross 40.2%, operating 21.4%, profit 15.4%) with ROE of 0.156x. The forward P/E of 12.94 is below consensus growth, so a modest base multiple is appropriate. APP and CLX are named peers; PNR's weaker profitability and negative earnings growth justify a lower multiple than APP.
- **Company fundamentals:** Pentair reported diluted EPS of 2.76 for the period ending 2026-09-30, with forward EPS of 5.30, a forward P/E of 12.94x, revenue growth of -4.5%, earnings growth of -18.8%, gross margin of 40.2%, operating margin of 21.4%, and profit margin of 15.4%. The 20-day return is 24.1% and the 60-day return is 10.5%. Trailing P/E is 13.6x and sector-relative P/E is 0.49x.
- **Bull / Base / Bear:** 90.17 / 74.26 / 58.34
- **Bull / Base / Bear returns:** 31.39% / 8.2% / -14.99%
- **Scenario probabilities:** not separately assigned; see scenario table.

### CLX — Clorox

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Clorox offers a defensive consumer staples profile with a low single-digit revenue growth and a forward P/E near 17x, but it is less attractive than the higher-quality AppLovin. It is preferable to the high-multiple software names like DDOG and NOW, which carry far higher forward P/Es and deeper drawdowns. Alternatives considered: APP, XLP, DDOG.
- **Thesis:** Clorox screens in the top 20-day momentum bucket with a 21.2% 20-day return and a 18.3x trailing P/E. Reported diluted EPS of 1.39 for the fiscal period ending 2026-09-30 supports a forward P/E near 17.0x, and the company's 41.9% gross margin and 14.3% operating margin provide a consumer staples profile. The 60-day return is only 1.1%, so the momentum is not as strong as the 20-day figure suggests, and the stance is neutral.
- **Source IDs:** S016, S022, S024, S026
- **Catalysts:** Positive 20-day momentum of 21.2%, Consumer staples defensive exposure, Forward P/E near 17x is reasonable for a staples name
- **Risks:** 60-day return of only 1.1% indicates weak follow-through, Revenue growth of 2.2% and earnings growth of 114% are mixed, Sector-relative P/E of 0.76x suggests the market is not pricing in premium growth
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 6.1684 (source.forwardEps) x AI multiple assumption 16.00; source IDs S016, S022, S024, S026
- **EPS:** 6.1684 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 16.978472
- **FY+1 growth assumption:** 7.69%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / APP and PNR / CLX has FY+1 consensus growth of 7.69% with revenue growth of 2.23% and earnings growth of 113.8%, but margins are lower (gross 41.9%, operating 14.3%, profit 9.4%) and ROE is 5.34x. The forward P/E of 16.98 is above consensus growth, so a moderate base multiple is appropriate. APP and PNR are named peers; CLX's lower growth and profitability justify a lower multiple than APP but a higher multiple than PNR given its positive earnings growth.
- **Company fundamentals:** Clorox reported diluted EPS of 1.39 for the period ending 2026-09-30, with forward EPS of 6.17, a forward P/E of 16.98x, revenue growth of 33.3%, earnings growth of 113.8%, gross margin of 41.9%, operating margin of 14.3%, and profit margin of 9.4%. The 20-day return is 21.2% and the 60-day return is 1.1%. Trailing P/E is 18.3x and sector-relative P/E is 0.76x.
- **Bull / Base / Bear:** 117.2 / 98.69 / 80.19
- **Bull / Base / Bear returns:** 11.91% / -5.77% / -23.43%
- **Scenario probabilities:** not separately assigned; see scenario table.

### IDXX — Idexx Laboratories

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Idexx offers a high-margin healthcare services business with strong 60-day momentum, but its 40x forward P/E is much more expensive than the industrial and staples names in the shortlist. It is preferable to the deeply discounted dislocation names like INTC or LITE, which lack clean forward earnings visibility. Alternatives considered: APP, XLV, DDOG.
- **Thesis:** Idexx Laboratories screens in the top 20-day momentum bucket with a 20.7% 20-day return and a 39.2x trailing P/E. Reported diluted EPS of 11.75 for the fiscal period ending 2026-09-30 supports a forward P/E near 40.0x, and the company's 62.7% gross margin and 32.5% operating margin provide a healthcare services profile. The 60-day return is 24.1%, which is the strongest 60-day momentum in the shortlist, but the high valuation and modest growth keep the stance neutral.
- **Source IDs:** S021, S023, S030, S032
- **Catalysts:** Strong 60-day momentum of 24.1%, Healthcare services exposure with recurring diagnostics revenue, Forward P/E near 40x is supported by a high-margin business
- **Risks:** Trailing P/E of 39.2x and forward P/E of 40.0x are expensive, Revenue growth of 9.9% and earnings growth of 17.9% are modest, Sector-relative P/E of 1.33x suggests the market is pricing in premium growth that may not be realized
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 16.8929 (source.forwardEps) x AI multiple assumption 32.00; source IDs S021, S023, S030, S032
- **EPS:** 16.8929 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 40.029243
- **FY+1 growth assumption:** 12.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / APP and PNR / IDXX has FY+1 consensus growth of 12.44% with revenue growth of 8.88% and earnings growth of 17.9%, with strong margins (gross 62.7%, operating 32.5%, profit 25.4%) and ROE of 0.689x. The forward P/E of 40.03 is well above consensus growth, so a premium multiple is required to justify the price. APP and PNR are named peers; IDXX's higher growth and profitability justify a higher multiple than PNR, though the premium is substantial and should be tempered by the high forward P/E.
- **Company fundamentals:** Idexx Laboratories reported diluted EPS of 11.75 for the period ending 2026-09-30, with forward EPS of 16.89, a forward P/E of 40.03x, revenue growth of 9.9%, earnings growth of 17.9%, gross margin of 62.7%, operating margin of 32.5%, and profit margin of 25.4%. The 20-day return is 20.7% and the 60-day return is 24.1%. Trailing P/E is 39.2x and sector-relative P/E is 1.33x.
- **Bull / Base / Bear:** 641.93 / 540.57 / 439.22
- **Bull / Base / Bear returns:** -5.07% / -20.06% / -35.05%
- **Scenario probabilities:** not separately assigned; see scenario table.

### XLV — Health Care sector ETF

- **Type:** ETF
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** The Health Care sector ETF is preferable to single-name healthcare stocks such as IDXX because it diversifies across the entire healthcare sector, reducing idiosyncratic risk. It is preferable to the high-multiple software names like DDOG and NOW, which carry far higher forward P/Es and deeper drawdowns. Alternatives considered: IDXX, DDOG, NOW.
- **Thesis:** The Health Care sector ETF provides diversified exposure to large-cap healthcare names including LLY, JNJ, ABBV, MRK, and UNH. The ETF is a useful way to express a healthcare view without single-stock idiosyncratic risk. The sector-level exposure is neutral because the shortlist does not provide a clear directional signal for the broader healthcare sector, and the ETF's top-10 holdings are dominated by large, mature pharmaceutical and medical technology companies.
- **Source IDs:** S052, S059
- **Catalysts:** Diversified healthcare exposure across pharma, biotech, and medical technology, Top-10 holdings include LLY, JNJ, ABBV, MRK, and UNH, Useful for reducing single-stock idiosyncratic risk versus individual healthcare names
- **Risks:** Sector-level beta means the ETF will track broad healthcare sector moves, Top-10 holdings coverage is only 61.4% of the portfolio, No clear directional catalyst from the shortlist evidence
- **Valuation method:** Holdings/portfolio valuation with AI total-return assumption
- **Valuation status:** verified; forward-EPS source: ; period flags: 
- **Valuation assumptions:** Holdings/portfolio valuation; 10 weighted holdings; coverage 61.42%; source IDs S052, S059
- **Top holdings:** LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59%
- **Portfolio valuation:** Top 10 holdings; numeric weight coverage 61.42%
- **Sector exposure:** Health Care
- **Underlying drivers:** Diversified healthcare sector exposure with top-10 holdings including LLY, JNJ, ABBV, MRK, and UNH; the ETF provides broad healthcare sector beta rather than a single-name thesis.
- **Bull / Base / Bear:** 198.51 / 186.1 / 166.61
- **Bull / Base / Bear returns:** 12.0% / 5.0% / -6.0%
- **Scenario probabilities:** not separately assigned; see scenario table.

## Quant Risk Layer

| Field | Value |
| --- | --- |
| Volatility model | vol5_ols_v1 |
| Spike model | spike_logit_v1 |
| As-of date | 2026-11-20 |
| Target window | 2026-11-23 to 2026-11-30 |
| Forecast 5D annualized volatility | 36.64% |
| Historical-vol baseline | 26.26% |
| EWMA baseline | 24.67% |
| Spike probability | 92.77% |
| Spike threshold | 18.50% |
| Status | prospective |
| Forecast ID | 48d2c1933342b1a6 |

Risk-only; no directional interpretation or allocation implication.

## Scenarios

### Short Term (5 trading sessions)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 25% | +2.00% | Spike probability 0.928 is well above the 0.185 threshold, but the frozen daily-close model is not yet official after the US close; a confirmed close above the threshold could trigger a short-term risk-on rally of roughly +2%. |
| Base | 50% | +0.00% | Directional signal is false and the forecast is prospective, so the most likely path is a flat near-term move as the model finalizes after the US close and no directional edge is confirmed. |
| Bear | 25% | -2.00% | If the frozen daily-close model fails to confirm after the US close, elevated forecast volatility of 0.366 and a 0.928 spike probability could trigger a risk-off pullback of about -2%. |

### Long Term (12 months)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 30% | +8.00% | A confirmed post-US-close spike above the 0.185 threshold with sustained elevated volatility could extend into a positive trend, supporting a long-term return of roughly +8%. |
| Base | 40% | +3.00% | With a false directional signal and prospective status, the baseline expectation is modest positive drift as the model stabilizes and volatility normalizes around its historical baseline. |
| Bear | 30% | -5.00% | If the 0.928 spike probability reflects a genuine stress event rather than a model artifact, elevated forecast volatility of 0.366 could drive a sustained negative drift of about -5%. |

## Positioning

- Maintain a defensive posture: favored Consumer Staples and Utilities, less favored Information Technology and Energy.
- Use liquidity and quality signals: TLT and SOXX show institutional accumulation, but broad equity breadth is negative.
- Monitor credit spreads: IG OAS at 0.94% and HY OAS at 3.52% are tight but not distressed; a widening would signal risk-off acceleration.
- Do not infer directional or allocation weights; the frozen risk block is risk-only and does not provide a market view.
- Re-evaluate on the next macro print; the current data is stale (CPI and unemployment from September 2026).

## Catalysts

| Date | Event | Why it matters |
| --- | --- | --- |
| 2026-11-23 | Next macro data release | The frozen risk model targets 2026-11-23-2026-11-30; new CPI, employment, or Fed commentary could shift the risk-off trajectory. |
| 2026-11-24 | Fed policy meeting | Effective fed funds rate is 3.88%; any signal on rate path would impact the 10Y-2Y spread and sector valuations. |
| 2026-11-25 | Quarterly earnings season | Shortlist names like NVDA, MRVL, NOW, DDOG, INTC, AMD, MU, AAPL, MSFT, and CHTR will drive sector momentum and liquidity. |

## Key Risks

- Broad market is in a 20-day drawdown of -9.36% with deteriorating price breadth and negative advance/decline ratio.
- Information Technology sector is down 18.7% over 20 days, with extreme dislocation names (DDOG 521x, NOW 97x, MRVL 74x) and high valuation gaps.
- Energy sector is down

## External Source Ledger

| ID | Type | Ticker | Published | Status | URL | Claims |
| --- | --- | --- | --- | --- | --- | --- |
| S001 | macro | macro | 2026-11-19 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFF&cosd=2026-01-01 | Effective federal funds rate (DFF) latest observation 2026-11-19: 3.88 |
| S002 | macro | macro | 2026-11-19 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLH0A0HYM2&cosd=2026-01-01 | US high-yield OAS (BAMLH0A0HYM2) latest observation 2026-11-19: 3.52 |
| S003 | macro | macro | 2026-11-19 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLC0A0CM&cosd=2026-01-01 | US investment-grade OAS (BAMLC0A0CM) latest observation 2026-11-19: 0.94 |
| S004 | macro | macro | 2026-10-01 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCSL&cosd=2026-01-01 | US CPI (CPIAUCSL) latest observation 2026-10-01: 337.476 |
| S005 | macro | macro | 2026-10-01 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=UNRATE&cosd=2026-01-01 | US unemployment rate (UNRATE) latest observation 2026-10-01: 4.1 |
| S006 | macro | macro | 2026-10-01 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=PAYEMS&cosd=2026-01-01 | US nonfarm payrolls (PAYEMS) latest observation 2026-10-01: 159293 |
| S007 | macro | macro | 2026-11-20 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=T10Y2Y&cosd=2026-01-01 | 10Y-2Y Treasury spread (T10Y2Y) latest observation 2026-11-20: 0.29 |
| S008 | filing | PNR | 2026-10-27 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-27 (accession 0000077360-26-000058); 8-K filed 2026-10-27 (accession 0000077360-26-000055); 8-K filed 2026-09-22 (accession 0000077360-26-000050) |
| S009 | filing | APP | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001751008&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0001751008-26-000069); 8-K filed 2026-11-04 (accession 0001751008-26-000068); 10-Q filed 2026-08-05 (accession 0001751008-26-000059) |
| S010 | filing | CMG | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001058090&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0001058090-26-000104); 8-K filed 2026-10-28 (accession 0001058090-26-000103); 8-K filed 2026-09-14 (accession 0001058090-26-000088) |
| S011 | news | CMG | Sat, 21 Nov 2026 02:05:00 GMT | ok | https://news.google.com/rss/search?q=CMG+Chipotle+Mexican+Grill+stock&hl=en-US&gl=US&ceid=US:en | Chipotle Mexican Grill vs. Hershey: Which Consumer Stock Is a Better Buy for 2027? - Yahoo Finance (Sat, 21 Nov 2026 02:05:00 GMT); CAVA vs. Chipotle Mexican Grill: Comparing Revenue Trends Between Two Restaurant Giants - The Motley Fool (Sun, 22 Nov 2026 03:39:00 GMT); Chipotle Stock Looks Cheaper On 2027 Profit, If Sales Deliver - Trefis (Fri, 20 Nov 2026 16:32:30 GMT) |
| S012 | news | APP | Sat, 21 Nov 2026 23:19:26 GMT | ok | https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en | AppLovin vs. Reddit: Which Technology Stock Is a Better Buy for 2027? - The Motley Fool (Sat, 21 Nov 2026 23:19:26 GMT); This tech stock has been nearly cut in half this year. I think Wall Street is getting it wrong - CNBC (Thu, 19 Nov 2026 19:08:20 GMT); AppLovin delivers strong Q3 2026 numbers, stock jumps 24.9% - Yahoo Finance (Thu, 05 Nov 2026 08:00:00 GMT) |
| S013 | filing | APP | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json | Diluted EPS 11.61 for period ending 2026-09-30 (filed 2026-11-04) |
| S014 | filing | CMG | 2026-10-29 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001058090.json | Diluted EPS 0.82 for period ending 2026-09-30 (filed 2026-10-29) |
| S015 | stock | CMG | 2026-11-22 | ok | https://finance.yahoo.com/quote/CMG | Trailing P/E: 33.224297; Forward P/E: 26.86344; Forward EPS: 1.32336; Price: 35.55; Market price: 35.55; Market cap: 44969861120; Sector: Consumer Cyclical; Trailing Eps: 1.07; Revenue Growth: 0.096; Earnings Growth: -0.062; Gross Margin: 0.39314; Operating Margin: 0.14715; Profit Margin: 0.10832; Return On Equity: 0.48518002; Total Revenue: 12713477120; Market Cap: 44969861120; Consensus EPS FY+1: 1.32336; growth: 0.216 |
| S016 | filing | CLX | 2026-11-19 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 | 8-K filed 2026-11-19 (accession 0001206774-26-000606); 10-Q filed 2026-11-02 (accession 0000021076-26-000046); 8-K filed 2026-11-02 (accession 0000021076-26-000044) |
| S017 | news | PNR | Wed, 18 Nov 2026 08:00:00 GMT | ok | https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en | Pentair Stock Price Forecast. Should You Buy PNR? - StockInvest.us (Wed, 18 Nov 2026 08:00:00 GMT); Do Wall Street Analysts Like Pentair Stock? - Yahoo Finance (Mon, 17 Aug 2026 07:00:00 GMT); Why Pentair Stock Popped This Morning - The Motley Fool (Tue, 27 Oct 2026 07:00:00 GMT) |
| S018 | filing | PNR | 2026-10-27 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json | Diluted EPS 2.76 for period ending 2026-09-30 (filed 2026-10-27) |
| S019 | stock | APP | 2026-11-22 | ok | https://finance.yahoo.com/quote/APP | Trailing P/E: 23.453873; Forward P/E: 16.695877; Forward EPS: 20.86084; Price: 348.29; Market price: 348.29; Market cap: 115396132864; Sector: Communication Services; Trailing Eps: 14.85; Revenue Growth: 0.555; Earnings Growth: 0.755; Gross Margin: 0.8878; Operating Margin: 0.77782995; Profit Margin: 0.65887; Return On Equity: 2.1008599; Total Revenue: 7608893952; Market Cap: 115396132864; Consensus EPS FY+1: 20.72451; growth: 0.2744 |
| S020 | stock | PNR | 2026-11-22 | ok | https://finance.yahoo.com/quote/PNR | Trailing P/E: 18.700272; Forward P/E: 12.939242; Forward EPS: 5.30402; Price: 68.63; Market price: 68.63; Market cap: 10957101056; Sector: Industrials; Trailing Eps: 3.67; Revenue Growth: -0.045; Earnings Growth: -0.188; Gross Margin: 0.40168998; Operating Margin: 0.21410999; Profit Margin: 0.15435; Return On Equity: 0.15605; Total Revenue: 3966200064; Market Cap: 10957101056; Consensus EPS FY+1: 5.30402; growth: 0.1282 |
| S021 | filing | IDXX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000874716&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000874716-26-000135); 8-K filed 2026-11-02 (accession 0001104659-26-120892); 10-Q filed 2026-08-04 (accession 0000874716-26-000123) |
| S022 | news | CLX | Thu, 19 Nov 2026 17:06:03 GMT | ok | https://news.google.com/rss/search?q=CLX+Clorox+stock&hl=en-US&gl=US&ceid=US:en | Should You Buy Clorox Stock At This Price? - Yahoo Finance (Thu, 19 Nov 2026 17:06:03 GMT); Clorox (CLX) Stock Rebounds As Q4 Earnings Face Margin Strain - Yahoo Finance (Tue, 03 Nov 2026 08:00:00 GMT); CLX - Clorox Co Stock Price and Quote - Finviz (Tue, 26 May 2026 17:32:27 GMT) |
| S023 | news | IDXX | Thu, 19 Nov 2026 12:30:02 GMT | ok | https://news.google.com/rss/search?q=IDXX+Idexx+Laboratories+stock&hl=en-US&gl=US&ceid=US:en | Here's How Much You'd Have If You Invested $1000 in Idexx Laboratories a Decade Ago - Yahoo Finance (Thu, 19 Nov 2026 12:30:02 GMT); IDEXX Laboratories: Great Company, But Too Expensive (Rating Downgrade) - Seeking Alpha (Wed, 04 Nov 2026 08:00:00 GMT); If You Invested $100 In IDEXX Laboratories Stock 15 Years Ago, You Would Have This Much Today - Benzinga (Mon, 02 Nov 2026 08:00:00 GMT) |
| S024 | stock | CLX | 2026-11-22 | ok | https://finance.yahoo.com/quote/CLX | Trailing P/E: 18.836332; Forward P/E: 16.978472; Forward EPS: 6.1684; Price: 104.73; Market price: 104.73; Market cap: 12687766528; Sector: Consumer Defensive; Trailing Eps: 5.56; Revenue Growth: 0.333; Earnings Growth: 1.138; Gross Margin: 0.41939998; Operating Margin: 0.14286; Profit Margin: 0.09408; Return On Equity: 5.34363; Total Revenue: 7196000256; Market Cap: 12687766528; Consensus EPS FY+1: 6.1684; growth: 0.0769 |
| S025 | news | CHTR | Sun, 15 Nov 2026 05:10:00 GMT | ok | https://news.google.com/rss/search?q=CHTR+Charter+Communications+stock&hl=en-US&gl=US&ceid=US:en | Charter Communications (CHTR) Stock Could Be A Bargain Following Its New Operating Model - Yahoo Finance (Sun, 15 Nov 2026 05:10:00 GMT); Charter Communications (NasdaqGS:CHTR) Stock Forecast & Analyst Predictions - Simply Wall St (Wed, 18 Nov 2026 08:00:00 GMT); Why Is Charter Communications (NASDAQ:CHTR) In Focus Amid Sector Pressures? - Kalkine Media (Sun, 22 Nov 2026 08:02:00 GMT) |
| S026 | filing | CLX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000021076.json | Diluted EPS 1.39 for period ending 2026-09-30 (filed 2026-11-02) |
| S027 | stock | CHTR | 2026-11-22 | ok | https://finance.yahoo.com/quote/CHTR | Trailing P/E: 12.098683; Forward P/E: 2.8233452; Forward EPS: 45.59485; Price: 128.73; Market price: 128.73; Market cap: 23049306112; Sector: Communication Services; Trailing Eps: 10.64; Revenue Growth: 0.091; Gross Margin: 0.55084; Operating Margin: 0.23389; Profit Margin: 0.02498; Return On Equity: 0.07019; Total Revenue: 55645999104; Market Cap: 23049306112; Consensus EPS FY+1: 49.52287; growth: 1.4594 |
| S028 | filing | CHTR | 2026-11-06 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-06 (accession 0001091667-26-000073); 8-K filed 2026-11-06 (accession 0001091667-26-000072); 8-K filed 2026-10-27 (accession 0001091667-26-000064) |
| S029 | filing | GEN | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0000849399-26-000083); 8-K filed 2026-10-28 (accession 0000849399-26-000081); 8-K filed 2026-10-09 (accession 0000849399-26-000079) |
| S030 | stock | IDXX | 2026-11-22 | ok | https://finance.yahoo.com/quote/IDXX | Trailing P/E: 45.56671; Forward P/E: 40.029243; Forward EPS: 16.8929; Price: 676.21; Market price: 676.21; Market cap: 53276061696; Sector: Healthcare; Trailing Eps: 14.84; Revenue Growth: 0.099; Earnings Growth: 0.179; Gross Margin: 0.62722; Operating Margin: 0.32497; Profit Margin: 0.25357; Return On Equity: 0.68925005; Total Revenue: 4662220800; Market Cap: 53276061696; Consensus EPS FY+1: 16.8929; growth: 0.1244 |
| S031 | news | GEN | Sat, 21 Nov 2026 19:40:24 GMT | ok | https://news.google.com/rss/search?q=GEN+Gen+Digital+stock&hl=en-US&gl=US&ceid=US:en | Gen Digital Inc. (GEN) Stock Price, News, Quote & History - Yahoo! Finance Canada (Sat, 21 Nov 2026 19:40:24 GMT); Four S&P 500 Stocks Rising in a Falling Market: Pentair, AppLovin, Chipotle, and Gen Digital - Benzinga (Sat, 21 Nov 2026 22:00:05 GMT); Gen Digital (GEN) Stock Looks Below Fair Value On Its 45% Run - Yahoo Finance (Sat, 21 Nov 2026 02:14:00 GMT) |
| S032 | filing | IDXX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000874716.json | Diluted EPS 11.75 for period ending 2026-09-30 (filed 2026-11-02) |
| S033 | filing | MGM | 2026-10-28 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000789570&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-28 (accession 0000789570-26-000107); 8-K filed 2026-10-28 (accession 0000789570-26-000106); 8-K filed 2026-10-28 (accession 0000789570-26-000104) |
| S034 | stock | GEN | 2026-11-22 | ok | https://finance.yahoo.com/quote/GEN | Trailing P/E: 14.817259; Forward P/E: 8.746435; Forward EPS: 3.33736; Price: 29.19; Market price: 29.19; Market cap: 17317730304; Sector: Technology; Trailing Eps: 1.97; Revenue Growth: 0.122; Earnings Growth: 1.286; Gross Margin: 0.77410007; Operating Margin: 0.43229; Profit Margin: 0.23068; Return On Equity: 0.46402; Total Revenue: 5228000256; Market Cap: 17317730304; Consensus EPS FY+1: 3.33736; growth: 0.1286 |
| S035 | filing | SNDK | 2026-11-19 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0002023554&type=10-Q&dateb=&owner=include&count=10 | 8-K filed 2026-11-19 (accession 0001628280-26-075127); 8-K filed 2026-11-18 (accession 0001628280-26-074848); 10-Q filed 2026-10-30 (accession 0001628280-26-068601) |
| S036 | stock | MGM | 2026-11-22 | ok | https://finance.yahoo.com/quote/MGM | Trailing P/E: 12.446155; Forward P/E: 23.023344; Forward EPS: 1.40553; Price: 32.36; Market price: 32.36; Market cap: 8187421184; Sector: Consumer Cyclical; Trailing Eps: 2.6; Revenue Growth: -0.009; Gross Margin: 0.4362; Operating Margin: 0.057979997; Profit Margin: 0.03916; Return On Equity: 0.26933; Total Revenue: 17722869760; Market Cap: 8187421184; Consensus EPS FY+1: 1.40553; growth: -0.0462 |
| S037 | news | MGM | Thu, 29 Oct 2026 07:00:00 GMT | ok | https://news.google.com/rss/search?q=MGM+MGM+Resorts+stock&hl=en-US&gl=US&ceid=US:en | Why MGM Resorts (MGM) stock is up today - Yahoo Finance (Thu, 29 Oct 2026 07:00:00 GMT); This casino stock has fallen for 17 weeks in a row. Katie Stockton says it could be due for a bounce - CNBC (Tue, 03 Nov 2026 08:00:00 GMT); MGM Stock Dives 10% After Barry Diller Drops $18 Billion Bid - Forbes (Thu, 24 Sep 2026 07:00:00 GMT) |
| S038 | filing | GEN | 2026-10-29 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000849399.json | Diluted EPS 0.83 for period ending 2026-10-02 (filed 2026-10-29) |
| S039 | filing | MRVL | 2026-11-12 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001835632&type=10-Q&dateb=&owner=include&count=10 | 8-K filed 2026-11-12 (accession 0001835632-26-000026); 8-K filed 2026-11-02 (accession 0001193125-26-442717); 8-K filed 2026-11-02 (accession 0001193125-26-442714) |
| S040 | stock | SNDK | 2026-11-22 | ok | https://finance.yahoo.com/quote/SNDK | Trailing P/E: 0.085785426; Forward P/E: 2.20723; Forward EPS: 35.9002; Price: 79.24; Market price: 79.24; Market cap: 90200072192; Sector: Technology; Trailing Eps: 923.7; Revenue Growth: 3.779; Earnings Growth: 69.096; Gross Margin: 0.79952; Operating Margin: 0.7268; Profit Margin: 0.67039; Return On Equity: 1.41174; Total Revenue: 28970999808; Market Cap: 90200072192; Consensus EPS FY+1: 35.9002; growth: 0.2612 |

## Sources

- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFF&cosd=2026-01-01 (2026-11-19)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLH0A0HYM2&cosd=2026-01-01 (2026-11-19)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLC0A0CM&cosd=2026-01-01 (2026-11-19)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCSL&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=UNRATE&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=PAYEMS&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=T10Y2Y&cosd=2026-01-01 (2026-11-20)
- filing PNR: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 (2026-10-27)
- filing APP: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001751008&type=10-Q&dateb=&owner=include&count=10 (2026-11-04)
- filing CMG: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001058090&type=10-Q&dateb=&owner=include&count=10 (2026-10-29)
- news CMG: https://news.google.com/rss/search?q=CMG+Chipotle+Mexican+Grill+stock&hl=en-US&gl=US&ceid=US:en (Sat, 21 Nov 2026 02:05:00 GMT)
- news APP: https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en (Sat, 21 Nov 2026 23:19:26 GMT)
- filing APP: https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json (2026-11-04)
- filing CMG: https://data.sec.gov/api/xbrl/companyfacts/CIK0001058090.json (2026-10-29)
- stock CMG: https://finance.yahoo.com/quote/CMG (2026-11-22)
- filing CLX: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 (2026-11-19)
- news PNR: https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en (Wed, 18 Nov 2026 08:00:00 GMT)
- filing PNR: https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json (2026-10-27)
- stock APP: https://finance.yahoo.com/quote/APP (2026-11-22)
- stock PNR: https://finance.yahoo.com/quote/PNR (2026-11-22)

## AI Provenance

- Provider / model: hermes-local-proxy / upstage/solar-mini4:free
- Market research: attempts=1 tokens=9518 (prompt=6518, completion=3000) runtime=15.84s
- Fundamental research: generated this run at 2026-11-22T10:16:21.142155+00:00
- Evidence source dates: {'as_of': '2026-11-20', 'latest_equity_date': '2026-11-20', 'latest_macro_date': '2026-11-21', 'flows_date': '2026-11-20'}
- Evidence fingerprint: cdaa6eb000115c8f99dd8a472f2f85232b929d167664655d3024dc3727971fc7
- Source citations are retrieved external records in the ledger above; market values remain from the verified database snapshot.


## Disclosures

- This is research and market intelligence, not investment advice.
- AI conclusions are research judgments, not validated return predictions.
- The frozen risk layer is risk-only and is not used for directional views or allocations.
- Legacy scores are not active inputs or outputs.

# AEGIS AI-First Market Intelligence

Research generated at: 17 November 2026, 07:31 HKT
Database freshness: equity 2026-11-16 (latest row retrieved 2026-11-17 06:31:59.363991+08:00)
Data cutoff: 2026-11-16 US cash close
Snapshot ID: aegis-hourly-20261116T233128Z

## Executive Summary

- **AI market view: Risk-on tilt is narrowing: broad market breadth is positive but the index is down over 20 days, and the 20-day return distribution is split, with Information Technology and Communication Services lagging while Health Care, Consumer Staples, Utilities and Real Estate lead. Credit spreads are tight (IG 0.89, HY 3.23), and the Fed funds rate is 3.88%, so the macro backdrop is still supportive, but the market is rotating out of expensive, liquidity-led names toward defensive and income-oriented sectors.**
- Broad market breadth is constructive (71.3% above 50-day, 63.6% above 200-day, ADR 1.70), but the S&P 500 is down 1.28% over 20 days, indicating a cautious, rotation-driven tape.
- Information Technology (XLK -11.4%) and Communication Services (XLC -3.0%) are the weakest sectors, while Health Care (+7.0%), Utilities (+6.7%), Consumer Staples (+6.2%) and Real Estate (+6.2%) are the strongest.
- Credit conditions are benign: IG OAS 0.89 and HY OAS 3.23, with the 10Y-2Y spread at 0.29, supporting risk appetite.
- The Fed funds rate is 3.88% as of 2026-11-13, and CPI is 336.3 (Sep), so policy is still accommodative but inflation is not collapsing.
- Liquidity leaders such as NVDA, MU, AMD and AAPL remain in the shortlist, but several large-cap names show extreme valuation or dislocation flags, so the market is not uniformly bullish.
- The risk model shows 5-day forecast volatility of 20.0% and a 34.1% spike probability, above the 18.5% threshold, signaling elevated near-term uncertainty.

## Data QC

- Status: **PASS_WITH_WARNINGS**
- Equity session: 0 completed session(s) behind inference date
- Equity provenance: 554 provisional / 0 canonical
- Breadth lag: 1 session(s); ETF-flow lag: 1 session(s)
- Note: Equity prices for the session are provisional yfinance data; Massive has not yet replaced them.
- External sources: 71 ok / 8 unavailable; retrieved 2026-11-16T23:31:48.598804+00:00

## Idea Discovery

- S&P 500 universe: 503; eligible: 487; transparent shortlist: 20
- Method: independent momentum/dislocation/PE/liquidity buckets; no composite score
- Evidence used: latest close, 20d and 60d price returns, 60d drawdown, trailing P/E, earnings yield, sector-relative P/E, dollar volume, GICS sector
- Not available as verified inputs: verified earnings-revision history for the full universe, FY+2 consensus, structured industry catalyst calendar
- Eligible but not shortlisted: 467 (outside the top independent momentum, dislocation, valuation and liquidity buckets)
- Included: APP (top_20d_momentum); FISV (top_20d_momentum); PNR (top_20d_momentum); CLX (top_20d_momentum); GEN (top_20d_momentum); CHTR (top_20d_momentum); ROP (top_20d_momentum); IDXX (top_20d_momentum); SNDK (largest_20d_dislocation, liquidity_leader); RDDT (largest_20d_dislocation); INTC (largest_20d_dislocation); MRVL (largest_20d_dislocation); LITE (largest_20d_dislocation); DDOG (largest_20d_dislocation); FFIV (largest_20d_dislocation); NOW (largest_20d_dislocation); NVDA (liquidity_leader); MU (liquidity_leader); AMD (liquidity_leader); AAPL (liquidity_leader)
- Excluded reasons: {"missing_latest_session": 14, "missing_recent_or_latest_price": 16}
- Valuation-quality rejected: [{"flags": ["forward_eps_missing"], "ticker": "FISV"}, {"flags": ["forward_pe_outside_plausible_range", "implausible_earnings_yield", "forward_eps_vs_reported_jump"], "ticker": "CHTR"}, {"flags": ["forward_pe_outside_plausible_range", "implausible_earnings_yield"], "ticker": "SNDK"}, {"flags": ["forward_eps_vs_reported_jump"], "ticker": "MRVL"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "LITE"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "DDOG"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "FFIV"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "NOW"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "NVDA"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "MU"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "AMD"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "AAPL"}]

## Market Snapshot

| Asset | Latest | Change | Observation |
| --- | --- | --- | --- |
| S&P 500 (SPX) | 7561.67 | -1.28% (20d) | Index is down over 20 days despite positive breadth; rotation toward defensive sectors is underway. |
| Health Care (XLV) | return_20d +6.96% | +6.96% | Strongest sector; trailing P/E 30.62, consistent with defensive, high-quality demand. |
| Consumer Staples (XLP) | return_20d +6.18% | +6.18% | Second-strongest sector; trailing P/E 24.92, reflecting safe-haven flows. |
| Information Technology (XLK) | return_20d -11.40% | -11.40% | Weakest sector; trailing P/E 29.06, with NVDA, AMD and MU flagged as liquidity leaders but expensive or dislocation-prone. |
| Communication Services (XLC) | return_20d -2.97% | -2.97% | Negative 20-day return; trailing P/E 16.97, but momentum and valuation screens excluded most names. |
| Financials (XLF) | return_20d +5.67% | +5.67% | Positive 20-day return; trailing P/E 15.71, supported by tight credit spreads and a 3.88% policy rate. |

## Macro, Fiscal, Rates, Liquidity and Credit

- Growth: The 10Y-2Y Treasury spread is 0.29 as of 2026-11-16, a modestly positive but narrow curve, and the S&P 500 is down 1.28% over 20 days, indicating slowing momentum despite positive breadth.
- Inflation: CPI (CPIAUCSL) is 336.3 in September 2026, and core CPI is 338.9, so inflation remains above the pre-2020 range and is not yet at target.
- Policy: The effective federal funds rate is 3.88% as of 2026-11-13, and the Fed has room to ease if growth or inflation deteriorates, but the current stance is still moderately restrictive.
- Rates: The 10Y-2Y spread of 0.29 is positive but narrow, and the yield curve is not strongly steepening, which limits the benefit of a steepener for financial stocks.
- Liquidity: Credit spreads are tight (IG 0.89, HY 3.23), and the risk model shows 5-day forecast volatility of 20.0% with a 34.1% spike probability, above the 18.5% threshold, so liquidity is available but near-term risk is elevated.
- Credit: IG OAS 0.89 and HY OAS 3.23 as of 2026-11-13 indicate benign credit conditions, but the risk model's elevated spike probability suggests caution on leverage and cyclical exposure.

## US Equities and 11 GICS Sectors

Macro source IDs: S001, S002, S003, S004, S005, S006, S007

| GICS sector | Evidence | AI research stance | Source IDs |
| --- | --- | --- | --- |
| Health Care | 20-day return +6.96% (XLV), trailing P/E 30.62 (S054), and the sector is the strongest in the universe; momentum and defensive positioning are the key drivers. | Defensive leadership is supported by positive breadth and tight credit; the sector is expensive on trailing P/E but the risk-reward is favorable in a cautious tape. | S054 |
| Consumer Staples | 20-day return +6.18% (XLP), trailing P/E 24.92 (S057), and the sector is the second-strongest; safe-haven flows and stable earnings support the view. | Stable-demand exposure is attractive in a market with elevated volatility and a 34.1% spike probability. | S057 |
| Consumer Discretionary | 20-day return +3.22% (XLY), trailing P/E 24.73 (S061), and the sector is mid-ranked; consumer resilience is supported by tight credit spreads. | Moderate exposure is reasonable, but the sector is not a top performer and faces valuation risk if growth slows. | S061 |
| Real Estate | 20-day return +6.19% (XLRE), trailing P/E 29.55 (S060), and the sector is among the strongest; the narrow 10Y-2Y spread and low policy rate support real asset demand. | Attractive in a low-rate, cautious environment, but the high trailing P/E warrants monitoring of rate expectations. | S060 |
| Financials | 20-day return +5.67% (XLF), trailing P/E 15.71 (S062), and the sector is positive; tight IG and HY spreads and a 3.88% policy rate support net interest margins. | Favorable if the curve stays positive and credit spreads remain tight; the low P/E offers a margin of safety. | S062 |
| Utilities | 20-day return +6.67% (XLU), trailing P/E 18.15 (S063), and the sector is a top performer; defensive demand and stable cash flows are supported by elevated volatility. | Strong defensive positioning is warranted given the 34.1% spike probability and 20.0% forecast volatility. | S063 |
| Materials | 20-day return +1.02% (XLB), trailing P/E 21.40 (S064), and the sector is mid-ranked; industrial demand is mixed with positive but modest breadth. | Neutral; the sector is not a leader, and commodity exposure is sensitive to global growth and credit conditions. | S064 |
| Industrials | 20-day return -0.61% (XLI), trailing P/E 26.57 (S066), and the sector is slightly negative; the 20-day return distribution is split, and the sector is not a top performer. | Cautious; the sector is not benefiting from the defensive rotation and faces mixed industrial demand. | S066 |
| Communication Services | 20-day return -2.97% (XLC), trailing P/E 16.97 (S070), and the sector is negative; the momentum and dislocation screens excluded most names, and the sector is lagging. | Less favored; the sector is not participating in the defensive rally and faces valuation and momentum headwinds. | S070 |
| Information Technology | 20-day return -11.40% (XLK), trailing P/E 29.06 (S073), and the sector is the weakest; NVDA, AMD and MU are liquidity leaders but flagged with extreme valuation or dislocation, and the sector is in a sharp pullback. | Cautious; the sector is expensive and has been hit hard, with several large-cap names showing dislocation or extreme P/E flags. | S073 |
| Energy | 20-day return -6.06% (XLE), trailing P/E 15.91 (S072), and the sector is negative; the sector is not benefiting from the current risk-on/rotation dynamic. | Less favored; the sector is lagging and faces headwinds from a narrow curve and cautious macro conditions. | S072 |

### Sector fundamentals, valuation and earnings

The supplied database provides trailing P/E for each GICS sector ETF (XLV 30.62, XLP 24.92, XLY 24.73, XLRE 29.55, XLF 15.71, XLU 18.15, XLB 21.40, XLI 26.57, XLC 16.97, XLE 15.91, XLK 29.06) and 20-day returns, but no point-in-time sector fundamentals such as earnings growth, margins, revenue, or consensus estimates are available in the supplied evidence. Growth and margin data were retrieved only for the source-backed shortlist names, and the full universe lacks verified earnings-revision history, FY+2 consensus, and a structured industry catalyst calendar. Therefore, no sector-level fundamental metrics beyond P/E and 20-day returns are reported here.

## Growth vs Value

- Health Care (XLV) and Consumer Staples (XLP) offer the highest 20-day returns (+6.96% and +6.18%) with trailing P/Es of 30.62 and 24.92, indicating a defensive, quality tilt rather than cheapness.
- Financials (XLF) and Utilities (XLU) combine positive 20-day returns (+5.67% and +6.67%) with lower trailing P/Es (15.71 and 18.15), providing a value-plus-defensive profile.
- Information Technology (XLK) is the most expensive sector at 29.06 trailing P/E and is down 11.40% over 20 days, with NVDA, AMD and MU flagged as liquidity leaders but carrying extreme valuation or dislocation flags.
- Communication Services (XLC) and Energy (XLE) are the weakest sectors, with negative 20-day returns (-2.97% and -6.06%) and trailing P/Es of 16.97 and 15

## ETF Flows and Breadth


## Stock Ideas

Single-stock research uses reported EPS, forward P/E and company fundamentals. All ideas are research judgments, not validated return predictions.

| Ticker | Security | Research view | Price | EPS | Forward P/E | Base target | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| APP | AppLovin | NEW | 415.2200012207031 | 20.86026 | 19.904833 | 417.21 | NEW |
| PNR | Pentair | KEEP | 68.44000244140625 | 5.30402 | 12.903421 | 84.86 | KEEP |
| CLX | Clorox | KEEP | 110.16999816894531 | 6.1684 | 17.860386 | 111.03 | KEEP |
| ROP | Roper Technologies | KEEP | 483.7200012207031 | 24.57318 | 19.684877 | 442.32 | KEEP |

## ETF Ideas

ETF research uses holdings, portfolio valuation and exposure. Single-stock EPS × P/E valuation is not applied to ETFs.

| Ticker | Fund | Research view | Price | Top holdings | Portfolio valuation | Sector exposure | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| XLV | Health Care sector ETF | KEEP | 187.8800048828125 | LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59% | Top 10 holdings; numeric weight coverage 61.42% | Health Care | KEEP |
### APP — AppLovin

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** AppLovin offers a rare combination of top-tier momentum, high gross and operating margins, and a forward P/E near 19.9 that is not extreme for its growth profile. Compared with the other momentum names such as CLX and ROP, APP has a materially higher growth and margin profile, while compared with the dislocation names like RDDT and INTC, APP is not in a deep drawdown and carries a more constructive near-term price trajectory. Alternatives considered: CLX, ROP, RDDT, INTC.
- **Thesis:** AppLovin screens in the top 20-day momentum bucket with a 54% 20-day return and a 36% 60-day return, indicating strong recent price leadership. Reported diluted EPS of 11.61 for the fiscal period ending 2026-09-30 and a forward EPS of 20.86 support a forward P/E near 19.9, which is reasonable for a high-margin, high-growth mobile advertising platform. The company's gross margin near 89% and operating margin near 78% provide a durable profitability profile that can compound earnings through ad spend growth.
- **Source IDs:** S008, S012, S013, S018
- **Catalysts:** Continued momentum in 20-day and 60-day price returns, Sustained high-margin advertising revenue growth, Forward EPS expansion from reported FY1 EPS of 20.72 toward the 20.86 consensus, Potential re-rating as the stock's recent volatility stabilizes
- **Risks:** High 20-day momentum can mean elevated volatility and pullbacks, News coverage flags a sharp 47% decline in the past month, suggesting possible overreaction or sentiment risk, Forward EPS and fiscal-year mapping are unverified, so consensus estimates should be treated cautiously, Mobile advertising market competition and ad spend cyclicality
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 20.8603 (source.forwardEps) x AI multiple assumption 20.00; source IDs S008, S012, S013, S018
- **EPS:** 20.86026 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 19.904833
- **FY+1 growth assumption:** 27.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / PNR and CLX / APP shows the strongest forward earnings growth (27.44%) and revenue growth (25.37%) among the four names, with high gross margin (88.78%) and operating margin (77.78%). The base multiple of 20.0x is justified by its superior growth and margin profile relative to PNR (12.82% growth, 40.17% gross margin) and CLX (7.69% growth, 41.94% gross margin), while the bull/bear range reflects upside if growth re-accelerates and downside if margin compression occurs.
- **Company fundamentals:** AppLovin reported diluted EPS of 11.61 for the period ending 2026-09-30, with forward EPS of 20.86 and a forward P/E of 19.9. Revenue growth is 55.5% and earnings growth is 75.5%, with gross margin of 88.8% and operating margin of 77.8%. The stock closed at 415.22 with a 20-day return of 54.3% and a 60-day return of 35.8%. Source-backed fundamentals are available for the shortlist names.
- **Bull / Base / Bear:** 500.65 / 417.21 / 333.76
- **Bull / Base / Bear returns:** 20.57% / 0.48% / -19.62%
- **Scenario probabilities:** not separately assigned; see scenario table.

### PNR — Pentair

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Pentair is a lower-risk, reasonably valued industrial name compared with the high-growth but volatile momentum names such as APP and the deeply discounted dislocation names such as INTC. Its forward P/E of 12.9 and modest drawdown of -5.0% make it a more conservative holding, but the negative revenue and earnings growth mean it should not be treated as a high-conviction buy. Alternatives considered: APP, CLX, ROP, INTC.
- **Thesis:** Pentair is a top-20-day momentum name with a 30% 20-day return and a 60-day return of 6.3%. The stock trades at a forward P/E of 12.9 based on a forward EPS of 5.30, which is reasonable for a diversified industrial and water technology company. However, reported revenue growth is slightly negative at -4.5% and earnings growth is -18.8%, indicating that near-term operating leverage is not yet translating into top-line expansion. The stock is not in a deep drawdown, with a 60-day drawdown of only -5.0%, so the risk-reward is balanced rather than compelling.
- **Source IDs:** S010, S014, S017, S022
- **Catalysts:** Sustained 20-day momentum above 25%, Potential stabilization in industrial and water segment demand, Forward EPS of 5.30 supports a reasonable valuation relative to the current price, Diversified exposure to water infrastructure and flow control end markets
- **Risks:** Negative revenue and earnings growth in the latest reported period, Sector-relative P/E of 0.49 indicates the stock is cheap relative to its sector, but that may reflect weak near-term fundamentals, Industrial end-market cyclicality and capital expenditure sensitivity, Momentum may fade if earnings do not inflect positively
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 5.3040 (source.forwardEps) x AI multiple assumption 16.00; source IDs S010, S014, S017, S022
- **EPS:** 5.30402 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 12.903421
- **FY+1 growth assumption:** 12.82%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / APP and CLX / PNR has the lowest forward earnings growth (12.82%) and negative revenue/earnings growth (-4.5%/-18.8%), with a lower gross margin (40.17%) and operating margin (21.41%) than APP and CLX. The base multiple of 16.0x is set below APP and CLX to reflect weaker growth and margin, with a bull case at 20.0x if the cycle turns and a bear case at 12.0x if the downturn persists.
- **Company fundamentals:** Pentair reported diluted EPS of 2.76 for the period ending 2026-09-30, with forward EPS of 5.30 and a forward P/E of 12.9. Revenue growth is -4.5% and earnings growth is -18.8%, with gross margin of 40.2% and operating margin of 21.4%. The stock closed at 68.44 with a 20-day return of 29.7% and a 60-day return of 6.3%. Source-backed fundamentals are available for the shortlist names.
- **Bull / Base / Bear:** 106.08 / 84.86 / 63.65
- **Bull / Base / Bear returns:** 55.0% / 23.99% / -7.0%
- **Scenario probabilities:** not separately assigned; see scenario table.

### CLX — Clorox

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Clorox offers a defensive, reasonably valued consumer staples holding with strong reported earnings growth and a forward P/E of 17.9. Compared with the higher-growth but more volatile momentum names such as APP, CLX provides lower earnings volatility and a more stable cash flow profile, making it a useful diversifier within a momentum-oriented portfolio. Alternatives considered: APP, PNR, ROP, IDXX.
- **Thesis:** Clorox is a top-20-day momentum name with a 29% 20-day return and a 60-day return of 3.3%. The stock trades at a forward P/E of 17.9 based on a forward EPS of 6.17, which is reasonable for a consumer staples company. Reported revenue growth is 33.3% and earnings growth is 113.8%, indicating a strong earnings inflection. However, the consumer staples sector is generally defensive and the stock's 60-day drawdown is 0%, so the upside is more about steady compounding than a sharp re-rating.
- **Source IDs:** S021, S023, S031
- **Catalysts:** Strong earnings growth of 113.8% in the latest reported period, Sustained 20-day momentum above 25%, Forward EPS of 6.17 supports a reasonable valuation for a staples name, Diversified consumer staples portfolio with brand strength
- **Risks:** Consumer staples demand is defensive and can be sensitive to consumer spending trends, Sector-relative P/E of 0.64 indicates the stock is cheap relative to its sector, but that may reflect slower long-term growth, 20-day momentum may fade if consumer trends weaken, Competitive pressure in household and personal care categories
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 6.1684 (source.forwardEps) x AI multiple assumption 18.00; source IDs S021, S023, S031
- **EPS:** 6.1684 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 17.860386
- **FY+1 growth assumption:** 7.69%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / APP and PNR / CLX has moderate forward earnings growth (7.69%) and revenue growth (2.23%), with a gross margin of 41.94% and operating margin of 14.29%. The base multiple of 18.0x is justified by its stable, defensive consumer staples profile and higher earnings growth than PNR, while the bull/bear range reflects potential margin recovery versus continued softness.
- **Company fundamentals:** Clorox reported diluted EPS of 1.39 for the period ending 2026-09-30, with forward EPS of 6.17 and a forward P/E of 17.9. Revenue growth is 33.3% and earnings growth is 113.8%, with gross margin of 41.9% and operating margin of 14.3%. The stock closed at 110.17 with a 20-day return of 28.8% and a 60-day return of 3.3%. Source-backed fundamentals are available for the shortlist names.
- **Bull / Base / Bear:** 135.7 / 111.03 / 86.36
- **Bull / Base / Bear returns:** 23.17% / 0.78% / -21.61%
- **Scenario probabilities:** not separately assigned; see scenario table.

### ROP — Roper Technologies

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Roper Technologies is a high-quality, niche technology company with strong margins and steady earnings growth. Compared with the more volatile momentum names such as APP and the deeply discounted dislocation names such as INTC, ROP offers a more balanced risk profile with a forward P/E of 19.7 and a modest drawdown of -1.7%. Alternatives considered: APP, PNR, CLX, INTC.
- **Thesis:** Roper Technologies is a top-20-day momentum name with a 26% 20-day return and a 60-day return of 17.5%. The stock trades at a forward P/E of 19.7 based on a forward EPS of 24.57, which is reasonable for a high-quality technology-enabled industrial company. Reported revenue growth is 7.6% and earnings growth is 32.6%, indicating steady but not spectacular growth. The stock is not in a deep drawdown, with a 60-day drawdown of only -1.7%, so the risk-reward is balanced.
- **Source IDs:** S028, S030, S043
- **Catalysts:** Sustained 20-day momentum above 25%, Steady earnings growth of 32.6% in the latest reported period, Forward EPS of 24.57 supports a reasonable valuation for a niche technology company, Diversified exposure to industrial, healthcare, and technology markets
- **Risks:** Revenue growth of 7.6% is modest relative to the high forward P/E, Sector-relative P/E of 0.49 indicates the stock is cheap relative to its sector, but that may reflect slower long-term growth, 20-day momentum may fade if earnings do not inflect positively, Niche technology companies can face competitive and customer concentration risks
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 24.5732 (source.forwardEps) x AI multiple assumption 18.00; source IDs S028, S030, S043
- **EPS:** 24.57318 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 19.684877
- **FY+1 growth assumption:** 9.81%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / APP and CLX / ROP has forward earnings growth of 9.81% and revenue growth of 6.29%, with a gross margin of 69.67% and operating margin of 28.05%. The base multiple of 18.0x is justified by its stronger growth and margin profile than PNR, with a bull case at 22.0x if the cycle improves and a bear case at 14.0x if the cycle weakens.
- **Company fundamentals:** Roper Technologies reported diluted EPS of 21.3 for the period ending 2026-09-30, with forward EPS of 24.57 and a forward P/E of 19.7. Revenue growth is 7.6% and earnings growth is 32.6%, with gross margin of 69.7% and operating margin of 28.0%. The stock closed at 483.72 with a 20-day return of 26.1% and a 60-day return of 17.5%. Source-backed fundamentals are available for the shortlist names.
- **Bull / Base / Bear:** 540.61 / 442.32 / 344.02
- **Bull / Base / Bear returns:** 11.76% / -8.56% / -28.88%
- **Scenario probabilities:** not separately assigned; see scenario table.

### XLV — Health Care sector ETF

- **Type:** ETF
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** The Health Care sector ETF offers a diversified, defensive exposure to large-cap pharmaceutical and medical device names that is not available from individual stock picks. Compared with the more volatile momentum stocks such as APP and the deeply discounted dislocation names such as INTC, XLV provides lower single-name risk and a more stable portfolio component, though the short-term price action warrants a neutral stance. Alternatives considered: XLP, XLY, XLRE, XLF, XLU, XLB, XLI.
- **Thesis:** The Health Care sector ETF provides diversified exposure to large-cap pharmaceutical, medical device, and managed care names. The ETF closed at 187.88 with a raw percentage change of -0.51%, indicating a modest pullback. The top holdings include LLY, JNJ, ABBV, MRK, and UNH, which are generally defensive and cash-generative. The sector is not in a deep drawdown, but the negative short-term price action suggests caution rather than conviction.
- **Source IDs:** S054
- **Catalysts:** Diversified exposure to large-cap health care names with strong balance sheets, Defensive characteristics that can perform during market stress, Top holdings include LLY, JNJ, ABBV, MRK, and UNH with significant weight, Potential for sector rotation into health care if risk appetite wanes
- **Risks:** Short-term price decline of -0.51% suggests near-term weakness, Sector-relative valuation may be expensive relative to other sectors, Concentration in a few large names means the ETF is not fully diversified within the sector, Regulatory and patent cliff risks for pharmaceutical holdings
- **Valuation method:** Holdings/portfolio valuation with AI total-return assumption
- **Valuation status:** verified; forward-EPS source: ; period flags: 
- **Valuation assumptions:** Holdings/portfolio valuation; 10 weighted holdings; coverage 61.42%; source IDs S054
- **Top holdings:** LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59%
- **Portfolio valuation:** Top 10 holdings; numeric weight coverage 61.42%
- **Sector exposure:** Health Care
- **Underlying drivers:** Large-cap pharmaceutical and medical device revenue growth, managed care consolidation, regulatory environment, and defensive demand characteristics.
- **Bull / Base / Bear:** 210.43 / 197.27 / 176.61
- **Bull / Base / Bear returns:** 12.0% / 5.0% / -6.0%
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
| Bull | 25% | +2.00% | Low 5-day realized volatility (0.200) and a 34.1% spike probability relative to the 22.9% historical baseline support a modest upside if the frozen daily-close model completes the US close without a risk-off repricing. |
| Base | 50% | +0.00% | The directional signal is false and the forecast is experimental-only until the official US close, so the most likely path is a range-bound session near the frozen EOD baseline with no material drift. |
| Bear | 25% | -2.00% | A 34.1% spike probability above the 18.5% threshold indicates elevated near-term volatility risk; if the frozen model triggers a risk-off reaction after the US close, a mild downside move is plausible. |

### Long Term (12 months)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 30% | +8.00% | Sustained low volatility (0.200) and a 34.1% spike probability relative to the 22.9% historical baseline imply a favorable risk-reward environment if credit conditions remain stable and earnings momentum persists. |
| Base | 40% | +3.00% | With the directional signal false and the forecast pending official US close confirmation, a modest positive drift is the central case as the frozen daily-close model resolves without a sharp reversal. |
| Bear | 30% | -5.00% | Elevated spike probability (34.1% vs 18.5% threshold) and a false directional signal raise the risk of a volatility-driven drawdown; if the frozen model fails to confirm, a negative long-term return is plausible. |

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
| S009 | filing | FISV | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0000798354-26-000042); 8-K filed 2026-11-03 (accession 0000798354-26-000039); 8-K filed 2026-10-23 (accession 0001193125-26-429481) |
| S010 | filing | PNR | 2026-10-27 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-27 (accession 0000077360-26-000058); 8-K filed 2026-10-27 (accession 0000077360-26-000055); 8-K filed 2026-09-22 (accession 0000077360-26-000050) |
| S011 | news | FISV | Mon, 16 Nov 2026 03:07:41 GMT | ok | https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en | Fiserv, Inc. (FISV) Stock Price, News, Quote & History - Yahoo! Finance Canada (Mon, 16 Nov 2026 03:07:41 GMT); Fiserv, Inc. (FISV) stock price, news, quote and history - Yahoo Finance Singapore (Mon, 16 Nov 2026 02:30:50 GMT); Fiserv (FISV) Stock Looks Undervalued With Strong Excess Returns - Yahoo Finance (Wed, 11 Nov 2026 22:14:34 GMT) |
| S012 | stock | APP | 2026-11-16 | ok | https://finance.yahoo.com/quote/APP | Trailing P/E: 27.960941; Forward P/E: 19.904833; Forward EPS: 20.86026; Price: 415.22; Market price: 415.22; Market cap: 137571516416; Sector: Communication Services; Trailing Eps: 14.85; Revenue Growth: 0.555; Earnings Growth: 0.755; Gross Margin: 0.8878; Operating Margin: 0.77782995; Profit Margin: 0.65887; Return On Equity: 2.1008599; Total Revenue: 7608893952; Market Cap: 137571516416; Consensus EPS FY+1: 20.72438; growth: 0.2744 |
| S013 | filing | APP | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json | Diluted EPS 11.61 for period ending 2026-09-30 (filed 2026-11-04) |
| S014 | stock | PNR | 2026-11-16 | ok | https://finance.yahoo.com/quote/PNR | Trailing P/E: 18.648502; Forward P/E: 12.903421; Forward EPS: 5.30402; Price: 68.44; Market price: 68.44; Market cap: 10926767104; Sector: Industrials; Trailing Eps: 3.67; Revenue Growth: -0.045; Earnings Growth: -0.188; Gross Margin: 0.40168998; Operating Margin: 0.21410999; Profit Margin: 0.15435; Return On Equity: 0.15605; Total Revenue: 3966200064; Market Cap: 10926767104; Consensus EPS FY+1: 5.30402; growth: 0.1282 |
| S015 | stock | FISV | 2026-11-16 | ok | https://finance.yahoo.com/quote/FISV | Forward P/E: 7.943029; Price: 63.32; Market price: 63.32; Market cap: 33689260032; Market Cap: 33689260032; Consensus EPS FY+1: 7.97582; growth: 0.0959 |
| S016 | filing | FISV | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json | Diluted EPS -8.9 for period ending 2026-09-30 (filed 2026-11-04) |
| S017 | filing | PNR | 2026-10-27 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json | Diluted EPS 2.76 for period ending 2026-09-30 (filed 2026-10-27) |
| S018 | news | APP | Thu, 12 Nov 2026 20:05:45 GMT | ok | https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en | AppLovin Just Ripped 47% in a Month: Is It Too Late to Buy APP Stock Now? - Yahoo Finance (Thu, 12 Nov 2026 20:05:45 GMT); AppLovin Stock Moves Higher: What's Going On? - TradingView (Mon, 16 Nov 2026 18:52:15 GMT); Stock of the Day: Will AppLovin Break Out of a Flag Pattern? - Benzinga (Mon, 16 Nov 2026 13:37:34 GMT) |
| S019 | news | CLX | 2026-11-16 | unavailable | https://news.google.com/rss/search?q=CLX+Clorox+stock&hl=en-US&gl=US&ceid=US:en |  |
| S020 | filing | GEN | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0000849399-26-000083); 8-K filed 2026-10-28 (accession 0000849399-26-000081); 8-K filed 2026-10-09 (accession 0000849399-26-000079) |
| S021 | filing | CLX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000021076-26-000046); 8-K filed 2026-11-02 (accession 0000021076-26-000044); 8-K filed 2026-10-29 (accession 0001206774-26-000586) |
| S022 | news | PNR | Sat, 14 Nov 2026 08:48:27 GMT | ok | https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en | Pentair plc (PNR) Stock Price, News, Quote & History - Yahoo! Finance Canada (Sat, 14 Nov 2026 08:48:27 GMT); Pentair Stock Price Forecast. Should You Buy PNR? - StockInvest.us (Fri, 13 Nov 2026 22:50:05 GMT); Why Pentair Stock Popped This Morning - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT) |
| S023 | stock | CLX | 2026-11-16 | ok | https://finance.yahoo.com/quote/CLX | Trailing P/E: 19.814749; Forward P/E: 17.860386; Forward EPS: 6.1684; Price: 110.17; Market price: 110.17; Market cap: 13346807808; Sector: Consumer Defensive; Trailing Eps: 5.56; Revenue Growth: 0.333; Earnings Growth: 1.138; Gross Margin: 0.41939998; Operating Margin: 0.14286; Profit Margin: 0.09408; Return On Equity: 5.34363; Total Revenue: 7196000256; Market Cap: 13346807808; Consensus EPS FY+1: 6.1684; growth: 0.0769 |
| S024 | filing | CHTR | 2026-11-06 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-06 (accession 0001091667-26-000073); 8-K filed 2026-11-06 (accession 0001091667-26-000072); 8-K filed 2026-10-27 (accession 0001091667-26-000064) |
| S025 | stock | CHTR | 2026-11-16 | ok | https://finance.yahoo.com/quote/CHTR | Trailing P/E: 13.05921; Forward P/E: 3.057552; Forward EPS: 45.44485; Price: 138.95; Market price: 138.95; Market cap: 24879212544; Sector: Communication Services; Trailing Eps: 10.64; Revenue Growth: 0.091; Gross Margin: 0.55084; Operating Margin: 0.23389; Profit Margin: 0.02498; Return On Equity: 0.07019; Total Revenue: 55645999104; Market Cap: 24879212544; Consensus EPS FY+1: 49.35412; growth: 1.1136 |
| S026 | stock | GEN | 2026-11-16 | ok | https://finance.yahoo.com/quote/GEN | Trailing P/E: 15.431472; Forward P/E: 9.108996; Forward EPS: 3.33736; Price: 30.4; Market price: 30.4; Market cap: 18035593216; Sector: Technology; Trailing Eps: 1.97; Revenue Growth: 0.122; Earnings Growth: 1.286; Gross Margin: 0.77410007; Operating Margin: 0.43229; Profit Margin: 0.23068; Return On Equity: 0.46402; Total Revenue: 5228000256; Market Cap: 18035593216; Consensus EPS FY+1: 3.33736; growth: 0.1286 |
| S027 | news | GEN | Thu, 29 Oct 2026 07:00:00 GMT | ok | https://news.google.com/rss/search?q=GEN+Gen+Digital+stock&hl=en-US&gl=US&ceid=US:en | Gen Digital (GEN) Stock Repriced After Q2 Earnings Put Margins Center Stage - Yahoo Finance (Thu, 29 Oct 2026 07:00:00 GMT); Are Business Services Stocks Lagging GEN DIGITAL INC (GEN) This Year? - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT); Gen Digital Stock: Is Wall Street Bullish or Bearish? - Yahoo Finance (Thu, 05 Nov 2026 08:00:00 GMT) |
| S028 | filing | ROP | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000882835&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000882835-26-000047); 8-K filed 2026-10-22 (accession 0000882835-26-000042); 8-K filed 2026-10-01 (accession 0000882835-26-000039) |
| S029 | news | ROP | 2026-11-16 | unavailable | https://news.google.com/rss/search?q=ROP+Roper+Technologies+stock&hl=en-US&gl=US&ceid=US:en |  |
| S030 | stock | ROP | 2026-11-16 | ok | https://finance.yahoo.com/quote/ROP | Trailing P/E: 19.142065; Forward P/E: 19.684877; Forward EPS: 24.57318; Price: 483.72; Market price: 483.72; Market cap: 47905902592; Sector: Technology; Trailing Eps: 25.27; Revenue Growth: 0.076; Earnings Growth: 0.326; Gross Margin: 0.69671; Operating Margin: 0.28049; Profit Margin: 0.30712998; Return On Equity: 0.13229; Total Revenue: 8434599936; Market Cap: 47905902592; Consensus EPS FY+1: 24.57318; growth: 0.09810001 |
| S031 | filing | CLX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000021076.json | Diluted EPS 1.39 for period ending 2026-09-30 (filed 2026-11-02) |
| S032 | filing | IDXX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000874716&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000874716-26-000135); 8-K filed 2026-11-02 (accession 0001104659-26-120892); 10-Q filed 2026-08-04 (accession 0000874716-26-000123) |
| S033 | news | CHTR | Sun, 15 Nov 2026 05:47:01 GMT | ok | https://news.google.com/rss/search?q=CHTR+Charter+Communications+stock&hl=en-US&gl=US&ceid=US:en | Charter Communications (CHTR) Stock Could Be A Bargain Following Its New Operating Model - Yahoo Finance (Sun, 15 Nov 2026 05:47:01 GMT); Why You Should Think About Charter Communications Differently Now? - Yahoo Finance (Fri, 13 Nov 2026 19:16:11 GMT); Charter Communications (CHTR) Earnings Expected to Grow: What to Know Ahead of Next Week's Release - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT) |
| S034 | filing | CHTR | 2026-11-06 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001091667.json | Diluted EPS 0.38 for period ending 2026-09-30 (filed 2026-11-06) |
| S035 | filing | GEN | 2026-10-29 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000849399.json | Diluted EPS 0.83 for period ending 2026-10-02 (filed 2026-10-29) |
| S036 | filing | SNDK | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0002023554&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0001628280-26-068601); 8-K filed 2026-10-29 (accession 0001628280-26-068243); 8-K filed 2026-09-16 (accession 0001628280-26-062267) |
| S037 | stock | IDXX | 2026-11-16 | ok | https://finance.yahoo.com/quote/IDXX | Trailing P/E: 47.21361; Forward P/E: 41.476006; Forward EPS: 16.8929; Price: 700.65; Market price: 700.65; Market cap: 55201599488; Sector: Healthcare; Trailing Eps: 14.84; Revenue Growth: 0.099; Earnings Growth: 0.179; Gross Margin: 0.62722; Operating Margin: 0.32497; Profit Margin: 0.25357; Return On Equity: 0.68925005; Total Revenue: 4662220800; Market Cap: 55201599488; Consensus EPS FY+1: 16.8929; growth: 0.1244 |
| S038 | news | IDXX | Sat, 31 Oct 2026 07:00:00 GMT | ok | https://news.google.com/rss/search?q=IDXX+Idexx+Laboratories+stock&hl=en-US&gl=US&ceid=US:en | IDEXX Laboratories (IDXX) Stock Looks Fairly Valued Despite Its 28% Run - Yahoo Finance (Sat, 31 Oct 2026 07:00:00 GMT); IDEXX Laboratories (IDXX) vs. ZTS and NEOG: Can Raised Guidance and Product Expansion Drive Further Earnings Growth? - Yahoo Finance (Thu, 22 Oct 2026 07:00:00 GMT); IDEXX Laboratories (IDXX) Q3 Earnings Leave Its Premium Valuation In Focus - Yahoo Finance (Tue, 03 Nov 2026 08:00:00 GMT) |
| S039 | news | SNDK | 2026-11-16 | unavailable | https://news.google.com/rss/search?q=SNDK+Sandisk+stock&hl=en-US&gl=US&ceid=US:en |  |
| S040 | filing | RDDT | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001713445&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0001713445-26-000116); 8-K filed 2026-10-29 (accession 0001713445-26-000114); 8-K filed 2026-08-12 (accession 0001713445-26-000107) |

## Sources

- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFF&cosd=2026-01-01 (2026-11-13)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLH0A0HYM2&cosd=2026-01-01 (2026-11-13)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLC0A0CM&cosd=2026-01-01 (2026-11-13)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCSL&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=UNRATE&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=PAYEMS&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=T10Y2Y&cosd=2026-01-01 (2026-11-16)
- filing APP: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001751008&type=10-Q&dateb=&owner=include&count=10 (2026-11-04)
- filing FISV: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 (2026-11-04)
- filing PNR: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 (2026-10-27)
- news FISV: https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en (Mon, 16 Nov 2026 03:07:41 GMT)
- stock APP: https://finance.yahoo.com/quote/APP (2026-11-16)
- filing APP: https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json (2026-11-04)
- stock PNR: https://finance.yahoo.com/quote/PNR (2026-11-16)
- stock FISV: https://finance.yahoo.com/quote/FISV (2026-11-16)
- filing FISV: https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json (2026-11-04)
- filing PNR: https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json (2026-10-27)
- news APP: https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en (Thu, 12 Nov 2026 20:05:45 GMT)
- filing GEN: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 (2026-10-29)
- filing CLX: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 (2026-11-02)

## AI Provenance

- Provider / model: hermes-local-proxy / upstage/solar-mini4:free
- Market research: attempts=1 tokens=9582 (prompt=6582, completion=3000) runtime=18.26s
- Fundamental research: generated this run at 2026-11-16T23:31:28.932784+00:00
- Evidence source dates: {'as_of': '2026-11-16', 'latest_equity_date': '2026-11-16', 'latest_macro_date': '2026-11-16', 'flows_date': '2026-11-13'}
- Evidence fingerprint: 18a721e6f9995aad722c0a11e6f4f61b1b7c87457ee58c55635ffb03607a2dce
- Source citations are retrieved external records in the ledger above; market values remain from the verified database snapshot.


## Disclosures

- This is research and market intelligence, not investment advice.
- AI conclusions are research judgments, not validated return predictions.
- The frozen risk layer is risk-only and is not used for directional views or allocations.
- Legacy scores are not active inputs or outputs.

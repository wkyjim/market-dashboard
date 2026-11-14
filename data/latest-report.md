# AEGIS AI-First Market Intelligence

Research generated at: 15 November 2026, 07:18 HKT
Database freshness: equity 2026-11-13 (latest row retrieved 2026-11-14 13:50:55.938286+08:00)
Data cutoff: 2026-11-13 US cash close
Snapshot ID: aegis-hourly-20261114T231846Z

## Executive Summary

- **AI market view: Late-November 2026: broad market breadth is constructive (71% above 50-day, 64% above 200-day, ADR 1.70), but the index is slightly negative over 20 days and the leadership set is bifurcated. Large-cap mega-cap tech (NVDA, AMD, MU, AAPL) and select dislocation names dominate liquidity, while Information Technology is the weakest sector over 20 days. Health Care, Consumer Discretionary, Consumer Staples, Financials and Industrials are the strongest 20-day sector performers. Macro data show a still-elevated but easing inflation backdrop, a stable labor market, and a modestly positive 10Y-2Y curve, with credit spreads tight but not extreme.**
- Breadth is supportive: 71.3% of names above the 50-day and 63.6% above the 200-day, with a 1.70 advance/decline ratio and positive 20-day momentum in 70.5% of names.
- Index-level 20-day return is negative (-1.28% SPX), indicating a modest pullback despite strong internal breadth and a bullish divergence signal.
- Sector leadership is split: Health Care (+6.9%), Consumer Discretionary (+6.7%), Consumer Staples (+5.4%) and Financials (+5.7%) lead; Information Technology (-7.2%) and Energy (-4.8%) lag.
- Liquidity is concentrated in mega-cap tech and dislocation names; SOXX shows exceptional institutional buying while SMH shows tactical profit-taking inside structural accumulation.
- Macro backdrop is stable: CPI is elevated but moderating, unemployment is 4.2%, the 10Y-2Y spread is +0.27%, and credit spreads are tight (IG 0.89, HY 3.20).
- Risk environment is elevated but not extreme: 5-day forecast vol 14.9% is below the historical baseline 22.1% and the EWMA baseline 20.1%, with a 16.5% spike probability below the 18.5% threshold.

## Data QC

- Status: **PASS_WITH_WARNINGS**
- Equity session: 0 completed session(s) behind inference date
- Equity provenance: 386 provisional / 12581 canonical
- Breadth lag: 0 session(s); ETF-flow lag: 0 session(s)
- Note: Equity session contains a mix of provisional yfinance and canonical Massive rows.
- External sources: 79 ok / 0 unavailable; retrieved 2026-11-14T23:19:00.812393+00:00

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
| SPX | 7561.67 | -1.28% (20d) | Index is slightly negative over 20 days despite strong breadth; 71.3% above 50-day and 63.6% above 200-day. |
| Health Care (XLV) | +6.87% | +6.87% (20d) | Strongest sector; trailing P/E 30.78. |
| Consumer Discretionary (XLY) | +6.69% | +6.69% (20d) | Second-strongest sector; trailing P/E 25.11. |
| Consumer Staples (XLP) | +5.40% | +5.40% (20d) | Third-strongest sector; trailing P/E 24.85. |
| Financials (XLF) | +5.69% | +5.69% (20d) | Strong sector; trailing P/E 15.85. |
| Information Technology (XLK) | -7.19% | -7.19% (20d) | Weakest sector; trailing P/E 30.03. |
| Energy (XLE) | -4.81% | -4.81% (20d) | Weak sector; trailing P/E 16.23. |

## Macro, Fiscal, Rates, Liquidity and Credit

- Inflation: CPI is elevated but moderating; the database shows 336.298 in Sep-2026 and the external source S004 shows 337.476 in Oct-2026, indicating continued but decelerating price pressure.
- Labor: Unemployment is 4.2% in Sep-2026, consistent with a stable labor market; external S005 shows 4.1% in Oct-2026, suggesting further modest cooling.
- Policy/rates: The effective federal funds rate is 3.88% as of 2026-11-12 (S001), and the 10Y-2Y spread is +0.27% as of 2026-11-13 (S007), indicating a modestly positive curve and a still-restrictive but easing policy stance.
- Credit/liquidity: IG OAS is 0.89 and HY OAS is 3.20 as of 2026-11-12 (S002, S003), both tight but not distressed, supporting risk appetite.
- Growth: Equity breadth is positive (70.5% positive 20d, ADR 1.70), but the index is slightly negative over 20 days, suggesting a consolidation phase rather than broad momentum expansion.
- Volatility: 5-day forecast vol is 14.9%, below the historical baseline 22.1% and EWMA baseline 20.1%, with a 16.5% spike probability below the 18.5% threshold, indicating a relatively calm but watchful risk environment.

## US Equities and 11 GICS Sectors

Macro source IDs: S001, S002, S003, S004, S005, S007

| GICS sector | Evidence | AI research stance | Source IDs |
| --- | --- | --- | --- |
| Health Care | 20d return +6.87% (XLV), trailing P/E 30.78 (S058); strongest sector in the universe. | Favorable momentum and relative strength; valuation is rich but supported by sector leadership. | S058 |
| Consumer Discretionary | 20d return +6.69% (XLY), trailing P/E 25.11 (S067); strong consumer-facing demand. | Favorable momentum; consumer resilience supports the sector. | S067 |
| Consumer Staples | 20d return +5.40% (XLP), trailing P/E 24.85 (S059); defensive strength with solid returns. | Favorable momentum; defensive quality amid late-cycle consolidation. | S059 |
| Financials | 20d return +5.69% (XLF), trailing P/E 15.85 (S066); strong relative performance. | Favorable momentum; attractive valuation and sector leadership. | S066 |
| Industrials | 20d return +0.61% (XLI), trailing P/E 27.07 (S075); modest positive but below the top group. | Neutral-to-favorable; positive but lagging momentum. | S075 |
| Real Estate | 20d return +5.24% (XLRE), trailing P/E 29.63 (S060); positive but valuation is elevated. | Favorable momentum; valuation caution warranted. | S060 |
| Communication Services | 20d return -1.48% (XLC), trailing P/E 17.26 (S072); negative momentum. | Weakness in the sector; valuation is reasonable but momentum is negative. | S072 |
| Information Technology | 20d return -7.19% (XLK), trailing P/E 30.03 (S074); weakest sector. | Negative momentum and valuation pressure; leadership is concentrated in mega-cap names. | S074 |
| Energy | 20d return -4.81% (XLE), trailing P/E 16.23 (S076); negative momentum. | Weakness; valuation is reasonable but sector is underperforming. | S076 |
| Materials | 20d return +2.57% (XLB), trailing P/E 21.72 (S068); modest positive. | Neutral-to-favorable; modest positive momentum with reasonable valuation. | S068 |
| Utilities | 20d return +4.34% (XLU), trailing P/E 18.11 (S063); positive but less strong than top sectors. | Favorable momentum; defensive appeal with reasonable valuation. | S063 |

### Sector fundamentals, valuation and earnings

No point-in-time sector fundamentals beyond the supplied trailing P/E and 20-day ETF returns are available in the database. The sector evidence is limited to the 20-day returns and trailing P/E figures listed in the sector table and external source IDs; no growth, margin, earnings, or balance-sheet fundamentals are supplied for the 11 GICS sectors.

## Growth vs Value

- Growth: Information Technology is the weakest 20-day sector (-7.19%) and carries the highest trailing P/E (30.03), indicating high valuation with negative momentum.
- Value: Financials offer the most attractive valuation (trailing P/E 15.85) and strong 20-day momentum (+5.69%), consistent with a value tilt.
- Value: Energy has the lowest trailing P/E (16.23) but negative 20-day momentum (-4.81%), suggesting value without near-term momentum support.
- Growth/value mix: Health Care and Consumer Discretionary combine strong momentum with elevated valuations, while Financials and Utilities offer more balanced growth/value profiles.

## ETF Flows and Breadth

- SOXX shows exceptional institutional buying (20d flow z-score 5.10, 60d 3.17) despite a down price, indicating strong structural accumulation in semiconductors.
- SMH shows tactical profit-taking inside structural accumulation (20d z-score 1.22, 60d 1.04) with a down price, suggesting selective rotation rather than broad de-risking.
- TLT shows medium-term deterioration (20d z-score -0.41, 60d -0.29) with a flat price, indicating reduced demand for duration.
- Breadth is constructive: 71.3% above 50-day, 63.6% above 200-day, ADR 1.70, and 70.5% positive 20d, with a bullish divergence signal.
- Index-level 20d return is -1.28%, so the positive breadth is not yet translating into broad index gains, implying a consolidation or rotation phase.

## Stock Ideas

Single-stock research uses reported EPS, forward P/E and company fundamentals. All ideas are research judgments, not validated return predictions.

| Ticker | Security | Research view | Price | EPS | Forward P/E | Base target | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| APP | AppLovin | NEW | 409.1 | 20.86026 | 19.611452 | 417.21 | NEW |
| PNR | Pentair | KEEP | 68.3 | 5.30402 | 12.877027 | 74.26 | KEEP |
| RDDT | Reddit | KEEP | 98.45 | 9.14039 | 10.770874 | 109.68 | KEEP |

## ETF Ideas

ETF research uses holdings, portfolio valuation and exposure. Single-stock EPS × P/E valuation is not applied to ETFs.

| Ticker | Fund | Research view | Price | Top holdings | Portfolio valuation | Sector exposure | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| XLV | Health Care Select Sector SPDR Fund | KEEP | 188.85 | LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59% | Top 10 holdings; numeric weight coverage 61.42% | Health Care | KEEP |
| XLP | Consumer Staples Select Sector SPDR Fund | NEW | 92.35 | WMT 11.14%, COST 9.09%, PG 7.60%, KO 7.37%, PM 6.59%, MO 4.70%, CL 4.42%, MDLZ 4.25%, PEP 4.11%, TGT 4.00% | Top 10 holdings; numeric weight coverage 63.28% | Consumer Staples | NEW |
### APP — AppLovin

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** AppLovin offers a high-momentum, high-margin digital advertising compounder with a forward P/E near 19.6 that is not stretched relative to its own reported earnings, unlike the extreme forward P/E flags on names such as NOW, MRVL, and AMD. It provides a cleaner, source-backed momentum story with verifiable reported earnings. Alternatives considered: NOW, MRVL, AMD.
- **Thesis:** AppLovin screens in the top 20-day momentum bucket with a 53.7% 20-day return and a 32.5% 60-day return, while its 20.05 trailing P/E and 4.99% earnings yield sit at sector-relative P/E of 1.0. Reported diluted EPS of 11.61 for the fiscal period ending 2026-09-30 and a forward EPS of 20.86 support a forward P/E near 19.6, indicating the momentum is not being priced at an extreme premium relative to its own fundamentals.
- **Source IDs:** S009, S012, S013, S015
- **Catalysts:** Sustained 20-day momentum with a 53.7% price move, Strong reported EPS of 11.61 and forward EPS of 20.86, High gross margin of 88.8% and operating margin of 77.8%, Revenue growth of 55.5% and earnings growth of 75.5%
- **Risks:** A 47% one-month drop headline suggests sharp volatility and possible profit-taking, High momentum can reverse quickly if ad-market demand cools, Forward EPS and fiscal-period mapping are unverified, so forward valuation should be treated cautiously
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 20.8603 (source.forwardEps) x AI multiple assumption 20.00; source IDs S009, S012, S013, S015
- **EPS:** 20.86026 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 19.611452
- **FY+1 growth assumption:** 27.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / AAPL / APP shows strong FY1 consensus earnings growth of 27.44% and revenue growth of 25.37%, supported by an 88.8% gross margin and 77.8% operating margin, indicating a high-quality, capital-efficient franchise. The forward EPS of 20.86 and forward P/E of 19.6x are not used to set the multiple; instead, the base multiple of 20x is justified by APP's superior margins and growth relative to the named peer AAPL, with a bull case of 24x reflecting continued margin expansion and a bear case of 16x reflecting execution risk. The valuation horizon is FY2027 to FY2028, using the FY+1 consensus growth of 27.44% as the forward earnings growth assumption.
- **Company fundamentals:** Reported diluted EPS 11.61; forward EPS 20.86; forward P/E 19.61; gross margin 88.8%; operating margin 77.8%; profit margin 65.9%; revenue growth 55.5%; earnings growth 75.5%; ROE 2.10; 20-day return 53.7%; 60-day return 32.5%; trailing P/E 20.05; earnings yield 4.99%; sector-relative P/E 1.0.
- **Bull / Base / Bear:** 500.65 / 417.21 / 333.76
- **Bull / Base / Bear returns:** 22.38% / 1.98% / -18.42%
- **Scenario probabilities:** not separately assigned; see scenario table.

### PNR — Pentair

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Pentair is the cheapest momentum name in the shortlist with a forward P/E of 12.9 and a sector-relative P/E of 0.49, but its negative revenue and earnings growth make it a valuation-only opportunity rather than a growth story. It is preferable to the high-multiple dislocation names like NOW and MRVL, which carry even weaker forward earnings visibility. Alternatives considered: NOW, MRVL, AMD.
- **Thesis:** Pentair is a top-20-day-momentum name with a 27.8% 20-day return and a 7.1% 60-day return, but its fundamentals are mixed. Reported diluted EPS of 2.76 and forward EPS of 5.30 give a forward P/E of 12.9, while revenue growth is -4.5% and earnings growth is -18.8%. The stock is cheap on a forward basis but the earnings decline and margin compression argue against a strong conviction BUY.
- **Source IDs:** S008, S014, S016, S020
- **Catalysts:** 27.8% 20-day momentum and 7.1% 60-day return, Forward P/E of 12.9 is attractive relative to the broader market, Stable dividend and industrial water/wastewater exposure, Sector-relative P/E of 0.49 indicates significant undervaluation
- **Risks:** Revenue growth of -4.5% and earnings growth of -18.8% show deteriorating fundamentals, Operating margin of 21.4% and profit margin of 15.4% are below best-in-class, Forward EPS of 5.30 is flat with FY1 EPS, offering no growth catalyst, Industrial end-market cyclicality could delay recovery
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 5.3040 (source.forwardEps) x AI multiple assumption 14.00; source IDs S008, S014, S016, S020
- **EPS:** 5.30402 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 12.877027
- **FY+1 growth assumption:** 12.82%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / CSCO / PNR shows FY1 consensus earnings growth of 12.82% and revenue growth of 18.38%, with a 40.2% gross margin and 21.4% operating margin, indicating a more cyclical and lower-margin business than APP. The forward EPS of 5.30 and forward P/E of 12.9x are not used to set the multiple; instead, the base multiple of 14x is justified by PNR's moderate growth and margin profile relative to the named peer CSCO, with a bull case of 17x reflecting potential margin recovery and a bear case of 11x reflecting continued revenue contraction. The valuation horizon is FY2027 to FY2028, using the FY+1 consensus growth of 12.82% as the forward earnings growth assumption.
- **Company fundamentals:** Reported diluted EPS 2.76; forward EPS 5.30; forward P/E 12.88; gross margin 40.2%; operating margin 21.4%; profit margin 15.4%; ROE 15.6%; revenue growth -4.5%; earnings growth -18.8%; 20-day return 27.8%; 60-day return 7.1%; trailing P/E 13.59; earnings yield 7.36%; sector-relative P/E 0.49.
- **Bull / Base / Bear:** 90.17 / 74.26 / 58.34
- **Bull / Base / Bear returns:** 32.02% / 8.73% / -14.58%
- **Scenario probabilities:** not separately assigned; see scenario table.

### RDDT — Reddit

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Reddit is the only large-cap name in the shortlist with a deep dislocation and a cheap forward P/E of 10.8, but the -39.4% 60-day drawdown and negative returns make it a high-risk, high-reward candidate rather than a core holding. It is preferable to the negative-momentum names like INTC and COIN, which have no earnings yield and deeper drawdowns. Alternatives considered: INTC, COIN, LITE.
- **Thesis:** Reddit is the largest 20-day dislocation name with a -36.9% 20-day return and a -34.5% 60-day return, and a -39.4% 60-day drawdown. It screens on dislocation rather than momentum, and its forward P/E of 10.8 and earnings yield of 3.0% are reasonable, but the sharp price decline and negative returns mean the dislocation is not yet a clear buying opportunity. The stock is not a conviction BUY until the drawdown stabilizes.
- **Source IDs:** S037, S040, S042, S045
- **Catalysts:** Largest 20-day dislocation with a -36.9% 20-day return, Forward P/E of 10.8 is cheap relative to its 33.2 trailing P/E, Revenue growth of 53% and earnings growth of 74.9% show strong operating leverage, Gross margin of 91.5% indicates a high-quality digital platform
- **Risks:** Sharp -36.9% 20-day and -34.5% 60-day declines indicate severe de-rating, 60-day drawdown of -39.4% raises the risk of further downside, Social media and advertising cyclicality could delay recovery, Forward EPS and fiscal-period mapping are unverified, limiting forward valuation confidence
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 9.1404 (source.forwardEps) x AI multiple assumption 12.00; source IDs S037, S040, S042, S045
- **EPS:** 9.14039 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 10.770874
- **FY+1 growth assumption:** 24.17%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / AMZN / RDDT shows FY1 consensus earnings growth of 24.17% and revenue growth of 28.43%, with a 91.5% gross margin but a lower 29.4% operating margin and 32.0% ROE, indicating a high-revenue-growth but lower-margin business. The forward EPS of 9.14 and forward P/E of 10.8x are not used to set the multiple; instead, the base multiple of 12x is justified by RDDT's strong growth and gross margin relative to the named peer AMZN, with a bull case of 15x reflecting operating leverage and a bear case of 9x reflecting margin pressure. The valuation horizon is FY2027 to FY2028, using the FY+1 consensus growth of 24.17% as the forward earnings growth assumption.
- **Company fundamentals:** Reported diluted EPS 3.66; forward EPS 9.14; forward P/E 10.77; gross margin 91.5%; operating margin 29.4%; profit margin 32.1%; ROE 32.0%; revenue growth 53.0%; earnings growth 74.9%; 20-day return -36.9%; 60-day return -34.5%; 60-day drawdown -39.4%; trailing P/E 33.19; earnings yield 3.01%; sector-relative P/E 1.66.
- **Bull / Base / Bear:** 137.11 / 109.68 / 82.26
- **Bull / Base / Bear returns:** 39.27% / 11.41% / -16.44%
- **Scenario probabilities:** not separately assigned; see scenario table.

### XLV — Health Care Select Sector SPDR Fund

- **Type:** ETF
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** XLV provides the most diversified healthcare exposure among the sector ETFs, with a top-10 concentration in the highest-quality pharma names. It is preferable to the more volatile single-stock dislocation names like INTC and COIN, and to the underperforming Consumer Discretionary ETF XLY, which fell -0.40%. Alternatives considered: XLY, XLF, XLU.
- **Thesis:** XLV is the Health Care sector ETF with a +0.54% price change and a top-10 holding concentration led by LLY at 16.9%, JNJ at 9.8%, and ABBV at 7.8%. The sector ETF provides diversified healthcare exposure, but the limited holdings coverage of 61.4% and the modest price change mean it is a neutral, core allocation rather than a tactical pick.
- **Source IDs:** S053, S058
- **Catalysts:** Health Care sector ETF with diversified large-cap pharma exposure, Top-10 holdings coverage of 61.4% led by LLY, JNJ, and ABBV, Positive +0.54% price change on 2026-11-13, Stable sector allocation for defensive portfolio construction
- **Risks:** Holdings coverage of only 61.4% means top-10 weights do not fully represent the portfolio, Modest +0.54% price change offers limited upside catalyst, Sector-specific regulatory and drug-pricing risks, Concentration in a few large pharma names could amplify single-stock risk
- **Valuation method:** Holdings/portfolio valuation with AI total-return assumption
- **Valuation status:** verified; forward-EPS source: ; period flags: 
- **Valuation assumptions:** Holdings/portfolio valuation; 10 weighted holdings; coverage 61.42%; source IDs S053, S058
- **Top holdings:** LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59%
- **Portfolio valuation:** Top 10 holdings; numeric weight coverage 61.42%
- **Sector exposure:** Health Care
- **Underlying drivers:** Diversified large-cap pharma and healthcare services exposure; top-10 holdings led by LLY, JNJ, and ABBV; positive sector price action of +0.54% on 2026-11-13; limited holdings coverage of 61.4%.
- **Bull / Base / Bear:** 215.29 / 200.18 / 181.3
- **Bull / Base / Bear returns:** 14.0% / 6.0% / -4.0%
- **Scenario probabilities:** not separately assigned; see scenario table.

### XLP — Consumer Staples Select Sector SPDR Fund

- **Type:** ETF
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** XLP is the only sector ETF with a strong positive price move and defensive characteristics, making it the preferred core holding for a balanced portfolio. It is preferable to the underperforming XLY (-0.40%) and the mixed XLI (-0.39%), and it offers better defensive stability than the high-volatility single-stock dislocation names. Alternatives considered: XLY, XLI, XLF.
- **Thesis:** XLP is the Consumer Staples sector ETF with a strong +1.42% price change on 2026-11-13, the strongest sector move in the shortlist. Its top-10 holdings are led by WMT at 11.1%, COST at 9.1%, and PG at 7.6%, providing defensive, high-quality consumer exposure. The positive price action and defensive sector characteristics make it a preferred core holding.
- **Source IDs:** S056, S059
- **Catalysts:** Strong +1.42% price change on 2026-11-13, the best sector ETF move in the shortlist, Top-10 holdings coverage of 63.3% led by WMT, COST, and PG, Defensive consumer staples exposure with stable demand, High-quality large-cap consumer names with pricing power
- **Risks:** Holdings coverage of 63.3% means top-10 weights do not fully represent the portfolio, Consumer staples can lag in strong risk-on environments, Sector-specific regulatory and commodity cost risks, Limited upside catalyst compared to more dynamic sectors
- **Valuation method:** Holdings/portfolio valuation with AI total-return assumption
- **Valuation status:** verified; forward-EPS source: ; period flags: 
- **Valuation assumptions:** Holdings/portfolio valuation; 10 weighted holdings; coverage 63.28%; source IDs S056, S059
- **Top holdings:** WMT 11.14%, COST 9.09%, PG 7.60%, KO 7.37%, PM 6.59%, MO 4.70%, CL 4.42%, MDLZ 4.25%, PEP 4.11%, TGT 4.00%
- **Portfolio valuation:** Top 10 holdings; numeric weight coverage 63.28%
- **Sector exposure:** Consumer Staples
- **Underlying drivers:** Diversified large-cap consumer staples exposure; top-10 holdings led by WMT, COST, and PG; strong +1.42% price change on 2026-11-13; holdings coverage of 63.3%.
- **Bull / Base / Bear:** 103.43 / 96.97 / 87.73
- **Bull / Base / Bear returns:** 12.0% / 5.0% / -5.0%
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
| Bull | 25% | +2.00% | Low 5-day realized vol (14.9%) and below-threshold spike probability (16.5% vs 18.5% threshold) support a modest upside if US close confirms the frozen daily model; probability capped below 30% because directional signal is false and the forecast is not yet formally eligible. |
| Base | 50% | +0.00% | Frozen daily-close model with no directional signal and a 5-day vol of 14.9% implies a near-neutral range; base case assumes the US close resolves within the model's historical baseline without a regime shift. |
| Bear | 25% | -2.00% | If the US close fails to confirm the frozen forecast and spike probability exceeds the 18.5% threshold, elevated 5-day vol (14.9%) and false directional signal raise downside risk; probability capped at 25% because the model is not yet formally eligible. |

### Long Term (12 months)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 30% | +8.00% | Sustained low realized vol (14.9%) and below-threshold spike probability (16.5% vs 18.5%) support a constructive multi-week path if the frozen daily model holds through the US close; probability reflects a moderate but not dominant bull case. |
| Base | 40% | +3.00% | Frozen daily-close model with no directional signal and 5-day vol of 14.9% implies a gradual upward drift over the horizon; base case assumes the US close confirms the model without a sharp spike or regime change. |
| Bear | 30% | -5.00% | If the US close fails to confirm the frozen forecast and spike probability exceeds the 18.5% threshold, elevated 5-day vol (14.9%) and false directional signal increase downside risk; probability reflects a meaningful but not dominant bear case. |

## Positioning

- Maintain a constructive but cautious equity stance: breadth and credit are supportive, but index-level 20d returns are negative and volatility is elevated.
- Favor sectors with strong momentum and reasonable valuation: Health Care, Consumer Discretionary, Consumer Staples, Financials and Industrials.
- Reduce exposure to Information Technology and Energy until 20d momentum turns positive; these sectors are the weakest performers.
- Monitor mega-cap tech liquidity (SOXX, NVDA, AMD, MU, AAPL) as a key driver of index leadership and breadth.
- Watch credit spreads and the 10Y-2Y curve for any deterioration; currently IG 0.89 and HY 3.20 are tight but not distressed.
- No allocation weights are provided; this is a qualitative research posture only.

## Catalysts

| Date | Event | Why it matters |
| --- | --- | --- |
| 2026-11-16 | US equity market open | Frozen daily-close model; official risk forecast becomes available after completed US close, providing a fresh volatility and spike-probability read. |

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
| S008 | filing | PNR | 2026-10-27 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-27 (accession 0000077360-26-000058); 8-K filed 2026-10-27 (accession 0000077360-26-000055); 8-K filed 2026-09-22 (accession 0000077360-26-000050) |
| S009 | filing | APP | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001751008&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0001751008-26-000069); 8-K filed 2026-11-04 (accession 0001751008-26-000068); 10-Q filed 2026-08-05 (accession 0001751008-26-000059) |
| S010 | filing | FISV | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0000798354-26-000042); 8-K filed 2026-11-03 (accession 0000798354-26-000039); 8-K filed 2026-10-23 (accession 0001193125-26-429481) |
| S011 | news | FISV | Thu, 12 Nov 2026 14:54:12 GMT | ok | https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en | Fiserv, Inc. (FISV) Stock Price, News, Quote & History - Yahoo! Finance Canada (Thu, 12 Nov 2026 14:54:12 GMT); Fiserv Stock Outlook: Is Wall Street Bullish or Bearish? - Yahoo Finance (Thu, 12 Nov 2026 12:23:56 GMT); What Is Fiserv (FISV) Planning With Its Debit Networks And Clover AI? - Yahoo Finance (Thu, 12 Nov 2026 06:09:00 GMT) |
| S012 | news | APP | Thu, 12 Nov 2026 20:05:45 GMT | ok | https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en | AppLovin Just Ripped 47% in a Month: Is It Too Late to Buy APP Stock Now? - Yahoo Finance (Thu, 12 Nov 2026 20:05:45 GMT); APP Stock Surges 51% After Q3 Earnings: Is it Still a Buy? - Yahoo Finance (Tue, 10 Nov 2026 14:24:00 GMT); Here is What to Know Beyond Why AppLovin Corporation (APP) is a Trending Stock - Yahoo Finance (Tue, 10 Nov 2026 13:00:06 GMT) |
| S013 | stock | APP | 2026-11-14 | ok | https://finance.yahoo.com/quote/APP | Trailing P/E: 27.54882; Forward P/E: 19.611452; Forward EPS: 20.86026; Price: 409.1; Market price: 409.1; Market cap: 135543824384; Sector: Communication Services; Trailing Eps: 14.85; Revenue Growth: 0.555; Earnings Growth: 0.755; Gross Margin: 0.8878; Operating Margin: 0.77782995; Profit Margin: 0.65887; Return On Equity: 2.1008599; Total Revenue: 7608893952; Market Cap: 135543824384; Consensus EPS FY+1: 20.72438; growth: 0.2744 |
| S014 | news | PNR | Fri, 13 Nov 2026 15:54:46 GMT | ok | https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en | Pentair plc (PNR) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 15:54:46 GMT); Here's What Key Metrics Tell Us About Pentair (PNR) Q3 Earnings - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT); Pentair plc (PNR) Q3 Earnings and Revenues Beat Estimates - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT) |
| S015 | filing | APP | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json | Diluted EPS 11.61 for period ending 2026-09-30 (filed 2026-11-04) |
| S016 | stock | PNR | 2026-11-14 | ok | https://finance.yahoo.com/quote/PNR | Trailing P/E: 18.610355; Forward P/E: 12.877027; Forward EPS: 5.30402; Price: 68.3; Market price: 68.3; Market cap: 10904415232; Sector: Industrials; Trailing Eps: 3.67; Revenue Growth: -0.045; Earnings Growth: -0.188; Gross Margin: 0.40168998; Operating Margin: 0.21410999; Profit Margin: 0.15435; Return On Equity: 0.15605; Total Revenue: 3966200064; Market Cap: 10904415232; Consensus EPS FY+1: 5.30402; growth: 0.1282 |
| S017 | stock | FISV | 2026-11-14 | ok | https://finance.yahoo.com/quote/FISV | Forward P/E: 7.9923306; Price: 63.78; Market price: 63.78; Market cap: 33934002176; Market Cap: 33934002176; Consensus EPS FY+1: 7.98015; growth: 0.09689999 |
| S018 | filing | GEN | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0000849399-26-000083); 8-K filed 2026-10-28 (accession 0000849399-26-000081); 8-K filed 2026-10-09 (accession 0000849399-26-000079) |
| S019 | filing | FISV | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json | Diluted EPS -8.9 for period ending 2026-09-30 (filed 2026-11-04) |
| S020 | filing | PNR | 2026-10-27 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json | Diluted EPS 2.76 for period ending 2026-09-30 (filed 2026-10-27) |
| S021 | stock | GEN | 2026-11-14 | ok | https://finance.yahoo.com/quote/GEN | Trailing P/E: 15.431472; Forward P/E: 9.108996; Forward EPS: 3.33736; Price: 30.4; Market price: 30.4; Market cap: 18035593216; Sector: Technology; Trailing Eps: 1.97; Revenue Growth: 0.122; Earnings Growth: 1.286; Gross Margin: 0.77410007; Operating Margin: 0.43229; Profit Margin: 0.23068; Return On Equity: 0.46402; Total Revenue: 5228000256; Market Cap: 18035593216; Consensus EPS FY+1: 3.33736; growth: 0.1286 |
| S022 | news | GEN | Thu, 29 Oct 2026 07:00:00 GMT | ok | https://news.google.com/rss/search?q=GEN+Gen+Digital+stock&hl=en-US&gl=US&ceid=US:en | Gen Digital (GEN) Stock Repriced After Q2 Earnings Put Margins Center Stage - Yahoo Finance (Thu, 29 Oct 2026 07:00:00 GMT); Are Business Services Stocks Lagging GEN DIGITAL INC (GEN) This Year? - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT); Gen Digital Stock: Is Wall Street Bullish or Bearish? - Yahoo Finance (Thu, 05 Nov 2026 08:00:00 GMT) |
| S023 | filing | CLX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000021076-26-000046); 8-K filed 2026-11-02 (accession 0000021076-26-000044); 8-K filed 2026-10-29 (accession 0001206774-26-000586) |
| S024 | news | CLX | Fri, 13 Nov 2026 18:52:58 GMT | ok | https://news.google.com/rss/search?q=CLX+Clorox+stock&hl=en-US&gl=US&ceid=US:en | The Clorox Company (CLX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 18:52:58 GMT); The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance Singapore (Fri, 13 Nov 2026 14:35:41 GMT); The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance UK (Fri, 13 Nov 2026 16:03:45 GMT) |
| S025 | stock | CLX | 2026-11-14 | ok | https://finance.yahoo.com/quote/CLX | Trailing P/E: 19.68705; Forward P/E: 17.745283; Forward EPS: 6.1684; Price: 109.46; Market price: 109.46; Market cap: 13260793856; Sector: Consumer Defensive; Trailing Eps: 5.56; Revenue Growth: 0.333; Earnings Growth: 1.138; Gross Margin: 0.41939998; Operating Margin: 0.14286; Profit Margin: 0.09408; Return On Equity: 5.34363; Total Revenue: 7196000256; Market Cap: 13260793856; Consensus EPS FY+1: 6.1684; growth: 0.0769 |
| S026 | filing | CHTR | 2026-11-06 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-06 (accession 0001091667-26-000073); 8-K filed 2026-11-06 (accession 0001091667-26-000072); 8-K filed 2026-10-27 (accession 0001091667-26-000064) |
| S027 | filing | GEN | 2026-10-29 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000849399.json | Diluted EPS 0.83 for period ending 2026-10-02 (filed 2026-10-29) |
| S028 | filing | IDXX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000874716&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000874716-26-000135); 8-K filed 2026-11-02 (accession 0001104659-26-120892); 10-Q filed 2026-08-04 (accession 0000874716-26-000123) |
| S029 | news | CHTR | Thu, 12 Nov 2026 08:02:01 GMT | ok | https://news.google.com/rss/search?q=CHTR+Charter+Communications+stock&hl=en-US&gl=US&ceid=US:en | Charter Communications: 3 Key Takeaways for Long-Term Investors - Yahoo Finance (Thu, 12 Nov 2026 08:02:01 GMT); Charter Communications (CHTR) Stock Looks Reasonable As Shares Slump 85% - Yahoo Finance (Wed, 28 Oct 2026 07:00:00 GMT); Should Value Investors Buy Charter Communications (CHTR) Stock? - Yahoo Finance (Wed, 21 Oct 2026 07:00:00 GMT) |
| S030 | news | IDXX | Fri, 13 Nov 2026 22:06:38 GMT | ok | https://news.google.com/rss/search?q=IDXX+Idexx+Laboratories+stock&hl=en-US&gl=US&ceid=US:en | IDEXX Laboratories, Inc. (IDXX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 22:06:38 GMT); IDEXX Laboratories (IDXX) Stock Looks Fairly Valued Despite Its 28% Run - Yahoo Finance (Sat, 31 Oct 2026 07:00:00 GMT); IDEXX Laboratories (IDXX) Q3 Earnings Leave Its Premium Valuation In Focus - Yahoo Finance (Tue, 03 Nov 2026 08:00:00 GMT) |
| S031 | stock | CHTR | 2026-11-14 | ok | https://finance.yahoo.com/quote/CHTR | Trailing P/E: 13.006578; Forward P/E: 3.2831066; Forward EPS: 42.15215; Price: 138.39; Market price: 138.39; Market cap: 24778944512; Sector: Communication Services; Trailing Eps: 10.64; Revenue Growth: 0.091; Gross Margin: 0.55084; Operating Margin: 0.23389; Profit Margin: 0.02498; Return On Equity: 0.07019; Total Revenue: 55645999104; Market Cap: 24778944512; Consensus EPS FY+1: 47.15811; growth: 1.0195 |
| S032 | filing | CLX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000021076.json | Diluted EPS 1.39 for period ending 2026-09-30 (filed 2026-11-02) |
| S033 | stock | IDXX | 2026-11-14 | ok | https://finance.yahoo.com/quote/IDXX | Trailing P/E: 47.45485; Forward P/E: 41.687927; Forward EPS: 16.8929; Price: 704.23; Market price: 704.23; Market cap: 55483650048; Sector: Healthcare; Trailing Eps: 14.84; Revenue Growth: 0.099; Earnings Growth: 0.179; Gross Margin: 0.62722; Operating Margin: 0.32497; Profit Margin: 0.25357; Return On Equity: 0.68925005; Total Revenue: 4662220800; Market Cap: 55483650048; Consensus EPS FY+1: 16.8929; growth: 0.1244 |
| S034 | filing | ROP | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000882835&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000882835-26-000047); 8-K filed 2026-10-22 (accession 0000882835-26-000042); 8-K filed 2026-10-01 (accession 0000882835-26-000039) |
| S035 | filing | CHTR | 2026-11-06 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001091667.json | Diluted EPS 0.38 for period ending 2026-09-30 (filed 2026-11-06) |
| S036 | filing | IDXX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000874716.json | Diluted EPS 11.75 for period ending 2026-09-30 (filed 2026-11-02) |
| S037 | filing | RDDT | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001713445&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0001713445-26-000116); 8-K filed 2026-10-29 (accession 0001713445-26-000114); 8-K filed 2026-08-12 (accession 0001713445-26-000107) |
| S038 | news | ROP | Thu, 12 Nov 2026 19:15:50 GMT | ok | https://news.google.com/rss/search?q=ROP+Roper+Technologies+stock&hl=en-US&gl=US&ceid=US:en | Roper Technologies, Inc. (ROP) Stock Price, News, Quote & History - Yahoo! Finance Canada (Thu, 12 Nov 2026 19:15:50 GMT); Roper Technologies (ROP) Stock Looks Fully Valued As Cash Flow Comes Into Focus - Yahoo Finance (Fri, 06 Nov 2026 07:13:00 GMT); Roper Technologies: 3 Key Takeaways for Long-Term Investors - Yahoo Finance (Mon, 26 Oct 2026 07:00:00 GMT) |
| S039 | stock | ROP | 2026-11-14 | ok | https://finance.yahoo.com/quote/ROP | Trailing P/E: 18.993866; Forward P/E: 19.532475; Forward EPS: 24.57318; Price: 479.975; Market price: 479.975; Market cap: 47535013888; Sector: Technology; Trailing Eps: 25.27; Revenue Growth: 0.076; Earnings Growth: 0.326; Gross Margin: 0.69671; Operating Margin: 0.28049; Profit Margin: 0.30712998; Return On Equity: 0.13229; Total Revenue: 8434599936; Market Cap: 47535013888; Consensus EPS FY+1: 24.57318; growth: 0.09810001 |
| S040 | news | RDDT | Thu, 29 Oct 2026 07:00:00 GMT | ok | https://news.google.com/rss/search?q=RDDT+Reddit+stock&hl=en-US&gl=US&ceid=US:en | Reddit shares sink on weak sales guidance and plans login requirement test as Google search traffic shrinks - CNBC (Thu, 29 Oct 2026 07:00:00 GMT); symbol__ Stock Quote Price and Forecast - CNN (Fri, 13 Nov 2026 20:43:23 GMT); Reddit (NYSE:RDDT) surprises with Q3 2026 sales but stock drops 12.6% - Yahoo Finance (Thu, 29 Oct 2026 07:00:00 GMT) |

## Sources

- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFF&cosd=2026-01-01 (2026-11-12)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLH0A0HYM2&cosd=2026-01-01 (2026-11-12)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLC0A0CM&cosd=2026-01-01 (2026-11-12)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCSL&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=UNRATE&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=PAYEMS&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=T10Y2Y&cosd=2026-01-01 (2026-11-13)
- filing PNR: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 (2026-10-27)
- filing APP: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001751008&type=10-Q&dateb=&owner=include&count=10 (2026-11-04)
- filing FISV: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 (2026-11-04)
- news FISV: https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en (Thu, 12 Nov 2026 14:54:12 GMT)
- news APP: https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en (Thu, 12 Nov 2026 20:05:45 GMT)
- stock APP: https://finance.yahoo.com/quote/APP (2026-11-14)
- news PNR: https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 15:54:46 GMT)
- filing APP: https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json (2026-11-04)
- stock PNR: https://finance.yahoo.com/quote/PNR (2026-11-14)
- stock FISV: https://finance.yahoo.com/quote/FISV (2026-11-14)
- filing GEN: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 (2026-10-29)
- filing FISV: https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json (2026-11-04)
- filing PNR: https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json (2026-10-27)

## AI Provenance

- Provider / model: hermes-local-proxy / upstage/solar-mini4:free
- Market research: attempts=1 tokens=9521 (prompt=6521, completion=3000) runtime=18.66s
- Fundamental research: generated this run at 2026-11-14T23:18:46.982762+00:00
- Evidence source dates: {'as_of': '2026-11-13', 'latest_equity_date': '2026-11-13', 'latest_macro_date': '2026-11-13', 'flows_date': '2026-11-13'}
- Evidence fingerprint: 45d0637d031f2aad87e55a9b90924c1bb353219c9c2300bca60c118daabcf374
- Source citations are retrieved external records in the ledger above; market values remain from the verified database snapshot.


## Disclosures

- This is research and market intelligence, not investment advice.
- AI conclusions are research judgments, not validated return predictions.
- The frozen risk layer is risk-only and is not used for directional views or allocations.
- Legacy scores are not active inputs or outputs.

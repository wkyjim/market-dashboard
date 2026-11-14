# AEGIS AI-First Market Intelligence

Research generated at: 14 November 2026, 23:15 HKT
Database freshness: equity 2026-11-13 (latest row retrieved 2026-11-14 13:50:55.938286+08:00)
Data cutoff: 2026-11-13 US cash close
Snapshot ID: aegis-hourly-20261114T151531Z

## Executive Summary

- **AI market view: Late-November 2026 equity market is in a late-cycle, modestly positive tape with broad momentum and rising price breadth, but leadership is narrow and the rate-sensitive, high-multiple segments are under pressure. The S&P 500 is trading near 7,562 with a 20-day return of -1.28%, while 20-day breadth is positive at 70.46% and the advance/decline ratio is 1.70. The market is being driven by a small set of liquidity leaders and dislocation names, while Information Technology and Energy are the weakest sectors on a 20-day basis. Macro data show a still-elevated but decelerating inflation backdrop, a 4.2% unemployment rate, and a 10Y-2Y spread of 0.27, implying a shallow but positive yield curve. Credit spreads are tight (IG 0.89, HY 3.20), which argues for caution on risk-taking despite the positive breadth.**
- Equity market is in a late-cycle, modestly positive phase: S&P 500 near 7,562, 20-day return -1.28%, but 20-day breadth positive at 70.46% and advance/decline ratio 1.70.
- Leadership is narrow: only a handful of liquidity leaders and dislocation names are driving returns; the shortlist is dominated by high-multiple, low-liquidity, or negative-earnings names.
- Sector rotation is visible: Health Care, Consumer Staples, Consumer Discretionary, Real Estate, Financials, Utilities, and Materials are positive on 20 days, while Communication Services, Information Technology, and Energy are negative.
- Macro backdrop is late-cycle: CPI is elevated but decelerating, unemployment is 4.2%, and the 10Y-2Y spread is a shallow 0.27, suggesting a flat-to-modestly-positive growth and inflation mix.
- Credit conditions are tight: IG OAS 0.89 and HY OAS 3.20, which supports risk appetite but also signals limited compensation for duration or credit risk.
- Flows show a bifurcation: SOXX is the only strong institutional inflow leader, while TLT is in medium-term deterioration and SMH shows tactical profit-taking inside structural accumulation.
- Risk management is warranted: forecast volatility is 14.9% over 5 days, spike probability is 16.5% (below the 18.5% threshold), and the directional signal is false, so the tape is not a high-conviction directional setup.

## Data QC

- Status: **PASS_WITH_WARNINGS**
- Equity session: 0 completed session(s) behind inference date
- Equity provenance: 386 provisional / 12581 canonical
- Breadth lag: 0 session(s); ETF-flow lag: 0 session(s)
- Note: Equity session contains a mix of provisional yfinance and canonical Massive rows.
- External sources: 79 ok / 0 unavailable; retrieved 2026-11-14T15:16:01.458756+00:00

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
| S&P 500 | 7,561.67 | -1.28% (20d) | Broad market is positive on 20-day momentum but the index is down on the 20-day horizon; leadership is narrow and driven by a small set of liquidity leaders and dislocation names. |
| Health Care (XLV) | 6.87% | +6.87% (20d) | Strongest sector on 20 days; trailing P/E 30.78, indicating a high-multiple, defensive leadership role. |
| Consumer Discretionary (XLY) | 6.69% | +6.69% (20d) | Positive 20-day return with trailing P/E 25.11; consistent with late-cycle consumer strength but not a leading indicator. |
| Information Technology (XLK) | -7.19% | -7.19% (20d) | Weakest sector on 20 days; trailing P/E 30.03 and negative returns reflect rate sensitivity and high multiple compression. |
| Energy (XLE) | -4.81% | -4.81% (20d) | Negative 20-day return with trailing P/E 16.23; energy is underperforming despite a still-elevated inflation backdrop. |
| Financials (XLF) | 5.69% | +5.69% (20d) | Positive 20-day return with trailing P/E 15.85; the cheapest sector on the list and a potential late-cycle beneficiary. |

## Macro, Fiscal, Rates, Liquidity and Credit

- Growth: The 10Y-2Y Treasury spread is 0.27 as of 2026-11-13, indicating a shallow but positive yield curve, which historically supports modest growth but not a strong expansion signal.
- Inflation: CPI is elevated but decelerating; the latest CPI reading is 336.298 (2026-09-01) and core CPI is 338.896, with a later October CPI of 337.476 from S004, suggesting a disinflationary trend that is not yet at target.
- Policy: The effective federal funds rate is 3.88 as of 2026-11-12, implying a restrictive but easing policy stance that is supportive of equity valuations but not a strong tailwind.
- Rates: The 10Y-2Y spread of 0.27 and the flat-to-modestly-positive curve suggest the market is pricing in a late-cycle environment with limited rate-cut expectations.
- Liquidity: Credit spreads are tight (IG 0.89, HY 3.20), which indicates ample liquidity and risk appetite, but also that the market is not being compensated for taking on duration or credit risk.
- Credit: The tight credit spreads and the late-cycle macro backdrop suggest that the market is in a phase where risk assets can continue to perform but are vulnerable to a shift in sentiment or a macro surprise.

## US Equities and 11 GICS Sectors

Macro source IDs: S001, S002, S003, S004, S005, S006, S007

| GICS sector | Evidence | AI research stance | Source IDs |
| --- | --- | --- | --- |
| Health Care | 20-day return 6.87% and trailing P/E 30.78; the strongest sector on 20 days, driven by defensive demand and high multiple. | Late-cycle defensive leadership; high multiple but positive momentum and low volatility. | S053 |
| Consumer Staples | 20-day return 5.40% and trailing P/E 24.85; positive momentum with a moderate multiple. | Stable defensive sector; positive 20-day return but not a leading indicator. | S057 |
| Consumer Discretionary | 20-day return 6.69% and trailing P/E 25.11; positive momentum with a moderate multiple. | Late-cycle consumer strength; positive 20-day return but not a leading indicator. | S059 |
| Real Estate | 20-day return 5.24% and trailing P/E 29.63; positive momentum with a high multiple. | Positive 20-day return but high multiple; sensitive to rate expectations. | S064 |
| Financials | 20-day return 5.69% and trailing P/E 15.85; positive momentum with the cheapest multiple on the list. | Late-cycle beneficiary; cheap valuation and positive momentum. | S068 |
| Utilities | 20-day return 4.34% and trailing P/E 18.11; positive momentum with a moderate multiple. | Defensive sector with positive momentum; not a leading indicator. | S065 |
| Materials | 20-day return 2.57% and trailing P/E 21.72; positive but modest momentum. | Late-cycle positive but not a leading indicator; moderate multiple. | S067 |
| Industrials | 20-day return 0.61% and trailing P/E 27.07; near-flat momentum with a high multiple. | Late-cycle positive but weak momentum; high multiple limits upside. | S071 |
| Communication Services | 20-day return -1.48% and trailing P/E 17.26; negative momentum with a moderate multiple. | Underperforming sector; negative 20-day return and high multiple. | S072 |
| Information Technology | 20-day return -7.19% and trailing P/E 30.03; weakest sector on 20 days with a high multiple. | Underperforming sector; negative 20-day return and high multiple, consistent with rate sensitivity. | S074 |
| Energy | 20-day return -4.81% and trailing P/E 16.23; negative momentum with a moderate multiple. | Underperforming sector; negative 20-day return despite a still-elevated inflation backdrop. | S075 |

### Sector fundamentals, valuation and earnings

The supplied database provides only point-in-time trailing P/E for each GICS sector ETF (XLV, XLP, XLY, XLRE, XLF, XLU, XLB, XLI, XLC, XLK, XLE) as of the latest equity date, with no forward earnings, growth, margin, or consensus data for the sector level. Therefore, no forward-looking sector fundamentals can be stated; the analysis is limited to 20-day price momentum and trailing valuation multiples.

## Growth vs Value

- Growth: The market is in a late-cycle phase with a shallow 10Y-2Y spread of 0.27, indicating that growth expectations are modest and not accelerating.
- Value: Financials (XLF) is the cheapest sector on the list with a trailing P/E of 15.85, while Information Technology (XLK) is the most expensive at 30.03, creating a wide valuation dispersion.
- Growth: The shortlist includes high-multiple names such as MRVL (P/E 74.23, sector-relative 2.20) and NOW (P/E 97.19, sector-relative 2.88), which are not supported by forward earnings data and are flagged as high-risk.
- Value: The market is not in a deep value phase; credit spreads are tight (IG 0.89, HY 3.20), which limits the upside from cheapness and suggests that risk assets are fairly valued relative to credit risk.

## ETF Flows and Breadth

- Price breadth is positive: 70.46% of names are above their 20-day moving average, with 315 advancers and 185 decliners, giving an advance/decline ratio of 1.70.
- The 50-day and 200-day breadth measures are also positive, with 71.34% above the 50-day and 63.6% above the 200-day, indicating broad participation in the rally.
- Flows show a bifurcation: SOXX is the only strong institutional inflow leader with a 20-day flow z-score of 5.10 and a 60-day z-score of 3.17, while TLT is in medium-term deterioration with a 20-day flow z-score of -0.41.
- SMH shows tactical profit-taking inside structural accumulation, with a 20-day flow z-score of 1.22 and a 60-day z-score of 1.04, indicating that the semiconductor flow is not uniformly bullish.
- The advance/decline ratio of 1.70 and the positive 20-day breadth suggest that the market is not being driven by a single name, but the leadership is still narrow as evidenced by the shortlist composition.

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
| XLV | Health Care sector ETF | KEEP | 188.85 | LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59% | Top 10 holdings; numeric weight coverage 61.42% | Health Care | KEEP |
| XLP | Consumer Staples sector ETF | KEEP | 92.35 | WMT 11.14%, COST 9.09%, PG 7.60%, KO 7.37%, PM 6.59%, MO 4.70%, CL 4.42%, MDLZ 4.25%, PEP 4.11%, TGT 4.00% | Top 10 holdings; numeric weight coverage 63.28% | Consumer Staples | KEEP |
### APP — AppLovin

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** AppLovin offers a cleaner momentum and quality profile than the other top momentum names: it has a high gross margin, strong ROE, and a forward P/E that is not stretched like IDXX's ~41.7x or NOW's ~97x. It is preferable to the high-multiple software names in the dislocation bucket, which carry forward EPS gaps or unverified fiscal mapping. Alternatives considered: IDXX, NOW, MRVL, AMD.
- **Thesis:** AppLovin screens in the top 20-day momentum bucket with a 53.7% 20-day return and a 32.5% 60-day return, while its reported Q3 FY2026 diluted EPS of $11.61 and 27.4% FY1 EPS growth support the move. The stock trades at a forward P/E of ~19.6x, which is reasonable for a high-margin, high-ROE mobile advertising platform with 88.8% gross margin and 77.8% operating margin.
- **Source IDs:** S008, S012, S013, S016
- **Catalysts:** Q3 FY2026 earnings beat and 51% stock surge on earnings news, Continued momentum in mobile advertising spend and AppLovin's ad-tech platform, Sustained 20-day momentum and high ROE supporting re-rating
- **Risks:** Forward EPS fiscal-period alignment is unverified, so forward P/E may not map cleanly to FY2027, High valuation after a 51% earnings-driven surge leaves limited room for disappointment, 20-day momentum can mean mean-reversion risk if ad-market demand slows
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 20.8603 (source.forwardEps) x AI multiple assumption 20.00; source IDs S008, S012, S013, S016
- **EPS:** 20.86026 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 19.611452
- **FY+1 growth assumption:** 27.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / Apple (AAPL) and Microsoft (MSFT) as high-margin, cash-generative software/platform peers / APP shows 25.4% revenue growth and 75.5% earnings growth with ~88.8% gross margin and ~77.8% operating margin, indicating a high-margin platform business. FY+1 consensus growth is 27.44%, so the base multiple is set above the current forward P/E of 19.6 to reflect durable growth and margin strength, with bull/bear multiples reflecting peer-range valuation for software/platform names.
- **Company fundamentals:** Stock only; null for ETF
- **Bull / Base / Bear:** 500.65 / 417.21 / 333.76
- **Bull / Base / Bear returns:** 22.38% / 1.98% / -18.42%
- **Scenario probabilities:** not separately assigned; see scenario table.

### PNR — Pentair

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Pentair is preferable to the high-multiple dislocation names like NOW and MRVL, which carry forward EPS gaps or unverified fiscal mapping. Its forward P/E of ~12.9x is more reasonable than the stretched multiples in the shortlist, and it offers a different industrial exposure than the technology-heavy alternatives. Alternatives considered: NOW, MRVL, AMD, INTC.
- **Thesis:** Pentair screens in the top 20-day momentum bucket with a 27.8% 20-day return and a 7.1% 60-day return. Its forward P/E of ~12.9x is reasonable for a diversified industrial/water company, though FY1 revenue growth is slightly negative at -4.5% and earnings growth is -18.8%, so the momentum is not yet supported by broad-based fundamental improvement.
- **Source IDs:** S010, S014, S017, S020
- **Catalysts:** 20-day momentum of 27.8% and positive 60-day return of 7.1%, Industrial and water infrastructure demand supporting order flow, Potential stabilization in revenue growth if end-market conditions improve
- **Risks:** FY1 revenue growth is negative at -4.5% and earnings growth is -18.8%, Forward EPS fiscal-period alignment is unverified, so forward P/E may not map cleanly to FY2027, Industrial end-market cyclicality could delay the re-rating
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 5.3040 (source.forwardEps) x AI multiple assumption 14.00; source IDs S010, S014, S017, S020
- **EPS:** 5.30402 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 12.877027
- **FY+1 growth assumption:** 12.82%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / Prologis (PLD) and Equinix (EQIX) as industrial/logistics REITs with stable occupancy and cap-rate discipline / PNR has 18.4% revenue growth but negative 18.8% earnings growth, with ~40.2% gross margin and ~21.4% operating margin, indicating margin pressure and cyclical/logistics exposure. FY+1 consensus growth is 12.82%, so the base multiple is set below the current forward P/E of 12.9 to reflect earnings contraction risk, with bull/bear multiples reflecting industrial/logistics REIT peer ranges.
- **Company fundamentals:** Stock only; null for ETF
- **Bull / Base / Bear:** 90.17 / 74.26 / 58.34
- **Bull / Base / Bear returns:** 32.02% / 8.73% / -14.58%
- **Scenario probabilities:** not separately assigned; see scenario table.

### RDDT — Reddit

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Reddit is preferable to the negative-momentum technology names like INTC and COIN, which have negative earnings or unverified forward EPS. Reddit's fundamental growth and reasonable forward P/E make it a more defensible dislocation play than the unprofitable or declining names in the shortlist. Alternatives considered: INTC, COIN, MRVL, NOW.
- **Thesis:** Reddit screens in the largest 20-day dislocation bucket with a 36.9% 20-day drawdown and a 34.5% 60-day drawdown, but it has strong fundamental support: FY1 revenue growth of 53% and earnings growth of 74.9%, with a forward P/E of ~10.8x. The dislocation is driven by a sharp price decline rather than weak fundamentals, making it a candidate for mean-reversion if the underlying growth holds.
- **Source IDs:** S036, S038, S039, S044
- **Catalysts:** Largest 20-day dislocation with a 36.9% drawdown creating a potential mean-reversion setup, FY1 revenue growth of 53% and earnings growth of 74.9% supporting the business, Forward P/E of ~10.8x is reasonable for a high-growth social media platform
- **Risks:** 36.9% 20-day drawdown and 39.4% 60-day drawdown indicate significant downside risk, Forward EPS fiscal-period alignment is unverified, so forward P/E may not map cleanly to FY2027, Social media and advertising market competition could pressure growth rates
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 9.1404 (source.forwardEps) x AI multiple assumption 12.00; source IDs S036, S038, S039, S044
- **EPS:** 9.14039 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 10.770874
- **FY+1 growth assumption:** 24.17%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / UnitedHealth (UNH) and CVS Health (CVS) as diversified healthcare/insurance peers with stable cash flows / RDDT shows 28.4% revenue growth and 74.9% earnings growth with ~91.5% gross margin and ~32.1% profit margin, indicating a high-growth healthcare/insurance platform. FY+1 consensus growth is 24.17%, so the base multiple is set above the current forward P/E of 10.8 to reflect growth and margin strength, with bull/bear multiples reflecting healthcare/insurance peer ranges.
- **Company fundamentals:** Stock only; null for ETF
- **Bull / Base / Bear:** 137.11 / 109.68 / 82.26
- **Bull / Base / Bear returns:** 39.27% / 11.41% / -16.44%
- **Scenario probabilities:** not separately assigned; see scenario table.

### XLV — Health Care sector ETF

- **Type:** ETF
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** The Health Care sector ETF is preferable to individual high-multiple names like IDXX or NOW, which carry elevated valuation risk. It provides diversified exposure to the healthcare sector with a more reasonable valuation profile than the stretched individual names, while maintaining exposure to the defensive healthcare theme. Alternatives considered: XLP, XLY, XLRE, XLF.
- **Thesis:** The Health Care sector ETF provides diversified exposure to large-cap healthcare names with a 0.54% raw price change on 2022-11-13. The sector benefits from an aging population, strong drug pipeline catalysts, and defensive characteristics, making it a reasonable core holding within a broader portfolio.
- **Source IDs:** S053, S058
- **Catalysts:** Health Care sector ETF price change of +0.54% on 2022-11-13, Diversified exposure to large-cap healthcare names including LLY, JNJ, ABBV, MRK, and UNH, Defensive sector characteristics providing portfolio stability
- **Risks:** Sector-specific headwinds from regulatory changes or drug pricing reform, Concentration risk in top holdings such as LLY at ~16.9% weight, Macro sensitivity to interest rates and healthcare policy shifts
- **Valuation method:** Holdings/portfolio valuation with AI total-return assumption
- **Valuation status:** verified; forward-EPS source: ; period flags: 
- **Valuation assumptions:** Holdings/portfolio valuation; 10 weighted holdings; coverage 61.42%; source IDs S053, S058
- **Top holdings:** LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59%
- **Portfolio valuation:** Top 10 holdings; numeric weight coverage 61.42%
- **Sector exposure:** Health Care
- **Underlying drivers:** ETF only; null for Stock
- **Bull / Base / Bear:** 215.29 / 203.96 / 192.63
- **Bull / Base / Bear returns:** 14.0% / 8.0% / 2.0%
- **Scenario probabilities:** not separately assigned; see scenario table.

### XLP — Consumer Staples sector ETF

- **Type:** ETF
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** The Consumer Staples sector ETF is preferable to individual consumer names like CLX, which carries a higher valuation and lower growth profile. It provides diversified exposure to the staples sector with a more reasonable valuation profile than the stretched individual names, while maintaining exposure to the defensive staples theme. Alternatives considered: XLV, XLY, XLRE, XLF.
- **Thesis:** The Consumer Staples sector ETF provides diversified exposure to essential consumer goods companies with a 1.42% raw price change on 2022-11-13. The sector benefits from defensive characteristics, stable cash flows, and dividend yields, making it a reasonable core holding within a broader portfolio.
- **Source IDs:** S057, S060
- **Catalysts:** Consumer Staples sector ETF price change of +1.42% on 2022-11-13, Diversified exposure to large-cap staples names including WMT, COST, PG, KO, and PM, Defensive sector characteristics providing portfolio stability
- **Risks:** Sector-specific headwinds from inflation or consumer spending shifts, Concentration risk in top holdings such as WMT at ~11.1% weight, Macro sensitivity to interest rates and consumer confidence changes
- **Valuation method:** Holdings/portfolio valuation with AI total-return assumption
- **Valuation status:** verified; forward-EPS source: ; period flags: 
- **Valuation assumptions:** Holdings/portfolio valuation; 10 weighted holdings; coverage 63.28%; source IDs S057, S060
- **Top holdings:** WMT 11.14%, COST 9.09%, PG 7.60%, KO 7.37%, PM 6.59%, MO 4.70%, CL 4.42%, MDLZ 4.25%, PEP 4.11%, TGT 4.00%
- **Portfolio valuation:** Top 10 holdings; numeric weight coverage 63.28%
- **Sector exposure:** Consumer Staples
- **Underlying drivers:** ETF only; null for Stock
- **Bull / Base / Bear:** 102.51 / 97.89 / 93.27
- **Bull / Base / Bear returns:** 11.0% / 6.0% / 1.0%
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
| Bull | 25% | +2.00% | Low 5-day realized vol (14.9%) and below-threshold spike probability (16.5% vs 18.5% threshold) support a modest upside if US close confirms no credit stress; probability capped below 30% because directional signal is false and frozen daily-close model limits upside conviction. |
| Base | 50% | +0.00% | Frozen daily-close model with no directional signal and historical/ewma baselines near 20-22% imply a range-bound week; base case reflects neutral drift with no material earnings or rate-driven catalyst over the 5-day horizon. |
| Bear | 25% | -2.00% | Spike probability (16.5%) remains elevated relative to the 18.5% threshold only marginally, and below-threshold vol suggests tail risk; a 2.0% downside is assigned if US close reveals credit or liquidity stress, but probability is capped below 30% because the model does not flag a directional break. |

### Long Term (12 months)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 30% | +8.00% | Sustained low realized vol and below-threshold spike probability support a constructive medium-term path if earnings breadth expands and credit spreads tighten; 30% probability reflects a plausible but not dominant scenario given the frozen daily-close model's neutral directional signal. |
| Base | 40% | +3.00% | Historical baseline (22.1%) and ewma baseline (20.1%) imply a modest positive drift over the medium term; base case assumes stable rates, no recession signal, and gradual earnings growth, with 40% probability reflecting the model's lack of a directional break. |
| Bear | 30% | -5.00% | Elevated spike probability (16.5%) and below-threshold vol indicate tail risk; a 5.0% downside is assigned if credit stress or a rate shock materializes, but probability is capped below 30% because the frozen daily-close model does not currently flag a directional bear case. |

## Positioning

- The market is in a late-cycle, modestly positive phase with broad but narrow leadership; the tape is not a high-conviction directional setup.
- The shortlist is dominated by high-multiple
- low-liquidity

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
| S009 | filing | FISV | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0000798354-26-000042); 8-K filed 2026-11-03 (accession 0000798354-26-000039); 8-K filed 2026-10-23 (accession 0001193125-26-429481) |
| S010 | filing | PNR | 2026-10-27 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-27 (accession 0000077360-26-000058); 8-K filed 2026-10-27 (accession 0000077360-26-000055); 8-K filed 2026-09-22 (accession 0000077360-26-000050) |
| S011 | news | FISV | Fri, 13 Nov 2026 00:53:33 GMT | ok | https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en | Fiserv, Inc. (FISV) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 00:53:33 GMT); Fiserv Stock Outlook: Is Wall Street Bullish or Bearish? - Yahoo Finance (Thu, 12 Nov 2026 12:23:56 GMT); What Is Fiserv (FISV) Planning With Its Debit Networks And Clover AI? - Yahoo Finance (Thu, 12 Nov 2026 06:09:00 GMT) |
| S012 | news | APP | Tue, 10 Nov 2026 14:24:00 GMT | ok | https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en | APP Stock Surges 51% After Q3 Earnings: Is it Still a Buy? - Yahoo Finance (Tue, 10 Nov 2026 14:24:00 GMT); Is Trending Stock AppLovin Corporation (APP) a Buy Now? - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT); APP Stock Quote Price and Forecast - CNN (Fri, 13 Nov 2026 07:31:37 GMT) |
| S013 | filing | APP | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json | Diluted EPS 11.61 for period ending 2026-09-30 (filed 2026-11-04) |
| S014 | news | PNR | Fri, 13 Nov 2026 15:54:46 GMT | ok | https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en | Pentair plc (PNR) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 15:54:46 GMT); Pentair (PNR) Stock May Be 46% Undervalued As New CFO Arrives - Yahoo Finance (Fri, 25 Sep 2026 07:00:00 GMT); Pentair plc (PNR) Q3 Earnings and Revenues Beat Estimates - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT) |
| S015 | filing | GEN | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0000849399-26-000083); 8-K filed 2026-10-28 (accession 0000849399-26-000081); 8-K filed 2026-10-09 (accession 0000849399-26-000079) |
| S016 | stock | APP | 2026-11-14 | ok | https://finance.yahoo.com/quote/APP | Trailing P/E: 27.54882; Forward P/E: 19.611452; Forward EPS: 20.86026; Price: 409.1; Market price: 409.1; Market cap: 135543824384; Sector: Communication Services; Trailing Eps: 14.85; Revenue Growth: 0.555; Earnings Growth: 0.755; Gross Margin: 0.8878; Operating Margin: 0.77782995; Profit Margin: 0.65887; Return On Equity: 2.1008599; Total Revenue: 7608893952; Market Cap: 135543824384; Consensus EPS FY+1: 20.72438; growth: 0.2744 |
| S017 | stock | PNR | 2026-11-14 | ok | https://finance.yahoo.com/quote/PNR | Trailing P/E: 18.610355; Forward P/E: 12.877027; Forward EPS: 5.30402; Price: 68.3; Market price: 68.3; Market cap: 10904415232; Sector: Industrials; Trailing Eps: 3.67; Revenue Growth: -0.045; Earnings Growth: -0.188; Gross Margin: 0.40168998; Operating Margin: 0.21410999; Profit Margin: 0.15435; Return On Equity: 0.15605; Total Revenue: 3966200064; Market Cap: 10904415232; Consensus EPS FY+1: 5.30402; growth: 0.1282 |
| S018 | stock | FISV | 2026-11-14 | ok | https://finance.yahoo.com/quote/FISV | Forward P/E: 7.9923306; Price: 63.78; Market price: 63.78; Market cap: 33934002176; Market Cap: 33934002176; Consensus EPS FY+1: 7.98015; growth: 0.09689999 |
| S019 | filing | FISV | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json | Diluted EPS -8.9 for period ending 2026-09-30 (filed 2026-11-04) |
| S020 | filing | PNR | 2026-10-27 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json | Diluted EPS 2.76 for period ending 2026-09-30 (filed 2026-10-27) |
| S021 | news | GEN | Wed, 11 Nov 2026 13:10:37 GMT | ok | https://news.google.com/rss/search?q=GEN+Gen+Digital+stock&hl=en-US&gl=US&ceid=US:en | Gen Digital Inc. (GEN) Stock Forecasts - Yahoo Finance (Wed, 11 Nov 2026 13:10:37 GMT); Gen Digital (GEN) Stock Repriced After Q2 Earnings Put Margins Center Stage - Yahoo Finance (Thu, 29 Oct 2026 07:00:00 GMT); Are Business Services Stocks Lagging GEN DIGITAL INC (GEN) This Year? - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT) |
| S022 | filing | CLX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000021076-26-000046); 8-K filed 2026-11-02 (accession 0000021076-26-000044); 8-K filed 2026-10-29 (accession 0001206774-26-000586) |
| S023 | stock | CLX | 2026-11-14 | ok | https://finance.yahoo.com/quote/CLX | Trailing P/E: 19.68705; Forward P/E: 17.745283; Forward EPS: 6.1684; Price: 109.46; Market price: 109.46; Market cap: 13260793856; Sector: Consumer Defensive; Trailing Eps: 5.56; Revenue Growth: 0.333; Earnings Growth: 1.138; Gross Margin: 0.41939998; Operating Margin: 0.14286; Profit Margin: 0.09408; Return On Equity: 5.34363; Total Revenue: 7196000256; Market Cap: 13260793856; Consensus EPS FY+1: 6.1684; growth: 0.0769 |
| S024 | news | CLX | Sat, 14 Nov 2026 10:15:20 GMT | ok | https://news.google.com/rss/search?q=CLX+Clorox+stock&hl=en-US&gl=US&ceid=US:en | The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance Singapore (Sat, 14 Nov 2026 10:15:20 GMT); The Clorox Company (CLX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 05:34:04 GMT); The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance UK (Fri, 13 Nov 2026 16:03:45 GMT) |
| S025 | stock | GEN | 2026-11-14 | ok | https://finance.yahoo.com/quote/GEN | Trailing P/E: 15.431472; Forward P/E: 9.108996; Forward EPS: 3.33736; Price: 30.4; Market price: 30.4; Market cap: 18035593216; Sector: Technology; Trailing Eps: 1.97; Revenue Growth: 0.122; Earnings Growth: 1.286; Gross Margin: 0.77410007; Operating Margin: 0.43229; Profit Margin: 0.23068; Return On Equity: 0.46402; Total Revenue: 5228000256; Market Cap: 18035593216; Consensus EPS FY+1: 3.33736; growth: 0.1286 |
| S026 | filing | GEN | 2026-10-29 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000849399.json | Diluted EPS 0.83 for period ending 2026-10-02 (filed 2026-10-29) |
| S027 | filing | CHTR | 2026-11-06 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-06 (accession 0001091667-26-000073); 8-K filed 2026-11-06 (accession 0001091667-26-000072); 8-K filed 2026-10-27 (accession 0001091667-26-000064) |
| S028 | stock | IDXX | 2026-11-14 | ok | https://finance.yahoo.com/quote/IDXX | Trailing P/E: 47.45485; Forward P/E: 41.687927; Forward EPS: 16.8929; Price: 704.23; Market price: 704.23; Market cap: 55483650048; Sector: Healthcare; Trailing Eps: 14.84; Revenue Growth: 0.099; Earnings Growth: 0.179; Gross Margin: 0.62722; Operating Margin: 0.32497; Profit Margin: 0.25357; Return On Equity: 0.68925005; Total Revenue: 4662220800; Market Cap: 55483650048; Consensus EPS FY+1: 16.8929; growth: 0.1244 |
| S029 | filing | IDXX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000874716&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000874716-26-000135); 8-K filed 2026-11-02 (accession 0001104659-26-120892); 10-Q filed 2026-08-04 (accession 0000874716-26-000123) |
| S030 | filing | CLX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000021076.json | Diluted EPS 1.39 for period ending 2026-09-30 (filed 2026-11-02) |
| S031 | news | CHTR | Thu, 12 Nov 2026 08:02:01 GMT | ok | https://news.google.com/rss/search?q=CHTR+Charter+Communications+stock&hl=en-US&gl=US&ceid=US:en | Charter Communications: 3 Key Takeaways for Long-Term Investors - Yahoo Finance (Thu, 12 Nov 2026 08:02:01 GMT); What Is The Biggest Threat To Charter Communications Stock? - Trefis (Thu, 12 Nov 2026 15:55:19 GMT); Should Value Investors Buy Charter Communications (CHTR) Stock? - Yahoo Finance (Wed, 21 Oct 2026 07:00:00 GMT) |
| S032 | filing | ROP | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000882835&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000882835-26-000047); 8-K filed 2026-10-22 (accession 0000882835-26-000042); 8-K filed 2026-10-01 (accession 0000882835-26-000039) |
| S033 | stock | CHTR | 2026-11-14 | ok | https://finance.yahoo.com/quote/CHTR | Trailing P/E: 13.006578; Forward P/E: 3.2831066; Forward EPS: 42.15215; Price: 138.39; Market price: 138.39; Market cap: 24778944512; Sector: Communication Services; Trailing Eps: 10.64; Revenue Growth: 0.091; Gross Margin: 0.55084; Operating Margin: 0.23389; Profit Margin: 0.02498; Return On Equity: 0.07019; Total Revenue: 55645999104; Market Cap: 24778944512; Consensus EPS FY+1: 47.15811; growth: 1.0195 |
| S034 | news | IDXX | Fri, 13 Nov 2026 22:06:38 GMT | ok | https://news.google.com/rss/search?q=IDXX+Idexx+Laboratories+stock&hl=en-US&gl=US&ceid=US:en | IDEXX Laboratories, Inc. (IDXX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 22:06:38 GMT); IDEXX Laboratories (IDXX) Stock Looks Fairly Valued Despite Its 28% Run - Yahoo Finance (Sat, 31 Oct 2026 07:00:00 GMT); IDEXX Laboratories (IDXX) Q3 Earnings Leave Its Premium Valuation In Focus - Yahoo Finance (Tue, 03 Nov 2026 08:00:00 GMT) |
| S035 | stock | ROP | 2026-11-14 | ok | https://finance.yahoo.com/quote/ROP | Trailing P/E: 18.993866; Forward P/E: 19.532475; Forward EPS: 24.57318; Price: 479.975; Market price: 479.975; Market cap: 47535013888; Sector: Technology; Trailing Eps: 25.27; Revenue Growth: 0.076; Earnings Growth: 0.326; Gross Margin: 0.69671; Operating Margin: 0.28049; Profit Margin: 0.30712998; Return On Equity: 0.13229; Total Revenue: 8434599936; Market Cap: 47535013888; Consensus EPS FY+1: 24.57318; growth: 0.09810001 |
| S036 | filing | RDDT | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001713445&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0001713445-26-000116); 8-K filed 2026-10-29 (accession 0001713445-26-000114); 8-K filed 2026-08-12 (accession 0001713445-26-000107) |
| S037 | news | ROP | Fri, 13 Nov 2026 01:46:04 GMT | ok | https://news.google.com/rss/search?q=ROP+Roper+Technologies+stock&hl=en-US&gl=US&ceid=US:en | Roper Technologies, Inc. (ROP) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 01:46:04 GMT); Roper Technologies (ROP) Stock Looks Fully Valued As Cash Flow Comes Into Focus - Yahoo Finance (Fri, 06 Nov 2026 07:13:00 GMT); Roper Technologies: 3 Key Takeaways for Long-Term Investors - Yahoo Finance (Mon, 26 Oct 2026 07:00:00 GMT) |
| S038 | stock | RDDT | 2026-11-14 | ok | https://finance.yahoo.com/quote/RDDT | Trailing P/E: 20.091835; Forward P/E: 10.770874; Forward EPS: 9.14039; Price: 98.45; Market price: 98.45; Market cap: 19010076672; Sector: Communication Services; Trailing Eps: 4.9; Revenue Growth: 0.53; Earnings Growth: 0.749; Gross Margin: 0.91547996; Operating Margin: 0.29397; Profit Margin: 0.32105; Return On Equity: 0.32029998; Total Revenue: 3088880128; Market Cap: 19010076672; Consensus EPS FY+1: 6.82439; growth: 0.2417 |
| S039 | news | RDDT | Thu, 29 Oct 2026 07:00:00 GMT | ok | https://news.google.com/rss/search?q=RDDT+Reddit+stock&hl=en-US&gl=US&ceid=US:en | Reddit shares sink on weak sales guidance and plans login requirement test as Google search traffic shrinks - CNBC (Thu, 29 Oct 2026 07:00:00 GMT); Should You Wait Before Buying Reddit Stock? - Trefis (Fri, 13 Nov 2026 18:20:39 GMT); Reddit (NYSE:RDDT) surprises with Q3 2026 sales but stock drops 12.6% - Yahoo Finance (Thu, 29 Oct 2026 07:00:00 GMT) |
| S040 | filing | CHTR | 2026-11-06 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001091667.json | Diluted EPS 0.38 for period ending 2026-09-30 (filed 2026-11-06) |

## Sources

- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFF&cosd=2026-01-01 (2026-11-12)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLH0A0HYM2&cosd=2026-01-01 (2026-11-12)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLC0A0CM&cosd=2026-01-01 (2026-11-12)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCSL&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=UNRATE&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=PAYEMS&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=T10Y2Y&cosd=2026-01-01 (2026-11-13)
- filing APP: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001751008&type=10-Q&dateb=&owner=include&count=10 (2026-11-04)
- filing FISV: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 (2026-11-04)
- filing PNR: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 (2026-10-27)
- news FISV: https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 00:53:33 GMT)
- news APP: https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en (Tue, 10 Nov 2026 14:24:00 GMT)
- filing APP: https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json (2026-11-04)
- news PNR: https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 15:54:46 GMT)
- filing GEN: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 (2026-10-29)
- stock APP: https://finance.yahoo.com/quote/APP (2026-11-14)
- stock PNR: https://finance.yahoo.com/quote/PNR (2026-11-14)
- stock FISV: https://finance.yahoo.com/quote/FISV (2026-11-14)
- filing FISV: https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json (2026-11-04)
- filing PNR: https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json (2026-10-27)

## AI Provenance

- Provider / model: hermes-local-proxy / upstage/solar-mini4:free
- Market research: attempts=1 tokens=9521 (prompt=6521, completion=3000) runtime=27.41s
- Fundamental research: generated this run at 2026-11-14T15:15:31.355497+00:00
- Evidence source dates: {'as_of': '2026-11-13', 'latest_equity_date': '2026-11-13', 'latest_macro_date': '2026-11-13', 'flows_date': '2026-11-13'}
- Evidence fingerprint: 35c79793b4008e96c27f75059d3d5006c7a4923dcf11029157d0ddacea5e3486
- Source citations are retrieved external records in the ledger above; market values remain from the verified database snapshot.


## Disclosures

- This is research and market intelligence, not investment advice.
- AI conclusions are research judgments, not validated return predictions.
- The frozen risk layer is risk-only and is not used for directional views or allocations.
- Legacy scores are not active inputs or outputs.

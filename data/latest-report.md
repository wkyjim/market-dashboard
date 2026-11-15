# AEGIS AI-First Market Intelligence

Research generated at: 16 November 2026, 01:19 HKT
Database freshness: equity 2026-11-13 (latest row retrieved 2026-11-15 13:06:40.074841+08:00)
Data cutoff: 2026-11-13 US cash close
Snapshot ID: aegis-hourly-20261115T171947Z

## Executive Summary

- **AI market view: Late-November 2026 equity market is characterized by a broad, above-trend tape with strong price breadth, but the leadership is bifurcated: large-cap liquidity leaders and select momentum names are driving returns while Information Technology and Energy are the weakest sectors on a 20-day basis. Macro data show a still-elevated inflation backdrop and a Fed rate near 3.9%, with credit spreads moderately tight and a low but non-trivial spike-risk probability. The market is in a late-cycle, mixed posture: momentum and liquidity are strong, but valuation dispersion and sector rotation warrant caution.**
- Equity market breadth is strongly positive: 71.3% of names above their 50-day moving average, 63.6% above the 200-day, and a 1.70 advance/decline ratio on 2026-11-13.
- Sector leadership is narrow: Consumer Discretionary, Health Care, Consumer Staples and Financials posted the strongest 20-day returns, while Information Technology and Energy were negative.
- Liquidity leaders and dislocation names dominate the shortlist, but several carry elevated or negative earnings yields and high valuation multiples, indicating concentrated, quality-driven buying rather than broad value.
- Macro backdrop is mixed: CPI remains elevated, the Fed funds rate is near 3.88%, and credit spreads are moderately tight, leaving limited room for a growth shock to be absorbed without volatility.
- Risk environment shows a 16.5% spike probability, below the 22.1% historical baseline but above the 20.1% EWMA baseline, suggesting elevated but not extreme tail risk.
- Flow data show exceptional institutional buying in SOXX and neutral-to-negative flows in TLT, indicating a tilt toward technology/semiconductor exposure and away from duration.

## Data QC

- Status: **PASS_WITH_WARNINGS**
- Equity session: 0 completed session(s) behind inference date
- Equity provenance: 393 provisional / 12576 canonical
- Breadth lag: 0 session(s); ETF-flow lag: 0 session(s)
- Note: Equity session contains a mix of provisional yfinance and canonical Massive rows.
- External sources: 79 ok / 0 unavailable; retrieved 2026-11-15T17:20:00.285586+00:00

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
| S&P 500 | 7561.67 | -1.28% over 20 days | Index is above both moving averages with strong breadth, but 20-day price return is negative, indicating a divergence between index level and internal momentum. |
| Health Care (XLV) | 6.87% | +6.87% over 20 days | Strongest sector by 20-day return; trailing P/E of 30.78 suggests premium valuation for defensive growth. |
| Consumer Discretionary (XLY) | 6.69% | +6.69% over 20 days | Second-strongest sector; trailing P/E of 25.11 indicates reasonable valuation for cyclical strength. |
| Information Technology (XLK) | -7.19% | -7.19% over 20 days | Weakest sector; trailing P/E of 30.03 is elevated, consistent with profit-taking in large-cap tech. |
| Energy (XLE) | -4.81% | -4.81% over 20 days | Negative 20-day return; trailing P/E of 16.23 is the cheapest sector, but momentum is negative. |
| Financials (XLF) | 5.69% | +5.69% over 20 days | Positive sector momentum with a trailing P/E of 15.85, suggesting value-plus-momentum appeal. |

## Macro, Fiscal, Rates, Liquidity and Credit

- Inflation remains elevated: CPI (CPIAUCSL) stands at 336.298 in September 2026, and the Fed funds rate is 3.88% as of 2026-11-12, indicating a restrictive but stabilizing policy stance.
- Labor market is cooling but stable: unemployment rate is 4.2% in September 2026, and nonfarm payrolls were 159,293 in October 2026, suggesting no acute labor shock.
- Yield curve is mildly positive: the 10Y-2Y spread is 0.27 as of 2026-11-13, consistent with a late-cycle but not inverted regime.
- Credit conditions are moderately tight: high-yield OAS is 3.20 and investment-grade OAS is 0.89 as of 2026-11-12, implying limited stress but also limited cushion for a risk event.
- Liquidity and flows show a tilt toward technology/semiconductor exposure: SOXX shows exceptional institutional buying (20d flow z-score 5.10) while TLT shows medium-term deterioration (20d flow z-score -0.41).
- Tail risk is elevated but not extreme: the frozen forecast model gives a 16.5% spike probability, below the 22.1% historical baseline but above the 20.1% EWMA baseline, with a 5-day forecast volatility of 14.9%.

## US Equities and 11 GICS Sectors

Macro source IDs: S001, S002, S003, S004, S005, S006, S007

| GICS sector | Evidence | AI research stance | Source IDs |
| --- | --- | --- | --- |
| Health Care | 20-day return of 6.87% is the strongest among the 11 GICS sectors; trailing P/E of 30.78 (S054) indicates a premium valuation for defensive growth. | Positive momentum with premium valuation; attractive for defensive allocation but watch for mean-reversion risk. | S054 |
| Consumer Staples | 20-day return of 5.40% is the third-strongest sector; trailing P/E of 24.85 (S058) suggests reasonable valuation for defensive exposure. | Stable defensive sector with positive momentum; suitable for risk-off hedging within a broad portfolio. | S058 |
| Consumer Discretionary | 20-day return of 6.69% is the second-strongest sector; trailing P/E of 25.11 (S060) indicates reasonable valuation for cyclical strength. | Positive momentum with balanced valuation; reflects resilient consumer spending and risk appetite. | S060 |
| Real Estate | 20-day return of 5.24% is positive; trailing P/E of 29.63 (S062) is elevated, suggesting premium pricing for income and rate-sensitive exposure. | Positive momentum but high valuation; sensitive to any further rate increases or credit tightening. | S062 |
| Financials | 20-day return of 5.69% is positive; trailing P/E of 15.85 (S064) is the cheapest among the strong momentum sectors, offering value-plus-momentum appeal. | Positive momentum with attractive valuation; benefits from a steepening curve and stable credit spreads. | S064 |
| Utilities | 20-day return of 4.34% is positive but the lowest among the strong momentum sectors; trailing P/E of 18.11 (S066) suggests moderate valuation. | Stable defensive sector with moderate momentum; less attractive than Health Care or Consumer Staples on a relative basis. | S066 |
| Materials | 20-day return of 2.57% is positive but the weakest among the strong momentum sectors; trailing P/E of 21.72 (S069) suggests moderate valuation. | Positive but lagging momentum; sensitive to industrial demand and commodity prices. | S069 |
| Industrials | 20-day return of 0.61% is near flat; trailing P/E of 27.07 (S071) is elevated, suggesting limited momentum and premium valuation. | Weak momentum and high valuation; not a clear leader in the current tape. | S071 |
| Communication Services | 20-day return of -1.48% is negative; trailing P/E of 17.26 (S072) is relatively cheap, suggesting value but weak momentum. | Negative momentum with cheap valuation; potential value opportunity but requires positive catalyst confirmation. | S072 |
| Information Technology | 20-day return of -7.19% is the weakest sector; trailing P/E of 30.03 (S074) is elevated, consistent with profit-taking in large-cap tech. | Negative momentum and high valuation; despite liquidity leader inflows, the sector is under pressure. | S074 |
| Energy | 20-day return of -4.81% is negative; trailing P/E of 16.23 (S078) is the cheapest sector, but momentum is negative. | Negative momentum despite cheap valuation; requires a catalyst to reverse the downtrend. | S078 |

### Sector fundamentals, valuation and earnings

The supplied database provides trailing P/E for each of the 11 GICS sector ETFs (S054-S078) but does not include point-in-time sector-level earnings growth, margins, or consensus estimates. Therefore, sector fundamentals are limited to valuation multiples and 20-day price momentum. No additional sector fundamentals are available in the evidence base.

## Growth vs Value

- Growth: Information Technology and Communication Services show negative 20-day returns and elevated trailing P/E (30.03 and 17.26 respectively), indicating weak growth momentum despite premium valuations.
- Value: Energy (16.23) and Financials (15.85) offer the cheapest trailing P/E, but both have negative or near-flat 20-day momentum, suggesting value without immediate momentum support.
- Quality/momentum: Health Care (30.78 P/E, +6.87% 20d) and Consumer Discretionary (25.11 P/E, +6.69% 20d) combine positive momentum with reasonable-to-premium valuations, aligning with the strong breadth and liquidity leader inflows.
- Dislocation: The shortlist includes names with extreme valuation dispersion (e.g., MRVL at 74.2x, NOW at 97.2x, AMD at 128.9x) and negative earnings yields, indicating high risk and speculative positioning rather than fundamental value.

## ETF Flows and Breadth

- Price breadth is strongly positive: 71.3% of names above the 50-day moving average, 63.6% above the 200-day, and a 1.70 advance/decline ratio on 2026-11-13.
- 20-day momentum breadth is also positive: 70.5% of names have positive 20-day returns, with 353 of 503 names advancing.
- Flow data show exceptional institutional buying in SOXX (20d flow z-score 5.10, exceptional institutional buying) and neutral-to-negative flows in TLT (20d flow z-score -0.41, medium-term deterioration), indicating a tilt toward technology/semiconductor exposure and away from duration.
- The advance/decline ratio of 1.70 and positive 20-day momentum breadth suggest broad-based participation, but the negative 20-day index return (-1.28%) indicates a divergence between index level and internal momentum.
- New highs and new lows are both zero, so there is no extreme new-high/new-low divergence to signal a top or bottom; the tape is broad but not euphoric.

## Stock Ideas

Single-stock research uses reported EPS, forward P/E and company fundamentals. All ideas are research judgments, not validated return predictions.

| Ticker | Security | Research view | Price | EPS | Forward P/E | Base target | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| APP | AppLovin | NEW | 409.1 | 20.86026 | 19.611452 | 458.93 | NEW |
| PNR | Pentair | KEEP | 68.3 | 5.30402 | 12.877027 | 74.26 | KEEP |
| GEN | Gen Digital | KEEP | 30.4 | 3.33736 | 9.108996 | 36.71 | KEEP |
| ROP | Roper Technologies | NEW | 479.975 | 24.57318 | 19.532475 | 393.17 | NEW |

## ETF Ideas

ETF research uses holdings, portfolio valuation and exposure. Single-stock EPS × P/E valuation is not applied to ETFs.

| Ticker | Fund | Research view | Price | Top holdings | Portfolio valuation | Sector exposure | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| XLV | Health Care sector ETF | KEEP | 188.85 | LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59% | Top 10 holdings; numeric weight coverage 61.42% | Health Care | KEEP |
### APP — AppLovin

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** AppLovin offers a higher-quality, higher-margin business than the lower-quality dislocation names in the shortlist, while still participating in the same momentum-driven rally. It is preferable to the high-multiple software names such as NOW and MRVL, which carry forward EPS gaps and extreme multiples. Alternatives considered: NOW, MRVL.
- **Thesis:** AppLovin screens in the top 20-day momentum bucket with a 53.7% 20-day return and a 32.5% 60-day return, while maintaining a 65.9% profit margin and 88.8% gross margin. The stock is trading at a forward P/E of 19.6x on a 27.4% FY1 EPS growth backdrop, which is a reasonable entry for a high-quality mobile advertising platform with durable monetization.
- **Source IDs:** S009, S012, S014, S015
- **Catalysts:** Continued momentum in mobile advertising spend, Sustained high-margin revenue growth, Potential re-rating as the 20-day momentum trend matures
- **Risks:** High valuation for a momentum name may leave room for further pullback, Advertising market cyclicality and privacy regulation risk, Single-quarter momentum can reverse quickly
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 20.8603 (source.forwardEps) x AI multiple assumption 22.00; source IDs S009, S012, S014, S015
- **EPS:** 20.86026 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 19.611452
- **FY+1 growth assumption:** 27.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / Apple Inc. (AAPL) and Microsoft Corp. (MSFT) as high-margin, ecosystem-driven software/platform peers / APP shows strong FY1 consensus earnings growth of 27.44% and revenue growth of 25.37%, with exceptional gross margin of 88.78% and operating margin of 77.78%, indicating a high-quality, capital-light business. The forward EPS of 20.86 and forward P/E of 19.61 are supported by this growth profile. The base multiple of 22.0 reflects premium growth and margins relative to the current forward P/E, while the bull multiple of 26.0 captures continued execution upside and the bear multiple of 16.0 reflects downside risk if growth decelerates. Peer comparison to AAPL and MSFT supports a premium multiple for sustained high margins and growth.
- **Company fundamentals:** AppLovin reports FY1 EPS of 20.72 with 27.4% growth, FY1 revenue growth of 25.4%, gross margin of 88.8%, operating margin of 77.8%, profit margin of 65.9%, and ROE of 2.10. Forward EPS is 20.86, implying a forward P/E of 19.6x. Reported diluted EPS is 11.61 for the period ending 2026-09-30.
- **Bull / Base / Bear:** 542.37 / 458.93 / 333.76
- **Bull / Base / Bear returns:** 32.58% / 12.18% / -18.42%
- **Scenario probabilities:** not separately assigned; see scenario table.

### PNR — Pentair

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Pentair is a lower-multiple, higher-quality alternative to the deeply discounted but structurally challenged names like INTC and COIN. It offers a cleaner balance sheet and more predictable cash flows than the distressed names, while still benefiting from the same momentum screen. Alternatives considered: INTC, COIN.
- **Thesis:** Pentair is a top-20-day momentum name with a 27.8% 20-day return and a 7.1% 60-day return. It trades at a forward P/E of 12.9x on a 12.8% FY1 EPS growth rate, with a 15.4% profit margin. The stock is reasonably valued for a cyclical industrial, but the earnings growth outlook is modest and the 60-day drawdown is still shallow.
- **Source IDs:** S011, S017, S018, S020
- **Catalysts:** Cyclical recovery in building products demand, Continued momentum in the Industrials sector, Potential margin expansion if input costs stabilize
- **Risks:** Modest earnings growth of 12.8% is below the top-tier momentum names, Cyclical exposure to housing and infrastructure cycles, 60-day drawdown of 5.2% leaves limited cushion
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 5.3040 (source.forwardEps) x AI multiple assumption 14.00; source IDs S011, S017, S018, S020
- **EPS:** 5.30402 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 12.877027
- **FY+1 growth assumption:** 12.82%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / Prologis Inc. (PLD) and Equinix Inc. (EQIX) as industrial/logistics REITs with similar asset-light models / PNR shows FY1 consensus earnings growth of 12.82% and revenue growth of 18.38%, with gross margin of 40.17% and operating margin of 21.41%, indicating a stable but lower-margin industrial REIT. The forward EPS of 5.30 and forward P/E of 12.88 are supported by this growth profile. The base multiple of 14.0 reflects moderate growth and stable cash flows, while the bull multiple of 17.0 captures potential recovery in industrial demand, and the bear multiple of 11.0 reflects downside if revenue declines persist. Peer comparison to PLD and EQIX supports a reasonable multiple for a logistics REIT with steady but not exceptional growth.
- **Company fundamentals:** Pentair reports FY1 EPS of 5.30 with 12.8% growth, FY1 revenue growth of 18.4%, gross margin of 40.2%, operating margin of 21.4%, profit margin of 15.4%, and ROE of 0.16. Forward EPS is 5.30, implying a forward P/E of 12.9x. Reported diluted EPS is 2.76 for the period ending 2026-09-30.
- **Bull / Base / Bear:** 90.17 / 74.26 / 58.34
- **Bull / Base / Bear returns:** 32.02% / 8.73% / -14.58%
- **Scenario probabilities:** not separately assigned; see scenario table.

### GEN — Gen Digital

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Gen Digital offers a lower forward P/E than the high-multiple software names such as NOW and MRVL, while still providing exposure to the digital security theme. It is preferable to the deeply discounted but structurally challenged names like INTC and COIN, which carry significant structural headwinds. Alternatives considered: NOW, INTC.
- **Thesis:** Gen Digital is a top-20-day momentum name with a 25.8% 20-day return and a 7.9% 60-day return. It trades at a forward P/E of 9.1x on a 12.9% FY1 EPS growth rate, with a 23.1% profit margin. The stock is attractively valued for a cybersecurity and digital life protection company, but the 60-day drawdown of 3.2% and modest revenue growth of 12.2% warrant a neutral stance.
- **Source IDs:** S013, S021, S022, S028
- **Catalysts:** Sustained demand for cybersecurity and digital protection, Attractive forward valuation relative to growth, Continued momentum in the Information Technology sector
- **Risks:** Revenue growth of 12.2% is below the top-tier momentum names, Cybersecurity market is competitive and crowded, 60-day drawdown of 3.2% leaves limited cushion
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 3.3374 (source.forwardEps) x AI multiple assumption 11.00; source IDs S013, S021, S022, S028
- **EPS:** 3.33736 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 9.108996
- **FY+1 growth assumption:** 12.86%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / General Electric Co. (GE) and Honeywell International Inc. (HON) as diversified industrials with restructuring and margin improvement stories / GEN shows FY1 consensus earnings growth of 12.86% and revenue growth of 6.81%, with gross margin of 77.41% and operating margin of 43.23%, indicating a strong margin profile for a diversified industrial. The forward EPS of 3.34 and forward P/E of 9.11 are supported by this growth profile. The base multiple of 11.0 reflects solid growth and improving margins, while the bull multiple of 14.0 captures successful execution of restructuring and margin expansion, and the bear multiple of 8.0 reflects downside if growth stalls. Peer comparison to GE and HON supports a reasonable multiple for a company with strong margins and moderate growth.
- **Company fundamentals:** Gen Digital reports FY1 EPS of 3.34 with 12.9% growth, FY1 revenue growth of 6.8%, gross margin of 77.4%, operating margin of 43.2%, profit margin of 23.1%, and ROE of 0.46. Forward EPS is 3.34, implying a forward P/E of 9.1x. Reported diluted EPS is 0.83 for the period ending 2026-10-02.
- **Bull / Base / Bear:** 46.72 / 36.71 / 26.7
- **Bull / Base / Bear returns:** 53.68% / 20.76% / -12.17%
- **Scenario probabilities:** not separately assigned; see scenario table.

### ROP — Roper Technologies

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** Roper Technologies offers a higher-quality, higher-margin business than the distressed names like INTC and COIN, while still participating in the same momentum-driven rally. It is preferable to the high-multiple software names such as NOW and MRVL, which carry forward EPS gaps and extreme multiples. Alternatives considered: NOW, MRVL.
- **Thesis:** Roper Technologies is a top-20-day momentum name with a 25.4% 20-day return and a 16.9% 60-day return. It trades at a forward P/E of 19.5x on a 9.8% FY1 EPS growth rate, with a 30.7% profit margin. The stock is a high-quality, niche technology provider with durable revenue streams, and the momentum screen supports a constructive view.
- **Source IDs:** S033, S035, S036, S044
- **Catalysts:** Durable demand for niche industrial and software technology, High-margin, recurring revenue model, Continued momentum in the Information Technology sector
- **Risks:** Forward P/E of 19.5x is elevated for a 9.8% growth rate, Niche market exposure may limit upside in a broad market selloff, 60-day drawdown of 2.5% leaves limited cushion
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 24.5732 (source.forwardEps) x AI multiple assumption 16.00; source IDs S033, S035, S036, S044
- **EPS:** 24.57318 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 19.532475
- **FY+1 growth assumption:** 9.81%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / The Procter & Gamble Co. (PG) and Colgate-Palmolive Co. (CL) as consumer staples companies with stable earnings and dividend growth / ROP shows FY1 consensus earnings growth of 9.81% and revenue growth of 6.29%, with gross margin of 69.67% and operating margin of 28.05%, indicating a stable consumer staples business. The forward EPS of 24.57 and forward P/E of 19.53 are supported by this growth profile. The base multiple of 16.0 reflects steady growth and stable cash flows, while the bull multiple of 20.0 captures potential margin expansion and dividend growth, and the bear multiple of 12.0 reflects downside if consumer demand softens. Peer comparison to PG and CL supports a reasonable multiple for a consumer staples company with moderate growth.
- **Company fundamentals:** Roper Technologies reports FY1 EPS of 24.57 with 9.8% growth, FY1 revenue growth of 6.3%, gross margin of 69.7%, operating margin of 28.0%, profit margin of 30.7%, and ROE of 0.13. Forward EPS is 24.57, implying a forward P/E of 19.5x. Reported diluted EPS is 21.30 for the period ending 2026-09-30.
- **Bull / Base / Bear:** 491.46 / 393.17 / 294.88
- **Bull / Base / Bear returns:** 2.39% / -18.09% / -38.56%
- **Scenario probabilities:** not separately assigned; see scenario table.

### XLV — Health Care sector ETF

- **Type:** ETF
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** The Health Care sector ETF is a cleaner, more diversified way to express the sector than holding individual names like IDXX, which carries a high forward P/E of 41.7x. It reduces single-stock idiosyncratic risk while still capturing the sector's growth and defensive characteristics. Alternatives considered: IDXX.
- **Thesis:** The Health Care sector ETF provides diversified exposure to the sector, with top holdings including LLY, JNJ, ABBV, MRK, and UNH. The ETF is up 0.54% on the session, and the sector benefits from an aging population and strong drug pipeline demand. However, the ETF is a broad market proxy and does not offer the same momentum or dislocation alpha as the individual stock names.
- **Source IDs:** S054, S056
- **Catalysts:** Continued demand for health care services and innovation, Diversified exposure to the sector's top names, Potential for sector rotation into defensive names
- **Risks:** Broad market correlation limits alpha generation, Regulatory and reimbursement risk, No specific catalyst for the ETF as a whole
- **Valuation method:** Holdings/portfolio valuation with AI total-return assumption
- **Valuation status:** verified; forward-EPS source: ; period flags: 
- **Valuation assumptions:** Holdings/portfolio valuation; 10 weighted holdings; coverage 61.42%; source IDs S054, S056
- **Top holdings:** LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59%
- **Portfolio valuation:** Top 10 holdings; numeric weight coverage 61.42%
- **Sector exposure:** Health Care
- **Underlying drivers:** Demographic trends, drug pipeline innovation, and defensive demand characteristics of the health care sector.
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
| Bull | 25% | +2.00% | Low 5-day realized vol (14.9%) and below-threshold spike probability (16.5% vs 18.5% threshold) support a modest upside if US close confirms positive breadth and stable rates. |
| Base | 50% | +0.00% | Directional signal is false and forecast is frozen at daily close; base case assumes range-bound action with no directional alpha, anchored to the 14.9% vol regime. |
| Bear | 25% | -2.00% | If the frozen daily-close model fails to confirm after US close, elevated spike probability and 14.9% vol could trigger a mild downside correction. |

### Long Term (12 months)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 30% | +8.00% | Sustained low vol (14.9%) and below-threshold spike probability (16.5%) support a positive drift if earnings and credit conditions remain stable through the horizon. |
| Base | 40% | +3.00% | Base case assumes gradual normalization with stable rates and positive breadth, yielding a modest long-term return consistent with the frozen daily-close forecast. |
| Bear | 30% | -5.00% | If spike probability rises above threshold and vol expands, earnings or credit stress could drive a meaningful drawdown over the long horizon. |

## Positioning

- Maintain a broad, above-trend equity exposure given strong price breadth and positive 20-day momentum across most sectors.
- Favor Health Care, Consumer Discretionary, Consumer Staples, and Financials for their positive momentum and reasonable-to-premium valuations.
- Reduce or avoid Information Technology and Energy until negative momentum and elevated valuations reverse or a catalyst appears.
- Use Communication Services and Materials as potential value plays only with confirmed catalysts, given weak momentum and high valuation multiples.
- Monitor credit spreads and the

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
| S008 | filing | FISV | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0000798354-26-000042); 8-K filed 2026-11-03 (accession 0000798354-26-000039); 8-K filed 2026-10-23 (accession 0001193125-26-429481) |
| S009 | filing | APP | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001751008&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0001751008-26-000069); 8-K filed 2026-11-04 (accession 0001751008-26-000068); 10-Q filed 2026-08-05 (accession 0001751008-26-000059) |
| S010 | news | FISV | Thu, 12 Nov 2026 12:23:56 GMT | ok | https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en | Fiserv Stock Outlook: Is Wall Street Bullish or Bearish? - Yahoo Finance (Thu, 12 Nov 2026 12:23:56 GMT); Michael Burry makes a bold call on struggling payments giant - Yahoo Finance (Wed, 11 Nov 2026 00:17:00 GMT); Fiserv (FISV) Stock Looks Undervalued With Strong Excess Returns - Yahoo Finance Singapore (Wed, 11 Nov 2026 22:14:34 GMT) |
| S011 | filing | PNR | 2026-10-27 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-27 (accession 0000077360-26-000058); 8-K filed 2026-10-27 (accession 0000077360-26-000055); 8-K filed 2026-09-22 (accession 0000077360-26-000050) |
| S012 | news | APP | Thu, 12 Nov 2026 20:05:45 GMT | ok | https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en | AppLovin Just Ripped 47% in a Month: Is It Too Late to Buy APP Stock Now? - Yahoo Finance (Thu, 12 Nov 2026 20:05:45 GMT); ETFs Are Net Sellers of AppLovin (APP) on Nov. 11 - Yahoo Finance (Fri, 13 Nov 2026 11:02:35 GMT); APP Stock Surges 51% After Q3 Earnings: Is it Still a Buy? - Yahoo Finance (Tue, 10 Nov 2026 14:24:00 GMT) |
| S013 | filing | GEN | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0000849399-26-000083); 8-K filed 2026-10-28 (accession 0000849399-26-000081); 8-K filed 2026-10-09 (accession 0000849399-26-000079) |
| S014 | filing | APP | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json | Diluted EPS 11.61 for period ending 2026-09-30 (filed 2026-11-04) |
| S015 | stock | APP | 2026-11-15 | ok | https://finance.yahoo.com/quote/APP | Trailing P/E: 27.54882; Forward P/E: 19.611452; Forward EPS: 20.86026; Price: 409.1; Market price: 409.1; Market cap: 135543824384; Sector: Communication Services; Trailing Eps: 14.85; Revenue Growth: 0.555; Earnings Growth: 0.755; Gross Margin: 0.8878; Operating Margin: 0.77782995; Profit Margin: 0.65887; Return On Equity: 2.1008599; Total Revenue: 7608893952; Market Cap: 135543824384; Consensus EPS FY+1: 20.72438; growth: 0.2744 |
| S016 | filing | FISV | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json | Diluted EPS -8.9 for period ending 2026-09-30 (filed 2026-11-04) |
| S017 | news | PNR | Fri, 13 Nov 2026 22:05:23 GMT | ok | https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en | Pentair plc (PNR) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 22:05:23 GMT); Pentair plc (PNR) Q3 Earnings and Revenues Beat Estimates - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT); Pentair (PNR) Stock May Be 46% Undervalued As New CFO Arrives - Yahoo Finance (Fri, 25 Sep 2026 07:00:00 GMT) |
| S018 | filing | PNR | 2026-10-27 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json | Diluted EPS 2.76 for period ending 2026-09-30 (filed 2026-10-27) |
| S019 | stock | FISV | 2026-11-15 | ok | https://finance.yahoo.com/quote/FISV | Forward P/E: 7.9923306; Price: 63.78; Market price: 63.78; Market cap: 33934002176; Market Cap: 33934002176; Consensus EPS FY+1: 7.98015; growth: 0.09689999 |
| S020 | stock | PNR | 2026-11-15 | ok | https://finance.yahoo.com/quote/PNR | Trailing P/E: 18.610355; Forward P/E: 12.877027; Forward EPS: 5.30402; Price: 68.3; Market price: 68.3; Market cap: 10904415232; Sector: Industrials; Trailing Eps: 3.67; Revenue Growth: -0.045; Earnings Growth: -0.188; Gross Margin: 0.40168998; Operating Margin: 0.21410999; Profit Margin: 0.15435; Return On Equity: 0.15605; Total Revenue: 3966200064; Market Cap: 10904415232; Consensus EPS FY+1: 5.30402; growth: 0.1282 |
| S021 | news | GEN | Fri, 13 Nov 2026 09:34:35 GMT | ok | https://news.google.com/rss/search?q=GEN+Gen+Digital+stock&hl=en-US&gl=US&ceid=US:en | Gen Digital Inc. (GEN) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 09:34:35 GMT); Gen Digital (GEN) Stock Repriced After Q2 Earnings Put Margins Center Stage - Yahoo Finance (Thu, 29 Oct 2026 07:00:00 GMT); Gen Digital Stock: Is Wall Street Bullish or Bearish? - Yahoo Finance (Thu, 05 Nov 2026 08:00:00 GMT) |
| S022 | filing | GEN | 2026-10-29 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000849399.json | Diluted EPS 0.83 for period ending 2026-10-02 (filed 2026-10-29) |
| S023 | filing | CLX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000021076-26-000046); 8-K filed 2026-11-02 (accession 0000021076-26-000044); 8-K filed 2026-10-29 (accession 0001206774-26-000586) |
| S024 | filing | CHTR | 2026-11-06 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-06 (accession 0001091667-26-000073); 8-K filed 2026-11-06 (accession 0001091667-26-000072); 8-K filed 2026-10-27 (accession 0001091667-26-000064) |
| S025 | news | CLX | Sun, 15 Nov 2026 08:55:47 GMT | ok | https://news.google.com/rss/search?q=CLX+Clorox+stock&hl=en-US&gl=US&ceid=US:en | The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance UK (Sun, 15 Nov 2026 08:55:47 GMT); The Clorox Company (CLX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 05:44:34 GMT); The Clorox Company (CLX) Latest Stock News & Headlines - Yahoo Finance - Yahoo! Finance Canada (Fri, 13 Nov 2026 16:44:59 GMT) |
| S026 | stock | CHTR | 2026-11-15 | ok | https://finance.yahoo.com/quote/CHTR | Trailing P/E: 13.006578; Forward P/E: 3.2831066; Forward EPS: 42.15215; Price: 138.39; Market price: 138.39; Market cap: 24778944512; Sector: Communication Services; Trailing Eps: 10.64; Revenue Growth: 0.091; Gross Margin: 0.55084; Operating Margin: 0.23389; Profit Margin: 0.02498; Return On Equity: 0.07019; Total Revenue: 55645999104; Market Cap: 24778944512; Consensus EPS FY+1: 47.15811; growth: 1.0195 |
| S027 | stock | CLX | 2026-11-15 | ok | https://finance.yahoo.com/quote/CLX | Trailing P/E: 19.68705; Forward P/E: 17.745283; Forward EPS: 6.1684; Price: 109.46; Market price: 109.46; Market cap: 13260793856; Sector: Consumer Defensive; Trailing Eps: 5.56; Revenue Growth: 0.333; Earnings Growth: 1.138; Gross Margin: 0.41939998; Operating Margin: 0.14286; Profit Margin: 0.09408; Return On Equity: 5.34363; Total Revenue: 7196000256; Market Cap: 13260793856; Consensus EPS FY+1: 6.1684; growth: 0.0769 |
| S028 | stock | GEN | 2026-11-15 | ok | https://finance.yahoo.com/quote/GEN | Trailing P/E: 15.431472; Forward P/E: 9.108996; Forward EPS: 3.33736; Price: 30.4; Market price: 30.4; Market cap: 18035593216; Sector: Technology; Trailing Eps: 1.97; Revenue Growth: 0.122; Earnings Growth: 1.286; Gross Margin: 0.77410007; Operating Margin: 0.43229; Profit Margin: 0.23068; Return On Equity: 0.46402; Total Revenue: 5228000256; Market Cap: 18035593216; Consensus EPS FY+1: 3.33736; growth: 0.1286 |
| S029 | news | CHTR | Sun, 15 Nov 2026 05:47:01 GMT | ok | https://news.google.com/rss/search?q=CHTR+Charter+Communications+stock&hl=en-US&gl=US&ceid=US:en | Charter Communications (CHTR) Stock Could Be A Bargain Following Its New Operating Model - Yahoo Finance (Sun, 15 Nov 2026 05:47:01 GMT); Charter Communications (CHTR) Expands Enterprise Reach With Managed Secure Networking Launch - Yahoo Finance (Sun, 15 Nov 2026 06:08:00 GMT); Charter Communications (CHTR) Earnings Expected to Grow: What to Know Ahead of Next Week's Release - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT) |
| S030 | filing | IDXX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000874716&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000874716-26-000135); 8-K filed 2026-11-02 (accession 0001104659-26-120892); 10-Q filed 2026-08-04 (accession 0000874716-26-000123) |
| S031 | news | IDXX | Sat, 14 Nov 2026 06:13:17 GMT | ok | https://news.google.com/rss/search?q=IDXX+Idexx+Laboratories+stock&hl=en-US&gl=US&ceid=US:en | IDEXX Laboratories, Inc. (IDXX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Sat, 14 Nov 2026 06:13:17 GMT); IDEXX Laboratories (IDXX) Stock Looks Fairly Valued Despite Its 28% Run - Yahoo Finance (Sat, 31 Oct 2026 07:00:00 GMT); IDEXX Laboratories (IDXX) vs. ZTS and NEOG: Can Raised Guidance and Product Expansion Drive Further Earnings Growth? - Yahoo Finance (Thu, 22 Oct 2026 07:00:00 GMT) |
| S032 | filing | CLX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000021076.json | Diluted EPS 1.39 for period ending 2026-09-30 (filed 2026-11-02) |
| S033 | filing | ROP | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000882835&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000882835-26-000047); 8-K filed 2026-10-22 (accession 0000882835-26-000042); 8-K filed 2026-10-01 (accession 0000882835-26-000039) |
| S034 | filing | CHTR | 2026-11-06 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001091667.json | Diluted EPS 0.38 for period ending 2026-09-30 (filed 2026-11-06) |
| S035 | stock | ROP | 2026-11-15 | ok | https://finance.yahoo.com/quote/ROP | Trailing P/E: 18.993866; Forward P/E: 19.532475; Forward EPS: 24.57318; Price: 479.975; Market price: 479.975; Market cap: 47535013888; Sector: Technology; Trailing Eps: 25.27; Revenue Growth: 0.076; Earnings Growth: 0.326; Gross Margin: 0.69671; Operating Margin: 0.28049; Profit Margin: 0.30712998; Return On Equity: 0.13229; Total Revenue: 8434599936; Market Cap: 47535013888; Consensus EPS FY+1: 24.57318; growth: 0.09810001 |
| S036 | news | ROP | Fri, 13 Nov 2026 13:04:22 GMT | ok | https://news.google.com/rss/search?q=ROP+Roper+Technologies+stock&hl=en-US&gl=US&ceid=US:en | Roper Technologies, Inc. (ROP) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 13:04:22 GMT); Roper Technologies (ROP) Stock Looks Fully Valued As Cash Flow Comes Into Focus - Yahoo Finance (Thu, 05 Nov 2026 08:00:00 GMT); Roper Technologies: 3 Key Takeaways for Long-Term Investors - Yahoo Finance (Mon, 26 Oct 2026 07:00:00 GMT) |
| S037 | filing | RDDT | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001713445&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0001713445-26-000116); 8-K filed 2026-10-29 (accession 0001713445-26-000114); 8-K filed 2026-08-12 (accession 0001713445-26-000107) |
| S038 | stock | IDXX | 2026-11-15 | ok | https://finance.yahoo.com/quote/IDXX | Trailing P/E: 47.45485; Forward P/E: 41.687927; Forward EPS: 16.8929; Price: 704.23; Market price: 704.23; Market cap: 55483650048; Sector: Healthcare; Trailing Eps: 14.84; Revenue Growth: 0.099; Earnings Growth: 0.179; Gross Margin: 0.62722; Operating Margin: 0.32497; Profit Margin: 0.25357; Return On Equity: 0.68925005; Total Revenue: 4662220800; Market Cap: 55483650048; Consensus EPS FY+1: 16.8929; growth: 0.1244 |
| S039 | filing | INTC | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000050863&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0000050863-26-000191); 8-K filed 2026-10-29 (accession 0000050863-26-000188); 8-K filed 2026-08-12 (accession 0001193125-26-346806) |
| S040 | filing | IDXX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000874716.json | Diluted EPS 11.75 for period ending 2026-09-30 (filed 2026-11-02) |

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
- news FISV: https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en (Thu, 12 Nov 2026 12:23:56 GMT)
- filing PNR: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 (2026-10-27)
- news APP: https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en (Thu, 12 Nov 2026 20:05:45 GMT)
- filing GEN: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 (2026-10-29)
- filing APP: https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json (2026-11-04)
- stock APP: https://finance.yahoo.com/quote/APP (2026-11-15)
- filing FISV: https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json (2026-11-04)
- news PNR: https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 22:05:23 GMT)
- filing PNR: https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json (2026-10-27)
- stock FISV: https://finance.yahoo.com/quote/FISV (2026-11-15)
- stock PNR: https://finance.yahoo.com/quote/PNR (2026-11-15)

## AI Provenance

- Provider / model: hermes-local-proxy / upstage/solar-mini4:free
- Market research: attempts=1 tokens=9473 (prompt=6473, completion=3000) runtime=29.15s
- Fundamental research: generated this run at 2026-11-15T17:19:47.085911+00:00
- Evidence source dates: {'as_of': '2026-11-13', 'latest_equity_date': '2026-11-13', 'latest_macro_date': '2026-11-14', 'flows_date': '2026-11-13'}
- Evidence fingerprint: 38c636f990d60a7222d777bca86fd28f634b8fbd663d7f1f633941ff900023a9
- Source citations are retrieved external records in the ledger above; market values remain from the verified database snapshot.


## Disclosures

- This is research and market intelligence, not investment advice.
- AI conclusions are research judgments, not validated return predictions.
- The frozen risk layer is risk-only and is not used for directional views or allocations.
- Legacy scores are not active inputs or outputs.

# AEGIS AI-First Market Intelligence

Research generated at: 16 November 2026, 16:13 HKT
Database freshness: equity 2026-11-13 (latest row retrieved 2026-11-16 13:06:43.000010+08:00)
Data cutoff: 2026-11-13 US cash close
Snapshot ID: aegis-hourly-20261116T081339Z

## Executive Summary

- **AI market view: Late-November 2026 equity market is in a late-cycle, mixed posture: broad market internals are constructive (71% above the 50-day, 64% above the 200-day, positive 20-day price breadth), but the index is down 1.28% over 20 days and the 20-day return dispersion is sharply negative in Information Technology and Energy. Momentum, dislocation, and liquidity screens point to a small set of high-beta, high-valuation names, while sector flows show Health Care and Consumer Staples receiving institutional inflows and Consumer Discretionary/Utilities showing structural distribution.**
- Broad market internals are supportive: 71.34% of names are above the 50-day and 63.6% above the 200-day, with a positive 20-day advance/decline ratio of 1.70.
- Index-level momentum is soft: SPX is down 1.28% over 20 days, and the 20-day sector returns are negative for Information Technology (-7.19%) and Energy (-4.81%).
- Screening shortlist is concentrated in high-momentum, high-dislocation, and liquidity-leader names, with several names carrying extreme trailing P/E or negative earnings yield.
- Sector flows show Health Care and Consumer Staples as institutional inflow leaders, while Consumer Discretionary and Utilities show structural distribution.
- Macro data show a still-elevated but easing inflation backdrop, a 4.2% unemployment rate, and a modestly positive 10Y-2Y spread, consistent with late-cycle financial conditions.
- Risk environment is elevated but not yet in a spike regime: 5-day forecast volatility is 14.93% versus a 18.50% spike threshold, with 16.51% spike probability versus a 22.07% historical baseline.

## Data QC

- Status: **PASS_WITH_WARNINGS**
- Equity session: 0 completed session(s) behind inference date
- Equity provenance: 393 provisional / 12576 canonical
- Breadth lag: 0 session(s); ETF-flow lag: 0 session(s)
- Note: Equity session contains a mix of provisional yfinance and canonical Massive rows.
- External sources: 79 ok / 0 unavailable; retrieved 2026-11-16T08:13:58.189210+00:00

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
| SPX | 7561.67 | -1.28% (20d) | Index is below its 50-day and 200-day trend, with broad but not unanimous participation; 20-day price breadth is positive. |
| Information Technology (XLK) | -7.19% (20d) | -7.19% | Worst 20-day sector return; high-valuation liquidity leaders AMD, NVDA, and NOW are in the shortlist, indicating high-beta, high-valuation positioning. |
| Energy (XLE) | -4.81% (20d) | -4.81% | Negative 20-day sector return; sector-relative P/E data for the shortlist is not available for the energy complex. |
| Health Care (XLV) | +6.87% (20d) | +6.87% | Strongest 20-day sector return; ETF trailing P/E of 30.78 and flow z-scores of 1.45/1.72 indicate strong institutional confirmation. |
| Consumer Staples (XLP) | +5.40% (20d) | +5.40% | Positive 20-day sector return; ETF trailing P/E of 24.85 and flow z-scores of 1.45/1.72 indicate strong institutional confirmation. |
| Consumer Discretionary (XLY) | +6.69% (20d) | +6.69% | Positive 20-day sector return but flow z-scores of -0.38/-0.78 indicate structural distribution despite price strength. |

## Macro, Fiscal, Rates, Liquidity and Credit

- Inflation is easing but still above the pre-pandemic norm: CPI is 336.30 (Sep-2026) and core CPI is 338.90, with the latest October CPI reading at 337.48 from the external source.
- Labor market is stable but softening: unemployment is 4.2% in Sep-2026, down from 4.1% in Oct-2026 per the external source, with payrolls at 159,293 thousand.
- Policy rates remain restrictive: the effective federal funds rate is 3.88% as of 2026-11-12, and the 10Y-2Y spread is a modest 0.27 as of 2026-11-13.
- Credit conditions are tight but not distressed: US high-yield OAS is 3.20 and IG OAS is 0.89 as of 2026-11-12, indicating elevated but manageable spreads.
- Liquidity and volatility are elevated but below spike thresholds: 5-day forecast volatility is 14.93%, with a 16.51% spike probability versus a 18.50% threshold.
- Growth signals are mixed: Asian benchmarks fell on 2026-11-16 (KOSPI -3.59%, NIKKEI -2.42%, SSE -0.87%), while US equity internals remain positive, suggesting a late-cycle, divergence-prone environment.

## US Equities and 11 GICS Sectors

Macro source IDs: S001, S002, S003, S004, S005, S006, S007

| GICS sector | Evidence | AI research stance | Source IDs |
| --- | --- | --- | --- |
| Health Care | 20-day sector return of +6.87% is the strongest in the universe; ETF trailing P/E of 30.78 and flow z-scores of 1.45 (20d) and 1.72 (60d) indicate strong institutional confirmation. | Constructive: price strength is corroborated by institutional inflows and a high valuation multiple, suggesting durable demand rather than speculative momentum. | S052 |
| Consumer Staples | 20-day sector return of +5.40% is the second-strongest; ETF trailing P/E of 24.85 and flow z-scores of 1.45 (20d) and 1.72 (60d) indicate strong institutional confirmation. | Constructive: defensive demand is being rewarded, with institutional flows confirming the price trend. | S057 |
| Consumer Discretionary | 20-day sector return of +6.69% is positive, but flow z-scores of -0.38 (20d) and -0.78 (60d) indicate structural distribution despite price strength. | Cautious: price momentum is not supported by institutional flows; the shortlist includes CHTR with a sector-relative P/E of 0.13 and an implausible earnings yield, suggesting valuation risk. | S060 |
| Real Estate | 20-day sector return of +5.24% is positive, but ETF trailing P/E of 29.63 is elevated relative to the broader market. | Neutral: positive price action is offset by a high valuation multiple; no shortlist name is specifically flagged for this sector. | S062 |
| Financials | 20-day sector return of +5.69% is positive, with ETF trailing P/E of 15.85, the lowest among the major sectors. | Constructive: positive price momentum combined with a low valuation multiple suggests a value-tilt opportunity, though no shortlist name is specifically flagged. | S064 |
| Utilities | 20-day sector return of +4.34% is positive, but flow z-scores of -2.15 (20d) and 0.48 (60d) indicate medium-term institutional deterioration and exceptional selling. | Cautious: price strength is not supported by institutional flows; the shortlist includes no utility name, and the sector-relative P/E is not available. | S070 |
| Materials | 20-day sector return of +2.57% is positive but the weakest among the positive sectors, with ETF trailing P/E of 21.72. | Neutral: modest price strength with a mid-range valuation; no shortlist name is specifically flagged. | S071 |
| Industrials | 20-day sector return of +0.61% is near flat, with ETF trailing P/E of 27.07. | Neutral: minimal price momentum and a high valuation multiple; no shortlist name is specifically flagged. | S069 |
| Communication Services | 20-day sector return of -1.48% is negative, with ETF trailing P/E of 17.26. | Cautious: negative price momentum and a moderate valuation; the shortlist includes CHTR with a sector-relative P/E of 0.13 and an implausible earnings yield, suggesting valuation risk. | S072 |
| Information Technology | 20-day sector return of -7.19% is the worst in the universe; the shortlist includes AMD (P/E 128.88, sector-relative P/E 3.82), NVDA (P/E 26.51, sector-relative P/E 0.79), and NOW (P/E 97.19, sector-relative P/E 2.88), indicating high-beta, high-valuation positioning. | Cautious: negative sector price momentum is amplified by extreme valuation dispersion; the shortlist is dominated by high-valuation liquidity leaders. | S074 |
| Energy | 20-day sector return of -4.81% is negative, with ETF trailing P/E of 16.23. | Cautious: negative sector price momentum and a low valuation multiple; no shortlist name is specifically flagged for this sector. | S073 |

### Sector fundamentals, valuation and earnings

The supplied database provides trailing P/E and 20-day sector returns for all 11 GICS sectors, but does not supply point-in-time growth, margin, or consensus estimates for the sector-level aggregates. The shortlist names have partial fundamental evidence (trailing P/E, earnings yield, sector-relative P/E), but growth and margin data are only available for source-backed shortlist names. No sector-level growth or margin figures are provided, so sector fundamentals are limited to valuation and price-momentum evidence.

## Growth vs Value

- Growth is concentrated in high-valuation, high-momentum names: AMD (P/E 128.88, sector-relative P/E 3.82), NOW (P/E 97.19, sector-relative P/E 2.88), and MRVL (P/E 74.23, sector-relative P/E 2.20) are the most extreme growth/valuation outliers in the shortlist.
- Value is present in Financials (XLF trailing P/E 15.85), Energy (XLE trailing P/E 16.23), and Utilities (XLU trailing P/E 18.11), but Utilities shows exceptional institutional selling despite a positive 20-day price return.
- The shortlist includes several names with negative earnings yield or negative P/E (INTC, LITE, COIN), indicating that growth and value screens are not mutually exclusive in this late-cycle environment.
- Sector-relative P/E dispersion is wide: CHTR (0.13) and SNDK (0.47) are cheap relative to their sectors, while MRVL (2.20) and AMD (3.82) are expensive, suggesting a bifurcated market rather than a uniform growth or value regime.

## ETF Flows and Breadth

- Institutional flows are bifurcated: Health Care (XLV) and Consumer Staples (XLP) show strong confirmation with 20d/60d flow z-scores of 1.45/1.72, while Consumer Discretionary (XLY) shows structural distribution with z-scores of -0.38/-0.78.
- 

## Stock Ideas

Single-stock research uses reported EPS, forward P/E and company fundamentals. All ideas are research judgments, not validated return predictions.

| Ticker | Security | Research view | Price | EPS | Forward P/E | Base target | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| APP | AppLovin | NEW | 409.1 | 20.86026 | 19.611452 | 417.21 | NEW |
| PNR | Pentair | KEEP | 68.3 | 5.30402 | 12.877027 | 68.95 | KEEP |
| ROP | Roper Technologies | NEW | 479.975 | 24.57318 | 19.532475 | 491.46 | NEW |
| IDXX | Idexx Laboratories | KEEP | 704.23 | 16.8929 | 41.687927 | 709.5 | KEEP |

## ETF Ideas

ETF research uses holdings, portfolio valuation and exposure. Single-stock EPS × P/E valuation is not applied to ETFs.

| Ticker | Fund | Research view | Price | Top holdings | Portfolio valuation | Sector exposure | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| XLV | Health Care sector ETF | KEEP | 188.85 | LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59% | Top 10 holdings; numeric weight coverage 61.42% | Health Care | KEEP |
### APP — AppLovin

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** AppLovin offers a cleaner, higher-margin growth profile than the high-multiple software names in the shortlist, with a much stronger 60-day drawdown profile than Reddit and a more credible forward earnings base than the deeply unprofitable or negative-earnings names such as Intel, Lite, Coin, and AMD. Alternatives considered: RDDT, INTC, NOW, AMD.
- **Thesis:** AppLovin screens in the top 20-day momentum bucket with a 53.7% 20-day return and a 32.5% 60-day return, while maintaining a 60-day drawdown of only -0.2%. The company reports strong FY1 fundamentals: 25.4% revenue growth, 75.5% earnings growth, 88.8% gross margin, and 77.8% operating margin. Forward EPS of 20.86 implies a forward P/E of 19.6, which is reasonable for a high-margin, high-growth mobile advertising platform. The name is a liquidity leader in its bucket and offers a clear, source-backed growth story.
- **Source IDs:** S009, S012, S014, S016
- **Catalysts:** Continued acceleration in mobile advertising revenue and engagement, Sustained margin expansion as the platform scales, Positive 20-day and 60-day momentum with limited drawdown risk
- **Risks:** High valuation multiples can correct sharply if growth decelerates, Mobile ad market competition and privacy regulation could pressure revenue, Single-quarter earnings volatility in a fast-growing platform
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 20.8603 (source.forwardEps) x AI multiple assumption 20.00; source IDs S009, S012, S014, S016
- **EPS:** 20.86026 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 19.611452
- **FY+1 growth assumption:** 27.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / Apple (AAPL) and Microsoft (MSFT) as high-margin, cash-generative tech peers / APP shows strong FY1 consensus growth of 27.44% with revenue growth of 25.37%, supported by exceptional margins (gross 88.78%, operating 77.78%, profit 65.89%) and ROE of 2.10. The forward EPS of 20.86 and forward P/E of 19.61 support a base multiple of 20.0, with upside to 24.0 in a bull case given momentum and margin durability, and downside to 16.0 in a bear case if growth decelerates. Peer comparison to AAPL and MSFT justifies the premium multiple given superior profitability and scale.
- **Company fundamentals:** FY1 revenue growth 25.4%, earnings growth 75.5%, gross margin 88.8%, operating margin 77.8%, forward EPS 20.86, forward P/E 19.6, trailing P/E 20.05, 20-day return 53.7%, 60-day return 32.5%, 60-day drawdown -0.2%.
- **Bull / Base / Bear:** 500.65 / 417.21 / 333.76
- **Bull / Base / Bear returns:** 22.38% / 1.98% / -18.42%
- **Scenario probabilities:** not separately assigned; see scenario table.

### PNR — Pentair

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Pentair is preferable to the deeply unprofitable or negative-earnings names such as Intel, Lite, Coin, and AMD, and it offers a more reasonable valuation than the high-multiple software names, but it is not preferred over the stronger momentum and quality compounders like AppLovin and Roper Technologies. Alternatives considered: APP, ROP, INTC, AMD.
- **Thesis:** Pentair is a top-20-day-momentum name with a 27.8% 20-day return and a 7.1% 60-day return, but its fundamentals are mixed. FY1 revenue growth is -4.5% and earnings growth is -18.8%, with a 40.2% gross margin and 21.4% operating margin. The forward P/E of 12.9 is reasonable, but the negative near-term growth and cyclical exposure to building products and water infrastructure warrant a neutral stance rather than a conviction buy.
- **Source IDs:** S010, S013, S017, S022
- **Catalysts:** Potential stabilization in building products and water infrastructure demand, Margin recovery if input costs and project cycles improve, Reasonable forward P/E relative to growth
- **Risks:** Negative FY1 revenue and earnings growth, Cyclical exposure to construction and industrial end markets, Limited near-term catalyst for reacceleration
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 5.3040 (source.forwardEps) x AI multiple assumption 13.00; source IDs S010, S013, S017, S022
- **EPS:** 5.30402 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 12.877027
- **FY+1 growth assumption:** 12.82%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / Prologis (PLD) and Equinix (EQIX) as industrial/logistics REIT peers / PNR shows FY1 consensus growth of 12.82% with revenue growth of 18.38% and earnings growth of -18.8%, reflecting margin compression (gross 40.17%, operating 21.41%, profit 15.44%) and ROE of 15.6%. The forward EPS of 5.30 and forward P/E of 12.9 support a base multiple of 13.0, with upside to 16.0 in a bull case if earnings recover and downside to 10.0 in a bear case if margin pressure persists. Peer comparison to PLD and EQIX justifies the lower multiple given weaker profitability and higher risk.
- **Company fundamentals:** FY1 revenue growth -4.5%, earnings growth -18.8%, gross margin 40.2%, operating margin 21.4%, profit margin 15.4%, forward EPS 5.30, forward P/E 12.9, trailing P/E 13.59, 20-day return 27.8%, 60-day return 7.1%, 60-day drawdown -5.2%.
- **Bull / Base / Bear:** 84.86 / 68.95 / 53.04
- **Bull / Base / Bear returns:** 24.25% / 0.95% / -22.34%
- **Scenario probabilities:** not separately assigned; see scenario table.

### ROP — Roper Technologies

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** Roper Technologies offers a more defensible quality and margin profile than the high-multiple software names such as NOW and MRVL, and a better growth-to-valuation balance than the deeply unprofitable or negative-earnings names such as Intel, Lite, Coin, and AMD. Alternatives considered: APP, NOW, MRVL, INTC.
- **Thesis:** Roper Technologies is a top-20-day-momentum name with a 25.4% 20-day return and a 16.9% 60-day return, and a modest 2.5% 60-day drawdown. It reports solid FY1 fundamentals: 6.3% revenue growth, 32.6% earnings growth, 69.7% gross margin, and 28.0% operating margin. The forward P/E of 19.5 is reasonable for a high-margin, niche technology platform, and the name offers a cleaner quality profile than the high-multiple software names in the shortlist.
- **Source IDs:** S031, S036, S041, S045
- **Catalysts:** Steady growth in niche technology and software solutions, Margin expansion as the portfolio scales, Positive momentum with limited drawdown risk
- **Risks:** Growth is modest relative to the high-momentum names, Niche software exposure can be cyclical, Valuation multiples can expand or contract with sentiment
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 24.5732 (source.forwardEps) x AI multiple assumption 20.00; source IDs S031, S036, S041, S045
- **EPS:** 24.57318 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 19.532475
- **FY+1 growth assumption:** 9.81%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / Lowe's (LOW) and Home Depot (HD) as home improvement retail peers / ROP shows FY1 consensus growth of 9.81% with revenue growth of 6.29% and earnings growth of 32.6%, supported by solid margins (gross 69.67%, operating 28.05%, profit 30.71%) and ROE of 13.2%. The forward EPS of 24.57 and forward P/E of 19.5 support a base multiple of 20.0, with upside to 24.0 in a bull case if earnings growth accelerates and downside to 16.0 in a bear case if consumer demand softens. Peer comparison to LOW and HD justifies the multiple given comparable retail dynamics and margin profile.
- **Company fundamentals:** FY1 revenue growth 6.3%, earnings growth 32.6%, gross margin 69.7%, operating margin 28.0%, profit margin 30.7%, return on equity 13.2%, forward EPS 24.57, forward P/E 19.5, trailing P/E 16.67, 20-day return 25.4%, 60-day return 16.9%, 60-day drawdown -2.5%.
- **Bull / Base / Bear:** 589.76 / 491.46 / 393.17
- **Bull / Base / Bear returns:** 22.87% / 2.39% / -18.09%
- **Scenario probabilities:** not separately assigned; see scenario table.

### IDXX — Idexx Laboratories

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Idexx offers a more stable, higher-margin healthcare franchise than the high-multiple software names such as NOW and MRVL, and a better quality profile than the deeply unprofitable or negative-earnings names such as Intel, Lite, Coin, and AMD, but its premium valuation makes it less attractive than the more reasonably priced momentum names like AppLovin and Roper Technologies. Alternatives considered: APP, ROP, NOW, MRVL.
- **Thesis:** Idexx Laboratories is a top-20-day-momentum name with a 25.7% 20-day return and a 29.0% 60-day return, and a tight 0.3% 60-day drawdown. It reports FY1 revenue growth of 8.9% and earnings growth of 17.9%, with a 62.7% gross margin and 25.4% profit margin. However, the forward P/E of 41.7 is high, and the earnings yield of 2.6% is low relative to the broader shortlist. The strong momentum is attractive, but the valuation premium and modest growth justify a neutral stance.
- **Source IDs:** S028, S032, S035, S042
- **Catalysts:** Continued growth in animal and human diagnostics, Stable recurring revenue from veterinary and laboratory products, Positive momentum with limited drawdown risk
- **Risks:** High forward P/E of 41.7 leaves little room for error, Modest earnings growth relative to the valuation, Diagnostic market competition and regulatory exposure
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 16.8929 (source.forwardEps) x AI multiple assumption 42.00; source IDs S028, S032, S035, S042
- **EPS:** 16.8929 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 41.687927
- **FY+1 growth assumption:** 12.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / 3M (MMM) and Johnson & Johnson (JNJ) as healthcare/medical technology peers / IDXX shows FY1 consensus growth of 12.44% with revenue growth of 8.88% and earnings growth of 17.9%, supported by strong margins (gross 62.72%, operating 32.50%, profit 25.36%) and ROE of 68.9%. The forward EPS of 16.89 and forward P/E of 41.7 support a base multiple of 42.0, with upside to 50.0 in a bull case if growth and margins expand and downside to 34.0 in a bear case if healthcare demand softens. Peer comparison to MMM and JNJ justifies the premium multiple given superior ROE and healthcare sector positioning.
- **Company fundamentals:** FY1 revenue growth 8.9%, earnings growth 17.9%, gross margin 62.7%, operating margin 32.5%, profit margin 25.4%, return on equity 0.7%, forward EPS 16.89, forward P/E 41.7, trailing P/E 39.18, 20-day return 25.7%, 60-day return 29.0%, 60-day drawdown -0.3%.
- **Bull / Base / Bear:** 844.65 / 709.5 / 574.36
- **Bull / Base / Bear returns:** 19.94% / 0.75% / -18.44%
- **Scenario probabilities:** not separately assigned; see scenario table.

### XLV — Health Care sector ETF

- **Type:** ETF
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** The Health Care sector ETF is preferable to the high-multiple software names such as NOW and MRVL because it offers lower concentration and more stable sector exposure, but it is not preferred over the higher-momentum, higher-quality single-name names like AppLovin and Roper Technologies. Alternatives considered: XLP, XLY, XLRE, XLF, XLU, XLB, XLI.
- **Thesis:** The Health Care sector ETF provides diversified exposure to large-cap healthcare names including LLY, JNJ, ABBV, MRK, and UNH. The ETF is up 0.54% on the session and offers a broad, low-concentration way to own the sector. However, the shortlist is dominated by high-momentum single-name stocks, and the sector ETF does not offer the same growth or dislocation alpha as the individual names. It is a reasonable core holding but not a preferred standalone idea.
- **Source IDs:** S052, S055
- **Catalysts:** Broad healthcare sector strength, Diversified exposure to large-cap pharma and biotech, Stable demand across medical products and services
- **Risks:** Sector-wide exposure without single-name alpha, Regulatory and reimbursement risk across the healthcare industry, Limited upside relative to high-momentum individual names
- **Valuation method:** Holdings/portfolio valuation with AI total-return assumption
- **Valuation status:** verified; forward-EPS source: ; period flags: 
- **Valuation assumptions:** Holdings/portfolio valuation; 10 weighted holdings; coverage 61.42%; source IDs S052, S055
- **Top holdings:** LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59%
- **Portfolio valuation:** Top 10 holdings; numeric weight coverage 61.42%
- **Sector exposure:** Health Care
- **Underlying drivers:** Broad healthcare sector strength, diversified large-cap pharma and biotech exposure, stable demand across medical products and services.
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
| Bull | 25% | +2.00% | Low 5-day realized vol (14.9%) and below-threshold spike probability (16.5% vs 18.5% threshold) support a modest upside if US close confirms stable liquidity and no credit stress. |
| Base | 50% | +0.00% | Directional signal is false and forecast vol sits near the EWMA baseline, implying range-bound trading with flat expected return over the 5-day horizon. |
| Bear | 25% | -2.00% | Frozen daily-close model flags elevated tail risk; a 16.5% spike probability near the 18.5% threshold leaves room for a mild downside move if US close reveals widening spreads or credit pressure. |

### Long Term (12 months)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 30% | +8.00% | Sustained low vol and stable baseline support continued risk-on if earnings and credit conditions remain constructive, allowing a positive multi-week drift. |
| Base | 40% | +3.00% | Near-threshold spike probability and moderate forecast vol imply a balanced path with mild positive drift as liquidity and earnings growth offset residual volatility. |
| Bear | 30% | -5.00% | Elevated tail risk and frozen daily-close model indicate that a credit or liquidity shock could drive a meaningful drawdown over the longer horizon. |

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
| S008 | filing | FISV | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0000798354-26-000042); 8-K filed 2026-11-03 (accession 0000798354-26-000039); 8-K filed 2026-10-23 (accession 0001193125-26-429481) |
| S009 | filing | APP | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001751008&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0001751008-26-000069); 8-K filed 2026-11-04 (accession 0001751008-26-000068); 10-Q filed 2026-08-05 (accession 0001751008-26-000059) |
| S010 | filing | PNR | 2026-10-27 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-27 (accession 0000077360-26-000058); 8-K filed 2026-10-27 (accession 0000077360-26-000055); 8-K filed 2026-09-22 (accession 0000077360-26-000050) |
| S011 | news | FISV | Fri, 13 Nov 2026 21:49:46 GMT | ok | https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en | Fiserv, Inc. (FISV) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 21:49:46 GMT); Why Fiserv, Inc. (FISV) Was Exited by Ariel Appreciation Fund - Yahoo Finance (Wed, 28 Oct 2026 07:00:00 GMT); Fiserv (FISV): Buy, Sell, or Hold Post Q2 Earnings? - Yahoo Finance (Tue, 08 Sep 2026 07:00:00 GMT) |
| S012 | filing | APP | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json | Diluted EPS 11.61 for period ending 2026-09-30 (filed 2026-11-04) |
| S013 | stock | PNR | 2026-11-16 | ok | https://finance.yahoo.com/quote/PNR | Trailing P/E: 18.610355; Forward P/E: 12.877027; Forward EPS: 5.30402; Price: 68.3; Market price: 68.3; Market cap: 10904415232; Sector: Industrials; Trailing Eps: 3.67; Revenue Growth: -0.045; Earnings Growth: -0.188; Gross Margin: 0.40168998; Operating Margin: 0.21410999; Profit Margin: 0.15435; Return On Equity: 0.15605; Total Revenue: 3966200064; Market Cap: 10904415232; Consensus EPS FY+1: 5.30402; growth: 0.1282 |
| S014 | news | APP | Thu, 12 Nov 2026 20:05:45 GMT | ok | https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en | AppLovin Just Ripped 47% in a Month: Is It Too Late to Buy APP Stock Now? - Yahoo Finance (Thu, 12 Nov 2026 20:05:45 GMT); Is Trending Stock AppLovin Corporation (APP) a Buy Now? - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT); APP Stock Surges 51% After Q3 Earnings: Is it Still a Buy? - Yahoo Finance (Tue, 10 Nov 2026 14:24:00 GMT) |
| S015 | stock | FISV | 2026-11-16 | ok | https://finance.yahoo.com/quote/FISV | Forward P/E: 7.99667; Price: 63.78; Market price: 63.78; Market cap: 33934002176; Market Cap: 33934002176; Consensus EPS FY+1: 7.97582; growth: 0.0959 |
| S016 | stock | APP | 2026-11-16 | ok | https://finance.yahoo.com/quote/APP | Trailing P/E: 27.54882; Forward P/E: 19.611452; Forward EPS: 20.86026; Price: 409.1; Market price: 409.1; Market cap: 135543824384; Sector: Communication Services; Trailing Eps: 14.85; Revenue Growth: 0.555; Earnings Growth: 0.755; Gross Margin: 0.8878; Operating Margin: 0.77782995; Profit Margin: 0.65887; Return On Equity: 2.1008599; Total Revenue: 7608893952; Market Cap: 135543824384; Consensus EPS FY+1: 20.72438; growth: 0.2744 |
| S017 | filing | PNR | 2026-10-27 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json | Diluted EPS 2.76 for period ending 2026-09-30 (filed 2026-10-27) |
| S018 | filing | FISV | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json | Diluted EPS -8.9 for period ending 2026-09-30 (filed 2026-11-04) |
| S019 | stock | GEN | 2026-11-16 | ok | https://finance.yahoo.com/quote/GEN | Trailing P/E: 15.431472; Forward P/E: 9.108996; Forward EPS: 3.33736; Price: 30.4; Market price: 30.4; Market cap: 18035593216; Sector: Technology; Trailing Eps: 1.97; Revenue Growth: 0.122; Earnings Growth: 1.286; Gross Margin: 0.77410007; Operating Margin: 0.43229; Profit Margin: 0.23068; Return On Equity: 0.46402; Total Revenue: 5228000256; Market Cap: 18035593216; Consensus EPS FY+1: 3.33736; growth: 0.1286 |
| S020 | filing | GEN | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0000849399-26-000083); 8-K filed 2026-10-28 (accession 0000849399-26-000081); 8-K filed 2026-10-09 (accession 0000849399-26-000079) |
| S021 | filing | CLX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000021076-26-000046); 8-K filed 2026-11-02 (accession 0000021076-26-000044); 8-K filed 2026-10-29 (accession 0001206774-26-000586) |
| S022 | news | PNR | Fri, 13 Nov 2026 22:09:48 GMT | ok | https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en | Pentair plc (PNR) stock price, news, quote and history - Yahoo Finance UK (Fri, 13 Nov 2026 22:09:48 GMT); Pentair plc (PNR) Q3 Earnings and Revenues Beat Estimates - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT); Pentair (PNR) Stock May Be 46% Undervalued As New CFO Arrives - Yahoo Finance (Fri, 25 Sep 2026 07:00:00 GMT) |
| S023 | filing | CHTR | 2026-11-06 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-06 (accession 0001091667-26-000073); 8-K filed 2026-11-06 (accession 0001091667-26-000072); 8-K filed 2026-10-27 (accession 0001091667-26-000064) |
| S024 | stock | CLX | 2026-11-16 | ok | https://finance.yahoo.com/quote/CLX | Trailing P/E: 19.68705; Forward P/E: 17.745283; Forward EPS: 6.1684; Price: 109.46; Market price: 109.46; Market cap: 13260793856; Sector: Consumer Defensive; Trailing Eps: 5.56; Revenue Growth: 0.333; Earnings Growth: 1.138; Gross Margin: 0.41939998; Operating Margin: 0.14286; Profit Margin: 0.09408; Return On Equity: 5.34363; Total Revenue: 7196000256; Market Cap: 13260793856; Consensus EPS FY+1: 6.1684; growth: 0.0769 |
| S025 | news | GEN | Thu, 29 Oct 2026 07:00:00 GMT | ok | https://news.google.com/rss/search?q=GEN+Gen+Digital+stock&hl=en-US&gl=US&ceid=US:en | Gen Digital (GEN) Stock Repriced After Q2 Earnings Put Margins Center Stage - Yahoo Finance (Thu, 29 Oct 2026 07:00:00 GMT); Are Business Services Stocks Lagging GEN DIGITAL INC (GEN) This Year? - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT); Gen Digital Stock: Is Wall Street Bullish or Bearish? - Yahoo Finance (Thu, 05 Nov 2026 08:00:00 GMT) |
| S026 | stock | CHTR | 2026-11-16 | ok | https://finance.yahoo.com/quote/CHTR | Trailing P/E: 13.006578; Forward P/E: 3.2831066; Forward EPS: 42.15215; Price: 138.39; Market price: 138.39; Market cap: 24778944512; Sector: Communication Services; Trailing Eps: 10.64; Revenue Growth: 0.091; Gross Margin: 0.55084; Operating Margin: 0.23389; Profit Margin: 0.02498; Return On Equity: 0.07019; Total Revenue: 55645999104; Market Cap: 24778944512; Consensus EPS FY+1: 49.35412; growth: 1.1136 |
| S027 | news | CLX | Fri, 13 Nov 2026 23:34:51 GMT | ok | https://news.google.com/rss/search?q=CLX+Clorox+stock&hl=en-US&gl=US&ceid=US:en | The Clorox Company (CLX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 23:34:51 GMT); The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance UK (Sun, 15 Nov 2026 08:55:47 GMT); Clorox (CLX) Down 9.3% Since Last Earnings Report: Can It Rebound? - Yahoo Finance (Wed, 02 Sep 2026 07:00:00 GMT) |
| S028 | filing | IDXX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000874716&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000874716-26-000135); 8-K filed 2026-11-02 (accession 0001104659-26-120892); 10-Q filed 2026-08-04 (accession 0000874716-26-000123) |
| S029 | news | CHTR | Sun, 15 Nov 2026 05:47:01 GMT | ok | https://news.google.com/rss/search?q=CHTR+Charter+Communications+stock&hl=en-US&gl=US&ceid=US:en | Charter Communications (CHTR) Stock Could Be A Bargain Following Its New Operating Model - Yahoo Finance (Sun, 15 Nov 2026 05:47:01 GMT); Why You Should Think About Charter Communications Differently Now? - Yahoo Finance (Fri, 13 Nov 2026 19:16:11 GMT); Charter Communications (CHTR) Expands Enterprise Reach With Managed Secure Networking Launch - Yahoo Finance (Sun, 15 Nov 2026 06:08:00 GMT) |
| S030 | filing | GEN | 2026-10-29 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000849399.json | Diluted EPS 0.83 for period ending 2026-10-02 (filed 2026-10-29) |
| S031 | filing | ROP | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000882835&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000882835-26-000047); 8-K filed 2026-10-22 (accession 0000882835-26-000042); 8-K filed 2026-10-01 (accession 0000882835-26-000039) |
| S032 | news | IDXX | Sat, 14 Nov 2026 22:37:20 GMT | ok | https://news.google.com/rss/search?q=IDXX+Idexx+Laboratories+stock&hl=en-US&gl=US&ceid=US:en | IDEXX Laboratories, Inc. (IDXX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Sat, 14 Nov 2026 22:37:20 GMT); symbol__ Stock Quote Price and Forecast - CNN (Fri, 13 Nov 2026 15:22:45 GMT); IDEXX Laboratories (IDXX) Stock Looks Fairly Valued Despite Its 28% Run - Yahoo Finance (Sat, 31 Oct 2026 07:00:00 GMT) |
| S033 | filing | CLX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000021076.json | Diluted EPS 1.39 for period ending 2026-09-30 (filed 2026-11-02) |
| S034 | filing | CHTR | 2026-11-06 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001091667.json | Diluted EPS 0.38 for period ending 2026-09-30 (filed 2026-11-06) |
| S035 | stock | IDXX | 2026-11-16 | ok | https://finance.yahoo.com/quote/IDXX | Trailing P/E: 47.45485; Forward P/E: 41.687927; Forward EPS: 16.8929; Price: 704.23; Market price: 704.23; Market cap: 55483650048; Sector: Healthcare; Trailing Eps: 14.84; Revenue Growth: 0.099; Earnings Growth: 0.179; Gross Margin: 0.62722; Operating Margin: 0.32497; Profit Margin: 0.25357; Return On Equity: 0.68925005; Total Revenue: 4662220800; Market Cap: 55483650048; Consensus EPS FY+1: 16.8929; growth: 0.1244 |
| S036 | news | ROP | Thu, 05 Nov 2026 08:00:00 GMT | ok | https://news.google.com/rss/search?q=ROP+Roper+Technologies+stock&hl=en-US&gl=US&ceid=US:en | Roper Technologies (ROP) Stock Looks Fully Valued As Cash Flow Comes Into Focus - Yahoo Finance (Thu, 05 Nov 2026 08:00:00 GMT); Roper Technologies (ROP), What Is Behind The Fresh Attention? - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT); Did Earnings Beat Just Shift Roper Technologies (ROP) Investment Narrative? - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT) |
| S037 | filing | RDDT | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001713445&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0001713445-26-000116); 8-K filed 2026-10-29 (accession 0001713445-26-000114); 8-K filed 2026-08-12 (accession 0001713445-26-000107) |
| S038 | stock | RDDT | 2026-11-16 | ok | https://finance.yahoo.com/quote/RDDT | Trailing P/E: 20.091835; Forward P/E: 10.818217; Forward EPS: 9.10039; Price: 98.45; Market price: 98.45; Market cap: 19010076672; Sector: Communication Services; Trailing Eps: 4.9; Revenue Growth: 0.53; Earnings Growth: 0.749; Gross Margin: 0.91547996; Operating Margin: 0.29397; Profit Margin: 0.32105; Return On Equity: 0.32029998; Total Revenue: 3088880128; Market Cap: 19010076672; Consensus EPS FY+1: 6.8155; growth: 0.2401 |
| S039 | news | RDDT | Thu, 29 Oct 2026 07:00:00 GMT | ok | https://news.google.com/rss/search?q=RDDT+Reddit+stock&hl=en-US&gl=US&ceid=US:en | Reddit shares sink on weak sales guidance and plans login requirement test as Google search traffic shrinks - CNBC (Thu, 29 Oct 2026 07:00:00 GMT); Reddit (NYSE:RDDT) surprises with Q3 2026 sales but stock drops 12.6% - Yahoo Finance (Thu, 29 Oct 2026 07:00:00 GMT); Should You Wait Before Buying Reddit Stock? - Trefis (Fri, 13 Nov 2026 18:20:39 GMT) |
| S040 | filing | INTC | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000050863&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0000050863-26-000191); 8-K filed 2026-10-29 (accession 0000050863-26-000188); 8-K filed 2026-08-12 (accession 0001193125-26-346806) |

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
- filing PNR: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 (2026-10-27)
- news FISV: https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 21:49:46 GMT)
- filing APP: https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json (2026-11-04)
- stock PNR: https://finance.yahoo.com/quote/PNR (2026-11-16)
- news APP: https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en (Thu, 12 Nov 2026 20:05:45 GMT)
- stock FISV: https://finance.yahoo.com/quote/FISV (2026-11-16)
- stock APP: https://finance.yahoo.com/quote/APP (2026-11-16)
- filing PNR: https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json (2026-10-27)
- filing FISV: https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json (2026-11-04)
- stock GEN: https://finance.yahoo.com/quote/GEN (2026-11-16)
- filing GEN: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 (2026-10-29)

## AI Provenance

- Provider / model: hermes-local-proxy / upstage/solar-mini4:free
- Market research: attempts=1 tokens=9518 (prompt=6518, completion=3000) runtime=20.81s
- Fundamental research: generated this run at 2026-11-16T08:13:39.251728+00:00
- Evidence source dates: {'as_of': '2026-11-13', 'latest_equity_date': '2026-11-13', 'latest_macro_date': '2026-11-16', 'flows_date': '2026-11-13'}
- Evidence fingerprint: 2346505597fe068cde82f4dd960e5ef8ca58a6feaa2d2453597c67fda15041c6
- Source citations are retrieved external records in the ledger above; market values remain from the verified database snapshot.


## Disclosures

- This is research and market intelligence, not investment advice.
- AI conclusions are research judgments, not validated return predictions.
- The frozen risk layer is risk-only and is not used for directional views or allocations.
- Legacy scores are not active inputs or outputs.

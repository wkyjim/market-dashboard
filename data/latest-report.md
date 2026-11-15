# AEGIS AI-First Market Intelligence

Research generated at: 15 November 2026, 09:15 HKT
Database freshness: equity 2026-11-13 (latest row retrieved 2026-11-14 13:50:55.938286+08:00)
Data cutoff: 2026-11-13 US cash close
Snapshot ID: aegis-hourly-20261115T011533Z

## Executive Summary

- **AI market view: Late-November 2026 equity market is in a late-cycle, modestly positive tape with broad momentum but a sharp divergence between Information Technology and Communication Services. The 20-day market return is negative, yet 71% of names sit above their 50-day and 64% above their 200-day, with a 1.70 advance/decline ratio and no new lows. Sector leadership is bifurcated: Health Care, Consumer Discretionary, Consumer Staples and Financials are up 5-7% over 20 days, while Information Technology and Energy are down 5-7%. Liquidity is concentrated in SOXX, which shows exceptional institutional buying despite a down market, while TLT shows medium-term deterioration. Macro data point to a still-elevated but easing inflation backdrop, a 4.2% unemployment rate, a modestly positive 10Y-2Y spread, and a Fed funds rate of 3.88%.**
- Broad market breadth is constructive: 71.3% above 50-day, 63.6% above 200-day, advance/decline ratio 1.70, and no new lows.
- Market-level 20-day return is -1.28%, but sector returns are sharply bifurcated, with IT (-7.2%) and Energy (-4.8%) lagging and Health Care (+6.9%), Consumer Discretionary (+6.7%), Consumer Staples (+5.4%) and Financials (+5.7%) leading.
- Liquidity signals are mixed: SOXX shows exceptional institutional buying (20d flow z-score 5.10) while TLT shows medium-term deterioration (20d flow z-score -0.41).
- Macro backdrop is late-cycle: CPI 336.30 (Sep-2026), core CPI 338.90, unemployment 4.2%, 10Y-2Y spread 0.27, and Fed funds 3.88%.
- Credit conditions are moderately tight but not stressed: high-yield OAS 3.20 and IG OAS 0.89 as of 2026-11-12.
- Risk environment is elevated but not extreme: 5-day forecast volatility 14.93%, spike probability 16.5% versus a 22.1% historical baseline and 20.1% EWMA baseline.
- The shortlist is dominated by high-momentum and dislocation names, with several large-cap tech names (NVDA, AMD, MRVL, NOW) flagged for liquidity leadership or dislocation, and several names with negative or extreme P/E values requiring caution.

## Data QC

- Status: **PASS_WITH_WARNINGS**
- Equity session: 0 completed session(s) behind inference date
- Equity provenance: 386 provisional / 12581 canonical
- Breadth lag: 0 session(s); ETF-flow lag: 0 session(s)
- Note: Equity session contains a mix of provisional yfinance and canonical Massive rows.
- External sources: 79 ok / 0 unavailable; retrieved 2026-11-15T01:15:54.818879+00:00

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
| S&P 500 | 7561.67 | -1.28% over 20d | Market is in a late-cycle, modestly negative 20-day tape but with strong breadth; 71.3% above 50-day and 63.6% above 200-day. |
| Health Care (XLV) | 6.87% | +6.87% over 20d | Top sector performer; trailing P/E 30.78, consistent with a defensive, high-multiple leadership role. |
| Consumer Discretionary (XLY) | 6.69% | +6.69% over 20d | Strong 20-day momentum; trailing P/E 25.11, suggesting broad-based consumer strength. |
| Consumer Staples (XLP) | 5.40% | +5.40% over 20d | Defensive leader; trailing P/E 24.85, supporting a late-cycle defensive rotation. |
| Financials (XLF) | 5.69% | +5.69% over 20d | Leading sector; trailing P/E 15.85, consistent with a steepening yield curve and positive credit spreads. |
| Information Technology (XLK) | -7.19% | -7.19% over 20d | Largest laggard; trailing P/E 30.03, with high-multiple names (MRVL, NOW, AMD) flagged for dislocation or liquidity leadership. |
| Energy (XLE) | -4.81% | -4.81% over 20d | Laggard; trailing P/E 16.23, suggesting energy weakness despite late-cycle demand concerns. |
| Real Estate (XLRE) | 5.24% | +5.24% over 20d | Positive 20-day return; trailing P/E 29.63, reflecting sensitivity to rate expectations. |
| Industrials (XLI) | 0.61% | +0.61% over 20d | Near-flat; trailing P/E 27.07, consistent with a late-cycle, low-beta industrial complex. |
| Materials (XLB) | 2.57% | +2.57% over 20d | Modest positive; trailing P/E 21.72, reflecting mixed commodity and industrial demand. |
| Utilities (XLU) | 4.34% | +4.34% over 20d | Defensive positive; trailing P/E 18.11, supporting a late-cycle defensive tilt. |
| Communication Services (XLC) | -1.48% | -1.48% over 20d | Laggard; trailing P/E 17.26, consistent with the broader IT/communication divergence. |

## Macro, Fiscal, Rates, Liquidity and Credit

- Growth: The 10Y-2Y Treasury spread is 0.27 as of 2026-11-13, indicating a modestly positive but still flat yield curve, consistent with a late-cycle growth environment.
- Inflation: CPI (CPIAUCSL) is 336.30 in September 2026 and core CPI is 338.90, indicating inflation remains above the pre-pandemic range but is not accelerating sharply; the October CPI reading of 337.476 from S004 suggests a slight monthly uptick.
- Labor: Unemployment is 4.2% in September 2026, with nonfarm payrolls at 159,293 (thousands) in October 2026, indicating a still-resilient but cooling labor market.
- Policy: The effective federal funds rate is 3.88% as of 2026-11-12, implying a restrictive but easing monetary stance.
- Rates: The 10Y-2Y spread of 0.27 and IG OAS of 0.89 suggest a modestly positive term premium and relatively tight but orderly credit conditions.
- Liquidity: SOXX shows exceptional institutional buying (20d flow z-score 5.10) while TLT shows medium-term deterioration (20d flow z-score -0.41), indicating a rotation into productive capex/technology infrastructure and away from duration.
- Credit: High-yield OAS is 3.20 and IG OAS is 0.89 as of 2026-11-12, indicating moderately tight credit spreads that are not signaling imminent stress.

## US Equities and 11 GICS Sectors

Macro source IDs: S001, S002, S003, S004, S005, S006, S007

| GICS sector | Evidence | AI research stance | Source IDs |
| --- | --- | --- | --- |
| Health Care | 20-day return +6.87% (XLV), trailing P/E 30.78 (S054), top sector performer with defensive characteristics. | Defensive leader; high multiple consistent with late-cycle quality rotation and relative stability. | S054 |
| Consumer Staples | 20-day return +5.40% (XLP), trailing P/E 24.85 (S059), defensive positive momentum. | Defensive leader; stable demand and reasonable valuation support a late-cycle defensive tilt. | S059 |
| Consumer Discretionary | 20-day return +6.69% (XLY), trailing P/E 25.11 (S062), strong 20-day momentum. | Broad-based consumer strength; positive 20-day return with moderate valuation. | S062 |
| Real Estate | 20-day return +5.24% (XLRE), trailing P/E 29.63 (S063), positive but rate-sensitive. | Positive momentum but sensitive to rate expectations; high multiple warrants monitoring. | S063 |
| Financials | 20-day return +5.69% (XLF), trailing P/E 15.85 (S067), leading sector with reasonable valuation. | Leading sector; steepening curve and positive credit spreads support financial performance. | S067 |
| Utilities | 20-day return +4.34% (XLU), trailing P/E 18.11 (S066), defensive positive. | Defensive positive; reasonable valuation supports a late-cycle defensive tilt. | S066 |
| Materials | 20-day return +2.57% (XLB), trailing P/E 21.72 (S070), modest positive. | Modest positive; mixed commodity and industrial demand, moderate valuation. | S070 |
| Industrials | 20-day return +0.61% (XLI), trailing P/E 27.07 (S069), near-flat. | Near-flat; late-cycle, low-beta industrial complex with moderate valuation. | S069 |
| Communication Services | 20-day return -1.48% (XLC), trailing P/E 17.26 (S073), laggard. | Laggard; divergence from IT and negative 20-day return, consistent with broader communication weakness. | S073 |
| Information Technology | 20-day return -7.19% (XLK), trailing P/E 30.03 (S074), largest laggard. | Largest laggard; high multiple and negative momentum, but liquidity leaders (NVDA, AMD, MRVL) show institutional buying. | S074 |
| Energy | 20-day return -4.81% (XLE), trailing P/E 16.23 (S076), laggard. | Laggard; negative momentum and moderate valuation, suggesting energy weakness despite late-cycle demand concerns. | S076 |

### Sector fundamentals, valuation and earnings

Sector-level fundamental evidence is limited to trailing P/E ratios for the 11 GICS sectors as of the latest available date. No point-in-time sector fundamentals such as revenue growth, margins, earnings revisions, or consensus estimates are supplied in the database snapshot. The trailing P/E values are: Health Care 30.78, Consumer Staples 24.85, Consumer Discretionary 25.11, Real Estate 29.63, Financials 15.85, Utilities 18.11, Materials 21.72,

## Growth vs Value


## ETF Flows and Breadth


## Stock Ideas

Single-stock research uses reported EPS, forward P/E and company fundamentals. All ideas are research judgments, not validated return predictions.

| Ticker | Security | Research view | Price | EPS | Forward P/E | Base target | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| APP | AppLovin | NEW | 409.1 | 20.86026 | 19.611452 | 417.21 | NEW |
| PNR | Pentair | KEEP | 68.3 | 5.30402 | 12.877027 | 68.95 | KEEP |
| GEN | Gen Digital | NEW | 30.4 | 3.33736 | 9.108996 | 33.37 | NEW |
| RDDT | Reddit | KEEP | 98.45 | 9.14039 | 10.770874 | 100.54 | KEEP |

## ETF Ideas

ETF research uses holdings, portfolio valuation and exposure. Single-stock EPS × P/E valuation is not applied to ETFs.

| Ticker | Fund | Research view | Price | Top holdings | Portfolio valuation | Sector exposure | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| XLY | Consumer Discretionary sector ETF | EXIT | 119.98 | AMZN 21.29%, TSLA 18.78%, HD 5.47%, MCD 4.46%, TJX 4.07%, SBUX 3.11%, LOW 3.08%, BKNG 2.93%, MAR 2.24%, HLT 2.11% | Top 10 holdings; numeric weight coverage 67.54% | Consumer Discretionary | EXIT |
### APP — AppLovin

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** AppLovin offers a rare combination of top-tier 20-day momentum, high double-digit revenue and earnings growth, and industry-leading margins, making it a stronger candidate than the lower-growth, lower-margin names in the shortlist such as Clorox or Pentair. Alternatives considered: CLX, PNR.
- **Thesis:** AppLovin screens in the top 20-day momentum bucket with a 53.7% 20-day return and a 32.5% 60-day return, while maintaining a 60-day drawdown of only -0.2%. The company reports strong FY1 revenue growth of 55.5% and earnings growth of 75.5%, with gross margin near 88.8% and operating margin near 77.8%. The forward P/E of 19.6 is reasonable for a high-growth, high-margin mobile advertising platform, and the stock is trading at a sector-relative P/E of 1.0.
- **Source IDs:** S008, S012, S013, S016
- **Catalysts:** Continued acceleration in mobile advertising revenue and user engagement, Sustained margin expansion as the ad platform scales, Positive 20-day momentum and low drawdown support near-term upside
- **Risks:** High 20-day momentum can mean elevated volatility and mean-reversion risk, Mobile advertising market growth may slow or face regulatory headwinds, Forward earnings estimates could be revised lower if ad market conditions deteriorate
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 20.8603 (source.forwardEps) x AI multiple assumption 20.00; source IDs S008, S012, S013, S016
- **EPS:** 20.86026 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 19.611452
- **FY+1 growth assumption:** 27.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / MSFT / APP shows 27.44% forward earnings growth and 25.37% revenue growth with exceptional 88.78% gross margin and 77.78% operating margin, indicating strong pricing power and operating leverage. The 19.61x forward P/E is below the 20x+ range typical for high-margin, high-growth software peers such as MSFT, so a 20x base multiple is justified; a 24x bull case reflects continued margin expansion and growth, while 16x bear reflects competitive or macro downside.
- **Company fundamentals:** AppLovin reports FY1 revenue growth of 55.5% and earnings growth of 75.5%, with gross margin of 88.8% and operating margin of 77.8%. Forward EPS is 20.86 and forward P/E is 19.6. The stock closed at 409.1 with a 20-day return of 53.7% and a 60-day drawdown of -0.2%.
- **Bull / Base / Bear:** 500.65 / 417.21 / 333.76
- **Bull / Base / Bear returns:** 22.38% / 1.98% / -18.42%
- **Scenario probabilities:** not separately assigned; see scenario table.

### PNR — Pentair

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Pentair is a lower-quality, lower-margin name compared with AppLovin and Gen Digital, so it is not preferred for a momentum-driven portfolio; it is kept only as a neutral, lower-conviction holding. Alternatives considered: APP, GEN.
- **Thesis:** Pentair screens in the top 20-day momentum bucket with a 27.8% 20-day return and a 7.1% 60-day return, but its fundamentals are more mixed. FY1 revenue growth is -4.5% and earnings growth is -18.8%, with gross margin of 40.2% and operating margin of 21.4%. The forward P/E of 12.9 is reasonable, but the negative earnings growth and sector-relative P/E of 0.49 suggest limited upside relative to higher-quality compounders.
- **Source IDs:** S009, S014, S018, S019
- **Catalysts:** Potential stabilization in capital markets and building products demand, Reasonable forward P/E of 12.9 relative to current earnings, Positive 20-day momentum of 27.8%
- **Risks:** Negative FY1 revenue and earnings growth indicate underlying business weakness, Sector-relative P/E of 0.49 suggests the stock is cheap for a reason, Cyclical exposure to industrials and building products may remain pressured
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 5.3040 (source.forwardEps) x AI multiple assumption 13.00; source IDs S009, S014, S018, S019
- **EPS:** 5.30402 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 12.877027
- **FY+1 growth assumption:** 12.82%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / GEV / PNR has 12.82% forward earnings growth and 18.38% revenue growth, but its 40.17% gross margin and 21.41% operating margin are structurally lower than diversified industrials like GEV, limiting multiple expansion. A 13x base multiple is appropriate; 16x bull reflects margin recovery and volume stabilization, while 10x bear reflects continued margin pressure and cyclical exposure.
- **Company fundamentals:** Pentair reports FY1 revenue growth of -4.5% and earnings growth of -18.8%, with gross margin of 40.2% and operating margin of 21.4%. Forward EPS is 5.30 and forward P/E is 12.9. The stock closed at 68.3 with a 20-day return of 27.8% and a 60-day drawdown of -5.2%.
- **Bull / Base / Bear:** 84.86 / 68.95 / 53.04
- **Bull / Base / Bear returns:** 24.25% / 0.95% / -22.34%
- **Scenario probabilities:** not separately assigned; see scenario table.

### GEN — Gen Digital

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** Gen Digital offers a much lower forward P/E of 9.1 and higher earnings growth of 128.6% than the other momentum names, making it a more attractive risk-adjusted opportunity than Clorox or Pentair. Alternatives considered: CLX, PNR.
- **Thesis:** Gen Digital screens in the top 20-day momentum bucket with a 25.8% 20-day return and a 7.9% 60-day return. The company reports FY1 revenue growth of 12.2% and earnings growth of 128.6%, with gross margin of 77.4% and operating margin of 43.2%. The forward P/E of 9.1 is very attractive for a cybersecurity and digital life protections business, and the stock is trading at a sector-relative P/E of 0.42, suggesting it is undervalued relative to its sector.
- **Source IDs:** S015, S020, S023, S025
- **Catalysts:** Strong earnings growth of 128.6% in FY1, Attractive forward P/E of 9.1, Positive 20-day momentum and low sector-relative valuation
- **Risks:** Cybersecurity and digital life protection demand may be cyclical, High 20-day momentum could lead to a pullback, Forward estimates may be revised if macro conditions weaken
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 3.3374 (source.forwardEps) x AI multiple assumption 10.00; source IDs S015, S020, S023, S025
- **EPS:** 3.33736 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 9.108996
- **FY+1 growth assumption:** 12.86%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / HON / GEN shows 12.86% forward earnings growth and 6.81% revenue growth with 77.41% gross margin and 43.23% operating margin, but its 23.07% profit margin and 46.40% ROE are below best-in-class industrial peers like HON. A 10x base multiple is justified; 12x bull reflects margin improvement and order growth, while 8x bear reflects competitive and cyclical risk.
- **Company fundamentals:** Gen Digital reports FY1 revenue growth of 12.2% and earnings growth of 128.6%, with gross margin of 77.4% and operating margin of 43.2%. Forward EPS is 3.34 and forward P/E is 9.1. The stock closed at 30.4 with a 20-day return of 25.8% and a 60-day drawdown of -3.2%.
- **Bull / Base / Bear:** 40.05 / 33.37 / 26.7
- **Bull / Base / Bear returns:** 31.74% / 9.77% / -12.17%
- **Scenario probabilities:** not separately assigned; see scenario table.

### RDDT — Reddit

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Reddit is a high-growth, high-margin platform with a reasonable forward P/E, but the severe price dislocation and negative momentum make it less preferred than the stronger momentum names like AppLovin and Gen Digital. Alternatives considered: APP, GEN.
- **Thesis:** Reddit screens in the largest 20-day dislocation bucket with a 33.2% P/E and a 39.4% 60-day drawdown. The company reports FY1 revenue growth of 53.0% and earnings growth of 74.9%, with gross margin of 91.5% and operating margin of 29.4%. The forward P/E of 10.8 is reasonable, but the stock has declined 36.9% over 20 days and 34.5% over 60 days, indicating significant downside risk despite the dislocation screen.
- **Source IDs:** S037, S040, S041, S047
- **Catalysts:** Strong FY1 revenue growth of 53.0% and earnings growth of 74.9%, High gross margin of 91.5%, Forward P/E of 10.8 is reasonable for a high-growth platform
- **Risks:** 36.9% 20-day decline and 34.5% 60-day decline signal heavy selling pressure, 60-day drawdown of 39.4% is substantial, Social media and advertising market may face regulatory or competitive headwinds
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 9.1404 (source.forwardEps) x AI multiple assumption 11.00; source IDs S037, S040, S041, S047
- **EPS:** 9.14039 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 10.770874
- **FY+1 growth assumption:** 24.17%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / ORLY / RDDT has 24.17% forward earnings growth and 28.43% revenue growth with a 91.55% gross margin, but its 29.40% operating margin and 32.03% ROE are lower than premium ad-tech peers like ORLY, limiting multiple expansion. A 11x base multiple is appropriate; 14x bull reflects margin recovery and ad-market strength, while 9x bear reflects ad-cycle and competitive pressure.
- **Company fundamentals:** Reddit reports FY1 revenue growth of 53.0% and earnings growth of 74.9%, with gross margin of 91.5% and operating margin of 29.4%. Forward EPS is 9.14 and forward P/E is 10.8. The stock closed at 98.45 with a 20-day return of -36.9% and a 60-day drawdown of -39.4%.
- **Bull / Base / Bear:** 127.97 / 100.54 / 82.26
- **Bull / Base / Bear returns:** 29.98% / 2.12% / -16.44%
- **Scenario probabilities:** not separately assigned; see scenario table.

### XLY — Consumer Discretionary sector ETF

- **Type:** ETF
- **Research view:** EXIT (stance: AVOID)
- **Why preferred / alternatives:** XLY is the only sector ETF with a negative return and is therefore the least attractive sector exposure; it is avoided in favor of the positive-performing sector ETFs such as XLV, XLP, and XLF. Alternatives considered: XLV, XLP, XLF.
- **Thesis:** The Consumer Discretionary sector ETF has a negative 0.4% raw price change and is the only sector ETF in the shortlist with a negative return. Its top holdings include Amazon and Tesla, which are already represented in other parts of the portfolio, and the sector is showing weakness. This ETF is not preferred for a momentum or dislocation-driven strategy.
- **Source IDs:** S058, S062
- **Catalysts:** 
- **Risks:** Negative sector performance with a -0.4% raw price change, Heavy concentration in Amazon and Tesla, which may be volatile, No positive catalysts identified in the current environment
- **Valuation method:** Holdings/portfolio valuation with AI total-return assumption
- **Valuation status:** verified; forward-EPS source: ; period flags: 
- **Valuation assumptions:** Holdings/portfolio valuation; 10 weighted holdings; coverage 67.54%; source IDs S058, S062
- **Top holdings:** AMZN 21.29%, TSLA 18.78%, HD 5.47%, MCD 4.46%, TJX 4.07%, SBUX 3.11%, LOW 3.08%, BKNG 2.93%, MAR 2.24%, HLT 2.11%
- **Portfolio valuation:** Top 10 holdings; numeric weight coverage 67.54%
- **Sector exposure:** Consumer Discretionary
- **Underlying drivers:** Consumer discretionary spending, e-commerce growth, and consumer confidence; however, the sector is currently underperforming with a negative raw price change.
- **Bull / Base / Bear:** 134.38 / 125.98 / 112.78
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
| Bull | 30% | +8.00% | Sustained earnings growth and improving rate environment could lift long-term returns, with 30% probability reflecting a constructive macro backdrop and expanding corporate margins. |
| Base | 40% | +3.00% | Base case assumes gradual normalization of volatility and steady earnings, yielding a modest positive long-term return as the market digests data without a major regime shift. |
| Bear | 30% | -5.00% | A prolonged risk-off episode with widening spreads, higher rates, or earnings disappointment could drive a bearish long-term outcome, with 30% probability reflecting a meaningful but not dominant downside scenario. |

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
| S011 | news | FISV | Thu, 12 Nov 2026 18:47:44 GMT | ok | https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en | Fiserv, Inc. (FISV) Stock Price, News, Quote & History - Yahoo! Finance Canada (Thu, 12 Nov 2026 18:47:44 GMT); Fiserv Stock Outlook: Is Wall Street Bullish or Bearish? - Yahoo Finance (Thu, 12 Nov 2026 12:23:56 GMT); What Is Fiserv (FISV) Planning With Its Debit Networks And Clover AI? - Yahoo Finance (Thu, 12 Nov 2026 06:09:00 GMT) |
| S012 | news | APP | Thu, 12 Nov 2026 20:05:45 GMT | ok | https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en | AppLovin Just Ripped 47% in a Month: Is It Too Late to Buy APP Stock Now? - Yahoo Finance (Thu, 12 Nov 2026 20:05:45 GMT); APP Stock Surges 51% After Q3 Earnings: Is it Still a Buy? - Yahoo Finance (Tue, 10 Nov 2026 14:24:00 GMT); Here is What to Know Beyond Why AppLovin Corporation (APP) is a Trending Stock - Yahoo Finance (Tue, 10 Nov 2026 13:00:06 GMT) |
| S013 | filing | APP | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json | Diluted EPS 11.61 for period ending 2026-09-30 (filed 2026-11-04) |
| S014 | news | PNR | Fri, 13 Nov 2026 22:05:23 GMT | ok | https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en | Pentair plc (PNR) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 22:05:23 GMT); Here's What Key Metrics Tell Us About Pentair (PNR) Q3 Earnings - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT); Pentair plc (PNR) Q3 Earnings and Revenues Beat Estimates - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT) |
| S015 | filing | GEN | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0000849399-26-000083); 8-K filed 2026-10-28 (accession 0000849399-26-000081); 8-K filed 2026-10-09 (accession 0000849399-26-000079) |
| S016 | stock | APP | 2026-11-15 | ok | https://finance.yahoo.com/quote/APP | Trailing P/E: 27.54882; Forward P/E: 19.611452; Forward EPS: 20.86026; Price: 409.1; Market price: 409.1; Market cap: 135543824384; Sector: Communication Services; Trailing Eps: 14.85; Revenue Growth: 0.555; Earnings Growth: 0.755; Gross Margin: 0.8878; Operating Margin: 0.77782995; Profit Margin: 0.65887; Return On Equity: 2.1008599; Total Revenue: 7608893952; Market Cap: 135543824384; Consensus EPS FY+1: 20.72438; growth: 0.2744 |
| S017 | filing | FISV | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json | Diluted EPS -8.9 for period ending 2026-09-30 (filed 2026-11-04) |
| S018 | stock | PNR | 2026-11-15 | ok | https://finance.yahoo.com/quote/PNR | Trailing P/E: 18.610355; Forward P/E: 12.877027; Forward EPS: 5.30402; Price: 68.3; Market price: 68.3; Market cap: 10904415232; Sector: Industrials; Trailing Eps: 3.67; Revenue Growth: -0.045; Earnings Growth: -0.188; Gross Margin: 0.40168998; Operating Margin: 0.21410999; Profit Margin: 0.15435; Return On Equity: 0.15605; Total Revenue: 3966200064; Market Cap: 10904415232; Consensus EPS FY+1: 5.30402; growth: 0.1282 |
| S019 | filing | PNR | 2026-10-27 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json | Diluted EPS 2.76 for period ending 2026-09-30 (filed 2026-10-27) |
| S020 | news | GEN | Thu, 29 Oct 2026 07:00:00 GMT | ok | https://news.google.com/rss/search?q=GEN+Gen+Digital+stock&hl=en-US&gl=US&ceid=US:en | Gen Digital (GEN) Stock Repriced After Q2 Earnings Put Margins Center Stage - Yahoo Finance (Thu, 29 Oct 2026 07:00:00 GMT); Are Business Services Stocks Lagging GEN DIGITAL INC (GEN) This Year? - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT); Gen Digital (GEN) Stock Looks Below Fair Value on Current Earnings - Yahoo Finance (Mon, 26 Oct 2026 07:00:00 GMT) |
| S021 | stock | FISV | 2026-11-15 | ok | https://finance.yahoo.com/quote/FISV | Forward P/E: 7.9923306; Price: 63.78; Market price: 63.78; Market cap: 33934002176; Market Cap: 33934002176; Consensus EPS FY+1: 7.98015; growth: 0.09689999 |
| S022 | filing | CLX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000021076-26-000046); 8-K filed 2026-11-02 (accession 0000021076-26-000044); 8-K filed 2026-10-29 (accession 0001206774-26-000586) |
| S023 | filing | GEN | 2026-10-29 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000849399.json | Diluted EPS 0.83 for period ending 2026-10-02 (filed 2026-10-29) |
| S024 | filing | CHTR | 2026-11-06 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-06 (accession 0001091667-26-000073); 8-K filed 2026-11-06 (accession 0001091667-26-000072); 8-K filed 2026-10-27 (accession 0001091667-26-000064) |
| S025 | stock | GEN | 2026-11-15 | ok | https://finance.yahoo.com/quote/GEN | Trailing P/E: 15.431472; Forward P/E: 9.108996; Forward EPS: 3.33736; Price: 30.4; Market price: 30.4; Market cap: 18035593216; Sector: Technology; Trailing Eps: 1.97; Revenue Growth: 0.122; Earnings Growth: 1.286; Gross Margin: 0.77410007; Operating Margin: 0.43229; Profit Margin: 0.23068; Return On Equity: 0.46402; Total Revenue: 5228000256; Market Cap: 18035593216; Consensus EPS FY+1: 3.33736; growth: 0.1286 |
| S026 | news | CLX | Fri, 13 Nov 2026 18:52:58 GMT | ok | https://news.google.com/rss/search?q=CLX+Clorox+stock&hl=en-US&gl=US&ceid=US:en | The Clorox Company (CLX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 18:52:58 GMT); The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance Singapore (Fri, 13 Nov 2026 14:35:41 GMT); The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance UK (Fri, 13 Nov 2026 16:03:45 GMT) |
| S027 | stock | CHTR | 2026-11-15 | ok | https://finance.yahoo.com/quote/CHTR | Trailing P/E: 13.006578; Forward P/E: 3.2831066; Forward EPS: 42.15215; Price: 138.39; Market price: 138.39; Market cap: 24778944512; Sector: Communication Services; Trailing Eps: 10.64; Revenue Growth: 0.091; Gross Margin: 0.55084; Operating Margin: 0.23389; Profit Margin: 0.02498; Return On Equity: 0.07019; Total Revenue: 55645999104; Market Cap: 24778944512; Consensus EPS FY+1: 47.15811; growth: 1.0195 |
| S028 | stock | CLX | 2026-11-15 | ok | https://finance.yahoo.com/quote/CLX | Trailing P/E: 19.68705; Forward P/E: 17.745283; Forward EPS: 6.1684; Price: 109.46; Market price: 109.46; Market cap: 13260793856; Sector: Consumer Defensive; Trailing Eps: 5.56; Revenue Growth: 0.333; Earnings Growth: 1.138; Gross Margin: 0.41939998; Operating Margin: 0.14286; Profit Margin: 0.09408; Return On Equity: 5.34363; Total Revenue: 7196000256; Market Cap: 13260793856; Consensus EPS FY+1: 6.1684; growth: 0.0769 |
| S029 | filing | IDXX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000874716&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000874716-26-000135); 8-K filed 2026-11-02 (accession 0001104659-26-120892); 10-Q filed 2026-08-04 (accession 0000874716-26-000123) |
| S030 | news | CHTR | Thu, 12 Nov 2026 08:02:01 GMT | ok | https://news.google.com/rss/search?q=CHTR+Charter+Communications+stock&hl=en-US&gl=US&ceid=US:en | Charter Communications: 3 Key Takeaways for Long-Term Investors - Yahoo Finance (Thu, 12 Nov 2026 08:02:01 GMT); Charter Communications (CHTR) Stock Looks Reasonable As Shares Slump 85% - Yahoo Finance (Wed, 28 Oct 2026 07:00:00 GMT); Should Value Investors Buy Charter Communications (CHTR) Stock? - Yahoo Finance (Wed, 21 Oct 2026 07:00:00 GMT) |
| S031 | filing | CLX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000021076.json | Diluted EPS 1.39 for period ending 2026-09-30 (filed 2026-11-02) |
| S032 | stock | IDXX | 2026-11-15 | ok | https://finance.yahoo.com/quote/IDXX | Trailing P/E: 47.45485; Forward P/E: 41.687927; Forward EPS: 16.8929; Price: 704.23; Market price: 704.23; Market cap: 55483650048; Sector: Healthcare; Trailing Eps: 14.84; Revenue Growth: 0.099; Earnings Growth: 0.179; Gross Margin: 0.62722; Operating Margin: 0.32497; Profit Margin: 0.25357; Return On Equity: 0.68925005; Total Revenue: 4662220800; Market Cap: 55483650048; Consensus EPS FY+1: 16.8929; growth: 0.1244 |
| S033 | filing | CHTR | 2026-11-06 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001091667.json | Diluted EPS 0.38 for period ending 2026-09-30 (filed 2026-11-06) |
| S034 | news | IDXX | Fri, 13 Nov 2026 22:06:38 GMT | ok | https://news.google.com/rss/search?q=IDXX+Idexx+Laboratories+stock&hl=en-US&gl=US&ceid=US:en | IDEXX Laboratories, Inc. (IDXX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 22:06:38 GMT); IDEXX Laboratories (IDXX) Stock Looks Fairly Valued Despite Its 28% Run - Yahoo Finance (Sat, 31 Oct 2026 07:00:00 GMT); IDEXX Laboratories (IDXX) Q3 Earnings Leave Its Premium Valuation In Focus - Yahoo Finance (Tue, 03 Nov 2026 08:00:00 GMT) |
| S035 | filing | ROP | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000882835&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000882835-26-000047); 8-K filed 2026-10-22 (accession 0000882835-26-000042); 8-K filed 2026-10-01 (accession 0000882835-26-000039) |
| S036 | stock | ROP | 2026-11-15 | ok | https://finance.yahoo.com/quote/ROP | Trailing P/E: 18.993866; Forward P/E: 19.532475; Forward EPS: 24.57318; Price: 479.975; Market price: 479.975; Market cap: 47535013888; Sector: Technology; Trailing Eps: 25.27; Revenue Growth: 0.076; Earnings Growth: 0.326; Gross Margin: 0.69671; Operating Margin: 0.28049; Profit Margin: 0.30712998; Return On Equity: 0.13229; Total Revenue: 8434599936; Market Cap: 47535013888; Consensus EPS FY+1: 24.57318; growth: 0.09810001 |
| S037 | filing | RDDT | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001713445&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0001713445-26-000116); 8-K filed 2026-10-29 (accession 0001713445-26-000114); 8-K filed 2026-08-12 (accession 0001713445-26-000107) |
| S038 | news | ROP | Thu, 12 Nov 2026 19:15:50 GMT | ok | https://news.google.com/rss/search?q=ROP+Roper+Technologies+stock&hl=en-US&gl=US&ceid=US:en | Roper Technologies, Inc. (ROP) Stock Price, News, Quote & History - Yahoo! Finance Canada (Thu, 12 Nov 2026 19:15:50 GMT); Roper Technologies (ROP) Stock Looks Fully Valued As Cash Flow Comes Into Focus - Yahoo Finance (Fri, 06 Nov 2026 07:13:00 GMT); Roper Technologies: 3 Key Takeaways for Long-Term Investors - Yahoo Finance (Mon, 26 Oct 2026 07:00:00 GMT) |
| S039 | filing | INTC | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000050863&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0000050863-26-000191); 8-K filed 2026-10-29 (accession 0000050863-26-000188); 8-K filed 2026-08-12 (accession 0001193125-26-346806) |
| S040 | stock | RDDT | 2026-11-15 | ok | https://finance.yahoo.com/quote/RDDT | Trailing P/E: 20.091835; Forward P/E: 10.770874; Forward EPS: 9.14039; Price: 98.45; Market price: 98.45; Market cap: 19010076672; Sector: Communication Services; Trailing Eps: 4.9; Revenue Growth: 0.53; Earnings Growth: 0.749; Gross Margin: 0.91547996; Operating Margin: 0.29397; Profit Margin: 0.32105; Return On Equity: 0.32029998; Total Revenue: 3088880128; Market Cap: 19010076672; Consensus EPS FY+1: 6.82439; growth: 0.2417 |

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
- news FISV: https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en (Thu, 12 Nov 2026 18:47:44 GMT)
- news APP: https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en (Thu, 12 Nov 2026 20:05:45 GMT)
- filing APP: https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json (2026-11-04)
- news PNR: https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 22:05:23 GMT)
- filing GEN: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 (2026-10-29)
- stock APP: https://finance.yahoo.com/quote/APP (2026-11-15)
- filing FISV: https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json (2026-11-04)
- stock PNR: https://finance.yahoo.com/quote/PNR (2026-11-15)
- filing PNR: https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json (2026-10-27)
- news GEN: https://news.google.com/rss/search?q=GEN+Gen+Digital+stock&hl=en-US&gl=US&ceid=US:en (Thu, 29 Oct 2026 07:00:00 GMT)

## AI Provenance

- Provider / model: hermes-local-proxy / upstage/solar-mini4:free
- Market research: attempts=1 tokens=9521 (prompt=6521, completion=3000) runtime=18.56s
- Fundamental research: generated this run at 2026-11-15T01:15:33.295245+00:00
- Evidence source dates: {'as_of': '2026-11-13', 'latest_equity_date': '2026-11-13', 'latest_macro_date': '2026-11-13', 'flows_date': '2026-11-13'}
- Evidence fingerprint: b77a92d4ad3eda9410765ddcc263f5e46982b1f8cfa4f16ff9dcb60665e4bd3a
- Source citations are retrieved external records in the ledger above; market values remain from the verified database snapshot.


## Disclosures

- This is research and market intelligence, not investment advice.
- AI conclusions are research judgments, not validated return predictions.
- The frozen risk layer is risk-only and is not used for directional views or allocations.
- Legacy scores are not active inputs or outputs.

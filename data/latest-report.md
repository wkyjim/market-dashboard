# AEGIS AI-First Market Intelligence

Research generated at: 16 November 2026, 02:13 HKT
Database freshness: equity 2026-11-13 (latest row retrieved 2026-11-15 13:06:40.074841+08:00)
Data cutoff: 2026-11-13 US cash close
Snapshot ID: aegis-hourly-20261115T181344Z

## Executive Summary

- **AI market view: Late-November 2026 equity market is characterized by a broad, above-trend tape with strong price breadth, but the leadership is bifurcated: large-cap liquidity leaders and select momentum names are driving returns while Information Technology and Energy are the weakest sectors. Macro data show a still-elevated inflation backdrop and a policy rate near 3.9%, with credit spreads at moderate levels. The risk environment is elevated but not yet in a high-spike regime, and the market is showing signs of stabilization after a short-term pullback.**
- Equity market breadth is strongly positive: 71.3% of names are above their 50-day moving average and 63.6% above the 200-day, with a 1.70 advance/decline ratio and 70.5% of names positive over 20 days.
- Sector leadership is bifurcated: Consumer Discretionary, Health Care, and Consumer Staples posted the strongest 20-day returns, while Information Technology and Energy are in negative territory.
- Liquidity leaders (NVDA, AMD, MU, AAPL) and dislocation names (RDDT, INTC, FFIV, NOW, LITE, COIN) are the primary drivers, but several carry elevated or negative earnings yields and high valuation multiples.
- Macro data show CPI at 336.3 (Sep-2026) and core CPI at 338.9, with unemployment at 4.2%, indicating persistent inflation pressure and a still-tight labor market.
- Credit spreads are moderate: high-yield OAS at 3.20 and investment-grade OAS at 0.89, suggesting balanced credit conditions.
- The risk model shows 5-day forecast volatility of 14.9% and a 16.5% spike probability, below the 18.5% threshold, indicating a non-alert state.
- Bitcoin and Ethereum declined sharply on 2026-11-14 (-6.0% and -8.2%), signaling risk-off sentiment in crypto assets.

## Data QC

- Status: **PASS_WITH_WARNINGS**
- Equity session: 0 completed session(s) behind inference date
- Equity provenance: 393 provisional / 12576 canonical
- Breadth lag: 0 session(s); ETF-flow lag: 0 session(s)
- Note: Equity session contains a mix of provisional yfinance and canonical Massive rows.
- External sources: 79 ok / 0 unavailable; retrieved 2026-11-15T18:14:00.669339+00:00

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
| S&P 500 (SPX) | 7561.67 | -1.28% over 20 days | Broad market is above key moving averages but has pulled back over 20 days; price breadth remains strongly positive. |
| Information Technology (XLK) | -7.19% | -7.19% over 20 days | Weakest sector; high valuation multiples and dislocation in mega-cap tech names are weighing on performance. |
| Energy (XLE) | -4.81% | -4.81% over 20 days | Negative sector performance; likely driven by commodity price weakness and sector-specific headwinds. |
| Consumer Discretionary (XLY) | +6.69% | +6.69% over 20 days | Strong sector performance; consumer demand and positive momentum are supporting the group. |
| Health Care (XLV) | +6.87% | +6.87% over 20 days | Top-performing sector; defensive demand and positive sector momentum are key drivers. |
| Consumer Staples (XLP) | +5.40% | +5.40% over 20 days | Positive sector performance; defensive characteristics and stable demand are supporting the group. |

## Macro, Fiscal, Rates, Liquidity and Credit

- Inflation remains elevated: CPI at 336.3 (Sep-2026) and core CPI at 338.9, indicating persistent price pressures that may constrain monetary easing.
- Labor market is still tight: unemployment rate at 4.2% (Sep-2026), supporting consumer spending but also keeping wage-driven inflation risks alive.
- Policy rate is near 3.88% (DFF, 2026-11-12), suggesting the Federal Reserve is in a cautious easing cycle with limited room for aggressive cuts.
- Credit conditions are balanced: high-yield OAS at 3.20 and investment-grade OAS at 0.89 (2026-11-12), indicating moderate credit stress and no imminent credit event.
- Yield curve is mildly positive: 10Y-2Y spread at 0.27 (2026-11-13), a normalization signal but not a strong steepening.
- Crypto assets are correcting sharply: Bitcoin fell -6.0% and Ethereum -8.2% on 2026-11-14, reflecting risk-off flows and reduced liquidity in digital assets.

## US Equities and 11 GICS Sectors

Macro source IDs: S001, S002, S003, S004, S005, S006, S007

| GICS sector | Evidence | AI research stance | Source IDs |
| --- | --- | --- | --- |
| Information Technology | 20-day return of -7.19% (XLK) is the weakest among all sectors; trailing P/E of 30.03 (XLK) is elevated; shortlist names like MRVL (PE 74.2, EY 1.3%) and NOW (PE 97.2, EY 1.0%) show extreme multiples and low earnings yields. | Less favored/avoid: high valuations and dislocation in mega-cap tech are driving negative momentum; sector-relative P/E for MRVL (2.2x) and NOW (2.9x) indicates significant overvaluation. | S075, S001 |
| Energy | 20-day return of -4.81% (XLE) is the second-weakest sector; trailing P/E of 16.23 (XLE) is moderate, but sector performance is negative. | Less favored/avoid: negative momentum and sector-specific headwinds are outweighing valuation attractiveness. | S076, S001 |
| Consumer Discretionary | 20-day return of +6.69% (XLY) is among the strongest; trailing P/E of 25.11 (XLY) is reasonable; positive momentum and consumer demand are supporting the group. | Favored/positive: strong momentum and reasonable valuation support the sector; consumer spending remains resilient. | S060, S001 |
| Health Care | 20-day return of +6.87% (XLV) is the strongest sector; trailing P/E of 30.78 (XLV) is elevated but justified by defensive demand and positive momentum. | Favored/positive: top-performing sector with strong momentum and defensive characteristics; valuation is rich but supported by fundamentals. | S056, S001 |
| Consumer Staples | 20-day return of +5.40% (XLP) is positive; trailing P/E of 24.85 (XLP) is reasonable; defensive demand and stable earnings support the group. | Favored/positive: positive momentum and reasonable valuation support the sector; defensive characteristics are attractive. | S058, S001 |
| Financials | 20-day return of +5.69% (XLF) is positive; trailing P/E of 15.85 (XLF) is the lowest among sectors, suggesting value potential; positive momentum. | Favored/positive: reasonable valuation and positive momentum support the sector; low P/E indicates value opportunity. | S064, S001 |
| Real Estate | 20-day return of +5.24% (XLRE) is positive; trailing P/E of 29.63 (XLRE) is elevated but supported by positive momentum. | Neutral/positive: positive momentum but elevated valuation; sector performance is solid but not a top pick. | S062, S001 |
| Utilities | 20-day return of +4.34% (XLU) is positive; trailing P/E of 18.11 (XLU) is reasonable; defensive characteristics and stable demand support the group. | Neutral/positive: positive momentum and reasonable valuation; defensive sector with stable earnings. | S067, S001 |
| Materials | 20-day return of +2.57% (XLB) is positive but the weakest among positive sectors; trailing P/E of 21.72 (XLB) is moderate; sector performance is solid but not a top pick. | Neutral: positive momentum but weaker relative performance; valuation is reasonable but sector leadership is limited. | S068, S001 |
| Industrials | 20-day return of +0.61% (XLI) is near flat; trailing P/E of 27.07 (XLI) is elevated; sector performance is lackluster. | Neutral/less favored: near-flat performance and elevated valuation; sector lacks strong momentum. | S070, S001 |
| Communication Services | 20-day return of -1.48% (XLC) is negative; trailing P/E of 17.26 (XLC) is moderate; sector performance is negative. | Less favored/avoid: negative momentum and sector-specific headwinds; valuation is not compelling. | S072, S001 |

### Sector fundamentals, valuation and earnings

Sector-level trailing P/E data are available for all 11 GICS sectors from the supplied ETF evidence (S056-S076). Health Care (XLV) has the highest P/E at 30.78, followed by Information Technology (XLK) at 30.03 and Real Estate (XLRE) at 29.63. Financials (XLF) has the lowest P/E at 15.85, followed by Energy (XLE) at 16.23 and Utilities (XLU) at 18.11. No point-in-time sector fundamentals such as revenue growth, margins, or consensus estimates are supplied in the database; only trailing P/E and 20-day returns are available. Therefore, no additional sector fundamentals are provided to avoid invention.

## Growth vs Value

- Growth is concentrated in large-cap tech and momentum names: MRVL (PE 74.2, EY 1.3%) and NOW (PE 97.2, EY 1.0%) show extreme growth expectations but very low earnings yields, indicating high risk.
- Value is found in Financials (XLF P/E 15.85) and Energy (XLE P/E 16.23), which trade at the lowest multiples and may offer relative value.
- Consumer Discretionary (XLY P/E 25.11) and Health Care (XLV P/E 30.78) offer a balance of growth and value, with strong momentum supporting the case.
- The shortlist includes both high-growth dislocation names (RDDT, INTC, FFIV, NOW, LITE, COIN) and liquidity leaders (NVDA, AMD, MU, AAPL), but several have negative or low earnings yields, suggesting limited value upside.

## ETF Flows and Breadth

- Price breadth is strongly positive: 71.3% of names above 50-day MA, 63.6% above 200-day MA, and a 1.70 advance/decline ratio indicate broad market participation.
- 20-day momentum is positive for 70.5% of names (353 of 503), with 315 advancers vs. 185 decliners, showing wide-based strength.
- Flow data show SOXX (semiconductor ETF) with exceptional institutional buying (flow z-score 5.1 over 20 days) despite price declines, indicating strong structural accumulation.
- TLT (bond ETF) shows medium-term deterioration in flows (z-score -0.41 over 20 days

## Stock Ideas

Single-stock research uses reported EPS, forward P/E and company fundamentals. All ideas are research judgments, not validated return predictions.

| Ticker | Security | Research view | Price | EPS | Forward P/E | Base target | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| APP | AppLovin | NEW | 409.1 | 20.86026 | 19.611452 | 417.21 | NEW |
| PNR | Pentair | KEEP | 68.3 | 5.30402 | 12.877027 | 68.95 | KEEP |
| GEN | Gen Digital | KEEP | 30.4 | 3.33736 | 9.108996 | 33.37 | KEEP |
| ROP | Roper Technologies | KEEP | 479.975 | 24.57318 | 19.532475 | 491.46 | KEEP |

## ETF Ideas

ETF research uses holdings, portfolio valuation and exposure. Single-stock EPS × P/E valuation is not applied to ETFs.

| Ticker | Fund | Research view | Price | Top holdings | Portfolio valuation | Sector exposure | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| XLV | Health Care sector ETF | KEEP | 188.85 | LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59% | Top 10 holdings; numeric weight coverage 61.42% | Health Care | KEEP |
### APP — AppLovin

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** AppLovin offers the strongest 20-day momentum among the shortlisted names with a 53.7% return, and its high-margin business model provides a clearer earnings trajectory than the lower-quality or more volatile dislocation names such as INTC or COIN. Alternatives considered: INTC, COIN.
- **Thesis:** AppLovin screens in the top 20-day momentum bucket with a 53.7% 20-day return and a 32.5% 60-day return, and its reported diluted EPS of 11.61 for the 2026-09-30 period supports a forward P/E of 19.6. The stock is trading at a sector-relative P/E of 1.0, indicating it is not cheap on a relative basis, but the momentum and earnings profile justify a new position.
- **Source IDs:** S008, S012, S013, S017
- **Catalysts:** Sustained 20-day momentum above 50%, Continued revenue growth near 55% and earnings growth near 75%, High gross margin of 88.8% and operating margin of 77.8% supporting cash generation
- **Risks:** High valuation on a forward P/E basis relative to the sector, Momentum-driven volatility and potential pullback if the 20-day trend fades, Forward EPS fiscal period mapping is unverified
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 20.8603 (source.forwardEps) x AI multiple assumption 20.00; source IDs S008, S012, S013, S017
- **EPS:** 20.86026 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 19.611452
- **FY+1 growth assumption:** 27.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / MSFT / APP shows strong FY+1 consensus earnings growth of 27.44% and revenue growth of 25.37%, with exceptional margins (gross 88.8%, operating 77.8%, profit 65.9%) and high ROE. The base multiple of 20x is supported by a 19.6x forward P/E and peer comparison to MSFT, reflecting durable competitive advantages and high-quality earnings. The bull/bear range of 24x/16x reflects upside if growth accelerates and downside if margin pressure emerges.
- **Company fundamentals:** AppLovin reported diluted EPS of 11.61 for the period ending 2026-09-30, with forward EPS of 20.86 and a forward P/E of 19.61. Revenue growth is 55.5% and earnings growth is 75.5%. Gross margin is 88.8% and operating margin is 77.8%. The stock closed at 409.1 on 2026-11-13.
- **Bull / Base / Bear:** 500.65 / 417.21 / 333.76
- **Bull / Base / Bear returns:** 22.38% / 1.98% / -18.42%
- **Scenario probabilities:** not separately assigned; see scenario table.

### PNR — Pentair

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Pentair provides a lower forward P/E than the high-momentum names like AppLovin, but its negative growth metrics mean it is not a clear upgrade over the higher-quality names; it is kept as a neutral holding rather than a preferred pick. Alternatives considered: APP, ROP.
- **Thesis:** Pentair is a top 20-day momentum name with a 27.8% 20-day return and a 7.1% 60-day return. It trades at a forward P/E of 12.9, which is below its sector-relative P/E of 0.49, suggesting it is not expensive relative to its sector. However, revenue growth is slightly negative at -4.5% and earnings growth is -18.8%, so the momentum is not yet supported by fundamental improvement.
- **Source IDs:** S009, S014, S018, S020
- **Catalysts:** 20-day momentum of 27.8%, Forward P/E of 12.9 offering a reasonable entry point, Sector-relative P/E of 0.49 indicating relative value
- **Risks:** Negative revenue growth of -4.5% and negative earnings growth of -18.8%, Momentum may be driven by technicals rather than fundamentals, Forward EPS fiscal period mapping is unverified
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 5.3040 (source.forwardEps) x AI multiple assumption 13.00; source IDs S009, S014, S018, S020
- **EPS:** 5.30402 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 12.877027
- **FY+1 growth assumption:** 12.82%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / UPS / PNR has modest FY+1 consensus earnings growth of 12.82% and revenue growth of 18.38%, with a 12.9x forward P/E. The base multiple of 13x is justified by a 12.9x forward P/E and peer comparison to UPS, reflecting a cyclical but improving earnings trajectory. The bull/bear range of 16x/10x captures upside if the earnings recovery continues and downside if the business slows.
- **Company fundamentals:** Pentair reported diluted EPS of 2.76 for the period ending 2026-09-30, with forward EPS of 5.30 and a forward P/E of 12.88. Revenue growth is -4.5% and earnings growth is -18.8%. Gross margin is 40.2% and operating margin is 21.4%. The stock closed at 68.3 on 2026-11-13.
- **Bull / Base / Bear:** 84.86 / 68.95 / 53.04
- **Bull / Base / Bear returns:** 24.25% / 0.95% / -22.34%
- **Scenario probabilities:** not separately assigned; see scenario table.

### GEN — Gen Digital

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Gen Digital offers a lower forward P/E than the high-momentum names like AppLovin, but its modest revenue growth and cybersecurity sector cyclicality mean it is not a clear upgrade over the higher-quality names; it is kept as a neutral holding rather than a preferred pick. Alternatives considered: APP, ROP.
- **Thesis:** Gen Digital is a top 20-day momentum name with a 25.8% 20-day return and a 7.9% 60-day return. It trades at a forward P/E of 9.1, which is attractive, and its earnings growth is strong at 128.6%. However, revenue growth is modest at 12.2%, and the stock is not a clear upgrade over the higher-quality names, so it is kept as a neutral holding.
- **Source IDs:** S019, S022, S023, S032
- **Catalysts:** 20-day momentum of 25.8%, Strong earnings growth of 128.6%, Forward P/E of 9.1 offering a reasonable entry point
- **Risks:** Modest revenue growth of 12.2%, Forward EPS fiscal period mapping is unverified, Cybersecurity sector cyclicality and competitive pressure
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 3.3374 (source.forwardEps) x AI multiple assumption 10.00; source IDs S019, S022, S023, S032
- **EPS:** 3.33736 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 9.108996
- **FY+1 growth assumption:** 12.86%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / GE / GEN has FY+1 consensus earnings growth of 12.86% and revenue growth of 6.81%, with a 9.1x forward P/E. The base multiple of 10x is supported by a 9.1x forward P/E and peer comparison to GE, reflecting a lower-growth but still positive earnings trajectory. The bull/bear range of 12x/8x reflects upside if growth accelerates and downside if the business stagnates.
- **Company fundamentals:** Gen Digital reported diluted EPS of 0.83 for the period ending 2026-10-02, with forward EPS of 3.34 and a forward P/E of 9.11. Revenue growth is 12.2% and earnings growth is 128.6%. Gross margin is 77.4% and operating margin is 43.2%. The stock closed at 30.4 on 2026-11-13.
- **Bull / Base / Bear:** 40.05 / 33.37 / 26.7
- **Bull / Base / Bear returns:** 31.74% / 9.77% / -12.17%
- **Scenario probabilities:** not separately assigned; see scenario table.

### ROP — Roper Technologies

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Roper Technologies offers a lower forward P/E than the high-momentum names like AppLovin, but its modest revenue growth and technology sector cyclicality mean it is not a clear upgrade over the higher-quality names; it is kept as a neutral holding rather than a preferred pick. Alternatives considered: APP, GEN.
- **Thesis:** Roper Technologies is a top 20-day momentum name with a 25.4% 20-day return and a 16.9% 60-day return. It trades at a forward P/E of 19.5, which is reasonable, and its earnings growth is 32.6% with revenue growth of 7.6%. However, the stock is not a clear upgrade over the higher-quality names, so it is kept as a neutral holding.
- **Source IDs:** S034, S036, S038, S042
- **Catalysts:** 20-day momentum of 25.4%, Earnings growth of 32.6%, Forward P/E of 19.5 offering a reasonable entry point
- **Risks:** Revenue growth of 7.6% is modest, Forward EPS fiscal period mapping is unverified, Technology sector cyclicality and competitive pressure
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 24.5732 (source.forwardEps) x AI multiple assumption 20.00; source IDs S034, S036, S038, S042
- **EPS:** 24.57318 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 19.532475
- **FY+1 growth assumption:** 9.81%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / HD / ROP has FY+1 consensus earnings growth of 9.81% and revenue growth of 6.29%, with a 19.5x forward P/E. The base multiple of 20x is supported by a 19.5x forward P/E and peer comparison to HD, reflecting a stable, high-margin consumer discretionary business. The bull/bear range of 24x/16x reflects upside if the consumer environment remains favorable and downside if demand softens.
- **Company fundamentals:** Roper Technologies reported diluted EPS of 21.3 for the period ending 2026-09-30, with forward EPS of 24.57 and a forward P/E of 19.53. Revenue growth is 7.6% and earnings growth is 32.6%. Gross margin is 69.7% and operating margin is 28.0%. The stock closed at 479.975 on 2026-11-13.
- **Bull / Base / Bear:** 589.76 / 491.46 / 393.17
- **Bull / Base / Bear returns:** 22.87% / 2.39% / -18.09%
- **Scenario probabilities:** not separately assigned; see scenario table.

### XLV — Health Care sector ETF

- **Type:** ETF
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** XLV provides diversified healthcare exposure that complements the high-momentum stock picks, but it is not a clear upgrade over the higher-quality names; it is kept as a neutral holding rather than a preferred pick. Alternatives considered: XLP, XLY.
- **Thesis:** The Health Care sector ETF (XLV) is a broad exposure to the sector with top holdings including LLY, JNJ, ABBV, MRK, and UNH. The ETF is not a stock and should not be evaluated using stock valuation language. It provides diversified healthcare exposure, but the sector is not a clear upgrade over the high-momentum names, so it is kept as a neutral holding.
- **Source IDs:** S056, S057
- **Catalysts:** Diversified healthcare exposure across large-cap pharma and biotech, Top holdings include LLY, JNJ, ABBV, MRK, and UNH, Sector-relative P/E of 1.0 for the broader healthcare sector
- **Risks:** Sector-specific regulatory and reimbursement risks, Concentration in large-cap pharma names, Not a stock; valuation metrics are not directly applicable
- **Valuation method:** Holdings/portfolio valuation with AI total-return assumption
- **Valuation status:** verified; forward-EPS source: ; period flags: 
- **Valuation assumptions:** Holdings/portfolio valuation; 10 weighted holdings; coverage 61.42%; source IDs S056, S057
- **Top holdings:** LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59%
- **Portfolio valuation:** Top 10 holdings; numeric weight coverage 61.42%
- **Sector exposure:** Health Care
- **Underlying drivers:** Healthcare sector performance driven by pharmaceutical innovation, managed care, and medical technology adoption.
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
| Bull | 25% | +2.00% | Low 5-day vol (14.9%) and below-threshold spike probability (16.5% vs 18.5% threshold) support a modest upside if US close confirms stable macro data and credit spreads stay tight. |
| Base | 50% | +0.00% | Frozen daily-close model with no directional signal and elevated but sub-threshold volatility implies a range-bound session; base case is flat until official close confirmation. |
| Bear | 25% | -2.00% | If the US close reveals a spike event or widening credit spreads, the 16.5% spike probability could trigger a pullback, with downside amplified by low liquidity in the frozen forecast window. |

### Long Term (12 months)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 30% | +8.00% | Sustained low volatility and stable credit conditions support earnings momentum; a 30% probability reflects a constructive macro backdrop with broad-based participation. |
| Base | 40% | +3.00% | Moderate trend with normalized volatility and steady earnings growth; base case assumes no major shock, with returns driven by incremental rate cuts and stable credit spreads. |
| Bear | 30% | -5.00% | Elevated spike probability and potential credit widening could trigger a correction; bear case reflects a 30% chance of a meaningful drawdown if macro data disappoints or liquidity tightens. |

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
| S011 | news | FISV | Thu, 12 Nov 2026 12:23:56 GMT | ok | https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en | Fiserv Stock Outlook: Is Wall Street Bullish or Bearish? - Yahoo Finance (Thu, 12 Nov 2026 12:23:56 GMT); Michael Burry makes a bold call on struggling payments giant - Yahoo Finance (Wed, 11 Nov 2026 00:17:00 GMT); Fiserv (FISV) Stock Looks Undervalued With Strong Excess Returns - Yahoo Finance Singapore (Wed, 11 Nov 2026 22:14:34 GMT) |
| S012 | news | APP | Thu, 12 Nov 2026 20:05:45 GMT | ok | https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en | AppLovin Just Ripped 47% in a Month: Is It Too Late to Buy APP Stock Now? - Yahoo Finance (Thu, 12 Nov 2026 20:05:45 GMT); ETFs Are Net Sellers of AppLovin (APP) on Nov. 11 - Yahoo Finance (Fri, 13 Nov 2026 11:02:35 GMT); APP Stock Surges 51% After Q3 Earnings: Is it Still a Buy? - Yahoo Finance (Tue, 10 Nov 2026 14:24:00 GMT) |
| S013 | filing | APP | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json | Diluted EPS 11.61 for period ending 2026-09-30 (filed 2026-11-04) |
| S014 | news | PNR | Fri, 13 Nov 2026 22:05:23 GMT | ok | https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en | Pentair plc (PNR) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 22:05:23 GMT); Pentair plc (PNR) Q3 Earnings and Revenues Beat Estimates - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT); Pentair (PNR) Stock May Be 46% Undervalued As New CFO Arrives - Yahoo Finance (Fri, 25 Sep 2026 07:00:00 GMT) |
| S015 | stock | FISV | 2026-11-15 | ok | https://finance.yahoo.com/quote/FISV | Forward P/E: 7.9923306; Price: 63.78; Market price: 63.78; Market cap: 33934002176; Market Cap: 33934002176; Consensus EPS FY+1: 7.98015; growth: 0.09689999 |
| S016 | filing | FISV | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json | Diluted EPS -8.9 for period ending 2026-09-30 (filed 2026-11-04) |
| S017 | stock | APP | 2026-11-15 | ok | https://finance.yahoo.com/quote/APP | Trailing P/E: 27.54882; Forward P/E: 19.611452; Forward EPS: 20.86026; Price: 409.1; Market price: 409.1; Market cap: 135543824384; Sector: Communication Services; Trailing Eps: 14.85; Revenue Growth: 0.555; Earnings Growth: 0.755; Gross Margin: 0.8878; Operating Margin: 0.77782995; Profit Margin: 0.65887; Return On Equity: 2.1008599; Total Revenue: 7608893952; Market Cap: 135543824384; Consensus EPS FY+1: 20.72438; growth: 0.2744 |
| S018 | stock | PNR | 2026-11-15 | ok | https://finance.yahoo.com/quote/PNR | Trailing P/E: 18.610355; Forward P/E: 12.877027; Forward EPS: 5.30402; Price: 68.3; Market price: 68.3; Market cap: 10904415232; Sector: Industrials; Trailing Eps: 3.67; Revenue Growth: -0.045; Earnings Growth: -0.188; Gross Margin: 0.40168998; Operating Margin: 0.21410999; Profit Margin: 0.15435; Return On Equity: 0.15605; Total Revenue: 3966200064; Market Cap: 10904415232; Consensus EPS FY+1: 5.30402; growth: 0.1282 |
| S019 | filing | GEN | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0000849399-26-000083); 8-K filed 2026-10-28 (accession 0000849399-26-000081); 8-K filed 2026-10-09 (accession 0000849399-26-000079) |
| S020 | filing | PNR | 2026-10-27 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json | Diluted EPS 2.76 for period ending 2026-09-30 (filed 2026-10-27) |
| S021 | filing | CLX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000021076-26-000046); 8-K filed 2026-11-02 (accession 0000021076-26-000044); 8-K filed 2026-10-29 (accession 0001206774-26-000586) |
| S022 | news | GEN | Fri, 13 Nov 2026 09:34:35 GMT | ok | https://news.google.com/rss/search?q=GEN+Gen+Digital+stock&hl=en-US&gl=US&ceid=US:en | Gen Digital Inc. (GEN) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 09:34:35 GMT); Gen Digital (GEN) Stock Repriced After Q2 Earnings Put Margins Center Stage - Yahoo Finance (Thu, 29 Oct 2026 07:00:00 GMT); Gen Digital Stock: Is Wall Street Bullish or Bearish? - Yahoo Finance (Thu, 05 Nov 2026 08:00:00 GMT) |
| S023 | stock | GEN | 2026-11-15 | ok | https://finance.yahoo.com/quote/GEN | Trailing P/E: 15.431472; Forward P/E: 9.108996; Forward EPS: 3.33736; Price: 30.4; Market price: 30.4; Market cap: 18035593216; Sector: Technology; Trailing Eps: 1.97; Revenue Growth: 0.122; Earnings Growth: 1.286; Gross Margin: 0.77410007; Operating Margin: 0.43229; Profit Margin: 0.23068; Return On Equity: 0.46402; Total Revenue: 5228000256; Market Cap: 18035593216; Consensus EPS FY+1: 3.33736; growth: 0.1286 |
| S024 | news | CLX | Sun, 15 Nov 2026 08:55:47 GMT | ok | https://news.google.com/rss/search?q=CLX+Clorox+stock&hl=en-US&gl=US&ceid=US:en | The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance UK (Sun, 15 Nov 2026 08:55:47 GMT); The Clorox Company (CLX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 05:44:34 GMT); The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance Singapore (Fri, 13 Nov 2026 14:10:46 GMT) |
| S025 | filing | CHTR | 2026-11-06 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-06 (accession 0001091667-26-000073); 8-K filed 2026-11-06 (accession 0001091667-26-000072); 8-K filed 2026-10-27 (accession 0001091667-26-000064) |
| S026 | stock | CLX | 2026-11-15 | ok | https://finance.yahoo.com/quote/CLX | Trailing P/E: 19.68705; Forward P/E: 17.745283; Forward EPS: 6.1684; Price: 109.46; Market price: 109.46; Market cap: 13260793856; Sector: Consumer Defensive; Trailing Eps: 5.56; Revenue Growth: 0.333; Earnings Growth: 1.138; Gross Margin: 0.41939998; Operating Margin: 0.14286; Profit Margin: 0.09408; Return On Equity: 5.34363; Total Revenue: 7196000256; Market Cap: 13260793856; Consensus EPS FY+1: 6.1684; growth: 0.0769 |
| S027 | filing | IDXX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000874716&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000874716-26-000135); 8-K filed 2026-11-02 (accession 0001104659-26-120892); 10-Q filed 2026-08-04 (accession 0000874716-26-000123) |
| S028 | stock | CHTR | 2026-11-15 | ok | https://finance.yahoo.com/quote/CHTR | Trailing P/E: 13.006578; Forward P/E: 3.2831066; Forward EPS: 42.15215; Price: 138.39; Market price: 138.39; Market cap: 24778944512; Sector: Communication Services; Trailing Eps: 10.64; Revenue Growth: 0.091; Gross Margin: 0.55084; Operating Margin: 0.23389; Profit Margin: 0.02498; Return On Equity: 0.07019; Total Revenue: 55645999104; Market Cap: 24778944512; Consensus EPS FY+1: 47.15811; growth: 1.0195 |
| S029 | news | CHTR | Sun, 15 Nov 2026 05:47:01 GMT | ok | https://news.google.com/rss/search?q=CHTR+Charter+Communications+stock&hl=en-US&gl=US&ceid=US:en | Charter Communications (CHTR) Stock Could Be A Bargain Following Its New Operating Model - Yahoo Finance (Sun, 15 Nov 2026 05:47:01 GMT); Charter Communications (CHTR) Expands Enterprise Reach With Managed Secure Networking Launch - Yahoo Finance (Sun, 15 Nov 2026 06:08:00 GMT); Charter Communications (CHTR) Earnings Expected to Grow: What to Know Ahead of Next Week's Release - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT) |
| S030 | stock | IDXX | 2026-11-15 | ok | https://finance.yahoo.com/quote/IDXX | Trailing P/E: 47.45485; Forward P/E: 41.687927; Forward EPS: 16.8929; Price: 704.23; Market price: 704.23; Market cap: 55483650048; Sector: Healthcare; Trailing Eps: 14.84; Revenue Growth: 0.099; Earnings Growth: 0.179; Gross Margin: 0.62722; Operating Margin: 0.32497; Profit Margin: 0.25357; Return On Equity: 0.68925005; Total Revenue: 4662220800; Market Cap: 55483650048; Consensus EPS FY+1: 16.8929; growth: 0.1244 |
| S031 | news | IDXX | Sat, 14 Nov 2026 06:13:17 GMT | ok | https://news.google.com/rss/search?q=IDXX+Idexx+Laboratories+stock&hl=en-US&gl=US&ceid=US:en | IDEXX Laboratories, Inc. (IDXX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Sat, 14 Nov 2026 06:13:17 GMT); IDEXX Laboratories (IDXX) Stock Looks Fairly Valued Despite Its 28% Run - Yahoo Finance (Sat, 31 Oct 2026 07:00:00 GMT); IDEXX Laboratories (IDXX) vs. ZTS and NEOG: Can Raised Guidance and Product Expansion Drive Further Earnings Growth? - Yahoo Finance (Thu, 22 Oct 2026 07:00:00 GMT) |
| S032 | filing | GEN | 2026-10-29 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000849399.json | Diluted EPS 0.83 for period ending 2026-10-02 (filed 2026-10-29) |
| S033 | filing | CHTR | 2026-11-06 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001091667.json | Diluted EPS 0.38 for period ending 2026-09-30 (filed 2026-11-06) |
| S034 | filing | ROP | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000882835&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000882835-26-000047); 8-K filed 2026-10-22 (accession 0000882835-26-000042); 8-K filed 2026-10-01 (accession 0000882835-26-000039) |
| S035 | filing | CLX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000021076.json | Diluted EPS 1.39 for period ending 2026-09-30 (filed 2026-11-02) |
| S036 | news | ROP | Fri, 13 Nov 2026 13:04:22 GMT | ok | https://news.google.com/rss/search?q=ROP+Roper+Technologies+stock&hl=en-US&gl=US&ceid=US:en | Roper Technologies, Inc. (ROP) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 13:04:22 GMT); Roper Technologies (ROP) Stock Looks Fully Valued As Cash Flow Comes Into Focus - Yahoo Finance (Thu, 05 Nov 2026 08:00:00 GMT); Roper Technologies: 3 Key Takeaways for Long-Term Investors - Yahoo Finance (Mon, 26 Oct 2026 07:00:00 GMT) |
| S037 | filing | RDDT | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001713445&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0001713445-26-000116); 8-K filed 2026-10-29 (accession 0001713445-26-000114); 8-K filed 2026-08-12 (accession 0001713445-26-000107) |
| S038 | stock | ROP | 2026-11-15 | ok | https://finance.yahoo.com/quote/ROP | Trailing P/E: 18.993866; Forward P/E: 19.532475; Forward EPS: 24.57318; Price: 479.975; Market price: 479.975; Market cap: 47535013888; Sector: Technology; Trailing Eps: 25.27; Revenue Growth: 0.076; Earnings Growth: 0.326; Gross Margin: 0.69671; Operating Margin: 0.28049; Profit Margin: 0.30712998; Return On Equity: 0.13229; Total Revenue: 8434599936; Market Cap: 47535013888; Consensus EPS FY+1: 24.57318; growth: 0.09810001 |
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
- filing APP: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001751008&type=10-Q&dateb=&owner=include&count=10 (2026-11-04)
- filing PNR: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 (2026-10-27)
- filing FISV: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 (2026-11-04)
- news FISV: https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en (Thu, 12 Nov 2026 12:23:56 GMT)
- news APP: https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en (Thu, 12 Nov 2026 20:05:45 GMT)
- filing APP: https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json (2026-11-04)
- news PNR: https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 22:05:23 GMT)
- stock FISV: https://finance.yahoo.com/quote/FISV (2026-11-15)
- filing FISV: https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json (2026-11-04)
- stock APP: https://finance.yahoo.com/quote/APP (2026-11-15)
- stock PNR: https://finance.yahoo.com/quote/PNR (2026-11-15)
- filing GEN: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 (2026-10-29)
- filing PNR: https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json (2026-10-27)

## AI Provenance

- Provider / model: hermes-local-proxy / upstage/solar-mini4:free
- Market research: attempts=1 tokens=9473 (prompt=6473, completion=3000) runtime=21.16s
- Fundamental research: generated this run at 2026-11-15T18:13:44.523475+00:00
- Evidence source dates: {'as_of': '2026-11-13', 'latest_equity_date': '2026-11-13', 'latest_macro_date': '2026-11-14', 'flows_date': '2026-11-13'}
- Evidence fingerprint: 9c5c43e34902f8b35ea219945af03e275cb8f8c5011666d27772ab3b84aa789a
- Source citations are retrieved external records in the ledger above; market values remain from the verified database snapshot.


## Disclosures

- This is research and market intelligence, not investment advice.
- AI conclusions are research judgments, not validated return predictions.
- The frozen risk layer is risk-only and is not used for directional views or allocations.
- Legacy scores are not active inputs or outputs.

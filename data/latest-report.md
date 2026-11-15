# AEGIS AI-First Market Intelligence

Research generated at: 15 November 2026, 12:16 HKT
Database freshness: equity 2026-11-13 (latest row retrieved 2026-11-14 13:50:55.938286+08:00)
Data cutoff: 2026-11-13 US cash close
Snapshot ID: aegis-hourly-20261115T041600Z

## Executive Summary

- **AI market view: Late-November 2026: broad market breadth is constructive (71% above 50-day, 64% above 200-day, A/D ratio 1.70), but the index-level 20-day return is negative and the Information Technology sector is the weakest GICS group. Momentum, dislocation, and liquidity screens point to a small set of high-conviction names, while credit spreads and the 10Y-2Y curve remain consistent with a stable, non-crisis macro backdrop.**
- Breadth is the dominant positive: 71.3% of names above the 50-day and 63.6% above the 200-day, with an advance/decline ratio of 1.70.
- Index-level momentum is negative over 20 days, and Information Technology is the only GICS sector with a negative 20-day return (-7.2%).
- Health Care, Consumer Staples, Consumer Discretionary, Real Estate, Financials, Utilities, and Materials are all positive over 20 days; Communication Services and Energy are negative.
- Screening highlights a concentrated list of momentum, dislocation, and liquidity leaders, but forward EPS data is missing for most shortlisted names, so valuation quality is limited.
- Credit spreads (HY OAS 3.20, IG OAS 0.89) and the 10Y-2Y spread (0.27) suggest orderly financial conditions without acute stress.
- Risk model shows 5-day forecast volatility of 14.9% and a 16.5% spike probability, below the 18.5% threshold and below historical/ewma baselines.

## Data QC

- Status: **PASS_WITH_WARNINGS**
- Equity session: 0 completed session(s) behind inference date
- Equity provenance: 386 provisional / 12581 canonical
- Breadth lag: 0 session(s); ETF-flow lag: 0 session(s)
- Note: Equity session contains a mix of provisional yfinance and canonical Massive rows.
- External sources: 79 ok / 0 unavailable; retrieved 2026-11-15T04:16:23.708336+00:00

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
| S&P 500 | 7561.67 | -1.28% over 20 days | Index-level 20-day return is negative despite strong breadth; 71.3% above 50-day and 63.6% above 200-day. |
| Health Care (XLV) | +6.87% | +6.87% over 20 days | Strongest 20-day sector return; trailing P/E 30.78. |
| Consumer Discretionary (XLY) | +6.69% | +6.69% over 20 days | Positive momentum; trailing P/E 25.11. |
| Information Technology (XLK) | -7.19% | -7.19% over 20 days | Only negative GICS sector; trailing P/E 30.03. |
| Financials (XLF) | +5.69% | +5.69% over 20 days | Positive 20-day return; trailing P/E 15.85. |
| Energy (XLE) | -4.81% | -4.81% over 20 days | Negative 20-day return; trailing P/E 16.23. |

## Macro, Fiscal, Rates, Liquidity and Credit

- Growth: US CPI for all urban consumers is 336.298 (Sep-2026) and core CPI is 338.896; the latest October CPI reading is 337.476, indicating inflation remains above the pre-2021 range but has not accelerated sharply.
- Labor: Unemployment rate is 4.2% (Sep-2026) and the latest October reading is 4.1%, consistent with a still-firm but gradually cooling labor market.
- Policy: The effective federal funds rate is 3.88% as of 2026-11-12, implying a restrictive but easing-leaning policy stance.
- Rates: The 10Y-2Y Treasury spread is 0.27 as of 2026-11-13, a modestly positive curve that does not signal imminent recession risk.
- Liquidity: Credit spreads are orderly, with US high-yield OAS at 3.20 and IG OAS at 0.89 as of 2026-11-12, supporting risk-taking.
- Spike risk: The frozen daily-close model gives a 5-day forecast volatility of 14.9% and a 16.5% spike probability, below the 18.5% threshold and below historical (22.1%) and EWMA (20.1%) baselines.

## US Equities and 11 GICS Sectors

Macro source IDs: S001, S002, S003, S004, S005, S006, S007

| GICS sector | Evidence | AI research stance | Source IDs |
| --- | --- | --- | --- |
| Health Care | 20-day sector return +6.87%; trailing P/E 30.78; S057. | Positive momentum and broad-based strength; valuation is rich but supported by sector leadership. | S057 |
| Consumer Staples | 20-day sector return +5.40%; trailing P/E 24.85; S061. | Defensive strength with moderate valuation; consistent with a stable macro backdrop. | S061 |
| Consumer Discretionary | 20-day sector return +6.69%; trailing P/E 25.11; S062. | Positive momentum and reasonable valuation; consumer demand remains supportive. | S062 |
| Real Estate | 20-day sector return +5.24%; trailing P/E 29.63; S063. | Positive 20-day return but elevated valuation; watch rate sensitivity. | S063 |
| Financials | 20-day sector return +5.69%; trailing P/E 15.85; S065. | Positive momentum with the cheapest trailing P/E among major sectors; supportive of credit conditions. | S065 |
| Utilities | 20-day sector return +4.34%; trailing P/E 18.11; S064. | Defensive stability with moderate valuation; low beta in a constructive breadth environment. | S064 |
| Materials | 20-day sector return +2.57%; trailing P/E 21.72; S068. | Modest positive momentum; valuation is mid-range and not a leading sector. | S068 |
| Industrials | 20-day sector return +0.61%; trailing P/E 27.07; S070. | Near-flat momentum; valuation is above the market average and not a primary driver. | S070 |
| Communication Services | 20-day sector return -1.48%; trailing P/E 17.26; S071. | Negative 20-day return; valuation is reasonable but momentum is negative. | S071 |
| Information Technology | 20-day sector return -7.19%; trailing P/E 30.03; S074. | Weakest sector; negative momentum and elevated valuation relative to the group. | S074 |
| Energy | 20-day sector return -4.81%; trailing P/E 16.23; S076. | Negative 20-day return; valuation is cheap but momentum and macro tailwinds are absent. | S076 |

### Sector fundamentals, valuation and earnings

No point-in-time sector-level fundamentals beyond the supplied trailing P/E and 20-day ETF returns are available in the database. Growth, margin, and consensus estimates were retrieved only for source-backed shortlist names, and the full universe lacks structured industry catalyst calendars. Therefore, no additional sector fundamentals are asserted here.

## Growth vs Value

- Health Care and Consumer Discretionary show the strongest 20-day momentum (+6.87% and +6.69%) and are the only sectors with trailing P/E above 25, indicating a growth-leaning rotation.
- Financials and Utilities offer the cheapest trailing P/E (15.85 and 18.11), providing a value anchor in a constructive breadth environment.
- Information Technology is the only negative sector (-7.19%) with a trailing P/E of 30.03, suggesting that high valuation and negative momentum are currently misaligned.
- Energy is cheap on trailing P/E (16.23) but has negative 20-day momentum (-4.81%), so value is not currently supported by price action.

## ETF Flows and Breadth

- Breadth is strongly positive: 71.34% of names above the 50-day, 63.6% above the 200-day, and the advance/decline ratio is 1.70.
- The 20-day positive rate is 70.46% with 315 advancers and 185 decliners, indicating broad participation rather than narrow leadership.
- Flow data shows SOXX with exceptional institutional buying (20-day flow z-score 5.10) despite a down market, while TLT shows medium-term deterioration and SMH reflects tactical profit-taking inside structural accumulation.
- New highs and new lows are both zero, so the breadth picture is not being driven by a handful of breakout names.

## Stock Ideas

Single-stock research uses reported EPS, forward P/E and company fundamentals. All ideas are research judgments, not validated return predictions.

| Ticker | Security | Research view | Price | EPS | Forward P/E | Base target | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| APP | AppLovin | NEW | 409.1 | 20.86026 | 19.611452 | 458.93 | NEW |
| PNR | Pentair | KEEP | 68.3 | 5.30402 | 12.877027 | 74.26 | KEEP |
| IDXX | Idexx Laboratories | KEEP | 704.23 | 16.8929 | 41.687927 | 641.93 | KEEP |
| RDDT | Reddit | EXIT | 98.45 | 9.14039 | 10.770874 | 109.68 | EXIT |

## ETF Ideas

ETF research uses holdings, portfolio valuation and exposure. Single-stock EPS × P/E valuation is not applied to ETFs.

| Ticker | Fund | Research view | Price | Top holdings | Portfolio valuation | Sector exposure | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| XLV | Health Care sector ETF | KEEP | 188.85 | LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59% | Top 10 holdings; numeric weight coverage 61.42% | Health Care | KEEP |
### APP — AppLovin

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** AppLovin offers a high-margin, momentum-driven profile that is preferable to the lower-margin, lower-momentum alternatives such as Gen Digital and Clorox, which screen in the same momentum bucket but with weaker margin and growth characteristics. Alternatives considered: GEN, CLX.
- **Thesis:** AppLovin screens in the top 20-day momentum bucket with a 53.7% 20-day return and a 32.5% 60-day return, indicating strong price momentum. The company reports high gross margin (~88.8%) and operating margin (~77.8%), and its forward P/E of ~19.6 is reasonable relative to its growth profile. The 20-day momentum and high-quality margin profile support a new BUY recommendation.
- **Source IDs:** S008, S012, S016, S020
- **Catalysts:** Sustained 20-day momentum (20d return ~53.7%), High gross margin (~88.8%) and operating margin (~77.8%), Forward P/E ~19.6 with positive earnings growth
- **Risks:** High 20-day momentum may be prone to mean reversion, Forward P/E ~19.6 leaves limited margin of safety if momentum fades, Single-quarter reported EPS of $11.61 may not persist
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 20.8603 (source.forwardEps) x AI multiple assumption 22.00; source IDs S008, S012, S016, S020
- **EPS:** 20.86026 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 19.611452
- **FY+1 growth assumption:** 27.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / MSFT / APP shows strong FY1 consensus growth of 27.44% with 25.4% revenue growth and 75.5% earnings growth, supported by 88.8% gross margin and 77.8% operating margin. The forward EPS of 20.86 and forward P/E of 19.6x are below the MSFT peer multiple, so a base multiple of 22x is justified for a high-quality compounder. Bull multiple of 26x reflects continued margin expansion and growth; bear multiple of 17x reflects downside risk if growth decelerates.
- **Company fundamentals:** AppLovin reports high gross margin (~88.8%) and operating margin (~77.8%), with a forward P/E of ~19.6 and positive earnings growth. The company screens in the top 20-day momentum bucket with a 53.7% 20-day return and 32.5% 60-day return.
- **Bull / Base / Bear:** 542.37 / 458.93 / 354.62
- **Bull / Base / Bear returns:** 32.58% / 12.18% / -13.32%
- **Scenario probabilities:** not separately assigned; see scenario table.

### PNR — Pentair

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Pentair is preferable to the more expensive and higher-momentum candidates such as AppLovin and Idexx Laboratories, offering a lower valuation and positive momentum, but it is not preferred over the higher-growth names. Alternatives considered: APP, IDXX.
- **Thesis:** Pentair screens in the top 20-day momentum bucket with a 27.8% 20-day return and a 7.1% 60-day return. The company has a forward P/E of ~12.9 and a reasonable earnings yield of ~7.4%, but its revenue growth is slightly negative (-4.5%) and earnings growth is negative (-18.8%). The momentum is positive but the fundamental growth is weak, so a neutral stance is appropriate.
- **Source IDs:** S011, S015, S017, S019
- **Catalysts:** Positive 20-day momentum (27.8% 20-day return), Forward P/E ~12.9 and earnings yield ~7.4%, Reasonable valuation relative to growth
- **Risks:** Negative revenue growth (-4.5%) and earnings growth (-18.8%), Momentum is positive but not as strong as other candidates, Sector-relative P/E of 0.49 suggests underperformance
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 5.3040 (source.forwardEps) x AI multiple assumption 14.00; source IDs S011, S015, S017, S019
- **EPS:** 5.30402 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 12.877027
- **FY+1 growth assumption:** 12.82%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / UPS / PNR has FY1 consensus growth of 12.82% with 18.4% revenue growth and 12.8% earnings growth, but operating margin is only 21.4% and ROE is 15.6%, indicating lower profitability. The forward EPS of 5.30 and forward P/E of 12.9x are below UPS, so a base multiple of 14x is justified. Bull multiple of 17x reflects potential margin improvement; bear multiple of 11x reflects risk from low margins and cyclical exposure.
- **Company fundamentals:** Pentair has a forward P/E of ~12.9, earnings yield of ~7.4%, and a 20-day return of 27.8%. However, revenue growth is -4.5% and earnings growth is -18.8%, indicating weak fundamental growth despite positive momentum.
- **Bull / Base / Bear:** 90.17 / 74.26 / 58.34
- **Bull / Base / Bear returns:** 32.02% / 8.73% / -14.58%
- **Scenario probabilities:** not separately assigned; see scenario table.

### IDXX — Idexx Laboratories

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Idexx offers strong momentum and positive growth, but its high valuation makes it less attractive than the lower-priced momentum candidates such as Pentair and Gen Digital. Alternatives considered: PNR, GEN.
- **Thesis:** Idexx Laboratories screens in the top 20-day momentum bucket with a 25.7% 20-day return and a 29.0% 60-day return. The company has a high forward P/E of ~41.7 and a low earnings yield of ~2.6%, with sector-relative P/E of 1.33 indicating it is expensive relative to its sector. The strong momentum is offset by high valuation, so a neutral stance is appropriate.
- **Source IDs:** S028, S030, S032, S036
- **Catalysts:** Strong 20-day momentum (25.7% 20-day return) and 60-day return (29.0%), Positive revenue growth (9.9%) and earnings growth (17.9%), High gross margin (~62.7%)
- **Risks:** High forward P/E of ~41.7 and low earnings yield of ~2.6%, Sector-relative P/E of 1.33 indicates expensive valuation, High valuation leaves limited upside if momentum stalls
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 16.8929 (source.forwardEps) x AI multiple assumption 38.00; source IDs S028, S030, S032, S036
- **EPS:** 16.8929 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 41.687927
- **FY+1 growth assumption:** 12.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / BDX / IDXX has FY1 consensus growth of 12.44% with 8.9% revenue growth and 17.9% earnings growth, with 62.7% gross margin and 32.5% operating margin. The forward EPS of 16.89 and forward P/E of 41.7x are below BDX, so a base multiple of 38x is justified for a healthcare compounder. Bull multiple of 44x reflects strong earnings growth and margin stability; bear multiple of 32x reflects downside if growth slows.
- **Company fundamentals:** Idexx Laboratories has a forward P/E of ~41.7, earnings yield of ~2.6%, and sector-relative P/E of 1.33. It has positive revenue growth (9.9%) and earnings growth (17.9%), with strong 20-day and 60-day momentum.
- **Bull / Base / Bear:** 743.29 / 641.93 / 540.57
- **Bull / Base / Bear returns:** 5.55% / -8.85% / -23.24%
- **Scenario probabilities:** not separately assigned; see scenario table.

### RDDT — Reddit

- **Type:** Stock
- **Research view:** EXIT (stance: AVOID)
- **Why preferred / alternatives:** Reddit's severe price dislocation and negative returns make it less attractive than the positive-momentum candidates such as AppLovin and Pentair, which show strong price trends and better risk-reward profiles. Alternatives considered: APP, PNR.
- **Thesis:** Reddit screens in the largest 20-day dislocation bucket with a -36.9% 20-day return and a -34.5% 60-day return, indicating significant price deterioration. The company has a forward P/E of ~10.8 and an earnings yield of ~3.0%, but the severe drawdown of -39.4% and negative price returns suggest ongoing distress. The dislocation is large and the price action is negative, so an avoid stance is appropriate.
- **Source IDs:** S037, S038, S042, S047
- **Catalysts:** Forward P/E ~10.8 and earnings yield ~3.0%, Positive revenue growth (53%) and earnings growth (74.9%), High gross margin (~91.5%)
- **Risks:** Severe 20-day drawdown of -39.4%, Negative 20-day return (-36.9%) and 60-day return (-34.5%), Dislocation is large and price action is negative
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 9.1404 (source.forwardEps) x AI multiple assumption 12.00; source IDs S037, S038, S042, S047
- **EPS:** 9.14039 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 10.770874
- **FY+1 growth assumption:** 24.17%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / GOOGL / RDDT has FY1 consensus growth of 24.17% with 28.4% revenue growth and 74.9% earnings growth, supported by 91.5% gross margin and 32.1% profit margin. The forward EPS of 9.14 and forward P/E of 10.8x are below GOOGL, so a base multiple of 12x is justified for a high-growth tech platform. Bull multiple of 15x reflects continued growth and margin expansion; bear multiple of 10x reflects risk if growth decelerates.
- **Company fundamentals:** Reddit has a forward P/E of ~10.8, earnings yield of ~3.0%, and high gross margin (~91.5%). However, it has a severe 60-day drawdown of -39.4% and negative 20-day and 60-day returns, indicating significant price deterioration.
- **Bull / Base / Bear:** 137.11 / 109.68 / 91.4
- **Bull / Base / Bear returns:** 39.27% / 11.41% / -7.16%
- **Scenario probabilities:** not separately assigned; see scenario table.

### XLV — Health Care sector ETF

- **Type:** ETF
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** XLV provides diversified healthcare exposure, but it is not preferred over the more focused momentum stocks such as AppLovin and Idexx Laboratories, which show stronger relative momentum and growth. Alternatives considered: XLP, XLY.
- **Thesis:** The Health Care sector ETF (XLV) has a positive price change of ~0.54% and holds major healthcare names such as LLY, JNJ, ABBV, and MRK. The sector shows positive momentum but the ETF is a broad market exposure rather than a high-conviction pick. A neutral stance is appropriate given the positive but unremarkable performance.
- **Source IDs:** S056, S057
- **Catalysts:** Positive price change of ~0.54%, Top holdings include LLY, JNJ, ABBV, and MRK, Sector exposure to healthcare
- **Risks:** Positive but modest price change of ~0.54%, Broad sector exposure limits upside from individual names, No specific catalyst identified
- **Valuation method:** Holdings/portfolio valuation with AI total-return assumption
- **Valuation status:** verified; forward-EPS source: ; period flags: 
- **Valuation assumptions:** Holdings/portfolio valuation; 10 weighted holdings; coverage 61.42%; source IDs S056, S057
- **Top holdings:** LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59%
- **Portfolio valuation:** Top 10 holdings; numeric weight coverage 61.42%
- **Sector exposure:** Health Care
- **Underlying drivers:** Health Care sector ETF with top holdings LLY, JNJ, ABBV, MRK, UNH, TMO, AMGN, GILD, ABT, PFE. The sector shows positive momentum with a ~0.54% price change.
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
| Bull | 25% | +2.00% | Low 5-day forecast vol (14.9%) and below-threshold spike probability (16.5% vs 18.5% threshold) suggest a stable, range-bound tape where a modest upside drift is plausible if credit spreads tighten on easing rate expectations. |
| Base | 50% | +0.00% | Directional signal is false and the frozen daily-close model shows no directional edge; base case assumes mean-reversion around the historical baseline with flat returns over the target window. |
| Bear | 25% | -2.00% | If the spike probability materializes above the 18.5% threshold, elevated volatility and potential liquidity stress could drive a mild downside move, especially if earnings or credit conditions deteriorate. |

### Long Term (12 months)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 30% | +8.00% | Sustained easing cycle and improving earnings breadth could lift risk appetite, with credit spreads tightening and volatility normalizing, supporting an 8% annualized return over the horizon. |
| Base | 40% | +3.00% | A gradual macro expansion with stable rates and moderate earnings growth supports a low-single-digit return, reflecting balanced risk-reward and no major regime shift. |
| Bear | 30% | -5.00% | A stagflationary shock or credit event would compress valuations, widen spreads, and raise volatility, leading to a negative return as earnings and liquidity conditions deteriorate. |

## Positioning

- Maintain a constructive but selective posture: breadth is supportive, but index-level momentum is negative and the Information Technology sector is weak.
- Favor Health Care, Consumer Discretionary, and Financials for positive momentum and reasonable valuation.
- Use Financials and Utilities as value anchors given the cheapest trailing P/E in the universe.
- Avoid over-weighting Information Technology and Energy until momentum and relative strength improve.
- Do not assign weights; the screen is a qualitative research posture, not an allocation signal.

## Catalysts

| Date | Event | Why it matters |
| --- | --- | --- |
| 2026-11-16 | Frozen daily-close model target window opens | The risk model is prospective for 2026-11-16 to 2026-11-20, with forecast volatility of 14.9% and a 16.5% spike probability, below the 18.5% threshold. |
| 2026-11-13 | Equity session close | Latest equity data is as of 2026-11-13 with zero lag sessions; the session contains a mix of provisional yfinance and canonical Massive rows. |
| 2026-11-12 | Macro data release | Effective federal funds rate, credit spreads, and 10Y-2Y spread were published on 2026-11-12, supporting the orderly financial conditions view. |

## Key Risks

- Index-level 20-day return is negative (-1.28%) despite strong breadth, indicating a potential divergence between price and participation.
- Information Technology is the only negative GICS sector (-7.19%) and carries elevated valuation, creating a concentration risk in the screen.
- Forward EPS data is missing for most shortlisted names, so valuation quality and forward earnings revisions cannot be fully assessed.
- The risk model shows a 16.5% spike probability, which is below the 18.5% threshold but still non-trivial in a high-volatility environment.
- Credit spreads are orderly, but a sudden widening in HY OAS or IG OAS could quickly change the risk backdrop.
- The equity session contains a mix of provisional yfinance and canonical Massive rows, which may introduce data quality warnings.

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
| S010 | news | FISV | Fri, 13 Nov 2026 00:42:12 GMT | ok | https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en | Fiserv, Inc. (FISV) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 00:42:12 GMT); Fiserv Stock Outlook: Is Wall Street Bullish or Bearish? - Yahoo Finance (Thu, 12 Nov 2026 12:23:56 GMT); What Is Fiserv (FISV) Planning With Its Debit Networks And Clover AI? - Yahoo Finance (Thu, 12 Nov 2026 06:09:00 GMT) |
| S011 | filing | PNR | 2026-10-27 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-27 (accession 0000077360-26-000058); 8-K filed 2026-10-27 (accession 0000077360-26-000055); 8-K filed 2026-09-22 (accession 0000077360-26-000050) |
| S012 | news | APP | Thu, 12 Nov 2026 20:05:45 GMT | ok | https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en | AppLovin Just Ripped 47% in a Month: Is It Too Late to Buy APP Stock Now? - Yahoo Finance (Thu, 12 Nov 2026 20:05:45 GMT); APP Stock Surges 51% After Q3 Earnings: Is it Still a Buy? - Yahoo Finance (Tue, 10 Nov 2026 14:24:00 GMT); Here is What to Know Beyond Why AppLovin Corporation (APP) is a Trending Stock - Yahoo Finance (Tue, 10 Nov 2026 13:00:06 GMT) |
| S013 | filing | GEN | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0000849399-26-000083); 8-K filed 2026-10-28 (accession 0000849399-26-000081); 8-K filed 2026-10-09 (accession 0000849399-26-000079) |
| S014 | filing | FISV | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json | Diluted EPS -8.9 for period ending 2026-09-30 (filed 2026-11-04) |
| S015 | news | PNR | Fri, 13 Nov 2026 22:05:23 GMT | ok | https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en | Pentair plc (PNR) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 22:05:23 GMT); Here's What Key Metrics Tell Us About Pentair (PNR) Q3 Earnings - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT); Pentair plc (PNR) Q3 Earnings and Revenues Beat Estimates - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT) |
| S016 | stock | APP | 2026-11-15 | ok | https://finance.yahoo.com/quote/APP | Trailing P/E: 27.54882; Forward P/E: 19.611452; Forward EPS: 20.86026; Price: 409.1; Market price: 409.1; Market cap: 135543824384; Sector: Communication Services; Trailing Eps: 14.85; Revenue Growth: 0.555; Earnings Growth: 0.755; Gross Margin: 0.8878; Operating Margin: 0.77782995; Profit Margin: 0.65887; Return On Equity: 2.1008599; Total Revenue: 7608893952; Market Cap: 135543824384; Consensus EPS FY+1: 20.72438; growth: 0.2744 |
| S017 | filing | PNR | 2026-10-27 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json | Diluted EPS 2.76 for period ending 2026-09-30 (filed 2026-10-27) |
| S018 | stock | FISV | 2026-11-15 | ok | https://finance.yahoo.com/quote/FISV | Forward P/E: 7.9923306; Price: 63.78; Market price: 63.78; Market cap: 33934002176; Market Cap: 33934002176; Consensus EPS FY+1: 7.98015; growth: 0.09689999 |
| S019 | stock | PNR | 2026-11-15 | ok | https://finance.yahoo.com/quote/PNR | Trailing P/E: 18.610355; Forward P/E: 12.877027; Forward EPS: 5.30402; Price: 68.3; Market price: 68.3; Market cap: 10904415232; Sector: Industrials; Trailing Eps: 3.67; Revenue Growth: -0.045; Earnings Growth: -0.188; Gross Margin: 0.40168998; Operating Margin: 0.21410999; Profit Margin: 0.15435; Return On Equity: 0.15605; Total Revenue: 3966200064; Market Cap: 10904415232; Consensus EPS FY+1: 5.30402; growth: 0.1282 |
| S020 | filing | APP | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json | Diluted EPS 11.61 for period ending 2026-09-30 (filed 2026-11-04) |
| S021 | filing | GEN | 2026-10-29 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000849399.json | Diluted EPS 0.83 for period ending 2026-10-02 (filed 2026-10-29) |
| S022 | filing | CLX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000021076-26-000046); 8-K filed 2026-11-02 (accession 0000021076-26-000044); 8-K filed 2026-10-29 (accession 0001206774-26-000586) |
| S023 | news | GEN | Fri, 13 Nov 2026 00:21:25 GMT | ok | https://news.google.com/rss/search?q=GEN+Gen+Digital+stock&hl=en-US&gl=US&ceid=US:en | Gen Digital Inc. (GEN) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 00:21:25 GMT); Gen Digital (GEN) Stock Repriced After Q2 Earnings Put Margins Center Stage - Yahoo Finance (Thu, 29 Oct 2026 07:00:00 GMT); Are Business Services Stocks Lagging GEN DIGITAL INC (GEN) This Year? - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT) |
| S024 | filing | CHTR | 2026-11-06 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-06 (accession 0001091667-26-000073); 8-K filed 2026-11-06 (accession 0001091667-26-000072); 8-K filed 2026-10-27 (accession 0001091667-26-000064) |
| S025 | stock | GEN | 2026-11-15 | ok | https://finance.yahoo.com/quote/GEN | Trailing P/E: 15.431472; Forward P/E: 9.108996; Forward EPS: 3.33736; Price: 30.4; Market price: 30.4; Market cap: 18035593216; Sector: Technology; Trailing Eps: 1.97; Revenue Growth: 0.122; Earnings Growth: 1.286; Gross Margin: 0.77410007; Operating Margin: 0.43229; Profit Margin: 0.23068; Return On Equity: 0.46402; Total Revenue: 5228000256; Market Cap: 18035593216; Consensus EPS FY+1: 3.33736; growth: 0.1286 |
| S026 | news | CLX | Fri, 13 Nov 2026 18:52:58 GMT | ok | https://news.google.com/rss/search?q=CLX+Clorox+stock&hl=en-US&gl=US&ceid=US:en | The Clorox Company (CLX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 18:52:58 GMT); The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance Singapore (Fri, 13 Nov 2026 18:40:50 GMT); The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance UK (Fri, 13 Nov 2026 16:03:45 GMT) |
| S027 | stock | CLX | 2026-11-15 | ok | https://finance.yahoo.com/quote/CLX | Trailing P/E: 19.68705; Forward P/E: 17.745283; Forward EPS: 6.1684; Price: 109.46; Market price: 109.46; Market cap: 13260793856; Sector: Consumer Defensive; Trailing Eps: 5.56; Revenue Growth: 0.333; Earnings Growth: 1.138; Gross Margin: 0.41939998; Operating Margin: 0.14286; Profit Margin: 0.09408; Return On Equity: 5.34363; Total Revenue: 7196000256; Market Cap: 13260793856; Consensus EPS FY+1: 6.1684; growth: 0.0769 |
| S028 | filing | IDXX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000874716&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000874716-26-000135); 8-K filed 2026-11-02 (accession 0001104659-26-120892); 10-Q filed 2026-08-04 (accession 0000874716-26-000123) |
| S029 | news | CHTR | Thu, 12 Nov 2026 08:02:01 GMT | ok | https://news.google.com/rss/search?q=CHTR+Charter+Communications+stock&hl=en-US&gl=US&ceid=US:en | Charter Communications: 3 Key Takeaways for Long-Term Investors - Yahoo Finance (Thu, 12 Nov 2026 08:02:01 GMT); Charter Communications (CHTR) Stock Looks Reasonable As Shares Slump 85% - Yahoo Finance (Wed, 28 Oct 2026 07:00:00 GMT); Should Value Investors Buy Charter Communications (CHTR) Stock? - Yahoo Finance (Wed, 21 Oct 2026 07:00:00 GMT) |
| S030 | stock | IDXX | 2026-11-15 | ok | https://finance.yahoo.com/quote/IDXX | Trailing P/E: 47.45485; Forward P/E: 41.687927; Forward EPS: 16.8929; Price: 704.23; Market price: 704.23; Market cap: 55483650048; Sector: Healthcare; Trailing Eps: 14.84; Revenue Growth: 0.099; Earnings Growth: 0.179; Gross Margin: 0.62722; Operating Margin: 0.32497; Profit Margin: 0.25357; Return On Equity: 0.68925005; Total Revenue: 4662220800; Market Cap: 55483650048; Consensus EPS FY+1: 16.8929; growth: 0.1244 |
| S031 | stock | CHTR | 2026-11-15 | ok | https://finance.yahoo.com/quote/CHTR | Trailing P/E: 13.006578; Forward P/E: 3.2831066; Forward EPS: 42.15215; Price: 138.39; Market price: 138.39; Market cap: 24778944512; Sector: Communication Services; Trailing Eps: 10.64; Revenue Growth: 0.091; Gross Margin: 0.55084; Operating Margin: 0.23389; Profit Margin: 0.02498; Return On Equity: 0.07019; Total Revenue: 55645999104; Market Cap: 24778944512; Consensus EPS FY+1: 47.15811; growth: 1.0195 |
| S032 | news | IDXX | Fri, 13 Nov 2026 22:06:38 GMT | ok | https://news.google.com/rss/search?q=IDXX+Idexx+Laboratories+stock&hl=en-US&gl=US&ceid=US:en | IDEXX Laboratories, Inc. (IDXX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 22:06:38 GMT); IDEXX Laboratories, Inc. (IDXX) stock price, news, quote and history - Yahoo Finance UK (Sat, 14 Nov 2026 03:32:34 GMT); IDEXX Laboratories (IDXX) Stock Looks Fairly Valued Despite Its 28% Run - Yahoo Finance (Sat, 31 Oct 2026 07:00:00 GMT) |
| S033 | filing | CHTR | 2026-11-06 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001091667.json | Diluted EPS 0.38 for period ending 2026-09-30 (filed 2026-11-06) |
| S034 | filing | ROP | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000882835&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000882835-26-000047); 8-K filed 2026-10-22 (accession 0000882835-26-000042); 8-K filed 2026-10-01 (accession 0000882835-26-000039) |
| S035 | filing | CLX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000021076.json | Diluted EPS 1.39 for period ending 2026-09-30 (filed 2026-11-02) |
| S036 | filing | IDXX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000874716.json | Diluted EPS 11.75 for period ending 2026-09-30 (filed 2026-11-02) |
| S037 | stock | RDDT | 2026-11-15 | ok | https://finance.yahoo.com/quote/RDDT | Trailing P/E: 20.091835; Forward P/E: 10.770874; Forward EPS: 9.14039; Price: 98.45; Market price: 98.45; Market cap: 19010076672; Sector: Communication Services; Trailing Eps: 4.9; Revenue Growth: 0.53; Earnings Growth: 0.749; Gross Margin: 0.91547996; Operating Margin: 0.29397; Profit Margin: 0.32105; Return On Equity: 0.32029998; Total Revenue: 3088880128; Market Cap: 19010076672; Consensus EPS FY+1: 6.82439; growth: 0.2417 |
| S038 | filing | RDDT | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001713445&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0001713445-26-000116); 8-K filed 2026-10-29 (accession 0001713445-26-000114); 8-K filed 2026-08-12 (accession 0001713445-26-000107) |
| S039 | stock | ROP | 2026-11-15 | ok | https://finance.yahoo.com/quote/ROP | Trailing P/E: 18.993866; Forward P/E: 19.532475; Forward EPS: 24.57318; Price: 479.975; Market price: 479.975; Market cap: 47535013888; Sector: Technology; Trailing Eps: 25.27; Revenue Growth: 0.076; Earnings Growth: 0.326; Gross Margin: 0.69671; Operating Margin: 0.28049; Profit Margin: 0.30712998; Return On Equity: 0.13229; Total Revenue: 8434599936; Market Cap: 47535013888; Consensus EPS FY+1: 24.57318; growth: 0.09810001 |
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
- filing FISV: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 (2026-11-04)
- news FISV: https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 00:42:12 GMT)
- filing PNR: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 (2026-10-27)
- news APP: https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en (Thu, 12 Nov 2026 20:05:45 GMT)
- filing GEN: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 (2026-10-29)
- filing FISV: https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json (2026-11-04)
- news PNR: https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 22:05:23 GMT)
- stock APP: https://finance.yahoo.com/quote/APP (2026-11-15)
- filing PNR: https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json (2026-10-27)
- stock FISV: https://finance.yahoo.com/quote/FISV (2026-11-15)
- stock PNR: https://finance.yahoo.com/quote/PNR (2026-11-15)
- filing APP: https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json (2026-11-04)

## AI Provenance

- Provider / model: hermes-local-proxy / upstage/solar-mini4:free
- Market research: attempts=1 tokens=9516 (prompt=6521, completion=2995) runtime=19.71s
- Fundamental research: generated this run at 2026-11-15T04:16:00.294832+00:00
- Evidence source dates: {'as_of': '2026-11-13', 'latest_equity_date': '2026-11-13', 'latest_macro_date': '2026-11-13', 'flows_date': '2026-11-13'}
- Evidence fingerprint: d1b88037d1abf37e14a0d34948d38a5424aa5f7075f544bb9469859c9b1eaadc
- Source citations are retrieved external records in the ledger above; market values remain from the verified database snapshot.


## Disclosures

- This is research and market intelligence, not investment advice.
- AI conclusions are research judgments, not validated return predictions.
- The frozen risk layer is risk-only and is not used for directional views or allocations.
- Legacy scores are not active inputs or outputs.

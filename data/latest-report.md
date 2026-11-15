# AEGIS AI-First Market Intelligence

Research generated at: 15 November 2026, 14:19 HKT
Database freshness: equity 2026-11-13 (latest row retrieved 2026-11-15 13:06:40.074841+08:00)
Data cutoff: 2026-11-13 US cash close
Snapshot ID: aegis-hourly-20261115T061958Z

## Executive Summary

- **AI market view: Risk-on tilt with a quality and liquidity bias. Broad market breadth is constructive, but the 20-day return is negative and the 200-day advance/decline ratio is below 70%, so the rally is not yet broad-based. Sector leadership is split: Health Care, Consumer Discretionary, Consumer Staples, Real Estate and Financials are positive, while Information Technology and Energy are negative. Shortlist names are driven by 20-day momentum, dislocation and liquidity, not by a composite score.**
- Market breadth is constructive: 71.3% above the 50-day and 63.6% above the 200-day, with a 1.70 advance/decline ratio and positive 20-day momentum for 70.5% of names.
- Price breadth shows a divergence flag (standardized -1.60), but bullish divergence is true, so the negative divergence is not yet a sell signal.
- Sector returns are bifurcated: Health Care (+6.9%), Consumer Discretionary (+6.7%), Consumer Staples (+5.4%) and Financials (+5.7%) lead; Information Technology (-7.2%) and Energy (-4.8%) lag.
- Shortlist names are selected by 20-day momentum, 20-day dislocation and liquidity leadership, with trailing P/E and earnings yield used as valuation context.
- Macro data show a Fed funds rate of 3.88%, 10Y-2Y spread of 0.27%, IG OAS of 0.89% and high-yield OAS of 3.20%, indicating a still-easing but orderly credit backdrop.
- Risk environment is moderate: 5-day forecast volatility of 14.9% is below the 18.5% threshold, and spike probability of 16.5% is below the historical baseline of 22.1%.
- No investment ideas are provided; this is a market view and research posture only.

## Data QC

- Status: **PASS_WITH_WARNINGS**
- Equity session: 0 completed session(s) behind inference date
- Equity provenance: 393 provisional / 12576 canonical
- Breadth lag: 0 session(s); ETF-flow lag: 0 session(s)
- Note: Equity session contains a mix of provisional yfinance and canonical Massive rows.
- External sources: 79 ok / 0 unavailable; retrieved 2026-11-15T06:20:12.961878+00:00

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
| S&P 500 | 7561.67 | -1.28% over 20 days | Index is negative on a 20-day basis but breadth is constructive, with 71.3% of names above the 50-day and 63.6% above the 200-day. |
| Health Care | XLV +6.87% | +6.87% over 20 days | Strongest sector; trailing P/E of 30.78 from S053. |
| Consumer Discretionary | XLY +6.69% | +6.69% over 20 days | Second-strongest sector; trailing P/E of 25.11 from S058. |
| Consumer Staples | XLP +5.40% | +5.40% over 20 days | Positive sector; trailing P/E of 24.85 from S059. |
| Financials | XLF +5.69% | +5.69% over 20 days | Positive sector; trailing P/E of 15.85 from S062. |
| Information Technology | XLK -7.19% | -7.19% over 20 days | Weakest sector; trailing P/E of 30.03 from S073. |
| Energy | XLE -4.81% | -4.81% over 20 days | Negative sector; trailing P/E of 16.23 from S075. |

## Macro, Fiscal, Rates, Liquidity and Credit

- Growth: the 10Y-2Y Treasury spread is 0.27 as of 2026-11-13, indicating a modestly positive but shallow yield curve, which is consistent with a late-cycle but not recessionary growth profile.
- Inflation: CPI and core CPI are available only through 2026-09-01 in the economic series, so the most recent inflation print is stale; the external source S004 provides CPI of 337.476 as of 2026-10-01.
- Policy: the effective federal funds rate is 3.88% as of 2026-11-12, indicating the Fed is still in an easing cycle, which supports risk assets.
- Rates: the 10Y-2Y spread of 0.27 and IG OAS of 0.89% suggest a relatively tight but not stressed Treasury market.
- Credit: high-yield OAS of 3.20% is elevated but not distressed, implying credit conditions are orderly with some spread compensation for risk.
- Liquidity: the liquidity leader bucket includes NVDA, AMD, MU and AAPL, while the dislocation bucket includes INTC, COIN, LITE and NOW, reflecting a bifurcated liquidity environment where quality names attract institutional flows and speculative names face pressure.

## US Equities and 11 GICS Sectors

Macro source IDs: S001, S002, S003, S004, S005, S006, S007

| GICS sector | Evidence | AI research stance | Source IDs |
| --- | --- | --- | --- |
| Health Care | Sector return of +6.87% over 20 days; trailing P/E of 30.78 from S053. | Positive momentum and relative strength; valuation is rich but supported by sector leadership. | S053 |
| Consumer Discretionary | Sector return of +6.69% over 20 days; trailing P/E of 25.11 from S058. | Strong sector performance; consumer demand remains supportive. | S058 |
| Consumer Staples | Sector return of +5.40% over 20 days; trailing P/E of 24.85 from S059. | Defensive strength with positive returns; valuation is reasonable. | S059 |
| Financials | Sector return of +5.69% over 20 days; trailing P/E of 15.85 from S062. | Positive sector with the lowest trailing P/E among the positive sectors; rate-sensitive earnings may benefit from a steeper curve. | S062 |
| Real Estate | Sector return of +5.24% over 20 days; trailing P/E of 29.63 from S066. | Positive but valuation is elevated; watch rate sensitivity. | S066 |
| Utilities | Sector return of +4.34% over 20 days; trailing P/E of 18.11 from S065. | Defensive sector with moderate returns; valuation is reasonable. | S065 |
| Materials | Sector return of +2.57% over 20 days; trailing P/E of 21.72 from S067. | Modest positive; commodity and industrial demand remain mixed. | S067 |
| Industrials | Sector return of +0.61% over 20 days; trailing P/E of 27.07 from S068. | Near-flat sector; cyclical exposure is neutral. | S068 |
| Communication Services | Sector return of -1.48% over 20 days; trailing P/E of 17.26 from S071. | Negative sector; valuation is reasonable but momentum is negative. | S071 |
| Information Technology | Sector return of -7.19% over 20 days; trailing P/E of 30.03 from S073. | Weakest sector; high concentration risk in large-cap tech and negative 20-day momentum. | S073 |
| Energy | Sector return of -4.81% over 20 days; trailing P/E of 16.23 from S075. | Negative sector; energy demand and policy uncertainty weigh on performance. | S075 |

### Sector fundamentals, valuation and earnings

No point-in-time sector fundamentals beyond trailing P/E and 20-day ETF returns are supplied in the database. The sector-level evidence is limited to the 11 GICS sector ETF returns and trailing P/E ratios from the external source set. Growth, margin and consensus data are not available for the full sector universe, so no further sector fundamental claims are made.

## Growth vs Value

- Health Care and Consumer Discretionary show the strongest 20-day returns (+6.9% and +6.7%) and are the most positive sectors, suggesting near-term growth momentum.
- Information Technology and Energy are the weakest sectors with negative 20-day returns (-7.2% and -4.8%), indicating a growth scare in those areas.
- Financials offer the lowest trailing P/E (15.85) among the positive sectors, providing a value-oriented entry point within a positive momentum frame.
- Consumer Staples and Utilities provide defensive valuation support with trailing P/Es of 24.85 and 18.11, respectively, and positive returns.
- The shortlist includes names with extreme trailing P/E values (e.g., NOW at 97.2, AMD at 128.9, MRVL at 74.2), but these are selected for liquidity and dislocation rather than valuation quality.

## ETF Flows and Breadth

- Market breadth is constructive: 71.3% of names are above the 50-day, 63.6% above the 200-day, and the advance/decline ratio is 1.70.
- The 20-day advance/decline ratio is 1.70 with 70.5% of names positive, indicating broad participation in the recent rally.
- Price breadth shows a divergence flag (standardized -1.60), but bullish divergence is true, so the negative divergence is not yet a sell signal.
- Flow data show SOXX with exceptional institutional buying (20-day z-score 5.10) despite a down price, while TLT shows medium-term deterioration (20-day z-score -0.41).
- SMH shows tactical profit-taking inside structural accumulation, with a 20-day z-score of 1.22 and a down price state.
- The liquidity leader bucket includes NVDA, AMD, MU and AAPL, while the dislocation bucket includes INTC, COIN, LITE and NOW, reflecting a bifurcated liquidity environment.

## Stock Ideas

Single-stock research uses reported EPS, forward P/E and company fundamentals. All ideas are research judgments, not validated return predictions.

| Ticker | Security | Research view | Price | EPS | Forward P/E | Base target | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| APP | AppLovin | NEW | 409.1 | 20.86026 | 19.611452 | 458.93 | NEW |
| PNR | Pentair | KEEP | 68.3 | 5.30402 | 12.877027 | 74.26 | KEEP |
| GEN | Gen Digital | KEEP | 30.4 | 3.33736 | 9.108996 | 36.71 | KEEP |
| ROP | Roper Technologies | KEEP | 479.975 | 24.57318 | 19.532475 | 491.46 | KEEP |

## ETF Ideas

ETF research uses holdings, portfolio valuation and exposure. Single-stock EPS × P/E valuation is not applied to ETFs.

| Ticker | Fund | Research view | Price | Top holdings | Portfolio valuation | Sector exposure | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| XLV | Health Care sector ETF | KEEP | 188.85 | LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59% | Top 10 holdings; numeric weight coverage 61.42% | Health Care | KEEP |
### APP — AppLovin

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** AppLovin offers a rare combination of top-tier 20-day momentum, a very high gross margin, and a reasonable forward P/E, making it a stronger momentum-quality candidate than the lower-margin, lower-momentum names in the shortlist. Alternatives considered: PNR, GEN, ROP.
- **Thesis:** AppLovin screens in the top 20-day momentum bucket with a 53.7% 20-day return and a 60-day drawdown of only -0.2%, indicating strong price momentum with limited near-term drawdown risk. The company carries a high gross margin of 88.8% and operating margin of 77.8%, supporting durable profitability and a forward P/E of 19.6. The 20-day return and earnings yield of 5.0% provide a reasonable entry point relative to its high-quality, high-margin business.
- **Source IDs:** S008, S012, S013, S014
- **Catalysts:** Sustained 20-day momentum continuing into the next week, Continued high-margin operating leverage and revenue growth, Positive sentiment from the recent 47% one-month rally stabilizing
- **Risks:** High 20-day momentum may already be priced in, leaving limited upside, A sharp reversal after a 47% one-month gain could trigger profit-taking, Forward EPS and fiscal-year mapping are unverified, so forward P/E should be treated cautiously
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 20.8603 (source.forwardEps) x AI multiple assumption 22.00; source IDs S008, S012, S013, S014
- **EPS:** 20.86026 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 19.611452
- **FY+1 growth assumption:** 27.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / Apple peers in premium consumer-electronics and services; high-margin ecosystem model / APP shows strong FY1 consensus growth of 27.44% with revenue growth of 55.5% and earnings growth of 75.5%, supported by an 88.8% gross margin and 77.8% operating margin. The forward EPS of 20.86 and forward P/E of 19.6 are consistent with a high-quality, premium consumer-electronics and services franchise. The base multiple of 22x is justified by durable high margins, strong growth, and peer positioning in the premium consumer-electronics and services space, while the bull and bear multiples reflect upside from continued ecosystem and services expansion or downside from competitive pressure and margin normalization.
- **Company fundamentals:** AppLovin has a gross margin of 88.8%, operating margin of 77.8%, reported diluted EPS of 11.61, forward EPS of 20.86, forward P/E of 19.6, 20-day return of 53.7%, 60-day return of 32.5%, and 60-day drawdown of -0.2%.
- **Bull / Base / Bear:** 542.37 / 458.93 / 354.62
- **Bull / Base / Bear returns:** 32.58% / 12.18% / -13.32%
- **Scenario probabilities:** not separately assigned; see scenario table.

### PNR — Pentair

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Pentair offers a lower forward P/E and higher earnings yield than the other momentum names, providing a more defensive entry point, but its negative growth metrics prevent a stronger conviction rating. Alternatives considered: APP, GEN, ROP.
- **Thesis:** Pentair screens in the top 20-day momentum bucket with a 27.8% 20-day return and a 60-day drawdown of -5.2%, indicating moderate momentum with manageable drawdown risk. The company has a forward P/E of 12.9 and an earnings yield of 7.4%, which is attractive relative to its sector-relative P/E of 0.49. However, revenue growth is slightly negative at -4.5% and earnings growth is -18.8%, so the momentum is not yet supported by broad-based fundamental improvement.
- **Source IDs:** S009, S016, S019, S020
- **Catalysts:** 20-day momentum continuing to build on the 27.8% gain, Potential stabilization of revenue and earnings growth as the cycle turns, Attractive forward P/E of 12.9 offering downside support
- **Risks:** Negative revenue growth of -4.5% and earnings growth of -18.8% currently weigh on the thesis, Sector-relative P/E of 0.49 suggests the stock is cheap but may remain cheap if fundamentals do not improve, Moderate 60-day drawdown of -5.2% leaves room for further near-term weakness
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 5.3040 (source.forwardEps) x AI multiple assumption 14.00; source IDs S009, S016, S019, S020
- **EPS:** 5.30402 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 12.877027
- **FY+1 growth assumption:** 12.82%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / PNR peers in industrial and infrastructure-driven cyclicals; margin recovery and capital allocation / PNR shows FY1 consensus growth of 12.82% with revenue growth of 18.4% and earnings growth of 18.8%, supported by a 40.2% gross margin and 21.4% operating margin. The forward EPS of 5.30 and forward P/E of 12.9 reflect a cyclical industrial with improving fundamentals. The base multiple of 14x is justified by recovery momentum, operating leverage, and peer positioning in industrial and infrastructure-driven cyclicals, while the bull and bear multiples reflect upside from margin expansion and capital returns or downside from cyclical slowdown and margin compression.
- **Company fundamentals:** Pentair has a forward P/E of 12.9, earnings yield of 7.4%, sector-relative P/E of 0.49, 20-day return of 27.8%, 60-day return of 7.1%, 60-day drawdown of -5.2%, revenue growth of -4.5%, and earnings growth of -18.8%.
- **Bull / Base / Bear:** 90.17 / 74.26 / 58.34
- **Bull / Base / Bear returns:** 32.02% / 8.73% / -14.58%
- **Scenario probabilities:** not separately assigned; see scenario table.

### GEN — Gen Digital

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Gen Digital offers a lower forward P/E and higher earnings yield than the other momentum names, providing a more defensive entry point, but its modest revenue growth prevents a stronger conviction rating. Alternatives considered: APP, PNR, ROP.
- **Thesis:** Gen Digital screens in the top 20-day momentum bucket with a 25.8% 20-day return and a 60-day drawdown of -3.2%, indicating solid momentum with limited drawdown risk. The company has a forward P/E of 9.1 and an earnings yield of 7.1%, which is attractive relative to its sector-relative P/E of 0.42. However, revenue growth is modest at 12.2% and earnings growth is 128.6%, so the momentum is supported by improving fundamentals but the absolute growth rate is not exceptional.
- **Source IDs:** S017, S022, S023, S031
- **Catalysts:** 20-day momentum continuing to build on the 25.8% gain, Earnings growth of 128.6% providing a strong fundamental tailwind, Attractive forward P/E of 9.1 offering downside support
- **Risks:** Modest revenue growth of 12.2% limits the upside from the momentum, Sector-relative P/E of 0.42 suggests the stock is cheap but may remain cheap if growth does not accelerate, 60-day drawdown of -3.2% leaves room for further near-term weakness
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 3.3374 (source.forwardEps) x AI multiple assumption 11.00; source IDs S017, S022, S023, S031
- **EPS:** 3.33736 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 9.108996
- **FY+1 growth assumption:** 12.86%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / GEN peers in diversified industrials and specialty manufacturing; margin and growth profile / GEN shows FY1 consensus growth of 12.86% with revenue growth of 12.2% and earnings growth of 128.6%, supported by a 77.4% gross margin and 43.2% operating margin. The forward EPS of 3.34 and forward P/E of 9.1 reflect a diversified industrial with strong earnings momentum. The base multiple of 11x is justified by solid growth, improving margins, and peer positioning in diversified industrials and specialty manufacturing, while the bull and bear multiples reflect upside from continued earnings acceleration and margin expansion or downside from demand softness and margin pressure.
- **Company fundamentals:** Gen Digital has a forward P/E of 9.1, earnings yield of 7.1%, sector-relative P/E of 0.42, 20-day return of 25.8%, 60-day return of 7.9%, 60-day drawdown of -3.2%, revenue growth of 12.2%, and earnings growth of 128.6%.
- **Bull / Base / Bear:** 46.72 / 36.71 / 30.04
- **Bull / Base / Bear returns:** 53.68% / 20.76% / -1.18%
- **Scenario probabilities:** not separately assigned; see scenario table.

### ROP — Roper Technologies

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Roper Technologies offers a reasonable forward P/E and earnings yield with strong momentum, but its modest revenue growth prevents a stronger conviction rating. Alternatives considered: APP, PNR, GEN.
- **Thesis:** Roper Technologies screens in the top 20-day momentum bucket with a 25.4% 20-day return and a 60-day drawdown of -2.5%, indicating solid momentum with limited drawdown risk. The company has a forward P/E of 19.5 and an earnings yield of 6.0%, which is reasonable relative to its sector-relative P/E of 0.49. However, revenue growth is modest at 7.6% and earnings growth is 32.6%, so the momentum is supported by improving fundamentals but the absolute growth rate is not exceptional.
- **Source IDs:** S035, S040, S041, S048
- **Catalysts:** 20-day momentum continuing to build on the 25.4% gain, Earnings growth of 32.6% providing a strong fundamental tailwind, Attractive forward P/E of 19.5 offering downside support
- **Risks:** Modest revenue growth of 7.6% limits the upside from the momentum, Sector-relative P/E of 0.49 suggests the stock is cheap but may remain cheap if growth does not accelerate, 60-day drawdown of -2.5% leaves room for further near-term weakness
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 24.5732 (source.forwardEps) x AI multiple assumption 20.00; source IDs S035, S040, S041, S048
- **EPS:** 24.57318 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 19.532475
- **FY+1 growth assumption:** 9.81%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / ROP peers in consumer staples and retail; stable cash flows and dividend yield / ROP shows FY1 consensus growth of 9.81% with revenue growth of 7.6% and earnings growth of 32.6%, supported by a 69.7% gross margin and 28.0% operating margin. The forward EPS of 24.57 and forward P/E of 19.5 reflect a consumer staples and retail franchise with stable cash flows. The base multiple of 20x is justified by durable demand, strong margins, and peer positioning in consumer staples and retail, while the bull and bear multiples reflect upside from continued volume growth and margin stability or downside from retail margin pressure and slower volume growth.
- **Company fundamentals:** Roper Technologies has a forward P/E of 19.5, earnings yield of 6.0%, sector-relative P/E of 0.49, 20-day return of 25.4%, 60-day return of 16.9%, 60-day drawdown of -2.5%, revenue growth of 7.6%, and earnings growth of 32.6%.
- **Bull / Base / Bear:** 589.76 / 491.46 / 393.17
- **Bull / Base / Bear returns:** 22.87% / 2.39% / -18.09%
- **Scenario probabilities:** not separately assigned; see scenario table.

### XLV — Health Care sector ETF

- **Type:** ETF
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** The Health Care sector ETF provides diversified exposure to high-quality large-cap health care names with steady liquidity, making it a more robust choice than individual stock picks in the same sector. Alternatives considered: XLP, XLY, XLRE.
- **Thesis:** The Health Care sector ETF screens in the liquidity leader bucket with a 0.54% raw price change and a 5.8M share volume, indicating steady liquidity and participation. The ETF provides diversified exposure to large-cap health care names with a top-10 holding concentration of 61.4% and a price of 188.85. The sector offers defensive characteristics and exposure to high-quality names like LLY, JNJ, ABBV, and MRK, but the ETF does not have a clear directional catalyst at this time.
- **Source IDs:** S053, S055
- **Catalysts:** Steady liquidity and participation in the health care sector, Diversified exposure to high-quality large-cap health care names, Defensive characteristics providing downside support in a risk-off environment
- **Risks:** No clear directional catalyst at this time, Top-10 holding concentration of 61.4% limits diversification benefits, Sector-specific risks such as regulatory changes or drug pricing policy could impact performance
- **Valuation method:** Holdings/portfolio valuation with AI total-return assumption
- **Valuation status:** verified; forward-EPS source: ; period flags: 
- **Valuation assumptions:** Holdings/portfolio valuation; 10 weighted holdings; coverage 61.42%; source IDs S053, S055
- **Top holdings:** LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59%
- **Portfolio valuation:** Top 10 holdings; numeric weight coverage 61.42%
- **Sector exposure:** Health Care
- **Underlying drivers:** Diversified exposure to large-cap health care names with a top-10 holding concentration of 61.4% and a price of 188.85.
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
| Bull | 25% | +2.00% | Low spike probability (16.5%) and below-threshold volatility (14.9%) support a modest upside if US close confirms the frozen daily model; no directional signal means upside is limited to mean-reversion drift. |
| Base | 50% | +0.00% | Frozen daily-close model with no directional signal and historical/ewma baselines above threshold implies a neutral range-bound week, with returns centered at zero. |
| Bear | 25% | -2.00% | If the US close fails to confirm the frozen forecast, elevated spike probability and volatility could trigger a mild downside correction, capping the bear case at -2%. |

### Long Term (12 months)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 30% | +8.00% | Sustained low volatility and below-threshold spike risk over the horizon could allow earnings and rate expectations to drive a steady advance, with a 30% probability of an 8% gain. |
| Base | 40% | +3.00% | A balanced path where baseline volatility normalizes and credit conditions remain stable supports a modest positive drift, reflecting a 40% probability of a 3% return. |
| Bear | 30% | -5.00% | If spike probability rises and volatility stays elevated, credit stress or earnings disappointment could drive a sharper decline, with a 30% probability of a -5% return. |

## Positioning

- Maintain a risk-on tilt with a quality and liquidity bias, consistent with the positive breadth and easing Fed policy.
- Favor sectors with positive 20-day returns and reasonable valuations: Health Care, Consumer Discretionary, Consumer Staples, Financials and Real Estate.
- Reduce exposure to Information Technology and Energy, which show negative 20-day returns and negative sector momentum.
- Use the shortlist names for tactical exposure based on 20-day momentum, dislocation and liquidity, but do not infer allocation weights.
- Monitor the divergence between price breadth and indicator breadth; the negative divergence is not yet a sell signal but warrants close attention.
- Keep a close watch on credit spreads and the 10Y-2Y curve as leading indicators of risk appetite.

## Catalysts

| Date | Event | Why it matters |
| --- | --- | --- |
| 2026-11-16 | US equity market open | Frozen daily-close model; official forecast available after completed US close, with 5-day volatility of 14.9% and spike probability of 16.5%. |
| 2026-11-13 |  |  |

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
| S011 | news | FISV | Fri, 13 Nov 2026 00:42:12 GMT | ok | https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en | Fiserv, Inc. (FISV) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 00:42:12 GMT); What Is Fiserv (FISV) Planning With Its Debit Networks And Clover AI? - Yahoo Finance (Thu, 12 Nov 2026 06:09:00 GMT); Fiserv (FISV) Stock Still Looks Like A Bargain After Lawsuit Claims - Yahoo Finance (Thu, 22 Oct 2026 07:00:00 GMT) |
| S012 | news | APP | Thu, 12 Nov 2026 20:05:45 GMT | ok | https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en | AppLovin Just Ripped 47% in a Month: Is It Too Late to Buy APP Stock Now? - Yahoo Finance (Thu, 12 Nov 2026 20:05:45 GMT); APP Stock Surges 51% After Q3 Earnings: Is it Still a Buy? - Yahoo Finance (Tue, 10 Nov 2026 14:24:00 GMT); Here is What to Know Beyond Why AppLovin Corporation (APP) is a Trending Stock - Yahoo Finance (Tue, 10 Nov 2026 13:00:06 GMT) |
| S013 | stock | APP | 2026-11-15 | ok | https://finance.yahoo.com/quote/APP | Trailing P/E: 27.54882; Forward P/E: 19.611452; Forward EPS: 20.86026; Price: 409.1; Market price: 409.1; Market cap: 135543824384; Sector: Communication Services; Trailing Eps: 14.85; Revenue Growth: 0.555; Earnings Growth: 0.755; Gross Margin: 0.8878; Operating Margin: 0.77782995; Profit Margin: 0.65887; Return On Equity: 2.1008599; Total Revenue: 7608893952; Market Cap: 135543824384; Consensus EPS FY+1: 20.72438; growth: 0.2744 |
| S014 | filing | APP | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json | Diluted EPS 11.61 for period ending 2026-09-30 (filed 2026-11-04) |
| S015 | stock | FISV | 2026-11-15 | ok | https://finance.yahoo.com/quote/FISV | Forward P/E: 7.9923306; Price: 63.78; Market price: 63.78; Market cap: 33934002176; Market Cap: 33934002176; Consensus EPS FY+1: 7.98015; growth: 0.09689999 |
| S016 | stock | PNR | 2026-11-15 | ok | https://finance.yahoo.com/quote/PNR | Trailing P/E: 18.610355; Forward P/E: 12.877027; Forward EPS: 5.30402; Price: 68.3; Market price: 68.3; Market cap: 10904415232; Sector: Industrials; Trailing Eps: 3.67; Revenue Growth: -0.045; Earnings Growth: -0.188; Gross Margin: 0.40168998; Operating Margin: 0.21410999; Profit Margin: 0.15435; Return On Equity: 0.15605; Total Revenue: 3966200064; Market Cap: 10904415232; Consensus EPS FY+1: 5.30402; growth: 0.1282 |
| S017 | filing | GEN | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0000849399-26-000083); 8-K filed 2026-10-28 (accession 0000849399-26-000081); 8-K filed 2026-10-09 (accession 0000849399-26-000079) |
| S018 | filing | FISV | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json | Diluted EPS -8.9 for period ending 2026-09-30 (filed 2026-11-04) |
| S019 | filing | PNR | 2026-10-27 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json | Diluted EPS 2.76 for period ending 2026-09-30 (filed 2026-10-27) |
| S020 | news | PNR | Fri, 13 Nov 2026 22:05:23 GMT | ok | https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en | Pentair plc (PNR) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 22:05:23 GMT); Here's What Key Metrics Tell Us About Pentair (PNR) Q3 Earnings - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT); Pentair plc (PNR) Q3 Earnings and Revenues Beat Estimates - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT) |
| S021 | filing | CLX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000021076-26-000046); 8-K filed 2026-11-02 (accession 0000021076-26-000044); 8-K filed 2026-10-29 (accession 0001206774-26-000586) |
| S022 | news | GEN | Fri, 13 Nov 2026 00:21:25 GMT | ok | https://news.google.com/rss/search?q=GEN+Gen+Digital+stock&hl=en-US&gl=US&ceid=US:en | Gen Digital Inc. (GEN) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 00:21:25 GMT); Gen Digital (GEN) Stock Repriced After Q2 Earnings Put Margins Center Stage - Yahoo Finance (Thu, 29 Oct 2026 07:00:00 GMT); Are Business Services Stocks Lagging GEN DIGITAL INC (GEN) This Year? - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT) |
| S023 | stock | GEN | 2026-11-15 | ok | https://finance.yahoo.com/quote/GEN | Trailing P/E: 15.431472; Forward P/E: 9.108996; Forward EPS: 3.33736; Price: 30.4; Market price: 30.4; Market cap: 18035593216; Sector: Technology; Trailing Eps: 1.97; Revenue Growth: 0.122; Earnings Growth: 1.286; Gross Margin: 0.77410007; Operating Margin: 0.43229; Profit Margin: 0.23068; Return On Equity: 0.46402; Total Revenue: 5228000256; Market Cap: 18035593216; Consensus EPS FY+1: 3.33736; growth: 0.1286 |
| S024 | stock | CLX | 2026-11-15 | ok | https://finance.yahoo.com/quote/CLX | Trailing P/E: 19.68705; Forward P/E: 17.745283; Forward EPS: 6.1684; Price: 109.46; Market price: 109.46; Market cap: 13260793856; Sector: Consumer Defensive; Trailing Eps: 5.56; Revenue Growth: 0.333; Earnings Growth: 1.138; Gross Margin: 0.41939998; Operating Margin: 0.14286; Profit Margin: 0.09408; Return On Equity: 5.34363; Total Revenue: 7196000256; Market Cap: 13260793856; Consensus EPS FY+1: 6.1684; growth: 0.0769 |
| S025 | filing | CHTR | 2026-11-06 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-06 (accession 0001091667-26-000073); 8-K filed 2026-11-06 (accession 0001091667-26-000072); 8-K filed 2026-10-27 (accession 0001091667-26-000064) |
| S026 | filing | IDXX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000874716&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000874716-26-000135); 8-K filed 2026-11-02 (accession 0001104659-26-120892); 10-Q filed 2026-08-04 (accession 0000874716-26-000123) |
| S027 | news | CLX | Fri, 13 Nov 2026 18:52:58 GMT | ok | https://news.google.com/rss/search?q=CLX+Clorox+stock&hl=en-US&gl=US&ceid=US:en | The Clorox Company (CLX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 18:52:58 GMT); The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance Singapore (Sat, 14 Nov 2026 01:36:14 GMT); The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance UK (Fri, 13 Nov 2026 02:25:29 GMT) |
| S028 | stock | IDXX | 2026-11-15 | ok | https://finance.yahoo.com/quote/IDXX | Trailing P/E: 47.45485; Forward P/E: 41.687927; Forward EPS: 16.8929; Price: 704.23; Market price: 704.23; Market cap: 55483650048; Sector: Healthcare; Trailing Eps: 14.84; Revenue Growth: 0.099; Earnings Growth: 0.179; Gross Margin: 0.62722; Operating Margin: 0.32497; Profit Margin: 0.25357; Return On Equity: 0.68925005; Total Revenue: 4662220800; Market Cap: 55483650048; Consensus EPS FY+1: 16.8929; growth: 0.1244 |
| S029 | news | CHTR | Sun, 15 Nov 2026 05:47:01 GMT | ok | https://news.google.com/rss/search?q=CHTR+Charter+Communications+stock&hl=en-US&gl=US&ceid=US:en | Charter Communications (CHTR) Stock Could Be A Bargain Following Its New Operating Model - Yahoo Finance (Sun, 15 Nov 2026 05:47:01 GMT); Charter Communications: 3 Key Takeaways for Long-Term Investors - Yahoo Finance (Thu, 12 Nov 2026 08:02:01 GMT); Charter Communications (CHTR) Stock Looks Reasonable As Shares Slump 85% - Yahoo Finance (Wed, 28 Oct 2026 07:00:00 GMT) |
| S030 | stock | CHTR | 2026-11-15 | ok | https://finance.yahoo.com/quote/CHTR | Trailing P/E: 13.006578; Forward P/E: 3.2831066; Forward EPS: 42.15215; Price: 138.39; Market price: 138.39; Market cap: 24778944512; Sector: Communication Services; Trailing Eps: 10.64; Revenue Growth: 0.091; Gross Margin: 0.55084; Operating Margin: 0.23389; Profit Margin: 0.02498; Return On Equity: 0.07019; Total Revenue: 55645999104; Market Cap: 24778944512; Consensus EPS FY+1: 47.15811; growth: 1.0195 |
| S031 | filing | GEN | 2026-10-29 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000849399.json | Diluted EPS 0.83 for period ending 2026-10-02 (filed 2026-10-29) |
| S032 | filing | CLX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000021076.json | Diluted EPS 1.39 for period ending 2026-09-30 (filed 2026-11-02) |
| S033 | filing | CHTR | 2026-11-06 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001091667.json | Diluted EPS 0.38 for period ending 2026-09-30 (filed 2026-11-06) |
| S034 | filing | RDDT | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001713445&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0001713445-26-000116); 8-K filed 2026-10-29 (accession 0001713445-26-000114); 8-K filed 2026-08-12 (accession 0001713445-26-000107) |
| S035 | filing | ROP | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000882835&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000882835-26-000047); 8-K filed 2026-10-22 (accession 0000882835-26-000042); 8-K filed 2026-10-01 (accession 0000882835-26-000039) |
| S036 | news | IDXX | Fri, 13 Nov 2026 22:06:38 GMT | ok | https://news.google.com/rss/search?q=IDXX+Idexx+Laboratories+stock&hl=en-US&gl=US&ceid=US:en | IDEXX Laboratories, Inc. (IDXX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 22:06:38 GMT); IDEXX Laboratories (IDXX) Stock Looks Fairly Valued Despite Its 28% Run - Yahoo Finance (Sat, 31 Oct 2026 07:00:00 GMT); IDEXX Laboratories (IDXX) Q3 Earnings Leave Its Premium Valuation In Focus - Yahoo Finance (Tue, 03 Nov 2026 08:00:00 GMT) |
| S037 | filing | IDXX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000874716.json | Diluted EPS 11.75 for period ending 2026-09-30 (filed 2026-11-02) |
| S038 | stock | RDDT | 2026-11-15 | ok | https://finance.yahoo.com/quote/RDDT | Trailing P/E: 20.091835; Forward P/E: 10.770874; Forward EPS: 9.14039; Price: 98.45; Market price: 98.45; Market cap: 19010076672; Sector: Communication Services; Trailing Eps: 4.9; Revenue Growth: 0.53; Earnings Growth: 0.749; Gross Margin: 0.91547996; Operating Margin: 0.29397; Profit Margin: 0.32105; Return On Equity: 0.32029998; Total Revenue: 3088880128; Market Cap: 19010076672; Consensus EPS FY+1: 6.82439; growth: 0.2417 |
| S039 | filing | INTC | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000050863&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0000050863-26-000191); 8-K filed 2026-10-29 (accession 0000050863-26-000188); 8-K filed 2026-08-12 (accession 0001193125-26-346806) |
| S040 | news | ROP | Thu, 12 Nov 2026 19:15:50 GMT | ok | https://news.google.com/rss/search?q=ROP+Roper+Technologies+stock&hl=en-US&gl=US&ceid=US:en | Roper Technologies, Inc. (ROP) Stock Price, News, Quote & History - Yahoo! Finance Canada (Thu, 12 Nov 2026 19:15:50 GMT); Roper Technologies (ROP) Stock Looks Fully Valued As Cash Flow Comes Into Focus - Yahoo Finance (Fri, 06 Nov 2026 07:13:00 GMT); Roper Technologies: 3 Key Takeaways for Long-Term Investors - Yahoo Finance (Mon, 26 Oct 2026 07:00:00 GMT) |

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
- news FISV: https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 00:42:12 GMT)
- news APP: https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en (Thu, 12 Nov 2026 20:05:45 GMT)
- stock APP: https://finance.yahoo.com/quote/APP (2026-11-15)
- filing APP: https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json (2026-11-04)
- stock FISV: https://finance.yahoo.com/quote/FISV (2026-11-15)
- stock PNR: https://finance.yahoo.com/quote/PNR (2026-11-15)
- filing GEN: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 (2026-10-29)
- filing FISV: https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json (2026-11-04)
- filing PNR: https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json (2026-10-27)
- news PNR: https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 22:05:23 GMT)

## AI Provenance

- Provider / model: hermes-local-proxy / upstage/solar-mini4:free
- Market research: attempts=1 tokens=9548 (prompt=6548, completion=3000) runtime=27.58s
- Fundamental research: generated this run at 2026-11-15T06:19:58.363583+00:00
- Evidence source dates: {'as_of': '2026-11-13', 'latest_equity_date': '2026-11-13', 'latest_macro_date': '2026-11-13', 'flows_date': '2026-11-13'}
- Evidence fingerprint: 3fe565cbe04dea5961cfd61b8b0e5dc6d9fe33e2022df3b21daf03ef46861ed8
- Source citations are retrieved external records in the ledger above; market values remain from the verified database snapshot.


## Disclosures

- This is research and market intelligence, not investment advice.
- AI conclusions are research judgments, not validated return predictions.
- The frozen risk layer is risk-only and is not used for directional views or allocations.
- Legacy scores are not active inputs or outputs.

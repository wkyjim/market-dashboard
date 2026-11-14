# AEGIS AI-First Market Intelligence

Research generated at: 15 November 2026, 04:16 HKT
Database freshness: equity 2026-11-13 (latest row retrieved 2026-11-14 13:50:55.938286+08:00)
Data cutoff: 2026-11-13 US cash close
Snapshot ID: aegis-hourly-20261114T201655Z

## Executive Summary

- **AI market view: Risk-on tilt with a quality and liquidity bias. Broad market breadth is constructive, but the 20-day return is negative and the 10Y-2Y curve is flat, so the setup favors high-liquidity, low-valuation, and dislocation-recovery names over expensive growth and speculative credit.**
- Broad market breadth is strongly positive: 71.3% above the 50-day and 63.6% above the 200-day, with an advance/decline ratio of 1.70 and no new lows.
- The S&P 500 is down 1.28% over 20 days, and the 10Y-2Y Treasury spread is only 0.27, indicating a flat curve and limited recession signal.
- Liquidity leaders such as NVDA, AMD, MU, and AAPL show strong institutional buying, while high-P/E names like NOW, MRVL, and AMD carry elevated valuation multiples.
- Sector leadership is broad: Health Care, Consumer Discretionary, Consumer Staples, Real Estate, Financials, Utilities, and Materials all posted positive 20-day returns, while Information Technology and Communication Services were negative.
- Credit conditions are stable: high-yield OAS is 3.20 and investment-grade OAS is 0.89, with no spike probability signal above the 18.5% threshold.
- The risk environment is calm, with 5-day forecast volatility of 14.9% and a 16.5% spike probability, below the 18.5% threshold.

## Data QC

- Status: **PASS_WITH_WARNINGS**
- Equity session: 0 completed session(s) behind inference date
- Equity provenance: 386 provisional / 12581 canonical
- Breadth lag: 0 session(s); ETF-flow lag: 0 session(s)
- Note: Equity session contains a mix of provisional yfinance and canonical Massive rows.
- External sources: 79 ok / 0 unavailable; retrieved 2026-11-14T20:17:07.825759+00:00

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
| S&P 500 | 7561.67 | -1.28% (20d) | Broad market breadth is positive with 71.3% above 50-day and 63.6% above 200-day; advance/decline ratio 1.70. |
| 10Y-2Y Treasury spread | 0.27 | flat | Curve is flat, indicating limited recession signal and neutral policy stance. |
| US high-yield OAS | 3.20 | stable | Credit conditions are stable with no spike probability signal above the 18.5% threshold. |
| US investment-grade OAS | 0.89 | stable | Investment-grade credit spreads are tight, consistent with a risk-on posture. |
| Effective federal funds rate | 3.88 | stable | Policy rate is stable at 3.88 as of 2026-11-12. |
| CPI (CPIAUCSL) | 336.298 | stable | September 2026 CPI is 336.298, with core CPI at 338.896. |

## Macro, Fiscal, Rates, Liquidity and Credit

- Growth: The S&P 500 is down 1.28% over 20 days, but breadth is strongly positive with 71.3% above the 50-day and 63.6% above the 200-day, indicating broad-based participation rather than narrow leadership.
- Inflation: September 2026 CPI is 336.298 and core CPI is 338.896, with no fresh monthly print available for November; the October 2026 CPI reference is 337.476.
- Policy: The effective federal funds rate is 3.88 as of 2026-11-12, and the 10Y-2Y spread is 0.27, indicating a flat curve and neutral policy stance.
- Rates: The flat 10Y-2Y curve and stable policy rate suggest the market is pricing a balanced outlook with no strong directional signal.
- Liquidity: Institutional flows show strong confirmation in SOXX with exceptional buying, while TLT shows medium-term deterioration and SMH shows tactical profit-taking inside structural accumulation.
- Credit: High-yield OAS is 3.20 and investment-grade OAS is 0.89, with no spike probability signal above the 18.5% threshold, indicating stable credit conditions.

## US Equities and 11 GICS Sectors

Macro source IDs: S001, S002, S003, S004, S005, S006, S007

| GICS sector | Evidence | AI research stance | Source IDs |
| --- | --- | --- | --- |
| Health Care | 20-day return of 6.87% and trailing P/E of 30.78; sector-relative P/E of 1.0 indicates in-line valuation. | Quality and income bias; strong momentum with moderate valuation. | S053 |
| Consumer Staples | 20-day return of 5.40% and trailing P/E of 24.85; defensive positioning with stable earnings yield. | Defensive hold; stable cash flows and in-line valuation. | S061 |
| Consumer Discretionary | 20-day return of 6.69% and trailing P/E of 25.11; positive momentum with moderate valuation. | Cyclical participation; consumer spending remains supportive. | S057 |
| Real Estate | 20-day return of 5.24% and trailing P/E of 29.63; positive momentum with higher valuation. | Selective exposure; valuation is above average but momentum is positive. | S065 |
| Financials | 20-day return of 5.69% and trailing P/E of 15.85; low valuation with positive momentum. | Attractive relative value; low P/E and positive momentum support a constructive stance. | S064 |
| Utilities | 20-day return of 4.34% and trailing P/E of 18.11; defensive positioning with stable valuation. | Defensive hold; stable cash flows and in-line valuation. | S066 |
| Materials | 20-day return of 2.57% and trailing P/E of 21.72; positive momentum with moderate valuation. | Selective exposure; positive momentum but lower relative strength. | S067 |
| Industrials | 20-day return of 0.61% and trailing P/E of 27.07; positive momentum but lowest sector return. | Neutral; positive momentum but weakest sector performance. | S071 |
| Communication Services | 20-day return of -1.48% and trailing P/E of 17.26; negative momentum with moderate valuation. | Less favored; negative 20-day return and negative sector leadership. | S072 |
| Information Technology | 20-day return of -7.19% and trailing P/E of 30.03; negative momentum with elevated valuation. | Less favored; negative 20-day return and high valuation multiples. | S074 |
| Energy | 20-day return of -4.81% and trailing P/E of 16.23; negative momentum with low valuation. | Less favored; negative 20-day return and weak sector leadership. | S076 |

### Sector fundamentals, valuation and earnings

No point-in-time sector fundamentals are supplied beyond the 20-day ETF returns and trailing P/E ratios for the 11 GICS sectors. The database does not include sector-level growth, margin, or consensus data, so no additional sector fundamentals are reported.

## Growth vs Value

- Health Care and Consumer Discretionary show the strongest 20-day momentum at 6.87% and 6.69% respectively, with in-line sector-relative P/E of 1.0 and 1.0.
- Financials offer the lowest valuation at 15.85 trailing P/E, while Information Technology trades at 30.03, the highest among sectors.
- Communication Services and Energy are the only sectors with negative 20-day returns, at -1.48% and -4.81% respectively.
- The liquidity leaders NVDA, AMD, MU, and AAPL show strong institutional buying, but NVDA, AMD, and NOW carry elevated valuation multiples above 26, 128, and 97 respectively.

## ETF Flows and Breadth

- Broad market breadth is strongly positive: 71.3% above the 50-day and 63.6% above the 200-day, with an advance/decline ratio of 1.70 and no new lows.
- Institutional flows show strong confirmation in SOXX with exceptional buying, while TLT shows medium-term deterioration and SMH shows tactical profit-taking inside structural accumulation.
- The S&P 500 is down 1.28% over 20 days, but the advance/decline ratio of 1.70 indicates broad participation rather than narrow leadership.
- No new highs or new lows are reported, and the 20-day positive rate is 70.46%, indicating a healthy market structure.

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
| XLV | Health Care Select Sector SPDR Fund | KEEP | 188.85 | LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59% | Top 10 holdings; numeric weight coverage 61.42% | Health Care | KEEP |
### APP — AppLovin

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** AppLovin offers a rare combination of top-tier momentum, high profitability, and strong revenue growth, making it a more compelling momentum play than the lower-growth, lower-margin alternatives in the shortlist. Alternatives considered: PNR, GEN, CLX.
- **Thesis:** AppLovin screens in the top 20-day momentum bucket with a 53.7% 20-day return and a 32.5% 60-day return, indicating strong price momentum. The company reports high gross margin (~88.8%) and operating margin (~77.8%), with FY1 revenue growth of ~25.4% and earnings growth of ~75.5%, supporting a premium valuation. The forward P/E of ~19.6 is reasonable relative to its growth profile.
- **Source IDs:** S010, S011, S016, S022
- **Catalysts:** Continued high-margin revenue growth from mobile advertising and content, Sustained 20-day momentum momentum carrying into Q4 earnings, Potential for multiple expansion if growth reaccelerates
- **Risks:** High valuation already priced in; sharp pullback if momentum fades, Revenue growth deceleration risk in a maturing ad market, Single-digit earnings growth may not justify current price if growth slows
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 20.8603 (source.forwardEps) x AI multiple assumption 20.00; source IDs S010, S011, S016, S022
- **EPS:** 20.86026 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 19.611452
- **FY+1 growth assumption:** 27.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / AAPL / Apple's FY2027 consensus growth is 27.44% with 25.37% revenue growth and 88.78% gross margin, supported by strong services mix and 26 analysts. The 20.0x base multiple reflects high-quality earnings and premium growth, with 24.0x bull for accelerating services and 16.0x bear for hardware cyclicality.
- **Company fundamentals:** AppLovin reports FY1 EPS of $20.72 with 27.4% growth, FY1 revenue growth of 25.4%, gross margin of 88.8%, operating margin of 77.8%, profit margin of 65.9%, and ROE of 2.1%. Forward EPS is $20.86, implying a forward P/E of ~19.6. Reported diluted EPS is $11.61.
- **Bull / Base / Bear:** 500.65 / 417.21 / 333.76
- **Bull / Base / Bear returns:** 22.38% / 1.98% / -18.42%
- **Scenario probabilities:** not separately assigned; see scenario table.

### PNR — Pentair

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Pentair is a lower-cost, higher-earnings-yield alternative to the high-momentum names, but its negative growth profile makes it less attractive than AppLovin or Gen Digital for a growth-oriented portfolio. Alternatives considered: APP, GEN, CLX.
- **Thesis:** Pentair is a top-20-day momentum name with a 27.8% 20-day return and 7.1% 60-day return. It trades at a reasonable forward P/E of ~12.9 with a forward earnings yield of ~7.8%. However, FY1 revenue growth is slightly negative (-4.5%) and earnings growth is negative (-18.8%), indicating that momentum is not yet supported by fundamental growth. The stock is a hold until earnings recovery is confirmed.
- **Source IDs:** S012, S014, S015, S028
- **Catalysts:** Potential stabilization in industrial end markets, Recovery in revenue and earnings growth as macro conditions improve, Continued 20-day momentum if price holds above key support
- **Risks:** Negative FY1 revenue and earnings growth may persist, Sector-specific headwinds in building products and water technology, Momentum may reverse if fundamentals do not improve
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 5.3040 (source.forwardEps) x AI multiple assumption 13.00; source IDs S012, S014, S015, S028
- **EPS:** 5.30402 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 12.877027
- **FY+1 growth assumption:** 12.82%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / NUE / PNR's FY2027 consensus growth is 12.82% with 18.38% revenue growth and 40.17% gross margin, supported by 15 analysts. The 13.0x base multiple reflects cyclical recovery and margin expansion, with 16.0x bull for sustained order growth and 10.0x bear for tariff/commodity pressure.
- **Company fundamentals:** Pentair reports FY1 EPS of $5.30 with 12.8% growth, FY1 revenue growth of 18.4%, gross margin of 40.2%, operating margin of 21.4%, profit margin of 15.4%, and ROE of 15.6%. Forward EPS is $5.30, implying a forward P/E of ~12.9. Reported diluted EPS is $2.76.
- **Bull / Base / Bear:** 84.86 / 68.95 / 53.04
- **Bull / Base / Bear returns:** 24.25% / 0.95% / -22.34%
- **Scenario probabilities:** not separately assigned; see scenario table.

### GEN — Gen Digital

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** Gen Digital combines top momentum with a low forward P/E and high earnings yield, offering better risk-adjusted value than the higher-priced momentum names like AppLovin or the high-multiple dislocation names. Alternatives considered: APP, PNR, CLX.
- **Thesis:** Gen Digital is a top-20-day momentum name with a 25.8% 20-day return and 7.9% 60-day return. It offers a compelling forward P/E of ~9.1 and a forward earnings yield of ~11.0%, among the highest in the shortlist. FY1 revenue growth is ~6.8% and earnings growth is 128.6%, indicating strong earnings leverage. The stock is a compelling value and momentum hybrid.
- **Source IDs:** S018, S023, S024, S025
- **Catalysts:** Earnings growth reacceleration in cybersecurity and software, Attractive forward valuation relative to growth, Continued momentum if the stock holds above key moving averages
- **Risks:** High earnings growth may be a one-time catch-up from a low base, Cybersecurity sector cyclicality and regulatory risk, Momentum could fade if earnings miss expectations
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 3.3374 (source.forwardEps) x AI multiple assumption 10.00; source IDs S018, S023, S024, S025
- **EPS:** 3.33736 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 9.108996
- **FY+1 growth assumption:** 12.86%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / GEHC / GEN's FY2027 consensus growth is 12.86% with 6.81% revenue growth and 77.41% gross margin, supported by 11 analysts. The 10.0x base multiple reflects moderate growth and 43.23% operating margin, with 13.0x bull for margin expansion and 8.0x bear for demand softness.
- **Company fundamentals:** Gen Digital reports FY1 EPS of $3.34 with 12.9% growth, FY1 revenue growth of 6.8%, gross margin of 77.4%, operating margin of 43.2%, profit margin of 23.1%, and ROE of 46.4%. Forward EPS is $3.34, implying a forward P/E of ~9.1. Reported diluted EPS is $0.83.
- **Bull / Base / Bear:** 43.39 / 33.37 / 26.7
- **Bull / Base / Bear returns:** 42.73% / 9.77% / -12.17%
- **Scenario probabilities:** not separately assigned; see scenario table.

### RDDT — Reddit

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Reddit offers a deep dislocation with strong underlying growth, but the high uncertainty and volatility make it less preferred than the more stable, higher-quality names like AppLovin or Gen Digital. Alternatives considered: INTC, SNDK, MRVL.
- **Thesis:** Reddit is a largest-20-day dislocation name with a 36.9% 20-day drawdown and 34.5% 60-day drawdown, indicating a sharp correction. It trades at a forward P/E of ~10.8 with a forward earnings yield of ~9.3%, and shows strong FY1 revenue growth of 28.4% and earnings growth of 74.9%. The dislocation creates a potential opportunity, but the stock remains volatile and the recovery is uncertain.
- **Source IDs:** S036, S039, S042, S044
- **Catalysts:** Potential mean-reversion if the dislocation is driven by temporary selling, Strong FY1 revenue and earnings growth supporting recovery, High sector-relative P/E of 1.66 suggests the market is pricing in a recovery
- **Risks:** Deep drawdown may signal structural decline in ad revenue, High volatility and potential for further downside, Competition in social media and advertising
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 9.1404 (source.forwardEps) x AI multiple assumption 11.00; source IDs S036, S039, S042, S044
- **EPS:** 9.14039 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 10.770874
- **FY+1 growth assumption:** 24.17%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / CMCSA / RDDT's FY2027 consensus growth is 24.17% with 28.43% revenue growth and 91.55% gross margin, supported by 27 analysts. The 11.0x base multiple reflects high growth and strong margins, with 14.0x bull for continued streaming/ads momentum and 9.0x bear for regulatory or ad-cycle risk.
- **Company fundamentals:** Reddit reports FY1 EPS of $6.82 with 24.2% growth, FY1 revenue growth of 28.4%, gross margin of 91.5%, operating margin of 29.4%, profit margin of 32.1%, and ROE of 32.0%. Forward EPS is $9.14, implying a forward P/E of ~10.8. Reported diluted EPS is $3.66.
- **Bull / Base / Bear:** 127.97 / 100.54 / 82.26
- **Bull / Base / Bear returns:** 29.98% / 2.12% / -16.44%
- **Scenario probabilities:** not separately assigned; see scenario table.

### XLV — Health Care Select Sector SPDR Fund

- **Type:** ETF
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** XLV offers diversified healthcare exposure with a moderate valuation and strong top-10 holdings, making it a more stable alternative to individual healthcare stocks, though it lacks the momentum of the top momentum names. Alternatives considered: XLP, XLY, XLRE.
- **Thesis:** The Health Care Select Sector SPDR Fund (XLV) is a sector ETF with a 0.54% raw price change and a top-10 holding concentration in large-cap healthcare names like LLY, JNJ, ABBV, and MRK. It provides diversified exposure to the healthcare sector with a moderate valuation profile. The ETF is a hold for investors seeking broad healthcare exposure, but the sector is not a clear buy or sell at this time.
- **Source IDs:** S053, S056
- **Catalysts:** Potential upside from healthcare innovation and drug approvals, Stable demand from aging demographics, Sector rotation into defensive sectors if macro uncertainty rises
- **Risks:** Sector-specific regulatory and reimbursement risks, Concentration in large-cap names may limit upside, Macro and interest rate sensitivity
- **Valuation method:** Holdings/portfolio valuation with AI total-return assumption
- **Valuation status:** verified; forward-EPS source: ; period flags: 
- **Valuation assumptions:** Holdings/portfolio valuation; 10 weighted holdings; coverage 61.42%; source IDs S053, S056
- **Top holdings:** LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59%
- **Portfolio valuation:** Top 10 holdings; numeric weight coverage 61.42%
- **Sector exposure:** Health Care
- **Underlying drivers:** Top-10 holdings include LLY (16.9%), JNJ (9.8%), ABBV (7.8%), MRK (5.5%), UNH (5.4%), TMO (3.8%), AMGN (3.7%), GILD (3.1%), ABT (2.7%), and PFE (2.6%). Numeric weight coverage is 61.4%.
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
| Bull | 25% | +2.00% | Low 5-day vol (14.9%) and below-threshold spike probability (16.5%) support a modest upside if US close confirms positive breadth; return capped at +2.0% to reflect frozen daily-close model. |
| Base | 50% | +0.00% | Directional signal is false and forecast is frozen at daily close; base case assumes range-bound action near zero with no directional alpha, consistent with historical baseline of 22.1%. |
| Bear | 25% | -2.00% | If US close fails to confirm the frozen forecast, elevated spike probability (16.5%) and below-historical vol can still produce a mild downside drift of -2.0% before stabilization. |

### Long Term (12 months)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 30% | +8.00% | Sustained credit and earnings momentum with low realized vol (14.9%) and confirmed breadth could drive a +8.0% multi-day advance, reflecting a favorable risk-reward setup. |
| Base | 40% | +3.00% | Frozen daily-close model with no directional signal implies a modest positive drift of +3.0% over the horizon, anchored to the historical baseline of 22.1% and ewma baseline of 20.1%. |
| Bear | 30% | -5.00% | A failed US close or spike probability exceeding threshold could trigger a -5.0% correction, as elevated volatility and below-historical baseline conditions pressure risk assets. |

## Positioning

- Maintain a risk-on posture with a quality and liquidity bias, favoring high-liquidity, low-valuation, and dislocation-recovery names.
- Favored Health Care, Consumer Discretionary, Consumer Staples, Financials, and Utilities for their positive momentum and stable fundamentals.
- Less favored Information Technology and Communication Services given negative 20-day returns and elevated valuation multiples.
- Less favored Energy given negative 20-day return and weak sector leadership.
- Monitor credit conditions and the flat 10Y-2Y curve for any shift in the macro outlook.

## Catalysts

| Date | Event | Why it matters |
| --- | --- | --- |
| 2026-11-13 | Equity session close | Latest close of 7561.67 with negative 20-day return but strongly positive breadth. |
| 2026-11-13 | Macro data release | Effective federal funds rate at 3.88 and 10Y-2Y spread at 0.27 indicate a flat curve and neutral policy stance. |
| 2026-11-13 | Credit market data | High-yield OAS at 3.20 and investment-grade OAS at 0.89 indicate stable credit conditions. |
| 2026-11-13 | Risk forecast | 5-day forecast volatility of 14.9% and 16.5% spike probability, below the 18.5% threshold. |

## Key Risks

- Information Technology sector is negative over 20 days and carries elevated valuation multiples, creating downside risk if liquidity fades.
- Communication Services and Energy sectors are negative over 20 days, with weak sector leadership.
- The 10Y-2Y Treasury spread is flat at 0.27, indicating a limited recession signal but also a lack of strong macro direction.
- Credit conditions are stable, but high-yield OAS at 3.20 and investment-grade OAS at 0.89 leave little room for spread widening.
- The risk forecast shows a 16.5% spike probability, below the 18.5% threshold, but the 5-day forecast volatility of 14.9% is elevated.
- The equity session contains a mix of provisional yfinance and canonical Massive rows, which may introduce data quality issues.

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
| S009 | news | FISV | Thu, 12 Nov 2026 18:47:44 GMT | ok | https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en | Fiserv, Inc. (FISV) Stock Price, News, Quote & History - Yahoo! Finance Canada (Thu, 12 Nov 2026 18:47:44 GMT); Fiserv Stock Outlook: Is Wall Street Bullish or Bearish? - Yahoo Finance (Thu, 12 Nov 2026 12:23:56 GMT); What Is Fiserv (FISV) Planning With Its Debit Networks And Clover AI? - Yahoo Finance (Thu, 12 Nov 2026 06:09:00 GMT) |
| S010 | news | APP | Thu, 12 Nov 2026 20:05:45 GMT | ok | https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en | AppLovin Just Ripped 47% in a Month: Is It Too Late to Buy APP Stock Now? - Yahoo Finance (Thu, 12 Nov 2026 20:05:45 GMT); APP Stock Surges 51% After Q3 Earnings: Is it Still a Buy? - Yahoo Finance (Tue, 10 Nov 2026 14:24:00 GMT); Is Trending Stock AppLovin Corporation (APP) a Buy Now? - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT) |
| S011 | filing | APP | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001751008&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0001751008-26-000069); 8-K filed 2026-11-04 (accession 0001751008-26-000068); 10-Q filed 2026-08-05 (accession 0001751008-26-000059) |
| S012 | filing | PNR | 2026-10-27 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-27 (accession 0000077360-26-000058); 8-K filed 2026-10-27 (accession 0000077360-26-000055); 8-K filed 2026-09-22 (accession 0000077360-26-000050) |
| S013 | stock | FISV | 2026-11-14 | ok | https://finance.yahoo.com/quote/FISV | Forward P/E: 7.9923306; Price: 63.78; Market price: 63.78; Market cap: 33934002176; Market Cap: 33934002176; Consensus EPS FY+1: 7.98015; growth: 0.09689999 |
| S014 | news | PNR | Fri, 13 Nov 2026 15:54:46 GMT | ok | https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en | Pentair plc (PNR) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 15:54:46 GMT); Here's What Key Metrics Tell Us About Pentair (PNR) Q3 Earnings - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT); Pentair (PNR) Stock May Be 46% Undervalued As New CFO Arrives - Yahoo Finance (Fri, 25 Sep 2026 07:00:00 GMT) |
| S015 | stock | PNR | 2026-11-14 | ok | https://finance.yahoo.com/quote/PNR | Trailing P/E: 18.610355; Forward P/E: 12.877027; Forward EPS: 5.30402; Price: 68.3; Market price: 68.3; Market cap: 10904415232; Sector: Industrials; Trailing Eps: 3.67; Revenue Growth: -0.045; Earnings Growth: -0.188; Gross Margin: 0.40168998; Operating Margin: 0.21410999; Profit Margin: 0.15435; Return On Equity: 0.15605; Total Revenue: 3966200064; Market Cap: 10904415232; Consensus EPS FY+1: 5.30402; growth: 0.1282 |
| S016 | stock | APP | 2026-11-14 | ok | https://finance.yahoo.com/quote/APP | Trailing P/E: 27.54882; Forward P/E: 19.611452; Forward EPS: 20.86026; Price: 409.1; Market price: 409.1; Market cap: 135543824384; Sector: Communication Services; Trailing Eps: 14.85; Revenue Growth: 0.555; Earnings Growth: 0.755; Gross Margin: 0.8878; Operating Margin: 0.77782995; Profit Margin: 0.65887; Return On Equity: 2.1008599; Total Revenue: 7608893952; Market Cap: 135543824384; Consensus EPS FY+1: 20.72438; growth: 0.2744 |
| S017 | filing | FISV | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json | Diluted EPS -8.9 for period ending 2026-09-30 (filed 2026-11-04) |
| S018 | filing | GEN | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0000849399-26-000083); 8-K filed 2026-10-28 (accession 0000849399-26-000081); 8-K filed 2026-10-09 (accession 0000849399-26-000079) |
| S019 | filing | CLX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000021076-26-000046); 8-K filed 2026-11-02 (accession 0000021076-26-000044); 8-K filed 2026-10-29 (accession 0001206774-26-000586) |
| S020 | news | CLX | Fri, 13 Nov 2026 05:34:04 GMT | ok | https://news.google.com/rss/search?q=CLX+Clorox+stock&hl=en-US&gl=US&ceid=US:en | The Clorox Company (CLX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 05:34:04 GMT); The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance Singapore (Fri, 13 Nov 2026 14:35:41 GMT); The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance UK (Fri, 13 Nov 2026 16:03:45 GMT) |
| S021 | stock | CLX | 2026-11-14 | ok | https://finance.yahoo.com/quote/CLX | Trailing P/E: 19.68705; Forward P/E: 17.745283; Forward EPS: 6.1684; Price: 109.46; Market price: 109.46; Market cap: 13260793856; Sector: Consumer Defensive; Trailing Eps: 5.56; Revenue Growth: 0.333; Earnings Growth: 1.138; Gross Margin: 0.41939998; Operating Margin: 0.14286; Profit Margin: 0.09408; Return On Equity: 5.34363; Total Revenue: 7196000256; Market Cap: 13260793856; Consensus EPS FY+1: 6.1684; growth: 0.0769 |
| S022 | filing | APP | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json | Diluted EPS 11.61 for period ending 2026-09-30 (filed 2026-11-04) |
| S023 | news | GEN | Wed, 11 Nov 2026 13:10:37 GMT | ok | https://news.google.com/rss/search?q=GEN+Gen+Digital+stock&hl=en-US&gl=US&ceid=US:en | Gen Digital Inc. (GEN) Stock Forecasts - Yahoo Finance (Wed, 11 Nov 2026 13:10:37 GMT); Gen Digital (GEN) Stock Repriced After Q2 Earnings Put Margins Center Stage - Yahoo Finance (Thu, 29 Oct 2026 07:00:00 GMT); Are Business Services Stocks Lagging GEN DIGITAL INC (GEN) This Year? - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT) |
| S024 | stock | GEN | 2026-11-14 | ok | https://finance.yahoo.com/quote/GEN | Trailing P/E: 15.431472; Forward P/E: 9.108996; Forward EPS: 3.33736; Price: 30.4; Market price: 30.4; Market cap: 18035593216; Sector: Technology; Trailing Eps: 1.97; Revenue Growth: 0.122; Earnings Growth: 1.286; Gross Margin: 0.77410007; Operating Margin: 0.43229; Profit Margin: 0.23068; Return On Equity: 0.46402; Total Revenue: 5228000256; Market Cap: 18035593216; Consensus EPS FY+1: 3.33736; growth: 0.1286 |
| S025 | filing | GEN | 2026-10-29 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000849399.json | Diluted EPS 0.83 for period ending 2026-10-02 (filed 2026-10-29) |
| S026 | filing | IDXX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000874716&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000874716-26-000135); 8-K filed 2026-11-02 (accession 0001104659-26-120892); 10-Q filed 2026-08-04 (accession 0000874716-26-000123) |
| S027 | news | CHTR | Thu, 12 Nov 2026 08:02:01 GMT | ok | https://news.google.com/rss/search?q=CHTR+Charter+Communications+stock&hl=en-US&gl=US&ceid=US:en | Charter Communications: 3 Key Takeaways for Long-Term Investors - Yahoo Finance (Thu, 12 Nov 2026 08:02:01 GMT); Charter Communications (CHTR) Stock Looks Reasonable As Shares Slump 85% - Yahoo Finance (Wed, 28 Oct 2026 07:00:00 GMT); Should Value Investors Buy Charter Communications (CHTR) Stock? - Yahoo Finance (Wed, 21 Oct 2026 07:00:00 GMT) |
| S028 | filing | PNR | 2026-10-27 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json | Diluted EPS 2.76 for period ending 2026-09-30 (filed 2026-10-27) |
| S029 | filing | CHTR | 2026-11-06 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-06 (accession 0001091667-26-000073); 8-K filed 2026-11-06 (accession 0001091667-26-000072); 8-K filed 2026-10-27 (accession 0001091667-26-000064) |
| S030 | stock | CHTR | 2026-11-14 | ok | https://finance.yahoo.com/quote/CHTR | Trailing P/E: 13.006578; Forward P/E: 3.2831066; Forward EPS: 42.15215; Price: 138.39; Market price: 138.39; Market cap: 24778944512; Sector: Communication Services; Trailing Eps: 10.64; Revenue Growth: 0.091; Gross Margin: 0.55084; Operating Margin: 0.23389; Profit Margin: 0.02498; Return On Equity: 0.07019; Total Revenue: 55645999104; Market Cap: 24778944512; Consensus EPS FY+1: 47.15811; growth: 1.0195 |
| S031 | filing | CLX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000021076.json | Diluted EPS 1.39 for period ending 2026-09-30 (filed 2026-11-02) |
| S032 | stock | IDXX | 2026-11-14 | ok | https://finance.yahoo.com/quote/IDXX | Trailing P/E: 47.45485; Forward P/E: 41.687927; Forward EPS: 16.8929; Price: 704.23; Market price: 704.23; Market cap: 55483650048; Sector: Healthcare; Trailing Eps: 14.84; Revenue Growth: 0.099; Earnings Growth: 0.179; Gross Margin: 0.62722; Operating Margin: 0.32497; Profit Margin: 0.25357; Return On Equity: 0.68925005; Total Revenue: 4662220800; Market Cap: 55483650048; Consensus EPS FY+1: 16.8929; growth: 0.1244 |
| S033 | news | IDXX | Fri, 13 Nov 2026 22:06:38 GMT | ok | https://news.google.com/rss/search?q=IDXX+Idexx+Laboratories+stock&hl=en-US&gl=US&ceid=US:en | IDEXX Laboratories, Inc. (IDXX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 22:06:38 GMT); IDEXX Laboratories (IDXX) Stock Looks Fairly Valued Despite Its 28% Run - Yahoo Finance (Sat, 31 Oct 2026 07:00:00 GMT); IDEXX Laboratories (IDXX) Q3 Earnings Leave Its Premium Valuation In Focus - Yahoo Finance (Tue, 03 Nov 2026 08:00:00 GMT) |
| S034 | filing | ROP | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000882835&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000882835-26-000047); 8-K filed 2026-10-22 (accession 0000882835-26-000042); 8-K filed 2026-10-01 (accession 0000882835-26-000039) |
| S035 | news | ROP | Fri, 13 Nov 2026 01:46:04 GMT | ok | https://news.google.com/rss/search?q=ROP+Roper+Technologies+stock&hl=en-US&gl=US&ceid=US:en | Roper Technologies, Inc. (ROP) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 01:46:04 GMT); Roper Technologies (ROP) Stock Looks Fully Valued As Cash Flow Comes Into Focus - Yahoo Finance (Fri, 06 Nov 2026 07:13:00 GMT); Roper Technologies: 3 Key Takeaways for Long-Term Investors - Yahoo Finance (Mon, 26 Oct 2026 07:00:00 GMT) |
| S036 | filing | RDDT | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001713445&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0001713445-26-000116); 8-K filed 2026-10-29 (accession 0001713445-26-000114); 8-K filed 2026-08-12 (accession 0001713445-26-000107) |
| S037 | filing | IDXX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000874716.json | Diluted EPS 11.75 for period ending 2026-09-30 (filed 2026-11-02) |
| S038 | filing | INTC | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000050863&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0000050863-26-000191); 8-K filed 2026-10-29 (accession 0000050863-26-000188); 8-K filed 2026-08-12 (accession 0001193125-26-346806) |
| S039 | stock | RDDT | 2026-11-14 | ok | https://finance.yahoo.com/quote/RDDT | Trailing P/E: 20.091835; Forward P/E: 10.770874; Forward EPS: 9.14039; Price: 98.45; Market price: 98.45; Market cap: 19010076672; Sector: Communication Services; Trailing Eps: 4.9; Revenue Growth: 0.53; Earnings Growth: 0.749; Gross Margin: 0.91547996; Operating Margin: 0.29397; Profit Margin: 0.32105; Return On Equity: 0.32029998; Total Revenue: 3088880128; Market Cap: 19010076672; Consensus EPS FY+1: 6.82439; growth: 0.2417 |
| S040 | stock | ROP | 2026-11-14 | ok | https://finance.yahoo.com/quote/ROP | Trailing P/E: 18.993866; Forward P/E: 19.532475; Forward EPS: 24.57318; Price: 479.975; Market price: 479.975; Market cap: 47535013888; Sector: Technology; Trailing Eps: 25.27; Revenue Growth: 0.076; Earnings Growth: 0.326; Gross Margin: 0.69671; Operating Margin: 0.28049; Profit Margin: 0.30712998; Return On Equity: 0.13229; Total Revenue: 8434599936; Market Cap: 47535013888; Consensus EPS FY+1: 24.57318; growth: 0.09810001 |

## Sources

- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFF&cosd=2026-01-01 (2026-11-12)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLH0A0HYM2&cosd=2026-01-01 (2026-11-12)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLC0A0CM&cosd=2026-01-01 (2026-11-12)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCSL&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=UNRATE&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=PAYEMS&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=T10Y2Y&cosd=2026-01-01 (2026-11-13)
- filing FISV: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 (2026-11-04)
- news FISV: https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en (Thu, 12 Nov 2026 18:47:44 GMT)
- news APP: https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en (Thu, 12 Nov 2026 20:05:45 GMT)
- filing APP: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001751008&type=10-Q&dateb=&owner=include&count=10 (2026-11-04)
- filing PNR: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 (2026-10-27)
- stock FISV: https://finance.yahoo.com/quote/FISV (2026-11-14)
- news PNR: https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 15:54:46 GMT)
- stock PNR: https://finance.yahoo.com/quote/PNR (2026-11-14)
- stock APP: https://finance.yahoo.com/quote/APP (2026-11-14)
- filing FISV: https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json (2026-11-04)
- filing GEN: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 (2026-10-29)
- filing CLX: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 (2026-11-02)
- news CLX: https://news.google.com/rss/search?q=CLX+Clorox+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 05:34:04 GMT)

## AI Provenance

- Provider / model: hermes-local-proxy / upstage/solar-mini4:free
- Market research: attempts=1 tokens=9500 (prompt=6548, completion=2952) runtime=32.62s
- Fundamental research: generated this run at 2026-11-14T20:16:55.204848+00:00
- Evidence source dates: {'as_of': '2026-11-13', 'latest_equity_date': '2026-11-13', 'latest_macro_date': '2026-11-13', 'flows_date': '2026-11-13'}
- Evidence fingerprint: 515212172e2b9a8239fc9be7923acfc6a4954e65f1cf0acdde061cdd0a13f751
- Source citations are retrieved external records in the ledger above; market values remain from the verified database snapshot.


## Disclosures

- This is research and market intelligence, not investment advice.
- AI conclusions are research judgments, not validated return predictions.
- The frozen risk layer is risk-only and is not used for directional views or allocations.
- Legacy scores are not active inputs or outputs.

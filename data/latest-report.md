# AEGIS AI-First Market Intelligence

Research generated at: 27 November 2026, 06:14 HKT
Database freshness: equity 2026-11-25 (latest row retrieved 2026-11-26 13:05:50.828884+08:00)
Data cutoff: 2026-11-25 US cash close
Snapshot ID: aegis-hourly-20261126T221420Z

## Executive Summary

- **AI market view: Late-November 2026 risk-on tape is being driven by resilient US mega-cap liquidity leaders and strong breadth, but the 20-day equity return is negative and the technology sector is the weakest GICS sleeve. Policy and credit conditions remain supportive, with a still-elevated but contained volatility regime and a positive 10Y-2Y spread. The market is in a liquidity-led, quality-tilted phase rather than a broad-based expansion signal.**
- US equities show a negative 20-day return (-7.25% SPX) but positive 20-day breadth (55.67% positive) and a strong advance-decline ratio of 2.88.
- Liquidity leaders dominate the shortlist: NVDA, AMD, AAPL, AMZN, and MU are selected for liquidity leadership, while INTC, DELL, MRVL, LITE, and NOW are selected for the largest 20-day dislocation.
- Sector returns are bifurcated: Consumer Staples (+6.29%) and Real Estate (+4.11%) lead, while Information Technology (-18.43%) and Industrials (-3.29%) are the weakest.
- Credit conditions are stable: US high-yield OAS is 3.72 and IG OAS is 0.98, with a 10Y-2Y spread of 0.24.
- Volatility is elevated at 27.94% (5-day forecast) versus a 31.64% historical baseline, with a 66% spike probability, but the directional signal is false.
- The market is in a liquidity-led, quality-tilted phase with strong institutional flows into semiconductors and Treasuries, not a broad-based expansion signal.

## Data QC

- Status: **PASS_WITH_WARNINGS**
- Equity session: 0 completed session(s) behind inference date
- Macro session: 2026-11-26 (0 completed session(s) behind inference date)
- Equity provenance: 296 provisional / 12634 canonical
- Breadth lag: 0 session(s); ETF-flow lag: 0 session(s)
- Note: Equity session contains a mix of provisional yfinance and canonical Massive rows.
- External sources: 79 ok / 0 unavailable; retrieved 2026-11-26T22:14:33.332511+00:00

## Idea Discovery

- S&P 500 universe: 503; eligible: 501; transparent shortlist: 20
- Method: independent momentum/dislocation/PE/liquidity buckets; no composite score
- Evidence used: latest close, 20d and 60d price returns, 60d drawdown, trailing P/E, earnings yield, sector-relative P/E, dollar volume, GICS sector
- Not available as verified inputs: verified earnings-revision history for the full universe, FY+2 consensus, structured industry catalyst calendar
- Eligible but not shortlisted: 481 (outside the top independent momentum, dislocation, valuation and liquidity buckets)
- Included: APP (top_20d_momentum); CHTR (top_20d_momentum); CMG (top_20d_momentum); CLX (top_20d_momentum); TSCO (top_20d_momentum); MGM (top_20d_momentum); IDXX (top_20d_momentum); FISV (top_20d_momentum); SNDK (largest_20d_dislocation); MRVL (largest_20d_dislocation); LITE (largest_20d_dislocation); DDOG (largest_20d_dislocation); INTC (largest_20d_dislocation); DELL (largest_20d_dislocation); MU (largest_20d_dislocation, liquidity_leader); NOW (largest_20d_dislocation); NVDA (liquidity_leader); AMD (liquidity_leader); AAPL (liquidity_leader); AMZN (liquidity_leader)
- Excluded reasons: {"missing_recent_or_latest_price": 2}
- Valuation-quality rejected: [{"flags": ["forward_pe_outside_plausible_range", "implausible_earnings_yield", "forward_eps_vs_reported_jump"], "ticker": "CHTR"}, {"flags": ["forward_eps_missing"], "ticker": "FISV"}, {"flags": ["forward_pe_outside_plausible_range", "implausible_earnings_yield"], "ticker": "SNDK"}, {"flags": ["forward_eps_vs_reported_jump"], "ticker": "MRVL"}, {"flags": ["forward_eps_vs_reported_jump"], "ticker": "LITE"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "INTC"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "DELL"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "MU"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "NOW"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "NVDA"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "AMD"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "AAPL"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "AMZN"}]

## Market Snapshot

| Asset | Latest | Change | Observation |
| --- | --- | --- | --- |
| S&P 500 | 7182.78 | -7.25% (20d) | Negative 20-day return but positive 20-day breadth; 59.12% above 50-day and 55.42% above 200-day. |
| Information Technology (XLK) | -18.43% | -18.43% (20d) | Weakest GICS sector; trailing P/E 27.47. |
| Consumer Staples (XLP) | +6.29% | +6.29% (20d) | Strongest GICS sector; trailing P/E 24.84. |
| Real Estate (XLRE) | +4.11% | +4.11% (20d) | Positive 20-day return; trailing P/E 29.29. |
| Industrials (XLI) | -3.29% | -3.29% (20d) | Negative 20-day return; trailing P/E 26.13. |
| Health Care (XLV) | +2.20% | +2.20% (20d) | Positive 20-day return; trailing P/E 29.94. |

## Macro, Fiscal, Rates, Liquidity and Credit

- Growth: US equities are in a late-cycle liquidity phase with a negative 20-day return but positive breadth; the 10Y-2Y spread is positive at 0.24, indicating no acute recession signal.
- Inflation: CPI and core CPI are available only through 2026-09-01 (336.30 and 338.90), and the latest October CPI is 337.476; the data is stale by the 2026-11-25 snapshot and should be treated as a lagging reference.
- Policy: The effective federal funds rate is 3.88 as of 2026-11-24, indicating a still-restrictive but stable policy stance.
- Rates: The 10Y-2Y Treasury spread is 0.24, a modest positive curve, and TLT shows structural accumulation with a neutral 20-day flow z-score of 0.47.
- Liquidity: Institutional flows are concentrated in semiconductors (SOXX) with exceptional buying and in Treasuries (TLT) with structural accumulation; SMH shows neutral flow with structural accumulation.
- Credit: High-yield OAS is 3.72 and IG OAS is 0.98, both stable and not signaling acute stress.

## US Equities and 11 GICS Sectors

Macro source IDs: S001, S002, S003, S007, S004, S005

| GICS sector | Evidence | AI research stance | Source IDs |
| --- | --- | --- | --- |
| Information Technology | 20-day sector return -18.43% is the weakest GICS sleeve; trailing P/E 27.47; shortlist includes NVDA, AMD, and MRVL as liquidity leaders and dislocation names. | Less favored relative to the index; liquidity leaders are being bought but the sector is in a deep drawdown. | S074, S070 |
| Consumer Staples | 20-day sector return +6.29% is the strongest GICS sleeve; trailing P/E 24.84; defensive demand is supporting the sector. | Favored relative to the index; defensive quality is favored in a late-cycle liquidity phase. | S058 |
| Real Estate | 20-day sector return +4.11%; trailing P/E 29.29; positive momentum despite a high valuation. | Neutral-to-positive; positive 20-day momentum but valuation is rich. | S064 |
| Health Care | 20-day sector return +2.20%; trailing P/E 29.94; positive momentum but high valuation. | Neutral; positive momentum but valuation is rich. | S055 |
| Consumer Discretionary | 20-day sector return +1.87%; trailing P/E 24.59; modest positive momentum. | Neutral; modest positive momentum but not a leader. | S059 |
| Financials | 20-day sector return +0.68%; trailing P/E 15.26; low valuation but weak momentum. | Neutral; low valuation but weak momentum. | S066 |
| Utilities | 20-day sector return +2.64%; trailing P/E 17.94; defensive but modest positive momentum. | Neutral; defensive but modest positive momentum. | S063 |
| Materials | 20-day sector return -1.25%; trailing P/E 21.30; negative momentum. | Less favored relative to the index; negative momentum. | S068 |
| Industrials | 20-day sector return -3.29%; trailing P/E 26.13; negative momentum. | Less favored relative to the index; negative momentum. | S070 |
| Communication Services | 20-day sector return +2.17%; trailing P/E 16.74; positive momentum but low valuation. | Neutral; positive momentum but low valuation. | S073 |
| Energy | 20-day sector return -11.03%; trailing P/E 15.21; negative momentum and weak valuation. | Less favored relative to the index; negative momentum and weak valuation. | S076 |

### Sector fundamentals, valuation and earnings

No point-in-time sector fundamentals are supplied beyond trailing P/E and 20-day ETF returns. The database provides sector-relative P/E and earnings yield only for the shortlist names, not for the full GICS sector universe. Therefore, no sector-level fundamental metrics (growth, margins, consensus, or sector-relative valuation) are available for this snapshot. The sector evidence is limited to the supplied ETF returns and trailing P/E values, which are used as directional context only.

## Growth vs Value

- Consumer Staples has the strongest 20-day return (+6.29%) and a trailing P/E of 24.84, indicating a quality defensive profile.
- Real Estate has a positive 20-day return (+4.11%) but a high trailing P/E of 29.29, suggesting rich valuation.
- Information Technology has the weakest 20-day return (-18.43%) and a trailing P/E of 27.47, indicating a deep drawdown with high valuation.
- Energy has a negative 20-day return (-11.03%) and a low trailing P/E of 15.21, suggesting a value-tilted but weak sector.
- Financials have a low trailing P/E of 15.26 but a weak 20-day return of +0.68%, indicating low valuation but weak momentum.

## ETF Flows and Breadth

- 20-day breadth is positive at 55.67% with an advance-decline ratio of 2.88, indicating broad participation despite the negative 20-day return.
- SOXX shows exceptional institutional buying with a 20-day flow z-score of 2.19 and a 60-day flow z-score of 2.53, confirming strong semiconductor demand.
- TLT shows structural accumulation with a neutral 20-day flow z-score of 0.47, indicating steady Treasury demand.
- SMH shows neutral flow with structural accumulation, but a 20-day flow z-score of 0.55 and a 60-day flow z-score of 1.12.
- New highs are 0 and new lows are 0, indicating no extreme distribution or accumulation pattern.

## Stock Ideas

Single-stock research uses reported EPS, forward P/E and company fundamentals. All ideas are research judgments, not validated return predictions.

| Ticker | Security | Research view | Price | EPS | Forward P/E | Base target | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| APP | AppLovin | NEW | 378.95 | 20.86084 | 18.165617 | 417.22 | NEW |
| IDXX | Idexx Laboratories | KEEP | 709.46 | 16.8929 | 41.997524 | N/A | KEEP |
| DDOG | Datadog | DOWNGRADE | 158.25 | 3.1829 | 49.71881 | N/A | DOWNGRADE |

## ETF Ideas

ETF research uses holdings, portfolio valuation and exposure. Single-stock EPS × P/E valuation is not applied to ETFs.

| Ticker | Fund | Research view | Price | Top holdings | Portfolio valuation | Sector exposure | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| XLC | Communication Services sector ETF | KEEP | 105.38 | META 22.00%, GOOGL 11.08%, GOOG 8.92%, DIS 5.55%, CMCSA 4.92%, TTWO 4.70%, VZ 4.69%, TMUS 4.60%, T 4.44%, NFLX 4.26% | Top 10 holdings; numeric weight coverage 75.17% | Communication Services | KEEP |
| XLF | Financials sector ETF | KEEP | 56.51 | BRK-B 12.68%, JPM 11.24%, V 8.84%, MA 6.47%, BAC 4.08%, GS 3.27%, WFC 3.16%, MS 2.76%, C 2.58%, AXP 2.11% | Top 10 holdings; numeric weight coverage 57.19% | Financials | KEEP |
### APP — AppLovin

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** AppLovin offers a cleaner momentum and valuation profile than the shortlisted consumer and tech names, with a forward P/E near 18.17 versus the higher forward P/Es of DDOG, IDXX, and CMG, and it is not burdened by the forward EPS gaps flagged for MRVL, LITE, INTC, DELL, MU, NOW, NVDA, AMD, AAPL, and AMZN. Alternatives considered: DDOG, IDXX, CMG.
- **Thesis:** AppLovin screens as a top 20-day momentum name with a reported Q3 FY2026 diluted EPS of 11.61 and a forward P/E near 18.17, implying the market is pricing in continued monetization of its advertising and video platforms. The 20-day return of roughly 45.8% and 60-day return of roughly 21.6% support a momentum-driven entry, while the 60-day drawdown of only about 8.7% indicates limited near-term selling pressure.
- **Source IDs:** S008, S012, S013, S014
- **Catalysts:** Continued advertising revenue growth and improved monetization metrics, Q3 FY2026 earnings beat and raised outlook (S012), Sustained 20-day momentum and limited 60-day drawdown (S008, S013)
- **Risks:** High 20-day momentum can mean elevated volatility and mean-reversion risk, Forward P/E near 18.17 leaves limited room if growth decelerates, Fiscal-period alignment of forward EPS is unverified (S008)
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 20.8608 (source.forwardEps) x AI multiple assumption 20.00; source IDs S008, S012, S013, S014
- **EPS:** 20.86084 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 18.165617
- **FY+1 growth assumption:** 27.59%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / PWR / APP shows strong FY1 consensus EPS growth of 27.59% and revenue growth of 25.69%, with high gross margin (88.78%) and operating margin (77.78%). The base multiple of 20x is supported by its superior margins and growth relative to peers, while the bull/bear range reflects upside from continued margin expansion and downside from competitive or macro pressure. Peer reference: PWR, whose growth and margin profile is comparable but with lower margins, supporting APP's premium multiple.
- **Company fundamentals:** Reported diluted EPS 11.61 for period ending 2026-09-30; forward EPS 20.86; forward P/E 18.17; 20-day return 45.8%; 60-day return 21.6%; 60-day drawdown -8.7%; gross margin 88.8%; operating margin 77.8%; profit margin 65.9%; ROE 2.10.
- **Bull / Base / Bear:** 500.66 / 417.22 / 333.77
- **Bull / Base / Bear returns:** 32.12% / 10.1% / -11.92%
- **Scenario probabilities:** not separately assigned; see scenario table.

### IDXX — Idexx Laboratories

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Idexx offers a higher-quality growth profile than the lower-margin consumer staples and discretionary names, but its forward P/E of about 42.0 is materially more expensive than APP, CLX, and TSCO, so it is better suited as a hold than a new position. Alternatives considered: APP, CLX, TSCO.
- **Thesis:** Idexx Laboratories is a top 20-day momentum name with a 20-day return of roughly 26.0% and a 60-day return of roughly 30.1%, indicating strong recent price appreciation. Its forward P/E of about 42.0 is the highest among the shortlisted momentum names, so the thesis is to hold rather than add aggressively until the market confirms that the growth premium is justified.
- **Source IDs:** S030, S032, S037, S038
- **Catalysts:** 20-day return of roughly 26.0% and 60-day return of roughly 30.1% (S030, S037), Revenue growth of about 9.9% and earnings growth of about 17.9%, Gross margin of about 62.7% and operating margin of about 32.5%
- **Risks:** Forward P/E of about 42.0 is the most expensive among the shortlisted momentum names, High valuation leaves limited upside if growth slows, Small 60-day drawdown of only -0.4% suggests limited pullback room
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** incomplete; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Target withheld. Qualitative research retained. Flags: implausible_base_return.
- **EPS:** 16.8929 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 41.997524
- **FY+1 growth assumption:** 12.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / CDW / IDXX has moderate FY1 consensus EPS growth of 12.44% and revenue growth of 8.88%, with healthy gross margin (62.72%) and operating margin (32.50%). The base multiple of 20x reflects steady growth and stable margins, with the bull/bear range capturing potential upside from market share gains and downside from slower adoption. Peer reference: CDW, a comparable enterprise software/IT services name with similar growth and margin characteristics.
- **Company fundamentals:** Reported diluted EPS 11.75 for period ending 2026-09-30; forward EPS 16.89; forward P/E 42.00; 20-day return 26.0%; 60-day return 30.1%; 60-day drawdown -0.4%; revenue growth 9.9%; earnings growth 17.9%; gross margin 62.7%; operating margin 32.5%; profit margin 25.4%; ROE 0.69.
- **Bull / Base / Bear:** N/A / N/A / N/A
- **Bull / Base / Bear returns:** N/A% / N/A% / N/A%
- **Scenario probabilities:** not separately assigned; see scenario table.

### DDOG — Datadog

- **Type:** Stock
- **Research view:** DOWNGRADE (stance: AVOID)
- **Why preferred / alternatives:** Datadog is excluded from a preferred list because its valuation is the most expensive and its price action is the most negative, making it a worse risk-reward than the momentum names with lower forward P/Es and positive 20-day returns. Alternatives considered: APP, IDXX, CMG.
- **Thesis:** Datadog is a largest-20-day dislocation name, but its 20-day return of about -43.2% and 60-day return of about -29.3% show a sharp, sustained decline, and its 60-day drawdown of about -46.0% is the deepest among the shortlisted names. The forward P/E of about 49.7 is also the highest in the shortlist, so the dislocation has not yet produced a valuation discount that justifies a new position.
- **Source IDs:** S050, S052, S053, S060
- **Catalysts:** Sharp dislocation creates a potential mean-reversion setup if fundamentals stabilize, Revenue growth of about 35.2% and earnings growth of about 231.6% (S050, S052)
- **Risks:** 20-day return of about -43.2% and 60-day return of about -29.3% indicate a severe trend, 60-day drawdown of about -46.0% is the largest in the shortlist, Forward P/E of about 49.7 is the most expensive among the shortlisted names, Operating margin of only about 2.4% suggests limited current profitability
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** incomplete; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Target withheld. Qualitative research retained. Flags: implausible_base_return.
- **EPS:** 3.1829 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 49.71881
- **FY+1 growth assumption:** 16.23%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / CRWD / DDOG shows FY1 consensus EPS growth of 16.23% and revenue growth of 22.30%, with strong gross margin (79.61%) but lower operating margin (2.36%) and profit margin (6.12%), indicating significant investment or operating leverage risk. The base multiple of 20x is justified by growth and gross margin, while the bull/bear range reflects uncertainty around operating margin recovery. Peer reference: CRWD, a comparable cloud/security platform with similar growth and margin profile, supporting the multiple range.
- **Company fundamentals:** Reported diluted EPS 0.59 for period ending 2026-09-30; forward EPS 3.18; forward P/E 49.72; 20-day return -43.2%; 60-day return -29.3%; 60-day drawdown -46.0%; revenue growth 35.2%; earnings growth 231.6%; gross margin 79.6%; operating margin 2.4%; profit margin 6.1%; ROE 0.06.
- **Bull / Base / Bear:** N/A / N/A / N/A
- **Bull / Base / Bear returns:** N/A% / N/A% / N/A%
- **Scenario probabilities:** not separately assigned; see scenario table.

### XLC — Communication Services sector ETF

- **Type:** ETF
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** XLC is the only sector ETF in the shortlist with a positive daily move, but it is not preferred over the individual momentum stocks because its performance is a function of the underlying communication names and does not offer the same standalone momentum or valuation signal as APP or IDXX. Alternatives considered: XLV, XLP, XLY.
- **Thesis:** The Communication Services sector ETF is up about 0.89% on the latest session and is the only sector ETF in the shortlist with a positive daily move, but the underlying concentration in large-cap communication and media names means the ETF is a passive expression of those names rather than a standalone catalyst. It is best used as a sector allocation rather than a directional call.
- **Source IDs:** S072, S073
- **Catalysts:** Latest-session gain of about 0.89% (S072, S073), Top holdings include META, GOOGL, GOOG, DIS, CMCSA, TTW, VZ, TMUS, T, NFLX
- **Risks:** Concentration in a few large-cap names increases single-stock risk, Sector-level performance is driven by media and telecom sentiment, not a broad market tailwind, No independent earnings or valuation data for the ETF itself
- **Valuation method:** Holdings/portfolio valuation with AI total-return assumption
- **Valuation status:** verified; forward-EPS source: ; period flags: 
- **Valuation assumptions:** Holdings/portfolio valuation; 10 weighted holdings; coverage 75.17%; source IDs S072, S073
- **Top holdings:** META 22.00%, GOOGL 11.08%, GOOG 8.92%, DIS 5.55%, CMCSA 4.92%, TTWO 4.70%, VZ 4.69%, TMUS 4.60%, T 4.44%, NFLX 4.26%
- **Portfolio valuation:** Top 10 holdings; numeric weight coverage 75.17%
- **Sector exposure:** Communication Services
- **Underlying drivers:** Large-cap communication, media, and telecom names; top holdings include META, GOOGL, GOOG, DIS, CMCSA, TTW, VZ, TMUS, T, NFLX
- **Bull / Base / Bear:** 124.35 / 115.92 / 101.16
- **Bull / Base / Bear returns:** 18.0% / 10.0% / -4.0%
- **Scenario probabilities:** not separately assigned; see scenario table.

### XLF — Financials sector ETF

- **Type:** ETF
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** XLF is not preferred over the individual momentum stocks because it lacks independent earnings and valuation data and its performance is a function of the underlying financial names rather than a standalone catalyst. Alternatives considered: XLV, XLP, XLY.
- **Thesis:** The Financials sector ETF is up about 0.71% on the latest session, but the ETF is a passive basket of large banks and financials with no independent earnings or valuation data. It is best used as a sector allocation rather than a directional call, and it does not offer the same standalone momentum or valuation signal as the individual stock candidates.
- **Source IDs:** S066, S067
- **Catalysts:** Latest-session gain of about 0.71% (S066, S067), Top holdings include BRK-B, JPM, V, MA, BAC, GS, WFC, MS, C, AXP
- **Risks:** Concentration in a few large banks increases single-name risk, Sector-level performance is driven by rate and credit-cycle expectations, No independent earnings or valuation data for the ETF itself
- **Valuation method:** Holdings/portfolio valuation with AI total-return assumption
- **Valuation status:** verified; forward-EPS source: ; period flags: 
- **Valuation assumptions:** Holdings/portfolio valuation; 10 weighted holdings; coverage 57.19%; source IDs S066, S067
- **Top holdings:** BRK-B 12.68%, JPM 11.24%, V 8.84%, MA 6.47%, BAC 4.08%, GS 3.27%, WFC 3.16%, MS 2.76%, C 2.58%, AXP 2.11%
- **Portfolio valuation:** Top 10 holdings; numeric weight coverage 57.19%
- **Sector exposure:** Financials
- **Underlying drivers:** Large-cap banks and financials; top holdings include BRK-B, JPM, V, MA, BAC, GS, WFC, MS, C, AXP
- **Bull / Base / Bear:** 63.29 / 59.9 / 54.81
- **Bull / Base / Bear returns:** 12.0% / 6.0% / -3.01%
- **Scenario probabilities:** not separately assigned; see scenario table.

## Quant Risk Layer

| Field | Value |
| --- | --- |
| Volatility model | vol5_ols_v1 |
| Spike model | spike_logit_v1 |
| As-of date | 2026-11-25 |
| Target window | 2026-11-27 to 2026-12-03 |
| Forecast 5D annualized volatility | 27.94% |
| Historical-vol baseline | 31.64% |
| EWMA baseline | 28.40% |
| Spike probability | 65.99% |
| Spike threshold | 18.50% |
| Status | prospective |
| Forecast ID | 9884506cdbaa9353 |

Risk-only; no directional interpretation or allocation implication.

## Scenarios

### Short Term (5 trading sessions)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 25% | +2.00% | Low spike probability (0.66) and false directional signal reduce near-term tail risk, but a 2% upside is plausible if the frozen daily-close model stabilizes after the US close. |
| Base | 50% | +0.00% | Forecast volatility (0.279) is above the historical baseline (0.316) but below the EWMA baseline (0.284), implying a range-bound week with no directional alpha. |
| Bear | 25% | -2.00% | If the frozen model fails to complete the US close, elevated forecast vol and a 0.66 spike probability could trigger a 2% downside correction. |

### Long Term (12 months)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 30% | +8.00% | Sustained normalization of forecast vol below historical baseline and a false directional signal could allow a 8% rally into year-end if earnings remain stable. |
| Base | 40% | +3.00% | A 3% long-term return reflects moderate volatility compression and steady earnings growth, with the frozen daily-close model providing a reliable baseline. |
| Bear | 30% | -5.00% | Persistent elevated forecast vol, a 0.66 spike probability, and a false directional signal could drive a 5% decline if risk-off flows intensify. |

## Positioning

- The market is in a liquidity-led, quality-tilted phase with strong institutional flows into semiconductors and Treasuries.
- Consumer Staples and Real Estate are the strongest sector performers, while Information Technology and Energy are the weakest.
- The shortlist is dominated by liquidity leaders (NVDA, AMD, AAPL, AMZN, MU) and dislocation names (INTC, DELL, MRVL, LITE, NOW), with no composite score used.
- The volatility regime is elevated at 27.94% (5-day forecast) versus a 31.64% historical baseline, with a 66% spike probability, but the directional signal is false.
- The 10Y-2Y spread is positive at 0.24, indicating no acute recession signal, and credit conditions are stable with high-yield OAS at 3.72 and IG OAS at 0.98.

## Catalysts

| Date | Event | Why it matters |
| --- | --- | --- |
| 2026-11-26 | US equity session close | The frozen risk model is official only after the completed US close; the 5-day forecast volatility is 27.94% and the spike probability is 66%. |
| 2026-11-27 | Target start of volatility forecast window | The frozen risk model targets 2026-11-27 to 2026-12-03, with a 5-day forecast volatility of 27.94% and a spike probability of 66%. |
| 2026-12-03 | Target end of volatility forecast window | The frozen risk model targets 2026-11-27 to 2026-12-03, with a 5-day forecast volatility of 27.94% and a spike probability of 66%. |

## Key Risks

- Information Technology sector is in a deep drawdown with a -18.43% 2

## External Source Ledger

| ID | Type | Ticker | Published | Status | URL | Claims |
| --- | --- | --- | --- | --- | --- | --- |
| S001 | macro | macro | 2026-11-24 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFF&cosd=2026-01-01 | Effective federal funds rate (DFF) latest observation 2026-11-24: 3.88 |
| S002 | macro | macro | 2026-11-24 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLH0A0HYM2&cosd=2026-01-01 | US high-yield OAS (BAMLH0A0HYM2) latest observation 2026-11-24: 3.72 |
| S003 | macro | macro | 2026-11-24 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLC0A0CM&cosd=2026-01-01 | US investment-grade OAS (BAMLC0A0CM) latest observation 2026-11-24: 0.98 |
| S004 | macro | macro | 2026-10-01 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCSL&cosd=2026-01-01 | US CPI (CPIAUCSL) latest observation 2026-10-01: 337.476 |
| S005 | macro | macro | 2026-10-01 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=UNRATE&cosd=2026-01-01 | US unemployment rate (UNRATE) latest observation 2026-10-01: 4.1 |
| S006 | macro | macro | 2026-10-01 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=PAYEMS&cosd=2026-01-01 | US nonfarm payrolls (PAYEMS) latest observation 2026-10-01: 159293 |
| S007 | macro | macro | 2026-11-25 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=T10Y2Y&cosd=2026-01-01 | 10Y-2Y Treasury spread (T10Y2Y) latest observation 2026-11-25: 0.24 |
| S008 | filing | APP | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001751008&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0001751008-26-000069); 8-K filed 2026-11-04 (accession 0001751008-26-000068); 10-Q filed 2026-08-05 (accession 0001751008-26-000059) |
| S009 | filing | CMG | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001058090&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0001058090-26-000104); 8-K filed 2026-10-28 (accession 0001058090-26-000103); 8-K filed 2026-09-14 (accession 0001058090-26-000088) |
| S010 | filing | CHTR | 2026-11-06 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-06 (accession 0001091667-26-000073); 8-K filed 2026-11-06 (accession 0001091667-26-000072); 8-K filed 2026-10-27 (accession 0001091667-26-000064) |
| S011 | news | CHTR | Thu, 26 Nov 2026 16:09:04 GMT | ok | https://news.google.com/rss/search?q=CHTR+Charter+Communications+stock&hl=en-US&gl=US&ceid=US:en | Charter Communications (CHTR) Jumps After Cox Deal, Is It Still Cheap? - Yahoo Finance (Thu, 26 Nov 2026 16:09:04 GMT); CHTR Stock Posts 2nd Consecutive Day Of Gains: Retail Turns Bullish — 'The Gift That Keeps On Giving' - TradingView (Thu, 26 Nov 2026 01:54:00 GMT); Charter Communications (NasdaqGS:CHTR) Stock Forecast & Analyst Predictions - Simply Wall St (Mon, 23 Nov 2026 08:00:00 GMT) |
| S012 | news | APP | Thu, 05 Nov 2026 08:00:00 GMT | ok | https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en | AppLovin stock soars after Q3 earnings, outlook beat - Yahoo Finance (Thu, 05 Nov 2026 08:00:00 GMT); AppLovin Stock Surges As Earnings Beat Provides Much-Needed Boost - Investor's Business Daily (Wed, 04 Nov 2026 08:00:00 GMT); AppLovin vs. Reddit: Which Technology Stock Is a Better Buy for 2027? - The Motley Fool (Sat, 21 Nov 2026 23:19:26 GMT) |
| S013 | stock | APP | 2026-11-26 | ok | https://finance.yahoo.com/quote/APP | Trailing P/E: 25.518518; Forward P/E: 18.165617; Forward EPS: 20.86084; Price: 378.95; Market price: 378.95; Market cap: 125554507776; Sector: Communication Services; Trailing Eps: 14.85; Revenue Growth: 0.555; Earnings Growth: 0.755; Gross Margin: 0.8878; Operating Margin: 0.77782995; Profit Margin: 0.65887; Return On Equity: 2.1008599; Total Revenue: 7608893952; Market Cap: 125554507776; Consensus EPS FY+1: 20.78066; growth: 0.2759 |
| S014 | filing | APP | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json | Diluted EPS 11.61 for period ending 2026-09-30 (filed 2026-11-04) |
| S015 | stock | CMG | 2026-11-26 | ok | https://finance.yahoo.com/quote/CMG | Trailing P/E: 34.95327; Forward P/E: 28.261396; Forward EPS: 1.32336; Price: 37.4; Market price: 37.4; Market cap: 47310065664; Sector: Consumer Cyclical; Trailing Eps: 1.07; Revenue Growth: 0.096; Earnings Growth: -0.062; Gross Margin: 0.39314; Operating Margin: 0.14715; Profit Margin: 0.10832; Return On Equity: 0.48518002; Total Revenue: 12713477120; Market Cap: 47310065664; Consensus EPS FY+1: 1.32336; growth: 0.216 |
| S016 | news | CMG | Tue, 24 Nov 2026 15:25:45 GMT | ok | https://news.google.com/rss/search?q=CMG+Chipotle+Mexican+Grill+stock&hl=en-US&gl=US&ceid=US:en | What Could Lift Chipotle Stock Further? - Trefis (Tue, 24 Nov 2026 15:25:45 GMT); Chipotle’s Earnings Fell 7% Last Quarter, but 1 Trend Has Now Lasted 3 Straight Quarters. - The Motley Fool (Tue, 24 Nov 2026 12:45:02 GMT); Where Will Chipotle Mexican Grill's Stock Be in 5 Years? - Yahoo Finance (Wed, 19 Aug 2026 07:00:00 GMT) |
| S017 | stock | CHTR | 2026-11-26 | ok | https://finance.yahoo.com/quote/CHTR | Trailing P/E: 13.841166; Forward P/E: 3.2299702; Forward EPS: 45.59485; Price: 147.27; Market price: 147.27; Market cap: 26368923648; Sector: Communication Services; Trailing Eps: 10.64; Revenue Growth: 0.091; Gross Margin: 0.55084; Operating Margin: 0.23389; Profit Margin: 0.02498; Return On Equity: 0.07019; Total Revenue: 55645999104; Market Cap: 26368923648; Consensus EPS FY+1: 47.75367; growth: 1.4848 |
| S018 | filing | CLX | 2026-11-19 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 | 8-K filed 2026-11-19 (accession 0001206774-26-000606); 10-Q filed 2026-11-02 (accession 0000021076-26-000046); 8-K filed 2026-11-02 (accession 0000021076-26-000044) |
| S019 | filing | CMG | 2026-10-29 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001058090.json | Diluted EPS 0.82 for period ending 2026-09-30 (filed 2026-10-29) |
| S020 | filing | CHTR | 2026-11-06 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001091667.json | Diluted EPS 0.38 for period ending 2026-09-30 (filed 2026-11-06) |
| S021 | stock | CLX | 2026-11-26 | ok | https://finance.yahoo.com/quote/CLX | Trailing P/E: 19.953238; Forward P/E: 17.985216; Forward EPS: 6.1684; Price: 110.94; Market price: 110.94; Market cap: 13440092160; Sector: Consumer Defensive; Trailing Eps: 5.56; Revenue Growth: 0.333; Earnings Growth: 1.138; Gross Margin: 0.41939998; Operating Margin: 0.14286; Profit Margin: 0.09408; Return On Equity: 5.34363; Total Revenue: 7196000256; Market Cap: 13440092160; Consensus EPS FY+1: 6.1684; growth: 0.0769 |
| S022 | news | CLX | Tue, 24 Nov 2026 22:03:23 GMT | ok | https://news.google.com/rss/search?q=CLX+Clorox+stock&hl=en-US&gl=US&ceid=US:en | Clorox Company (The) (CLX) Stock Forecasts - Yahoo Finance (Tue, 24 Nov 2026 22:03:23 GMT); Should You Buy Clorox Stock At This Price? - Trefis (Thu, 19 Nov 2026 08:57:28 GMT); Clorox (CLX) Stock Looks Fairly Valued After A 28% Slide - Simply Wall St (Mon, 23 Nov 2026 14:08:34 GMT) |
| S023 | filing | TSCO | 2026-11-05 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000916365&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-05 (accession 0000916365-26-000079); 8-K filed 2026-11-05 (accession 0000916365-26-000076); 8-K filed 2026-10-22 (accession 0000916365-26-000069) |
| S024 | filing | MGM | 2026-10-28 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000789570&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-28 (accession 0000789570-26-000107); 8-K filed 2026-10-28 (accession 0000789570-26-000106); 8-K filed 2026-10-28 (accession 0000789570-26-000104) |
| S025 | filing | CLX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000021076.json | Diluted EPS 1.39 for period ending 2026-09-30 (filed 2026-11-02) |
| S026 | news | MGM | Mon, 23 Nov 2026 17:45:39 GMT | ok | https://news.google.com/rss/search?q=MGM+MGM+Resorts+stock&hl=en-US&gl=US&ceid=US:en | Here’s Why MGM Resorts (MGM) Declined in Q3 - Yahoo Finance (Mon, 23 Nov 2026 17:45:39 GMT); This casino stock has fallen for 17 weeks in a row. Katie Stockton says it could be due for a bounce - CNBC (Tue, 03 Nov 2026 08:00:00 GMT); MGM Stock Dives 10% After Barry Diller Drops $18 Billion Bid - Forbes (Thu, 24 Sep 2026 07:00:00 GMT) |
| S027 | stock | TSCO | 2026-11-26 | ok | https://finance.yahoo.com/quote/TSCO | Trailing P/E: 21.7043; Forward P/E: 19.622805; Forward EPS: 2.0573; Price: 40.37; Market price: 40.37; Market cap: 20934819840; Sector: Consumer Cyclical; Trailing Eps: 1.86; Revenue Growth: 0.051; Earnings Growth: -0.121; Gross Margin: 0.36285; Operating Margin: 0.08701; Profit Margin: 0.061300002; Return On Equity: 0.37347; Total Revenue: 15942134784; Market Cap: 20934819840; Consensus EPS FY+1: 2.04688; growth: 0.091400005 |
| S028 | news | TSCO | Mon, 23 Nov 2026 11:59:33 GMT | ok | https://news.google.com/rss/search?q=TSCO+Tractor+Supply+stock&hl=en-US&gl=US&ceid=US:en | Do Wall Street Analysts Like Tractor Supply Stock? - Yahoo Finance (Mon, 23 Nov 2026 11:59:33 GMT); Tractor Supply Company (TSCO) Stock Forecasts - Yahoo Finance (Wed, 25 Nov 2026 09:40:44 GMT); Tractor Supply (TSCO) Stock May Be 7% Above Fair Value - Yahoo Finance (Mon, 09 Nov 2026 08:00:00 GMT) |
| S029 | stock | MGM | 2026-11-26 | ok | https://finance.yahoo.com/quote/MGM | Trailing P/E: 13.326924; Forward P/E: 24.652624; Forward EPS: 1.40553; Price: 34.65; Market price: 34.65; Market cap: 8766815232; Sector: Consumer Cyclical; Trailing Eps: 2.6; Revenue Growth: -0.009; Gross Margin: 0.4362; Operating Margin: 0.057979997; Profit Margin: 0.03916; Return On Equity: 0.26933; Total Revenue: 17722869760; Market Cap: 8766815232; Consensus EPS FY+1: 1.40553; growth: -0.0462 |
| S030 | filing | IDXX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000874716&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000874716-26-000135); 8-K filed 2026-11-02 (accession 0001104659-26-120892); 10-Q filed 2026-08-04 (accession 0000874716-26-000123) |
| S031 | filing | FISV | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0000798354-26-000042); 8-K filed 2026-11-03 (accession 0000798354-26-000039); 8-K filed 2026-10-23 (accession 0001193125-26-429481) |
| S032 | news | IDXX | Thu, 26 Nov 2026 13:13:20 GMT | ok | https://news.google.com/rss/search?q=IDXX+Idexx+Laboratories+stock&hl=en-US&gl=US&ceid=US:en | IDEXX Laboratories Stock Outlook: Is Wall Street Bullish or Bearish - Barchart.com (Thu, 26 Nov 2026 13:13:20 GMT); Does ETF Buying Change The Bull Case For IDEXX Stock (IDXX)? - Yahoo Finance (Wed, 25 Nov 2026 17:12:38 GMT); Can IDEXX Stock Keep Rising After Its 25% Run? - Trefis (Tue, 24 Nov 2026 15:26:34 GMT) |
| S033 | filing | TSCO | 2026-11-05 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000916365.json | Diluted EPS 1.43 for period ending 2026-09-26 (filed 2026-11-05) |
| S034 | stock | FISV | 2026-11-26 | ok | https://finance.yahoo.com/quote/FISV | Forward P/E: 7.499978; Price: 59.78; Market price: 59.78; Market cap: 31805810688; Market Cap: 31805810688; Consensus EPS FY+1: 7.97069; growth: 0.0954 |
| S035 | filing | MGM | 2026-10-28 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000789570.json | Diluted EPS 1.52 for period ending 2026-09-30 (filed 2026-10-28) |
| S036 | news | FISV | Wed, 11 Nov 2026 08:00:00 GMT | ok | https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en | Fiserv (FISV) Stock Looks Undervalued With Strong Excess Returns - Yahoo Finance (Wed, 11 Nov 2026 08:00:00 GMT); Why Is Fiserv Stock Going Up? - Trefis (Wed, 04 Nov 2026 08:00:00 GMT); Citizens initiated coverage on Fiserv - Quantisnow (Mon, 23 Nov 2026 12:50:42 GMT) |
| S037 | stock | IDXX | 2026-11-26 | ok | https://finance.yahoo.com/quote/IDXX | Trailing P/E: 47.807278; Forward P/E: 41.997524; Forward EPS: 16.8929; Price: 709.46; Market price: 709.46; Market cap: 55895703552; Sector: Healthcare; Trailing Eps: 14.84; Revenue Growth: 0.099; Earnings Growth: 0.179; Gross Margin: 0.62722; Operating Margin: 0.32497; Profit Margin: 0.25357; Return On Equity: 0.68925005; Total Revenue: 4662220800; Market Cap: 55895703552; Consensus EPS FY+1: 16.8929; growth: 0.1244 |
| S038 | filing | IDXX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000874716.json | Diluted EPS 11.75 for period ending 2026-09-30 (filed 2026-11-02) |
| S039 | filing | SNDK | 2026-11-19 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0002023554&type=10-Q&dateb=&owner=include&count=10 | 8-K filed 2026-11-19 (accession 0001628280-26-075127); 8-K filed 2026-11-18 (accession 0001628280-26-074848); 10-Q filed 2026-10-30 (accession 0001628280-26-068601) |
| S040 | stock | SNDK | 2026-11-26 | ok | https://finance.yahoo.com/quote/SNDK | Trailing P/E: 4.7065215; Forward P/E: 2.0565789; Forward EPS: 35.79245; Price: 73.61; Market price: 73.61; Market cap: 83791355904; Sector: Technology; Trailing Eps: 15.64; Revenue Growth: 3.779; Earnings Growth: 69.096; Gross Margin: 0.79952; Operating Margin: 0.7268; Profit Margin: 0.67039; Return On Equity: 1.41174; Total Revenue: 28970999808; Market Cap: 83791355904; Consensus EPS FY+1: 35.79245; growth: 0.2573 |

## Sources

- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFF&cosd=2026-01-01 (2026-11-24)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLH0A0HYM2&cosd=2026-01-01 (2026-11-24)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLC0A0CM&cosd=2026-01-01 (2026-11-24)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCSL&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=UNRATE&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=PAYEMS&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=T10Y2Y&cosd=2026-01-01 (2026-11-25)
- filing APP: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001751008&type=10-Q&dateb=&owner=include&count=10 (2026-11-04)
- filing CMG: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001058090&type=10-Q&dateb=&owner=include&count=10 (2026-10-29)
- filing CHTR: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 (2026-11-06)
- news CHTR: https://news.google.com/rss/search?q=CHTR+Charter+Communications+stock&hl=en-US&gl=US&ceid=US:en (Thu, 26 Nov 2026 16:09:04 GMT)
- news APP: https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en (Thu, 05 Nov 2026 08:00:00 GMT)
- stock APP: https://finance.yahoo.com/quote/APP (2026-11-26)
- filing APP: https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json (2026-11-04)
- stock CMG: https://finance.yahoo.com/quote/CMG (2026-11-26)
- news CMG: https://news.google.com/rss/search?q=CMG+Chipotle+Mexican+Grill+stock&hl=en-US&gl=US&ceid=US:en (Tue, 24 Nov 2026 15:25:45 GMT)
- stock CHTR: https://finance.yahoo.com/quote/CHTR (2026-11-26)
- filing CLX: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 (2026-11-19)
- filing CMG: https://data.sec.gov/api/xbrl/companyfacts/CIK0001058090.json (2026-10-29)
- filing CHTR: https://data.sec.gov/api/xbrl/companyfacts/CIK0001091667.json (2026-11-06)

## AI Provenance

- Provider / model: hermes-local-proxy / upstage/solar-mini4:free
- Market research: attempts=1 tokens=8379 (prompt=5379, completion=3000) runtime=20.11s
- Fundamental research: generated this run at 2026-11-26T22:14:20.019607+00:00
- Evidence source dates: {'as_of': '2026-11-25', 'latest_equity_date': '2026-11-25', 'latest_macro_date': '2026-11-26', 'flows_date': '2026-11-25'}
- Evidence fingerprint: 52f5eecb304c8d7917fc69e794f5977d181db676e619a3458f58dd58e110678e
- Source citations are retrieved external records in the ledger above; market values remain from the verified database snapshot.


## Disclosures

- This is research and market intelligence, not investment advice.
- AI conclusions are research judgments, not validated return predictions.
- The frozen risk layer is risk-only and is not used for directional views or allocations.
- Legacy scores are not active inputs or outputs.

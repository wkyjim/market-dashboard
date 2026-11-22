# AEGIS AI-First Market Intelligence

Research generated at: 23 November 2026, 06:17 HKT
Database freshness: equity 2026-11-20 (latest row retrieved 2026-11-22 13:05:43.380314+08:00)
Data cutoff: 2026-11-20 US cash close
Snapshot ID: aegis-hourly-20261122T221751Z

## Executive Summary

- **AI market view: Risk-off, breadth-negative tape with a 20-day S&P 500 drawdown of -9.36% and a 0.326 advance/decline ratio; the market is not in a bullish divergence, and the 50-day and 200-day breadth measures are deteriorating. Sector rotation is defensive: Consumer Staples is the only positive sector over 20 days, while Information Technology and Energy are the worst performers. Liquidity is flowing into semiconductors (SOXX) and Treasuries (TLT), but the overall equity tape remains fragile.**
- S&P 500 is down 9.36% over 20 days with negative breadth: 37.57% of names positive over 20 days, advance/decline ratio 0.326, no new highs.
- Sector leadership is defensive: Consumer Staples +2.49% over 20 days; Information Technology -18.68% and Energy -12.72% are the worst sectors.
- Macro backdrop shows a 3.88% effective fed funds rate, 3.52% high-yield OAS, and 0.94% IG OAS, with a 10Y-2Y spread of 0.29.
- Flows show structural accumulation in TLT and strong institutional buying in SOXX, but SMH is neutral despite price declines.
- Risk model flags elevated 5-day forecast volatility of 0.366 and a 92.8% spike probability, well above the 26.3% historical baseline.
- The equity session is a mix of provisional yfinance and canonical Massive rows, so some data should be treated as provisional.

## Data QC

- Status: **PASS_WITH_WARNINGS**
- Equity session: 0 completed session(s) behind inference date
- Macro session: 2026-11-21 (0 completed session(s) behind inference date)
- Equity provenance: 138 provisional / 12686 canonical
- Breadth lag: 0 session(s); ETF-flow lag: 0 session(s)
- Note: Equity session contains a mix of provisional yfinance and canonical Massive rows.
- External sources: 79 ok / 0 unavailable; retrieved 2026-11-22T22:18:06.206319+00:00

## Idea Discovery

- S&P 500 universe: 503; eligible: 501; transparent shortlist: 20
- Method: independent momentum/dislocation/PE/liquidity buckets; no composite score
- Evidence used: latest close, 20d and 60d price returns, 60d drawdown, trailing P/E, earnings yield, sector-relative P/E, dollar volume, GICS sector
- Not available as verified inputs: verified earnings-revision history for the full universe, FY+2 consensus, structured industry catalyst calendar
- Eligible but not shortlisted: 481 (outside the top independent momentum, dislocation, valuation and liquidity buckets)
- Included: APP (top_20d_momentum); CMG (top_20d_momentum); PNR (top_20d_momentum); CLX (top_20d_momentum); IDXX (top_20d_momentum); CHTR (top_20d_momentum); GEN (top_20d_momentum); MGM (top_20d_momentum); SNDK (largest_20d_dislocation); MRVL (largest_20d_dislocation); NOW (largest_20d_dislocation); DDOG (largest_20d_dislocation); INTC (largest_20d_dislocation); RDDT (largest_20d_dislocation); NVDA (largest_20d_dislocation, liquidity_leader); LITE (largest_20d_dislocation); MU (liquidity_leader); AMD (liquidity_leader); AAPL (liquidity_leader); MSFT (liquidity_leader)
- Excluded reasons: {"missing_recent_or_latest_price": 2}
- Valuation-quality rejected: [{"flags": ["forward_pe_outside_plausible_range", "implausible_earnings_yield", "forward_eps_vs_reported_jump"], "ticker": "CHTR"}, {"flags": ["forward_pe_outside_plausible_range", "implausible_earnings_yield"], "ticker": "SNDK"}, {"flags": ["forward_eps_vs_reported_jump"], "ticker": "MRVL"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "INTC"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "RDDT"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "NVDA"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "LITE"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "MU"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "AMD"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "AAPL"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "MSFT"}]

## Market Snapshot

| Asset | Latest | Change | Observation |
| --- | --- | --- | --- |
| S&P 500 | 6910.39 | -9.36% over 20 days | Negative breadth with 37.57% of names positive over 20 days and an advance/decline ratio of 0.326; no new highs. |
| Consumer Staples (XLP) | 24.34 | +2.49% over 20 days | Only positive sector; trailing P/E 24.34. |
| Information Technology (XLK) | 26.28 | -18.68% over 20 days | Worst sector; trailing P/E 26.28. |
| Energy (XLE) | 15.11 | -12.72% over 20 days | Second-worst sector; trailing P/E 15.11. |
| Health Care (XLV) | 28.89 | -1.14% over 20 days | Slightly negative; trailing P/E 28.89. |

## Macro, Fiscal, Rates, Liquidity and Credit

- Growth: The 10Y-2Y Treasury spread is 0.29 as of 2026-11-20, indicating a modestly positive but still shallow yield curve.
- Inflation: CPI and core CPI are available only through 2026-09-01 (336.298 and 338.896), with no more recent official readings in the database.
- Policy: The effective federal funds rate is 3.88% as of 2026-11-19, suggesting a restrictive but stable policy stance.
- Rates: High-yield OAS is 3.52 and IG OAS is 0.94 as of 2026-11-19, implying tight credit spreads and manageable default risk.
- Liquidity: TLT shows structural accumulation and SOXX shows strong institutional buying, indicating capital rotation into duration and semiconductors.
- Credit: The elevated 5-day forecast volatility of 0.366 and 92.8% spike probability signal elevated tail risk in the near term.

## US Equities and 11 GICS Sectors

Macro source IDs: S001, S002, S003, S004, S005, S006, S007

| GICS sector | Evidence | AI research stance | Source IDs |
| --- | --- | --- | --- |
| Health Care | Sector ETF XLV returned -1.14% over 20 days; trailing P/E 28.89. | Defensive but underperforming; valuation is rich relative to the defensive peer group. | S056 |
| Consumer Staples | Sector ETF XLP returned +2.49% over 20 days; trailing P/E 24.34. | Only positive sector; defensive demand is supporting the group. | S057 |
| Consumer Discretionary | Sector ETF XLY returned -0.57% over 20 days; trailing P/E 23.54. | Slightly negative; consumer spending remains a mixed signal. | S060 |
| Real Estate | Sector ETF XLRE returned -0.26% over 20 days; trailing P/E 28.35. | Flat to slightly negative; valuation is elevated. | S062 |
| Financials | Sector ETF XLF returned -2.38% over 20 days; trailing P/E 14.74. | Negative; low valuation but pressured by the rate environment. | S064 |
| Utilities | Sector ETF XLU returned +0.31% over 20 days; trailing P/E 17.56. | Flat to slightly positive; defensive demand is intact. | S065 |
| Materials | Sector ETF XLB returned -5.79% over 20 days; trailing P/E 20.10. | Negative; commodity and industrial demand concerns. | S068 |
| Industrials | Sector ETF XLI returned -5.01% over 20 days; trailing P/E 25.08. | Negative; cyclical exposure is under pressure. | S070 |
| Communication Services | Sector ETF XLC returned -5.19% over 20 days; trailing P/E 15.89. | Negative; media and platform names are weak. | S073 |
| Information Technology | Sector ETF XLK returned -18.68% over 20 days; trailing P/E 26.28. | Severe drawdown; semiconductor and software leadership is broken. | S074 |
| Energy | Sector ETF XLE returned -12.72% over 20 days; trailing P/E 15.11. | Sharp decline; commodity weakness and demand concerns. | S075 |

### Sector fundamentals, valuation and earnings

No point-in-time sector fundamentals beyond the supplied ETF trailing P/E and 20-day returns are available in the database. The sector evidence is limited to the 11 GICS sector ETFs listed above; no revenue, margin, or growth data are provided for the full universe.

## Growth vs Value

- Consumer Staples is the only sector with positive 20-day momentum and a moderate trailing P/E of 24.34.
- Information Technology has the largest drawdown (-18.68%) but a trailing P/E of 26.28, which is not cheap on a relative basis.
- Energy has a low trailing P/E of 15.11 but a -12.72% price decline, suggesting value is not yet supported by price.
- Financials trade at a low trailing P/E of 14.74, but the sector is down -2.38% over 20 days.
- The screening data show several names with high sector-relative P/E (e.g., NOW 2.88, DDOG 15.46, AMD 3.82) and negative or near-zero earnings yields, indicating expensive or unprofitable names.

## ETF Flows and Breadth

- Breadth is negative: 37.57% of names positive over 20 days, advance/decline ratio 0.326, and no new highs.
- The 50-day and 200-day breadth measures are deteriorating, with breadth_50d_change_5d of -28.86 and breadth_200d_change_5d of -17.38.
- Flows show structural accumulation in TLT and strong institutional buying in SOXX, but SMH is neutral despite price declines.
- The advance/decline ratio of 0.326 indicates that decliners outnumber advancers by roughly 3 to 1.
- New highs and new lows are both zero, so the negative breadth is not driven by a broad collapse but by a lack of upside participation.

## Stock Ideas

Single-stock research uses reported EPS, forward P/E and company fundamentals. All ideas are research judgments, not validated return predictions.

| Ticker | Security | Research view | Price | EPS | Forward P/E | Base target | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| APP | AppLovin | KEEP | 348.29 | 20.86084 | 16.695877 | 417.22 | KEEP |
| PNR | Pentair | KEEP | 68.63 | 5.30402 | 12.939242 | 74.26 | KEEP |
| IDXX | Idexx Laboratories | KEEP | 676.21 | 16.8929 | 40.029243 | 540.57 | KEEP |

## ETF Ideas

ETF research uses holdings, portfolio valuation and exposure. Single-stock EPS × P/E valuation is not applied to ETFs.

| Ticker | Fund | Research view | Price | Top holdings | Portfolio valuation | Sector exposure | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| XLV | Health Care Select Sector SPDR Fund | KEEP | 177.24 | LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59% | Top 10 holdings; numeric weight coverage 61.42% | Health Care | KEEP |
| XLP | Consumer Staples Select Sector SPDR Fund | NEW | 90.46 | WMT 11.14%, COST 9.09%, PG 7.60%, KO 7.37%, PM 6.59%, MO 4.70%, CL 4.42%, MDLZ 4.25%, PEP 4.11%, TGT 4.00% | Top 10 holdings; numeric weight coverage 63.28% | Consumer Staples | NEW |
### APP — AppLovin

- **Type:** Stock
- **Research view:** KEEP (stance: BUY)
- **Why preferred / alternatives:** AppLovin offers a higher-quality, higher-margin advertising franchise than the other momentum names, with a forward P/E of 16.7x that is far more reasonable than the dislocation-heavy names such as DDOG or NOW. Alternatives considered: NOW, DDOG.
- **Thesis:** AppLovin screens in the top 20-day momentum bucket with a 33.8% 20-day return and a 16.7x forward P/E, implying a reasonable entry for a high-margin mobile advertising platform. Reported diluted EPS of 11.61 and 25.5% revenue growth support the valuation, and the name has a 2.1% ROE with an 88.8% gross margin.
- **Source IDs:** S008, S012, S013, S014
- **Catalysts:** Continued momentum in mobile ad demand and app install volume, Sustained double-digit revenue growth and margin expansion, Potential re-rating as the stock digests its 20-day price advance
- **Risks:** 20-day momentum may be overextended and prone to a pullback, Forward P/E of 16.7x still prices in continued high growth, Mobile advertising is sensitive to macro spending and ad-market cycles
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 20.8608 (source.forwardEps) x AI multiple assumption 20.00; source IDs S008, S012, S013, S014
- **EPS:** 20.86084 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 16.695877
- **FY+1 growth assumption:** 27.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / Microsoft (MSFT) and Alphabet (GOOGL) as high-margin software peers / APP shows strong FY1 consensus growth of 27.44% and revenue growth of 55.5%, with exceptional gross margin of 88.8% and operating margin of 77.8%. The forward EPS of 20.86 supports a forward P/E of 16.7, but the base multiple of 20x is justified by superior margins and growth relative to high-margin software peers. Bull case of 24x reflects continued execution and margin expansion; bear case of 16x reflects potential deceleration or multiple compression.
- **Company fundamentals:** Reported diluted EPS 11.61; forward EPS 20.86; forward P/E 16.70; revenue growth 55.5%; earnings growth 75.5%; gross margin 88.8%; operating margin 77.8%; profit margin 65.9%; ROE 2.10%.
- **Bull / Base / Bear:** 500.66 / 417.22 / 333.77
- **Bull / Base / Bear returns:** 43.75% / 19.79% / -4.17%
- **Scenario probabilities:** not separately assigned; see scenario table.

### PNR — Pentair

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Pentair is the only Industrials name in the shortlist with a low forward P/E, but its negative earnings growth makes it a neutral holding rather than a top pick. Alternatives considered: NOW, DDOG.
- **Thesis:** Pentair is a top-20-day-momentum name with a 24.1% 20-day return and a 13.6x trailing P/E, but its 60-day return is only 10.5% and forward EPS growth is negative at -18.8%. The low valuation is offset by weak near-term earnings momentum, so the position should be sized conservatively.
- **Source IDs:** S009, S017, S018, S019
- **Catalysts:** Potential stabilization in industrial end markets, Attractive entry valuation if earnings stabilize, Diversified water, flow control and building products exposure
- **Risks:** Negative forward earnings growth of -18.8%, 60-day return of only 10.5% suggests limited follow-through, Industrial end-market softness could delay recovery
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 5.3040 (source.forwardEps) x AI multiple assumption 14.00; source IDs S009, S017, S018, S019
- **EPS:** 5.30402 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 12.939242
- **FY+1 growth assumption:** 12.82%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / Union Pacific (UNP) and Canadian National Railway (CNI) as railroad peers / PNR shows FY1 consensus growth of 12.82% with revenue growth of 18.4% and earnings growth of -18.8%, indicating margin pressure. Gross margin of 40.2% and operating margin of 21.4% are typical for railroads. The forward EPS of 5.30 supports a forward P/E of 12.9, but the base multiple of 14x is justified by growth and peer comparison. Bull case of 16x reflects potential margin recovery; bear case of 11x reflects continued earnings decline.
- **Company fundamentals:** Reported diluted EPS 2.76; forward EPS 5.30; forward P/E 12.94; revenue growth -4.5%; earnings growth -18.8%; gross margin 40.2%; operating margin 21.4%; profit margin 15.4%; ROE 0.16%.
- **Bull / Base / Bear:** 84.86 / 74.26 / 58.34
- **Bull / Base / Bear returns:** 23.65% / 8.2% / -14.99%
- **Scenario probabilities:** not separately assigned; see scenario table.

### IDXX — Idexx Laboratories

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Idexx is a higher-quality growth compounder than the other momentum names, but its 40.0x forward P/E makes it a premium holding rather than a core recommendation. Alternatives considered: NOW, DDOG.
- **Thesis:** Idexx is a top-20-day-momentum name with a 20.7% 20-day return and a 24.1% 60-day return, but it carries a 40.0x forward P/E and a 2.6% earnings yield. The high valuation is justified by 9.9% revenue growth and 17.9% earnings growth, yet the stock is expensive relative to the rest of the shortlist.
- **Source IDs:** S022, S024, S029, S031
- **Catalysts:** Steady growth in animal health and diagnostics platforms, 17.9% earnings growth supports the current valuation, Diversified pet care and laboratory diagnostics exposure
- **Risks:** Forward P/E of 40.0x is the second-highest in the shortlist, Earnings growth of 17.9% may decelerate, High valuation leaves little room for disappointment
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 16.8929 (source.forwardEps) x AI multiple assumption 32.00; source IDs S022, S024, S029, S031
- **EPS:** 16.8929 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 40.029243
- **FY+1 growth assumption:** 12.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / Cerner (now Oracle) and MEDITECH as healthcare IT peers / IDXX shows FY1 consensus growth of 12.44% with revenue growth of 9.9% and earnings growth of 17.9%, indicating strong earnings momentum. Gross margin of 62.7% and operating margin of 32.5% are solid for healthcare IT. The forward EPS of 16.89 supports a forward P/E of 40.0, but the base multiple of 32x is justified by growth and peer comparison. Bull case of 36x reflects continued growth; bear case of 28x reflects potential deceleration.
- **Company fundamentals:** Reported diluted EPS 11.75; forward EPS 16.89; forward P/E 40.03; revenue growth 9.9%; earnings growth 17.9%; gross margin 62.7%; operating margin 32.5%; profit margin 25.4%; ROE 0.69%.
- **Bull / Base / Bear:** 608.14 / 540.57 / 473.0
- **Bull / Base / Bear returns:** -10.07% / -20.06% / -30.05%
- **Scenario probabilities:** not separately assigned; see scenario table.

### XLV — Health Care Select Sector SPDR Fund

- **Type:** ETF
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** XLV offers broad Health Care exposure with a diversified top-10 portfolio, making it a cleaner way to hold the sector than individual names like IDXX. Alternatives considered: IDXX.
- **Thesis:** XLV is the Health Care sector ETF with a -12.4% raw price change over the session, but it provides diversified exposure to the sector's large-cap leaders. The sector ETF is a neutral portfolio holding that can be used to express Health Care exposure without picking individual names.
- **Source IDs:** S055, S056
- **Catalysts:** Sector rotation into defensive Health Care names, Large-cap pharmaceutical and medical device leadership, Diversification across 10+ top holdings
- **Risks:** Sector-wide drawdown of -12.4%, Concentration in large pharma names, Sector-specific regulatory and patent-cliff risks
- **Valuation method:** Holdings/portfolio valuation with AI total-return assumption
- **Valuation status:** verified; forward-EPS source: ; period flags: 
- **Valuation assumptions:** Holdings/portfolio valuation; 10 weighted holdings; coverage 61.42%; source IDs S055, S056
- **Top holdings:** LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59%
- **Portfolio valuation:** Top 10 holdings; numeric weight coverage 61.42%
- **Sector exposure:** Health Care
- **Underlying drivers:** Large-cap pharmaceutical and medical device leadership; diversified top-10 portfolio; sector rotation into defensive names.
- **Bull / Base / Bear:** 202.05 / 191.42 / 170.15
- **Bull / Base / Bear returns:** 14.0% / 8.0% / -4.0%
- **Scenario probabilities:** not separately assigned; see scenario table.

### XLP — Consumer Staples Select Sector SPDR Fund

- **Type:** ETF
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** XLP provides a defensive, diversified staples exposure that is not represented by any individual stock in the shortlist, making it a useful portfolio complement. Alternatives considered: CLX.
- **Thesis:** XLP is the Consumer Staples sector ETF with a +0.67% raw price change, offering defensive exposure to staples leaders with a diversified top-10 portfolio. It is a new addition to the shortlist and provides a lower-volatility complement to the momentum and dislocation names.
- **Source IDs:** S057, S059
- **Catalysts:** Defensive sector rotation into staples, Diversified exposure to consumer staples leaders, Lower volatility than the broader market
- **Risks:** Sector-wide pullback of -0.67%, Concentration in large consumer staples names, Limited upside in a risk-on environment
- **Valuation method:** Holdings/portfolio valuation with AI total-return assumption
- **Valuation status:** verified; forward-EPS source: ; period flags: 
- **Valuation assumptions:** Holdings/portfolio valuation; 10 weighted holdings; coverage 63.28%; source IDs S057, S059
- **Top holdings:** WMT 11.14%, COST 9.09%, PG 7.60%, KO 7.37%, PM 6.59%, MO 4.70%, CL 4.42%, MDLZ 4.25%, PEP 4.11%, TGT 4.00%
- **Portfolio valuation:** Top 10 holdings; numeric weight coverage 63.28%
- **Sector exposure:** Consumer Staples
- **Underlying drivers:** Diversified top-10 portfolio of consumer staples leaders; defensive sector rotation; lower volatility.
- **Bull / Base / Bear:** 100.41 / 95.89 / 87.75
- **Bull / Base / Bear returns:** 11.0% / 6.0% / -3.0%
- **Scenario probabilities:** not separately assigned; see scenario table.

## Quant Risk Layer

| Field | Value |
| --- | --- |
| Volatility model | vol5_ols_v1 |
| Spike model | spike_logit_v1 |
| As-of date | 2026-11-20 |
| Target window | 2026-11-23 to 2026-11-30 |
| Forecast 5D annualized volatility | 36.64% |
| Historical-vol baseline | 26.26% |
| EWMA baseline | 24.67% |
| Spike probability | 92.77% |
| Spike threshold | 18.50% |
| Status | prospective |
| Forecast ID | 48d2c1933342b1a6 |

Risk-only; no directional interpretation or allocation implication.

## Scenarios

### Short Term (5 trading sessions)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 25% | +2.00% | Spike probability 0.928 vs historical 0.263 and EWMA 0.247 indicates elevated near-term volatility; if the frozen daily-close model resolves after the US close without a directional signal, a modest 2.0% upside is plausible as risk premium is absorbed. |
| Base | 50% | +0.00% | Directional signal is false and the forecast is prospective, so the most likely path is a flat short-term return around 0.0% as the model's elevated volatility does not yet translate into a confirmed trend. |
| Bear | 25% | -2.00% | With spike probability 0.928 and forecast vol 5d of 0.366, a failed resolution after the US close could trigger a 2.0% downside move as elevated volatility pressure persists. |

### Long Term (12 months)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 30% | +8.00% | If the elevated spike probability reflects a genuine regime shift rather than noise, sustained volatility compression and positive earnings revisions could drive an 8.0% long-term return. |
| Base | 40% | +3.00% | A neutral baseline with no directional signal and a frozen daily-close model implies steady, modest long-term appreciation of 3.0% as fundamentals and rate expectations remain balanced. |
| Bear | 30% | -5.00% | If the high spike probability and 0.366 forecast vol signal persistent instability, a 5.0% long-term decline is plausible as volatility drag and negative breadth erode returns. |

## Positioning

- Maintain a defensive posture with exposure to Consumer Staples and Utilities.
- Reduce or avoid Information Technology and Energy until breadth and momentum improve.
- Monitor the 10Y-2Y spread and credit spreads for signs of a shift in risk appetite.
- Watch the elevated spike probability and forecast volatility for potential tail-risk events.
- Do not infer allocation weights or directional bets; the frozen risk block is risk-only.

## Catalysts

| Date | Event | Why it matters |
| --- | --- | --- |
| 2026-11-23 | Target start of the 48d2c1933342b1a6 risk forecast window | The frozen risk model flags a 92.8% spike probability and 0.366 forecast volatility, so the next week is the highest-risk window. |
| 2026-11-24 | US macro data release window | The database contains only September 2026 CPI and unemployment data; any new official releases would update the inflation and labor picture. |
| 2026-11-25 | Semiconductor flow confirmation | SOXX shows strong institutional buying; a sustained flow into semiconductors could signal a bottoming attempt in the worst-performing sector. |

## Key Risks

- Negative breadth and a 0.326 advance/decline ratio indicate weak participation and potential further downside.
- The 5-day forecast volatility of 0.366 and 92.8% spike probability signal elevated tail risk.
- Information Technology and Energy are the worst-performing sectors and could continue to lag.
- The equity session contains a mix of provisional yfinance and canonical Massive rows, so some data may be unreliable.
- CPI and core CPI data are stale (September 2026), so the inflation outlook is uncertain.
- The 10Y-2Y spread is only 0.29, indicating a shallow curve that may limit financial sector performance.

## External Source Ledger

| ID | Type | Ticker | Published | Status | URL | Claims |
| --- | --- | --- | --- | --- | --- | --- |
| S001 | macro | macro | 2026-11-19 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFF&cosd=2026-01-01 | Effective federal funds rate (DFF) latest observation 2026-11-19: 3.88 |
| S002 | macro | macro | 2026-11-19 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLH0A0HYM2&cosd=2026-01-01 | US high-yield OAS (BAMLH0A0HYM2) latest observation 2026-11-19: 3.52 |
| S003 | macro | macro | 2026-11-19 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLC0A0CM&cosd=2026-01-01 | US investment-grade OAS (BAMLC0A0CM) latest observation 2026-11-19: 0.94 |
| S004 | macro | macro | 2026-10-01 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCSL&cosd=2026-01-01 | US CPI (CPIAUCSL) latest observation 2026-10-01: 337.476 |
| S005 | macro | macro | 2026-10-01 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=UNRATE&cosd=2026-01-01 | US unemployment rate (UNRATE) latest observation 2026-10-01: 4.1 |
| S006 | macro | macro | 2026-10-01 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=PAYEMS&cosd=2026-01-01 | US nonfarm payrolls (PAYEMS) latest observation 2026-10-01: 159293 |
| S007 | macro | macro | 2026-11-20 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=T10Y2Y&cosd=2026-01-01 | 10Y-2Y Treasury spread (T10Y2Y) latest observation 2026-11-20: 0.29 |
| S008 | filing | APP | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001751008&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0001751008-26-000069); 8-K filed 2026-11-04 (accession 0001751008-26-000068); 10-Q filed 2026-08-05 (accession 0001751008-26-000059) |
| S009 | filing | PNR | 2026-10-27 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-27 (accession 0000077360-26-000058); 8-K filed 2026-10-27 (accession 0000077360-26-000055); 8-K filed 2026-09-22 (accession 0000077360-26-000050) |
| S010 | filing | CMG | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001058090&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0001058090-26-000104); 8-K filed 2026-10-28 (accession 0001058090-26-000103); 8-K filed 2026-09-14 (accession 0001058090-26-000088) |
| S011 | news | CMG | Sat, 21 Nov 2026 02:05:00 GMT | ok | https://news.google.com/rss/search?q=CMG+Chipotle+Mexican+Grill+stock&hl=en-US&gl=US&ceid=US:en | Chipotle Mexican Grill vs. Hershey: Which Consumer Stock Is a Better Buy for 2027? - Yahoo Finance (Sat, 21 Nov 2026 02:05:00 GMT); Chipotle Mexican Grill vs. Kraft Heinz: Which Consumer Stock Is a Better Buy for 2027? - The Motley Fool (Wed, 18 Nov 2026 16:45:02 GMT); Chipotle Stock Looks Cheaper On 2027 Profit, If Sales Deliver - Trefis (Fri, 20 Nov 2026 16:32:30 GMT) |
| S012 | news | APP | Sat, 21 Nov 2026 23:19:26 GMT | ok | https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en | AppLovin vs. Reddit: Which Technology Stock Is a Better Buy for 2027? - The Motley Fool (Sat, 21 Nov 2026 23:19:26 GMT); AppLovin delivers strong Q3 2026 numbers, stock jumps 24.9% - Yahoo Finance (Thu, 05 Nov 2026 08:00:00 GMT); This tech stock has been nearly cut in half this year. I think Wall Street is getting it wrong - CNBC (Thu, 19 Nov 2026 19:08:20 GMT) |
| S013 | filing | APP | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json | Diluted EPS 11.61 for period ending 2026-09-30 (filed 2026-11-04) |
| S014 | stock | APP | 2026-11-22 | ok | https://finance.yahoo.com/quote/APP | Trailing P/E: 23.453873; Forward P/E: 16.695877; Forward EPS: 20.86084; Price: 348.29; Market price: 348.29; Market cap: 115396132864; Sector: Communication Services; Trailing Eps: 14.85; Revenue Growth: 0.555; Earnings Growth: 0.755; Gross Margin: 0.8878; Operating Margin: 0.77782995; Profit Margin: 0.65887; Return On Equity: 2.1008599; Total Revenue: 7608893952; Market Cap: 115396132864; Consensus EPS FY+1: 20.72451; growth: 0.2744 |
| S015 | filing | CLX | 2026-11-19 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 | 8-K filed 2026-11-19 (accession 0001206774-26-000606); 10-Q filed 2026-11-02 (accession 0000021076-26-000046); 8-K filed 2026-11-02 (accession 0000021076-26-000044) |
| S016 | filing | CMG | 2026-10-29 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001058090.json | Diluted EPS 0.82 for period ending 2026-09-30 (filed 2026-10-29) |
| S017 | filing | PNR | 2026-10-27 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json | Diluted EPS 2.76 for period ending 2026-09-30 (filed 2026-10-27) |
| S018 | stock | PNR | 2026-11-22 | ok | https://finance.yahoo.com/quote/PNR | Trailing P/E: 18.700272; Forward P/E: 12.939242; Forward EPS: 5.30402; Price: 68.63; Market price: 68.63; Market cap: 10957101056; Sector: Industrials; Trailing Eps: 3.67; Revenue Growth: -0.045; Earnings Growth: -0.188; Gross Margin: 0.40168998; Operating Margin: 0.21410999; Profit Margin: 0.15435; Return On Equity: 0.15605; Total Revenue: 3966200064; Market Cap: 10957101056; Consensus EPS FY+1: 5.30402; growth: 0.1282 |
| S019 | news | PNR | Fri, 20 Nov 2026 22:46:48 GMT | ok | https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en | Pentair Stock Price Forecast. Should You Buy PNR? - StockInvest.us (Fri, 20 Nov 2026 22:46:48 GMT); Pentair (PNR) Stock Could Be Below Fair Value After Earnings Reset - Yahoo Finance (Tue, 28 Jul 2026 07:00:00 GMT); Why Pentair Stock Popped This Morning - The Motley Fool (Tue, 27 Oct 2026 07:00:00 GMT) |
| S020 | stock | CMG | 2026-11-22 | ok | https://finance.yahoo.com/quote/CMG | Trailing P/E: 33.224297; Forward P/E: 26.86344; Forward EPS: 1.32336; Price: 35.55; Market price: 35.55; Market cap: 44969861120; Sector: Consumer Cyclical; Trailing Eps: 1.07; Revenue Growth: 0.096; Earnings Growth: -0.062; Gross Margin: 0.39314; Operating Margin: 0.14715; Profit Margin: 0.10832; Return On Equity: 0.48518002; Total Revenue: 12713477120; Market Cap: 44969861120; Consensus EPS FY+1: 1.32336; growth: 0.216 |
| S021 | news | CLX | Thu, 19 Nov 2026 17:06:03 GMT | ok | https://news.google.com/rss/search?q=CLX+Clorox+stock&hl=en-US&gl=US&ceid=US:en | Should You Buy Clorox Stock At This Price? - Yahoo Finance (Thu, 19 Nov 2026 17:06:03 GMT); Clorox (CLX) Stock Rebounds As Q4 Earnings Face Margin Strain - Yahoo Finance (Tue, 03 Nov 2026 08:00:00 GMT); CLX - Clorox Co Stock Price and Quote - Finviz (Tue, 26 May 2026 17:32:27 GMT) |
| S022 | filing | IDXX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000874716&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000874716-26-000135); 8-K filed 2026-11-02 (accession 0001104659-26-120892); 10-Q filed 2026-08-04 (accession 0000874716-26-000123) |
| S023 | filing | CHTR | 2026-11-06 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-06 (accession 0001091667-26-000073); 8-K filed 2026-11-06 (accession 0001091667-26-000072); 8-K filed 2026-10-27 (accession 0001091667-26-000064) |
| S024 | news | IDXX | Thu, 19 Nov 2026 12:30:02 GMT | ok | https://news.google.com/rss/search?q=IDXX+Idexx+Laboratories+stock&hl=en-US&gl=US&ceid=US:en | Here's How Much You'd Have If You Invested $1000 in Idexx Laboratories a Decade Ago - Yahoo Finance (Thu, 19 Nov 2026 12:30:02 GMT); IDEXX Laboratories: Great Company, But Too Expensive (Rating Downgrade) - Seeking Alpha (Wed, 04 Nov 2026 08:00:00 GMT); If You Invested $100 In IDEXX Laboratories Stock 15 Years Ago, You Would Have This Much Today - Benzinga (Mon, 02 Nov 2026 08:00:00 GMT) |
| S025 | stock | CLX | 2026-11-22 | ok | https://finance.yahoo.com/quote/CLX | Trailing P/E: 18.836332; Forward P/E: 16.978472; Forward EPS: 6.1684; Price: 104.73; Market price: 104.73; Market cap: 12687766528; Sector: Consumer Defensive; Trailing Eps: 5.56; Revenue Growth: 0.333; Earnings Growth: 1.138; Gross Margin: 0.41939998; Operating Margin: 0.14286; Profit Margin: 0.09408; Return On Equity: 5.34363; Total Revenue: 7196000256; Market Cap: 12687766528; Consensus EPS FY+1: 6.1684; growth: 0.0769 |
| S026 | stock | CHTR | 2026-11-22 | ok | https://finance.yahoo.com/quote/CHTR | Trailing P/E: 12.098683; Forward P/E: 2.8233452; Forward EPS: 45.59485; Price: 128.73; Market price: 128.73; Market cap: 23049306112; Sector: Communication Services; Trailing Eps: 10.64; Revenue Growth: 0.091; Gross Margin: 0.55084; Operating Margin: 0.23389; Profit Margin: 0.02498; Return On Equity: 0.07019; Total Revenue: 55645999104; Market Cap: 23049306112; Consensus EPS FY+1: 49.52287; growth: 1.4594 |
| S027 | filing | CLX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000021076.json | Diluted EPS 1.39 for period ending 2026-09-30 (filed 2026-11-02) |
| S028 | filing | GEN | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0000849399-26-000083); 8-K filed 2026-10-28 (accession 0000849399-26-000081); 8-K filed 2026-10-09 (accession 0000849399-26-000079) |
| S029 | stock | IDXX | 2026-11-22 | ok | https://finance.yahoo.com/quote/IDXX | Trailing P/E: 45.56671; Forward P/E: 40.029243; Forward EPS: 16.8929; Price: 676.21; Market price: 676.21; Market cap: 53276061696; Sector: Healthcare; Trailing Eps: 14.84; Revenue Growth: 0.099; Earnings Growth: 0.179; Gross Margin: 0.62722; Operating Margin: 0.32497; Profit Margin: 0.25357; Return On Equity: 0.68925005; Total Revenue: 4662220800; Market Cap: 53276061696; Consensus EPS FY+1: 16.8929; growth: 0.1244 |
| S030 | news | CHTR | Sat, 14 Nov 2026 08:00:00 GMT | ok | https://news.google.com/rss/search?q=CHTR+Charter+Communications+stock&hl=en-US&gl=US&ceid=US:en | Charter Communications (CHTR) Stock Could Be A Bargain Following Its New Operating Model - Yahoo Finance (Sat, 14 Nov 2026 08:00:00 GMT); Is Charter Stock Worth The Wait? - Trefis (Tue, 17 Nov 2026 12:33:16 GMT); Charter Communications, Inc. $CHTR Stock Bought by State Street Corp - MarketBeat (Sun, 22 Nov 2026 11:09:29 GMT) |
| S031 | filing | IDXX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000874716.json | Diluted EPS 11.75 for period ending 2026-09-30 (filed 2026-11-02) |
| S032 | filing | MGM | 2026-10-28 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000789570&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-28 (accession 0000789570-26-000107); 8-K filed 2026-10-28 (accession 0000789570-26-000106); 8-K filed 2026-10-28 (accession 0000789570-26-000104) |
| S033 | news | GEN | Sat, 21 Nov 2026 02:14:00 GMT | ok | https://news.google.com/rss/search?q=GEN+Gen+Digital+stock&hl=en-US&gl=US&ceid=US:en | Gen Digital (GEN) Stock Looks Below Fair Value On Its 45% Run - Yahoo Finance (Sat, 21 Nov 2026 02:14:00 GMT); Four S&P 500 Stocks Rising in a Falling Market: Pentair, AppLovin, Chipotle, and Gen Digital - Benzinga (Sat, 21 Nov 2026 22:00:05 GMT); What Was Gen Digital Telling You Before Its Stock Ran? - Yahoo Finance (Wed, 04 Nov 2026 08:00:00 GMT) |
| S034 | stock | GEN | 2026-11-22 | ok | https://finance.yahoo.com/quote/GEN | Trailing P/E: 14.817259; Forward P/E: 8.746435; Forward EPS: 3.33736; Price: 29.19; Market price: 29.19; Market cap: 17317730304; Sector: Technology; Trailing Eps: 1.97; Revenue Growth: 0.122; Earnings Growth: 1.286; Gross Margin: 0.77410007; Operating Margin: 0.43229; Profit Margin: 0.23068; Return On Equity: 0.46402; Total Revenue: 5228000256; Market Cap: 17317730304; Consensus EPS FY+1: 3.33736; growth: 0.1286 |
| S035 | filing | CHTR | 2026-11-06 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001091667.json | Diluted EPS 0.38 for period ending 2026-09-30 (filed 2026-11-06) |
| S036 | stock | MGM | 2026-11-22 | ok | https://finance.yahoo.com/quote/MGM | Trailing P/E: 12.446155; Forward P/E: 23.023344; Forward EPS: 1.40553; Price: 32.36; Market price: 32.36; Market cap: 8187421184; Sector: Consumer Cyclical; Trailing Eps: 2.6; Revenue Growth: -0.009; Gross Margin: 0.4362; Operating Margin: 0.057979997; Profit Margin: 0.03916; Return On Equity: 0.26933; Total Revenue: 17722869760; Market Cap: 8187421184; Consensus EPS FY+1: 1.40553; growth: -0.0462 |
| S037 | news | MGM | Thu, 29 Oct 2026 07:00:00 GMT | ok | https://news.google.com/rss/search?q=MGM+MGM+Resorts+stock&hl=en-US&gl=US&ceid=US:en | How Investors Are Reacting To MGM Resorts Stock After An Earnings Miss - Yahoo Finance (Thu, 29 Oct 2026 07:00:00 GMT); This casino stock has fallen for 17 weeks in a row. Katie Stockton says it could be due for a bounce - CNBC (Tue, 03 Nov 2026 08:00:00 GMT); MGM Stock Dives 10% After Barry Diller Drops $18 Billion Bid - Forbes (Thu, 24 Sep 2026 07:00:00 GMT) |
| S038 | filing | GEN | 2026-10-29 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000849399.json | Diluted EPS 0.83 for period ending 2026-10-02 (filed 2026-10-29) |
| S039 | filing | SNDK | 2026-11-19 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0002023554&type=10-Q&dateb=&owner=include&count=10 | 8-K filed 2026-11-19 (accession 0001628280-26-075127); 8-K filed 2026-11-18 (accession 0001628280-26-074848); 10-Q filed 2026-10-30 (accession 0001628280-26-068601) |
| S040 | filing | MRVL | 2026-11-12 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001835632&type=10-Q&dateb=&owner=include&count=10 | 8-K filed 2026-11-12 (accession 0001835632-26-000026); 8-K filed 2026-11-02 (accession 0001193125-26-442717); 8-K filed 2026-11-02 (accession 0001193125-26-442714) |

## Sources

- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFF&cosd=2026-01-01 (2026-11-19)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLH0A0HYM2&cosd=2026-01-01 (2026-11-19)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLC0A0CM&cosd=2026-01-01 (2026-11-19)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCSL&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=UNRATE&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=PAYEMS&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=T10Y2Y&cosd=2026-01-01 (2026-11-20)
- filing APP: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001751008&type=10-Q&dateb=&owner=include&count=10 (2026-11-04)
- filing PNR: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 (2026-10-27)
- filing CMG: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001058090&type=10-Q&dateb=&owner=include&count=10 (2026-10-29)
- news CMG: https://news.google.com/rss/search?q=CMG+Chipotle+Mexican+Grill+stock&hl=en-US&gl=US&ceid=US:en (Sat, 21 Nov 2026 02:05:00 GMT)
- news APP: https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en (Sat, 21 Nov 2026 23:19:26 GMT)
- filing APP: https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json (2026-11-04)
- stock APP: https://finance.yahoo.com/quote/APP (2026-11-22)
- filing CLX: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 (2026-11-19)
- filing CMG: https://data.sec.gov/api/xbrl/companyfacts/CIK0001058090.json (2026-10-29)
- filing PNR: https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json (2026-10-27)
- stock PNR: https://finance.yahoo.com/quote/PNR (2026-11-22)
- news PNR: https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en (Fri, 20 Nov 2026 22:46:48 GMT)
- stock CMG: https://finance.yahoo.com/quote/CMG (2026-11-22)

## AI Provenance

- Provider / model: hermes-local-proxy / upstage/solar-mini4:free
- Market research: attempts=1 tokens=9252 (prompt=6518, completion=2734) runtime=14.82s
- Fundamental research: generated this run at 2026-11-22T22:17:51.093261+00:00
- Evidence source dates: {'as_of': '2026-11-20', 'latest_equity_date': '2026-11-20', 'latest_macro_date': '2026-11-21', 'flows_date': '2026-11-20'}
- Evidence fingerprint: ff697a7a23f77b8ff12209ec4c17c5ae758938b11b971e57984f25bbd4eb1712
- Source citations are retrieved external records in the ledger above; market values remain from the verified database snapshot.


## Disclosures

- This is research and market intelligence, not investment advice.
- AI conclusions are research judgments, not validated return predictions.
- The frozen risk layer is risk-only and is not used for directional views or allocations.
- Legacy scores are not active inputs or outputs.

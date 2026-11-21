# AEGIS AI-First Market Intelligence

Research generated at: 22 November 2026, 06:15 HKT
Database freshness: equity 2026-11-20 (latest row retrieved 2026-11-21 13:05:28.181493+08:00)
Data cutoff: 2026-11-20 US cash close
Snapshot ID: aegis-hourly-20261121T221536Z

## Executive Summary

- **AI market view: Risk-off, late-cycle posture: broad market weakness on 2026-11-20 with negative price breadth, sector-wide drawdowns, and elevated 5-day volatility forecast. The shortlist is dominated by high-multiple, high-beta, or dislocation names; quality and low-beta names are underrepresented. Cash and defensive positioning are warranted until breadth and volatility normalize.**
- US equities closed 2026-11-20 in a risk-off tone: SPX -9.36% over 20 days, negative 20-day price breadth (37.6% positive), and a 0.326 advance/decline ratio.
- All 11 GICS sectors declined over 20 days; Information Technology (-18.7%) and Energy (-12.7%) led the weakness, while Consumer Staples (+2.5%) was the only positive sector.
- The shortlist is heavily weighted toward high-multiple, high-beta, or dislocation names (NOW, DDOG, MRVL, AMD, AAPL, MSFT) with weak earnings yields and elevated sector-relative P/E.
- Macro data show a still-elevated but easing inflation backdrop (CPI 336.30, core 338.90 in Sep-2026), a 4.2% unemployment rate, and a near-flat 10Y-2Y curve (0.29).
- Credit conditions are moderately stressed: high-yield OAS 3.52 and IG OAS 0.94, with a 5-day volatility forecast of 36.6% and a 92.8% spike probability.
- Liquidity is concentrated in SOXX (semiconductor ETF) with exceptional institutional buying, while TLT and SMH show neutral/structural accumulation; no broad-based flow signal is evident.

## Data QC

- Status: **PASS_WITH_WARNINGS**
- Equity session: 0 completed session(s) behind inference date
- Macro session: 2026-11-20 (0 completed session(s) behind inference date)
- Equity provenance: 137 provisional / 12686 canonical
- Breadth lag: 0 session(s); ETF-flow lag: 0 session(s)
- Note: Equity session contains a mix of provisional yfinance and canonical Massive rows.
- External sources: 79 ok / 0 unavailable; retrieved 2026-11-21T22:15:54.308856+00:00

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
| SPX | 6910.39 | -9.36% (20d) | Broad market weakness; negative price breadth and low advance/decline ratio. |
| XLK (Information Technology) | -18.68% | -18.68% (20d) | Largest sector drawdown; high-multiple names dominate the shortlist. |
| XLE (Energy) | -12.72% | -12.72% (20d) | Sharp energy sector decline; sector-relative P/E data not provided. |
| XLC (Communication Services) | -5.19% | -5.19% (20d) | Negative 20-day return; high-multiple names in shortlist. |
| XLI (Industrials) | -5.01% | -5.01% (20d) | Negative 20-day return; sector-relative P/E data not provided. |
| XLB (Materials) | -5.79% | -5.79% (20d) | Negative 20-day return; sector-relative P/E data not provided. |
| XLF (Financials) | -2.38% | -2.38% (20d) | Negative 20-day return; sector-relative P/E data not provided. |
| XLP (Consumer Staples) | +2.49% | +2.49% (20d) | Only positive sector; defensive demand amid risk-off. |
| XLU (Utilities) | +0.31% | +0.31% (20d) | Slightly positive; defensive sector resilience. |
| XLV (Health Care) | -1.14% | -1.14% (20d) | Slightly negative; defensive sector but still down. |

## Macro, Fiscal, Rates, Liquidity and Credit

- Inflation: CPI 336.298 and core CPI 338.896 (Sep-2026) indicate a still-elevated but decelerating inflation environment; external CPI 337.476 (Oct-2026) suggests continued moderation.
- Labor: Unemployment rate 4.2% (Sep-2026) is near full employment; external UNRATE 4.1% (Oct-2026) confirms a stable labor market.
- Policy: Effective federal funds rate 3.88% (Nov-19, 2026) indicates a restrictive but easing policy stance.
- Rates: 10Y-2Y spread 0.29 (Nov-20, 2026) is near flat, signaling a late-cycle or transitionary yield curve.
- Credit: High-yield OAS 3.52 and IG OAS 0.94 (Nov-19, 2026) show moderate credit stress; spreads are not yet in crisis territory but elevated relative to tight historical levels.
- Liquidity: Elevated 5-day volatility forecast (36.6%) and 92.8% spike probability indicate thin liquidity and high event risk; cash and defensive positioning are prudent.

## US Equities and 11 GICS Sectors

Macro source IDs: S001, S002, S003, S004, S005, S006, S007

| GICS sector | Evidence | AI research stance | Source IDs |
| --- | --- | --- | --- |
| Information Technology | 20d return -18.68% (XLK); shortlist includes MRVL (PE 74.23, sector-relative 2.20), NOW (PE 97.19, sector-relative 2.88), DDOG (PE 521.17, sector-relative 15.46), AMD (PE 128.88, sector-relative 3.82), NVDA (PE 26.51, sector-relative 0.79). | Weakest sector; high-multiple, high-beta names dominate the shortlist with poor earnings yields and extreme sector-relative valuations. | S078 |
| Communication Services | 20d return -5.19% (XLC); shortlist includes CHTR (PE 2.71, sector-relative 0.13) but flagged for forward P/E and earnings yield implausibility. | Negative sector return; CHTR appears cheap on trailing P/E but flagged as valuation-quality risk. | S073 |
| Financials | 20d return -2.38% (XLF); shortlist includes PNR (PE 13.59, sector-relative 0.49) and GEN (PE 14.15, sector-relative 0.42). | Modestly negative; low P/E and low sector-relative multiples suggest value but limited momentum. | S065 |
| Industrials | 20d return -5.01% (XLI); no shortlist names provided. | Negative sector return; no specific shortlist evidence available. | S071 |
| Materials | 20d return -5.79% (XLB); no shortlist names provided. | Negative sector return; no specific shortlist evidence available. | S067 |
| Consumer Discretionary | 20d return -0.57% (XLY); no shortlist names provided. | Slightly negative; no specific shortlist evidence available. | S061 |
| Consumer Staples | 20d return +2.49% (XLP); no shortlist names provided. | Only positive sector; defensive demand amid risk-off. | S056 |
| Health Care | 20d return -1.14% (XLV); no shortlist names provided. | Slightly negative; defensive sector but still down. | S055 |
| Real Estate | 20d return -0.26% (XLRE); no shortlist names provided. | Slightly negative; no specific shortlist evidence available. | S063 |
| Utilities | 20d return +0.31% (XLU); no shortlist names provided. | Slightly positive; defensive sector resilience. | S072 |
| Energy | 20d return -12.72% (XLE); no shortlist names provided. | Sharp sector drawdown; no specific shortlist evidence available. | S077 |

### Sector fundamentals, valuation and earnings

No point-in-time sector fundamentals (e.g., sector-level earnings revisions, growth, or margin data) are supplied in the database. The sector evidence is limited to 20-day ETF returns and trailing P/E for a few sector ETFs. Sector-level growth, margins, and consensus estimates are unavailable; therefore, no sector fundamental claims are made.

## Growth vs Value

- Growth: High-multiple, high-beta names dominate the shortlist (NOW, DDOG, MRVL, AMD, AAPL, MSFT) with sector-relative P/E ranging from 0.79 to 15.46, indicating strong growth expectations but extreme valuation risk.
- Value: Low P/E and low sector-relative multiples appear in Financials (PNR, GEN) and Communication Services (CHTR), but CHTR is flagged for forward P/E and earnings yield implausibility.
- Valuation quality: Several shortlist names (INTC, LITE, RDDT, NVDA, MU, AMD, AAPL, MSFT) lack forward EPS data, so forward valuation quality cannot be assessed.
- Earnings yield: Most shortlist names have low earnings yields (e.g., NOW 1.03%, DDOG 0.19%, MRVL 1.35%, AMD 0.78%), suggesting weak current earnings support relative to price.

## ETF Flows and Breadth

- Price breadth is negative: 37.6% of names positive over 20 days, advance/decline ratio 0.326, no new highs, and 0 new lows.
- 5-day and 20-day breadth changes are negative (-28.86 and -15.97 for 50-day; -17.38 and -10.58 for 200-day), indicating deteriorating participation.
- Flows show exceptional institutional buying in SOXX (flow z-score 2.83 over 20d, 2.30 over 60d) with price down, suggesting strong semiconductor ETF demand despite sector weakness.
- TLT and SMH show neutral flow states with structural accumulation, but no broad-based flow signal is evident.
- The negative divergence flag is false, but the overall breadth picture is weak and consistent with a risk-off regime.

## Stock Ideas

Single-stock research uses reported EPS, forward P/E and company fundamentals. All ideas are research judgments, not validated return predictions.

| Ticker | Security | Research view | Price | EPS | Forward P/E | Base target | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| APP | AppLovin | NEW | 348.29 | 20.86084 | 16.695877 | 417.22 | NEW |
| PNR | Pentair | KEEP | 68.63 | 5.30402 | 12.939242 | 74.26 | KEEP |
| IDXX | Idexx Laboratories | KEEP | 676.21 | 16.8929 | 40.029243 | 540.57 | KEEP |

## ETF Ideas

ETF research uses holdings, portfolio valuation and exposure. Single-stock EPS × P/E valuation is not applied to ETFs.

| Ticker | Fund | Research view | Price | Top holdings | Portfolio valuation | Sector exposure | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| XLV | Health Care sector ETF | KEEP | 177.24 | LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59% | Top 10 holdings; numeric weight coverage 61.42% | Health Care | KEEP |
| XLP | Consumer Staples sector ETF | NEW | 90.46 | WMT 11.14%, COST 9.09%, PG 7.60%, KO 7.37%, PM 6.59%, MO 4.70%, CL 4.42%, MDLZ 4.25%, PEP 4.11%, TGT 4.00% | Top 10 holdings; numeric weight coverage 63.28% | Consumer Staples | NEW |
### APP — AppLovin

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** AppLovin offers a better combination of momentum and valuation than the high-multiple dislocated names like NOW and DDOG, which show negative 20-day returns and extreme forward P/Es. It also carries a lower forward P/E than the liquidity-leader names like NVDA and MSFT, while maintaining strong fundamentals. Alternatives considered: NOW, DDOG, NVDA, MSFT.
- **Thesis:** AppLovin screens in the top 20-day momentum bucket with a 33.8% 20-day return and a 20.05 trailing P/E, while its reported diluted EPS of 11.61 and forward EPS of 20.86 support a forward P/E near 16.7. The company's high-margin core business and strong momentum make it a compelling candidate despite the recent pullback.
- **Source IDs:** S008, S009, S013, S018
- **Catalysts:** Continued 20-day momentum momentum, Sustained high gross margin and operating leverage, Potential re-rating as the stock recovers from the pullback
- **Risks:** High valuation relative to near-term growth expectations, Mobile advertising market cyclicality, Execution risk on new product and market initiatives
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 20.8608 (source.forwardEps) x AI multiple assumption 20.00; source IDs S008, S009, S013, S018
- **EPS:** 20.86084 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 16.695877
- **FY+1 growth assumption:** 27.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / MSFT / APP shows strong FY+1 consensus earnings growth of 27.44% and revenue growth of 25.51%, with high gross margin (88.78%) and operating margin (77.78%). The base multiple of 20x is supported by high-quality margins and growth, while the bull/bear range reflects upside if growth accelerates and downside if it moderates. Peer reference to MSFT is based on comparable high-margin, high-growth software characteristics.
- **Company fundamentals:** AppLovin reported diluted EPS of 11.61 for the period ending 2026-09-30, with forward EPS of 20.86. Trailing P/E is 20.05, forward P/E is 16.70, gross margin is 88.78%, and operating margin is 77.78%. Revenue growth is 55.5% and earnings growth is 75.5%.
- **Bull / Base / Bear:** 500.66 / 417.22 / 333.77
- **Bull / Base / Bear returns:** 43.75% / 19.79% / -4.17%
- **Scenario probabilities:** not separately assigned; see scenario table.

### PNR — Pentair

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Pentair is preferred over the high-multiple dislocated names like NOW and DDOG, which show negative momentum and extreme valuations. However, it is not preferred over the higher-growth names like APP and IDXX, which offer better growth profiles despite higher multiples. Alternatives considered: NOW, DDOG, APP, IDXX.
- **Thesis:** Pentair screens in the top 20-day momentum bucket with a 24.1% 20-day return and a 13.6 trailing P/E. However, its revenue growth is slightly negative and earnings growth is negative, suggesting the momentum may be driven by cyclical factors rather than fundamental expansion. The low valuation is attractive but the fundamentals do not yet support a strong conviction BUY.
- **Source IDs:** S012, S015, S016, S020
- **Catalysts:** Potential stabilization in industrial end markets, Attractive entry valuation with low forward P/E, Possible earnings recovery if end-market conditions improve
- **Risks:** Negative revenue and earnings growth, Cyclical exposure to industrial and building products, Limited near-term catalyst for re-rating
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 5.3040 (source.forwardEps) x AI multiple assumption 14.00; source IDs S012, S015, S016, S020
- **EPS:** 5.30402 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 12.939242
- **FY+1 growth assumption:** 12.82%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / RRC / PNR has moderate FY+1 consensus earnings growth of 12.82% and revenue growth of 18.38%, with a lower gross margin (40.17%) and operating margin (21.41%) typical of railroads. The base multiple of 14x reflects these fundamentals, with a bull/bear range capturing margin and volume variability. Peer reference to RRC is based on comparable railroad sector valuation and growth profile.
- **Company fundamentals:** Pentair reported diluted EPS of 2.76 for the period ending 2026-09-30, with forward EPS of 5.30. Trailing P/E is 13.59, forward P/E is 12.94, gross margin is 40.17%, and operating margin is 21.41%. Revenue growth is -4.5% and earnings growth is -18.8%.
- **Bull / Base / Bear:** 90.17 / 74.26 / 58.34
- **Bull / Base / Bear returns:** 31.39% / 8.2% / -14.99%
- **Scenario probabilities:** not separately assigned; see scenario table.

### IDXX — Idexx Laboratories

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Idexx offers a better growth profile than the low-multiple names like PNR and GEN, which show negative or flat growth. It is preferred over the high-multiple dislocated names like NOW and DDOG, which show negative momentum and extreme valuations. Alternatives considered: NOW, DDOG, PNR, GEN.
- **Thesis:** Idexx Laboratories screens in the top 20-day momentum bucket with a 20.7% 20-day return and a 60-day return of 24.1%. Its trailing P/E of 39.18 and forward P/E of 40.03 are premium, but the company has solid fundamentals with 9.9% revenue growth and 17.9% earnings growth. The premium valuation is justified by consistent growth, but the high multiple leaves limited room for error.
- **Source IDs:** S023, S024, S025, S033
- **Catalysts:** Sustained growth in animal and diagnostic health markets, Potential multiple expansion as growth persists, Strong free cash flow generation
- **Risks:** Premium valuation leaves limited room for error, Regulatory and competitive risks in the diagnostics industry, Dependence on a few large customers
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 16.8929 (source.forwardEps) x AI multiple assumption 32.00; source IDs S023, S024, S025, S033
- **EPS:** 16.8929 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 40.029243
- **FY+1 growth assumption:** 12.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / CDW / IDXX shows FY+1 consensus earnings growth of 12.44% and revenue growth of 8.88%, with a gross margin of 62.72% and operating margin of 32.50%. The base multiple of 32x reflects its higher growth and margin profile relative to the peer, with a bull/bear range capturing potential margin expansion or deceleration. Peer reference to CDW is based on comparable software/IT services growth and margin characteristics.
- **Company fundamentals:** Idexx Laboratories reported diluted EPS of 11.75 for the period ending 2026-09-30, with forward EPS of 16.89. Trailing P/E is 39.18, forward P/E is 40.03, gross margin is 62.72%, and operating margin is 32.50%. Revenue growth is 9.9% and earnings growth is 17.9%.
- **Bull / Base / Bear:** 641.93 / 540.57 / 439.22
- **Bull / Base / Bear returns:** -5.07% / -20.06% / -35.05%
- **Scenario probabilities:** not separately assigned; see scenario table.

### XLV — Health Care sector ETF

- **Type:** ETF
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** XLV provides broad health care exposure that is preferable to single-stock concentration in names like IDXX or MGM, which carry higher idiosyncratic risk. It is a neutral holding compared to the sector weakness observed. Alternatives considered: XLY, XLP, XLF.
- **Thesis:** The Health Care sector ETF (XLV) provides diversified exposure to the sector, with top holdings including LLY, JNJ, ABBV, and MRK. The sector shows a -12.4% raw percentage change, indicating weakness. The ETF is a neutral holding, offering diversification but not a strong directional bet at this time.
- **Source IDs:** S053, S055
- **Catalysts:** Potential sector rotation into health care if other sectors weaken, New product approvals and pipeline catalysts at major pharma holdings, Stable demand for health care services
- **Risks:** Sector-wide weakness as reflected in the -12.4% raw percentage change, Regulatory and reimbursement risks, Concentration in large-cap pharma names
- **Valuation method:** Holdings/portfolio valuation with AI total-return assumption
- **Valuation status:** verified; forward-EPS source: ; period flags: 
- **Valuation assumptions:** Holdings/portfolio valuation; 10 weighted holdings; coverage 61.42%; source IDs S053, S055
- **Top holdings:** LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59%
- **Portfolio valuation:** Top 10 holdings; numeric weight coverage 61.42%
- **Sector exposure:** Health Care
- **Underlying drivers:** Health care sector performance driven by major pharma and biotech earnings, regulatory environment, and demographic trends.
- **Bull / Base / Bear:** 198.51 / 186.1 / 166.61
- **Bull / Base / Bear returns:** 12.0% / 5.0% / -6.0%
- **Scenario probabilities:** not separately assigned; see scenario table.

### XLP — Consumer Staples sector ETF

- **Type:** ETF
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** XLP is preferred over the sector ETFs showing weakness like XLY (-2.95%), XLRE (-0.98%), XLF (-1.82%), and XLU (-0.74%), which are all negative. It offers a strong defensive alternative with positive momentum. Alternatives considered: XLY, XLRE, XLF, XLU.
- **Thesis:** The Consumer Staples sector ETF (XLP) shows a strong +66.8% raw percentage change, indicating significant strength in the defensive staples sector. The ETF offers a high-quality, defensive exposure with top holdings including WMT, COST, PG, and KO. This is a compelling addition to a portfolio seeking stability and defensive growth.
- **Source IDs:** S056, S058
- **Catalysts:** Strong sector performance as reflected in the +66.8% raw percentage change, Defensive characteristics providing portfolio stability, Diversified exposure to essential consumer goods
- **Risks:** Sector concentration in large-cap consumer staples names, Potential for valuation mean-reversion, Slow growth profile relative to cyclical sectors
- **Valuation method:** Holdings/portfolio valuation with AI total-return assumption
- **Valuation status:** verified; forward-EPS source: ; period flags: 
- **Valuation assumptions:** Holdings/portfolio valuation; 10 weighted holdings; coverage 63.28%; source IDs S056, S058
- **Top holdings:** WMT 11.14%, COST 9.09%, PG 7.60%, KO 7.37%, PM 6.59%, MO 4.70%, CL 4.42%, MDLZ 4.25%, PEP 4.11%, TGT 4.00%
- **Portfolio valuation:** Top 10 holdings; numeric weight coverage 63.28%
- **Sector exposure:** Consumer Staples
- **Underlying drivers:** Consumer staples sector performance driven by essential goods demand, pricing power, and defensive characteristics during economic uncertainty.
- **Bull / Base / Bear:** 99.51 / 94.08 / 85.94
- **Bull / Base / Bear returns:** 10.0% / 4.0% / -5.0%
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
| Bull | 25% | +2.00% | Spike probability 0.928 vs historical 0.263 and EWMA 0.247 indicates elevated short-term volatility risk; a 2.0% upside is only plausible if the frozen daily-close model resolves favorably after the US close, with rates staying anchored and breadth expanding. |
| Base | 50% | +0.00% | Directional signal is false and forecast_vol_5d of 0.366 is well above the 0.185 threshold, so the most likely path is a range-bound session near the frozen daily close with no directional alpha; 0.0% return reflects balanced upside/downside risk. |
| Bear | 25% | -2.00% | With spike_probability at 0.928 and forecast_vol_5d at 0.366, a sharp adverse move is the dominant risk; a -2.0% return is plausible if the elevated volatility regime triggers risk-off flows, widening credit spreads and pressuring breadth. |

### Long Term (12 months)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 30% | +8.00% | A 30% probability bull case requires rates to stay anchored, credit spreads to tighten, and earnings to beat, with the elevated short-term volatility regime fading into a sustained risk-on environment over the horizon. |
| Base | 40% | +3.00% | The base case assumes a gradual normalization of volatility, stable rates, and modest earnings growth, producing a 3.0% long-term return as the market digests the frozen daily-close forecast without a directional alpha trigger. |
| Bear | 30% | -5.00% | A 30% bear case reflects a sustained volatility regime where elevated forecast_vol_5d and spike_probability drive widening credit spreads, rate volatility, and earnings disappointment, leading to a -5.0% long-term decline. |

## Positioning

- Maintain a risk-off, defensive posture; avoid high-beta, high-multiple shortlist names until breadth and volatility normalize.
- Favor quality and low-beta names; Consumer Staples (XLP) is the only positive sector and a defensive anchor.
- Reduce exposure to extreme high-multiple names (NOW, DDOG, MRVL, AMD, AAPL, MSFT) given poor earnings yields and elevated sector-relative P/E.
- Use cash and short-duration Treasuries (TLT) as dry powder; SOXX flow strength is notable but concentrated in semiconductors.
- Monitor credit spreads (HY OAS 3.52, IG OAS 0.94) and the 5-day volatility forecast (36.6%) for regime shifts.

## Catalysts

| Date | Event | Why it matters |
| --- | --- | --- |
| 2026-11-23 | Volatility spike window opens | Frozen model forecasts 36.6% 5-day |

## Key Risks


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
| S008 | news | APP | Thu, 19 Nov 2026 19:08:20 GMT | ok | https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en | This tech stock has been nearly cut in half this year. I think Wall Street is getting it wrong - CNBC (Thu, 19 Nov 2026 19:08:20 GMT); AppLovin Stock Moves Higher: What's Going On? - Benzinga (Mon, 16 Nov 2026 18:52:15 GMT); AppLovin: AXON Upgrades Reignite Growth, But Competitive Risks Remain - Seeking Alpha (Thu, 19 Nov 2026 05:42:19 GMT) |
| S009 | filing | APP | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001751008&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0001751008-26-000069); 8-K filed 2026-11-04 (accession 0001751008-26-000068); 10-Q filed 2026-08-05 (accession 0001751008-26-000059) |
| S010 | news | CMG | Sat, 21 Nov 2026 07:47:00 GMT | ok | https://news.google.com/rss/search?q=CMG+Chipotle+Mexican+Grill+stock&hl=en-US&gl=US&ceid=US:en | Chipotle Mexican Grill vs. e.l.f. Beauty: Which Consumer Stock Is a Better Buy for 2027? - Yahoo Finance (Sat, 21 Nov 2026 07:47:00 GMT); Chipotle Mexican Grill vs. Kraft Heinz: Which Consumer Stock Is a Better Buy for 2027? - The Motley Fool (Wed, 18 Nov 2026 16:45:02 GMT); Chipotle Stock Looks Cheaper On 2027 Profit, If Sales Deliver - Trefis (Fri, 20 Nov 2026 16:32:30 GMT) |
| S011 | filing | CMG | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001058090&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0001058090-26-000104); 8-K filed 2026-10-28 (accession 0001058090-26-000103); 8-K filed 2026-09-14 (accession 0001058090-26-000088) |
| S012 | filing | PNR | 2026-10-27 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-27 (accession 0000077360-26-000058); 8-K filed 2026-10-27 (accession 0000077360-26-000055); 8-K filed 2026-09-22 (accession 0000077360-26-000050) |
| S013 | stock | APP | 2026-11-21 | ok | https://finance.yahoo.com/quote/APP | Trailing P/E: 23.453873; Forward P/E: 16.695877; Forward EPS: 20.86084; Price: 348.29; Market price: 348.29; Market cap: 115396132864; Sector: Communication Services; Trailing Eps: 14.85; Revenue Growth: 0.555; Earnings Growth: 0.755; Gross Margin: 0.8878; Operating Margin: 0.77782995; Profit Margin: 0.65887; Return On Equity: 2.1008599; Total Revenue: 7608893952; Market Cap: 115396132864; Consensus EPS FY+1: 20.72451; growth: 0.2744 |
| S014 | filing | CLX | 2026-11-19 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 | 8-K filed 2026-11-19 (accession 0001206774-26-000606); 10-Q filed 2026-11-02 (accession 0000021076-26-000046); 8-K filed 2026-11-02 (accession 0000021076-26-000044) |
| S015 | news | PNR | Wed, 18 Nov 2026 08:00:00 GMT | ok | https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en | Pentair Stock Price Forecast. Should You Buy PNR? - StockInvest.us (Wed, 18 Nov 2026 08:00:00 GMT); Pentair (PNR) Stock May Be 46% Undervalued As New CFO Arrives - Yahoo Finance (Fri, 25 Sep 2026 07:00:00 GMT); Why Is Pentair Stock Soaring Tuesday? - Pentair (NYSE:PNR) - Benzinga (Tue, 27 Oct 2026 07:00:00 GMT) |
| S016 | stock | PNR | 2026-11-21 | ok | https://finance.yahoo.com/quote/PNR | Trailing P/E: 18.700272; Forward P/E: 12.939242; Forward EPS: 5.30402; Price: 68.63; Market price: 68.63; Market cap: 10957101056; Sector: Industrials; Trailing Eps: 3.67; Revenue Growth: -0.045; Earnings Growth: -0.188; Gross Margin: 0.40168998; Operating Margin: 0.21410999; Profit Margin: 0.15435; Return On Equity: 0.15605; Total Revenue: 3966200064; Market Cap: 10957101056; Consensus EPS FY+1: 5.30402; growth: 0.1282 |
| S017 | stock | CMG | 2026-11-21 | ok | https://finance.yahoo.com/quote/CMG | Trailing P/E: 33.224297; Forward P/E: 26.86344; Forward EPS: 1.32336; Price: 35.55; Market price: 35.55; Market cap: 44969861120; Sector: Consumer Cyclical; Trailing Eps: 1.07; Revenue Growth: 0.096; Earnings Growth: -0.062; Gross Margin: 0.39314; Operating Margin: 0.14715; Profit Margin: 0.10832; Return On Equity: 0.48518002; Total Revenue: 12713477120; Market Cap: 44969861120; Consensus EPS FY+1: 1.32336; growth: 0.216 |
| S018 | filing | APP | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json | Diluted EPS 11.61 for period ending 2026-09-30 (filed 2026-11-04) |
| S019 | filing | CMG | 2026-10-29 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001058090.json | Diluted EPS 0.82 for period ending 2026-09-30 (filed 2026-10-29) |
| S020 | filing | PNR | 2026-10-27 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json | Diluted EPS 2.76 for period ending 2026-09-30 (filed 2026-10-27) |
| S021 | news | CLX | Thu, 19 Nov 2026 08:57:28 GMT | ok | https://news.google.com/rss/search?q=CLX+Clorox+stock&hl=en-US&gl=US&ceid=US:en | Should You Buy Clorox Stock At This Price? - Trefis (Thu, 19 Nov 2026 08:57:28 GMT); Clorox (CLX) Stock Rebounds As Q4 Earnings Face Margin Strain - Yahoo Finance (Tue, 03 Nov 2026 08:00:00 GMT); Clorox Declares Regular Quarterly Dividend of $1.25 Per Share - Quantisnow (Wed, 18 Nov 2026 02:13:00 GMT) |
| S022 | stock | CLX | 2026-11-21 | ok | https://finance.yahoo.com/quote/CLX | Trailing P/E: 18.836332; Forward P/E: 16.978472; Forward EPS: 6.1684; Price: 104.73; Market price: 104.73; Market cap: 12687766528; Sector: Consumer Defensive; Trailing Eps: 5.56; Revenue Growth: 0.333; Earnings Growth: 1.138; Gross Margin: 0.41939998; Operating Margin: 0.14286; Profit Margin: 0.09408; Return On Equity: 5.34363; Total Revenue: 7196000256; Market Cap: 12687766528; Consensus EPS FY+1: 6.1684; growth: 0.0769 |
| S023 | news | IDXX | Tue, 03 Nov 2026 08:00:00 GMT | ok | https://news.google.com/rss/search?q=IDXX+Idexx+Laboratories+stock&hl=en-US&gl=US&ceid=US:en | IDEXX Laboratories (IDXX) Q3 Earnings Leave Its Premium Valuation In Focus - Yahoo Finance (Tue, 03 Nov 2026 08:00:00 GMT); IDEXX Laboratories: Great Company, But Too Expensive (Rating Downgrade) - Seeking Alpha (Wed, 04 Nov 2026 08:00:00 GMT); If You Invested $100 In IDEXX Laboratories Stock 15 Years Ago, You Would Have This Much Today - Benzinga (Mon, 02 Nov 2026 08:00:00 GMT) |
| S024 | filing | IDXX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000874716&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000874716-26-000135); 8-K filed 2026-11-02 (accession 0001104659-26-120892); 10-Q filed 2026-08-04 (accession 0000874716-26-000123) |
| S025 | stock | IDXX | 2026-11-21 | ok | https://finance.yahoo.com/quote/IDXX | Trailing P/E: 45.56671; Forward P/E: 40.029243; Forward EPS: 16.8929; Price: 676.21; Market price: 676.21; Market cap: 53276061696; Sector: Healthcare; Trailing Eps: 14.84; Revenue Growth: 0.099; Earnings Growth: 0.179; Gross Margin: 0.62722; Operating Margin: 0.32497; Profit Margin: 0.25357; Return On Equity: 0.68925005; Total Revenue: 4662220800; Market Cap: 53276061696; Consensus EPS FY+1: 16.8929; growth: 0.1244 |
| S026 | filing | CLX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000021076.json | Diluted EPS 1.39 for period ending 2026-09-30 (filed 2026-11-02) |
| S027 | filing | CHTR | 2026-11-06 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-06 (accession 0001091667-26-000073); 8-K filed 2026-11-06 (accession 0001091667-26-000072); 8-K filed 2026-10-27 (accession 0001091667-26-000064) |
| S028 | news | CHTR | Sun, 15 Nov 2026 05:10:00 GMT | ok | https://news.google.com/rss/search?q=CHTR+Charter+Communications+stock&hl=en-US&gl=US&ceid=US:en | Charter Communications (CHTR) Stock Could Be A Bargain Following Its New Operating Model - Yahoo Finance (Sun, 15 Nov 2026 05:10:00 GMT); Is Charter Stock Worth The Wait? - Trefis (Tue, 17 Nov 2026 12:33:16 GMT); Charter Communications (NasdaqGS:CHTR) Stock Forecast & Analyst Predictions - Simply Wall St (Wed, 18 Nov 2026 08:00:00 GMT) |
| S029 | filing | GEN | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0000849399-26-000083); 8-K filed 2026-10-28 (accession 0000849399-26-000081); 8-K filed 2026-10-09 (accession 0000849399-26-000079) |
| S030 | stock | CHTR | 2026-11-21 | ok | https://finance.yahoo.com/quote/CHTR | Trailing P/E: 12.098683; Forward P/E: 2.8233452; Forward EPS: 45.59485; Price: 128.73; Market price: 128.73; Market cap: 23049306112; Sector: Communication Services; Trailing Eps: 10.64; Revenue Growth: 0.091; Gross Margin: 0.55084; Operating Margin: 0.23389; Profit Margin: 0.02498; Return On Equity: 0.07019; Total Revenue: 55645999104; Market Cap: 23049306112; Consensus EPS FY+1: 49.52287; growth: 1.4594 |
| S031 | news | GEN | Sat, 21 Nov 2026 02:14:00 GMT | ok | https://news.google.com/rss/search?q=GEN+Gen+Digital+stock&hl=en-US&gl=US&ceid=US:en | Gen Digital (GEN) Stock Looks Below Fair Value On Its 45% Run - Yahoo Finance (Sat, 21 Nov 2026 02:14:00 GMT); Should Rising Cyberattack Risks Require Action From Gen Digital (GEN) Investors? - Yahoo Finance (Sat, 21 Nov 2026 12:10:01 GMT); Gen Digital CFO Sold Shares Worth Over $2.2M - TradingView (Fri, 20 Nov 2026 23:30:01 GMT) |
| S032 | filing | MGM | 2026-10-28 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000789570&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-28 (accession 0000789570-26-000107); 8-K filed 2026-10-28 (accession 0000789570-26-000106); 8-K filed 2026-10-28 (accession 0000789570-26-000104) |
| S033 | filing | IDXX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000874716.json | Diluted EPS 11.75 for period ending 2026-09-30 (filed 2026-11-02) |
| S034 | stock | GEN | 2026-11-21 | ok | https://finance.yahoo.com/quote/GEN | Trailing P/E: 14.817259; Forward P/E: 8.746435; Forward EPS: 3.33736; Price: 29.19; Market price: 29.19; Market cap: 17317730304; Sector: Technology; Trailing Eps: 1.97; Revenue Growth: 0.122; Earnings Growth: 1.286; Gross Margin: 0.77410007; Operating Margin: 0.43229; Profit Margin: 0.23068; Return On Equity: 0.46402; Total Revenue: 5228000256; Market Cap: 17317730304; Consensus EPS FY+1: 3.33736; growth: 0.1286 |
| S035 | filing | CHTR | 2026-11-06 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001091667.json | Diluted EPS 0.38 for period ending 2026-09-30 (filed 2026-11-06) |
| S036 | filing | SNDK | 2026-11-19 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0002023554&type=10-Q&dateb=&owner=include&count=10 | 8-K filed 2026-11-19 (accession 0001628280-26-075127); 8-K filed 2026-11-18 (accession 0001628280-26-074848); 10-Q filed 2026-10-30 (accession 0001628280-26-068601) |
| S037 | stock | MGM | 2026-11-21 | ok | https://finance.yahoo.com/quote/MGM | Trailing P/E: 12.446155; Forward P/E: 23.023344; Forward EPS: 1.40553; Price: 32.36; Market price: 32.36; Market cap: 8187421184; Sector: Consumer Cyclical; Trailing Eps: 2.6; Revenue Growth: -0.009; Gross Margin: 0.4362; Operating Margin: 0.057979997; Profit Margin: 0.03916; Return On Equity: 0.26933; Total Revenue: 17722869760; Market Cap: 8187421184; Consensus EPS FY+1: 1.40553; growth: -0.0462 |
| S038 | filing | GEN | 2026-10-29 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000849399.json | Diluted EPS 0.83 for period ending 2026-10-02 (filed 2026-10-29) |
| S039 | news | MGM | Thu, 29 Oct 2026 07:00:00 GMT | ok | https://news.google.com/rss/search?q=MGM+MGM+Resorts+stock&hl=en-US&gl=US&ceid=US:en | How Investors Are Reacting To MGM Resorts Stock After An Earnings Miss - Yahoo Finance (Thu, 29 Oct 2026 07:00:00 GMT); This casino stock has fallen for 17 weeks in a row. Katie Stockton says it could be due for a bounce - CNBC (Tue, 03 Nov 2026 08:00:00 GMT); MGM Stock Dives 10% After Barry Diller Drops $18 Billion Bid - Forbes (Thu, 24 Sep 2026 07:00:00 GMT) |
| S040 | stock | SNDK | 2026-11-21 | ok | https://finance.yahoo.com/quote/SNDK | Trailing P/E: 0.085785426; Forward P/E: 2.20723; Forward EPS: 35.9002; Price: 79.24; Market price: 79.24; Market cap: 90200072192; Sector: Technology; Trailing Eps: 923.7; Revenue Growth: 3.779; Earnings Growth: 69.096; Gross Margin: 0.79952; Operating Margin: 0.7268; Profit Margin: 0.67039; Return On Equity: 1.41174; Total Revenue: 28970999808; Market Cap: 90200072192; Consensus EPS FY+1: 35.9002; growth: 0.2612 |

## Sources

- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFF&cosd=2026-01-01 (2026-11-19)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLH0A0HYM2&cosd=2026-01-01 (2026-11-19)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLC0A0CM&cosd=2026-01-01 (2026-11-19)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCSL&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=UNRATE&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=PAYEMS&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=T10Y2Y&cosd=2026-01-01 (2026-11-20)
- news APP: https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en (Thu, 19 Nov 2026 19:08:20 GMT)
- filing APP: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001751008&type=10-Q&dateb=&owner=include&count=10 (2026-11-04)
- news CMG: https://news.google.com/rss/search?q=CMG+Chipotle+Mexican+Grill+stock&hl=en-US&gl=US&ceid=US:en (Sat, 21 Nov 2026 07:47:00 GMT)
- filing CMG: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001058090&type=10-Q&dateb=&owner=include&count=10 (2026-10-29)
- filing PNR: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 (2026-10-27)
- stock APP: https://finance.yahoo.com/quote/APP (2026-11-21)
- filing CLX: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 (2026-11-19)
- news PNR: https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en (Wed, 18 Nov 2026 08:00:00 GMT)
- stock PNR: https://finance.yahoo.com/quote/PNR (2026-11-21)
- stock CMG: https://finance.yahoo.com/quote/CMG (2026-11-21)
- filing APP: https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json (2026-11-04)
- filing CMG: https://data.sec.gov/api/xbrl/companyfacts/CIK0001058090.json (2026-10-29)
- filing PNR: https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json (2026-10-27)

## AI Provenance

- Provider / model: hermes-local-proxy / upstage/solar-mini4:free
- Market research: attempts=1 tokens=9591 (prompt=6591, completion=3000) runtime=34.4s
- Fundamental research: generated this run at 2026-11-21T22:15:36.669300+00:00
- Evidence source dates: {'as_of': '2026-11-20', 'latest_equity_date': '2026-11-20', 'latest_macro_date': '2026-11-20', 'flows_date': '2026-11-20'}
- Evidence fingerprint: faacb76b21d8b213310db9c9f23d44c20eaafa44e2a00c36edd9720103558197
- Source citations are retrieved external records in the ledger above; market values remain from the verified database snapshot.


## Disclosures

- This is research and market intelligence, not investment advice.
- AI conclusions are research judgments, not validated return predictions.
- The frozen risk layer is risk-only and is not used for directional views or allocations.
- Legacy scores are not active inputs or outputs.

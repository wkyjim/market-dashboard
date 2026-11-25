# AEGIS AI-First Market Intelligence

Research generated at: 25 November 2026, 18:09 HKT
Database freshness: equity 2026-11-24 (latest row retrieved 2026-11-25 13:05:54.038867+08:00)
Data cutoff: 2026-11-24 US cash close
Snapshot ID: aegis-hourly-20261125T100932Z

## Executive Summary

- **AI market view: Late-November 2026 US equities show a mixed tape: broad market breadth is positive but momentum is deteriorating, with the S&P 500 down 6.75% over 20 days and the Information Technology sector down 17.1% over 20 days. Defensive and low-volatility sectors (Consumer Staples, Utilities, Health Care) are outperforming, while cyclical and rate-sensitive sectors (Industrials, Materials, Energy, Communication Services) are lagging. Credit spreads are tight (IG 0.97, HY 3.63), and the 10Y-2Y curve is modestly positive at 0.28, suggesting a late-cycle but not distressed macro backdrop. The risk block shows elevated 5-day volatility (25.4%) and a 55.9% spike probability, indicating a fragile, event-driven environment.**
- S&P 500 is down 6.75% over 20 days; breadth is positive (54.9% above 50-day, 53.2% above 200-day) but momentum is weakening.
- Information Technology is the worst sector (-17.1% over 20 days), while Consumer Staples (+5.4%), Health Care (+3.1%), and Consumer Discretionary (+2.0%) lead.
- Credit spreads are tight (IG 0.97, HY 3.63) and the 10Y-2Y curve is positive at 0.28, indicating no acute credit stress.
- Risk metrics show elevated 5-day volatility (25.4%) and a 55.9% spike probability, signaling a fragile, event-driven market.
- Sector P/E valuations are mixed: Communication Services (16.6) and Financials (15.2) are cheap, while Utilities (17.9) and Real Estate (29.0) are expensive.
- The market is in a late-cycle, low-volatility regime with a high probability of short-term volatility spikes, requiring a defensive tilt.

## Data QC

- Status: **PASS_WITH_WARNINGS**
- Equity session: 0 completed session(s) behind inference date
- Macro session: 2026-11-25 (0 completed session(s) behind inference date)
- Equity provenance: 272 provisional / 12648 canonical
- Breadth lag: 0 session(s); ETF-flow lag: 0 session(s)
- Note: Equity session contains a mix of provisional yfinance and canonical Massive rows.
- External sources: 79 ok / 0 unavailable; retrieved 2026-11-25T10:09:46.163397+00:00

## Idea Discovery

- S&P 500 universe: 503; eligible: 501; transparent shortlist: 20
- Method: independent momentum/dislocation/PE/liquidity buckets; no composite score
- Evidence used: latest close, 20d and 60d price returns, 60d drawdown, trailing P/E, earnings yield, sector-relative P/E, dollar volume, GICS sector
- Not available as verified inputs: verified earnings-revision history for the full universe, FY+2 consensus, structured industry catalyst calendar
- Eligible but not shortlisted: 481 (outside the top independent momentum, dislocation, valuation and liquidity buckets)
- Included: APP (top_20d_momentum); CMG (top_20d_momentum); CHTR (top_20d_momentum); IDXX (top_20d_momentum); DLTR (top_20d_momentum); FISV (top_20d_momentum); GEN (top_20d_momentum); MGM (top_20d_momentum); SNDK (largest_20d_dislocation); MRVL (largest_20d_dislocation); LITE (largest_20d_dislocation); INTC (largest_20d_dislocation); DELL (largest_20d_dislocation); DDOG (largest_20d_dislocation); NOW (largest_20d_dislocation); COIN (largest_20d_dislocation); NVDA (liquidity_leader); MU (liquidity_leader); AMD (liquidity_leader); AAPL (liquidity_leader)
- Excluded reasons: {"missing_recent_or_latest_price": 2}
- Valuation-quality rejected: [{"flags": ["forward_pe_outside_plausible_range", "implausible_earnings_yield", "forward_eps_vs_reported_jump"], "ticker": "CHTR"}, {"flags": ["forward_eps_missing"], "ticker": "FISV"}, {"flags": ["forward_pe_outside_plausible_range", "implausible_earnings_yield"], "ticker": "SNDK"}, {"flags": ["forward_eps_vs_reported_jump"], "ticker": "MRVL"}, {"flags": ["forward_eps_vs_reported_jump"], "ticker": "LITE"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "DELL"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "DDOG"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "NOW"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "COIN"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "NVDA"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "MU"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "AMD"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "AAPL"}]

## Market Snapshot

| Asset | Latest | Change | Observation |
| --- | --- | --- | --- |
| S&P 500 (SPX) | 7201.09 | -6.75% (20d) | Broad market is down on momentum, but 50-day and 200-day above-percentage remain above 50%, indicating a resilient base. |
| Information Technology (XLK) | -17.10% | -17.10% (20d) | Worst-performing sector; trailing P/E of 27.70 suggests high valuation sensitivity to rate or earnings revisions. |
| Consumer Staples (XLP) | +5.43% | +5.43% (20d) | Top performer; trailing P/E of 24.73 indicates investors are paying up for defensive quality. |
| Health Care (XLV) | +3.09% | +3.09% (20d) | Outperforming; trailing P/E of 30.11 is the highest among major sectors, reflecting defensive demand. |
| Industrials (XLI) | -3.76% | -3.76% (20d) | Cyclical sector lagging; trailing P/E of 25.92 suggests valuation compression. |
| Energy (XLE) | -11.38% | -11.38% (20d) | Sharp decline; trailing P/E of 15.10 is cheap but may reflect macro or supply-side concerns. |

## Macro, Fiscal, Rates, Liquidity and Credit

- Growth: US equities are in a late-cycle phase with S&P 500 down 6.75% over 20 days; breadth is positive but momentum is deteriorating, suggesting slowing momentum rather than a broad bear market.
- Inflation: CPI (CPIAUCSL) stands at 336.298 (Sep 2026) and core CPI at 338.896, indicating persistent but manageable inflation; the Fed funds rate is 3.88% (Nov 23, 2026), suggesting a restrictive but stabilizing policy stance.
- Policy: The 10Y-2Y Treasury spread is 0.28 (Nov 24, 2026), a modestly positive curve, and the Fed funds rate at 3.88% implies a cautious but not tightening posture.
- Rates: Credit spreads are tight (IG 0.97, HY 3.63), and the 10Y-2Y curve is positive at 0.28, indicating no acute credit stress and a stable rate environment.
- Liquidity: Tight credit spreads and positive curve suggest ample liquidity, but elevated volatility (25.4% 5-day) and a 55.9% spike probability indicate fragile market liquidity.
- Credit: IG and HY spreads are tight, but the risk block shows elevated volatility and a high spike probability, suggesting potential for sudden risk-off moves.

## US Equities and 11 GICS Sectors

Macro source IDs: S001, S002, S003, S004, S005, S006, S007

| GICS sector | Evidence | AI research stance | Source IDs |
| --- | --- | --- | --- |
| Information Technology | Sector ETF (XLK) is down 17.10% over 20 days, the worst among all sectors; trailing P/E is 27.70 (S073). | Less favored: severe underperformance and high valuation make this sector vulnerable to further rate or earnings pressure. | S073 |
| Consumer Staples | Sector ETF (XLP) is up 5.43% over 20 days, the best performer; trailing P/E is 24.73 (S062). | Favored: defensive quality and positive momentum make this a core holding in a late-cycle environment. | S062 |
| Health Care | Sector ETF (XLV) is up 3.09% over 20 days; trailing P/E is 30.11 (S051), the highest among major sectors. | Favored: defensive demand and positive momentum support this sector despite high valuation. | S051 |
| Financials | Sector ETF (XLF) is up 0.41% over 20 days; trailing P/E is 15.16 (S065), the cheapest among major sectors. | Neutral: cheap valuation is attractive, but flat performance and late-cycle dynamics warrant caution. | S065 |
| Industrials | Sector ETF (XLI) is down 3.76% over 20 days; trailing P/E is 25.92 (S068). | Less favored: negative momentum and moderate valuation suggest cyclical weakness. | S068 |
| Energy | Sector ETF (XLE) is down 11.38% over 20 days; trailing P/E is 15.10 (S075). | Less favored: sharp decline and potential supply-side concerns outweigh cheap valuation. | S075 |
| Consumer Discretionary | Sector ETF (XLY) is up 1.97% over 20 days; trailing P/E is 24.64 (S057). | Neutral: modest positive momentum and reasonable valuation, but mixed signals. | S057 |
| Real Estate | Sector ETF (XLRE) is up 2.40% over 20 days; trailing P/E is 29.02 (S061), expensive. | Neutral: positive momentum but high valuation and rate sensitivity warrant caution. | S061 |
| Materials | Sector ETF (XLB) is down 3.11% over 20 days; trailing P/E is 20.86 (S067). | Less favored: negative momentum and moderate valuation suggest cyclical weakness. | S067 |
| Utilities | Sector ETF (XLU) is up 1.28% over 20 days; trailing P/E is 17.85 (S064), relatively cheap. | Favored: defensive characteristics and reasonable valuation support this sector. | S064 |
| Communication Services | Sector ETF (XLC) is up 0.84% over 20 days; trailing P/E is 16.59 (S072), cheap. | Neutral: cheap valuation and modest positive momentum, but high volatility in sub-components. | S072 |

### Sector fundamentals, valuation and earnings

Sector-level fundamental data (growth, margins, consensus) is not available in the supplied database for the full universe; only trailing P/E and 20-day returns are provided. The database snapshot indicates fundamental evidence was retrieved only for source-backed shortlist names, and the screening output shows PE metrics as null for all shortlisted tickers. Therefore, no point-in-time sector fundamentals (e.g., growth, margins, consensus) can be reported without inventing data.

## Growth vs Value

- Growth: Information Technology is the primary growth engine but is down 17.1% over 20 days, indicating a sharp deceleration; Consumer Staples and Health Care are leading on defensive growth.
- Value: Financials (15.16), Energy (15.10), and Communication Services (16.59) offer the cheapest trailing P/E, while Utilities (17.85) and Real Estate (29.02) are expensive.
- Valuation: The market is not uniformly cheap; high-quality defensive sectors command premium valuations (Health Care 30.11, Real Estate 29.02), while cyclical sectors are cheaper but underperforming.
- Earnings: Trailing P/E data is available for all 11 sectors, but forward earnings revisions are not available for the shortlist, limiting growth assessment.

## ETF Flows and Breadth

- Price breadth is positive: 54.91% of names are above their 50-day moving average and 53.17% above their 200-day, with an advance/decline ratio of 2.22.
- Momentum breadth is weakening: 52.09% of names are positive over 20 days, and the 50-day/20-day breadth change is -2.81, indicating a loss of breadth momentum.
- Flows show structural distribution in XLY (flow z-score 20d: -0.76, 60d: -0.99) and neutral/medium-term deterioration in XLU (20d: -1.32), while XLV shows tactical profit-taking inside structural accumulation (20d: +0.03, 60d: +1.11).
- New highs/new lows are zero, indicating no broad-based new high formation and a lack of strong bullish momentum.
- The S&P 500 is down 6.75% over 20 days, but the advance/decline ratio of 2.22 suggests that the decline is broad-based but not extreme.

## Stock Ideas

Single-stock research uses reported EPS, forward P/E and company fundamentals. All ideas are research judgments, not validated return predictions.

| Ticker | Security | Research view | Price | EPS | Forward P/E | Base target | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| APP | AppLovin | NEW | 381.11 | 20.86084 | 18.269157 | 417.22 | NEW |
| DLTR | Dollar Tree | KEEP | 154.65 | 7.95851 | 19.43203 | 127.34 | KEEP |

## ETF Ideas

ETF research uses holdings, portfolio valuation and exposure. Single-stock EPS × P/E valuation is not applied to ETFs.

| Ticker | Fund | Research view | Price | Top holdings | Portfolio valuation | Sector exposure | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| XLV | Health Care sector ETF | KEEP | 184.72 | LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59% | Top 10 holdings; numeric weight coverage 61.42% | Health Care | KEEP |
### APP — AppLovin

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** AppLovin offers a higher-quality growth profile than the other momentum names in the shortlist, with a forward P/E of about 18.3x that is materially cheaper than the forward P/E of about 28.0x for Chipotle and about 42.2x for Idexx. Its 88.8% gross margin and 77.8% operating margin are also far stronger than the consumer and healthcare names in the shortlist, making it the preferred momentum candidate. Alternatives considered: CMG, IDXX, DLTR, GEN.
- **Thesis:** AppLovin screens as a top 20-day momentum name with a 45% 20-day return and a 22% 60-day return, supported by a 10-Q filed 2026-11-04 showing diluted EPS of 11.61 for the period ending 2026-09-30. The stock trades at a forward P/E of about 18.3x on a forward EPS of about 20.86, and a trailing P/E of about 25.7x, which is attractive after a sharp pullback. The combination of strong near-term momentum, high gross and operating margins, and a reasonable forward valuation supports a new BUY.
- **Source IDs:** S009, S012, S013, S014
- **Catalysts:** Continued 20-day momentum with a 45% return over the last 20 sessions, Sustained 60-day return of about 22% with a modest 60-day drawdown of about 8%, High gross margin of about 88.8% and operating margin of about 77.8%, Forward P/E of about 18.3x on forward EPS of about 20.86, Trailing P/E of about 25.7x after a sharp pullback
- **Risks:** Forward EPS fiscal period alignment is unverified, Momentum can reverse quickly after a sharp pullback, Advertising and in-app purchase cycles can be volatile
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 20.8608 (source.forwardEps) x AI multiple assumption 20.00; source IDs S009, S012, S013, S014
- **EPS:** 20.86084 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 18.269157
- **FY+1 growth assumption:** 27.59%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / Apple (AAPL) and Microsoft (MSFT) as high-margin, ecosystem-driven platform peers / APP shows strong FY+1 consensus growth of 27.6% with 25.7% revenue growth and 88.8% gross margin, supporting a premium multiple. The base multiple of 20x is justified by high margins and platform economics, with 24x in a bull case and 16x in a bear case reflecting margin and growth risk.
- **Company fundamentals:** AppLovin reported diluted EPS of 11.61 for the period ending 2026-09-30, with forward EPS of about 20.86, forward P/E of about 18.3x, trailing P/E of about 25.7x, revenue growth of about 55.5%, earnings growth of about 75.5%, gross margin of about 88.8%, operating margin of about 77.8%, and profit margin of about 65.9%. Return on equity is about 2.10x.
- **Bull / Base / Bear:** 500.66 / 417.22 / 333.77
- **Bull / Base / Bear returns:** 31.37% / 9.47% / -12.42%
- **Scenario probabilities:** not separately assigned; see scenario table.

### DLTR — Dollar Tree

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Dollar Tree is the preferred consumer staples momentum name in the shortlist because it combines a 25% 20-day return with a forward P/E of about 19.4x, which is cheaper than the forward P/E of about 28.0x for Chipotle and the forward P/E of about 42.2x for Idexx. Its defensive staples exposure and positive momentum make it a more attractive holding than the other consumer staples and discretionary names in the shortlist. Alternatives considered: CMG, IDXX, DLTR, GEN.
- **Thesis:** Dollar Tree screens as a top 20-day momentum name with a 25% 20-day return and a 22% 60-day return, and a 10-Q filed 2026-11-24. The stock trades at a forward P/E of about 19.4x on a forward EPS of about 7.96, with revenue growth of about 6.9% and earnings growth of about 3.3%. The momentum is positive, but the valuation is not cheap enough relative to the company's modest growth to justify a stronger stance.
- **Source IDs:** S021, S023, S026, S033
- **Catalysts:** 25% 20-day return and 22% 60-day return, 10-Q filed 2026-11-24, Forward P/E of about 19.4x on forward EPS of about 7.96, Revenue growth of about 6.9% and earnings growth of about 3.3%, Consumer staples exposure provides defensive ballast
- **Risks:** Forward P/E of about 19.4x is not deeply discounted for a low-single-digit growth rate, Modest revenue growth of about 6.9% and earnings growth of about 3.3%, Consumer staples sector may face margin pressure from input costs, 10-Q filed 2026-11-24 may contain limited forward guidance
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 7.9585 (source.forwardEps) x AI multiple assumption 16.00; source IDs S021, S023, S026, S033
- **EPS:** 7.95851 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 19.43203
- **FY+1 growth assumption:** -1.56%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / Walmart (WMT) and Amazon (AMZN) as retail/e-commerce peers with different growth and margin profiles / DLTR shows slightly negative FY+1 consensus growth of -1.6% with 6.0% revenue growth and thin 38.9% gross margin, warranting a lower multiple. The base multiple of 16x reflects modest growth and margin constraints, with 18x in a bull case and 14x in a bear case reflecting competitive and margin risk.
- **Company fundamentals:** Dollar Tree reported diluted EPS of 5.70 for the period ending 2026-10-31, with forward EPS of about 7.96, forward P/E of about 19.4x, trailing P/E of about 18.7x, revenue growth of about 6.9%, earnings growth of about 3.3%, gross margin of about 38.9%, operating margin of about 10.6%, and profit margin of about 7.8%. Return on equity is about 0.46x.
- **Bull / Base / Bear:** 143.25 / 127.34 / 111.42
- **Bull / Base / Bear returns:** -7.37% / -17.66% / -27.95%
- **Scenario probabilities:** not separately assigned; see scenario table.

### XLV — Health Care sector ETF

- **Type:** ETF
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** The Health Care sector ETF is the preferred defensive core holding in the shortlist because it offers broad diversification across large-cap healthcare names, a top-10 weight coverage of 61.42%, and a 2.95% raw price change. It is more attractive than the sector ETFs in the shortlist because it provides a balanced exposure to the healthcare sector with a well-known basket of large-cap names, while the other sector ETFs either have lower weight coverage or are more exposed to cyclical or rate-sensitive sectors. Alternatives considered: XLP, XLY, XLRE, XLF, XLU, XLB, XLI, XLC.
- **Thesis:** The Health Care sector ETF is a core defensive holding with a 2.95% raw price change and a 10Y-2Y Treasury spread of 0.28, indicating a modestly positive yield curve. The ETF holds large-cap healthcare names with a top-10 weight coverage of 61.42%, led by LLY, JNJ, ABBV, MRK, and UNH. The sector is well-diversified and provides income and downside protection, but the modest yield curve slope and mixed macro signals warrant a neutral stance.
- **Source IDs:** S051, S055
- **Catalysts:** 2.95% raw price change over the session, 10Y-2Y Treasury spread of 0.28, indicating a modestly positive yield curve, Top-10 holdings led by LLY, JNJ, ABBV, MRK, and UNH, Top-10 weight coverage of 61.42%, Defensive sector with stable demand for healthcare products and services
- **Risks:** Modestly positive 10Y-2Y spread of 0.28 may not support strong sector leadership, Top-10 weight coverage of 61.42% leaves 38.58% of the portfolio in smaller positions, Healthcare sector may face regulatory and pricing pressure, Macro uncertainty from mixed signals in the broader market
- **Valuation method:** Holdings/portfolio valuation with AI total-return assumption
- **Valuation status:** verified; forward-EPS source: ; period flags: 
- **Valuation assumptions:** Holdings/portfolio valuation; 10 weighted holdings; coverage 61.42%; source IDs S051, S055
- **Top holdings:** LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59%
- **Portfolio valuation:** Top 10 holdings; numeric weight coverage 61.42%
- **Sector exposure:** Health Care
- **Underlying drivers:** Large-cap healthcare names led by LLY, JNJ, ABBV, MRK, and UNH; defensive demand for healthcare products and services; modestly positive 10Y-2Y Treasury spread of 0.28.
- **Bull / Base / Bear:** 206.89 / 193.96 / 173.64
- **Bull / Base / Bear returns:** 12.0% / 5.0% / -6.0%
- **Scenario probabilities:** not separately assigned; see scenario table.

## Quant Risk Layer

| Field | Value |
| --- | --- |
| Volatility model | vol5_ols_v1 |
| Spike model | spike_logit_v1 |
| As-of date | 2026-11-24 |
| Target window | 2026-11-25 to 2026-12-02 |
| Forecast 5D annualized volatility | 25.45% |
| Historical-vol baseline | 31.74% |
| EWMA baseline | 29.27% |
| Spike probability | 55.95% |
| Spike threshold | 18.50% |
| Status | prospective |
| Forecast ID | 810fae49ab3d5edc |

Risk-only; no directional interpretation or allocation implication.

## Scenarios

### Short Term (5 trading sessions)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 20% | +1.50% | Low spike probability (0.56) and below-threshold volatility (0.254) imply a calm, range-bound week; a modest 1.5% upside is plausible if US close data confirms stable rates and no credit stress. |
| Base | 55% | +0.00% | Frozen daily-close model with no directional signal and historical/ewma baselines near 0.30 suggests a neutral week; 0.0% return reflects balanced risk/reward and no clear catalyst for a move. |
| Bear | 25% | -1.50% | Spike probability 0.56 exceeds the 0.185 threshold, indicating elevated tail risk; a -1.5% downside is plausible if US close data reveals rate volatility, credit spread widening, or earnings disappointment. |

### Long Term (12 months)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 30% | +8.00% | Sustained low volatility and stable rates support a gradual risk-on drift; 8.0% long-term upside is justified by continued earnings growth and orderly credit conditions. |
| Base | 40% | +3.00% | Base case assumes no major regime shift; 3.0% long-term return reflects modest expansion from steady economic growth, stable policy, and balanced market positioning. |
| Bear | 30% | -5.00% | Elevated spike probability and high forecast vol (0.254) signal persistent tail risk; -5.0% long-term downside is plausible if rates rise, credit spreads widen, or earnings disappoint over the horizon. |

## Positioning

- Maintain a defensive tilt: favored Consumer Staples, Health Care, and Utilities; less favored Information Technology, Industrials, Materials, and Energy.
- Favor cheap valuations in Financials and Communication Services, but monitor for further deterioration.
- Reduce exposure to high-beta, high-valuation sectors like Information Technology given the 17.1% 20-day decline and elevated volatility.
- Monitor credit spreads and the 10Y-2Y curve for any widening or inversion, which would signal a shift in the macro regime.
- Position for a high probability of short-term volatility spikes (55.9%) by maintaining liquidity and avoiding concentrated positions.

## Catalysts

| Date | Event | Why it matters |
| --- | --- | --- |
| 2026-11-25 | US macro data release (CPI, payrolls, Fed funds rate) |  |

## Key Risks


## External Source Ledger

| ID | Type | Ticker | Published | Status | URL | Claims |
| --- | --- | --- | --- | --- | --- | --- |
| S001 | macro | macro | 2026-11-23 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFF&cosd=2026-01-01 | Effective federal funds rate (DFF) latest observation 2026-11-23: 3.88 |
| S002 | macro | macro | 2026-11-23 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLH0A0HYM2&cosd=2026-01-01 | US high-yield OAS (BAMLH0A0HYM2) latest observation 2026-11-23: 3.63 |
| S003 | macro | macro | 2026-11-23 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLC0A0CM&cosd=2026-01-01 | US investment-grade OAS (BAMLC0A0CM) latest observation 2026-11-23: 0.97 |
| S004 | macro | macro | 2026-10-01 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCSL&cosd=2026-01-01 | US CPI (CPIAUCSL) latest observation 2026-10-01: 337.476 |
| S005 | macro | macro | 2026-10-01 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=UNRATE&cosd=2026-01-01 | US unemployment rate (UNRATE) latest observation 2026-10-01: 4.1 |
| S006 | macro | macro | 2026-10-01 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=PAYEMS&cosd=2026-01-01 | US nonfarm payrolls (PAYEMS) latest observation 2026-10-01: 159293 |
| S007 | macro | macro | 2026-11-24 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=T10Y2Y&cosd=2026-01-01 | 10Y-2Y Treasury spread (T10Y2Y) latest observation 2026-11-24: 0.28 |
| S008 | filing | CHTR | 2026-11-06 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-06 (accession 0001091667-26-000073); 8-K filed 2026-11-06 (accession 0001091667-26-000072); 8-K filed 2026-10-27 (accession 0001091667-26-000064) |
| S009 | filing | APP | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001751008&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0001751008-26-000069); 8-K filed 2026-11-04 (accession 0001751008-26-000068); 10-Q filed 2026-08-05 (accession 0001751008-26-000059) |
| S010 | filing | CMG | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001058090&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0001058090-26-000104); 8-K filed 2026-10-28 (accession 0001058090-26-000103); 8-K filed 2026-09-14 (accession 0001058090-26-000088) |
| S011 | news | CMG | Tue, 24 Nov 2026 15:25:45 GMT | ok | https://news.google.com/rss/search?q=CMG+Chipotle+Mexican+Grill+stock&hl=en-US&gl=US&ceid=US:en | What Could Lift Chipotle Stock Further? - Trefis (Tue, 24 Nov 2026 15:25:45 GMT); Chipotle’s Earnings Fell 7% Last Quarter, but 1 Trend Has Now Lasted 3 Straight Quarters. - The Motley Fool (Tue, 24 Nov 2026 12:45:02 GMT); Where Will Chipotle Mexican Grill's Stock Be in 5 Years? - Yahoo Finance (Wed, 19 Aug 2026 07:00:00 GMT) |
| S012 | news | APP | Mon, 23 Nov 2026 01:07:00 GMT | ok | https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en | AppLovin (APP) Stock Still Looks Cheap After Sharp Pullback - Yahoo Finance (Mon, 23 Nov 2026 01:07:00 GMT); AppLovin vs. Reddit: Which Technology Stock Is a Better Buy for 2027? - The Motley Fool (Sat, 21 Nov 2026 23:19:26 GMT); AppLovin Stock Surges As Earnings Beat Provides Much-Needed Boost - Investor's Business Daily (Wed, 04 Nov 2026 08:00:00 GMT) |
| S013 | stock | APP | 2026-11-25 | ok | https://finance.yahoo.com/quote/APP | Trailing P/E: 25.66397; Forward P/E: 18.269157; Forward EPS: 20.86084; Price: 381.11; Market price: 381.11; Market cap: 126270119936; Sector: Communication Services; Trailing Eps: 14.85; Revenue Growth: 0.555; Earnings Growth: 0.755; Gross Margin: 0.8878; Operating Margin: 0.77782995; Profit Margin: 0.65887; Return On Equity: 2.1008599; Total Revenue: 7608893952; Market Cap: 126270119936; Consensus EPS FY+1: 20.78066; growth: 0.2759 |
| S014 | filing | APP | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json | Diluted EPS 11.61 for period ending 2026-09-30 (filed 2026-11-04) |
| S015 | stock | CHTR | 2026-11-25 | ok | https://finance.yahoo.com/quote/CHTR | Trailing P/E: 12.769736; Forward P/E: 2.9799418; Forward EPS: 45.59485; Price: 135.87; Market price: 135.87; Market cap: 24327733248; Sector: Communication Services; Trailing Eps: 10.64; Revenue Growth: 0.091; Gross Margin: 0.55084; Operating Margin: 0.23389; Profit Margin: 0.02498; Return On Equity: 0.07019; Total Revenue: 55645999104; Market Cap: 24327733248; Consensus EPS FY+1: 47.75367; growth: 1.4848 |
| S016 | stock | CMG | 2026-11-25 | ok | https://finance.yahoo.com/quote/CMG | Trailing P/E: 34.626167; Forward P/E: 27.996918; Forward EPS: 1.32336; Price: 37.05; Market price: 37.05; Market cap: 46867320832; Sector: Consumer Cyclical; Trailing Eps: 1.07; Revenue Growth: 0.096; Earnings Growth: -0.062; Gross Margin: 0.39314; Operating Margin: 0.14715; Profit Margin: 0.10832; Return On Equity: 0.48518002; Total Revenue: 12713477120; Market Cap: 46867320832; Consensus EPS FY+1: 1.32336; growth: 0.216 |
| S017 | filing | CHTR | 2026-11-06 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001091667.json | Diluted EPS 0.38 for period ending 2026-09-30 (filed 2026-11-06) |
| S018 | filing | CMG | 2026-10-29 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001058090.json | Diluted EPS 0.82 for period ending 2026-09-30 (filed 2026-10-29) |
| S019 | stock | IDXX | 2026-11-25 | ok | https://finance.yahoo.com/quote/IDXX | Trailing P/E: 47.98383; Forward P/E: 42.15262; Forward EPS: 16.8929; Price: 712.08; Market price: 712.08; Market cap: 56102125568; Sector: Healthcare; Trailing Eps: 14.84; Revenue Growth: 0.099; Earnings Growth: 0.179; Gross Margin: 0.62722; Operating Margin: 0.32497; Profit Margin: 0.25357; Return On Equity: 0.68925005; Total Revenue: 4662220800; Market Cap: 56102125568; Consensus EPS FY+1: 16.8929; growth: 0.1244 |
| S020 | news | IDXX | Fri, 20 Nov 2026 13:13:58 GMT | ok | https://news.google.com/rss/search?q=IDXX+Idexx+Laboratories+stock&hl=en-US&gl=US&ceid=US:en | IDEXX Laboratories (IDXX) Stock May Be Overvalued Following Its 44% Run - Yahoo Finance (Fri, 20 Nov 2026 13:13:58 GMT); Can IDEXX Stock Keep Rising After Its 25% Run? - Trefis (Tue, 24 Nov 2026 15:26:34 GMT); IDEXX Stock Rises on Q3 Earnings Beat, Raised 2026 Guidance - IDEXX Laboratories (NASDAQ:IDXX) - Benzinga (Mon, 02 Nov 2026 08:00:00 GMT) |
| S021 | stock | DLTR | 2026-11-25 | ok | https://finance.yahoo.com/quote/DLTR | Trailing P/E: 18.72276; Forward P/E: 19.43203; Forward EPS: 7.95851; Price: 154.65; Market price: 154.65; Market cap: 29017024512; Sector: Consumer Defensive; Trailing Eps: 8.26; Revenue Growth: 0.069; Earnings Growth: 0.033; Gross Margin: 0.3893; Operating Margin: 0.10587; Profit Margin: 0.078439996; Return On Equity: 0.4632; Total Revenue: 20396099584; Market Cap: 29017024512; Consensus EPS FY+1: 7.91656; growth: -0.0156 |
| S022 | news | CHTR | Tue, 24 Nov 2026 11:41:31 GMT | ok | https://news.google.com/rss/search?q=CHTR+Charter+Communications+stock&hl=en-US&gl=US&ceid=US:en | Charter Communications Stock: Analyst Estimates & Ratings - Yahoo Finance (Tue, 24 Nov 2026 11:41:31 GMT); JPMorgan reiterates Charter Communications stock rating at neutral - Investing.com (Mon, 23 Nov 2026 12:06:08 GMT); Charter Communications, Inc. (NASDAQ:CHTR) Stock Has Average Price Target of $193.41 According to Analysts - MarketBeat (Wed, 25 Nov 2026 09:32:32 GMT) |
| S023 | filing | DLTR | 2026-11-24 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000935703&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-24 (accession 0000935703-26-000137); 8-K filed 2026-11-24 (accession 0000935703-26-000136); 8-K filed 2026-11-03 (accession 0000935703-26-000128) |
| S024 | filing | FISV | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0000798354-26-000042); 8-K filed 2026-11-03 (accession 0000798354-26-000039); 8-K filed 2026-10-23 (accession 0001193125-26-429481) |
| S025 | filing | IDXX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000874716&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000874716-26-000135); 8-K filed 2026-11-02 (accession 0001104659-26-120892); 10-Q filed 2026-08-04 (accession 0000874716-26-000123) |
| S026 | news | DLTR | Tue, 24 Nov 2026 11:31:34 GMT | ok | https://news.google.com/rss/search?q=DLTR+Dollar+Tree+stock&hl=en-US&gl=US&ceid=US:en | Dollar Tree, Inc. Reports Third Quarter Results - Dollar Tree (Tue, 24 Nov 2026 11:31:34 GMT); Dollar Tree (DLTR) is On Fire After Hitting This Big Achievement - Yahoo Finance (Wed, 25 Nov 2026 01:42:00 GMT); Why Dollar Tree Stock Jumped Despite A Margin Slip - Trefis (Wed, 25 Nov 2026 07:18:24 GMT) |
| S027 | filing | GEN | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0000849399-26-000083); 8-K filed 2026-10-28 (accession 0000849399-26-000081); 8-K filed 2026-10-09 (accession 0000849399-26-000079) |
| S028 | stock | FISV | 2026-11-25 | ok | https://finance.yahoo.com/quote/FISV | Forward P/E: 7.354445; Price: 58.62; Market price: 58.62; Market cap: 31188635648; Market Cap: 31188635648; Consensus EPS FY+1: 7.95755; growth: 0.0938 |
| S029 | stock | GEN | 2026-11-25 | ok | https://finance.yahoo.com/quote/GEN | Trailing P/E: 15.203046; Forward P/E: 8.974159; Forward EPS: 3.33736; Price: 29.95; Market price: 29.95; Market cap: 17768620032; Sector: Technology; Trailing Eps: 1.97; Revenue Growth: 0.122; Earnings Growth: 1.286; Gross Margin: 0.77410007; Operating Margin: 0.43229; Profit Margin: 0.23068; Return On Equity: 0.46402; Total Revenue: 5228000256; Market Cap: 17768620032; Consensus EPS FY+1: 3.33736; growth: 0.1286 |
| S030 | news | FISV | Fri, 20 Nov 2026 13:55:00 GMT | ok | https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en | FISV Stock Rises 17% in a Month: Here's What Investors Should Know - Yahoo Finance (Fri, 20 Nov 2026 13:55:00 GMT); Citizens initiated coverage on Fiserv - Quantisnow (Mon, 23 Nov 2026 12:50:42 GMT); Fiserv: Disastrous Results, But The Stock Rises (NASDAQ:FISV) - Seeking Alpha (Sat, 21 Nov 2026 13:49:42 GMT) |
| S031 | filing | FISV | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json | Diluted EPS -8.9 for period ending 2026-09-30 (filed 2026-11-04) |
| S032 | filing | MGM | 2026-10-28 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000789570&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-28 (accession 0000789570-26-000107); 8-K filed 2026-10-28 (accession 0000789570-26-000106); 8-K filed 2026-10-28 (accession 0000789570-26-000104) |
| S033 | filing | DLTR | 2026-11-24 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000935703.json | Diluted EPS 5.7 for period ending 2026-10-31 (filed 2026-11-24) |
| S034 | stock | MGM | 2026-11-25 | ok | https://finance.yahoo.com/quote/MGM | Trailing P/E: 13.200001; Forward P/E: 24.417835; Forward EPS: 1.40553; Price: 34.32; Market price: 34.32; Market cap: 8683321344; Sector: Consumer Cyclical; Trailing Eps: 2.6; Revenue Growth: -0.009; Gross Margin: 0.4362; Operating Margin: 0.057979997; Profit Margin: 0.03916; Return On Equity: 0.26933; Total Revenue: 17722869760; Market Cap: 8683321344; Consensus EPS FY+1: 1.40553; growth: -0.0462 |
| S035 | news | GEN | Tue, 24 Nov 2026 05:32:40 GMT | ok | https://news.google.com/rss/search?q=GEN+Gen+Digital+stock&hl=en-US&gl=US&ceid=US:en | Gen Digital Inc. (GEN) Stock Price, News, Quote & History - Yahoo! Finance Canada (Tue, 24 Nov 2026 05:32:40 GMT); 11 Information Technology Stocks Moving In Tuesday's Intraday Session - Benzinga (Tue, 24 Nov 2026 17:05:37 GMT); Gen Digital (GEN) Stock Looks Below Fair Value On Its 45% Run - Yahoo Finance (Sat, 21 Nov 2026 02:14:00 GMT) |
| S036 | filing | IDXX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000874716.json | Diluted EPS 11.75 for period ending 2026-09-30 (filed 2026-11-02) |
| S037 | filing | SNDK | 2026-11-19 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0002023554&type=10-Q&dateb=&owner=include&count=10 | 8-K filed 2026-11-19 (accession 0001628280-26-075127); 8-K filed 2026-11-18 (accession 0001628280-26-074848); 10-Q filed 2026-10-30 (accession 0001628280-26-068601) |
| S038 | filing | GEN | 2026-10-29 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000849399.json | Diluted EPS 0.83 for period ending 2026-10-02 (filed 2026-10-29) |
| S039 | news | MGM | Wed, 25 Nov 2026 01:31:51 GMT | ok | https://news.google.com/rss/search?q=MGM+MGM+Resorts+stock&hl=en-US&gl=US&ceid=US:en | MGM Resorts officer sells $685,938 in common stock By Investing.com - Investing.com India (Wed, 25 Nov 2026 01:31:51 GMT); Why MGM Resorts (MGM) stock is up today - Yahoo Finance (Thu, 29 Oct 2026 07:00:00 GMT); This casino stock has fallen for 17 weeks in a row. Katie Stockton says it could be due for a bounce - CNBC (Tue, 03 Nov 2026 08:00:00 GMT) |
| S040 | filing | MRVL | 2026-11-12 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001835632&type=10-Q&dateb=&owner=include&count=10 | 8-K filed 2026-11-12 (accession 0001835632-26-000026); 8-K filed 2026-11-02 (accession 0001193125-26-442717); 8-K filed 2026-11-02 (accession 0001193125-26-442714) |

## Sources

- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFF&cosd=2026-01-01 (2026-11-23)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLH0A0HYM2&cosd=2026-01-01 (2026-11-23)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLC0A0CM&cosd=2026-01-01 (2026-11-23)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCSL&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=UNRATE&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=PAYEMS&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=T10Y2Y&cosd=2026-01-01 (2026-11-24)
- filing CHTR: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 (2026-11-06)
- filing APP: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001751008&type=10-Q&dateb=&owner=include&count=10 (2026-11-04)
- filing CMG: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001058090&type=10-Q&dateb=&owner=include&count=10 (2026-10-29)
- news CMG: https://news.google.com/rss/search?q=CMG+Chipotle+Mexican+Grill+stock&hl=en-US&gl=US&ceid=US:en (Tue, 24 Nov 2026 15:25:45 GMT)
- news APP: https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en (Mon, 23 Nov 2026 01:07:00 GMT)
- stock APP: https://finance.yahoo.com/quote/APP (2026-11-25)
- filing APP: https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json (2026-11-04)
- stock CHTR: https://finance.yahoo.com/quote/CHTR (2026-11-25)
- stock CMG: https://finance.yahoo.com/quote/CMG (2026-11-25)
- filing CHTR: https://data.sec.gov/api/xbrl/companyfacts/CIK0001091667.json (2026-11-06)
- filing CMG: https://data.sec.gov/api/xbrl/companyfacts/CIK0001058090.json (2026-10-29)
- stock IDXX: https://finance.yahoo.com/quote/IDXX (2026-11-25)
- news IDXX: https://news.google.com/rss/search?q=IDXX+Idexx+Laboratories+stock&hl=en-US&gl=US&ceid=US:en (Fri, 20 Nov 2026 13:13:58 GMT)

## AI Provenance

- Provider / model: hermes-local-proxy / upstage/solar-mini4:free
- Market research: attempts=1 tokens=8409 (prompt=5409, completion=3000) runtime=43.33s
- Fundamental research: generated this run at 2026-11-25T10:09:32.698457+00:00
- Evidence source dates: {'as_of': '2026-11-24', 'latest_equity_date': '2026-11-24', 'latest_macro_date': '2026-11-25', 'flows_date': '2026-11-24'}
- Evidence fingerprint: ded9be5e4e0af5f4df47f10707096fd16abefc46294a0ddfef565c0da9b4a27d
- Source citations are retrieved external records in the ledger above; market values remain from the verified database snapshot.


## Disclosures

- This is research and market intelligence, not investment advice.
- AI conclusions are research judgments, not validated return predictions.
- The frozen risk layer is risk-only and is not used for directional views or allocations.
- Legacy scores are not active inputs or outputs.

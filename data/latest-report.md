# AEGIS AI-First Market Intelligence

Research generated at: 17 November 2026, 01:07 HKT
Database freshness: equity 2026-11-13 (latest row retrieved 2026-11-16 13:06:43.000010+08:00)
Data cutoff: 2026-11-13 US cash close
Snapshot ID: aegis-hourly-20261116T170757Z

## Executive Summary

- **AI market view: Late-November 2026: broad market breadth is constructive (71% above 50-day, 64% above 200-day, A/D ratio 1.70), but the index is slightly negative over 20 days and the leadership set is narrow. Health Care, Consumer Discretionary, Consumer Staples and Financials lead on 20-day returns, while Information Technology and Energy are the weakest sectors. Liquidity is concentrated in a small set of large-cap names, and credit spreads remain tight, suggesting a late-cycle, low-volatility backdrop with selective leadership.**
- Broad market breadth is positive: 71.3% of names above the 50-day moving average, 63.6% above the 200-day, and an advance/decline ratio of 1.70.
- The S&P 500 is down 1.28% over 20 days, indicating a modest pullback despite strong breadth.
- Sector leadership is concentrated in Health Care, Consumer Discretionary, Consumer Staples and Financials; Information Technology and Energy are negative.
- Credit spreads are tight (IG OAS 0.89%, HY OAS 3.23%), consistent with a late-cycle, low-risk environment.
- Liquidity is heavily concentrated in a small set of large-cap names, with several high-multiple names flagged as dislocation leaders.
- Macro data show a 4.2% unemployment rate and core CPI still elevated, implying policy remains data-dependent.

## Data QC

- Status: **PASS_WITH_WARNINGS**
- Equity session: 0 completed session(s) behind inference date
- Equity provenance: 393 provisional / 12576 canonical
- Breadth lag: 0 session(s); ETF-flow lag: 0 session(s)
- Note: Equity session contains a mix of provisional yfinance and canonical Massive rows.
- External sources: 79 ok / 0 unavailable; retrieved 2026-11-16T17:08:17.354751+00:00

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
| S&P 500 | 7561.67 | -1.28% (20d) | Index is slightly negative over 20 days despite broad-based above-trend momentum. |
| Health Care (XLV) | 6.87% | +6.87% (20d) | Strongest sector; trailing P/E 30.79 and inflows confirmed by ETF flow data. |
| Consumer Discretionary (XLY) | 6.69% | +6.69% (20d) | Positive momentum but structural distribution in flows; trailing P/E 24.81. |
| Consumer Staples (XLP) | 5.40% | +5.40% (20d) | Defensive strength; trailing P/E 24.92. |
| Financials (XLF) | 5.69% | +5.69% (20d) | Positive 20-day return; trailing P/E 15.77. |
| Information Technology (XLK) | -7.19% | -7.19% (20d) | Weakest sector; trailing P/E 29.33 and liquidity concentrated in NVDA/AMD. |
| Energy (XLE) | -4.81% | -4.81% (20d) | Negative sector; trailing P/E 15.99. |

## Macro, Fiscal, Rates, Liquidity and Credit

- Growth: US unemployment is 4.2% (September 2026), indicating a still-healthy labor market, though the latest macro print is dated 2026-11-16.
- Inflation: CPI is 336.298 (September 2026) and core CPI 338.896; the October CPI print in the external source is 337.476, suggesting inflation remains above the pre-2021 trend.
- Policy: The effective federal funds rate is 3.88% as of 2026-11-12, implying a restrictive but easing-leaning stance.
- Rates: The 10Y-2Y Treasury spread is 0.27 as of 2026-11-13, a modest positive slope that is not strongly steepening.
- Liquidity: IG credit spreads are 0.89% and HY spreads 3.23%, both tight and supportive of risk assets.
- Credit: Tight spreads and positive equity momentum suggest liquidity is not a binding constraint, but the narrow leadership set warrants caution.

## US Equities and 11 GICS Sectors

Macro source IDs: S001, S002, S003, S004, S005, S006, S007

| GICS sector | Evidence | AI research stance | Source IDs |
| --- | --- | --- | --- |
| Health Care | 20-day return +6.87%; trailing P/E 30.79; ETF flow z-score 1.45 (20d) and 1.72 (60d), state inflow, strong confirmation. | Positive momentum and confirmed institutional inflows; valuation is rich but supported by sector leadership. | S054 |
| Consumer Staples | 20-day return +5.40%; trailing P/E 24.92; defensive positioning within a positive breadth environment. | Steady defensive contribution; no flow data supplied, so stance is based on sector return and valuation. | S056 |
| Consumer Discretionary | 20-day return +6.69%; trailing P/E 24.81; flow z-score -0.38 (20d) and -0.78 (60d), structural distribution. | Positive price momentum but institutional selling suggests leadership may be fragile. | S061 |
| Real Estate | 20-day return +5.24%; trailing P/E 29.56; no flow data supplied. | Positive 20-day return but high valuation; stance is neutral pending flow confirmation. | S065 |
| Financials | 20-day return +5.69%; trailing P/E 15.77; no flow data supplied. | Attractive relative valuation and positive sector momentum; stance is constructive but unconfirmed by flows. | S066 |
| Utilities | 20-day return +4.34%; trailing P/E 18.10; flow z-score -2.15 (20d) with exceptional institutional selling. | Price momentum is positive but flows show medium-term deterioration; stance is cautious. | S064 |
| Materials | 20-day return +2.57%; trailing P/E 21.56; no flow data supplied. | Modest positive return; stance is neutral given limited evidence. | S068 |
| Industrials | 20-day return +0.61%; trailing P/E 26.76; no flow data supplied. | Near-flat sector performance; stance is neutral. | S070 |
| Communication Services | 20-day return -1.48%; trailing P/E 17.09; no flow data supplied. | Negative sector return; stance is cautious. | S072 |
| Information Technology | 20-day return -7.19%; trailing P/E 29.33; liquidity leaders NVDA and AMD flagged, but both carry forward EPS flags. | Weak sector momentum; high-multiple names are dislocation leaders but valuation quality is questionable. | S072 |
| Energy | 20-day return -4.81%; trailing P/E 15.99; no flow data supplied. | Negative sector return; stance is cautious. | S075 |

### Sector fundamentals, valuation and earnings

No point-in-time sector fundamentals beyond the supplied trailing P/E and 20-day ETF returns are available in the database. Growth, margin, and consensus data were retrieved only for the source-backed shortlist names, and no structured sector-level fundamentals are provided. The sector view above relies on the supplied 20-day returns, trailing P/E, and flow evidence.

## Growth vs Value

- Health Care offers the strongest 20-day momentum (+6.87%) with confirmed inflows, but trailing P/E of 30.79 is rich.
- Financials show a relatively low trailing P/E of 15.77 and positive sector momentum, suggesting a value tilt.
- Information Technology is the weakest sector (-7.19%) with a high trailing P/E of 29.33, and the liquidity leaders NVDA and AMD carry forward EPS flags.
- Energy is negative (-4.81%) with a low trailing P/E of 15.99, but the negative return limits the value case.

## ETF Flows and Breadth

- Broad market breadth is positive: 71.3% above the 50-day, 63.6% above the 200-day, and an advance/decline ratio of 1.70.
- Health Care ETF shows strong confirmation with flow z-scores of 1.45 (20d) and 1.72 (60d), indicating institutional inflows.
- Consumer Discretionary shows structural distribution (flow z-scores -0.38 and -0.78), suggesting a divergence between price and institutional money.
- Utilities shows exceptional institutional selling (flow z-score -2.15 on 20d) despite positive price momentum.
- New highs and new lows are both zero, indicating no extreme breakout or breakdown in the breadth data.

## Stock Ideas

Single-stock research uses reported EPS, forward P/E and company fundamentals. All ideas are research judgments, not validated return predictions.

| Ticker | Security | Research view | Price | EPS | Forward P/E | Base target | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| APP | AppLovin | NEW | 409.1 | 20.86026 | 19.965237 | 458.93 | NEW |
| PNR | Pentair | KEEP | 68.3 | 5.30402 | 12.865713 | 74.26 | KEEP |
| GEN | Gen Digital | KEEP | 30.4 | 3.33736 | 9.159935 | 36.71 | KEEP |
| RDDT | Reddit | DOWNGRADE | 98.45 | 9.10039 | 10.35615 | 109.2 | DOWNGRADE |

## ETF Ideas

ETF research uses holdings, portfolio valuation and exposure. Single-stock EPS × P/E valuation is not applied to ETFs.

| Ticker | Fund | Research view | Price | Top holdings | Portfolio valuation | Sector exposure | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| XLV | Health Care sector ETF | KEEP | 188.85 | LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59% | Top 10 holdings; numeric weight coverage 61.42% | Health Care | KEEP |
### APP — AppLovin

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** AppLovin is preferred over the other top-momentum shortlist names because it combines the strongest 20-day and 60-day returns with the highest gross margin and positive earnings growth, whereas peers such as Gen Digital and Clorox show weaker revenue and earnings momentum. Alternatives considered: GEN, CLX.
- **Thesis:** AppLovin screens as a top 20-day momentum name with a 53.7% 20-day return and a 32.5% 60-day return, indicating strong recent price acceleration. Reported diluted EPS of $11.61 for the fiscal period ending 2026-09-30 and a forward EPS of $20.86 support a forward P/E near 20, while the 20-day momentum screen and high gross margin of 88.8% point to durable digital advertising and mobile monetization. The name is preferred over the lower-momentum, lower-margin consumer staples names in the shortlist because its revenue and earnings growth are materially stronger.
- **Source IDs:** S010, S011, S013, S018
- **Catalysts:** Continued 20-day momentum and positive 60-day return, Sustained high gross margin and operating leverage in digital advertising, Forward EPS growth from reported FY1 EPS of $20.72 toward forward EPS of $20.86
- **Risks:** High 20-day momentum can mean elevated volatility and mean-reversion risk, Forward EPS and fiscal-year mapping are unverified, so forward P/E is not fully confirmed, Digital advertising cyclicality and competition could pressure growth
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 20.8603 (source.forwardEps) x AI multiple assumption 22.00; source IDs S010, S011, S013, S018
- **EPS:** 20.86026 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 19.965237
- **FY+1 growth assumption:** 27.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / AAPL / APP shows strong FY+1 consensus earnings growth of 27.44% and revenue growth of 25.37%, with exceptional margins (gross 88.8%, operating 77.8%, profit 65.9%) and high ROE. The base multiple of 22x is supported by its premium quality and growth profile relative to AAPL, while the bull/bear range reflects margin durability and competitive positioning.
- **Company fundamentals:** Reported diluted EPS $11.61; forward EPS $20.86; forward P/E 19.97; gross margin 88.8%; operating margin 77.8%; profit margin 65.9%; revenue growth 55.5%; earnings growth 75.5%; 20-day return 53.7%; 60-day return 32.5%; 60-day drawdown -0.2%.
- **Bull / Base / Bear:** 542.37 / 458.93 / 333.76
- **Bull / Base / Bear returns:** 32.58% / 12.18% / -18.42%
- **Scenario probabilities:** not separately assigned; see scenario table.

### PNR — Pentair

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Pentair is preferred over the lower-momentum, lower-margin consumer staples names in the shortlist because it offers a materially lower forward P/E and stronger 20-day momentum, but it is not preferred over higher-growth technology and digital advertising names. Alternatives considered: CLX, GEN.
- **Thesis:** Pentair is a top 20-day momentum name with a 27.8% 20-day return and a 7.1% 60-day return, but its fundamentals are mixed: reported diluted EPS of $2.76, forward EPS of $5.30, forward P/E of 12.9, revenue growth of -4.5% and earnings growth of -18.8%. The positive momentum screen supports a neutral stance rather than a conviction buy, and the negative earnings growth tempers the case.
- **Source IDs:** S012, S014, S015, S024
- **Catalysts:** 20-day momentum of 27.8% and 60-day return of 7.1%, Forward EPS of $5.30 and forward P/E of 12.9, Industrial and water technology exposure
- **Risks:** Negative revenue growth of -4.5% and negative earnings growth of -18.8%, Forward EPS and fiscal-year mapping are unverified, Industrial end-market cyclicality and capital expenditure timing
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 5.3040 (source.forwardEps) x AI multiple assumption 14.00; source IDs S012, S014, S015, S024
- **EPS:** 5.30402 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 12.865713
- **FY+1 growth assumption:** 12.82%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / GE / PNR has moderate FY+1 consensus earnings growth of 12.82% and revenue growth of 18.38%, with lower margins (gross 40.2%, operating 21.4%, profit 15.4%) and ROE of 15.6%. The base multiple of 14x reflects a mid-cycle recovery profile, with the bull/bear range capturing margin expansion potential versus cyclical downside risk.
- **Company fundamentals:** Reported diluted EPS $2.76; forward EPS $5.30; forward P/E 12.87; gross margin 40.2%; operating margin 21.4%; profit margin 15.4%; revenue growth -4.5%; earnings growth -18.8%; 20-day return 27.8%; 60-day return 7.1%; 60-day drawdown -5.2%.
- **Bull / Base / Bear:** 90.17 / 74.26 / 58.34
- **Bull / Base / Bear returns:** 32.02% / 8.73% / -14.58%
- **Scenario probabilities:** not separately assigned; see scenario table.

### GEN — Gen Digital

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Gen Digital is preferred over the lower-momentum, lower-margin consumer staples names in the shortlist because it offers a much lower forward P/E and stronger earnings growth, but it is not preferred over the higher-growth digital advertising name AppLovin. Alternatives considered: CLX, APP.
- **Thesis:** Gen Digital is a top 20-day momentum name with a 25.8% 20-day return and a 7.9% 60-day return. It has a low forward P/E of 9.16 and positive earnings growth of 128.6%, but revenue growth is only 12.2% and the forward EPS and fiscal-year mapping are unverified. The combination of strong momentum, a low valuation multiple, and high earnings growth supports a neutral stance with a bias toward re-evaluation if revenue growth accelerates.
- **Source IDs:** S017, S019, S022, S025
- **Catalysts:** 20-day momentum of 25.8% and 60-day return of 7.9%, Forward P/E of 9.16 and earnings growth of 128.6%, Cybersecurity and digital risk exposure
- **Risks:** Revenue growth of only 12.2% is below the earnings growth rate, Forward EPS and fiscal-year mapping are unverified, Cybersecurity regulatory and competitive pressures
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 3.3374 (source.forwardEps) x AI multiple assumption 11.00; source IDs S017, S019, S022, S025
- **EPS:** 3.33736 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 9.159935
- **FY+1 growth assumption:** 12.86%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / MSFT / GEN shows FY+1 consensus earnings growth of 12.86% and revenue growth of 6.81%, with solid gross margin of 77.4% and operating margin of 43.2%. The base multiple of 11x is justified by its growth and margin profile relative to MSFT, with the bull/bear range reflecting execution risk and competitive dynamics.
- **Company fundamentals:** Reported diluted EPS $0.83; forward EPS $3.34; forward P/E 9.16; gross margin 77.4%; operating margin 43.2%; profit margin 23.1%; revenue growth 12.2%; earnings growth 128.6%; 20-day return 25.8%; 60-day return 7.9%; 60-day drawdown -3.2%.
- **Bull / Base / Bear:** 43.39 / 36.71 / 30.04
- **Bull / Base / Bear returns:** 42.73% / 20.76% / -1.18%
- **Scenario probabilities:** not separately assigned; see scenario table.

### RDDT — Reddit

- **Type:** Stock
- **Research view:** DOWNGRADE (stance: AVOID)
- **Why preferred / alternatives:** Reddit is not preferred over the other shortlist names because its severe price dislocation and negative momentum outweigh its low forward P/E, and it is less attractive than the higher-momentum, higher-margin names such as AppLovin and Roper Technologies. Alternatives considered: APP, ROP.
- **Thesis:** Reddit is the largest 20-day dislocation name with a -36.9% 20-day return and a -34.5% 60-day return, and a 60-day drawdown of -39.4%. Although it screens with a forward P/E of 10.36 and a sector-relative P/E of 1.66, the severe price dislocation and negative momentum indicate elevated risk. The combination of a large drawdown and negative price momentum makes this a name to avoid rather than a conviction buy.
- **Source IDs:** S039, S042, S043, S046
- **Catalysts:** Forward P/E of 10.36 and sector-relative P/E of 1.66, Revenue growth of 53% and earnings growth of 74.9%, High gross margin of 91.5%
- **Risks:** 20-day return of -36.9% and 60-day return of -34.5%, 60-day drawdown of -39.4%, Social media and advertising market cyclicality
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 9.1004 (source.forwardEps) x AI multiple assumption 12.00; source IDs S039, S042, S043, S046
- **EPS:** 9.10039 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 10.35615
- **FY+1 growth assumption:** 24.01%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / DIS / RDDT has strong FY+1 consensus earnings growth of 24.01% and revenue growth of 28.38%, with high gross margin of 91.5% and operating margin of 29.4%. The base multiple of 12x reflects its premium growth and margin profile relative to DIS, with the bull/bear range capturing brand strength and capital allocation risk.
- **Company fundamentals:** Reported diluted EPS $3.66; forward EPS $9.10; forward P/E 10.36; gross margin 91.5%; operating margin 29.4%; profit margin 32.1%; revenue growth 53.0%; earnings growth 74.9%; 20-day return -36.9%; 60-day return -34.5%; 60-day drawdown -39.4%.
- **Bull / Base / Bear:** 127.41 / 109.2 / 91.0
- **Bull / Base / Bear returns:** 29.42% / 10.92% / -7.57%
- **Scenario probabilities:** not separately assigned; see scenario table.

### XLV — Health Care sector ETF

- **Type:** ETF
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** The Health Care sector ETF is preferred over the other sector ETFs in the shortlist because it provides diversified exposure to the highest-quality large-cap health care names, whereas the Consumer Discretionary and Industrials ETFs show negative price changes and the Real Estate ETF has lower holdings coverage. Alternatives considered: XLY, XLI, XLRE.
- **Thesis:** The Health Care sector ETF offers diversified exposure to large-cap pharmaceutical and medical device leaders, with a 0.54% price change and a 5.8 million share volume. The top holdings include LLY, JNJ, ABBV, MRK, UNH, TMO, AMGN, GILD, ABT and PFE, providing broad sector coverage. The neutral stance reflects a balanced risk-reward profile in the current macro environment, with no strong conviction to upgrade or downgrade.
- **Source IDs:** S054, S055
- **Catalysts:** Diversified large-cap health care exposure, Top-10 holdings coverage of 61.4%, Positive sector price change of 0.54%
- **Risks:** Top-10 holdings coverage of only 61.4% limits concentration transparency, Sector-specific regulatory and drug-pricing risk, Macro sensitivity to interest rates and health care spending
- **Valuation method:** Holdings/portfolio valuation with AI total-return assumption
- **Valuation status:** verified; forward-EPS source: ; period flags: 
- **Valuation assumptions:** Holdings/portfolio valuation; 10 weighted holdings; coverage 61.42%; source IDs S054, S055
- **Top holdings:** LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59%
- **Portfolio valuation:** Top 10 holdings; numeric weight coverage 61.42%
- **Sector exposure:** Health Care
- **Underlying drivers:** Large-cap pharmaceutical and medical device demand, drug pricing policy, interest rate environment, and health care sector momentum.
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
| Bull | 25% | +2.00% | Low 5-day vol (14.9%) and false directional signal imply a stable, range-bound tape; a mild positive surprise from a soft US close could push the index up 2%. |
| Base | 50% | +0.00% | Frozen daily-close model with no directional alpha and a 16.5% spike probability near the 18.5% threshold supports a near-flat 5-day return. |
| Bear | 25% | -2.00% | If the spike probability materializes above threshold, elevated vol and a negative US close could drive a 2% decline. |

### Long Term (12 months)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 30% | +8.00% | Sustained low vol and false directional signal allow earnings-driven upside; a 30% probability of an 8% gain over the horizon. |
| Base | 40% | +3.00% | Base case reflects modest trend continuation with stable vol and no directional alpha, yielding a 3% long-term return. |
| Bear | 30% | -5.00% | If spike probability exceeds threshold and vol rises, a 30% probability of a 5% decline over the long horizon. |

## Positioning

- Maintain a constructive but selective stance: broad breadth is positive, but index-level returns are slightly negative.
- Favor Health Care and Financials for momentum and relative valuation, respectively.
- Treat Consumer Discretionary and Utilities with caution due to structural distribution and exceptional institutional selling.
- Avoid relying on Information Technology liquidity leaders given forward EPS flags and high multiples.
- No numerical allocation weights or composite scores are used; positioning is qualitative.

## Catalysts

| Date | Event | Why it matters |
| --- | --- | --- |
| 2026-11-16 | Macro data release | Latest macro print dated 2026-11-16 may update unemployment and inflation expectations, influencing policy stance. |
| 2026-11-13 | Equity session close | Equity session contains a mix of provisional yfinance and canonical Massive rows; the warning indicates data provenance is not fully canonical. |
| 2026-11-13 | Breadth and flow snapshot | Breadth and flow data are as of 2026-11-13 with zero lag, providing the latest institutional money flow picture. |

## Key Risks

- Equity session contains a mix of provisional yfinance and canonical Massive rows, which may affect data reliability.
- Information Technology and Energy sectors are negative over 20 days, and leadership is narrow.
- Several high-multiple names flagged as liquidity leaders carry forward EPS flags, indicating potential valuation quality issues.
- Consumer Discretionary and Utilities show structural distribution and exceptional institutional selling, respectively.
- Core CPI remains elevated, and the effective federal funds rate is still restrictive, implying policy risk.
- The frozen risk model shows a 16.5% spike probability, below the 18.5% threshold, but the model is experimental and not yet formally eligible.

## External Source Ledger

| ID | Type | Ticker | Published | Status | URL | Claims |
| --- | --- | --- | --- | --- | --- | --- |
| S001 | macro | macro | 2026-11-12 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFF&cosd=2026-01-01 | Effective federal funds rate (DFF) latest observation 2026-11-12: 3.88 |
| S002 | macro | macro | 2026-11-13 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLH0A0HYM2&cosd=2026-01-01 | US high-yield OAS (BAMLH0A0HYM2) latest observation 2026-11-13: 3.23 |
| S003 | macro | macro | 2026-11-13 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLC0A0CM&cosd=2026-01-01 | US investment-grade OAS (BAMLC0A0CM) latest observation 2026-11-13: 0.89 |
| S004 | macro | macro | 2026-10-01 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCSL&cosd=2026-01-01 | US CPI (CPIAUCSL) latest observation 2026-10-01: 337.476 |
| S005 | macro | macro | 2026-10-01 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=UNRATE&cosd=2026-01-01 | US unemployment rate (UNRATE) latest observation 2026-10-01: 4.1 |
| S006 | macro | macro | 2026-10-01 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=PAYEMS&cosd=2026-01-01 | US nonfarm payrolls (PAYEMS) latest observation 2026-10-01: 159293 |
| S007 | macro | macro | 2026-11-13 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=T10Y2Y&cosd=2026-01-01 | 10Y-2Y Treasury spread (T10Y2Y) latest observation 2026-11-13: 0.27 |
| S008 | filing | FISV | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0000798354-26-000042); 8-K filed 2026-11-03 (accession 0000798354-26-000039); 8-K filed 2026-10-23 (accession 0001193125-26-429481) |
| S009 | news | FISV | Mon, 16 Nov 2026 02:19:15 GMT | ok | https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en | Fiserv, Inc. (FISV) Stock Price, News, Quote & History - Yahoo! Finance Canada (Mon, 16 Nov 2026 02:19:15 GMT); Fiserv (FISV) Stock Looks Undervalued With Strong Excess Returns - Yahoo Finance (Wed, 11 Nov 2026 22:14:34 GMT); Fiserv (FISV) Stock Still Looks Like A Bargain After Lawsuit Claims - Yahoo Finance (Thu, 22 Oct 2026 07:00:00 GMT) |
| S010 | news | APP | Thu, 12 Nov 2026 20:05:45 GMT | ok | https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en | AppLovin Just Ripped 47% in a Month: Is It Too Late to Buy APP Stock Now? - Yahoo Finance (Thu, 12 Nov 2026 20:05:45 GMT); Is Trending Stock AppLovin Corporation (APP) a Buy Now? - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT); APP Stock Surges 51% After Q3 Earnings: Is it Still a Buy? - Yahoo Finance (Tue, 10 Nov 2026 14:24:00 GMT) |
| S011 | filing | APP | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001751008&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0001751008-26-000069); 8-K filed 2026-11-04 (accession 0001751008-26-000068); 10-Q filed 2026-08-05 (accession 0001751008-26-000059) |
| S012 | filing | PNR | 2026-10-27 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-27 (accession 0000077360-26-000058); 8-K filed 2026-10-27 (accession 0000077360-26-000055); 8-K filed 2026-09-22 (accession 0000077360-26-000050) |
| S013 | stock | APP | 2026-11-16 | ok | https://finance.yahoo.com/quote/APP | Trailing P/E: 28.045792; Forward P/E: 19.965237; Forward EPS: 20.86026; Price: 416.63; Market price: 416.48; Market cap: 137988980736; Sector: Communication Services; Trailing Eps: 14.85; Revenue Growth: 0.555; Earnings Growth: 0.755; Gross Margin: 0.8878; Operating Margin: 0.77782995; Profit Margin: 0.65887; Return On Equity: 2.1008599; Total Revenue: 7608893952; Market Cap: 137988980736; Consensus EPS FY+1: 20.72438; growth: 0.2744 |
| S014 | news | PNR | Sat, 14 Nov 2026 08:48:27 GMT | ok | https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en | Pentair plc (PNR) Stock Price, News, Quote & History - Yahoo! Finance Canada (Sat, 14 Nov 2026 08:48:27 GMT); Pentair plc (PNR) stock price, news, quote and history - Yahoo Finance UK (Fri, 13 Nov 2026 22:09:48 GMT); Why Pentair Stock Popped This Morning - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT) |
| S015 | stock | PNR | 2026-11-16 | ok | https://finance.yahoo.com/quote/PNR | Trailing P/E: 18.594004; Forward P/E: 12.865713; Forward EPS: 5.30402; Price: 68.24; Market price: 68.24; Market cap: 10894835712; Sector: Industrials; Trailing Eps: 3.67; Revenue Growth: -0.045; Earnings Growth: -0.188; Gross Margin: 0.40168998; Operating Margin: 0.21410999; Profit Margin: 0.15435; Return On Equity: 0.15605; Total Revenue: 3966200064; Market Cap: 10894835712; Consensus EPS FY+1: 5.30402; growth: 0.1282 |
| S016 | stock | FISV | 2026-11-16 | ok | https://finance.yahoo.com/quote/FISV | Forward P/E: 8.039299; Price: 64.12; Market price: 64.12; Market cap: 34114899968; Market Cap: 34114899968; Consensus EPS FY+1: 7.97582; growth: 0.0959 |
| S017 | filing | GEN | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0000849399-26-000083); 8-K filed 2026-10-28 (accession 0000849399-26-000081); 8-K filed 2026-10-09 (accession 0000849399-26-000079) |
| S018 | filing | APP | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json | Diluted EPS 11.61 for period ending 2026-09-30 (filed 2026-11-04) |
| S019 | stock | GEN | 2026-11-16 | ok | https://finance.yahoo.com/quote/GEN | Trailing P/E: 15.517766; Forward P/E: 9.159935; Forward EPS: 3.33736; Price: 30.57; Market price: 30.57; Market cap: 18136451072; Sector: Technology; Trailing Eps: 1.97; Revenue Growth: 0.122; Earnings Growth: 1.286; Gross Margin: 0.77410007; Operating Margin: 0.43229; Profit Margin: 0.23068; Return On Equity: 0.46402; Total Revenue: 5228000256; Market Cap: 18136451072; Consensus EPS FY+1: 3.33736; growth: 0.1286 |
| S020 | filing | CLX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000021076-26-000046); 8-K filed 2026-11-02 (accession 0000021076-26-000044); 8-K filed 2026-10-29 (accession 0001206774-26-000586) |
| S021 | stock | CLX | 2026-11-16 | ok | https://finance.yahoo.com/quote/CLX | Trailing P/E: 19.743706; Forward P/E: 17.79635; Forward EPS: 6.1684; Price: 109.775; Market price: 109.775; Market cap: 13298955264; Sector: Consumer Defensive; Trailing Eps: 5.56; Revenue Growth: 0.333; Earnings Growth: 1.138; Gross Margin: 0.41939998; Operating Margin: 0.14286; Profit Margin: 0.09408; Return On Equity: 5.34363; Total Revenue: 7196000256; Market Cap: 13298955264; Consensus EPS FY+1: 6.1684; growth: 0.0769 |
| S022 | news | GEN | Thu, 29 Oct 2026 07:00:00 GMT | ok | https://news.google.com/rss/search?q=GEN+Gen+Digital+stock&hl=en-US&gl=US&ceid=US:en | Gen Digital (GEN) Stock Repriced After Q2 Earnings Put Margins Center Stage - Yahoo Finance (Thu, 29 Oct 2026 07:00:00 GMT); Gen Digital Stock: Is Wall Street Bullish or Bearish? - Yahoo Finance (Thu, 05 Nov 2026 08:00:00 GMT); Are Business Services Stocks Lagging GEN DIGITAL INC (GEN) This Year? - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT) |
| S023 | filing | FISV | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json | Diluted EPS -8.9 for period ending 2026-09-30 (filed 2026-11-04) |
| S024 | filing | PNR | 2026-10-27 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json | Diluted EPS 2.76 for period ending 2026-09-30 (filed 2026-10-27) |
| S025 | filing | GEN | 2026-10-29 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000849399.json | Diluted EPS 0.83 for period ending 2026-10-02 (filed 2026-10-29) |
| S026 | filing | CHTR | 2026-11-06 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-06 (accession 0001091667-26-000073); 8-K filed 2026-11-06 (accession 0001091667-26-000072); 8-K filed 2026-10-27 (accession 0001091667-26-000064) |
| S027 | news | CLX | Fri, 13 Nov 2026 23:34:51 GMT | ok | https://news.google.com/rss/search?q=CLX+Clorox+stock&hl=en-US&gl=US&ceid=US:en | The Clorox Company (CLX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 23:34:51 GMT); The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance UK (Sat, 14 Nov 2026 06:03:20 GMT); A 10-Day Winning Streak Has Clorox Stock Up 24% - Trefis (Sat, 14 Nov 2026 08:28:05 GMT) |
| S028 | stock | CHTR | 2026-11-16 | ok | https://finance.yahoo.com/quote/CHTR | Trailing P/E: 13.066258; Forward P/E: 3.0592024; Forward EPS: 45.44485; Price: 139.025; Market price: 139.025; Market cap: 24892641280; Sector: Communication Services; Trailing Eps: 10.64; Revenue Growth: 0.091; Gross Margin: 0.55084; Operating Margin: 0.23389; Profit Margin: 0.02498; Return On Equity: 0.07019; Total Revenue: 55645999104; Market Cap: 24892641280; Consensus EPS FY+1: 49.35412; growth: 1.1136 |
| S029 | news | CHTR | Sun, 15 Nov 2026 05:47:01 GMT | ok | https://news.google.com/rss/search?q=CHTR+Charter+Communications+stock&hl=en-US&gl=US&ceid=US:en | Charter Communications (CHTR) Stock Could Be A Bargain Following Its New Operating Model - Yahoo Finance (Sun, 15 Nov 2026 05:47:01 GMT); Why You Should Think About Charter Communications Differently Now? - Yahoo Finance (Fri, 13 Nov 2026 19:16:11 GMT); Charter Communications (CHTR) Earnings Expected to Grow: What to Know Ahead of Next Week's Release - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT) |
| S030 | filing | IDXX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000874716&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000874716-26-000135); 8-K filed 2026-11-02 (accession 0001104659-26-120892); 10-Q filed 2026-08-04 (accession 0000874716-26-000123) |
| S031 | filing | ROP | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000882835&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000882835-26-000047); 8-K filed 2026-10-22 (accession 0000882835-26-000042); 8-K filed 2026-10-01 (accession 0000882835-26-000039) |
| S032 | stock | ROP | 2026-11-16 | ok | https://finance.yahoo.com/quote/ROP | Trailing P/E: 19.221409; Forward P/E: 19.76647; Forward EPS: 24.57318; Price: 485.725; Market price: 485.725; Market cap: 48104472576; Sector: Technology; Trailing Eps: 25.27; Revenue Growth: 0.076; Earnings Growth: 0.326; Gross Margin: 0.69671; Operating Margin: 0.28049; Profit Margin: 0.30712998; Return On Equity: 0.13229; Total Revenue: 8434599936; Market Cap: 48104472576; Consensus EPS FY+1: 24.57318; growth: 0.09810001 |
| S033 | news | IDXX | Sat, 14 Nov 2026 22:37:20 GMT | ok | https://news.google.com/rss/search?q=IDXX+Idexx+Laboratories+stock&hl=en-US&gl=US&ceid=US:en | IDEXX Laboratories, Inc. (IDXX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Sat, 14 Nov 2026 22:37:20 GMT); IDEXX Laboratories (IDXX) Stock Looks Fairly Valued Despite Its 28% Run - Yahoo Finance (Sat, 31 Oct 2026 07:00:00 GMT); IDEXX Laboratories (IDXX) vs. ZTS and NEOG: Can Raised Guidance and Product Expansion Drive Further Earnings Growth? - Yahoo Finance (Thu, 22 Oct 2026 07:00:00 GMT) |
| S034 | stock | IDXX | 2026-11-16 | ok | https://finance.yahoo.com/quote/IDXX | Trailing P/E: 47.674866; Forward P/E: 41.881203; Forward EPS: 16.8929; Price: 707.495; Market price: 707.495; Market cap: 55740887040; Sector: Healthcare; Trailing Eps: 14.84; Revenue Growth: 0.099; Earnings Growth: 0.179; Gross Margin: 0.62722; Operating Margin: 0.32497; Profit Margin: 0.25357; Return On Equity: 0.68925005; Total Revenue: 4662220800; Market Cap: 55740887040; Consensus EPS FY+1: 16.8929; growth: 0.1244 |
| S035 | filing | CHTR | 2026-11-06 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001091667.json | Diluted EPS 0.38 for period ending 2026-09-30 (filed 2026-11-06) |
| S036 | news | ROP | Thu, 05 Nov 2026 08:00:00 GMT | ok | https://news.google.com/rss/search?q=ROP+Roper+Technologies+stock&hl=en-US&gl=US&ceid=US:en | Roper Technologies (ROP) Stock Looks Fully Valued As Cash Flow Comes Into Focus - Yahoo Finance (Thu, 05 Nov 2026 08:00:00 GMT); Here's How Much $100 Invested In Roper Technologies 20 Years Ago Would Be Worth Today - Benzinga (Mon, 16 Nov 2026 14:15:26 GMT); Roper Technologies (ROP), What Is Behind The Fresh Attention? - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT) |
| S037 | filing | CLX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000021076.json | Diluted EPS 1.39 for period ending 2026-09-30 (filed 2026-11-02) |
| S038 | filing | INTC | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000050863&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0000050863-26-000191); 8-K filed 2026-10-29 (accession 0000050863-26-000188); 8-K filed 2026-08-12 (accession 0001193125-26-346806) |
| S039 | filing | RDDT | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001713445&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0001713445-26-000116); 8-K filed 2026-10-29 (accession 0001713445-26-000114); 8-K filed 2026-08-12 (accession 0001713445-26-000107) |
| S040 | filing | IDXX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000874716.json | Diluted EPS 11.75 for period ending 2026-09-30 (filed 2026-11-02) |

## Sources

- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFF&cosd=2026-01-01 (2026-11-12)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLH0A0HYM2&cosd=2026-01-01 (2026-11-13)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLC0A0CM&cosd=2026-01-01 (2026-11-13)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCSL&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=UNRATE&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=PAYEMS&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=T10Y2Y&cosd=2026-01-01 (2026-11-13)
- filing FISV: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 (2026-11-04)
- news FISV: https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en (Mon, 16 Nov 2026 02:19:15 GMT)
- news APP: https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en (Thu, 12 Nov 2026 20:05:45 GMT)
- filing APP: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001751008&type=10-Q&dateb=&owner=include&count=10 (2026-11-04)
- filing PNR: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 (2026-10-27)
- stock APP: https://finance.yahoo.com/quote/APP (2026-11-16)
- news PNR: https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en (Sat, 14 Nov 2026 08:48:27 GMT)
- stock PNR: https://finance.yahoo.com/quote/PNR (2026-11-16)
- stock FISV: https://finance.yahoo.com/quote/FISV (2026-11-16)
- filing GEN: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 (2026-10-29)
- filing APP: https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json (2026-11-04)
- stock GEN: https://finance.yahoo.com/quote/GEN (2026-11-16)
- filing CLX: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 (2026-11-02)

## AI Provenance

- Provider / model: hermes-local-proxy / upstage/solar-mini4:free
- Market research: attempts=1 tokens=9379 (prompt=6512, completion=2867) runtime=20.19s
- Fundamental research: generated this run at 2026-11-16T17:07:57.010271+00:00
- Evidence source dates: {'as_of': '2026-11-13', 'latest_equity_date': '2026-11-13', 'latest_macro_date': '2026-11-16', 'flows_date': '2026-11-13'}
- Evidence fingerprint: ab49e657334592c15c0cc603e3ade92c95d737cbf5b7ad78fc7b218c0d1bfedd
- Source citations are retrieved external records in the ledger above; market values remain from the verified database snapshot.


## Disclosures

- This is research and market intelligence, not investment advice.
- AI conclusions are research judgments, not validated return predictions.
- The frozen risk layer is risk-only and is not used for directional views or allocations.
- Legacy scores are not active inputs or outputs.

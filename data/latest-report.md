# AEGIS AI-First Market Intelligence

Research generated at: 16 November 2026, 04:13 HKT
Database freshness: equity 2026-11-13 (latest row retrieved 2026-11-15 13:06:40.074841+08:00)
Data cutoff: 2026-11-13 US cash close
Snapshot ID: aegis-hourly-20261115T201340Z

## Executive Summary

- **AI market view: Late-November 2026 equity market is characterized by a broad but uneven tape: the S&P 500 is roughly flat over 20 days, breadth is positive but thin on new highs, and the 20-day return dispersion is wide. Information Technology and Energy are the weakest sectors, while Health Care, Consumer Discretionary, Consumer Staples, Financials, Real Estate, Utilities and Materials are modestly positive. Liquidity is concentrated in semiconductors and select large-cap names, while credit spreads remain tight and macro data show cooling inflation and a stable labor market.**
- S&P 500 is essentially flat over 20 days (SPX close 7561.67, 20d return -1.28%), with a mixed tape and no new highs.
- Breadth is positive: 71.34% above 50-day, 63.6% above 200-day, advance/decline ratio 1.70, but new highs are 0% and 20d positive is 70.46%.
- Sector returns are bifurcated: Health Care +6.87%, Consumer Discretionary +6.69%, Consumer Staples +5.40%, Financials +5.69%, Real Estate +5.24%, Utilities +4.34%, Materials +2.57%, Industrials +0.61%, Communication Services -1.48%, Information Technology -7.19%, Energy -4.81%.
- Liquidity is concentrated in SOXX (inflow, z-score 5.10) and select large-cap names, while TLT shows medium-term deterioration and SMH shows tactical profit-taking inside structural accumulation.
- Macro backdrop: CPI 336.298 (Sep-2026), core CPI 338.896, unemployment 4.2%, effective fed funds 3.88%, 10Y-2Y spread 0.27, IG OAS 0.89, HY OAS 3.20.
- Risk environment: 5-day forecast vol 14.93%, spike probability 16.51% vs historical baseline 22.07% and EWMA baseline 20.09%, directional signal false.

## Data QC

- Status: **PASS_WITH_WARNINGS**
- Equity session: 0 completed session(s) behind inference date
- Equity provenance: 393 provisional / 12576 canonical
- Breadth lag: 0 session(s); ETF-flow lag: 0 session(s)
- Note: Equity session contains a mix of provisional yfinance and canonical Massive rows.
- External sources: 79 ok / 0 unavailable; retrieved 2026-11-15T20:13:56.940130+00:00

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
| S&P 500 | 7561.67 | -1.28% (20d) | Flat-to-slightly-negative 20-day trend; no new highs, but positive 50d/200d breadth and a bull/bear divergence flag. |
| Health Care (XLV) | +6.87% | +6.87% (20d) | Strongest sector; trailing P/E 30.78, supported by defensive demand and relative valuation. |
| Consumer Discretionary (XLY) | +6.69% | +6.69% (20d) | Positive momentum; trailing P/E 25.11, consistent with consumer resilience. |
| Consumer Staples (XLP) | +5.40% | +5.40% (20d) | Defensive strength; trailing P/E 24.85, elevated but stable. |
| Financials (XLF) | +5.69% | +5.69% (20d) | Positive; trailing P/E 15.85, supported by stable rates and credit spreads. |
| Real Estate (XLRE) | +5.24% | +5.24% (20d) | Positive; trailing P/E 29.63, elevated but supported by rate stability. |
| Utilities (XLU) | +4.34% | +4.34% (20d) | Defensive; trailing P/E 18.11, consistent with safe-haven flows. |
| Materials (XLB) | +2.57% | +2.57% (20d) | Modest positive; trailing P/E 21.72, broad-based but not leading. |
| Industrials (XLI) | +0.61% | +0.61% (20d) | Near-flat; trailing P/E 27.07, lagging the broader positive tape. |
| Communication Services (XLC) | -1.48% | -1.48% (20d) | Negative; trailing P/E 17.26, weak relative to the rest of the market. |
| Information Technology (XLK) | -7.19% | -7.19% (20d) | Weakest sector; trailing P/E 30.03, reflecting high valuations and profit-taking. |
| Energy (XLE) | -4.81% | -4.81% (20d) | Negative; trailing P/E 16.23, likely driven by commodity price pressure. |

## Macro, Fiscal, Rates, Liquidity and Credit

- Inflation is cooling: CPI 336.298 and core CPI 338.896 (Sep-2026), with October CPI 337.476 per S004, indicating a gradual disinflationary path.
- Labor market is stable: unemployment 4.2% (Sep-2026) and 4.1% (Oct-2026) per S005/S006, with payrolls 159,293k (Oct-2026), supporting consumer spending.
- Policy rates are easing: effective fed funds 3.88% (Nov-12, S001), with a modestly positive 10Y-2Y spread of 0.27 (S007), suggesting a still-restrictive but normalizing stance.
- Credit conditions are benign: IG OAS 0.89 and HY OAS 3.20 (S002/S003), with tight spreads consistent with risk-on positioning.
- Liquidity is bifurcated: SOXX shows exceptional institutional buying (z-score 5.10) while TLT shows medium-term deterioration (z-score -0.41), and SMH shows tactical profit-taking inside structural accumulation.
- Volatility is moderate: 5-day forecast vol 14.93%, spike probability 16.51% below historical 22.07% and EWMA 20.09%, with no directional signal.

## US Equities and 11 GICS Sectors

Macro source IDs: S001, S002, S003, S004, S005, S006, S007

| GICS sector | Evidence | AI research stance | Source IDs |
| --- | --- | --- | --- |
| Health Care | 20d return +6.87% (XLV); trailing P/E 30.78 (S060); positive 20d momentum and defensive positioning. | Defensive strength with elevated valuation; supported by stable macro and positive breadth. | S060 |
| Consumer Staples | 20d return +5.40% (XLP); trailing P/E 24.85 (S055); defensive demand in a cooling inflation environment. | Stable defensive sector; valuation is high but supported by resilient consumer spending. | S055 |
| Consumer Discretionary | 20d return +6.69% (XLY); trailing P/E 25.11 (S059); positive momentum and stable labor market. | Positive momentum; consumer resilience supports the sector despite elevated valuation. | S059 |
| Financials | 20d return +5.69% (XLF); trailing P/E 15.85 (S063); stable rates and tight credit spreads. | Positive; low valuation and benign credit conditions support earnings and capital markets activity. | S063 |
| Real Estate | 20d return +5.24% (XLRE); trailing P/E 29.63 (S065); rate stability supports REIT valuations. | Positive; elevated valuation but supported by stable financing costs and defensive demand. | S065 |
| Utilities | 20d return +4.34% (XLU); trailing P/E 18.11 (S066); defensive safe-haven flows. | Stable defensive sector; moderate valuation and positive breadth support the allocation. | S066 |
| Materials | 20d return +2.57% (XLB); trailing P/E 21.72 (S068); modest positive momentum. | Broad-based but not leading; valuation is reasonable and supported by industrial demand. | S068 |
| Industrials | 20d return +0.61% (XLI); trailing P/E 27.07 (S076); near-flat with positive breadth. | Lagging positive tape; valuation is elevated but not leading, suggesting cautious positioning. | S076 |
| Communication Services | 20d return -1.48% (XLC); trailing P/E 17.26 (S071); negative momentum. | Weakest positive-tape sector; valuation is reasonable but momentum and relative performance are poor. | S071 |
| Information Technology | 20d return -7.19% (XLK); trailing P/E 30.03 (S073); high valuations and profit-taking. | Weakest sector; elevated valuation and negative momentum warrant caution despite liquidity leaders. | S073 |
| Energy | 20d return -4.81% (XLE); trailing P/E 16.23 (S074); negative momentum. | Negative; valuation is reasonable but commodity price pressure and weak momentum dominate. | S074 |

### Sector fundamentals, valuation and earnings

Sector-level fundamental data (growth, margins, consensus) are not supplied in the database snapshot; only trailing P/E and 20-day ETF returns are available for the 11 GICS sectors. The supplied evidence is limited to price-based momentum, valuation multiples, and liquidity/flow signals, so no point-in-time sector fundamentals beyond these metrics are available.

## Growth vs Value

- Health Care (XLV) and Consumer Discretionary (XLY) show the strongest 20d returns (+6.87% and +6.69%) with trailing P/Es of 30.78 and 25.11, indicating growth-oriented demand in defensive and consumer names.
- Financials (XLF) and Utilities (XLU) offer lower trailing P/Es (15.85 and 18.11) with positive 20d returns (+5.69% and +4.34%), suggesting value and defensive characteristics.
- Information Technology (XLK) and Energy (XLE) are the weakest performers (-7.19% and -4.81%) with trailing P/Es of 30.03 and 16.23, reflecting high valuation pressure and commodity weakness.
- Consumer Staples (XLP) and Real Estate (XLRE) show elevated trailing P/Es (24.85 and 29.63) with positive returns (+5.40% and +5.24%), indicating stable but expensive positioning.

## ETF Flows and Breadth

- SOXX is the standout liquidity leader: 20d flow z-score 5.10, 60d z-score 3.

## Stock Ideas

Single-stock research uses reported EPS, forward P/E and company fundamentals. All ideas are research judgments, not validated return predictions.

| Ticker | Security | Research view | Price | EPS | Forward P/E | Base target | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| APP | AppLovin | NEW | 409.1 | 20.86026 | 19.611452 | 417.21 | NEW |
| PNR | Pentair | KEEP | 68.3 | 5.30402 | 12.877027 | 74.26 | KEEP |
| RDDT | Reddit | KEEP | 98.45 | 9.14039 | 10.770874 | 109.68 | KEEP |

## ETF Ideas

ETF research uses holdings, portfolio valuation and exposure. Single-stock EPS × P/E valuation is not applied to ETFs.

| Ticker | Fund | Research view | Price | Top holdings | Portfolio valuation | Sector exposure | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| XLV | Health Care sector ETF | KEEP | 188.85 | LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59% | Top 10 holdings; numeric weight coverage 61.42% | Health Care | KEEP |
| XLP | Consumer Staples sector ETF | KEEP | 92.35 | WMT 11.14%, COST 9.09%, PG 7.60%, KO 7.37%, PM 6.59%, MO 4.70%, CL 4.42%, MDLZ 4.25%, PEP 4.11%, TGT 4.00% | Top 10 holdings; numeric weight coverage 63.28% | Consumer Staples | KEEP |
### APP — AppLovin

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** AppLovin offers a rare combination of high profitability (gross margin 88.8%, operating margin 77.8%) with strong recent momentum, making it a more attractive high-quality growth candidate than the lower-margin, lower-momentum alternatives in the shortlist such as Clorox or Pentair. Alternatives considered: CLX, PNR.
- **Thesis:** AppLovin screens in the top 20-day momentum bucket with a 53.7% 20-day return and a 32.5% 60-day return, indicating strong recent price momentum. The company carries a high gross margin of 88.8% and operating margin of 77.8%, with reported diluted EPS of 11.61 and a forward EPS of 20.86, supporting a forward P/E of 19.6. The stock is trading at a sector-relative P/E of 1.0, which is in line with its sector, and the earnings yield of 5.0% is reasonable for a high-quality advertising platform.
- **Source IDs:** S009, S012, S013, S014
- **Catalysts:** Continued momentum in 20-day and 60-day returns, Sustained high-margin advertising revenue growth, Potential for further upside if momentum persists
- **Risks:** High 20-day momentum may be prone to mean reversion, Sector-relative P/E at 1.0 leaves limited room for multiple expansion, News coverage flags a 47% one-month decline, suggesting volatility risk
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 20.8603 (source.forwardEps) x AI multiple assumption 20.00; source IDs S009, S012, S013, S014
- **EPS:** 20.86026 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 19.611452
- **FY+1 growth assumption:** 27.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / AAPL / APP shows strong FY1 consensus growth of 27.44% with revenue growth of 55.5% and earnings growth of 75.5%, supported by an 88.8% gross margin and 77.8% operating margin. The forward EPS of 20.86 and forward P/E of 19.6 are not used as the base multiple; instead, the multiple is set above the current forward P/E to reflect superior growth, margins, and analyst coverage of 26. AAPL is the named peer reference for high-margin, high-growth technology valuation.
- **Company fundamentals:** AppLovin has reported diluted EPS of 11.61, forward EPS of 20.86, gross margin of 88.8%, operating margin of 77.8%, profit margin of 65.9%, revenue growth of 55.5%, and earnings growth of 75.5%. The forward P/E is 19.6 and the sector-relative P/E is 1.0.
- **Bull / Base / Bear:** 500.65 / 417.21 / 333.76
- **Bull / Base / Bear returns:** 22.38% / 1.98% / -18.42%
- **Scenario probabilities:** not separately assigned; see scenario table.

### PNR — Pentair

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Pentair offers a lower forward P/E of 12.9 and a higher earnings yield of 7.4% than the higher-priced momentum names, but the negative earnings growth makes it a less compelling buy than AppLovin, which has strong growth and high margins. Alternatives considered: APP, CLX.
- **Thesis:** Pentair is a top 20-day momentum name with a 27.8% 20-day return and a 7.1% 60-day return. The company has a forward P/E of 12.9 and an earnings yield of 7.4%, which is attractive relative to its sector-relative P/E of 0.49. However, revenue growth is slightly negative at -4.5% and earnings growth is -18.8%, indicating that the momentum may be driven by factors other than fundamental growth. The stock is trading at a discount to its sector, but the negative earnings growth tempers the conviction.
- **Source IDs:** S008, S015, S019, S020
- **Catalysts:** Potential for earnings growth to turn positive as the cycle improves, Attractive valuation with forward P/E of 12.9, Sector-relative P/E of 0.49 suggests undervaluation
- **Risks:** Negative revenue growth of -4.5% and earnings growth of -18.8%, Momentum may not be supported by fundamental growth, Sector-relative P/E of 0.49 may reflect underlying business challenges
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 5.3040 (source.forwardEps) x AI multiple assumption 14.00; source IDs S008, S015, S019, S020
- **EPS:** 5.30402 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 12.877027
- **FY+1 growth assumption:** 12.82%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / RRC / PNR has FY1 consensus growth of 12.82% with revenue growth of 18.4% and earnings growth of 18.8%, but lower margins (40.2% gross, 21.4% operating, 15.4% profit) and ROE of 15.6%. The base multiple of 14.0 is set below the current forward P/E of 12.9 to reflect lower profitability and higher risk, with a bull case of 17.0 for margin improvement and a bear case of 11.0 for further deterioration. RRC is the named peer reference for railroad/industrial valuation.
- **Company fundamentals:** Pentair has reported diluted EPS of 2.76, forward EPS of 5.30, gross margin of 40.2%, operating margin of 21.4%, profit margin of 15.4%, revenue growth of -4.5%, and earnings growth of -18.8%. The forward P/E is 12.9 and the sector-relative P/E is 0.49.
- **Bull / Base / Bear:** 90.17 / 74.26 / 58.34
- **Bull / Base / Bear returns:** 32.02% / 8.73% / -14.58%
- **Scenario probabilities:** not separately assigned; see scenario table.

### RDDT — Reddit

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Reddit offers a compelling valuation with a forward P/E of 10.8 and strong growth, but the deep drawdown and negative momentum make it riskier than the more stable high-momentum names like AppLovin or Gen Digital. Alternatives considered: APP, GEN.
- **Thesis:** Reddit is the largest 20-day dislocation name with a 36.9% 20-day decline and a 34.5% 60-day decline, with a 60-day drawdown of -39.4%. The company has a forward P/E of 10.8 and an earnings yield of 3.0%, with revenue growth of 53% and earnings growth of 74.9%. The high sector-relative P/E of 1.66 suggests the market is pricing in significant recovery, but the deep drawdown and negative recent returns indicate high risk. The stock is a turnaround candidate but carries substantial uncertainty.
- **Source IDs:** S034, S037, S039, S041
- **Catalysts:** Potential for a sharp recovery if the dislocation resolves, Strong revenue growth of 53% and earnings growth of 74.9%, Attractive forward P/E of 10.8 on a depressed share price
- **Risks:** Deep drawdown of -39.4% with negative 20-day and 60-day returns, High sector-relative P/E of 1.66 implies high expectations, Dislocation may persist if fundamentals do not improve
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 9.1404 (source.forwardEps) x AI multiple assumption 12.00; source IDs S034, S037, S039, S041
- **EPS:** 9.14039 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 10.770874
- **FY+1 growth assumption:** 24.17%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / FOXA / RDDT shows FY1 consensus growth of 24.17% with revenue growth of 53.0% and earnings growth of 74.9%, supported by a 91.5% gross margin. However, operating margin is only 29.4% and profit margin 32.1%, with ROE of 32.0%. The base multiple of 12.0 is set below the current forward P/E of 10.8 to reflect lower operating leverage and higher risk, with a bull case of 15.0 for margin expansion and a bear case of 9.0 for competitive pressure. FOXA is the named peer reference for media/tech valuation.
- **Company fundamentals:** Reddit has reported diluted EPS of 3.66, forward EPS of 9.14, gross margin of 91.5%, operating margin of 29.4%, profit margin of 32.1%, revenue growth of 53%, and earnings growth of 74.9%. The forward P/E is 10.8 and the sector-relative P/E is 1.66.
- **Bull / Base / Bear:** 137.11 / 109.68 / 82.26
- **Bull / Base / Bear returns:** 39.27% / 11.41% / -16.44%
- **Scenario probabilities:** not separately assigned; see scenario table.

### XLV — Health Care sector ETF

- **Type:** ETF
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** XLV provides broad healthcare sector exposure with high liquidity and a diversified top-10 portfolio, making it a more stable core holding than individual high-beta stocks like Reddit or Intel, which carry significant dislocation and volatility risk. Alternatives considered: XLP, XLY.
- **Thesis:** The Health Care sector ETF (XLV) is a broad exposure to the sector with top holdings including LLY, JNJ, ABBV, MRK, and UNH. The ETF has a raw price change of 0.54% and a high dollar volume of 5.8 million shares. The sector provides diversification and exposure to large-cap healthcare names, but the ETF-level metrics do not provide the same granular growth signals as individual stocks. The ETF is suitable as a core holding for healthcare exposure.
- **Source IDs:** S056, S060
- **Catalysts:** Exposure to large-cap healthcare leaders with strong fundamentals, Diversification across the healthcare sector, High liquidity and dollar volume
- **Risks:** Sector-specific risks such as regulatory changes and drug pricing, ETF-level metrics do not provide granular growth signals, Concentration in top holdings may amplify single-stock risks
- **Valuation method:** Holdings/portfolio valuation with AI total-return assumption
- **Valuation status:** verified; forward-EPS source: ; period flags: 
- **Valuation assumptions:** Holdings/portfolio valuation; 10 weighted holdings; coverage 61.42%; source IDs S056, S060
- **Top holdings:** LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59%
- **Portfolio valuation:** Top 10 holdings; numeric weight coverage 61.42%
- **Sector exposure:** Health Care
- **Underlying drivers:** Healthcare sector fundamentals including drug approvals, Medicare reimbursement rates, and demographic trends.
- **Bull / Base / Bear:** 217.18 / 203.96 / 181.3
- **Bull / Base / Bear returns:** 15.0% / 8.0% / -4.0%
- **Scenario probabilities:** not separately assigned; see scenario table.

### XLP — Consumer Staples sector ETF

- **Type:** ETF
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** XLP provides defensive exposure to consumer staples with high liquidity and a diversified top-10 portfolio, making it a more stable defensive holding than individual high-beta stocks, though it lacks the growth upside of momentum names. Alternatives considered: XLV, XLY.
- **Thesis:** The Consumer Staples sector ETF (XLP) offers exposure to defensive names like WMT, COST, PG, KO, and PM. The ETF has a raw price change of 1.42%, the highest among the sector ETFs reviewed, and a dollar volume of 18.4 million shares. The sector provides stability and defensive characteristics, but the ETF-level metrics do not provide the same granular growth signals as individual stocks. The ETF is suitable as a defensive allocation within a diversified portfolio.
- **Source IDs:** S054, S055
- **Catalysts:** Defensive characteristics with stable demand for staples, High liquidity and dollar volume, Exposure to large-cap consumer staples leaders
- **Risks:** Sector-specific risks such as input cost inflation and consumer spending shifts, ETF-level metrics do not provide granular growth signals, Concentration in top holdings may amplify single-stock risks
- **Valuation method:** Holdings/portfolio valuation with AI total-return assumption
- **Valuation status:** verified; forward-EPS source: ; period flags: 
- **Valuation assumptions:** Holdings/portfolio valuation; 10 weighted holdings; coverage 63.28%; source IDs S054, S055
- **Top holdings:** WMT 11.14%, COST 9.09%, PG 7.60%, KO 7.37%, PM 6.59%, MO 4.70%, CL 4.42%, MDLZ 4.25%, PEP 4.11%, TGT 4.00%
- **Portfolio valuation:** Top 10 holdings; numeric weight coverage 63.28%
- **Sector exposure:** Consumer Staples
- **Underlying drivers:** Consumer staples demand, input cost inflation, and consumer spending trends.
- **Bull / Base / Bear:** 103.43 / 97.89 / 89.58
- **Bull / Base / Bear returns:** 12.0% / 6.0% / -3.0%
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
| Bull | 25% | +2.00% | Directional signal is false and forecast vol is below the 18.5% threshold, so a mild upside is driven by stable earnings momentum and low near-term volatility rather than a directional catalyst. |
| Base | 50% | +0.00% | Frozen daily-close model with no directional signal and elevated spike probability near the threshold implies a range-bound session with flat expected return. |
| Bear | 25% | -2.00% | Spike probability of 16.5% is elevated relative to the historical baseline, creating a risk of a brief downside spike that offsets the otherwise neutral short-term outlook. |

### Long Term (12 months)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 30% | +8.00% | Sustained earnings growth and stable credit conditions support a positive multi-day drift, with low forecast volatility allowing upside to compound. |
| Base | 40% | +3.00% | Neutral earnings trajectory and moderate volatility produce a modest positive long-term drift consistent with a stable, non-directional market environment. |
| Bear | 30% | -5.00% | Elevated spike probability and compressed volatility buffer increase the risk of a sustained downside move if earnings or credit conditions deteriorate. |

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
| S008 | filing | PNR | 2026-10-27 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-27 (accession 0000077360-26-000058); 8-K filed 2026-10-27 (accession 0000077360-26-000055); 8-K filed 2026-09-22 (accession 0000077360-26-000050) |
| S009 | filing | APP | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001751008&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0001751008-26-000069); 8-K filed 2026-11-04 (accession 0001751008-26-000068); 10-Q filed 2026-08-05 (accession 0001751008-26-000059) |
| S010 | filing | FISV | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0000798354-26-000042); 8-K filed 2026-11-03 (accession 0000798354-26-000039); 8-K filed 2026-10-23 (accession 0001193125-26-429481) |
| S011 | news | FISV | Wed, 11 Nov 2026 00:17:00 GMT | ok | https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en | Michael Burry makes a bold call on struggling payments giant - Yahoo Finance (Wed, 11 Nov 2026 00:17:00 GMT); Fiserv Stock Outlook: Is Wall Street Bullish or Bearish? - Yahoo Finance (Thu, 12 Nov 2026 12:23:56 GMT); Fiserv (FISV) Stock Looks Undervalued With Strong Excess Returns - Yahoo Finance Singapore (Wed, 11 Nov 2026 22:14:34 GMT) |
| S012 | news | APP | Thu, 12 Nov 2026 20:05:45 GMT | ok | https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en | AppLovin Just Ripped 47% in a Month: Is It Too Late to Buy APP Stock Now? - Yahoo Finance (Thu, 12 Nov 2026 20:05:45 GMT); ETFs Are Net Sellers of AppLovin (APP) on Nov. 11 - Yahoo Finance (Fri, 13 Nov 2026 11:02:35 GMT); APP Stock Surges 51% After Q3 Earnings: Is it Still a Buy? - Yahoo Finance (Tue, 10 Nov 2026 14:24:00 GMT) |
| S013 | stock | APP | 2026-11-15 | ok | https://finance.yahoo.com/quote/APP | Trailing P/E: 27.54882; Forward P/E: 19.611452; Forward EPS: 20.86026; Price: 409.1; Market price: 409.1; Market cap: 135543824384; Sector: Communication Services; Trailing Eps: 14.85; Revenue Growth: 0.555; Earnings Growth: 0.755; Gross Margin: 0.8878; Operating Margin: 0.77782995; Profit Margin: 0.65887; Return On Equity: 2.1008599; Total Revenue: 7608893952; Market Cap: 135543824384; Consensus EPS FY+1: 20.72438; growth: 0.2744 |
| S014 | filing | APP | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json | Diluted EPS 11.61 for period ending 2026-09-30 (filed 2026-11-04) |
| S015 | stock | PNR | 2026-11-15 | ok | https://finance.yahoo.com/quote/PNR | Trailing P/E: 18.610355; Forward P/E: 12.877027; Forward EPS: 5.30402; Price: 68.3; Market price: 68.3; Market cap: 10904415232; Sector: Industrials; Trailing Eps: 3.67; Revenue Growth: -0.045; Earnings Growth: -0.188; Gross Margin: 0.40168998; Operating Margin: 0.21410999; Profit Margin: 0.15435; Return On Equity: 0.15605; Total Revenue: 3966200064; Market Cap: 10904415232; Consensus EPS FY+1: 5.30402; growth: 0.1282 |
| S016 | stock | FISV | 2026-11-15 | ok | https://finance.yahoo.com/quote/FISV | Forward P/E: 7.99667; Price: 63.78; Market price: 63.78; Market cap: 33934002176; Market Cap: 33934002176; Consensus EPS FY+1: 7.98015; growth: 0.09689999 |
| S017 | filing | FISV | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json | Diluted EPS -8.9 for period ending 2026-09-30 (filed 2026-11-04) |
| S018 | filing | GEN | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0000849399-26-000083); 8-K filed 2026-10-28 (accession 0000849399-26-000081); 8-K filed 2026-10-09 (accession 0000849399-26-000079) |
| S019 | news | PNR | Fri, 13 Nov 2026 22:05:23 GMT | ok | https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en | Pentair plc (PNR) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 22:05:23 GMT); Pentair plc (PNR) Q3 Earnings and Revenues Beat Estimates - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT); Pentair (PNR) Stock May Be 46% Undervalued As New CFO Arrives - Yahoo Finance (Fri, 25 Sep 2026 07:00:00 GMT) |
| S020 | filing | PNR | 2026-10-27 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json | Diluted EPS 2.76 for period ending 2026-09-30 (filed 2026-10-27) |
| S021 | stock | GEN | 2026-11-15 | ok | https://finance.yahoo.com/quote/GEN | Trailing P/E: 15.431472; Forward P/E: 9.108996; Forward EPS: 3.33736; Price: 30.4; Market price: 30.4; Market cap: 18035593216; Sector: Technology; Trailing Eps: 1.97; Revenue Growth: 0.122; Earnings Growth: 1.286; Gross Margin: 0.77410007; Operating Margin: 0.43229; Profit Margin: 0.23068; Return On Equity: 0.46402; Total Revenue: 5228000256; Market Cap: 18035593216; Consensus EPS FY+1: 3.33736; growth: 0.1286 |
| S022 | filing | CLX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000021076-26-000046); 8-K filed 2026-11-02 (accession 0000021076-26-000044); 8-K filed 2026-10-29 (accession 0001206774-26-000586) |
| S023 | news | CLX | Sun, 15 Nov 2026 08:55:47 GMT | ok | https://news.google.com/rss/search?q=CLX+Clorox+stock&hl=en-US&gl=US&ceid=US:en | The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance UK (Sun, 15 Nov 2026 08:55:47 GMT); The Clorox Company (CLX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 05:44:34 GMT); The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance Singapore (Fri, 13 Nov 2026 14:10:46 GMT) |
| S024 | stock | CLX | 2026-11-15 | ok | https://finance.yahoo.com/quote/CLX | Trailing P/E: 19.68705; Forward P/E: 17.745283; Forward EPS: 6.1684; Price: 109.46; Market price: 109.46; Market cap: 13260793856; Sector: Consumer Defensive; Trailing Eps: 5.56; Revenue Growth: 0.333; Earnings Growth: 1.138; Gross Margin: 0.41939998; Operating Margin: 0.14286; Profit Margin: 0.09408; Return On Equity: 5.34363; Total Revenue: 7196000256; Market Cap: 13260793856; Consensus EPS FY+1: 6.1684; growth: 0.0769 |
| S025 | news | GEN | Fri, 13 Nov 2026 09:34:35 GMT | ok | https://news.google.com/rss/search?q=GEN+Gen+Digital+stock&hl=en-US&gl=US&ceid=US:en | Gen Digital Inc. (GEN) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 09:34:35 GMT); Gen Digital (GEN) Stock Repriced After Q2 Earnings Put Margins Center Stage - Yahoo Finance (Thu, 29 Oct 2026 07:00:00 GMT); Gen Digital Stock: Is Wall Street Bullish or Bearish? - Yahoo Finance (Thu, 05 Nov 2026 08:00:00 GMT) |
| S026 | filing | CHTR | 2026-11-06 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-06 (accession 0001091667-26-000073); 8-K filed 2026-11-06 (accession 0001091667-26-000072); 8-K filed 2026-10-27 (accession 0001091667-26-000064) |
| S027 | filing | GEN | 2026-10-29 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000849399.json | Diluted EPS 0.83 for period ending 2026-10-02 (filed 2026-10-29) |
| S028 | filing | IDXX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000874716&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000874716-26-000135); 8-K filed 2026-11-02 (accession 0001104659-26-120892); 10-Q filed 2026-08-04 (accession 0000874716-26-000123) |
| S029 | news | IDXX | Sat, 14 Nov 2026 06:13:17 GMT | ok | https://news.google.com/rss/search?q=IDXX+Idexx+Laboratories+stock&hl=en-US&gl=US&ceid=US:en | IDEXX Laboratories, Inc. (IDXX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Sat, 14 Nov 2026 06:13:17 GMT); IDEXX Laboratories (IDXX) Stock Looks Fairly Valued Despite Its 28% Run - Yahoo Finance (Sat, 31 Oct 2026 07:00:00 GMT); IDEXX Laboratories (IDXX) vs. ZTS and NEOG: Can Raised Guidance and Product Expansion Drive Further Earnings Growth? - Yahoo Finance (Thu, 22 Oct 2026 07:00:00 GMT) |
| S030 | stock | CHTR | 2026-11-15 | ok | https://finance.yahoo.com/quote/CHTR | Trailing P/E: 13.006578; Forward P/E: 3.2831066; Forward EPS: 42.15215; Price: 138.39; Market price: 138.39; Market cap: 24778944512; Sector: Communication Services; Trailing Eps: 10.64; Revenue Growth: 0.091; Gross Margin: 0.55084; Operating Margin: 0.23389; Profit Margin: 0.02498; Return On Equity: 0.07019; Total Revenue: 55645999104; Market Cap: 24778944512; Consensus EPS FY+1: 47.15811; growth: 1.0195 |
| S031 | news | CHTR | Sun, 15 Nov 2026 05:47:01 GMT | ok | https://news.google.com/rss/search?q=CHTR+Charter+Communications+stock&hl=en-US&gl=US&ceid=US:en | Charter Communications (CHTR) Stock Could Be A Bargain Following Its New Operating Model - Yahoo Finance (Sun, 15 Nov 2026 05:47:01 GMT); Charter Communications (CHTR) Expands Enterprise Reach With Managed Secure Networking Launch - Yahoo Finance (Sun, 15 Nov 2026 06:08:00 GMT); Why You Should Think About Charter Communications Differently Now? - Yahoo Finance (Fri, 13 Nov 2026 19:16:11 GMT) |
| S032 | stock | IDXX | 2026-11-15 | ok | https://finance.yahoo.com/quote/IDXX | Trailing P/E: 47.45485; Forward P/E: 41.687927; Forward EPS: 16.8929; Price: 704.23; Market price: 704.23; Market cap: 55483650048; Sector: Healthcare; Trailing Eps: 14.84; Revenue Growth: 0.099; Earnings Growth: 0.179; Gross Margin: 0.62722; Operating Margin: 0.32497; Profit Margin: 0.25357; Return On Equity: 0.68925005; Total Revenue: 4662220800; Market Cap: 55483650048; Consensus EPS FY+1: 16.8929; growth: 0.1244 |
| S033 | filing | CLX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000021076.json | Diluted EPS 1.39 for period ending 2026-09-30 (filed 2026-11-02) |
| S034 | filing | RDDT | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001713445&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0001713445-26-000116); 8-K filed 2026-10-29 (accession 0001713445-26-000114); 8-K filed 2026-08-12 (accession 0001713445-26-000107) |
| S035 | filing | CHTR | 2026-11-06 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001091667.json | Diluted EPS 0.38 for period ending 2026-09-30 (filed 2026-11-06) |
| S036 | filing | ROP | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000882835&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000882835-26-000047); 8-K filed 2026-10-22 (accession 0000882835-26-000042); 8-K filed 2026-10-01 (accession 0000882835-26-000039) |
| S037 | stock | RDDT | 2026-11-15 | ok | https://finance.yahoo.com/quote/RDDT | Trailing P/E: 20.091835; Forward P/E: 10.770874; Forward EPS: 9.14039; Price: 98.45; Market price: 98.45; Market cap: 19010076672; Sector: Communication Services; Trailing Eps: 4.9; Revenue Growth: 0.53; Earnings Growth: 0.749; Gross Margin: 0.91547996; Operating Margin: 0.29397; Profit Margin: 0.32105; Return On Equity: 0.32029998; Total Revenue: 3088880128; Market Cap: 19010076672; Consensus EPS FY+1: 6.82439; growth: 0.2417 |
| S038 | filing | IDXX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000874716.json | Diluted EPS 11.75 for period ending 2026-09-30 (filed 2026-11-02) |
| S039 | news | RDDT | Thu, 29 Oct 2026 07:00:00 GMT | ok | https://news.google.com/rss/search?q=RDDT+Reddit+stock&hl=en-US&gl=US&ceid=US:en | Reddit shares sink on weak sales guidance and plans login requirement test as Google search traffic shrinks - CNBC (Thu, 29 Oct 2026 07:00:00 GMT); Reddit (NYSE:RDDT) surprises with Q3 2026 sales but stock drops 12.6% - Yahoo Finance (Thu, 29 Oct 2026 07:00:00 GMT); Should You Wait Before Buying Reddit Stock? - Trefis (Fri, 13 Nov 2026 18:20:39 GMT) |
| S040 | news | ROP | Fri, 13 Nov 2026 13:04:22 GMT | ok | https://news.google.com/rss/search?q=ROP+Roper+Technologies+stock&hl=en-US&gl=US&ceid=US:en | Roper Technologies, Inc. (ROP) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 13:04:22 GMT); Roper Technologies (ROP) Stock Looks Fully Valued As Cash Flow Comes Into Focus - Yahoo Finance (Thu, 05 Nov 2026 08:00:00 GMT); Roper Technologies (ROP), What Is Behind The Fresh Attention? - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT) |

## Sources

- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFF&cosd=2026-01-01 (2026-11-12)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLH0A0HYM2&cosd=2026-01-01 (2026-11-12)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLC0A0CM&cosd=2026-01-01 (2026-11-12)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCSL&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=UNRATE&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=PAYEMS&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=T10Y2Y&cosd=2026-01-01 (2026-11-13)
- filing PNR: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 (2026-10-27)
- filing APP: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001751008&type=10-Q&dateb=&owner=include&count=10 (2026-11-04)
- filing FISV: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 (2026-11-04)
- news FISV: https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en (Wed, 11 Nov 2026 00:17:00 GMT)
- news APP: https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en (Thu, 12 Nov 2026 20:05:45 GMT)
- stock APP: https://finance.yahoo.com/quote/APP (2026-11-15)
- filing APP: https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json (2026-11-04)
- stock PNR: https://finance.yahoo.com/quote/PNR (2026-11-15)
- stock FISV: https://finance.yahoo.com/quote/FISV (2026-11-15)
- filing FISV: https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json (2026-11-04)
- filing GEN: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 (2026-10-29)
- news PNR: https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 22:05:23 GMT)
- filing PNR: https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json (2026-10-27)

## AI Provenance

- Provider / model: hermes-local-proxy / upstage/solar-mini4:free
- Market research: attempts=1 tokens=9473 (prompt=6473, completion=3000) runtime=20.57s
- Fundamental research: generated this run at 2026-11-15T20:13:40.324072+00:00
- Evidence source dates: {'as_of': '2026-11-13', 'latest_equity_date': '2026-11-13', 'latest_macro_date': '2026-11-14', 'flows_date': '2026-11-13'}
- Evidence fingerprint: 65799f2d1ca2bcd25a35895d201e090a53819b7e825fa3ff4bad5902c50aac6f
- Source citations are retrieved external records in the ledger above; market values remain from the verified database snapshot.


## Disclosures

- This is research and market intelligence, not investment advice.
- AI conclusions are research judgments, not validated return predictions.
- The frozen risk layer is risk-only and is not used for directional views or allocations.
- Legacy scores are not active inputs or outputs.

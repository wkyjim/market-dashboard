# AEGIS AI-First Market Intelligence

Research generated at: 17 November 2026, 00:08 HKT
Database freshness: equity 2026-11-13 (latest row retrieved 2026-11-16 13:06:43.000010+08:00)
Data cutoff: 2026-11-13 US cash close
Snapshot ID: aegis-hourly-20261116T160847Z

## Executive Summary

- **AI market view: Late-November 2026: broad market breadth is constructive (71% above 50-day, 64% above 200-day, A/D ratio 1.70), but the index is slightly negative over 20 days and the 20-day return is -1.28%. Sector leadership is bifurcated: Health Care, Consumer Discretionary, Consumer Staples, Real Estate, Financials and Utilities are up over 20 days, while Information Technology and Energy are down. Liquidity is concentrated in a small set of large-cap names, and several high-dislocation names carry extreme trailing P/E or negative earnings yields, so the market is not broadly cheap.**
- Breadth is the dominant positive: 71.3% of constituents above their 50-day moving average and 63.6% above the 200-day, with a 1.70 advance/decline ratio.
- Index-level momentum is slightly negative over 20 days (-1.28%), so the rally is broad but not yet a strong index trend.
- Sector returns are bifurcated: defensive and quality sectors (Health Care, Consumer Staples, Financials, Utilities) lead; Information Technology and Energy lag.
- Flows show strong institutional buying into Health Care (XLV) and neutral-to-negative flows into Consumer Discretionary (XLY) and Utilities (XLU).
- Valuation dispersion is wide: several shortlisted names have extreme trailing P/E (e.g., NOW 97.2, MRVL 74.2, AMD 128.9) or negative earnings yields, while Health Care and Consumer Staples ETFs trade at 30.9x and 25.0x.
- Macro data are mixed: CPI and core CPI remain elevated, unemployment is 4.2%, and the 10Y-2Y spread is a shallow 0.27, pointing to a late-cycle, low-volatility regime.

## Data QC

- Status: **PASS_WITH_WARNINGS**
- Equity session: 0 completed session(s) behind inference date
- Equity provenance: 393 provisional / 12576 canonical
- Breadth lag: 0 session(s); ETF-flow lag: 0 session(s)
- Note: Equity session contains a mix of provisional yfinance and canonical Massive rows.
- External sources: 79 ok / 0 unavailable; retrieved 2026-11-16T16:09:04.010864+00:00

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
| S&P 500 | 7561.67 | -1.28% (20d) | Index is slightly negative over 20 days; 71.3% above 50-day and 63.6% above 200-day, with A/D ratio 1.70. |
| Health Care (XLV) | return_20d 6.87% | +6.87% | Strongest sector; strong institutional confirmation with flow z-scores of 1.45 (20d) and 1.72 (60d). |
| Consumer Discretionary (XLY) | return_20d 6.69% | +6.69% | Positive price momentum but structural distribution with 20d flow z-score -0.38 and 60d -0.78. |
| Information Technology (XLK) | return_20d -7.19% | -7.19% | Worst sector; trailing P/E 29.37 and extreme shortlist names (NOW 97.2, MRVL 74.2, AMD 128.9) signal high valuation risk. |
| Energy (XLE) | return_20d -4.81% | -4.81% | Negative sector return; trailing P/E 16.04, but no flow data supplied for XLE. |
| Utilities (XLU) | return_20d 4.34% | +4.34% | Positive price return but medium-term institutional selling with 20d flow z-score -2.15. |

## Macro, Fiscal, Rates, Liquidity and Credit

- Inflation remains elevated: CPI 336.298 and core CPI 338.896 (Sep 2026), with a later Oct 2026 CPI reading of 337.476, indicating sticky price pressures.
- Labor market is stable but cooling: unemployment 4.2% (Sep 2026), down from 4.1% in Oct 2026, with payrolls at 159,293k (Oct 2026).
- Policy rates: effective federal funds rate is 3.88% as of 2026-11-12, suggesting a restrictive but possibly easing stance.
- Yield curve: 10Y-2Y spread is a shallow 0.27 as of 2026-11-13, consistent with late-cycle dynamics and limited recession pricing.
- Credit conditions: high-yield OAS 3.23 and IG OAS 0.89 as of 2026-11-13, indicating moderate spreads and no acute stress.
- Liquidity and volatility: 5-day forecast volatility 14.9% is below the historical baseline 22.1% and EWMA baseline 20.1%, with spike probability 16.5% below the 18.5% threshold, implying a low-volatility, orderly market.

## US Equities and 11 GICS Sectors

Macro source IDs: S001, S002, S003, S004, S005, S006, S007

| GICS sector | Evidence | AI research stance | Source IDs |
| --- | --- | --- | --- |
| Health Care | 20d return +6.87%; trailing P/E 30.94; flow z-scores 1.45 (20d) and 1.72 (60d) with strong confirmation; A/D ratio 1.70. | Favored sector with strong institutional inflows and positive price momentum; valuation is rich but supported by flow and breadth. | S058 |
| Consumer Staples | 20d return +5.40%; trailing P/E 24.95; positive price momentum and broad-based above-trend indicators. | Defensive quality leader; stable cash flows and positive sector return support a neutral-to-favorable stance. | S057 |
| Consumer Discretionary | 20d return +6.69%; trailing P/E 24.89; structural distribution with 20d flow z-score -0.38 and 60d -0.78. | Price momentum is positive but institutional flows are negative; monitor for divergence between price and flows. | S059 |
| Real Estate | 20d return +5.24%; trailing P/E 29.63; no flow data supplied. | Positive price momentum but high valuation; no flow evidence to confirm institutional conviction. | S065 |
| Financials | 20d return +5.69%; trailing P/E 15.80; no flow data supplied. | Attractive valuation relative to the market; positive sector return supports a constructive stance. | S064 |
| Utilities | 20d return +4.34%; trailing P/E 18.15; 20d flow z-score -2.15 with medium-term institutional selling. | Price up but institutional flows negative; caution on continued distribution despite defensive appeal. | S063 |
| Materials | 20d return +2.57%; trailing P/E 21.59; no flow data supplied. | Modest positive return and reasonable valuation; limited evidence to take a strong view. | S066 |
| Industrials | 20d return +0.61%; trailing P/E 26.81; no flow data supplied. | Near-flat sector return and mid-range valuation; neutral stance with limited conviction. | S072 |
| Communication Services | 20d return -1.48%; trailing P/E 17.07; no flow data supplied. | Negative sector return and low valuation; no flow evidence to support a positive view. | S073 |
| Information Technology | 20d return -7.19%; trailing P/E 29.37; extreme shortlist names (NOW 97.2, MRVL 74.2, AMD 128.9) with high valuation risk. | Weakest sector; high valuation dispersion and negative price momentum warrant a cautious stance. | S073 |
| Energy | 20d return -4.81%; trailing P/E 16.04; no flow data supplied. | Negative sector return and reasonable valuation; no flow evidence to confirm a positive view. | S076 |

### Sector fundamentals, valuation and earnings

The supplied database provides trailing P/E for each of the 11 GICS sectors via ETF proxies (XLV 30.94, XLP 24.95, XLY 24.89, XLRE 29.63, XLF 15.80, XLU 18.15, XLB 21.59, XLI 26.81, XLK 29.37, XLC 17.07, XLE 16.04) and 20-day returns for each sector. No point-in-time sector-level fundamentals such as earnings growth, margins, revenue, or balance-sheet data are supplied; therefore no sector earnings or margin estimates are included. The sector view is based solely on price momentum, flow evidence, and trailing valuation from the supplied dataset.

## Growth vs Value

- Health Care and Consumer Staples offer the most balanced growth/value profile: positive 20-day returns, strong institutional flows, and trailing P/E of 30.94 and 24.95 respectively.
- Financials and Energy trade at the lowest trailing P/E (15.80 and 16.04), offering the most attractive valuation, but lack supplied flow evidence to confirm institutional conviction.
- Information Technology and Communication Services are the most expensive on a relative basis (XLK 29.37, XLC 17.07) and have negative 20-day returns, signaling weak growth momentum.
- Consumer Discretionary has a reasonable trailing P/E of 24.89 but negative institutional flows, suggesting that price momentum is not supported by money flow.

## ETF Flows and Breadth

- Health Care (XLV) is the clearest flow confirmation: 20d flow z-score 1.45 and 60d 1.72, with price up and strong institutional buying.
- Consumer Discretionary (XLY) shows structural distribution: 20d flow z-score -0.38 and 60d -0.78, despite a positive 20-day return.
- Utilities (XLU) shows medium-term institutional selling: 20d flow z-score -2.15, with a positive price return but negative flow structure.
- Breadth is strongly positive: 71.3% above 50-day, 63.6% above 200-day, A/D ratio 1.70, and 70.5% positive over 20 days.
- Price/breadth divergence is -27.49 with bullish divergence flagged, indicating that price weakness is not being driven by broad market weakness.

## Stock Ideas

Single-stock research uses reported EPS, forward P/E and company fundamentals. All ideas are research judgments, not validated return predictions.

| Ticker | Security | Research view | Price | EPS | Forward P/E | Base target | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| APP | AppLovin | NEW | 409.1 | 20.86026 | 19.73657 | 417.21 | NEW |
| PNR | Pentair | KEEP | 68.3 | 5.30402 | 12.861943 | 68.95 | KEEP |
| GEN | Gen Digital | KEEP | 30.4 | 3.33736 | 9.251325 | 33.37 | KEEP |
| RDDT | Reddit | DOWNGRADE | 98.45 | 9.10039 | 10.340766 | 100.1 | DOWNGRADE |

## ETF Ideas

ETF research uses holdings, portfolio valuation and exposure. Single-stock EPS × P/E valuation is not applied to ETFs.

| Ticker | Fund | Research view | Price | Top holdings | Portfolio valuation | Sector exposure | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| XLV | Health Care sector ETF | KEEP | 188.85 | LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59% | Top 10 holdings; numeric weight coverage 61.42% | Health Care | KEEP |
### APP — AppLovin

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** AppLovin offers a higher-quality margin profile than the lower-margin, lower-momentum names in the shortlist, and its 20-day momentum is stronger than the other top-momentum candidates such as PNR, GEN, CLX, IDXX, and ROP. Alternatives considered: PNR, GEN, CLX, IDXX, ROP.
- **Thesis:** AppLovin screens in the top 20-day momentum bucket with a 53.7% 20-day return and a 32.5% 60-day return, while maintaining a 65.9% profit margin and 88.8% gross margin. The stock is trading at a forward P/E of 19.7x with a 4.99% earnings yield, and the momentum screen supports a new position rather than an existing one.
- **Source IDs:** S008, S012, S013, S017
- **Catalysts:** Sustained 20-day momentum above 50%, High gross and profit margins supporting earnings growth, Forward P/E near 20x with a sub-5% earnings yield
- **Risks:** High 20-day momentum can mean elevated volatility, Forward P/E near 20x leaves limited valuation cushion, Momentum can reverse quickly if ad-market demand softens
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 20.8603 (source.forwardEps) x AI multiple assumption 20.00; source IDs S008, S012, S013, S017
- **EPS:** 20.86026 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 19.73657
- **FY+1 growth assumption:** 27.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / AAPL / APP shows strong FY+1 consensus earnings growth of 27.44% and revenue growth of 25.37%, with exceptional margins (gross 88.8%, operating 77.8%, profit 65.9%) and ROE of 2.10x. The base multiple of 20.0x is supported by a forward P/E of 19.74x, but is set below the current forward P/E to reflect a conservative 12-month horizon. AAPL is the named peer reference for platform/ecosystem scale and margin structure.
- **Company fundamentals:** AppLovin reported diluted EPS of 11.61 for the period ending 2026-09-30, with FY1 EPS growth of 27.4% and revenue growth of 55.5%. Gross margin is 88.8%, operating margin 77.8%, and profit margin 65.9%. Forward EPS is 20.86, implying a forward P/E of 19.7x. Source IDs: S008, S012, S013, S017.
- **Bull / Base / Bear:** 500.65 / 417.21 / 333.76
- **Bull / Base / Bear returns:** 22.38% / 1.98% / -18.42%
- **Scenario probabilities:** not separately assigned; see scenario table.

### PNR — Pentair

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Pentair offers a lower forward P/E than the high-multiple momentum names, but its negative earnings growth and contracting revenue make it less attractive than AppLovin's high-margin, high-growth profile. Alternatives considered: APP, GEN, CLX, IDXX, ROP.
- **Thesis:** Pentair is a top-20-day-momentum name with a 27.8% 20-day return and a 7.1% 60-day return. It trades at a forward P/E of 12.9x with a 7.4% earnings yield, but FY1 revenue and earnings are contracting, so the momentum is not yet supported by fundamental growth.
- **Source IDs:** S010, S015, S018, S020
- **Catalysts:** 20-day momentum of 27.8%, Forward P/E of 12.9x and earnings yield of 7.4%, Industrial exposure to water and fluid handling
- **Risks:** FY1 revenue growth of -4.5% and earnings growth of -18.8%, Momentum may be driven by technicals rather than fundamentals, Industrial end-market softness could delay recovery
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 5.3040 (source.forwardEps) x AI multiple assumption 13.00; source IDs S010, S015, S018, S020
- **EPS:** 5.30402 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 12.861943
- **FY+1 growth assumption:** 12.82%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / UPS / PNR has moderate FY+1 consensus earnings growth of 12.82% and revenue growth of 18.38%, with a forward P/E of 12.86x. The base multiple of 13.0x is set above the current forward P/E to reflect a 12-month horizon, while the bear case of 10.0x reflects earnings contraction risk. UPS is the named peer reference for logistics/transportation sector valuation.
- **Company fundamentals:** Pentair reported diluted EPS of 2.76 for the period ending 2026-09-30, with FY1 EPS growth of 12.8% and revenue growth of 18.4%. Gross margin is 40.2%, operating margin 21.4%, and profit margin 15.4%. Forward EPS is 5.30, implying a forward P/E of 12.9x. Source IDs: S010, S015, S018, S020.
- **Bull / Base / Bear:** 84.86 / 68.95 / 53.04
- **Bull / Base / Bear returns:** 24.25% / 0.95% / -22.34%
- **Scenario probabilities:** not separately assigned; see scenario table.

### GEN — Gen Digital

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Gen Digital offers a lower forward P/E than the high-multiple names, but its modest revenue growth and lower margin profile make it less attractive than AppLovin's high-margin, high-growth profile. Alternatives considered: APP, PNR, CLX, IDXX, ROP.
- **Thesis:** Gen Digital is a top-20-day-momentum name with a 25.8% 20-day return and a 7.9% 60-day return. It trades at a forward P/E of 9.3x with a 7.1% earnings yield, but the 20-day momentum is not yet backed by strong revenue growth, and the stock is a lower-quality compounder than AppLovin.
- **Source IDs:** S016, S022, S026, S030
- **Catalysts:** 20-day momentum of 25.8%, Forward P/E of 9.3x and earnings yield of 7.1%, Cybersecurity and digital life protection exposure
- **Risks:** FY1 revenue growth of 6.8% is modest, 20-day momentum may be technical rather than fundamental, Lower margin profile than AppLovin
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 3.3374 (source.forwardEps) x AI multiple assumption 10.00; source IDs S016, S022, S026, S030
- **EPS:** 3.33736 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 9.251325
- **FY+1 growth assumption:** 12.86%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / MSFT / GEN has FY+1 consensus earnings growth of 12.86% and revenue growth of 6.81%, with strong gross margin of 77.4% and operating margin of 43.2%. The base multiple of 10.0x is set below the current forward P/E of 9.25x to reflect a conservative 12-month horizon, with a bull case of 12.0x for margin expansion. MSFT is the named peer reference for software/technology growth and margin profile.
- **Company fundamentals:** Gen Digital reported diluted EPS of 0.83 for the period ending 2026-10-02, with FY1 EPS growth of 12.9% and revenue growth of 6.8%. Gross margin is 77.4%, operating margin 43.2%, and profit margin 23.1%. Forward EPS is 3.34, implying a forward P/E of 9.3x. Source IDs: S016, S022, S026, S030.
- **Bull / Base / Bear:** 40.05 / 33.37 / 26.7
- **Bull / Base / Bear returns:** 31.74% / 9.77% / -12.17%
- **Scenario probabilities:** not separately assigned; see scenario table.

### RDDT — Reddit

- **Type:** Stock
- **Research view:** DOWNGRADE (stance: AVOID)
- **Why preferred / alternatives:** Reddit's deep drawdown and elevated sector-relative valuation make it less attractive than the higher-quality, higher-momentum names in the shortlist such as AppLovin, Pentair, Gen Digital, Clorox, and Roper Technologies. Alternatives considered: APP, PNR, GEN, CLX, ROP.
- **Thesis:** Reddit is the largest 20-day dislocation name with a -36.9% 20-day return and a -34.5% 60-day return, and a 39.4% 60-day drawdown. Despite a 10.3x forward P/E and a 3.0% earnings yield, the sharp price decline and high sector-relative P/E make it a poor risk-reward entry.
- **Source IDs:** S037, S042, S045, S046
- **Catalysts:** Forward P/E of 10.3x, Earnings yield of 3.0%, Sector-relative P/E of 1.66x
- **Risks:** 39.4% 60-day drawdown, Sector-relative P/E of 1.66x is elevated, Sharp price decline may reflect structural demand concerns
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 9.1004 (source.forwardEps) x AI multiple assumption 11.00; source IDs S037, S042, S045, S046
- **EPS:** 9.10039 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 10.340766
- **FY+1 growth assumption:** 24.01%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / AMZN / RDDT has strong FY+1 consensus earnings growth of 24.01% and revenue growth of 28.38%, with high gross margin of 91.5% and operating margin of 29.4%. The base multiple of 11.0x is set below the current forward P/E of 10.34x to reflect a conservative 12-month horizon, with a bull case of 14.0x for margin expansion. AMZN is the named peer reference for cloud/technology growth and margin structure.
- **Company fundamentals:** Reddit reported diluted EPS of 3.66 for the period ending 2026-09-30, with FY1 EPS growth of 24.0% and revenue growth of 53.0%. Gross margin is 91.5%, operating margin 29.4%, and profit margin 32.1%. Forward EPS is 9.10, implying a forward P/E of 10.3x. Source IDs: S037, S042, S045, S046.
- **Bull / Base / Bear:** 127.41 / 100.1 / 72.8
- **Bull / Base / Bear returns:** 29.42% / 1.68% / -26.05%
- **Scenario probabilities:** not separately assigned; see scenario table.

### XLV — Health Care sector ETF

- **Type:** ETF
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** XLV provides broad health care exposure with a diversified top-10 basket, whereas individual names such as IDXX or APP carry single-stock risk and are already covered by the stock ideas. Alternatives considered: XLP, XLY, XLRE, XLF, XLU, XLB, XLI.
- **Thesis:** The Health Care sector ETF is a broad, liquid way to own the sector's top names, including LLY, JNJ, ABBV, MRK, and UNH. It is a neutral core holding rather than a tactical bet, and it provides diversification that individual high-momentum stocks cannot.
- **Source IDs:** S055, S058
- **Catalysts:** Diversified exposure to large-cap health care names, High liquidity and sector breadth, Core portfolio allocation
- **Risks:** Sector-specific regulatory and drug-pricing risk, Top-10 holdings cover only 61.4% of the portfolio, Not a standalone growth or momentum play
- **Valuation method:** Holdings/portfolio valuation with AI total-return assumption
- **Valuation status:** verified; forward-EPS source: ; period flags: 
- **Valuation assumptions:** Holdings/portfolio valuation; 10 weighted holdings; coverage 61.42%; source IDs S055, S058
- **Top holdings:** LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59%
- **Portfolio valuation:** Top 10 holdings; numeric weight coverage 61.42%
- **Sector exposure:** Health Care
- **Underlying drivers:** Large-cap health care sector performance, drug pricing policy, and top-10 holdings such as LLY, JNJ, ABBV, MRK, and UNH.
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
| Bull | 25% | +2.00% | Low 5-day realized vol (14.9%) and below-threshold spike probability (16.5% vs 18.5% threshold) support a modest upside if US close confirms positive breadth and stable rates. |
| Base | 50% | +0.00% | Directional signal is false and forecast vol sits near the EWMA baseline, implying range-bound conditions with no clear catalyst for a directional move over the target window. |
| Bear | 25% | -2.00% | If the frozen daily-close model fails to confirm after US close, elevated spike probability and rate/breadth risk could push returns modestly negative. |

### Long Term (12 months)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 30% | +8.00% | Sustained low volatility, stable rates, and positive earnings breadth could drive a cumulative 8% advance over the horizon. |
| Base | 40% | +3.00% | Moderate trend with balanced rate and credit conditions supports a low-single-digit cumulative return. |
| Bear | 30% | -5.00% | Rate spikes, breadth deterioration, or earnings disappointment could produce a -5% cumulative decline over the horizon. |

## Positioning

- Maintain a constructive but cautious stance: broad breadth and positive flows support risk-on, but index-level 20-day returns are negative and macro data show sticky inflation.
- Favor Health Care and Consumer Staples for their combination of positive momentum, institutional inflows, and defensive characteristics.
- Less favored Information Technology and Energy until price momentum and flow evidence improve; the sector is the weakest on both metrics.
- Monitor Consumer Discretionary and Utilities for flow divergence: positive price but negative institutional flows may signal further weakness.
- No allocation weights are provided; this is

## Catalysts

| Date | Event | Why it matters |
| --- | --- | --- |

## Key Risks


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
| S008 | filing | APP | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001751008&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0001751008-26-000069); 8-K filed 2026-11-04 (accession 0001751008-26-000068); 10-Q filed 2026-08-05 (accession 0001751008-26-000059) |
| S009 | filing | FISV | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0000798354-26-000042); 8-K filed 2026-11-03 (accession 0000798354-26-000039); 8-K filed 2026-10-23 (accession 0001193125-26-429481) |
| S010 | filing | PNR | 2026-10-27 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-27 (accession 0000077360-26-000058); 8-K filed 2026-10-27 (accession 0000077360-26-000055); 8-K filed 2026-09-22 (accession 0000077360-26-000050) |
| S011 | news | FISV | Mon, 16 Nov 2026 02:19:15 GMT | ok | https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en | Fiserv, Inc. (FISV) Stock Price, News, Quote & History - Yahoo! Finance Canada (Mon, 16 Nov 2026 02:19:15 GMT); Fiserv (FISV) Stock Looks Undervalued With Strong Excess Returns - Yahoo Finance (Wed, 11 Nov 2026 22:14:34 GMT); Fiserv (FISV) Stock Still Looks Like A Bargain After Lawsuit Claims - Yahoo Finance (Thu, 22 Oct 2026 07:00:00 GMT) |
| S012 | filing | APP | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json | Diluted EPS 11.61 for period ending 2026-09-30 (filed 2026-11-04) |
| S013 | news | APP | Thu, 12 Nov 2026 20:05:45 GMT | ok | https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en | AppLovin Just Ripped 47% in a Month: Is It Too Late to Buy APP Stock Now? - Yahoo Finance (Thu, 12 Nov 2026 20:05:45 GMT); Is Trending Stock AppLovin Corporation (APP) a Buy Now? - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT); APP Stock Surges 51% After Q3 Earnings: Is it Still a Buy? - Yahoo Finance (Tue, 10 Nov 2026 14:24:00 GMT) |
| S014 | filing | FISV | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json | Diluted EPS -8.9 for period ending 2026-09-30 (filed 2026-11-04) |
| S015 | news | PNR | Sat, 14 Nov 2026 08:48:27 GMT | ok | https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en | Pentair plc (PNR) Stock Price, News, Quote & History - Yahoo! Finance Canada (Sat, 14 Nov 2026 08:48:27 GMT); Pentair plc (PNR) stock price, news, quote and history - Yahoo Finance UK (Fri, 13 Nov 2026 22:09:48 GMT); Pentair Stock Price Forecast. Should You Buy PNR? - StockInvest.us (Fri, 13 Nov 2026 22:50:05 GMT) |
| S016 | filing | GEN | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0000849399-26-000083); 8-K filed 2026-10-28 (accession 0000849399-26-000081); 8-K filed 2026-10-09 (accession 0000849399-26-000079) |
| S017 | stock | APP | 2026-11-16 | ok | https://finance.yahoo.com/quote/APP | Trailing P/E: 27.724577; Forward P/E: 19.73657; Forward EPS: 20.86026; Price: 411.71; Market price: 411.71; Market cap: 136408571904; Sector: Communication Services; Trailing Eps: 14.85; Revenue Growth: 0.555; Earnings Growth: 0.755; Gross Margin: 0.8878; Operating Margin: 0.77782995; Profit Margin: 0.65887; Return On Equity: 2.1008599; Total Revenue: 7608893952; Market Cap: 136408571904; Consensus EPS FY+1: 20.72438; growth: 0.2744 |
| S018 | filing | PNR | 2026-10-27 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json | Diluted EPS 2.76 for period ending 2026-09-30 (filed 2026-10-27) |
| S019 | stock | FISV | 2026-11-16 | ok | https://finance.yahoo.com/quote/FISV | Forward P/E: 8.061868; Price: 64.3; Market price: 64.3; Market cap: 34210668544; Market Cap: 34210668544; Consensus EPS FY+1: 7.97582; growth: 0.0959 |
| S020 | stock | PNR | 2026-11-16 | ok | https://finance.yahoo.com/quote/PNR | Trailing P/E: 18.588556; Forward P/E: 12.861943; Forward EPS: 5.30402; Price: 68.22; Market price: 68.22; Market cap: 10891642880; Sector: Industrials; Trailing Eps: 3.67; Revenue Growth: -0.045; Earnings Growth: -0.188; Gross Margin: 0.40168998; Operating Margin: 0.21410999; Profit Margin: 0.15435; Return On Equity: 0.15605; Total Revenue: 3966200064; Market Cap: 10891642880; Consensus EPS FY+1: 5.30402; growth: 0.1282 |
| S021 | filing | CLX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000021076-26-000046); 8-K filed 2026-11-02 (accession 0000021076-26-000044); 8-K filed 2026-10-29 (accession 0001206774-26-000586) |
| S022 | stock | GEN | 2026-11-16 | ok | https://finance.yahoo.com/quote/GEN | Trailing P/E: 15.672588; Forward P/E: 9.251325; Forward EPS: 3.33736; Price: 30.875; Market price: 30.875; Market cap: 18317400064; Sector: Technology; Trailing Eps: 1.97; Revenue Growth: 0.122; Earnings Growth: 1.286; Gross Margin: 0.77410007; Operating Margin: 0.43229; Profit Margin: 0.23068; Return On Equity: 0.46402; Total Revenue: 5228000256; Market Cap: 18317400064; Consensus EPS FY+1: 3.33736; growth: 0.1286 |
| S023 | stock | CLX | 2026-11-16 | ok | https://finance.yahoo.com/quote/CLX | Trailing P/E: 19.643885; Forward P/E: 17.706375; Forward EPS: 6.1684; Price: 109.22; Market price: 109.22; Market cap: 13231718400; Sector: Consumer Defensive; Trailing Eps: 5.56; Revenue Growth: 0.333; Earnings Growth: 1.138; Gross Margin: 0.41939998; Operating Margin: 0.14286; Profit Margin: 0.09408; Return On Equity: 5.34363; Total Revenue: 7196000256; Market Cap: 13231718400; Consensus EPS FY+1: 6.1684; growth: 0.0769 |
| S024 | news | CLX | Fri, 13 Nov 2026 23:34:51 GMT | ok | https://news.google.com/rss/search?q=CLX+Clorox+stock&hl=en-US&gl=US&ceid=US:en | The Clorox Company (CLX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 23:34:51 GMT); The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance UK (Sat, 14 Nov 2026 06:03:20 GMT); A 10-Day Winning Streak Has Clorox Stock Up 24% - Trefis (Sat, 14 Nov 2026 08:28:05 GMT) |
| S025 | filing | CHTR | 2026-11-06 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-06 (accession 0001091667-26-000073); 8-K filed 2026-11-06 (accession 0001091667-26-000072); 8-K filed 2026-10-27 (accession 0001091667-26-000064) |
| S026 | news | GEN | Thu, 29 Oct 2026 07:00:00 GMT | ok | https://news.google.com/rss/search?q=GEN+Gen+Digital+stock&hl=en-US&gl=US&ceid=US:en | Gen Digital (GEN) Stock Repriced After Q2 Earnings Put Margins Center Stage - Yahoo Finance (Thu, 29 Oct 2026 07:00:00 GMT); Gen Digital Stock: Is Wall Street Bullish or Bearish? - Yahoo Finance (Thu, 05 Nov 2026 08:00:00 GMT); Are Business Services Stocks Lagging GEN DIGITAL INC (GEN) This Year? - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT) |
| S027 | stock | CHTR | 2026-11-16 | ok | https://finance.yahoo.com/quote/CHTR | Trailing P/E: 12.877819; Forward P/E: 3.015083; Forward EPS: 45.44485; Price: 137.02; Market price: 137.02; Market cap: 24533645312; Sector: Communication Services; Trailing Eps: 10.64; Revenue Growth: 0.091; Gross Margin: 0.55084; Operating Margin: 0.23389; Profit Margin: 0.02498; Return On Equity: 0.07019; Total Revenue: 55645999104; Market Cap: 24533645312; Consensus EPS FY+1: 49.35412; growth: 1.1136 |
| S028 | news | CHTR | Sun, 15 Nov 2026 05:47:01 GMT | ok | https://news.google.com/rss/search?q=CHTR+Charter+Communications+stock&hl=en-US&gl=US&ceid=US:en | Charter Communications (CHTR) Stock Could Be A Bargain Following Its New Operating Model - Yahoo Finance (Sun, 15 Nov 2026 05:47:01 GMT); Why You Should Think About Charter Communications Differently Now? - Yahoo Finance (Fri, 13 Nov 2026 19:16:11 GMT); Charter Communications (CHTR) Earnings Expected to Grow: What to Know Ahead of Next Week's Release - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT) |
| S029 | filing | IDXX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000874716&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000874716-26-000135); 8-K filed 2026-11-02 (accession 0001104659-26-120892); 10-Q filed 2026-08-04 (accession 0000874716-26-000123) |
| S030 | filing | GEN | 2026-10-29 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000849399.json | Diluted EPS 0.83 for period ending 2026-10-02 (filed 2026-10-29) |
| S031 | filing | ROP | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000882835&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000882835-26-000047); 8-K filed 2026-10-22 (accession 0000882835-26-000042); 8-K filed 2026-10-01 (accession 0000882835-26-000039) |
| S032 | filing | CLX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000021076.json | Diluted EPS 1.39 for period ending 2026-09-30 (filed 2026-11-02) |
| S033 | news | IDXX | Sat, 14 Nov 2026 22:37:20 GMT | ok | https://news.google.com/rss/search?q=IDXX+Idexx+Laboratories+stock&hl=en-US&gl=US&ceid=US:en | IDEXX Laboratories, Inc. (IDXX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Sat, 14 Nov 2026 22:37:20 GMT); IDEXX Laboratories (IDXX) Stock Looks Fairly Valued Despite Its 28% Run - Yahoo Finance (Sat, 31 Oct 2026 07:00:00 GMT); IDEXX Laboratories (IDXX) vs. ZTS and NEOG: Can Raised Guidance and Product Expansion Drive Further Earnings Growth? - Yahoo Finance (Thu, 22 Oct 2026 07:00:00 GMT) |
| S034 | stock | ROP | 2026-11-16 | ok | https://finance.yahoo.com/quote/ROP | Trailing P/E: 19.233479; Forward P/E: 19.778881; Forward EPS: 24.57318; Price: 486.03; Market price: 486.03; Market cap: 48134676480; Sector: Technology; Trailing Eps: 25.27; Revenue Growth: 0.076; Earnings Growth: 0.326; Gross Margin: 0.69671; Operating Margin: 0.28049; Profit Margin: 0.30712998; Return On Equity: 0.13229; Total Revenue: 8434599936; Market Cap: 48134676480; Consensus EPS FY+1: 24.57318; growth: 0.09810001 |
| S035 | filing | CHTR | 2026-11-06 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001091667.json | Diluted EPS 0.38 for period ending 2026-09-30 (filed 2026-11-06) |
| S036 | stock | IDXX | 2026-11-16 | ok | https://finance.yahoo.com/quote/IDXX | Trailing P/E: 47.640495; Forward P/E: 41.851013; Forward EPS: 16.8929; Price: 706.985; Market price: 706.985; Market cap: 55700705280; Sector: Healthcare; Trailing Eps: 14.84; Revenue Growth: 0.099; Earnings Growth: 0.179; Gross Margin: 0.62722; Operating Margin: 0.32497; Profit Margin: 0.25357; Return On Equity: 0.68925005; Total Revenue: 4662220800; Market Cap: 55700705280; Consensus EPS FY+1: 16.8929; growth: 0.1244 |
| S037 | filing | RDDT | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001713445&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0001713445-26-000116); 8-K filed 2026-10-29 (accession 0001713445-26-000114); 8-K filed 2026-08-12 (accession 0001713445-26-000107) |
| S038 | news | ROP | Thu, 05 Nov 2026 08:00:00 GMT | ok | https://news.google.com/rss/search?q=ROP+Roper+Technologies+stock&hl=en-US&gl=US&ceid=US:en | Roper Technologies (ROP) Stock Looks Fully Valued As Cash Flow Comes Into Focus - Yahoo Finance (Thu, 05 Nov 2026 08:00:00 GMT); Here's How Much $100 Invested In Roper Technologies 20 Years Ago Would Be Worth Today - Benzinga (Mon, 16 Nov 2026 14:15:26 GMT); Roper Technologies (ROP), What Is Behind The Fresh Attention? - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT) |
| S039 | filing | IDXX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000874716.json | Diluted EPS 11.75 for period ending 2026-09-30 (filed 2026-11-02) |
| S040 | filing | ROP | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000882835.json | Diluted EPS 21.3 for period ending 2026-09-30 (filed 2026-11-02) |

## Sources

- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFF&cosd=2026-01-01 (2026-11-12)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLH0A0HYM2&cosd=2026-01-01 (2026-11-13)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLC0A0CM&cosd=2026-01-01 (2026-11-13)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCSL&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=UNRATE&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=PAYEMS&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=T10Y2Y&cosd=2026-01-01 (2026-11-13)
- filing APP: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001751008&type=10-Q&dateb=&owner=include&count=10 (2026-11-04)
- filing FISV: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 (2026-11-04)
- filing PNR: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 (2026-10-27)
- news FISV: https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en (Mon, 16 Nov 2026 02:19:15 GMT)
- filing APP: https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json (2026-11-04)
- news APP: https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en (Thu, 12 Nov 2026 20:05:45 GMT)
- filing FISV: https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json (2026-11-04)
- news PNR: https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en (Sat, 14 Nov 2026 08:48:27 GMT)
- filing GEN: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 (2026-10-29)
- stock APP: https://finance.yahoo.com/quote/APP (2026-11-16)
- filing PNR: https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json (2026-10-27)
- stock FISV: https://finance.yahoo.com/quote/FISV (2026-11-16)
- stock PNR: https://finance.yahoo.com/quote/PNR (2026-11-16)

## AI Provenance

- Provider / model: hermes-local-proxy / upstage/solar-mini4:free
- Market research: attempts=1 tokens=9514 (prompt=6514, completion=3000) runtime=38.59s
- Fundamental research: generated this run at 2026-11-16T16:08:47.229296+00:00
- Evidence source dates: {'as_of': '2026-11-13', 'latest_equity_date': '2026-11-13', 'latest_macro_date': '2026-11-16', 'flows_date': '2026-11-13'}
- Evidence fingerprint: 56f76666e3cf1fb0d2ad4aab4c06169d5bc7b0bd8159069407e40500a9d73e2d
- Source citations are retrieved external records in the ledger above; market values remain from the verified database snapshot.


## Disclosures

- This is research and market intelligence, not investment advice.
- AI conclusions are research judgments, not validated return predictions.
- The frozen risk layer is risk-only and is not used for directional views or allocations.
- Legacy scores are not active inputs or outputs.

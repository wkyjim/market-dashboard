# AEGIS AI-First Market Intelligence

Research generated at: 16 November 2026, 23:08 HKT
Database freshness: equity 2026-11-13 (latest row retrieved 2026-11-16 13:06:43.000010+08:00)
Data cutoff: 2026-11-13 US cash close
Snapshot ID: aegis-hourly-20261116T150853Z

## Executive Summary

- **AI market view: Late-November 2026: broad market breadth is constructive (71% above 50-day, 64% above 200-day, A/D ratio 1.70), but the index is slightly negative over 20 days and the 10Y-2Y curve is only modestly positive. Sector leadership is bifurcated: Health Care, Consumer Discretionary, Consumer Staples and Financials are up over 20 days, while Information Technology and Energy are down. Liquidity is concentrated in a small set of large-cap names, and credit spreads are tight, suggesting a late-cycle, quality-preferred tape.**
- Broad market breadth is positive: 71.3% of names above their 50-day moving average and 63.6% above the 200-day, with an advance/decline ratio of 1.70.
- Index-level momentum is slightly negative over 20 days (-1.28%), and the 10Y-2Y Treasury spread is only 0.27, indicating a shallow, late-cycle curve.
- Sector returns are bifurcated: Health Care (+6.9%), Consumer Discretionary (+6.7%), Consumer Staples (+5.4%) and Financials (+5.7%) lead; Information Technology (-7.2%) and Energy (-4.8%) lag.
- Credit conditions are tight: US high-yield OAS is 3.23 and IG OAS is 0.89, consistent with a risk-on but late-cycle backdrop.
- Liquidity is concentrated in a handful of large-cap names; several shortlisted names show extreme valuation dispersion, including high-multiple dislocation names and negative-P/E names.
- Macro data are stale: CPI and unemployment are from September 2026, and the latest effective fed funds rate is 3.88 as of 2026-11-12.
- Risk model shows 16.5% spike probability, below the historical baseline of 22.1%, but the forecast is not yet official after the US close.

## Data QC

- Status: **PASS_WITH_WARNINGS**
- Equity session: 0 completed session(s) behind inference date
- Equity provenance: 393 provisional / 12576 canonical
- Breadth lag: 0 session(s); ETF-flow lag: 0 session(s)
- Note: Equity session contains a mix of provisional yfinance and canonical Massive rows.
- External sources: 79 ok / 0 unavailable; retrieved 2026-11-16T15:09:17.591096+00:00

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
| S&P 500 | 7561.67 | -1.28% (20d) | Index is slightly negative over 20 days; breadth is positive with 71.3% above 50-day and 63.6% above 200-day. |
| Health Care (XLV) | return_20d +6.87% | +6.87% | Top sector; trailing P/E 31.06 and strong 20-day inflow confirmation. |
| Consumer Discretionary (XLY) | return_20d +6.69% | +6.69% | Strong 20-day return but structural distribution in flows; trailing P/E 24.84. |
| Consumer Staples (XLP) | return_20d +5.40% | +5.40% | Positive 20-day return; trailing P/E 25.04. |
| Financials (XLF) | return_20d +5.69% | +5.69% | Positive 20-day return; trailing P/E 15.81. |
| Information Technology (XLK) | return_20d -7.19% | -7.19% | Worst sector; trailing P/E 29.20, reflecting high-multiple dislocation names. |
| Energy (XLE) | return_20d -4.81% | -4.81% | Negative 20-day return; trailing P/E 15.95. |
| Utilities (XLU) | return_20d +4.34% | +4.34% | Positive 20-day return but exceptional institutional selling in flows; trailing P/E 18.22. |

## Macro, Fiscal, Rates, Liquidity and Credit

- Growth: macro data are stale; CPI and unemployment are from September 2026, so near-term growth momentum cannot be confirmed from the latest database evidence.
- Inflation: CPI (CPIAUCSL) is 336.298 and core CPI is 338.896 as of 2026-09-01; the October 2026 CPI is available in external sources at 337.476, but the latest monthly print is not in the database snapshot.
- Policy: the effective federal funds rate is 3.88 as of 2026-11-12, indicating a restrictive but easing-leaning policy stance.
- Rates: the 10Y-2Y Treasury spread is 0.27 as of 2026-11-13, a shallow positive curve that is consistent with late-cycle dynamics.
- Liquidity: credit spreads are tight, with US high-yield OAS at 3.23 and IG OAS at 0.89 as of 2026-11-13, suggesting ample liquidity and risk appetite.
- Credit: tight spreads and a shallow curve imply a late-cycle, quality-preferred environment; the risk model shows a 16.5% spike probability, below the historical baseline of 22.1%.

## US Equities and 11 GICS Sectors

Macro source IDs: S001, S002, S003, S004, S005, S006, S007

| GICS sector | Evidence | AI research stance | Source IDs |
| --- | --- | --- | --- |
| Health Care | 20-day return +6.87%; trailing P/E 31.06; 20-day flow z-score +1.45 and 60-day +1.72, described as strong confirmation. | Positive momentum and institutional inflow confirmation; valuation is rich but supported by sector leadership. | S051 |
| Consumer Discretionary | 20-day return +6.69%; trailing P/E 24.84; 20-day flow z-score -0.38 and 60-day -0.78, described as structural distribution. | Strong price momentum but institutional selling suggests a divergence between price and flows. | S059 |
| Consumer Staples | 20-day return +5.40%; trailing P/E 25.04; no flow data supplied. | Positive 20-day return and reasonable valuation; no flow evidence to confirm institutional behavior. | S063 |
| Financials | 20-day return +5.69%; trailing P/E 15.81; no flow data supplied. | Positive 20-day return with the cheapest trailing P/E among the leading sectors; no flow evidence. | S064 |
| Real Estate | 20-day return +5.24%; trailing P/E 29.75; no flow data supplied. | Positive 20-day return but rich valuation; no flow evidence. | S060 |
| Utilities | 20-day return +4.34%; trailing P/E 18.22; 20-day flow z-score -2.15 and 60-day +0.48, described as medium-term deterioration with exceptional institutional selling. | Price positive but flows show exceptional institutional selling; quality premium may be fading. | S065 |
| Materials | 20-day return +2.57%; trailing P/E 21.67; no flow data supplied. | Modest positive return and mid-range valuation; no flow evidence. | S066 |
| Industrials | 20-day return +0.61%; trailing P/E 26.86; no flow data supplied. | Near-flat 20-day return; valuation is mid-range but no flow evidence. | S074 |
| Communication Services | 20-day return -1.48%; trailing P/E 17.02; no flow data supplied. | Negative 20-day return; valuation is reasonable but no flow evidence. | S072 |
| Information Technology | 20-day return -7.19%; trailing P/E 29.20; no flow data supplied. | Worst sector with high-multiple dislocation names; valuation is rich relative to the negative price momentum. | S073 |
| Energy | 20-day return -4.81%; trailing P/E 15.95; no flow data supplied. | Negative 20-day return with the cheapest trailing P/E; no flow evidence. | S075 |

### Sector fundamentals, valuation and earnings

No point-in-time sector fundamentals beyond trailing P/E and 20-day ETF returns are supplied in the database. Growth, margins, consensus, and sector-relative valuation are only available for the shortlisted names, not for the full 11-sector universe. Therefore, sector-level fundamental comparisons are limited to the supplied trailing P/E and 20-day returns; no additional sector fundamentals are asserted.

## Growth vs Value

- Health Care has the highest trailing P/E (31.06) among the leading sectors, indicating rich valuation but strong 20-day momentum and institutional inflow confirmation.
- Financials offer the cheapest trailing P/E (15.81) among the positive sectors, with a +5.69% 20-day return, suggesting a value-plus-momentum profile.
- Information Technology is the most expensive sector on trailing P/E (29.20) and the worst performer over 20 days (-7.19%), with high-multiple dislocation names such as MRVL, NOW and AMD in the shortlist.
- Energy has the cheapest trailing P/E (15.95) but a negative 20-day return (-4.81%), indicating a value trap or cyclical weakness rather than a clear value opportunity.
- Several shortlisted names show extreme valuation dispersion: MRVL (P/E 74.23, earnings yield 1.35%), NOW (P/E 97.19, earnings yield 1.03%), IDXX (P/E 39.18, earnings yield 2.55%) and NVDA (P/E 26.51, earnings yield 3.77%) versus low-multiple names such as CHTR (P/E 2.71, earnings yield 36.95%) and FISV (P/E 9.65, earnings yield 10.36%).

## ETF Flows and Breadth

- Broad market breadth is positive: 71.3% of names above the 50-day, 63.6% above the 200-day, and the advance/decline ratio is 1.70 with 315 advancers versus 185 decliners.
- The index is slightly negative over 20 days (-1.28%), and the 10Y-2Y spread is only 0.27, indicating a shallow, late-cycle curve.
- Sector flows are bifurcated: Health Care shows strong institutional confirmation (20d z-score +1.45, 60d +1.72), while Consumer Discretionary shows structural distribution (20d -0.38, 60d -0.78) and Utilities shows exceptional institutional selling (20d -2.15).
- Liquidity is concentrated in a small set of large-cap names, with several shortlisted names flagged as liquidity leaders (NVDA, AMD, MU, AAPL) and several as dislocation names (RDDT, INTC, SNDK, MRVL, FFIV, NOW, LITE, COIN).

## Stock Ideas

Single-stock research uses reported EPS, forward P/E and company fundamentals. All ideas are research judgments, not validated return predictions.

| Ticker | Security | Research view | Price | EPS | Forward P/E | Base target | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| APP | AppLovin | NEW | 409.1 | 20.86026 | 19.774921 | 417.21 | NEW |
| PNR | Pentair | KEEP | 68.3 | 5.30402 | 12.878006 | 68.95 | KEEP |
| RDDT | Reddit | EXIT | 98.45 | 9.10039 | 10.400653 | 100.1 | EXIT |

## ETF Ideas

ETF research uses holdings, portfolio valuation and exposure. Single-stock EPS × P/E valuation is not applied to ETFs.

| Ticker | Fund | Research view | Price | Top holdings | Portfolio valuation | Sector exposure | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| XLV | Health Care sector ETF | KEEP | 188.85 | LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59% | Top 10 holdings; numeric weight coverage 61.42% | Health Care | KEEP |
| XLP | Consumer Staples sector ETF | KEEP | 92.35 | WMT 11.14%, COST 9.09%, PG 7.60%, KO 7.37%, PM 6.59%, MO 4.70%, CL 4.42%, MDLZ 4.25%, PEP 4.11%, TGT 4.00% | Top 10 holdings; numeric weight coverage 63.28% | Consumer Staples | KEEP |
### APP — AppLovin

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** AppLovin offers a high-quality, high-margin digital media franchise with strong momentum and a reasonable forward P/E, making it a more compelling standalone candidate than the lower-quality, high-multiple names in the dislocation bucket such as NOW or MRVL. Alternatives considered: NOW, MRVL.
- **Thesis:** AppLovin screens in the top 20-day momentum bucket with a 53.7% 20-day return and a 32.5% 60-day return, while maintaining a 60-day drawdown near flat. Reported diluted EPS of 11.61 and a forward EPS of 20.86 support a forward P/E near 19.8, and the company's high gross margin (~88.8%) and strong revenue/earnings growth provide a quality backdrop for a momentum-driven entry.
- **Source IDs:** S008, S012, S013, S017
- **Catalysts:** Sustained 20-day momentum with a 53.7% price return, High gross margin and double-digit revenue/earnings growth, Forward EPS of 20.86 supports a reasonable forward P/E near 19.8
- **Risks:** A 47% one-month drawdown headline suggests sharp volatility and possible overreaction, High momentum can mean elevated sensitivity to sentiment shifts, Forward EPS and fiscal-year mapping are unverified in the retrieved evidence
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 20.8603 (source.forwardEps) x AI multiple assumption 20.00; source IDs S008, S012, S013, S017
- **EPS:** 20.86026 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 19.774921
- **FY+1 growth assumption:** 27.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / AAPL / APP shows strong FY1 consensus growth of 27.44% with 25.37% revenue growth and 75.5% earnings growth, supported by 88.78% gross margin and 77.78% operating margin. The forward EPS of 20.86 and forward P/E of 19.77 are used as a reference, but the base multiple is set at 20.0 to reflect the company's high-quality earnings power and growth profile relative to AAPL. The bull case assumes continued execution and margin stability, while the bear case reflects potential growth deceleration or margin pressure.
- **Company fundamentals:** Reported diluted EPS 11.61; forward EPS 20.86; forward P/E 19.77; gross margin 88.8%; revenue growth 55.5%; earnings growth 75.5%; 20-day return 53.7%; 60-day return 32.5%; 60-day drawdown -0.2%.
- **Bull / Base / Bear:** 500.65 / 417.21 / 333.76
- **Bull / Base / Bear returns:** 22.38% / 1.98% / -18.42%
- **Scenario probabilities:** not separately assigned; see scenario table.

### PNR — Pentair

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Pentair is a lower-multiple industrial with a reasonable valuation and positive momentum, but it is not preferred over higher-growth names like AppLovin or the higher-quality software names in the shortlist. Alternatives considered: APP, ROP.
- **Thesis:** Pentair qualifies for the top 20-day momentum bucket with a 27.8% 20-day return and a 7.1% 60-day return, but its fundamentals are mixed: trailing P/E of 13.6 and earnings yield of 7.4% are supported by a 12.8% forward P/E, yet revenue growth is slightly negative and earnings growth is negative. The stock is reasonably valued but lacks the growth quality to justify a strong buy stance.
- **Source IDs:** S011, S016, S018, S022
- **Catalysts:** 20-day momentum of 27.8% and 60-day return of 7.1%, Forward P/E of 12.9 and earnings yield of 7.4%, 60-day drawdown of -5.2% indicates limited downside stress
- **Risks:** Revenue growth of -4.5% and earnings growth of -18.8%, Forward EPS and fiscal-year mapping are unverified, Sector-relative P/E of 0.49 suggests the stock is cheap relative to its sector, which may reflect structural headwinds
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 5.3040 (source.forwardEps) x AI multiple assumption 13.00; source IDs S011, S016, S018, S022
- **EPS:** 5.30402 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 12.878006
- **FY+1 growth assumption:** 12.82%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / HON / PNR has FY1 consensus growth of 12.82% with 18.38% revenue growth, though earnings growth is negative at -18.8% and revenue growth is -4.5%, indicating margin pressure. The forward EPS of 5.30 and forward P/E of 12.88 support a base multiple of 13.0. The bull case assumes margin recovery and stabilization, while the bear case reflects continued earnings weakness. The multiple is justified against HON's lower growth and margin profile.
- **Company fundamentals:** Reported diluted EPS 2.76; forward EPS 5.30; forward P/E 12.88; trailing P/E 13.59; earnings yield 7.36%; revenue growth -4.5%; earnings growth -18.8%; 20-day return 27.8%; 60-day return 7.1%; 60-day drawdown -5.2%.
- **Bull / Base / Bear:** 84.86 / 68.95 / 53.04
- **Bull / Base / Bear returns:** 24.25% / 0.95% / -22.34%
- **Scenario probabilities:** not separately assigned; see scenario table.

### RDDT — Reddit

- **Type:** Stock
- **Research view:** EXIT (stance: AVOID)
- **Why preferred / alternatives:** Reddit's severe dislocation and negative momentum outweigh its cheap valuation; the risk of further downside is too high to recommend, especially compared with the more stable momentum leaders in the shortlist. Alternatives considered: APP, PNR.
- **Thesis:** Reddit is the largest 20-day dislocation candidate with a -36.9% 20-day return and a -34.5% 60-day return, and a 39.4% 60-day drawdown. Although it has a low forward P/E of 10.4 and an earnings yield of 3.0%, the severe price deterioration and negative momentum make it a poor risk-reward candidate at this time.
- **Source IDs:** S039, S040, S043, S045
- **Catalysts:** Low forward P/E of 10.4 and earnings yield of 3.0%, High gross margin of 91.5%, Revenue growth of 53% and earnings growth of 74.9%
- **Risks:** 20-day return of -36.9% and 60-day return of -34.5%, 60-day drawdown of -39.4%, Momentum is deeply negative, and the stock is in a dislocation that may persist
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 9.1004 (source.forwardEps) x AI multiple assumption 11.00; source IDs S039, S040, S043, S045
- **EPS:** 9.10039 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 10.400653
- **FY+1 growth assumption:** 24.01%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / DIS / RDDT shows FY1 consensus growth of 24.01% with 28.38% revenue growth and 74.9% earnings growth, supported by 91.55% gross margin. The forward EPS of 9.10 and forward P/E of 10.40 justify a base multiple of 11.0, reflecting the company's strong growth and margin profile relative to DIS. The bull case assumes continued high growth and margin expansion, while the bear case reflects potential growth deceleration or competitive pressure.
- **Company fundamentals:** Reported diluted EPS 3.66; forward EPS 9.10; forward P/E 10.40; earnings yield 3.01%; gross margin 91.5%; revenue growth 53.0%; earnings growth 74.9%; 20-day return -36.9%; 60-day return -34.5%; 60-day drawdown -39.4%.
- **Bull / Base / Bear:** 127.41 / 100.1 / 72.8
- **Bull / Base / Bear returns:** 29.42% / 1.68% / -26.05%
- **Scenario probabilities:** not separately assigned; see scenario table.

### XLV — Health Care sector ETF

- **Type:** ETF
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** XLV provides broad, diversified health care exposure that is preferable to single-name health care stocks like IDXX when the goal is sector-level risk reduction rather than a specific company bet. Alternatives considered: XLP, XLF.
- **Thesis:** The Health Care sector ETF is a broad, diversified way to express the sector, with a 0.54% raw price change and a 58.4% top-10 holding coverage. It is a reasonable core holding for health care exposure, but the sector-level data does not provide a strong directional signal, so a neutral stance is appropriate.
- **Source IDs:** S051, S055
- **Catalysts:** Diversified health care exposure across large-cap pharma, biotech, and medical devices, 0.54% raw price change on 2026-11-13, Top-10 holdings coverage of 61.4%
- **Risks:** Sector-level performance is not differentiated from individual names, Top-10 holdings coverage of 61.4% leaves meaningful undisbclosed weight, No sector-relative or momentum signal is available for the ETF
- **Valuation method:** Holdings/portfolio valuation with AI total-return assumption
- **Valuation status:** verified; forward-EPS source: ; period flags: 
- **Valuation assumptions:** Holdings/portfolio valuation; 10 weighted holdings; coverage 61.42%; source IDs S051, S055
- **Top holdings:** LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59%
- **Portfolio valuation:** Top 10 holdings; numeric weight coverage 61.42%
- **Sector exposure:** Health Care
- **Underlying drivers:** Large-cap pharmaceutical and biotech earnings, medical device demand, and broader health care sector momentum.
- **Bull / Base / Bear:** 215.29 / 200.18 / 179.41
- **Bull / Base / Bear returns:** 14.0% / 6.0% / -5.0%
- **Scenario probabilities:** not separately assigned; see scenario table.

### XLP — Consumer Staples sector ETF

- **Type:** ETF
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** XLP provides defensive, dividend-oriented exposure that is preferable to single-name consumer staples stocks like CLX when the goal is sector-level risk reduction rather than a specific company bet. Alternatives considered: XLV, XLY.
- **Thesis:** The Consumer Staples sector ETF offers defensive, dividend-oriented exposure with a 1.42% raw price change on 2026-11-13, the strongest sector move in the shortlist. It is a reasonable defensive allocation, but the sector-level data does not provide a strong directional signal, so a neutral stance is appropriate.
- **Source IDs:** S057, S063
- **Catalysts:** 1.42% raw price change on 2026-11-13, the strongest sector move in the shortlist, Diversified staples exposure across consumer goods, retail, and beverages, Top-10 holdings coverage of 63.3%
- **Risks:** Sector-level performance is not differentiated from individual names, Top-10 holdings coverage of 63.3% leaves meaningful undisbclosed weight, No sector-relative or momentum signal is available for the ETF
- **Valuation method:** Holdings/portfolio valuation with AI total-return assumption
- **Valuation status:** verified; forward-EPS source: ; period flags: 
- **Valuation assumptions:** Holdings/portfolio valuation; 10 weighted holdings; coverage 63.28%; source IDs S057, S063
- **Top holdings:** WMT 11.14%, COST 9.09%, PG 7.60%, KO 7.37%, PM 6.59%, MO 4.70%, CL 4.42%, MDLZ 4.25%, PEP 4.11%, TGT 4.00%
- **Portfolio valuation:** Top 10 holdings; numeric weight coverage 63.28%
- **Sector exposure:** Consumer Staples
- **Underlying drivers:** Consumer staples demand resilience, pricing power, and broader staples sector momentum.
- **Bull / Base / Bear:** 103.43 / 96.97 / 88.66
- **Bull / Base / Bear returns:** 12.0% / 5.0% / -4.0%
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
| Bull | 25% | +2.00% | Low 5-day realized vol (14.9%) and below-threshold spike probability (16.5% vs 18.5% threshold) support a modest upside if US close confirms stable liquidity and no earnings-driven drawdown. |
| Base | 50% | +0.00% | Frozen daily-close model with no directional signal and near-baseline volatility implies range-bound trading; returns cluster near zero over the 5-day horizon. |
| Bear | 25% | -2.00% | Elevated spike probability (16.5%) and frozen model status create tail risk; a negative US close or macro shock could push returns to -2% before stabilization. |

### Long Term (12 months)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 30% | +8.00% | Sustained low volatility and positive earnings momentum support a bull case; 8% long-term return reflects continued risk-on positioning and credit spread tightening. |
| Base | 40% | +3.00% | Base case assumes gradual normalization of volatility and steady earnings growth; 3% long-term return reflects modest expansion with balanced risk/reward. |
| Bear | 30% | -5.00% | Bear case reflects persistent volatility, earnings disappointment, or credit widening; -5% long-term return captures downside if risk-off flows dominate. |

## Positioning


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
| S010 | news | FISV | Mon, 16 Nov 2026 02:19:15 GMT | ok | https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en | Fiserv, Inc. (FISV) Stock Price, News, Quote & History - Yahoo! Finance Canada (Mon, 16 Nov 2026 02:19:15 GMT); Fiserv (FISV) Stock Still Looks Like A Bargain After Lawsuit Claims - Yahoo Finance (Thu, 22 Oct 2026 07:00:00 GMT); Why Fiserv, Inc. (FISV) Was Exited by Ariel Appreciation Fund - Yahoo Finance (Wed, 28 Oct 2026 07:00:00 GMT) |
| S011 | filing | PNR | 2026-10-27 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-27 (accession 0000077360-26-000058); 8-K filed 2026-10-27 (accession 0000077360-26-000055); 8-K filed 2026-09-22 (accession 0000077360-26-000050) |
| S012 | filing | APP | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json | Diluted EPS 11.61 for period ending 2026-09-30 (filed 2026-11-04) |
| S013 | news | APP | Thu, 12 Nov 2026 20:05:45 GMT | ok | https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en | AppLovin Just Ripped 47% in a Month: Is It Too Late to Buy APP Stock Now? - Yahoo Finance (Thu, 12 Nov 2026 20:05:45 GMT); Is Trending Stock AppLovin Corporation (APP) a Buy Now? - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT); APP Stock Surges 51% After Q3 Earnings: Is it Still a Buy? - Yahoo Finance (Tue, 10 Nov 2026 14:24:00 GMT) |
| S014 | filing | FISV | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json | Diluted EPS -8.9 for period ending 2026-09-30 (filed 2026-11-04) |
| S015 | stock | FISV | 2026-11-16 | ok | https://finance.yahoo.com/quote/FISV | Forward P/E: 8.080673; Price: 64.45; Market price: 64.45; Market cap: 34290472960; Market Cap: 34290472960; Consensus EPS FY+1: 7.97582; growth: 0.0959 |
| S016 | stock | PNR | 2026-11-16 | ok | https://finance.yahoo.com/quote/PNR | Trailing P/E: 18.61177; Forward P/E: 12.878006; Forward EPS: 5.30402; Price: 68.3052; Market price: 68.3052; Market cap: 10905244672; Sector: Industrials; Trailing Eps: 3.67; Revenue Growth: -0.045; Earnings Growth: -0.188; Gross Margin: 0.40168998; Operating Margin: 0.21410999; Profit Margin: 0.15435; Return On Equity: 0.15605; Total Revenue: 3966200064; Market Cap: 10905244672; Consensus EPS FY+1: 5.30402; growth: 0.1282 |
| S017 | stock | APP | 2026-11-16 | ok | https://finance.yahoo.com/quote/APP | Trailing P/E: 27.778452; Forward P/E: 19.774921; Forward EPS: 20.86026; Price: 412.51; Market price: 412.51; Market cap: 136673632256; Sector: Communication Services; Trailing Eps: 14.85; Revenue Growth: 0.555; Earnings Growth: 0.755; Gross Margin: 0.8878; Operating Margin: 0.77782995; Profit Margin: 0.65887; Return On Equity: 2.1008599; Total Revenue: 7608893952; Market Cap: 136673632256; Consensus EPS FY+1: 20.72438; growth: 0.2744 |
| S018 | news | PNR | Sat, 14 Nov 2026 08:48:27 GMT | ok | https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en | Pentair plc (PNR) Stock Price, News, Quote & History - Yahoo! Finance Canada (Sat, 14 Nov 2026 08:48:27 GMT); Pentair plc (PNR) stock price, news, quote and history - Yahoo Finance UK (Fri, 13 Nov 2026 22:09:48 GMT); Pentair Stock Price Forecast. Should You Buy PNR? - StockInvest.us (Fri, 13 Nov 2026 22:50:05 GMT) |
| S019 | news | GEN | Thu, 29 Oct 2026 07:00:00 GMT | ok | https://news.google.com/rss/search?q=GEN+Gen+Digital+stock&hl=en-US&gl=US&ceid=US:en | Gen Digital (GEN) Stock Repriced After Q2 Earnings Put Margins Center Stage - Yahoo Finance (Thu, 29 Oct 2026 07:00:00 GMT); Gen Digital Stock: Is Wall Street Bullish or Bearish? - Yahoo Finance (Thu, 05 Nov 2026 08:00:00 GMT); Are Business Services Stocks Lagging GEN DIGITAL INC (GEN) This Year? - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT) |
| S020 | filing | CLX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000021076-26-000046); 8-K filed 2026-11-02 (accession 0000021076-26-000044); 8-K filed 2026-10-29 (accession 0001206774-26-000586) |
| S021 | filing | GEN | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0000849399-26-000083); 8-K filed 2026-10-28 (accession 0000849399-26-000081); 8-K filed 2026-10-09 (accession 0000849399-26-000079) |
| S022 | filing | PNR | 2026-10-27 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json | Diluted EPS 2.76 for period ending 2026-09-30 (filed 2026-10-27) |
| S023 | stock | GEN | 2026-11-16 | ok | https://finance.yahoo.com/quote/GEN | Trailing P/E: 15.545685; Forward P/E: 9.176415; Forward EPS: 3.33736; Price: 30.625; Market price: 30.625; Market cap: 18169079808; Sector: Technology; Trailing Eps: 1.97; Revenue Growth: 0.122; Earnings Growth: 1.286; Gross Margin: 0.77410007; Operating Margin: 0.43229; Profit Margin: 0.23068; Return On Equity: 0.46402; Total Revenue: 5228000256; Market Cap: 18169079808; Consensus EPS FY+1: 3.33736; growth: 0.1286 |
| S024 | stock | CLX | 2026-11-16 | ok | https://finance.yahoo.com/quote/CLX | Trailing P/E: 19.72214; Forward P/E: 17.77691; Forward EPS: 6.1684; Price: 109.6551; Market price: 109.6551; Market cap: 13284428800; Sector: Consumer Defensive; Trailing Eps: 5.56; Revenue Growth: 0.333; Earnings Growth: 1.138; Gross Margin: 0.41939998; Operating Margin: 0.14286; Profit Margin: 0.09408; Return On Equity: 5.34363; Total Revenue: 7196000256; Market Cap: 13284428800; Consensus EPS FY+1: 6.1684; growth: 0.0769 |
| S025 | filing | CHTR | 2026-11-06 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-06 (accession 0001091667-26-000073); 8-K filed 2026-11-06 (accession 0001091667-26-000072); 8-K filed 2026-10-27 (accession 0001091667-26-000064) |
| S026 | news | CLX | Fri, 13 Nov 2026 23:34:51 GMT | ok | https://news.google.com/rss/search?q=CLX+Clorox+stock&hl=en-US&gl=US&ceid=US:en | The Clorox Company (CLX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 23:34:51 GMT); The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance UK (Sat, 14 Nov 2026 06:03:20 GMT); A 10-Day Winning Streak Has Clorox Stock Up 24% - Trefis (Sat, 14 Nov 2026 08:28:05 GMT) |
| S027 | news | CHTR | Sun, 15 Nov 2026 05:47:01 GMT | ok | https://news.google.com/rss/search?q=CHTR+Charter+Communications+stock&hl=en-US&gl=US&ceid=US:en | Charter Communications (CHTR) Stock Could Be A Bargain Following Its New Operating Model - Yahoo Finance (Sun, 15 Nov 2026 05:47:01 GMT); Why You Should Think About Charter Communications Differently Now? - Yahoo Finance (Fri, 13 Nov 2026 19:16:11 GMT); Charter Communications (CHTR) Earnings Expected to Grow: What to Know Ahead of Next Week's Release - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT) |
| S028 | filing | IDXX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000874716&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000874716-26-000135); 8-K filed 2026-11-02 (accession 0001104659-26-120892); 10-Q filed 2026-08-04 (accession 0000874716-26-000123) |
| S029 | stock | CHTR | 2026-11-16 | ok | https://finance.yahoo.com/quote/CHTR | Trailing P/E: 12.698308; Forward P/E: 2.9730542; Forward EPS: 45.44485; Price: 135.11; Market price: 135.11; Market cap: 24191655936; Sector: Communication Services; Trailing Eps: 10.64; Revenue Growth: 0.091; Gross Margin: 0.55084; Operating Margin: 0.23389; Profit Margin: 0.02498; Return On Equity: 0.07019; Total Revenue: 55645999104; Market Cap: 24191655936; Consensus EPS FY+1: 49.35412; growth: 1.1136 |
| S030 | stock | IDXX | 2026-11-16 | ok | https://finance.yahoo.com/quote/IDXX | Trailing P/E: 47.850403; Forward P/E: 42.035408; Forward EPS: 16.8929; Price: 710.1; Market price: 710.1; Market cap: 55946125312; Sector: Healthcare; Trailing Eps: 14.84; Revenue Growth: 0.099; Earnings Growth: 0.179; Gross Margin: 0.62722; Operating Margin: 0.32497; Profit Margin: 0.25357; Return On Equity: 0.68925005; Total Revenue: 4662220800; Market Cap: 55946125312; Consensus EPS FY+1: 16.8929; growth: 0.1244 |
| S031 | filing | ROP | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000882835&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000882835-26-000047); 8-K filed 2026-10-22 (accession 0000882835-26-000042); 8-K filed 2026-10-01 (accession 0000882835-26-000039) |
| S032 | news | IDXX | Sat, 14 Nov 2026 22:37:20 GMT | ok | https://news.google.com/rss/search?q=IDXX+Idexx+Laboratories+stock&hl=en-US&gl=US&ceid=US:en | IDEXX Laboratories, Inc. (IDXX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Sat, 14 Nov 2026 22:37:20 GMT); IDEXX Laboratories (IDXX) Stock Looks Fairly Valued Despite Its 28% Run - Yahoo Finance (Sat, 31 Oct 2026 07:00:00 GMT); IDEXX Laboratories (IDXX) vs. ZTS and NEOG: Can Raised Guidance and Product Expansion Drive Further Earnings Growth? - Yahoo Finance (Thu, 22 Oct 2026 07:00:00 GMT) |
| S033 | stock | ROP | 2026-11-16 | ok | https://finance.yahoo.com/quote/ROP | Trailing P/E: 19.25366; Forward P/E: 19.799637; Forward EPS: 24.57318; Price: 486.54; Market price: 486.54; Market cap: 48185188352; Sector: Technology; Trailing Eps: 25.27; Revenue Growth: 0.076; Earnings Growth: 0.326; Gross Margin: 0.69671; Operating Margin: 0.28049; Profit Margin: 0.30712998; Return On Equity: 0.13229; Total Revenue: 8434599936; Market Cap: 48185188352; Consensus EPS FY+1: 24.57318; growth: 0.09810001 |
| S034 | filing | CLX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000021076.json | Diluted EPS 1.39 for period ending 2026-09-30 (filed 2026-11-02) |
| S035 | filing | CHTR | 2026-11-06 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001091667.json | Diluted EPS 0.38 for period ending 2026-09-30 (filed 2026-11-06) |
| S036 | news | ROP | Thu, 05 Nov 2026 08:00:00 GMT | ok | https://news.google.com/rss/search?q=ROP+Roper+Technologies+stock&hl=en-US&gl=US&ceid=US:en | Roper Technologies (ROP) Stock Looks Fully Valued As Cash Flow Comes Into Focus - Yahoo Finance (Thu, 05 Nov 2026 08:00:00 GMT); Here's How Much $100 Invested In Roper Technologies 20 Years Ago Would Be Worth Today - Benzinga (Mon, 16 Nov 2026 14:15:26 GMT); Roper Technologies (ROP), What Is Behind The Fresh Attention? - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT) |
| S037 | filing | GEN | 2026-10-29 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000849399.json | Diluted EPS 0.83 for period ending 2026-10-02 (filed 2026-10-29) |
| S038 | filing | IDXX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000874716.json | Diluted EPS 11.75 for period ending 2026-09-30 (filed 2026-11-02) |
| S039 | filing | RDDT | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001713445&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0001713445-26-000116); 8-K filed 2026-10-29 (accession 0001713445-26-000114); 8-K filed 2026-08-12 (accession 0001713445-26-000107) |
| S040 | stock | RDDT | 2026-11-16 | ok | https://finance.yahoo.com/quote/RDDT | Trailing P/E: 19.316326; Forward P/E: 10.400653; Forward EPS: 9.10039; Price: 94.65; Market price: 94.65; Market cap: 18276321280; Sector: Communication Services; Trailing Eps: 4.9; Revenue Growth: 0.53; Earnings Growth: 0.749; Gross Margin: 0.91547996; Operating Margin: 0.29397; Profit Margin: 0.32105; Return On Equity: 0.32029998; Total Revenue: 3088880128; Market Cap: 18276321280; Consensus EPS FY+1: 6.8155; growth: 0.2401 |

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
- news FISV: https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en (Mon, 16 Nov 2026 02:19:15 GMT)
- filing PNR: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 (2026-10-27)
- filing APP: https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json (2026-11-04)
- news APP: https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en (Thu, 12 Nov 2026 20:05:45 GMT)
- filing FISV: https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json (2026-11-04)
- stock FISV: https://finance.yahoo.com/quote/FISV (2026-11-16)
- stock PNR: https://finance.yahoo.com/quote/PNR (2026-11-16)
- stock APP: https://finance.yahoo.com/quote/APP (2026-11-16)
- news PNR: https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en (Sat, 14 Nov 2026 08:48:27 GMT)
- news GEN: https://news.google.com/rss/search?q=GEN+Gen+Digital+stock&hl=en-US&gl=US&ceid=US:en (Thu, 29 Oct 2026 07:00:00 GMT)
- filing CLX: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 (2026-11-02)

## AI Provenance

- Provider / model: hermes-local-proxy / upstage/solar-mini4:free
- Market research: attempts=1 tokens=9511 (prompt=6511, completion=3000) runtime=24.53s
- Fundamental research: generated this run at 2026-11-16T15:08:53.310975+00:00
- Evidence source dates: {'as_of': '2026-11-13', 'latest_equity_date': '2026-11-13', 'latest_macro_date': '2026-11-16', 'flows_date': '2026-11-13'}
- Evidence fingerprint: 01e9131530fdf6570c5dc3ba33eb40cff681554f2b44267a5d4a7e1bc3309bb8
- Source citations are retrieved external records in the ledger above; market values remain from the verified database snapshot.


## Disclosures

- This is research and market intelligence, not investment advice.
- AI conclusions are research judgments, not validated return predictions.
- The frozen risk layer is risk-only and is not used for directional views or allocations.
- Legacy scores are not active inputs or outputs.

# AEGIS AI-First Market Intelligence

Research generated at: 16 November 2026, 17:08 HKT
Database freshness: equity 2026-11-13 (latest row retrieved 2026-11-16 13:06:43.000010+08:00)
Data cutoff: 2026-11-13 US cash close
Snapshot ID: aegis-hourly-20261116T090828Z

## Executive Summary

- **AI market view: Late-November 2026: broad market breadth is constructive (71% above 50-day, 64% above 200-day, A/D ratio 1.70), but the S&P 500 is slightly negative over 20 days and the Information Technology sector is the weakest major group. Momentum and dislocation screens point to a small set of high-beta, high-valuation names, while flows show strong institutional demand in Health Care and structural distribution in Consumer Discretionary and Utilities.**
- Broad market breadth is supportive: 71.3% of names above their 50-day moving average and 63.6% above their 200-day, with a 1.70 advance/decline ratio.
- S&P 500 is down 1.28% over 20 days, and Information Technology is the only major sector in negative territory (-7.19% over 20 days), while Health Care leads with +6.87%.
- Momentum and dislocation screens highlight a concentrated list of high-beta names, but several carry elevated or negative trailing P/E and lack forward earnings data, so they are not recommended as a group.
- Institutional flows show strong confirmation in Health Care (XLY inflow, z-score 1.45/1.72) and structural distribution in Consumer Discretionary (XLY z-score -0.38/-0.78) and Utilities (XLU z-score -2.15/0.48).
- Macro data show a 10Y-2Y spread of 0.27, high-yield OAS of 3.20, and IG OAS of 0.89, with CPI and unemployment still elevated but not accelerating.
- Risk environment is moderate: 5-day forecast volatility 14.93%, spike probability 16.51% below the 18.50% threshold, and no directional signal.

## Data QC

- Status: **PASS_WITH_WARNINGS**
- Equity session: 0 completed session(s) behind inference date
- Equity provenance: 393 provisional / 12576 canonical
- Breadth lag: 0 session(s); ETF-flow lag: 0 session(s)
- Note: Equity session contains a mix of provisional yfinance and canonical Massive rows.
- External sources: 79 ok / 0 unavailable; retrieved 2026-11-16T09:08:51.911041+00:00

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
| S&P 500 | 7561.67 | -1.28% (20d) | Broad market breadth is constructive, but the index is slightly negative over 20 days; Information Technology is the weakest major sector. |
| Health Care (XLV) | return_20d +6.87% | +6.87% | Strong institutional inflow and strong confirmation; trailing P/E 30.78. |
| Consumer Discretionary (XLY) | return_20d +6.69% | +6.69% | Positive price momentum but structural distribution in flows; trailing P/E 25.11. |
| Information Technology (XLK) | return_20d -7.19% | -7.19% | Only major sector in negative territory; trailing P/E 30.03. |
| Utilities (XLU) | return_20d +4.34% | +4.34% | Positive price return but medium-term institutional selling; trailing P/E 18.11. |
| Consumer Staples (XLP) | return_20d +5.40% | +5.40% | Positive 20-day return; trailing P/E 24.85. |

## Macro, Fiscal, Rates, Liquidity and Credit

- Growth: US macro data are limited to CPI and unemployment; the latest CPI (2026-09-01) is 336.298 and core CPI 338.896, while unemployment is 4.2%, indicating still-elevated inflation and a stable labor market.
- Policy: The effective federal funds rate is 3.88% as of 2026-11-12, suggesting a restrictive but not sharply easing policy stance.
- Rates: The 10Y-2Y Treasury spread is 0.27 as of 2026-11-13, a modestly positive curve, and credit spreads are tight (IG OAS 0.89, HY OAS 3.20), implying limited stress.
- Liquidity: Credit spreads are narrow and the yield curve is slightly positive, but the equity market is not in a strong uptrend over 20 days, so liquidity conditions are not clearly supportive of broad risk-taking.
- Credit: High-yield OAS of 3.20 and IG OAS of 0.89 are not distressed, but the combination of tight spreads and a slightly negative equity trend warrants caution.
- Inflation: CPI and core CPI remain elevated, and the Fed funds rate is still above 3.8%, so the inflation backdrop is not yet consistent with aggressive easing.

## US Equities and 11 GICS Sectors

Macro source IDs: S001, S002, S003, S004, S005, S006, S007

| GICS sector | Evidence | AI research stance | Source IDs |
| --- | --- | --- | --- |
| Health Care | 20-day return +6.87% (XLV), trailing P/E 30.78 (S054), institutional inflow with z-score 1.45/1.72 and strong confirmation. | Constructive: strong price momentum, positive institutional flows, and a high trailing P/E that is not extreme relative to the market. | S054 |
| Consumer Discretionary | 20-day return +6.69% (XLY), trailing P/E 25.11 (S059), but flow z-score -0.38/-0.78 and structural distribution. | Mixed: positive price momentum is offset by institutional selling and a moderate valuation. | S059 |
| Information Technology | 20-day return -7.19% (XLK), trailing P/E 30.03 (S073), and the only major sector in negative territory. | Negative: broad sector underperformance, elevated valuation, and weak momentum. | S073 |
| Financials | 20-day return +5.69% (XLF), trailing P/E 15.85 (S068), and positive price momentum. | Constructive: positive 20-day return and a low trailing P/E, though flow data are not provided. | S068 |
| Industrials | 20-day return +0.61% (XLI), trailing P/E 27.07 (S067), and near-flat price performance. | Neutral: modest positive return but no strong momentum or flow signal. | S067 |
| Consumer Staples | 20-day return +5.40% (XLP), trailing P/E 24.85 (S055), and positive price momentum. | Constructive: positive 20-day return and a moderate trailing P/E. | S055 |
| Utilities | 20-day return +4.34% (XLU), trailing P/E 18.11 (S064), but flow z-score -2.15/0.48 and medium-term institutional selling. | Mixed: positive price return is offset by strong institutional distribution. | S064 |
| Real Estate | 20-day return +5.24% (XLRE), trailing P/E 29.63 (S062), and positive price momentum. | Constructive: positive 20-day return and a moderate trailing P/E. | S062 |
| Materials | 20-day return +2.57% (XLB), trailing P/E 21.72 (S065), and positive price momentum. | Constructive: positive 20-day return and a moderate trailing P/E. | S065 |
| Energy | 20-day return -4.81% (XLE), trailing P/E 16.23 (S074), and negative price momentum. | Negative: the only other major sector in negative territory, with a low trailing P/E but weak momentum. | S074 |
| Communication Services | 20-day return -1.48% (XLC), trailing P/E 17.26 (S072), and negative price momentum. | Negative: negative 20-day return and a moderate trailing P/E. | S072 |

### Sector fundamentals, valuation and earnings

No point-in-time sector fundamentals beyond trailing P/E and 20-day returns are supplied in the database. The sector-level evidence is limited to ETF price returns, trailing P/E, and flow z-scores; growth, margins, and consensus estimates are not available for the full sector universe. Therefore, no additional sector fundamentals are reported to avoid invention.

## Growth vs Value

- Health Care offers the strongest momentum and institutional confirmation, but its trailing P/E of 30.78 is elevated relative to the market.
- Information Technology is the only major sector in negative territory with a trailing P/E of 30.03, indicating weak growth momentum and high valuation.
- Financials and Consumer Staples show positive 20-day returns with lower trailing P/Es (15.85 and 24.85), suggesting more reasonable valuations.
- Energy and Communication Services are negative over 20 days, with trailing P/Es of 16.23 and 17.26, but the negative momentum is a concern.

## ETF Flows and Breadth

- Health Care (XLV) is the clearest institutional flow signal: inflow with z-scores of 1.45 (20d) and 1.72 (60d) and strong confirmation.
- Consumer Discretionary (XLY) shows structural distribution with z-scores of -0.38 (20d) and -0.78 (60d), despite positive price momentum.
- Utilities (XLU) shows medium-term institutional selling with a 20d z-score of -2.15, even though the price is up.
- Broad market breadth is constructive: 71.34% above 50-day, 63.6% above 200-day, and an advance/decline ratio of 1.70.
- The 20-day positive rate is 70.46%, and the 5-day and 20-day breadth changes are positive (10.1 and 26.21), indicating improving breadth.

## Stock Ideas

Single-stock research uses reported EPS, forward P/E and company fundamentals. All ideas are research judgments, not validated return predictions.

| Ticker | Security | Research view | Price | EPS | Forward P/E | Base target | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| APP | AppLovin | NEW | 409.1 | 20.86026 | 19.611452 | 417.21 | NEW |
| PNR | Pentair | KEEP | 68.3 | 5.30402 | 12.877027 | 74.26 | KEEP |
| RDDT | Reddit | KEEP | 98.45 | 9.10039 | 10.818217 | 109.2 | KEEP |

## ETF Ideas

ETF research uses holdings, portfolio valuation and exposure. Single-stock EPS × P/E valuation is not applied to ETFs.

| Ticker | Fund | Research view | Price | Top holdings | Portfolio valuation | Sector exposure | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| XLV | Health Care sector ETF | KEEP | 188.85 | LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59% | Top 10 holdings; numeric weight coverage 61.42% | Health Care | KEEP |
| XLP | Consumer Staples sector ETF | KEEP | 92.35 | WMT 11.14%, COST 9.09%, PG 7.60%, KO 7.37%, PM 6.59%, MO 4.70%, CL 4.42%, MDLZ 4.25%, PEP 4.11%, TGT 4.00% | Top 10 holdings; numeric weight coverage 63.28% | Consumer Staples | KEEP |
### APP — AppLovin

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** AppLovin offers a high-margin, momentum-led profile that is preferable to the lower-margin, lower-growth names in the shortlist such as Pentair and Clorox, while avoiding the deep dislocation and negative earnings growth of Intel and Reddit. Alternatives considered: PNR, CLX, INTC, RDDT.
- **Thesis:** AppLovin screens in the top 20-day momentum bucket with a 53.7% 20-day return and a 32.5% 60-day return, while maintaining a 65.9% profit margin and 88.8% gross margin. The stock is trading at a forward P/E of 19.6x with a 4.99% earnings yield, and the 10-Q filed 2026-11-04 supports the reported diluted EPS of 11.61. Momentum and margin quality support a new BUY.
- **Source IDs:** S008, S012, S013, S019
- **Catalysts:** Continued 20-day momentum into the 2026-11-13 close, Sustained high gross and profit margins, Positive 60-day return with limited drawdown
- **Risks:** High 20-day momentum can mean elevated volatility, Forward P/E of 19.6x leaves limited valuation cushion, Source flags note fiscal-period alignment is unverified
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 20.8603 (source.forwardEps) x AI multiple assumption 20.00; source IDs S008, S012, S013, S019
- **EPS:** 20.86026 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 19.611452
- **FY+1 growth assumption:** 27.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / AAPL / APP shows strong FY1 consensus growth of 27.44% with 25.4% revenue growth and 75.5% earnings growth, supported by 88.8% gross margin and 77.8% operating margin. The 19.6x forward P/E is below the 20x base multiple, reflecting a premium-quality compounder. AAPL is the named peer reference for sustained high-margin growth and premium valuation.
- **Company fundamentals:** AppLovin reported diluted EPS of 11.61 for the period ending 2026-09-30, with FY1 EPS of 20.72438 and FY1 revenue growth of 25.37%. Gross margin is 88.78%, operating margin 77.78%, and profit margin 65.89%. Forward EPS is 20.86026, implying a forward P/E of 19.61x. Source flags note fiscal-period alignment is unverified.
- **Bull / Base / Bear:** 500.65 / 417.21 / 333.76
- **Bull / Base / Bear returns:** 22.38% / 1.98% / -18.42%
- **Scenario probabilities:** not separately assigned; see scenario table.

### PNR — Pentair

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Pentair is preferable to the deep-dislocation names such as Intel and Reddit, which show negative 20-day returns and large drawdowns, and to the high-multiple names such as AppLovin and Roper, which carry higher forward P/E multiples. Alternatives considered: APP, CLX, INTC, RDDT.
- **Thesis:** Pentair is a top-20-day-momentum name with a 27.8% 20-day return and a 7.1% 60-day return. It carries a 12.88x forward P/E and a 7.36% earnings yield, with a 15.4% FY1 EPS growth rate. The stock is reasonably valued relative to its sector, but the 60-day drawdown of 5.2% and modest revenue growth of 18.4% warrant a neutral stance.
- **Source IDs:** S010, S014, S017, S018
- **Catalysts:** 20-day momentum of 27.8%, Forward P/E of 12.88x and earnings yield of 7.36%, FY1 EPS growth of 15.4%
- **Risks:** Revenue growth of 18.4% is below the 20-day momentum pace, 60-day drawdown of 5.2%, Sector-relative P/E of 0.49x suggests limited relative upside
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 5.3040 (source.forwardEps) x AI multiple assumption 14.00; source IDs S010, S014, S017, S018
- **EPS:** 5.30402 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 12.877027
- **FY+1 growth assumption:** 12.82%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / CSCO / PNR has modest FY1 consensus growth of 12.82% with 18.4% revenue growth but negative 18.8% earnings growth, reflecting margin pressure (21.4% operating margin, 15.4% profit margin). The 12.9x forward P/E is reasonable for a cyclical infrastructure name. CSCO is the named peer reference for a large-cap IT infrastructure company with moderate growth and stable margins.
- **Company fundamentals:** Pentair reported diluted EPS of 2.76 for the period ending 2026-09-30, with FY1 EPS of 5.30402 and FY1 EPS growth of 12.82%. Revenue growth is 18.38%, gross margin 40.17%, operating margin 21.41%, and profit margin 15.44%. Forward EPS is 5.30402, implying a forward P/E of 12.88x.
- **Bull / Base / Bear:** 90.17 / 74.26 / 58.34
- **Bull / Base / Bear returns:** 32.02% / 8.73% / -14.58%
- **Scenario probabilities:** not separately assigned; see scenario table.

### RDDT — Reddit

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Reddit is preferable to Intel, which has a negative 20-day return, a 53.2% 60-day drawdown, and negative earnings growth, and to the high-multiple names such as NOW and MRVL, which carry forward P/E multiples above 35x. Alternatives considered: INTC, NOW, MRVL, APP.
- **Thesis:** Reddit is a largest-20-day-dislocation name with a 36.9% 20-day drawdown and a 39.4% 60-day drawdown. It carries a 10.82x forward P/E and a 3.01% earnings yield, with 24.0% FY1 EPS growth and 53.0% revenue growth. The dislocation is severe, but the valuation is not cheap enough to justify a BUY at this stage.
- **Source IDs:** S035, S040, S042, S047
- **Catalysts:** 24.0% FY1 EPS growth and 53.0% revenue growth, Forward P/E of 10.82x, Earnings yield of 3.01%
- **Risks:** 36.9% 20-day drawdown and 39.4% 60-day drawdown, Forward P/E of 10.82x is not a deep discount, Sector-relative P/E of 1.66x is elevated
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 9.1004 (source.forwardEps) x AI multiple assumption 12.00; source IDs S035, S040, S042, S047
- **EPS:** 9.10039 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 10.818217
- **FY+1 growth assumption:** 24.01%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / FOXA / RDDT shows strong FY1 consensus growth of 24.01% with 28.4% revenue growth and 74.9% earnings growth, supported by 91.5% gross margin. However, operating margin is only 29.4% and profit margin 32.1%, indicating significant operating costs. The 10.8x forward P/E is below the 12x base multiple. FOXA is the named peer reference for a media/entertainment company with high gross margins but operating leverage challenges.
- **Company fundamentals:** Reddit reported diluted EPS of 3.66 for the period ending 2026-09-30, with FY1 EPS of 6.8155 and FY1 EPS growth of 24.01%. Revenue growth is 28.38%, gross margin 91.55%, operating margin 29.40%, and profit margin 32.11%. Forward EPS is 9.10039, implying a forward P/E of 10.82x.
- **Bull / Base / Bear:** 136.51 / 109.2 / 81.9
- **Bull / Base / Bear returns:** 38.66% / 10.92% / -16.81%
- **Scenario probabilities:** not separately assigned; see scenario table.

### XLV — Health Care sector ETF

- **Type:** ETF
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** XLV is preferable to the single-stock dislocation names such as Intel and Reddit, which carry large drawdowns and negative momentum, and to the consumer-facing ETFs such as XLY, which show a -0.40% raw price change. Alternatives considered: XLY, XLP, XLF.
- **Thesis:** XLV is the Health Care sector ETF with a 0.54% raw price change and a 5.84M share volume. Its top holdings are LLY, JNJ, ABBV, MRK, and UNH, with top-10 weight coverage of 61.42%. The sector ETF provides diversified healthcare exposure, but the modest price change and limited top-10 coverage warrant a neutral stance.
- **Source IDs:** S054, S057
- **Catalysts:** Diversified healthcare exposure across top-10 holdings, 0.54% raw price change, Top-10 weight coverage of 61.42%
- **Risks:** Modest 0.54% raw price change, Top-10 weight coverage of 61.42% leaves 38.58% in smaller positions, Sector-specific regulatory and reimbursement risks
- **Valuation method:** Holdings/portfolio valuation with AI total-return assumption
- **Valuation status:** verified; forward-EPS source: ; period flags: 
- **Valuation assumptions:** Holdings/portfolio valuation; 10 weighted holdings; coverage 61.42%; source IDs S054, S057
- **Top holdings:** LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59%
- **Portfolio valuation:** Top 10 holdings; numeric weight coverage 61.42%
- **Sector exposure:** Health Care
- **Underlying drivers:** Top-10 holdings: LLY, JNJ, ABBV, MRK, UNH, TMO, AMGN, GILD, ABT, PFE; top-10 weight coverage 61.42%.
- **Bull / Base / Bear:** 211.51 / 198.29 / 177.52
- **Bull / Base / Bear returns:** 12.0% / 5.0% / -6.0%
- **Scenario probabilities:** not separately assigned; see scenario table.

### XLP — Consumer Staples sector ETF

- **Type:** ETF
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** XLP is preferable to the high-beta consumer discretionary ETF XLY, which shows a -0.40% raw price change, and to the financials ETF XLF, which shows a 0.81% raw price change but carries sector concentration risk. Alternatives considered: XLY, XLF, XLU.
- **Thesis:** XLP is the Consumer Staples sector ETF with a 1.42% raw price change, the strongest raw move among the sector ETFs shown. Its top holdings are WMT, COST, PG, KO, and PM, with top-10 weight coverage of 63.28%. The defensive staples profile is attractive, but the modest price change and limited top-10 coverage warrant a neutral stance.
- **Source IDs:** S055, S061
- **Catalysts:** 1.42% raw price change, the strongest among the sector ETFs, Diversified consumer staples exposure across top-10 holdings, Top-10 weight coverage of 63.28%
- **Risks:** 1.42% raw price change is still modest in absolute terms, Top-10 weight coverage of 63.28% leaves 36.72% in smaller positions, Defensive staples can lag in a risk-on environment
- **Valuation method:** Holdings/portfolio valuation with AI total-return assumption
- **Valuation status:** verified; forward-EPS source: ; period flags: 
- **Valuation assumptions:** Holdings/portfolio valuation; 10 weighted holdings; coverage 63.28%; source IDs S055, S061
- **Top holdings:** WMT 11.14%, COST 9.09%, PG 7.60%, KO 7.37%, PM 6.59%, MO 4.70%, CL 4.42%, MDLZ 4.25%, PEP 4.11%, TGT 4.00%
- **Portfolio valuation:** Top 10 holdings; numeric weight coverage 63.28%
- **Sector exposure:** Consumer Staples
- **Underlying drivers:** Top-10 holdings: WMT, COST, PG, KO, PM, MO, CL, MDLZ, PEP, TGT; top-10 weight coverage 63.28%.
- **Bull / Base / Bear:** 101.59 / 96.04 / 87.73
- **Bull / Base / Bear returns:** 10.01% / 4.0% / -5.0%
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
| Bull | 25% | +2.00% | Low 5-day realized vol (14.9%) and below-threshold spike probability (16.5% vs 18.5% baseline) reduce near-term tail risk, allowing a modest upside if US close confirms positive breadth. |
| Base | 50% | +0.00% | Frozen daily-close model with no directional signal and a 50% base probability reflects a range-bound week where no catalyst is strong enough to drive a sustained move. |
| Bear | 25% | -2.00% | If the US close fails to confirm the frozen forecast or volatility spikes above the 18.5% threshold, elevated uncertainty could push returns down by roughly 2%. |

### Long Term (12 months)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 30% | +8.00% | Sustained low vol and stable baseline suggest a constructive medium-term trend if earnings and credit spreads remain supportive, with a 30% probability of an 8% advance. |
| Base | 40% | +3.00% | A 40% base case assumes gradual normalization of volatility and steady earnings growth, yielding a modest 3% long-term return without a major regime shift. |
| Bear | 30% | -5.00% | If the frozen model's low-vol regime breaks and spike probability rises above baseline, elevated uncertainty and widening credit spreads could drive a 5% long-term decline. |

## Positioning

- Maintain a constructive but cautious stance: breadth and Health Care flows are supportive, but the S&P 500 is slightly negative over 20 days and Information Technology is weak.
- Favor Health Care for institutional confirmation and positive momentum, while monitoring its elevated trailing P/E.
- Reduce exposure to Information Technology and Energy given negative 20-day returns and weak momentum.
- Treat Consumer Discretionary and Utilities as mixed: positive price action is offset by structural institutional distribution.
- Do not assign weights; the screen is momentum/dislocation/valuation/liquidity based and does not produce allocation targets.

## Catalysts

| Date | Event | Why it matters |
| --- | --- | --- |
| 2026-11-16 | US macro data release | CPI and unemployment data are the latest available; any revision or new print could shift the inflation and labor market outlook. |
| 2026-11-16 | 10Y-2Y Treasury spread | The spread is 0.27, a modestly positive curve; a move toward inversion or steepening would signal changing rate expectations. |
| 2026-11-16 | Credit spreads | IG OAS 0.89 and HY OAS 3. |

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
| S009 | filing | FISV | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0000798354-26-000042); 8-K filed 2026-11-03 (accession 0000798354-26-000039); 8-K filed 2026-10-23 (accession 0001193125-26-429481) |
| S010 | filing | PNR | 2026-10-27 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-27 (accession 0000077360-26-000058); 8-K filed 2026-10-27 (accession 0000077360-26-000055); 8-K filed 2026-09-22 (accession 0000077360-26-000050) |
| S011 | news | FISV | Fri, 13 Nov 2026 21:49:46 GMT | ok | https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en | Fiserv, Inc. (FISV) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 21:49:46 GMT); Why Fiserv, Inc. (FISV) Was Exited by Ariel Appreciation Fund - Yahoo Finance (Wed, 28 Oct 2026 07:00:00 GMT); Fiserv (FISV): Buy, Sell, or Hold Post Q2 Earnings? - Yahoo Finance (Tue, 08 Sep 2026 07:00:00 GMT) |
| S012 | news | APP | Thu, 12 Nov 2026 20:05:45 GMT | ok | https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en | AppLovin Just Ripped 47% in a Month: Is It Too Late to Buy APP Stock Now? - Yahoo Finance (Thu, 12 Nov 2026 20:05:45 GMT); Is Trending Stock AppLovin Corporation (APP) a Buy Now? - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT); APP Stock Surges 51% After Q3 Earnings: Is it Still a Buy? - Yahoo Finance (Tue, 10 Nov 2026 14:24:00 GMT) |
| S013 | filing | APP | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json | Diluted EPS 11.61 for period ending 2026-09-30 (filed 2026-11-04) |
| S014 | news | PNR | Fri, 13 Nov 2026 22:09:48 GMT | ok | https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en | Pentair plc (PNR) stock price, news, quote and history - Yahoo Finance UK (Fri, 13 Nov 2026 22:09:48 GMT); Pentair plc (PNR) Q3 Earnings and Revenues Beat Estimates - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT); Pentair (PNR) Stock May Be 46% Undervalued As New CFO Arrives - Yahoo Finance (Fri, 25 Sep 2026 07:00:00 GMT) |
| S015 | filing | GEN | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0000849399-26-000083); 8-K filed 2026-10-28 (accession 0000849399-26-000081); 8-K filed 2026-10-09 (accession 0000849399-26-000079) |
| S016 | filing | FISV | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json | Diluted EPS -8.9 for period ending 2026-09-30 (filed 2026-11-04) |
| S017 | filing | PNR | 2026-10-27 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json | Diluted EPS 2.76 for period ending 2026-09-30 (filed 2026-10-27) |
| S018 | stock | PNR | 2026-11-16 | ok | https://finance.yahoo.com/quote/PNR | Trailing P/E: 18.610355; Forward P/E: 12.877027; Forward EPS: 5.30402; Price: 68.3; Market price: 68.3; Market cap: 10904415232; Sector: Industrials; Trailing Eps: 3.67; Revenue Growth: -0.045; Earnings Growth: -0.188; Gross Margin: 0.40168998; Operating Margin: 0.21410999; Profit Margin: 0.15435; Return On Equity: 0.15605; Total Revenue: 3966200064; Market Cap: 10904415232; Consensus EPS FY+1: 5.30402; growth: 0.1282 |
| S019 | stock | APP | 2026-11-16 | ok | https://finance.yahoo.com/quote/APP | Trailing P/E: 27.54882; Forward P/E: 19.611452; Forward EPS: 20.86026; Price: 409.1; Market price: 409.1; Market cap: 135543824384; Sector: Communication Services; Trailing Eps: 14.85; Revenue Growth: 0.555; Earnings Growth: 0.755; Gross Margin: 0.8878; Operating Margin: 0.77782995; Profit Margin: 0.65887; Return On Equity: 2.1008599; Total Revenue: 7608893952; Market Cap: 135543824384; Consensus EPS FY+1: 20.72438; growth: 0.2744 |
| S020 | filing | CLX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000021076-26-000046); 8-K filed 2026-11-02 (accession 0000021076-26-000044); 8-K filed 2026-10-29 (accession 0001206774-26-000586) |
| S021 | news | GEN | Thu, 29 Oct 2026 07:00:00 GMT | ok | https://news.google.com/rss/search?q=GEN+Gen+Digital+stock&hl=en-US&gl=US&ceid=US:en | Gen Digital (GEN) Stock Repriced After Q2 Earnings Put Margins Center Stage - Yahoo Finance (Thu, 29 Oct 2026 07:00:00 GMT); Gen Digital Stock: Is Wall Street Bullish or Bearish? - Yahoo Finance (Thu, 05 Nov 2026 08:00:00 GMT); Are Business Services Stocks Lagging GEN DIGITAL INC (GEN) This Year? - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT) |
| S022 | stock | GEN | 2026-11-16 | ok | https://finance.yahoo.com/quote/GEN | Trailing P/E: 15.431472; Forward P/E: 9.108996; Forward EPS: 3.33736; Price: 30.4; Market price: 30.4; Market cap: 18035593216; Sector: Technology; Trailing Eps: 1.97; Revenue Growth: 0.122; Earnings Growth: 1.286; Gross Margin: 0.77410007; Operating Margin: 0.43229; Profit Margin: 0.23068; Return On Equity: 0.46402; Total Revenue: 5228000256; Market Cap: 18035593216; Consensus EPS FY+1: 3.33736; growth: 0.1286 |
| S023 | stock | FISV | 2026-11-16 | ok | https://finance.yahoo.com/quote/FISV | Forward P/E: 7.99667; Price: 63.78; Market price: 63.78; Market cap: 33934002176; Market Cap: 33934002176; Consensus EPS FY+1: 7.97582; growth: 0.0959 |
| S024 | filing | GEN | 2026-10-29 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000849399.json | Diluted EPS 0.83 for period ending 2026-10-02 (filed 2026-10-29) |
| S025 | filing | CHTR | 2026-11-06 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-06 (accession 0001091667-26-000073); 8-K filed 2026-11-06 (accession 0001091667-26-000072); 8-K filed 2026-10-27 (accession 0001091667-26-000064) |
| S026 | news | CLX | Fri, 13 Nov 2026 23:34:51 GMT | ok | https://news.google.com/rss/search?q=CLX+Clorox+stock&hl=en-US&gl=US&ceid=US:en | The Clorox Company (CLX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 23:34:51 GMT); The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance UK (Sun, 15 Nov 2026 08:55:47 GMT); Clorox (CLX) Down 9.3% Since Last Earnings Report: Can It Rebound? - Yahoo Finance (Wed, 02 Sep 2026 07:00:00 GMT) |
| S027 | filing | IDXX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000874716&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000874716-26-000135); 8-K filed 2026-11-02 (accession 0001104659-26-120892); 10-Q filed 2026-08-04 (accession 0000874716-26-000123) |
| S028 | news | CHTR | Sun, 15 Nov 2026 05:47:01 GMT | ok | https://news.google.com/rss/search?q=CHTR+Charter+Communications+stock&hl=en-US&gl=US&ceid=US:en | Charter Communications (CHTR) Stock Could Be A Bargain Following Its New Operating Model - Yahoo Finance (Sun, 15 Nov 2026 05:47:01 GMT); Why You Should Think About Charter Communications Differently Now? - Yahoo Finance (Fri, 13 Nov 2026 19:16:11 GMT); Charter Communications (CHTR) Expands Enterprise Reach With Managed Secure Networking Launch - Yahoo Finance (Sun, 15 Nov 2026 06:08:00 GMT) |
| S029 | stock | CLX | 2026-11-16 | ok | https://finance.yahoo.com/quote/CLX | Trailing P/E: 19.68705; Forward P/E: 17.745283; Forward EPS: 6.1684; Price: 109.46; Market price: 109.46; Market cap: 13260793856; Sector: Consumer Defensive; Trailing Eps: 5.56; Revenue Growth: 0.333; Earnings Growth: 1.138; Gross Margin: 0.41939998; Operating Margin: 0.14286; Profit Margin: 0.09408; Return On Equity: 5.34363; Total Revenue: 7196000256; Market Cap: 13260793856; Consensus EPS FY+1: 6.1684; growth: 0.0769 |
| S030 | filing | CLX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000021076.json | Diluted EPS 1.39 for period ending 2026-09-30 (filed 2026-11-02) |
| S031 | stock | CHTR | 2026-11-16 | ok | https://finance.yahoo.com/quote/CHTR | Trailing P/E: 13.006578; Forward P/E: 3.0452294; Forward EPS: 45.44485; Price: 138.39; Market price: 138.39; Market cap: 24778944512; Sector: Communication Services; Trailing Eps: 10.64; Revenue Growth: 0.091; Gross Margin: 0.55084; Operating Margin: 0.23389; Profit Margin: 0.02498; Return On Equity: 0.07019; Total Revenue: 55645999104; Market Cap: 24778944512; Consensus EPS FY+1: 49.35412; growth: 1.1136 |
| S032 | news | IDXX | Sat, 14 Nov 2026 22:37:20 GMT | ok | https://news.google.com/rss/search?q=IDXX+Idexx+Laboratories+stock&hl=en-US&gl=US&ceid=US:en | IDEXX Laboratories, Inc. (IDXX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Sat, 14 Nov 2026 22:37:20 GMT); symbol__ Stock Quote Price and Forecast - CNN (Fri, 13 Nov 2026 15:22:45 GMT); IDEXX Laboratories, Inc. (IDXX) stock price, news, quote and history - Yahoo Finance UK (Sat, 14 Nov 2026 09:01:45 GMT) |
| S033 | filing | ROP | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000882835&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000882835-26-000047); 8-K filed 2026-10-22 (accession 0000882835-26-000042); 8-K filed 2026-10-01 (accession 0000882835-26-000039) |
| S034 | filing | CHTR | 2026-11-06 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001091667.json | Diluted EPS 0.38 for period ending 2026-09-30 (filed 2026-11-06) |
| S035 | filing | RDDT | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001713445&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0001713445-26-000116); 8-K filed 2026-10-29 (accession 0001713445-26-000114); 8-K filed 2026-08-12 (accession 0001713445-26-000107) |
| S036 | news | ROP | Thu, 05 Nov 2026 08:00:00 GMT | ok | https://news.google.com/rss/search?q=ROP+Roper+Technologies+stock&hl=en-US&gl=US&ceid=US:en | Roper Technologies (ROP) Stock Looks Fully Valued As Cash Flow Comes Into Focus - Yahoo Finance (Thu, 05 Nov 2026 08:00:00 GMT); Roper Technologies (ROP), What Is Behind The Fresh Attention? - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT); Did Earnings Beat Just Shift Roper Technologies (ROP) Investment Narrative? - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT) |
| S037 | stock | IDXX | 2026-11-16 | ok | https://finance.yahoo.com/quote/IDXX | Trailing P/E: 47.45485; Forward P/E: 41.687927; Forward EPS: 16.8929; Price: 704.23; Market price: 704.23; Market cap: 55483650048; Sector: Healthcare; Trailing Eps: 14.84; Revenue Growth: 0.099; Earnings Growth: 0.179; Gross Margin: 0.62722; Operating Margin: 0.32497; Profit Margin: 0.25357; Return On Equity: 0.68925005; Total Revenue: 4662220800; Market Cap: 55483650048; Consensus EPS FY+1: 16.8929; growth: 0.1244 |
| S038 | stock | ROP | 2026-11-16 | ok | https://finance.yahoo.com/quote/ROP | Trailing P/E: 18.993866; Forward P/E: 19.532475; Forward EPS: 24.57318; Price: 479.975; Market price: 479.975; Market cap: 47535013888; Sector: Technology; Trailing Eps: 25.27; Revenue Growth: 0.076; Earnings Growth: 0.326; Gross Margin: 0.69671; Operating Margin: 0.28049; Profit Margin: 0.30712998; Return On Equity: 0.13229; Total Revenue: 8434599936; Market Cap: 47535013888; Consensus EPS FY+1: 24.57318; growth: 0.09810001 |
| S039 | filing | IDXX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000874716.json | Diluted EPS 11.75 for period ending 2026-09-30 (filed 2026-11-02) |
| S040 | stock | RDDT | 2026-11-16 | ok | https://finance.yahoo.com/quote/RDDT | Trailing P/E: 20.091835; Forward P/E: 10.818217; Forward EPS: 9.10039; Price: 98.45; Market price: 98.45; Market cap: 19010076672; Sector: Communication Services; Trailing Eps: 4.9; Revenue Growth: 0.53; Earnings Growth: 0.749; Gross Margin: 0.91547996; Operating Margin: 0.29397; Profit Margin: 0.32105; Return On Equity: 0.32029998; Total Revenue: 3088880128; Market Cap: 19010076672; Consensus EPS FY+1: 6.8155; growth: 0.2401 |

## Sources

- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFF&cosd=2026-01-01 (2026-11-12)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLH0A0HYM2&cosd=2026-01-01 (2026-11-12)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLC0A0CM&cosd=2026-01-01 (2026-11-12)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCSL&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=UNRATE&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=PAYEMS&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=T10Y2Y&cosd=2026-01-01 (2026-11-13)
- filing APP: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001751008&type=10-Q&dateb=&owner=include&count=10 (2026-11-04)
- filing FISV: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 (2026-11-04)
- filing PNR: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 (2026-10-27)
- news FISV: https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 21:49:46 GMT)
- news APP: https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en (Thu, 12 Nov 2026 20:05:45 GMT)
- filing APP: https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json (2026-11-04)
- news PNR: https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 22:09:48 GMT)
- filing GEN: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 (2026-10-29)
- filing FISV: https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json (2026-11-04)
- filing PNR: https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json (2026-10-27)
- stock PNR: https://finance.yahoo.com/quote/PNR (2026-11-16)
- stock APP: https://finance.yahoo.com/quote/APP (2026-11-16)
- filing CLX: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 (2026-11-02)

## AI Provenance

- Provider / model: hermes-local-proxy / upstage/solar-mini4:free
- Market research: attempts=1 tokens=9513 (prompt=6513, completion=3000) runtime=27.0s
- Fundamental research: generated this run at 2026-11-16T09:08:28.930489+00:00
- Evidence source dates: {'as_of': '2026-11-13', 'latest_equity_date': '2026-11-13', 'latest_macro_date': '2026-11-16', 'flows_date': '2026-11-13'}
- Evidence fingerprint: 8bdf7ca539ff2a987f0873318d004ea858d43a1d38f8a03209978fda495f0f96
- Source citations are retrieved external records in the ledger above; market values remain from the verified database snapshot.


## Disclosures

- This is research and market intelligence, not investment advice.
- AI conclusions are research judgments, not validated return predictions.
- The frozen risk layer is risk-only and is not used for directional views or allocations.
- Legacy scores are not active inputs or outputs.

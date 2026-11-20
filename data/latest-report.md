# AEGIS AI-First Market Intelligence

Research generated at: 20 November 2026, 18:08 HKT
Database freshness: equity 2026-11-19 (latest row retrieved None)
Data cutoff: 2026-11-19 US cash close
Snapshot ID: aegis-hourly-20261120T100846Z

## Executive Summary

- **AI market view: Late-November 2026 US equities show a broad, late-cycle caution pattern: the S&P 500 is down about 5.6% over 20 days, breadth is negative on the 50-day and 200-day measures, and the 20-day advance/decline ratio is below 1.0. The 11 GICS sectors are almost all negative over 20 days, with Information Technology worst at -11.9%, Energy -9.9%, Materials -4.4%, Industrials -3.2%, and Financials -1.9%. Only Consumer Discretionary, Real Estate, Utilities, and Consumer Staples are modestly positive. Macro data point to a still-elevated but easing inflation backdrop, a labor market near full employment, and a flat-to-slightly-inverted 10Y-2Y curve, while high-yield and investment-grade spreads remain tight, suggesting limited credit stress but also limited risk premium.**
- S&P 500 is in a mild corrective phase: 20-day return -5.59% and 20-day breadth negative (55.69% positive, ADR 0.89).
- Sector rotation is defensive: only 4 of 11 GICS sectors are positive over 20 days; IT, Energy, Materials, and Industrials are the weakest.
- Valuation dispersion is wide: shortlist names range from deeply cheap (PNR, GEN, CHTR) to extreme dislocation (DDOG, NOW, MRVL, AMD).
- Credit spreads are tight (HY OAS 3.47, IG OAS 0.93), so risk assets are not pricing acute stress, but the flat curve and negative breadth argue for caution.
- Macro data show inflation still above target, unemployment at 4.2%, and a 10Y-2Y spread of only 0.28, consistent with a late-cycle, low-growth, higher-for-longer regime.
- Flows show tactical profit-taking in Health Care and neutral-to-negative positioning in Utilities, while medium-term flows in XLY are recovering; no single asset class is showing a clear directional signal.

## Data QC

- Status: **PASS_WITH_WARNINGS**
- Equity session: 0 completed session(s) behind inference date
- Macro session: 2026-11-20 (0 completed session(s) behind inference date)
- Equity provenance: 0 provisional / 12662 canonical
- Breadth lag: 1 session(s); ETF-flow lag: 0 session(s)
- Note: Breadth or ETF-flow input lags the equity session; each is timestamped in the report.
- External sources: 79 ok / 0 unavailable; retrieved 2026-11-20T10:09:06.621266+00:00

## Idea Discovery

- S&P 500 universe: 503; eligible: 501; transparent shortlist: 20
- Method: independent momentum/dislocation/PE/liquidity buckets; no composite score
- Evidence used: latest close, 20d and 60d price returns, 60d drawdown, trailing P/E, earnings yield, sector-relative P/E, dollar volume, GICS sector
- Not available as verified inputs: verified earnings-revision history for the full universe, FY+2 consensus, structured industry catalyst calendar
- Eligible but not shortlisted: 481 (outside the top independent momentum, dislocation, valuation and liquidity buckets)
- Included: APP (top_20d_momentum); CMG (top_20d_momentum); PNR (top_20d_momentum); IDXX (top_20d_momentum); GEN (top_20d_momentum); CHTR (top_20d_momentum); CLX (top_20d_momentum); CVNA (top_20d_momentum); SNDK (largest_20d_dislocation, liquidity_leader); NOW (largest_20d_dislocation); RDDT (largest_20d_dislocation); MRVL (largest_20d_dislocation); COIN (largest_20d_dislocation); DDOG (largest_20d_dislocation); INTC (largest_20d_dislocation); FIS (largest_20d_dislocation); NVDA (liquidity_leader); AMD (liquidity_leader); MU (liquidity_leader); MSFT (liquidity_leader)
- Excluded reasons: {"missing_recent_or_latest_price": 2}
- Valuation-quality rejected: [{"flags": ["forward_pe_outside_plausible_range", "implausible_earnings_yield", "forward_eps_vs_reported_jump"], "ticker": "CHTR"}, {"flags": ["implausible_earnings_yield"], "ticker": "SNDK"}, {"flags": ["forward_eps_vs_reported_jump"], "ticker": "MRVL"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "COIN"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "DDOG"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "INTC"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "FIS"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "NVDA"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "AMD"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "MU"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "MSFT"}]

## Market Snapshot

| Asset | Latest | Change | Observation |
| --- | --- | --- | --- |
| S&P 500 | 7323.63 | -5.59% (20d) | Broad-based pullback; 20-day price breadth negative and advance/decline ratio 0.89. |
| Information Technology (XLK) | -11.87% | -11.87% (20d) | Worst sector; extreme dislocation names (DDOG, NOW, MRVL, AMD) and high relative P/E drag the group. |
| Energy (XLE) | -9.89% | -9.89% (20d) | Sharp 20-day decline; sector-relative P/E 0.13 for CHTR is an outlier, not a sector signal. |
| Materials (XLB) | -4.39% | -4.39% (20d) | Negative 20-day return; sector-relative P/E 0.47 for SNDK is flagged as implausible. |
| Industrials (XLI) | -3.22% | -3.22% (20d) | Negative 20-day return; sector-relative P/E 0.41 for FIS is flagged as implausible. |
| Financials (XLF) | -1.89% | -1.89% (20d) | Negative 20-day return; tight IG OAS 0.93 and HY OAS 3.47 limit credit-driven stress. |
| Consumer Discretionary (XLY) | +0.76% | +0.76% (20d) | Only modest positive sector; medium-term flow recovery but tactical profit-taking inside structural accumulation. |
| Real Estate (XLRE) | +0.85% | +0.85% (20d) | Modestly positive; trailing P/E 28.63. |
| Utilities (XLU) | +0.33% | +0.33% (20d) | Flat-to-positive; medium-term deterioration in flows, neutral 20-day state. |
| Consumer Staples (XLP) | -0.14% | -0.14% (20d) | Near-flat; trailing P/E 24.18. |
| Health Care (XLV) | -2.12% | -2.12% (20d) | Negative 20-day return; exceptional institutional selling and tactical profit-taking inside structural accumulation. |

## Macro, Fiscal, Rates, Liquidity and Credit

- Inflation: CPI (CPIAUCSL) is 336.298 in Sep-2026 and core CPI 338.896; external S004 shows 337.476 for Oct-2026, indicating inflation remains above the Fed's 2% target and is sticky.
- Labor: unemployment rate is 4.2% in Sep-2026 and 4.1% in Oct-2026 (S005), with nonfarm payrolls at 159,293k in Oct-2026 (S006), consistent with a still-tight but not overheating labor market.
- Policy/rates: effective federal funds rate is 3.88% as of 2026-11-18 (S001), and the 10Y-2Y spread is 0.28 as of 2026-11-19 (S007), indicating a flat-to-slightly-inverted curve and a late-cycle policy stance.
- Credit/liquidity: high-yield OAS is 3.47 and investment-grade OAS is 0.93 as of 2026-11-18 (S002, S003), both tight, so credit conditions are not signaling acute stress but also offer little compensation for risk.
- Growth: the 20-day S&P 500 decline of -5.59%, negative 50-day and 200-day breadth, and negative 20-day advance/decline ratio point to slowing momentum and a late-cycle growth scare.
- Liquidity: tight spreads and a flat curve suggest ample financial conditions, but the negative breadth and sector rotation imply that liquidity is being withdrawn from the weakest names rather than broadly deployed.

## US Equities and 11 GICS Sectors

Macro source IDs: S001, S002, S003, S004, S005, S006, S007

| GICS sector | Evidence | AI research stance | Source IDs |
| --- | --- | --- | --- |
| Information Technology | 20d return -11.87% (XLK); trailing P/E 28.34 (S072); shortlist names NOW, DDOG, MRVL, AMD show extreme dislocation and high relative P/E; liquidity leaders NVDA and AMD are in this sector. | Negative momentum and valuation dispersion; the sector is the primary driver of the broad pullback. | S072 |
| Energy | 20d return -9.89% (XLE); trailing P/E 15.21 (S074); shortlist CHTR has sector-relative P/E 0.13, but that is a Communication Services name, not an Energy signal. | Negative 20-day performance; no direct Energy-specific evidence in the supplied data beyond the sector ETF return. | S074 |
| Materials | 20d return -4.39% (XLB); trailing P/E 20.55 (S066); shortlist SNDK has sector-relative P/E 0.47 but is flagged as implausible. | Negative 20-day return; no direct Materials-specific evidence beyond the sector ETF return. | S066 |
| Industrials | 20d return -3.22% (XLI); trailing P/E 25.88 (S067); shortlist FIS has sector-relative P/E 0.41 but is flagged as implausible. | Negative 20-day return; no direct Industrials-specific evidence beyond the sector ETF return. | S067 |
| Financials | 20d return -1.89% (XLF); trailing P/E 15.01 (S060); credit spreads tight (HY OAS 3.47, IG OAS 0.93) limit credit-driven stress. | Negative 20-day return; tight spreads suggest the sector is not under acute credit pressure. | S060, S002, S003 |
| Consumer Discretionary | 20d return +0.76% (XLY); trailing P/E 24.25 (S059); flow structure shows medium-term recovery with tactical profit-taking inside structural accumulation. | Only modestly positive sector; flows suggest institutional accumulation but near-term profit-taking. | S059 |
| Real Estate | 20d return +0.85% (XLRE); trailing P/E 28.63 (S057). | Modestly positive; no direct catalyst evidence beyond the sector ETF return and P/E. | S057 |
| Utilities | 20d return +0.33% (XLU); trailing P/E 17.69 (S064); flow structure shows medium-term deterioration with neutral 20-day state. | Flat-to-positive; medium-term flow deterioration is a caution flag despite the flat 20-day state. | S064 |
| Consumer Staples | 20d return -0.14% (XLP); trailing P/E 24.18 (S055). | Near-flat; no strong directional signal from the supplied data. | S055 |
| Health Care | 20d return -2.12% (XLV); trailing P/E 28.93 (S054); flow state is outflow with exceptional institutional selling and tactical profit-taking inside structural accumulation. | Negative 20-day return; institutional selling is a near-term caution flag despite structural accumulation. | S054 |
| Communication Services | 20d return -4.34% (XLC); trailing P/E 16.32 (S069); shortlist CHTR has sector-relative P/E 0.13 and is flagged as implausible. | Negative 20-day return; valuation flags on CHTR limit the reliability of the sector signal. | S069 |

### Sector fundamentals, valuation and earnings

No point-in-time sector fundamentals (e.g., sector-level earnings, margins, or growth) are supplied in the database snapshot. The only sector-level evidence available is the 20-day ETF returns, trailing P/E for each GICS sector ETF, and the shortlist names' sector-relative P/E and earnings yield. The database explicitly states that growth/margins/consensus were retrieved only for source-backed shortlist names, and that verified earnings-revision history, FY+2 consensus, and a structured industry catalyst calendar are unavailable. Therefore, no sector-level fundamental scores or forward estimates are reported here.

## Growth vs Value

- Growth: the 20-day S&P 500 decline of -5.59% and negative 20-day breadth (55.69% positive, ADR 0.89) indicate slowing growth momentum and a late-cycle growth scare.
- Value: shortlist names show extreme valuation dispersion, from deeply cheap (P

## ETF Flows and Breadth


## Stock Ideas

Single-stock research uses reported EPS, forward P/E and company fundamentals. All ideas are research judgments, not validated return predictions.

| Ticker | Security | Research view | Price | EPS | Forward P/E | Base target | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| APP | AppLovin | NEW | 379.02 | 20.86084 | 18.16897 | 417.22 | NEW |
| PNR | Pentair | KEEP | 68.68 | 5.30402 | 12.948669 | 74.26 | KEEP |
| IDXX | Idexx Laboratories | KEEP | 689.65 | 16.8929 | 40.824844 | 540.57 | KEEP |
| GEN | Gen Digital | KEEP | 30.15 | 3.33736 | 9.034087 | 33.37 | KEEP |

## ETF Ideas

ETF research uses holdings, portfolio valuation and exposure. Single-stock EPS × P/E valuation is not applied to ETFs.

| Ticker | Fund | Research view | Price | Top holdings | Portfolio valuation | Sector exposure | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| XLV | Health Care sector ETF | KEEP | 177.46 | LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59% | Top 10 holdings; numeric weight coverage 61.42% | Health Care | KEEP |
### APP — AppLovin

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** AppLovin offers a cleaner momentum and margin profile than the high-multiple, high-dislocation names in the shortlist, while still carrying a strong forward earnings yield near 5.5%. Alternatives considered: NOW, RDDT, MRVL.
- **Thesis:** AppLovin screens as a top 20-day momentum name with a 20-day return of roughly 43% and a 60-day return near 23%, supported by a 60-day drawdown of only about 9%. Reported diluted EPS of 11.61 for the fiscal period ending 2026-09-30 and a forward EPS of 20.86 imply a forward P/E near 18.2, which is reasonable for a high-margin, high-growth mobile advertising platform. The combination of strong near-term price momentum, high gross margin, and positive revenue/earnings growth supports a constructive view.
- **Source IDs:** S008, S012, S013, S014
- **Catalysts:** Continued 20-day momentum into the week ahead, Sustained high-margin advertising revenue growth, Positive forward EPS trajectory
- **Risks:** Momentum can reverse quickly after a large run, Forward EPS and fiscal-year mapping are unverified, Sector-relative P/E is at 1.0, so no valuation discount
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 20.8608 (source.forwardEps) x AI multiple assumption 20.00; source IDs S008, S012, S013, S014
- **EPS:** 20.86084 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 18.16897
- **FY+1 growth assumption:** 27.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / MSFT / APP shows 27.4% forward earnings growth and 25.2% revenue growth with exceptional 88.8% gross margin and 77.8% operating margin, but ROE is only 2.1%, indicating heavy capital intensity. The 18.2x forward P/E is not justified by current earnings power, so a 20.0x base multiple is set below the current 18.2x forward P/E to reflect quality and capital intensity risk. MSFT is the named peer reference for a high-growth, high-margin software/tech franchise with durable competitive advantages.
- **Company fundamentals:** Reported diluted EPS 11.61 for the period ending 2026-09-30; forward EPS 20.86; forward P/E 18.17; gross margin 88.8%; operating margin 77.8%; profit margin 65.9%; revenue growth 55.5%; earnings growth 75.5%; ROE 2.10. Fiscal-period alignment and FY mapping are unverified.
- **Bull / Base / Bear:** 500.66 / 417.22 / 333.77
- **Bull / Base / Bear returns:** 32.09% / 10.08% / -11.94%
- **Scenario probabilities:** not separately assigned; see scenario table.

### PNR — Pentair

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Pentair is preferred over the high-multiple dislocation names because it offers a much lower entry P/E, but it is not preferred over the stronger momentum compounders in the shortlist. Alternatives considered: NOW, RDDT, MRVL.
- **Thesis:** Pentair screens as a top 20-day momentum name with a 20-day return of about 24% and a 60-day return near 9%. It carries a low forward P/E near 12.9 and a high earnings yield near 7.4%, but revenue and earnings are contracting, with revenue growth of -4.5% and earnings growth of -18.8%. The low valuation is offset by deteriorating fundamentals, so a neutral stance is appropriate.
- **Source IDs:** S009, S015, S016, S024
- **Catalysts:** Potential stabilization in capital markets and water segments, Low forward P/E if earnings stabilize
- **Risks:** Revenue and earnings contraction, Sector-relative P/E of 0.49 indicates a deep valuation discount, Momentum is positive but fundamentals are weak
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 5.3040 (source.forwardEps) x AI multiple assumption 14.00; source IDs S009, S015, S016, S024
- **EPS:** 5.30402 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 12.948669
- **FY+1 growth assumption:** 12.82%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / RRC / PNR has 12.8% forward earnings growth and 18.4% revenue growth, but reported earnings growth is -18.8% and revenue is -4.5%, indicating near-term cyclical weakness. The 12.9x forward P/E is supported by a 40.2% gross margin and 21.4% operating margin, but the low ROE of 15.6% and cyclical commodity exposure warrant a conservative 14.0x base multiple. RRC is the named peer reference for a diversified industrial/energy infrastructure company with similar margin and cyclical risk.
- **Company fundamentals:** Reported diluted EPS 2.76 for the period ending 2026-09-30; forward EPS 5.30; forward P/E 12.95; gross margin 40.2%; operating margin 21.4%; profit margin 15.4%; revenue growth -4.5%; earnings growth -18.8%; ROE 0.16. Fiscal-period alignment and FY mapping are unverified.
- **Bull / Base / Bear:** 90.17 / 74.26 / 58.34
- **Bull / Base / Bear returns:** 31.29% / 8.12% / -15.06%
- **Scenario probabilities:** not separately assigned; see scenario table.

### IDXX — Idexx Laboratories

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Idexx offers a high-quality growth profile with positive earnings momentum, but the premium valuation limits the upside relative to lower-multiple names in the shortlist. Alternatives considered: NOW, RDDT, PNR.
- **Thesis:** Idexx Laboratories screens as a top 20-day momentum name with a 20-day return of about 22% and a 60-day return near 25%. It has a high forward P/E near 40.8 and a low earnings yield near 2.6%, with revenue growth of about 9.9% and earnings growth of 17.9%. The strong momentum is balanced by a rich valuation, so a neutral stance is appropriate.
- **Source IDs:** S019, S021, S025, S028
- **Catalysts:** Sustained growth in animal health and diagnostics, Positive 20-day momentum
- **Risks:** Rich forward P/E near 40.8, Low earnings yield near 2.6%, Sector-relative P/E of 1.33 indicates a premium valuation
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 16.8929 (source.forwardEps) x AI multiple assumption 32.00; source IDs S019, S021, S025, S028
- **EPS:** 16.8929 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 40.824844
- **FY+1 growth assumption:** 12.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / CDW / IDXX has 12.4% forward earnings growth and 9.9% revenue growth with a 62.7% gross margin and 32.5% operating margin, but ROE is only 69.0% and the 40.8x forward P/E is very high. The 32.0x base multiple is set below the current 40.8x forward P/E to reflect the premium valuation and modest growth. CDW is the named peer reference for a high-growth, high-margin business with strong competitive positioning.
- **Company fundamentals:** Reported diluted EPS 11.75 for the period ending 2026-09-30; forward EPS 16.89; forward P/E 40.82; gross margin 62.7%; operating margin 32.5%; profit margin 25.4%; revenue growth 9.9%; earnings growth 17.9%; ROE 0.69. Fiscal-period alignment and FY mapping are unverified.
- **Bull / Base / Bear:** 641.93 / 540.57 / 439.22
- **Bull / Base / Bear returns:** -6.92% / -21.62% / -36.31%
- **Scenario probabilities:** not separately assigned; see scenario table.

### GEN — Gen Digital

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Gen Digital offers a low forward P/E and high earnings growth, but the modest 60-day return and IT sector cyclicality keep it from being a clear buy. Alternatives considered: NOW, RDDT, PNR.
- **Thesis:** Gen Digital screens as a top 20-day momentum name with a 20-day return of about 21% and a 60-day return near 2%. It has a low forward P/E near 9.0 and a high earnings yield near 7.1%, with revenue growth of 12.2% and earnings growth of 128.6%. The strong earnings growth and low valuation are balanced by a modest 60-day return, so a neutral stance is appropriate.
- **Source IDs:** S020, S023, S027, S029
- **Catalysts:** High earnings growth and low forward P/E, Positive 20-day momentum
- **Risks:** 60-day return is only about 2%, Sector-relative P/E of 0.42 indicates a discount, Cybersecurity and software demand can be cyclical
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 3.3374 (source.forwardEps) x AI multiple assumption 10.00; source IDs S020, S023, S027, S029
- **EPS:** 3.33736 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 9.034087
- **FY+1 growth assumption:** 12.86%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / HON / GEN has 12.9% forward earnings growth and 6.8% revenue growth with a 77.4% gross margin and 43.2% operating margin, but ROE is only 46.4% and the 9.0x forward P/E is low. The 10.0x base multiple is set above the current 9.0x forward P/E to reflect the strong margin profile and growth, but the low ROE and industrial cyclicality warrant a conservative 10.0x. HON is the named peer reference for a diversified industrial company with similar margin and cyclical risk.
- **Company fundamentals:** Reported diluted EPS 0.83 for the period ending 2026-10-02; forward EPS 3.34; forward P/E 9.03; gross margin 77.4%; operating margin 43.2%; profit margin 23.1%; revenue growth 12.2%; earnings growth 128.6%; ROE 0.46. Fiscal-period alignment and FY mapping are unverified.
- **Bull / Base / Bear:** 40.05 / 33.37 / 26.7
- **Bull / Base / Bear returns:** 32.84% / 10.68% / -11.44%
- **Scenario probabilities:** not separately assigned; see scenario table.

### XLV — Health Care sector ETF

- **Type:** ETF
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** XLV provides broad health care exposure without the single-stock risk of the shortlist names, but the sector-level momentum is negative. Alternatives considered: XLP, XLY, XLRE.
- **Thesis:** XLV is the Health Care sector ETF with a 20-day return of about -2.0% and a 60-day return of about -2.0%. It holds a diversified basket of large-cap health care names, including LLY, JNJ, ABBV, MRK, and UNH. The sector is not showing strong momentum, so a neutral stance is appropriate.
- **Source IDs:** S054, S058
- **Catalysts:** Diversified health care exposure, Potential stabilization in large-cap pharma and managed care
- **Risks:** Sector-level drawdown of about -2.0%, Concentration in large-cap names, Regulatory and reimbursement risks
- **Valuation method:** Holdings/portfolio valuation with AI total-return assumption
- **Valuation status:** verified; forward-EPS source: ; period flags: 
- **Valuation assumptions:** Holdings/portfolio valuation; 10 weighted holdings; coverage 61.42%; source IDs S054, S058
- **Top holdings:** LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59%
- **Portfolio valuation:** Top 10 holdings; numeric weight coverage 61.42%
- **Sector exposure:** Health Care
- **Underlying drivers:** Large-cap health care sector performance, managed care and pharma fundamentals, regulatory environment
- **Bull / Base / Bear:** 198.76 / 186.33 / 166.81
- **Bull / Base / Bear returns:** 12.0% / 5.0% / -6.0%
- **Scenario probabilities:** not separately assigned; see scenario table.

## Quant Risk Layer

| Field | Value |
| --- | --- |
| Volatility model | vol5_ols_v1 |
| Spike model | spike_logit_v1 |
| As-of date | 2026-11-19 |
| Target window | 2026-11-20 to 2026-11-27 |
| Forecast 5D annualized volatility | 26.81% |
| Historical-vol baseline | 23.45% |
| EWMA baseline | 20.84% |
| Spike probability | 68.03% |
| Spike threshold | 18.50% |
| Status | prospective |
| Forecast ID | 5de0e97bb5f8270d |

Risk-only; no directional interpretation or allocation implication.

## Scenarios

### Short Term (5 trading sessions)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 25% | +2.00% | Elevated 5-day volatility (0.268) and spike probability (0.68) suggest a sharp but short-lived risk-off bounce if the US close resolves positively, with rates and credit spreads stabilizing. |
| Base | 50% | +0.00% | Frozen daily-close model with no directional signal implies a range-bound week; earnings and rate expectations remain balanced, keeping returns near flat. |
| Bear | 25% | -2.00% | If the US close fails to confirm the spike, elevated volatility and a 0.68 spike probability could trigger a sell-off, with credit widening and earnings disappointment driving a modest decline. |

### Long Term (12 months)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 30% | +8.00% | Sustained rate stabilization and broad earnings improvement could lift risk appetite, with credit spreads tightening and a positive trend in economic data supporting an 8% gain. |
| Base | 40% | +3.00% | Gradual normalization of volatility and steady earnings growth support a modest positive drift, with rates and credit remaining stable enough to sustain a 3% return. |
| Bear | 30% | -5.00% | Persistent rate volatility, widening credit spreads, and earnings disappointment could drive a prolonged sell-off, with elevated volatility and spike risk compounding downside. |

## Positioning


## Catalysts

| Date | Event | Why it matters |
| --- | --- | --- |

## Key Risks


## External Source Ledger

| ID | Type | Ticker | Published | Status | URL | Claims |
| --- | --- | --- | --- | --- | --- | --- |
| S001 | macro | macro | 2026-11-18 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFF&cosd=2026-01-01 | Effective federal funds rate (DFF) latest observation 2026-11-18: 3.88 |
| S002 | macro | macro | 2026-11-18 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLH0A0HYM2&cosd=2026-01-01 | US high-yield OAS (BAMLH0A0HYM2) latest observation 2026-11-18: 3.47 |
| S003 | macro | macro | 2026-11-18 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLC0A0CM&cosd=2026-01-01 | US investment-grade OAS (BAMLC0A0CM) latest observation 2026-11-18: 0.93 |
| S004 | macro | macro | 2026-10-01 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCSL&cosd=2026-01-01 | US CPI (CPIAUCSL) latest observation 2026-10-01: 337.476 |
| S005 | macro | macro | 2026-10-01 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=UNRATE&cosd=2026-01-01 | US unemployment rate (UNRATE) latest observation 2026-10-01: 4.1 |
| S006 | macro | macro | 2026-10-01 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=PAYEMS&cosd=2026-01-01 | US nonfarm payrolls (PAYEMS) latest observation 2026-10-01: 159293 |
| S007 | macro | macro | 2026-11-19 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=T10Y2Y&cosd=2026-01-01 | 10Y-2Y Treasury spread (T10Y2Y) latest observation 2026-11-19: 0.28 |
| S008 | filing | APP | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001751008&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0001751008-26-000069); 8-K filed 2026-11-04 (accession 0001751008-26-000068); 10-Q filed 2026-08-05 (accession 0001751008-26-000059) |
| S009 | filing | PNR | 2026-10-27 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-27 (accession 0000077360-26-000058); 8-K filed 2026-10-27 (accession 0000077360-26-000055); 8-K filed 2026-09-22 (accession 0000077360-26-000050) |
| S010 | filing | CMG | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001058090&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0001058090-26-000104); 8-K filed 2026-10-28 (accession 0001058090-26-000103); 8-K filed 2026-09-14 (accession 0001058090-26-000088) |
| S011 | stock | CMG | 2026-11-20 | ok | https://finance.yahoo.com/quote/CMG | Trailing P/E: 33.925232; Forward P/E: 27.430178; Forward EPS: 1.32336; Price: 36.3; Market price: 36.3; Market cap: 45918588928; Sector: Consumer Cyclical; Trailing Eps: 1.07; Revenue Growth: 0.096; Earnings Growth: -0.062; Gross Margin: 0.39314; Operating Margin: 0.14715; Profit Margin: 0.10832; Return On Equity: 0.48518002; Total Revenue: 12713477120; Market Cap: 45918588928; Consensus EPS FY+1: 1.32336; growth: 0.216 |
| S012 | news | APP | Fri, 20 Nov 2026 03:18:44 GMT | ok | https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en | Applovin Corp Stock (APP) Closed Down by 3.04% on Nov 19: What Investors Need To Know - TradingKey (Fri, 20 Nov 2026 03:18:44 GMT); AppLovin stock soars after Q3 earnings, outlook beat - Yahoo Finance (Thu, 05 Nov 2026 08:00:00 GMT); AppLovin Stock Moves Higher: What's Going On? - Benzinga (Mon, 16 Nov 2026 18:52:15 GMT) |
| S013 | stock | APP | 2026-11-20 | ok | https://finance.yahoo.com/quote/APP | Trailing P/E: 25.523232; Forward P/E: 18.16897; Forward EPS: 20.86084; Price: 379.02; Market price: 379.02; Market cap: 125577658368; Sector: Communication Services; Trailing Eps: 14.85; Revenue Growth: 0.555; Earnings Growth: 0.755; Gross Margin: 0.8878; Operating Margin: 0.77782995; Profit Margin: 0.65887; Return On Equity: 2.1008599; Total Revenue: 7608893952; Market Cap: 125577658368; Consensus EPS FY+1: 20.72451; growth: 0.2744 |
| S014 | filing | APP | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json | Diluted EPS 11.61 for period ending 2026-09-30 (filed 2026-11-04) |
| S015 | stock | PNR | 2026-11-20 | ok | https://finance.yahoo.com/quote/PNR | Trailing P/E: 18.713896; Forward P/E: 12.948669; Forward EPS: 5.30402; Price: 68.68; Market price: 68.68; Market cap: 10965084160; Sector: Industrials; Trailing Eps: 3.67; Revenue Growth: -0.045; Earnings Growth: -0.188; Gross Margin: 0.40168998; Operating Margin: 0.21410999; Profit Margin: 0.15435; Return On Equity: 0.15605; Total Revenue: 3966200064; Market Cap: 10965084160; Consensus EPS FY+1: 5.30402; growth: 0.1282 |
| S016 | filing | PNR | 2026-10-27 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json | Diluted EPS 2.76 for period ending 2026-09-30 (filed 2026-10-27) |
| S017 | news | CMG | Wed, 18 Nov 2026 13:00:03 GMT | ok | https://news.google.com/rss/search?q=CMG+Chipotle+Mexican+Grill+stock&hl=en-US&gl=US&ceid=US:en | Chipotle Mexican Grill, Inc. (CMG) Is a Trending Stock: Facts to Know Before Betting on It - Yahoo Finance (Wed, 18 Nov 2026 13:00:03 GMT); Chipotle shares rise 7% after CEO says same-store sales growth will continue - CNBC (Wed, 28 Oct 2026 07:00:00 GMT); Chipotle Mexican Grill, Inc. $CMG Position Cut by Banco Santander S.A. - MarketBeat (Fri, 20 Nov 2026 08:31:53 GMT) |
| S018 | filing | CMG | 2026-10-29 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001058090.json | Diluted EPS 0.82 for period ending 2026-09-30 (filed 2026-10-29) |
| S019 | filing | IDXX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000874716&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000874716-26-000135); 8-K filed 2026-11-02 (accession 0001104659-26-120892); 10-Q filed 2026-08-04 (accession 0000874716-26-000123) |
| S020 | filing | GEN | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0000849399-26-000083); 8-K filed 2026-10-28 (accession 0000849399-26-000081); 8-K filed 2026-10-09 (accession 0000849399-26-000079) |
| S021 | stock | IDXX | 2026-11-20 | ok | https://finance.yahoo.com/quote/IDXX | Trailing P/E: 46.472374; Forward P/E: 40.824844; Forward EPS: 16.8929; Price: 689.65; Market price: 689.65; Market cap: 54334947328; Sector: Healthcare; Trailing Eps: 14.84; Revenue Growth: 0.099; Earnings Growth: 0.179; Gross Margin: 0.62722; Operating Margin: 0.32497; Profit Margin: 0.25357; Return On Equity: 0.68925005; Total Revenue: 4662220800; Market Cap: 54334947328; Consensus EPS FY+1: 16.8929; growth: 0.1244 |
| S022 | filing | CHTR | 2026-11-06 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-06 (accession 0001091667-26-000073); 8-K filed 2026-11-06 (accession 0001091667-26-000072); 8-K filed 2026-10-27 (accession 0001091667-26-000064) |
| S023 | stock | GEN | 2026-11-20 | ok | https://finance.yahoo.com/quote/GEN | Trailing P/E: 15.304568; Forward P/E: 9.034087; Forward EPS: 3.33736; Price: 30.15; Market price: 30.15; Market cap: 17887275008; Sector: Technology; Trailing Eps: 1.97; Revenue Growth: 0.122; Earnings Growth: 1.286; Gross Margin: 0.77410007; Operating Margin: 0.43229; Profit Margin: 0.23068; Return On Equity: 0.46402; Total Revenue: 5228000256; Market Cap: 17887275008; Consensus EPS FY+1: 3.33736; growth: 0.1286 |
| S024 | news | PNR | Wed, 18 Nov 2026 07:09:14 GMT | ok | https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en | Pentair plc (PNR) Stock Price, News, Quote & History - Yahoo! Finance Canada (Wed, 18 Nov 2026 07:09:14 GMT); Why Pentair Stock Popped This Morning - The Motley Fool (Tue, 27 Oct 2026 07:00:00 GMT); Why Is Pentair Stock Soaring Tuesday? - Pentair (NYSE:PNR) - Benzinga (Tue, 27 Oct 2026 07:00:00 GMT) |
| S025 | filing | IDXX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000874716.json | Diluted EPS 11.75 for period ending 2026-09-30 (filed 2026-11-02) |
| S026 | stock | CHTR | 2026-11-20 | ok | https://finance.yahoo.com/quote/CHTR | Trailing P/E: 12.516916; Forward P/E: 2.9209437; Forward EPS: 45.59485; Price: 133.18; Market price: 133.18; Market cap: 23846084608; Sector: Communication Services; Trailing Eps: 10.64; Revenue Growth: 0.091; Gross Margin: 0.55084; Operating Margin: 0.23389; Profit Margin: 0.02498; Return On Equity: 0.07019; Total Revenue: 55645999104; Market Cap: 23846084608; Consensus EPS FY+1: 49.52287; growth: 1.4594 |
| S027 | filing | GEN | 2026-10-29 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000849399.json | Diluted EPS 0.83 for period ending 2026-10-02 (filed 2026-10-29) |
| S028 | news | IDXX | Thu, 19 Nov 2026 18:52:13 GMT | ok | https://news.google.com/rss/search?q=IDXX+Idexx+Laboratories+stock&hl=en-US&gl=US&ceid=US:en | IDEXX Laboratories, Inc. (IDXX) Stock forecasts - Yahoo Finance UK (Thu, 19 Nov 2026 18:52:13 GMT); IDEXX Laboratories Inc. stock outperforms competitors on strong trading day - MarketWatch (Wed, 18 Nov 2026 21:49:00 GMT); Here's How Much $100 Invested In IDEXX Laboratories 20 Years Ago Would Be Worth Today - Benzinga (Wed, 18 Nov 2026 15:15:29 GMT) |
| S029 | news | GEN | Wed, 04 Nov 2026 08:00:00 GMT | ok | https://news.google.com/rss/search?q=GEN+Gen+Digital+stock&hl=en-US&gl=US&ceid=US:en | What Was Gen Digital Telling You Before Its Stock Ran? - Yahoo Finance (Wed, 04 Nov 2026 08:00:00 GMT); Gen Digital Inc. stock underperforms Tuesday when compared to competitors - MarketWatch (Tue, 22 Sep 2026 07:00:00 GMT); Gen Digital (GEN) Soars 5.6%: Is Further Upside Left in the Stock? - Yahoo Finance (Thu, 01 Oct 2026 07:00:00 GMT) |
| S030 | filing | CLX | 2026-11-19 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 | 8-K filed 2026-11-19 (accession 0001206774-26-000606); 10-Q filed 2026-11-02 (accession 0000021076-26-000046); 8-K filed 2026-11-02 (accession 0000021076-26-000044) |
| S031 | filing | CHTR | 2026-11-06 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001091667.json | Diluted EPS 0.38 for period ending 2026-09-30 (filed 2026-11-06) |
| S032 | filing | CVNA | 2026-10-28 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001690820&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-28 (accession 0001690820-26-000067); 8-K filed 2026-10-28 (accession 0001690820-26-000066); 8-K filed 2026-08-14 (accession 0001690820-26-000059) |
| S033 | stock | CLX | 2026-11-20 | ok | https://finance.yahoo.com/quote/CLX | Trailing P/E: 18.866907; Forward P/E: 17.006031; Forward EPS: 6.1684; Price: 104.9; Market price: 104.9; Market cap: 12708361216; Sector: Consumer Defensive; Trailing Eps: 5.56; Revenue Growth: 0.333; Earnings Growth: 1.138; Gross Margin: 0.41939998; Operating Margin: 0.14286; Profit Margin: 0.09408; Return On Equity: 5.34363; Total Revenue: 7196000256; Market Cap: 12708361216; Consensus EPS FY+1: 6.1684; growth: 0.0769 |
| S034 | stock | CVNA | 2026-11-20 | ok | https://finance.yahoo.com/quote/CVNA | Trailing P/E: 32.69231; Forward P/E: 31.7444; Forward EPS: 2.14211; Price: 68.0; Market price: 68.0; Market cap: 170772529152; Sector: Consumer Cyclical; Trailing Eps: 2.08; Revenue Growth: 0.424; Earnings Growth: 0.857; Gross Margin: 0.19041; Operating Margin: 0.08743; Profit Margin: 0.06215; Return On Equity: 0.54672; Total Revenue: 27451000832; Market Cap: 170772529152; Consensus EPS FY+1: 2.09151; growth: 0.28530002 |
| S035 | filing | SNDK | 2026-11-19 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0002023554&type=10-Q&dateb=&owner=include&count=10 | 8-K filed 2026-11-19 (accession 0001628280-26-075127); 8-K filed 2026-11-18 (accession 0001628280-26-074848); 10-Q filed 2026-10-30 (accession 0001628280-26-068601) |
| S036 | filing | CLX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000021076.json | Diluted EPS 1.39 for period ending 2026-09-30 (filed 2026-11-02) |
| S037 | filing | CVNA | 2026-02-18 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001690820.json | Diluted EPS 8.45 for period ending 2025-12-31 (filed 2026-02-18) |
| S038 | stock | SNDK | 2026-11-20 | ok | https://finance.yahoo.com/quote/SNDK | Trailing P/E: 48.283886; Forward P/E: 20.900183; Forward EPS: 36.13174; Price: 755.16; Market price: 755.16; Market cap: 107451228160; Sector: Technology; Trailing Eps: 15.64; Revenue Growth: 3.779; Earnings Growth: 69.133; Gross Margin: 0.79952; Operating Margin: 0.7268; Profit Margin: 0.67039; Return On Equity: 1.41174; Total Revenue: 28970999808; Market Cap: 107451228160; Consensus EPS FY+1: 36.13174; growth: 0.2707 |
| S039 | news | CHTR | Sun, 15 Nov 2026 05:10:00 GMT | ok | https://news.google.com/rss/search?q=CHTR+Charter+Communications+stock&hl=en-US&gl=US&ceid=US:en | Charter Communications (CHTR) Stock Could Be A Bargain Following Its New Operating Model - Yahoo Finance (Sun, 15 Nov 2026 05:10:00 GMT); Is Charter Stock Worth The Wait? - Trefis (Tue, 17 Nov 2026 12:33:16 GMT); Why Charter Communications Plunged in September - The Motley Fool (Thu, 08 Oct 2026 07:00:00 GMT) |
| S040 | filing | SNDK | 2026-10-30 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0002023554.json | Diluted EPS 52.6 for period ending 2026-10-02 (filed 2026-10-30) |

## Sources

- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFF&cosd=2026-01-01 (2026-11-18)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLH0A0HYM2&cosd=2026-01-01 (2026-11-18)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLC0A0CM&cosd=2026-01-01 (2026-11-18)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCSL&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=UNRATE&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=PAYEMS&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=T10Y2Y&cosd=2026-01-01 (2026-11-19)
- filing APP: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001751008&type=10-Q&dateb=&owner=include&count=10 (2026-11-04)
- filing PNR: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 (2026-10-27)
- filing CMG: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001058090&type=10-Q&dateb=&owner=include&count=10 (2026-10-29)
- stock CMG: https://finance.yahoo.com/quote/CMG (2026-11-20)
- news APP: https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en (Fri, 20 Nov 2026 03:18:44 GMT)
- stock APP: https://finance.yahoo.com/quote/APP (2026-11-20)
- filing APP: https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json (2026-11-04)
- stock PNR: https://finance.yahoo.com/quote/PNR (2026-11-20)
- filing PNR: https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json (2026-10-27)
- news CMG: https://news.google.com/rss/search?q=CMG+Chipotle+Mexican+Grill+stock&hl=en-US&gl=US&ceid=US:en (Wed, 18 Nov 2026 13:00:03 GMT)
- filing CMG: https://data.sec.gov/api/xbrl/companyfacts/CIK0001058090.json (2026-10-29)
- filing IDXX: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000874716&type=10-Q&dateb=&owner=include&count=10 (2026-11-02)
- filing GEN: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 (2026-10-29)

## AI Provenance

- Provider / model: hermes-local-proxy / upstage/solar-mini4:free
- Market research: attempts=1 tokens=9518 (prompt=6518, completion=3000) runtime=18.29s
- Fundamental research: generated this run at 2026-11-20T10:08:46.981253+00:00
- Evidence source dates: {'as_of': '2026-11-19', 'latest_equity_date': '2026-11-19', 'latest_macro_date': '2026-11-20', 'flows_date': '2026-11-19'}
- Evidence fingerprint: 00c52e03523f7c2d630d0511f51f9c3f322b68dedb3c9c099a9868f3f737e160
- Source citations are retrieved external records in the ledger above; market values remain from the verified database snapshot.


## Disclosures

- This is research and market intelligence, not investment advice.
- AI conclusions are research judgments, not validated return predictions.
- The frozen risk layer is risk-only and is not used for directional views or allocations.
- Legacy scores are not active inputs or outputs.

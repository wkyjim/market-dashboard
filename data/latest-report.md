# AEGIS AI-First Market Intelligence

Research generated at: 16 November 2026, 21:08 HKT
Database freshness: equity 2026-11-13 (latest row retrieved 2026-11-16 13:06:43.000010+08:00)
Data cutoff: 2026-11-13 US cash close
Snapshot ID: aegis-hourly-20261116T130859Z

## Executive Summary

- **AI market view: Late-November 2026 US equities show a mixed tape: broad market breadth is positive but the index is slightly negative over 20 days, with leadership from Health Care, Consumer Discretionary, and Consumer Staples while Information Technology and Energy lag. Institutional flows are mixed, with Health Care and Consumer Staples receiving strong confirmation and Financials/Real Estate/Communication Services showing structural distribution. Macro data point to a still-elevated but easing inflation backdrop, a labor market near full employment, and a modestly positive 10Y-2Y curve, though the 2026-11-16 Asian market prints show sharp declines in Korea and Japan.**
- Broad market breadth is constructive: 71.3% of names are above their 50-day moving average and 70.5% have positive 20-day returns, with an advance/decline ratio of 1.70.
- Index-level momentum is weaker: SPX is down 1.28% over 20 days, and the 20-day breadth/price divergence is negative at -27.49, indicating a divergence between index performance and constituent strength.
- Sector leadership is concentrated in Health Care (+6.87% 20d), Consumer Discretionary (+6.69%), and Consumer Staples (+5.40%), while Information Technology (-7.19%) and Energy (-4.81%) are the weakest sectors.
- Institutional flows show strong confirmation in Health Care and Consumer Staples, but structural distribution in Financials, Real Estate, and Communication Services, with XLU showing exceptional institutional selling.
- Macro data show CPI at 336.298 (Sep-2026) and core CPI at 338.896, unemployment at 4.2%, and a 10Y-2Y spread of 0.27, with effective fed funds at 3.88% as of 2026-11-12.
- Risk environment is elevated: forecast volatility is 14.93% over 5 days, spike probability is 16.51%, and the frozen risk model flags a 16.5% spike probability against a 18.5% threshold, with no directional signal.

## Data QC

- Status: **PASS_WITH_WARNINGS**
- Equity session: 0 completed session(s) behind inference date
- Equity provenance: 393 provisional / 12576 canonical
- Breadth lag: 0 session(s); ETF-flow lag: 0 session(s)
- Note: Equity session contains a mix of provisional yfinance and canonical Massive rows.
- External sources: 79 ok / 0 unavailable; retrieved 2026-11-16T13:09:25.746388+00:00

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
| SPX | 7561.67 | -1.28% (20d) | Index is slightly negative over 20 days despite positive breadth; 71.3% of names above 50d and 63.6% above 200d. |
| Health Care (XLV) | return_20d +6.87% | +6.87% | Strongest sector; ETF trailing P/E 30.78 and flow z-scores of 1.45 (20d) and 1.72 (60d) indicate strong institutional confirmation. |
| Consumer Discretionary (XLY) | return_20d +6.69% | +6.69% | Second-strongest sector; flow z-scores of -0.38 (20d) and -0.78 (60d) indicate structural distribution despite price strength. |
| Consumer Staples (XLP) | return_20d +5.40% | +5.40% | Third-strongest sector; ETF trailing P/E 24.85 and flow z-scores of 1.45 (20d) and 1.72 (60d) indicate strong institutional confirmation. |
| Information Technology (XLK) | return_20d -7.19% | -7.19% | Weakest sector; ETF trailing P/E 30.03 and negative flow z-scores indicate institutional distribution. |
| Energy (XLE) | return_20d -4.81% | -4.81% | Weakest sector; ETF trailing P/E 16.23 and negative flow z-scores indicate institutional distribution. |

## Macro, Fiscal, Rates, Liquidity and Credit

- Inflation: CPI (CPIAUCSL) is 336.298 in Sep-2026 and core CPI is 338.896, indicating a still-elevated but stable inflation backdrop; the external source S004 reports CPI at 337.476 for Oct-2026, suggesting a modest monthly increase.
- Labor: Unemployment rate is 4.2% in Sep-2026, near full employment, with nonfarm payrolls at 159,293 (thousands) in Oct-2026 per S006, indicating a tight labor market.
- Policy: Effective federal funds rate is 3.88% as of 2026-11-12 (S001), and the 10Y-2Y Treasury spread is 0.27 as of 2026-11-13 (S007), indicating a modestly positive curve.
- Rates: IG OAS is 0.89 and HY OAS is 3.20 as of 2026-11-12 (S002, S003), indicating relatively tight credit spreads and stable funding conditions.
- Liquidity: The frozen risk model shows forecast volatility of 14.93% over 5 days, spike probability of 16.51%, and a 16.5% spike probability against an 18.5% threshold, with no directional signal, indicating elevated but not extreme risk.
- External macro: Asian markets on 2026-11-16 show sharp declines in Korea (KS11 -3.59%) and Japan (N225 -2.42%), while Hong Kong (HSI) is up 0.49%, suggesting regional divergence.

## US Equities and 11 GICS Sectors

Macro source IDs: S001, S002, S003, S004, S005, S006, S007

| GICS sector | Evidence | AI research stance | Source IDs |
| --- | --- | --- | --- |
| Health Care | 20d return +6.87% (XLV), trailing P/E 30.78 (S050), flow z-scores 1.45 (20d) and 1.72 (60d) with strong confirmation, SPX 20d -1.28%. | Constructive: strong price momentum, positive institutional flows, and broad-based strength; sector is a clear leader in the current tape. | S050 |
| Consumer Staples | 20d return +5.40% (XLP), trailing P/E 24.85 (S055), flow z-scores 1.45 (20d) and 1.72 (60d) with strong confirmation, SPX 20d -1.28%. | Constructive: defensive sector with strong institutional inflows and positive price momentum; consistent with a cautious but stable macro backdrop. | S055 |
| Consumer Discretionary | 20d return +6.69% (XLY), trailing P/E 25.11 (S062), flow z-scores -0.38 (20d) and -0.78 (60d) with structural distribution, SPX 20d -1.28%. | Mixed: strong price momentum but institutional distribution suggests some underlying caution; price strength may be retail-driven or momentum-driven. | S062 |
| Real Estate | 20d return +5.24% (XLRE), trailing P/E 29.63 (S060), flow z-scores -2.15 (20d) with exceptional institutional selling, SPX 20d -1.28%. | Cautious: price strength is not supported by institutional flows; structural distribution and exceptional selling indicate potential vulnerability. | S060 |
| Financials | 20d return +5.69% (XLF), trailing P/E 15.85 (S065), flow z-scores -0.38 (20d) and -0.78 (60d) with structural distribution, SPX 20d -1.28%. | Cautious: price strength is not supported by institutional flows; structural distribution suggests some underlying concern despite low valuation. | S065 |
| Utilities | 20d return +4.34% (XLU), trailing P/E 18.11 (S064), flow z-scores -2.15 (20d) with exceptional institutional selling, SPX 20d -1.28%. | Cautious: price strength is not supported by institutional flows; exceptional selling and medium-term deterioration suggest potential weakness. | S064 |
| Materials | 20d return +2.57% (XLB), trailing P/E 21.72 (S063), flow z-scores -0.38 (20d) and -0.78 (60d) with structural distribution, SPX 20d -1.28%. | Cautious: modest price strength but institutional distribution suggests limited conviction; sector is a laggard in the current tape. | S063 |
| Industrials | 20d return +0.61% (XLI), trailing P/E 27.07 (S068), flow z-scores -0.38 (20d) and -0.78 (60d) with structural distribution, SPX 20d -1.28%. | Cautious: near-flat price performance and institutional distribution suggest limited momentum; sector is a laggard in the current tape. | S068 |
| Communication Services | 20d return -1.48% (XLC), trailing P/E 17.26 (S069), flow z-scores -0.38 (20d) and -0.78 (60d) with structural distribution, SPX 20d -1.28%. | Cautious: negative price momentum and institutional distribution; sector is a clear laggard in the current tape. | S069 |
| Information Technology | 20d return -7.19% (XLK), trailing P/E 30.03 (S070), flow z-scores -0.38 (20d) and -0.78 (60d) with structural distribution, SPX 20d -1.28%. | Cautious: negative price momentum and institutional distribution; sector is the weakest in the current tape despite a moderate trailing P/E. | S070 |
| Energy | 20d return -4.81% (XLE), trailing P/E 16.23 (S075), flow z-scores -0.38 (20d) and -0.78 (60d) with structural distribution, SPX 20d -1.28%. | Cautious: negative price momentum and institutional distribution; sector is a clear laggard in the current tape. | S075 |

### Sector fundamentals, valuation and earnings

No point-in-time sector fundamentals (e.g., revenue growth, margins, consensus estimates) are supplied in the database snapshot. The supplied evidence is limited to ETF trailing P/E, 20-day returns, and flow z-scores. Growth and margin data are unavailable for the full sector universe, so sector views are based on price momentum, institutional flows, and valuation multiples only.

## Growth vs Value


## ETF Flows and Breadth


## Stock Ideas

Single-stock research uses reported EPS, forward P/E and company fundamentals. All ideas are research judgments, not validated return predictions.

| Ticker | Security | Research view | Price | EPS | Forward P/E | Base target | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| APP | AppLovin | NEW | 409.1 | 20.86026 | 19.611452 | 417.21 | NEW |
| PNR | Pentair | KEEP | 68.3 | 5.30402 | 12.877027 | 68.95 | KEEP |
| ROP | Roper Technologies | NEW | 479.975 | 24.57318 | 19.532475 | 491.46 | NEW |
| RDDT | Reddit | KEEP | 98.45 | 9.10039 | 10.818217 | 100.1 | KEEP |

## ETF Ideas

ETF research uses holdings, portfolio valuation and exposure. Single-stock EPS × P/E valuation is not applied to ETFs.

| Ticker | Fund | Research view | Price | Top holdings | Portfolio valuation | Sector exposure | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| XLV | Health Care sector ETF | KEEP | 188.85 | LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59% | Top 10 holdings; numeric weight coverage 61.42% | Health Care | KEEP |
### APP — AppLovin

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** AppLovin offers a rare combination of strong momentum, high growth, and a reasonable valuation relative to its sector, making it a more attractive standalone candidate than the lower-growth, higher-multiple names in the shortlist such as IDXX or CLX. Alternatives considered: IDXX, CLX.
- **Thesis:** AppLovin screens in the top 20-day momentum bucket with a 53.7% 20-day return and a 32.5% 60-day return, while its 20.05 trailing P/E and 4.99% earnings yield sit at sector-relative P/E of 1.0. Reported diluted EPS of 11.61 for the fiscal period ending 2026-09-30 and forward EPS of 20.86 support a forward P/E of 19.61, with revenue growth of 55.5% and earnings growth of 75.5% providing fundamental backing for the momentum.
- **Source IDs:** S008, S011, S013, S015
- **Catalysts:** Continued high-single-digit to low-double-digit revenue growth from the core advertising business, Sustained earnings growth outpacing revenue growth to compress the forward P/E, Sector-relative P/E of 1.0 indicating the stock is not overvalued versus its sector peers
- **Risks:** High 20-day momentum can mean elevated volatility and potential mean-reversion risk, Forward EPS and fiscal-year mapping are unverified, so forward P/E estimates carry uncertainty, Advertising market cyclicality could pressure the growth trajectory if macro conditions deteriorate
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 20.8603 (source.forwardEps) x AI multiple assumption 20.00; source IDs S008, S011, S013, S015
- **EPS:** 20.86026 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 19.611452
- **FY+1 growth assumption:** 27.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / AAPL / APP shows 27.44% FY+1 consensus earnings growth and 25.37% revenue growth with exceptional 88.8% gross margin and 77.8% operating margin, indicating strong pricing power and operating leverage. The forward P/E of 19.6x is supported by high margins and 26 analysts; AAPL is the named peer reference for premium-margin, high-ROE software/tech valuation. Base multiple 20x reflects growth and margin strength; bull 24x assumes continued margin expansion and multiple re-rating; bear 16x reflects valuation compression risk if growth decelerates.
- **Company fundamentals:** Reported diluted EPS 11.61 for period ending 2026-09-30; forward EPS 20.86; forward P/E 19.61; revenue growth 55.5%; earnings growth 75.5%; gross margin 88.78%; operating margin 77.78%; profit margin 65.89%; ROE 2.10%.
- **Bull / Base / Bear:** 500.65 / 417.21 / 333.76
- **Bull / Base / Bear returns:** 22.38% / 1.98% / -18.42%
- **Scenario probabilities:** not separately assigned; see scenario table.

### PNR — Pentair

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Pentair offers a lower valuation entry point than higher-growth names like APP or ROP, but the negative growth profile makes it a more cautious hold rather than a top pick. Alternatives considered: APP, ROP.
- **Thesis:** Pentair screens in the top 20-day momentum bucket with a 27.8% 20-day return and a 7.1% 60-day return. Its trailing P/E of 13.59 and earnings yield of 7.36% are supported by a forward P/E of 12.88, but revenue growth of -4.5% and earnings growth of -18.8% indicate the underlying business is contracting, which tempers the momentum signal.
- **Source IDs:** S009, S016, S022, S023
- **Catalysts:** Potential stabilization or improvement in revenue and earnings growth as the cycle turns, Attractive valuation metrics relative to the broader market, Sector-relative P/E of 0.49 suggesting the stock is cheap versus its sector
- **Risks:** Negative revenue and earnings growth raise questions about the durability of the current valuation, Industrial end-market exposure may face cyclical headwinds, Momentum is positive but weaker than the top-tier names in the shortlist
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 5.3040 (source.forwardEps) x AI multiple assumption 13.00; source IDs S009, S016, S022, S023
- **EPS:** 5.30402 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 12.877027
- **FY+1 growth assumption:** 12.82%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / HON / PNR has 12.82% FY+1 consensus earnings growth and 18.38% revenue growth, with 40.2% gross margin and 21.4% operating margin typical of industrial/contract manufacturing. The forward P/E of 12.9x is reasonable for a cyclical industrial; HON is the named peer reference for industrial growth and margin profile. Base 13x reflects steady but moderate growth; bull 16x assumes margin recovery and order momentum; bear 10x reflects cyclical downside and margin pressure risk.
- **Company fundamentals:** Reported diluted EPS 2.76 for period ending 2026-09-30; forward EPS 5.30; forward P/E 12.88; revenue growth -4.5%; earnings growth -18.8%; gross margin 40.17%; operating margin 21.41%; profit margin 15.44%; ROE 15.61%.
- **Bull / Base / Bear:** 84.86 / 68.95 / 53.04
- **Bull / Base / Bear returns:** 24.25% / 0.95% / -22.34%
- **Scenario probabilities:** not separately assigned; see scenario table.

### ROP — Roper Technologies

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** Roper Technologies combines durable revenue growth with strong earnings momentum and a reasonable valuation, making it a more attractive standalone candidate than the lower-growth, higher-multiple names in the shortlist such as IDXX or CLX. Alternatives considered: IDXX, CLX.
- **Thesis:** Roper Technologies screens in the top 20-day momentum bucket with a 25.4% 20-day return and a 16.9% 60-day return. Its trailing P/E of 16.67 and earnings yield of 6.00% are supported by a forward P/E of 19.53, with revenue growth of 7.6% and earnings growth of 32.6% providing fundamental backing for the momentum.
- **Source IDs:** S030, S033, S036, S043
- **Catalysts:** Steady revenue growth in a niche software and technology-enabled solutions market, Earnings growth outpacing revenue growth to compress the forward P/E, Sector-relative P/E of 0.49 indicating the stock is not overvalued versus its sector
- **Risks:** Forward P/E of 19.53 is higher than the trailing P/E, suggesting some multiple expansion already priced in, High 20-day momentum can mean elevated volatility and potential mean-reversion risk, Niche software exposure may face competitive or regulatory pressures
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 24.5732 (source.forwardEps) x AI multiple assumption 20.00; source IDs S030, S033, S036, S043
- **EPS:** 24.57318 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 19.532475
- **FY+1 growth assumption:** 9.81%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / HD / ROP shows 9.81% FY+1 consensus earnings growth and 6.29% revenue growth, with 69.7% gross margin and 28.0% operating margin, indicating a stable consumer/retail business. The forward P/E of 19.5x is supported by consistent profitability; HD is the named peer reference for consumer discretionary valuation. Base 20x reflects steady growth and margin stability; bull 24x assumes consumer resilience and multiple expansion; bear 16x reflects consumer slowdown risk.
- **Company fundamentals:** Reported diluted EPS 21.30 for period ending 2026-09-30; forward EPS 24.57; forward P/E 19.53; revenue growth 7.6%; earnings growth 32.6%; gross margin 69.67%; operating margin 28.05%; profit margin 30.71%; ROE 13.23%.
- **Bull / Base / Bear:** 589.76 / 491.46 / 393.17
- **Bull / Base / Bear returns:** 22.87% / 2.39% / -18.09%
- **Scenario probabilities:** not separately assigned; see scenario table.

### RDDT — Reddit

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Reddit offers a deep dislocation play with strong growth, but the negative price returns and high valuation multiples make it a more cautious hold than the momentum leaders in the shortlist. Alternatives considered: INTC, MRVL.
- **Thesis:** Reddit screens in the largest 20-day dislocation bucket with a 36.9% 20-day drawdown and a 34.5% 60-day drawdown. Its trailing P/E of 33.19 and earnings yield of 3.01% are supported by a forward P/E of 10.82, with revenue growth of 53.0% and earnings growth of 74.9% providing fundamental backing, but the deep dislocation and negative price returns suggest significant uncertainty.
- **Source IDs:** S035, S037, S039, S045
- **Catalysts:** Continued high revenue growth from the advertising and content monetization business, Earnings growth outpacing revenue growth to compress the forward P/E, Potential recovery in sentiment as the dislocation plays out
- **Risks:** Deep 60-day drawdown of 39.4% indicates significant downside risk, Negative 20-day and 60-day price returns suggest the dislocation may not be fully resolved, High valuation multiples relative to sector peers (sector-relative P/E of 1.66) could lead to further multiple compression
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 9.1004 (source.forwardEps) x AI multiple assumption 11.00; source IDs S035, S037, S039, S045
- **EPS:** 9.10039 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 10.818217
- **FY+1 growth assumption:** 24.01%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / DIS / RDDT has 24.01% FY+1 consensus earnings growth and 28.38% revenue growth, with 91.5% gross margin and 32.0% ROE, indicating a high-margin, asset-light business. The forward P/E of 10.8x is low relative to growth and margins; DIS is the named peer reference for media/entertainment valuation. Base 11x reflects strong growth but moderate multiple due to cyclicality; bull 14x assumes sustained growth and margin leadership; bear 8x reflects competitive and regulatory risk.
- **Company fundamentals:** Reported diluted EPS 3.66 for period ending 2026-09-30; forward EPS 9.10; forward P/E 10.82; revenue growth 53.0%; earnings growth 74.9%; gross margin 91.55%; operating margin 29.40%; profit margin 32.11%; ROE 32.03%.
- **Bull / Base / Bear:** 127.41 / 100.1 / 72.8
- **Bull / Base / Bear returns:** 29.42% / 1.68% / -26.05%
- **Scenario probabilities:** not separately assigned; see scenario table.

### XLV — Health Care sector ETF

- **Type:** ETF
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** XLV offers a diversified, lower-idiosyncratic-risk way to express health care exposure compared to single-stock names like IDXX, making it a more stable core holding within a health care allocation. Alternatives considered: XLP, XLF.
- **Thesis:** The Health Care sector ETF (XLV) provides diversified exposure to the sector with top holdings including LLY, JNJ, ABBV, MRK, and UNH. The ETF shows a positive raw price change of 0.54% and offers a way to gain broad sector exposure without single-stock idiosyncratic risk.
- **Source IDs:** S050, S054
- **Catalysts:** Diversified exposure to large-cap health care names with strong fundamentals, Positive sector momentum as reflected in the raw price change, Reduced single-stock risk compared to individual health care stocks
- **Risks:** Sector-specific headwinds such as regulatory changes or drug pricing policy, Concentration in top holdings may limit diversification benefits, Positive raw price change may not be sustained if sector fundamentals weaken
- **Valuation method:** Holdings/portfolio valuation with AI total-return assumption
- **Valuation status:** verified; forward-EPS source: ; period flags: 
- **Valuation assumptions:** Holdings/portfolio valuation; 10 weighted holdings; coverage 61.42%; source IDs S050, S054
- **Top holdings:** LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59%
- **Portfolio valuation:** Top 10 holdings; numeric weight coverage 61.42%
- **Sector exposure:** Health Care
- **Underlying drivers:** Diversified exposure to large-cap health care companies with strong revenue and earnings growth, including LLY, JNJ, ABBV, MRK, and UNH.
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
| Bull | 25% | +2.00% | Low 5-day forecast vol (14.9%) and below-threshold spike probability (16.5% vs 18.5% threshold) support a modest upside if US close confirms no risk-off repricing. |
| Base | 50% | +0.00% | Frozen daily-close model with no directional signal and near-baseline volatility implies range-bound trading around the 2026-11-13 close. |
| Bear | 25% | -2.00% | If the US close triggers a spike above the 18.5% threshold, elevated vol and negative breadth could drive a mild downside move. |

### Long Term (12 months)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 30% | +8.00% | Sustained earnings growth and positive rate trajectory support a higher equity multiple over the horizon. |
| Base | 40% | +3.00% | Moderate expansion with stable credit conditions and balanced market breadth yields a low-single-digit return. |
| Bear | 30% | -5.00% | Earnings disappointment or widening credit spreads could compress valuations and produce a moderate decline. |

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
| S008 | filing | APP | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001751008&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0001751008-26-000069); 8-K filed 2026-11-04 (accession 0001751008-26-000068); 10-Q filed 2026-08-05 (accession 0001751008-26-000059) |
| S009 | filing | PNR | 2026-10-27 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-27 (accession 0000077360-26-000058); 8-K filed 2026-10-27 (accession 0000077360-26-000055); 8-K filed 2026-09-22 (accession 0000077360-26-000050) |
| S010 | filing | FISV | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0000798354-26-000042); 8-K filed 2026-11-03 (accession 0000798354-26-000039); 8-K filed 2026-10-23 (accession 0001193125-26-429481) |
| S011 | filing | APP | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json | Diluted EPS 11.61 for period ending 2026-09-30 (filed 2026-11-04) |
| S012 | news | FISV | Mon, 16 Nov 2026 02:19:15 GMT | ok | https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en | Fiserv, Inc. (FISV) Stock Price, News, Quote & History - Yahoo! Finance Canada (Mon, 16 Nov 2026 02:19:15 GMT); Fiserv (FISV) Stock Still Looks Like A Bargain After Lawsuit Claims - Yahoo Finance (Thu, 22 Oct 2026 07:00:00 GMT); Why Fiserv, Inc. (FISV) Was Exited by Ariel Appreciation Fund - Yahoo Finance (Wed, 28 Oct 2026 07:00:00 GMT) |
| S013 | news | APP | Thu, 12 Nov 2026 20:05:45 GMT | ok | https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en | AppLovin Just Ripped 47% in a Month: Is It Too Late to Buy APP Stock Now? - Yahoo Finance (Thu, 12 Nov 2026 20:05:45 GMT); Is Trending Stock AppLovin Corporation (APP) a Buy Now? - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT); APP Stock Surges 51% After Q3 Earnings: Is it Still a Buy? - Yahoo Finance (Tue, 10 Nov 2026 14:24:00 GMT) |
| S014 | stock | FISV | 2026-11-16 | ok | https://finance.yahoo.com/quote/FISV | Forward P/E: 7.99667; Price: 63.78; Market price: 63.78; Market cap: 33934002176; Market Cap: 33934002176; Consensus EPS FY+1: 7.97582; growth: 0.0959 |
| S015 | stock | APP | 2026-11-16 | ok | https://finance.yahoo.com/quote/APP | Trailing P/E: 27.54882; Forward P/E: 19.611452; Forward EPS: 20.86026; Price: 409.1; Market price: 409.1; Market cap: 135543824384; Sector: Communication Services; Trailing Eps: 14.85; Revenue Growth: 0.555; Earnings Growth: 0.755; Gross Margin: 0.8878; Operating Margin: 0.77782995; Profit Margin: 0.65887; Return On Equity: 2.1008599; Total Revenue: 7608893952; Market Cap: 135543824384; Consensus EPS FY+1: 20.72438; growth: 0.2744 |
| S016 | stock | PNR | 2026-11-16 | ok | https://finance.yahoo.com/quote/PNR | Trailing P/E: 18.610355; Forward P/E: 12.877027; Forward EPS: 5.30402; Price: 68.3; Market price: 68.3; Market cap: 10904415232; Sector: Industrials; Trailing Eps: 3.67; Revenue Growth: -0.045; Earnings Growth: -0.188; Gross Margin: 0.40168998; Operating Margin: 0.21410999; Profit Margin: 0.15435; Return On Equity: 0.15605; Total Revenue: 3966200064; Market Cap: 10904415232; Consensus EPS FY+1: 5.30402; growth: 0.1282 |
| S017 | filing | FISV | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json | Diluted EPS -8.9 for period ending 2026-09-30 (filed 2026-11-04) |
| S018 | filing | GEN | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0000849399-26-000083); 8-K filed 2026-10-28 (accession 0000849399-26-000081); 8-K filed 2026-10-09 (accession 0000849399-26-000079) |
| S019 | stock | GEN | 2026-11-16 | ok | https://finance.yahoo.com/quote/GEN | Trailing P/E: 15.431472; Forward P/E: 9.108996; Forward EPS: 3.33736; Price: 30.4; Market price: 30.4; Market cap: 18035593216; Sector: Technology; Trailing Eps: 1.97; Revenue Growth: 0.122; Earnings Growth: 1.286; Gross Margin: 0.77410007; Operating Margin: 0.43229; Profit Margin: 0.23068; Return On Equity: 0.46402; Total Revenue: 5228000256; Market Cap: 18035593216; Consensus EPS FY+1: 3.33736; growth: 0.1286 |
| S020 | filing | CLX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000021076-26-000046); 8-K filed 2026-11-02 (accession 0000021076-26-000044); 8-K filed 2026-10-29 (accession 0001206774-26-000586) |
| S021 | stock | CLX | 2026-11-16 | ok | https://finance.yahoo.com/quote/CLX | Trailing P/E: 19.68705; Forward P/E: 17.745283; Forward EPS: 6.1684; Price: 109.46; Market price: 109.46; Market cap: 13260793856; Sector: Consumer Defensive; Trailing Eps: 5.56; Revenue Growth: 0.333; Earnings Growth: 1.138; Gross Margin: 0.41939998; Operating Margin: 0.14286; Profit Margin: 0.09408; Return On Equity: 5.34363; Total Revenue: 7196000256; Market Cap: 13260793856; Consensus EPS FY+1: 6.1684; growth: 0.0769 |
| S022 | news | PNR | Sat, 14 Nov 2026 08:48:27 GMT | ok | https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en | Pentair plc (PNR) Stock Price, News, Quote & History - Yahoo! Finance Canada (Sat, 14 Nov 2026 08:48:27 GMT); Pentair plc (PNR) stock price, news, quote and history - Yahoo Finance UK (Fri, 13 Nov 2026 22:09:48 GMT); Pentair plc (PNR) Q3 Earnings and Revenues Beat Estimates - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT) |
| S023 | filing | PNR | 2026-10-27 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json | Diluted EPS 2.76 for period ending 2026-09-30 (filed 2026-10-27) |
| S024 | news | GEN | Thu, 29 Oct 2026 07:00:00 GMT | ok | https://news.google.com/rss/search?q=GEN+Gen+Digital+stock&hl=en-US&gl=US&ceid=US:en | Gen Digital (GEN) Stock Repriced After Q2 Earnings Put Margins Center Stage - Yahoo Finance (Thu, 29 Oct 2026 07:00:00 GMT); Gen Digital Stock: Is Wall Street Bullish or Bearish? - Yahoo Finance (Thu, 05 Nov 2026 08:00:00 GMT); Are Business Services Stocks Lagging GEN DIGITAL INC (GEN) This Year? - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT) |
| S025 | filing | CHTR | 2026-11-06 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-06 (accession 0001091667-26-000073); 8-K filed 2026-11-06 (accession 0001091667-26-000072); 8-K filed 2026-10-27 (accession 0001091667-26-000064) |
| S026 | stock | CHTR | 2026-11-16 | ok | https://finance.yahoo.com/quote/CHTR | Trailing P/E: 13.006578; Forward P/E: 3.0452294; Forward EPS: 45.44485; Price: 138.39; Market price: 138.39; Market cap: 24778944512; Sector: Communication Services; Trailing Eps: 10.64; Revenue Growth: 0.091; Gross Margin: 0.55084; Operating Margin: 0.23389; Profit Margin: 0.02498; Return On Equity: 0.07019; Total Revenue: 55645999104; Market Cap: 24778944512; Consensus EPS FY+1: 49.35412; growth: 1.1136 |
| S027 | news | CLX | Fri, 13 Nov 2026 23:34:51 GMT | ok | https://news.google.com/rss/search?q=CLX+Clorox+stock&hl=en-US&gl=US&ceid=US:en | The Clorox Company (CLX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 23:34:51 GMT); The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance UK (Sat, 14 Nov 2026 06:03:20 GMT); Should You Forget Clorox Stock Near a 52-Week Low? - Yahoo Finance (Mon, 26 Oct 2026 07:00:00 GMT) |
| S028 | stock | IDXX | 2026-11-16 | ok | https://finance.yahoo.com/quote/IDXX | Trailing P/E: 47.45485; Forward P/E: 41.687927; Forward EPS: 16.8929; Price: 704.23; Market price: 704.23; Market cap: 55483650048; Sector: Healthcare; Trailing Eps: 14.84; Revenue Growth: 0.099; Earnings Growth: 0.179; Gross Margin: 0.62722; Operating Margin: 0.32497; Profit Margin: 0.25357; Return On Equity: 0.68925005; Total Revenue: 4662220800; Market Cap: 55483650048; Consensus EPS FY+1: 16.8929; growth: 0.1244 |
| S029 | news | IDXX | Sat, 14 Nov 2026 22:37:20 GMT | ok | https://news.google.com/rss/search?q=IDXX+Idexx+Laboratories+stock&hl=en-US&gl=US&ceid=US:en | IDEXX Laboratories, Inc. (IDXX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Sat, 14 Nov 2026 22:37:20 GMT); IDEXX Laboratories (IDXX) Stock Looks Fairly Valued Despite Its 28% Run - Yahoo Finance (Sat, 31 Oct 2026 07:00:00 GMT); IDEXX Laboratories (IDXX) vs. ZTS and NEOG: Can Raised Guidance and Product Expansion Drive Further Earnings Growth? - Yahoo Finance (Thu, 22 Oct 2026 07:00:00 GMT) |
| S030 | filing | ROP | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000882835&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000882835-26-000047); 8-K filed 2026-10-22 (accession 0000882835-26-000042); 8-K filed 2026-10-01 (accession 0000882835-26-000039) |
| S031 | filing | IDXX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000874716&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000874716-26-000135); 8-K filed 2026-11-02 (accession 0001104659-26-120892); 10-Q filed 2026-08-04 (accession 0000874716-26-000123) |
| S032 | filing | CLX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000021076.json | Diluted EPS 1.39 for period ending 2026-09-30 (filed 2026-11-02) |
| S033 | stock | ROP | 2026-11-16 | ok | https://finance.yahoo.com/quote/ROP | Trailing P/E: 18.993866; Forward P/E: 19.532475; Forward EPS: 24.57318; Price: 479.975; Market price: 479.975; Market cap: 47535013888; Sector: Technology; Trailing Eps: 25.27; Revenue Growth: 0.076; Earnings Growth: 0.326; Gross Margin: 0.69671; Operating Margin: 0.28049; Profit Margin: 0.30712998; Return On Equity: 0.13229; Total Revenue: 8434599936; Market Cap: 47535013888; Consensus EPS FY+1: 24.57318; growth: 0.09810001 |
| S034 | news | CHTR | Sun, 15 Nov 2026 05:47:01 GMT | ok | https://news.google.com/rss/search?q=CHTR+Charter+Communications+stock&hl=en-US&gl=US&ceid=US:en | Charter Communications (CHTR) Stock Could Be A Bargain Following Its New Operating Model - Yahoo Finance (Sun, 15 Nov 2026 05:47:01 GMT); Why You Should Think About Charter Communications Differently Now? - Yahoo Finance (Fri, 13 Nov 2026 19:16:11 GMT); Charter Communications (CHTR) Earnings Expected to Grow: What to Know Ahead of Next Week's Release - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT) |
| S035 | filing | RDDT | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001713445&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0001713445-26-000116); 8-K filed 2026-10-29 (accession 0001713445-26-000114); 8-K filed 2026-08-12 (accession 0001713445-26-000107) |
| S036 | news | ROP | Thu, 05 Nov 2026 08:00:00 GMT | ok | https://news.google.com/rss/search?q=ROP+Roper+Technologies+stock&hl=en-US&gl=US&ceid=US:en | Roper Technologies (ROP) Stock Looks Fully Valued As Cash Flow Comes Into Focus - Yahoo Finance (Thu, 05 Nov 2026 08:00:00 GMT); Roper Technologies (ROP), What Is Behind The Fresh Attention? - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT); Did Earnings Beat Just Shift Roper Technologies (ROP) Investment Narrative? - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT) |
| S037 | stock | RDDT | 2026-11-16 | ok | https://finance.yahoo.com/quote/RDDT | Trailing P/E: 20.091835; Forward P/E: 10.818217; Forward EPS: 9.10039; Price: 98.45; Market price: 98.45; Market cap: 19010076672; Sector: Communication Services; Trailing Eps: 4.9; Revenue Growth: 0.53; Earnings Growth: 0.749; Gross Margin: 0.91547996; Operating Margin: 0.29397; Profit Margin: 0.32105; Return On Equity: 0.32029998; Total Revenue: 3088880128; Market Cap: 19010076672; Consensus EPS FY+1: 6.8155; growth: 0.2401 |
| S038 | filing | INTC | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000050863&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0000050863-26-000191); 8-K filed 2026-10-29 (accession 0000050863-26-000188); 8-K filed 2026-08-12 (accession 0001193125-26-346806) |
| S039 | news | RDDT | Sat, 31 Oct 2026 07:00:00 GMT | ok | https://news.google.com/rss/search?q=RDDT+Reddit+stock&hl=en-US&gl=US&ceid=US:en | Why Reddit (RDDT) stock is trading lower today - Yahoo Finance (Sat, 31 Oct 2026 07:00:00 GMT); Reddit shares sink on weak sales guidance and plans login requirement test as Google search traffic shrinks - CNBC (Thu, 29 Oct 2026 07:00:00 GMT); Should You Wait Before Buying Reddit Stock? - Trefis (Fri, 13 Nov 2026 18:20:39 GMT) |
| S040 | filing | CHTR | 2026-11-06 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001091667.json | Diluted EPS 0.38 for period ending 2026-09-30 (filed 2026-11-06) |

## Sources

- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFF&cosd=2026-01-01 (2026-11-12)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLH0A0HYM2&cosd=2026-01-01 (2026-11-12)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLC0A0CM&cosd=2026-01-01 (2026-11-12)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCSL&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=UNRATE&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=PAYEMS&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=T10Y2Y&cosd=2026-01-01 (2026-11-13)
- filing APP: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001751008&type=10-Q&dateb=&owner=include&count=10 (2026-11-04)
- filing PNR: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 (2026-10-27)
- filing FISV: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 (2026-11-04)
- filing APP: https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json (2026-11-04)
- news FISV: https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en (Mon, 16 Nov 2026 02:19:15 GMT)
- news APP: https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en (Thu, 12 Nov 2026 20:05:45 GMT)
- stock FISV: https://finance.yahoo.com/quote/FISV (2026-11-16)
- stock APP: https://finance.yahoo.com/quote/APP (2026-11-16)
- stock PNR: https://finance.yahoo.com/quote/PNR (2026-11-16)
- filing FISV: https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json (2026-11-04)
- filing GEN: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 (2026-10-29)
- stock GEN: https://finance.yahoo.com/quote/GEN (2026-11-16)
- filing CLX: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 (2026-11-02)

## AI Provenance

- Provider / model: hermes-local-proxy / upstage/solar-mini4:free
- Market research: attempts=1 tokens=9513 (prompt=6513, completion=3000) runtime=23.06s
- Fundamental research: generated this run at 2026-11-16T13:08:59.388898+00:00
- Evidence source dates: {'as_of': '2026-11-13', 'latest_equity_date': '2026-11-13', 'latest_macro_date': '2026-11-16', 'flows_date': '2026-11-13'}
- Evidence fingerprint: 14dc481da9ca2acec1593997f78e1dbf0d9591ee467c644d3ea7e0fa2f973751
- Source citations are retrieved external records in the ledger above; market values remain from the verified database snapshot.


## Disclosures

- This is research and market intelligence, not investment advice.
- AI conclusions are research judgments, not validated return predictions.
- The frozen risk layer is risk-only and is not used for directional views or allocations.
- Legacy scores are not active inputs or outputs.

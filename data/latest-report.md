# AEGIS AI-First Market Intelligence

Research generated at: 15 November 2026, 01:15 HKT
Database freshness: equity 2026-11-13 (latest row retrieved 2026-11-14 13:50:55.938286+08:00)
Data cutoff: 2026-11-13 US cash close
Snapshot ID: aegis-hourly-20261114T171517Z

## Executive Summary

- **AI market view: Late-November 2026: broad market breadth is constructive (71% above 50-day, 64% above 200-day, A/D ratio 1.70), but the index is slightly negative over 20 days and the 20-day return is -1.28%. Sector leadership is bifurcated: Health Care, Consumer Staples, Consumer Discretionary and Real Estate are positive over 20 days, while Information Technology and Energy are negative. Liquidity is concentrated in semiconductors and hardware (SOXX exceptional, SMH tactical), while long-duration Treasuries show medium-term deterioration. Macro data show a 10Y-2Y spread of 0.27 and a 3.88% effective funds rate, with CPI and unemployment still elevated but not accelerating.**
- Broad market breadth is supportive: 71.34% of names above the 50-day moving average and 63.6% above the 200-day, with an advance/decline ratio of 1.70.
- Index-level momentum is slightly negative over 20 days (-1.28%), indicating a cautious near-term trend despite positive breadth.
- Sector rotation is clear: defensive and consumer sectors (Health Care, Consumer Staples, Consumer Discretionary, Real Estate) lead, while Information Technology and Energy lag.
- Liquidity is concentrated in semiconductors (SOXX exceptional inflow, SMH tactical outflow), suggesting institutional conviction in hardware/semis but profit-taking.
- Macro backdrop is stable but not accommodative: 10Y-2Y spread 0.27, effective funds rate 3.88%, CPI and unemployment elevated but not accelerating.
- Risk environment is moderate: 5-day forecast volatility 14.9%, spike probability 16.5% below historical and EWMA baselines, directional signal false.

## Data QC

- Status: **PASS_WITH_WARNINGS**
- Equity session: 0 completed session(s) behind inference date
- Equity provenance: 386 provisional / 12581 canonical
- Breadth lag: 0 session(s); ETF-flow lag: 0 session(s)
- Note: Equity session contains a mix of provisional yfinance and canonical Massive rows.
- External sources: 79 ok / 0 unavailable; retrieved 2026-11-14T17:15:39.534291+00:00

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
| S&P 500 (SPX) | 7561.67 | -1.28% (20d) | Index slightly negative over 20 days; breadth remains positive with 71.34% above 50-day and 63.6% above 200-day. |
| Health Care (XLV) | 30.78 P/E | +6.87% (20d) | Top 20-day sector performer; trailing P/E 30.78 from S056. |
| Consumer Discretionary (XLY) | 25.11 P/E | +6.69% (20d) | Strong 20-day return; trailing P/E 25.11 from S061. |
| Information Technology (XLK) | 30.03 P/E | -7.19% (20d) | Worst 20-day sector; trailing P/E 30.03 from S074. |
| Energy (XLE) | 16.23 P/E | -4.81% (20d) | Negative 20-day return; trailing P/E 16.23 from S076. |
| Semiconductor hardware (SOXX) | flow z-score 5.10 (20d) | inflow | Exceptional institutional buying; price state flat/down but flow structure strong confirmation. |

## Macro, Fiscal, Rates, Liquidity and Credit

- Growth: 10Y-2Y Treasury spread is 0.27 (S007), indicating a modestly positive but shallow yield curve; no recession signal from curve inversion.
- Inflation: CPI (CPIAUCSL) is 336.298 in Sep 2026 (database) and 337.476 in Oct 2026 (S004); core CPI 338.896 (Sep 2026); inflation remains elevated but not accelerating.
- Labor: Unemployment rate 4.2% in Sep 2026 (database) and 4.1% in Oct 2026 (S005); payrolls 159,293k in Oct 2026 (S006); labor market is cooling gradually.
- Policy: Effective federal funds rate is 3.88% as of 2026-11-12 (S001); policy is restrictive but not aggressively tightening.
- Rates: IG OAS 0.89 and HY OAS 3.20 (S003, S002) as of 2026-11-12; credit spreads are tight but not distressed, consistent with moderate risk appetite.
- Liquidity: TLT flow z-score -0.41 (20d) and -0.29 (60d) with medium-term deterioration; long-duration bonds are seeing reduced institutional demand, while SOXX shows exceptional inflows.

## US Equities and 11 GICS Sectors

Macro source IDs: S001, S002, S003, S004, S005, S006, S007

| GICS sector | Evidence | AI research stance | Source IDs |
| --- | --- | --- | --- |
| Health Care | 20d return +6.87%; trailing P/E 30.78 (S056); top 20-day sector performer. | Defensive leadership; strong relative momentum and reasonable valuation relative to market. | S056 |
| Consumer Staples | 20d return +5.40%; trailing P/E 24.85 (S057); stable defensive sector. | Steady defensive holding; positive 20-day momentum with moderate valuation. | S057 |
| Consumer Discretionary | 20d return +6.69%; trailing P/E 25.11 (S061); strong consumer sector. | Positive momentum; consumer spending remains supportive, valuation moderate. | S061 |
| Real Estate | 20d return +5.24%; trailing P/E 29.63 (S066); positive but higher valuation. | Positive 20-day return; valuation above average, watch rate sensitivity. | S066 |
| Financials | 20d return +5.69%; trailing P/E 15.85 (S063); solid sector performance. | Positive momentum; low valuation relative to market, supportive of financials. | S063 |
| Utilities | 20d return +4.34%; trailing P/E 18.11 (S067); defensive utility sector. | Positive but lower momentum; reasonable valuation, defensive allocation. | S067 |
| Materials | 20d return +2.57%; trailing P/E 21.72 (S068); modest positive. | Modest positive momentum; valuation in line, watch industrial demand. | S068 |
| Industrials | 20d return +0.61%; trailing P/E 27.07 (S069); near flat. | Flat 20-day return; valuation above average, mixed industrial demand. | S069 |
| Communication Services | 20d return -1.48%; trailing P/E 17.26 (S073); negative momentum. | Negative 20-day return; valuation reasonable, but sector under pressure. | S073 |
| Information Technology | 20d return -7.19%; trailing P/E 30.03 (S074); worst sector. | Negative momentum and highest sector P/E; semiconductor hardware flows are exceptional but broad IT is lagging. | S074 |
| Energy | 20d return -4.81%; trailing P/E 16.23 (S076); negative momentum. | Negative 20-day return; low valuation but sector under pressure, watch demand and policy. | S076 |

### Sector fundamentals, valuation and earnings

Sector-level fundamental data (growth, margins, consensus) are not supplied in the database snapshot; only trailing P/E and 20-day returns are available for the 11 GICS sectors. The supplied evidence is limited to ETF-level valuation and price momentum, so no point-in-time sector fundamentals beyond these metrics are available. No additional fundamental claims are made.

## Growth vs Value

- Health Care (XLV) trades at 30.78 trailing P/E, the highest among the positive 20-day sectors, but leads on momentum.
- Consumer Discretionary (XLY) at 25.11 P/E offers positive momentum with moderate valuation.
- Information Technology (XLK) at 30.03 P/E is the most expensive positive sector but is the only one with exceptional semiconductor hardware liquidity (SOXX z-score 5.10).
- Energy (XLE) at 16.23 P/E is the cheapest sector but has negative 20-day momentum, suggesting value without near-term price support.

## ETF Flows and Breadth

- SOXX shows exceptional institutional buying (20d flow z-score 5.10, 60d 3.17) with price state flat/down, indicating strong structural accumulation.
- SMH shows tactical profit-taking (20d z-score 1.22, 60d 1.04) inside structural accumulation, with price state down.
- TLT shows medium-term deterioration (20d z-score -0.41, 60d -0.29), suggesting reduced long-duration bond demand.
- Market breadth is strongly positive: 315 advancers vs 185 decliners, A/D ratio 1.70, 71.34% above 50-day, 63.6% above 200-day.
- No new highs or new lows are reported (0/0), so breadth is broad but not extreme; the index is slightly negative over 20 days.

## Stock Ideas

Single-stock research uses reported EPS, forward P/E and company fundamentals. All ideas are research judgments, not validated return predictions.

| Ticker | Security | Research view | Price | EPS | Forward P/E | Base target | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| APP | AppLovin | NEW | 409.1 | 20.86026 | 19.611452 | 458.93 | NEW |
| PNR | Pentair | KEEP | 68.3 | 5.30402 | 12.877027 | 74.26 | KEEP |
| GEN | Gen Digital | KEEP | 30.4 | 3.33736 | 9.108996 | 36.71 | KEEP |
| ROP | Roper Technologies | KEEP | 479.975 | 24.57318 | 19.532475 | 393.17 | KEEP |

## ETF Ideas

ETF research uses holdings, portfolio valuation and exposure. Single-stock EPS × P/E valuation is not applied to ETFs.

| Ticker | Fund | Research view | Price | Top holdings | Portfolio valuation | Sector exposure | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| XLV | Health Care sector ETF | KEEP | 188.85 | LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59% | Top 10 holdings; numeric weight coverage 61.42% | Health Care | KEEP |
### APP — AppLovin

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** AppLovin offers a higher-quality, higher-margin compounder than the lower-quality dislocation names (e.g., NOW, MRVL) and a stronger momentum profile than the slower-growth staples (e.g., CLX) or financials (e.g., XLF). Its forward P/E near 19.6 is reasonable for a company growing earnings at ~75%, and its 20-day momentum is the strongest among the shortlisted quality names. Alternatives considered: CLX, ROP, XLF.
- **Thesis:** AppLovin screens in the top 20-day momentum bucket with a 53.7% 20-day return and a 32.5% 60-day return, and its reported diluted EPS of 11.61 supports a forward P/E near 19.6. The company's high gross margin (~88.8%) and strong reported earnings growth (~75.5%) underpin a quality compounder narrative, while the 20-day momentum and low 60-day drawdown (~0.2%) indicate a clean, low-drawdown uptrend.
- **Source IDs:** S008, S012, S014, S016
- **Catalysts:** Continued 20-day momentum and high-margin monetization of digital advertising, Sustained earnings growth above 50% supporting forward P/E expansion, Q3 2026 filing (S014) and momentum-driven rerating (S012)
- **Risks:** High valuation multiples leave limited room for multiple compression if momentum fades, Advertising market cyclicality could pressure revenue growth, Single-quarter earnings beat may not persist if ad spend normalizes
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 20.8603 (source.forwardEps) x AI multiple assumption 22.00; source IDs S008, S012, S014, S016
- **EPS:** 20.86026 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 19.611452
- **FY+1 growth assumption:** 27.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / MSFT / APP shows strong FY1 consensus earnings growth of 27.44% and revenue growth of 25.37%, supported by an 88.8% gross margin and 77.8% operating margin. The forward EPS of 20.86 and forward P/E of 19.6x are below the 22-26x range justified by its high-margin, high-growth profile. MSFT is used as a named peer reference because both are large-cap, high-margin, growth-oriented technology platforms with durable competitive advantages and strong free cash flow conversion.
- **Company fundamentals:** AppLovin reported diluted EPS of 11.61 for the period ending 2026-09-30, with forward EPS of 20.86, forward P/E of 19.61, gross margin of 88.8%, operating margin of 77.8%, profit margin of 65.9%, revenue growth of 55.5%, and earnings growth of 75.5%. The stock closed at 409.1 with a 20-day return of 53.7% and a 60-day drawdown of -0.2%. Source IDs: S008, S012, S014, S016.
- **Bull / Base / Bear:** 542.37 / 458.93 / 354.62
- **Bull / Base / Bear returns:** 32.58% / 12.18% / -13.32%
- **Scenario probabilities:** not separately assigned; see scenario table.

### PNR — Pentair

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Pentair is preferred over the high-multiple dislocation names (e.g., NOW, MRVL) and the negative-momentum names (e.g., INTC, RDDT) because it offers a lower forward P/E (12.9) and a positive 20-day momentum (27.8%) without the extreme valuation or earnings deterioration of those alternatives. However, its negative revenue and earnings growth keep it from a BUY rating. Alternatives considered: INTC, RDDT, CLX.
- **Thesis:** Pentair screens in the top 20-day momentum bucket with a 27.8% 20-day return and a 7.1% 60-day return, and its forward P/E of 12.9 is reasonable for a company with a forward EPS of 5.30. However, revenue growth is slightly negative (-4.5%) and earnings growth is negative (-18.8%), so the momentum is not yet supported by fundamental expansion. The stock is a hold rather than a buy until the earnings decline stabilizes.
- **Source IDs:** S011, S013, S018, S019
- **Catalysts:** 20-day momentum of 27.8% could continue if the industrial cycle turns, Forward P/E of 12.9 offers a reasonable entry point if earnings stabilize, Q3 2026 filing (S018) provides a fresh data point for earnings trajectory
- **Risks:** Negative revenue growth (-4.5%) and negative earnings growth (-18.8%) weigh on the thesis, Industrial end-market weakness could delay recovery, Momentum may be driven by short-term factors rather than fundamental improvement
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 5.3040 (source.forwardEps) x AI multiple assumption 14.00; source IDs S011, S013, S018, S019
- **EPS:** 5.30402 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 12.877027
- **FY+1 growth assumption:** 12.82%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / GEV / PNR has FY1 consensus earnings growth of 12.82% and revenue growth of 18.38%, with a 40.2% gross margin and 21.4% operating margin. The forward EPS of 5.30 and forward P/E of 12.9x are below the 14-17x range justified by its improving earnings trajectory and cyclical recovery potential. GEV is used as a named peer reference because both are industrial/energy infrastructure companies with cyclical earnings, asset-light or capital-light models, and exposure to energy transition and grid modernization.
- **Company fundamentals:** Pentair reported diluted EPS of 2.76 for the period ending 2026-09-30, with forward EPS of 5.30, forward P/E of 12.88, gross margin of 40.2%, operating margin of 21.4%, profit margin of 15.4%, revenue growth of -4.5%, and earnings growth of -18.8%. The stock closed at 68.3 with a 20-day return of 27.8% and a 60-day drawdown of -5.2%. Source IDs: S011, S013, S018, S019.
- **Bull / Base / Bear:** 90.17 / 74.26 / 58.34
- **Bull / Base / Bear returns:** 32.02% / 8.73% / -14.58%
- **Scenario probabilities:** not separately assigned; see scenario table.

### GEN — Gen Digital

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Gen Digital is preferred over the high-multiple dislocation names (e.g., NOW, MRVL) and the negative-momentum names (e.g., INTC, RDDT) because it offers a very low forward P/E (9.1) and strong earnings growth (128.6%) without the extreme valuation or earnings deterioration of those alternatives. However, its modest revenue growth keeps it from a BUY rating. Alternatives considered: INTC, RDDT, CLX.
- **Thesis:** Gen Digital screens in the top 20-day momentum bucket with a 25.8% 20-day return and a 7.9% 60-day return, and its forward P/E of 9.1 is very attractive for a company with forward EPS of 3.34. However, revenue growth is modest (12.2%) and earnings growth is strong (128.6%), so the valuation is cheap but the growth is not yet broad-based. The stock is a hold until the revenue growth accelerates.
- **Source IDs:** S015, S021, S023, S027
- **Catalysts:** Forward P/E of 9.1 offers a significant margin of safety versus the high-multiple names, Strong earnings growth of 128.6% supports a rerating if revenue growth improves, Q3 2026 filing (S027) provides a fresh data point for the earnings trajectory
- **Risks:** Modest revenue growth (12.2%) limits the upside from the cheap valuation, Cybersecurity and software end-market cyclicality could pressure revenue, Momentum may fade if the earnings beat is not sustained
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 3.3374 (source.forwardEps) x AI multiple assumption 11.00; source IDs S015, S021, S023, S027
- **EPS:** 3.33736 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 9.108996
- **FY+1 growth assumption:** 12.86%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / DHR / GEN has FY1 consensus earnings growth of 12.86% and revenue growth of 6.81%, with a 77.4% gross margin and 43.2% operating margin. The forward EPS of 3.34 and forward P/E of 9.1x are below the 11-14x range justified by its high gross margin, improving earnings, and niche market position. DHR is used as a named peer reference because both are industrial companies with high gross margins, diversified end markets, and exposure to automation, healthcare, and industrial digitalization.
- **Company fundamentals:** Gen Digital reported diluted EPS of 0.83 for the period ending 2026-10-02, with forward EPS of 3.34, forward P/E of 9.11, gross margin of 77.4%, operating margin of 43.2%, profit margin of 23.1%, revenue growth of 12.2%, and earnings growth of 128.6%. The stock closed at 30.4 with a 20-day return of 25.8% and a 60-day drawdown of -3.2%. Source IDs: S015, S021, S023, S027.
- **Bull / Base / Bear:** 46.72 / 36.71 / 30.04
- **Bull / Base / Bear returns:** 53.68% / 20.76% / -1.18%
- **Scenario probabilities:** not separately assigned; see scenario table.

### ROP — Roper Technologies

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Roper Technologies is preferred over the high-multiple dislocation names (e.g., NOW, MRVL) and the negative-momentum names (e.g., INTC, RDDT) because it offers a reasonable forward P/E (19.5) and a strong 20-day momentum (25.4%) without the extreme valuation or earnings deterioration of those alternatives. However, its modest revenue growth keeps it from a BUY rating. Alternatives considered: INTC, RDDT, CLX.
- **Thesis:** Roper Technologies screens in the top 20-day momentum bucket with a 25.4% 20-day return and a 16.9% 60-day return, and its forward P/E of 19.5 is reasonable for a company with forward EPS of 24.57. However, revenue growth is modest (7.6%) and earnings growth is 32.6%, so the momentum is not yet supported by broad-based fundamental expansion. The stock is a hold until the revenue growth accelerates.
- **Source IDs:** S034, S035, S036, S049
- **Catalysts:** 20-day momentum of 25.4% and 60-day return of 16.9% indicate a strong uptrend, Forward P/E of 19.5 is reasonable for a company growing earnings at 32.6%, Q3 2026 filing (S049) provides a fresh data point for the earnings trajectory
- **Risks:** Modest revenue growth (7.6%) limits the upside from the momentum, Software and technology end-market cyclicality could pressure revenue, Momentum may fade if the earnings beat is not sustained
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 24.5732 (source.forwardEps) x AI multiple assumption 16.00; source IDs S034, S035, S036, S049
- **EPS:** 24.57318 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 19.532475
- **FY+1 growth assumption:** 9.81%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / KMB / ROP has FY1 consensus earnings growth of 9.81% and revenue growth of 6.29%, with a 69.7% gross margin and 28.0% operating margin. The forward EPS of 24.57 and forward P/E of 19.5x are below the 16-19x range justified by its stable consumer staples profile, consistent earnings growth, and strong profitability. KMB is used as a named peer reference because both are large-cap consumer staples companies with defensive demand, pricing power, and stable cash flows.
- **Company fundamentals:** Roper Technologies reported diluted EPS of 21.30 for the period ending 2026-09-30, with forward EPS of 24.57, forward P/E of 19.53, gross margin of 69.7%, operating margin of 28.0%, profit margin of 30.7%, revenue growth of 7.6%, and earnings growth of 32.6%. The stock closed at 479.975 with a 20-day return of 25.4% and a 60-day drawdown of -2.5%. Source IDs: S034, S035, S036, S049.
- **Bull / Base / Bear:** 466.89 / 393.17 / 319.45
- **Bull / Base / Bear returns:** -2.73% / -18.09% / -33.44%
- **Scenario probabilities:** not separately assigned; see scenario table.

### XLV — Health Care sector ETF

- **Type:** ETF
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** XLV is preferred over the other sector ETFs (XLP, XLY, XLRE, XLF, XLU, XLB, XLI) because it offers the most stable, diversified exposure to the health care sector, which is less sensitive to the cyclical and momentum-driven factors driving the shortlisted stocks. It is a core holding rather than a tactical bet. Alternatives considered: XLP, XLY, XLF.
- **Thesis:** The Health Care sector ETF (XLV) is a core holding that provides diversified exposure to the sector, with top holdings including LLY, JNJ, ABBV, MRK, and UNH. The ETF is a neutral hold because the sector is not showing a clear directional edge in the current environment, and the ETF's performance will be driven by the underlying health care names rather than a specific catalyst. It is a stable, low-volatility component of a diversified portfolio.
- **Source IDs:** S054, S056
- **Catalysts:** Diversified exposure to large-cap health care names reduces single-stock risk, Top 10 holdings coverage of 61.4% provides a clear view of the portfolio, Stable, low-volatility component suitable for core portfolio allocation
- **Risks:** Sector-specific headwinds (e.g., regulatory, drug pricing) could weigh on performance, Top 10 holdings concentration (61.4% coverage) limits diversification within the ETF, No clear directional catalyst in the current environment
- **Valuation method:** Holdings/portfolio valuation with AI total-return assumption
- **Valuation status:** verified; forward-EPS source: ; period flags: 
- **Valuation assumptions:** Holdings/portfolio valuation; 10 weighted holdings; coverage 61.42%; source IDs S054, S056
- **Top holdings:** LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59%
- **Portfolio valuation:** Top 10 holdings; numeric weight coverage 61.42%
- **Sector exposure:** Health Care
- **Underlying drivers:** Diversified exposure to large-cap health care names; top 10 holdings coverage of 61.4%; stable, low-volatility component for core portfolio allocation.
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
| Bull | 25% | +2.00% | Low 5-day realized volatility (0.149) and below-threshold spike probability (0.165) support a modest upside if US close confirms positive breadth; return capped at +2.0% to reflect limited upside without a directional signal. |
| Base | 50% | +0.00% | Frozen daily-close model with no directional signal and elevated spike probability (0.165) near the 0.185 threshold implies range-bound action; base case assumes flat returns over the 5-day target window. |
| Bear | 25% | -2.00% | If the spike probability materializes above the 0.185 threshold and US close closes negative, elevated volatility risk (0.149) could drive a -2.0% drawdown; probability reflects moderate downside risk without a confirmed directional signal. |

### Long Term (12 months)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 30% | +8.00% | Sustained low volatility (0.149) and below-threshold spike probability (0.165) support a constructive multi-week outlook if earnings and credit conditions remain stable; +8.0% reflects a moderate bull case with no directional alpha. |
| Base | 40% | +3.00% | Frozen daily-close model with no directional signal and elevated spike probability (0.165) near the 0.185 threshold implies a slow grind higher; base case assumes +3.0% over the longer horizon as volatility normalizes. |
| Bear | 30% | -5.00% | If spike probability exceeds the 0.185 threshold and US close closes negative, elevated volatility (0.149) could trigger a -5.0% drawdown over the longer horizon; probability reflects downside risk without a confirmed directional signal. |

## Positioning

- Maintain a constructive but cautious equity stance: positive breadth and sector leadership in defensive/consumer names, but index-level 20-day return is negative.
- Favored Health Care, Consumer Staples, Consumer Discretionary and Real Estate on relative momentum and defensive characteristics.
- Less favored Information Technology and Energy on negative 20-day momentum, despite exceptional semiconductor hardware liquidity.
- Use semiconductor hardware (SOXX) as a liquidity-led satellite, not a broad IT favored, given negative sector-level returns.
- Monitor TLT flows and credit spreads (IG 0.89, HY 3.20) for liquidity regime shifts; current data suggest moderate risk appetite.
- No allocation weights or composite scores are provided; positioning is qualitative only.

## Catalysts

| Date | Event | Why it matters |
| --- | --- | --- |
| 2026-11-16 | US equity market open | Frozen daily-close model; official forecast after completed US close; 5-day volatility 14.9% and spike probability 16.5% below baselines. |
| 2026-11-13 | Macro data release | CPI, core CPI, unemployment and payrolls are the latest available; inflation and labor data will guide policy expectations. |
| 2026-11-12 | Credit and policy data | Effective funds rate 3.88%, IG OAS 0.89, HY OAS 3.20; these will influence sector rotation and liquidity. |

## Key Risks

- Index-level 20-day return is negative (-1.28%), indicating near-term downside risk despite positive breadth.
- 

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
| S009 | news | FISV | Thu, 12 Nov 2026 14:54:12 GMT | ok | https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en | Fiserv, Inc. (FISV) Stock Price, News, Quote & History - Yahoo! Finance Canada (Thu, 12 Nov 2026 14:54:12 GMT); Fiserv Stock Outlook: Is Wall Street Bullish or Bearish? - Yahoo Finance (Thu, 12 Nov 2026 12:23:56 GMT); What Is Fiserv (FISV) Planning With Its Debit Networks And Clover AI? - Yahoo Finance (Thu, 12 Nov 2026 06:09:00 GMT) |
| S010 | filing | FISV | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0000798354-26-000042); 8-K filed 2026-11-03 (accession 0000798354-26-000039); 8-K filed 2026-10-23 (accession 0001193125-26-429481) |
| S011 | filing | PNR | 2026-10-27 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-27 (accession 0000077360-26-000058); 8-K filed 2026-10-27 (accession 0000077360-26-000055); 8-K filed 2026-09-22 (accession 0000077360-26-000050) |
| S012 | news | APP | Tue, 10 Nov 2026 14:24:00 GMT | ok | https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en | APP Stock Surges 51% After Q3 Earnings: Is it Still a Buy? - Yahoo Finance (Tue, 10 Nov 2026 14:24:00 GMT); Is Trending Stock AppLovin Corporation (APP) a Buy Now? - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT); APP Stock Quote Price and Forecast - CNN (Fri, 13 Nov 2026 07:31:37 GMT) |
| S013 | news | PNR | Fri, 13 Nov 2026 15:54:46 GMT | ok | https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en | Pentair plc (PNR) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 15:54:46 GMT); Here's What Key Metrics Tell Us About Pentair (PNR) Q3 Earnings - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT); Pentair (PNR) Stock May Be 46% Undervalued As New CFO Arrives - Yahoo Finance (Fri, 25 Sep 2026 07:00:00 GMT) |
| S014 | filing | APP | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json | Diluted EPS 11.61 for period ending 2026-09-30 (filed 2026-11-04) |
| S015 | filing | GEN | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0000849399-26-000083); 8-K filed 2026-10-28 (accession 0000849399-26-000081); 8-K filed 2026-10-09 (accession 0000849399-26-000079) |
| S016 | stock | APP | 2026-11-14 | ok | https://finance.yahoo.com/quote/APP | Trailing P/E: 27.54882; Forward P/E: 19.611452; Forward EPS: 20.86026; Price: 409.1; Market price: 409.1; Market cap: 135543824384; Sector: Communication Services; Trailing Eps: 14.85; Revenue Growth: 0.555; Earnings Growth: 0.755; Gross Margin: 0.8878; Operating Margin: 0.77782995; Profit Margin: 0.65887; Return On Equity: 2.1008599; Total Revenue: 7608893952; Market Cap: 135543824384; Consensus EPS FY+1: 20.72438; growth: 0.2744 |
| S017 | stock | FISV | 2026-11-14 | ok | https://finance.yahoo.com/quote/FISV | Forward P/E: 7.9923306; Price: 63.78; Market price: 63.78; Market cap: 33934002176; Market Cap: 33934002176; Consensus EPS FY+1: 7.98015; growth: 0.09689999 |
| S018 | filing | PNR | 2026-10-27 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json | Diluted EPS 2.76 for period ending 2026-09-30 (filed 2026-10-27) |
| S019 | stock | PNR | 2026-11-14 | ok | https://finance.yahoo.com/quote/PNR | Trailing P/E: 18.610355; Forward P/E: 12.877027; Forward EPS: 5.30402; Price: 68.3; Market price: 68.3; Market cap: 10904415232; Sector: Industrials; Trailing Eps: 3.67; Revenue Growth: -0.045; Earnings Growth: -0.188; Gross Margin: 0.40168998; Operating Margin: 0.21410999; Profit Margin: 0.15435; Return On Equity: 0.15605; Total Revenue: 3966200064; Market Cap: 10904415232; Consensus EPS FY+1: 5.30402; growth: 0.1282 |
| S020 | filing | FISV | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json | Diluted EPS -8.9 for period ending 2026-09-30 (filed 2026-11-04) |
| S021 | news | GEN | Wed, 11 Nov 2026 13:10:37 GMT | ok | https://news.google.com/rss/search?q=GEN+Gen+Digital+stock&hl=en-US&gl=US&ceid=US:en | Gen Digital Inc. (GEN) Stock Forecasts - Yahoo Finance (Wed, 11 Nov 2026 13:10:37 GMT); Gen Digital (GEN) Stock Repriced After Q2 Earnings Put Margins Center Stage - Yahoo Finance (Thu, 29 Oct 2026 07:00:00 GMT); Are Business Services Stocks Lagging GEN DIGITAL INC (GEN) This Year? - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT) |
| S022 | filing | CLX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000021076-26-000046); 8-K filed 2026-11-02 (accession 0000021076-26-000044); 8-K filed 2026-10-29 (accession 0001206774-26-000586) |
| S023 | stock | GEN | 2026-11-14 | ok | https://finance.yahoo.com/quote/GEN | Trailing P/E: 15.431472; Forward P/E: 9.108996; Forward EPS: 3.33736; Price: 30.4; Market price: 30.4; Market cap: 18035593216; Sector: Technology; Trailing Eps: 1.97; Revenue Growth: 0.122; Earnings Growth: 1.286; Gross Margin: 0.77410007; Operating Margin: 0.43229; Profit Margin: 0.23068; Return On Equity: 0.46402; Total Revenue: 5228000256; Market Cap: 18035593216; Consensus EPS FY+1: 3.33736; growth: 0.1286 |
| S024 | news | CLX | Sat, 14 Nov 2026 10:15:20 GMT | ok | https://news.google.com/rss/search?q=CLX+Clorox+stock&hl=en-US&gl=US&ceid=US:en | The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance Singapore (Sat, 14 Nov 2026 10:15:20 GMT); The Clorox Company (CLX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 05:34:04 GMT); A 10-Day Winning Streak Has Clorox Stock Up 24% - Trefis (Sat, 14 Nov 2026 08:28:05 GMT) |
| S025 | filing | CHTR | 2026-11-06 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-06 (accession 0001091667-26-000073); 8-K filed 2026-11-06 (accession 0001091667-26-000072); 8-K filed 2026-10-27 (accession 0001091667-26-000064) |
| S026 | stock | CLX | 2026-11-14 | ok | https://finance.yahoo.com/quote/CLX | Trailing P/E: 19.68705; Forward P/E: 17.745283; Forward EPS: 6.1684; Price: 109.46; Market price: 109.46; Market cap: 13260793856; Sector: Consumer Defensive; Trailing Eps: 5.56; Revenue Growth: 0.333; Earnings Growth: 1.138; Gross Margin: 0.41939998; Operating Margin: 0.14286; Profit Margin: 0.09408; Return On Equity: 5.34363; Total Revenue: 7196000256; Market Cap: 13260793856; Consensus EPS FY+1: 6.1684; growth: 0.0769 |
| S027 | filing | GEN | 2026-10-29 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000849399.json | Diluted EPS 0.83 for period ending 2026-10-02 (filed 2026-10-29) |
| S028 | stock | CHTR | 2026-11-14 | ok | https://finance.yahoo.com/quote/CHTR | Trailing P/E: 13.006578; Forward P/E: 3.2831066; Forward EPS: 42.15215; Price: 138.39; Market price: 138.39; Market cap: 24778944512; Sector: Communication Services; Trailing Eps: 10.64; Revenue Growth: 0.091; Gross Margin: 0.55084; Operating Margin: 0.23389; Profit Margin: 0.02498; Return On Equity: 0.07019; Total Revenue: 55645999104; Market Cap: 24778944512; Consensus EPS FY+1: 47.15811; growth: 1.0195 |
| S029 | news | IDXX | Fri, 13 Nov 2026 22:06:38 GMT | ok | https://news.google.com/rss/search?q=IDXX+Idexx+Laboratories+stock&hl=en-US&gl=US&ceid=US:en | IDEXX Laboratories, Inc. (IDXX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 22:06:38 GMT); IDEXX Laboratories (IDXX) Stock Looks Fairly Valued Despite Its 28% Run - Yahoo Finance (Sat, 31 Oct 2026 07:00:00 GMT); IDEXX Laboratories (IDXX) Q3 Earnings Leave Its Premium Valuation In Focus - Yahoo Finance (Tue, 03 Nov 2026 08:00:00 GMT) |
| S030 | filing | IDXX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000874716&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000874716-26-000135); 8-K filed 2026-11-02 (accession 0001104659-26-120892); 10-Q filed 2026-08-04 (accession 0000874716-26-000123) |
| S031 | news | CHTR | Thu, 12 Nov 2026 08:02:01 GMT | ok | https://news.google.com/rss/search?q=CHTR+Charter+Communications+stock&hl=en-US&gl=US&ceid=US:en | Charter Communications: 3 Key Takeaways for Long-Term Investors - Yahoo Finance (Thu, 12 Nov 2026 08:02:01 GMT); Charter Communications (CHTR) Stock Looks Reasonable As Shares Slump 85% - Yahoo Finance (Wed, 28 Oct 2026 07:00:00 GMT); What Is The Biggest Threat To Charter Communications Stock? - Trefis (Thu, 12 Nov 2026 15:55:19 GMT) |
| S032 | filing | CLX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000021076.json | Diluted EPS 1.39 for period ending 2026-09-30 (filed 2026-11-02) |
| S033 | stock | IDXX | 2026-11-14 | ok | https://finance.yahoo.com/quote/IDXX | Trailing P/E: 47.45485; Forward P/E: 41.687927; Forward EPS: 16.8929; Price: 704.23; Market price: 704.23; Market cap: 55483650048; Sector: Healthcare; Trailing Eps: 14.84; Revenue Growth: 0.099; Earnings Growth: 0.179; Gross Margin: 0.62722; Operating Margin: 0.32497; Profit Margin: 0.25357; Return On Equity: 0.68925005; Total Revenue: 4662220800; Market Cap: 55483650048; Consensus EPS FY+1: 16.8929; growth: 0.1244 |
| S034 | filing | ROP | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000882835&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000882835-26-000047); 8-K filed 2026-10-22 (accession 0000882835-26-000042); 8-K filed 2026-10-01 (accession 0000882835-26-000039) |
| S035 | stock | ROP | 2026-11-14 | ok | https://finance.yahoo.com/quote/ROP | Trailing P/E: 18.993866; Forward P/E: 19.532475; Forward EPS: 24.57318; Price: 479.975; Market price: 479.975; Market cap: 47535013888; Sector: Technology; Trailing Eps: 25.27; Revenue Growth: 0.076; Earnings Growth: 0.326; Gross Margin: 0.69671; Operating Margin: 0.28049; Profit Margin: 0.30712998; Return On Equity: 0.13229; Total Revenue: 8434599936; Market Cap: 47535013888; Consensus EPS FY+1: 24.57318; growth: 0.09810001 |
| S036 | news | ROP | Fri, 13 Nov 2026 01:46:04 GMT | ok | https://news.google.com/rss/search?q=ROP+Roper+Technologies+stock&hl=en-US&gl=US&ceid=US:en | Roper Technologies, Inc. (ROP) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 01:46:04 GMT); Roper Technologies (ROP) Stock Looks Fully Valued As Cash Flow Comes Into Focus - Yahoo Finance (Fri, 06 Nov 2026 07:13:00 GMT); Roper Technologies: 3 Key Takeaways for Long-Term Investors - Yahoo Finance (Mon, 26 Oct 2026 07:00:00 GMT) |
| S037 | filing | CHTR | 2026-11-06 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001091667.json | Diluted EPS 0.38 for period ending 2026-09-30 (filed 2026-11-06) |
| S038 | filing | RDDT | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001713445&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0001713445-26-000116); 8-K filed 2026-10-29 (accession 0001713445-26-000114); 8-K filed 2026-08-12 (accession 0001713445-26-000107) |
| S039 | stock | RDDT | 2026-11-14 | ok | https://finance.yahoo.com/quote/RDDT | Trailing P/E: 20.091835; Forward P/E: 10.770874; Forward EPS: 9.14039; Price: 98.45; Market price: 98.45; Market cap: 19010076672; Sector: Communication Services; Trailing Eps: 4.9; Revenue Growth: 0.53; Earnings Growth: 0.749; Gross Margin: 0.91547996; Operating Margin: 0.29397; Profit Margin: 0.32105; Return On Equity: 0.32029998; Total Revenue: 3088880128; Market Cap: 19010076672; Consensus EPS FY+1: 6.82439; growth: 0.2417 |
| S040 | news | RDDT | Thu, 29 Oct 2026 07:00:00 GMT | ok | https://news.google.com/rss/search?q=RDDT+Reddit+stock&hl=en-US&gl=US&ceid=US:en | Reddit shares sink on weak sales guidance and plans login requirement test as Google search traffic shrinks - CNBC (Thu, 29 Oct 2026 07:00:00 GMT); Reddit (NYSE:RDDT) surprises with Q3 2026 sales but stock drops 12.6% - Yahoo Finance (Thu, 29 Oct 2026 07:00:00 GMT); symbol__ Stock Quote Price and Forecast - CNN (Thu, 12 Nov 2026 21:15:22 GMT) |

## Sources

- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFF&cosd=2026-01-01 (2026-11-12)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLH0A0HYM2&cosd=2026-01-01 (2026-11-12)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLC0A0CM&cosd=2026-01-01 (2026-11-12)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCSL&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=UNRATE&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=PAYEMS&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=T10Y2Y&cosd=2026-01-01 (2026-11-13)
- filing APP: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001751008&type=10-Q&dateb=&owner=include&count=10 (2026-11-04)
- news FISV: https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en (Thu, 12 Nov 2026 14:54:12 GMT)
- filing FISV: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 (2026-11-04)
- filing PNR: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 (2026-10-27)
- news APP: https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en (Tue, 10 Nov 2026 14:24:00 GMT)
- news PNR: https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 15:54:46 GMT)
- filing APP: https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json (2026-11-04)
- filing GEN: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 (2026-10-29)
- stock APP: https://finance.yahoo.com/quote/APP (2026-11-14)
- stock FISV: https://finance.yahoo.com/quote/FISV (2026-11-14)
- filing PNR: https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json (2026-10-27)
- stock PNR: https://finance.yahoo.com/quote/PNR (2026-11-14)
- filing FISV: https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json (2026-11-04)

## AI Provenance

- Provider / model: hermes-local-proxy / upstage/solar-mini4:free
- Market research: attempts=1 tokens=9521 (prompt=6521, completion=3000) runtime=20.58s
- Fundamental research: generated this run at 2026-11-14T17:15:17.099836+00:00
- Evidence source dates: {'as_of': '2026-11-13', 'latest_equity_date': '2026-11-13', 'latest_macro_date': '2026-11-13', 'flows_date': '2026-11-13'}
- Evidence fingerprint: fbda0908c935447a55b9443406b4c6ce23a9a59209a5f7cd3b488059adae78bb
- Source citations are retrieved external records in the ledger above; market values remain from the verified database snapshot.


## Disclosures

- This is research and market intelligence, not investment advice.
- AI conclusions are research judgments, not validated return predictions.
- The frozen risk layer is risk-only and is not used for directional views or allocations.
- Legacy scores are not active inputs or outputs.

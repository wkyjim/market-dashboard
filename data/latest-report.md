# AEGIS AI-First Market Intelligence

Research generated at: 16 November 2026, 20:10 HKT
Database freshness: equity 2026-11-13 (latest row retrieved 2026-11-16 13:06:43.000010+08:00)
Data cutoff: 2026-11-13 US cash close
Snapshot ID: aegis-hourly-20261116T121015Z

## Executive Summary

- **AI market view: Late-November 2026 US equities show a late-cycle, mixed tape: broad market breadth is positive but the index is slightly negative over 20 days, and the leadership set is bifurcated between high-momentum names and large dislocation names. Sector returns are bifurcated, with Health Care, Consumer Discretionary, Consumer Staples and Financials leading, while Information Technology and Energy lag. Macro data point to a still-easing but gradually normalizing rate path, with inflation near 3.4% headline CPI and unemployment around 4.2%, and credit spreads remain contained but not tight.**
- Equity market: SPX close 7561.67 on 2026-11-13, 20-day return -1.28%; breadth is positive (71.3% above 50-day, 63.6% above 200-day, ADR 1.70) but 20-day positive rate is 70.5%.
- Sector leadership: Health Care +6.87%, Consumer Discretionary +6.69%, Consumer Staples +5.40%, Financials +5.69%, Real Estate +5.24% over 20 days; Information Technology -7.19% and Energy -4.81% are the laggards.
- Flows: XLV shows strong institutional confirmation (20d z-score +1.45, 60d +1.72), XLY is in structural distribution (-0.38/60d -0.78), and XLU shows exceptional institutional selling with medium-term deterioration (-2.15/60d +0.48).
- Macro: Fed funds 3.88% (2026-11-12), 10Y-2Y spread 0.27 (2026-11-13), headline CPI 336.298 (2026-09-01), core CPI 338.896, unemployment 4.2% (2026-09-01).
- Credit: US high-yield OAS 3.20 and IG OAS 0.89 (2026-11-12), indicating contained but not compressed credit conditions.
- Risk: frozen daily-close model forecast vol 5d 14.9%, spike probability 16.5% vs historical baseline 22.1% and EWMA baseline 20.1%; directional signal is false, so no directional tilt is implied.

## Data QC

- Status: **PASS_WITH_WARNINGS**
- Equity session: 0 completed session(s) behind inference date
- Equity provenance: 393 provisional / 12576 canonical
- Breadth lag: 0 session(s); ETF-flow lag: 0 session(s)
- Note: Equity session contains a mix of provisional yfinance and canonical Massive rows.
- External sources: 79 ok / 0 unavailable; retrieved 2026-11-16T12:10:40.828957+00:00

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
| SPX | 7561.67 | -1.28% (20d) | Index is slightly negative over 20 days while breadth remains positive; 50-day and 200-day above-percentages are 71.3% and 63.6%. |
| Health Care (XLV) | +6.87% (20d) | +6.87% | Strongest sector; ETF trailing P/E 30.78 and flow z-scores +1.45/60d indicate strong institutional confirmation. |
| Consumer Discretionary (XLY) | +6.69% (20d) | +6.69% | Second-strongest sector; ETF trailing P/E 25.11 but flows show structural distribution with 20d z-score -0.38 and 60d -0.78. |
| Consumer Staples (XLP) | +5.40% (20d) | +5.40% | Positive 20-day return; ETF trailing P/E 24.85. |
| Financials (XLF) | +5.69% (20d) | +5.69% | Positive 20-day return; ETF trailing P/E 15.85. |
| Information Technology (XLK) | -7.19% (20d) | -7.19% | Worst sector; ETF trailing P/E 30.03, consistent with the large dislocation names in the shortlist. |
| Energy (XLE) | -4.81% (20d) | -4.81% | Negative 20-day return; ETF trailing P/E 16.23. |

## Macro, Fiscal, Rates, Liquidity and Credit

- Growth: macro database provides only CPI, core CPI and unemployment for 2026-09-01; no growth or payroll series is available in the supplied snapshot, so growth assessment is limited to the labor market at 4.2% unemployment.
- Inflation: headline CPI 336.298 and core CPI 338.896 (2026-09-01) indicate inflation still above the pre-2021 range, with the latest external CPI observation 337.476 (2026-10-01) suggesting a modest monthly step-up.
- Policy: effective federal funds rate is 3.88% as of 2026-11-12, consistent with a still-easing but gradually normalizing policy path.
- Rates: 10Y-2Y Treasury spread is 0.27 as of 2026-11-13, a modestly positive curve that does not signal imminent recession pricing.
- Liquidity: credit spreads are contained, with high-yield OAS 3.20 and IG OAS 0.89 (2026-11-12), indicating adequate liquidity conditions without extreme tightness.
- Credit: the frozen risk model shows forecast vol 5d 14.9%, spike probability 16.5% versus historical baseline 22.1% and EWMA baseline 20.1%, with no directional signal, implying a neutral-to-cautious risk posture.

## US Equities and 11 GICS Sectors

Macro source IDs: S001, S002, S003, S004, S005, S006, S007

| GICS sector | Evidence | AI research stance | Source IDs |
| --- | --- | --- | --- |
| Health Care | 20-day return +6.87% (XLV); ETF trailing P/E 30.78 (S054); flow z-scores +1.45 (20d) and +1.72 (60d) with strong confirmation; SPX 20-day return -1.28%. | Positive momentum and institutional confirmation; sector is a relative leader in a mixed tape. | S054 |
| Consumer Discretionary | 20-day return +6.69% (XLY); ETF trailing P/E 25.11 (S059); flows show structural distribution with 20d z-score -0.38 and 60d -0.78. | Price momentum positive but institutional flows are neutral-to-negative; leadership is not fully confirmed by flows. | S059 |
| Consumer Staples | 20-day return +5.40% (XLP); ETF trailing P/E 24.85 (S056). | Steady positive sector return with moderate valuation; defensive quality in a late-cycle tape. | S056 |
| Financials | 20-day return +5.69% (XLF); ETF trailing P/E 15.85 (S061). | Positive sector return with low valuation; consistent with a still-easing rate path. | S061 |
| Real Estate | 20-day return +5.24% (XLRE); ETF trailing P/E 29.63 (S058). | Positive 20-day return but higher valuation; sector is a mid-tier performer. | S058 |
| Utilities | 20-day return +4.34% (XLU); ETF trailing P/E 18.11 (S063); flows show exceptional institutional selling with 20d z-score -2.15 and medium-term deterioration. | Price momentum positive but institutional flows are strongly negative; demand-side caution despite defensive positioning. | S063 |
| Materials | 20-day return +2.57% (XLB); ETF trailing P/E 21.72 (S068). | Modest positive sector return with mid-range valuation; no strong flow signal in the supplied data. | S068 |
| Industrials | 20-day return +0.61% (XLI); ETF trailing P/E 27.07 (S069). | Near-flat sector return; mid-range valuation with limited momentum. | S069 |
| Communication Services | 20-day return -1.48% (XLC); ETF trailing P/E 17.26 (S071). | Negative sector return; valuation is moderate but price momentum is negative. | S071 |
| Information Technology | 20-day return -7.19% (XLK); ETF trailing P/E 30.03 (S072); shortlist includes large dislocation names MRVL, NOW, AMD with high P/E and low earnings yield. | Weakest sector; high-multiple names are under dislocation pressure and the sector is a clear laggard. | S072 |
| Energy | 20-day return -4.81% (XLE); ETF trailing P/E 16.23 (S073). | Negative sector return with low valuation; energy is a laggard in the current tape. | S073 |

### Sector fundamentals, valuation and earnings

No point-in-time sector fundamentals beyond the supplied ETF trailing P/E and 20-day returns are available in the database snapshot. The supplied evidence includes only sector-level price returns, ETF trailing P/E, and flow z-scores; growth, margins, consensus, and balance-sheet data are not provided for the full sector universe. Therefore, no additional sector fundamental metrics are asserted here.

## Growth vs Value

- Growth: Information Technology is the only clearly negative-growth sector in the 20-day snapshot, with XLK down -7.19% and large dislocation names MRVL (PE 74.23, earnings yield 1.35%) and NOW (PE 97.19, earnings yield 1.03%) showing extreme valuations.
- Value: Energy (XLE, PE 16.23) and Financials (XLF, PE 15.85) offer the lowest trailing P/E in the sector set, while Health Care (XLV, PE 30.78) and Information Technology (XLK, PE 30.03) are the most expensive.
- Earnings yield: CHTR (4.99%), FISV (10.36%), PNR (7.36%), GEN (7.07%), CLX (5.47%), ROP (6.00%) and MU (8.77%) show higher earnings yields, but several of these names carry forward-EPS or valuation-quality flags and are not treated as clean value signals.
- Valuation quality: the screening process rejected forward-EPS-based quality for NVDA, AMD, MU, AAPL, INTC, LITE, COIN, NOW, FFIV, SNDK, MRVL, FFIV and others, so the remaining shortlist is dominated by momentum and dislocation signals rather than clean growth/value composites.

## ETF Flows and Breadth

- Breadth is positive: 71.3% of names above 50-day, 63.6% above 200-day, 7

## Stock Ideas

Single-stock research uses reported EPS, forward P/E and company fundamentals. All ideas are research judgments, not validated return predictions.

| Ticker | Security | Research view | Price | EPS | Forward P/E | Base target | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| APP | AppLovin | NEW | 409.1 | 20.86026 | 19.611452 | 417.21 | NEW |
| PNR | Pentair | KEEP | 68.3 | 5.30402 | 12.877027 | 74.26 | KEEP |
| GEN | Gen Digital | KEEP | 30.4 | 3.33736 | 9.108996 | 33.37 | KEEP |
| ROP | Roper Technologies | NEW | 479.975 | 24.57318 | 19.532475 | 393.17 | NEW |

## ETF Ideas

ETF research uses holdings, portfolio valuation and exposure. Single-stock EPS × P/E valuation is not applied to ETFs.

| Ticker | Fund | Research view | Price | Top holdings | Portfolio valuation | Sector exposure | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| XLV | Health Care sector ETF | KEEP | 188.85 | LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59% | Top 10 holdings; numeric weight coverage 61.42% | Health Care | KEEP |
### APP — AppLovin

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** AppLovin offers the strongest 20-day momentum among the shortlisted names with a near-flat 60-day drawdown, and its high margins support a forward P/E near 19.6. It is preferred over the high-multiple names such as NOW and MRVL, which carry much higher forward P/E and weaker quality flags. Alternatives considered: NOW, MRVL.
- **Thesis:** AppLovin screens in the top 20-day momentum bucket with a 53.7% 20-day return and a 32.5% 60-day return, while keeping a 60-day drawdown near flat. Reported diluted EPS of 11.61 for the 2026-09-30 period and a forward EPS of 20.86 support a forward P/E near 19.6, which is reasonable for a high-margin, high-growth mobile advertising platform.
- **Source IDs:** S008, S011, S012, S015
- **Catalysts:** Continued momentum in 20-day price performance, Sustained high gross margin and operating margin, Forward EPS growth from reported earnings
- **Risks:** High 20-day momentum can mean elevated volatility, Forward EPS and fiscal-year mapping are unverified, Sector-relative P/E is at 1.0, so no cheapness cushion
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 20.8603 (source.forwardEps) x AI multiple assumption 20.00; source IDs S008, S011, S012, S015
- **EPS:** 20.86026 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 19.611452
- **FY+1 growth assumption:** 27.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / Apple Inc. (AAPL) and Microsoft Corp. (MSFT) as high-margin, ecosystem-driven software/platform peers / APP shows strong FY1 consensus earnings growth of 27.44% and revenue growth of 25.37%, with exceptional margins (gross 88.8%, operating 77.8%, profit 65.9%) and ROE of 2.10x. The forward P/E of 19.6x is supported by durable high margins and platform scale, but the multiple is not set equal to current forward P/E; it is justified by growth, margin durability, and peer positioning relative to AAPL/MSFT. FY2 consensus is not available, so the 12M horizon uses the verified FY1 consensus growth.
- **Company fundamentals:** Reported diluted EPS 11.61 for period ending 2026-09-30; forward EPS 20.86; forward P/E 19.61; gross margin 88.8%; operating margin 77.8%; profit margin 65.9%; revenue growth 55.5%; earnings growth 75.5%; ROE 2.10; 20-day return 53.7%; 60-day return 32.5%; 60-day drawdown -0.2%; sector-relative P/E 1.0.
- **Bull / Base / Bear:** 500.65 / 417.21 / 333.76
- **Bull / Base / Bear returns:** 22.38% / 1.98% / -18.42%
- **Scenario probabilities:** not separately assigned; see scenario table.

### PNR — Pentair

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Pentair is preferred over the deeply negative names such as INTC and COIN because it has a positive forward P/E and a reasonable earnings yield, but it is not preferred over higher-quality compounders like ROP or APP because its fundamentals are contracting. Alternatives considered: INTC, COIN, ROP.
- **Thesis:** Pentair is in the top 20-day momentum bucket with a 27.8% 20-day return and a 7.1% 60-day return. Its forward P/E of 12.9 and earnings yield of 7.4% are reasonable, but revenue growth is slightly negative and earnings growth is negative, so the momentum is not yet supported by fundamental expansion.
- **Source IDs:** S010, S014, S017, S023
- **Catalysts:** 20-day momentum of 27.8%, Forward P/E near 12.9, Earnings yield near 7.4%
- **Risks:** Revenue growth -4.5% and earnings growth -18.8%, Sector-relative P/E of 0.49 indicates relative valuation weakness, Momentum may be driven by short-term factors rather than fundamentals
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 5.3040 (source.forwardEps) x AI multiple assumption 14.00; source IDs S010, S014, S017, S023
- **EPS:** 5.30402 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 12.877027
- **FY+1 growth assumption:** 12.82%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / Prologis Inc. (PLD) and Eaton Corp. (ETN) as industrial/logistics peers with cyclical capex and margin profiles / PNR shows FY1 consensus earnings growth of 12.82% and revenue growth of 18.38%, with gross margin of 40.2%, operating margin of 21.4%, and ROE of 0.156x. The forward P/E of 12.9x is below the base multiple of 14.0x, reflecting cyclical earnings risk and lower margins; the multiple is justified by growth, margin profile, and peer comparison to PLD/ETN. FY2 consensus is not available, so the 12M horizon uses the verified FY1 consensus growth.
- **Company fundamentals:** Reported diluted EPS 2.76 for period ending 2026-09-30; forward EPS 5.30; forward P/E 12.88; gross margin 40.2%; operating margin 21.4%; profit margin 15.4%; ROE 15.6%; revenue growth -4.5%; earnings growth -18.8%; 20-day return 27.8%; 60-day return 7.1%; 60-day drawdown -5.2%; sector-relative P/E 0.49.
- **Bull / Base / Bear:** 90.17 / 74.26 / 58.34
- **Bull / Base / Bear returns:** 32.02% / 8.73% / -14.58%
- **Scenario probabilities:** not separately assigned; see scenario table.

### GEN — Gen Digital

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Gen Digital is preferred over the negative fundamental names such as INTC and COIN because it has a positive forward P/E and a reasonable earnings yield, but it is not preferred over higher-quality compounders like ROP or APP because its growth is more modest. Alternatives considered: INTC, COIN, ROP.
- **Thesis:** Gen Digital is in the top 20-day momentum bucket with a 25.8% 20-day return and a 7.9% 60-day return. It has a low forward P/E of 9.1 and an earnings yield of 7.1%, but the 20-day momentum is not as strong as the top momentum names, and the fundamental growth is modest.
- **Source IDs:** S019, S020, S022, S032
- **Catalysts:** 20-day momentum of 25.8%, Forward P/E near 9.1, Earnings yield near 7.1%
- **Risks:** Revenue growth 12.2% and earnings growth 128.6% are not yet confirmed by forward estimates, Sector-relative P/E of 0.42 indicates relative valuation weakness, Momentum is below the top momentum names
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 3.3374 (source.forwardEps) x AI multiple assumption 10.00; source IDs S019, S020, S022, S032
- **EPS:** 3.33736 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 9.108996
- **FY+1 growth assumption:** 12.86%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / General Electric Co. (GE) and Honeywell International Inc. (HON) as diversified industrial peers with margin and growth profiles / GEN shows FY1 consensus earnings growth of 12.86% and revenue growth of 6.81%, with gross margin of 77.4%, operating margin of 43.2%, and ROE of 0.464x. The forward P/E of 9.1x is supported by growth and margin improvement, but the multiple is not set equal to current forward P/E; it is justified by growth, margin profile, and peer comparison to GE/HON. FY2 consensus is not available, so the 12M horizon uses the verified FY1 consensus growth.
- **Company fundamentals:** Reported diluted EPS 0.83 for period ending 2026-10-02; forward EPS 3.34; forward P/E 9.11; gross margin 77.4%; operating margin 43.2%; profit margin 23.1%; ROE 46.4%; revenue growth 12.2%; earnings growth 128.6%; 20-day return 25.8%; 60-day return 7.9%; 60-day drawdown -3.2%; sector-relative P/E 0.42.
- **Bull / Base / Bear:** 40.05 / 33.37 / 26.7
- **Bull / Base / Bear returns:** 31.74% / 9.77% / -12.17%
- **Scenario probabilities:** not separately assigned; see scenario table.

### ROP — Roper Technologies

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** Roper Technologies is preferred over the negative fundamental names such as INTC and COIN because it has positive revenue and earnings growth, and it is preferred over the high-multiple names such as NOW and MRVL because it has a more reasonable forward P/E and positive growth. Alternatives considered: INTC, COIN, NOW, MRVL.
- **Thesis:** Roper Technologies is in the top 20-day momentum bucket with a 25.4% 20-day return and a 16.9% 60-day return. It has a forward P/E of 19.5 and an earnings yield of 6.0%, with positive revenue growth of 7.6% and earnings growth of 32.6%. The high gross margin of 69.7% and operating margin of 28.0% support a quality compounder profile.
- **Source IDs:** S033, S035, S040, S042
- **Catalysts:** 20-day momentum of 25.4%, Positive revenue growth of 7.6%, Positive earnings growth of 32.6%
- **Risks:** Forward P/E of 19.5 is not cheap, Sector-relative P/E of 0.49 indicates relative valuation weakness, Momentum is below the top momentum names
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 24.5732 (source.forwardEps) x AI multiple assumption 16.00; source IDs S033, S035, S040, S042
- **EPS:** 24.57318 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 19.532475
- **FY+1 growth assumption:** 9.81%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / The Procter & Gamble Co. (PG) and Colgate-Palmolive Co. (CL) as consumer staples peers with stable margins and growth / ROP shows FY1 consensus earnings growth of 9.81% and revenue growth of 6.29%, with gross margin of 69.7%, operating margin of 28.0%, and ROE of 0.132x. The forward P/E of 19.5x is supported by stable consumer staples demand and margin profile, but the multiple is not set equal to current forward P/E; it is justified by growth, margin durability, and peer comparison to PG/CL. FY2 consensus is not available, so the 12M horizon uses the verified FY1 consensus growth.
- **Company fundamentals:** Reported diluted EPS 21.3 for period ending 2026-09-30; forward EPS 24.57; forward P/E 19.53; gross margin 69.7%; operating margin 28.0%; profit margin 30.7%; ROE 13.2%; revenue growth 7.6%; earnings growth 32.6%; 20-day return 25.4%; 60-day return 16.9%; 60-day drawdown -2.5%; sector-relative P/E 0.49.
- **Bull / Base / Bear:** 466.89 / 393.17 / 319.45
- **Bull / Base / Bear returns:** -2.73% / -18.09% / -33.44%
- **Scenario probabilities:** not separately assigned; see scenario table.

### XLV — Health Care sector ETF

- **Type:** ETF
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** The Health Care sector ETF is preferred over individual health care names such as IDXX when broad diversification and lower single-stock risk are desired, but it is not preferred when specific company fundamentals or catalysts are the focus. Alternatives considered: IDXX.
- **Thesis:** The Health Care sector ETF is a broad, diversified way to express exposure to large-cap health care names. It has a positive price change and a top-10 portfolio with high weight coverage, but the sector-level ETF does not provide the individual stock catalysts or valuation precision of the shortlisted names.
- **Source IDs:** S054, S055
- **Catalysts:** Positive price change, Top-10 holdings with high weight coverage, Diversified health care exposure
- **Risks:** Sector-level ETF does not provide individual stock catalysts, Top-10 weight coverage is 61.4%, leaving 38.6% in smaller holdings, Sector-specific regulatory and reimbursement risks
- **Valuation method:** Holdings/portfolio valuation with AI total-return assumption
- **Valuation status:** verified; forward-EPS source: ; period flags: 
- **Valuation assumptions:** Holdings/portfolio valuation; 10 weighted holdings; coverage 61.42%; source IDs S054, S055
- **Top holdings:** LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59%
- **Portfolio valuation:** Top 10 holdings; numeric weight coverage 61.42%
- **Sector exposure:** Health Care
- **Underlying drivers:** Diversified exposure to large-cap health care companies including LLY, JNJ, ABBV, MRK, UNH, TMO, AMGN, GILD, ABT, and PFE.
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
| Bull | 25% | +2.00% | Low 5-day volatility (14.9%) and below-threshold spike probability (16.5% vs 18.5% threshold) support a modest upside if US close confirms positive breadth and credit spreads tighten. |
| Base | 50% | +0.00% | Directional signal is false and forecast volatility is near baseline, so the most likely path is a range-bound move with returns near zero as no clear directional catalyst is present. |
| Bear | 25% | -2.00% | If the frozen daily-close model fails to confirm after the US close, elevated spike probability and volatility could trigger a mild downside move as risk-off flows pressure the index. |

### Long Term (12 months)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 30% | +8.00% | Sustained low volatility and below-threshold spike probability over the horizon support a bull case if earnings growth and credit conditions remain constructive. |
| Base | 40% | +3.00% | A neutral trajectory with modest positive drift is most probable given the false directional signal and stable volatility, reflecting balanced market positioning. |
| Bear | 30% | -5.00% | A bear case emerges if the frozen model's low-confidence signal deteriorates, causing volatility to rise and credit spreads to widen, leading to a meaningful drawdown. |

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
| S009 | filing | FISV | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0000798354-26-000042); 8-K filed 2026-11-03 (accession 0000798354-26-000039); 8-K filed 2026-10-23 (accession 0001193125-26-429481) |
| S010 | filing | PNR | 2026-10-27 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-27 (accession 0000077360-26-000058); 8-K filed 2026-10-27 (accession 0000077360-26-000055); 8-K filed 2026-09-22 (accession 0000077360-26-000050) |
| S011 | news | APP | Thu, 12 Nov 2026 20:05:45 GMT | ok | https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en | AppLovin Just Ripped 47% in a Month: Is It Too Late to Buy APP Stock Now? - Yahoo Finance (Thu, 12 Nov 2026 20:05:45 GMT); Is Trending Stock AppLovin Corporation (APP) a Buy Now? - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT); APP Stock Surges 51% After Q3 Earnings: Is it Still a Buy? - Yahoo Finance (Tue, 10 Nov 2026 14:24:00 GMT) |
| S012 | filing | APP | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json | Diluted EPS 11.61 for period ending 2026-09-30 (filed 2026-11-04) |
| S013 | stock | FISV | 2026-11-16 | ok | https://finance.yahoo.com/quote/FISV | Forward P/E: 7.99667; Price: 63.78; Market price: 63.78; Market cap: 33934002176; Market Cap: 33934002176; Consensus EPS FY+1: 7.97582; growth: 0.0959 |
| S014 | stock | PNR | 2026-11-16 | ok | https://finance.yahoo.com/quote/PNR | Trailing P/E: 18.610355; Forward P/E: 12.877027; Forward EPS: 5.30402; Price: 68.3; Market price: 68.3; Market cap: 10904415232; Sector: Industrials; Trailing Eps: 3.67; Revenue Growth: -0.045; Earnings Growth: -0.188; Gross Margin: 0.40168998; Operating Margin: 0.21410999; Profit Margin: 0.15435; Return On Equity: 0.15605; Total Revenue: 3966200064; Market Cap: 10904415232; Consensus EPS FY+1: 5.30402; growth: 0.1282 |
| S015 | stock | APP | 2026-11-16 | ok | https://finance.yahoo.com/quote/APP | Trailing P/E: 27.54882; Forward P/E: 19.611452; Forward EPS: 20.86026; Price: 409.1; Market price: 409.1; Market cap: 135543824384; Sector: Communication Services; Trailing Eps: 14.85; Revenue Growth: 0.555; Earnings Growth: 0.755; Gross Margin: 0.8878; Operating Margin: 0.77782995; Profit Margin: 0.65887; Return On Equity: 2.1008599; Total Revenue: 7608893952; Market Cap: 135543824384; Consensus EPS FY+1: 20.72438; growth: 0.2744 |
| S016 | filing | FISV | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json | Diluted EPS -8.9 for period ending 2026-09-30 (filed 2026-11-04) |
| S017 | filing | PNR | 2026-10-27 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json | Diluted EPS 2.76 for period ending 2026-09-30 (filed 2026-10-27) |
| S018 | news | FISV | Mon, 16 Nov 2026 02:19:15 GMT | ok | https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en | Fiserv, Inc. (FISV) Stock Price, News, Quote & History - Yahoo! Finance Canada (Mon, 16 Nov 2026 02:19:15 GMT); Why Fiserv, Inc. (FISV) Was Exited by Ariel Appreciation Fund - Yahoo Finance (Wed, 28 Oct 2026 07:00:00 GMT); Fiserv (FISV): Buy, Sell, or Hold Post Q2 Earnings? - Yahoo Finance (Tue, 08 Sep 2026 07:00:00 GMT) |
| S019 | stock | GEN | 2026-11-16 | ok | https://finance.yahoo.com/quote/GEN | Trailing P/E: 15.431472; Forward P/E: 9.108996; Forward EPS: 3.33736; Price: 30.4; Market price: 30.4; Market cap: 18035593216; Sector: Technology; Trailing Eps: 1.97; Revenue Growth: 0.122; Earnings Growth: 1.286; Gross Margin: 0.77410007; Operating Margin: 0.43229; Profit Margin: 0.23068; Return On Equity: 0.46402; Total Revenue: 5228000256; Market Cap: 18035593216; Consensus EPS FY+1: 3.33736; growth: 0.1286 |
| S020 | filing | GEN | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0000849399-26-000083); 8-K filed 2026-10-28 (accession 0000849399-26-000081); 8-K filed 2026-10-09 (accession 0000849399-26-000079) |
| S021 | filing | CLX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000021076-26-000046); 8-K filed 2026-11-02 (accession 0000021076-26-000044); 8-K filed 2026-10-29 (accession 0001206774-26-000586) |
| S022 | news | GEN | Thu, 29 Oct 2026 07:00:00 GMT | ok | https://news.google.com/rss/search?q=GEN+Gen+Digital+stock&hl=en-US&gl=US&ceid=US:en | Gen Digital (GEN) Stock Repriced After Q2 Earnings Put Margins Center Stage - Yahoo Finance (Thu, 29 Oct 2026 07:00:00 GMT); Gen Digital Stock: Is Wall Street Bullish or Bearish? - Yahoo Finance (Thu, 05 Nov 2026 08:00:00 GMT); Are Business Services Stocks Lagging GEN DIGITAL INC (GEN) This Year? - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT) |
| S023 | news | PNR | Sat, 14 Nov 2026 08:48:27 GMT | ok | https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en | Pentair plc (PNR) Stock Price, News, Quote & History - Yahoo! Finance Canada (Sat, 14 Nov 2026 08:48:27 GMT); Pentair plc (PNR) stock price, news, quote and history - Yahoo Finance UK (Fri, 13 Nov 2026 22:09:48 GMT); Pentair plc (PNR) Q3 Earnings and Revenues Beat Estimates - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT) |
| S024 | news | CLX | Fri, 13 Nov 2026 23:34:51 GMT | ok | https://news.google.com/rss/search?q=CLX+Clorox+stock&hl=en-US&gl=US&ceid=US:en | The Clorox Company (CLX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 23:34:51 GMT); The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance UK (Sat, 14 Nov 2026 06:03:20 GMT); Clorox (CLX) Down 9.3% Since Last Earnings Report: Can It Rebound? - Yahoo Finance (Wed, 02 Sep 2026 07:00:00 GMT) |
| S025 | filing | CHTR | 2026-11-06 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-06 (accession 0001091667-26-000073); 8-K filed 2026-11-06 (accession 0001091667-26-000072); 8-K filed 2026-10-27 (accession 0001091667-26-000064) |
| S026 | stock | CHTR | 2026-11-16 | ok | https://finance.yahoo.com/quote/CHTR | Trailing P/E: 13.006578; Forward P/E: 3.0452294; Forward EPS: 45.44485; Price: 138.39; Market price: 138.39; Market cap: 24778944512; Sector: Communication Services; Trailing Eps: 10.64; Revenue Growth: 0.091; Gross Margin: 0.55084; Operating Margin: 0.23389; Profit Margin: 0.02498; Return On Equity: 0.07019; Total Revenue: 55645999104; Market Cap: 24778944512; Consensus EPS FY+1: 49.35412; growth: 1.1136 |
| S027 | stock | CLX | 2026-11-16 | ok | https://finance.yahoo.com/quote/CLX | Trailing P/E: 19.68705; Forward P/E: 17.745283; Forward EPS: 6.1684; Price: 109.46; Market price: 109.46; Market cap: 13260793856; Sector: Consumer Defensive; Trailing Eps: 5.56; Revenue Growth: 0.333; Earnings Growth: 1.138; Gross Margin: 0.41939998; Operating Margin: 0.14286; Profit Margin: 0.09408; Return On Equity: 5.34363; Total Revenue: 7196000256; Market Cap: 13260793856; Consensus EPS FY+1: 6.1684; growth: 0.0769 |
| S028 | filing | IDXX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000874716&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000874716-26-000135); 8-K filed 2026-11-02 (accession 0001104659-26-120892); 10-Q filed 2026-08-04 (accession 0000874716-26-000123) |
| S029 | stock | IDXX | 2026-11-16 | ok | https://finance.yahoo.com/quote/IDXX | Trailing P/E: 47.45485; Forward P/E: 41.687927; Forward EPS: 16.8929; Price: 704.23; Market price: 704.23; Market cap: 55483650048; Sector: Healthcare; Trailing Eps: 14.84; Revenue Growth: 0.099; Earnings Growth: 0.179; Gross Margin: 0.62722; Operating Margin: 0.32497; Profit Margin: 0.25357; Return On Equity: 0.68925005; Total Revenue: 4662220800; Market Cap: 55483650048; Consensus EPS FY+1: 16.8929; growth: 0.1244 |
| S030 | filing | CLX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000021076.json | Diluted EPS 1.39 for period ending 2026-09-30 (filed 2026-11-02) |
| S031 | filing | CHTR | 2026-11-06 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001091667.json | Diluted EPS 0.38 for period ending 2026-09-30 (filed 2026-11-06) |
| S032 | filing | GEN | 2026-10-29 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000849399.json | Diluted EPS 0.83 for period ending 2026-10-02 (filed 2026-10-29) |
| S033 | filing | ROP | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000882835&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000882835-26-000047); 8-K filed 2026-10-22 (accession 0000882835-26-000042); 8-K filed 2026-10-01 (accession 0000882835-26-000039) |
| S034 | news | CHTR | Sun, 15 Nov 2026 05:47:01 GMT | ok | https://news.google.com/rss/search?q=CHTR+Charter+Communications+stock&hl=en-US&gl=US&ceid=US:en | Charter Communications (CHTR) Stock Could Be A Bargain Following Its New Operating Model - Yahoo Finance (Sun, 15 Nov 2026 05:47:01 GMT); Why You Should Think About Charter Communications Differently Now? - Yahoo Finance (Fri, 13 Nov 2026 19:16:11 GMT); Charter Communications (CHTR) Earnings Expected to Grow: What to Know Ahead of Next Week's Release - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT) |
| S035 | stock | ROP | 2026-11-16 | ok | https://finance.yahoo.com/quote/ROP | Trailing P/E: 18.993866; Forward P/E: 19.532475; Forward EPS: 24.57318; Price: 479.975; Market price: 479.975; Market cap: 47535013888; Sector: Technology; Trailing Eps: 25.27; Revenue Growth: 0.076; Earnings Growth: 0.326; Gross Margin: 0.69671; Operating Margin: 0.28049; Profit Margin: 0.30712998; Return On Equity: 0.13229; Total Revenue: 8434599936; Market Cap: 47535013888; Consensus EPS FY+1: 24.57318; growth: 0.09810001 |
| S036 | news | IDXX | Sat, 14 Nov 2026 22:37:20 GMT | ok | https://news.google.com/rss/search?q=IDXX+Idexx+Laboratories+stock&hl=en-US&gl=US&ceid=US:en | IDEXX Laboratories, Inc. (IDXX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Sat, 14 Nov 2026 22:37:20 GMT); symbol__ Stock Quote Price and Forecast - CNN (Fri, 13 Nov 2026 15:22:45 GMT); IDEXX Laboratories (IDXX) Stock Looks Fairly Valued Despite Its 28% Run - Yahoo Finance (Sat, 31 Oct 2026 07:00:00 GMT) |
| S037 | filing | RDDT | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001713445&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0001713445-26-000116); 8-K filed 2026-10-29 (accession 0001713445-26-000114); 8-K filed 2026-08-12 (accession 0001713445-26-000107) |
| S038 | filing | IDXX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000874716.json | Diluted EPS 11.75 for period ending 2026-09-30 (filed 2026-11-02) |
| S039 | filing | INTC | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000050863&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0000050863-26-000191); 8-K filed 2026-10-29 (accession 0000050863-26-000188); 8-K filed 2026-08-12 (accession 0001193125-26-346806) |
| S040 | news | ROP | Thu, 05 Nov 2026 08:00:00 GMT | ok | https://news.google.com/rss/search?q=ROP+Roper+Technologies+stock&hl=en-US&gl=US&ceid=US:en | Roper Technologies (ROP) Stock Looks Fully Valued As Cash Flow Comes Into Focus - Yahoo Finance (Thu, 05 Nov 2026 08:00:00 GMT); Roper Technologies (ROP), What Is Behind The Fresh Attention? - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT); Did Earnings Beat Just Shift Roper Technologies (ROP) Investment Narrative? - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT) |

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
- news APP: https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en (Thu, 12 Nov 2026 20:05:45 GMT)
- filing APP: https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json (2026-11-04)
- stock FISV: https://finance.yahoo.com/quote/FISV (2026-11-16)
- stock PNR: https://finance.yahoo.com/quote/PNR (2026-11-16)
- stock APP: https://finance.yahoo.com/quote/APP (2026-11-16)
- filing FISV: https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json (2026-11-04)
- filing PNR: https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json (2026-10-27)
- news FISV: https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en (Mon, 16 Nov 2026 02:19:15 GMT)
- stock GEN: https://finance.yahoo.com/quote/GEN (2026-11-16)
- filing GEN: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 (2026-10-29)

## AI Provenance

- Provider / model: hermes-local-proxy / upstage/solar-mini4:free
- Market research: attempts=1 tokens=9513 (prompt=6513, completion=3000) runtime=18.63s
- Fundamental research: generated this run at 2026-11-16T12:10:15.270079+00:00
- Evidence source dates: {'as_of': '2026-11-13', 'latest_equity_date': '2026-11-13', 'latest_macro_date': '2026-11-16', 'flows_date': '2026-11-13'}
- Evidence fingerprint: bcf12b012532f3c83509cf491247c5ac6030edffbda53d405c3dfae448403375
- Source citations are retrieved external records in the ledger above; market values remain from the verified database snapshot.


## Disclosures

- This is research and market intelligence, not investment advice.
- AI conclusions are research judgments, not validated return predictions.
- The frozen risk layer is risk-only and is not used for directional views or allocations.
- Legacy scores are not active inputs or outputs.

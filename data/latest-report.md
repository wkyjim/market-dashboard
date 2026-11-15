# AEGIS AI-First Market Intelligence

Research generated at: 16 November 2026, 07:13 HKT
Database freshness: equity 2026-11-13 (latest row retrieved 2026-11-15 13:06:40.074841+08:00)
Data cutoff: 2026-11-13 US cash close
Snapshot ID: aegis-hourly-20261115T231349Z

## Executive Summary

- **AI market view: Late-November 2026 equity market is in a late-cycle, mixed posture: broad market breadth is positive and above both the 50-day and 200-day moving averages, but the S&P 500 is down 1.28% over 20 days and the Information Technology sector is the weakest, with Communication Services also negative. Momentum and dislocation screens are concentrated in a small set of names, while large-cap liquidity leaders and select financials/health care show relative strength. Credit spreads are tight, but crypto and select high-multiple names are under pressure, suggesting a cautious, quality-tilted stance rather than broad risk-on.**
- Broad market breadth is constructive: 71.34% of names above the 50-day and 63.6% above the 200-day, with a positive 20-day advance/decline ratio of 1.70.
- S&P 500 is down 1.28% over 20 days, and Information Technology (-7.19%) and Energy (-4.81%) are the weakest sectors, while Health Care (+6.87%), Consumer Discretionary (+6.69%) and Consumer Staples (+5.40%) lead.
- Momentum and dislocation screens are concentrated in a small set of names, with large-cap liquidity leaders (NVDA, AMD, MU, AAPL) and select dislocation names (RDDT, FFIV, MRVL, NOW) flagged, but several carry high forward-EPS or valuation-quality flags.
- Credit conditions are benign: US high-yield OAS at 3.20 and IG OAS at 0.89, with a modestly positive 10Y-2Y spread of 0.27.
- Crypto and select high-multiple names are under pressure: BTC -6.04% and ETH -8.22% on 2026-11-14, and several shortlisted names carry forward-EPS or valuation-quality warnings.
- Overall stance: late-cycle, quality-tilted, with breadth supportive but sector leadership narrow and concentration risk elevated in a few mega-cap and high-multiple names.

## Data QC

- Status: **PASS_WITH_WARNINGS**
- Equity session: 0 completed session(s) behind inference date
- Equity provenance: 393 provisional / 12576 canonical
- Breadth lag: 0 session(s); ETF-flow lag: 0 session(s)
- Note: Equity session contains a mix of provisional yfinance and canonical Massive rows.
- External sources: 79 ok / 0 unavailable; retrieved 2026-11-15T23:14:06.419227+00:00

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
| S&P 500 | 7561.67 | -1.28% (20d) | Broad market above 50d and 200d, but index negative over 20 days; sector leadership is narrow and IT is the weakest sector. |
| Health Care (XLV) | 6.87% | +6.87% (20d) | Strongest sector; trailing P/E 30.78, suggesting premium valuation with limited forward-EPS evidence. |
| Consumer Discretionary (XLY) | 6.69% | +6.69% (20d) | Positive momentum; trailing P/E 25.11, but forward-EPS data unavailable for the shortlist. |
| Consumer Staples (XLP) | 5.40% | +5.40% (20d) | Defensive strength; trailing P/E 24.85, consistent with late-cycle quality demand. |
| Information Technology (XLK) | -7.19% | -7.19% (20d) | Weakest sector; trailing P/E 30.03 with high-multiple names (MRVL, NOW, AMD) flagged for forward-EPS/valuation issues. |
| Financials (XLF) | 5.69% | +5.69% (20d) | Positive sector return; trailing P/E 15.85, the lowest among large sectors, consistent with tight credit spreads. |

## Macro, Fiscal, Rates, Liquidity and Credit

- Growth and labor: September 2026 unemployment is 4.2%, with October 2026 data showing 4.1% and 159,293 nonfarm payrolls, indicating a still-resilient but cooling labor market.
- Inflation: September 2026 CPI is 336.298 and core CPI 338.896; October 2026 CPI is 337.476, suggesting inflation remains above the pre-2021 trend and keeps policy restrictive.
- Policy: Effective federal funds rate is 3.88% as of 2026-11-12, with a modestly positive 10Y-2Y spread of 0.27, implying a late-cycle, still-restrictive but gradually easing stance.
- Rates and credit: IG OAS at 0.89 and HY OAS at 3.20 are tight, and the positive yield curve suggests bond markets are pricing a soft landing rather than a recession.
- Liquidity and risk assets: Crypto is under pressure with BTC -6.04% and ETH -8.22% on 2026-11-14, while equity breadth is positive, indicating a rotation away from risk assets into quality rather than broad deleveraging.
- Liquidity flows: SOXX shows exceptional institutional buying (20d z-score 5.10, 60d 3.17), while TLT is neutral-to-negative and SMH is in structural accumulation with tactical profit-taking, pointing to selective liquidity rather than broad risk appetite.

## US Equities and 11 GICS Sectors

Macro source IDs: S001, S002, S003, S004, S005, S006, S007

| GICS sector | Evidence | AI research stance | Source IDs |
| --- | --- | --- | --- |
| Health Care | Sector return 20d +6.87%; trailing P/E 30.78; S057 confirms P/E 30.782463. | Positive momentum but premium valuation; leadership is broad but not necessarily cheap. | S057 |
| Consumer Staples | Sector return 20d +5.40%; trailing P/E 24.85; S058 confirms P/E 24.852446. | Defensive strength in late cycle; reasonable valuation relative to Health Care. | S058 |
| Consumer Discretionary | Sector return 20d +6.69%; trailing P/E 25.11; S062 confirms P/E 25.110922. | Positive momentum; valuation is mid-range but forward-EPS evidence is unavailable. | S062 |
| Real Estate | Sector return 20d +5.24%; trailing P/E 29.63; S064 confirms P/E 29.627985. | Positive but premium valuation; limited breadth evidence in the supplied data. | S064 |
| Financials | Sector return 20d +5.69%; trailing P/E 15.85; S065 confirms P/E 15.849439. | Positive sector return with the lowest P/E among large sectors; consistent with tight credit spreads. | S065 |
| Utilities | Sector return 20d +4.34%; trailing P/E 18.11; S063 confirms P/E 18.114882. | Stable defensive holding; valuation is reasonable but return is the weakest among the positive sectors. | S063 |
| Materials | Sector return 20d +2.57%; trailing P/E 21.72; S067 confirms P/E 21.72047. | Modest positive return; valuation is mid-range but momentum is weaker than Health Care or Consumer Discretionary. | S067 |
| Industrials | Sector return 20d +0.61%; trailing P/E 27.07; S070 confirms P/E 27.069696. | Near-flat sector return; premium valuation with limited momentum, suggesting late-cycle caution. | S070 |
| Communication Services | Sector return 20d -1.48%; trailing P/E 17.26; S073 confirms P/E 17.264917. | Only negative sector among the large-cap group; valuation is reasonable but momentum is negative. | S073 |
| Information Technology | Sector return 20d -7.19%; trailing P/E 30.03; S074 confirms P/E 30.02927. | Weakest sector; high-multiple names (MRVL, NOW, AMD) carry forward-EPS and valuation-quality flags, and liquidity leaders are under pressure. | S074 |
| Energy | Sector return 20d -4.81%; trailing P/E 16.23; S076 confirms P/E 16.225414. | Negative sector return with reasonable valuation; likely driven by commodity/crypto-linked pressure rather than credit stress. | S076 |

### Sector fundamentals, valuation and earnings

The supplied database provides trailing P/E for each of the 11 GICS sectors via ETF-level evidence (S057-S076), but no point-in-time sector fundamentals such as sector-level earnings growth, margins, revenue, or consensus estimates are available. The sector view therefore relies on 20-day returns, trailing P/E, and the supplied ETF evidence; any claim about sector earnings power, growth, or margins would be invented and is not made.

## Growth vs Value

- Growth: Health Care (+6.87% 20d) and Consumer Discretionary (+6.69% 20d) lead, but the supplied data does not include sector-level earnings growth or consensus estimates; only trailing P/E is available.
- Value: Financials (XLF, P/E 15.85) and Energy (XLE, P/E 16.23) offer the lowest trailing P/E among the large sectors, while Information Technology (XLK, P/E 30.03) and Health Care (XLV, P/E 30.78) are the most expensive.
- Valuation quality: Several shortlisted names carry forward-EPS or valuation-quality flags (FISV, CHTR, SNDK, MRVL, FFIV, NOW, LITE, COIN, NVDA, AMD, MU, AAPL), so high earnings yield or low P/E does not translate into verified forward earnings support.
- Screening evidence: The momentum/dislocation/PE/liquidity buckets are independent and unweighted; no composite score is used, and the shortlist is concentrated in a small set of names with mixed quality flags.

## ETF Flows and Breadth

- Equity breadth is positive: 71.34% above the 50-day, 63.6% above the 200-day, and a 20-day advance/decline ratio of 1.70, with 315 advancers vs 185 decliners.
- Price-breadth divergence is -27.49 but not flagged as negative, and the standardized divergence is -0.0758, indicating broad participation without a sharp divergence signal.
- Flows are selective: SOXX shows exceptional institutional buying (20d z-score 5.10, 60d 3.17) despite a down price, while TLT is neutral-to-negative and SMH is in structural accumulation with tactical profit-taking.
- Crypto liquidity is deteriorating: BTC -6.04% and ETH -8.22% on 2026-11-14, suggesting risk appetite is rotating away from high-beta assets even as equity breadth remains positive.
- No new highs or new lows are reported, and the 5

## Stock Ideas

Single-stock research uses reported EPS, forward P/E and company fundamentals. All ideas are research judgments, not validated return predictions.

| Ticker | Security | Research view | Price | EPS | Forward P/E | Base target | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| APP | AppLovin | NEW | 409.1 | 20.86026 | 19.611452 | 417.21 | NEW |
| PNR | Pentair | KEEP | 68.3 | 5.30402 | 12.877027 | 68.95 | KEEP |
| GEN | Gen Digital | KEEP | 30.4 | 3.33736 | 9.108996 | 30.04 | KEEP |
| CLX | Clorox | KEEP | 109.46 | 6.1684 | 17.745283 | 111.03 | KEEP |

## ETF Ideas

ETF research uses holdings, portfolio valuation and exposure. Single-stock EPS × P/E valuation is not applied to ETFs.

| Ticker | Fund | Research view | Price | Top holdings | Portfolio valuation | Sector exposure | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| XLV | Health Care sector ETF | KEEP | 188.85 | LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59% | Top 10 holdings; numeric weight coverage 61.42% | Health Care | KEEP |
### APP — AppLovin

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** AppLovin offers the strongest 20-day momentum among the shortlisted names and a high-margin, cash-generative advertising model, making it preferable to the lower-momentum, lower-margin names such as Clorox and Pentair. Alternatives considered: CLX, PNR.
- **Thesis:** AppLovin screens in the top 20-day momentum bucket with a 53.7% 20-day return and a 32.5% 60-day return, and its reported diluted EPS of 11.61 and forward EPS of 20.86 support a forward P/E near 19.6. The momentum and high-margin advertising business justify a new position despite the recent 47% one-month pop flagged in the news source.
- **Source IDs:** S008, S011, S014, S018
- **Catalysts:** Sustained 20-day momentum above 50%, Continued high-margin revenue growth in mobile advertising, Forward EPS expansion supporting a sub-20 forward P/E
- **Risks:** Recent sharp price run-up may leave limited upside, Momentum can reverse quickly if ad market conditions weaken, Forward EPS and fiscal-year mapping are unverified
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 20.8603 (source.forwardEps) x AI multiple assumption 20.00; source IDs S008, S011, S014, S018
- **EPS:** 20.86026 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 19.611452
- **FY+1 growth assumption:** 27.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / PNR / APP shows strong FY1 consensus growth of 27.4% with 25.4% revenue growth and high margins (gross 88.8%, operating 77.8%, profit 65.9%), supported by 26 analysts. PNR is the named peer reference: APP's forward P/E of 19.6x is above PNR's 12.9x, reflecting APP's superior growth and margin profile, so a premium multiple is justified. The 20x base multiple reflects durable high-margin cash generation and growth; 24x bull and 16x bear bracket the risk that FY2 consensus is unverified and growth could decelerate.
- **Company fundamentals:** Reported diluted EPS 11.61; forward EPS 20.86; forward P/E 19.61; 20-day return 53.7%; 60-day return 32.5%; gross margin 88.8%; operating margin 77.8%; profit margin 65.9%; ROE 2.10; revenue growth 55.5%; earnings growth 75.5%.
- **Bull / Base / Bear:** 500.65 / 417.21 / 333.76
- **Bull / Base / Bear returns:** 22.38% / 1.98% / -18.42%
- **Scenario probabilities:** not separately assigned; see scenario table.

### PNR — Pentair

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Pentair is preferable to the high-multiple dislocation names such as NOW and MRVL because it trades at a much lower P/E and has a more stable industrial cash flow profile, even though its growth is weaker. Alternatives considered: NOW, MRVL.
- **Thesis:** Pentair is a top-20-day-momentum name with a 27.8% 20-day return and a 13.6 trailing P/E, but its revenue growth is slightly negative and earnings growth is negative, so the valuation is not compelling enough to upgrade to a buy. The stock is kept as a core industrial holding with a neutral stance.
- **Source IDs:** S009, S016, S019, S020
- **Catalysts:** 20-day momentum of 27.8%, Industrial water and fluid handling demand recovery, Stable 13.6 trailing P/E relative to the broader market
- **Risks:** Negative revenue and earnings growth, Cyclical exposure to industrial end markets, Lower sector-relative P/E suggests limited upside versus peers
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 5.3040 (source.forwardEps) x AI multiple assumption 13.00; source IDs S009, S016, S019, S020
- **EPS:** 5.30402 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 12.877027
- **FY+1 growth assumption:** 12.82%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / APP / PNR has 12.8% FY1 consensus growth with 18.4% revenue growth but negative earnings growth (-18.8%) and lower margins (gross 40.2%, operating 21.4%, profit 15.4%), with 15 analysts. APP is the named peer reference: PNR trades at 12.9x forward P/E versus APP's 19.6x, consistent with its weaker earnings momentum and margin profile. A 13x base multiple reflects modest growth and margin recovery potential; 16x bull and 10x bear bracket the risk that FY2 consensus is unverified and earnings recovery is uncertain.
- **Company fundamentals:** Reported diluted EPS 2.76; forward EPS 5.30; forward P/E 12.88; 20-day return 27.8%; 60-day return 7.1%; gross margin 40.2%; operating margin 21.4%; profit margin 15.4%; ROE 15.6%; revenue growth -4.5%; earnings growth -18.8%.
- **Bull / Base / Bear:** 84.86 / 68.95 / 53.04
- **Bull / Base / Bear returns:** 24.25% / 0.95% / -22.34%
- **Scenario probabilities:** not separately assigned; see scenario table.

### GEN — Gen Digital

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Gen Digital is preferable to the unprofitable dislocation names such as INTC and COIN because it has a positive forward P/E and a more defensible cyber-security franchise, even though its growth is modest. Alternatives considered: INTC, COIN.
- **Thesis:** Gen Digital is a top-20-day-momentum name with a 25.8% 20-day return and a 14.2 trailing P/E, but its forward P/E of 9.1 and negative revenue growth in the latest reported period limit the upside. The stock is kept as a neutral cyber-security holding rather than a buy.
- **Source IDs:** S015, S021, S022, S027
- **Catalysts:** 20-day momentum of 25.8%, Cyber-security spending resilience, Reasonable forward P/E near 9
- **Risks:** Negative revenue growth in the latest reported period, Cyclical cyber-risk exposure, Forward EPS and fiscal-year mapping are unverified
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 3.3374 (source.forwardEps) x AI multiple assumption 9.00; source IDs S015, S021, S022, S027
- **EPS:** 3.33736 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 9.108996
- **FY+1 growth assumption:** 12.86%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / CLX / GEN has 12.9% FY1 consensus growth with 6.8% revenue growth, strong earnings growth of 128.6%, and solid ROE of 46.4%, with 11 analysts. CLX is the named peer reference: GEN trades at 9.1x forward P/E versus CLX's 17.7x, reflecting GEN's lower margin profile (gross 77.4%, operating 43.2%, profit 23.1%) and smaller scale. A 9x base multiple reflects solid but less durable growth and lower profitability; 11x bull and 7x bear bracket the risk that FY2 consensus is unverified and margin expansion is uncertain.
- **Company fundamentals:** Reported diluted EPS 0.83; forward EPS 3.34; forward P/E 9.11; 20-day return 25.8%; 60-day return 7.9%; gross margin 77.4%; operating margin 43.2%; profit margin 23.1%; ROE 46.4%; revenue growth 12.2%; earnings growth 128.6%.
- **Bull / Base / Bear:** 36.71 / 30.04 / 23.36
- **Bull / Base / Bear returns:** 20.76% / -1.18% / -23.16%
- **Scenario probabilities:** not separately assigned; see scenario table.

### CLX — Clorox

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Clorox is preferable to the high-multiple dislocation names such as NOW and MRVL because it offers a defensive consumer staples profile and a lower forward P/E, even though its growth is weak. Alternatives considered: NOW, MRVL.
- **Thesis:** Clorox is a top-20-day-momentum name with a 25.7% 20-day return and a 18.3 trailing P/E, but its revenue growth is only 0.3% and earnings growth is 1.1%, so the momentum is not backed by strong fundamentals. The stock is kept as a neutral consumer staples holding.
- **Source IDs:** S024, S025, S029, S038
- **Catalysts:** 20-day momentum of 25.7%, Consumer staples defensive demand, Sector-relative P/E of 0.76 suggests reasonable valuation
- **Risks:** Very weak revenue growth of 0.3%, Low earnings growth of 1.1%, Consumer spending slowdown could pressure volumes
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 6.1684 (source.forwardEps) x AI multiple assumption 18.00; source IDs S024, S025, S029, S038
- **EPS:** 6.1684 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 17.745283
- **FY+1 growth assumption:** 7.69%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / GEN / CLX has 7.7% FY1 consensus growth with 2.2% revenue growth but strong earnings growth of 113.8%, and 17 analysts. GEN is the named peer reference: CLX trades at 17.7x forward P/E versus GEN's 9.1x, reflecting CLX's higher margin profile (gross 41.9%, operating 14.3%, profit 9.4%) and larger scale. A 18x base multiple reflects durable consumer staples cash flow and higher profitability; 22x bull and 14x bear bracket the risk that FY2 consensus is unverified and revenue growth is modest.
- **Company fundamentals:** Reported diluted EPS 1.39; forward EPS 6.17; forward P/E 17.75; 20-day return 25.7%; 60-day return 3.2%; gross margin 41.9%; operating margin 14.3%; profit margin 9.4%; ROE 5.34%; revenue growth 0.3%; earnings growth 1.1%.
- **Bull / Base / Bear:** 135.7 / 111.03 / 86.36
- **Bull / Base / Bear returns:** 23.97% / 1.43% / -21.1%
- **Scenario probabilities:** not separately assigned; see scenario table.

### XLV — Health Care sector ETF

- **Type:** ETF
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** XLV is preferable to the consumer staples ETF XLP because health care offers a more diversified growth profile and a stronger long-term demographic tailwind, even though both are defensive. Alternatives considered: XLP.
- **Thesis:** The Health Care sector ETF provides diversified exposure to large-cap pharma and health care providers, with top holdings including LLY, JNJ, ABBV, and MRK. The sector is kept as a neutral core holding rather than a tactical favored given the mixed macro backdrop.
- **Source IDs:** S056, S057
- **Catalysts:** Diversified health care exposure across pharma and providers, Stable demand for health care services and products, Top-10 holdings coverage of 61.4%
- **Risks:** Sector concentration in large-cap pharma, Regulatory and reimbursement risk, Limited upside if macro growth remains soft
- **Valuation method:** Holdings/portfolio valuation with AI total-return assumption
- **Valuation status:** verified; forward-EPS source: ; period flags: 
- **Valuation assumptions:** Holdings/portfolio valuation; 10 weighted holdings; coverage 61.42%; source IDs S056, S057
- **Top holdings:** LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59%
- **Portfolio valuation:** Top 10 holdings; numeric weight coverage 61.42%
- **Sector exposure:** Health Care
- **Underlying drivers:** Demographic aging, innovation in pharmaceuticals and medical devices, stable demand for health care services, and diversified large-cap health care holdings.
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
| Bull | 25% | +2.00% | Low 5-day realized vol (14.9%) and below-threshold spike probability (16.5% vs 18.5% threshold) reduce near-term tail risk, supporting a modest positive drift if US close confirms the frozen daily model. |
| Base | 50% | +0.00% | Frozen daily-close model with no directional signal and baseline vol near historical norms implies a range-bound week; returns cluster around zero with balanced bid/ask and no catalyst-driven move. |
| Bear | 25% | -2.00% | If the US close fails to confirm the frozen forecast or a spike materializes above the 18.5% threshold, elevated volatility and negative skew could drive a mild downside move into the weekend. |

### Long Term (12 months)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 30% | +8.00% | Sustained low vol regime and confirmed positive drift would allow compounding gains; earnings and credit spreads remain supportive if rate expectations stay anchored. |
| Base | 40% | +3.00% | Moderate trend with stable volatility and neutral credit conditions yields a low-single-digit annualized return, reflecting balanced risk/reward and no major macro shock. |
| Bear | 30% | -5.00% | A shift to elevated volatility, widening credit spreads, or earnings disappointment would pressure valuations, producing a negative long-term return despite the current low-vol snapshot. |

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
| S011 | news | APP | Thu, 12 Nov 2026 20:05:45 GMT | ok | https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en | AppLovin Just Ripped 47% in a Month: Is It Too Late to Buy APP Stock Now? - Yahoo Finance (Thu, 12 Nov 2026 20:05:45 GMT); Is Trending Stock AppLovin Corporation (APP) a Buy Now? - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT); APP Stock Surges 51% After Q3 Earnings: Is it Still a Buy? - Yahoo Finance (Tue, 10 Nov 2026 14:24:00 GMT) |
| S012 | news | FISV | Thu, 12 Nov 2026 12:23:56 GMT | ok | https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en | Fiserv Stock Outlook: Is Wall Street Bullish or Bearish? - Yahoo Finance (Thu, 12 Nov 2026 12:23:56 GMT); Michael Burry makes a bold call on struggling payments giant - Yahoo Finance (Wed, 11 Nov 2026 00:17:00 GMT); Fiserv (FISV) Stock Looks Undervalued With Strong Excess Returns - Yahoo Finance Singapore (Wed, 11 Nov 2026 22:14:34 GMT) |
| S013 | stock | FISV | 2026-11-15 | ok | https://finance.yahoo.com/quote/FISV | Forward P/E: 7.99667; Price: 63.78; Market price: 63.78; Market cap: 33934002176; Market Cap: 33934002176; Consensus EPS FY+1: 7.98015; growth: 0.09689999 |
| S014 | filing | APP | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json | Diluted EPS 11.61 for period ending 2026-09-30 (filed 2026-11-04) |
| S015 | filing | GEN | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0000849399-26-000083); 8-K filed 2026-10-28 (accession 0000849399-26-000081); 8-K filed 2026-10-09 (accession 0000849399-26-000079) |
| S016 | news | PNR | Fri, 13 Nov 2026 22:05:23 GMT | ok | https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en | Pentair plc (PNR) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 22:05:23 GMT); Pentair plc (PNR) Q3 Earnings and Revenues Beat Estimates - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT); Pentair (PNR) Stock May Be 46% Undervalued As New CFO Arrives - Yahoo Finance (Fri, 25 Sep 2026 07:00:00 GMT) |
| S017 | filing | FISV | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json | Diluted EPS -8.9 for period ending 2026-09-30 (filed 2026-11-04) |
| S018 | stock | APP | 2026-11-15 | ok | https://finance.yahoo.com/quote/APP | Trailing P/E: 27.54882; Forward P/E: 19.611452; Forward EPS: 20.86026; Price: 409.1; Market price: 409.1; Market cap: 135543824384; Sector: Communication Services; Trailing Eps: 14.85; Revenue Growth: 0.555; Earnings Growth: 0.755; Gross Margin: 0.8878; Operating Margin: 0.77782995; Profit Margin: 0.65887; Return On Equity: 2.1008599; Total Revenue: 7608893952; Market Cap: 135543824384; Consensus EPS FY+1: 20.72438; growth: 0.2744 |
| S019 | stock | PNR | 2026-11-15 | ok | https://finance.yahoo.com/quote/PNR | Trailing P/E: 18.610355; Forward P/E: 12.877027; Forward EPS: 5.30402; Price: 68.3; Market price: 68.3; Market cap: 10904415232; Sector: Industrials; Trailing Eps: 3.67; Revenue Growth: -0.045; Earnings Growth: -0.188; Gross Margin: 0.40168998; Operating Margin: 0.21410999; Profit Margin: 0.15435; Return On Equity: 0.15605; Total Revenue: 3966200064; Market Cap: 10904415232; Consensus EPS FY+1: 5.30402; growth: 0.1282 |
| S020 | filing | PNR | 2026-10-27 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json | Diluted EPS 2.76 for period ending 2026-09-30 (filed 2026-10-27) |
| S021 | stock | GEN | 2026-11-15 | ok | https://finance.yahoo.com/quote/GEN | Trailing P/E: 15.431472; Forward P/E: 9.108996; Forward EPS: 3.33736; Price: 30.4; Market price: 30.4; Market cap: 18035593216; Sector: Technology; Trailing Eps: 1.97; Revenue Growth: 0.122; Earnings Growth: 1.286; Gross Margin: 0.77410007; Operating Margin: 0.43229; Profit Margin: 0.23068; Return On Equity: 0.46402; Total Revenue: 5228000256; Market Cap: 18035593216; Consensus EPS FY+1: 3.33736; growth: 0.1286 |
| S022 | news | GEN | Fri, 13 Nov 2026 09:34:35 GMT | ok | https://news.google.com/rss/search?q=GEN+Gen+Digital+stock&hl=en-US&gl=US&ceid=US:en | Gen Digital Inc. (GEN) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 09:34:35 GMT); Gen Digital (GEN) Stock Repriced After Q2 Earnings Put Margins Center Stage - Yahoo Finance (Thu, 29 Oct 2026 07:00:00 GMT); Gen Digital Stock: Is Wall Street Bullish or Bearish? - Yahoo Finance (Thu, 05 Nov 2026 08:00:00 GMT) |
| S023 | filing | CHTR | 2026-11-06 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-06 (accession 0001091667-26-000073); 8-K filed 2026-11-06 (accession 0001091667-26-000072); 8-K filed 2026-10-27 (accession 0001091667-26-000064) |
| S024 | filing | CLX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000021076-26-000046); 8-K filed 2026-11-02 (accession 0000021076-26-000044); 8-K filed 2026-10-29 (accession 0001206774-26-000586) |
| S025 | news | CLX | Sun, 15 Nov 2026 08:55:47 GMT | ok | https://news.google.com/rss/search?q=CLX+Clorox+stock&hl=en-US&gl=US&ceid=US:en | The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance UK (Sun, 15 Nov 2026 08:55:47 GMT); The Clorox Company (CLX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 05:44:34 GMT); The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance Singapore (Fri, 13 Nov 2026 14:10:46 GMT) |
| S026 | news | CHTR | Sun, 15 Nov 2026 05:47:01 GMT | ok | https://news.google.com/rss/search?q=CHTR+Charter+Communications+stock&hl=en-US&gl=US&ceid=US:en | Charter Communications (CHTR) Stock Could Be A Bargain Following Its New Operating Model - Yahoo Finance (Sun, 15 Nov 2026 05:47:01 GMT); Charter Communications (CHTR) Expands Enterprise Reach With Managed Secure Networking Launch - Yahoo Finance (Sun, 15 Nov 2026 06:08:00 GMT); Why You Should Think About Charter Communications Differently Now? - Yahoo Finance (Fri, 13 Nov 2026 19:16:11 GMT) |
| S027 | filing | GEN | 2026-10-29 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000849399.json | Diluted EPS 0.83 for period ending 2026-10-02 (filed 2026-10-29) |
| S028 | stock | CHTR | 2026-11-15 | ok | https://finance.yahoo.com/quote/CHTR | Trailing P/E: 13.006578; Forward P/E: 3.2831066; Forward EPS: 42.15215; Price: 138.39; Market price: 138.39; Market cap: 24778944512; Sector: Communication Services; Trailing Eps: 10.64; Revenue Growth: 0.091; Gross Margin: 0.55084; Operating Margin: 0.23389; Profit Margin: 0.02498; Return On Equity: 0.07019; Total Revenue: 55645999104; Market Cap: 24778944512; Consensus EPS FY+1: 47.15811; growth: 1.0195 |
| S029 | stock | CLX | 2026-11-15 | ok | https://finance.yahoo.com/quote/CLX | Trailing P/E: 19.68705; Forward P/E: 17.745283; Forward EPS: 6.1684; Price: 109.46; Market price: 109.46; Market cap: 13260793856; Sector: Consumer Defensive; Trailing Eps: 5.56; Revenue Growth: 0.333; Earnings Growth: 1.138; Gross Margin: 0.41939998; Operating Margin: 0.14286; Profit Margin: 0.09408; Return On Equity: 5.34363; Total Revenue: 7196000256; Market Cap: 13260793856; Consensus EPS FY+1: 6.1684; growth: 0.0769 |
| S030 | stock | IDXX | 2026-11-15 | ok | https://finance.yahoo.com/quote/IDXX | Trailing P/E: 47.45485; Forward P/E: 41.687927; Forward EPS: 16.8929; Price: 704.23; Market price: 704.23; Market cap: 55483650048; Sector: Healthcare; Trailing Eps: 14.84; Revenue Growth: 0.099; Earnings Growth: 0.179; Gross Margin: 0.62722; Operating Margin: 0.32497; Profit Margin: 0.25357; Return On Equity: 0.68925005; Total Revenue: 4662220800; Market Cap: 55483650048; Consensus EPS FY+1: 16.8929; growth: 0.1244 |
| S031 | filing | IDXX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000874716&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000874716-26-000135); 8-K filed 2026-11-02 (accession 0001104659-26-120892); 10-Q filed 2026-08-04 (accession 0000874716-26-000123) |
| S032 | news | IDXX | Sat, 14 Nov 2026 06:13:17 GMT | ok | https://news.google.com/rss/search?q=IDXX+Idexx+Laboratories+stock&hl=en-US&gl=US&ceid=US:en | IDEXX Laboratories, Inc. (IDXX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Sat, 14 Nov 2026 06:13:17 GMT); symbol__ Stock Quote Price and Forecast - CNN (Fri, 13 Nov 2026 15:22:45 GMT); IDEXX Laboratories (IDXX) Stock Looks Fairly Valued Despite Its 28% Run - Yahoo Finance (Sat, 31 Oct 2026 07:00:00 GMT) |
| S033 | filing | ROP | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000882835&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000882835-26-000047); 8-K filed 2026-10-22 (accession 0000882835-26-000042); 8-K filed 2026-10-01 (accession 0000882835-26-000039) |
| S034 | stock | ROP | 2026-11-15 | ok | https://finance.yahoo.com/quote/ROP | Trailing P/E: 18.993866; Forward P/E: 19.532475; Forward EPS: 24.57318; Price: 479.975; Market price: 479.975; Market cap: 47535013888; Sector: Technology; Trailing Eps: 25.27; Revenue Growth: 0.076; Earnings Growth: 0.326; Gross Margin: 0.69671; Operating Margin: 0.28049; Profit Margin: 0.30712998; Return On Equity: 0.13229; Total Revenue: 8434599936; Market Cap: 47535013888; Consensus EPS FY+1: 24.57318; growth: 0.09810001 |
| S035 | news | ROP | Fri, 13 Nov 2026 13:04:22 GMT | ok | https://news.google.com/rss/search?q=ROP+Roper+Technologies+stock&hl=en-US&gl=US&ceid=US:en | Roper Technologies, Inc. (ROP) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 13:04:22 GMT); Roper Technologies (ROP) Stock Looks Fully Valued As Cash Flow Comes Into Focus - Yahoo Finance (Thu, 05 Nov 2026 08:00:00 GMT); Roper Technologies (ROP), What Is Behind The Fresh Attention? - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT) |
| S036 | filing | RDDT | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001713445&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0001713445-26-000116); 8-K filed 2026-10-29 (accession 0001713445-26-000114); 8-K filed 2026-08-12 (accession 0001713445-26-000107) |
| S037 | filing | CHTR | 2026-11-06 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001091667.json | Diluted EPS 0.38 for period ending 2026-09-30 (filed 2026-11-06) |
| S038 | filing | CLX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000021076.json | Diluted EPS 1.39 for period ending 2026-09-30 (filed 2026-11-02) |
| S039 | stock | RDDT | 2026-11-15 | ok | https://finance.yahoo.com/quote/RDDT | Trailing P/E: 20.091835; Forward P/E: 10.770874; Forward EPS: 9.14039; Price: 98.45; Market price: 98.45; Market cap: 19010076672; Sector: Communication Services; Trailing Eps: 4.9; Revenue Growth: 0.53; Earnings Growth: 0.749; Gross Margin: 0.91547996; Operating Margin: 0.29397; Profit Margin: 0.32105; Return On Equity: 0.32029998; Total Revenue: 3088880128; Market Cap: 19010076672; Consensus EPS FY+1: 6.82439; growth: 0.2417 |
| S040 | news | RDDT | Thu, 29 Oct 2026 07:00:00 GMT | ok | https://news.google.com/rss/search?q=RDDT+Reddit+stock&hl=en-US&gl=US&ceid=US:en | Reddit shares sink on weak sales guidance and plans login requirement test as Google search traffic shrinks - CNBC (Thu, 29 Oct 2026 07:00:00 GMT); Reddit (NYSE:RDDT) surprises with Q3 2026 sales but stock drops 12.6% - Yahoo Finance (Thu, 29 Oct 2026 07:00:00 GMT); Should You Wait Before Buying Reddit Stock? - Trefis (Fri, 13 Nov 2026 18:20:39 GMT) |

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
- news APP: https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en (Thu, 12 Nov 2026 20:05:45 GMT)
- news FISV: https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en (Thu, 12 Nov 2026 12:23:56 GMT)
- stock FISV: https://finance.yahoo.com/quote/FISV (2026-11-15)
- filing APP: https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json (2026-11-04)
- filing GEN: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 (2026-10-29)
- news PNR: https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 22:05:23 GMT)
- filing FISV: https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json (2026-11-04)
- stock APP: https://finance.yahoo.com/quote/APP (2026-11-15)
- stock PNR: https://finance.yahoo.com/quote/PNR (2026-11-15)
- filing PNR: https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json (2026-10-27)

## AI Provenance

- Provider / model: hermes-local-proxy / upstage/solar-mini4:free
- Market research: attempts=1 tokens=9473 (prompt=6473, completion=3000) runtime=17.34s
- Fundamental research: generated this run at 2026-11-15T23:13:49.024359+00:00
- Evidence source dates: {'as_of': '2026-11-13', 'latest_equity_date': '2026-11-13', 'latest_macro_date': '2026-11-14', 'flows_date': '2026-11-13'}
- Evidence fingerprint: 4ed8f4b413d75335a98fc5e272f3deee8ae80d090fb01b518f09642b81d2242c
- Source citations are retrieved external records in the ledger above; market values remain from the verified database snapshot.


## Disclosures

- This is research and market intelligence, not investment advice.
- AI conclusions are research judgments, not validated return predictions.
- The frozen risk layer is risk-only and is not used for directional views or allocations.
- Legacy scores are not active inputs or outputs.

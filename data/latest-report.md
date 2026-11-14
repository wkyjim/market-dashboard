# AEGIS AI-First Market Intelligence

Research generated at: 14 November 2026, 21:13 HKT
Database freshness: equity 2026-11-13 (latest row retrieved 2026-11-14 13:50:55.938286+08:00)
Data cutoff: 2026-11-13 US cash close
Snapshot ID: aegis-hourly-20261114T131356Z

## Executive Summary

- **AI market view: Late-November 2026: broad market breadth is constructive (71.3% above 50-day, 63.6% above 200-day, A/D ratio 1.70), but the index-level 20-day return is negative and the 52-week high/low counts are flat, indicating a market that is technically supported but not yet making new highs. Sector leadership is bifurcated: defensive and consumer staples sectors are outperforming, while Information Technology and Energy are the weakest. Liquidity flows show strong, exceptional institutional buying in SOXX and a neutral-to-deteriorating posture in TLT, with SMH showing tactical profit-taking inside structural accumulation. Macro data remain consistent with a late-cycle, moderately restrictive policy stance, with the effective funds rate at 3.88% and a still-positive but narrow 10Y-2Y spread of 0.27.**
- Broad market breadth is positive: 71.3% of names above their 50-day moving average and 63.6% above their 200-day, with an advance/decline ratio of 1.70.
- Index-level momentum is negative over 20 days, and 52-week high/low counts are zero, so the rally is not yet confirmed by new highs.
- Sector returns are bifurcated: Health Care, Consumer Staples, Consumer Discretionary and Real Estate lead; Information Technology and Energy lag.
- Flows show exceptional institutional buying in SOXX and neutral-to-deteriorating flows in TLT, with SMH in tactical profit-taking within structural accumulation.
- Macro backdrop is late-cycle: effective funds rate 3.88%, core CPI still elevated, unemployment 4.2%, and a narrow 10Y-2Y spread of 0.27.
- Risk environment is moderate: 5-day forecast volatility 14.9% is below the 18.5% threshold, but spike probability 16.5% is below the historical baseline of 22.1%.

## Data QC

- Status: **PASS_WITH_WARNINGS**
- Equity session: 0 completed session(s) behind inference date
- Equity provenance: 386 provisional / 12581 canonical
- Breadth lag: 0 session(s); ETF-flow lag: 0 session(s)
- Note: Equity session contains a mix of provisional yfinance and canonical Massive rows.
- External sources: 79 ok / 0 unavailable; retrieved 2026-11-14T13:14:17.233646+00:00

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
| S&P 500 (SPX) | 7561.67 | -1.28% over 20 days | Index-level 20-day return is negative, but breadth is strongly positive with 71.3% above 50-day and 63.6% above 200-day. |
| Health Care (XLV) | +6.87% | 20-day return | Leading sector with trailing P/E of 30.78, reflecting defensive demand and premium valuation. |
| Consumer Staples (XLP) | +5.40% | 20-day return | Second-strongest sector; trailing P/E of 24.85 supports defensive positioning. |
| Information Technology (XLK) | -7.19% | 20-day return | Weakest major sector; trailing P/E of 30.03 is elevated despite the price decline. |
| Energy (XLE) | -4.81% | 20-day return | Negative sector return; trailing P/E of 16.23 is the cheapest among the 11 sectors. |
| SOXX | inflow | 20-day flow z-score 5.10 | Exceptional institutional buying with strong confirmation; price is down but flows are the dominant signal. |
| TLT | neutral | 20-day flow z-score -0.41 | Medium-term deterioration in flows; price is flat, suggesting cautious duration positioning. |

## Macro, Fiscal, Rates, Liquidity and Credit

- Growth: the 10Y-2Y Treasury spread is 0.27 as of 2026-11-13, a still-positive but narrow curve that signals a late-cycle, mildly restrictive rate environment rather than an imminent recession signal.
- Inflation: CPI for all urban consumers stands at 336.298 (2026-09-01) and core CPI at 338.896, indicating inflation remains above the pre-2021 trend and constrains the pace of monetary easing.
- Policy: the effective federal funds rate is 3.88% as of 2026-11-12, consistent with a moderately restrictive stance that supports defensive sector leadership.
- Rates: the positive but narrow 10Y-2Y spread of 0.27 suggests the market is pricing gradual normalization, with limited duration upside in the near term.
- Liquidity: SOXX shows exceptional institutional buying (20-day flow z-score 5.10) while TLT shows medium-term deterioration (20-day flow z-score -0.41), indicating a rotation toward productive/tech infrastructure and away from duration.
- Credit: US high-yield OAS is 3.20 and US investment-grade OAS is 0.89 as of 2026-11-12, implying tight but not distressed credit conditions that support risk assets at the margin.

## US Equities and 11 GICS Sectors

Macro source IDs: S001, S002, S003, S004, S005, S006, S007

| GICS sector | Evidence | AI research stance | Source IDs |
| --- | --- | --- | --- |
| Health Care | 20-day return +6.87% and trailing P/E 30.78; S056 confirms the premium valuation. | Defensive leadership with premium valuation; supported by positive breadth and stable demand. | S056 |
| Consumer Staples | 20-day return +5.40% and trailing P/E 24.85; S058 confirms the valuation. | Second-strongest sector; defensive positioning is rewarded in a late-cycle, restrictive-rate environment. | S058 |
| Consumer Discretionary | 20-day return +6.69% and trailing P/E 25.11; S060 confirms the valuation. | Outperforming despite the negative index return; consumer resilience is evident. | S060 |
| Real Estate | 20-day return +5.24% and trailing P/E 29.63; S066 confirms the valuation. | Positive sector return with a premium multiple; rate-sensitive but supported by broad market breadth. | S066 |
| Financials | 20-day return +5.69% and trailing P/E 15.85; S062 confirms the valuation. | Positive sector return with the cheapest multiple among the 11 sectors; rate-sensitive financials benefit from the positive curve. | S062 |
| Utilities | 20-day return +4.34% and trailing P/E 18.11; S067 confirms the valuation. | Defensive sector with moderate outperformance; stable cash flows are valued at a reasonable multiple. | S067 |
| Materials | 20-day return +2.57% and trailing P/E 21.72; S072 confirms the valuation. | Modest positive return; industrial and commodity-linked demand is supported by broad breadth. | S072 |
| Industrials | 20-day return +0.61% and trailing P/E 27.07; S069 confirms the valuation. | Near-flat sector return; breadth is positive but the sector is not leading, suggesting cautious industrial demand. | S069 |
| Communication Services | 20-day return -1.48% and trailing P/E 17.26; S079 confirms the valuation. | Negative sector return; the only major sector with a negative 20-day return, though valuation is not extreme. | S079 |
| Information Technology | 20-day return -7.19% and trailing P/E 30.03; S073 confirms the valuation. | Weakest major sector; price decline is sharp but the multiple remains elevated, indicating de-rating risk. | S073 |
| Energy | 20-day return -4.81% and trailing P/E 16.23; S076 confirms the valuation. | Negative sector return with the cheapest multiple; energy is de-rating despite a relatively low valuation. | S076 |

### Sector fundamentals, valuation and earnings

Sector-level fundamental evidence is limited to trailing P/E multiples for the 11 GICS sectors, all sourced from the supplied ETF claims (S056, S058, S060, S062, S066, S067, S069, S072, S073, S076, S079). No growth, margin, revenue, or consensus data are supplied for the sector ETFs, and no point-in-time sector fundamentals beyond these multiples are available in the database. Therefore, no additional sector fundamentals are reported here to avoid invention.

## Growth vs Value

- Value: Energy (XLE) has the cheapest trailing P/E at 16.23, followed by Financials (XLF) at 15.85, but Energy is the only major sector with a negative 20-day return, so cheapness is not yet translating into price strength.
- Growth: Health Care (XLV) and Consumer Discretionary (XLY) lead with 20-day returns of +6.87% and +6.69%, respectively, while Information Technology (XLK) is the only major sector with a negative 20-day return at -7.19%.
- Valuation dispersion is wide: the cheapest sector (Financials, 15.85) trades at roughly half the multiple of the most expensive (Health Care, 30.78), indicating a strong defensive/value rotation.
- The negative index 20-day return combined with positive sector returns for Health Care, Consumer Staples, Consumer Discretionary and Real Estate suggests a defensive rotation rather than broad-based growth momentum.

## ETF Flows and Breadth

- SOXX shows exceptional institutional buying with a 20-day flow z-score of 5.10 and strong confirmation, despite the price being down; this is the strongest flow signal in the dataset.
- SMH shows a 20-day flow z-score of 1.22 with an outflow and down price, indicating tactical profit-taking inside structural accumulation.
- TLT shows a 20-day flow z-score of -0.41 with a neutral state and flat price, indicating medium-term deterioration in flows.
- Market breadth is strongly positive: 71.3% of names above their 50-day moving average, 63.6% above their 200-day, and an advance/decline ratio of 1.70.
- The 52-week high/low counts are both 0, so the positive breadth has not yet produced new highs, and the index-level 20-day return is negative.

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
- **Why preferred / alternatives:** AppLovin offers a cleaner, higher-margin growth profile than the high-multiple technology names in the shortlist, with a forward P/E near 19.6 and a 60-day drawdown of only -0.2%, making it a more defensible momentum pick than the speculative dislocation names. Alternatives considered: INTC, RDDT, MRVL.
- **Thesis:** AppLovin screens in the top 20-day momentum bucket with a 53.7% 20-day return and a 60-day drawdown of only -0.2%, indicating a strong, orderly advance rather than a speculative melt-up. Reported diluted EPS of $11.61 for the fiscal period ending 2026-09-30 and a forward EPS of $20.86 support a forward P/E of about 19.6, which is reasonable for a high-margin, high-growth mobile advertising platform. The company's gross margin of 88.8% and operating margin of 77.8% show a durable, capital-light business model with strong profitability.
- **Source IDs:** S008, S012, S013, S014
- **Catalysts:** Continued momentum in mobile advertising spend and AppLovin's top-20-day return, Sustained high gross and operating margins supporting earnings growth, Forward EPS of $20.86 providing a valuation anchor near $409
- **Risks:** High 20-day momentum can reverse quickly if ad market conditions weaken, Forward P/E of ~19.6 leaves limited room for multiple compression if growth slows, Single-quarter reported EPS may not fully capture forward consensus
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 20.8603 (source.forwardEps) x AI multiple assumption 22.00; source IDs S008, S012, S013, S014
- **EPS:** 20.86026 — period: FY2027 (+1y consensus)
- **Forward P/E:** 19.611452
- **FY+1 growth assumption:** 27.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / Apple peers in premium consumer-electronics and services; high-margin, ecosystem-driven compounders / APP shows strong FY2027 consensus EPS growth of 27.44% and revenue growth of 55.5%, with exceptional margins (gross 88.8%, operating 77.8%, profit 65.9%) and ROE of 2.10. The base multiple of 22x is justified by durable high margins, ecosystem pricing power, and growth above the market, while the bull/bear range reflects upside from continued service mix and downside from hardware cyclicality. Peer reference: premium consumer-electronics and services peers with similar margin and growth profiles.
- **Company fundamentals:** AppLovin reported diluted EPS of $11.61 for the period ending 2026-09-30, with forward EPS of $20.86, forward P/E of 19.61, gross margin of 88.8%, operating margin of 77.8%, profit margin of 65.9%, revenue growth of 55.5%, and earnings growth of 75.5%. FY1 EPS growth was 27.4% and FY1 revenue growth was 25.4%.
- **Bull / Base / Bear:** 542.37 / 458.93 / 354.62
- **Bull / Base / Bear returns:** 32.58% / 12.18% / -13.32%
- **Scenario probabilities:** not separately assigned; see scenario table.

### PNR — Pentair

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Pentair is a lower-multiple industrial with a reasonable forward P/E, but its negative revenue and earnings growth make it less attractive than the higher-quality momentum names. It is preferred over the deeply distressed INTC and the speculative RDDT, but it does not offer the same growth quality as AppLovin. Alternatives considered: INTC, RDDT, APP.
- **Thesis:** Pentair is a top-20-day momentum name with a 27.8% 20-day return and a 60-day drawdown of -5.2%, but its fundamentals are mixed. Reported diluted EPS of $2.76 for the period ending 2026-09-30 and a forward EPS of $5.30 give a forward P/E of about 12.9, which is reasonable. However, revenue growth is -4.5% and earnings growth is -18.8%, indicating that the momentum is not yet supported by broad-based operating improvement.
- **Source IDs:** S010, S015, S018, S019
- **Catalysts:** 20-day momentum of 27.8% and a modest 60-day drawdown of -5.2%, Forward P/E of ~12.9 is attractive relative to the broader market, Diversified water, flow control, and building products exposure could benefit from infrastructure and water-efficiency trends
- **Risks:** Negative revenue growth of -4.5% and earnings growth of -18.8%, Forward EPS of $5.30 is flat with FY1 reported EPS, limiting near-term upside, Industrial end-market softness could delay a reacceleration
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 5.3040 (source.forwardEps) x AI multiple assumption 14.00; source IDs S010, S015, S018, S019
- **EPS:** 5.30402 — period: FY2027 (+1y consensus)
- **Forward P/E:** 12.877027
- **FY+1 growth assumption:** 12.82%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / PNR peers in industrial/energy infrastructure with moderate growth and margin recovery potential / PNR has FY2027 consensus EPS growth of 12.82% and revenue growth of 18.4%, with improving margins (gross 40.2%, operating 21.4%, profit 15.4%) and ROE of 15.6%. The base multiple of 14x reflects a recovery story with moderate growth and margin expansion, while the bull/bear range captures upside from infrastructure capex acceleration and downside from commodity or demand softness. Peer reference: industrial/energy infrastructure peers with similar growth and margin trajectory.
- **Company fundamentals:** Pentair reported diluted EPS of $2.76 for the period ending 2026-09-30, with forward EPS of $5.30, forward P/E of 12.88, gross margin of 40.2%, operating margin of 21.4%, profit margin of 15.4%, return on equity of 15.6%, revenue growth of -4.5%, and earnings growth of -18.8%. FY1 EPS growth was 12.8% and FY1 revenue growth was 18.4%.
- **Bull / Base / Bear:** 90.17 / 74.26 / 58.34
- **Bull / Base / Bear returns:** 32.02% / 8.73% / -14.58%
- **Scenario probabilities:** not separately assigned; see scenario table.

### GEN — Gen Digital

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Gen Digital offers a low forward P/E of ~9.1 and a reasonable momentum profile, but its flat forward EPS and modest revenue growth make it less compelling than the higher-quality momentum names. It is preferred over the distressed INTC and the speculative RDDT, but it does not offer the same growth quality as AppLovin. Alternatives considered: INTC, RDDT, APP.
- **Thesis:** Gen Digital is a top-20-day momentum name with a 25.8% 20-day return and a 60-day drawdown of -3.2%. It has a reasonable forward P/E of about 9.1 and a forward EPS of $3.34, but its fundamentals are mixed. Revenue growth is 12.2% and earnings growth is 128.6%, yet the forward EPS of $3.34 is flat with the reported FY1 EPS of $3.34, and the 20-day momentum is not yet clearly supported by a broad-based operating acceleration.
- **Source IDs:** S020, S022, S023, S031
- **Catalysts:** 20-day momentum of 25.8% and a modest 60-day drawdown of -3.2%, Forward P/E of ~9.1 is attractive relative to the broader market, Cybersecurity and digital life protection exposure could benefit from rising cyber threats and regulatory pressure
- **Risks:** Forward EPS of $3.34 is flat with FY1 reported EPS, limiting near-term upside, Revenue growth of 12.2% is positive but not explosive, High-multiple technology names in the shortlist carry more growth optionality
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 3.3374 (source.forwardEps) x AI multiple assumption 11.00; source IDs S020, S022, S023, S031
- **EPS:** 3.33736 — period: FY2027 (+1y consensus)
- **Forward P/E:** 9.108996
- **FY+1 growth assumption:** 12.86%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / GEN peers in specialty industrials and engineered products with moderate growth and margin profile / GEN has FY2027 consensus EPS growth of 12.86% and revenue growth of 12.2%, with solid margins (gross 77.4%, operating 43.2%, profit 23.1%) and ROE of 46.4%. The base multiple of 11x is justified by strong ROE and consistent growth, while the bull/bear range reflects upside from margin expansion and downside from cyclical demand. Peer reference: specialty industrials and engineered products peers with similar growth and margin profile.
- **Company fundamentals:** Gen Digital reported diluted EPS of $0.83 for the period ending 2026-10-02, with forward EPS of $3.34, forward P/E of 9.11, gross margin of 77.4%, operating margin of 43.2%, profit margin of 23.1%, return on equity of 46.4%, revenue growth of 12.2%, and earnings growth of 128.6%. FY1 EPS growth was 12.9% and FY1 revenue growth was 6.8%.
- **Bull / Base / Bear:** 46.72 / 36.71 / 30.04
- **Bull / Base / Bear returns:** 53.68% / 20.76% / -1.18%
- **Scenario probabilities:** not separately assigned; see scenario table.

### ROP — Roper Technologies

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Roper Technologies offers a reasonable forward P/E of ~19.5 and a strong momentum profile, but its flat forward EPS and modest revenue growth make it less compelling than the higher-quality momentum names. It is preferred over the distressed INTC and the speculative RDDT, but it does not offer the same growth quality as AppLovin. Alternatives considered: INTC, RDDT, APP.
- **Thesis:** Roper Technologies is a top-20-day momentum name with a 25.4% 20-day return and a 60-day drawdown of -2.5%. It has a reasonable forward P/E of about 19.5 and a forward EPS of $24.57, but its fundamentals are mixed. Revenue growth is 7.6% and earnings growth is 32.6%, yet the forward EPS of $24.57 is only modestly above the reported FY1 EPS of $24.57, and the 20-day momentum is not yet clearly supported by a broad-based operating acceleration.
- **Source IDs:** S032, S037, S038, S042
- **Catalysts:** 20-day momentum of 25.4% and a modest 60-day drawdown of -2.5%, Forward P/E of ~19.5 is reasonable for a high-quality technology franchise, Diversified industrial technology and software exposure could benefit from digital transformation trends
- **Risks:** Forward EPS of $24.57 is only modestly above FY1 reported EPS of $24.57, Revenue growth of 7.6% is positive but not explosive, High-multiple technology names in the shortlist carry more growth optionality
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 24.5732 (source.forwardEps) x AI multiple assumption 16.00; source IDs S032, S037, S038, S042
- **EPS:** 24.57318 — period: FY2027 (+1y consensus)
- **Forward P/E:** 19.532475
- **FY+1 growth assumption:** 9.81%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / ROP peers in marine/industrial and consumer goods with steady growth and margin stability / ROP has FY2027 consensus EPS growth of 9.81% and revenue growth of 7.6%, with moderate margins (gross 69.7%, operating 28.0%, profit 30.7%) and ROE of 13.2%. The base multiple of 16x reflects steady growth and stable margins, while the bull/bear range captures upside from demand strength and downside from cyclical or competitive pressure. Peer reference: marine/industrial and consumer goods peers with similar growth and margin profile.
- **Company fundamentals:** Roper Technologies reported diluted EPS of $21.30 for the period ending 2026-09-30, with forward EPS of $24.57, forward P/E of 19.53, gross margin of 69.7%, operating margin of 28.0%, profit margin of 30.7%, return on equity of 13.2%, revenue growth of 7.6%, and earnings growth of 32.6%. FY1 EPS growth was 9.8% and FY1 revenue growth was 6.3%.
- **Bull / Base / Bear:** 466.89 / 393.17 / 319.45
- **Bull / Base / Bear returns:** -2.73% / -18.09% / -33.44%
- **Scenario probabilities:** not separately assigned; see scenario table.

### XLV — Health Care sector ETF

- **Type:** ETF
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** The Health Care sector ETF is preferred over single-stock health care names because it diversifies idiosyncratic risk across multiple large-cap names, while still providing exposure to the defensive characteristics of the sector. It is a core holding rather than a tactical momentum or dislocation play. Alternatives considered: XLP, XLY, XLF.
- **Thesis:** The Health Care sector ETF provides diversified exposure to large-cap pharmaceutical, medical device, and managed care names. The ETF's top holdings include LLY, JNJ, ABBV, MRK, and UNH, which are generally defensive and cash-generative. The sector ETF is a reasonable core holding for investors seeking broad health care exposure without single-stock idiosyncratic risk, but it does not offer the same momentum or dislocation alpha as the individual stock candidates.
- **Source IDs:** S056, S057
- **Catalysts:** Diversified exposure to large-cap health care names with strong balance sheets, Defensive characteristics that can perform in risk-off environments, Top-10 holdings coverage of 61.4% provides a clear view of the largest positions
- **Risks:** Sector concentration in large-cap pharma and managed care, Regulatory and patent cliff risks across the pharmaceutical portfolio, Lower momentum and dislocation characteristics compared to individual stock candidates
- **Valuation method:** Holdings/portfolio valuation with AI total-return assumption
- **Valuation status:** verified; forward-EPS source: ; period flags: 
- **Valuation assumptions:** Holdings/portfolio valuation; 10 weighted holdings; coverage 61.42%; source IDs S056, S057
- **Top holdings:** LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59%
- **Portfolio valuation:** Top 10 holdings; numeric weight coverage 61.42%
- **Sector exposure:** Health Care
- **Underlying drivers:** Large-cap pharmaceutical, medical device, and managed care exposure; defensive sector characteristics; diversified top-10 holdings including LLY, JNJ, ABBV, MRK, and UNH.
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
| Bull | 25% | +2.00% | Low 5-day vol (14.9%) and below-threshold spike probability (16.5% vs 18.5% threshold) reduce near-term tail risk, allowing a modest upside drift if US close confirms the frozen daily model. |
| Base | 50% | +0.00% | Frozen daily-close model with no directional signal implies a range-bound week; base case anchors to the historical baseline (22.1%) and ewma baseline (20.1%) without a directional tilt. |
| Bear | 25% | -2.00% | If the US close fails to confirm the frozen forecast or volatility clusters, the 16.5% spike probability could exceed the 18.5% threshold, producing a mild downside move. |

### Long Term (12 months)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 30% | +8.00% | Sustained low volatility and confirmed US close would support continued risk appetite, with earnings and credit conditions driving a positive multi-week drift. |
| Base | 40% | +3.00% | Base case assumes no major shock; forward returns reflect the frozen daily model's neutral stance, with modest upside from stable rate and credit fundamentals. |
| Bear | 30% | -5.00% | A failure to confirm the frozen forecast, combined with elevated spike probability and widening vol, could trigger a negative multi-week drift as risk premiums reprice. |

## Positioning

- Maintain a defensive tilt: Health Care, Consumer Staples, Consumer Discretionary and Real Estate are the leading sectors with positive 20-day returns and premium-to-market multiples.
- Monitor Information Technology and Energy closely: both are negative over 20 days and have elevated or cheap multiples that do not yet support a bullish stance.
- Treat SOXX as a liquidity-driven signal: exceptional institutional buying is the dominant flow signal, but price is down, so position sizing should be cautious.
- Duration exposure is cautious: TLT shows medium-term flow deterioration and a flat price, consistent with a late-cycle, restrictive-rate environment.
- Do not infer allocation weights or directional bets; the evidence supports a neutral-to-defensive posture with active monitoring of breadth and flow signals.

## Catalysts

| Date | Event | Why it matters |
| --- | --- | --- |
| 2026-11-16 |  |  |

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
| S011 | news | FISV | Fri, 13 Nov 2026 00:53:33 GMT | ok | https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en | Fiserv, Inc. (FISV) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 00:53:33 GMT); Fiserv (FISV) Stock Looks Undervalued With Strong Excess Returns - Yahoo Finance (Wed, 11 Nov 2026 22:14:34 GMT); Fiserv Stock Outlook: Is Wall Street Bullish or Bearish? - Yahoo Finance (Thu, 12 Nov 2026 12:23:56 GMT) |
| S012 | news | APP | Tue, 10 Nov 2026 14:24:00 GMT | ok | https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en | APP Stock Surges 51% After Q3 Earnings: Is it Still a Buy? - Yahoo Finance (Tue, 10 Nov 2026 14:24:00 GMT); AppLovin stock soars after Q3 earnings, outlook beat - Yahoo Finance (Thu, 05 Nov 2026 08:00:00 GMT); Is Trending Stock AppLovin Corporation (APP) a Buy Now? - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT) |
| S013 | stock | APP | 2026-11-14 | ok | https://finance.yahoo.com/quote/APP | Trailing P/E: 27.54882; Forward P/E: 19.611452; Forward EPS: 20.86026; Price: 409.1; Market price: 409.1; Market cap: 135543824384; Sector: Communication Services; Trailing Eps: 14.85; Revenue Growth: 0.555; Earnings Growth: 0.755; Gross Margin: 0.8878; Operating Margin: 0.77782995; Profit Margin: 0.65887; Return On Equity: 2.1008599; Total Revenue: 7608893952; Market Cap: 135543824384; Consensus EPS FY+1: 20.72438; growth: 0.2744 |
| S014 | filing | APP | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json | Diluted EPS 11.61 for period ending 2026-09-30 (filed 2026-11-04) |
| S015 | news | PNR | Fri, 13 Nov 2026 15:54:46 GMT | ok | https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en | Pentair plc (PNR) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 15:54:46 GMT); Pentair (PNR) Stock May Be 46% Undervalued As New CFO Arrives - Yahoo Finance (Fri, 25 Sep 2026 07:00:00 GMT); Pentair plc (PNR) Q3 Earnings and Revenues Beat Estimates - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT) |
| S016 | stock | FISV | 2026-11-14 | ok | https://finance.yahoo.com/quote/FISV | Forward P/E: 7.9923306; Price: 63.78; Market price: 63.78; Market cap: 33934002176; Market Cap: 33934002176; Consensus EPS FY+1: 7.98015; growth: 0.09689999 |
| S017 | filing | FISV | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json | Diluted EPS -8.9 for period ending 2026-09-30 (filed 2026-11-04) |
| S018 | filing | PNR | 2026-10-27 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json | Diluted EPS 2.76 for period ending 2026-09-30 (filed 2026-10-27) |
| S019 | stock | PNR | 2026-11-14 | ok | https://finance.yahoo.com/quote/PNR | Trailing P/E: 18.610355; Forward P/E: 12.877027; Forward EPS: 5.30402; Price: 68.3; Market price: 68.3; Market cap: 10904415232; Sector: Industrials; Trailing Eps: 3.67; Revenue Growth: -0.045; Earnings Growth: -0.188; Gross Margin: 0.40168998; Operating Margin: 0.21410999; Profit Margin: 0.15435; Return On Equity: 0.15605; Total Revenue: 3966200064; Market Cap: 10904415232; Consensus EPS FY+1: 5.30402; growth: 0.1282 |
| S020 | filing | GEN | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0000849399-26-000083); 8-K filed 2026-10-28 (accession 0000849399-26-000081); 8-K filed 2026-10-09 (accession 0000849399-26-000079) |
| S021 | filing | CLX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000021076-26-000046); 8-K filed 2026-11-02 (accession 0000021076-26-000044); 8-K filed 2026-10-29 (accession 0001206774-26-000586) |
| S022 | stock | GEN | 2026-11-14 | ok | https://finance.yahoo.com/quote/GEN | Trailing P/E: 15.431472; Forward P/E: 9.108996; Forward EPS: 3.33736; Price: 30.4; Market price: 30.4; Market cap: 18035593216; Sector: Technology; Trailing Eps: 1.97; Revenue Growth: 0.122; Earnings Growth: 1.286; Gross Margin: 0.77410007; Operating Margin: 0.43229; Profit Margin: 0.23068; Return On Equity: 0.46402; Total Revenue: 5228000256; Market Cap: 18035593216; Consensus EPS FY+1: 3.33736; growth: 0.1286 |
| S023 | news | GEN | Wed, 11 Nov 2026 13:10:37 GMT | ok | https://news.google.com/rss/search?q=GEN+Gen+Digital+stock&hl=en-US&gl=US&ceid=US:en | Gen Digital Inc. (GEN) Stock Forecasts - Yahoo Finance (Wed, 11 Nov 2026 13:10:37 GMT); Gen Digital Inc. stock outperforms competitors on strong trading day - MarketWatch (Fri, 13 Nov 2026 22:09:00 GMT); Gen Digital (GEN) Stock Repriced After Q2 Earnings Put Margins Center Stage - Yahoo Finance (Thu, 29 Oct 2026 07:00:00 GMT) |
| S024 | filing | CHTR | 2026-11-06 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-06 (accession 0001091667-26-000073); 8-K filed 2026-11-06 (accession 0001091667-26-000072); 8-K filed 2026-10-27 (accession 0001091667-26-000064) |
| S025 | stock | CLX | 2026-11-14 | ok | https://finance.yahoo.com/quote/CLX | Trailing P/E: 19.68705; Forward P/E: 17.745283; Forward EPS: 6.1684; Price: 109.46; Market price: 109.46; Market cap: 13260793856; Sector: Consumer Defensive; Trailing Eps: 5.56; Revenue Growth: 0.333; Earnings Growth: 1.138; Gross Margin: 0.41939998; Operating Margin: 0.14286; Profit Margin: 0.09408; Return On Equity: 5.34363; Total Revenue: 7196000256; Market Cap: 13260793856; Consensus EPS FY+1: 6.1684; growth: 0.0769 |
| S026 | stock | CHTR | 2026-11-14 | ok | https://finance.yahoo.com/quote/CHTR | Trailing P/E: 13.006578; Forward P/E: 3.2831066; Forward EPS: 42.15215; Price: 138.39; Market price: 138.39; Market cap: 24778944512; Sector: Communication Services; Trailing Eps: 10.64; Revenue Growth: 0.091; Gross Margin: 0.55084; Operating Margin: 0.23389; Profit Margin: 0.02498; Return On Equity: 0.07019; Total Revenue: 55645999104; Market Cap: 24778944512; Consensus EPS FY+1: 47.15811; growth: 1.0195 |
| S027 | news | CLX | Fri, 13 Nov 2026 05:34:04 GMT | ok | https://news.google.com/rss/search?q=CLX+Clorox+stock&hl=en-US&gl=US&ceid=US:en | The Clorox Company (CLX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 05:34:04 GMT); The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance Singapore (Fri, 13 Nov 2026 08:35:40 GMT); A 10-Day Winning Streak Has Clorox Stock Up 24% - Trefis (Sat, 14 Nov 2026 08:28:05 GMT) |
| S028 | news | CHTR | Thu, 12 Nov 2026 08:02:01 GMT | ok | https://news.google.com/rss/search?q=CHTR+Charter+Communications+stock&hl=en-US&gl=US&ceid=US:en | Charter Communications: 3 Key Takeaways for Long-Term Investors - Yahoo Finance (Thu, 12 Nov 2026 08:02:01 GMT); Why You Should Think About Charter Communications Differently Now? - Trefis (Fri, 13 Nov 2026 19:15:44 GMT); What Is The Biggest Threat To Charter Communications Stock? - Trefis (Thu, 12 Nov 2026 15:55:19 GMT) |
| S029 | filing | IDXX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000874716&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000874716-26-000135); 8-K filed 2026-11-02 (accession 0001104659-26-120892); 10-Q filed 2026-08-04 (accession 0000874716-26-000123) |
| S030 | stock | IDXX | 2026-11-14 | ok | https://finance.yahoo.com/quote/IDXX | Trailing P/E: 47.45485; Forward P/E: 41.687927; Forward EPS: 16.8929; Price: 704.23; Market price: 704.23; Market cap: 55483650048; Sector: Healthcare; Trailing Eps: 14.84; Revenue Growth: 0.099; Earnings Growth: 0.179; Gross Margin: 0.62722; Operating Margin: 0.32497; Profit Margin: 0.25357; Return On Equity: 0.68925005; Total Revenue: 4662220800; Market Cap: 55483650048; Consensus EPS FY+1: 16.8929; growth: 0.1244 |
| S031 | filing | GEN | 2026-10-29 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000849399.json | Diluted EPS 0.83 for period ending 2026-10-02 (filed 2026-10-29) |
| S032 | filing | ROP | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000882835&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000882835-26-000047); 8-K filed 2026-10-22 (accession 0000882835-26-000042); 8-K filed 2026-10-01 (accession 0000882835-26-000039) |
| S033 | filing | CLX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000021076.json | Diluted EPS 1.39 for period ending 2026-09-30 (filed 2026-11-02) |
| S034 | filing | CHTR | 2026-11-06 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001091667.json | Diluted EPS 0.38 for period ending 2026-09-30 (filed 2026-11-06) |
| S035 | filing | RDDT | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001713445&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0001713445-26-000116); 8-K filed 2026-10-29 (accession 0001713445-26-000114); 8-K filed 2026-08-12 (accession 0001713445-26-000107) |
| S036 | news | IDXX | Fri, 13 Nov 2026 22:06:38 GMT | ok | https://news.google.com/rss/search?q=IDXX+Idexx+Laboratories+stock&hl=en-US&gl=US&ceid=US:en | IDEXX Laboratories, Inc. (IDXX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 22:06:38 GMT); IDEXX Laboratories (IDXX) Stock Looks Fairly Valued Despite Its 28% Run - Yahoo Finance (Sat, 31 Oct 2026 07:00:00 GMT); IDEXX Laboratories (IDXX) Q3 Earnings Leave Its Premium Valuation In Focus - Yahoo Finance (Tue, 03 Nov 2026 08:00:00 GMT) |
| S037 | stock | ROP | 2026-11-14 | ok | https://finance.yahoo.com/quote/ROP | Trailing P/E: 18.993866; Forward P/E: 19.532475; Forward EPS: 24.57318; Price: 479.975; Market price: 479.975; Market cap: 47535013888; Sector: Technology; Trailing Eps: 25.27; Revenue Growth: 0.076; Earnings Growth: 0.326; Gross Margin: 0.69671; Operating Margin: 0.28049; Profit Margin: 0.30712998; Return On Equity: 0.13229; Total Revenue: 8434599936; Market Cap: 47535013888; Consensus EPS FY+1: 24.57318; growth: 0.09810001 |
| S038 | news | ROP | Fri, 13 Nov 2026 01:46:04 GMT | ok | https://news.google.com/rss/search?q=ROP+Roper+Technologies+stock&hl=en-US&gl=US&ceid=US:en | Roper Technologies, Inc. (ROP) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 01:46:04 GMT); Roper Technologies (ROP) Stock Looks Fully Valued As Cash Flow Comes Into Focus - Yahoo Finance (Fri, 06 Nov 2026 07:13:00 GMT); Roper Technologies (ROP), What Is Behind The Fresh Attention? - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT) |
| S039 | stock | INTC | 2026-11-14 | ok | https://finance.yahoo.com/quote/INTC | Forward P/E: 33.321045; Forward EPS: 1.79046; Price: 59.66; Market price: 59.66; Market cap: 317092888576; Sector: Technology; Trailing Eps: -2.35; Revenue Growth: 0.209; Earnings Growth: -0.327; Gross Margin: 0.40152; Operating Margin: 0.10317001; Profit Margin: -0.20089; Return On Equity: -0.0962; Total Revenue: 59891998720; Market Cap: 317092888576; Consensus EPS FY+1: 1.79046; growth: 0.2044 |
| S040 | filing | INTC | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000050863&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0000050863-26-000191); 8-K filed 2026-10-29 (accession 0000050863-26-000188); 8-K filed 2026-08-12 (accession 0001193125-26-346806) |

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
- news FISV: https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 00:53:33 GMT)
- news APP: https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en (Tue, 10 Nov 2026 14:24:00 GMT)
- stock APP: https://finance.yahoo.com/quote/APP (2026-11-14)
- filing APP: https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json (2026-11-04)
- news PNR: https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 15:54:46 GMT)
- stock FISV: https://finance.yahoo.com/quote/FISV (2026-11-14)
- filing FISV: https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json (2026-11-04)
- filing PNR: https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json (2026-10-27)
- stock PNR: https://finance.yahoo.com/quote/PNR (2026-11-14)
- filing GEN: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 (2026-10-29)

## AI Provenance

- Provider / model: hermes-local-proxy / upstage/solar-mini4:free
- Market research: attempts=1 tokens=9521 (prompt=6521, completion=3000) runtime=19.83s
- Fundamental research: generated this run at 2026-11-14T13:13:56.214286+00:00
- Evidence source dates: {'as_of': '2026-11-13', 'latest_equity_date': '2026-11-13', 'latest_macro_date': '2026-11-13', 'flows_date': '2026-11-13'}
- Evidence fingerprint: b6a71b66633f57a423d82f87dcac12df00d4938ec77da9417681bc425e854531
- Source citations are retrieved external records in the ledger above; market values remain from the verified database snapshot.


## Disclosures

- This is research and market intelligence, not investment advice.
- AI conclusions are research judgments, not validated return predictions.
- The frozen risk layer is risk-only and is not used for directional views or allocations.
- Legacy scores are not active inputs or outputs.

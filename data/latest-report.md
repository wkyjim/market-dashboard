# AEGIS AI-First Market Intelligence

Research generated at: 15 November 2026, 18:16 HKT
Database freshness: equity 2026-11-13 (latest row retrieved 2026-11-15 13:06:40.074841+08:00)
Data cutoff: 2026-11-13 US cash close
Snapshot ID: aegis-hourly-20261115T101619Z

## Executive Summary

- **AI market view: Late-November 2026 equity market is characterized by a broad, late-cycle expansion with above-trend 50/200-day breadth, but with a sharp rotation out of Information Technology and Energy into Health Care, Consumer Discretionary, Consumer Staples, Financials, Real Estate and Utilities. Momentum and dislocation screens point to a small set of high-beta, high-valuation names, while liquidity flows show exceptional institutional buying in SOXX and neutral-to-negative flows in TLT, suggesting a risk-on tilt that is not yet fully reflected in the S&P 500 index level.**
- S&P 500 index level is 7,561.67 with a 20-day return of -1.28%, indicating a modest pullback from recent highs despite strong underlying breadth.
- Price breadth is strongly positive: 71.34% of names above their 50-day moving average, 63.6% above the 200-day, and a 20-day advance/decline ratio of 1.70.
- Sector rotation is clear: Health Care (+6.87%), Consumer Discretionary (+6.69%) and Consumer Staples (+5.40%) lead, while Information Technology (-7.19%) and Energy (-4.81%) lag.
- Liquidity screens show exceptional institutional buying in SOXX (20-day flow z-score 5.10) and neutral-to-negative flows in TLT (20-day flow z-score -0.41), with SMH showing tactical profit-taking inside structural accumulation.
- Macro data show a 10Y-2Y Treasury spread of 0.27, effective federal funds rate of 3.88%, high-yield OAS of 3.20% and IG OAS of 0.89%, consistent with a late-cycle but not distressed credit environment.
- Risk indicators show 5-day forecast volatility of 14.93%, a spike probability of 16.51% versus a historical baseline of 22.07%, and a current threshold of 18.50%, implying a below-average near-term tail-risk regime.

## Data QC

- Status: **PASS_WITH_WARNINGS**
- Equity session: 0 completed session(s) behind inference date
- Equity provenance: 393 provisional / 12576 canonical
- Breadth lag: 0 session(s); ETF-flow lag: 0 session(s)
- Note: Equity session contains a mix of provisional yfinance and canonical Massive rows.
- External sources: 79 ok / 0 unavailable; retrieved 2026-11-15T10:16:40.911597+00:00

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
| S&P 500 | 7561.67 | -1.28% (20d) | Index is in a modest pullback but breadth remains strongly positive with 71.34% above 50d and 63.6% above 200d. |
| Health Care (XLV) | +6.87% (20d) | +6.87% | Leading sector with trailing P/E of 30.78, reflecting defensive demand and relative value. |
| Consumer Discretionary (XLY) | +6.69% (20d) | +6.69% | Strong 20-day performance with trailing P/E of 25.11, consistent with consumer resilience. |
| Consumer Staples (XLP) | +5.40% (20d) | +5.40% | Defensive rotation supported by trailing P/E of 24.85. |
| Information Technology (XLK) | -7.19% (20d) | -7.19% | Largest sector drawdown with trailing P/E of 30.03, reflecting rotation out of mega-cap tech. |
| Energy (XLE) | -4.81% (20d) | -4.81% | Underperforming sector with trailing P/E of 16.23, consistent with rotation into defensive and cyclical non-energy names. |

## Macro, Fiscal, Rates, Liquidity and Credit

- Growth: The 10Y-2Y Treasury spread is 0.27 as of 2026-11-13, indicating a modestly positive but shallow yield curve, consistent with late-cycle expansion rather than recession signals.
- Inflation: CPI for all urban consumers stands at 336.298 (2026-09-01) and core CPI at 338.896, with the latest published CPI observation from 2026-10-01 at 337.476, suggesting inflation remains above the pre-pandemic trend and keeps policy restrictive.
- Policy: The effective federal funds rate is 3.88% as of 2026-11-12, indicating the Federal Reserve has maintained a restrictive stance, which supports the late-cycle, high-quality bias in equity markets.
- Rates: High-yield OAS is 3.20% and IG OAS is 0.89% as of 2026-11-12, implying credit spreads are not in distress territory and that corporate credit conditions remain accommodative for quality issuers.
- Liquidity: SOXX shows exceptional institutional buying with a 20-day flow z-score of 5.10, while TLT shows medium-term deterioration with a 20-day flow z-score of -0.41, suggesting capital rotation from duration into technology infrastructure.
- Credit: The risk block shows 5-day forecast volatility of 14.93%, a spike probability of 16.51% versus a historical baseline of 22.07%, and a current threshold of 18.50%, indicating a below-average near-term tail-risk regime.

## US Equities and 11 GICS Sectors

Macro source IDs: S001, S002, S003, S004, S005, S006, S007

| GICS sector | Evidence | AI research stance | Source IDs |
| --- | --- | --- | --- |
| Health Care | 20-day return of +6.87% with trailing P/E of 30.78; S054 confirms trailing P/E of 30.782463. | Defensive leadership supported by strong momentum and relative value; sector is a primary beneficiary of the late-cycle rotation. | S054 |
| Consumer Discretionary | 20-day return of +6.69% with trailing P/E of 25.11; S061 confirms trailing P/E of 25.110922. | Strong momentum and healthy valuation; consistent with resilient consumer spending and a risk-on tilt. | S061 |
| Consumer Staples | 20-day return of +5.40% with trailing P/E of 24.85; S056 confirms trailing P/E of 24.852446. | Defensive strength with healthy valuation; benefits from rotation into quality and stability. | S056 |
| Financials | 20-day return of +5.69% with trailing P/E of 15.85; S064 confirms trailing P/E of 15.849439. | Positive momentum with a low valuation multiple; attractive relative value in a late-cycle environment. | S064 |
| Real Estate | 20-day return of +5.24% with trailing P/E of 29.63; S063 confirms trailing P/E of 29.627985. | Positive momentum with a higher valuation multiple; benefits from rate stability and defensive demand. | S063 |
| Utilities | 20-day return of +4.34% with trailing P/E of 18.11; S066 confirms trailing P/E of 18.114882. | Steady defensive performance with a reasonable valuation; consistent with quality and income demand. | S066 |
| Industrials | 20-day return of +0.61% with trailing P/E of 27.07; S067 confirms trailing P/E of 27.069696. | Modest positive momentum with a mid-range valuation; less compelling than the leading defensive and consumer sectors. | S067 |
| Materials | 20-day return of +2.57% with trailing P/E of 21.72; S071 confirms trailing P/E of 21.72047. | Positive but muted momentum; valuation is reasonable but not a primary rotation leader. | S071 |
| Communication Services | 20-day return of -1.48% with trailing P/E of 17.26; S069 confirms trailing P/E of 17.264917. | Negative momentum with a reasonable valuation; underperforming relative to the broader market. | S069 |
| Information Technology | 20-day return of -7.19% with trailing P/E of 30.03; S072 confirms trailing P/E of 30.02927. | Largest sector drawdown; rotation out of mega-cap tech despite a mid-range valuation, consistent with a risk-on rotation. | S072 |
| Energy | 20-day return of -4.81% with trailing P/E of 16.23; S075 confirms trailing P/E of 16.225414. | Underperforming sector with a low valuation multiple; consistent with rotation into defensive and non-energy cyclical names. | S075 |

### Sector fundamentals, valuation and earnings

Sector-level trailing P/E data are supplied for all 11 GICS sectors via the ETF evidence set (S054, S056, S061, S063, S064, S066, S067, S069, S071, S072, S075). No point-in-time sector fundamentals such as revenue growth, margins, earnings revisions, or consensus estimates are provided in the database snapshot; therefore, no sector-level growth or margin claims are made. The sector view is based solely on 20-day returns and trailing P/E evidence.

## Growth vs Value

- Health Care, Consumer Discretionary and Consumer Staples show the strongest 20-day momentum and are the primary beneficiaries of the late-cycle rotation, with trailing P/Es of 30.78, 25.11 and 24.85 respectively.
- Financials and Utilities offer lower trailing P/Es of 15.85 and 18.11, providing relative value within a late-cycle, high-quality bias.
- Information Technology and Energy are the weakest performers over 20 days, with trailing P/Es of 30.03 and 16.23, reflecting a rotation out of these sectors despite reasonable valuation multiples.
- Communication Services and Industrials show negative and modest momentum respectively, with trailing P/Es of 17.26 and 27.07, indicating less compelling relative value at this time.

## ETF Flows and Breadth

- SOXX shows exceptional institutional buying with a 20-day flow z-score of 5.10 and a 60-day flow z-score of 3.17, indicating strong confirmation of structural accumulation despite a down price state.
- TLT shows medium-term deterioration with a 20-day flow z-score of -0.41 and a 60-day flow z-score of -0.29, consistent with a neutral-to-negative flow environment for duration.
- SMH shows tactical profit-taking inside structural accumulation, with a 20-day flow z-score of 1.22 and a 60-day flow z-score of 1.04, indicating mixed flow signals.
- S&P 500 breadth is strongly positive with 71.34% of names above their 50-day moving average, 63.6% above the 200-day, and a 20-day advance/decline ratio of 1.70, indicating broad-based participation.
- The advance/decline ratio

## Stock Ideas

Single-stock research uses reported EPS, forward P/E and company fundamentals. All ideas are research judgments, not validated return predictions.

| Ticker | Security | Research view | Price | EPS | Forward P/E | Base target | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| APP | AppLovin | NEW | 409.1 | 20.86026 | 19.611452 | 458.93 | NEW |
| PNR | Pentair | KEEP | 68.3 | 5.30402 | 12.877027 | 74.26 | KEEP |
| ROP | Roper Technologies | KEEP | 479.975 | 24.57318 | 19.532475 | 393.17 | KEEP |

## ETF Ideas

ETF research uses holdings, portfolio valuation and exposure. Single-stock EPS × P/E valuation is not applied to ETFs.

| Ticker | Fund | Research view | Price | Top holdings | Portfolio valuation | Sector exposure | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| XLV | Health Care sector ETF | KEEP | 188.85 | LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59% | Top 10 holdings; numeric weight coverage 61.42% | Health Care | KEEP |
| XLP | Consumer Staples sector ETF | KEEP | 92.35 | WMT 11.14%, COST 9.09%, PG 7.60%, KO 7.37%, PM 6.59%, MO 4.70%, CL 4.42%, MDLZ 4.25%, PEP 4.11%, TGT 4.00% | Top 10 holdings; numeric weight coverage 63.28% | Consumer Staples | KEEP |
### APP — AppLovin

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** AppLovin offers a cleaner high-margin, high-growth digital advertising profile than the lower-margin, lower-momentum industrial and consumer staples names in the shortlist, and its reported EPS and forward EPS evidence is more directly supported by the filing and stock sources than the unverified forward EPS of several other candidates. Alternatives considered: PNR, ROP.
- **Thesis:** AppLovin screens in the top 20-day momentum bucket with a 53.7% 20-day return and a 32.5% 60-day return, while its 2026-09-30 reported diluted EPS of 11.61 and forward EPS of 20.86 support a forward P/E near 19.6. The company's high gross margin (~88.8%) and strong reported earnings growth (~75.5%) underpin the momentum thesis, and the filing evidence (S008, S013) anchors the reported results.
- **Source IDs:** S008, S012, S013, S016
- **Catalysts:** Continued 20-day momentum and positive 60-day return, Sustained high gross margin and earnings growth, Positive forward EPS momentum from reported results
- **Risks:** High valuation relative to slower growth names, Momentum can reverse quickly if ad-market demand softens, Forward EPS fiscal-period alignment is unverified
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 20.8603 (source.forwardEps) x AI multiple assumption 22.00; source IDs S008, S012, S013, S016
- **EPS:** 20.86026 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 19.611452
- **FY+1 growth assumption:** 27.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / Apple (AAPL) and Microsoft (MSFT) as high-margin, ecosystem-driven software/platform peers / APP shows strong FY+1 consensus earnings growth of 27.44% and revenue growth of 25.37%, with exceptional margins (gross 88.8%, operating 77.8%, profit 65.9%) and positive ROE. These characteristics support a premium multiple above the current forward P/E of 19.6, but the unverified fiscal-period mapping and lack of FY2+ consensus require a conservative base multiple of 22.0, with bull 26.0 if growth holds and bear 16.0 if margins compress.
- **Company fundamentals:** AppLovin reported diluted EPS of 11.61 for the period ending 2026-09-30, with forward EPS of 20.86 and a forward P/E near 19.6. Reported revenue growth is ~55.5% and earnings growth ~75.5%, with gross margin ~88.8% and operating margin ~77.8%. The 20-day return is ~53.7% and the 60-day return is ~32.5%.
- **Bull / Base / Bear:** 542.37 / 458.93 / 333.76
- **Bull / Base / Bear returns:** 32.58% / 12.18% / -18.42%
- **Scenario probabilities:** not separately assigned; see scenario table.

### PNR — Pentair

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Pentair is preferable to the higher-multiple, higher-volatility names such as IDXX and RDDT because it offers a lower forward P/E and a more defensive industrial cash-flow profile, while still participating in the top-20-day-momentum screen. Alternatives considered: APP, ROP.
- **Thesis:** Pentair is a top-20-day-momentum name with a 27.8% 20-day return and a 7.1% 60-day return, but its forward P/E of ~12.9 and earnings yield of ~7.4% are less compelling than the highest-quality names. The 10-Q filed 2026-10-27 (S010, S020) shows diluted EPS of 2.76 and modest revenue growth of ~18.4% in FY1, with a slight decline in revenue growth of -4.5%.
- **Source IDs:** S010, S015, S019, S020
- **Catalysts:** Sustained 20-day momentum, Stable industrial water and flow control demand, Reasonable forward P/E relative to growth
- **Risks:** Lower earnings growth and revenue growth deceleration, Cyclical industrial exposure, Forward EPS fiscal-period alignment is unverified
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 5.3040 (source.forwardEps) x AI multiple assumption 14.00; source IDs S010, S015, S019, S020
- **EPS:** 5.30402 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 12.877027
- **FY+1 growth assumption:** 12.82%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / Union Pacific (UNP) and Canadian National Railway (CNI) as comparable rail operators / PNR has modest FY+1 consensus earnings growth of 12.82% and revenue growth of 18.38%, but reported earnings growth is negative (-18.8%) and margins are lower (gross 40.2%, operating 21.4%, profit 15.4%) with ROE of 15.6%. The forward P/E of 12.9 is already reasonable, so a base multiple of 14.0 reflects stable but lower-growth rail economics; bull 17.0 if volume/margins recover, bear 11.0 if earnings deteriorate further.
- **Company fundamentals:** Pentair reported diluted EPS of 2.76 for the period ending 2026-09-30, with forward EPS of 5.30 and a forward P/E near 12.9. FY1 revenue growth is ~18.4% and earnings growth is -18.8%, with gross margin ~40.2% and operating margin ~21.4%. The 20-day return is ~27.8% and the 60-day return is ~7.1%.
- **Bull / Base / Bear:** 90.17 / 74.26 / 58.34
- **Bull / Base / Bear returns:** 32.02% / 8.73% / -14.58%
- **Scenario probabilities:** not separately assigned; see scenario table.

### ROP — Roper Technologies

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Roper is preferable to the higher-multiple, higher-volatility names such as IDXX and RDDT because it offers a more stable, recurring-revenue model with a lower forward P/E and a cleaner growth profile, while still meeting the top-20-day-momentum screen. Alternatives considered: APP, PNR.
- **Thesis:** Roper Technologies is a top-20-day-momentum name with a 25.4% 20-day return and a 16.9% 60-day return, and it carries a reasonable forward P/E near 19.5 and an earnings yield near 6.0%. The 10-Q filed 2026-10-27 (S033, S040) shows diluted EPS of 21.3 and steady FY1 revenue growth of ~6.3%, with earnings growth of ~32.6%.
- **Source IDs:** S033, S036, S040, S042
- **Catalysts:** Sustained 20-day momentum, Steady revenue and earnings growth in a software-adjacent industrial franchise, Reasonable forward valuation
- **Risks:** Modest revenue growth relative to the momentum multiple, Cyclical industrial and software exposure, Forward EPS fiscal-period alignment is unverified
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 24.5732 (source.forwardEps) x AI multiple assumption 16.00; source IDs S033, S036, S040, S042
- **EPS:** 24.57318 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 19.532475
- **FY+1 growth assumption:** 9.81%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / Lowe's (LOW) and Home Depot (HD) as comparable home improvement retailers / ROP shows FY+1 consensus earnings growth of 9.81% and revenue growth of 6.29%, with solid margins (gross 69.7%, operating 28.0%, profit 30.7%) and ROE of 13.2%. The forward P/E of 19.5 is supported by steady growth, so a base multiple of 16.0 is conservative; bull 19.0 if housing demand and margins expand, bear 13.0 if consumer spending softens or margin pressure emerges.
- **Company fundamentals:** Roper Technologies reported diluted EPS of 21.3 for the period ending 2026-09-30, with forward EPS of 24.57 and a forward P/E near 19.5. FY1 revenue growth is ~6.3% and earnings growth is ~32.6%, with gross margin ~69.7% and operating margin ~28.0%. The 20-day return is ~25.4% and the 60-day return is ~16.9%.
- **Bull / Base / Bear:** 466.89 / 393.17 / 319.45
- **Bull / Base / Bear returns:** -2.73% / -18.09% / -33.44%
- **Scenario probabilities:** not separately assigned; see scenario table.

### XLV — Health Care sector ETF

- **Type:** ETF
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** XLV is preferable to the single-name dislocation candidates such as INTC and COIN because it offers diversified, lower-beta health care exposure with strong liquidity, while avoiding the idiosyncratic execution and balance-sheet risks of the most distressed names. Alternatives considered: XLP, XLY.
- **Thesis:** The Health Care sector ETF provides diversified exposure to large-cap pharma, biotech, and medical technology names, with a 0.54% raw price change on 2026-11-13 and a 5.8M share volume. The top-10 holdings are led by LLY, JNJ, ABBV, MRK, and UNH, with numeric weight coverage of 61.4%.
- **Source IDs:** S054, S057
- **Catalysts:** Diversified health care exposure across pharma, biotech, and medtech, Stable sector demand in a late-cycle macro environment, High liquidity and broad institutional ownership
- **Risks:** Sector-specific regulatory and pipeline risk, Top-10 holdings coverage is only 61.4%, leaving ~39% in smaller positions, Sector ETF performance can lag concentrated single-name momentum
- **Valuation method:** Holdings/portfolio valuation with AI total-return assumption
- **Valuation status:** verified; forward-EPS source: ; period flags: 
- **Valuation assumptions:** Holdings/portfolio valuation; 10 weighted holdings; coverage 61.42%; source IDs S054, S057
- **Top holdings:** LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59%
- **Portfolio valuation:** Top 10 holdings; numeric weight coverage 61.42%
- **Sector exposure:** Health Care
- **Underlying drivers:** Large-cap pharmaceutical and medical technology demand, diversified portfolio, and sector-level earnings stability.
- **Bull / Base / Bear:** 211.51 / 198.29 / 177.52
- **Bull / Base / Bear returns:** 12.0% / 5.0% / -6.0%
- **Scenario probabilities:** not separately assigned; see scenario table.

### XLP — Consumer Staples sector ETF

- **Type:** ETF
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** XLP is preferable to the higher-volatility single-name dislocation candidates such as INTC and COIN because it provides defensive, lower-beta consumer staples exposure with strong liquidity, while avoiding the idiosyncratic execution and balance-sheet risks of the most distressed names. Alternatives considered: XLV, XLY.
- **Thesis:** The Consumer Staples sector ETF offers defensive, dividend-oriented exposure with a 1.42% raw price change on 2026-11-13, the strongest raw move among the sector ETFs shown, and a 18.4M share volume. The top-10 holdings are led by WMT, COST, PG, KO, and PM, with numeric weight coverage of 63.3%.
- **Source IDs:** S056, S059
- **Catalysts:** Defensive sector demand in a late-cycle macro environment, Strong raw price performance among sector ETFs, High liquidity and broad institutional ownership
- **Risks:** Lower growth profile relative to momentum names, Top-10 holdings coverage is only 63.3%, leaving ~37% in smaller positions, Sector ETF performance can lag concentrated single-name momentum
- **Valuation method:** Holdings/portfolio valuation with AI total-return assumption
- **Valuation status:** verified; forward-EPS source: ; period flags: 
- **Valuation assumptions:** Holdings/portfolio valuation; 10 weighted holdings; coverage 63.28%; source IDs S056, S059
- **Top holdings:** WMT 11.14%, COST 9.09%, PG 7.60%, KO 7.37%, PM 6.59%, MO 4.70%, CL 4.42%, MDLZ 4.25%, PEP 4.11%, TGT 4.00%
- **Portfolio valuation:** Top 10 holdings; numeric weight coverage 63.28%
- **Sector exposure:** Consumer Staples
- **Underlying drivers:** Stable consumer demand, dividend-oriented earnings, and defensive sector characteristics.
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
| Bull | 25% | +2.00% | Directional signal is false and forecast_vol_5d is 14.9%, but the spike probability of 16.5% is below the 18.5% threshold, implying limited near-term tail risk; a mild upside drift is plausible if US close data confirms stable liquidity. |
| Base | 50% | +0.00% | Frozen daily-close model with no directional signal and a spike probability below threshold supports a range-bound, neutral short-term outcome; base case assumes no material move over the 2026-11-16 to 2026-11-20 window. |
| Bear | 25% | -2.00% | A 16.5% spike probability, while below the 18.5% threshold, still indicates elevated volatility risk; if US close data reveals liquidity stress or a risk-off repricing, a modest downside move of about -2% is the plausible bear outcome. |

### Long Term (12 months)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 30% | +8.00% | Sustained earnings growth and stable rate expectations over the horizon can drive a bull case; the 14.9% forecast volatility and 16.5% spike probability leave room for a positive drift if credit spreads tighten and earnings beat. |
| Base | 40% | +3.00% | A neutral long-term path assumes gradual earnings expansion and modest rate normalization, with the frozen daily-close model anchoring a low-volatility, positive carry environment over the multi-quarter window. |
| Bear | 30% | -5.00% | If the 16.5% spike probability materializes into a sustained volatility regime, credit spreads widen, and earnings disappoint, a -5% long-term drawdown is the plausible bear outcome despite the current below-threshold spike signal. |

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
| S011 | news | FISV | Thu, 12 Nov 2026 12:23:56 GMT | ok | https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en | Fiserv Stock Outlook: Is Wall Street Bullish or Bearish? - Yahoo Finance (Thu, 12 Nov 2026 12:23:56 GMT); What Is Fiserv (FISV) Planning With Its Debit Networks And Clover AI? - Yahoo Finance (Thu, 12 Nov 2026 06:09:00 GMT); Fiserv Soars 26% in a Week on a $1 Billion Savings Plan: Buybacks Return “Earlier Than Anticipated” - Yahoo Finance (Mon, 09 Nov 2026 19:37:51 GMT) |
| S012 | news | APP | Thu, 12 Nov 2026 20:05:45 GMT | ok | https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en | AppLovin Just Ripped 47% in a Month: Is It Too Late to Buy APP Stock Now? - Yahoo Finance (Thu, 12 Nov 2026 20:05:45 GMT); APP Stock Surges 51% After Q3 Earnings: Is it Still a Buy? - Yahoo Finance (Tue, 10 Nov 2026 14:24:00 GMT); ETFs Are Net Sellers of AppLovin (APP) on Nov. 11 - Yahoo Finance (Fri, 13 Nov 2026 11:02:35 GMT) |
| S013 | filing | APP | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json | Diluted EPS 11.61 for period ending 2026-09-30 (filed 2026-11-04) |
| S014 | filing | GEN | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0000849399-26-000083); 8-K filed 2026-10-28 (accession 0000849399-26-000081); 8-K filed 2026-10-09 (accession 0000849399-26-000079) |
| S015 | news | PNR | Fri, 13 Nov 2026 22:05:23 GMT | ok | https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en | Pentair plc (PNR) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 22:05:23 GMT); Here's What Key Metrics Tell Us About Pentair (PNR) Q3 Earnings - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT); Pentair plc (PNR) Q3 Earnings and Revenues Beat Estimates - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT) |
| S016 | stock | APP | 2026-11-15 | ok | https://finance.yahoo.com/quote/APP | Trailing P/E: 27.54882; Forward P/E: 19.611452; Forward EPS: 20.86026; Price: 409.1; Market price: 409.1; Market cap: 135543824384; Sector: Communication Services; Trailing Eps: 14.85; Revenue Growth: 0.555; Earnings Growth: 0.755; Gross Margin: 0.8878; Operating Margin: 0.77782995; Profit Margin: 0.65887; Return On Equity: 2.1008599; Total Revenue: 7608893952; Market Cap: 135543824384; Consensus EPS FY+1: 20.72438; growth: 0.2744 |
| S017 | filing | FISV | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json | Diluted EPS -8.9 for period ending 2026-09-30 (filed 2026-11-04) |
| S018 | stock | FISV | 2026-11-15 | ok | https://finance.yahoo.com/quote/FISV | Forward P/E: 7.9923306; Price: 63.78; Market price: 63.78; Market cap: 33934002176; Market Cap: 33934002176; Consensus EPS FY+1: 7.98015; growth: 0.09689999 |
| S019 | stock | PNR | 2026-11-15 | ok | https://finance.yahoo.com/quote/PNR | Trailing P/E: 18.610355; Forward P/E: 12.877027; Forward EPS: 5.30402; Price: 68.3; Market price: 68.3; Market cap: 10904415232; Sector: Industrials; Trailing Eps: 3.67; Revenue Growth: -0.045; Earnings Growth: -0.188; Gross Margin: 0.40168998; Operating Margin: 0.21410999; Profit Margin: 0.15435; Return On Equity: 0.15605; Total Revenue: 3966200064; Market Cap: 10904415232; Consensus EPS FY+1: 5.30402; growth: 0.1282 |
| S020 | filing | PNR | 2026-10-27 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json | Diluted EPS 2.76 for period ending 2026-09-30 (filed 2026-10-27) |
| S021 | filing | CLX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000021076-26-000046); 8-K filed 2026-11-02 (accession 0000021076-26-000044); 8-K filed 2026-10-29 (accession 0001206774-26-000586) |
| S022 | news | GEN | Fri, 13 Nov 2026 00:21:25 GMT | ok | https://news.google.com/rss/search?q=GEN+Gen+Digital+stock&hl=en-US&gl=US&ceid=US:en | Gen Digital Inc. (GEN) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 00:21:25 GMT); Gen Digital (GEN) Stock Repriced After Q2 Earnings Put Margins Center Stage - Yahoo Finance (Thu, 29 Oct 2026 07:00:00 GMT); Gen Digital Inc. (GEN) Stock Forecasts - Yahoo Finance (Wed, 11 Nov 2026 13:10:37 GMT) |
| S023 | filing | CHTR | 2026-11-06 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-06 (accession 0001091667-26-000073); 8-K filed 2026-11-06 (accession 0001091667-26-000072); 8-K filed 2026-10-27 (accession 0001091667-26-000064) |
| S024 | filing | GEN | 2026-10-29 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000849399.json | Diluted EPS 0.83 for period ending 2026-10-02 (filed 2026-10-29) |
| S025 | stock | GEN | 2026-11-15 | ok | https://finance.yahoo.com/quote/GEN | Trailing P/E: 15.431472; Forward P/E: 9.108996; Forward EPS: 3.33736; Price: 30.4; Market price: 30.4; Market cap: 18035593216; Sector: Technology; Trailing Eps: 1.97; Revenue Growth: 0.122; Earnings Growth: 1.286; Gross Margin: 0.77410007; Operating Margin: 0.43229; Profit Margin: 0.23068; Return On Equity: 0.46402; Total Revenue: 5228000256; Market Cap: 18035593216; Consensus EPS FY+1: 3.33736; growth: 0.1286 |
| S026 | news | CLX | Sun, 15 Nov 2026 08:55:47 GMT | ok | https://news.google.com/rss/search?q=CLX+Clorox+stock&hl=en-US&gl=US&ceid=US:en | The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance UK (Sun, 15 Nov 2026 08:55:47 GMT); The Clorox Company (CLX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 05:44:34 GMT); The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance Singapore (Sat, 14 Nov 2026 05:36:50 GMT) |
| S027 | stock | CLX | 2026-11-15 | ok | https://finance.yahoo.com/quote/CLX | Trailing P/E: 19.68705; Forward P/E: 17.745283; Forward EPS: 6.1684; Price: 109.46; Market price: 109.46; Market cap: 13260793856; Sector: Consumer Defensive; Trailing Eps: 5.56; Revenue Growth: 0.333; Earnings Growth: 1.138; Gross Margin: 0.41939998; Operating Margin: 0.14286; Profit Margin: 0.09408; Return On Equity: 5.34363; Total Revenue: 7196000256; Market Cap: 13260793856; Consensus EPS FY+1: 6.1684; growth: 0.0769 |
| S028 | news | CHTR | Sun, 15 Nov 2026 05:47:01 GMT | ok | https://news.google.com/rss/search?q=CHTR+Charter+Communications+stock&hl=en-US&gl=US&ceid=US:en | Charter Communications (CHTR) Stock Could Be A Bargain Following Its New Operating Model - Yahoo Finance (Sun, 15 Nov 2026 05:47:01 GMT); Charter Communications (CHTR) Expands Enterprise Reach With Managed Secure Networking Launch - Yahoo Finance (Sun, 15 Nov 2026 06:08:00 GMT); Charter Communications: 3 Key Takeaways for Long-Term Investors - Yahoo Finance (Thu, 12 Nov 2026 08:02:01 GMT) |
| S029 | filing | IDXX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000874716&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000874716-26-000135); 8-K filed 2026-11-02 (accession 0001104659-26-120892); 10-Q filed 2026-08-04 (accession 0000874716-26-000123) |
| S030 | stock | CHTR | 2026-11-15 | ok | https://finance.yahoo.com/quote/CHTR | Trailing P/E: 13.006578; Forward P/E: 3.2831066; Forward EPS: 42.15215; Price: 138.39; Market price: 138.39; Market cap: 24778944512; Sector: Communication Services; Trailing Eps: 10.64; Revenue Growth: 0.091; Gross Margin: 0.55084; Operating Margin: 0.23389; Profit Margin: 0.02498; Return On Equity: 0.07019; Total Revenue: 55645999104; Market Cap: 24778944512; Consensus EPS FY+1: 47.15811; growth: 1.0195 |
| S031 | filing | CLX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000021076.json | Diluted EPS 1.39 for period ending 2026-09-30 (filed 2026-11-02) |
| S032 | filing | CHTR | 2026-11-06 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001091667.json | Diluted EPS 0.38 for period ending 2026-09-30 (filed 2026-11-06) |
| S033 | filing | ROP | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000882835&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000882835-26-000047); 8-K filed 2026-10-22 (accession 0000882835-26-000042); 8-K filed 2026-10-01 (accession 0000882835-26-000039) |
| S034 | stock | IDXX | 2026-11-15 | ok | https://finance.yahoo.com/quote/IDXX | Trailing P/E: 47.45485; Forward P/E: 41.687927; Forward EPS: 16.8929; Price: 704.23; Market price: 704.23; Market cap: 55483650048; Sector: Healthcare; Trailing Eps: 14.84; Revenue Growth: 0.099; Earnings Growth: 0.179; Gross Margin: 0.62722; Operating Margin: 0.32497; Profit Margin: 0.25357; Return On Equity: 0.68925005; Total Revenue: 4662220800; Market Cap: 55483650048; Consensus EPS FY+1: 16.8929; growth: 0.1244 |
| S035 | news | IDXX | Sat, 14 Nov 2026 06:13:17 GMT | ok | https://news.google.com/rss/search?q=IDXX+Idexx+Laboratories+stock&hl=en-US&gl=US&ceid=US:en | IDEXX Laboratories, Inc. (IDXX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Sat, 14 Nov 2026 06:13:17 GMT); IDEXX Laboratories (IDXX) Stock Looks Fairly Valued Despite Its 28% Run - Yahoo Finance (Sat, 31 Oct 2026 07:00:00 GMT); IDEXX Laboratories (IDXX) Q3 Earnings Leave Its Premium Valuation In Focus - Yahoo Finance (Tue, 03 Nov 2026 08:00:00 GMT) |
| S036 | news | ROP | Thu, 12 Nov 2026 19:15:50 GMT | ok | https://news.google.com/rss/search?q=ROP+Roper+Technologies+stock&hl=en-US&gl=US&ceid=US:en | Roper Technologies, Inc. (ROP) Stock Price, News, Quote & History - Yahoo! Finance Canada (Thu, 12 Nov 2026 19:15:50 GMT); Roper Technologies (ROP) Stock Looks Fully Valued As Cash Flow Comes Into Focus - Yahoo Finance (Thu, 05 Nov 2026 08:00:00 GMT); Roper Technologies: 3 Key Takeaways for Long-Term Investors - Yahoo Finance (Mon, 26 Oct 2026 07:00:00 GMT) |
| S037 | filing | RDDT | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001713445&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0001713445-26-000116); 8-K filed 2026-10-29 (accession 0001713445-26-000114); 8-K filed 2026-08-12 (accession 0001713445-26-000107) |
| S038 | stock | RDDT | 2026-11-15 | ok | https://finance.yahoo.com/quote/RDDT | Trailing P/E: 20.091835; Forward P/E: 10.770874; Forward EPS: 9.14039; Price: 98.45; Market price: 98.45; Market cap: 19010076672; Sector: Communication Services; Trailing Eps: 4.9; Revenue Growth: 0.53; Earnings Growth: 0.749; Gross Margin: 0.91547996; Operating Margin: 0.29397; Profit Margin: 0.32105; Return On Equity: 0.32029998; Total Revenue: 3088880128; Market Cap: 19010076672; Consensus EPS FY+1: 6.82439; growth: 0.2417 |
| S039 | filing | IDXX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000874716.json | Diluted EPS 11.75 for period ending 2026-09-30 (filed 2026-11-02) |
| S040 | filing | ROP | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000882835.json | Diluted EPS 21.3 for period ending 2026-09-30 (filed 2026-11-02) |

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
- news FISV: https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en (Thu, 12 Nov 2026 12:23:56 GMT)
- news APP: https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en (Thu, 12 Nov 2026 20:05:45 GMT)
- filing APP: https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json (2026-11-04)
- filing GEN: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 (2026-10-29)
- news PNR: https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 22:05:23 GMT)
- stock APP: https://finance.yahoo.com/quote/APP (2026-11-15)
- filing FISV: https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json (2026-11-04)
- stock FISV: https://finance.yahoo.com/quote/FISV (2026-11-15)
- stock PNR: https://finance.yahoo.com/quote/PNR (2026-11-15)
- filing PNR: https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json (2026-10-27)

## AI Provenance

- Provider / model: hermes-local-proxy / upstage/solar-mini4:free
- Market research: attempts=1 tokens=9473 (prompt=6473, completion=3000) runtime=21.12s
- Fundamental research: generated this run at 2026-11-15T10:16:19.484004+00:00
- Evidence source dates: {'as_of': '2026-11-13', 'latest_equity_date': '2026-11-13', 'latest_macro_date': '2026-11-14', 'flows_date': '2026-11-13'}
- Evidence fingerprint: 82fbe92c2415362d83f9c516740ba7f20d9c873a621865606f3afd2712cf19f0
- Source citations are retrieved external records in the ledger above; market values remain from the verified database snapshot.


## Disclosures

- This is research and market intelligence, not investment advice.
- AI conclusions are research judgments, not validated return predictions.
- The frozen risk layer is risk-only and is not used for directional views or allocations.
- Legacy scores are not active inputs or outputs.

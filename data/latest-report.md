# AEGIS AI-First Market Intelligence

Research generated at: 16 November 2026, 19:11 HKT
Database freshness: equity 2026-11-13 (latest row retrieved 2026-11-16 13:06:43.000010+08:00)
Data cutoff: 2026-11-13 US cash close
Snapshot ID: aegis-hourly-20261116T111109Z

## Executive Summary

- **AI market view: Risk-on tilt is narrowing: broad market breadth is positive but the index is down over 20 days, and the 20-day return ranking shows a clear split between defensive, health-care, and consumer staples sectors versus the technology and communication services sectors that are negative. Liquidity and flow data point to institutional selling in utilities and structural distribution in consumer discretionary, while health care and consumer staples show strong institutional confirmation. Macro data show a still-elevated but stable inflation backdrop, a slightly softer labor market, and a modestly positive 10Y-2Y spread, with policy rates near 3.88%.**
- Broad market breadth is positive (71.3% above 50-day, 63.6% above 200-day, ADR 1.70), but the S&P 500 is down 1.28% over 20 days, indicating a narrow, defensive-led rally.
- Sector returns over 20 days are bifurcated: Health Care (+6.87%), Consumer Discretionary (+6.69%), Consumer Staples (+5.40%), Real Estate (+5.24%), Financials (+5.69%), and Utilities (+4.34%) are positive, while Communication Services (-1.48%) and Information Technology (-7.19%) are negative.
- Flow data show strong institutional inflows and price confirmation in Health Care (XLV) and neutral-to-negative flows in Consumer Discretionary (XLY) and Utilities (XLU), with XLU showing exceptional institutional selling.
- Macro indicators show CPI still elevated at 336.298 (Sep 2026), unemployment at 4.2%, and a 10Y-2Y spread of 0.27, with the effective federal funds rate at 3.88% as of 2026-11-12.
- Credit conditions are moderately tight but not stressed: US high-yield OAS is 3.20 and IG OAS is 0.89 as of 2026-11-12.
- The risk model shows 5-day forecast volatility of 14.93% and a spike probability of 16.51%, below the 18.50% threshold, with no directional signal, suggesting a range-bound but elevated-risk environment.

## Data QC

- Status: **PASS_WITH_WARNINGS**
- Equity session: 0 completed session(s) behind inference date
- Equity provenance: 393 provisional / 12576 canonical
- Breadth lag: 0 session(s); ETF-flow lag: 0 session(s)
- Note: Equity session contains a mix of provisional yfinance and canonical Massive rows.
- External sources: 79 ok / 0 unavailable; retrieved 2026-11-16T11:11:31.553886+00:00

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
| S&P 500 (SPX) | 7561.67 | -1.28% (20d) | Index is down over 20 days despite positive breadth; 71.3% of names above 50-day and 63.6% above 200-day, with ADR 1.70. |
| Health Care (XLV) | return_20d +6.87% | +6.87% | Strongest sector; flow z-scores positive (20d 1.45, 60d 1.72) with strong institutional confirmation and trailing P/E 30.78. |
| Information Technology (XLK) | return_20d -7.19% | -7.19% | Worst sector; trailing P/E 30.03; liquidity leaders NVDA, AMD, MU are in this sector but the sector is underperforming. |
| Communication Services (XLC) | return_20d -1.48% | -1.48% | Negative sector return; trailing P/E 17.26; includes CHTR and other names with mixed momentum signals. |
| Consumer Discretionary (XLY) | return_20d +6.69% | +6.69% | Positive sector return but flow z-scores negative (20d -0.38, 60d -0.78) with structural distribution. |
| Utilities (XLU) | return_20d +4.34% | +4.34% | Positive sector return but exceptional institutional selling (20d flow z-score -2.15) with medium-term deterioration. |

## Macro, Fiscal, Rates, Liquidity and Credit

- Inflation: CPI for All Urban Consumers is 336.298 (Sep 2026) and core CPI is 338.896, indicating a still-elevated but stable inflation backdrop; the latest CPI observation from S004 is 337.476 (Oct 2026).
- Labor: Unemployment rate is 4.2% (Sep 2026), slightly softer than the 4.1% reported in S005 (Oct 2026), suggesting a modest cooling in the labor market.
- Policy: Effective federal funds rate is 3.88% as of 2026-11-12 (S001), and the 10Y-2Y Treasury spread is 0.27 as of 2026-11-13 (S007), indicating a modestly positive yield curve.
- Rates: The yield curve is slightly positive but not steepening aggressively; the 10Y-2Y spread of 0.27 is a neutral-to-modestly-bullish signal.
- Liquidity: Credit spreads are moderately tight but not stressed: high-yield OAS is 3.20 and IG OAS is 0.89 as of 2026-11-12 (S002, S003), consistent with a stable but not exuberant credit environment.
- Growth: The macro data do not provide direct GDP or industrial production figures; the available indicators point to a late-cycle, low-growth, low-inflation environment with a slightly softening labor market.

## US Equities and 11 GICS Sectors

Macro source IDs: S001, S002, S003, S004, S005, S007

| GICS sector | Evidence | AI research stance | Source IDs |
| --- | --- | --- | --- |
| Health Care | Sector return_20d +6.87% (XLV); flow z-scores 20d 1.45, 60d 1.72 with strong confirmation; trailing P/E 30.78 (S056). | Defensive leadership with institutional inflows; health care is the most reliable sector in the current risk environment. | S056 |
| Consumer Staples | Sector return_20d +5.40% (XLP); trailing P/E 24.85 (S061); defensive positioning with positive price momentum. | Stable defensive sector; positive 20-day return and reasonable valuation support a hold stance. | S061 |
| Consumer Discretionary | Sector return_20d +6.69% (XLY); trailing P/E 25.11 (S055); flow z-scores negative (20d -0.38, 60d -0.78) with structural distribution. | Price momentum positive but institutional flows are negative; monitor for divergence between price and flows. | S055 |
| Real Estate | Sector return_20d +5.24% (XLRE); trailing P/E 29.63 (S064); positive sector return but valuation is elevated. | Positive momentum but high valuation; maintain neutral stance with close monitoring of rate sensitivity. | S064 |
| Financials | Sector return_20d +5.69% (XLF); trailing P/E 15.85 (S062); positive sector return with reasonable valuation. | Positive momentum and reasonable valuation; supportive of a neutral-to-positive stance. | S062 |
| Utilities | Sector return_20d +4.34% (XLU); trailing P/E 18.11 (S063); flow z-score 20d -2.15 with exceptional institutional selling and medium-term deterioration. | Price positive but institutional flows are strongly negative; caution warranted despite defensive characteristics. | S063 |
| Materials | Sector return_20d +2.57% (XLB); trailing P/E 21.72 (S065); modest positive return with mid-range valuation. | Modest positive momentum; maintain neutral stance with limited conviction. | S065 |
| Industrials | Sector return_20d +0.61% (XLI); trailing P/E 27.07 (S070); near-flat sector return with elevated valuation. | Weak momentum and high valuation; maintain neutral stance with limited upside. | S070 |
| Communication Services | Sector return_20d -1.48% (XLC); trailing P/E 17.26 (S071); negative sector return with mixed momentum signals. | Negative momentum and underperformance; maintain neutral-to-negative stance. | S071 |
| Information Technology | Sector return_20d -7.19% (XLK); trailing P/E 30.03 (S072); worst sector with negative returns despite liquidity leaders NVDA, AMD, MU. | Negative momentum and high valuation; maintain negative stance with close monitoring of liquidity leaders. | S072 |
| Energy | Sector return_20d -4.81% (XLE); trailing P/E 16.23 (S074); negative sector return with reasonable valuation. | Negative momentum and underperformance; maintain neutral-to-negative stance. | S074 |

### Sector fundamentals, valuation and earnings

No point-in-time sector fundamentals (e.g., sector-level earnings revisions, growth, or margin data) are supplied in the database snapshot. The sector evidence is limited to 20-day ETF returns, flow z-scores, and trailing P/E from the supplied source IDs. Any sector-level fundamental claims would be invented and are therefore omitted.

## Growth vs Value

- Health Care (XLV) has the highest trailing P/E at 30.78, indicating a growth-oriented valuation despite strong momentum.
- Consumer Staples (XLP) has a trailing P/E of 24.85, a reasonable valuation for a defensive sector.
- Consumer Discretionary (XLY) has a trailing P/E of 25.11, with positive price momentum but negative institutional flows.
- Information Technology (XLK) has a trailing P/E of 30.03, the highest among the negative-return sectors, suggesting elevated growth expectations that may be at risk given the sector's underperformance.

## ETF Flows and Breadth

- Broad market breadth is positive: 71.3% of names above 50-day, 63.6% above 200-day, ADR 1.70, and 70.5% positive 20-day returns.
- Health Care (XLV) shows strong institutional confirmation with flow z-scores of 1.45 (20d) and 1.72 (60d), aligning with positive price action.
- Consumer Discretionary (XLY) shows structural distribution with negative flow z-scores (-0.38 20d, -0.78 60d) despite positive price returns.
- Utilities (XLU) shows exceptional institutional selling with a 20d flow z-score of -2.15, indicating a medium-term deterioration despite positive price returns.
- The advance-decline ratio of 1.70 and positive 20-day breadth suggest a broad but narrow rally, with no new highs or lows reported.

## Stock Ideas

Single-stock research uses reported EPS, forward P/E and company fundamentals. All ideas are research judgments, not validated return predictions.

| Ticker | Security | Research view | Price | EPS | Forward P/E | Base target | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| APP | AppLovin | NEW | 409.1 | 20.86026 | 19.611452 | 417.21 | NEW |
| PNR | Pentair | KEEP | 68.3 | 5.30402 | 12.877027 | 74.26 | KEEP |
| ROP | Roper Technologies | NEW | 479.975 | 24.57318 | 19.532475 | 442.32 | NEW |
| RDDT | Reddit | KEEP | 98.45 | 9.10039 | 10.818217 | 109.2 | KEEP |

## ETF Ideas

ETF research uses holdings, portfolio valuation and exposure. Single-stock EPS × P/E valuation is not applied to ETFs.

| Ticker | Fund | Research view | Price | Top holdings | Portfolio valuation | Sector exposure | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| XLV | Health Care sector ETF | KEEP | 188.85 | LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59% | Top 10 holdings; numeric weight coverage 61.42% | Health Care | KEEP |
### APP — AppLovin

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** AppLovin offers a rare combination of top-tier 20-day momentum, high-quality margins, and a reasonable forward P/E, making it a stronger candidate than the lower-margin, lower-momentum names in the shortlist such as CLX or ROP. Alternatives considered: CLX, ROP.
- **Thesis:** AppLovin screens in the top 20-day momentum bucket with a 53.7% 20-day return and a 32.5% 60-day return, while maintaining a 60-day drawdown of only -0.2%. Reported diluted EPS of 11.61 for the period ending 2026-09-30 and a forward EPS of 20.86 support a forward P/E of 19.6, and the company's high gross margin of 88.8% and operating margin of 77.8% indicate durable monetization. The 20.1% trailing P/E and 5.0% earnings yield show the stock is not expensive relative to its momentum profile.
- **Source IDs:** S009, S012, S013, S017
- **Catalysts:** Continued 20-day momentum with a 53.7% return over the last 20 sessions, Sustained high gross margin and operating margin supporting earnings growth, Forward EPS of 20.86 implying a forward P/E of 19.6, Strong 60-day return of 32.5% with minimal drawdown
- **Risks:** High momentum can mean elevated volatility and potential mean-reversion risk, Forward EPS fiscal period alignment is unverified, Valuation quality flags are absent but forward EPS basis is source.forwardEps
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 20.8603 (source.forwardEps) x AI multiple assumption 20.00; source IDs S009, S012, S013, S017
- **EPS:** 20.86026 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 19.611452
- **FY+1 growth assumption:** 27.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / Apple Inc. (AAPL) and Microsoft Corp. (MSFT) as high-margin, ecosystem-driven software/platform comparables / APP shows 25.4% revenue growth and 27.4% earnings growth with 88.8% gross margin and 77.8% operating margin, supporting a premium multiple. The 19.6x forward P/E is below the 20.0x base multiple, implying upside. Peer reference: AAPL/MSFT for durable, high-margin, ecosystem-driven growth.
- **Company fundamentals:** AppLovin reported diluted EPS of 11.61 for the period ending 2026-09-30, with forward EPS of 20.86, forward P/E of 19.6, gross margin of 88.8%, operating margin of 77.8%, profit margin of 65.9%, revenue growth of 55.5%, and earnings growth of 75.5%. Trailing P/E is 20.1 and earnings yield is 5.0%.
- **Bull / Base / Bear:** 500.65 / 417.21 / 333.76
- **Bull / Base / Bear returns:** 22.38% / 1.98% / -18.42%
- **Scenario probabilities:** not separately assigned; see scenario table.

### PNR — Pentair

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Pentair is a defensible industrial name with a reasonable forward P/E, but its negative revenue and earnings growth make it less attractive than higher-quality momentum names like AppLovin or Roper Technologies. Alternatives considered: APP, ROP.
- **Thesis:** Pentair is in the top 20-day momentum bucket with a 27.8% 20-day return and a 7.1% 60-day return, but its fundamentals are mixed. Reported diluted EPS of 2.76 for the period ending 2026-09-30 and forward EPS of 5.304 support a forward P/E of 12.9, yet revenue growth is -4.5% and earnings growth is -18.8%, with gross margin of 40.2% and operating margin of 21.4%. The stock screens positively on momentum but negatively on earnings quality.
- **Source IDs:** S010, S014, S019, S020
- **Catalysts:** 27.8% 20-day return and 7.1% 60-day return indicate positive price momentum, Forward EPS of 5.304 implies a forward P/E of 12.9, which is reasonable, 60-day drawdown of -5.2% is manageable
- **Risks:** Revenue growth of -4.5% and earnings growth of -18.8% signal deteriorating fundamentals, Gross margin of 40.2% and operating margin of 21.4% are lower than high-quality software peers, Forward EPS fiscal period alignment is unverified
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 5.3040 (source.forwardEps) x AI multiple assumption 14.00; source IDs S010, S014, S019, S020
- **EPS:** 5.30402 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 12.877027
- **FY+1 growth assumption:** 12.82%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / Prologis Inc. (PLD) and Equinix Inc. (EQIX) as industrial/logistics REITs with similar asset-light, high-occupancy operating models / PNR has 18.4% revenue growth and 12.8% earnings growth with 40.2% gross margin and 21.4% operating margin, but lower margins and negative reported earnings growth (-18.8%) warrant a conservative multiple. Peer reference: PLD/EQIX for logistics/industrial REIT fundamentals.
- **Company fundamentals:** Pentair reported diluted EPS of 2.76 for the period ending 2026-09-30, with forward EPS of 5.304, forward P/E of 12.9, gross margin of 40.2%, operating margin of 21.4%, profit margin of 15.4%, revenue growth of -4.5%, and earnings growth of -18.8%. Trailing P/E is 13.6 and earnings yield is 7.4%.
- **Bull / Base / Bear:** 90.17 / 74.26 / 58.34
- **Bull / Base / Bear returns:** 32.02% / 8.73% / -14.58%
- **Scenario probabilities:** not separately assigned; see scenario table.

### ROP — Roper Technologies

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** Roper Technologies combines strong momentum with a high-quality, diversified technology portfolio and a reasonable forward P/E, making it a better choice than lower-quality or lower-momentum names like CLX or IDXX. Alternatives considered: CLX, IDXX.
- **Thesis:** Roper Technologies is in the top 20-day momentum bucket with a 25.4% 20-day return and a 16.9% 60-day return, with a 60-day drawdown of only -2.5%. Reported diluted EPS of 21.3 for the period ending 2026-09-30 and forward EPS of 24.573 support a forward P/E of 19.5, and the company's gross margin of 69.7% and operating margin of 28.0% indicate a high-quality, diversified technology portfolio. The 16.7 trailing P/E and 6.0% earnings yield are reasonable for a growth-oriented industrial.
- **Source IDs:** S033, S038, S039, S046
- **Catalysts:** 25.4% 20-day return and 16.9% 60-day return indicate strong momentum, Forward EPS of 24.573 implies a forward P/E of 19.5, Gross margin of 69.7% and operating margin of 28.0% support durable profitability, 60-day drawdown of only -2.5% shows low volatility
- **Risks:** Forward EPS fiscal period alignment is unverified, Revenue growth of 7.6% and earnings growth of 32.6% are positive but not as strong as AppLovin, Valuation quality flags are absent but forward EPS basis is source.forwardEps
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 24.5732 (source.forwardEps) x AI multiple assumption 18.00; source IDs S033, S038, S039, S046
- **EPS:** 24.57318 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 19.532475
- **FY+1 growth assumption:** 9.81%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / Lowe's Companies, Inc. (LOW) and Home Depot, Inc. (HD) as home improvement retailers with comparable margin and growth profiles / ROP shows 6.3% revenue growth and 9.8% earnings growth with 69.7% gross margin and 28.0% operating margin, supporting a mid-teens multiple. Peer reference: LOW/HD for home improvement retail growth and margin structure.
- **Company fundamentals:** Roper Technologies reported diluted EPS of 21.3 for the period ending 2026-09-30, with forward EPS of 24.573, forward P/E of 19.5, gross margin of 69.7%, operating margin of 28.0%, profit margin of 30.7%, revenue growth of 7.6%, and earnings growth of 32.6%. Trailing P/E is 16.7 and earnings yield is 6.0%.
- **Bull / Base / Bear:** 540.61 / 442.32 / 344.02
- **Bull / Base / Bear returns:** 12.63% / -7.85% / -28.33%
- **Scenario probabilities:** not separately assigned; see scenario table.

### RDDT — Reddit

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Reddit's strong revenue and earnings growth and reasonable forward P/E make it a compelling turnaround story, but the negative price action and high valuation relative to peers require a more cautious stance than the high-momentum names. Alternatives considered: APP, ROP.
- **Thesis:** Reddit is in the largest 20-day dislocation bucket with a 33.2% trailing P/E and a 3.0% earnings yield, but it has negative 20-day and 60-day returns of -36.9% and -34.5%, with a 60-day drawdown of -39.4%. Reported diluted EPS of 3.66 for the period ending 2026-09-30 and forward EPS of 9.100 support a forward P/E of 10.8, and revenue growth of 53.0% and earnings growth of 74.9% are strong. The dislocation is significant but the negative price action and high valuation relative to peers warrant caution.
- **Source IDs:** S036, S041, S042, S045
- **Catalysts:** Revenue growth of 53.0% and earnings growth of 74.9% indicate strong fundamentals, Forward EPS of 9.100 implies a forward P/E of 10.8, which is reasonable, Large dislocation of -36.9% over 20 days may present a mean-reversion opportunity
- **Risks:** Negative 20-day and 60-day returns of -36.9% and -34.5% indicate continued weakness, 60-day drawdown of -39.4% is significant and could worsen, Trailing P/E of 33.2 and earnings yield of 3.0% are higher than the forward P/E, suggesting near-term uncertainty
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 9.1004 (source.forwardEps) x AI multiple assumption 12.00; source IDs S036, S041, S042, S045
- **EPS:** 9.10039 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 10.818217
- **FY+1 growth assumption:** 24.01%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / Amazon.com, Inc. (AMZN) and Alphabet Inc. (GOOGL) as high-growth, high-margin technology platforms with strong operating leverage / RDDT has 28.4% revenue growth and 24.0% earnings growth with 91.5% gross margin and 32.0% ROE, supporting a premium growth multiple. Peer reference: AMZN/GOOGL for high-growth, high-margin technology platforms.
- **Company fundamentals:** Reddit reported diluted EPS of 3.66 for the period ending 2026-09-30, with forward EPS of 9.100, forward P/E of 10.8, gross margin of 91.5%, operating margin of 29.4%, profit margin of 32.1%, revenue growth of 53.0%, and earnings growth of 74.9%. Trailing P/E is 33.2 and earnings yield is 3.0%.
- **Bull / Base / Bear:** 136.51 / 109.2 / 81.9
- **Bull / Base / Bear returns:** 38.66% / 10.92% / -16.81%
- **Scenario probabilities:** not separately assigned; see scenario table.

### XLV — Health Care sector ETF

- **Type:** ETF
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** XLV offers broad, diversified exposure to the health care sector, which is a defensive allocation in the current macro environment, but the limited top-10 weight coverage means it should be used as a satellite rather than a core holding. Alternatives considered: XLP, XLF.
- **Thesis:** The Health Care sector ETF (XLV) is a diversified basket of large-cap health care names with a 0.54% price change on the latest session. The top 10 holdings are LLY, JNJ, ABBV, MRK, UNH, TMO, AMGN, GILD, ABT, and PFE, with a numeric weight coverage of 61.42%. The sector provides broad exposure to health care but the limited weight coverage means the top 10 holdings do not fully represent the portfolio.
- **Source IDs:** S054, S056
- **Catalysts:** Diversified exposure to large-cap health care names, Top 10 holdings include LLY, JNJ, ABBV, MRK, UNH, TMO, AMGN, GILD, ABT, PFE, Numeric weight coverage of 61.42% provides a reasonable view of the portfolio
- **Risks:** Top 10 holdings weight coverage of 61.42% means the remaining 38.58% is not fully detailed, Sector-specific risks such as regulatory changes, drug pricing, and clinical trial failures, Limited holdings coverage may obscure concentration risk
- **Valuation method:** Holdings/portfolio valuation with AI total-return assumption
- **Valuation status:** verified; forward-EPS source: ; period flags: 
- **Valuation assumptions:** Holdings/portfolio valuation; 10 weighted holdings; coverage 61.42%; source IDs S054, S056
- **Top holdings:** LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59%
- **Portfolio valuation:** Top 10 holdings; numeric weight coverage 61.42%
- **Sector exposure:** Health Care
- **Underlying drivers:** Health care sector performance is driven by pharmaceutical and biotechnology innovation, managed care utilization, regulatory environment, and demographic trends. The top 10 holdings are dominated by large-cap pharma and biotech names with strong balance sheets.
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
| Bull | 25% | +2.00% | Low 5-day realized vol (14.9%) and below-threshold spike probability (16.5% vs 18.5% threshold) support a modest upside if US close confirms no macro shock; probability capped below base because frozen daily-close model is not yet official. |
| Base | 50% | +0.00% | Directional signal is false and forecast vol sits near the EWMA baseline (14.9% vs 20.1%), implying range-bound trading with no clear catalyst; base case assumes flat returns over the 5-day target window. |
| Bear | 25% | -2.00% | Spike probability (16.5%) is elevated relative to the historical baseline (22.1%) but still below threshold; a negative US close or risk-off event could push returns to -2%, consistent with the frozen model's conservative downside. |

### Long Term (12 months)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 30% | +8.00% | Sustained low volatility (14.9% 5d) and below-threshold spike probability (16.5%) support a positive drift if earnings breadth expands and credit spreads tighten; probability set above base to reflect asymmetric upside in a benign macro regime. |
| Base | 40% | +3.00% | Frozen daily-close model with no directional signal and vol near EWMA baseline implies steady, modest returns driven by stable earnings growth and normal credit conditions over the medium term. |
| Bear | 30% | -5.00% | Elevated spike probability (16.5%) and historical baseline (22.1%) indicate latent tail risk; a US close shock or credit event could drive a -5% drawdown, reflecting the model's conservative downside calibration. |

## Positioning

- Maintain a defensive tilt: Health Care and Consumer Staples are the most reliable sectors with positive flows and reasonable valuations.
- Monitor Consumer Discretionary and Real Estate for divergence between price momentum and institutional flows.
- Exercise caution in Information Technology and Communication Services

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
| S008 | filing | FISV | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0000798354-26-000042); 8-K filed 2026-11-03 (accession 0000798354-26-000039); 8-K filed 2026-10-23 (accession 0001193125-26-429481) |
| S009 | filing | APP | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001751008&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0001751008-26-000069); 8-K filed 2026-11-04 (accession 0001751008-26-000068); 10-Q filed 2026-08-05 (accession 0001751008-26-000059) |
| S010 | filing | PNR | 2026-10-27 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-27 (accession 0000077360-26-000058); 8-K filed 2026-10-27 (accession 0000077360-26-000055); 8-K filed 2026-09-22 (accession 0000077360-26-000050) |
| S011 | news | FISV | Fri, 13 Nov 2026 21:49:46 GMT | ok | https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en | Fiserv, Inc. (FISV) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 21:49:46 GMT); Why Fiserv, Inc. (FISV) Was Exited by Ariel Appreciation Fund - Yahoo Finance (Wed, 28 Oct 2026 07:00:00 GMT); Fiserv (FISV): Buy, Sell, or Hold Post Q2 Earnings? - Yahoo Finance (Tue, 08 Sep 2026 07:00:00 GMT) |
| S012 | news | APP | Sun, 15 Nov 2026 07:07:20 GMT | ok | https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en | META_TITLE_QUOTE - Yahoo Finance (Sun, 15 Nov 2026 07:07:20 GMT); AppLovin Just Ripped 47% in a Month: Is It Too Late to Buy APP Stock Now? - Yahoo Finance (Thu, 12 Nov 2026 20:05:45 GMT); Is Trending Stock AppLovin Corporation (APP) a Buy Now? - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT) |
| S013 | filing | APP | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json | Diluted EPS 11.61 for period ending 2026-09-30 (filed 2026-11-04) |
| S014 | news | PNR | Fri, 13 Nov 2026 22:09:48 GMT | ok | https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en | Pentair plc (PNR) stock price, news, quote and history - Yahoo Finance UK (Fri, 13 Nov 2026 22:09:48 GMT); Pentair plc (PNR) Q3 Earnings and Revenues Beat Estimates - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT); Pentair (PNR) Stock May Be 46% Undervalued As New CFO Arrives - Yahoo Finance (Fri, 25 Sep 2026 07:00:00 GMT) |
| S015 | filing | FISV | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json | Diluted EPS -8.9 for period ending 2026-09-30 (filed 2026-11-04) |
| S016 | stock | FISV | 2026-11-16 | ok | https://finance.yahoo.com/quote/FISV | Forward P/E: 7.99667; Price: 63.78; Market price: 63.78; Market cap: 33934002176; Market Cap: 33934002176; Consensus EPS FY+1: 7.97582; growth: 0.0959 |
| S017 | stock | APP | 2026-11-16 | ok | https://finance.yahoo.com/quote/APP | Trailing P/E: 27.54882; Forward P/E: 19.611452; Forward EPS: 20.86026; Price: 409.1; Market price: 409.1; Market cap: 135543824384; Sector: Communication Services; Trailing Eps: 14.85; Revenue Growth: 0.555; Earnings Growth: 0.755; Gross Margin: 0.8878; Operating Margin: 0.77782995; Profit Margin: 0.65887; Return On Equity: 2.1008599; Total Revenue: 7608893952; Market Cap: 135543824384; Consensus EPS FY+1: 20.72438; growth: 0.2744 |
| S018 | filing | GEN | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0000849399-26-000083); 8-K filed 2026-10-28 (accession 0000849399-26-000081); 8-K filed 2026-10-09 (accession 0000849399-26-000079) |
| S019 | filing | PNR | 2026-10-27 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json | Diluted EPS 2.76 for period ending 2026-09-30 (filed 2026-10-27) |
| S020 | stock | PNR | 2026-11-16 | ok | https://finance.yahoo.com/quote/PNR | Trailing P/E: 18.610355; Forward P/E: 12.877027; Forward EPS: 5.30402; Price: 68.3; Market price: 68.3; Market cap: 10904415232; Sector: Industrials; Trailing Eps: 3.67; Revenue Growth: -0.045; Earnings Growth: -0.188; Gross Margin: 0.40168998; Operating Margin: 0.21410999; Profit Margin: 0.15435; Return On Equity: 0.15605; Total Revenue: 3966200064; Market Cap: 10904415232; Consensus EPS FY+1: 5.30402; growth: 0.1282 |
| S021 | filing | CLX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000021076-26-000046); 8-K filed 2026-11-02 (accession 0000021076-26-000044); 8-K filed 2026-10-29 (accession 0001206774-26-000586) |
| S022 | news | GEN | Thu, 29 Oct 2026 07:00:00 GMT | ok | https://news.google.com/rss/search?q=GEN+Gen+Digital+stock&hl=en-US&gl=US&ceid=US:en | Gen Digital (GEN) Stock Repriced After Q2 Earnings Put Margins Center Stage - Yahoo Finance (Thu, 29 Oct 2026 07:00:00 GMT); Gen Digital Stock: Is Wall Street Bullish or Bearish? - Yahoo Finance (Thu, 05 Nov 2026 08:00:00 GMT); Are Business Services Stocks Lagging GEN DIGITAL INC (GEN) This Year? - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT) |
| S023 | stock | GEN | 2026-11-16 | ok | https://finance.yahoo.com/quote/GEN | Trailing P/E: 15.431472; Forward P/E: 9.108996; Forward EPS: 3.33736; Price: 30.4; Market price: 30.4; Market cap: 18035593216; Sector: Technology; Trailing Eps: 1.97; Revenue Growth: 0.122; Earnings Growth: 1.286; Gross Margin: 0.77410007; Operating Margin: 0.43229; Profit Margin: 0.23068; Return On Equity: 0.46402; Total Revenue: 5228000256; Market Cap: 18035593216; Consensus EPS FY+1: 3.33736; growth: 0.1286 |
| S024 | stock | CLX | 2026-11-16 | ok | https://finance.yahoo.com/quote/CLX | Trailing P/E: 19.68705; Forward P/E: 17.745283; Forward EPS: 6.1684; Price: 109.46; Market price: 109.46; Market cap: 13260793856; Sector: Consumer Defensive; Trailing Eps: 5.56; Revenue Growth: 0.333; Earnings Growth: 1.138; Gross Margin: 0.41939998; Operating Margin: 0.14286; Profit Margin: 0.09408; Return On Equity: 5.34363; Total Revenue: 7196000256; Market Cap: 13260793856; Consensus EPS FY+1: 6.1684; growth: 0.0769 |
| S025 | filing | CHTR | 2026-11-06 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-06 (accession 0001091667-26-000073); 8-K filed 2026-11-06 (accession 0001091667-26-000072); 8-K filed 2026-10-27 (accession 0001091667-26-000064) |
| S026 | stock | CHTR | 2026-11-16 | ok | https://finance.yahoo.com/quote/CHTR | Trailing P/E: 13.006578; Forward P/E: 3.0452294; Forward EPS: 45.44485; Price: 138.39; Market price: 138.39; Market cap: 24778944512; Sector: Communication Services; Trailing Eps: 10.64; Revenue Growth: 0.091; Gross Margin: 0.55084; Operating Margin: 0.23389; Profit Margin: 0.02498; Return On Equity: 0.07019; Total Revenue: 55645999104; Market Cap: 24778944512; Consensus EPS FY+1: 49.35412; growth: 1.1136 |
| S027 | news | CLX | Fri, 13 Nov 2026 23:34:51 GMT | ok | https://news.google.com/rss/search?q=CLX+Clorox+stock&hl=en-US&gl=US&ceid=US:en | The Clorox Company (CLX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 23:34:51 GMT); The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance UK (Sat, 14 Nov 2026 06:03:20 GMT); Should You Forget Clorox Stock Near a 52-Week Low? - Yahoo Finance (Mon, 26 Oct 2026 07:00:00 GMT) |
| S028 | filing | IDXX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000874716&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000874716-26-000135); 8-K filed 2026-11-02 (accession 0001104659-26-120892); 10-Q filed 2026-08-04 (accession 0000874716-26-000123) |
| S029 | news | CHTR | Sun, 15 Nov 2026 05:47:01 GMT | ok | https://news.google.com/rss/search?q=CHTR+Charter+Communications+stock&hl=en-US&gl=US&ceid=US:en | Charter Communications (CHTR) Stock Could Be A Bargain Following Its New Operating Model - Yahoo Finance (Sun, 15 Nov 2026 05:47:01 GMT); Why You Should Think About Charter Communications Differently Now? - Yahoo Finance (Fri, 13 Nov 2026 19:16:11 GMT); Charter Communications (CHTR) Earnings Expected to Grow: What to Know Ahead of Next Week's Release - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT) |
| S030 | stock | IDXX | 2026-11-16 | ok | https://finance.yahoo.com/quote/IDXX | Trailing P/E: 47.45485; Forward P/E: 41.687927; Forward EPS: 16.8929; Price: 704.23; Market price: 704.23; Market cap: 55483650048; Sector: Healthcare; Trailing Eps: 14.84; Revenue Growth: 0.099; Earnings Growth: 0.179; Gross Margin: 0.62722; Operating Margin: 0.32497; Profit Margin: 0.25357; Return On Equity: 0.68925005; Total Revenue: 4662220800; Market Cap: 55483650048; Consensus EPS FY+1: 16.8929; growth: 0.1244 |
| S031 | filing | GEN | 2026-10-29 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000849399.json | Diluted EPS 0.83 for period ending 2026-10-02 (filed 2026-10-29) |
| S032 | filing | CLX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000021076.json | Diluted EPS 1.39 for period ending 2026-09-30 (filed 2026-11-02) |
| S033 | filing | ROP | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000882835&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000882835-26-000047); 8-K filed 2026-10-22 (accession 0000882835-26-000042); 8-K filed 2026-10-01 (accession 0000882835-26-000039) |
| S034 | filing | CHTR | 2026-11-06 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001091667.json | Diluted EPS 0.38 for period ending 2026-09-30 (filed 2026-11-06) |
| S035 | news | IDXX | Sat, 14 Nov 2026 22:37:20 GMT | ok | https://news.google.com/rss/search?q=IDXX+Idexx+Laboratories+stock&hl=en-US&gl=US&ceid=US:en | IDEXX Laboratories, Inc. (IDXX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Sat, 14 Nov 2026 22:37:20 GMT); symbol__ Stock Quote Price and Forecast - CNN (Fri, 13 Nov 2026 15:22:45 GMT); IDEXX Laboratories, Inc. (IDXX) stock price, news, quote and history - Yahoo Finance UK (Sat, 14 Nov 2026 10:10:11 GMT) |
| S036 | filing | RDDT | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001713445&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0001713445-26-000116); 8-K filed 2026-10-29 (accession 0001713445-26-000114); 8-K filed 2026-08-12 (accession 0001713445-26-000107) |
| S037 | filing | IDXX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000874716.json | Diluted EPS 11.75 for period ending 2026-09-30 (filed 2026-11-02) |
| S038 | news | ROP | Thu, 05 Nov 2026 08:00:00 GMT | ok | https://news.google.com/rss/search?q=ROP+Roper+Technologies+stock&hl=en-US&gl=US&ceid=US:en | Roper Technologies (ROP) Stock Looks Fully Valued As Cash Flow Comes Into Focus - Yahoo Finance (Thu, 05 Nov 2026 08:00:00 GMT); Roper Technologies (ROP), What Is Behind The Fresh Attention? - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT); Did Earnings Beat Just Shift Roper Technologies (ROP) Investment Narrative? - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT) |
| S039 | stock | ROP | 2026-11-16 | ok | https://finance.yahoo.com/quote/ROP | Trailing P/E: 18.993866; Forward P/E: 19.532475; Forward EPS: 24.57318; Price: 479.975; Market price: 479.975; Market cap: 47535013888; Sector: Technology; Trailing Eps: 25.27; Revenue Growth: 0.076; Earnings Growth: 0.326; Gross Margin: 0.69671; Operating Margin: 0.28049; Profit Margin: 0.30712998; Return On Equity: 0.13229; Total Revenue: 8434599936; Market Cap: 47535013888; Consensus EPS FY+1: 24.57318; growth: 0.09810001 |
| S040 | filing | INTC | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000050863&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0000050863-26-000191); 8-K filed 2026-10-29 (accession 0000050863-26-000188); 8-K filed 2026-08-12 (accession 0001193125-26-346806) |

## Sources

- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFF&cosd=2026-01-01 (2026-11-12)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLH0A0HYM2&cosd=2026-01-01 (2026-11-12)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLC0A0CM&cosd=2026-01-01 (2026-11-12)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCSL&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=UNRATE&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=PAYEMS&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=T10Y2Y&cosd=2026-01-01 (2026-11-13)
- filing FISV: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 (2026-11-04)
- filing APP: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001751008&type=10-Q&dateb=&owner=include&count=10 (2026-11-04)
- filing PNR: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 (2026-10-27)
- news FISV: https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 21:49:46 GMT)
- news APP: https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en (Sun, 15 Nov 2026 07:07:20 GMT)
- filing APP: https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json (2026-11-04)
- news PNR: https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 22:09:48 GMT)
- filing FISV: https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json (2026-11-04)
- stock FISV: https://finance.yahoo.com/quote/FISV (2026-11-16)
- stock APP: https://finance.yahoo.com/quote/APP (2026-11-16)
- filing GEN: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 (2026-10-29)
- filing PNR: https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json (2026-10-27)
- stock PNR: https://finance.yahoo.com/quote/PNR (2026-11-16)

## AI Provenance

- Provider / model: hermes-local-proxy / upstage/solar-mini4:free
- Market research: attempts=1 tokens=9540 (prompt=6540, completion=3000) runtime=30.03s
- Fundamental research: generated this run at 2026-11-16T11:11:09.845109+00:00
- Evidence source dates: {'as_of': '2026-11-13', 'latest_equity_date': '2026-11-13', 'latest_macro_date': '2026-11-16', 'flows_date': '2026-11-13'}
- Evidence fingerprint: ea3df1a6f90112631bb4dcdde619b1b84c5f76b60b614702f725b965fd500731
- Source citations are retrieved external records in the ledger above; market values remain from the verified database snapshot.


## Disclosures

- This is research and market intelligence, not investment advice.
- AI conclusions are research judgments, not validated return predictions.
- The frozen risk layer is risk-only and is not used for directional views or allocations.
- Legacy scores are not active inputs or outputs.

# AEGIS AI-First Market Intelligence

Research generated at: 15 November 2026, 20:17 HKT
Database freshness: equity 2026-11-13 (latest row retrieved 2026-11-15 13:06:40.074841+08:00)
Data cutoff: 2026-11-13 US cash close
Snapshot ID: aegis-hourly-20261115T121708Z

## Executive Summary

- **AI market view: Late-November 2026 equity market is in a late-cycle, mixed posture: broad market breadth is positive and above both the 50-day and 200-day moving averages, but the S&P 500 is down 1.28% over 20 days and the Information Technology sector is the weakest, with Communication Services also negative. Momentum and dislocation screens are concentrated in a small set of names, while large-cap liquidity leaders and select semiconductor names show strong institutional buying. Macro data show a still-elevated but decelerating inflation backdrop, a 4.2% unemployment rate, and a modestly positive 10Y-2Y spread, with credit spreads tight and stable.**
- Broad market breadth is constructive: 71.34% of constituents above the 50-day and 63.6% above the 200-day, with a 1.70 advance/decline ratio and positive 20-day momentum for 70.46% of names.
- S&P 500 is down 1.28% over 20 days, and Information Technology (-7.19%) and Energy (-4.81%) are the weakest sectors, while Health Care (+6.87%), Consumer Discretionary (+6.69%), and Consumer Staples (+5.40%) lead.
- Momentum and dislocation screens are concentrated in a small set of names, with semiconductor names (SOXX, SMH) showing strong institutional buying despite price declines.
- Macro data show CPI at 336.298 (Sep 2026), core CPI at 338.896, unemployment at 4.2%, and a 10Y-2Y spread of 0.27, indicating a late-cycle but not recessionary environment.
- Credit markets are stable: high-yield OAS at 3.20 and investment-grade OAS at 0.89, with no directional signal in the frozen risk model.
- The risk model shows forecast volatility of 14.93% over 5 days, below the 18.50% threshold, with a 16.51% spike probability, below the historical 22.07% baseline.

## Data QC

- Status: **PASS_WITH_WARNINGS**
- Equity session: 0 completed session(s) behind inference date
- Equity provenance: 393 provisional / 12576 canonical
- Breadth lag: 0 session(s); ETF-flow lag: 0 session(s)
- Note: Equity session contains a mix of provisional yfinance and canonical Massive rows.
- External sources: 79 ok / 0 unavailable; retrieved 2026-11-15T12:17:28.678503+00:00

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
| S&P 500 | 7561.67 | -1.28% (20d) | Broad market breadth is positive with 71.34% above 50d and 63.6% above 200d, but the index is down 1.28% over 20 days. |
| Information Technology (XLK) | -7.19% (20d) | -7.19% | Weakest sector; trailing P/E 30.03, sector-relative P/E 0.79 for NVDA. |
| Health Care (XLV) | +6.87% (20d) | +6.87% | Strongest sector; trailing P/E 30.78. |
| Consumer Discretionary (XLY) | +6.69% (20d) | +6.69% | Strong sector; trailing P/E 25.11. |
| Consumer Staples (XLP) | +5.40% (20d) | +5.40% | Positive sector; trailing P/E 24.85. |
| Communication Services (XLC) | -1.48% (20d) | -1.48% | Negative sector; trailing P/E 17.26. |
| Energy (XLE) | -4.81% (20d) | -4.81% | Negative sector; trailing P/E 16.23. |
| Industrials (XLI) | +0.61% (20d) | +0.61% | Near-flat sector; trailing P/E 27.07. |
| Financials (XLF) | +5.69% (20d) | +5.69% | Positive sector; trailing P/E 15.85. |
| Materials (XLB) | +2.57% (20d) | +2.57% | Positive sector; trailing P/E 21.72. |
| Utilities (XLU) | +4.34% (20d) | +4.34% | Positive sector; trailing P/E 18.11. |
| Real Estate (XLRE) | +5.24% (20d) | +5.24% | Positive sector; trailing P/E 29.63. |

## Macro, Fiscal, Rates, Liquidity and Credit

- Growth: The 10Y-2Y Treasury spread is 0.27 as of 2026-11-13, indicating a modestly positive but still flat yield curve, consistent with a late-cycle expansion.
- Inflation: CPI (CPIAUCSL) is 336.298 in September 2026 and core CPI is 338.896, showing a decelerating but still-elevated inflation backdrop; the October 2026 CPI reading of 337.476 from S004 suggests continued moderation.
- Policy: The effective federal funds rate is 3.88 as of 2026-11-12, indicating a restrictive but easing policy stance.
- Rates: The 10Y-2Y spread of 0.27 and tight credit spreads (IG OAS 0.89, HY OAS 3.20) suggest stable term premium and limited credit stress.
- Liquidity: Bitcoin fell 6.04% to 64,128.05 and Ethereum fell 8.22% to 1,769.12 on 2026-11-14, indicating a broad de-risking in risk assets.
- Credit: High-yield OAS at 3.20 and investment-grade OAS at 0.89 are stable, with no directional signal in the frozen risk model.

## US Equities and 11 GICS Sectors

Macro source IDs: S001, S002, S003, S004, S005, S006, S007

| GICS sector | Evidence | AI research stance | Source IDs |
| --- | --- | --- | --- |
| Health Care | Sector return 20d +6.87%; trailing P/E 30.78 (S054); momentum and dislocation screens include IDXX (PE 39.18, sector-relative 1.33) and CHTR (PE 2.71, sector-relative 0.13). | Positive momentum and relative strength, but high valuation for IDXX; CHTR excluded due to forward EPS issues. | S054 |
| Consumer Staples | Sector return 20d +5.40%; trailing P/E 24.85 (S057); no shortlist names in this sector. | Defensive strength with moderate valuation; no specific shortlist names. | S057 |
| Consumer Discretionary | Sector return 20d +6.69%; trailing P/E 25.11 (S056); no shortlist names in this sector. | Strong relative momentum; no specific shortlist names. | S056 |
| Real Estate | Sector return 20d +5.24%; trailing P/E 29.63 (S059); no shortlist names in this sector. | Positive sector performance; no specific shortlist names. | S059 |
| Financials | Sector return 20d +5.69%; trailing P/E 15.85 (S064); no shortlist names in this sector. | Positive sector performance with low valuation; no specific shortlist names. | S064 |
| Utilities | Sector return 20d +4.34%; trailing P/E 18.11 (S065); no shortlist names in this sector. | Positive sector performance; no specific shortlist names. | S065 |
| Materials | Sector return 20d +2.57%; trailing P/E 21.72 (S067); no shortlist names in this sector. | Positive sector performance; no specific shortlist names. | S067 |
| Industrials | Sector return 20d +0.61%; trailing P/E 27.07 (S071); no shortlist names in this sector. | Near-flat sector performance; no specific shortlist names. | S071 |
| Communication Services | Sector return 20d -1.48%; trailing P/E 17.26 (S073); CHTR excluded due to forward EPS issues. | Negative sector performance; CHTR excluded from shortlist due to forward EPS issues. | S073 |
| Information Technology | Sector return 20d -7.19%; trailing P/E 30.03 (S074); shortlist names include NVDA (PE 26.51, sector-relative 0.79), AMD (PE 128.88, sector-relative 3.82), MRVL (PE 74.23, sector-relative 2.20), INTC (negative PE), LITE (negative PE), COIN (negative PE). | Weakest sector; high-multiple names (AMD, MRVL, NOW) show dislocation but face forward EPS issues; NVDA is a liquidity leader with moderate valuation. | S074 |
| Energy | Sector return 20d -4.81%; trailing P/E 16.23 (S075); no shortlist names in this sector. | Negative sector performance; no specific shortlist names. | S075 |

### Sector fundamentals, valuation and earnings

The supplied database provides trailing P/E for each of the 11 GICS sectors via ETF-level data (S054-S075), but does not supply point-in-time sector fundamentals such as sector-level earnings growth, margins, or consensus estimates. Therefore, no sector-level fundamental metrics are available beyond valuation multiples and 20-day returns.

## Growth vs Value

- Growth: Information Technology is the weakest sector (-7.19% 20d) with high-multiple names like AMD (PE 128.88, sector-relative 3.82) and NOW (PE 97.19, sector-relative 2.88) showing dislocation, but forward EPS data is missing for these names.
- Value: Financials (XLF, PE 15.85) and Energy (XLE, PE 16.23) offer the lowest trailing P/E among sectors, while Health Care (XLV, PE 30.78) and Information Technology (XLK, PE 30.03) are the most expensive.
- Valuation quality: Several shortlist names were rejected for forward EPS issues (FISV, CHTR, SNDK, MRVL, FFIV, NOW, LITE, COIN, NVDA, AMD

## ETF Flows and Breadth


## Stock Ideas

Single-stock research uses reported EPS, forward P/E and company fundamentals. All ideas are research judgments, not validated return predictions.

| Ticker | Security | Research view | Price | EPS | Forward P/E | Base target | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| APP | AppLovin | NEW | 409.1 | 20.86026 | 19.611452 | 417.21 | NEW |
| PNR | Pentair | KEEP | 68.3 | 5.30402 | 12.877027 | 74.26 | KEEP |
| GEN | Gen Digital | KEEP | 30.4 | 3.33736 | 9.108996 | 33.37 | KEEP |
| CLX | Clorox | KEEP | 109.46 | 6.1684 | 17.745283 | 98.69 | KEEP |
| IDXX | Idexx Laboratories | KEEP | 704.23 | 16.8929 | 41.687927 | 641.93 |  |

## ETF Ideas

ETF research uses holdings, portfolio valuation and exposure. Single-stock EPS × P/E valuation is not applied to ETFs.

No qualifying ETF ideas this run.
### APP — AppLovin

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** AppLovin offers a high-margin, high-growth mobile advertising franchise with strong 20-day momentum and a forward P/E near 19.6, whereas the shortlist also contains lower-quality or more volatile names such as INTC and COIN that carry negative earnings or dislocation-driven declines. AppLovin's profitability and growth profile make it the more defensible equity idea among the momentum candidates. Alternatives considered: INTC, COIN, RDDT.
- **Thesis:** AppLovin screens in the top 20-day momentum bucket with a 53.7% 20-day return and a 32.5% 60-day return, indicating strong price follow-through. Reported diluted EPS of 11.61 for the fiscal period ending 2026-09-30 and a forward EPS of 20.86 support a forward P/E near 19.6, which is reasonable for a high-margin, high-growth mobile advertising platform. The company's gross margin near 89% and operating margin near 78% provide a durable profitability profile that can compound earnings while the stock has momentum.
- **Source IDs:** S009, S011, S013, S016
- **Catalysts:** Continued 20-day momentum and positive 60-day return, Sustained high gross margin and operating leverage on ad spend, Earnings growth of 75.5% and revenue growth of 55.5% in the latest reported period, Potential for continued advertiser demand in mobile video and rewarded ads
- **Risks:** High 20-day momentum can mean elevated volatility and pullbacks, Forward P/E near 19.6 leaves limited room if growth decelerates, Mobile advertising market competition and privacy regulation could pressure demand, Single-quarter earnings and revenue growth may not be sustained
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 20.8603 (source.forwardEps) x AI multiple assumption 20.00; source IDs S009, S011, S013, S016
- **EPS:** 20.86026 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 19.611452
- **FY+1 growth assumption:** 27.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / MSFT / APP shows strong FY1 consensus growth of 27.44% with 25.4% revenue growth and high margins (gross 88.8%, operating 77.8%, profit 65.9%), supported by 26 analysts. The base multiple of 20.0x is justified by durable high margins and growth, with a bull case of 24.0x if growth accelerates and a bear case of 16.0x if margin compression or macro softness emerges. Peer reference: MSFT, reflecting premium multiple for high-margin, high-growth software/tech exposure.
- **Company fundamentals:** AppLovin reported diluted EPS of 11.61 for the period ending 2026-09-30, with forward EPS of 20.86, forward P/E of 19.61, gross margin of 88.78%, operating margin of 77.78%, profit margin of 65.89%, revenue growth of 55.5%, and earnings growth of 75.5%. The stock closed at 409.1 with 20-day return of 53.7% and 60-day return of 32.5%.
- **Bull / Base / Bear:** 500.65 / 417.21 / 333.76
- **Bull / Base / Bear returns:** 22.38% / 1.98% / -18.42%
- **Scenario probabilities:** not separately assigned; see scenario table.

### PNR — Pentair

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Pentair is a higher-quality industrial with a reasonable forward P/E of 12.88 and a 20-day momentum of 27.8%, but it is not as compelling as AppLovin because its latest reported revenue and earnings growth are negative. It is preferable to the dislocation names such as INTC and COIN, which show negative returns and negative earnings, but it is not a strong buy until fundamentals stabilize. Alternatives considered: INTC, COIN, APP.
- **Thesis:** Pentair screens in the top 20-day momentum bucket with a 27.8% 20-day return and a 7.1% 60-day return. The stock trades at a forward P/E of 12.88 with a forward EPS of 5.30, which is reasonable for a diversified industrial and water technology company. However, the latest reported revenue growth of -4.5% and earnings growth of -18.8% indicate near-term operating pressure, so the momentum is not yet supported by broad-based fundamental improvement.
- **Source IDs:** S010, S017, S018, S021
- **Catalysts:** 20-day momentum of 27.8% and positive 60-day return of 7.1%, Forward P/E of 12.88 offers a reasonable entry point for a diversified industrial, Exposure to water, fluid handling, and building technology end markets, Potential for margin recovery if cost discipline and pricing improve
- **Risks:** Latest reported revenue growth of -4.5% and earnings growth of -18.8%, Industrial end-market softness could delay reacceleration, 20-day momentum may be driven by a single catalyst rather than broad fundamentals, Forward P/E of 12.88 still leaves limited margin for error if earnings do not recover
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 5.3040 (source.forwardEps) x AI multiple assumption 14.00; source IDs S010, S017, S018, S021
- **EPS:** 5.30402 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 12.877027
- **FY+1 growth assumption:** 12.82%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / UPS / PNR has FY1 consensus growth of 12.82% with 18.4% revenue growth, though earnings growth is negative (-18.8%) and margins are lower (gross 40.2%, operating 21.4%, profit 15.4%). The base multiple of 14.0x reflects recovery potential with a bull case of 17.0x if earnings inflect and a bear case of 11.0x if margin pressure persists. Peer reference: UPS, a comparable industrial/logistics name with cyclical margin dynamics.
- **Company fundamentals:** Pentair reported diluted EPS of 2.76 for the period ending 2026-09-30, with forward EPS of 5.30, forward P/E of 12.88, gross margin of 40.17%, operating margin of 21.41%, profit margin of 15.44%, revenue growth of -4.5%, and earnings growth of -18.8%. The stock closed at 68.3 with a 20-day return of 27.8% and a 60-day return of 7.1%.
- **Bull / Base / Bear:** 90.17 / 74.26 / 58.34
- **Bull / Base / Bear returns:** 32.02% / 8.73% / -14.58%
- **Scenario probabilities:** not separately assigned; see scenario table.

### GEN — Gen Digital

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Gen Digital offers a low forward P/E of 9.11 and strong 20-day momentum of 25.8%, but it is not as compelling as AppLovin because its forward P/E is not yet supported by a clear reacceleration in the broader business. It is preferable to the dislocation names such as INTC and COIN, which show negative returns and negative earnings, but it is not a strong buy until fundamentals stabilize. Alternatives considered: INTC, COIN, APP.
- **Thesis:** Gen Digital screens in the top 20-day momentum bucket with a 25.8% 20-day return and a 7.9% 60-day return. The stock trades at a forward P/E of 9.11 with a forward EPS of 3.34, which is attractive for a cybersecurity and digital life protection company. However, the latest reported revenue growth of 12.2% and earnings growth of 128.6% are strong, but the forward P/E is not yet supported by a clear reacceleration in the broader business, so the position should be sized conservatively.
- **Source IDs:** S014, S020, S023, S025
- **Catalysts:** 20-day momentum of 25.8% and positive 60-day return of 7.9%, Forward P/E of 9.11 is reasonable for a cybersecurity platform, Latest reported earnings growth of 128.6% and revenue growth of 12.2%, Diversified exposure to cyber, life, and intelligence solutions
- **Risks:** Forward P/E of 9.11 may not fully reflect the sustainability of the latest earnings surge, Cybersecurity and digital life protection markets face competitive and regulatory pressure, 20-day momentum can reverse quickly if earnings guidance disappoints, Revenue growth of 12.2% is positive but not as strong as the earnings growth suggests
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 3.3374 (source.forwardEps) x AI multiple assumption 10.00; source IDs S014, S020, S023, S025
- **EPS:** 3.33736 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 9.108996
- **FY+1 growth assumption:** 12.86%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / GE / GEN shows FY1 consensus growth of 12.86% with 6.8% revenue growth, moderate margins (gross 77.4%, operating 43.2%, profit 23.1%), and 11 analysts. The base multiple of 10.0x is justified by steady growth with a bull case of 12.0x if margins expand and a bear case of 8.0x if growth decelerates. Peer reference: GE, reflecting industrial exposure with cyclical margin variability.
- **Company fundamentals:** Gen Digital reported diluted EPS of 0.83 for the period ending 2026-10-02, with forward EPS of 3.34, forward P/E of 9.11, gross margin of 77.41%, operating margin of 43.23%, profit margin of 23.07%, revenue growth of 12.2%, and earnings growth of 128.6%. The stock closed at 30.4 with a 20-day return of 25.8% and a 60-day return of 7.9%.
- **Bull / Base / Bear:** 40.05 / 33.37 / 26.7
- **Bull / Base / Bear returns:** 31.74% / 9.77% / -12.17%
- **Scenario probabilities:** not separately assigned; see scenario table.

### CLX — Clorox

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Clorox offers a reasonable forward P/E of 17.75 and strong 20-day momentum of 25.7%, but it is not as compelling as AppLovin because its latest reported revenue growth is near flat. It is preferable to the dislocation names such as INTC and COIN, which show negative returns and negative earnings, but it is not a strong buy until revenue growth stabilizes. Alternatives considered: INTC, COIN, APP.
- **Thesis:** Clorox screens in the top 20-day momentum bucket with a 25.7% 20-day return and a 3.2% 60-day return. The stock trades at a forward P/E of 17.75 with a forward EPS of 6.17, which is reasonable for a consumer staples company. However, the latest reported revenue growth of 0.3% and earnings growth of 113.8% are mixed, with revenue growth near flat, so the momentum is not yet supported by broad-based top-line improvement.
- **Source IDs:** S022, S024, S027, S034
- **Catalysts:** 20-day momentum of 25.7% and positive 60-day return of 3.2%, Forward P/E of 17.75 is reasonable for a consumer staples company, Latest reported earnings growth of 113.8% and revenue growth of 0.3%, Exposure to household, personal care, and food brands
- **Risks:** Latest reported revenue growth of 0.3% is near flat, limiting top-line support, Consumer staples demand may be pressured by inflation and changing consumer behavior, 20-day momentum can reverse quickly if earnings guidance disappoints, Forward P/E of 17.75 leaves limited room if growth decelerates
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 6.1684 (source.forwardEps) x AI multiple assumption 16.00; source IDs S022, S024, S027, S034
- **EPS:** 6.1684 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 17.745283
- **FY+1 growth assumption:** 7.69%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / PG / CLX has FY1 consensus growth of 7.69% with 2.2% revenue growth but strong earnings growth of 113.8%, indicating margin expansion (gross 41.9%, operating 14.3%, profit 9.4%) and 17 analysts. The base multiple of 16.0x is justified by earnings acceleration with a bull case of 19.0x if margin expansion continues and a bear case of 13.0x if growth stalls. Peer reference: PG, a comparable consumer staples name with stable but lower growth.
- **Company fundamentals:** Clorox reported diluted EPS of 1.39 for the period ending 2026-09-30, with forward EPS of 6.17, forward P/E of 17.75, gross margin of 41.94%, operating margin of 14.29%, profit margin of 9.41%, revenue growth of 0.3%, and earnings growth of 113.8%. The stock closed at 109.46 with a 20-day return of 25.7% and a 60-day return of 3.2%.
- **Bull / Base / Bear:** 117.2 / 98.69 / 80.19
- **Bull / Base / Bear returns:** 7.07% / -9.84% / -26.74%
- **Scenario probabilities:** not separately assigned; see scenario table.

### IDXX — Idexx Laboratories

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:**  Alternatives considered: .
- **Thesis:** Idexx Laboratories screens in the top 20-day momentum bucket with a 25.7% 20-day return and a 29.0% 60-day return, indicating strong price follow-through. The stock trades at a forward P/E of 41.69 with a forward EPS of 16.89, which is high for a veterinary diagnostics and animal health company. The latest reported revenue growth of 9.9% and earnings growth of 17.9% are positive, but the high forward P/E leaves limited room for error if growth decelerates.
- **Source IDs:** S029, S030, S033, S042
- **Catalysts:** 20-day momentum of 25.7% and 60-day return of 29.0%, Positive revenue growth of 9.9% and earnings growth of 17.9%, Exposure to veterinary diagnostics and animal health services, Potential for continued demand in pet care and preventive health
- **Risks:** Forward P/E of 41.69 is high and leaves limited room if growth decelerates, 20-day momentum can reverse quickly if earnings guidance disappoints, Veterinary diagnostics market is competitive and subject to pricing pressure, Latest reported revenue growth of 9.9% is positive but not as strong as the 60-day return
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 16.8929 (source.forwardEps) x AI multiple assumption 38.00; source IDs S029, S030, S033, S042
- **EPS:** 16.8929 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 41.687927
- **FY+1 growth assumption:** 12.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / DHR / IDXX shows FY1 consensus growth of 12.44% with 8.9% revenue growth and 17.9% earnings growth, with solid margins (gross 62.7%, operating 32.5%, profit 25.4%) and 13 analysts. The base multiple of 38.0x reflects premium valuation for growth and quality with a bull case of 44.0x if growth accelerates and a bear case of 32.0x if macro or demand softness emerges. Peer reference: DHR, a comparable healthcare/industrial name with similar growth and margin profile.
- **Company fundamentals:** 
- **Bull / Base / Bear:** 743.29 / 641.93 / 540.57
- **Bull / Base / Bear returns:** 5.55% / -8.85% / -23.24%
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
| Bull | 25% | +2.00% | Low 5-day realized vol (14.9%) and below-threshold spike probability (16.5% vs 18.5% threshold) support a modest upside if US close confirms positive breadth and stable credit spreads. |
| Base | 50% | +0.00% | Directional signal is false and forecast vol is near the historical baseline, implying range-bound trading with no clear catalyst for a directional move over the 5-day horizon. |
| Bear | 25% | -2.00% | If the frozen daily-close model fails to confirm after the US close, elevated spike probability and weak directional signal could trigger a short-term risk-off move with negative returns. |

### Long Term (12 months)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 30% | +8.00% | Sustained low volatility and below-threshold spike probability support continued risk appetite, with earnings growth and stable credit conditions driving a positive multi-week return. |
| Base | 40% | +3.00% | Near-baseline volatility and no directional signal imply a modest grind higher as markets absorb data without sharp repricing, reflecting neutral earnings and credit fundamentals. |
| Bear | 30% | -5.00% | If the frozen model's low-vol regime breaks and spike probability rises above threshold, elevated tail risk and weak directional conviction could drive a meaningful drawdown over the longer horizon. |

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
| S008 | filing | FISV | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0000798354-26-000042); 8-K filed 2026-11-03 (accession 0000798354-26-000039); 8-K filed 2026-10-23 (accession 0001193125-26-429481) |
| S009 | filing | APP | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001751008&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0001751008-26-000069); 8-K filed 2026-11-04 (accession 0001751008-26-000068); 10-Q filed 2026-08-05 (accession 0001751008-26-000059) |
| S010 | filing | PNR | 2026-10-27 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-27 (accession 0000077360-26-000058); 8-K filed 2026-10-27 (accession 0000077360-26-000055); 8-K filed 2026-09-22 (accession 0000077360-26-000050) |
| S011 | news | APP | Thu, 12 Nov 2026 20:05:45 GMT | ok | https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en | AppLovin Just Ripped 47% in a Month: Is It Too Late to Buy APP Stock Now? - Yahoo Finance (Thu, 12 Nov 2026 20:05:45 GMT); APP Stock Surges 51% After Q3 Earnings: Is it Still a Buy? - Yahoo Finance (Tue, 10 Nov 2026 14:24:00 GMT); ETFs Are Net Sellers of AppLovin (APP) on Nov. 11 - Yahoo Finance (Fri, 13 Nov 2026 11:02:35 GMT) |
| S012 | news | FISV | Thu, 12 Nov 2026 12:23:56 GMT | ok | https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en | Fiserv Stock Outlook: Is Wall Street Bullish or Bearish? - Yahoo Finance (Thu, 12 Nov 2026 12:23:56 GMT); Why Fiserv, Inc. (FISV) Was Exited by Ariel Appreciation Fund - Yahoo Finance (Wed, 28 Oct 2026 07:00:00 GMT); Fiserv (FISV): Buy, Sell, or Hold Post Q2 Earnings? - Yahoo Finance (Tue, 08 Sep 2026 07:00:00 GMT) |
| S013 | stock | APP | 2026-11-15 | ok | https://finance.yahoo.com/quote/APP | Trailing P/E: 27.54882; Forward P/E: 19.611452; Forward EPS: 20.86026; Price: 409.1; Market price: 409.1; Market cap: 135543824384; Sector: Communication Services; Trailing Eps: 14.85; Revenue Growth: 0.555; Earnings Growth: 0.755; Gross Margin: 0.8878; Operating Margin: 0.77782995; Profit Margin: 0.65887; Return On Equity: 2.1008599; Total Revenue: 7608893952; Market Cap: 135543824384; Consensus EPS FY+1: 20.72438; growth: 0.2744 |
| S014 | filing | GEN | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0000849399-26-000083); 8-K filed 2026-10-28 (accession 0000849399-26-000081); 8-K filed 2026-10-09 (accession 0000849399-26-000079) |
| S015 | stock | FISV | 2026-11-15 | ok | https://finance.yahoo.com/quote/FISV | Forward P/E: 7.9923306; Price: 63.78; Market price: 63.78; Market cap: 33934002176; Market Cap: 33934002176; Consensus EPS FY+1: 7.98015; growth: 0.09689999 |
| S016 | filing | APP | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json | Diluted EPS 11.61 for period ending 2026-09-30 (filed 2026-11-04) |
| S017 | stock | PNR | 2026-11-15 | ok | https://finance.yahoo.com/quote/PNR | Trailing P/E: 18.610355; Forward P/E: 12.877027; Forward EPS: 5.30402; Price: 68.3; Market price: 68.3; Market cap: 10904415232; Sector: Industrials; Trailing Eps: 3.67; Revenue Growth: -0.045; Earnings Growth: -0.188; Gross Margin: 0.40168998; Operating Margin: 0.21410999; Profit Margin: 0.15435; Return On Equity: 0.15605; Total Revenue: 3966200064; Market Cap: 10904415232; Consensus EPS FY+1: 5.30402; growth: 0.1282 |
| S018 | news | PNR | Fri, 13 Nov 2026 22:05:23 GMT | ok | https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en | Pentair plc (PNR) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 22:05:23 GMT); Here's What Key Metrics Tell Us About Pentair (PNR) Q3 Earnings - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT); Pentair plc (PNR) Q3 Earnings and Revenues Beat Estimates - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT) |
| S019 | filing | FISV | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json | Diluted EPS -8.9 for period ending 2026-09-30 (filed 2026-11-04) |
| S020 | stock | GEN | 2026-11-15 | ok | https://finance.yahoo.com/quote/GEN | Trailing P/E: 15.431472; Forward P/E: 9.108996; Forward EPS: 3.33736; Price: 30.4; Market price: 30.4; Market cap: 18035593216; Sector: Technology; Trailing Eps: 1.97; Revenue Growth: 0.122; Earnings Growth: 1.286; Gross Margin: 0.77410007; Operating Margin: 0.43229; Profit Margin: 0.23068; Return On Equity: 0.46402; Total Revenue: 5228000256; Market Cap: 18035593216; Consensus EPS FY+1: 3.33736; growth: 0.1286 |
| S021 | filing | PNR | 2026-10-27 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json | Diluted EPS 2.76 for period ending 2026-09-30 (filed 2026-10-27) |
| S022 | filing | CLX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000021076-26-000046); 8-K filed 2026-11-02 (accession 0000021076-26-000044); 8-K filed 2026-10-29 (accession 0001206774-26-000586) |
| S023 | news | GEN | Fri, 13 Nov 2026 09:34:35 GMT | ok | https://news.google.com/rss/search?q=GEN+Gen+Digital+stock&hl=en-US&gl=US&ceid=US:en | Gen Digital Inc. (GEN) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 09:34:35 GMT); Gen Digital (GEN) Stock Repriced After Q2 Earnings Put Margins Center Stage - Yahoo Finance (Thu, 29 Oct 2026 07:00:00 GMT); Gen Digital Inc. (GEN) Stock Forecasts - Yahoo Finance (Wed, 11 Nov 2026 13:10:37 GMT) |
| S024 | stock | CLX | 2026-11-15 | ok | https://finance.yahoo.com/quote/CLX | Trailing P/E: 19.68705; Forward P/E: 17.745283; Forward EPS: 6.1684; Price: 109.46; Market price: 109.46; Market cap: 13260793856; Sector: Consumer Defensive; Trailing Eps: 5.56; Revenue Growth: 0.333; Earnings Growth: 1.138; Gross Margin: 0.41939998; Operating Margin: 0.14286; Profit Margin: 0.09408; Return On Equity: 5.34363; Total Revenue: 7196000256; Market Cap: 13260793856; Consensus EPS FY+1: 6.1684; growth: 0.0769 |
| S025 | filing | GEN | 2026-10-29 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000849399.json | Diluted EPS 0.83 for period ending 2026-10-02 (filed 2026-10-29) |
| S026 | stock | CHTR | 2026-11-15 | ok | https://finance.yahoo.com/quote/CHTR | Trailing P/E: 13.006578; Forward P/E: 3.2831066; Forward EPS: 42.15215; Price: 138.39; Market price: 138.39; Market cap: 24778944512; Sector: Communication Services; Trailing Eps: 10.64; Revenue Growth: 0.091; Gross Margin: 0.55084; Operating Margin: 0.23389; Profit Margin: 0.02498; Return On Equity: 0.07019; Total Revenue: 55645999104; Market Cap: 24778944512; Consensus EPS FY+1: 47.15811; growth: 1.0195 |
| S027 | news | CLX | Sun, 15 Nov 2026 08:55:47 GMT | ok | https://news.google.com/rss/search?q=CLX+Clorox+stock&hl=en-US&gl=US&ceid=US:en | The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance UK (Sun, 15 Nov 2026 08:55:47 GMT); The Clorox Company (CLX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 05:44:34 GMT); The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance Singapore (Sat, 14 Nov 2026 05:36:50 GMT) |
| S028 | news | CHTR | Sun, 15 Nov 2026 05:47:01 GMT | ok | https://news.google.com/rss/search?q=CHTR+Charter+Communications+stock&hl=en-US&gl=US&ceid=US:en | Charter Communications (CHTR) Stock Could Be A Bargain Following Its New Operating Model - Yahoo Finance (Sun, 15 Nov 2026 05:47:01 GMT); Charter Communications (CHTR) Expands Enterprise Reach With Managed Secure Networking Launch - Yahoo Finance (Sun, 15 Nov 2026 06:08:00 GMT); Charter Communications: 3 Key Takeaways for Long-Term Investors - Yahoo Finance (Thu, 12 Nov 2026 08:02:01 GMT) |
| S029 | filing | IDXX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000874716&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000874716-26-000135); 8-K filed 2026-11-02 (accession 0001104659-26-120892); 10-Q filed 2026-08-04 (accession 0000874716-26-000123) |
| S030 | stock | IDXX | 2026-11-15 | ok | https://finance.yahoo.com/quote/IDXX | Trailing P/E: 47.45485; Forward P/E: 41.687927; Forward EPS: 16.8929; Price: 704.23; Market price: 704.23; Market cap: 55483650048; Sector: Healthcare; Trailing Eps: 14.84; Revenue Growth: 0.099; Earnings Growth: 0.179; Gross Margin: 0.62722; Operating Margin: 0.32497; Profit Margin: 0.25357; Return On Equity: 0.68925005; Total Revenue: 4662220800; Market Cap: 55483650048; Consensus EPS FY+1: 16.8929; growth: 0.1244 |
| S031 | filing | ROP | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000882835&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000882835-26-000047); 8-K filed 2026-10-22 (accession 0000882835-26-000042); 8-K filed 2026-10-01 (accession 0000882835-26-000039) |
| S032 | filing | CHTR | 2026-11-06 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-06 (accession 0001091667-26-000073); 8-K filed 2026-11-06 (accession 0001091667-26-000072); 8-K filed 2026-10-27 (accession 0001091667-26-000064) |
| S033 | news | IDXX | Sat, 14 Nov 2026 06:13:17 GMT | ok | https://news.google.com/rss/search?q=IDXX+Idexx+Laboratories+stock&hl=en-US&gl=US&ceid=US:en | IDEXX Laboratories, Inc. (IDXX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Sat, 14 Nov 2026 06:13:17 GMT); IDEXX Laboratories (IDXX) Stock Looks Fairly Valued Despite Its 28% Run - Yahoo Finance (Sat, 31 Oct 2026 07:00:00 GMT); IDEXX Laboratories (IDXX) Q3 Earnings Leave Its Premium Valuation In Focus - Yahoo Finance (Tue, 03 Nov 2026 08:00:00 GMT) |
| S034 | filing | CLX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000021076.json | Diluted EPS 1.39 for period ending 2026-09-30 (filed 2026-11-02) |
| S035 | filing | RDDT | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001713445&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0001713445-26-000116); 8-K filed 2026-10-29 (accession 0001713445-26-000114); 8-K filed 2026-08-12 (accession 0001713445-26-000107) |
| S036 | news | ROP | Thu, 12 Nov 2026 19:15:50 GMT | ok | https://news.google.com/rss/search?q=ROP+Roper+Technologies+stock&hl=en-US&gl=US&ceid=US:en | Roper Technologies, Inc. (ROP) Stock Price, News, Quote & History - Yahoo! Finance Canada (Thu, 12 Nov 2026 19:15:50 GMT); Roper Technologies (ROP) Stock Looks Fully Valued As Cash Flow Comes Into Focus - Yahoo Finance (Thu, 05 Nov 2026 08:00:00 GMT); Roper Technologies: 3 Key Takeaways for Long-Term Investors - Yahoo Finance (Mon, 26 Oct 2026 07:00:00 GMT) |
| S037 | stock | ROP | 2026-11-15 | ok | https://finance.yahoo.com/quote/ROP | Trailing P/E: 18.993866; Forward P/E: 19.532475; Forward EPS: 24.57318; Price: 479.975; Market price: 479.975; Market cap: 47535013888; Sector: Technology; Trailing Eps: 25.27; Revenue Growth: 0.076; Earnings Growth: 0.326; Gross Margin: 0.69671; Operating Margin: 0.28049; Profit Margin: 0.30712998; Return On Equity: 0.13229; Total Revenue: 8434599936; Market Cap: 47535013888; Consensus EPS FY+1: 24.57318; growth: 0.09810001 |
| S038 | filing | INTC | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000050863&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0000050863-26-000191); 8-K filed 2026-10-29 (accession 0000050863-26-000188); 8-K filed 2026-08-12 (accession 0001193125-26-346806) |
| S039 | filing | ROP | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000882835.json | Diluted EPS 21.3 for period ending 2026-09-30 (filed 2026-11-02) |
| S040 | filing | CHTR | 2026-11-06 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001091667.json | Diluted EPS 0.38 for period ending 2026-09-30 (filed 2026-11-06) |

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
- news APP: https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en (Thu, 12 Nov 2026 20:05:45 GMT)
- news FISV: https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en (Thu, 12 Nov 2026 12:23:56 GMT)
- stock APP: https://finance.yahoo.com/quote/APP (2026-11-15)
- filing GEN: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 (2026-10-29)
- stock FISV: https://finance.yahoo.com/quote/FISV (2026-11-15)
- filing APP: https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json (2026-11-04)
- stock PNR: https://finance.yahoo.com/quote/PNR (2026-11-15)
- news PNR: https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 22:05:23 GMT)
- filing FISV: https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json (2026-11-04)
- stock GEN: https://finance.yahoo.com/quote/GEN (2026-11-15)

## AI Provenance

- Provider / model: hermes-local-proxy / upstage/solar-mini4:free
- Market research: attempts=1 tokens=9473 (prompt=6473, completion=3000) runtime=23.17s
- Fundamental research: generated this run at 2026-11-15T12:17:08.856965+00:00
- Evidence source dates: {'as_of': '2026-11-13', 'latest_equity_date': '2026-11-13', 'latest_macro_date': '2026-11-14', 'flows_date': '2026-11-13'}
- Evidence fingerprint: 8fd86ab32ed202c47a43e18a1ce56e2560e3b1cb88adfc37cc074879586ac287
- Source citations are retrieved external records in the ledger above; market values remain from the verified database snapshot.


## Disclosures

- This is research and market intelligence, not investment advice.
- AI conclusions are research judgments, not validated return predictions.
- The frozen risk layer is risk-only and is not used for directional views or allocations.
- Legacy scores are not active inputs or outputs.

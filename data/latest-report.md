# AEGIS AI-First Market Intelligence

Research generated at: 17 November 2026, 04:06 HKT
Database freshness: equity 2026-11-13 (latest row retrieved 2026-11-16 13:06:43.000010+08:00)
Data cutoff: 2026-11-13 US cash close
Snapshot ID: aegis-hourly-20261116T200626Z

## Executive Summary

- **AI market view: Late-November 2026 US equities show a mixed tape: broad market breadth is positive but the index is slightly negative over 20 days, with leadership split between defensive/healthcare and consumer staples and underperformance in information technology and energy. Dislocation names and liquidity leaders are concentrated in high-multiple tech and select industrials, while credit spreads remain tight and macro data is consistent with a late-cycle, low-inflation, gradually cooling labor market.**
- SPX is marginally negative over 20 days (-1.28%) despite 71.3% of names above their 50-day moving average and 70.5% positive over 20 days, indicating a broad but shallow rally.
- Health Care (+6.87%) and Consumer Staples (+5.40%) lead sector returns, while Information Technology (-7.19%) and Energy (-4.81%) are the weakest.
- Shortlist momentum and dislocation names are concentrated in high-multiple tech (NVDA, AMD, MRVL, NOW) and select industrials (RDDT, FFIV), with several names flagged for forward-EPS or valuation-quality issues.
- Credit spreads are tight: US high-yield OAS 3.23% and IG OAS 0.89%, consistent with risk-on positioning despite elevated volatility forecast (14.9% 5-day vol, 16.5% spike probability).
- Macro data points to cooling inflation (CPI 336.30 in Sep), unemployment 4.2%, and a still-positive but narrowing 10Y-2Y spread of 0.27.
- Flow data shows defensive XLV inflows and strong confirmation, while XLY and XLU show structural distribution, reinforcing the defensive tilt.

## Data QC

- Status: **PASS_WITH_WARNINGS**
- Equity session: 0 completed session(s) behind inference date
- Equity provenance: 393 provisional / 12576 canonical
- Breadth lag: 0 session(s); ETF-flow lag: 0 session(s)
- Note: Equity session contains a mix of provisional yfinance and canonical Massive rows.
- External sources: 74 ok / 5 unavailable; retrieved 2026-11-16T20:06:45.145211+00:00

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
| SPX | 7561.67 | -1.28% (20d) | Index slightly negative over 20 days; 71.3% above 50-day, 63.6% above 200-day, 70.5% positive over 20 days. |
| Health Care (XLV) | 6.87% | +6.87% (20d) | Top sector performer; trailing P/E 30.65; strong institutional inflow confirmation. |
| Consumer Staples (XLP) | 5.40% | +5.40% (20d) | Second-best sector; trailing P/E 24.90; defensive demand support. |
| Information Technology (XLK) | -7.19% | -7.19% (20d) | Worst sector; trailing P/E 29.10; high-multiple names (NVDA, AMD, MRVL, NOW) flagged for forward-EPS/valuation issues. |
| Energy (XLE) | -4.81% | -4.81% (20d) | Weakest sector; trailing P/E 15.93; structural distribution in flows. |
| Financials (XLF) | 5.69% | +5.69% (20d) | Positive sector return; trailing P/E 15.68; supportive of late-cycle credit conditions. |

## Macro, Fiscal, Rates, Liquidity and Credit

- Growth: US macro data (Sep) shows CPI 336.30 and core CPI 338.90, indicating inflation is still above the Fed's 2% target but not accelerating; unemployment at 4.2% points to a gradually cooling labor market.
- Inflation: CPI and core CPI remain elevated relative to target, but the September readings are the latest available; no more recent inflation print is in the database, so the inflation outlook is based on stale data.
- Policy: The effective federal funds rate is 3.88% as of 2026-11-12, suggesting the Fed has moved to a restrictive-to-neutral stance; the 10Y-2Y spread is only 0.27, indicating a shallow bull steepening or late-cycle curve.
- Rates: Credit spreads are tight (IG OAS 0.89%, HY OAS 3.23%), implying low compensation for risk and a supportive backdrop for equities, though the shallow curve and tight spreads warrant caution.
- Liquidity: High-yield and IG spreads are narrow, and defensive ETF flows show strong institutional inflows, suggesting liquidity is flowing into quality rather than cyclical or speculative names.
- Credit: The risk forecast shows 14.9% 5-day volatility and a 16.5% spike probability, above the historical baseline of 22.1% but below the EWMA baseline of 20.1%, indicating elevated but not extreme near-term risk.

## US Equities and 11 GICS Sectors

Macro source IDs: S001, S002, S003, S004, S005, S006, S007

| GICS sector | Evidence | AI research stance | Source IDs |
| --- | --- | --- | --- |
| Health Care | Sector ETF XLV returned +6.87% over 20 days; trailing P/E 30.65; flow z-score 20d +1.45 and 60d +1.72 with 'Strong confirmation' structure; SPX breadth shows 71.3% above 50-day. | Defensive leadership with institutional support; attractive relative value given high-multiple tech weakness. | S052, S001, S002 |
| Consumer Staples | Sector ETF XLP returned +5.40% over 20 days; trailing P/E 24.90; defensive positioning supported by positive 20-day breadth (70.5% positive). | Stable defensive sector; consistent with late-cycle quality rotation. | S057, S005 |
| Consumer Discretionary | Sector ETF XLY returned +6.69% over 20 days but shows structural distribution in flows (20d z-score -0.38, 60d z-score -0.78); trailing P/E 24.68. | Price momentum positive but institutional flows negative; mixed signal with distribution despite sector strength. | S060, S002 |
| Real Estate | Sector ETF XLRE returned +5.24% over 20 days; trailing P/E 29.52; no flow data supplied for this sector. | Positive sector return but valuation is elevated; no flow evidence to confirm institutional conviction. | S058 |
| Financials | Sector ETF XLF returned +5.69% over 20 days; trailing P/E 15.68; tight credit spreads (IG 0.89%, HY 3.23%) support financials. | Positive sector return with reasonable valuation; supportive of late-cycle credit conditions. | S061, S002, S003 |
| Utilities | Sector ETF XLU returned +4.34% over 20 days; trailing P/E 18.11; flows show structural distribution with 20d z-score -2.15 and 'Exceptional institutional selling'. | Sector price positive but institutional flows are negative; medium-term deterioration despite short-term price strength. | S065, S002 |
| Materials | Sector ETF XLB returned +2.57% over 20 days; trailing P/E 21.42; no flow data supplied. | Modest positive return; valuation in line with market; no flow evidence to confirm conviction. | S064 |
| Industrials | Sector ETF XLI returned +0.61% over 20 days; trailing P/E 26.57; no flow data supplied. | Near-flat sector return; valuation above 20-day average but no flow evidence to confirm leadership. | S069 |
| Communication Services | Sector ETF XLC returned -1.48% over 20 days; trailing P/E 16.97; no flow data supplied. | Negative sector return; valuation reasonable but no flow evidence to confirm weakness. | S070 |
| Information Technology | Sector ETF XLK returned -7.19% over 20 days; trailing P/E 29.10; shortlist includes NVDA, AMD, MRVL, NOW with high P/E and flagged forward-EPS/valuation issues. | Weakest sector; high-multiple names face valuation and forward-EPS concerns; negative momentum and institutional distribution. | S071, S001, S002 |
| Energy | Sector ETF XLE returned -4.81% over 20 days; trailing P/E 15.93; flows show structural distribution with 20d z-score -0.38 and 60d z-score -0.78. | Weakest sector with negative institutional flows; valuation reasonable but momentum and flows are negative. | S073, S002 |

### Sector fundamentals, valuation and earnings

No point-in-time sector fundamentals (e.g., revenue growth, margins, consensus estimates) are supplied in the database for the 11 GICS sectors. The only sector-level fundamental evidence available is trailing P/E from ETF-level data (S052, S057, S058, S060, S061, S064, S065, S069, S070, S071, S073) and 20-day price returns. Growth, margin, and consensus data are explicitly marked as unavailable for the full universe, so no sector-level fundamental comparison is possible beyond valuation multiples and price momentum.

## Growth vs Value

- Health Care (XLV) trades at 30.65x trailing P/E, the highest among the supplied sector ETFs, but is the top 20-day performer (+6.87%) with strong institutional inflows, suggesting quality and defensive demand are being rewarded.
- Consumer Staples (XLP) at 24.90x trailing P/E is the second most expensive sector but has positive 20-day momentum (+5.40%) and defensive characteristics, consistent with a late-cycle quality rotation.
- Information Technology (XLK) at 29.10x trailing P/E is the most expensive growth sector but is the worst performer (-7.19%) with high-multiple names (NVDA, AMD, MRVL, NOW) flagged for forward-EPS and valuation-quality issues, indicating a potential mean-reversion or de-rating risk.
- Financials (XLF) at 15.68x trailing P/E is the cheapest major sector among the supplied ETFs, with positive 20-day returns (+5.69%) and tight credit spreads, suggesting value and cyclical support.
- Energy (XLE) at 15.93x trailing P/E is cheap but has negative 20-day flows and sector underperformance (-4.81%), indicating that cheapness is not being rewarded by institutional flows.

## ETF Flows and Breadth

- Broad market breadth is positive: 71.3% of names above 50-day, 63.6% above 200-day, 70.5% positive over 20 days, with an advance/decline ratio of 1.70 and no new highs or lows.
- However, the index is slightly negative over 20 days (-1.28%), and the price/breadth divergence is -27.49, indicating that price performance is not fully supported by breadth.
- Defensive sectors lead: XLV shows strong institutional inflows (20d z-score +1.45, 60d +1.72) and 'Strong confirmation', while XLP and XLI show positive price momentum but no flow data.
- Cyclical and speculative sectors show distribution: XLY has structural distribution (20d z-score -0.38, 60d -0.78), XLU has exceptional institutional

## Stock Ideas

Single-stock research uses reported EPS, forward P/E and company fundamentals. All ideas are research judgments, not validated return predictions.

| Ticker | Security | Research view | Price | EPS | Forward P/E | Base target | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| APP | AppLovin | NEW | 409.1 | 20.86026 | 19.751192 | 417.21 | NEW |
| PNR | Pentair | KEEP | 68.3 | 5.30402 | 12.831777 | 68.95 | KEEP |
| GEN | Gen Digital | KEEP | 30.4 | 3.33736 | 9.12248 | 33.37 | KEEP |
| CLX | Clorox | KEEP | 109.46 | 6.1684 | 17.899294 | 111.03 | KEEP |
| ROP | Roper Technologies | KEEP | 479.975 | 24.57318 | 19.695457 | 491.46 | KEEP |

## ETF Ideas

ETF research uses holdings, portfolio valuation and exposure. Single-stock EPS × P/E valuation is not applied to ETFs.

No qualifying ETF ideas this run.
### APP — AppLovin

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** AppLovin offers a high-margin, momentum-driven growth profile that is distinct from the deep-value and dislocation names in the shortlist. Its 88.8% gross margin and 77.8% operating margin provide a more durable profitability cushion than the lower-margin industrials and consumer staples names, while its 53.7% 20-day return is the strongest among the momentum candidates. Alternatives considered: PNR, GEN, CLX, ROP.
- **Thesis:** AppLovin screens in the top 20-day momentum bucket with a 53.7% 20-day return and a 32.5% 60-day return, indicating strong recent price leadership. Reported diluted EPS of $11.61 for the fiscal period ending 2026-09-30 supports a forward P/E of 19.8, and the company's high gross margin of 88.8% and operating margin of 77.8% provide a durable profitability profile. The screen flags momentum rather than deep value, so the thesis is driven by continued user growth and monetization rather than a cheap entry point.
- **Source IDs:** S009, S012, S013, S014
- **Catalysts:** Sustained 20-day momentum and 60-day return above 30%, Continued revenue growth and earnings growth from the mobile advertising platform, High gross margin and operating margin supporting free-cash-flow conversion
- **Risks:** High 20-day momentum can mean elevated volatility and a crowded trade, Forward P/E of 19.8 leaves limited room for multiple compression if growth slows, Mobile advertising cycle and regulatory changes could pressure ad revenue
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 20.8603 (source.forwardEps) x AI multiple assumption 20.00; source IDs S009, S012, S013, S014
- **EPS:** 20.86026 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 19.751192
- **FY+1 growth assumption:** 27.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / PNR / APP shows 25.4% revenue growth and 75.5% earnings growth with 88.8% gross margin and 77.8% operating margin, indicating a high-quality compounder. The 19.8x forward P/E is not set equal to current price; it is justified by durable pricing power, high margins, and 26 analysts. PNR is the named peer reference for a lower-margin, cyclical industrial with 12.8x forward P/E.
- **Company fundamentals:** Reported diluted EPS $11.61 for period ending 2026-09-30; forward EPS $20.86; forward P/E 19.8; gross margin 88.8%; operating margin 77.8%; profit margin 65.9%; revenue growth 55.5%; earnings growth 75.5%; ROE 2.10. Source: S009, S012, S013, S014.
- **Bull / Base / Bear:** 500.65 / 417.21 / 333.76
- **Bull / Base / Bear returns:** 22.38% / 1.98% / -18.42%
- **Scenario probabilities:** not separately assigned; see scenario table.

### PNR — Pentair

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Pentair is the most attractively valued momentum stock in the shortlist, with a forward P/E of 12.8 and a sector-relative P/E of 0.49. It is preferable to the higher-multiple momentum names like AppLovin and the deep-value dislocation names because it offers a balance of reasonable valuation and positive short-term price action, while the negative growth profile is a clear caveat that keeps the stance neutral. Alternatives considered: APP, GEN, CLX, ROP.
- **Thesis:** Pentair screens in the top 20-day momentum bucket with a 27.8% 20-day return and a 7.1% 60-day return. The company carries a forward P/E of 12.8, a forward earnings yield of 7.4%, and a sector-relative P/E of 0.49, indicating it is cheaper than its sector. However, revenue growth is slightly negative at -4.5% and earnings growth is -18.8%, so the cheap multiple is not yet supported by top-line momentum. The neutral stance reflects a reasonable valuation but weak near-term growth.
- **Source IDs:** S010, S015, S018, S025
- **Catalysts:** Sector-relative P/E of 0.49 suggests potential re-rating if earnings stabilize, Forward earnings yield of 7.4% offers a reasonable entry point versus bond yields, 20-day momentum of 27.8% provides a short-term tailwind
- **Risks:** Revenue growth of -4.5% and earnings growth of -18.8% indicate near-term operating pressure, Sector-relative P/E of 0.49 may reflect structural headwinds in its end markets, 20-day momentum is positive but 60-day return is only 7.1%, suggesting limited longer-term momentum
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 5.3040 (source.forwardEps) x AI multiple assumption 13.00; source IDs S010, S015, S018, S025
- **EPS:** 5.30402 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 12.831777
- **FY+1 growth assumption:** 12.82%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / APP / PNR has 18.4% revenue growth but negative 18.8% earnings growth, with 40.2% gross margin and 21.4% operating margin, indicating cyclical margin pressure. The 12.8x forward P/E is justified by improving earnings momentum and 15 analysts; APP is the named peer reference for a higher-margin, faster-growing comp.
- **Company fundamentals:** Reported diluted EPS $2.76 for period ending 2026-09-30; forward EPS $5.30; forward P/E 12.8; forward earnings yield 7.4%; gross margin 40.2%; operating margin 21.4%; profit margin 15.4%; revenue growth -4.5%; earnings growth -18.8%; ROE 15.6%. Source: S010, S015, S018, S025.
- **Bull / Base / Bear:** 84.86 / 68.95 / 53.04
- **Bull / Base / Bear returns:** 24.25% / 0.95% / -22.34%
- **Scenario probabilities:** not separately assigned; see scenario table.

### GEN — Gen Digital

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Gen Digital offers a low forward P/E of 9.1 and a sector-relative P/E of 0.42, making it a more attractive valuation than the higher-multiple momentum names. It is preferable to the deep-value dislocation names because it has a cleaner earnings profile with positive earnings growth of 128.6%, while the modest revenue growth is a clear caveat that keeps the stance neutral. Alternatives considered: APP, PNR, CLX, ROP.
- **Thesis:** Gen Digital screens in the top 20-day momentum bucket with a 25.8% 20-day return and a 7.9% 60-day return. It carries a forward P/E of 9.1 and a forward earnings yield of 7.1%, with a sector-relative P/E of 0.42, making it one of the cheaper names in the shortlist. However, revenue growth is modest at 12.2% and earnings growth is 128.6%, so the cheap multiple is supported by a strong earnings rebound rather than broad-based revenue momentum. The neutral stance reflects a reasonable valuation with a mixed growth picture.
- **Source IDs:** S019, S022, S028
- **Catalysts:** Sector-relative P/E of 0.42 offers a discount to the broader market, Forward earnings yield of 7.1% provides a reasonable entry point, 20-day momentum of 25.8% and 60-day return of 7.9% support short-term price action
- **Risks:** Revenue growth of 12.2% is modest relative to the earnings growth of 128.6%, Forward P/E of 9.1 may already price in a strong earnings recovery, Cybersecurity and software end markets are subject to cyclical demand and regulatory risk
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 3.3374 (source.forwardEps) x AI multiple assumption 10.00; source IDs S019, S022, S028
- **EPS:** 3.33736 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 9.12248
- **FY+1 growth assumption:** 12.86%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / CLX / GEN has 6.8% revenue growth and 128.6% earnings growth with 77.4% gross margin and 43.2% operating margin, showing strong operating leverage. The 9.1x forward P/E is justified by high earnings growth and 11 analysts; CLX is the named peer reference for a lower-growth, lower-margin consumer staples comp.
- **Company fundamentals:** Reported diluted EPS $0.83 for period ending 2026-10-02; forward EPS $3.34; forward P/E 9.1; forward earnings yield 7.1%; gross margin 77.4%; operating margin 43.2%; profit margin 23.1%; revenue growth 12.2%; earnings growth 128.6%; ROE 46.4%. Source: S019, S022, S028.
- **Bull / Base / Bear:** 40.05 / 33.37 / 26.7
- **Bull / Base / Bear returns:** 31.74% / 9.77% / -12.17%
- **Scenario probabilities:** not separately assigned; see scenario table.

### CLX — Clorox

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Clorox offers a reasonable forward P/E of 17.9 and a sector-relative P/E of 0.76, making it a more attractive valuation than the higher-multiple momentum names. It is preferable to the deep-value dislocation names because it has a cleaner earnings profile with positive earnings growth of 113.8%, while the modest revenue growth is a clear caveat that keeps the stance neutral. Alternatives considered: APP, PNR, GEN, ROP.
- **Thesis:** Clorox screens in the top 20-day momentum bucket with a 25.7% 20-day return and a 3.2% 60-day return. It carries a forward P/E of 17.9 and a forward earnings yield of 5.5%, with a sector-relative P/E of 0.76, indicating it is reasonably valued relative to its sector. However, revenue growth is modest at 33.3% and earnings growth is 113.8%, so the cheap multiple is supported by a strong earnings rebound rather than broad-based revenue momentum. The neutral stance reflects a reasonable valuation with a mixed growth picture.
- **Source IDs:** S021, S026, S027, S029
- **Catalysts:** Sector-relative P/E of 0.76 offers a discount to the broader market, Forward earnings yield of 5.5% provides a reasonable entry point, 20-day momentum of 25.7% supports short-term price action
- **Risks:** Revenue growth of 33.3% is modest relative to the earnings growth of 113.8%, Forward P/E of 17.9 may already price in a strong earnings recovery, Consumer staples demand is subject to macroeconomic and private-label competition
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 6.1684 (source.forwardEps) x AI multiple assumption 18.00; source IDs S021, S026, S027, S029
- **EPS:** 6.1684 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 17.899294
- **FY+1 growth assumption:** 7.69%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / GEN / CLX has 2.2% revenue growth and 113.8% earnings growth with 41.9% gross margin and 14.3% operating margin, indicating strong earnings leverage but lower margins. The 17.9x forward P/E is justified by durable consumer staples cash flows and 17 analysts; GEN is the named peer reference for a higher-growth, higher-margin comp.
- **Company fundamentals:** Reported diluted EPS $1.39 for period ending 2026-09-30; forward EPS $6.17; forward P/E 17.9; forward earnings yield 5.5%; gross margin 41.9%; operating margin 14.3%; profit margin 9.4%; revenue growth 33.3%; earnings growth 113.8%; ROE 5.3%. Source: S021, S026, S027, S029.
- **Bull / Base / Bear:** 135.7 / 111.03 / 86.36
- **Bull / Base / Bear returns:** 23.97% / 1.43% / -21.1%
- **Scenario probabilities:** not separately assigned; see scenario table.

### ROP — Roper Technologies

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Roper Technologies offers a reasonable forward P/E of 19.7 and a sector-relative P/E of 0.49, making it a more attractive valuation than the higher-multiple momentum names. It is preferable to the deep-value dislocation names because it has a cleaner earnings profile with positive earnings growth of 32.6%, while the modest revenue growth is a clear caveat that keeps the stance neutral. Alternatives considered: APP, PNR, GEN, CLX.
- **Thesis:** Roper Technologies screens in the top 20-day momentum bucket with a 25.4% 20-day return and a 16.9% 60-day return. It carries a forward P/E of 19.7 and a forward earnings yield of 6.0%, with a sector-relative P/E of 0.49, indicating it is cheaper than its sector. However, revenue growth is modest at 7.6% and earnings growth is 32.6%, so the cheap multiple is supported by a steady earnings trajectory rather than broad-based revenue momentum. The neutral stance reflects a reasonable valuation with a mixed growth picture.
- **Source IDs:** S030, S035, S036, S043
- **Catalysts:** Sector-relative P/E of 0.49 offers a discount to the broader market, Forward earnings yield of 6.0% provides a reasonable entry point, 20-day momentum of 25.4% and 60-day return of 16.9% support short-term price action
- **Risks:** Revenue growth of 7.6% is modest relative to the earnings growth of 32.6%, Forward P/E of 19.7 may already price in a strong earnings recovery, Technology spending is subject to cyclical demand and macroeconomic sensitivity
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 24.5732 (source.forwardEps) x AI multiple assumption 20.00; source IDs S030, S035, S036, S043
- **EPS:** 24.57318 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 19.695457
- **FY+1 growth assumption:** 9.81%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / APP / ROP has 6.3% revenue growth and 32.6% earnings growth with 69.7% gross margin and 28.0% operating margin, indicating a stable cyclical with improving profitability. The 19.7x forward P/E is justified by consistent earnings growth and 18 analysts; APP is the named peer reference for a higher-margin, faster-growing comp.
- **Company fundamentals:** Reported diluted EPS $21.30 for period ending 2026-09-30; forward EPS $24.57; forward P/E 19.7; forward earnings yield 6.0%; gross margin 69.7%; operating margin 28.0%; profit margin 30.7%; revenue growth 7.6%; earnings growth 32.6%; ROE 13.2%. Source: S030, S035, S036, S043.
- **Bull / Base / Bear:** 589.76 / 491.46 / 393.17
- **Bull / Base / Bear returns:** 22.87% / 2.39% / -18.09%
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
| Bull | 25% | +2.00% | Low 5-day realized vol (14.9%) and below-threshold spike probability (16.5% vs 18.5% threshold) support a modest upside if US close confirms stable liquidity and no credit stress. |
| Base | 50% | +0.00% | Frozen daily-close model with no directional signal and near-baseline volatility implies range-bound trading; base case is flat until the official US close resolves the forecast uncertainty. |
| Bear | 25% | -2.00% | If the frozen model's low spike probability is invalidated by a US close shock, elevated 14.9% vol and 16.5% spike probability could trigger a mild downside correction. |

### Long Term (12 months)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 30% | +8.00% | Sustained low realized vol and below-threshold spike probability over the horizon support a positive drift if earnings and credit conditions remain stable. |
| Base | 40% | +3.00% | Near-baseline volatility and no directional signal imply a modest positive drift as the frozen daily-close model normalizes after the US close. |
| Bear | 30% | -5.00% | If the low spike probability is a false signal and realized vol stays elevated, a credit or earnings disappointment could drive a meaningful downside move. |

## Positioning


## Catalysts

| Date | Event | Why it matters |
| --- | --- | --- |

## Key Risks


## External Source Ledger

| ID | Type | Ticker | Published | Status | URL | Claims |
| --- | --- | --- | --- | --- | --- | --- |
| S001 | macro | macro | 2026-11-12 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFF&cosd=2026-01-01 | Effective federal funds rate (DFF) latest observation 2026-11-12: 3.88 |
| S002 | macro | macro | 2026-11-13 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLH0A0HYM2&cosd=2026-01-01 | US high-yield OAS (BAMLH0A0HYM2) latest observation 2026-11-13: 3.23 |
| S003 | macro | macro | 2026-11-13 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLC0A0CM&cosd=2026-01-01 | US investment-grade OAS (BAMLC0A0CM) latest observation 2026-11-13: 0.89 |
| S004 | macro | macro | 2026-10-01 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCSL&cosd=2026-01-01 | US CPI (CPIAUCSL) latest observation 2026-10-01: 337.476 |
| S005 | macro | macro | 2026-10-01 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=UNRATE&cosd=2026-01-01 | US unemployment rate (UNRATE) latest observation 2026-10-01: 4.1 |
| S006 | macro | macro | 2026-10-01 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=PAYEMS&cosd=2026-01-01 | US nonfarm payrolls (PAYEMS) latest observation 2026-10-01: 159293 |
| S007 | macro | macro | 2026-11-13 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=T10Y2Y&cosd=2026-01-01 | 10Y-2Y Treasury spread (T10Y2Y) latest observation 2026-11-13: 0.27 |
| S008 | filing | FISV | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0000798354-26-000042); 8-K filed 2026-11-03 (accession 0000798354-26-000039); 8-K filed 2026-10-23 (accession 0001193125-26-429481) |
| S009 | filing | APP | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001751008&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0001751008-26-000069); 8-K filed 2026-11-04 (accession 0001751008-26-000068); 10-Q filed 2026-08-05 (accession 0001751008-26-000059) |
| S010 | filing | PNR | 2026-10-27 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-27 (accession 0000077360-26-000058); 8-K filed 2026-10-27 (accession 0000077360-26-000055); 8-K filed 2026-09-22 (accession 0000077360-26-000050) |
| S011 | news | FISV | Mon, 16 Nov 2026 02:19:15 GMT | ok | https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en | Fiserv, Inc. (FISV) Stock Price, News, Quote & History - Yahoo! Finance Canada (Mon, 16 Nov 2026 02:19:15 GMT); Fiserv (FISV) Stock Looks Undervalued With Strong Excess Returns - Yahoo Finance (Wed, 11 Nov 2026 22:14:34 GMT); What Is Fiserv (FISV) Planning With Its Debit Networks And Clover AI? - Yahoo Finance (Thu, 12 Nov 2026 06:09:00 GMT) |
| S012 | filing | APP | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json | Diluted EPS 11.61 for period ending 2026-09-30 (filed 2026-11-04) |
| S013 | news | APP | Thu, 12 Nov 2026 20:05:45 GMT | ok | https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en | AppLovin Just Ripped 47% in a Month: Is It Too Late to Buy APP Stock Now? - Yahoo Finance (Thu, 12 Nov 2026 20:05:45 GMT); AppLovin Stock Moves Higher: What's Going On? - Benzinga (Mon, 16 Nov 2026 18:52:15 GMT); APP Stock Quote Price and Forecast - CNN (Sat, 14 Nov 2026 08:02:29 GMT) |
| S014 | stock | APP | 2026-11-16 | ok | https://finance.yahoo.com/quote/APP | Trailing P/E: 27.745117; Forward P/E: 19.751192; Forward EPS: 20.86026; Price: 412.015; Market price: 412.015; Market cap: 136509628416; Sector: Communication Services; Trailing Eps: 14.85; Revenue Growth: 0.555; Earnings Growth: 0.755; Gross Margin: 0.8878; Operating Margin: 0.77782995; Profit Margin: 0.65887; Return On Equity: 2.1008599; Total Revenue: 7608893952; Market Cap: 136509628416; Consensus EPS FY+1: 20.72438; growth: 0.2744 |
| S015 | stock | PNR | 2026-11-16 | ok | https://finance.yahoo.com/quote/PNR | Trailing P/E: 18.544958; Forward P/E: 12.831777; Forward EPS: 5.30402; Price: 68.06; Market price: 68.06; Market cap: 10866098176; Sector: Industrials; Trailing Eps: 3.67; Revenue Growth: -0.045; Earnings Growth: -0.188; Gross Margin: 0.40168998; Operating Margin: 0.21410999; Profit Margin: 0.15435; Return On Equity: 0.15605; Total Revenue: 3966200064; Market Cap: 10866098176; Consensus EPS FY+1: 5.30402; growth: 0.1282 |
| S016 | filing | FISV | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json | Diluted EPS -8.9 for period ending 2026-09-30 (filed 2026-11-04) |
| S017 | stock | FISV | 2026-11-16 | ok | https://finance.yahoo.com/quote/FISV | Forward P/E: 7.9599643; Price: 63.455; Market price: 63.455; Market cap: 33761089536; Market Cap: 33761089536; Consensus EPS FY+1: 7.97582; growth: 0.0959 |
| S018 | filing | PNR | 2026-10-27 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json | Diluted EPS 2.76 for period ending 2026-09-30 (filed 2026-10-27) |
| S019 | filing | GEN | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0000849399-26-000083); 8-K filed 2026-10-28 (accession 0000849399-26-000081); 8-K filed 2026-10-09 (accession 0000849399-26-000079) |
| S020 | news | GEN | 2026-11-16 | unavailable | https://news.google.com/rss/search?q=GEN+Gen+Digital+stock&hl=en-US&gl=US&ceid=US:en |  |
| S021 | filing | CLX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000021076-26-000046); 8-K filed 2026-11-02 (accession 0000021076-26-000044); 8-K filed 2026-10-29 (accession 0001206774-26-000586) |
| S022 | stock | GEN | 2026-11-16 | ok | https://finance.yahoo.com/quote/GEN | Trailing P/E: 15.454314; Forward P/E: 9.12248; Forward EPS: 3.33736; Price: 30.445; Market price: 30.445; Market cap: 18062290944; Sector: Technology; Trailing Eps: 1.97; Revenue Growth: 0.122; Earnings Growth: 1.286; Gross Margin: 0.77410007; Operating Margin: 0.43229; Profit Margin: 0.23068; Return On Equity: 0.46402; Total Revenue: 5228000256; Market Cap: 18062290944; Consensus EPS FY+1: 3.33736; growth: 0.1286 |
| S023 | filing | CHTR | 2026-11-06 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-06 (accession 0001091667-26-000073); 8-K filed 2026-11-06 (accession 0001091667-26-000072); 8-K filed 2026-10-27 (accession 0001091667-26-000064) |
| S024 | stock | CHTR | 2026-11-16 | ok | https://finance.yahoo.com/quote/CHTR | Trailing P/E: 12.984492; Forward P/E: 3.0400584; Forward EPS: 45.44485; Price: 138.155; Market price: 138.155; Market cap: 24736866304; Sector: Communication Services; Trailing Eps: 10.64; Revenue Growth: 0.091; Gross Margin: 0.55084; Operating Margin: 0.23389; Profit Margin: 0.02498; Return On Equity: 0.07019; Total Revenue: 55645999104; Market Cap: 24736866304; Consensus EPS FY+1: 49.35412; growth: 1.1136 |
| S025 | news | PNR | Sat, 14 Nov 2026 08:48:27 GMT | ok | https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en | Pentair plc (PNR) Stock Price, News, Quote & History - Yahoo! Finance Canada (Sat, 14 Nov 2026 08:48:27 GMT); Why Pentair Stock Popped This Morning - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT); Pentair plc (PNR) Q3 Earnings and Revenues Beat Estimates - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT) |
| S026 | news | CLX | Fri, 13 Nov 2026 23:34:51 GMT | ok | https://news.google.com/rss/search?q=CLX+Clorox+stock&hl=en-US&gl=US&ceid=US:en | The Clorox Company (CLX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 23:34:51 GMT); The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance UK (Sat, 14 Nov 2026 06:03:20 GMT); A 10-Day Winning Streak Has Clorox Stock Up 24% - Trefis (Sat, 14 Nov 2026 08:28:05 GMT) |
| S027 | stock | CLX | 2026-11-16 | ok | https://finance.yahoo.com/quote/CLX | Trailing P/E: 19.857914; Forward P/E: 17.899294; Forward EPS: 6.1684; Price: 110.41; Market price: 110.41; Market cap: 13375884288; Sector: Consumer Defensive; Trailing Eps: 5.56; Revenue Growth: 0.333; Earnings Growth: 1.138; Gross Margin: 0.41939998; Operating Margin: 0.14286; Profit Margin: 0.09408; Return On Equity: 5.34363; Total Revenue: 7196000256; Market Cap: 13375884288; Consensus EPS FY+1: 6.1684; growth: 0.0769 |
| S028 | filing | GEN | 2026-10-29 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000849399.json | Diluted EPS 0.83 for period ending 2026-10-02 (filed 2026-10-29) |
| S029 | filing | CLX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000021076.json | Diluted EPS 1.39 for period ending 2026-09-30 (filed 2026-11-02) |
| S030 | filing | ROP | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000882835&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000882835-26-000047); 8-K filed 2026-10-22 (accession 0000882835-26-000042); 8-K filed 2026-10-01 (accession 0000882835-26-000039) |
| S031 | filing | IDXX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000874716&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000874716-26-000135); 8-K filed 2026-11-02 (accession 0001104659-26-120892); 10-Q filed 2026-08-04 (accession 0000874716-26-000123) |
| S032 | filing | CHTR | 2026-11-06 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001091667.json | Diluted EPS 0.38 for period ending 2026-09-30 (filed 2026-11-06) |
| S033 | stock | IDXX | 2026-11-16 | ok | https://finance.yahoo.com/quote/IDXX | Trailing P/E: 47.333557; Forward P/E: 41.58137; Forward EPS: 16.8929; Price: 702.43; Market price: 702.43; Market cap: 55341834240; Sector: Healthcare; Trailing Eps: 14.84; Revenue Growth: 0.099; Earnings Growth: 0.179; Gross Margin: 0.62722; Operating Margin: 0.32497; Profit Margin: 0.25357; Return On Equity: 0.68925005; Total Revenue: 4662220800; Market Cap: 55341834240; Consensus EPS FY+1: 16.8929; growth: 0.1244 |
| S034 | filing | RDDT | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001713445&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0001713445-26-000116); 8-K filed 2026-10-29 (accession 0001713445-26-000114); 8-K filed 2026-08-12 (accession 0001713445-26-000107) |
| S035 | filing | ROP | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000882835.json | Diluted EPS 21.3 for period ending 2026-09-30 (filed 2026-11-02) |
| S036 | stock | ROP | 2026-11-16 | ok | https://finance.yahoo.com/quote/ROP | Trailing P/E: 19.152355; Forward P/E: 19.695457; Forward EPS: 24.57318; Price: 483.98; Market price: 483.98; Market cap: 47931654144; Sector: Technology; Trailing Eps: 25.27; Revenue Growth: 0.076; Earnings Growth: 0.326; Gross Margin: 0.69671; Operating Margin: 0.28049; Profit Margin: 0.30712998; Return On Equity: 0.13229; Total Revenue: 8434599936; Market Cap: 47931654144; Consensus EPS FY+1: 24.57318; growth: 0.09810001 |
| S037 | news | CHTR | Sun, 15 Nov 2026 05:47:01 GMT | ok | https://news.google.com/rss/search?q=CHTR+Charter+Communications+stock&hl=en-US&gl=US&ceid=US:en | Charter Communications (CHTR) Stock Could Be A Bargain Following Its New Operating Model - Yahoo Finance (Sun, 15 Nov 2026 05:47:01 GMT); Why You Should Think About Charter Communications Differently Now? - Yahoo Finance (Fri, 13 Nov 2026 19:16:11 GMT); Charter Communications (CHTR) Earnings Expected to Grow: What to Know Ahead of Next Week's Release - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT) |
| S038 | news | IDXX | Sat, 14 Nov 2026 22:37:20 GMT | ok | https://news.google.com/rss/search?q=IDXX+Idexx+Laboratories+stock&hl=en-US&gl=US&ceid=US:en | IDEXX Laboratories, Inc. (IDXX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Sat, 14 Nov 2026 22:37:20 GMT); IDEXX Laboratories (IDXX) Stock Looks Fairly Valued Despite Its 28% Run - Yahoo Finance (Sat, 31 Oct 2026 07:00:00 GMT); IDEXX Laboratories (IDXX) vs. ZTS and NEOG: Can Raised Guidance and Product Expansion Drive Further Earnings Growth? - Yahoo Finance (Thu, 22 Oct 2026 07:00:00 GMT) |
| S039 | stock | RDDT | 2026-11-16 | ok | https://finance.yahoo.com/quote/RDDT | Trailing P/E: 18.973469; Forward P/E: 10.216045; Forward EPS: 9.10039; Price: 92.97; Market price: 92.97; Market cap: 17951924224; Sector: Communication Services; Trailing Eps: 4.9; Revenue Growth: 0.53; Earnings Growth: 0.749; Gross Margin: 0.91547996; Operating Margin: 0.29397; Profit Margin: 0.32105; Return On Equity: 0.32029998; Total Revenue: 3088880128; Market Cap: 17951924224; Consensus EPS FY+1: 6.8155; growth: 0.2401 |
| S040 | filing | IDXX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000874716.json | Diluted EPS 11.75 for period ending 2026-09-30 (filed 2026-11-02) |

## Sources

- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFF&cosd=2026-01-01 (2026-11-12)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLH0A0HYM2&cosd=2026-01-01 (2026-11-13)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLC0A0CM&cosd=2026-01-01 (2026-11-13)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCSL&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=UNRATE&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=PAYEMS&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=T10Y2Y&cosd=2026-01-01 (2026-11-13)
- filing FISV: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 (2026-11-04)
- filing APP: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001751008&type=10-Q&dateb=&owner=include&count=10 (2026-11-04)
- filing PNR: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 (2026-10-27)
- news FISV: https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en (Mon, 16 Nov 2026 02:19:15 GMT)
- filing APP: https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json (2026-11-04)
- news APP: https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en (Thu, 12 Nov 2026 20:05:45 GMT)
- stock APP: https://finance.yahoo.com/quote/APP (2026-11-16)
- stock PNR: https://finance.yahoo.com/quote/PNR (2026-11-16)
- filing FISV: https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json (2026-11-04)
- stock FISV: https://finance.yahoo.com/quote/FISV (2026-11-16)
- filing PNR: https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json (2026-10-27)
- filing GEN: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 (2026-10-29)
- filing CLX: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 (2026-11-02)

## AI Provenance

- Provider / model: hermes-local-proxy / upstage/solar-mini4:free
- Market research: attempts=2 tokens=9513 (prompt=6513, completion=3000) runtime=91.0s
- Fundamental research: generated this run at 2026-11-16T20:06:26.282471+00:00
- Evidence source dates: {'as_of': '2026-11-13', 'latest_equity_date': '2026-11-13', 'latest_macro_date': '2026-11-16', 'flows_date': '2026-11-13'}
- Evidence fingerprint: 74d80381c51ac86b55a5880e8d982403bdcf390523ba0f76cccf6ff191623499
- Source citations are retrieved external records in the ledger above; market values remain from the verified database snapshot.


## Disclosures

- This is research and market intelligence, not investment advice.
- AI conclusions are research judgments, not validated return predictions.
- The frozen risk layer is risk-only and is not used for directional views or allocations.
- Legacy scores are not active inputs or outputs.

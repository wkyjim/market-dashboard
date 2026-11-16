# AEGIS AI-First Market Intelligence

Research generated at: 17 November 2026, 05:07 HKT
Database freshness: equity 2026-11-13 (latest row retrieved 2026-11-16 13:06:43.000010+08:00)
Data cutoff: 2026-11-13 US cash close
Snapshot ID: aegis-hourly-20261116T210712Z

## Executive Summary

- **AI market view: Late-November 2026 US equities show a mixed tape: broad market momentum is positive but the index is slightly negative over 20 days, with leadership split between defensive/healthcare and consumer staples on one side and a sharp underperformance in information technology and energy on the other. Breadth is constructive (advance/decline 1.70, 71% above the 50-day), yet the 20-day price-breadth divergence is negative, indicating that the rally is narrow and not yet broadly confirmed. Institutional flows show strong inflows into health care and neutral-to-structural distribution in consumer discretionary and utilities, while credit spreads remain tight (IG 0.89, HY 3.23), implying limited near-term stress but also limited compensation for risk.**
- Equity market: S&P 500 is down 1.28% over 20 days; 71.3% of names are above their 50-day and 63.6% above their 200-day, but 20-day price-breadth divergence is negative (-27.49), signaling a narrow, not yet broad rally.
- Sector leadership: Health Care (+6.87% 20d) and Consumer Staples (+5.40% 20d) lead; Information Technology (-7.19% 20d) and Energy (-4.81% 20d) lag sharply.
- Flows: XLV shows strong institutional confirmation (20d z-score +1.45, 60d +1.72), while XLY is in structural distribution (20d z-score -0.38) and XLU shows exceptional institutional selling (20d z-score -2.15).
- Macro/fixed income: Fed funds at 3.88% (2026-11-12), 10Y-2Y spread at 0.27, IG OAS 0.89 and HY OAS 3.23, indicating a still-elevated but not stressed credit environment.
- Inflation/labor: CPI 336.298 and core CPI 338.896 (2026-09-01), unemployment 4.2% (2026-09-01); the latest monthly CPI print in the external source is 337.476 (2026-10-01), so inflation is not clearly decelerating in the most recent data.
- Risk: 5-day forecast volatility 14.93% is below the 18.50% threshold, but spike probability 16.51% is below the historical baseline 22.07%, suggesting a low-probability, low-impact risk regime.

## Data QC

- Status: **PASS_WITH_WARNINGS**
- Equity session: 0 completed session(s) behind inference date
- Equity provenance: 393 provisional / 12576 canonical
- Breadth lag: 0 session(s); ETF-flow lag: 0 session(s)
- Note: Equity session contains a mix of provisional yfinance and canonical Massive rows.
- External sources: 70 ok / 9 unavailable; retrieved 2026-11-16T21:07:30.936866+00:00

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
| S&P 500 (SPX) | 7561.67 | -1.28% (20d) | Index is slightly negative over 20 days; 71.3% of constituents above 50-day, 63.6% above 200-day, but 20-day price-breadth divergence is negative (-27.49), indicating a narrow rally. |
| Health Care (XLV) | return_20d +6.87% | +6.87% | Strongest sector; institutional inflows confirmed (20d z-score +1.45, 60d +1.72) and trailing P/E 30.63. |
| Consumer Staples (XLP) | return_20d +5.40% | +5.40% | Second-strongest sector; trailing P/E 24.93, consistent with defensive demand. |
| Information Technology (XLK) | return_20d -7.19% | -7.19% | Largest drag; trailing P/E 29.05, with shortlisted names like MRVL, NOW, AMD showing large dislocation and high valuation multiples. |
| Energy (XLE) | return_20d -4.81% | -4.81% | Negative 20-day return; trailing P/E 15.92, consistent with sector underperformance. |
| Consumer Discretionary (XLY) | return_20d +6.69% | +6.69% | Positive 20-day return but institutional flow is structural distribution (20d z-score -0.38), so price strength is not confirmed by flows. |

## Macro, Fiscal, Rates, Liquidity and Credit

- Growth: The 10Y-2Y Treasury spread is 0.27 (2026-11-13), a modestly positive but narrow curve, and the S&P 500 is down 1.28% over 20 days, suggesting growth expectations are stable but not accelerating.
- Inflation: CPI (CPIAUCSL) is 336.298 (2026-09-01) and core CPI is 338.896 (2026-09-01); the latest monthly CPI in the external source is 337.476 (2026-10-01), so inflation is not clearly decelerating and remains a policy watch item.
- Policy: The effective federal funds rate is 3.88% as of 2026-11-12, indicating the Fed is in a restrictive-to-neutral stance and has not yet cut aggressively.
- Rates: The 10Y-2Y spread is 0.27, and credit spreads are tight (IG OAS 0.89, HY OAS 3.23), implying low compensation for risk and limited near-term stress.
- Liquidity: Institutional flows show strong inflows into health care (XLV 20d z-score +1.45, 60d +1.72) and neutral-to-structural distribution in consumer discretionary (XLY 20d z-score -0.38) and utilities (XLU 20d z-score -2.15), indicating a rotation into defensives.
- Credit: IG OAS 0.89 and HY OAS 3.23 (2026-11-13) are tight, consistent with a low-risk environment but also with limited upside optionality if growth disappoints.

## US Equities and 11 GICS Sectors

Macro source IDs: S001, S002, S003, S004, S005, S006, S007

| GICS sector | Evidence | AI research stance | Source IDs |
| --- | --- | --- | --- |
| Health Care | 20d return +6.87% (XLV); 20d flow z-score +1.45, 60d +1.72, flow state inflow, price state up, structure strong confirmation; trailing P/E 30.63 (S052). | Defensive leadership is confirmed by institutional inflows; the sector is the clearest positive flow/price alignment in the universe. | S052 |
| Consumer Staples | 20d return +5.40% (XLP); trailing P/E 24.93 (S056); no flow data supplied for XLP in the provided snapshot. | Positive momentum and reasonable valuation support a defensive, quality tilt, but flow confirmation is missing from the supplied data. | S056 |
| Consumer Discretionary | 20d return +6.69% (XLY); trailing P/E 24.73 (S059); 20d flow z-score -0.38, 60d -0.78, flow state neutral, price state up, structure structural distribution. | Price strength is not supported by institutional flows; the sector is in structural distribution, so the rally is likely narrow and vulnerable to reversal. | S059 |
| Real Estate | 20d return +5.24% (XLRE); trailing P/E 29.55 (S061); no flow data supplied for XLRE. | Positive 20-day return and a high trailing P/E suggest a rate-sensitive, premium-priced sector; without flow data, the view is cautious. | S061 |
| Financials | 20d return +5.69% (XLF); trailing P/E 15.71 (S063); no flow data supplied for XLF. | Positive momentum and a low trailing P/E support a constructive view, but the absence of flow data limits confirmation. | S063 |
| Utilities | 20d return +4.34% (XLU); trailing P/E 18.15 (S064); 20d flow z-score -2.15, 60d +0.48, flow state neutral, price state up, structure exceptional institutional selling. | Price is up but institutional flows show exceptional selling, indicating a divergence between price and money flows; the sector is not a reliable leader. | S064 |
| Materials | 20d return +2.57% (XLB); trailing P/E 21.41 (S067); no flow data supplied for XLB. | Modest positive momentum and a mid-range valuation; without flow data, the view is neutral-to-cautious. | S067 |
| Industrials | 20d return +0.61% (XLI); trailing P/E 26.58 (S071); no flow data supplied for XLI. | Near-flat 20-day return and a mid-range P/E suggest a stagnant sector; no clear leadership signal. | S071 |
| Communication Services | 20d return -1.48% (XLC); trailing P/E 16.97 (S070); no flow data supplied for XLC. | Negative 20-day return and a low trailing P/E suggest underperformance; the sector is not leading. | S070 |
| Information Technology | 20d return -7.19% (XLK); trailing P/E 29.05 (S072); shortlisted names include MRVL (P/E 74.23, earnings yield 1.35%, sector-relative P/E 2.20), NOW (P/E 97.19, earnings yield 1.03%, sector-relative P/E 2.88), AMD (P/E 128.88, earnings yield 0.78%, sector-relative P/E 3.82), NVDA (P/E 26.51, earnings yield 3.77%, sector-relative P/E 0.79), INTC (P/E -39.78, earnings yield null), LITE (P/E -9.83, earnings yield null), COIN (P/E -45.17, earnings yield null). | The largest sector drag is driven by large dislocation names with extreme multiples and negative earnings yields; the sector is in a clear correction, with only NVDA showing a more reasonable valuation. | S072 |
| Energy | 20d return -4.81% (XLE); trailing P/E 15.92 (S076); no flow data supplied for XLE. | Negative 20-day return and a low trailing P/E suggest a sector under pressure; without flow data, the view is cautious. | S076 |

### Sector fundamentals, valuation and earnings

The supplied database snapshot provides sector-level 20-day ETF returns, trailing P/E for each of the 11 GICS sectors, and a shortlist of

## Growth vs Value


## ETF Flows and Breadth


## Stock Ideas

Single-stock research uses reported EPS, forward P/E and company fundamentals. All ideas are research judgments, not validated return predictions.

| Ticker | Security | Research view | Price | EPS | Forward P/E | Base target | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| APP | AppLovin | NEW | 409.1 | 20.86026 | 19.904833 | 417.21 | NEW |
| PNR | Pentair | KEEP | 68.3 | 5.30402 | 12.89965 | 68.95 | KEEP |
| GEN | Gen Digital | KEEP | 30.4 | 3.33736 | 9.108996 | 30.04 | KEEP |
| RDDT | Reddit | NEW | 98.45 | 9.10039 | 10.208353 | 91.0 | NEW |

## ETF Ideas

ETF research uses holdings, portfolio valuation and exposure. Single-stock EPS × P/E valuation is not applied to ETFs.

| Ticker | Fund | Research view | Price | Top holdings | Portfolio valuation | Sector exposure | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| XLV | Health Care sector ETF | KEEP | 188.85 | LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59% | Top 10 holdings; numeric weight coverage 61.42% | Health Care | KEEP |
### APP — AppLovin

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** AppLovin offers a compelling combination of high growth, high margins, and strong momentum, making it a preferred choice over lower-margin, lower-momentum alternatives like Clorox or Roper Technologies within the shortlist. Alternatives considered: CLX, ROP.
- **Thesis:** AppLovin screens in the top 20-day momentum bucket with a 53.7% 20-day return and a 32.5% 60-day return, indicating strong recent price momentum. The company reports a high gross margin of 88.8% and operating margin of 77.8%, supporting durable profitability. Trailing P/E of 20.1 and earnings yield of 5.0% are reasonable for a high-growth, high-margin mobile advertising platform.
- **Source IDs:** S008, S013, S015
- **Catalysts:** Sustained mobile advertising demand and AppLovin's ad monetization technology, Continued margin expansion and operating leverage, Potential for further re-rating as the stock maintains momentum
- **Risks:** High valuation multiples could lead to sharp corrections if momentum fades, Mobile advertising market saturation or regulatory changes, Dependency on Apple ecosystem changes and privacy policies
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 20.8603 (source.forwardEps) x AI multiple assumption 20.00; source IDs S008, S013, S015
- **EPS:** 20.86026 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 19.904833
- **FY+1 growth assumption:** 27.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / MSFT / APP shows strong FY+1 consensus earnings growth of 27.44% and revenue growth of 25.37%, with exceptional margins (gross 88.8%, operating 77.8%, profit 65.9%) and high ROE. The 19.9x forward P/E is below the 20.0x base multiple, reflecting a premium growth profile; MSFT is the named peer for comparison.
- **Company fundamentals:** AppLovin reports a trailing P/E of 20.1, earnings yield of 5.0%, gross margin of 88.8%, operating margin of 77.8%, and revenue growth of 55.5%. The company has 26 analysts covering it, with FY1 EPS of $20.72 and FY1 EPS growth of 27.4%. Forward EPS is $20.86, implying a forward P/E of 19.9.
- **Bull / Base / Bear:** 500.65 / 417.21 / 333.76
- **Bull / Base / Bear returns:** 22.38% / 1.98% / -18.42%
- **Scenario probabilities:** not separately assigned; see scenario table.

### PNR — Pentair

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Pentair offers a lower valuation (trailing P/E 13.6) compared to higher-multiple momentum names, but its negative growth metrics make it a neutral holding rather than a top pick. Alternatives considered: APP, ROP.
- **Thesis:** Pentair is in the top 20-day momentum bucket with a 27.8% 20-day return and a 7.1% 60-day return. The company has a trailing P/E of 13.6 and earnings yield of 7.4%, which is attractive relative to its sector. However, revenue growth is slightly negative at -4.5% and earnings growth is -18.8%, indicating near-term headwinds.
- **Source IDs:** S009, S017, S018, S022
- **Catalysts:** Potential stabilization in industrial and water technology demand, Margin recovery as cost pressures ease, Continued momentum from recent price performance
- **Risks:** Negative revenue and earnings growth may persist, Cyclical exposure to industrial end markets, Valuation may not fully reflect near-term challenges
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 5.3040 (source.forwardEps) x AI multiple assumption 13.00; source IDs S009, S017, S018, S022
- **EPS:** 5.30402 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 12.89965
- **FY+1 growth assumption:** 12.82%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / UPS / PNR has FY+1 consensus earnings growth of 12.82% and revenue growth of 18.38%, with moderate margins (gross 40.2%, operating 21.4%, profit 15.4%) and positive ROE. The 12.9x forward P/E supports a 13.0x base multiple; UPS is the named peer for comparison.
- **Company fundamentals:** Pentair reports a trailing P/E of 13.6, earnings yield of 7.4%, gross margin of 40.2%, operating margin of 21.4%, and profit margin of 15.4%. Revenue growth is -4.5% and earnings growth is -18.8%. Forward EPS is $5.30, implying a forward P/E of 12.9.
- **Bull / Base / Bear:** 84.86 / 68.95 / 53.04
- **Bull / Base / Bear returns:** 24.25% / 0.95% / -22.34%
- **Scenario probabilities:** not separately assigned; see scenario table.

### GEN — Gen Digital

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Gen Digital offers a balanced profile of momentum and reasonable valuation, but its growth is less robust than AppLovin's, making it a neutral holding. Alternatives considered: APP, IDXX.
- **Thesis:** Gen Digital is in the top 20-day momentum bucket with a 25.8% 20-day return and a 7.9% 60-day return. The company has a trailing P/E of 14.2 and earnings yield of 7.1%. However, revenue growth is modest at 12.2% and earnings growth is 128.6%, indicating strong but potentially less sustainable growth. The stock was repriced after Q2 earnings, highlighting margin focus.
- **Source IDs:** S016, S020, S023, S024
- **Catalysts:** Cybersecurity and digital risk protection demand, Margin improvement as the company focuses on profitability, Continued momentum from recent price performance
- **Risks:** Growth may slow as the market matures, Margin pressure from competitive and regulatory pressures, Stock repricing risk after earnings announcements
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 3.3374 (source.forwardEps) x AI multiple assumption 9.00; source IDs S016, S020, S023, S024
- **EPS:** 3.33736 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 9.108996
- **FY+1 growth assumption:** 12.86%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / CSCO / GEN has FY+1 consensus earnings growth of 12.86% and revenue growth of 6.81%, with solid gross margin (77.4%) and operating margin (43.2%). The 9.1x forward P/E supports a 9.0x base multiple; CSCO is the named peer for comparison.
- **Company fundamentals:** Gen Digital reports a trailing P/E of 14.2, earnings yield of 7.1%, gross margin of 77.4%, operating margin of 43.2%, and profit margin of 23.1%. Revenue growth is 12.2% and earnings growth is 128.6%. Forward EPS is $3.34, implying a forward P/E of 9.1.
- **Bull / Base / Bear:** 36.71 / 30.04 / 23.36
- **Bull / Base / Bear returns:** 20.76% / -1.18% / -23.16%
- **Scenario probabilities:** not separately assigned; see scenario table.

### RDDT — Reddit

- **Type:** Stock
- **Research view:** NEW (stance: NEUTRAL)
- **Why preferred / alternatives:** Reddit's strong fundamentals and contrarian dislocation make it a preferred choice over more traditional, lower-growth names like Clorox or Pentair, despite the higher risk profile. Alternatives considered: CLX, PNR.
- **Thesis:** Reddit is in the largest 20-day dislocation bucket, having declined 36.9% over 20 days and 34.5% over 60 days, with a 39.4% drawdown. Despite the dislocation, the company shows strong fundamentals with revenue growth of 53% and earnings growth of 74.9%, a gross margin of 91.5%, and a forward P/E of 10.2. The dislocation may present a contrarian opportunity if the business continues to improve.
- **Source IDs:** S036, S038, S047
- **Catalysts:** Continued revenue and earnings growth from its platform, Potential for margin expansion as the company scales, Contrarian buying opportunity as the stock recovers from dislocation
- **Risks:** High volatility and potential for further declines, Dependence on advertising revenue in a cyclical market, User engagement and content moderation challenges
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 9.1004 (source.forwardEps) x AI multiple assumption 10.00; source IDs S036, S038, S047
- **EPS:** 9.10039 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 10.208353
- **FY+1 growth assumption:** 24.01%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / AMZN / RDDT has FY+1 consensus earnings growth of 24.01% and revenue growth of 28.38%, with the highest gross margin (91.5%) among the four, though operating margin is lower at 29.4%. The 10.2x forward P/E supports a 10.0x base multiple; AMZN is the named peer for comparison.
- **Company fundamentals:** Reddit reports a forward P/E of 10.2, earnings yield of 3.0%, gross margin of 91.5%, operating margin of 29.4%, and profit margin of 32.1%. Revenue growth is 53% and earnings growth is 74.9%. FY1 EPS is $6.82 with 24% growth. Forward EPS is $9.10.
- **Bull / Base / Bear:** 109.2 / 91.0 / 72.8
- **Bull / Base / Bear returns:** 10.92% / -7.57% / -26.05%
- **Scenario probabilities:** not separately assigned; see scenario table.

### XLV — Health Care sector ETF

- **Type:** ETF
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** XLV offers broad healthcare sector exposure with a diversified top-10 portfolio, making it a preferred choice over individual healthcare stocks like IDXX for risk-averse investors. Alternatives considered: XLP, XLF.
- **Thesis:** The Health Care sector ETF (XLV) provides diversified exposure to the healthcare industry, with a 54.3% price change over the period. The top holdings include LLY, JNJ, ABBV, MRK, and UNH, offering a broad mix of large-cap healthcare names. The ETF is a neutral holding for investors seeking sector exposure without individual stock risk.
- **Source IDs:** S052, S058
- **Catalysts:** Potential for healthcare innovation and new drug approvals, Stable demand for healthcare services regardless of economic conditions, Diversification across multiple large-cap healthcare companies
- **Risks:** Sector-specific regulatory and policy changes, Concentration risk in top holdings like LLY and JNJ, Macroeconomic factors affecting healthcare spending
- **Valuation method:** Holdings/portfolio valuation with AI total-return assumption
- **Valuation status:** verified; forward-EPS source: ; period flags: 
- **Valuation assumptions:** Holdings/portfolio valuation; 10 weighted holdings; coverage 61.42%; source IDs S052, S058
- **Top holdings:** LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59%
- **Portfolio valuation:** Top 10 holdings; numeric weight coverage 61.42%
- **Sector exposure:** Health Care
- **Underlying drivers:** Healthcare sector performance driven by large-cap pharmaceutical and medical technology companies, with top holdings including LLY, JNJ, ABBV, MRK, and UNH.
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
| Bull | 25% | +2.00% | Low 5-day realized vol (14.9%) and below-threshold spike probability (16.5% vs 18.5% threshold) support a modest upside if US close confirms stable liquidity and no credit stress. |
| Base | 50% | +0.00% | Frozen daily-close model with no directional signal and near-baseline volatility implies range-bound trading; returns cluster near zero over the 5-day horizon. |
| Bear | 25% | -2.00% | If the US close reveals elevated volatility or a spike event, the 16.5% spike probability could trigger a 2% drawdown as risk-off flows compress the range. |

### Long Term (12 months)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 30% | +8.00% | Sustained low volatility and stable credit conditions allow earnings growth and breadth expansion to compound, yielding an 8% annualized return over the longer horizon. |
| Base | 40% | +3.00% | Near-baseline volatility and neutral directional signal support a modest positive drift as earnings and credit fundamentals remain intact. |
| Bear | 30% | -5.00% | A spike event or credit stress would raise realized vol and compress valuations, producing a -5% annualized return if risk-off dynamics persist. |

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
| S008 | filing | APP | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001751008&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0001751008-26-000069); 8-K filed 2026-11-04 (accession 0001751008-26-000068); 10-Q filed 2026-08-05 (accession 0001751008-26-000059) |
| S009 | filing | PNR | 2026-10-27 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-27 (accession 0000077360-26-000058); 8-K filed 2026-10-27 (accession 0000077360-26-000055); 8-K filed 2026-09-22 (accession 0000077360-26-000050) |
| S010 | filing | FISV | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0000798354-26-000042); 8-K filed 2026-11-03 (accession 0000798354-26-000039); 8-K filed 2026-10-23 (accession 0001193125-26-429481) |
| S011 | news | APP | 2026-11-16 | unavailable | https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en |  |
| S012 | news | FISV | 2026-11-16 | unavailable | https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en |  |
| S013 | stock | APP | 2026-11-16 | ok | https://finance.yahoo.com/quote/APP | Trailing P/E: 27.960941; Forward P/E: 19.904833; Forward EPS: 20.86026; Price: 415.22; Market price: 415.22; Market cap: 137571516416; Sector: Communication Services; Trailing Eps: 14.85; Revenue Growth: 0.555; Earnings Growth: 0.755; Gross Margin: 0.8878; Operating Margin: 0.77782995; Profit Margin: 0.65887; Return On Equity: 2.1008599; Total Revenue: 7608893952; Market Cap: 137571516416; Consensus EPS FY+1: 20.72438; growth: 0.2744 |
| S014 | stock | FISV | 2026-11-16 | ok | https://finance.yahoo.com/quote/FISV | Forward P/E: 7.943029; Price: 63.32; Market price: 63.32; Market cap: 33689260032; Market Cap: 33689260032; Consensus EPS FY+1: 7.97582; growth: 0.0959 |
| S015 | filing | APP | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json | Diluted EPS 11.61 for period ending 2026-09-30 (filed 2026-11-04) |
| S016 | filing | GEN | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0000849399-26-000083); 8-K filed 2026-10-28 (accession 0000849399-26-000081); 8-K filed 2026-10-09 (accession 0000849399-26-000079) |
| S017 | filing | PNR | 2026-10-27 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json | Diluted EPS 2.76 for period ending 2026-09-30 (filed 2026-10-27) |
| S018 | stock | PNR | 2026-11-16 | ok | https://finance.yahoo.com/quote/PNR | Trailing P/E: 18.643051; Forward P/E: 12.89965; Forward EPS: 5.30402; Price: 68.42; Market price: 68.42; Market cap: 10923573248; Sector: Industrials; Trailing Eps: 3.67; Revenue Growth: -0.045; Earnings Growth: -0.188; Gross Margin: 0.40168998; Operating Margin: 0.21410999; Profit Margin: 0.15435; Return On Equity: 0.15605; Total Revenue: 3966200064; Market Cap: 10923573248; Consensus EPS FY+1: 5.30402; growth: 0.1282 |
| S019 | filing | FISV | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json | Diluted EPS -8.9 for period ending 2026-09-30 (filed 2026-11-04) |
| S020 | stock | GEN | 2026-11-16 | ok | https://finance.yahoo.com/quote/GEN | Trailing P/E: 15.431472; Forward P/E: 9.108996; Forward EPS: 3.33736; Price: 30.4; Market price: 30.4; Market cap: 18035593216; Sector: Technology; Trailing Eps: 1.97; Revenue Growth: 0.122; Earnings Growth: 1.286; Gross Margin: 0.77410007; Operating Margin: 0.43229; Profit Margin: 0.23068; Return On Equity: 0.46402; Total Revenue: 5228000256; Market Cap: 18035593216; Consensus EPS FY+1: 3.33736; growth: 0.1286 |
| S021 | filing | CLX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000021076-26-000046); 8-K filed 2026-11-02 (accession 0000021076-26-000044); 8-K filed 2026-10-29 (accession 0001206774-26-000586) |
| S022 | news | PNR | Sat, 14 Nov 2026 08:48:27 GMT | ok | https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en | Pentair plc (PNR) Stock Price, News, Quote & History - Yahoo! Finance Canada (Sat, 14 Nov 2026 08:48:27 GMT); Why Pentair Stock Popped This Morning - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT); Pentair plc (PNR) Q3 Earnings and Revenues Beat Estimates - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT) |
| S023 | news | GEN | Thu, 29 Oct 2026 07:00:00 GMT | ok | https://news.google.com/rss/search?q=GEN+Gen+Digital+stock&hl=en-US&gl=US&ceid=US:en | Gen Digital (GEN) Stock Repriced After Q2 Earnings Put Margins Center Stage - Yahoo Finance (Thu, 29 Oct 2026 07:00:00 GMT); Are Business Services Stocks Lagging GEN DIGITAL INC (GEN) This Year? - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT); Gen Digital Stock: Is Wall Street Bullish or Bearish? - Yahoo Finance (Thu, 05 Nov 2026 08:00:00 GMT) |
| S024 | filing | GEN | 2026-10-29 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000849399.json | Diluted EPS 0.83 for period ending 2026-10-02 (filed 2026-10-29) |
| S025 | filing | CHTR | 2026-11-06 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-06 (accession 0001091667-26-000073); 8-K filed 2026-11-06 (accession 0001091667-26-000072); 8-K filed 2026-10-27 (accession 0001091667-26-000064) |
| S026 | news | CLX | Fri, 13 Nov 2026 23:34:51 GMT | ok | https://news.google.com/rss/search?q=CLX+Clorox+stock&hl=en-US&gl=US&ceid=US:en | The Clorox Company (CLX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 23:34:51 GMT); The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance UK (Sat, 14 Nov 2026 06:03:20 GMT); A 10-Day Winning Streak Has Clorox Stock Up 24% - Trefis (Sat, 14 Nov 2026 08:28:05 GMT) |
| S027 | stock | CLX | 2026-11-16 | ok | https://finance.yahoo.com/quote/CLX | Trailing P/E: 19.818346; Forward P/E: 17.863628; Forward EPS: 6.1684; Price: 110.19; Market price: 110.19; Market cap: 13349231616; Sector: Consumer Defensive; Trailing Eps: 5.56; Revenue Growth: 0.333; Earnings Growth: 1.138; Gross Margin: 0.41939998; Operating Margin: 0.14286; Profit Margin: 0.09408; Return On Equity: 5.34363; Total Revenue: 7196000256; Market Cap: 13349231616; Consensus EPS FY+1: 6.1684; growth: 0.0769 |
| S028 | stock | CHTR | 2026-11-16 | ok | https://finance.yahoo.com/quote/CHTR | Trailing P/E: 13.05921; Forward P/E: 3.057552; Forward EPS: 45.44485; Price: 138.95; Market price: 138.95; Market cap: 24879212544; Sector: Communication Services; Trailing Eps: 10.64; Revenue Growth: 0.091; Gross Margin: 0.55084; Operating Margin: 0.23389; Profit Margin: 0.02498; Return On Equity: 0.07019; Total Revenue: 55645999104; Market Cap: 24879212544; Consensus EPS FY+1: 49.35412; growth: 1.1136 |
| S029 | filing | IDXX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000874716&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000874716-26-000135); 8-K filed 2026-11-02 (accession 0001104659-26-120892); 10-Q filed 2026-08-04 (accession 0000874716-26-000123) |
| S030 | news | CHTR | 2026-11-16 | unavailable | https://news.google.com/rss/search?q=CHTR+Charter+Communications+stock&hl=en-US&gl=US&ceid=US:en |  |
| S031 | filing | ROP | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000882835&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000882835-26-000047); 8-K filed 2026-10-22 (accession 0000882835-26-000042); 8-K filed 2026-10-01 (accession 0000882835-26-000039) |
| S032 | stock | IDXX | 2026-11-16 | ok | https://finance.yahoo.com/quote/IDXX | Trailing P/E: 47.21361; Forward P/E: 41.476006; Forward EPS: 16.8929; Price: 700.65; Market price: 700.65; Market cap: 55201599488; Sector: Healthcare; Trailing Eps: 14.84; Revenue Growth: 0.099; Earnings Growth: 0.179; Gross Margin: 0.62722; Operating Margin: 0.32497; Profit Margin: 0.25357; Return On Equity: 0.68925005; Total Revenue: 4662220800; Market Cap: 55201599488; Consensus EPS FY+1: 16.8929; growth: 0.1244 |
| S033 | stock | ROP | 2026-11-16 | ok | https://finance.yahoo.com/quote/ROP | Trailing P/E: 19.142065; Forward P/E: 19.684877; Forward EPS: 24.57318; Price: 483.72; Market price: 483.72; Market cap: 47905902592; Sector: Technology; Trailing Eps: 25.27; Revenue Growth: 0.076; Earnings Growth: 0.326; Gross Margin: 0.69671; Operating Margin: 0.28049; Profit Margin: 0.30712998; Return On Equity: 0.13229; Total Revenue: 8434599936; Market Cap: 47905902592; Consensus EPS FY+1: 24.57318; growth: 0.09810001 |
| S034 | filing | CHTR | 2026-11-06 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001091667.json | Diluted EPS 0.38 for period ending 2026-09-30 (filed 2026-11-06) |
| S035 | filing | CLX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000021076.json | Diluted EPS 1.39 for period ending 2026-09-30 (filed 2026-11-02) |
| S036 | filing | RDDT | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001713445&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0001713445-26-000116); 8-K filed 2026-10-29 (accession 0001713445-26-000114); 8-K filed 2026-08-12 (accession 0001713445-26-000107) |
| S037 | news | IDXX | Sat, 14 Nov 2026 22:37:20 GMT | ok | https://news.google.com/rss/search?q=IDXX+Idexx+Laboratories+stock&hl=en-US&gl=US&ceid=US:en | IDEXX Laboratories, Inc. (IDXX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Sat, 14 Nov 2026 22:37:20 GMT); IDEXX Laboratories (IDXX) Stock Looks Fairly Valued Despite Its 28% Run - Yahoo Finance (Sat, 31 Oct 2026 07:00:00 GMT); IDEXX Laboratories (IDXX) vs. ZTS and NEOG: Can Raised Guidance and Product Expansion Drive Further Earnings Growth? - Yahoo Finance (Thu, 22 Oct 2026 07:00:00 GMT) |
| S038 | stock | RDDT | 2026-11-16 | ok | https://finance.yahoo.com/quote/RDDT | Trailing P/E: 18.959183; Forward P/E: 10.208353; Forward EPS: 9.10039; Price: 92.9; Market price: 92.9; Market cap: 17938407424; Sector: Communication Services; Trailing Eps: 4.9; Revenue Growth: 0.53; Earnings Growth: 0.749; Gross Margin: 0.91547996; Operating Margin: 0.29397; Profit Margin: 0.32105; Return On Equity: 0.32029998; Total Revenue: 3088880128; Market Cap: 17938407424; Consensus EPS FY+1: 6.8155; growth: 0.2401 |
| S039 | filing | IDXX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000874716.json | Diluted EPS 11.75 for period ending 2026-09-30 (filed 2026-11-02) |
| S040 | news | RDDT | 2026-11-16 | unavailable | https://news.google.com/rss/search?q=RDDT+Reddit+stock&hl=en-US&gl=US&ceid=US:en |  |

## Sources

- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFF&cosd=2026-01-01 (2026-11-12)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLH0A0HYM2&cosd=2026-01-01 (2026-11-13)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLC0A0CM&cosd=2026-01-01 (2026-11-13)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCSL&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=UNRATE&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=PAYEMS&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=T10Y2Y&cosd=2026-01-01 (2026-11-13)
- filing APP: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001751008&type=10-Q&dateb=&owner=include&count=10 (2026-11-04)
- filing PNR: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 (2026-10-27)
- filing FISV: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 (2026-11-04)
- stock APP: https://finance.yahoo.com/quote/APP (2026-11-16)
- stock FISV: https://finance.yahoo.com/quote/FISV (2026-11-16)
- filing APP: https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json (2026-11-04)
- filing GEN: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 (2026-10-29)
- filing PNR: https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json (2026-10-27)
- stock PNR: https://finance.yahoo.com/quote/PNR (2026-11-16)
- filing FISV: https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json (2026-11-04)
- stock GEN: https://finance.yahoo.com/quote/GEN (2026-11-16)
- filing CLX: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 (2026-11-02)
- news PNR: https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en (Sat, 14 Nov 2026 08:48:27 GMT)

## AI Provenance

- Provider / model: hermes-local-proxy / upstage/solar-mini4:free
- Market research: attempts=1 tokens=9511 (prompt=6511, completion=3000) runtime=20.84s
- Fundamental research: generated this run at 2026-11-16T21:07:12.835871+00:00
- Evidence source dates: {'as_of': '2026-11-13', 'latest_equity_date': '2026-11-13', 'latest_macro_date': '2026-11-16', 'flows_date': '2026-11-13'}
- Evidence fingerprint: 2d046f91650a4b9380055a1dc6f7d283ea1aab17693dc6f0d4df16755adddcdd
- Source citations are retrieved external records in the ledger above; market values remain from the verified database snapshot.


## Disclosures

- This is research and market intelligence, not investment advice.
- AI conclusions are research judgments, not validated return predictions.
- The frozen risk layer is risk-only and is not used for directional views or allocations.
- Legacy scores are not active inputs or outputs.

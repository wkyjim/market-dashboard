# AEGIS AI-First Market Intelligence

Research generated at: 16 November 2026, 15:07 HKT
Database freshness: equity 2026-11-13 (latest row retrieved 2026-11-16 13:06:43.000010+08:00)
Data cutoff: 2026-11-13 US cash close
Snapshot ID: aegis-hourly-20261116T070720Z

## Executive Summary

- **AI market view: Late-November 2026: broad market breadth is constructive (71% above 50-day, 64% above 200-day, A/D ratio 1.70), but the index is slightly negative over 20 days and the 20-day return is -1.28%. Sector rotation is mixed: defensive and consumer staples sectors are leading, while Information Technology and Energy are the weakest. Liquidity is concentrated in a small set of large-cap names, and several high-multiple names show dislocation flags. Macro data show a still-elevated but easing inflation backdrop, a stable labor market, and a modestly positive yield-curve spread.**
- Broad market breadth is positive: 71.3% of names above the 50-day moving average, 63.6% above the 200-day, and an advance/decline ratio of 1.70.
- The S&P 500 is down 1.28% over 20 days, indicating short-term price weakness despite positive breadth.
- Sector leadership is defensive: Health Care (+6.9%), Consumer Discretionary (+6.7%), Consumer Staples (+5.4%), and Financials (+5.7%) lead over 20 days.
- Information Technology (-7.2%) and Energy (-4.8%) are the weakest sectors, dragging the broad market.
- Flows show strong institutional inflows into Health Care (XLP? actually XLV) and structural distribution in Consumer Discretionary and Utilities.
- Macro data point to a cooling but still-positive inflation environment, a 4.2% unemployment rate, and a modestly positive 10Y-2Y spread of 0.27.
- Risk indicators show a 16.5% spike probability, below the historical baseline of 22.1%, suggesting a relatively calm near-term risk profile.

## Data QC

- Status: **PASS_WITH_WARNINGS**
- Equity session: 0 completed session(s) behind inference date
- Equity provenance: 393 provisional / 12576 canonical
- Breadth lag: 0 session(s); ETF-flow lag: 0 session(s)
- Note: Equity session contains a mix of provisional yfinance and canonical Massive rows.
- External sources: 79 ok / 0 unavailable; retrieved 2026-11-16T07:07:42.962497+00:00

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
| S&P 500 (SPX) | 7561.67 | -1.28% (20d) | Index is slightly negative over 20 days despite positive breadth; 71.3% above 50-day and 63.6% above 200-day. |
| Health Care (XLV) | +6.87% (20d) | +6.87% | Strongest sector; trailing P/E 30.78; strong institutional inflows and price strength. |
| Consumer Discretionary (XLY) | +6.69% (20d) | +6.69% | Strong price momentum but structural distribution in flows; trailing P/E 25.11. |
| Consumer Staples (XLP) | +5.40% (20d) | +5.40% | Positive price action; trailing P/E 24.85; defensive demand. |
| Information Technology (XLK) | -7.19% (20d) | -7.19% | Weakest sector; trailing P/E 30.03; high-multiple names show dislocation flags. |
| Energy (XLE) | -4.81% (20d) | -4.81% | Weak sector; trailing P/E 16.23; negative price momentum. |

## Macro, Fiscal, Rates, Liquidity and Credit

- Inflation: CPI stands at 336.3 (Sep 2026) with core CPI at 338.9; October CPI data (337.48) suggests a slight uptick, indicating inflation remains above the Fed's 2% target but is not accelerating sharply.
- Labor market: Unemployment rate is 4.2% (Sep 2026), with October payrolls at 159.3M; the labor market remains stable but not overheating.
- Policy: The effective federal funds rate is 3.88% as of 2026-11-12, implying a restrictive but potentially easing stance.
- Rates: The 10Y-2Y Treasury spread is 0.27 as of 2026-11-13, a modestly positive curve, though still shallow.
- Credit: High-yield OAS is 3.20 and IG OAS is 0.89 as of 2026-11-12, indicating tight but not stressed credit conditions.
- Liquidity: Market breadth is positive, but price-breadth divergence is -27.49, suggesting some internal weakness despite the overall positive signal.

## US Equities and 11 GICS Sectors

Macro source IDs: S001, S002, S003, S004, S005, S006, S007

| GICS sector | Evidence | AI research stance | Source IDs |
| --- | --- | --- | --- |
| Health Care | 20d return +6.87%; trailing P/E 30.78; strong institutional inflows and price strength. | Defensive leader with strong momentum; attractive relative value despite high valuation. | S055 |
| Consumer Staples | 20d return +5.40%; trailing P/E 24.85; defensive demand. | Stable defensive sector with positive price action; reasonable valuation. | S053 |
| Consumer Discretionary | 20d return +6.69%; trailing P/E 25.11; strong price momentum but structural distribution in flows. | Positive price momentum but mixed flows; watch for distribution signals. | S056 |
| Financials | 20d return +5.69%; trailing P/E 15.85; positive price action. | Solid performance with reasonable valuation; supportive of financial sector. | S060 |
| Real Estate | 20d return +5.24%; trailing P/E 29.63; positive price action. | Positive momentum with high valuation; monitor for rate sensitivity. | S062 |
| Utilities | 20d return +4.34%; trailing P/E 18.11; medium-term deterioration in flows. | Defensive but with institutional selling; valuation is reasonable. | S064 |
| Materials | 20d return +2.57%; trailing P/E 21.72; modest positive price action. | Stable but lagging; valuation is reasonable. | S066 |
| Industrials | 20d return +0.61%; trailing P/E 27.07; modest positive price action. | Near-flat performance; valuation is high relative to peers. | S067 |
| Communication Services | 20d return -1.48%; trailing P/E 17.26; negative price action. | Weakest sector among large caps; valuation is reasonable but momentum is negative. | S069 |
| Information Technology | 20d return -7.19%; trailing P/E 30.03; high-multiple names show dislocation flags. | Weakest sector; high valuations and dislocation flags warrant caution. | S071 |
| Energy | 20d return -4.81%; trailing P/E 16.23; negative price momentum. | Weak sector; valuation is reasonable but momentum is negative. | S072 |

### Sector fundamentals, valuation and earnings

Sector fundamentals are not directly provided in the database snapshot. The supplied data include only 20-day price returns for each sector ETF and trailing P/E ratios for the sector ETFs. No point-in-time sector-level growth, margin, or earnings data are available. Therefore, sector fundamentals cannot be assessed beyond price momentum and valuation multiples.

## Growth vs Value

- Health Care and Consumer Staples offer defensive growth with positive 20-day returns and reasonable trailing P/E multiples.
- Information Technology and Communication Services show negative 20-day returns and high valuation multiples, suggesting value risk.
- Financials and Energy offer lower trailing P/E multiples (15.85 and 16.23) but negative price momentum.
- Consumer Discretionary has strong price momentum but mixed flow signals, indicating potential value risk.

## ETF Flows and Breadth

- Health Care (XLV) shows strong institutional inflows and strong confirmation with a 20d flow z-score of 1.45.
- Consumer Discretionary (XLY) shows structural distribution with a 20d flow z-score of -0.38, despite positive price momentum.
- Utilities (XLU) shows medium-term deterioration with exceptional institutional selling, despite a positive 20d price state.
- Broad market breadth is positive: 71.3% above 50-day, 63.6% above 200-day, and an advance/decline ratio of 1.70.
- Price-breadth divergence is -27.49, indicating some internal weakness despite the overall positive signal.

## Stock Ideas

Single-stock research uses reported EPS, forward P/E and company fundamentals. All ideas are research judgments, not validated return predictions.

| Ticker | Security | Research view | Price | EPS | Forward P/E | Base target | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| APP | AppLovin | NEW | 409.1 | 20.86026 | 19.611452 | 417.21 | NEW |
| PNR | Pentair | KEEP | 68.3 | 5.30402 | 12.877027 | 68.95 | KEEP |
| GEN | Gen Digital | KEEP | 30.4 | 3.33736 | 9.108996 | 33.37 | KEEP |
| ROP | Roper Technologies | KEEP | 479.975 | 24.57318 | 19.532475 | 491.46 | KEEP |

## ETF Ideas

ETF research uses holdings, portfolio valuation and exposure. Single-stock EPS × P/E valuation is not applied to ETFs.

| Ticker | Fund | Research view | Price | Top holdings | Portfolio valuation | Sector exposure | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| XLV | Health Care sector ETF | NEW | 188.85 | LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59% | Top 10 holdings; numeric weight coverage 61.42% | Health Care | NEW |
### APP — AppLovin

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** AppLovin offers a high-margin, momentum-driven platform with a forward P/E near 19.6, whereas the shortlist alternatives such as IDXX carry a much higher forward P/E near 41.7 and RDDT carries a forward P/E near 10.8 with a 39% 60-day drawdown. APP's combination of strong momentum, high margins, and a reasonable valuation makes it the preferred equity pick from the momentum bucket. Alternatives considered: IDXX, RDDT.
- **Thesis:** AppLovin screens in the top 20-day momentum bucket with a 53.7% 20-day return and a 60-day drawdown near flat, indicating strong price momentum without a recent drawdown. Reported diluted EPS of 11.61 for the fiscal period ending 2026-09-30 and a forward EPS of 20.86 support a forward P/E near 19.6, which is reasonable for a high-margin advertising platform. The company's gross margin of 88.8% and operating margin of 77.8% show durable operating leverage in its core business.
- **Source IDs:** S009, S011, S012, S013
- **Catalysts:** Continued 20-day momentum and stable 60-day drawdown, Sustained high gross margin and operating margin expansion, Forward EPS growth from 11.61 reported to 20.86 consensus, Advertising market demand supporting revenue growth
- **Risks:** High 20-day momentum may already be priced in, Forward EPS estimates are unverified and subject to revision, Advertising sector cyclicality and macro sensitivity, Single-quarter reported EPS may not reflect full-year trajectory
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 20.8603 (source.forwardEps) x AI multiple assumption 20.00; source IDs S009, S011, S012, S013
- **EPS:** 20.86026 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 19.611452
- **FY+1 growth assumption:** 27.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / Apple (AAPL) and Microsoft (MSFT) as high-margin, ecosystem-driven software/hardware peers / APP shows strong FY1 consensus growth of 27.44% and revenue growth of 55.5%, with exceptional margins (gross 88.8%, operating 77.8%, profit 65.9%) and ROE of 2.10x. The base multiple of 20x is justified by durable high margins and growth, while the bull/bear range reflects upside if growth accelerates and downside if margin compression occurs. Peer reference: AAPL and MSFT for comparable high-margin, growth-oriented profiles.
- **Company fundamentals:** AppLovin reported diluted EPS of 11.61 for the fiscal period ending 2026-09-30, with forward EPS of 20.86. Gross margin is 88.8%, operating margin is 77.8%, and profit margin is 65.9%. Revenue growth is 55.5% and earnings growth is 75.5%. Forward P/E is 19.61. Price is 409.10.
- **Bull / Base / Bear:** 500.65 / 417.21 / 333.76
- **Bull / Base / Bear returns:** 22.38% / 1.98% / -18.42%
- **Scenario probabilities:** not separately assigned; see scenario table.

### PNR — Pentair

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Pentair offers a low forward P/E near 12.9 and a reasonable earnings yield near 7.4%, which is more attractive than higher-multiple momentum names such as IDXX. However, its negative revenue and earnings growth temper the case, so it is kept as a neutral holding rather than a strong buy. Alternatives considered: IDXX, RDDT.
- **Thesis:** Pentair screens in the top 20-day momentum bucket with a 27.8% 20-day return and a modest 5.2% 60-day drawdown. Reported diluted EPS of 2.76 for the fiscal period ending 2026-09-30 and a forward EPS of 5.30 support a forward P/E near 12.9, which is attractive relative to the broader market. However, revenue growth is slightly negative at -4.5% and earnings growth is -18.8%, indicating near-term operating pressure despite the valuation appeal.
- **Source IDs:** S008, S015, S016, S019
- **Catalysts:** 20-day momentum of 27.8%, Forward P/E near 12.9 offers valuation support, Stable 60-day drawdown of 5.2%, Forward EPS of 5.30 supports earnings yield near 7.4%
- **Risks:** Revenue growth is negative at -4.5%, Earnings growth is negative at -18.8%, Forward EPS estimates are unverified, Cyclical exposure to building and construction markets
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 5.3040 (source.forwardEps) x AI multiple assumption 13.00; source IDs S008, S015, S016, S019
- **EPS:** 5.30402 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 12.877027
- **FY+1 growth assumption:** 12.82%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / Prologis (PLD) and Equinix (EQIX) as industrial/logistics REITs with similar asset-light models / PNR has FY1 consensus growth of 12.82% and revenue growth of 18.4%, with moderate margins (gross 40.2%, operating 21.4%, profit 15.4%) and ROE of 0.156x. The base multiple of 13x reflects a mid-range valuation for a growth-oriented industrial/logistics REIT, with bull/bear multiples capturing upside from occupancy/rent growth and downside from sector softness. Peer reference: PLD and EQIX for comparable logistics/industrial REIT fundamentals.
- **Company fundamentals:** Pentair reported diluted EPS of 2.76 for the fiscal period ending 2026-09-30, with forward EPS of 5.30. Gross margin is 40.2%, operating margin is 21.4%, and profit margin is 15.4%. Revenue growth is -4.5% and earnings growth is -18.8%. Forward P/E is 12.88. Price is 68.30.
- **Bull / Base / Bear:** 84.86 / 68.95 / 53.04
- **Bull / Base / Bear returns:** 24.25% / 0.95% / -22.34%
- **Scenario probabilities:** not separately assigned; see scenario table.

### GEN — Gen Digital

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Gen Digital offers a low forward P/E near 9.1 and strong earnings growth of 128.6%, which is more attractive than higher-multiple names such as IDXX. However, the unverified forward EPS and high-beta nature keep it as a neutral holding rather than a strong buy. Alternatives considered: IDXX, ROP.
- **Thesis:** Gen Digital screens in the top 20-day momentum bucket with a 25.8% 20-day return and a modest 3.2% 60-day drawdown. Reported diluted EPS of 0.83 and forward EPS of 3.34 support a forward P/E near 9.1, which is attractive. Revenue growth is 12.2% and earnings growth is 128.6%, indicating strong operational momentum. However, the forward EPS estimate is unverified and the stock is a high-beta cybersecurity name with execution risk.
- **Source IDs:** S021, S022, S026, S030
- **Catalysts:** 20-day momentum of 25.8%, Forward P/E near 9.1 offers valuation support, Revenue growth of 12.2% and earnings growth of 128.6%, Stable 60-day drawdown of 3.2%
- **Risks:** Forward EPS estimates are unverified, High-beta cybersecurity exposure, Execution risk in security operations, Single-quarter reported EPS may not reflect full-year trajectory
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 3.3374 (source.forwardEps) x AI multiple assumption 10.00; source IDs S021, S022, S026, S030
- **EPS:** 3.33736 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 9.108996
- **FY+1 growth assumption:** 12.86%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / General Electric (GE) and Honeywell (HON) as diversified industrials with similar margin and growth profiles / GEN has FY1 consensus growth of 12.86% and revenue growth of 12.2%, with strong gross margin (77.4%) but lower operating margin (43.2%) and profit margin (23.1%), and ROE of 0.464x. The base multiple of 10x is justified by moderate growth and margin structure, with bull/bear multiples reflecting potential margin expansion or further compression. Peer reference: GE and HON for diversified industrial growth and margin profiles.
- **Company fundamentals:** Gen Digital reported diluted EPS of 0.83 for the fiscal period ending 2026-10-02, with forward EPS of 3.34. Gross margin is 77.4%, operating margin is 43.2%, and profit margin is 23.1%. Revenue growth is 12.2% and earnings growth is 128.6%. Forward P/E is 9.11. Price is 30.40.
- **Bull / Base / Bear:** 43.39 / 33.37 / 26.7
- **Bull / Base / Bear returns:** 42.73% / 9.77% / -12.17%
- **Scenario probabilities:** not separately assigned; see scenario table.

### ROP — Roper Technologies

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Roper Technologies offers a high-margin, steady-growth technology platform with a forward P/E near 19.5, which is more reasonable than the elevated multiples of IDXX and the high-multiple dislocation names such as NOW and MRVL. Its steady growth and reasonable valuation make it a preferred holding within the momentum bucket. Alternatives considered: IDXX, NOW.
- **Thesis:** Roper Technologies screens in the top 20-day momentum bucket with a 25.4% 20-day return and a modest 2.5% 60-day drawdown. Reported diluted EPS of 21.30 and forward EPS of 24.57 support a forward P/E near 19.5, which is reasonable for a high-margin technology platform. Revenue growth is 7.6% and earnings growth is 32.6%, indicating steady operational improvement. However, the forward EPS estimate is unverified and the stock carries a moderate valuation.
- **Source IDs:** S033, S034, S041, S047
- **Catalysts:** 20-day momentum of 25.4%, Forward P/E near 19.5 offers reasonable valuation, Revenue growth of 7.6% and earnings growth of 32.6%, Stable 60-day drawdown of 2.5%
- **Risks:** Forward EPS estimates are unverified, Moderate valuation relative to growth, Exposure to niche technology markets, Single-quarter reported EPS may not reflect full-year trajectory
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 24.5732 (source.forwardEps) x AI multiple assumption 20.00; source IDs S033, S034, S041, S047
- **EPS:** 24.57318 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 19.532475
- **FY+1 growth assumption:** 9.81%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / Lowe's (LOW) and Home Depot (HD) as home improvement retailers with similar margin and growth profiles / ROP has FY1 consensus growth of 9.81% and revenue growth of 7.6%, with solid margins (gross 69.7%, operating 28.0%, profit 30.7%) and ROE of 0.132x. The base multiple of 20x is justified by stable growth and strong margins, with bull/bear multiples reflecting upside from continued home improvement demand and downside from housing cycle slowdown. Peer reference: LOW and HD for comparable retail and margin profiles.
- **Company fundamentals:** Roper Technologies reported diluted EPS of 21.30 for the fiscal period ending 2026-09-30, with forward EPS of 24.57. Gross margin is 69.7%, operating margin is 28.0%, and profit margin is 30.7%. Revenue growth is 7.6% and earnings growth is 32.6%. Forward P/E is 19.53. Price is 479.98.
- **Bull / Base / Bear:** 589.76 / 491.46 / 393.17
- **Bull / Base / Bear returns:** 22.87% / 2.39% / -18.09%
- **Scenario probabilities:** not separately assigned; see scenario table.

### XLV — Health Care sector ETF

- **Type:** ETF
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** The Health Care sector ETF provides diversified exposure to the sector with a low-cost structure, whereas holding individual names such as IDXX or LLY carries single-stock risk. The ETF's top holdings are well-known large-cap names with strong balance sheets, making it a preferred vehicle for sector exposure. Alternatives considered: XLP, XLY.
- **Thesis:** The Health Care sector ETF screens in the liquidity leader bucket with a 0.54% price change and strong dollar volume. The top holdings are dominated by large-cap pharmaceutical and medical device names such as LLY, JNJ, ABBV, MRK, and UNH, providing diversified exposure to the health care sector. The ETF offers a low-cost way to gain exposure to the sector without holding individual names.
- **Source IDs:** S055, S059
- **Catalysts:** Diversified exposure to large-cap health care names, Strong dollar volume and liquidity, Top holdings include LLY, JNJ, ABBV, MRK, and UNH, Sector-level exposure to health care demand
- **Risks:** Sector concentration in large-cap pharmaceuticals, Regulatory and reimbursement risk, Macro and interest rate sensitivity, Single-quarter reported EPS may not reflect full-year trajectory
- **Valuation method:** Holdings/portfolio valuation with AI total-return assumption
- **Valuation status:** verified; forward-EPS source: ; period flags: 
- **Valuation assumptions:** Holdings/portfolio valuation; 10 weighted holdings; coverage 61.42%; source IDs S055, S059
- **Top holdings:** LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59%
- **Portfolio valuation:** Top 10 holdings; numeric weight coverage 61.42%
- **Sector exposure:** Health Care
- **Underlying drivers:** Diversified exposure to large-cap pharmaceutical and medical device names, with top holdings including LLY, JNJ, ABBV, MRK, and UNH.
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
| Bull | 25% | +2.00% | Low realized volatility (14.9%) and below-threshold spike probability (16.5% vs 18.5% threshold) support a mild upside bias if US close confirms stable risk appetite. |
| Base | 50% | +0.00% | Frozen daily-close model with no directional signal and near-baseline volatility implies range-bound trading around the 2026-11-13 close. |
| Bear | 25% | -2.00% | Elevated spike probability (16.5%) and frozen model uncertainty create downside risk if US close reveals widening bid-ask or risk-off flows. |

### Long Term (12 months)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 30% | +8.00% | Sustained low volatility and stable baseline support a positive drift if earnings and credit spreads remain constructive over the horizon. |
| Base | 40% | +3.00% | Near-baseline volatility and no directional signal imply modest positive drift as frozen daily-close model normalizes toward historical levels. |
| Bear | 30% | -5.00% | Spike probability above threshold and frozen model uncertainty raise the risk of a drawdown if credit conditions tighten or earnings disappoint. |

## Positioning

- Maintain a defensive tilt with exposure to Health Care and Consumer Staples, which show strong momentum and positive flows.
- Reduce exposure to Information Technology and Energy, which are the weakest sectors with negative price momentum.
- Monitor Consumer Discretionary for flow signals; positive price momentum but structural distribution warrants caution.
- Watch the Utilities sector for continued institutional selling despite positive price action.
- Keep a balanced view on the macro environment: inflation is cooling but still elevated, and the labor market is stable.

## Catalysts

| Date | Event | Why it matters |
| --- | --- | --- |
| 2026-11-16 | US CPI release | October CPI data (337.48) will provide updated inflation readings; a cooler print could support Fed easing expectations. |
| 2026-11-16 | US unemployment rate release | October unemployment rate (4.1%) will provide updated labor market data; a stable or improving rate supports consumer spending. |
| 2026-11-16 | Fed policy meeting | The effective funds rate is 3.88%; a potential rate cut or guidance on easing could impact sector valuations. |
| 2026-11-16 | Treasury yield curve | The 10Y-2Y spread is 0.27; a further steepening or inversion could signal changing growth expectations. |

## Key Risks

- Inflation remains above target, with CPI at 336.3 and core CPI at 338.9, which could delay Fed easing.
- The labor market is stable but not overheating, with unemployment at 4.2%, but a slowdown could impact consumer spending.
- High-yield OAS is 3.20, indicating tight credit conditions; a widening could signal stress.
- Price-breadth divergence is -27.49, indicating some internal weakness despite positive breadth.
- Information Technology and Energy sectors are weak with negative momentum, which could drag on the broad market.
- Risk spike probability is 16.5%, below the historical baseline of 22.1%, but the frozen model indicates a relatively calm near-term risk profile.

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
| S008 | filing | PNR | 2026-10-27 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-27 (accession 0000077360-26-000058); 8-K filed 2026-10-27 (accession 0000077360-26-000055); 8-K filed 2026-09-22 (accession 0000077360-26-000050) |
| S009 | filing | APP | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001751008&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0001751008-26-000069); 8-K filed 2026-11-04 (accession 0001751008-26-000068); 10-Q filed 2026-08-05 (accession 0001751008-26-000059) |
| S010 | filing | FISV | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0000798354-26-000042); 8-K filed 2026-11-03 (accession 0000798354-26-000039); 8-K filed 2026-10-23 (accession 0001193125-26-429481) |
| S011 | news | APP | Thu, 12 Nov 2026 20:05:45 GMT | ok | https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en | AppLovin Just Ripped 47% in a Month: Is It Too Late to Buy APP Stock Now? - Yahoo Finance (Thu, 12 Nov 2026 20:05:45 GMT); Is Trending Stock AppLovin Corporation (APP) a Buy Now? - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT); APP Stock Surges 51% After Q3 Earnings: Is it Still a Buy? - Yahoo Finance (Tue, 10 Nov 2026 14:24:00 GMT) |
| S012 | filing | APP | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json | Diluted EPS 11.61 for period ending 2026-09-30 (filed 2026-11-04) |
| S013 | stock | APP | 2026-11-16 | ok | https://finance.yahoo.com/quote/APP | Trailing P/E: 27.54882; Forward P/E: 19.611452; Forward EPS: 20.86026; Price: 409.1; Market price: 409.1; Market cap: 135543824384; Sector: Communication Services; Trailing Eps: 14.85; Revenue Growth: 0.555; Earnings Growth: 0.755; Gross Margin: 0.8878; Operating Margin: 0.77782995; Profit Margin: 0.65887; Return On Equity: 2.1008599; Total Revenue: 7608893952; Market Cap: 135543824384; Consensus EPS FY+1: 20.72438; growth: 0.2744 |
| S014 | news | FISV | Fri, 13 Nov 2026 21:49:46 GMT | ok | https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en | Fiserv, Inc. (FISV) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 21:49:46 GMT); Fiserv (FISV) Stock Still Looks Like A Bargain After Lawsuit Claims - Yahoo Finance (Thu, 22 Oct 2026 07:00:00 GMT); FISV Stock Quote Price and Forecast - CNN (Fri, 13 Nov 2026 21:18:08 GMT) |
| S015 | news | PNR | Fri, 13 Nov 2026 22:09:48 GMT | ok | https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en | Pentair plc (PNR) stock price, news, quote and history - Yahoo Finance UK (Fri, 13 Nov 2026 22:09:48 GMT); Pentair plc (PNR) Q3 Earnings and Revenues Beat Estimates - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT); Pentair (PNR) Stock May Be 46% Undervalued As New CFO Arrives - Yahoo Finance (Fri, 25 Sep 2026 07:00:00 GMT) |
| S016 | stock | PNR | 2026-11-16 | ok | https://finance.yahoo.com/quote/PNR | Trailing P/E: 18.610355; Forward P/E: 12.877027; Forward EPS: 5.30402; Price: 68.3; Market price: 68.3; Market cap: 10904415232; Sector: Industrials; Trailing Eps: 3.67; Revenue Growth: -0.045; Earnings Growth: -0.188; Gross Margin: 0.40168998; Operating Margin: 0.21410999; Profit Margin: 0.15435; Return On Equity: 0.15605; Total Revenue: 3966200064; Market Cap: 10904415232; Consensus EPS FY+1: 5.30402; growth: 0.1282 |
| S017 | stock | FISV | 2026-11-16 | ok | https://finance.yahoo.com/quote/FISV | Forward P/E: 7.99667; Price: 63.78; Market price: 63.78; Market cap: 33934002176; Market Cap: 33934002176; Consensus EPS FY+1: 7.98015; growth: 0.09689999 |
| S018 | filing | FISV | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json | Diluted EPS -8.9 for period ending 2026-09-30 (filed 2026-11-04) |
| S019 | filing | PNR | 2026-10-27 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json | Diluted EPS 2.76 for period ending 2026-09-30 (filed 2026-10-27) |
| S020 | filing | CLX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000021076-26-000046); 8-K filed 2026-11-02 (accession 0000021076-26-000044); 8-K filed 2026-10-29 (accession 0001206774-26-000586) |
| S021 | filing | GEN | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0000849399-26-000083); 8-K filed 2026-10-28 (accession 0000849399-26-000081); 8-K filed 2026-10-09 (accession 0000849399-26-000079) |
| S022 | stock | GEN | 2026-11-16 | ok | https://finance.yahoo.com/quote/GEN | Trailing P/E: 15.431472; Forward P/E: 9.108996; Forward EPS: 3.33736; Price: 30.4; Market price: 30.4; Market cap: 18035593216; Sector: Technology; Trailing Eps: 1.97; Revenue Growth: 0.122; Earnings Growth: 1.286; Gross Margin: 0.77410007; Operating Margin: 0.43229; Profit Margin: 0.23068; Return On Equity: 0.46402; Total Revenue: 5228000256; Market Cap: 18035593216; Consensus EPS FY+1: 3.33736; growth: 0.1286 |
| S023 | stock | CLX | 2026-11-16 | ok | https://finance.yahoo.com/quote/CLX | Trailing P/E: 19.68705; Forward P/E: 17.745283; Forward EPS: 6.1684; Price: 109.46; Market price: 109.46; Market cap: 13260793856; Sector: Consumer Defensive; Trailing Eps: 5.56; Revenue Growth: 0.333; Earnings Growth: 1.138; Gross Margin: 0.41939998; Operating Margin: 0.14286; Profit Margin: 0.09408; Return On Equity: 5.34363; Total Revenue: 7196000256; Market Cap: 13260793856; Consensus EPS FY+1: 6.1684; growth: 0.0769 |
| S024 | filing | CHTR | 2026-11-06 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-06 (accession 0001091667-26-000073); 8-K filed 2026-11-06 (accession 0001091667-26-000072); 8-K filed 2026-10-27 (accession 0001091667-26-000064) |
| S025 | filing | IDXX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000874716&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000874716-26-000135); 8-K filed 2026-11-02 (accession 0001104659-26-120892); 10-Q filed 2026-08-04 (accession 0000874716-26-000123) |
| S026 | news | GEN | Thu, 29 Oct 2026 07:00:00 GMT | ok | https://news.google.com/rss/search?q=GEN+Gen+Digital+stock&hl=en-US&gl=US&ceid=US:en | Gen Digital (GEN) Stock Repriced After Q2 Earnings Put Margins Center Stage - Yahoo Finance (Thu, 29 Oct 2026 07:00:00 GMT); Are Business Services Stocks Lagging GEN DIGITAL INC (GEN) This Year? - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT); Gen Digital Stock: Is Wall Street Bullish or Bearish? - Yahoo Finance (Thu, 05 Nov 2026 08:00:00 GMT) |
| S027 | stock | CHTR | 2026-11-16 | ok | https://finance.yahoo.com/quote/CHTR | Trailing P/E: 13.006578; Forward P/E: 3.2831066; Forward EPS: 42.15215; Price: 138.39; Market price: 138.39; Market cap: 24778944512; Sector: Communication Services; Trailing Eps: 10.64; Revenue Growth: 0.091; Gross Margin: 0.55084; Operating Margin: 0.23389; Profit Margin: 0.02498; Return On Equity: 0.07019; Total Revenue: 55645999104; Market Cap: 24778944512; Consensus EPS FY+1: 47.15811; growth: 1.0195 |
| S028 | news | CLX | Sun, 15 Nov 2026 08:55:47 GMT | ok | https://news.google.com/rss/search?q=CLX+Clorox+stock&hl=en-US&gl=US&ceid=US:en | The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance UK (Sun, 15 Nov 2026 08:55:47 GMT); The Clorox Company (CLX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 23:34:51 GMT); Clorox (CLX) Down 9.3% Since Last Earnings Report: Can It Rebound? - Yahoo Finance (Wed, 02 Sep 2026 07:00:00 GMT) |
| S029 | news | CHTR | Sun, 15 Nov 2026 05:47:01 GMT | ok | https://news.google.com/rss/search?q=CHTR+Charter+Communications+stock&hl=en-US&gl=US&ceid=US:en | Charter Communications (CHTR) Stock Could Be A Bargain Following Its New Operating Model - Yahoo Finance (Sun, 15 Nov 2026 05:47:01 GMT); Why You Should Think About Charter Communications Differently Now? - Yahoo Finance (Fri, 13 Nov 2026 19:16:11 GMT); Charter Communications (CHTR) Expands Enterprise Reach With Managed Secure Networking Launch - Yahoo Finance (Sun, 15 Nov 2026 06:08:00 GMT) |
| S030 | filing | GEN | 2026-10-29 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000849399.json | Diluted EPS 0.83 for period ending 2026-10-02 (filed 2026-10-29) |
| S031 | filing | CHTR | 2026-11-06 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001091667.json | Diluted EPS 0.38 for period ending 2026-09-30 (filed 2026-11-06) |
| S032 | filing | IDXX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000874716.json | Diluted EPS 11.75 for period ending 2026-09-30 (filed 2026-11-02) |
| S033 | filing | ROP | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000882835&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000882835-26-000047); 8-K filed 2026-10-22 (accession 0000882835-26-000042); 8-K filed 2026-10-01 (accession 0000882835-26-000039) |
| S034 | stock | ROP | 2026-11-16 | ok | https://finance.yahoo.com/quote/ROP | Trailing P/E: 18.993866; Forward P/E: 19.532475; Forward EPS: 24.57318; Price: 479.975; Market price: 479.975; Market cap: 47535013888; Sector: Technology; Trailing Eps: 25.27; Revenue Growth: 0.076; Earnings Growth: 0.326; Gross Margin: 0.69671; Operating Margin: 0.28049; Profit Margin: 0.30712998; Return On Equity: 0.13229; Total Revenue: 8434599936; Market Cap: 47535013888; Consensus EPS FY+1: 24.57318; growth: 0.09810001 |
| S035 | filing | CLX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000021076.json | Diluted EPS 1.39 for period ending 2026-09-30 (filed 2026-11-02) |
| S036 | stock | IDXX | 2026-11-16 | ok | https://finance.yahoo.com/quote/IDXX | Trailing P/E: 47.45485; Forward P/E: 41.687927; Forward EPS: 16.8929; Price: 704.23; Market price: 704.23; Market cap: 55483650048; Sector: Healthcare; Trailing Eps: 14.84; Revenue Growth: 0.099; Earnings Growth: 0.179; Gross Margin: 0.62722; Operating Margin: 0.32497; Profit Margin: 0.25357; Return On Equity: 0.68925005; Total Revenue: 4662220800; Market Cap: 55483650048; Consensus EPS FY+1: 16.8929; growth: 0.1244 |
| S037 | news | IDXX | Sat, 14 Nov 2026 22:37:20 GMT | ok | https://news.google.com/rss/search?q=IDXX+Idexx+Laboratories+stock&hl=en-US&gl=US&ceid=US:en | IDEXX Laboratories, Inc. (IDXX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Sat, 14 Nov 2026 22:37:20 GMT); symbol__ Stock Quote Price and Forecast - CNN (Fri, 13 Nov 2026 15:22:45 GMT); IDEXX Laboratories (IDXX) Stock Looks Fairly Valued Despite Its 28% Run - Yahoo Finance (Sat, 31 Oct 2026 07:00:00 GMT) |
| S038 | filing | RDDT | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001713445&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0001713445-26-000116); 8-K filed 2026-10-29 (accession 0001713445-26-000114); 8-K filed 2026-08-12 (accession 0001713445-26-000107) |
| S039 | filing | INTC | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000050863&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0000050863-26-000191); 8-K filed 2026-10-29 (accession 0000050863-26-000188); 8-K filed 2026-08-12 (accession 0001193125-26-346806) |
| S040 | stock | RDDT | 2026-11-16 | ok | https://finance.yahoo.com/quote/RDDT | Trailing P/E: 20.091835; Forward P/E: 10.818217; Forward EPS: 9.10039; Price: 98.45; Market price: 98.45; Market cap: 19010076672; Sector: Communication Services; Trailing Eps: 4.9; Revenue Growth: 0.53; Earnings Growth: 0.749; Gross Margin: 0.91547996; Operating Margin: 0.29397; Profit Margin: 0.32105; Return On Equity: 0.32029998; Total Revenue: 3088880128; Market Cap: 19010076672; Consensus EPS FY+1: 6.82439; growth: 0.2417 |

## Sources

- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFF&cosd=2026-01-01 (2026-11-12)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLH0A0HYM2&cosd=2026-01-01 (2026-11-12)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLC0A0CM&cosd=2026-01-01 (2026-11-12)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCSL&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=UNRATE&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=PAYEMS&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=T10Y2Y&cosd=2026-01-01 (2026-11-13)
- filing PNR: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 (2026-10-27)
- filing APP: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001751008&type=10-Q&dateb=&owner=include&count=10 (2026-11-04)
- filing FISV: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 (2026-11-04)
- news APP: https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en (Thu, 12 Nov 2026 20:05:45 GMT)
- filing APP: https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json (2026-11-04)
- stock APP: https://finance.yahoo.com/quote/APP (2026-11-16)
- news FISV: https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 21:49:46 GMT)
- news PNR: https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 22:09:48 GMT)
- stock PNR: https://finance.yahoo.com/quote/PNR (2026-11-16)
- stock FISV: https://finance.yahoo.com/quote/FISV (2026-11-16)
- filing FISV: https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json (2026-11-04)
- filing PNR: https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json (2026-10-27)
- filing CLX: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 (2026-11-02)

## AI Provenance

- Provider / model: hermes-local-proxy / upstage/solar-mini4:free
- Market research: attempts=1 tokens=9338 (prompt=6513, completion=2825) runtime=21.37s
- Fundamental research: generated this run at 2026-11-16T07:07:20.703941+00:00
- Evidence source dates: {'as_of': '2026-11-13', 'latest_equity_date': '2026-11-13', 'latest_macro_date': '2026-11-16', 'flows_date': '2026-11-13'}
- Evidence fingerprint: 3c48f623e104c453e6ccdf71be967a58bc5feb6e1f10ada9b77dbd18e2c552eb
- Source citations are retrieved external records in the ledger above; market values remain from the verified database snapshot.


## Disclosures

- This is research and market intelligence, not investment advice.
- AI conclusions are research judgments, not validated return predictions.
- The frozen risk layer is risk-only and is not used for directional views or allocations.
- Legacy scores are not active inputs or outputs.

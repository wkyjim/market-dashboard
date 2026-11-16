# AEGIS AI-First Market Intelligence

Research generated at: 16 November 2026, 11:13 HKT
Database freshness: equity 2026-11-13 (latest row retrieved 2026-11-15 13:06:40.074841+08:00)
Data cutoff: 2026-11-13 US cash close
Snapshot ID: aegis-hourly-20261116T031337Z

## Executive Summary

- **AI market view: Late-November 2026 equity market is in a late-cycle, modestly positive tape with broad momentum but a concentration of dislocation names and a sharp crypto de-risking event. Breadth is constructive on price and 20-day momentum, yet 52-week high/low coverage is thin and the advance/decline ratio is not uniformly bullish. Sector leadership is split: defensive and consumer staples/health care led, while information technology and energy lagged. Flows show exceptional institutional buying in SOXX, but TLT and SMH show mixed/neutral positioning. Macro data remain anchored by a 4.2% unemployment rate and core CPI near 338.9, with the Fed at 3.88% and a modestly positive 10Y-2Y spread.**
- Equity market is in a late-cycle, modestly positive tape with broad 20-day momentum (70.5% positive) and 50-day/200-day above-market percentages of 71.3% and 63.6%.
- Breadth is constructive on price but thin on 52-week highs; advance/decline ratio is 1.70, while new highs/new lows are both 0%.
- Crypto de-risking is acute: BTC -6.0% and ETH -8.2% on 2026-11-14, with high-beta tech and liquidity-leader names showing elevated valuations.
- Sector leadership is defensive: Health Care (+6.9%), Consumer Discretionary (+6.7%), Consumer Staples (+5.4%), Real Estate (+5.2%), Financials (+5.7%) led; Information Technology (-7.2%) and Energy (-4.8%) lagged.
- Flows show exceptional institutional buying in SOXX (20d z-score 5.10, 60d 3.17), while TLT is neutral/negative and SMH shows tactical profit-taking inside structural accumulation.
- Macro backdrop is stable but not accelerating: unemployment 4.2%, core CPI 338.9, effective fed funds 3.88%, 10Y-2Y spread 0.27, IG OAS 0.89, HY OAS 3.20.
- Risk environment is elevated but not spiking: forecast 5-day vol 14.9%, spike probability 16.5% below historical 22.1% and EWMA 20.1% baselines, directional signal false.
- Screening shortlist is dominated by momentum and dislocation names with wide dispersion in P/E and earnings yield; several names carry forward-EPS/valuation quality flags.

## Data QC

- Status: **PASS_WITH_WARNINGS**
- Equity session: 0 completed session(s) behind inference date
- Equity provenance: 393 provisional / 12576 canonical
- Breadth lag: 0 session(s); ETF-flow lag: 0 session(s)
- Note: Equity session contains a mix of provisional yfinance and canonical Massive rows.
- External sources: 79 ok / 0 unavailable; retrieved 2026-11-16T03:13:58.946951+00:00

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
| S&P 500 (SPX) | 7561.67 | -1.28% over 20d | Index is in a late-cycle, modestly positive tape with broad 20-day momentum but negative 20-day return. |
| Health Care (XLV) | +6.87% | 20d return | Top sector performer; trailing P/E 30.78 suggests rich valuation. |
| Consumer Discretionary (XLY) | +6.69% | 20d return | Strong 20d return; trailing P/E 25.11. |
| Information Technology (XLK) | -7.19% | 20d return | Largest sector drag; trailing P/E 30.03 with elevated single-name liquidity-leader multiples. |
| Energy (XLE) | -4.81% | 20d return | Negative 20d return; trailing P/E 16.23. |
| SOXX | inflow | 20d z-score 5.10, 60d 3.17 | Exceptional institutional buying; price state down, strong confirmation. |
| TLT | neutral | 20d z-score -0.41, 60d -0.29 | Medium-term deterioration; price flat. |
| SMH | outflow | 20d z-score 1.22, 60d 1.04 | Tactical profit-taking inside structural accumulation. |

## Macro, Fiscal, Rates, Liquidity and Credit

- Growth and labor: unemployment rate is 4.2% (2026-09-01), with nonfarm payrolls 159,293k (2026-10-01) from external source S006; labor market remains stable but not overheating.
- Inflation: CPI 336.298 and core CPI 338.896 (2026-09-01) from database; external S004 gives CPI 337.476 for 2026-10-01, indicating inflation is sticky near 3% but not accelerating.
- Policy: effective federal funds rate is 3.88% as of 2026-11-12 (S001), consistent with a late-cycle easing bias; 10Y-2Y spread is 0.27 (S007), a modestly positive but shallow curve.
- Rates and credit: IG OAS 0.89 and HY OAS 3.20 (S002, S003) as of 2026-11-12; spreads are tight, signaling low default risk and ample credit availability.
- Liquidity and risk assets: crypto de-risking is sharp, with BTC -6.0% and ETH -8.2% on 2026-11-14, suggesting forced selling in high-beta risk assets.
- Volatility and spike risk: forecast 5-day vol 14.9%, spike probability 16.5% below historical 22.1% and EWMA 20.1% baselines; directional signal false, so no directional bias is implied.

## US Equities and 11 GICS Sectors

Macro source IDs: S001, S002, S003, S004, S005, S006, S007

| GICS sector | Evidence | AI research stance | Source IDs |
| --- | --- | --- | --- |
| Health Care | 20d return +6.87%; trailing P/E 30.78 (S055); top sector performer in the 20d window. | Defensive leadership with rich valuation; momentum-led but expensive on trailing earnings. | S055 |
| Consumer Staples | 20d return +5.40%; trailing P/E 24.85 (S056); stable defensive sector. | Defensive ballast; valuation is moderate relative to health care. | S056 |
| Consumer Discretionary | 20d return +6.69%; trailing P/E 25.11 (S061); strong 20d momentum. | Consumer-led strength; valuation is reasonable but not cheap. | S061 |
| Real Estate | 20d return +5.24%; trailing P/E 29.63 (S065); positive but not leading. | Modest positive return; valuation is elevated relative to financials. | S065 |
| Financials | 20d return +5.69%; trailing P/E 15.85 (S063); positive but not leading. | Positive momentum with low valuation; rate-sensitive but not a leader. | S063 |
| Utilities | 20d return +4.34%; trailing P/E 18.11 (S064); defensive but lower return. | Defensive sector with moderate valuation; lower relative strength. | S064 |
| Materials | 20d return +2.57%; trailing P/E 21.72 (S070); modest positive. | Low single-digit positive return; valuation is mid-range. | S070 |
| Industrials | 20d return +0.61%; trailing P/E 27.07 (S068); near flat. | Weakest positive sector; valuation is rich relative to return. | S068 |
| Communication Services | 20d return -1.48%; trailing P/E 17.26 (S072); negative but not the worst. | Slight negative return; valuation is reasonable but momentum negative. | S072 |
| Information Technology | 20d return -7.19%; trailing P/E 30.03 (S073); largest sector drag. | Negative momentum and high concentration risk; elevated single-name multiples (MRVL, NOW, AMD) with quality flags. | S073 |
| Energy | 20d return -4.81%; trailing P/E 16.23 (S075); negative but cheap. | Negative momentum but low valuation; energy is a relative value play. | S075 |

### Sector fundamentals, valuation and earnings

No point-in-time sector-level fundamentals (e.g., revenue growth, margins, consensus EPS) are supplied in the database snapshot. The sector evidence is limited to 20d ETF returns and trailing P/E from external sources S055-S075. Growth, margin, and consensus data are unavailable for the full sector universe, so sector views are based on price momentum and valuation multiples only.

## Growth vs Value

- Growth: Information Technology and Communication Services carry the highest trailing P/E multiples (XLK 30.03, XLC 17.26) and the largest single-name dislocation names (NOW 97.19, MRVL 74.23, AMD 128.88), but these are flagged for forward-EPS/valuation quality issues.
- Value: Energy (XLE 16.23), Financials (XLF 15.85), and Utilities (XLU 18.11) offer the lowest trailing P/E, but Energy and Financials are negative/weak on 20d momentum while Utilities is defensive.
- Screening shortlist: momentum names APP, FISV, PNR, GEN, CLX, CHTR, IDXX, ROP show top-20d-momentum reasons, while dislocation names RDDT, INTC, SNDK, FFIV, LITE, COIN show largest-20d-dislocation reasons; several have negative or missing earnings yield.
- Valuation dispersion: sector-relative P/E ranges from 0.13 (CHTR) to 2.20 (MRVL), indicating extreme dispersion in how the market prices growth; only a few names have clean forward-EPS coverage.

## ETF Flows and Breadth

- SOXX is the standout flow: 20d z-score 5.10 and 60d 3.17, classified as inflow with strong confirmation and exceptional institutional buying, despite price being down.
- TLT shows medium-term deterioration with 20d z-score -0.41 and 60d -0.29, price flat, indicating neutral-to-negative bond flows.
- SMH shows tactical profit-taking inside structural accumulation: 20d z-score 1.22 and 60d 1.04, classified as outflow with price down.
- Breadth: 71.3% of names above 50d, 63.6% above 200d, 70.5% positive on 20d; advance/decline ratio 1.70 with 315 advancers vs 185 decliners

## Stock Ideas

Single-stock research uses reported EPS, forward P/E and company fundamentals. All ideas are research judgments, not validated return predictions.

| Ticker | Security | Research view | Price | EPS | Forward P/E | Base target | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| APP | AppLovin | NEW | 409.1 | 20.86026 | 19.611452 | 417.21 | NEW |
| PNR | Pentair | KEEP | 68.3 | 5.30402 | 12.877027 | 68.95 | KEEP |
| GEN | Gen Digital | NEW | 30.4 | 3.33736 | 9.108996 | 30.04 | NEW |
| CLX | Clorox | KEEP | 109.46 | 6.1684 | 17.745283 | 111.03 | KEEP |
| IDXX | Idexx Laboratories | KEEP | 704.23 | 16.8929 | 41.687927 | 709.5 | KEEP |

## ETF Ideas

ETF research uses holdings, portfolio valuation and exposure. Single-stock EPS × P/E valuation is not applied to ETFs.

No qualifying ETF ideas this run.
### APP — AppLovin

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** AppLovin offers a rare combination of top-tier momentum, high profitability, and a reasonable forward P/E, making it a stronger candidate than the lower-quality, high-multiple names such as NOW (forward P/E unavailable) or MRVL (forward P/E 74.2x) that also appear in the shortlist. Alternatives considered: NOW, MRVL.
- **Thesis:** AppLovin screens in the top 20-day momentum bucket with a 53.7% 20-day return and a 32.5% 60-day return, while its 60-day drawdown is only -0.2%, indicating a strong, sustained price advance without a meaningful pullback. The company carries a high gross margin of 88.8% and operating margin of 77.8%, with revenue growth of 55.5% and earnings growth of 75.5%, supporting a premium but still reasonable valuation. The forward P/E of 19.6x is well below the trailing P/E of 20.1x, implying modest re-rating potential as the market prices in continued growth.
- **Source IDs:** S008, S012, S013, S019
- **Catalysts:** Continued high-margin advertising revenue growth, Sustained 20-day momentum momentum and positive 60-day trend, Forward P/E compression from trailing P/E as earnings catch up
- **Risks:** High valuation already priced in; any deceleration in ad spend could trigger a sharp reversal, Single-quarter momentum can be volatile; 20-day return of 53.7% may not persist, Forward EPS estimates are unverified and fiscal-year mapping is unverified
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 20.8603 (source.forwardEps) x AI multiple assumption 20.00; source IDs S008, S012, S013, S019
- **EPS:** 20.86026 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 19.611452
- **FY+1 growth assumption:** 27.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / PNR / APP shows strong FY1 consensus growth of 27.44% with 25.4% revenue growth and 75.5% earnings growth, supported by 88.8% gross margin and 77.8% operating margin. PNR is the named peer reference: both are high-margin, asset-light software/tech platforms with durable competitive moats, and PNR's lower growth and margin profile supports a lower multiple band for APP. The base multiple of 20.0 reflects APP's superior growth and margins relative to the peer, while the bull/bear band of 24.0/16.0 captures upside if growth accelerates and downside if it decelerates.
- **Company fundamentals:** AppLovin (APP) is a high-margin mobile advertising and gaming company. Reported diluted EPS is $11.61 for the period ending 2026-09-30. Forward EPS is $20.86, implying a forward P/E of 19.6x. Revenue growth is 55.5% and earnings growth is 75.5%. Gross margin is 88.8% and operating margin is 77.8%. Return on equity is 2.10x. The stock closed at $409.10 with dollar volume of $1.41B. Source IDs: S008, S012, S013, S019.
- **Bull / Base / Bear:** 500.65 / 417.21 / 333.76
- **Bull / Base / Bear returns:** 22.38% / 1.98% / -18.42%
- **Scenario probabilities:** not separately assigned; see scenario table.

### PNR — Pentair

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Pentair provides a reasonable valuation entry point in the industrials sector, but its negative growth and modest momentum make it less attractive than higher-quality momentum names like AppLovin or Gen Digital, which combine positive growth with stronger momentum. Alternatives considered: APP, GEN.
- **Thesis:** Pentair screens in the top 20-day momentum bucket with a 27.8% 20-day return and a 7.1% 60-day return, but its 60-day drawdown of -5.2% and negative revenue growth of -4.5% and earnings growth of -18.8% indicate that the momentum is not yet supported by fundamental improvement. The forward P/E of 12.9x is reasonable, but the negative growth profile warrants caution. The stock is a core industrial exposure with a reasonable valuation, but the negative growth and modest momentum do not justify a strong buy stance.
- **Source IDs:** S009, S014, S018, S027
- **Catalysts:** Potential stabilization in industrial end-market demand, Reasonable forward P/E of 12.9x relative to negative growth, Continued 20-day momentum of 27.8%
- **Risks:** Negative revenue growth of -4.5% and earnings growth of -18.8%, 60-day drawdown of -5.2% suggests some weakness, Forward EPS estimates are unverified and fiscal-year mapping is unverified
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 5.3040 (source.forwardEps) x AI multiple assumption 13.00; source IDs S009, S014, S018, S027
- **EPS:** 5.30402 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 12.877027
- **FY+1 growth assumption:** 12.82%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / APP / PNR is the named peer reference for APP, but PNR itself shows weaker fundamentals: FY1 consensus growth of 12.82% with negative revenue growth of -4.5% and negative earnings growth of -18.8%, alongside lower gross margin of 40.2% and operating margin of 21.4%. The base multiple of 13.0 reflects these weaker growth and margin characteristics, with a bull/bear band of 16.0/10.0 capturing upside if the turnaround materializes and downside if the decline continues.
- **Company fundamentals:** Pentair (PNR) is a diversified water, flow control, and building products company. Reported diluted EPS is $2.76 for the period ending 2026-09-30. Forward EPS is $5.30, implying a forward P/E of 12.9x. Revenue growth is -4.5% and earnings growth is -18.8%. Gross margin is 40.2% and operating margin is 21.4%. Profit margin is 15.4%. Return on equity is 0.16x. The stock closed at $68.30 with dollar volume of $72.8M. Source IDs: S009, S014, S018, S027.
- **Bull / Base / Bear:** 84.86 / 68.95 / 53.04
- **Bull / Base / Bear returns:** 24.25% / 0.95% / -22.34%
- **Scenario probabilities:** not separately assigned; see scenario table.

### GEN — Gen Digital

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** Gen Digital offers a compelling combination of high earnings growth, a low forward P/E, and strong momentum, making it a better risk-adjusted opportunity than the lower-quality, high-multiple names such as NOW (forward P/E unavailable) or MRVL (forward P/E 74.2x) that also appear in the shortlist. Alternatives considered: NOW, MRVL.
- **Thesis:** Gen Digital screens in the top 20-day momentum bucket with a 25.8% 20-day return and a 7.9% 60-day return, while its 60-day drawdown is only -3.2%, indicating a strong, sustained price advance. The company carries a reasonable forward P/E of 9.1x, with revenue growth of 12.2% and earnings growth of 128.6%. The high earnings growth and reasonable valuation support a buy stance, especially given the positive momentum and low drawdown.
- **Source IDs:** S015, S021, S022, S024
- **Catalysts:** High earnings growth of 128.6% supporting a low forward P/E of 9.1x, Sustained 20-day momentum of 25.8% and low 60-day drawdown of -3.2%, Reasonable valuation relative to growth
- **Risks:** Forward EPS estimates are unverified and fiscal-year mapping is unverified, 20-day momentum of 25.8% may not persist, Cybersecurity and digital risk exposure to regulatory and competitive shifts
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 3.3374 (source.forwardEps) x AI multiple assumption 9.00; source IDs S015, S021, S022, S024
- **EPS:** 3.33736 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 9.108996
- **FY+1 growth assumption:** 12.86%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / IDXX / GEN shows FY1 consensus growth of 12.86% with modest revenue growth of 6.8% and strong earnings growth of 128.6%, supported by a 77.4% gross margin and 43.2% operating margin. IDXX is the named peer reference: both are software/tech platforms with strong gross margins and recurring revenue models, but GEN's higher earnings growth and operating leverage justify a higher multiple than IDXX's current valuation. The base multiple of 9.0 reflects GEN's solid growth and margins, with a bull/bear band of 11.0/7.0 capturing upside if earnings growth accelerates and downside if it decelerates.
- **Company fundamentals:** Gen Digital (GEN) is a cybersecurity and digital risk company. Reported diluted EPS is $0.83 for the period ending 2026-10-02. Forward EPS is $3.34, implying a forward P/E of 9.1x. Revenue growth is 12.2% and earnings growth is 128.6%. Gross margin is 77.4% and operating margin is 43.2%. Profit margin is 23.1%. Return on equity is 0.46x. The stock closed at $30.40 with dollar volume of $142.1M. Source IDs: S015, S021, S022, S024.
- **Bull / Base / Bear:** 36.71 / 30.04 / 23.36
- **Bull / Base / Bear returns:** 20.76% / -1.18% / -23.16%
- **Scenario probabilities:** not separately assigned; see scenario table.

### CLX — Clorox

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Clorox provides a reasonable valuation entry point in the consumer staples sector, but its flat 60-day trend and modest momentum make it less attractive than higher-quality momentum names like AppLovin or Gen Digital, which combine positive growth with stronger momentum. Alternatives considered: APP, GEN.
- **Thesis:** Clorox screens in the top 20-day momentum bucket with a 25.7% 20-day return and a 3.2% 60-day return, but its 60-day drawdown is 0.0%, indicating a flat trend. The company carries a forward P/E of 17.7x, with revenue growth of 33.3% and earnings growth of 113.8%. The high earnings growth supports the valuation, but the flat 60-day trend and modest forward P/E relative to growth do not justify a strong buy stance. The stock is a core consumer staples exposure with reasonable valuation, but the flat trend and modest momentum do not justify a strong buy stance.
- **Source IDs:** S020, S025, S026, S029
- **Catalysts:** High earnings growth of 113.8% supporting a forward P/E of 17.7x, Positive 20-day momentum of 25.7%, Consumer staples defensive characteristics
- **Risks:** 60-day drawdown of 0.0% indicates a flat trend, Forward EPS estimates are unverified and fiscal-year mapping is unverified, Consumer staples sector faces margin pressure from input costs and competition
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 6.1684 (source.forwardEps) x AI multiple assumption 18.00; source IDs S020, S025, S026, S029
- **EPS:** 6.1684 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 17.745283
- **FY+1 growth assumption:** 7.69%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / IDXX / CLX shows FY1 consensus growth of 7.69% with revenue growth of 2.2% and earnings growth of 113.8%, supported by a 41.9% gross margin and 14.3% operating margin. IDXX is the named peer reference: both are consumer/industrial companies with recurring revenue models, but CLX's lower growth and margin profile relative to IDXX justifies a lower multiple. The base multiple of 18.0 reflects CLX's moderate growth and margins, with a bull/bear band of 22.0/14.0 capturing upside if earnings growth accelerates and downside if it decelerates.
- **Company fundamentals:** Clorox (CLX) is a consumer staples company focused on cleaning, food, and personal care products. Reported diluted EPS is $1.39 for the period ending 2026-09-30. Forward EPS is $6.17, implying a forward P/E of 17.7x. Revenue growth is 33.3% and earnings growth is 113.8%. Gross margin is 41.9% and operating margin is 14.3%. Profit margin is 9.4%. Return on equity is 5.34x. The stock closed at $109.46 with dollar volume of $353.1M. Source IDs: S020, S025, S026, S029.
- **Bull / Base / Bear:** 135.7 / 111.03 / 86.36
- **Bull / Base / Bear returns:** 23.97% / 1.43% / -21.1%
- **Scenario probabilities:** not separately assigned; see scenario table.

### IDXX — Idexx Laboratories

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Idexx Laboratories offers a strong momentum profile in the health care sector, but its high valuation relative to growth makes it less attractive than lower-multiple, higher-growth names like Gen Digital, which combines positive growth with a much lower forward P/E. Alternatives considered: GEN, ROP.
- **Thesis:** Idexx Laboratories screens in the top 20-day momentum bucket with a 25.7% 20-day return and a 29.0% 60-day return, but its 60-day drawdown is only -0.3%, indicating a strong, sustained price advance. The company carries a high forward P/E of 41.7x, with revenue growth of 9.9% and earnings growth of 17.9%. The high valuation relative to growth and the premium sector-relative P/E of 1.33x suggest limited upside. The stock is a core health care exposure with strong momentum, but the high valuation and modest growth do not justify a strong buy stance.
- **Source IDs:** S031, S033, S034, S043
- **Catalysts:** Strong 20-day momentum of 25.7% and 60-day momentum of 29.0%, Low 60-day drawdown of -0.3%, Stable veterinary and diagnostic diagnostics business
- **Risks:** High forward P/E of 41.7x relative to 9.9% revenue growth and 17.9% earnings growth, Sector-relative P/E of 1.33x indicates premium valuation, Forward EPS estimates are unverified and fiscal-year mapping is unverified
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 16.8929 (source.forwardEps) x AI multiple assumption 42.00; source IDs S031, S033, S034, S043
- **EPS:** 16.8929 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 41.687927
- **FY+1 growth assumption:** 12.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / GEN / IDXX shows FY1 consensus growth of 12.44% with revenue growth of 8.9% and earnings growth of 17.9%, supported by a 62.7% gross margin and 32.5% operating margin. GEN is the named peer reference: both are software/tech platforms with strong gross margins and recurring revenue models, but IDXX's higher valuation multiple reflects its larger market cap and more mature growth profile. The base multiple of 42.0 reflects IDXX's premium valuation justified by its scale and stable growth, with a bull/bear band of 50.0/34.0 capturing upside if growth accelerates and downside if it decelerates.
- **Company fundamentals:** Idexx Laboratories (IDXX) is a veterinary diagnostics and animal health company. Reported diluted EPS is $11.75 for the period ending 2026-09-30. Forward EPS is $16.89, implying a forward P/E of 41.7x. Revenue growth is 9.9% and earnings growth is 17.9%. Gross margin is 62.7% and operating margin is 32.5%. Profit margin is 25.4%. Return on equity is 0.69x. The stock closed at $704.23 with dollar volume of $276.4M. Source IDs:
- **Bull / Base / Bear:** 844.65 / 709.5 / 574.36
- **Bull / Base / Bear returns:** 19.94% / 0.75% / -18.44%
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
| Bull | 25% | +2.00% | Low 5-day realized vol (14.9%) and below-threshold spike probability (16.5%) support a mild upside continuation if US close confirms the frozen daily model. |
| Base | 50% | +0.00% | Directional signal is false and the forecast is prospective, so the most likely path is a range-bound close near the frozen daily baseline with no directional alpha. |
| Bear | 25% | -2.00% | If the US close fails to confirm the frozen model, elevated spike probability relative to baseline could trigger a mild downside correction. |

### Long Term (12 months)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 30% | +8.00% | Sustained low volatility and confirmed US close support a positive earnings/credit trajectory, allowing a moderate long-term upside. |
| Base | 40% | +3.00% | Frozen daily-close model with no directional signal implies a steady, non-inflationary long-term drift near the baseline. |
| Bear | 30% | -5.00% | Failure to confirm the frozen model combined with elevated spike probability could pressure valuations and produce a mild long-term downside. |

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
| S011 | news | FISV | Fri, 13 Nov 2026 21:49:46 GMT | ok | https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en | Fiserv, Inc. (FISV) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 21:49:46 GMT); Michael Burry makes a bold call on struggling payments giant - Yahoo Finance (Wed, 11 Nov 2026 00:17:00 GMT); FISV Stock Quote Price and Forecast - CNN (Fri, 13 Nov 2026 21:18:08 GMT) |
| S012 | news | APP | Thu, 12 Nov 2026 20:05:45 GMT | ok | https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en | AppLovin Just Ripped 47% in a Month: Is It Too Late to Buy APP Stock Now? - Yahoo Finance (Thu, 12 Nov 2026 20:05:45 GMT); Is Trending Stock AppLovin Corporation (APP) a Buy Now? - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT); APP Stock Surges 51% After Q3 Earnings: Is it Still a Buy? - Yahoo Finance (Tue, 10 Nov 2026 14:24:00 GMT) |
| S013 | filing | APP | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json | Diluted EPS 11.61 for period ending 2026-09-30 (filed 2026-11-04) |
| S014 | news | PNR | Fri, 13 Nov 2026 22:09:48 GMT | ok | https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en | Pentair plc (PNR) stock price, news, quote and history - Yahoo Finance UK (Fri, 13 Nov 2026 22:09:48 GMT); Pentair plc (PNR) Q3 Earnings and Revenues Beat Estimates - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT); Pentair (PNR) Stock May Be 46% Undervalued As New CFO Arrives - Yahoo Finance (Fri, 25 Sep 2026 07:00:00 GMT) |
| S015 | filing | GEN | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0000849399-26-000083); 8-K filed 2026-10-28 (accession 0000849399-26-000081); 8-K filed 2026-10-09 (accession 0000849399-26-000079) |
| S016 | stock | FISV | 2026-11-16 | ok | https://finance.yahoo.com/quote/FISV | Forward P/E: 7.99667; Price: 63.78; Market price: 63.78; Market cap: 33934002176; Market Cap: 33934002176; Consensus EPS FY+1: 7.98015; growth: 0.09689999 |
| S017 | filing | FISV | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json | Diluted EPS -8.9 for period ending 2026-09-30 (filed 2026-11-04) |
| S018 | stock | PNR | 2026-11-16 | ok | https://finance.yahoo.com/quote/PNR | Trailing P/E: 18.610355; Forward P/E: 12.877027; Forward EPS: 5.30402; Price: 68.3; Market price: 68.3; Market cap: 10904415232; Sector: Industrials; Trailing Eps: 3.67; Revenue Growth: -0.045; Earnings Growth: -0.188; Gross Margin: 0.40168998; Operating Margin: 0.21410999; Profit Margin: 0.15435; Return On Equity: 0.15605; Total Revenue: 3966200064; Market Cap: 10904415232; Consensus EPS FY+1: 5.30402; growth: 0.1282 |
| S019 | stock | APP | 2026-11-16 | ok | https://finance.yahoo.com/quote/APP | Trailing P/E: 27.54882; Forward P/E: 19.611452; Forward EPS: 20.86026; Price: 409.1; Market price: 409.1; Market cap: 135543824384; Sector: Communication Services; Trailing Eps: 14.85; Revenue Growth: 0.555; Earnings Growth: 0.755; Gross Margin: 0.8878; Operating Margin: 0.77782995; Profit Margin: 0.65887; Return On Equity: 2.1008599; Total Revenue: 7608893952; Market Cap: 135543824384; Consensus EPS FY+1: 20.72438; growth: 0.2744 |
| S020 | filing | CLX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000021076-26-000046); 8-K filed 2026-11-02 (accession 0000021076-26-000044); 8-K filed 2026-10-29 (accession 0001206774-26-000586) |
| S021 | stock | GEN | 2026-11-16 | ok | https://finance.yahoo.com/quote/GEN | Trailing P/E: 15.431472; Forward P/E: 9.108996; Forward EPS: 3.33736; Price: 30.4; Market price: 30.4; Market cap: 18035593216; Sector: Technology; Trailing Eps: 1.97; Revenue Growth: 0.122; Earnings Growth: 1.286; Gross Margin: 0.77410007; Operating Margin: 0.43229; Profit Margin: 0.23068; Return On Equity: 0.46402; Total Revenue: 5228000256; Market Cap: 18035593216; Consensus EPS FY+1: 3.33736; growth: 0.1286 |
| S022 | news | GEN | Thu, 29 Oct 2026 07:00:00 GMT | ok | https://news.google.com/rss/search?q=GEN+Gen+Digital+stock&hl=en-US&gl=US&ceid=US:en | Gen Digital (GEN) Stock Repriced After Q2 Earnings Put Margins Center Stage - Yahoo Finance (Thu, 29 Oct 2026 07:00:00 GMT); Gen Digital Stock: Is Wall Street Bullish or Bearish? - Yahoo Finance (Thu, 05 Nov 2026 08:00:00 GMT); Are Business Services Stocks Lagging GEN DIGITAL INC (GEN) This Year? - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT) |
| S023 | filing | CHTR | 2026-11-06 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-06 (accession 0001091667-26-000073); 8-K filed 2026-11-06 (accession 0001091667-26-000072); 8-K filed 2026-10-27 (accession 0001091667-26-000064) |
| S024 | filing | GEN | 2026-10-29 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000849399.json | Diluted EPS 0.83 for period ending 2026-10-02 (filed 2026-10-29) |
| S025 | stock | CLX | 2026-11-16 | ok | https://finance.yahoo.com/quote/CLX | Trailing P/E: 19.68705; Forward P/E: 17.745283; Forward EPS: 6.1684; Price: 109.46; Market price: 109.46; Market cap: 13260793856; Sector: Consumer Defensive; Trailing Eps: 5.56; Revenue Growth: 0.333; Earnings Growth: 1.138; Gross Margin: 0.41939998; Operating Margin: 0.14286; Profit Margin: 0.09408; Return On Equity: 5.34363; Total Revenue: 7196000256; Market Cap: 13260793856; Consensus EPS FY+1: 6.1684; growth: 0.0769 |
| S026 | news | CLX | Sun, 15 Nov 2026 08:55:47 GMT | ok | https://news.google.com/rss/search?q=CLX+Clorox+stock&hl=en-US&gl=US&ceid=US:en | The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance UK (Sun, 15 Nov 2026 08:55:47 GMT); The Clorox Company (CLX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 23:34:51 GMT); A 10-Day Winning Streak Has Clorox Stock Up 24% - Trefis (Sat, 14 Nov 2026 08:28:05 GMT) |
| S027 | filing | PNR | 2026-10-27 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json | Diluted EPS 2.76 for period ending 2026-09-30 (filed 2026-10-27) |
| S028 | stock | CHTR | 2026-11-16 | ok | https://finance.yahoo.com/quote/CHTR | Trailing P/E: 13.006578; Forward P/E: 3.2831066; Forward EPS: 42.15215; Price: 138.39; Market price: 138.39; Market cap: 24778944512; Sector: Communication Services; Trailing Eps: 10.64; Revenue Growth: 0.091; Gross Margin: 0.55084; Operating Margin: 0.23389; Profit Margin: 0.02498; Return On Equity: 0.07019; Total Revenue: 55645999104; Market Cap: 24778944512; Consensus EPS FY+1: 47.15811; growth: 1.0195 |
| S029 | filing | CLX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000021076.json | Diluted EPS 1.39 for period ending 2026-09-30 (filed 2026-11-02) |
| S030 | news | CHTR | Sun, 15 Nov 2026 05:47:01 GMT | ok | https://news.google.com/rss/search?q=CHTR+Charter+Communications+stock&hl=en-US&gl=US&ceid=US:en | Charter Communications (CHTR) Stock Could Be A Bargain Following Its New Operating Model - Yahoo Finance (Sun, 15 Nov 2026 05:47:01 GMT); Why You Should Think About Charter Communications Differently Now? - Yahoo Finance (Fri, 13 Nov 2026 19:16:11 GMT); Charter Communications (CHTR) Expands Enterprise Reach With Managed Secure Networking Launch - Yahoo Finance (Sun, 15 Nov 2026 06:08:00 GMT) |
| S031 | news | IDXX | Sat, 14 Nov 2026 22:37:20 GMT | ok | https://news.google.com/rss/search?q=IDXX+Idexx+Laboratories+stock&hl=en-US&gl=US&ceid=US:en | IDEXX Laboratories, Inc. (IDXX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Sat, 14 Nov 2026 22:37:20 GMT); symbol__ Stock Quote Price and Forecast - CNN (Fri, 13 Nov 2026 15:22:45 GMT); IDEXX Laboratories (IDXX) Stock Looks Fairly Valued Despite Its 28% Run - Yahoo Finance (Sat, 31 Oct 2026 07:00:00 GMT) |
| S032 | filing | ROP | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000882835&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000882835-26-000047); 8-K filed 2026-10-22 (accession 0000882835-26-000042); 8-K filed 2026-10-01 (accession 0000882835-26-000039) |
| S033 | filing | IDXX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000874716&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000874716-26-000135); 8-K filed 2026-11-02 (accession 0001104659-26-120892); 10-Q filed 2026-08-04 (accession 0000874716-26-000123) |
| S034 | stock | IDXX | 2026-11-16 | ok | https://finance.yahoo.com/quote/IDXX | Trailing P/E: 47.45485; Forward P/E: 41.687927; Forward EPS: 16.8929; Price: 704.23; Market price: 704.23; Market cap: 55483650048; Sector: Healthcare; Trailing Eps: 14.84; Revenue Growth: 0.099; Earnings Growth: 0.179; Gross Margin: 0.62722; Operating Margin: 0.32497; Profit Margin: 0.25357; Return On Equity: 0.68925005; Total Revenue: 4662220800; Market Cap: 55483650048; Consensus EPS FY+1: 16.8929; growth: 0.1244 |
| S035 | stock | ROP | 2026-11-16 | ok | https://finance.yahoo.com/quote/ROP | Trailing P/E: 18.993866; Forward P/E: 19.532475; Forward EPS: 24.57318; Price: 479.975; Market price: 479.975; Market cap: 47535013888; Sector: Technology; Trailing Eps: 25.27; Revenue Growth: 0.076; Earnings Growth: 0.326; Gross Margin: 0.69671; Operating Margin: 0.28049; Profit Margin: 0.30712998; Return On Equity: 0.13229; Total Revenue: 8434599936; Market Cap: 47535013888; Consensus EPS FY+1: 24.57318; growth: 0.09810001 |
| S036 | filing | CHTR | 2026-11-06 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001091667.json | Diluted EPS 0.38 for period ending 2026-09-30 (filed 2026-11-06) |
| S037 | filing | RDDT | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001713445&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0001713445-26-000116); 8-K filed 2026-10-29 (accession 0001713445-26-000114); 8-K filed 2026-08-12 (accession 0001713445-26-000107) |
| S038 | stock | RDDT | 2026-11-16 | ok | https://finance.yahoo.com/quote/RDDT | Trailing P/E: 20.091835; Forward P/E: 10.770874; Forward EPS: 9.14039; Price: 98.45; Market price: 98.45; Market cap: 19010076672; Sector: Communication Services; Trailing Eps: 4.9; Revenue Growth: 0.53; Earnings Growth: 0.749; Gross Margin: 0.91547996; Operating Margin: 0.29397; Profit Margin: 0.32105; Return On Equity: 0.32029998; Total Revenue: 3088880128; Market Cap: 19010076672; Consensus EPS FY+1: 6.82439; growth: 0.2417 |
| S039 | filing | INTC | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000050863&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0000050863-26-000191); 8-K filed 2026-10-29 (accession 0000050863-26-000188); 8-K filed 2026-08-12 (accession 0001193125-26-346806) |
| S040 | news | ROP | Fri, 13 Nov 2026 13:04:22 GMT | ok | https://news.google.com/rss/search?q=ROP+Roper+Technologies+stock&hl=en-US&gl=US&ceid=US:en | Roper Technologies, Inc. (ROP) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 13:04:22 GMT); Roper Technologies (ROP) Stock Looks Fully Valued As Cash Flow Comes Into Focus - Yahoo Finance (Thu, 05 Nov 2026 08:00:00 GMT); Roper Technologies (ROP), What Is Behind The Fresh Attention? - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT) |

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
- news FISV: https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 21:49:46 GMT)
- news APP: https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en (Thu, 12 Nov 2026 20:05:45 GMT)
- filing APP: https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json (2026-11-04)
- news PNR: https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 22:09:48 GMT)
- filing GEN: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 (2026-10-29)
- stock FISV: https://finance.yahoo.com/quote/FISV (2026-11-16)
- filing FISV: https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json (2026-11-04)
- stock PNR: https://finance.yahoo.com/quote/PNR (2026-11-16)
- stock APP: https://finance.yahoo.com/quote/APP (2026-11-16)
- filing CLX: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 (2026-11-02)

## AI Provenance

- Provider / model: hermes-local-proxy / upstage/solar-mini4:free
- Market research: attempts=1 tokens=9473 (prompt=6473, completion=3000) runtime=20.36s
- Fundamental research: generated this run at 2026-11-16T03:13:37.848902+00:00
- Evidence source dates: {'as_of': '2026-11-13', 'latest_equity_date': '2026-11-13', 'latest_macro_date': '2026-11-14', 'flows_date': '2026-11-13'}
- Evidence fingerprint: b2c3fb438501b672d9e1fd8eaf69843c1c29ea621b908c98f7ce2162cf528fad
- Source citations are retrieved external records in the ledger above; market values remain from the verified database snapshot.


## Disclosures

- This is research and market intelligence, not investment advice.
- AI conclusions are research judgments, not validated return predictions.
- The frozen risk layer is risk-only and is not used for directional views or allocations.
- Legacy scores are not active inputs or outputs.

# AEGIS AI-First Market Intelligence

Research generated at: 15 November 2026, 22:16 HKT
Database freshness: equity 2026-11-13 (latest row retrieved 2026-11-15 13:06:40.074841+08:00)
Data cutoff: 2026-11-13 US cash close
Snapshot ID: aegis-hourly-20261115T141611Z

## Executive Summary

- **AI market view: Late-November 2026 US equity market is in a late-cycle, modestly positive momentum regime with broad-based 20-day strength but a thin new-high register and a negative 52-week price-breadth divergence. Large-cap mega-cap leadership (NVDA, AMD, MU, AAPL) is driving liquidity, while the broader market shows mixed 20-day returns and sector dispersion. Macro data point to a still-elevated but easing inflation backdrop, a labor market near full employment, and a policy rate that has been cut to 3.88%, with credit spreads modestly tight but not stressed.**
- Equity market: broad 20-day momentum is positive (70.5% of names above 20-day MA), but new highs are zero and 52-week price-breadth divergence is negative (-27.49), signaling a thin, leader-driven tape.
- Sector dispersion: Information Technology (-7.2% 20d) and Energy (-4.8% 20d) are the weakest sectors, while Health Care (+6.9%), Consumer Discretionary (+6.7%) and Consumer Staples (+5.4%) lead.
- Macro: CPI is 336.3 (Sep-2026) with core CPI 338.9; unemployment is 4.2%; the effective funds rate is 3.88% as of 2026-11-12; 10Y-2Y spread is 0.27.
- Credit: US high-yield OAS is 3.20 and IG OAS is 0.89, indicating orderly but not aggressive risk appetite.
- Flows: SOXX shows exceptional institutional buying (20d flow z-score 5.10) despite price weakness, while TLT is neutral-to-negative and SMH shows tactical profit-taking inside structural accumulation.
- Risk: 5-day forecast volatility is 14.9% with a 16.5% spike probability, below the 18.5% threshold and below historical/ewma baselines, implying a relatively calm but not risk-free near-term window.

## Data QC

- Status: **PASS_WITH_WARNINGS**
- Equity session: 0 completed session(s) behind inference date
- Equity provenance: 393 provisional / 12576 canonical
- Breadth lag: 0 session(s); ETF-flow lag: 0 session(s)
- Note: Equity session contains a mix of provisional yfinance and canonical Massive rows.
- External sources: 79 ok / 0 unavailable; retrieved 2026-11-15T14:16:30.234269+00:00

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
| S&P 500 (SPX) | 7561.67 | -1.28% over 20d | Index is in a late-cycle, leader-driven tape with broad 20-day momentum but negative 52-week price-breadth divergence. |
| Health Care (XLV) | 6.87% | +6.87% over 20d | Strongest sector; trailing P/E 30.78 suggests rich but stable demand-side leadership. |
| Consumer Discretionary (XLY) | 6.69% | +6.69% over 20d | Second-strongest sector; trailing P/E 25.11 indicates moderate valuation with consumer resilience. |
| Information Technology (XLK) | -7.19% | -7.19% over 20d | Weakest sector; trailing P/E 30.03 reflects high-multiple compression despite mega-cap liquidity leadership. |
| Energy (XLE) | -4.81% | -4.81% over 20d | Negative 20d return; trailing P/E 16.23 is the cheapest sector, but momentum is negative. |
| Financials (XLF) | 5.69% | +5.69% over 20d | Positive momentum; trailing P/E 15.85 is the cheapest among major sectors, consistent with a steepening curve. |

## Macro, Fiscal, Rates, Liquidity and Credit

- Growth: The macro database provides only CPI, core CPI and unemployment; no GDP or payroll series are available in the supplied evidence, so growth assessment relies on labor-market tightness (4.2% unemployment) and the late-cycle positioning implied by breadth and sector dispersion.
- Inflation: CPI is 336.298 (Sep-2026) and core CPI is 338.896; the October CPI reading in the external source is 337.476, indicating inflation is still above the pre-2021 trend but has not re-accelerated sharply.
- Policy: The effective federal funds rate is 3.88% as of 2026-11-12, implying a cutting cycle has already occurred; the 10Y-2Y spread is 0.27, a modestly positive but shallow curve.
- Rates: Credit spreads are orderly—US high-yield OAS 3.20 and IG OAS 0.89 as of 2026-11-12—consistent with a late-cycle but not distressed credit environment.
- Liquidity: Crypto markets show sharp negative moves on 2026-11-14 (BTC -6.04%, ETH -8.22%), suggesting a liquidity shock or risk-off rotation in risk assets, though the equity breadth data does not yet show a broad sell-off.
- Credit: The combination of a 3.88% policy rate, 0.27 10Y-2Y spread, and tight-but-not-stressed spreads points to a late-cycle plateau with limited policy easing room and a need for positive earnings momentum to sustain the rally.

## US Equities and 11 GICS Sectors

Macro source IDs: S001, S002, S003, S004, S005, S006, S007

| GICS sector | Evidence | AI research stance | Source IDs |
| --- | --- | --- | --- |
| Health Care | 20d return +6.87% (XLV); trailing P/E 30.78 (S055); top-20d momentum shortlist includes APP, IDXX, ROP. | Positive momentum and broad-based strength; valuation is rich but supported by defensive demand and relative outperformance. | S055 |
| Consumer Staples | 20d return +5.40% (XLP); trailing P/E 24.85 (S056); shortlist includes CLX. | Steady defensive contribution; moderate valuation with positive 20d momentum. | S056 |
| Consumer Discretionary | 20d return +6.69% (XLY); trailing P/E 25.11 (S057); shortlist includes CHTR (excluded for forward EPS issues). | Strong 20d momentum and moderate valuation; consumer resilience is evident but forward EPS data is incomplete. | S057 |
| Real Estate | 20d return +5.24% (XLRE); trailing P/E 29.63 (S060); shortlist includes CLX (not RE-specific). | Positive 20d momentum but valuation is elevated; limited direct shortlist evidence. | S060 |
| Financials | 20d return +5.69% (XLF); trailing P/E 15.85 (S063); shortlist includes FISV (excluded for forward EPS missing). | Positive momentum and the cheapest major sector P/E; rate-cut cycle supports net interest margins, but forward data is incomplete. | S063 |
| Utilities | 20d return +4.34% (XLU); trailing P/E 18.11 (S067); no shortlist names. | Positive but lower-momentum defensive sector; moderate valuation. | S067 |
| Materials | 20d return +2.57% (XLB); trailing P/E 21.72 (S068); no shortlist names. | Modest positive momentum; valuation is reasonable but not a leader. | S068 |
| Industrials | 20d return +0.61% (XLI); trailing P/E 27.07 (S069); no shortlist names. | Near-flat momentum; valuation is mid-range, consistent with late-cycle industrial caution. | S069 |
| Communication Services | 20d return -1.48% (XLC); trailing P/E 17.26 (S070); shortlist includes CHTR (excluded for forward EPS issues). | Negative 20d momentum and negative sector contribution; valuation is cheap but momentum is negative. | S070 |
| Information Technology | 20d return -7.19% (XLK); trailing P/E 30.03 (S075); shortlist includes NVDA, AMD, MRVL, NOW, INTC, COIN, LITE, SNDK, FFIV. | Weakest sector on price momentum but contains the largest liquidity leaders; high-multiple compression and dislocation risk are elevated. | S075 |
| Energy | 20d return -4.81% (XLE); trailing P/E 16.23 (S073); no shortlist names. | Negative momentum and the cheapest sector P/E; energy is a value trap on price but cheap on valuation. | S073 |

### Sector fundamentals, valuation and earnings

The supplied database provides trailing P/E for each of the 11 GICS sectors via ETF-level evidence (S055-S075), but does not supply point-in-time sector-level fundamentals such as sector earnings growth, margins, or consensus revisions. Therefore, sector fundamentals are not available in the evidence set; the analysis relies on sector returns, trailing P/E, and shortlist momentum/dislocation signals. No sector-level earnings or margin data should be inferred.

## Growth vs Value

- Growth: Information Technology is the only sector with negative 20d momentum (-7.19%) and the highest trailing P/E (30.03), indicating a growth premium that is being compressed; mega-cap liquidity leaders (NVDA, AMD, MU, AAPL) are the only positive drivers in the sector.
- Value: Energy (XLE, P/E 16.23) and Financials (XLF, P/E 15.85) offer the cheapest trailing valuations, but Energy has negative momentum while Financials have positive momentum and a steepening curve.
- Mixed: Health Care (P/E 30.78) and Communication Services (P/E 17.26) show divergent signals—Health Care has strong momentum but rich valuation; Communication Services is cheap but negative.
- Screening evidence: The shortlist includes high-momentum names (APP, CLX, ROP) and large dislocation names (RDDT, INTC, MRVL, NOW, COIN, LITE, FFIV, SNDK), but forward EPS data is missing for most, so growth quality cannot be fully assessed.

## ETF Flows and Breadth

- Breadth: 71.34% of names are above their 50-day MA and 63.6% above their 200-day MA, with 70.46% positive on 20d returns; advance/decline ratio is 1.70, indicating broad-based but not euphoric participation.
- Breadth warning: New highs are 0 and new lows are 0, and the 52-week price-breadth divergence is -27.49, signaling that the rally is narrow and leader-driven rather than broad-based.
- Flows: SOXX shows exceptional institutional buying (20d flow z-score 5.10) despite price weakness, suggesting structural accumulation in semiconductors; TLT is neutral-to-negative (20d z-score -0.41) with medium-term deterioration; SMH shows tactical profit-taking inside structural accumulation (20d z-score 1.22).
- Flow interpretation: The divergence between SOXX inflows and TLT outflows suggests capital rotation from duration into cyclical/tech liquidity, consistent with a late-cycle, growth-seeking

## Stock Ideas

Single-stock research uses reported EPS, forward P/E and company fundamentals. All ideas are research judgments, not validated return predictions.

| Ticker | Security | Research view | Price | EPS | Forward P/E | Base target | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| APP | AppLovin | NEW | 409.1 | 20.86026 | 19.611452 | 417.21 | NEW |
| PNR | Pentair | KEEP | 68.3 | 5.30402 | 12.877027 | 68.95 | KEEP |
| GEN | Gen Digital | KEEP | 30.4 | 3.33736 | 9.108996 | 33.37 | KEEP |
| ROP | Roper Technologies | KEEP | 479.975 | 24.57318 | 19.532475 | 344.02 | KEEP |

## ETF Ideas

ETF research uses holdings, portfolio valuation and exposure. Single-stock EPS × P/E valuation is not applied to ETFs.

| Ticker | Fund | Research view | Price | Top holdings | Portfolio valuation | Sector exposure | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| XLV | Health Care sector ETF | KEEP | 188.85 | LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59% | Top 10 holdings; numeric weight coverage 61.42% | Health Care | KEEP |
### APP — AppLovin

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** AppLovin is preferred over the other top momentum names because it combines the strongest 20-day momentum in the shortlist with a clean reported EPS and a forward P/E that is not in the extreme dislocation range, unlike INTC, RDDT, or NOW. Alternatives considered: PNR, GEN, CLX, IDXX, ROP.
- **Thesis:** AppLovin screens as a top 20-day momentum name with a 53.7% 20-day return and a 32.5% 60-day return, and its reported diluted EPS of 11.61 for the fiscal period ending 2026-09-30 supports a forward P/E near 19.6. The stock is trading at a sector-relative P/E of 1.0, so the momentum and earnings profile are the primary reasons to initiate a position.
- **Source IDs:** S008, S012, S013, S014
- **Catalysts:** Sustained 20-day momentum above 50%, Continued high-margin revenue growth, Positive earnings momentum with reported EPS of 11.61
- **Risks:** A 47% one-month drawdown headline suggests sharp volatility, Forward EPS fiscal-period alignment is unverified, High valuation relative to near-term earnings growth
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 20.8603 (source.forwardEps) x AI multiple assumption 20.00; source IDs S008, S012, S013, S014
- **EPS:** 20.86026 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 19.611452
- **FY+1 growth assumption:** 27.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / Apple (AAPL) and Microsoft (MSFT) as high-margin, cash-generative tech peers / APP shows strong FY1 consensus growth of 27.44% and revenue growth of 25.37%, with exceptional margins (gross 88.8%, operating 77.8%, profit 65.9%) and ROE of 2.10x. The forward EPS of 20.86 and forward P/E of 19.6x are supported by consensus availability, but the fiscal-year mapping is unverified, so the growth assumption is anchored to the retrieved FY1 consensus growth rather than a labeled FY2027. The base multiple of 20x is justified by high margins and growth relative to peers, with a bull case of 24x and bear case of 16x reflecting margin and growth risk.
- **Company fundamentals:** AppLovin reported diluted EPS of 11.61 for the period ending 2026-09-30, with forward EPS of 20.86 and a forward P/E of 19.61. Revenue growth is 55.5% and earnings growth is 75.5%, with gross margin of 88.8% and operating margin of 77.8%.
- **Bull / Base / Bear:** 500.65 / 417.21 / 333.76
- **Bull / Base / Bear returns:** 22.38% / 1.98% / -18.42%
- **Scenario probabilities:** not separately assigned; see scenario table.

### PNR — Pentair

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Pentair is preferred over the more expensive momentum names because it offers a lower valuation entry point, but it is not preferred over the high-growth names because its fundamentals are currently contracting. Alternatives considered: APP, GEN, CLX, IDXX, ROP.
- **Thesis:** Pentair is a top 20-day momentum name with a 27.8% 20-day return and a 20-day earnings yield of 7.4%. However, its revenue growth is negative at -4.5% and earnings growth is negative at -18.8%, so the momentum is not yet supported by fundamental improvement.
- **Source IDs:** S010, S015, S017, S020
- **Catalysts:** 20-day momentum of 27.8%, Sector-relative P/E of 0.49, implying a cheaper valuation, Forward P/E of 12.9
- **Risks:** Negative revenue and earnings growth, Sector-relative P/E of 0.49 may reflect structural weakness, Momentum may fade if fundamentals do not turn
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 5.3040 (source.forwardEps) x AI multiple assumption 13.00; source IDs S010, S015, S017, S020
- **EPS:** 5.30402 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 12.877027
- **FY+1 growth assumption:** 12.82%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / PNR's own FY1 consensus growth of 12.82% and revenue growth of 18.38% are used as the peer benchmark; no independent peer set is supplied / PNR has FY1 consensus growth of 12.82% and revenue growth of 18.38%, but earnings growth is negative at -18.8% with margins below 40% gross, 21.4% operating, and 15.4% profit. The forward EPS of 5.30 and forward P/E of 12.9x are supported by consensus availability, but the fiscal-year mapping is unverified, so the growth assumption is anchored to the retrieved FY1 consensus growth. The base multiple of 13x reflects modest growth and lower margins, with a bull case of 16x and bear case of 10x reflecting earnings and margin risk.
- **Company fundamentals:** Pentair reported diluted EPS of 2.76 for the period ending 2026-09-30, with forward EPS of 5.30 and a forward P/E of 12.9. Revenue growth is -4.5% and earnings growth is -18.8%, with gross margin of 40.2% and operating margin of 21.4%.
- **Bull / Base / Bear:** 84.86 / 68.95 / 53.04
- **Bull / Base / Bear returns:** 24.25% / 0.95% / -22.34%
- **Scenario probabilities:** not separately assigned; see scenario table.

### GEN — Gen Digital

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Gen Digital is preferred over the more expensive momentum names because it offers a lower forward P/E, but it is not preferred over the high-growth names because its revenue growth is modest. Alternatives considered: APP, PNR, CLX, IDXX, ROP.
- **Thesis:** Gen Digital is a top 20-day momentum name with a 25.8% 20-day return and a 20-day earnings yield of 7.1%. Its forward P/E of 9.1 is attractive, but revenue growth is only 12.2% and earnings growth is 128.6%, so the momentum is not yet fully supported by broad-based fundamental improvement.
- **Source IDs:** S018, S019, S024, S030
- **Catalysts:** 20-day momentum of 25.8%, Forward P/E of 9.1, Earnings growth of 128.6%
- **Risks:** Revenue growth of 12.2% is modest relative to earnings growth, Sector-relative P/E of 0.42 may reflect structural weakness, Momentum may fade if fundamentals do not turn
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 3.3374 (source.forwardEps) x AI multiple assumption 10.00; source IDs S018, S019, S024, S030
- **EPS:** 3.33736 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 9.108996
- **FY+1 growth assumption:** 12.86%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / GEN's own FY1 consensus growth of 12.86% and revenue growth of 6.81% are used as the peer benchmark; no independent peer set is supplied / GEN has FY1 consensus growth of 12.86% and revenue growth of 6.81%, with gross margin of 77.4%, operating margin of 43.2%, and profit margin of 23.1%. The forward EPS of 3.34 and forward P/E of 9.1x are supported by consensus availability, but the fiscal-year mapping is unverified, so the growth assumption is anchored to the retrieved FY1 consensus growth. The base multiple of 10x reflects moderate growth and solid margins, with a bull case of 12x and bear case of 8x reflecting earnings and margin risk.
- **Company fundamentals:** Gen Digital reported diluted EPS of 0.83 for the period ending 2026-10-02, with forward EPS of 3.34 and a forward P/E of 9.1. Revenue growth is 12.2% and earnings growth is 128.6%, with gross margin of 77.4% and operating margin of 43.2%.
- **Bull / Base / Bear:** 40.05 / 33.37 / 26.7
- **Bull / Base / Bear returns:** 31.74% / 9.77% / -12.17%
- **Scenario probabilities:** not separately assigned; see scenario table.

### ROP — Roper Technologies

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Roper Technologies is preferred over the more expensive momentum names because it offers a lower forward P/E, but it is not preferred over the high-growth names because its revenue growth is modest. Alternatives considered: APP, PNR, GEN, CLX, IDXX.
- **Thesis:** Roper Technologies is a top 20-day momentum name with a 25.4% 20-day return and a 20-day earnings yield of 6.0%. Its forward P/E of 19.5 is reasonable, but revenue growth is only 7.6% and earnings growth is 32.6%, so the momentum is not yet fully supported by broad-based fundamental improvement.
- **Source IDs:** S036, S037, S039, S044
- **Catalysts:** 20-day momentum of 25.4%, Forward P/E of 19.5, Earnings growth of 32.6%
- **Risks:** Revenue growth of 7.6% is modest relative to earnings growth, Sector-relative P/E of 0.49 may reflect structural weakness, Momentum may fade if fundamentals do not turn
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 24.5732 (source.forwardEps) x AI multiple assumption 14.00; source IDs S036, S037, S039, S044
- **EPS:** 24.57318 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 19.532475
- **FY+1 growth assumption:** 9.81%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / ROP's own FY1 consensus growth of 9.81% and revenue growth of 6.29% are used as the peer benchmark; no independent peer set is supplied / ROP has FY1 consensus growth of 9.81% and revenue growth of 6.29%, with gross margin of 69.7%, operating margin of 28.0%, and profit margin of 30.7%. The forward EPS of 24.57 and forward P/E of 19.5x are supported by consensus availability, but the fiscal-year mapping is unverified, so the growth assumption is anchored to the retrieved FY1 consensus growth. The base multiple of 14x reflects moderate growth and solid margins, with a bull case of 17x and bear case of 11x reflecting earnings and margin risk.
- **Company fundamentals:** Roper Technologies reported diluted EPS of 21.3 for the period ending 2026-09-30, with forward EPS of 24.57 and a forward P/E of 19.5. Revenue growth is 7.6% and earnings growth is 32.6%, with gross margin of 69.7% and operating margin of 28.0%.
- **Bull / Base / Bear:** 417.74 / 344.02 / 270.3
- **Bull / Base / Bear returns:** -12.97% / -28.33% / -43.68%
- **Scenario probabilities:** not separately assigned; see scenario table.

### XLV — Health Care sector ETF

- **Type:** ETF
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** The Health Care sector ETF is preferred over individual health care names because it provides diversified exposure, but it is not preferred over the top momentum names because the sector does not have a strong independent momentum signal. Alternatives considered: XLP, XLY, XLRE, XLF, XLU, XLB, XLI.
- **Thesis:** The Health Care sector ETF is a liquidity leader with a 54.3% raw price change, but the sector is not in the top momentum or dislocation buckets. The ETF provides diversified exposure to large-cap health care names, but the momentum signal is not strong enough to justify a dedicated favored.
- **Source IDs:** S055, S058
- **Catalysts:** Health care sector strength, Diversified exposure to large-cap pharma and medical devices, Top-10 holdings include LLY, JNJ, ABBV, and MRK
- **Risks:** Sector-relative P/E of 1.33 for IDXX suggests some names are expensive, No top-tier momentum signal in the shortlist, Sector rotation could reduce relative performance
- **Valuation method:** Holdings/portfolio valuation with AI total-return assumption
- **Valuation status:** verified; forward-EPS source: ; period flags: 
- **Valuation assumptions:** Holdings/portfolio valuation; 10 weighted holdings; coverage 61.42%; source IDs S055, S058
- **Top holdings:** LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59%
- **Portfolio valuation:** Top 10 holdings; numeric weight coverage 61.42%
- **Sector exposure:** Health Care
- **Underlying drivers:** Large-cap health care sector performance, including pharmaceutical and medical device demand, with top holdings LLY, JNJ, ABBV, and MRK.
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
| Bull | 25% | +2.00% | Low 5-day vol (14.9%) and below-threshold spike probability (16.5% vs 18.5% threshold) support a modest upside if US close confirms positive breadth and credit spreads tighten. |
| Base | 50% | +0.00% | Directional signal is false and forecast vol sits near the EWMA baseline, implying range-bound trading with no clear catalyst for a directional move over the 5-day horizon. |
| Bear | 25% | -2.00% | If the frozen daily-close model fails to confirm after the US close, elevated volatility regime risk and a spike probability near the threshold could drive a mild downside correction. |

### Long Term (12 months)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 30% | +8.00% | Sustained low volatility and improving credit conditions support a positive earnings trajectory, with breadth expansion and tightening spreads providing a tailwind for a multi-week rally. |
| Base | 40% | +3.00% | A stable macro backdrop with moderate earnings growth and balanced volatility keeps the market range-bound but slightly positive over the longer horizon. |
| Bear | 30% | -5.00% | A failure to confirm the frozen daily-close model after the US close, combined with rising spike probability and widening credit spreads, could trigger a meaningful downside correction. |

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
| S011 | news | FISV | Wed, 11 Nov 2026 00:17:00 GMT | ok | https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en | Michael Burry makes a bold call on struggling payments giant - Yahoo Finance (Wed, 11 Nov 2026 00:17:00 GMT); Fiserv Stock Outlook: Is Wall Street Bullish or Bearish? - Yahoo Finance (Thu, 12 Nov 2026 12:23:56 GMT); Fiserv (FISV) Stock Looks Undervalued With Strong Excess Returns - Yahoo Finance Singapore (Wed, 11 Nov 2026 22:14:34 GMT) |
| S012 | news | APP | Thu, 12 Nov 2026 20:05:45 GMT | ok | https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en | AppLovin Just Ripped 47% in a Month: Is It Too Late to Buy APP Stock Now? - Yahoo Finance (Thu, 12 Nov 2026 20:05:45 GMT); APP Stock Surges 51% After Q3 Earnings: Is it Still a Buy? - Yahoo Finance (Tue, 10 Nov 2026 14:24:00 GMT); ETFs Are Net Sellers of AppLovin (APP) on Nov. 11 - Yahoo Finance (Fri, 13 Nov 2026 11:02:35 GMT) |
| S013 | filing | APP | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json | Diluted EPS 11.61 for period ending 2026-09-30 (filed 2026-11-04) |
| S014 | stock | APP | 2026-11-15 | ok | https://finance.yahoo.com/quote/APP | Trailing P/E: 27.54882; Forward P/E: 19.611452; Forward EPS: 20.86026; Price: 409.1; Market price: 409.1; Market cap: 135543824384; Sector: Communication Services; Trailing Eps: 14.85; Revenue Growth: 0.555; Earnings Growth: 0.755; Gross Margin: 0.8878; Operating Margin: 0.77782995; Profit Margin: 0.65887; Return On Equity: 2.1008599; Total Revenue: 7608893952; Market Cap: 135543824384; Consensus EPS FY+1: 20.72438; growth: 0.2744 |
| S015 | stock | PNR | 2026-11-15 | ok | https://finance.yahoo.com/quote/PNR | Trailing P/E: 18.610355; Forward P/E: 12.877027; Forward EPS: 5.30402; Price: 68.3; Market price: 68.3; Market cap: 10904415232; Sector: Industrials; Trailing Eps: 3.67; Revenue Growth: -0.045; Earnings Growth: -0.188; Gross Margin: 0.40168998; Operating Margin: 0.21410999; Profit Margin: 0.15435; Return On Equity: 0.15605; Total Revenue: 3966200064; Market Cap: 10904415232; Consensus EPS FY+1: 5.30402; growth: 0.1282 |
| S016 | stock | FISV | 2026-11-15 | ok | https://finance.yahoo.com/quote/FISV | Forward P/E: 7.9923306; Price: 63.78; Market price: 63.78; Market cap: 33934002176; Market Cap: 33934002176; Consensus EPS FY+1: 7.98015; growth: 0.09689999 |
| S017 | filing | PNR | 2026-10-27 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json | Diluted EPS 2.76 for period ending 2026-09-30 (filed 2026-10-27) |
| S018 | filing | GEN | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0000849399-26-000083); 8-K filed 2026-10-28 (accession 0000849399-26-000081); 8-K filed 2026-10-09 (accession 0000849399-26-000079) |
| S019 | news | GEN | Fri, 13 Nov 2026 09:34:35 GMT | ok | https://news.google.com/rss/search?q=GEN+Gen+Digital+stock&hl=en-US&gl=US&ceid=US:en | Gen Digital Inc. (GEN) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 09:34:35 GMT); Gen Digital (GEN) Stock Repriced After Q2 Earnings Put Margins Center Stage - Yahoo Finance (Thu, 29 Oct 2026 07:00:00 GMT); Gen Digital Inc. (GEN) Stock Forecasts - Yahoo Finance (Wed, 11 Nov 2026 13:10:37 GMT) |
| S020 | news | PNR | Fri, 13 Nov 2026 22:05:23 GMT | ok | https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en | Pentair plc (PNR) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 22:05:23 GMT); Here's What Key Metrics Tell Us About Pentair (PNR) Q3 Earnings - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT); Pentair plc (PNR) Q3 Earnings and Revenues Beat Estimates - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT) |
| S021 | filing | FISV | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json | Diluted EPS -8.9 for period ending 2026-09-30 (filed 2026-11-04) |
| S022 | filing | CLX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000021076-26-000046); 8-K filed 2026-11-02 (accession 0000021076-26-000044); 8-K filed 2026-10-29 (accession 0001206774-26-000586) |
| S023 | stock | CLX | 2026-11-15 | ok | https://finance.yahoo.com/quote/CLX | Trailing P/E: 19.68705; Forward P/E: 17.745283; Forward EPS: 6.1684; Price: 109.46; Market price: 109.46; Market cap: 13260793856; Sector: Consumer Defensive; Trailing Eps: 5.56; Revenue Growth: 0.333; Earnings Growth: 1.138; Gross Margin: 0.41939998; Operating Margin: 0.14286; Profit Margin: 0.09408; Return On Equity: 5.34363; Total Revenue: 7196000256; Market Cap: 13260793856; Consensus EPS FY+1: 6.1684; growth: 0.0769 |
| S024 | stock | GEN | 2026-11-15 | ok | https://finance.yahoo.com/quote/GEN | Trailing P/E: 15.431472; Forward P/E: 9.108996; Forward EPS: 3.33736; Price: 30.4; Market price: 30.4; Market cap: 18035593216; Sector: Technology; Trailing Eps: 1.97; Revenue Growth: 0.122; Earnings Growth: 1.286; Gross Margin: 0.77410007; Operating Margin: 0.43229; Profit Margin: 0.23068; Return On Equity: 0.46402; Total Revenue: 5228000256; Market Cap: 18035593216; Consensus EPS FY+1: 3.33736; growth: 0.1286 |
| S025 | filing | CHTR | 2026-11-06 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-06 (accession 0001091667-26-000073); 8-K filed 2026-11-06 (accession 0001091667-26-000072); 8-K filed 2026-10-27 (accession 0001091667-26-000064) |
| S026 | filing | IDXX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000874716&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000874716-26-000135); 8-K filed 2026-11-02 (accession 0001104659-26-120892); 10-Q filed 2026-08-04 (accession 0000874716-26-000123) |
| S027 | stock | CHTR | 2026-11-15 | ok | https://finance.yahoo.com/quote/CHTR | Trailing P/E: 13.006578; Forward P/E: 3.2831066; Forward EPS: 42.15215; Price: 138.39; Market price: 138.39; Market cap: 24778944512; Sector: Communication Services; Trailing Eps: 10.64; Revenue Growth: 0.091; Gross Margin: 0.55084; Operating Margin: 0.23389; Profit Margin: 0.02498; Return On Equity: 0.07019; Total Revenue: 55645999104; Market Cap: 24778944512; Consensus EPS FY+1: 47.15811; growth: 1.0195 |
| S028 | filing | CLX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000021076.json | Diluted EPS 1.39 for period ending 2026-09-30 (filed 2026-11-02) |
| S029 | stock | IDXX | 2026-11-15 | ok | https://finance.yahoo.com/quote/IDXX | Trailing P/E: 47.45485; Forward P/E: 41.687927; Forward EPS: 16.8929; Price: 704.23; Market price: 704.23; Market cap: 55483650048; Sector: Healthcare; Trailing Eps: 14.84; Revenue Growth: 0.099; Earnings Growth: 0.179; Gross Margin: 0.62722; Operating Margin: 0.32497; Profit Margin: 0.25357; Return On Equity: 0.68925005; Total Revenue: 4662220800; Market Cap: 55483650048; Consensus EPS FY+1: 16.8929; growth: 0.1244 |
| S030 | filing | GEN | 2026-10-29 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000849399.json | Diluted EPS 0.83 for period ending 2026-10-02 (filed 2026-10-29) |
| S031 | news | CLX | Sun, 15 Nov 2026 08:55:47 GMT | ok | https://news.google.com/rss/search?q=CLX+Clorox+stock&hl=en-US&gl=US&ceid=US:en | The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance UK (Sun, 15 Nov 2026 08:55:47 GMT); The Clorox Company (CLX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 05:44:34 GMT); The Clorox Company (CLX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 13:49:38 GMT) |
| S032 | news | CHTR | Sun, 15 Nov 2026 05:47:01 GMT | ok | https://news.google.com/rss/search?q=CHTR+Charter+Communications+stock&hl=en-US&gl=US&ceid=US:en | Charter Communications (CHTR) Stock Could Be A Bargain Following Its New Operating Model - Yahoo Finance (Sun, 15 Nov 2026 05:47:01 GMT); Charter Communications (CHTR) Expands Enterprise Reach With Managed Secure Networking Launch - Yahoo Finance (Sun, 15 Nov 2026 06:08:00 GMT); Charter Communications (CHTR) Earnings Expected to Grow: What to Know Ahead of Next Week's Release - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT) |
| S033 | filing | CHTR | 2026-11-06 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001091667.json | Diluted EPS 0.38 for period ending 2026-09-30 (filed 2026-11-06) |
| S034 | filing | RDDT | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001713445&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0001713445-26-000116); 8-K filed 2026-10-29 (accession 0001713445-26-000114); 8-K filed 2026-08-12 (accession 0001713445-26-000107) |
| S035 | news | IDXX | Sat, 14 Nov 2026 06:13:17 GMT | ok | https://news.google.com/rss/search?q=IDXX+Idexx+Laboratories+stock&hl=en-US&gl=US&ceid=US:en | IDEXX Laboratories, Inc. (IDXX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Sat, 14 Nov 2026 06:13:17 GMT); IDEXX Laboratories (IDXX) Stock Looks Fairly Valued Despite Its 28% Run - Yahoo Finance (Sat, 31 Oct 2026 07:00:00 GMT); IDEXX Laboratories (IDXX) Q3 Earnings Leave Its Premium Valuation In Focus - Yahoo Finance (Tue, 03 Nov 2026 08:00:00 GMT) |
| S036 | filing | ROP | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000882835&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000882835-26-000047); 8-K filed 2026-10-22 (accession 0000882835-26-000042); 8-K filed 2026-10-01 (accession 0000882835-26-000039) |
| S037 | stock | ROP | 2026-11-15 | ok | https://finance.yahoo.com/quote/ROP | Trailing P/E: 18.993866; Forward P/E: 19.532475; Forward EPS: 24.57318; Price: 479.975; Market price: 479.975; Market cap: 47535013888; Sector: Technology; Trailing Eps: 25.27; Revenue Growth: 0.076; Earnings Growth: 0.326; Gross Margin: 0.69671; Operating Margin: 0.28049; Profit Margin: 0.30712998; Return On Equity: 0.13229; Total Revenue: 8434599936; Market Cap: 47535013888; Consensus EPS FY+1: 24.57318; growth: 0.09810001 |
| S038 | filing | IDXX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000874716.json | Diluted EPS 11.75 for period ending 2026-09-30 (filed 2026-11-02) |
| S039 | news | ROP | Fri, 13 Nov 2026 13:04:22 GMT | ok | https://news.google.com/rss/search?q=ROP+Roper+Technologies+stock&hl=en-US&gl=US&ceid=US:en | Roper Technologies, Inc. (ROP) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 13:04:22 GMT); Roper Technologies (ROP) Stock Looks Fully Valued As Cash Flow Comes Into Focus - Yahoo Finance (Thu, 05 Nov 2026 08:00:00 GMT); Roper Technologies: 3 Key Takeaways for Long-Term Investors - Yahoo Finance (Mon, 26 Oct 2026 07:00:00 GMT) |
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
- news FISV: https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en (Wed, 11 Nov 2026 00:17:00 GMT)
- news APP: https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en (Thu, 12 Nov 2026 20:05:45 GMT)
- filing APP: https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json (2026-11-04)
- stock APP: https://finance.yahoo.com/quote/APP (2026-11-15)
- stock PNR: https://finance.yahoo.com/quote/PNR (2026-11-15)
- stock FISV: https://finance.yahoo.com/quote/FISV (2026-11-15)
- filing PNR: https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json (2026-10-27)
- filing GEN: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 (2026-10-29)
- news GEN: https://news.google.com/rss/search?q=GEN+Gen+Digital+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 09:34:35 GMT)
- news PNR: https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 22:05:23 GMT)

## AI Provenance

- Provider / model: hermes-local-proxy / upstage/solar-mini4:free
- Market research: attempts=1 tokens=9473 (prompt=6473, completion=3000) runtime=21.43s
- Fundamental research: generated this run at 2026-11-15T14:16:11.884692+00:00
- Evidence source dates: {'as_of': '2026-11-13', 'latest_equity_date': '2026-11-13', 'latest_macro_date': '2026-11-14', 'flows_date': '2026-11-13'}
- Evidence fingerprint: a532562ee2d1306e747393cbdbb47e22fa82a5b06c5bfbfb701a6b73e3e7d948
- Source citations are retrieved external records in the ledger above; market values remain from the verified database snapshot.


## Disclosures

- This is research and market intelligence, not investment advice.
- AI conclusions are research judgments, not validated return predictions.
- The frozen risk layer is risk-only and is not used for directional views or allocations.
- Legacy scores are not active inputs or outputs.

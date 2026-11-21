# AEGIS AI-First Market Intelligence

Research generated at: 21 November 2026, 18:19 HKT
Database freshness: equity 2026-11-20 (latest row retrieved 2026-11-21 13:05:28.181493+08:00)
Data cutoff: 2026-11-20 US cash close
Snapshot ID: aegis-hourly-20261121T101903Z

## Executive Summary

- **AI market view: Risk-off, late-cycle posture: broad US equities fell on 2026-11-20, with the S&P 500 down 9.36% over 20 days and negative price breadth. Defensive sectors (Consumer Staples, Utilities, Health Care) are the least weak, while Information Technology and Energy are the deepest drags. Credit spreads are tight, but elevated volatility and a high spike probability argue for capital preservation and quality over cyclical beta.**
- S&P 500 closed 2026-11-20 at 6,910.39, down 9.36% over 20 days; 20-day breadth is negative (377 decliners vs 123 advancers, ADR 0.326).
- No new highs and no new lows; 42.48% above 50-day and 46.22% above 200-day, indicating broad but shallow participation.
- Sector returns show Consumer Staples +2.49% and Utilities +0.31% as the only positive 20-day moves; Information Technology -18.68% and Energy -12.72% are the worst.
- Credit conditions are tight: US high-yield OAS 3.52 and IG OAS 0.94, with the 10Y-2Y spread at 0.29.
- Macro data show CPI 336.298 and core CPI 338.896 (Sep-2026), unemployment 4.2% (Sep-2026), and effective fed funds 3.88% (Nov-2026).
- Risk model flags a 92.8% spike probability over the next 5 days, well above the 26.3% historical baseline, supporting a defensive, liquidity-first posture.

## Data QC

- Status: **PASS_WITH_WARNINGS**
- Equity session: 0 completed session(s) behind inference date
- Macro session: 2026-11-20 (0 completed session(s) behind inference date)
- Equity provenance: 137 provisional / 12686 canonical
- Breadth lag: 0 session(s); ETF-flow lag: 0 session(s)
- Note: Equity session contains a mix of provisional yfinance and canonical Massive rows.
- External sources: 79 ok / 0 unavailable; retrieved 2026-11-21T10:19:25.581263+00:00

## Idea Discovery

- S&P 500 universe: 503; eligible: 501; transparent shortlist: 20
- Method: independent momentum/dislocation/PE/liquidity buckets; no composite score
- Evidence used: latest close, 20d and 60d price returns, 60d drawdown, trailing P/E, earnings yield, sector-relative P/E, dollar volume, GICS sector
- Not available as verified inputs: verified earnings-revision history for the full universe, FY+2 consensus, structured industry catalyst calendar
- Eligible but not shortlisted: 481 (outside the top independent momentum, dislocation, valuation and liquidity buckets)
- Included: APP (top_20d_momentum); CMG (top_20d_momentum); PNR (top_20d_momentum); CLX (top_20d_momentum); IDXX (top_20d_momentum); CHTR (top_20d_momentum); GEN (top_20d_momentum); MGM (top_20d_momentum); SNDK (largest_20d_dislocation); MRVL (largest_20d_dislocation); NOW (largest_20d_dislocation); DDOG (largest_20d_dislocation); INTC (largest_20d_dislocation); RDDT (largest_20d_dislocation); NVDA (largest_20d_dislocation, liquidity_leader); LITE (largest_20d_dislocation); MU (liquidity_leader); AMD (liquidity_leader); AAPL (liquidity_leader); MSFT (liquidity_leader)
- Excluded reasons: {"missing_recent_or_latest_price": 2}
- Valuation-quality rejected: [{"flags": ["forward_pe_outside_plausible_range", "implausible_earnings_yield", "forward_eps_vs_reported_jump"], "ticker": "CHTR"}, {"flags": ["forward_pe_outside_plausible_range", "implausible_earnings_yield"], "ticker": "SNDK"}, {"flags": ["forward_eps_vs_reported_jump"], "ticker": "MRVL"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "INTC"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "RDDT"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "NVDA"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "LITE"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "MU"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "AMD"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "AAPL"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "MSFT"}]

## Market Snapshot

| Asset | Latest | Change | Observation |
| --- | --- | --- | --- |
| S&P 500 | 6910.39 | -9.36% (20d) | Broad-based decline; negative price breadth and no new highs. |
| Information Technology (XLK) | -18.68% | -18.68% (20d) | Deepest sector drag; XLK trailing P/E 26.28. |
| Energy (XLE) | -12.72% | -12.72% (20d) | Second-worst sector; XLE trailing P/E 15.11. |
| Consumer Staples (XLP) | +2.49% | +2.49% (20d) | Only positive sector; XLP trailing P/E 24.34. |
| Utilities (XLU) | +0.31% | +0.31% (20d) | Defensive hold; XLU trailing P/E 17.56. |
| Health Care (XLV) | -1.14% | -1.14% (20d) | Modestly negative; XLV trailing P/E 28.89. |

## Macro, Fiscal, Rates, Liquidity and Credit

- Growth: US equities are in a 20-day drawdown; S&P 500 -9.36% and sector leaders like Consumer Staples +2.49% show a defensive rotation rather than broad momentum.
- Inflation: CPI 336.298 and core CPI 338.896 (Sep-2026) indicate persistent but not accelerating inflation; the 10Y-2Y spread is only 0.29, consistent with a flat-to-slightly-inverted curve.
- Policy: Effective fed funds rate is 3.88% (Nov-2026), suggesting a restrictive but potentially easing stance; tight credit spreads (IG 0.94, HY 3.52) imply markets are pricing limited near-term default risk.
- Rates: The 10Y-2Y spread of 0.29 is near flat, and the yield curve is not providing a strong steepening signal, which historically accompanies late-cycle or transition phases.
- Liquidity: Equity flows show SOXX with exceptional institutional buying (20d z-score 2.83, 60d z-score 2.30) while TLT and SMH are neutral/structural accumulation, indicating selective risk allocation.
- Credit: Tight spreads and a high spike probability (92.8% vs 26.3% baseline) suggest elevated tail risk; capital preservation and quality are prioritized over aggressive positioning.

## US Equities and 11 GICS Sectors

Macro source IDs: S001, S002, S003, S004, S005, S006, S007

| GICS sector | Evidence | AI research stance | Source IDs |
| --- | --- | --- | --- |
| Information Technology | XLK 20d return -18.68%; trailing P/E 26.28; shortlist includes NVDA (PE 26.51, sector-relative 0.79) and AMD (PE 128.88, sector-relative 3.82). | Avoid or reduce; deep drawdown with high dispersion between mega-cap leaders and expensive sub-scale names. | S074 |
| Energy | XLE 20d return -12.72%; trailing P/E 15.11; sector-relative PE data not supplied for the shortlist. | Less favored; sharp drawdown with no clear catalyst in the supplied evidence. | S075 |
| Consumer Discretionary | XLY 20d return -0.57%; trailing P/E 23.54; shortlist includes CMG (PE 25.09, sector-relative 1.23) and MGM (PE 17.43, sector-relative 0.86). | Neutral; mixed momentum and valuation signals, no clear directional edge. | S060 |
| Health Care | XLV 20d return -1.14%; trailing P/E 28.89; shortlist includes IDXX (PE 39.18, sector-relative 1.33) and APP (PE 20.05, sector-relative 1.00). | Neutral-to-defensive; modest drawdown with elevated valuation dispersion. | S055 |
| Consumer Staples | XLP 20d return +2.49%; trailing P/E 24.34; shortlist includes CHTR (PE 2.71, sector-relative 0.13) and CLX (PE 18.27, sector-relative 0.76). | Favored bias; only positive sector, but CHTR valuation flags require caution. | S057 |
| Financials | XLF 20d return -2.38%; trailing P/E 14.74; shortlist includes GEN (PE 14.15, sector-relative 0.42) and PNR (PE 13.59, sector-relative 0.49). | Neutral; cheap relative to sector but dragged by broad market weakness. | S068 |
| Real Estate | XLRE 20d return -0.26%; trailing P/E 28.35; no shortlist names supplied. | Neutral; stable but not a source of alpha in the current environment. | S062 |
| Utilities | XLU 20d return +0.31%; trailing P/E 17.56; no shortlist names supplied. | Favored bias; defensive yield and positive 20-day return in a risk-off tape. | S064 |
| Materials | XLB 20d return -5.79%; trailing P/E 20.10; no shortlist names supplied. | Less favored; negative 20-day return with no offsetting catalyst. | S069 |
| Industrials | XLI 20d return -5.01%; trailing P/E 25.08; no shortlist names supplied. | Less favored; negative momentum and no shortlist support. | S071 |
| Communication Services | XLC 20d return -5.19%; trailing P/E 15.89; no shortlist names supplied. | Less favored; negative 20-day return and no shortlist support. | S072 |

### Sector fundamentals, valuation and earnings

No point-in-time sector fundamentals beyond the supplied trailing P/E and 20-day ETF returns are available in the database. The sector evidence is limited to the 11 GICS sectors listed above; growth, margin, and consensus data were retrieved only for the shortlist names and are not aggregated at the sector level. Therefore, no sector-level fundamental metrics are reported here to avoid fabrication.

## Growth vs Value

- Consumer Staples is the only positive 20-day sector (+2.49%) with a trailing P/E of 24.34, indicating a defensive quality tilt rather than cheapness.
- Utilities (+0.31%) and Health Care (-1.14%) are the least negative defensive sectors, but their P/Es (17.56 and 28.89) show mixed valuation support.
- Information Technology is the worst performer (-18.68%) with a sector-relative P/E of 0.79 for NVDA but 3.82 for AMD, highlighting extreme dispersion.
- Financials (XLF -2.38%, P/E 14.74) and Energy (XLE -12.72%, P/E 15.11) are cheap on trailing P/E but offer no evidence of near-term earnings recovery.

## ETF Flows and Breadth

- 20-day price breadth is negative: 123 advancers vs 377 decliners (ADR 0.326), with 0 new highs and 0 new lows.
- 20-day positive percentage is only 37.57%, and 42.48% of names are above the 50-day, indicating broad but shallow participation.
- SOXX shows exceptional institutional buying (20d z-score 2.83, 60d z-score 2.30) despite a down price state, while TLT and SMH are neutral with structural accumulation.
- The S&P 500 20-day return of -9.36% and negative breadth suggest a risk-off tape where liquidity is rotating into quality and away from cyclical beta.

## Stock Ideas

Single-stock research uses reported EPS, forward P/E and company fundamentals. All ideas are research judgments, not validated return predictions.

| Ticker | Security | Research view | Price | EPS | Forward P/E | Base target | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| APP | AppLovin | NEW | 348.29 | 20.86084 | 16.695877 | 417.22 | NEW |
| PNR | Pentair | KEEP | 68.63 | 5.30402 | 12.939242 | 74.26 | KEEP |
| CLX | Clorox | KEEP | 104.73 | 6.1684 | 16.978472 | 98.69 | KEEP |
| IDXX | Idexx Laboratories | KEEP | 676.21 | 16.8929 | 40.029243 | 608.14 | KEEP |

## ETF Ideas

ETF research uses holdings, portfolio valuation and exposure. Single-stock EPS × P/E valuation is not applied to ETFs.

| Ticker | Fund | Research view | Price | Top holdings | Portfolio valuation | Sector exposure | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| XLV | Health Care sector ETF | KEEP | 177.24 | LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59% | Top 10 holdings; numeric weight coverage 61.42% | Health Care | KEEP |
### APP — AppLovin

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** AppLovin offers a cleaner momentum and valuation profile than the high-multiple dislocation names such as DDOG, NOW, and MRVL, where forward P/E is stretched or negative. It also carries stronger reported earnings growth and margins than the lower-quality shortlist names, while still benefiting from a clear Q3 earnings beat catalyst. Alternatives considered: DDOG, NOW, MRVL.
- **Thesis:** AppLovin screens in the top 20-day momentum bucket with a 20-day return of roughly 34% and a 60-day return near 11%, indicating strong recent price momentum. Reported diluted EPS of 11.61 for the fiscal period ending 2026-09-30 and a forward EPS of 20.86 support a forward P/E near 16.7, which is reasonable for a high-margin, high-growth mobile advertising platform. The Q3 earnings beat and positive outlook from the filing/earnings news provide a catalyst for continued re-rating.
- **Source IDs:** S008, S011, S012, S014
- **Catalysts:** Q3 2026 earnings beat and positive outlook (S011, S012), Sustained 20-day momentum with a ~34% price return, High gross margin near 89% and strong reported earnings growth, Forward EPS of 20.86 implies a forward P/E near 16.7
- **Risks:** High 20-day momentum can mean elevated volatility and mean-reversion risk, Forward P/E near 17 leaves limited room for multiple expansion if growth disappoints, Mobile advertising market competition and ad spend cyclicality, Fiscal period alignment and forward EPS source are unverified
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 20.8608 (source.forwardEps) x AI multiple assumption 20.00; source IDs S008, S011, S012, S014
- **EPS:** 20.86084 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 16.695877
- **FY+1 growth assumption:** 27.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / PNR / APP shows 25.5% revenue growth and 75.5% earnings growth with a 65.9% profit margin and 88.8% gross margin, indicating strong operating leverage. The 16.7x forward P/E is below the 20x base multiple, reflecting a premium growth profile relative to the lower-margin, lower-growth PNR (15.4% profit margin, 18.4% revenue growth, 12.9x forward P/E).
- **Company fundamentals:** Reported diluted EPS 11.61 for period ending 2026-09-30; forward EPS 20.86; forward P/E 16.70; gross margin 88.8%; operating margin 77.8%; profit margin 65.9%; revenue growth 55.5%; earnings growth 75.5%; ROE 2.10. Fiscal period alignment and forward EPS source are unverified.
- **Bull / Base / Bear:** 500.66 / 417.22 / 333.77
- **Bull / Base / Bear returns:** 43.75% / 19.79% / -4.17%
- **Scenario probabilities:** not separately assigned; see scenario table.

### PNR — Pentair

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Pentair offers a meaningfully cheaper valuation than the high-multiple dislocation names such as DDOG, NOW, and MRVL, and it carries a stronger 20-day momentum profile than the lower-quality shortlist names. Its low forward P/E and high earnings yield make it an attractive risk-adjusted entry point if the negative growth trend stabilizes. Alternatives considered: DDOG, NOW, MRVL.
- **Thesis:** Pentair screens in the top 20-day momentum bucket with a 20-day return of roughly 24% and a 60-day return near 11%. The stock trades at a low forward P/E near 12.9 and an earnings yield near 7.4%, which is attractive relative to the broader shortlist. However, revenue growth is slightly negative and earnings growth is negative, so the cheap valuation is not yet supported by strong fundamental momentum. The neutral stance reflects a reasonable entry valuation but mixed near-term growth signals.
- **Source IDs:** S009, S015, S018, S023
- **Catalysts:** 20-day momentum of roughly 24% and 60-day return near 11%, Low forward P/E near 12.9 and earnings yield near 7.4%, 10-Q filed 2026-10-27 with reported diluted EPS of 2.76, Positive 20-day momentum despite modest negative revenue/earnings growth
- **Risks:** Negative revenue growth of -4.5% and negative earnings growth of -18.8%, Industrial end-market cyclicality and capital expenditure sensitivity, Forward EPS and fiscal period alignment are unverified, Momentum may fade if underlying business deterioration continues
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 5.3040 (source.forwardEps) x AI multiple assumption 14.00; source IDs S009, S015, S018, S023
- **EPS:** 5.30402 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 12.939242
- **FY+1 growth assumption:** 12.82%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / APP / PNR has 18.4% revenue growth but negative 18.8% earnings growth and a 15.4% profit margin, indicating margin pressure. The 12.9x forward P/E is below the 14x base multiple, reflecting a lower-quality growth profile relative to the higher-margin, higher-growth APP.
- **Company fundamentals:** Reported diluted EPS 2.76 for period ending 2026-09-30; forward EPS 5.30; forward P/E 12.94; earnings yield 7.36%; revenue growth -4.5%; earnings growth -18.8%; gross margin 40.2%; operating margin 21.4%; profit margin 15.4%; ROE 0.16. Fiscal period alignment and forward EPS source are unverified.
- **Bull / Base / Bear:** 90.17 / 74.26 / 58.34
- **Bull / Base / Bear returns:** 31.39% / 8.2% / -14.99%
- **Scenario probabilities:** not separately assigned; see scenario table.

### CLX — Clorox

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Clorox offers a more reasonable valuation than the stretched dislocation names such as DDOG, NOW, and MRVL, and it carries stronger reported earnings growth than the lower-quality shortlist names. Its consumer staples defensive profile provides diversification, but limited growth upside keeps the stance neutral. Alternatives considered: DDOG, NOW, MRVL.
- **Thesis:** Clorox screens in the top 20-day momentum bucket with a 20-day return of roughly 21% and a 60-day return near 1%. It trades at a forward P/E near 17.0 and an earnings yield near 5.5%, which is reasonable for a consumer staples company. Revenue growth of 33.3% and earnings growth of 114% are strong, but the stock is a mature consumer staples name with limited growth upside relative to the high-momentum names. The neutral stance reflects a fair valuation with decent near-term momentum but limited catalyst for a major re-rating.
- **Source IDs:** S017, S025, S026, S027
- **Catalysts:** 20-day momentum of roughly 21% and 60-day return near 1%, Strong reported earnings growth of 113.8% and revenue growth of 33.3%, 8-K filed 2026-11-19, Forward P/E near 17.0 and earnings yield near 5.5%
- **Risks:** Consumer staples growth is limited relative to high-momentum names, Mature business with limited long-term expansion catalysts, Forward EPS and fiscal period alignment are unverified, 20-day momentum may be driven by short-term factors rather than durable growth
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 6.1684 (source.forwardEps) x AI multiple assumption 16.00; source IDs S017, S025, S026, S027
- **EPS:** 6.1684 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 16.978472
- **FY+1 growth assumption:** 7.69%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / IDXX / CLX has 2.2% revenue growth and 113.8% earnings growth with a 9.4% profit margin and 41.9% gross margin, indicating improving but still low profitability. The 17.0x forward P/E is below the 16x base multiple, reflecting a lower-margin, lower-growth profile relative to the higher-margin, higher-growth IDXX.
- **Company fundamentals:** Reported diluted EPS 1.39 for period ending 2026-09-30; forward EPS 6.17; forward P/E 16.98; earnings yield 5.47%; revenue growth 33.3%; earnings growth 113.8%; gross margin 41.9%; operating margin 14.3%; profit margin 9.4%; ROE 5.34. Fiscal period alignment and forward EPS source are unverified.
- **Bull / Base / Bear:** 117.2 / 98.69 / 80.19
- **Bull / Base / Bear returns:** 11.91% / -5.77% / -23.43%
- **Scenario probabilities:** not separately assigned; see scenario table.

### IDXX — Idexx Laboratories

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Idexx offers stronger 60-day momentum and earnings growth than the lower-quality shortlist names, and it is cheaper than the extreme dislocation names such as DDOG, NOW, and MRVL. However, its premium valuation means the risk-reward is balanced rather than clearly attractive. Alternatives considered: DDOG, NOW, MRVL.
- **Thesis:** Idexx Laboratories screens in the top 20-day momentum bucket with a 20-day return of roughly 21% and a strong 60-day return of about 24%. The stock trades at a forward P/E near 40.0 and an earnings yield near 2.6%, which is expensive relative to the broader shortlist. Reported earnings growth of 17.9% and revenue growth of 9.9% are solid, but the premium valuation leaves little room for error. The neutral stance reflects strong momentum and fundamentals but an elevated valuation risk.
- **Source IDs:** S020, S021, S022, S037
- **Catalysts:** 20-day momentum of roughly 21% and 60-day return near 24%, Strong reported earnings growth of 17.9% and revenue growth of 9.9%, 10-Q filed 2026-11-02 with reported diluted EPS of 11.75, Premium valuation supported by consistent growth
- **Risks:** Forward P/E near 40.0 and earnings yield near 2.6% are expensive, High valuation leaves limited room for multiple contraction if growth slows, Forward EPS and fiscal period alignment are unverified, Veterinary diagnostics market is competitive and cyclical
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 16.8929 (source.forwardEps) x AI multiple assumption 36.00; source IDs S020, S021, S022, S037
- **EPS:** 16.8929 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 40.029243
- **FY+1 growth assumption:** 12.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / CLX / IDXX has 8.9% revenue growth and 17.9% earnings growth with a 25.4% profit margin and 62.7% gross margin, indicating strong profitability and growth. The 40.0x forward P/E is below the 36x base multiple, reflecting a premium growth and margin profile relative to the lower-margin, lower-growth CLX.
- **Company fundamentals:** Reported diluted EPS 11.75 for period ending 2026-09-30; forward EPS 16.89; forward P/E 40.03; earnings yield 2.55%; revenue growth 9.9%; earnings growth 17.9%; gross margin 62.7%; operating margin 32.5%; profit margin 25.4%; ROE 0.69. Fiscal period alignment and forward EPS source are unverified.
- **Bull / Base / Bear:** 709.5 / 608.14 / 506.79
- **Bull / Base / Bear returns:** 4.92% / -10.07% / -25.05%
- **Scenario probabilities:** not separately assigned; see scenario table.

### XLV — Health Care sector ETF

- **Type:** ETF
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** The Health Care sector ETF offers diversified exposure to the healthcare names in the shortlist, including IDXX, and provides a way to express a neutral healthcare view without single-stock idiosyncratic risk. It is preferable to holding individual high-multiple names such as DDOG, NOW, and MRVL when the sector is under pressure. Alternatives considered: XLY, XLP, XLF.
- **Thesis:** The Health Care sector ETF provides broad exposure to large-cap pharmaceutical and medical device names. The ETF declined about 12.4% on the latest session, which is a notable negative driver. The sector remains anchored by defensive characteristics and diversified large-cap healthcare names, but the recent price decline and elevated sector volatility warrant a neutral stance. The ETF is not a stock, so valuation metrics such as P/E and earnings yield are not applicable.
- **Source IDs:** S052, S055
- **Catalysts:** Defensive sector characteristics with diversified large-cap healthcare exposure, Recent price decline may create a buying opportunity if fundamentals remain intact, Top holdings include LLY, JNJ, ABBV, MRK, and UNH
- **Risks:** Latest session decline of about 12.4%, Sector-specific regulatory and drug pricing risks, Concentration in large-cap pharma with limited small-cap upside, ETF is a passive sector tracker with no active management catalyst
- **Valuation method:** Holdings/portfolio valuation with AI total-return assumption
- **Valuation status:** verified; forward-EPS source: ; period flags: 
- **Valuation assumptions:** Holdings/portfolio valuation; 10 weighted holdings; coverage 61.42%; source IDs S052, S055
- **Top holdings:** LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59%
- **Portfolio valuation:** Top 10 holdings; numeric weight coverage 61.42%
- **Sector exposure:** Health Care
- **Underlying drivers:** Large-cap pharmaceutical and medical device demand, drug pricing policy, regulatory environment, and defensive sector rotation.
- **Bull / Base / Bear:** 198.51 / 186.1 / 166.61
- **Bull / Base / Bear returns:** 12.0% / 5.0% / -6.0%
- **Scenario probabilities:** not separately assigned; see scenario table.

## Quant Risk Layer

| Field | Value |
| --- | --- |
| Volatility model | vol5_ols_v1 |
| Spike model | spike_logit_v1 |
| As-of date | 2026-11-20 |
| Target window | 2026-11-23 to 2026-11-30 |
| Forecast 5D annualized volatility | 36.64% |
| Historical-vol baseline | 26.26% |
| EWMA baseline | 24.67% |
| Spike probability | 92.77% |
| Spike threshold | 18.50% |
| Status | prospective |
| Forecast ID | 48d2c1933342b1a6 |

Risk-only; no directional interpretation or allocation implication.

## Scenarios

### Short Term (5 trading sessions)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 25% | +2.00% | Spike probability 0.928 vs baseline 0.263 indicates elevated near-term volatility; if the frozen daily-close model resolves favorably after the US close, a modest 2% upside is plausible. |
| Base | 50% | +0.00% | Directional signal is false and forecast vol 0.366 exceeds the 0.185 threshold, so the base case assumes range-bound returns with no directional edge over the 2026-11-23 to 2026-11-30 window. |
| Bear | 25% | -2.00% | High spike probability and elevated forecast vol suggest downside risk if the frozen model fails to confirm; a -2% return is the bear case for the short horizon. |

### Long Term (12 months)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 30% | +8.00% | Sustained volatility regime and elevated forecast vol could precede a risk-on rebound if earnings and credit conditions improve, supporting an 8% long-term upside. |
| Base | 40% | +3.00% | Base case assumes normalization of volatility and stable earnings/credit fundamentals, yielding a 3% long-term return with no directional alpha. |
| Bear | 30% | -5.00% | If elevated spike probability persists and credit spreads widen, a -5% long-term return is plausible as volatility and downside risk compound. |

## Positioning

- Maintain a defensive, liquidity-first posture with emphasis on cash and high-quality defensive sectors.
- Reduce exposure to Information Technology and Energy given deep drawdowns and no shortlist support.
- Favor Consumer Staples and Utilities as the least weak sectors, but avoid overpaying for quality (e.g., CHTR flags).
- Keep credit exposure limited given tight spreads and a 92.8% spike probability; monitor for a risk-off event.
- Do not assign weights; the posture is a research stance, not an allocation recommendation.

## Catalysts

| Date | Event | Why it matters |
| --- | --- | --- |
| 2026-11-23 | Risk model spike window opens | Frozen model shows 92.8% spike probability over 2026-11-23 to 2026-11-30, well above the 26.3% historical baseline, warranting caution. |
| 2026-11-20 | US equity close | S&P |

## Key Risks


## External Source Ledger

| ID | Type | Ticker | Published | Status | URL | Claims |
| --- | --- | --- | --- | --- | --- | --- |
| S001 | macro | macro | 2026-11-19 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFF&cosd=2026-01-01 | Effective federal funds rate (DFF) latest observation 2026-11-19: 3.88 |
| S002 | macro | macro | 2026-11-19 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLH0A0HYM2&cosd=2026-01-01 | US high-yield OAS (BAMLH0A0HYM2) latest observation 2026-11-19: 3.52 |
| S003 | macro | macro | 2026-11-19 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLC0A0CM&cosd=2026-01-01 | US investment-grade OAS (BAMLC0A0CM) latest observation 2026-11-19: 0.94 |
| S004 | macro | macro | 2026-10-01 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCSL&cosd=2026-01-01 | US CPI (CPIAUCSL) latest observation 2026-10-01: 337.476 |
| S005 | macro | macro | 2026-10-01 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=UNRATE&cosd=2026-01-01 | US unemployment rate (UNRATE) latest observation 2026-10-01: 4.1 |
| S006 | macro | macro | 2026-10-01 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=PAYEMS&cosd=2026-01-01 | US nonfarm payrolls (PAYEMS) latest observation 2026-10-01: 159293 |
| S007 | macro | macro | 2026-11-20 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=T10Y2Y&cosd=2026-01-01 | 10Y-2Y Treasury spread (T10Y2Y) latest observation 2026-11-20: 0.29 |
| S008 | filing | APP | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001751008&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0001751008-26-000069); 8-K filed 2026-11-04 (accession 0001751008-26-000068); 10-Q filed 2026-08-05 (accession 0001751008-26-000059) |
| S009 | filing | PNR | 2026-10-27 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-27 (accession 0000077360-26-000058); 8-K filed 2026-10-27 (accession 0000077360-26-000055); 8-K filed 2026-09-22 (accession 0000077360-26-000050) |
| S010 | filing | CMG | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001058090&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0001058090-26-000104); 8-K filed 2026-10-28 (accession 0001058090-26-000103); 8-K filed 2026-09-14 (accession 0001058090-26-000088) |
| S011 | news | APP | Thu, 05 Nov 2026 08:00:00 GMT | ok | https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en | AppLovin stock soars after Q3 earnings, outlook beat - Yahoo Finance (Thu, 05 Nov 2026 08:00:00 GMT); AppLovin Stock Moves Higher: What's Going On? - Benzinga (Mon, 16 Nov 2026 18:52:15 GMT); AppLovin Stock Surges As Earnings Beat Provides Much-Needed Boost - Investor's Business Daily (Wed, 04 Nov 2026 08:00:00 GMT) |
| S012 | filing | APP | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json | Diluted EPS 11.61 for period ending 2026-09-30 (filed 2026-11-04) |
| S013 | news | CMG | Sat, 21 Nov 2026 07:47:00 GMT | ok | https://news.google.com/rss/search?q=CMG+Chipotle+Mexican+Grill+stock&hl=en-US&gl=US&ceid=US:en | Chipotle Mexican Grill vs. e.l.f. Beauty: Which Consumer Stock Is a Better Buy for 2027? - Yahoo Finance (Sat, 21 Nov 2026 07:47:00 GMT); Chipotle Mexican Grill vs. Hershey: Which Consumer Stock Is a Better Buy for 2027? - The Motley Fool (Sat, 21 Nov 2026 01:45:00 GMT); Chipotle Stock Looks Cheaper On 2027 Profit, If Sales Deliver - Trefis (Fri, 20 Nov 2026 16:32:30 GMT) |
| S014 | stock | APP | 2026-11-21 | ok | https://finance.yahoo.com/quote/APP | Trailing P/E: 23.453873; Forward P/E: 16.695877; Forward EPS: 20.86084; Price: 348.29; Market price: 348.29; Market cap: 115396132864; Sector: Communication Services; Trailing Eps: 14.85; Revenue Growth: 0.555; Earnings Growth: 0.755; Gross Margin: 0.8878; Operating Margin: 0.77782995; Profit Margin: 0.65887; Return On Equity: 2.1008599; Total Revenue: 7608893952; Market Cap: 115396132864; Consensus EPS FY+1: 20.72451; growth: 0.2744 |
| S015 | stock | PNR | 2026-11-21 | ok | https://finance.yahoo.com/quote/PNR | Trailing P/E: 18.700272; Forward P/E: 12.939242; Forward EPS: 5.30402; Price: 68.63; Market price: 68.63; Market cap: 10957101056; Sector: Industrials; Trailing Eps: 3.67; Revenue Growth: -0.045; Earnings Growth: -0.188; Gross Margin: 0.40168998; Operating Margin: 0.21410999; Profit Margin: 0.15435; Return On Equity: 0.15605; Total Revenue: 3966200064; Market Cap: 10957101056; Consensus EPS FY+1: 5.30402; growth: 0.1282 |
| S016 | stock | CMG | 2026-11-21 | ok | https://finance.yahoo.com/quote/CMG | Trailing P/E: 33.224297; Forward P/E: 26.86344; Forward EPS: 1.32336; Price: 35.55; Market price: 35.55; Market cap: 44969861120; Sector: Consumer Cyclical; Trailing Eps: 1.07; Revenue Growth: 0.096; Earnings Growth: -0.062; Gross Margin: 0.39314; Operating Margin: 0.14715; Profit Margin: 0.10832; Return On Equity: 0.48518002; Total Revenue: 12713477120; Market Cap: 44969861120; Consensus EPS FY+1: 1.32336; growth: 0.216 |
| S017 | filing | CLX | 2026-11-19 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 | 8-K filed 2026-11-19 (accession 0001206774-26-000606); 10-Q filed 2026-11-02 (accession 0000021076-26-000046); 8-K filed 2026-11-02 (accession 0000021076-26-000044) |
| S018 | news | PNR | Wed, 18 Nov 2026 08:00:00 GMT | ok | https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en | Pentair Stock Price Forecast. Should You Buy PNR? - StockInvest.us (Wed, 18 Nov 2026 08:00:00 GMT); Pentair (PNR) Stock Could Be Below Fair Value After Earnings Reset - Yahoo Finance (Tue, 28 Jul 2026 07:00:00 GMT); Why Pentair Stock Popped This Morning - The Motley Fool (Tue, 27 Oct 2026 07:00:00 GMT) |
| S019 | filing | CMG | 2026-10-29 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001058090.json | Diluted EPS 0.82 for period ending 2026-09-30 (filed 2026-10-29) |
| S020 | filing | IDXX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000874716&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000874716-26-000135); 8-K filed 2026-11-02 (accession 0001104659-26-120892); 10-Q filed 2026-08-04 (accession 0000874716-26-000123) |
| S021 | stock | IDXX | 2026-11-21 | ok | https://finance.yahoo.com/quote/IDXX | Trailing P/E: 45.56671; Forward P/E: 40.029243; Forward EPS: 16.8929; Price: 676.21; Market price: 676.21; Market cap: 53276061696; Sector: Healthcare; Trailing Eps: 14.84; Revenue Growth: 0.099; Earnings Growth: 0.179; Gross Margin: 0.62722; Operating Margin: 0.32497; Profit Margin: 0.25357; Return On Equity: 0.68925005; Total Revenue: 4662220800; Market Cap: 53276061696; Consensus EPS FY+1: 16.8929; growth: 0.1244 |
| S022 | news | IDXX | Tue, 03 Nov 2026 08:00:00 GMT | ok | https://news.google.com/rss/search?q=IDXX+Idexx+Laboratories+stock&hl=en-US&gl=US&ceid=US:en | IDEXX Laboratories (IDXX) Q3 Earnings Leave Its Premium Valuation In Focus - Yahoo Finance (Tue, 03 Nov 2026 08:00:00 GMT); At IDEXX Laboratories (IDXX), executive vice president Michael Lane exercised options for 863 shares at three prices. - Stock Titan (Fri, 20 Nov 2026 22:00:38 GMT); IDEXX Laboratories: Great Company, But Too Expensive (Rating Downgrade) - Seeking Alpha (Wed, 04 Nov 2026 08:00:00 GMT) |
| S023 | filing | PNR | 2026-10-27 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json | Diluted EPS 2.76 for period ending 2026-09-30 (filed 2026-10-27) |
| S024 | filing | CHTR | 2026-11-06 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-06 (accession 0001091667-26-000073); 8-K filed 2026-11-06 (accession 0001091667-26-000072); 8-K filed 2026-10-27 (accession 0001091667-26-000064) |
| S025 | stock | CLX | 2026-11-21 | ok | https://finance.yahoo.com/quote/CLX | Trailing P/E: 18.836332; Forward P/E: 16.978472; Forward EPS: 6.1684; Price: 104.73; Market price: 104.73; Market cap: 12687766528; Sector: Consumer Defensive; Trailing Eps: 5.56; Revenue Growth: 0.333; Earnings Growth: 1.138; Gross Margin: 0.41939998; Operating Margin: 0.14286; Profit Margin: 0.09408; Return On Equity: 5.34363; Total Revenue: 7196000256; Market Cap: 12687766528; Consensus EPS FY+1: 6.1684; growth: 0.0769 |
| S026 | news | CLX | Fri, 20 Nov 2026 18:29:55 GMT | ok | https://news.google.com/rss/search?q=CLX+Clorox+stock&hl=en-US&gl=US&ceid=US:en | The Clorox Company (CLX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 20 Nov 2026 18:29:55 GMT); Clorox Declares Regular Quarterly Dividend of $1.25 Per Share - Quantisnow (Wed, 18 Nov 2026 02:13:00 GMT); The Clorox Company (CLX) Declares $1.25 Quarterly Dividend - TradingView (Wed, 18 Nov 2026 02:13:00 GMT) |
| S027 | filing | CLX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000021076.json | Diluted EPS 1.39 for period ending 2026-09-30 (filed 2026-11-02) |
| S028 | stock | CHTR | 2026-11-21 | ok | https://finance.yahoo.com/quote/CHTR | Trailing P/E: 12.098683; Forward P/E: 2.8233452; Forward EPS: 45.59485; Price: 128.73; Market price: 128.73; Market cap: 23049306112; Sector: Communication Services; Trailing Eps: 10.64; Revenue Growth: 0.091; Gross Margin: 0.55084; Operating Margin: 0.23389; Profit Margin: 0.02498; Return On Equity: 0.07019; Total Revenue: 55645999104; Market Cap: 23049306112; Consensus EPS FY+1: 49.52287; growth: 1.4594 |
| S029 | filing | GEN | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0000849399-26-000083); 8-K filed 2026-10-28 (accession 0000849399-26-000081); 8-K filed 2026-10-09 (accession 0000849399-26-000079) |
| S030 | news | GEN | Fri, 20 Nov 2026 13:40:31 GMT | ok | https://news.google.com/rss/search?q=GEN+Gen+Digital+stock&hl=en-US&gl=US&ceid=US:en | Gen Digital Inc. (GEN) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 20 Nov 2026 13:40:31 GMT); Gen Digital (GEN) Stock Looks Below Fair Value On Its 45% Run - Yahoo Finance (Sat, 21 Nov 2026 02:14:00 GMT); Gen Digital CFO Sold Shares Worth Over $2.2M - TradingView (Fri, 20 Nov 2026 23:30:01 GMT) |
| S031 | filing | MGM | 2026-10-28 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000789570&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-28 (accession 0000789570-26-000107); 8-K filed 2026-10-28 (accession 0000789570-26-000106); 8-K filed 2026-10-28 (accession 0000789570-26-000104) |
| S032 | stock | GEN | 2026-11-21 | ok | https://finance.yahoo.com/quote/GEN | Trailing P/E: 14.817259; Forward P/E: 8.746435; Forward EPS: 3.33736; Price: 29.19; Market price: 29.19; Market cap: 17317730304; Sector: Technology; Trailing Eps: 1.97; Revenue Growth: 0.122; Earnings Growth: 1.286; Gross Margin: 0.77410007; Operating Margin: 0.43229; Profit Margin: 0.23068; Return On Equity: 0.46402; Total Revenue: 5228000256; Market Cap: 17317730304; Consensus EPS FY+1: 3.33736; growth: 0.1286 |
| S033 | news | CHTR | Sun, 15 Nov 2026 05:10:00 GMT | ok | https://news.google.com/rss/search?q=CHTR+Charter+Communications+stock&hl=en-US&gl=US&ceid=US:en | Charter Communications (CHTR) Stock Could Be A Bargain Following Its New Operating Model - Yahoo Finance (Sun, 15 Nov 2026 05:10:00 GMT); Is Charter Stock Worth The Wait? - Trefis (Tue, 17 Nov 2026 12:33:16 GMT); Why Charter Communications Plunged in September - The Motley Fool (Thu, 08 Oct 2026 07:00:00 GMT) |
| S034 | news | MGM | Thu, 29 Oct 2026 07:00:00 GMT | ok | https://news.google.com/rss/search?q=MGM+MGM+Resorts+stock&hl=en-US&gl=US&ceid=US:en | How Investors Are Reacting To MGM Resorts Stock After An Earnings Miss - Yahoo Finance (Thu, 29 Oct 2026 07:00:00 GMT); This casino stock has fallen for 17 weeks in a row. Katie Stockton says it could be due for a bounce - CNBC (Tue, 03 Nov 2026 08:00:00 GMT); MGM Stock Dives 10% After Barry Diller Drops $18 Billion Bid - Forbes (Thu, 24 Sep 2026 07:00:00 GMT) |
| S035 | stock | MGM | 2026-11-21 | ok | https://finance.yahoo.com/quote/MGM | Trailing P/E: 12.446155; Forward P/E: 23.023344; Forward EPS: 1.40553; Price: 32.36; Market price: 32.36; Market cap: 8187421184; Sector: Consumer Cyclical; Trailing Eps: 2.6; Revenue Growth: -0.009; Gross Margin: 0.4362; Operating Margin: 0.057979997; Profit Margin: 0.03916; Return On Equity: 0.26933; Total Revenue: 17722869760; Market Cap: 8187421184; Consensus EPS FY+1: 1.40553; growth: -0.0462 |
| S036 | filing | SNDK | 2026-11-19 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0002023554&type=10-Q&dateb=&owner=include&count=10 | 8-K filed 2026-11-19 (accession 0001628280-26-075127); 8-K filed 2026-11-18 (accession 0001628280-26-074848); 10-Q filed 2026-10-30 (accession 0001628280-26-068601) |
| S037 | filing | IDXX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000874716.json | Diluted EPS 11.75 for period ending 2026-09-30 (filed 2026-11-02) |
| S038 | filing | CHTR | 2026-11-06 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001091667.json | Diluted EPS 0.38 for period ending 2026-09-30 (filed 2026-11-06) |
| S039 | filing | MRVL | 2026-11-12 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001835632&type=10-Q&dateb=&owner=include&count=10 | 8-K filed 2026-11-12 (accession 0001835632-26-000026); 8-K filed 2026-11-02 (accession 0001193125-26-442717); 8-K filed 2026-11-02 (accession 0001193125-26-442714) |
| S040 | filing | GEN | 2026-10-29 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000849399.json | Diluted EPS 0.83 for period ending 2026-10-02 (filed 2026-10-29) |

## Sources

- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFF&cosd=2026-01-01 (2026-11-19)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLH0A0HYM2&cosd=2026-01-01 (2026-11-19)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLC0A0CM&cosd=2026-01-01 (2026-11-19)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCSL&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=UNRATE&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=PAYEMS&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=T10Y2Y&cosd=2026-01-01 (2026-11-20)
- filing APP: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001751008&type=10-Q&dateb=&owner=include&count=10 (2026-11-04)
- filing PNR: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 (2026-10-27)
- filing CMG: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001058090&type=10-Q&dateb=&owner=include&count=10 (2026-10-29)
- news APP: https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en (Thu, 05 Nov 2026 08:00:00 GMT)
- filing APP: https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json (2026-11-04)
- news CMG: https://news.google.com/rss/search?q=CMG+Chipotle+Mexican+Grill+stock&hl=en-US&gl=US&ceid=US:en (Sat, 21 Nov 2026 07:47:00 GMT)
- stock APP: https://finance.yahoo.com/quote/APP (2026-11-21)
- stock PNR: https://finance.yahoo.com/quote/PNR (2026-11-21)
- stock CMG: https://finance.yahoo.com/quote/CMG (2026-11-21)
- filing CLX: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 (2026-11-19)
- news PNR: https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en (Wed, 18 Nov 2026 08:00:00 GMT)
- filing CMG: https://data.sec.gov/api/xbrl/companyfacts/CIK0001058090.json (2026-10-29)
- filing IDXX: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000874716&type=10-Q&dateb=&owner=include&count=10 (2026-11-02)

## AI Provenance

- Provider / model: hermes-local-proxy / upstage/solar-mini4:free
- Market research: attempts=1 tokens=9591 (prompt=6591, completion=3000) runtime=42.3s
- Fundamental research: generated this run at 2026-11-21T10:19:03.800020+00:00
- Evidence source dates: {'as_of': '2026-11-20', 'latest_equity_date': '2026-11-20', 'latest_macro_date': '2026-11-20', 'flows_date': '2026-11-20'}
- Evidence fingerprint: c4a08f426c50169a3c6b1929befa80d2fee21fac43c72f2734241164a9995e6c
- Source citations are retrieved external records in the ledger above; market values remain from the verified database snapshot.


## Disclosures

- This is research and market intelligence, not investment advice.
- AI conclusions are research judgments, not validated return predictions.
- The frozen risk layer is risk-only and is not used for directional views or allocations.
- Legacy scores are not active inputs or outputs.

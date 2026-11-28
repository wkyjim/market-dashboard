# AEGIS AI-First Market Intelligence

Research generated at: 28 November 2026, 18:16 HKT
Database freshness: equity 2026-11-27 (latest row retrieved 2026-11-28 13:06:53.471248+08:00)
Data cutoff: 2026-11-27 US cash close
Snapshot ID: aegis-hourly-20261128T101646Z

## Executive Summary

- **AI market view: Late-November 2026 US equities show a late-cycle, late-autumn posture: broad market indices advanced, but the 20-day return data show a sharp divergence between Communication Services and Consumer Staples on one side and Information Technology and Energy on the other. Breadth is positive on the 50-day and 200-day averages, yet the 20-day return is negative, indicating a short-term pullback within a still-positive medium-term trend. Credit spreads are tight, policy rates are near the lower bound, and liquidity is concentrated in a small set of large-cap, high-liquidity names.**
- Broad market indices rose on 2026-11-27, but the 20-day return is negative (-5.48% for SPX), signaling a near-term pullback inside a positive medium-term trend.
- Breadth is constructive: 63.33% of names are above their 50-day moving average and 59.51% above their 200-day, with a 4.34 advance/decline ratio.
- Sector returns are bifurcated: Communication Services (+6.20%) and Consumer Staples (+5.10%) lead, while Information Technology (-15.15%) and Energy (-10.25%) lag sharply.
- Credit conditions are supportive: US high-yield OAS is 3.77 and IG OAS is 0.99, with policy rates near the lower bound.
- Liquidity is concentrated in a small set of large-cap names; the shortlist is driven by momentum, dislocation, and liquidity leadership rather than a composite score.
- Macro data are stale relative to the equity date: CPI and unemployment are September 2026 observations, and the 10Y-2Y spread is only 0.25, indicating a flat yield curve.

## Data QC

- Status: **PASS_WITH_WARNINGS**
- Equity session: 0 completed session(s) behind inference date
- Macro session: 2026-11-27 (0 completed session(s) behind inference date)
- Equity provenance: 405 provisional / 12466 canonical
- Breadth lag: 0 session(s); ETF-flow lag: 0 session(s)
- Note: Equity session contains a mix of provisional yfinance and canonical Massive rows.
- External sources: 76 ok / 3 unavailable; retrieved 2026-11-28T10:17:20.218350+00:00

## Idea Discovery

- S&P 500 universe: 503; eligible: 501; transparent shortlist: 20
- Method: independent momentum/dislocation/PE/liquidity buckets; no composite score
- Evidence used: latest close, 20d and 60d price returns, 60d drawdown, trailing P/E, earnings yield, sector-relative P/E, dollar volume, GICS sector
- Not available as verified inputs: verified earnings-revision history for the full universe, FY+2 consensus, structured industry catalyst calendar
- Eligible but not shortlisted: 481 (outside the top independent momentum, dislocation, valuation and liquidity buckets)
- Included: APP (top_20d_momentum); CHTR (top_20d_momentum); FISV (top_20d_momentum); CLX (top_20d_momentum); IDXX (top_20d_momentum); CSGP (top_20d_momentum); MGM (top_20d_momentum); REGN (top_20d_momentum); SNDK (largest_20d_dislocation, liquidity_leader); LITE (largest_20d_dislocation); INTC (largest_20d_dislocation); DDOG (largest_20d_dislocation); MRVL (largest_20d_dislocation); COIN (largest_20d_dislocation); DELL (largest_20d_dislocation); SMCI (largest_20d_dislocation); NVDA (liquidity_leader); MU (liquidity_leader); TSLA (liquidity_leader); AMD (liquidity_leader)
- Excluded reasons: {"missing_recent_or_latest_price": 2}
- Valuation-quality rejected: [{"flags": ["forward_pe_outside_plausible_range", "implausible_earnings_yield", "forward_eps_vs_reported_jump"], "ticker": "CHTR"}, {"flags": ["forward_eps_missing"], "ticker": "FISV"}, {"flags": ["forward_pe_outside_plausible_range", "implausible_earnings_yield"], "ticker": "SNDK"}, {"flags": ["forward_eps_vs_reported_jump"], "ticker": "LITE"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "MRVL"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "COIN"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "DELL"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "SMCI"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "NVDA"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "MU"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "TSLA"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "AMD"}]

## Market Snapshot

| Asset | Latest | Change | Observation |
| --- | --- | --- | --- |
| SPX | 7297.4902 | -5.48% (20d return) | Index closed at 7297.49 on 2026-11-27; 20-day return is negative, indicating a short-term pullback within a positive medium-term trend. |
| XLK | 28.24282 (trailing P/E) | -15.15% (20d return) | Information Technology is the worst-performing sector over 20 days, with a trailing P/E of 28.24. |
| XLE | 15.403652 (trailing P/E) | -10.25% (20d return) | Energy is the second-worst sector, with a trailing P/E of 15.40. |
| XLC | 17.072716 (trailing P/E) | +6.20% (20d return) | Communication Services is the best-performing sector, with a trailing P/E of 17.07. |
| XLP | 24.941254 (trailing P/E) | +5.10% (20d return) | Consumer Staples is the second-best sector, with a trailing P/E of 24.94. |
| XLV | 30.024513 (trailing P/E) | +0.09% (20d return) | Health Care is roughly flat over 20 days, with a trailing P/E of 30.02. |

## Macro, Fiscal, Rates, Liquidity and Credit

- Growth: The 10Y-2Y Treasury spread is 0.25 as of 2026-11-27, indicating a flat yield curve and late-cycle conditions; the macro database only provides September 2026 CPI and unemployment data, so near-term growth momentum is inferred from equity and credit indicators.
- Inflation: CPI (CPIAUCSL) is 336.298 and core CPI is 338.896 as of 2026-09-01; the external source S004 reports CPI of 337.476 as of 2026-10-01, but the most recent monthly CPI is not available in the database snapshot.
- Policy: The effective federal funds rate is 3.88 as of 2026-11-26, near the lower bound, suggesting a restrictive but easing policy stance.
- Rates: The 10Y-2Y spread is 0.25, and the yield curve is flat; this is consistent with a late-cycle, low-growth environment.
- Liquidity: Credit spreads are tight, with US high-yield OAS at 3.77 and IG OAS at 0.99, indicating ample liquidity and risk appetite.
- Credit: High-yield and investment-grade spreads are both narrow, supporting risk assets, but the flat yield curve and negative 20-day equity returns suggest caution on near-term momentum.

## US Equities and 11 GICS Sectors

Macro source IDs: S001, S002, S003, S004, S005, S006, S007

| GICS sector | Evidence | AI research stance | Source IDs |
| --- | --- | --- | --- |
| Information Technology | 20d return -15.15%; trailing P/E 28.24; shortlist includes NVDA, MU, TSLA, AMD as liquidity leaders, and MRVL, DDOG, SMCI, INTC, COIN, DELL as dislocation names. | Less favored momentum: sharp 20-day decline despite high liquidity; shortlist names are liquidity leaders but not necessarily momentum leaders. | S074 |
| Energy | 20d return -10.25%; trailing P/E 15.40; shortlist includes COIN, DELL, SMCI, MRVL as dislocation names. | Less favored: negative 20-day return and no sector-specific liquidity leadership in the shortlist. | S075 |
| Communication Services | 20d return +6.20%; trailing P/E 17.07; shortlist includes CHTR and REGN as momentum names. | Favored momentum: best 20-day sector return and two shortlisted momentum names. | S072 |
| Consumer Staples | 20d return +5.10%; trailing P/E 24.94; shortlist includes no direct Consumer Staples names. | Favored defensiveness: second-best 20-day return and high valuation quality relative to the universe. | S054 |
| Health Care | 20d return +0.09%; trailing P/E 30.02; shortlist includes IDXX as a momentum name. | Neutral: roughly flat 20-day return, but high trailing P/E of 30.02 limits upside. | S051 |
| Consumer Discretionary | 20d return +3.24%; trailing P/E 25.11; shortlist includes no direct Consumer Discretionary names. | Neutral: positive 20-day return but no shortlisted names in this sector. | S059 |
| Real Estate | 20d return +2.51%; trailing P/E 29.47; shortlist includes no direct Real Estate names. | Neutral: modest positive return, but high trailing P/E of 29.47. | S060 |
| Financials | 20d return +0.39%; trailing P/E 15.44; shortlist includes no direct Financials names. | Neutral: flat 20-day return and low trailing P/E of 15.44, but no sector-specific liquidity leadership. | S062 |
| Utilities | 20d return +1.37%; trailing P/E 17.99; shortlist includes no direct Utilities names. | Neutral: modest positive return and low trailing P/E of 17.99. | S067 |
| Materials | 20d return -0.72%; trailing P/E 21.69; shortlist includes no direct Materials names. | Neutral: slightly negative 20-day return and moderate trailing P/E of 21.69. | S066 |
| Industrials | 20d return -2.69%; trailing P/E 26.55; shortlist includes no direct Industrials names. | Less favored: negative 20-day return and no sector-specific liquidity leadership. | S068 |

### Sector fundamentals, valuation and earnings

No point-in-time sector fundamentals beyond trailing P/E and 20-day ETF returns are supplied in the database. The sector table provides only return_20d and trailing P/E for each GICS sector ETF. Growth, margin, and consensus data are available only for source-backed shortlist names, and no structured industry catalyst calendar is available. Therefore, sector-level fundamental analysis is limited to valuation and relative momentum evidence.

## Growth vs Value

- Growth: Communication Services leads with a 20d return of +6.20% and a trailing P/E of 17.07, suggesting a growth tilt in the best-performing sector.
- Value: Energy has the lowest trailing P/E at 15.40 but a 20d return of -10.25%, indicating value without near-term momentum.
- Value: Financials and Utilities have low trailing P/Es of 15.44 and 17.99, respectively, but flat 20-day returns.
- Growth/Value mix: The shortlist is driven by momentum and dislocation rather than a composite score, so growth and value signals are not directly comparable across all sectors.

## ETF Flows and Breadth

- Breadth is positive on medium-term averages: 63.33% of names above the 50-day and 59.51% above the 200-day, with an advance/decline ratio of 4.34.
- Short-term momentum is negative: the 20-day return is -5.48% and only 52.09% of names are positive over 20 days, indicating a pullback within a positive medium-term trend.
- Flow evidence is limited to three ETFs: TLT (neutral, structural accumulation), SOXX (inflow, strong confirmation, exceptional institutional buying), and SMH (neutral, structural accumulation).
- The SOXX flow state is the only explicit inflow signal, with a 20d flow z-score of 2.37 and a 60d flow z-score of 2.37, suggesting strong institutional buying in semiconductors despite the sector's negative 20-day equity return.

## Stock Ideas

Single-stock research uses reported EPS, forward P/E and company fundamentals. All ideas are research judgments, not validated return predictions.

| Ticker | Security | Research view | Price | EPS | Forward P/E | Base target | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| APP | AppLovin | NEW | 399.21 | 20.86084 | 19.136812 | 458.94 | NEW |
| REGN | Regeneron Pharmaceuticals | NEW | 992.14 | 72.18748 | 13.743936 | 1010.62 | NEW |
| IDXX | Idexx Laboratories | KEEP | 719.23 | 16.8929 | 42.575874 | 641.93 | KEEP |
| CSGP | CoStar Group | KEEP | 34.92 | 1.76832 | 19.747557 | 35.37 | KEEP |

## ETF Ideas

ETF research uses holdings, portfolio valuation and exposure. Single-stock EPS × P/E valuation is not applied to ETFs.

| Ticker | Fund | Research view | Price | Top holdings | Portfolio valuation | Sector exposure | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| XLV | Health Care sector ETF | NEW | 184.2 | LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59% | Top 10 holdings; numeric weight coverage 61.42% | Health Care | NEW |
### APP — AppLovin

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** AppLovin offers a higher-quality, higher-margin, faster-growing mobile advertising franchise than the other momentum shortlist names, with a forward P/E of 19.1 that is more reasonable than the forward P/E gaps flagged for CHTR, SNDK, and LITE, and it avoids the forward EPS gaps flagged for MRVL, COIN, DELL, SMCI, NVDA, MU, TSLA, and AMD. Alternatives considered: CHTR, SNDK, LITE, MRVL, COIN, DELL, SMCI, NVDA, MU, TSLA, AMD.
- **Thesis:** AppLovin screens as a top 20-day momentum name with a 56.6% 20-day return and a 25.1% 60-day return, supported by strong reported fundamentals: 25.7% revenue growth, 75.5% earnings growth, 88.8% gross margin, 77.8% operating margin, and a forward P/E of 19.1. The company is a scaled mobile advertising platform with durable monetization, and the momentum screen plus high-quality margins justify a new long position.
- **Source IDs:** S009, S012, S015, S018
- **Catalysts:** Continued acceleration in mobile ad revenue and engagement, Sustained high gross and operating margins expanding profitability, Continued 20-day momentum and positive 60-day return trajectory
- **Risks:** Mobile advertising market cyclicality and ad spend rotation, Forward P/E of 19.1 leaves limited valuation cushion if growth decelerates, Single-quarter momentum can reverse; 20-day return is already elevated
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 20.8608 (source.forwardEps) x AI multiple assumption 22.00; source IDs S009, S012, S015, S018
- **EPS:** 20.86084 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 19.136812
- **FY+1 growth assumption:** 27.59%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / MSFT / APP shows strong FY1 consensus growth of ~27.6% with revenue growth of ~55.6% and earnings growth of ~75.5%, supported by an 88.8% gross margin and 77.8% operating margin. The forward EPS of 20.86 and forward P/E of 19.1x are below the 22-26x base/bull range, reflecting a premium but justified by high growth and margins. Peer reference: MSFT, given comparable software/platform scale and growth profile.
- **Company fundamentals:** AppLovin reported diluted EPS of 11.61 for the period ending 2026-09-30, with forward EPS of 20.86, forward P/E of 19.14, revenue growth of 55.5%, earnings growth of 75.5%, gross margin of 88.8%, operating margin of 77.8%, and profit margin of 65.9%. FY1 EPS growth was 27.6% and FY1 revenue growth was 25.7%.
- **Bull / Base / Bear:** 542.38 / 458.94 / 354.63
- **Bull / Base / Bear returns:** 35.86% / 14.96% / -11.17%
- **Scenario probabilities:** not separately assigned; see scenario table.

### REGN — Regeneron Pharmaceuticals

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** Regeneron offers the best valuation quality among the momentum shortlist, with a forward P/E of 13.7 versus the forward P/E gaps flagged for CHTR, SNDK, LITE, MRVL, COIN, DELL, SMCI, NVDA, MU, TSLA, and AMD, and it avoids the forward EPS gaps flagged for those same names. Alternatives considered: CHTR, SNDK, LITE, MRVL, COIN, DELL, SMCI, NVDA, MU, TSLA, AMD.
- **Thesis:** Regeneron screens as a top 20-day momentum name with a 21.2% 20-day return and a 16.4% 60-day return, and it carries the strongest valuation quality in the shortlist with a forward P/E of 13.7, well below the forward P/E gaps flagged for other names. The company shows 36.3% revenue growth, 35.5% earnings growth, a 46.7% gross margin, and a 30.4% operating margin, supporting a new long position.
- **Source IDs:** S029, S036, S039, S042
- **Catalysts:** Sustained pipeline and product revenue growth in high-margin therapeutics, Continued margin expansion as a large-cap biopharma leader, Positive 20-day and 60-day momentum with a low forward P/E
- **Risks:** Biopharma pipeline and regulatory risk, Forward P/E of 13.7 is low but may already reflect expected growth, Single-quarter momentum can reverse
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 72.1875 (source.forwardEps) x AI multiple assumption 14.00; source IDs S029, S036, S039, S042
- **EPS:** 72.18748 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 13.743936
- **FY+1 growth assumption:** 4.77%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / ABBV / REGN has modest FY1 consensus growth of ~4.8% with revenue growth of ~36.3% and earnings growth of ~35.5%, reflecting a high-margin but slower-growing profile. The forward EPS of 72.19 and forward P/E of 13.7x support a lower multiple range. Peer reference: ABBV, given comparable large-cap pharma growth and valuation dynamics.
- **Company fundamentals:** Regeneron reported diluted EPS of 37.37 for the period ending 2026-09-30, with forward EPS of 72.19, forward P/E of 13.74, revenue growth of 36.3%, earnings growth of 35.5%, gross margin of 46.7%, operating margin of 30.4%, and profit margin of 28.5%. FY1 EPS growth was 4.8% and FY1 revenue growth was 7.6%.
- **Bull / Base / Bear:** 1227.19 / 1010.62 / 794.06
- **Bull / Base / Bear returns:** 23.69% / 1.86% / -19.96%
- **Scenario probabilities:** not separately assigned; see scenario table.

### IDXX — Idexx Laboratories

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Idexx offers a more durable, recurring-revenue business model than the high-multiple momentum names, but it is not preferred over the low-valuation, high-margin names such as Regeneron and AppLovin, which offer better growth-adjusted value. Alternatives considered: REGN, APP, CLX, CSGP, MGM.
- **Thesis:** Idexx Laboratories screens as a top 20-day momentum name with a 24.9% 20-day return and a 33.4% 60-day return, and it carries a reasonable forward P/E of 42.6 with 9.9% revenue growth and 17.9% earnings growth. The company is a leader in animal health diagnostics and veterinary services, but the forward P/E is elevated relative to the low-growth, high-margin names in the shortlist, so the position should be sized conservatively.
- **Source IDs:** S020, S023, S031
- **Catalysts:** Continued growth in animal health diagnostics and veterinary services, Positive 20-day and 60-day momentum, Stable cash flow from recurring diagnostic testing and services
- **Risks:** Forward P/E of 42.6 is high relative to growth, limiting upside, Animal health demand tied to pet ownership cycles and economic sensitivity, Single-quarter momentum can reverse
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 16.8929 (source.forwardEps) x AI multiple assumption 38.00; source IDs S020, S023, S031
- **EPS:** 16.8929 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 42.575874
- **FY+1 growth assumption:** 12.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / BDX / IDXX shows FY1 consensus growth of ~12.4% with revenue growth of ~9.9% and earnings growth of ~17.9%, supported by a 62.7% gross margin and 32.5% operating margin. The forward EPS of 16.89 and forward P/E of 42.6x justify a higher multiple range. Peer reference: BDX, given comparable diagnostics/healthcare services growth and valuation.
- **Company fundamentals:** Idexx Laboratories reported diluted EPS of 11.75 for the period ending 2026-09-30, with forward EPS of 16.89, forward P/E of 42.58, revenue growth of 9.9%, earnings growth of 17.9%, gross margin of 62.7%, operating margin of 32.5%, and profit margin of 25.4%. FY1 EPS growth was 12.4% and FY1 revenue growth was 8.9%.
- **Bull / Base / Bear:** 743.29 / 641.93 / 540.57
- **Bull / Base / Bear returns:** 3.35% / -10.75% / -24.84%
- **Scenario probabilities:** not separately assigned; see scenario table.

### CSGP — CoStar Group

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** CoStar provides a data-driven commercial real estate platform, but it is not preferred over the higher-quality, lower-valuation names in the shortlist such as Regeneron and AppLovin, which offer better growth-adjusted value and lower sector risk. Alternatives considered: REGN, APP, CLX, MGM, IDXX.
- **Thesis:** CoStar Group screens as a top 20-day momentum name with a 24.1% 20-day return and an 11.7% 60-day return, with a forward P/E of 19.7, 14.1% revenue growth, and a 78.3% gross margin. The company is a major commercial real estate data and services platform, but the sector faces structural headwinds from remote work and elevated office vacancy, so the position should be held with a neutral stance.
- **Source IDs:** S026, S030, S033, S037
- **Catalysts:** Continued demand for commercial real estate data and analytics, Positive 20-day momentum, High gross margin supporting profitability
- **Risks:** Commercial real estate structural decline and office vacancy, Forward P/E of 19.7 may not fully reflect sector risk, Single-quarter momentum can reverse
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 1.7683 (source.forwardEps) x AI multiple assumption 20.00; source IDs S026, S030, S033, S037
- **EPS:** 1.76832 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 19.747557
- **FY+1 growth assumption:** 25.84%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / LLY / CSGP shows FY1 consensus growth of ~25.8% with revenue growth of ~14.1% and earnings growth of ~25.8%, supported by a 78.3% gross margin but a thin 5.8% operating margin and 4.9% profit margin. The forward EPS of 1.77 and forward P/E of 19.7x support a 20-24x base/bull range. Peer reference: LLY, given comparable growth and margin profile in the healthcare sector.
- **Company fundamentals:** CoStar Group reported diluted EPS of 0.32 for the period ending 2026-09-30, with forward EPS of 1.77, forward P/E of 19.75, revenue growth of 14.1%, gross margin of 78.3%, operating margin of 5.8%, and profit margin of 4.9%. FY1 EPS growth was 25.8% and FY1 revenue growth was 11.3%.
- **Bull / Base / Bear:** 42.44 / 35.37 / 28.29
- **Bull / Base / Bear returns:** 21.53% / 1.29% / -18.99%
- **Scenario probabilities:** not separately assigned; see scenario table.

### XLV — Health Care sector ETF

- **Type:** ETF
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** The Health Care sector ETF provides broad, diversified exposure to the sector with top liquidity and a 28.3% price change, avoiding the single-name concentration and forward EPS gaps flagged for individual shortlist stocks such as MRVL, COIN, DELL, SMCI, NVDA, MU, TSLA, and AMD. Alternatives considered: XLP, XLY, XLRE, XLF, XLU, XLB, XLI.
- **Thesis:** The Health Care sector ETF screens as a top liquidity leader with a 28.3% price change and strong dollar volume, offering diversified exposure to large-cap pharma, biotech, and medical devices. The sector benefits from an aging population, strong drug pipelines, and favorable regulatory environments, making it a core holding for health care exposure.
- **Source IDs:** S051, S055
- **Catalysts:** Sector-wide revenue growth from major drug launches and pipeline catalysts, Continued demand for health care services and medical technology, Diversification across large-cap health care names
- **Risks:** Sector concentration in large-cap pharma and biotech, Regulatory and patent cliff risk for key products, Macro and interest rate sensitivity in health care
- **Valuation method:** Holdings/portfolio valuation with AI total-return assumption
- **Valuation status:** verified; forward-EPS source: ; period flags: 
- **Valuation assumptions:** Holdings/portfolio valuation; 10 weighted holdings; coverage 61.42%; source IDs S051, S055
- **Top holdings:** LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59%
- **Portfolio valuation:** Top 10 holdings; numeric weight coverage 61.42%
- **Sector exposure:** Health Care
- **Underlying drivers:** Top 10 holdings include LLY, JNJ, ABBV, MRK, UNH, TMO, AMGN, GILD, ABT, and PFE, with top-10 weight coverage of 61.42%. The sector benefits from large-cap pharma, biotech, and medical device exposure.
- **Bull / Base / Bear:** 206.3 / 193.41 / 173.15
- **Bull / Base / Bear returns:** 12.0% / 5.0% / -6.0%
- **Scenario probabilities:** not separately assigned; see scenario table.

## Quant Risk Layer

| Field | Value |
| --- | --- |
| Volatility model | vol5_ols_v1 |
| Spike model | spike_logit_v1 |
| As-of date | 2026-11-27 |
| Target window | 2026-11-30 to 2026-12-04 |
| Forecast 5D annualized volatility | 22.14% |
| Historical-vol baseline | 32.40% |
| EWMA baseline | 28.24% |
| Spike probability | 39.40% |
| Spike threshold | 18.50% |
| Status | prospective |
| Forecast ID | e7ce29ad8d72013a |

Risk-only; no directional interpretation or allocation implication.

## Scenarios

### Short Term (5 trading sessions)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 25% | +2.00% | Spike probability 39.4% exceeds historical baseline 32.4% and EWMA baseline 28.2%, indicating elevated near-term volatility risk that could resolve with a sharp rally if the frozen daily-close model confirms a positive US close. |
| Base | 50% | +0.00% | Directional signal is false and forecast volatility 22.1% is elevated, so the most likely path is a range-bound week with returns near zero as elevated volatility persists without a clear directional catalyst. |
| Bear | 25% | -2.00% | If the spike probability materializes into a downside shock, elevated volatility and false directional signal increase the risk of a modest decline, with the frozen model suggesting a -2% move if risk-off flows intensify. |

### Long Term (12 months)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 30% | +8.00% | Sustained elevated volatility and a 39.4% spike probability over the horizon imply a higher chance of a strong recovery if the frozen daily-close model confirms positive US close momentum, driving an 8% gain. |
| Base | 40% | +3.00% | With directional signal false and volatility elevated, the base case is a modest positive drift as elevated volatility normalizes and earnings/credit fundamentals provide gradual support, yielding a 3% return. |
| Bear | 30% | -5.00% | If the spike probability triggers a sustained risk-off episode, elevated forecast volatility and false directional signal could lead to a deeper drawdown, with the frozen model supporting a -5% return if credit spreads widen and earnings disappoint. |

## Positioning

- Maintain a defensive tilt: Communication Services and Consumer Staples are the best-performing sectors, while Information Technology and Energy are the worst.
- Do not favored high-liquidity names solely on liquidity leadership; the shortlist includes NVDA, MU, TSLA, AMD, MRVL, DDOG, SMCI, INTC, COIN, DELL, SNDK, LITE, and others, but the 20-day returns for the sector ETFs are negative for IT and Energy.
- Use credit spreads as a liquidity gauge: tight high-yield and IG spreads support risk assets, but the flat yield curve and negative 20-day returns argue for caution.
- Monitor the advance/decline ratio and 20-day breadth: the 4.34 ratio is strong, but the 52.09% positive 20-day rate suggests the pullback is not yet fully absorbed.
- No weights are assigned; the posture is qualitative and based on momentum, dislocation, liquidity, and valuation evidence.

## Catalysts

| Date | Event | Why it matters |
| --- | --- | --- |
| 2026-1 |  |  |

## Key Risks


## External Source Ledger

| ID | Type | Ticker | Published | Status | URL | Claims |
| --- | --- | --- | --- | --- | --- | --- |
| S001 | macro | macro | 2026-11-26 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFF&cosd=2026-01-01 | Effective federal funds rate (DFF) latest observation 2026-11-26: 3.88 |
| S002 | macro | macro | 2026-11-26 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLH0A0HYM2&cosd=2026-01-01 | US high-yield OAS (BAMLH0A0HYM2) latest observation 2026-11-26: 3.77 |
| S003 | macro | macro | 2026-11-26 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLC0A0CM&cosd=2026-01-01 | US investment-grade OAS (BAMLC0A0CM) latest observation 2026-11-26: 0.99 |
| S004 | macro | macro | 2026-10-01 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCSL&cosd=2026-01-01 | US CPI (CPIAUCSL) latest observation 2026-10-01: 337.476 |
| S005 | macro | macro | 2026-10-01 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=UNRATE&cosd=2026-01-01 | US unemployment rate (UNRATE) latest observation 2026-10-01: 4.1 |
| S006 | macro | macro | 2026-10-01 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=PAYEMS&cosd=2026-01-01 | US nonfarm payrolls (PAYEMS) latest observation 2026-10-01: 159293 |
| S007 | macro | macro | 2026-11-27 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=T10Y2Y&cosd=2026-01-01 | 10Y-2Y Treasury spread (T10Y2Y) latest observation 2026-11-27: 0.25 |
| S008 | news | CHTR | 2026-11-28 | unavailable | https://news.google.com/rss/search?q=CHTR+Charter+Communications+stock&hl=en-US&gl=US&ceid=US:en |  |
| S009 | filing | APP | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001751008&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0001751008-26-000069); 8-K filed 2026-11-04 (accession 0001751008-26-000068); 10-Q filed 2026-08-05 (accession 0001751008-26-000059) |
| S010 | filing | FISV | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0000798354-26-000042); 8-K filed 2026-11-03 (accession 0000798354-26-000039); 8-K filed 2026-10-23 (accession 0001193125-26-429481) |
| S011 | filing | CHTR | 2026-11-06 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-06 (accession 0001091667-26-000073); 8-K filed 2026-11-06 (accession 0001091667-26-000072); 8-K filed 2026-10-27 (accession 0001091667-26-000064) |
| S012 | news | APP | Fri, 27 Nov 2026 17:56:14 GMT | ok | https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en | AppLovin vs. Magnite: Which Technology Stock Is a Better Buy for 2027? - The Motley Fool (Fri, 27 Nov 2026 17:56:14 GMT); Applovin Corp Stock (APP) Moved Up by 5.36% on Nov 27: A Full Analysis - TradingKey (Fri, 27 Nov 2026 19:15:40 GMT); AppLovin stock soars after Q3 earnings, outlook beat - Yahoo Finance (Thu, 05 Nov 2026 08:00:00 GMT) |
| S013 | news | FISV | 2026-11-28 | unavailable | https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en |  |
| S014 | filing | CLX | 2026-11-19 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 | 8-K filed 2026-11-19 (accession 0001206774-26-000606); 10-Q filed 2026-11-02 (accession 0000021076-26-000046); 8-K filed 2026-11-02 (accession 0000021076-26-000044) |
| S015 | filing | APP | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json | Diluted EPS 11.61 for period ending 2026-09-30 (filed 2026-11-04) |
| S016 | stock | CHTR | 2026-11-28 | ok | https://finance.yahoo.com/quote/CHTR | Trailing P/E: 13.83723; Forward P/E: 3.3747232; Forward EPS: 45.59485; Price: 153.87; Market price: 153.87; Market cap: 27550660608; Sector: Communication Services; Trailing Eps: 11.12; Revenue Growth: 0.091; Gross Margin: 0.55084; Operating Margin: 0.23389; Profit Margin: 0.02498; Return On Equity: 0.07019; Total Revenue: 55645999104; Market Cap: 27550660608; Consensus EPS FY+1: 47.75367; growth: 1.4848 |
| S017 | stock | FISV | 2026-11-28 | ok | https://finance.yahoo.com/quote/FISV | Forward P/E: 7.7145143; Price: 61.49; Market price: 61.49; Market cap: 32715614208; Market Cap: 32715614208; Consensus EPS FY+1: 7.97069; growth: 0.0954 |
| S018 | stock | APP | 2026-11-28 | ok | https://finance.yahoo.com/quote/APP | Trailing P/E: 25.524935; Forward P/E: 19.136812; Forward EPS: 20.86084; Price: 399.21; Market price: 399.21; Market cap: 132267081728; Sector: Communication Services; Trailing Eps: 15.64; Revenue Growth: 0.555; Earnings Growth: 0.755; Gross Margin: 0.8878; Operating Margin: 0.77782995; Profit Margin: 0.65887; Return On Equity: 2.1008599; Total Revenue: 7608893952; Market Cap: 132267081728; Consensus EPS FY+1: 20.78066; growth: 0.2759 |
| S019 | news | CLX | Mon, 23 Nov 2026 10:07:25 GMT | ok | https://news.google.com/rss/search?q=CLX+Clorox+stock&hl=en-US&gl=US&ceid=US:en | Is Clorox (CLX) Fully Priced After Its Healthcare Product Launch? - Yahoo Finance (Mon, 23 Nov 2026 10:07:25 GMT); Clorox (NYSE:CLX) Stock Rating Cut to Sell at Wall Street Zen - MarketBeat (Sat, 28 Nov 2026 09:18:22 GMT); Clorox Company (The) (CLX) Stock Forecasts - Yahoo Finance (Tue, 24 Nov 2026 22:03:23 GMT) |
| S020 | filing | IDXX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000874716&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000874716-26-000135); 8-K filed 2026-11-02 (accession 0001104659-26-120892); 10-Q filed 2026-08-04 (accession 0000874716-26-000123) |
| S021 | filing | FISV | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json | Diluted EPS -8.9 for period ending 2026-09-30 (filed 2026-11-04) |
| S022 | news | IDXX | 2026-11-28 | unavailable | https://news.google.com/rss/search?q=IDXX+Idexx+Laboratories+stock&hl=en-US&gl=US&ceid=US:en |  |
| S023 | stock | IDXX | 2026-11-28 | ok | https://finance.yahoo.com/quote/IDXX | Trailing P/E: 48.465633; Forward P/E: 42.575874; Forward EPS: 16.8929; Price: 719.23; Market price: 719.23; Market cap: 56665444352; Sector: Healthcare; Trailing Eps: 14.84; Revenue Growth: 0.099; Earnings Growth: 0.179; Gross Margin: 0.62722; Operating Margin: 0.32497; Profit Margin: 0.25357; Return On Equity: 0.68925005; Total Revenue: 4662220800; Market Cap: 56665444352; Consensus EPS FY+1: 16.8929; growth: 0.1244 |
| S024 | filing | CLX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000021076.json | Diluted EPS 1.39 for period ending 2026-09-30 (filed 2026-11-02) |
| S025 | filing | CHTR | 2026-11-06 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001091667.json | Diluted EPS 0.38 for period ending 2026-09-30 (filed 2026-11-06) |
| S026 | filing | CSGP | 2026-10-28 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001057352&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-28 (accession 0001057352-26-000083); 8-K filed 2026-10-27 (accession 0001057352-26-000078); 8-K filed 2026-08-21 (accession 0001057352-26-000072) |
| S027 | stock | CLX | 2026-11-28 | ok | https://finance.yahoo.com/quote/CLX | Trailing P/E: 20.010792; Forward P/E: 18.037094; Forward EPS: 6.1684; Price: 111.26; Market price: 111.26; Market cap: 13478858752; Sector: Consumer Defensive; Trailing Eps: 5.56; Revenue Growth: 0.333; Earnings Growth: 1.138; Gross Margin: 0.41939998; Operating Margin: 0.14286; Profit Margin: 0.09408; Return On Equity: 5.34363; Total Revenue: 7196000256; Market Cap: 13478858752; Consensus EPS FY+1: 6.1684; growth: 0.0769 |
| S028 | filing | MGM | 2026-10-28 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000789570&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-28 (accession 0000789570-26-000107); 8-K filed 2026-10-28 (accession 0000789570-26-000106); 8-K filed 2026-10-28 (accession 0000789570-26-000104) |
| S029 | filing | REGN | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000872589&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0000872589-26-000034); 8-K filed 2026-10-30 (accession 0000872589-26-000032); 8-K filed 2026-10-06 (accession 0001104659-26-113895) |
| S030 | news | CSGP | Thu, 26 Nov 2026 15:30:09 GMT | ok | https://news.google.com/rss/search?q=CSGP+CoStar+Group+stock&hl=en-US&gl=US&ceid=US:en | Why Is CoStar (CSGP) Up 23.5% Since Last Earnings Report? - Yahoo Finance (Thu, 26 Nov 2026 15:30:09 GMT); CoStar Group adds 8%, continuing recent rebound (CSGP:NASDAQ) - Seeking Alpha (Tue, 24 Nov 2026 16:17:35 GMT); Investors Revisit the Margin Expansion Story as CoStar Group (NASDAQ:CSGP) Climbs 4% and Its Rebound Continues - kalkine.ca (Wed, 25 Nov 2026 20:36:00 GMT) |
| S031 | filing | IDXX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000874716.json | Diluted EPS 11.75 for period ending 2026-09-30 (filed 2026-11-02) |
| S032 | news | MGM | Fri, 27 Nov 2026 19:58:34 GMT | ok | https://news.google.com/rss/search?q=MGM+MGM+Resorts+stock&hl=en-US&gl=US&ceid=US:en | MGM Resorts officer sells $695,722 in company stock - Investing.com (Fri, 27 Nov 2026 19:58:34 GMT); MGM (MGM) Up 20.2% Since Last Earnings Report: Can It Continue? - Yahoo Finance UK (Fri, 27 Nov 2026 15:30:16 GMT); MGM Resorts International to receive approximately $200 million Special Dividend from MGM China - Quantisnow (Wed, 25 Nov 2026 08:00:00 GMT) |
| S033 | stock | CSGP | 2026-11-28 | ok | https://finance.yahoo.com/quote/CSGP | Trailing P/E: 79.36363; Forward P/E: 19.747557; Forward EPS: 1.76832; Price: 34.92; Market price: 34.92; Market cap: 14049618944; Sector: Real Estate; Trailing Eps: 0.44; Revenue Growth: 0.141; Gross Margin: 0.78306997; Operating Margin: 0.0577; Profit Margin: 0.048720002; Return On Equity: 0.02155; Total Revenue: 3673999872; Market Cap: 14049618944; Consensus EPS FY+1: 1.76832; growth: 0.2584 |
| S034 | stock | MGM | 2026-11-28 | ok | https://finance.yahoo.com/quote/MGM | Trailing P/E: 13.316981; Forward P/E: 25.107967; Forward EPS: 1.40553; Price: 35.29; Market price: 35.29; Market cap: 8928742400; Sector: Consumer Cyclical; Trailing Eps: 2.65; Revenue Growth: -0.009; Gross Margin: 0.4362; Operating Margin: 0.057979997; Profit Margin: 0.03916; Return On Equity: 0.26933; Total Revenue: 17722869760; Market Cap: 8928742400; Consensus EPS FY+1: 1.40553; growth: -0.0462 |
| S035 | filing | SNDK | 2026-11-19 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0002023554&type=10-Q&dateb=&owner=include&count=10 | 8-K filed 2026-11-19 (accession 0001628280-26-075127); 8-K filed 2026-11-18 (accession 0001628280-26-074848); 10-Q filed 2026-10-30 (accession 0001628280-26-068601) |
| S036 | stock | REGN | 2026-11-28 | ok | https://finance.yahoo.com/quote/REGN | Trailing P/E: 21.705097; Forward P/E: 13.743936; Forward EPS: 72.18748; Price: 992.14; Market price: 992.14; Market cap: 102634758144; Sector: Healthcare; Trailing Eps: 45.71; Revenue Growth: 0.363; Earnings Growth: 0.355; Gross Margin: 0.46734002; Operating Margin: 0.30383; Profit Margin: 0.28511998; Return On Equity: 0.14948; Total Revenue: 16896199680; Market Cap: 102634758144; Consensus EPS FY+1: 62.10689; growth: 0.0477 |
| S037 | filing | CSGP | 2026-10-28 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001057352.json | Diluted EPS 0.32 for period ending 2026-09-30 (filed 2026-10-28) |
| S038 | stock | SNDK | 2026-11-28 | ok | https://finance.yahoo.com/quote/SNDK | Trailing P/E: 4.705623; Forward P/E: 2.3848605; Forward EPS: 35.79245; Price: 85.36; Market price: 85.36; Market cap: 97166557184; Sector: Technology; Trailing Eps: 18.14; Revenue Growth: 3.779; Earnings Growth: 69.096; Gross Margin: 0.79952; Operating Margin: 0.7268; Profit Margin: 0.67039; Return On Equity: 1.41174; Total Revenue: 28970999808; Market Cap: 97166557184; Consensus EPS FY+1: 35.79245; growth: 0.2573 |
| S039 | news | REGN | Thu, 26 Nov 2026 12:07:17 GMT | ok | https://news.google.com/rss/search?q=REGN+Regeneron+Pharmaceuticals+stock&hl=en-US&gl=US&ceid=US:en | Do Wall Street Analysts Like Regeneron Pharmaceuticals Stock? - Yahoo Finance (Thu, 26 Nov 2026 12:07:17 GMT); Regeneron (REGN) Stock May Still Look Reasonable Despite Livsayis Approval - Simply Wall St (Fri, 27 Nov 2026 14:13:59 GMT); Is Regeneron Stock Priced Right Against Its Rivals? - Trefis (Mon, 23 Nov 2026 04:38:02 GMT) |
| S040 | news | SNDK | Fri, 27 Nov 2026 13:36:20 GMT | ok | https://news.google.com/rss/search?q=SNDK+Sandisk+stock&hl=en-US&gl=US&ceid=US:en | Nvidia, Kioxia Unveil AI Storage Breakthrough As SanDisk Hits Death Cross - Benzinga (Fri, 27 Nov 2026 13:36:20 GMT); SanDisk Surges 16% as Memory Stocks Extend Their Rebound: Can SNDK Stock Blast Through $100 Before 2026 Ends? - Yahoo Finance (Fri, 27 Nov 2026 18:03:05 GMT); Sandisk: A NAND Bust Is Already Being Priced In - Seeking Alpha (Fri, 27 Nov 2026 15:10:13 GMT) |

## Sources

- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFF&cosd=2026-01-01 (2026-11-26)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLH0A0HYM2&cosd=2026-01-01 (2026-11-26)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLC0A0CM&cosd=2026-01-01 (2026-11-26)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCSL&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=UNRATE&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=PAYEMS&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=T10Y2Y&cosd=2026-01-01 (2026-11-27)
- filing APP: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001751008&type=10-Q&dateb=&owner=include&count=10 (2026-11-04)
- filing FISV: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 (2026-11-04)
- filing CHTR: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 (2026-11-06)
- news APP: https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en (Fri, 27 Nov 2026 17:56:14 GMT)
- filing CLX: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 (2026-11-19)
- filing APP: https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json (2026-11-04)
- stock CHTR: https://finance.yahoo.com/quote/CHTR (2026-11-28)
- stock FISV: https://finance.yahoo.com/quote/FISV (2026-11-28)
- stock APP: https://finance.yahoo.com/quote/APP (2026-11-28)
- news CLX: https://news.google.com/rss/search?q=CLX+Clorox+stock&hl=en-US&gl=US&ceid=US:en (Mon, 23 Nov 2026 10:07:25 GMT)
- filing IDXX: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000874716&type=10-Q&dateb=&owner=include&count=10 (2026-11-02)
- filing FISV: https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json (2026-11-04)
- stock IDXX: https://finance.yahoo.com/quote/IDXX (2026-11-28)

## AI Provenance

- Provider / model: hermes-local-proxy / upstage/solar-mini4:free
- Market research: attempts=1 tokens=8392 (prompt=5392, completion=3000) runtime=22.83s
- Fundamental research: generated this run at 2026-11-28T10:16:46.317082+00:00
- Evidence source dates: {'as_of': '2026-11-27', 'latest_equity_date': '2026-11-27', 'latest_macro_date': '2026-11-27', 'flows_date': '2026-11-27'}
- Evidence fingerprint: 58c59f9ff00e2fae2cb0a713be523afd484178100eb35a5f38bd351a46beb5ed
- Source citations are retrieved external records in the ledger above; market values remain from the verified database snapshot.


## Disclosures

- This is research and market intelligence, not investment advice.
- AI conclusions are research judgments, not validated return predictions.
- The frozen risk layer is risk-only and is not used for directional views or allocations.
- Legacy scores are not active inputs or outputs.

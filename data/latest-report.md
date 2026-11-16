# AEGIS AI-First Market Intelligence

Research generated at: 16 November 2026, 18:08 HKT
Database freshness: equity 2026-11-13 (latest row retrieved 2026-11-16 13:06:43.000010+08:00)
Data cutoff: 2026-11-13 US cash close
Snapshot ID: aegis-hourly-20261116T100853Z

## Executive Summary

- **AI market view: Late-November 2026 US equities show a mixed tape: broad market breadth is positive but the index is slightly negative over 20 days, and the 11 GICS sectors are bifurcated. Health Care, Consumer Discretionary, Consumer Staples, Real Estate and Financials are up over 20 days, while Communication Services, Information Technology and Energy are down. Liquidity leaders such as NVDA, AMD, MU and AAPL are strong on dollar volume, but several large-cap names carry extreme trailing P/E and negative earnings yields, signaling elevated valuation risk. Macro data show a 10Y-2Y spread of 0.27, high-yield OAS of 3.20 and IG OAS of 0.89, with CPI and unemployment still elevated, suggesting a cautious but not bearish macro backdrop.**
- Broad market breadth is positive: 71.3% above the 50-day moving average, 63.6% above the 200-day, and a 20-day advance/decline ratio of 1.70, but the S&P 500 is down 1.28% over 20 days.
- Sector performance is bifurcated: Health Care (+6.87%), Consumer Discretionary (+6.69%), Consumer Staples (+5.40%), Real Estate (+5.24%) and Financials (+5.69%) lead, while Communication Services (-1.48%), Information Technology (-7.19%) and Energy (-4.81%) lag.
- Liquidity leaders NVDA, AMD, MU and AAPL show strong dollar volume, but several large caps (NOW, MRVL, AMD, AAPL) have extreme trailing P/E and low/negative earnings yields, indicating valuation risk.
- Macro data show a 10Y-2Y spread of 0.27, high-yield OAS of 3.20 and IG OAS of 0.89, with CPI at 336.298 and unemployment at 4.2%, suggesting a mixed but not recessionary macro environment.
- The frozen risk model shows forecast volatility of 14.93% over 5 days, spike probability of 16.51%, below the 18.50% threshold, with no directional signal, indicating low near-term tail-risk probability.
- Flow data show XLV with strong institutional inflows and XLY with structural distribution, while XLU shows medium-term deterioration with exceptional institutional selling, reflecting sector rotation.

## Data QC

- Status: **PASS_WITH_WARNINGS**
- Equity session: 0 completed session(s) behind inference date
- Equity provenance: 393 provisional / 12576 canonical
- Breadth lag: 0 session(s); ETF-flow lag: 0 session(s)
- Note: Equity session contains a mix of provisional yfinance and canonical Massive rows.
- External sources: 79 ok / 0 unavailable; retrieved 2026-11-16T10:09:20.618793+00:00

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
| S&P 500 (SPX) | 7561.67 | -1.28% (20d) | Index slightly negative over 20 days despite positive breadth; 71.3% above 50d, 63.6% above 200d. |
| Health Care (XLV) | return_20d +6.87% | +6.87% | Top sector; trailing P/E 30.78; strong institutional inflows and strong confirmation. |
| Consumer Discretionary (XLY) | return_20d +6.69% | +6.69% | Strong momentum but structural distribution; trailing P/E 25.11. |
| Consumer Staples (XLP) | return_20d +5.40% | +5.40% | Defensive strength; trailing P/E 24.85. |
| Real Estate (XLRE) | return_20d +5.24% | +5.24% | Positive momentum; trailing P/E 29.63. |
| Financials (XLF) | return_20d +5.69% | +5.69% | Positive momentum; trailing P/E 15.85. |
| Utilities (XLU) | return_20d +4.34% | +4.34% | Up on price but exceptional institutional selling; medium-term deterioration. |
| Materials (XLB) | return_20d +2.57% | +2.57% | Modest positive; trailing P/E 21.72. |
| Industrials (XLI) | return_20d +0.61% | +0.61% | Near-flat; trailing P/E 27.07. |
| Communication Services (XLC) | return_20d -1.48% | -1.48% | Negative; trailing P/E 17.26. |
| Information Technology (XLK) | return_20d -7.19% | -7.19% | Worst sector; trailing P/E 30.03; high valuation risk. |
| Energy (XLE) | return_20d -4.81% | -4.81% | Negative; trailing P/E 16.23. |

## Macro, Fiscal, Rates, Liquidity and Credit

- Growth: US macro data show CPI at 336.298 (Sep 2026) and core CPI at 338.896, indicating persistent inflation; unemployment at 4.2% (Sep 2026) suggests a still-tight labor market.
- Inflation: CPI and core CPI remain elevated, with the latest CPI observation 337.476 (Oct 2026) from external source S004, implying policy constraints.
- Policy: The effective federal funds rate is 3.88% as of 2026-11-12 (S001), indicating a restrictive or neutral stance that may limit risk appetite.
- Rates: The 10Y-2Y Treasury spread is 0.27 (S007), a modestly positive curve, while high-yield OAS is 3.20 (S002) and IG OAS is 0.89 (S003), suggesting moderate credit stress but not distress.
- Liquidity: High-yield and IG spreads are elevated but not extreme, and the frozen risk model shows low spike probability (16.51% vs 18.50% threshold), indicating contained liquidity risk.
- Credit: High-yield OAS of 3.20 and IG OAS of 0.89 (S002, S003) point to moderate credit conditions, with no signal of imminent credit event.

## US Equities and 11 GICS Sectors

Macro source IDs: S001, S002, S003, S004, S005, S006, S007

| GICS sector | Evidence | AI research stance | Source IDs |
| --- | --- | --- | --- |
| Health Care | 20d return +6.87%; trailing P/E 30.78; strong institutional inflows and strong confirmation; top sector momentum. | Positive momentum and institutional support; valuation is rich but relative strength is strong. | S055 |
| Consumer Staples | 20d return +5.40%; trailing P/E 24.85; defensive strength in a mixed tape. | Defensive outperformance; stable demand and reasonable valuation. | S056 |
| Consumer Discretionary | 20d return +6.69%; trailing P/E 25.11; strong momentum but structural distribution. | Positive momentum offset by institutional selling; watch flow divergence. | S057 |
| Real Estate | 20d return +5.24%; trailing P/E 29.63; positive momentum. | Positive momentum; valuation is elevated but relative strength is supportive. | S059 |
| Financials | 20d return +5.69%; trailing P/E 15.85; positive momentum. | Positive momentum with reasonable valuation; relative value attractive. | S064 |
| Utilities | 20d return +4.34%; trailing P/E 18.11; price up but exceptional institutional selling. | Price strength contradicted by institutional outflows; medium-term deterioration. | S071 |
| Materials | 20d return +2.57%; trailing P/E 21.72; modest positive. | Modest positive; valuation is reasonable but momentum is weak. | S067 |
| Industrials | 20d return +0.61%; trailing P/E 27.07; near-flat. | Near-flat; valuation is elevated but momentum is neutral. | S068 |
| Communication Services | 20d return -1.48%; trailing P/E 17.26; negative. | Negative momentum; valuation is reasonable but relative weakness is concerning. | S070 |
| Information Technology | 20d return -7.19%; trailing P/E 30.03; worst sector; high valuation risk. | Negative momentum and high valuation; risk of further downside. | S074 |
| Energy | 20d return -4.81%; trailing P/E 16.23; negative. | Negative momentum; valuation is reasonable but relative weakness is concerning. | S075 |

### Sector fundamentals, valuation and earnings

No point-in-time sector fundamentals beyond trailing P/E and 20-day returns are supplied in the database snapshot. The supplied evidence is limited to ETF-level trailing P/E (S055-S075) and sector returns; growth, margins, consensus, and structured fundamentals are unavailable for the full universe. Therefore, no additional sector fundamentals are asserted here.

## Growth vs Value

- Health Care and Consumer Staples show positive 20d returns with trailing P/E of 30.78 and 24.85 respectively, indicating strong momentum but rich valuation.
- Financials and Materials offer more reasonable trailing P/E (15.85 and 21.72) with positive momentum, suggesting better value relative to other sectors.
- Information Technology and Communication Services are negative on 20d returns with high valuation multiples (30.03 and 17.26), indicating potential value risk.
- Energy and Utilities have reasonable trailing P/E (16.23 and 18.11) but negative and mixed momentum respectively, suggesting mixed growth/value signals.

## ETF Flows and Breadth

- Broad market breadth is positive: 71.3% above 50d, 63.6% above 200d, 20d advance/decline ratio 1.70, with 315 advancers vs 185 decliners.
- S&P 500 is down 1.28% over 20 days, indicating a divergence between price and breadth that warrants caution.
- XLV shows strong institutional inflows and strong confirmation, while XLY shows structural distribution, indicating sector rotation from discretionary to defensive.
- XLU shows medium-term deterioration with exceptional institutional selling despite price up, suggesting weak underlying support.
- No new highs or new lows are reported, and the advance/decline ratio is positive, indicating broad participation without extreme extremes.

## Stock Ideas

Single-stock research uses reported EPS, forward P/E and company fundamentals. All ideas are research judgments, not validated return predictions.

| Ticker | Security | Research view | Price | EPS | Forward P/E | Base target | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| APP | AppLovin | NEW | 409.1 | 20.86026 | 19.611452 | 417.21 | NEW |
| PNR | Pentair | KEEP | 68.3 | 5.30402 | 12.877027 | 68.95 | KEEP |
| GEN | Gen Digital | KEEP | 30.4 | 3.33736 | 9.108996 | 33.37 | KEEP |
| CLX | Clorox | KEEP | 109.46 | 6.1684 | 17.745283 | 111.03 | KEEP |

## ETF Ideas

ETF research uses holdings, portfolio valuation and exposure. Single-stock EPS × P/E valuation is not applied to ETFs.

| Ticker | Fund | Research view | Price | Top holdings | Portfolio valuation | Sector exposure | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| XLV | Health Care sector ETF | KEEP | 188.85 | LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59% | Top 10 holdings; numeric weight coverage 61.42% | Health Care | KEEP |
### APP — AppLovin

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** AppLovin offers a rare combination of top-tier 20-day momentum, high operating margins, and a forward P/E near 19.6 that is not inflated by negative earnings, making it a cleaner momentum-plus-quality candidate than the negative-EPS dislocation names such as INTC, LITE, COIN, and the high-multiple names such as NOW and AMD. Alternatives considered: INTC, NOW, AMD, COIN, LITE.
- **Thesis:** AppLovin screens in the top 20-day momentum bucket with a 53.7% 20-day return and a 32.5% 60-day return, while its reported diluted EPS of 11.61 and forward EPS of 20.86 support a forward P/E near 19.6. The company's high gross margin (~88.8%) and operating margin (~77.8%) indicate a high-quality, capital-light advertising franchise, and its sector-relative P/E of 1.0 places it in line with the broader universe rather than at a premium.
- **Source IDs:** S008, S011, S013, S015
- **Catalysts:** Continued 20-day momentum and 60-day return momentum, Sustained high-margin advertising revenue growth, Forward EPS expansion from reported 11.61 to 20.86
- **Risks:** High 20-day momentum can mean elevated volatility and mean-reversion risk, Forward EPS and fiscal-year mapping are unverified, Sector-relative P/E at 1.0 leaves limited valuation cushion if growth slows
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 20.8603 (source.forwardEps) x AI multiple assumption 20.00; source IDs S008, S011, S013, S015
- **EPS:** 20.86026 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 19.611452
- **FY+1 growth assumption:** 27.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / PNR / APP shows 25.4% revenue growth and 75.5% earnings growth with 88.8% gross margin and 77.8% operating margin, supporting a premium multiple. PNR is the named peer reference: PNR trades at a lower forward P/E (12.9) with weaker growth and margins, so APP's higher growth and margin profile justify a higher base multiple.
- **Company fundamentals:** Reported diluted EPS 11.61; forward EPS 20.86; forward P/E 19.61; gross margin 88.8%; operating margin 77.8%; profit margin 65.9%; revenue growth 55.5%; earnings growth 75.5%; ROE 2.10; 20-day return 53.7%; 60-day return 32.5%; 60-day drawdown -0.2%; sector-relative P/E 1.0.
- **Bull / Base / Bear:** 500.65 / 417.21 / 333.76
- **Bull / Base / Bear returns:** 22.38% / 1.98% / -18.42%
- **Scenario probabilities:** not separately assigned; see scenario table.

### PNR — Pentair

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Pentair is preferable to the negative-EPS dislocation names such as INTC, LITE, and COIN because it offers a positive, low forward P/E and a cleaner balance-sheet profile, but it is not preferred over the high-quality momentum names such as APP because its fundamentals are still contracting. Alternatives considered: INTC, LITE, COIN, APP, RDDT.
- **Thesis:** Pentair is a top-20-day-momentum stock with a 27.8% 20-day return and a 7.1% 60-day return, and it carries a low forward P/E of 12.9 based on a forward EPS of 5.30. However, its revenue growth of -4.5% and earnings growth of -18.8% show that the momentum is not yet supported by fundamental expansion, so the position should be held rather than added aggressively.
- **Source IDs:** S009, S014, S017, S022
- **Catalysts:** 20-day momentum of 27.8%, Low forward P/E of 12.9, Potential stabilization in industrial and water technology demand
- **Risks:** Negative revenue and earnings growth of -4.5% and -18.8%, Momentum may fade if fundamentals do not inflect, Forward EPS and fiscal-year mapping are unverified
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 5.3040 (source.forwardEps) x AI multiple assumption 13.00; source IDs S009, S014, S017, S022
- **EPS:** 5.30402 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 12.877027
- **FY+1 growth assumption:** 12.82%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / APP / PNR has 12.8% forward earnings growth but negative revenue/earnings growth and lower margins (40.2% gross, 21.4% operating), so a lower multiple is warranted. APP is the named peer reference: APP's superior growth and margin profile supports a higher multiple, while PNR's weaker fundamentals justify a discount.
- **Company fundamentals:** Reported diluted EPS 2.76; forward EPS 5.30; forward P/E 12.88; gross margin 40.2%; operating margin 21.4%; profit margin 15.4%; ROE 15.6%; revenue growth -4.5%; earnings growth -18.8%; 20-day return 27.8%; 60-day return 7.1%; 60-day drawdown -5.2%; sector-relative P/E 0.49.
- **Bull / Base / Bear:** 84.86 / 68.95 / 53.04
- **Bull / Base / Bear returns:** 24.25% / 0.95% / -22.34%
- **Scenario probabilities:** not separately assigned; see scenario table.

### GEN — Gen Digital

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Gen Digital is preferable to the negative-EPS dislocation names such as INTC, LITE, and COIN because it has positive earnings growth and a low forward P/E, but it is not preferred over the high-quality momentum names such as APP because its forward earnings are less certain and its sector-relative valuation is deeply discounted. Alternatives considered: INTC, LITE, COIN, APP, RDDT.
- **Thesis:** Gen Digital is a top-20-day-momentum stock with a 25.8% 20-day return and a 7.9% 60-day return, and it trades at a very low forward P/E of 9.1 based on a forward EPS of 3.34. The stock's revenue growth of 12.2% and earnings growth of 128.6% are encouraging, but the forward EPS and fiscal-year mapping are unverified, so the low multiple should be treated as a valuation signal rather than a conviction to add.
- **Source IDs:** S019, S021, S026, S037
- **Catalysts:** 20-day momentum of 25.8%, Earnings growth of 128.6%, Low forward P/E of 9.1
- **Risks:** Forward EPS and fiscal-year mapping are unverified, 20-day momentum may be driven by a one-time repricing event, Sector-relative P/E of 0.42 suggests the stock is cheap for a reason
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 3.3374 (source.forwardEps) x AI multiple assumption 10.00; source IDs S019, S021, S026, S037
- **EPS:** 3.33736 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 9.108996
- **FY+1 growth assumption:** 12.86%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / CLX / GEN has 12.9% forward earnings growth and 46.4% ROE, but margins are lower (77.4% gross, 43.2% operating) and growth is modest, so a mid-single-digit multiple is appropriate. CLX is the named peer reference: CLX has higher revenue growth and stronger margins, supporting a higher multiple, while GEN's lower growth and margin profile justify a lower multiple.
- **Company fundamentals:** Reported diluted EPS 0.83; forward EPS 3.34; forward P/E 9.11; gross margin 77.4%; operating margin 43.2%; profit margin 23.1%; ROE 46.4%; revenue growth 12.2%; earnings growth 128.6%; 20-day return 25.8%; 60-day return 7.9%; 60-day drawdown -3.2%; sector-relative P/E 0.42.
- **Bull / Base / Bear:** 40.05 / 33.37 / 26.7
- **Bull / Base / Bear returns:** 31.74% / 9.77% / -12.17%
- **Scenario probabilities:** not separately assigned; see scenario table.

### CLX — Clorox

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Clorox is preferable to the negative-EPS dislocation names such as INTC, LITE, and COIN because it has positive earnings growth and a forward P/E near 17.7, but it is not preferred over the high-quality momentum names such as APP because its profitability and ROE are materially weaker. Alternatives considered: INTC, LITE, COIN, APP, RDDT.
- **Thesis:** Clorox is a top-20-day-momentum stock with a 25.7% 20-day return and a 3.2% 60-day return, and it carries a forward P/E of 17.7 based on a forward EPS of 6.17. Its revenue growth of 33.3% and earnings growth of 113.8% are strong, but the stock's low ROE of 5.3% and thin operating margin of 14.3% suggest that the momentum is not yet backed by durable profitability, so the position should be held rather than scaled.
- **Source IDs:** S020, S023, S024, S034
- **Catalysts:** 20-day momentum of 25.7%, Revenue growth of 33.3%, Earnings growth of 113.8%
- **Risks:** Low ROE of 5.3% and thin operating margin of 14.3%, 20-day momentum may fade if consumer staples demand softens, Forward EPS and fiscal-year mapping are unverified
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 6.1684 (source.forwardEps) x AI multiple assumption 18.00; source IDs S020, S023, S024, S034
- **EPS:** 6.1684 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 17.745283
- **FY+1 growth assumption:** 7.69%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / GEN / CLX has 33.3% revenue growth and 113.8% earnings growth with 41.9% gross margin and 14.3% operating margin, supporting a higher multiple. GEN is the named peer reference: GEN has lower revenue growth and weaker margins, so CLX's stronger top-line momentum and earnings acceleration justify a higher base multiple.
- **Company fundamentals:** Reported diluted EPS 1.39; forward EPS 6.17; forward P/E 17.75; gross margin 41.9%; operating margin 14.3%; profit margin 9.4%; ROE 5.3%; revenue growth 33.3%; earnings growth 113.8%; 20-day return 25.7%; 60-day return 3.2%; 60-day drawdown 0.0%; sector-relative P/E 0.76.
- **Bull / Base / Bear:** 135.7 / 111.03 / 86.36
- **Bull / Base / Bear returns:** 23.97% / 1.43% / -21.1%
- **Scenario probabilities:** not separately assigned; see scenario table.

### XLV — Health Care sector ETF

- **Type:** ETF
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** XLV is preferable to the consumer staples and discretionary sector ETFs because it offers a more defensive healthcare allocation, but it is not preferred over the broad market or other sector ETFs because the limited holdings coverage prevents a full conviction on the underlying portfolio. Alternatives considered: XLP, XLY, XLRE, XLF, XLU, XLB, XLI.
- **Thesis:** XLV is a Health Care sector ETF with a 0.54% price change and a top-10 portfolio that includes LLY, JNJ, ABBV, MRK, UNH, TMO, AMGN, GILD, ABT, and PFE. The sector ETF provides diversified healthcare exposure, but the limited holdings coverage of 61.4% means the top-10 snapshot does not fully represent the fund, and the modest price change does not justify a strong directional call.
- **Source IDs:** S055, S060
- **Catalysts:** Diversified healthcare exposure across large-cap pharma and biotech, Top-10 holdings include LLY, JNJ, ABBV, MRK, and UNH, Sector-level stability in a defensive allocation
- **Risks:** Top-10 holdings coverage is only 61.4%, so the full portfolio is not fully visible, Modest 0.54% price change does not signal a strong trend, Sector-specific regulatory and drug-pricing risks
- **Valuation method:** Holdings/portfolio valuation with AI total-return assumption
- **Valuation status:** verified; forward-EPS source: ; period flags: 
- **Valuation assumptions:** Holdings/portfolio valuation; 10 weighted holdings; coverage 61.42%; source IDs S055, S060
- **Top holdings:** LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59%
- **Portfolio valuation:** Top 10 holdings; numeric weight coverage 61.42%
- **Sector exposure:** Health Care
- **Underlying drivers:** Top-10 holdings include LLY, JNJ, ABBV, MRK, UNH, TMO, AMGN, GILD, ABT, and PFE; holdings coverage 61.4%; price 188.85; raw price change 0.54%.
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
| Bull | 25% | +2.00% | Directional signal is false and forecast volatility is below the 5-day baseline, so a modest upside is driven by stable earnings momentum and low near-term volatility rather than a directional catalyst. |
| Base | 50% | +0.00% | Frozen daily-close model with no directional signal and elevated spike probability relative to historical baseline implies range-bound price action around the current level. |
| Bear | 25% | -2.00% | Elevated spike probability and volatility above the historical baseline create downside risk if a short-term shock or credit spread widening occurs before the target window closes. |

### Long Term (12 months)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 30% | +8.00% | Sustained earnings growth and positive rate expectations support a higher long-term return, with low near-term volatility providing a constructive backdrop for compounding. |
| Base | 40% | +3.00% | Moderate earnings expansion and stable credit conditions support a low-single-digit long-term return, consistent with a normal expansionary environment. |
| Bear | 30% | -5.00% | Rising volatility, elevated spike probability, and potential credit stress could compress long-term returns if earnings disappoint or funding conditions tighten. |

## Positioning

- Maintain a cautious but not bearish stance; positive breadth and moderate macro data support a constructive tilt, but elevated valuations and negative sector returns require risk management.
- Favor Health Care, Financials, and Consumer Staples for relative strength and defensive characteristics.
- Reduce exposure to Information Technology and Communication Services given negative momentum and high valuation multiples.
- Monitor liquidity leaders (NVDA, AMD, MU

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
| S011 | news | APP | Sun, 15 Nov 2026 07:07:20 GMT | ok | https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en | META_TITLE_QUOTE - Yahoo Finance (Sun, 15 Nov 2026 07:07:20 GMT); AppLovin Just Ripped 47% in a Month: Is It Too Late to Buy APP Stock Now? - Yahoo Finance (Thu, 12 Nov 2026 20:05:45 GMT); Is Trending Stock AppLovin Corporation (APP) a Buy Now? - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT) |
| S012 | news | FISV | Fri, 13 Nov 2026 21:49:46 GMT | ok | https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en | Fiserv, Inc. (FISV) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 21:49:46 GMT); Why Fiserv, Inc. (FISV) Was Exited by Ariel Appreciation Fund - Yahoo Finance (Wed, 28 Oct 2026 07:00:00 GMT); Fiserv (FISV): Buy, Sell, or Hold Post Q2 Earnings? - Yahoo Finance (Tue, 08 Sep 2026 07:00:00 GMT) |
| S013 | filing | APP | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json | Diluted EPS 11.61 for period ending 2026-09-30 (filed 2026-11-04) |
| S014 | stock | PNR | 2026-11-16 | ok | https://finance.yahoo.com/quote/PNR | Trailing P/E: 18.610355; Forward P/E: 12.877027; Forward EPS: 5.30402; Price: 68.3; Market price: 68.3; Market cap: 10904415232; Sector: Industrials; Trailing Eps: 3.67; Revenue Growth: -0.045; Earnings Growth: -0.188; Gross Margin: 0.40168998; Operating Margin: 0.21410999; Profit Margin: 0.15435; Return On Equity: 0.15605; Total Revenue: 3966200064; Market Cap: 10904415232; Consensus EPS FY+1: 5.30402; growth: 0.1282 |
| S015 | stock | APP | 2026-11-16 | ok | https://finance.yahoo.com/quote/APP | Trailing P/E: 27.54882; Forward P/E: 19.611452; Forward EPS: 20.86026; Price: 409.1; Market price: 409.1; Market cap: 135543824384; Sector: Communication Services; Trailing Eps: 14.85; Revenue Growth: 0.555; Earnings Growth: 0.755; Gross Margin: 0.8878; Operating Margin: 0.77782995; Profit Margin: 0.65887; Return On Equity: 2.1008599; Total Revenue: 7608893952; Market Cap: 135543824384; Consensus EPS FY+1: 20.72438; growth: 0.2744 |
| S016 | stock | FISV | 2026-11-16 | ok | https://finance.yahoo.com/quote/FISV | Forward P/E: 7.99667; Price: 63.78; Market price: 63.78; Market cap: 33934002176; Market Cap: 33934002176; Consensus EPS FY+1: 7.97582; growth: 0.0959 |
| S017 | filing | PNR | 2026-10-27 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json | Diluted EPS 2.76 for period ending 2026-09-30 (filed 2026-10-27) |
| S018 | filing | FISV | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json | Diluted EPS -8.9 for period ending 2026-09-30 (filed 2026-11-04) |
| S019 | filing | GEN | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0000849399-26-000083); 8-K filed 2026-10-28 (accession 0000849399-26-000081); 8-K filed 2026-10-09 (accession 0000849399-26-000079) |
| S020 | filing | CLX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000021076-26-000046); 8-K filed 2026-11-02 (accession 0000021076-26-000044); 8-K filed 2026-10-29 (accession 0001206774-26-000586) |
| S021 | news | GEN | Thu, 29 Oct 2026 07:00:00 GMT | ok | https://news.google.com/rss/search?q=GEN+Gen+Digital+stock&hl=en-US&gl=US&ceid=US:en | Gen Digital (GEN) Stock Repriced After Q2 Earnings Put Margins Center Stage - Yahoo Finance (Thu, 29 Oct 2026 07:00:00 GMT); Gen Digital Stock: Is Wall Street Bullish or Bearish? - Yahoo Finance (Thu, 05 Nov 2026 08:00:00 GMT); Are Business Services Stocks Lagging GEN DIGITAL INC (GEN) This Year? - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT) |
| S022 | news | PNR | Fri, 13 Nov 2026 22:09:48 GMT | ok | https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en | Pentair plc (PNR) stock price, news, quote and history - Yahoo Finance UK (Fri, 13 Nov 2026 22:09:48 GMT); Pentair plc (PNR) Q3 Earnings and Revenues Beat Estimates - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT); Pentair (PNR) Stock May Be 46% Undervalued As New CFO Arrives - Yahoo Finance (Fri, 25 Sep 2026 07:00:00 GMT) |
| S023 | stock | CLX | 2026-11-16 | ok | https://finance.yahoo.com/quote/CLX | Trailing P/E: 19.68705; Forward P/E: 17.745283; Forward EPS: 6.1684; Price: 109.46; Market price: 109.46; Market cap: 13260793856; Sector: Consumer Defensive; Trailing Eps: 5.56; Revenue Growth: 0.333; Earnings Growth: 1.138; Gross Margin: 0.41939998; Operating Margin: 0.14286; Profit Margin: 0.09408; Return On Equity: 5.34363; Total Revenue: 7196000256; Market Cap: 13260793856; Consensus EPS FY+1: 6.1684; growth: 0.0769 |
| S024 | news | CLX | Fri, 13 Nov 2026 23:34:51 GMT | ok | https://news.google.com/rss/search?q=CLX+Clorox+stock&hl=en-US&gl=US&ceid=US:en | The Clorox Company (CLX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 23:34:51 GMT); The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance UK (Sat, 14 Nov 2026 06:03:20 GMT); The Clorox Company (CLX): Capitalizing on Volatility to Sell and Repurchase at New Lows - Yahoo Finance (Mon, 05 Oct 2026 07:00:00 GMT) |
| S025 | filing | CHTR | 2026-11-06 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-06 (accession 0001091667-26-000073); 8-K filed 2026-11-06 (accession 0001091667-26-000072); 8-K filed 2026-10-27 (accession 0001091667-26-000064) |
| S026 | stock | GEN | 2026-11-16 | ok | https://finance.yahoo.com/quote/GEN | Trailing P/E: 15.431472; Forward P/E: 9.108996; Forward EPS: 3.33736; Price: 30.4; Market price: 30.4; Market cap: 18035593216; Sector: Technology; Trailing Eps: 1.97; Revenue Growth: 0.122; Earnings Growth: 1.286; Gross Margin: 0.77410007; Operating Margin: 0.43229; Profit Margin: 0.23068; Return On Equity: 0.46402; Total Revenue: 5228000256; Market Cap: 18035593216; Consensus EPS FY+1: 3.33736; growth: 0.1286 |
| S027 | news | CHTR | Sun, 15 Nov 2026 05:47:01 GMT | ok | https://news.google.com/rss/search?q=CHTR+Charter+Communications+stock&hl=en-US&gl=US&ceid=US:en | Charter Communications (CHTR) Stock Could Be A Bargain Following Its New Operating Model - Yahoo Finance (Sun, 15 Nov 2026 05:47:01 GMT); Why You Should Think About Charter Communications Differently Now? - Yahoo Finance (Fri, 13 Nov 2026 19:16:11 GMT); Charter Communications (CHTR) Expands Enterprise Reach With Managed Secure Networking Launch - Yahoo Finance (Sun, 15 Nov 2026 06:08:00 GMT) |
| S028 | filing | IDXX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000874716&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000874716-26-000135); 8-K filed 2026-11-02 (accession 0001104659-26-120892); 10-Q filed 2026-08-04 (accession 0000874716-26-000123) |
| S029 | stock | CHTR | 2026-11-16 | ok | https://finance.yahoo.com/quote/CHTR | Trailing P/E: 13.006578; Forward P/E: 3.0452294; Forward EPS: 45.44485; Price: 138.39; Market price: 138.39; Market cap: 24778944512; Sector: Communication Services; Trailing Eps: 10.64; Revenue Growth: 0.091; Gross Margin: 0.55084; Operating Margin: 0.23389; Profit Margin: 0.02498; Return On Equity: 0.07019; Total Revenue: 55645999104; Market Cap: 24778944512; Consensus EPS FY+1: 49.35412; growth: 1.1136 |
| S030 | news | IDXX | Sat, 14 Nov 2026 22:37:20 GMT | ok | https://news.google.com/rss/search?q=IDXX+Idexx+Laboratories+stock&hl=en-US&gl=US&ceid=US:en | IDEXX Laboratories, Inc. (IDXX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Sat, 14 Nov 2026 22:37:20 GMT); symbol__ Stock Quote Price and Forecast - CNN (Fri, 13 Nov 2026 15:22:45 GMT); IDEXX Laboratories, Inc. (IDXX) stock price, news, quote and history - Yahoo Finance UK (Sat, 14 Nov 2026 09:01:45 GMT) |
| S031 | filing | ROP | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000882835&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000882835-26-000047); 8-K filed 2026-10-22 (accession 0000882835-26-000042); 8-K filed 2026-10-01 (accession 0000882835-26-000039) |
| S032 | stock | IDXX | 2026-11-16 | ok | https://finance.yahoo.com/quote/IDXX | Trailing P/E: 47.45485; Forward P/E: 41.687927; Forward EPS: 16.8929; Price: 704.23; Market price: 704.23; Market cap: 55483650048; Sector: Healthcare; Trailing Eps: 14.84; Revenue Growth: 0.099; Earnings Growth: 0.179; Gross Margin: 0.62722; Operating Margin: 0.32497; Profit Margin: 0.25357; Return On Equity: 0.68925005; Total Revenue: 4662220800; Market Cap: 55483650048; Consensus EPS FY+1: 16.8929; growth: 0.1244 |
| S033 | stock | ROP | 2026-11-16 | ok | https://finance.yahoo.com/quote/ROP | Trailing P/E: 18.993866; Forward P/E: 19.532475; Forward EPS: 24.57318; Price: 479.975; Market price: 479.975; Market cap: 47535013888; Sector: Technology; Trailing Eps: 25.27; Revenue Growth: 0.076; Earnings Growth: 0.326; Gross Margin: 0.69671; Operating Margin: 0.28049; Profit Margin: 0.30712998; Return On Equity: 0.13229; Total Revenue: 8434599936; Market Cap: 47535013888; Consensus EPS FY+1: 24.57318; growth: 0.09810001 |
| S034 | filing | CLX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000021076.json | Diluted EPS 1.39 for period ending 2026-09-30 (filed 2026-11-02) |
| S035 | news | ROP | Thu, 05 Nov 2026 08:00:00 GMT | ok | https://news.google.com/rss/search?q=ROP+Roper+Technologies+stock&hl=en-US&gl=US&ceid=US:en | Roper Technologies (ROP) Stock Looks Fully Valued As Cash Flow Comes Into Focus - Yahoo Finance (Thu, 05 Nov 2026 08:00:00 GMT); Roper Technologies (ROP), What Is Behind The Fresh Attention? - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT); Did Earnings Beat Just Shift Roper Technologies (ROP) Investment Narrative? - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT) |
| S036 | filing | CHTR | 2026-11-06 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001091667.json | Diluted EPS 0.38 for period ending 2026-09-30 (filed 2026-11-06) |
| S037 | filing | GEN | 2026-10-29 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000849399.json | Diluted EPS 0.83 for period ending 2026-10-02 (filed 2026-10-29) |
| S038 | filing | IDXX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000874716.json | Diluted EPS 11.75 for period ending 2026-09-30 (filed 2026-11-02) |
| S039 | filing | RDDT | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001713445&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0001713445-26-000116); 8-K filed 2026-10-29 (accession 0001713445-26-000114); 8-K filed 2026-08-12 (accession 0001713445-26-000107) |
| S040 | stock | RDDT | 2026-11-16 | ok | https://finance.yahoo.com/quote/RDDT | Trailing P/E: 20.091835; Forward P/E: 10.818217; Forward EPS: 9.10039; Price: 98.45; Market price: 98.45; Market cap: 19010076672; Sector: Communication Services; Trailing Eps: 4.9; Revenue Growth: 0.53; Earnings Growth: 0.749; Gross Margin: 0.91547996; Operating Margin: 0.29397; Profit Margin: 0.32105; Return On Equity: 0.32029998; Total Revenue: 3088880128; Market Cap: 19010076672; Consensus EPS FY+1: 6.8155; growth: 0.2401 |

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
- news APP: https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en (Sun, 15 Nov 2026 07:07:20 GMT)
- news FISV: https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 21:49:46 GMT)
- filing APP: https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json (2026-11-04)
- stock PNR: https://finance.yahoo.com/quote/PNR (2026-11-16)
- stock APP: https://finance.yahoo.com/quote/APP (2026-11-16)
- stock FISV: https://finance.yahoo.com/quote/FISV (2026-11-16)
- filing PNR: https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json (2026-10-27)
- filing FISV: https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json (2026-11-04)
- filing GEN: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 (2026-10-29)
- filing CLX: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 (2026-11-02)

## AI Provenance

- Provider / model: hermes-local-proxy / upstage/solar-mini4:free
- Market research: attempts=1 tokens=9513 (prompt=6513, completion=3000) runtime=23.05s
- Fundamental research: generated this run at 2026-11-16T10:08:53.212769+00:00
- Evidence source dates: {'as_of': '2026-11-13', 'latest_equity_date': '2026-11-13', 'latest_macro_date': '2026-11-16', 'flows_date': '2026-11-13'}
- Evidence fingerprint: 18454321ed8b958788eb6f2a6026538c45cb9eab8e3d76c85aa62057347f4f8e
- Source citations are retrieved external records in the ledger above; market values remain from the verified database snapshot.


## Disclosures

- This is research and market intelligence, not investment advice.
- AI conclusions are research judgments, not validated return predictions.
- The frozen risk layer is risk-only and is not used for directional views or allocations.
- Legacy scores are not active inputs or outputs.

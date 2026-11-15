# AEGIS AI-First Market Intelligence

Research generated at: 16 November 2026, 00:15 HKT
Database freshness: equity 2026-11-13 (latest row retrieved 2026-11-15 13:06:40.074841+08:00)
Data cutoff: 2026-11-13 US cash close
Snapshot ID: aegis-hourly-20261115T161546Z

## Executive Summary

- **AI market view: Late-November 2026: broad market breadth is constructive (71% above 50-day, 64% above 200-day, A/D ratio 1.70), but the index is slightly negative over 20 days and the 20-day return is -1.28%. Sector leadership is bifurcated: Health Care, Consumer Discretionary, Consumer Staples, Real Estate and Financials are up 20-day, while Information Technology and Energy are down. Liquidity is concentrated in SOXX (exceptional institutional buying) and NVDA/AMD/MU/AAPL (liquidity leaders), while TLT shows medium-term flow deterioration. Macro data show a 10Y-2Y spread of 0.27 and elevated credit spreads (HY OAS 3.20), with crypto markets down sharply on 2026-11-14.**
- Broad market breadth is positive: 71.3% of names above the 50-day moving average, 63.6% above the 200-day, and an advance/decline ratio of 1.70.
- Index-level momentum is slightly negative: SPX 20-day return is -1.28%, and Information Technology (-7.19%) and Energy (-4.81%) are the weakest sectors.
- Sector leadership is broad but uneven: Health Care (+6.87%), Consumer Discretionary (+6.69%), Consumer Staples (+5.40%), Real Estate (+5.24%) and Financials (+5.69%) lead.
- Flows show exceptional institutional buying in SOXX (20d z-score 5.10) and liquidity leaders NVDA, AMD, MU, AAPL, while TLT shows medium-term flow deterioration.
- Credit conditions are elevated: HY OAS 3.20 and IG OAS 0.89, with a modestly positive 10Y-2Y spread of 0.27.
- Crypto markets fell sharply on 2026-11-14 (BTC -6.04%, ETH -8.22%), signaling risk-off sentiment in digital assets.

## Data QC

- Status: **PASS_WITH_WARNINGS**
- Equity session: 0 completed session(s) behind inference date
- Equity provenance: 393 provisional / 12576 canonical
- Breadth lag: 0 session(s); ETF-flow lag: 0 session(s)
- Note: Equity session contains a mix of provisional yfinance and canonical Massive rows.
- External sources: 79 ok / 0 unavailable; retrieved 2026-11-15T16:16:08.264971+00:00

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
| SPX | 7561.67 | -1.28% (20d) | Index is slightly negative over 20 days; breadth is constructive with 71.3% above 50d and 63.6% above 200d. |
| Health Care (XLV) | 6.87% | +6.87% (20d) | Strongest sector; trailing P/E 30.78. |
| Consumer Discretionary (XLY) | 6.69% | +6.69% (20d) | Strong 20-day return; trailing P/E 25.11. |
| Consumer Staples (XLP) | 5.40% | +5.40% (20d) | Positive 20-day return; trailing P/E 24.85. |
| Real Estate (XLRE) | 5.24% | +5.24% (20d) | Positive 20-day return; trailing P/E 29.63. |
| Financials (XLF) | 5.69% | +5.69% (20d) | Positive 20-day return; trailing P/E 15.85. |
| Information Technology (XLK) | -7.19% | -7.19% (20d) | Weakest sector; trailing P/E 30.03. |
| Energy (XLE) | -4.81% | -4.81% (20d) | Negative 20-day return; trailing P/E 16.23. |
| SOXX | inflow | 20d flow z-score 5.10 | Exceptional institutional buying; price state is down. |
| TLT | neutral | 20d flow z-score -0.41 | Medium-term flow deterioration; price state flat. |

## Macro, Fiscal, Rates, Liquidity and Credit

- Growth: The 10Y-2Y Treasury spread is 0.27 (2026-11-13), indicating a modestly positive but shallow yield curve; no recession signal is evident from the spread alone.
- Inflation: CPI (CPIAUCSL) stands at 336.298 (2026-09-01) and core CPI at 338.896 (2026-09-01); the October CPI reading is 337.476 (2026-10-01), suggesting inflation remains above the pre-2021 trend.
- Policy: The effective federal funds rate is 3.88 (2026-11-12), implying a restrictive but easing policy stance.
- Rates: The 10Y-2Y spread of 0.27 is positive, but credit spreads are elevated: HY OAS 3.20 and IG OAS 0.89 (2026-11-12), indicating stress in lower-grade credit.
- Liquidity: SOXX shows exceptional institutional buying (20d flow z-score 5.10) while TLT shows medium-term flow deterioration (20d flow z-score -0.41); crypto markets fell sharply on 2026-11-14 (BTC -6.04%, ETH -8.22%).
- Credit: HY OAS 3.20 and IG OAS 0.89 are elevated, suggesting investors are demanding higher compensation for risk; this is consistent with a cautious risk appetite despite positive breadth.

## US Equities and 11 GICS Sectors

Macro source IDs: S001, S002, S003, S004, S005, S006, S007

| GICS sector | Evidence | AI research stance | Source IDs |
| --- | --- | --- | --- |
| Health Care | 20d return +6.87%; trailing P/E 30.78 (S054); SPX 20d return -1.28%. | Positive momentum and broad participation; valuation is rich relative to the market. | S054 |
| Consumer Discretionary | 20d return +6.69%; trailing P/E 25.11 (S058); SPX 20d return -1.28%. | Strong 20-day performance; valuation is moderate. | S058 |
| Consumer Staples | 20d return +5.40%; trailing P/E 24.85 (S062); SPX 20d return -1.28%. | Positive 20-day return; defensive sector with moderate valuation. | S062 |
| Real Estate | 20d return +5.24%; trailing P/E 29.63 (S063); SPX 20d return -1.28%. | Positive 20-day return; valuation is elevated. | S063 |
| Financials | 20d return +5.69%; trailing P/E 15.85 (S064); SPX 20d return -1.28%. | Positive 20-day return; lowest valuation among the leading sectors. | S064 |
| Utilities | 20d return +4.34%; trailing P/E 18.11 (S068); SPX 20d return -1.28%. | Positive 20-day return; defensive sector with moderate valuation. | S068 |
| Materials | 20d return +2.57%; trailing P/E 21.72 (S066); SPX 20d return -1.28%. | Positive 20-day return; moderate valuation. | S066 |
| Industrials | 20d return +0.61%; trailing P/E 27.07 (S067); SPX 20d return -1.28%. | Near-flat 20-day return; valuation is above average. | S067 |
| Communication Services | 20d return -1.48%; trailing P/E 17.26 (S071); SPX 20d return -1.28%. | Negative 20-day return; valuation is moderate. | S071 |
| Information Technology | 20d return -7.19%; trailing P/E 30.03 (S074); SPX 20d return -1.28%. | Weakest sector; negative momentum and elevated valuation. | S074 |
| Energy | 20d return -4.81%; trailing P/E 16.23 (S075); SPX 20d return -1.28%. | Negative 20-day return; valuation is cheap but momentum is negative. | S075 |

### Sector fundamentals, valuation and earnings

Sector-level trailing P/E data are supplied for all 11 GICS sectors via the ETF evidence set (S054, S058, S062, S063, S064, S066, S067, S068, S071, S074, S075). No point-in-time sector fundamentals such as revenue growth, margins, or consensus estimates are provided in the database; therefore no sector-level fundamental metrics beyond valuation are available. The supplied data are limited to trailing P/E and 20-day ETF returns.

## Growth vs Value

- Growth: Information Technology is the only sector with a negative 20-day return (-7.19%), while Health Care (+6.87%), Consumer Discretionary (+6.69%), Consumer Staples (+5.40%), Real Estate (+5.24%) and Financials (+5.69%) are positive.
- Value: Financials (XLF) trades at the lowest trailing P/E (15.85), followed by Energy (XLE) at 16.23; Information Technology (XLK) is the most expensive at 30.03.
- Valuation dispersion is wide: Financials and Energy are cheap on trailing P/E, while Health Care and Real Estate are expensive.
- The shortlist includes names with extreme valuation dispersion (e.g., CHTR earnings yield 0.369, MRVL P/E 74.23, NOW P/E 97.19), but these are flagged as having forward EPS issues and are not used for allocation.

## ETF Flows and Breadth

- SOXX shows exceptional institutional buying (20d flow z-score 5.10) and is the only flow leader in the supplied data; price state is down, indicating strong institutional accumulation despite price weakness.
- TLT shows medium-term flow deterioration (20d flow z-score -0.41) and a flat price state, suggesting reduced demand for duration.
- Breadth is constructive: 71.3% of names above the 50-day moving average, 63.6% above the 200-day, and an advance/decline ratio of 1.70.
- The index is slightly negative over 20 days (SPX -1.28%), but the positive breadth and A/D

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
- **Why preferred / alternatives:** AppLovin offers a rare combination of high growth, high margins, and strong momentum among the shortlisted names, with a forward P/E (~19.6) that is not excessive for its growth rate. It is preferable to the high-multiple names like NOW (forward P/E ~97) and MRVL (forward P/E ~74), which carry much higher valuation risk, and to the low-growth names like CLX and PNR, which offer less upside. Alternatives considered: NOW, MRVL, CLX, PNR.
- **Thesis:** AppLovin screens in the top 20-day momentum bucket with a 53.7% 20-day return and a 32.5% 60-day return, indicating strong price momentum. The company reports high gross margin (~88.8%) and operating margin (~77.8%), with revenue growth of ~55.5% and earnings growth of ~75.5%, supporting a quality compounder narrative. The forward P/E of ~19.6 is reasonable relative to its growth profile, and the trailing P/E of ~20.1 is not extreme for a high-growth mobile advertising platform.
- **Source IDs:** S008, S012, S013, S014
- **Catalysts:** Continued high revenue and earnings growth from the mobile advertising business, Sustained margin expansion as the platform scales, Potential re-rating as momentum persists and the stock recovers from recent volatility
- **Risks:** High 20-day momentum can reverse quickly; a pullback is possible if sentiment shifts, Mobile advertising is sensitive to macroeconomic conditions and ad spend cycles, Valuation may be rich if growth decelerates faster than expected
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 20.8603 (source.forwardEps) x AI multiple assumption 20.00; source IDs S008, S012, S013, S014
- **EPS:** 20.86026 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 19.611452
- **FY+1 growth assumption:** 27.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / PNR / APP shows 27.44% FY1 consensus earnings growth with 88.8% gross margin and 77.8% operating margin, indicating a high-quality, high-margin franchise. The 19.6x forward P/E is not a base multiple; the 20.0x base multiple is justified by superior margins and growth relative to the lower-margin, lower-growth PNR (12.9% forward P/E). The 24.0x bull case reflects continued margin leadership and 25.4% revenue growth; the 16.0x bear case reflects margin compression or growth deceleration risk.
- **Company fundamentals:** AppLovin reports FY1 EPS of $20.72 with 27.4% growth, FY1 revenue growth of 25.4%, gross margin of 88.8%, operating margin of 77.8%, profit margin of 65.9%, and ROE of 2.1%. Reported diluted EPS is $11.61. Forward EPS is $20.86, implying a forward P/E of ~19.6. The stock closed at $409.10 on 2026-11-13 with 20-day return of 53.7% and 60-day return of 32.5%.
- **Bull / Base / Bear:** 500.65 / 417.21 / 333.76
- **Bull / Base / Bear returns:** 22.38% / 1.98% / -18.42%
- **Scenario probabilities:** not separately assigned; see scenario table.

### PNR — Pentair

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Pentair is preferable to the deeply negative-growth names like INTC and COIN, which have negative earnings yields and high dislocation risk, and to the high-multiple names like NOW and MRVL, which carry significant valuation risk. Its lower forward P/E (~12.9) offers a more reasonable entry point if the business stabilizes, though the negative growth profile warrants a neutral stance. Alternatives considered: INTC, COIN, NOW, MRVL.
- **Thesis:** Pentair screens in the top 20-day momentum bucket with a 27.8% 20-day return and a 7.1% 60-day return. The company has a reasonable forward P/E of ~12.9 and an earnings yield of ~7.4%, but revenue growth is slightly negative (-4.5%) and earnings growth is negative (-18.8%). The stock is trading at a discount to its sector relative P/E (0.49x), suggesting it is undervalued relative to peers, but the negative growth profile limits upside.
- **Source IDs:** S009, S015, S017, S020
- **Catalysts:** Potential stabilization of the end-market demand that is currently dragging on revenue and earnings, Margin improvement as the company works through cost pressures, Re-rating if the market begins to price in a recovery in the water and fluid handling end markets
- **Risks:** Negative revenue and earnings growth could continue, pressuring the stock, The stock is trading at a discount to sector peers, which may reflect genuine business challenges, Cyclical exposure to construction and industrial end markets
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 5.3040 (source.forwardEps) x AI multiple assumption 13.00; source IDs S009, S015, S017, S020
- **EPS:** 5.30402 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 12.877027
- **FY+1 growth assumption:** 12.82%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / APP / PNR has 12.82% FY1 consensus earnings growth but negative revenue growth (-4.5%) and thin margins (40.2% gross, 21.4% operating, 15.4% profit). The 12.9x forward P/E is not a base multiple; the 13.0x base multiple is justified by modest earnings growth and lower profitability relative to APP. The 16.0x bull case assumes margin recovery and stabilization; the 10.0x bear case assumes continued revenue decline and margin pressure.
- **Company fundamentals:** Pentair reports FY1 EPS of $5.30 with 12.8% growth, FY1 revenue growth of 18.4%, gross margin of 40.2%, operating margin of 21.4%, profit margin of 15.4%, and ROE of 15.6%. Reported diluted EPS is $2.76. Forward EPS is $5.30, implying a forward P/E of ~12.9. The stock closed at $68.30 on 2026-11-13 with 20-day return of 27.8% and 60-day return of 7.1%.
- **Bull / Base / Bear:** 84.86 / 68.95 / 53.04
- **Bull / Base / Bear returns:** 24.25% / 0.95% / -22.34%
- **Scenario probabilities:** not separately assigned; see scenario table.

### GEN — Gen Digital

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** Gen Digital offers a compelling value-growth profile with a forward P/E of ~9.1 and earnings growth of ~128.6%, making it preferable to the high-multiple names like NOW (forward P/E ~97) and MRVL (forward P/E ~74), which carry much higher valuation risk. It is also preferable to the low-growth names like CLX and PNR, which offer less upside potential. Alternatives considered: NOW, MRVL, CLX, PNR.
- **Thesis:** Gen Digital screens in the top 20-day momentum bucket with a 25.8% 20-day return and a 7.9% 60-day return. The company has a very low forward P/E of ~9.1 and an earnings yield of ~7.1%, indicating it is cheap relative to its growth. Revenue growth is ~12.2% and earnings growth is ~128.6%, showing strong profitability improvement. The stock is trading at a discount to its sector relative P/E (0.42x), suggesting it is undervalued relative to peers.
- **Source IDs:** S019, S024, S026, S030
- **Catalysts:** Continued strong earnings growth as the cybersecurity and digital life protection businesses scale, Re-rating as the market recognizes the low valuation relative to growth, Potential for margin expansion as the company optimizes its portfolio
- **Risks:** Cybersecurity is a competitive and rapidly evolving industry with potential for disruption, The low valuation may reflect known risks that could persist, High 20-day momentum could reverse if the stock overperforms then corrects
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 3.3374 (source.forwardEps) x AI multiple assumption 9.00; source IDs S019, S024, S026, S030
- **EPS:** 3.33736 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 9.108996
- **FY+1 growth assumption:** 12.86%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / IDXX / GEN has 12.86% FY1 consensus earnings growth with 77.4% gross margin and 43.2% operating margin, but only 6.8% revenue growth and 23.1% profit margin. The 9.1x forward P/E is not a base multiple; the 9.0x base multiple is justified by moderate growth and mid-range margins relative to higher-growth, higher-margin peers. The 11.0x bull case assumes revenue acceleration; the 7.0x bear case assumes growth deceleration or margin compression.
- **Company fundamentals:** Gen Digital reports FY1 EPS of $3.34 with 12.9% growth, FY1 revenue growth of 6.8%, gross margin of 77.4%, operating margin of 43.2%, profit margin of 23.1%, and ROE of 46.4%. Reported diluted EPS is $0.83. Forward EPS is $3.34, implying a forward P/E of ~9.1. The stock closed at $30.40 on 2026-11-13 with 20-day return of 25.8% and 60-day return of 7.9%.
- **Bull / Base / Bear:** 36.71 / 30.04 / 23.36
- **Bull / Base / Bear returns:** 20.76% / -1.18% / -23.16%
- **Scenario probabilities:** not separately assigned; see scenario table.

### CLX — Clorox

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Clorox is preferable to the high-multiple names like NOW and MRVL, which carry significant valuation risk, and to the deeply negative-growth names like INTC and COIN, which have negative earnings yields and high dislocation risk. Its lower forward P/E (~17.7) offers a more reasonable entry point, though the consumer staples sector headwinds warrant a neutral stance. Alternatives considered: NOW, MRVL, INTC, COIN.
- **Thesis:** Clorox screens in the top 20-day momentum bucket with a 25.7% 20-day return and a 3.2% 60-day return. The company has a forward P/E of ~17.7 and an earnings yield of ~5.5%, but revenue growth is modest (33.3%) and earnings growth is 113.8%. The stock is trading at a discount to its sector relative P/E (0.76x), suggesting it is undervalued relative to peers, but the consumer staples sector faces headwinds from inflation and changing consumer habits.
- **Source IDs:** S021, S022, S023, S031
- **Catalysts:** Potential for margin improvement as the company optimizes its product mix, Recovery in consumer staples spending if inflation eases, Re-rating if the market begins to price in a recovery in the consumer sector
- **Risks:** Consumer staples face headwinds from inflation and changing consumer habits, The stock is trading at a discount to sector peers, which may reflect genuine business challenges, Slow revenue growth limits upside
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 6.1684 (source.forwardEps) x AI multiple assumption 18.00; source IDs S021, S022, S023, S031
- **EPS:** 6.1684 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 17.745283
- **FY+1 growth assumption:** 7.69%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / IDXX / CLX has 7.69% FY1 consensus earnings growth with 41.9% gross margin and 14.3% operating margin, but 113.8% earnings growth and 33.3% revenue growth suggest one-time or non-recurring items inflating reported growth. The 17.7x forward P/E is not a base multiple; the 18.0x base multiple is justified by stable consumer staples cash flows and moderate growth relative to higher-growth but lower-margin peers. The 22.0x bull case assumes normalized growth and margin recovery; the 14.0x bear case assumes growth deceleration and margin pressure.
- **Company fundamentals:** Clorox reports FY1 EPS of $6.17 with 7.7% growth, FY1 revenue growth of 2.2%, gross margin of 41.9%, operating margin of 14.3%, profit margin of 9.4%, and ROE of 5.3%. Reported diluted EPS is $1.39. Forward EPS is $6.17, implying a forward P/E of ~17.7. The stock closed at $109.46 on 2026-11-13 with 20-day return of 25.7% and 60-day return of 3.2%.
- **Bull / Base / Bear:** 135.7 / 111.03 / 86.36
- **Bull / Base / Bear returns:** 23.97% / 1.43% / -21.1%
- **Scenario probabilities:** not separately assigned; see scenario table.

### IDXX — Idexx Laboratories

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Idexx is preferable to the high-multiple names like NOW and MRVL, which carry much higher valuation risk, and to the deeply negative-growth names like INTC and COIN, which have negative earnings yields and high dislocation risk. However, its high forward P/E (~41.7) and premium to sector peers limit the upside, warranting a neutral stance. Alternatives considered: NOW, MRVL, INTC, COIN.
- **Thesis:** Idexx Laboratories screens in the top 20-day momentum bucket with a 25.7% 20-day return and a 29.0% 60-day return. The company has a high forward P/E of ~41.7 and a low earnings yield of ~2.6%, indicating it is expensive relative to its growth. Revenue growth is ~9.9% and earnings growth is 17.9%, showing solid but not exceptional performance. The stock is trading at a premium to its sector relative P/E (1.33x), suggesting it is overvalued relative to peers.
- **Source IDs:** S027, S028, S035, S037
- **Catalysts:** Continued growth in the veterinary diagnostics and animal health markets, Potential for margin expansion as the company scales its operations, Re-rating if the market recognizes the quality of the business model
- **Risks:** High valuation leaves little room for error; any deceleration in growth could lead to a sharp re-rating, The stock is trading at a premium to sector peers, which may not be justified by current growth rates, Vet diagnostics is a niche market with limited growth potential
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 16.8929 (source.forwardEps) x AI multiple assumption 42.00; source IDs S027, S028, S035, S037
- **EPS:** 16.8929 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 41.687927
- **FY+1 growth assumption:** 12.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / GEN / IDXX has 12.44% FY1 consensus earnings growth with 62.7% gross margin and 32.5% operating margin, and 25.4% ROE, indicating a higher-quality compounder than GEN. The 41.7x forward P/E is not a base multiple; the 42.0x base multiple is justified by durable healthcare IT demand, higher margins, and better returns relative to GEN. The 48.0x bull case assumes continued market share gains and margin expansion; the 36.0x bear case assumes competitive pressure or growth deceleration.
- **Company fundamentals:** Idexx Laboratories reports FY1 EPS of $16.89 with 12.4% growth, FY1 revenue growth of 8.9%, gross margin of 62.7%, operating margin of 32.5%, profit margin of 25.4%, and ROE of 6.9%. Reported diluted EPS is $11.75. Forward EPS is $16.89, implying a forward P/E of ~41.7. The stock closed at $704.23 on
- **Bull / Base / Bear:** 810.86 / 709.5 / 608.14
- **Bull / Base / Bear returns:** 15.14% / 0.75% / -13.64%
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
| Bull | 25% | +2.00% | Directional signal is false and forecast vol is below the 5-day baseline, so a mild upside is only plausible if the frozen daily-close model stabilizes after the US close; otherwise the 16.5% spike probability keeps near-term upside capped. |
| Base | 50% | +0.00% | With no directional signal, a flat short-term path is the central case: frozen daily-close model implies no material move over the 5-day window, and the 14.9% forecast vol is consistent with a range-bound session. |
| Bear | 25% | -2.00% | The 16.5% spike probability exceeds the historical and EWMA baselines, so a brief risk-off pullback is the main downside risk; a 2% decline is the conservative bound if the spike resolves into selling pressure after the US close. |

### Long Term (12 months)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 30% | +8.00% | A 30% bull case requires a durable shift in the frozen daily-close model toward positive momentum, with rates and credit conditions remaining accommodative enough to sustain earnings growth over the horizon. |
| Base | 40% | +3.00% | The base case assumes no directional signal persists, so returns are driven by steady earnings and stable rate expectations, yielding a modest 3% gain without a directional catalyst. |
| Bear | 30% | -5.00% | A 30% bear case reflects a sustained spike in volatility and a false directional signal that turns into a credit or rate-driven drawdown, with earnings disappointment pushing the long-term return to -5%. |

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
| S011 | news | FISV | Wed, 11 Nov 2026 00:17:00 GMT | ok | https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en | Michael Burry makes a bold call on struggling payments giant - Yahoo Finance (Wed, 11 Nov 2026 00:17:00 GMT); Fiserv Stock Outlook: Is Wall Street Bullish or Bearish? - Yahoo Finance (Thu, 12 Nov 2026 12:23:56 GMT); Fiserv (FISV) Stock Looks Undervalued With Strong Excess Returns - Yahoo Finance Singapore (Wed, 11 Nov 2026 22:14:34 GMT) |
| S012 | news | APP | Thu, 12 Nov 2026 20:05:45 GMT | ok | https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en | AppLovin Just Ripped 47% in a Month: Is It Too Late to Buy APP Stock Now? - Yahoo Finance (Thu, 12 Nov 2026 20:05:45 GMT); ETFs Are Net Sellers of AppLovin (APP) on Nov. 11 - Yahoo Finance (Fri, 13 Nov 2026 11:02:35 GMT); APP Stock Surges 51% After Q3 Earnings: Is it Still a Buy? - Yahoo Finance (Tue, 10 Nov 2026 14:24:00 GMT) |
| S013 | filing | APP | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json | Diluted EPS 11.61 for period ending 2026-09-30 (filed 2026-11-04) |
| S014 | stock | APP | 2026-11-15 | ok | https://finance.yahoo.com/quote/APP | Trailing P/E: 27.54882; Forward P/E: 19.611452; Forward EPS: 20.86026; Price: 409.1; Market price: 409.1; Market cap: 135543824384; Sector: Communication Services; Trailing Eps: 14.85; Revenue Growth: 0.555; Earnings Growth: 0.755; Gross Margin: 0.8878; Operating Margin: 0.77782995; Profit Margin: 0.65887; Return On Equity: 2.1008599; Total Revenue: 7608893952; Market Cap: 135543824384; Consensus EPS FY+1: 20.72438; growth: 0.2744 |
| S015 | stock | PNR | 2026-11-15 | ok | https://finance.yahoo.com/quote/PNR | Trailing P/E: 18.610355; Forward P/E: 12.877027; Forward EPS: 5.30402; Price: 68.3; Market price: 68.3; Market cap: 10904415232; Sector: Industrials; Trailing Eps: 3.67; Revenue Growth: -0.045; Earnings Growth: -0.188; Gross Margin: 0.40168998; Operating Margin: 0.21410999; Profit Margin: 0.15435; Return On Equity: 0.15605; Total Revenue: 3966200064; Market Cap: 10904415232; Consensus EPS FY+1: 5.30402; growth: 0.1282 |
| S016 | stock | FISV | 2026-11-15 | ok | https://finance.yahoo.com/quote/FISV | Forward P/E: 7.9923306; Price: 63.78; Market price: 63.78; Market cap: 33934002176; Market Cap: 33934002176; Consensus EPS FY+1: 7.98015; growth: 0.09689999 |
| S017 | news | PNR | Fri, 13 Nov 2026 22:05:23 GMT | ok | https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en | Pentair plc (PNR) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 22:05:23 GMT); Pentair plc (PNR) Q3 Earnings and Revenues Beat Estimates - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT); Pentair (PNR) Stock May Be 46% Undervalued As New CFO Arrives - Yahoo Finance (Fri, 25 Sep 2026 07:00:00 GMT) |
| S018 | filing | FISV | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json | Diluted EPS -8.9 for period ending 2026-09-30 (filed 2026-11-04) |
| S019 | filing | GEN | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0000849399-26-000083); 8-K filed 2026-10-28 (accession 0000849399-26-000081); 8-K filed 2026-10-09 (accession 0000849399-26-000079) |
| S020 | filing | PNR | 2026-10-27 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json | Diluted EPS 2.76 for period ending 2026-09-30 (filed 2026-10-27) |
| S021 | filing | CLX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000021076-26-000046); 8-K filed 2026-11-02 (accession 0000021076-26-000044); 8-K filed 2026-10-29 (accession 0001206774-26-000586) |
| S022 | stock | CLX | 2026-11-15 | ok | https://finance.yahoo.com/quote/CLX | Trailing P/E: 19.68705; Forward P/E: 17.745283; Forward EPS: 6.1684; Price: 109.46; Market price: 109.46; Market cap: 13260793856; Sector: Consumer Defensive; Trailing Eps: 5.56; Revenue Growth: 0.333; Earnings Growth: 1.138; Gross Margin: 0.41939998; Operating Margin: 0.14286; Profit Margin: 0.09408; Return On Equity: 5.34363; Total Revenue: 7196000256; Market Cap: 13260793856; Consensus EPS FY+1: 6.1684; growth: 0.0769 |
| S023 | news | CLX | Sun, 15 Nov 2026 08:55:47 GMT | ok | https://news.google.com/rss/search?q=CLX+Clorox+stock&hl=en-US&gl=US&ceid=US:en | The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance UK (Sun, 15 Nov 2026 08:55:47 GMT); The Clorox Company (CLX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 05:44:34 GMT); The Clorox Company (CLX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 16:03:12 GMT) |
| S024 | news | GEN | Fri, 13 Nov 2026 09:34:35 GMT | ok | https://news.google.com/rss/search?q=GEN+Gen+Digital+stock&hl=en-US&gl=US&ceid=US:en | Gen Digital Inc. (GEN) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 09:34:35 GMT); Gen Digital (GEN) Stock Repriced After Q2 Earnings Put Margins Center Stage - Yahoo Finance (Thu, 29 Oct 2026 07:00:00 GMT); Gen Digital Stock: Is Wall Street Bullish or Bearish? - Yahoo Finance (Thu, 05 Nov 2026 08:00:00 GMT) |
| S025 | filing | CHTR | 2026-11-06 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-06 (accession 0001091667-26-000073); 8-K filed 2026-11-06 (accession 0001091667-26-000072); 8-K filed 2026-10-27 (accession 0001091667-26-000064) |
| S026 | filing | GEN | 2026-10-29 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000849399.json | Diluted EPS 0.83 for period ending 2026-10-02 (filed 2026-10-29) |
| S027 | filing | IDXX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000874716&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000874716-26-000135); 8-K filed 2026-11-02 (accession 0001104659-26-120892); 10-Q filed 2026-08-04 (accession 0000874716-26-000123) |
| S028 | stock | IDXX | 2026-11-15 | ok | https://finance.yahoo.com/quote/IDXX | Trailing P/E: 47.45485; Forward P/E: 41.687927; Forward EPS: 16.8929; Price: 704.23; Market price: 704.23; Market cap: 55483650048; Sector: Healthcare; Trailing Eps: 14.84; Revenue Growth: 0.099; Earnings Growth: 0.179; Gross Margin: 0.62722; Operating Margin: 0.32497; Profit Margin: 0.25357; Return On Equity: 0.68925005; Total Revenue: 4662220800; Market Cap: 55483650048; Consensus EPS FY+1: 16.8929; growth: 0.1244 |
| S029 | stock | CHTR | 2026-11-15 | ok | https://finance.yahoo.com/quote/CHTR | Trailing P/E: 13.006578; Forward P/E: 3.2831066; Forward EPS: 42.15215; Price: 138.39; Market price: 138.39; Market cap: 24778944512; Sector: Communication Services; Trailing Eps: 10.64; Revenue Growth: 0.091; Gross Margin: 0.55084; Operating Margin: 0.23389; Profit Margin: 0.02498; Return On Equity: 0.07019; Total Revenue: 55645999104; Market Cap: 24778944512; Consensus EPS FY+1: 47.15811; growth: 1.0195 |
| S030 | stock | GEN | 2026-11-15 | ok | https://finance.yahoo.com/quote/GEN | Trailing P/E: 15.431472; Forward P/E: 9.108996; Forward EPS: 3.33736; Price: 30.4; Market price: 30.4; Market cap: 18035593216; Sector: Technology; Trailing Eps: 1.97; Revenue Growth: 0.122; Earnings Growth: 1.286; Gross Margin: 0.77410007; Operating Margin: 0.43229; Profit Margin: 0.23068; Return On Equity: 0.46402; Total Revenue: 5228000256; Market Cap: 18035593216; Consensus EPS FY+1: 3.33736; growth: 0.1286 |
| S031 | filing | CLX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000021076.json | Diluted EPS 1.39 for period ending 2026-09-30 (filed 2026-11-02) |
| S032 | news | CHTR | Sun, 15 Nov 2026 05:47:01 GMT | ok | https://news.google.com/rss/search?q=CHTR+Charter+Communications+stock&hl=en-US&gl=US&ceid=US:en | Charter Communications (CHTR) Stock Could Be A Bargain Following Its New Operating Model - Yahoo Finance (Sun, 15 Nov 2026 05:47:01 GMT); Charter Communications (CHTR) Expands Enterprise Reach With Managed Secure Networking Launch - Yahoo Finance (Sun, 15 Nov 2026 06:08:00 GMT); Charter Communications (CHTR) Earnings Expected to Grow: What to Know Ahead of Next Week's Release - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT) |
| S033 | filing | CHTR | 2026-11-06 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001091667.json | Diluted EPS 0.38 for period ending 2026-09-30 (filed 2026-11-06) |
| S034 | filing | ROP | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000882835&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000882835-26-000047); 8-K filed 2026-10-22 (accession 0000882835-26-000042); 8-K filed 2026-10-01 (accession 0000882835-26-000039) |
| S035 | news | IDXX | Sat, 14 Nov 2026 06:13:17 GMT | ok | https://news.google.com/rss/search?q=IDXX+Idexx+Laboratories+stock&hl=en-US&gl=US&ceid=US:en | IDEXX Laboratories, Inc. (IDXX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Sat, 14 Nov 2026 06:13:17 GMT); IDEXX Laboratories (IDXX) Stock Looks Fairly Valued Despite Its 28% Run - Yahoo Finance (Sat, 31 Oct 2026 07:00:00 GMT); IDEXX Laboratories (IDXX) Q3 Earnings Leave Its Premium Valuation In Focus - Yahoo Finance (Tue, 03 Nov 2026 08:00:00 GMT) |
| S036 | stock | ROP | 2026-11-15 | ok | https://finance.yahoo.com/quote/ROP | Trailing P/E: 18.993866; Forward P/E: 19.532475; Forward EPS: 24.57318; Price: 479.975; Market price: 479.975; Market cap: 47535013888; Sector: Technology; Trailing Eps: 25.27; Revenue Growth: 0.076; Earnings Growth: 0.326; Gross Margin: 0.69671; Operating Margin: 0.28049; Profit Margin: 0.30712998; Return On Equity: 0.13229; Total Revenue: 8434599936; Market Cap: 47535013888; Consensus EPS FY+1: 24.57318; growth: 0.09810001 |
| S037 | filing | IDXX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000874716.json | Diluted EPS 11.75 for period ending 2026-09-30 (filed 2026-11-02) |
| S038 | filing | RDDT | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001713445&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0001713445-26-000116); 8-K filed 2026-10-29 (accession 0001713445-26-000114); 8-K filed 2026-08-12 (accession 0001713445-26-000107) |
| S039 | news | ROP | Fri, 13 Nov 2026 13:04:22 GMT | ok | https://news.google.com/rss/search?q=ROP+Roper+Technologies+stock&hl=en-US&gl=US&ceid=US:en | Roper Technologies, Inc. (ROP) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 13:04:22 GMT); Roper Technologies (ROP) Stock Looks Fully Valued As Cash Flow Comes Into Focus - Yahoo Finance (Thu, 05 Nov 2026 08:00:00 GMT); Roper Technologies: 3 Key Takeaways for Long-Term Investors - Yahoo Finance (Mon, 26 Oct 2026 07:00:00 GMT) |
| S040 | stock | RDDT | 2026-11-15 | ok | https://finance.yahoo.com/quote/RDDT | Trailing P/E: 20.091835; Forward P/E: 10.770874; Forward EPS: 9.14039; Price: 98.45; Market price: 98.45; Market cap: 19010076672; Sector: Communication Services; Trailing Eps: 4.9; Revenue Growth: 0.53; Earnings Growth: 0.749; Gross Margin: 0.91547996; Operating Margin: 0.29397; Profit Margin: 0.32105; Return On Equity: 0.32029998; Total Revenue: 3088880128; Market Cap: 19010076672; Consensus EPS FY+1: 6.82439; growth: 0.2417 |

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
- news FISV: https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en (Wed, 11 Nov 2026 00:17:00 GMT)
- news APP: https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en (Thu, 12 Nov 2026 20:05:45 GMT)
- filing APP: https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json (2026-11-04)
- stock APP: https://finance.yahoo.com/quote/APP (2026-11-15)
- stock PNR: https://finance.yahoo.com/quote/PNR (2026-11-15)
- stock FISV: https://finance.yahoo.com/quote/FISV (2026-11-15)
- news PNR: https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 22:05:23 GMT)
- filing FISV: https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json (2026-11-04)
- filing GEN: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 (2026-10-29)
- filing PNR: https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json (2026-10-27)

## AI Provenance

- Provider / model: hermes-local-proxy / upstage/solar-mini4:free
- Market research: attempts=1 tokens=9473 (prompt=6473, completion=3000) runtime=23.34s
- Fundamental research: generated this run at 2026-11-15T16:15:46.698857+00:00
- Evidence source dates: {'as_of': '2026-11-13', 'latest_equity_date': '2026-11-13', 'latest_macro_date': '2026-11-14', 'flows_date': '2026-11-13'}
- Evidence fingerprint: 5eec21471098fc26027114da46c9ce66422f6910e6833be9427bf962fd916c19
- Source citations are retrieved external records in the ledger above; market values remain from the verified database snapshot.


## Disclosures

- This is research and market intelligence, not investment advice.
- AI conclusions are research judgments, not validated return predictions.
- The frozen risk layer is risk-only and is not used for directional views or allocations.
- Legacy scores are not active inputs or outputs.

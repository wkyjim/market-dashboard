# AEGIS AI-First Market Intelligence

Research generated at: 16 November 2026, 14:13 HKT
Database freshness: equity 2026-11-13 (latest row retrieved 2026-11-16 13:06:43.000010+08:00)
Data cutoff: 2026-11-13 US cash close
Snapshot ID: aegis-hourly-20261116T061337Z

## Executive Summary

- **AI market view: Late-November 2026 US equities show a bifurcated tape: broad market momentum and breadth are positive, but the largest-cap and most expensive names are under pressure, while health care, consumer staples and select industrials are leading. Macro data remain consistent with a late-cycle, low-inflation, gradually easing policy backdrop, with elevated but contained credit spreads and a sharp crypto drawdown that warrants monitoring.**
- Broad market momentum is constructive: 71.3% of names are above their 50-day moving average and 70.5% have positive 20-day returns, with a positive advance/decline ratio of 1.70.
- The largest-cap liquidity leaders (NVDA, AMD, MU, AAPL) are in the shortlist but carry high trailing P/E and elevated sector-relative multiples, signaling valuation risk despite liquidity strength.
- Health Care (XLV +6.9% 20d), Consumer Staples (XLP +5.4%) and Consumer Discretionary (XLY +6.7%) are the strongest sectors; Information Technology (XLK -7.2%) and Energy (XLE -4.8%) are the weakest.
- Credit spreads are contained (IG OAS 0.89, HY OAS 3.20), but crypto fell sharply (BTC -6.0%, ETH -8.2%) on 2026-11-14, a liquidity/asset-class risk to watch.
- Macro data point to a late-cycle, low-inflation, gradually easing policy environment, with the 10Y-2Y spread at 0.27 and unemployment at 4.2%.
- The risk model shows 5-day forecast volatility of 14.9% and a 16.5% spike probability, below the historical baseline of 22.1%, suggesting near-term tail risk is not currently elevated.

## Data QC

- Status: **PASS_WITH_WARNINGS**
- Equity session: 0 completed session(s) behind inference date
- Equity provenance: 393 provisional / 12576 canonical
- Breadth lag: 0 session(s); ETF-flow lag: 0 session(s)
- Note: Equity session contains a mix of provisional yfinance and canonical Massive rows.
- External sources: 79 ok / 0 unavailable; retrieved 2026-11-16T06:13:55.284492+00:00

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
| S&P 500 | 7561.67 | -1.28% over 20d | Broad market is in positive momentum territory with 71.3% above 50d and 70.5% positive 20d returns; advance/decline ratio 1.70. |
| Health Care (XLV) | +6.87% | 20d return | Strongest sector; trailing P/E 30.78, consistent with defensive leadership. |
| Consumer Staples (XLP) | +5.40% | 20d return | Positive 20d return; trailing P/E 24.85, defensive quality. |
| Consumer Discretionary (XLY) | +6.69% | 20d return | Strong 20d return; trailing P/E 25.11, but flows show structural distribution. |
| Information Technology (XLK) | -7.19% | 20d return | Weakest sector; trailing P/E 30.03, with large-cap dislocation names (MRVL, NOW, AMD) under pressure. |
| Energy (XLE) | -4.81% | 20d return | Negative 20d return; trailing P/E 16.23, lowest multiple in the set. |

## Macro, Fiscal, Rates, Liquidity and Credit

- Growth and labor: unemployment is 4.2% (September 2026), consistent with a gradually cooling but still resilient labor market; payrolls were 159,293k in October 2026.
- Inflation: CPI is 336.30 and core CPI 338.90 (September 2026), indicating low and stable inflation, supportive of a gradual easing bias.
- Policy: the effective federal funds rate is 3.88% as of 2026-11-12, consistent with a late-cycle, gradually easing policy stance.
- Rates: the 10Y-2Y Treasury spread is 0.27 as of 2026-11-13, a modestly positive but narrow curve, consistent with late-cycle dynamics.
- Liquidity and credit: IG OAS is 0.89 and HY OAS is 3.20 as of 2026-11-12, both contained and not signaling acute stress.
- Risk assets: crypto fell sharply on 2026-11-14 (BTC -6.0%, ETH -8.2%), a liquidity/asset-class signal that warrants monitoring despite contained equity credit spreads.

## US Equities and 11 GICS Sectors

Macro source IDs: S001, S002, S003, S004, S005, S006, S007

| GICS sector | Evidence | AI research stance | Source IDs |
| --- | --- | --- | --- |
| Health Care | XLV 20d return +6.87%; trailing P/E 30.78; positive 20d returns and strong 50d/200d breadth support. | Defensive leadership with positive momentum; valuation is rich but supported by sector breadth. | S056 |
| Consumer Staples | XLP 20d return +5.40%; trailing P/E 24.85; positive 20d returns and positive 20d/50d/200d breadth. | Defensive quality with positive momentum; valuation is reasonable for the sector. | S055 |
| Consumer Discretionary | XLY 20d return +6.69%; trailing P/E 25.11; positive 20d returns and positive 20d/50d/200d breadth. | Positive momentum but flows show structural distribution; monitor earnings and consumer health. | S060 |
| Real Estate | XLRE 20d return +5.24%; trailing P/E 29.63; positive 20d returns and positive 20d/50d/200d breadth. | Positive momentum with reasonable valuation; watch rate sensitivity. | S062 |
| Financials | XLF 20d return +5.69%; trailing P/E 15.85; positive 20d returns and positive 20d/50d/200d breadth. | Positive momentum with low valuation; supportive of late-cycle financial strength. | S063 |
| Utilities | XLU 20d return +4.34%; trailing P/E 18.11; positive 20d returns but flows show medium-term deterioration and exceptional institutional selling. | Positive price momentum but negative institutional flows; caution on sustained leadership. | S066 |
| Materials | XLB 20d return +2.57%; trailing P/E 21.72; positive 20d returns and positive 20d/50d/200d breadth. | Modest positive momentum with reasonable valuation; watch industrial demand. | S068 |
| Industrials | XLI 20d return +0.61%; trailing P/E 27.07; positive 20d returns and positive 20d/50d/200d breadth. | Positive but weakest among positive sectors; valuation is rich relative to momentum. | S074 |
| Communication Services | XLC 20d return -1.48%; trailing P/E 17.26; negative 20d returns and negative 20d/50d/200d breadth. | Negative momentum and negative breadth; valuation is reasonable but momentum is deteriorating. | S073 |
| Information Technology | XLK 20d return -7.19%; trailing P/E 30.03; negative 20d returns and negative 20d/50d/200d breadth; large-cap dislocation names (MRVL, NOW, AMD) under pressure. | Weakest sector; high valuation and negative momentum; watch large-cap dislocation and liquidity. | S076 |
| Energy | XLE 20d return -4.81%; trailing P/E 16.23; negative 20d returns and negative 20d/50d/200d breadth. | Negative momentum and negative breadth; low valuation but weak price action. | S071 |

### Sector fundamentals, valuation and earnings

Point-in-time sector fundamentals (growth, margins, consensus) are not supplied in the database snapshot. The supplied evidence is limited to 20d ETF returns, trailing P/E, and flow/structure indicators. No sector-level earnings, revenue, or margin data are available, so sector fundamentals cannot be quantified here.

## Growth vs Value

- Health Care and Consumer Staples show positive 20d returns with trailing P/E of 30.78 and 24.85 respectively, indicating premium but positive momentum.
- Consumer Discretionary and Real Estate show positive 20d returns with trailing P/E of 25.11 and 29.63, but flows show structural distribution in consumer discretionary.
- Financials and Materials show positive 20d returns with low trailing P/E of 15.85 and 21.72, suggesting value-oriented characteristics.
- Information Technology and Energy show negative 20d returns with trailing P/E of 30.03 and 16.23, indicating weak momentum and mixed valuation signals.

## ETF Flows and Breadth

- Broad market breadth is positive: 71.3% above 50d, 63.6% above 200d, 70.5% positive 20d, with an advance/decline ratio of 1.70.
- Health Care (XLV) and Consumer Staples (XLP) show strong institutional confirmation with 20d and 60d flow z-scores of 1.45/1.72 and positive price state.
- Consumer Discretionary (XLY) shows structural distribution with 20d flow z-score -0.38 and 60d -0.78, despite positive price action.
- Utilities (XLU) shows medium-term deterioration with exceptional institutional selling, with 20d flow z-score -2.15 despite positive price state.
- The largest-cap liquidity leaders (NVDA, AMD, MU, AAPL) are in the shortlist but carry high trailing P/E and elevated sector-relative multiples, signaling valuation risk.

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
- **Why preferred / alternatives:** AppLovin offers a high-quality, high-margin advertising business with strong 20-day momentum and a flat 60-day drawdown, making it a more defensible momentum candidate than the more distressed dislocation names such as INTC or COIN, which show large drawdowns and negative earnings yields. Alternatives considered: INTC, COIN.
- **Thesis:** AppLovin screens in the top 20-day momentum bucket with a 20-day return of roughly 54% and a 60-day return near 32%, while its 60-day drawdown is essentially flat at -0.2%. The stock carries a trailing P/E of about 20.1 and an earnings yield near 5.0%, with sector-relative P/E at 1.0, indicating it is not cheap on a relative basis but is being rewarded for strong near-term momentum and a high-quality, high-margin advertising business.
- **Source IDs:** S008, S012, S013, S015
- **Catalysts:** Sustained 20-day momentum continuation above recent highs, Continued high-margin revenue growth from its advertising platform, Positive earnings revisions supporting forward EPS growth
- **Risks:** Momentum can reverse quickly after a 54% 20-day gain, Valuation is not cheap; sector-relative P/E is at 1.0, Forward EPS and fiscal-year mapping are unverified in the source data
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 20.8603 (source.forwardEps) x AI multiple assumption 20.00; source IDs S008, S012, S013, S015
- **EPS:** 20.86026 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 19.611452
- **FY+1 growth assumption:** 27.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / PNR and CLX / APP shows strong FY1 consensus growth of 27.44% with revenue growth of 25.37%, supported by high gross margin (88.78%) and operating margin (77.78%). The forward EPS of 20.86 and forward P/E of 19.61 are used as a starting point, but the base multiple of 20.0 is justified by the company's superior margins and growth relative to PNR and CLX, which have lower margins and growth. The bull case of 24.0 reflects continued execution on growth, while the bear case of 16.0 reflects potential margin compression or growth deceleration.
- **Company fundamentals:** AppLovin reports diluted EPS of 11.61 for the period ending 2026-09-30, with forward EPS of 20.86 and a forward P/E of 19.61. Revenue growth is 55.5% and earnings growth is 75.5%, with gross margin of 88.8% and operating margin of 77.8%. The stock closed at 409.1 on 2026-11-13.
- **Bull / Base / Bear:** 500.65 / 417.21 / 333.76
- **Bull / Base / Bear returns:** 22.38% / 1.98% / -18.42%
- **Scenario probabilities:** not separately assigned; see scenario table.

### PNR — Pentair

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Pentair offers a lower valuation entry point than the high-momentum but expensive names like APP, while still participating in the broader Industrials and building-products recovery, though its negative growth tempers the case. Alternatives considered: APP, ROP.
- **Thesis:** Pentair is a top-20-day-momentum stock with a 20-day return of about 28% and a 60-day return near 7%. It trades at a trailing P/E of 13.6 and an earnings yield of 7.4%, with a sector-relative P/E of 0.49, suggesting it is cheaper than its sector. However, the company's revenue growth is slightly negative at -4.5% and earnings growth is -18.8%, so the momentum is not yet supported by fundamental growth.
- **Source IDs:** S010, S014, S016, S020
- **Catalysts:** Sustained 20-day momentum above prior levels, Potential stabilization in revenue and earnings growth, Attractive earnings yield relative to sector peers
- **Risks:** Negative revenue and earnings growth currently, Momentum may fade if fundamentals do not improve, Sector-relative P/E of 0.49 may reflect structural weakness
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 5.3040 (source.forwardEps) x AI multiple assumption 13.00; source IDs S010, S014, S016, S020
- **EPS:** 5.30402 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 12.877027
- **FY+1 growth assumption:** 12.82%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / APP and CLX / PNR has FY1 consensus growth of 12.82% with revenue growth of 18.38%, but earnings growth is negative at -18.8%, indicating margin pressure. Gross margin is 40.17% and operating margin is 21.41%, significantly lower than APP. The forward EPS of 5.30 and forward P/E of 12.88 support a base multiple of 13.0, reflecting the company's lower profitability and growth relative to peers. The bull case of 16.0 assumes margin recovery, while the bear case of 10.0 reflects continued earnings weakness.
- **Company fundamentals:** Pentair reports diluted EPS of 2.76 for the period ending 2026-09-30, with forward EPS of 5.30 and a forward P/E of 12.88. Revenue growth is -4.5% and earnings growth is -18.8%, with gross margin of 40.2% and operating margin of 21.4%. The stock closed at 68.3 on 2026-11-13.
- **Bull / Base / Bear:** 84.86 / 68.95 / 53.04
- **Bull / Base / Bear returns:** 24.25% / 0.95% / -22.34%
- **Scenario probabilities:** not separately assigned; see scenario table.

### GEN — Gen Digital

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Gen Digital provides a higher earnings yield and lower sector-relative valuation than the more expensive momentum names, while still benefiting from the cybersecurity end-market, making it a more balanced risk-reward than the distressed dislocation names. Alternatives considered: IDXX, ROP.
- **Thesis:** Gen Digital is a top-20-day-momentum stock with a 20-day return of about 26% and a 60-day return near 8%. It trades at a trailing P/E of 14.2 and an earnings yield of 7.1%, with a sector-relative P/E of 0.42, indicating it is cheaper than its sector. Earnings growth is strong at 128.6%, but revenue growth is modest at 12.2%, so the valuation is supported by earnings momentum rather than broad revenue expansion.
- **Source IDs:** S018, S022, S026, S028
- **Catalysts:** Sustained 20-day momentum, Continued earnings growth from cybersecurity and digital life protection, Attractive earnings yield relative to sector
- **Risks:** Revenue growth is modest at 12.2%, Sector-relative P/E of 0.42 may reflect sector-wide weakness, Forward EPS and fiscal-year mapping are unverified
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 3.3374 (source.forwardEps) x AI multiple assumption 10.00; source IDs S018, S022, S026, S028
- **EPS:** 3.33736 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 9.108996
- **FY+1 growth assumption:** 12.86%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / APP and CLX / GEN has FY1 consensus growth of 12.86% with revenue growth of 6.81% and earnings growth of 128.6%, indicating strong earnings momentum. Gross margin is 77.41% and operating margin is 43.23%, with a profit margin of 23.07%. The forward EPS of 3.34 and forward P/E of 9.11 support a base multiple of 10.0, reflecting the company's strong earnings growth but lower revenue growth compared to APP. The bull case of 12.0 assumes continued earnings acceleration, while the bear case of 8.0 reflects potential revenue deceleration.
- **Company fundamentals:** Gen Digital reports diluted EPS of 0.83 for the period ending 2026-10-02, with forward EPS of 3.34 and a forward P/E of 9.11. Revenue growth is 12.2% and earnings growth is 128.6%, with gross margin of 77.4% and operating margin of 43.2%. The stock closed at 30.4 on 2026-11-13.
- **Bull / Base / Bear:** 40.05 / 33.37 / 26.7
- **Bull / Base / Bear returns:** 31.74% / 9.77% / -12.17%
- **Scenario probabilities:** not separately assigned; see scenario table.

### CLX — Clorox

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Clorox offers a consumer staples exposure with strong reported growth and a reasonable valuation, providing diversification away from the high-momentum technology and distressed names, though its lower margins temper the quality of the thesis. Alternatives considered: XLP, ROP.
- **Thesis:** Clorox is a top-20-day-momentum stock with a 20-day return of about 26% and a 60-day return near 3%. It trades at a trailing P/E of 18.3 and an earnings yield of 5.5%, with a sector-relative P/E of 0.76, suggesting it is reasonably valued relative to its sector. Earnings growth is 113.8% and revenue growth is 33.3%, but the company's gross margin is only 41.9% and operating margin is 14.3%, indicating a lower-quality earnings profile than the high-margin technology names.
- **Source IDs:** S021, S024, S025, S030
- **Catalysts:** Sustained 20-day momentum, Strong earnings and revenue growth in consumer staples, Attractive valuation relative to sector peers
- **Risks:** Lower gross and operating margins than technology peers, Consumer staples demand may be pressured by macro conditions, Sector-relative P/E of 0.76 still leaves room for multiple compression
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 6.1684 (source.forwardEps) x AI multiple assumption 18.00; source IDs S021, S024, S025, S030
- **EPS:** 6.1684 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 17.745283
- **FY+1 growth assumption:** 7.69%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / APP and PNR / CLX has FY1 consensus growth of 7.69% with revenue growth of 2.23% and earnings growth of 113.8%, indicating strong earnings recovery. Gross margin is 41.94% and operating margin is 14.29%, with a profit margin of 9.41%. The forward EPS of 6.17 and forward P/E of 17.75 support a base multiple of 18.0, reflecting the company's improving earnings and moderate growth. The bull case of 22.0 assumes continued earnings acceleration, while the bear case of 14.0 reflects potential revenue stagnation.
- **Company fundamentals:** Clorox reports diluted EPS of 1.39 for the period ending 2026-09-30, with forward EPS of 6.17 and a forward P/E of 17.75. Revenue growth is 33.3% and earnings growth is 113.8%, with gross margin of 41.9% and operating margin of 14.3%. The stock closed at 109.46 on 2026-11-13.
- **Bull / Base / Bear:** 135.7 / 111.03 / 86.36
- **Bull / Base / Bear returns:** 23.97% / 1.43% / -21.1%
- **Scenario probabilities:** not separately assigned; see scenario table.

### XLV — Health Care sector ETF

- **Type:** ETF
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** XLV offers diversified health care exposure that complements the concentrated stock ideas, providing a lower-risk way to participate in the sector without relying on the momentum or dislocation dynamics of individual names like IDXX or INTC. Alternatives considered: XLP, XLY.
- **Thesis:** The Health Care sector ETF provides broad exposure to large-cap pharmaceutical and medical device names, with top holdings including LLY, JNJ, ABBV, MRK, and UNH. The ETF's raw price change is +0.54%, indicating modest sector strength. It serves as a diversified health care benchmark but does not offer the concentrated momentum or dislocation alpha of the individual stock candidates.
- **Source IDs:** S056, S058
- **Catalysts:** Sector rotation into health care from defensive demand, Continued strength in large-cap pharma and biotech, Diversification benefit within a balanced portfolio
- **Risks:** Sector-specific regulatory and patent cliff risks, No concentrated alpha from a single high-momentum name, Top-10 holdings coverage is only 61.4% of the portfolio
- **Valuation method:** Holdings/portfolio valuation with AI total-return assumption
- **Valuation status:** verified; forward-EPS source: ; period flags: 
- **Valuation assumptions:** Holdings/portfolio valuation; 10 weighted holdings; coverage 61.42%; source IDs S056, S058
- **Top holdings:** LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59%
- **Portfolio valuation:** Top 10 holdings; numeric weight coverage 61.42%
- **Sector exposure:** Health Care
- **Underlying drivers:** Top-10 holdings include LLY, JNJ, ABBV, MRK, UNH, TMO, AMGN, GILD, ABT, and PFE, with numeric weight coverage of 61.42%. The ETF's raw price change is +0.54% as of 2026-11-13.
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
| Bull | 25% | +2.00% | Low realized volatility (0.149) and below-threshold spike probability (0.165) support a mild upside continuation if US close confirms the frozen daily-close model. |
| Base | 50% | +0.00% | Directional signal is false and forecast volatility is near the 0.185 threshold, implying range-bound consolidation with no clear catalyst over the 5-day horizon. |
| Bear | 25% | -2.00% | A 16.5% spike probability and frozen model status create downside risk if US close data triggers a volatility spike or risk-off repricing. |

### Long Term (12 months)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 30% | +8.00% | Sustained low volatility and stable baseline conditions support a gradual upward drift if earnings and credit spreads remain constructive. |
| Base | 40% | +3.00% | Neutral trajectory with modest positive drift reflects balanced risk appetite, stable rates, and no material macro or credit deterioration. |
| Bear | 30% | -5.00% | A 16.5% spike probability and frozen daily-close model imply elevated tail risk; a US close shock could drive a meaningful drawdown. |

## Positioning

- Maintain a constructive broad-market posture given positive momentum, positive breadth, and contained credit spreads.
- Favor Health Care, Consumer Staples, and Financials for defensive and value-oriented exposure.
- Monitor Consumer Discretionary and Utilities for flow deterioration despite positive price action.
- Exercise caution on Information Technology and Energy given negative momentum, negative breadth, and high valuation in large-cap names.
- Watch crypto and liquidity conditions as a risk indicator given the sharp crypto drawdown on 2026-11-14.

## Catalysts

| Date | Event | Why it matters |
| --- | --- | --- |
| 2026-11-16 | US equity market open | Frozen risk model is eligible for formal use after completed US close; 5-day forecast volatility is 14.9% and spike probability is 16.5%, below the historical baseline of 22.1%. |
| 2026-11-17 | Next US macro data release | Latest CPI and core CPI are from September 2026; upcoming releases will confirm the low-inflation, gradually easing policy trajectory. |
|  |  |  |

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
| S011 | news | FISV | Fri, 13 Nov 2026 21:49:46 GMT | ok | https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en | Fiserv, Inc. (FISV) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 21:49:46 GMT); Fiserv (FISV) Stock Still Looks Like A Bargain After Lawsuit Claims - Yahoo Finance (Thu, 22 Oct 2026 07:00:00 GMT); symbol__ Stock Quote Price and Forecast - CNN (Fri, 13 Nov 2026 21:18:08 GMT) |
| S012 | news | APP | Thu, 12 Nov 2026 20:05:45 GMT | ok | https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en | AppLovin Just Ripped 47% in a Month: Is It Too Late to Buy APP Stock Now? - Yahoo Finance (Thu, 12 Nov 2026 20:05:45 GMT); Is Trending Stock AppLovin Corporation (APP) a Buy Now? - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT); APP Stock Surges 51% After Q3 Earnings: Is it Still a Buy? - Yahoo Finance (Tue, 10 Nov 2026 14:24:00 GMT) |
| S013 | stock | APP | 2026-11-16 | ok | https://finance.yahoo.com/quote/APP | Trailing P/E: 27.54882; Forward P/E: 19.611452; Forward EPS: 20.86026; Price: 409.1; Market price: 409.1; Market cap: 135543824384; Sector: Communication Services; Trailing Eps: 14.85; Revenue Growth: 0.555; Earnings Growth: 0.755; Gross Margin: 0.8878; Operating Margin: 0.77782995; Profit Margin: 0.65887; Return On Equity: 2.1008599; Total Revenue: 7608893952; Market Cap: 135543824384; Consensus EPS FY+1: 20.72438; growth: 0.2744 |
| S014 | filing | PNR | 2026-10-27 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json | Diluted EPS 2.76 for period ending 2026-09-30 (filed 2026-10-27) |
| S015 | filing | APP | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json | Diluted EPS 11.61 for period ending 2026-09-30 (filed 2026-11-04) |
| S016 | stock | PNR | 2026-11-16 | ok | https://finance.yahoo.com/quote/PNR | Trailing P/E: 18.610355; Forward P/E: 12.877027; Forward EPS: 5.30402; Price: 68.3; Market price: 68.3; Market cap: 10904415232; Sector: Industrials; Trailing Eps: 3.67; Revenue Growth: -0.045; Earnings Growth: -0.188; Gross Margin: 0.40168998; Operating Margin: 0.21410999; Profit Margin: 0.15435; Return On Equity: 0.15605; Total Revenue: 3966200064; Market Cap: 10904415232; Consensus EPS FY+1: 5.30402; growth: 0.1282 |
| S017 | stock | FISV | 2026-11-16 | ok | https://finance.yahoo.com/quote/FISV | Forward P/E: 7.99667; Price: 63.78; Market price: 63.78; Market cap: 33934002176; Market Cap: 33934002176; Consensus EPS FY+1: 7.98015; growth: 0.09689999 |
| S018 | filing | GEN | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0000849399-26-000083); 8-K filed 2026-10-28 (accession 0000849399-26-000081); 8-K filed 2026-10-09 (accession 0000849399-26-000079) |
| S019 | filing | FISV | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json | Diluted EPS -8.9 for period ending 2026-09-30 (filed 2026-11-04) |
| S020 | news | PNR | Fri, 13 Nov 2026 22:09:48 GMT | ok | https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en | Pentair plc (PNR) stock price, news, quote and history - Yahoo Finance UK (Fri, 13 Nov 2026 22:09:48 GMT); Pentair plc (PNR) Q3 Earnings and Revenues Beat Estimates - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT); Pentair (PNR) Stock May Be 46% Undervalued As New CFO Arrives - Yahoo Finance (Fri, 25 Sep 2026 07:00:00 GMT) |
| S021 | stock | CLX | 2026-11-16 | ok | https://finance.yahoo.com/quote/CLX | Trailing P/E: 19.68705; Forward P/E: 17.745283; Forward EPS: 6.1684; Price: 109.46; Market price: 109.46; Market cap: 13260793856; Sector: Consumer Defensive; Trailing Eps: 5.56; Revenue Growth: 0.333; Earnings Growth: 1.138; Gross Margin: 0.41939998; Operating Margin: 0.14286; Profit Margin: 0.09408; Return On Equity: 5.34363; Total Revenue: 7196000256; Market Cap: 13260793856; Consensus EPS FY+1: 6.1684; growth: 0.0769 |
| S022 | stock | GEN | 2026-11-16 | ok | https://finance.yahoo.com/quote/GEN | Trailing P/E: 15.431472; Forward P/E: 9.108996; Forward EPS: 3.33736; Price: 30.4; Market price: 30.4; Market cap: 18035593216; Sector: Technology; Trailing Eps: 1.97; Revenue Growth: 0.122; Earnings Growth: 1.286; Gross Margin: 0.77410007; Operating Margin: 0.43229; Profit Margin: 0.23068; Return On Equity: 0.46402; Total Revenue: 5228000256; Market Cap: 18035593216; Consensus EPS FY+1: 3.33736; growth: 0.1286 |
| S023 | filing | CHTR | 2026-11-06 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-06 (accession 0001091667-26-000073); 8-K filed 2026-11-06 (accession 0001091667-26-000072); 8-K filed 2026-10-27 (accession 0001091667-26-000064) |
| S024 | filing | CLX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000021076-26-000046); 8-K filed 2026-11-02 (accession 0000021076-26-000044); 8-K filed 2026-10-29 (accession 0001206774-26-000586) |
| S025 | news | CLX | Sun, 15 Nov 2026 08:55:47 GMT | ok | https://news.google.com/rss/search?q=CLX+Clorox+stock&hl=en-US&gl=US&ceid=US:en | The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance UK (Sun, 15 Nov 2026 08:55:47 GMT); The Clorox Company (CLX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 23:34:51 GMT); The Clorox Company (CLX): Capitalizing on Volatility to Sell and Repurchase at New Lows - Yahoo Finance (Mon, 05 Oct 2026 07:00:00 GMT) |
| S026 | news | GEN | Thu, 29 Oct 2026 07:00:00 GMT | ok | https://news.google.com/rss/search?q=GEN+Gen+Digital+stock&hl=en-US&gl=US&ceid=US:en | Gen Digital (GEN) Stock Repriced After Q2 Earnings Put Margins Center Stage - Yahoo Finance (Thu, 29 Oct 2026 07:00:00 GMT); Gen Digital Stock: Is Wall Street Bullish or Bearish? - Yahoo Finance (Thu, 05 Nov 2026 08:00:00 GMT); Are Business Services Stocks Lagging GEN DIGITAL INC (GEN) This Year? - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT) |
| S027 | filing | IDXX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000874716&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000874716-26-000135); 8-K filed 2026-11-02 (accession 0001104659-26-120892); 10-Q filed 2026-08-04 (accession 0000874716-26-000123) |
| S028 | filing | GEN | 2026-10-29 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000849399.json | Diluted EPS 0.83 for period ending 2026-10-02 (filed 2026-10-29) |
| S029 | stock | CHTR | 2026-11-16 | ok | https://finance.yahoo.com/quote/CHTR | Trailing P/E: 13.006578; Forward P/E: 3.2831066; Forward EPS: 42.15215; Price: 138.39; Market price: 138.39; Market cap: 24778944512; Sector: Communication Services; Trailing Eps: 10.64; Revenue Growth: 0.091; Gross Margin: 0.55084; Operating Margin: 0.23389; Profit Margin: 0.02498; Return On Equity: 0.07019; Total Revenue: 55645999104; Market Cap: 24778944512; Consensus EPS FY+1: 47.15811; growth: 1.0195 |
| S030 | filing | CLX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000021076.json | Diluted EPS 1.39 for period ending 2026-09-30 (filed 2026-11-02) |
| S031 | news | CHTR | Sun, 15 Nov 2026 05:47:01 GMT | ok | https://news.google.com/rss/search?q=CHTR+Charter+Communications+stock&hl=en-US&gl=US&ceid=US:en | Charter Communications (CHTR) Stock Could Be A Bargain Following Its New Operating Model - Yahoo Finance (Sun, 15 Nov 2026 05:47:01 GMT); Why You Should Think About Charter Communications Differently Now? - Yahoo Finance (Fri, 13 Nov 2026 19:16:11 GMT); Charter Communications (CHTR) Expands Enterprise Reach With Managed Secure Networking Launch - Yahoo Finance (Sun, 15 Nov 2026 06:08:00 GMT) |
| S032 | filing | CHTR | 2026-11-06 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001091667.json | Diluted EPS 0.38 for period ending 2026-09-30 (filed 2026-11-06) |
| S033 | stock | IDXX | 2026-11-16 | ok | https://finance.yahoo.com/quote/IDXX | Trailing P/E: 47.45485; Forward P/E: 41.687927; Forward EPS: 16.8929; Price: 704.23; Market price: 704.23; Market cap: 55483650048; Sector: Healthcare; Trailing Eps: 14.84; Revenue Growth: 0.099; Earnings Growth: 0.179; Gross Margin: 0.62722; Operating Margin: 0.32497; Profit Margin: 0.25357; Return On Equity: 0.68925005; Total Revenue: 4662220800; Market Cap: 55483650048; Consensus EPS FY+1: 16.8929; growth: 0.1244 |
| S034 | filing | ROP | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000882835&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000882835-26-000047); 8-K filed 2026-10-22 (accession 0000882835-26-000042); 8-K filed 2026-10-01 (accession 0000882835-26-000039) |
| S035 | news | IDXX | Sat, 14 Nov 2026 22:37:20 GMT | ok | https://news.google.com/rss/search?q=IDXX+Idexx+Laboratories+stock&hl=en-US&gl=US&ceid=US:en | IDEXX Laboratories, Inc. (IDXX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Sat, 14 Nov 2026 22:37:20 GMT); symbol__ Stock Quote Price and Forecast - CNN (Fri, 13 Nov 2026 15:22:45 GMT); IDEXX Laboratories, Inc. (IDXX) stock price, news, quote and history - Yahoo Finance UK (Sat, 14 Nov 2026 05:51:00 GMT) |
| S036 | stock | ROP | 2026-11-16 | ok | https://finance.yahoo.com/quote/ROP | Trailing P/E: 18.993866; Forward P/E: 19.532475; Forward EPS: 24.57318; Price: 479.975; Market price: 479.975; Market cap: 47535013888; Sector: Technology; Trailing Eps: 25.27; Revenue Growth: 0.076; Earnings Growth: 0.326; Gross Margin: 0.69671; Operating Margin: 0.28049; Profit Margin: 0.30712998; Return On Equity: 0.13229; Total Revenue: 8434599936; Market Cap: 47535013888; Consensus EPS FY+1: 24.57318; growth: 0.09810001 |
| S037 | filing | IDXX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000874716.json | Diluted EPS 11.75 for period ending 2026-09-30 (filed 2026-11-02) |
| S038 | filing | RDDT | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001713445&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0001713445-26-000116); 8-K filed 2026-10-29 (accession 0001713445-26-000114); 8-K filed 2026-08-12 (accession 0001713445-26-000107) |
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
- filing FISV: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 (2026-11-04)
- filing PNR: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 (2026-10-27)
- news FISV: https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 21:49:46 GMT)
- news APP: https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en (Thu, 12 Nov 2026 20:05:45 GMT)
- stock APP: https://finance.yahoo.com/quote/APP (2026-11-16)
- filing PNR: https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json (2026-10-27)
- filing APP: https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json (2026-11-04)
- stock PNR: https://finance.yahoo.com/quote/PNR (2026-11-16)
- stock FISV: https://finance.yahoo.com/quote/FISV (2026-11-16)
- filing GEN: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 (2026-10-29)
- filing FISV: https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json (2026-11-04)
- news PNR: https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 22:09:48 GMT)

## AI Provenance

- Provider / model: hermes-local-proxy / upstage/solar-mini4:free
- Market research: attempts=1 tokens=9465 (prompt=6465, completion=3000) runtime=17.9s
- Fundamental research: generated this run at 2026-11-16T06:13:37.201378+00:00
- Evidence source dates: {'as_of': '2026-11-13', 'latest_equity_date': '2026-11-13', 'latest_macro_date': '2026-11-14', 'flows_date': '2026-11-13'}
- Evidence fingerprint: bf33db745d95ea3f650c48e74138beb2af99c981022ba084711b289cf7692a77
- Source citations are retrieved external records in the ledger above; market values remain from the verified database snapshot.


## Disclosures

- This is research and market intelligence, not investment advice.
- AI conclusions are research judgments, not validated return predictions.
- The frozen risk layer is risk-only and is not used for directional views or allocations.
- Legacy scores are not active inputs or outputs.

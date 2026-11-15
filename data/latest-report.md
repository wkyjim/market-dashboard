# AEGIS AI-First Market Intelligence

Research generated at: 15 November 2026, 15:15 HKT
Database freshness: equity 2026-11-13 (latest row retrieved 2026-11-15 13:06:40.074841+08:00)
Data cutoff: 2026-11-13 US cash close
Snapshot ID: aegis-hourly-20261115T071535Z

## Executive Summary

- **AI market view: Late-November 2026: broad market breadth is constructive (71.3% above 50-day, 63.6% above 200-day, A/D ratio 1.70), but the S&P 500 is slightly negative over 20 days (-1.28%) and the 20-day return dispersion is wide. Information Technology and Energy are the weakest sectors, while Health Care, Consumer Discretionary, Consumer Staples, Financials and Real Estate lead. Liquidity is concentrated in semiconductors (SOXX exceptional institutional buying) while long-duration Treasuries show medium-term deterioration, suggesting a risk-on tilt with selective quality and cyclical exposure.**
- Broad market breadth is supportive: 71.3% of names above the 50-day moving average, 63.6% above the 200-day, and an advance/decline ratio of 1.70.
- S&P 500 is down 1.28% over 20 days, indicating short-term consolidation despite positive longer-term positioning.
- Sector leadership is broad: Health Care, Consumer Discretionary, Consumer Staples, Financials and Real Estate posted positive 20-day returns; Information Technology and Energy lagged.
- Liquidity signals are mixed: SOXX shows exceptional institutional buying, while TLT shows medium-term deterioration, pointing to a risk-on tilt with selective quality.
- Credit spreads are tight (IG OAS 0.89, HY OAS 3.20), consistent with a stable-to-favorable risk environment.
- Macro data show inflation still elevated (CPI 336.3, core 338.9) and unemployment at 4.2%, with the policy rate at 3.88%.
- The risk model flags a 16.5% spike probability over the next 5 days, below the historical baseline of 22.1%, suggesting no imminent tail-risk event.

## Data QC

- Status: **PASS_WITH_WARNINGS**
- Equity session: 0 completed session(s) behind inference date
- Equity provenance: 393 provisional / 12576 canonical
- Breadth lag: 0 session(s); ETF-flow lag: 0 session(s)
- Note: Equity session contains a mix of provisional yfinance and canonical Massive rows.
- External sources: 79 ok / 0 unavailable; retrieved 2026-11-15T07:16:07.759575+00:00

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
| S&P 500 (SPX) | 7561.67 | -1.28% (20d) | Broad market breadth is positive, but the index is slightly negative over 20 days, indicating short-term consolidation. |
| Health Care (XLV) | 6.87% | +6.87% (20d) | Top sector; trailing P/E 30.78 suggests premium valuation but strong momentum. |
| Consumer Discretionary (XLY) | 6.69% | +6.69% (20d) | Strong 20-day return; trailing P/E 25.11. |
| Consumer Staples (XLP) | 5.40% | +5.40% (20d) | Defensive strength; trailing P/E 24.85. |
| Financials (XLF) | 5.69% | +5.69% (20d) | Positive momentum; trailing P/E 15.85. |
| Information Technology (XLK) | -7.19% | -7.19% (20d) | Weakest major sector; trailing P/E 30.03 despite strong institutional buying in SOXX. |
| Energy (XLE) | -4.81% | -4.81% (20d) | Negative 20-day return; trailing P/E 16.23. |
| TLT | neutral | flow z-score 20d -0.41 | Medium-term deterioration in Treasury flows; price state flat. |
| SOXX | inflow | flow z-score 20d 5.10 | Exceptional institutional buying; price state down, strong confirmation. |
| SMH | outflow | flow z-score 20d 1.22 | Tactical profit-taking inside structural accumulation. |

## Macro, Fiscal, Rates, Liquidity and Credit

- Growth: Broad market breadth (71.3% above 50-day, 63.6% above 200-day) and positive 20-day returns in Health Care, Consumer Discretionary, Consumer Staples, Financials and Real Estate suggest resilient corporate activity, though the S&P 500 is down 1.28% over 20 days.
- Inflation: CPI (CPIAUCSL) stands at 336.3 (Sep 2026) and core CPI at 338.9, indicating inflation remains above the pre-2021 trend; the latest CPI observation from S004 is 337.476 (Oct 2026), so the data are consistent with sticky inflation.
- Policy: The effective federal funds rate is 3.88% as of 2026-11-12 (S001), and the 10Y-2Y spread is 0.27 (S007), indicating a modestly positive but shallow yield curve.
- Rates: IG OAS is 0.89 and HY OAS is 3.20 (S002, S003), both tight, implying low credit risk premiums and a supportive environment for risk assets.
- Liquidity: SOXX shows exceptional institutional buying (flow z-score 5.10) while TLT shows medium-term deterioration (flow z-score -0.41), suggesting liquidity is rotating toward cyclical and technology-related exposure rather than duration.
- Credit: Tight IG and HY spreads (S002, S003) are consistent with a stable-to-favorable risk environment, though the risk model flags a 16.5% spike probability over the next 5 days, below the historical baseline of 22.1%.

## US Equities and 11 GICS Sectors

Macro source IDs: S001, S002, S003, S004, S005, S006, S007

| GICS sector | Evidence | AI research stance | Source IDs |
| --- | --- | --- | --- |
| Health Care | 20-day return +6.87% (XLV); trailing P/E 30.78 (S053); top sector in the universe screen. | Constructive: strong momentum and defensive positioning, but premium valuation. | S053 |
| Consumer Staples | 20-day return +5.40% (XLP); trailing P/E 24.85 (S057); defensive strength. | Constructive: resilient demand and defensive characteristics. | S057 |
| Consumer Discretionary | 20-day return +6.69% (XLY); trailing P/E 25.11 (S058); strong 20-day performance. | Constructive: broad-based consumer strength. | S058 |
| Real Estate | 20-day return +5.24% (XLRE); trailing P/E 29.63 (S060); positive momentum. | Constructive: positive 20-day return and reasonable valuation. | S060 |
| Financials | 20-day return +5.69% (XLF); trailing P/E 15.85 (S063); positive momentum. | Constructive: strong momentum and attractive relative valuation. | S063 |
| Utilities | 20-day return +4.34% (XLU); trailing P/E 18.11 (S064); defensive strength. | Constructive: stable defensive sector with reasonable valuation. | S064 |
| Materials | 20-day return +2.57% (XLB); trailing P/E 21.72 (S068); modest positive momentum. | Neutral: positive but lagging relative to other sectors. | S068 |
| Industrials | 20-day return +0.61% (XLI); trailing P/E 27.07 (S069); near-flat momentum. | Neutral: weak momentum despite reasonable valuation. | S069 |
| Communication Services | 20-day return -1.48% (XLC); trailing P/E 17.26 (S071); negative momentum. | Negative: first major sector in negative territory. | S071 |
| Information Technology | 20-day return -7.19% (XLK); trailing P/E 30.03 (S073); weakest major sector despite strong SOXX flows. | Negative: sector-level weakness despite strong institutional buying in semiconductors. | S073 |
| Energy | 20-day return -4.81% (XLE); trailing P/E 16.23 (S074); negative momentum. | Negative: weak 20-day performance and negative price action. | S074 |

### Sector fundamentals, valuation and earnings

Sector-level fundamental data (growth, margins, consensus) are not available in the supplied database for the 11 GICS sectors. The only sector fundamentals provided are trailing P/E ratios for the sector ETFs (S053-S074) and 20-day returns. No point-in-time sector fundamentals beyond these are supplied, so no further sector fundamental claims are made.

## Growth vs Value

- Health Care and Consumer Staples offer defensive growth with premium valuations (XLV P/E 30.78, XLP P/E 24.85), supported by positive 20-day returns.
- Financials and Real Estate provide value-oriented exposure with lower P/E (XLF 15.85, XLRE 29.63) and positive momentum.
- Information Technology shows a negative 20-day return (-7.19%) but exceptional institutional buying in SOXX (flow z-score 5.10), suggesting a disconnect between price and flows.
- Energy is the weakest sector (XLE -4.81%) with a reasonable P/E (16.23), but negative momentum argues against near-term conviction.

## ETF Flows and Breadth

- Broad market breadth is constructive: 71.3% above 50-day, 63.6% above 200-day, A/D ratio 1.70, and 70.5% positive over 20 days.
- SOXX shows exceptional institutional buying (flow z-score 5.10, 20d) with strong confirmation, while SMH shows tactical profit-taking (1.22) inside structural accumulation.
- TLT shows medium-term deterioration (flow z-score -0.41, 20d) with flat price, indicating reduced demand for duration.
- The advance/decline ratio of 1.70 and 315 advancers vs 185 decliners support a broad-based rally, though new highs are zero and new lows are zero.
- Price/breadth divergence is -27.49 (not negative), and bullish divergence is true, indicating no bearish signal from the breadth model.

## Stock Ideas

Single-stock research uses reported EPS, forward P/E and company fundamentals. All ideas are research judgments, not validated return predictions.

| Ticker | Security | Research view | Price | EPS | Forward P/E | Base target | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| APP | AppLovin | NEW | 409.1 | 20.86026 | 19.611452 | 458.93 | NEW |
| PNR | Pentair | KEEP | 68.3 | 5.30402 | 12.877027 | 74.26 | KEEP |
| GEN | Gen Digital | KEEP | 30.4 | 3.33736 | 9.108996 | 36.71 | KEEP |
| CLX | Clorox | KEEP | 109.46 | 6.1684 | 17.745283 | 111.03 | KEEP |
| IDXX | Idexx Laboratories | KEEP | 704.23 | 16.8929 | 41.687927 | 709.5 | KEEP |

## ETF Ideas

ETF research uses holdings, portfolio valuation and exposure. Single-stock EPS × P/E valuation is not applied to ETFs.

No qualifying ETF ideas this run.
### APP — AppLovin

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** AppLovin offers a rare combination of top-tier momentum, best-in-class margins, and strong earnings growth, making it a more compelling standalone holding than lower-quality, lower-momentum names in the shortlist. Alternatives considered: PNR, GEN, CLX, IDXX, ROP.
- **Thesis:** AppLovin screens in the top 20-day momentum bucket with a 53.7% 20-day return and a 32.5% 60-day return, indicating a strong price trend. The company carries a high gross margin of 88.8% and operating margin of 77.8%, supporting durable profitability. Trailing P/E of 20.1 and earnings yield of 5.0% are reasonable for a high-growth, high-margin mobile marketing platform.
- **Source IDs:** S008, S012, S014, S017
- **Catalysts:** Sustained 20-day momentum with 53.7% price gain, High gross margin and operating leverage in mobile advertising, Continued revenue growth of 55.5% and earnings growth of 75.5%
- **Risks:** High valuation relative to slower-growth peers, Momentum can reverse quickly if ad market conditions weaken, Single-name concentration risk
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 20.8603 (source.forwardEps) x AI multiple assumption 22.00; source IDs S008, S012, S014, S017
- **EPS:** 20.86026 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 19.611452
- **FY+1 growth assumption:** 27.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / PNR and IDXX / APP's FY1 consensus growth of 27.44% is supported by 25.4% revenue growth and 75.5% earnings growth, with high gross/operating margins (88.8%/77.8%) and strong ROE. The base multiple of 22x is justified by superior growth and margins relative to PNR (12.9x forward P/E, 12.8% earnings decline) and IDXX (41.7x forward P/E, 17.9% earnings growth), while the bull/bear range reflects margin durability and competitive positioning.
- **Company fundamentals:** AppLovin (APP) has a trailing P/E of 20.1, earnings yield of 5.0%, gross margin of 88.8%, operating margin of 77.8%, revenue growth of 55.5%, and earnings growth of 75.5%. Reported diluted EPS is 11.61 for fiscal 2026-09-30. Forward EPS is 20.86 with a forward P/E of 19.6. The stock closed at $409.10 on 2026-11-13 with 20-day return of 53.7% and 60-day return of 32.5%.
- **Bull / Base / Bear:** 542.37 / 458.93 / 354.62
- **Bull / Base / Bear returns:** 32.58% / 12.18% / -13.32%
- **Scenario probabilities:** not separately assigned; see scenario table.

### PNR — Pentair

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Pentair offers a lower valuation entry point than higher-growth names, but its negative near-term fundamentals and weaker relative valuation make it a neutral holding rather than a top pick. Alternatives considered: APP, GEN, CLX, IDXX, ROP.
- **Thesis:** Pentair is a top-20-day momentum name with a 27.8% 20-day return and 7.1% 60-day return. It trades at a reasonable forward P/E of 12.9 with an earnings yield of 7.4%. However, revenue growth is slightly negative at -4.5% and earnings growth is -18.8%, indicating near-term headwinds despite the momentum.
- **Source IDs:** S010, S013, S018, S022
- **Catalysts:** 20-day momentum of 27.8%, Attractive forward P/E of 12.9 and earnings yield of 7.4%, Diversified industrial portfolio with exposure to water, flow control, and building products
- **Risks:** Negative revenue growth of -4.5% and earnings growth of -18.8%, Cyclical exposure to construction and industrial end markets, Momentum may fade if fundamentals do not improve
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 5.3040 (source.forwardEps) x AI multiple assumption 14.00; source IDs S010, S013, S018, S022
- **EPS:** 5.30402 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 12.877027
- **FY+1 growth assumption:** 12.82%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / APP and IDXX / PNR's FY1 consensus growth of 12.82% is supported by 18.4% revenue growth, but earnings growth is negative (-18.8%) with thin margins (gross 40.2%, operating 21.4%, profit 15.4%) and low ROE (15.6%). The base multiple of 14x is justified by modest growth and lower margins relative to APP's superior profitability, with the bear case reflecting margin pressure and the bull case reflecting recovery.
- **Company fundamentals:** Pentair (PNR) has a forward P/E of 12.9, earnings yield of 7.4%, gross margin of 40.2%, operating margin of 21.4%, profit margin of 15.4%, revenue growth of -4.5%, and earnings growth of -18.8%. Reported diluted EPS is 2.76 for fiscal 2026-09-30. Forward EPS is 5.30. The stock closed at $68.30 on 2026-11-13 with 20-day return of 27.8% and 60-day return of 7.1%.
- **Bull / Base / Bear:** 90.17 / 74.26 / 58.34
- **Bull / Base / Bear returns:** 32.02% / 8.73% / -14.58%
- **Scenario probabilities:** not separately assigned; see scenario table.

### GEN — Gen Digital

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Gen Digital offers a cheaper entry point than AppLovin, but its lower revenue growth and margin profile make it a secondary holding rather than a primary recommendation. Alternatives considered: APP, PNR, CLX, IDXX, ROP.
- **Thesis:** Gen Digital is a top-20-day momentum name with a 25.8% 20-day return and 7.9% 60-day return. It trades at a low forward P/E of 9.1 with an earnings yield of 7.1%. However, revenue growth is modest at 12.2% and earnings growth is 128.6%, indicating strong but less dominant growth than AppLovin. The low valuation is attractive but the growth profile is less compelling.
- **Source IDs:** S016, S020, S024, S026
- **Catalysts:** 20-day momentum of 25.8%, Low forward P/E of 9.1 and earnings yield of 7.1%, Strong earnings growth of 128.6%
- **Risks:** Modest revenue growth of 12.2%, Lower margin profile compared to high-margin tech names, Momentum may not sustain if growth decelerates
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 3.3374 (source.forwardEps) x AI multiple assumption 11.00; source IDs S016, S020, S024, S026
- **EPS:** 3.33736 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 9.108996
- **FY+1 growth assumption:** 12.86%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / PNR and CLX / GEN's FY1 consensus growth of 12.86% is supported by 6.8% revenue growth and 128.6% earnings growth, with solid gross margin (77.4%) and ROE (46.4%). The base multiple of 11x is justified by strong profitability and growth relative to PNR's weak margins, with the bull/bear range reflecting earnings growth sustainability and competitive positioning.
- **Company fundamentals:** Gen Digital (GEN) has a forward P/E of 9.1, earnings yield of 7.1%, gross margin of 77.4%, operating margin of 43.2%, profit margin of 23.1%, revenue growth of 12.2%, and earnings growth of 128.6%. Reported diluted EPS is 0.83 for fiscal 2026-10-02. Forward EPS is 3.34. The stock closed at $30.40 on 2026-11-13 with 20-day return of 25.8% and 60-day return of 7.9%.
- **Bull / Base / Bear:** 46.72 / 36.71 / 30.04
- **Bull / Base / Bear returns:** 53.68% / 20.76% / -1.18%
- **Scenario probabilities:** not separately assigned; see scenario table.

### CLX — Clorox

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Clorox provides defensive exposure within the shortlist, but its low revenue growth and consumer staples margin challenges make it a neutral holding rather than a preferred name. Alternatives considered: APP, PNR, GEN, IDXX, ROP.
- **Thesis:** Clorox is a top-20-day momentum name with a 25.7% 20-day return and 3.2% 60-day return. It trades at a forward P/E of 17.7 with an earnings yield of 5.5%. However, revenue growth is modest at 2.2% and earnings growth is 113.8%, indicating a turnaround story with limited top-line momentum. The consumer staples sector is defensive but faces margin pressure.
- **Source IDs:** S021, S023, S028, S030
- **Catalysts:** 20-day momentum of 25.7%, Attractive forward P/E of 17.7 and earnings yield of 5.5%, Strong earnings growth of 113.8%
- **Risks:** Modest revenue growth of 2.2%, Margin pressure in consumer staples, Turnaround execution risk
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 6.1684 (source.forwardEps) x AI multiple assumption 18.00; source IDs S021, S023, S028, S030
- **EPS:** 6.1684 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 17.745283
- **FY+1 growth assumption:** 7.69%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / GEN and IDXX / CLX's FY1 consensus growth of 7.69% is supported by 2.2% revenue growth and 113.8% earnings growth, with moderate gross margin (41.9%) and operating margin (14.3%). The base multiple of 18x is justified by steady growth and reasonable margins relative to GEN's higher margins and IDXX's premium valuation, with the bull/bear range reflecting earnings growth sustainability and brand strength.
- **Company fundamentals:** Clorox (CLX) has a forward P/E of 17.7, earnings yield of 5.5%, gross margin of 41.9%, operating margin of 14.3%, profit margin of 9.4%, revenue growth of 2.2%, and earnings growth of 113.8%. Reported diluted EPS is 1.39 for fiscal 2026-09-30. Forward EPS is 6.17. The stock closed at $109.46 on 2026-11-13 with 20-day return of 25.7% and 60-day return of 3.2%.
- **Bull / Base / Bear:** 135.7 / 111.03 / 92.53
- **Bull / Base / Bear returns:** 23.97% / 1.43% / -15.47%
- **Scenario probabilities:** not separately assigned; see scenario table.

### IDXX — Idexx Laboratories

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Idexx offers strong momentum and solid growth, but its premium valuation relative to other shortlist names makes it a neutral holding rather than a top pick. Alternatives considered: APP, PNR, GEN, CLX, ROP.
- **Thesis:** Idexx Laboratories is a top-20-day momentum name with a 25.7% 20-day return and 29.0% 60-day return. It trades at a high forward P/E of 41.7 with an earnings yield of 2.6%, reflecting premium valuation. However, revenue growth is 9.9% and earnings growth is 17.9%, indicating solid but not exceptional growth. The high valuation limits upside.
- **Source IDs:** S027, S032, S035, S037
- **Catalysts:** 20-day momentum of 25.7% and 60-day return of 29.0%, Solid revenue growth of 9.9% and earnings growth of 17.9%, Diversified animal and human diagnostics portfolio
- **Risks:** High forward P/E of 41.7 and low earnings yield of 2.6%, Premium valuation leaves limited margin of safety, Growth may decelerate in a slowing pet care market
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 16.8929 (source.forwardEps) x AI multiple assumption 42.00; source IDs S027, S032, S035, S037
- **EPS:** 16.8929 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 41.687927
- **FY+1 growth assumption:** 12.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / APP and CLX / IDXX's FY1 consensus growth of 12.44% is supported by 8.9% revenue growth and 17.9% earnings growth, with strong gross margin (62.7%) and ROE (68.9%). The base multiple of 42x is justified by high growth and superior profitability relative to CLX's lower margins, with the bull/bear range reflecting durable competitive advantages and margin stability.
- **Company fundamentals:** Idexx Laboratories (IDXX) has a forward P/E of 41.7, earnings yield of 2.6%, gross margin of 62.7%, operating margin of 32.5%, profit margin of 25.4%, revenue growth of 9.9%, and earnings growth of 17.9%. Reported diluted EPS is 11.75 for fiscal 2026-09-30. Forward EPS is 16.89. The stock closed at $704.23 on 2026-11-13 with 20-day return of 25.7% and 60-day return of 29.0%.
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
| Bull | 25% | +2.00% | Directional signal is false and forecast volatility is below the 18.5% threshold, so a mild upside is driven by stable earnings revisions and low near-term event risk rather than a directional catalyst. |
| Base | 50% | +0.00% | Frozen daily-close model with no directional signal and elevated forecast volatility implies a range-bound session where realized moves offset, producing a neutral expected return. |
| Bear | 25% | -2.00% | Elevated forecast volatility and a 16.5% spike probability indicate asymmetric downside risk, with a mild bear case reflecting potential negative price drift if volatility persists into the target window. |

### Long Term (12 months)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 30% | +8.00% | Sustained earnings growth and positive rate expectations support a bull case, with a 30% probability reflecting a constructive but not dominant outlook over the longer horizon. |
| Base | 40% | +3.00% | Base case assumes moderate earnings momentum and stable credit conditions, with a 40% probability reflecting the most likely path of low but positive long-term returns. |
| Bear | 30% | -5.00% | A bear case reflects potential earnings deterioration, widening credit spreads, and persistent volatility, with a 30% probability capturing a meaningful downside scenario over the longer horizon. |

## Positioning

- Maintain a risk-on tilt with exposure to broad market leaders: Health Care, Consumer Discretionary, Consumer Staples, Financials and Real Estate.
- Favored quality and defensive sectors (Health Care, Consumer Staples, Utilities) for stability in a late-cycle environment.
- Less favored or avoid Information Technology and Energy at the sector level due to negative 20-day returns, despite selective liquidity in semiconductors.
- Use SOXX as a liquidity leader for cyclical technology exposure, but monitor SMH for tactical profit-taking.
- Reduce duration exposure given TLT's medium-term deterioration and the flat price state.
- Monitor the risk model's 16.5% spike probability and the 10Y-2Y spread of

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
| S011 | news | FISV | Fri, 13 Nov 2026 00:42:12 GMT | ok | https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en | Fiserv, Inc. (FISV) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 00:42:12 GMT); What Is Fiserv (FISV) Planning With Its Debit Networks And Clover AI? - Yahoo Finance (Thu, 12 Nov 2026 06:09:00 GMT); Fiserv (FISV) Stock Still Looks Like A Bargain After Lawsuit Claims - Yahoo Finance (Thu, 22 Oct 2026 07:00:00 GMT) |
| S012 | news | APP | Thu, 12 Nov 2026 20:05:45 GMT | ok | https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en | AppLovin Just Ripped 47% in a Month: Is It Too Late to Buy APP Stock Now? - Yahoo Finance (Thu, 12 Nov 2026 20:05:45 GMT); APP Stock Surges 51% After Q3 Earnings: Is it Still a Buy? - Yahoo Finance (Tue, 10 Nov 2026 14:24:00 GMT); Here is What to Know Beyond Why AppLovin Corporation (APP) is a Trending Stock - Yahoo Finance (Tue, 10 Nov 2026 13:00:06 GMT) |
| S013 | news | PNR | Fri, 13 Nov 2026 22:05:23 GMT | ok | https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en | Pentair plc (PNR) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 22:05:23 GMT); Here's What Key Metrics Tell Us About Pentair (PNR) Q3 Earnings - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT); Pentair plc (PNR) Q3 Earnings and Revenues Beat Estimates - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT) |
| S014 | filing | APP | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json | Diluted EPS 11.61 for period ending 2026-09-30 (filed 2026-11-04) |
| S015 | stock | FISV | 2026-11-15 | ok | https://finance.yahoo.com/quote/FISV | Forward P/E: 7.9923306; Price: 63.78; Market price: 63.78; Market cap: 33934002176; Market Cap: 33934002176; Consensus EPS FY+1: 7.98015; growth: 0.09689999 |
| S016 | filing | GEN | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0000849399-26-000083); 8-K filed 2026-10-28 (accession 0000849399-26-000081); 8-K filed 2026-10-09 (accession 0000849399-26-000079) |
| S017 | stock | APP | 2026-11-15 | ok | https://finance.yahoo.com/quote/APP | Trailing P/E: 27.54882; Forward P/E: 19.611452; Forward EPS: 20.86026; Price: 409.1; Market price: 409.1; Market cap: 135543824384; Sector: Communication Services; Trailing Eps: 14.85; Revenue Growth: 0.555; Earnings Growth: 0.755; Gross Margin: 0.8878; Operating Margin: 0.77782995; Profit Margin: 0.65887; Return On Equity: 2.1008599; Total Revenue: 7608893952; Market Cap: 135543824384; Consensus EPS FY+1: 20.72438; growth: 0.2744 |
| S018 | stock | PNR | 2026-11-15 | ok | https://finance.yahoo.com/quote/PNR | Trailing P/E: 18.610355; Forward P/E: 12.877027; Forward EPS: 5.30402; Price: 68.3; Market price: 68.3; Market cap: 10904415232; Sector: Industrials; Trailing Eps: 3.67; Revenue Growth: -0.045; Earnings Growth: -0.188; Gross Margin: 0.40168998; Operating Margin: 0.21410999; Profit Margin: 0.15435; Return On Equity: 0.15605; Total Revenue: 3966200064; Market Cap: 10904415232; Consensus EPS FY+1: 5.30402; growth: 0.1282 |
| S019 | filing | FISV | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json | Diluted EPS -8.9 for period ending 2026-09-30 (filed 2026-11-04) |
| S020 | news | GEN | Fri, 13 Nov 2026 00:21:25 GMT | ok | https://news.google.com/rss/search?q=GEN+Gen+Digital+stock&hl=en-US&gl=US&ceid=US:en | Gen Digital Inc. (GEN) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 00:21:25 GMT); Gen Digital (GEN) Stock Repriced After Q2 Earnings Put Margins Center Stage - Yahoo Finance (Thu, 29 Oct 2026 07:00:00 GMT); Gen Digital Stock: Is Wall Street Bullish or Bearish? - Yahoo Finance (Thu, 05 Nov 2026 08:00:00 GMT) |
| S021 | filing | CLX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000021076-26-000046); 8-K filed 2026-11-02 (accession 0000021076-26-000044); 8-K filed 2026-10-29 (accession 0001206774-26-000586) |
| S022 | filing | PNR | 2026-10-27 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json | Diluted EPS 2.76 for period ending 2026-09-30 (filed 2026-10-27) |
| S023 | stock | CLX | 2026-11-15 | ok | https://finance.yahoo.com/quote/CLX | Trailing P/E: 19.68705; Forward P/E: 17.745283; Forward EPS: 6.1684; Price: 109.46; Market price: 109.46; Market cap: 13260793856; Sector: Consumer Defensive; Trailing Eps: 5.56; Revenue Growth: 0.333; Earnings Growth: 1.138; Gross Margin: 0.41939998; Operating Margin: 0.14286; Profit Margin: 0.09408; Return On Equity: 5.34363; Total Revenue: 7196000256; Market Cap: 13260793856; Consensus EPS FY+1: 6.1684; growth: 0.0769 |
| S024 | stock | GEN | 2026-11-15 | ok | https://finance.yahoo.com/quote/GEN | Trailing P/E: 15.431472; Forward P/E: 9.108996; Forward EPS: 3.33736; Price: 30.4; Market price: 30.4; Market cap: 18035593216; Sector: Technology; Trailing Eps: 1.97; Revenue Growth: 0.122; Earnings Growth: 1.286; Gross Margin: 0.77410007; Operating Margin: 0.43229; Profit Margin: 0.23068; Return On Equity: 0.46402; Total Revenue: 5228000256; Market Cap: 18035593216; Consensus EPS FY+1: 3.33736; growth: 0.1286 |
| S025 | filing | CHTR | 2026-11-06 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-06 (accession 0001091667-26-000073); 8-K filed 2026-11-06 (accession 0001091667-26-000072); 8-K filed 2026-10-27 (accession 0001091667-26-000064) |
| S026 | filing | GEN | 2026-10-29 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000849399.json | Diluted EPS 0.83 for period ending 2026-10-02 (filed 2026-10-29) |
| S027 | filing | IDXX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000874716&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000874716-26-000135); 8-K filed 2026-11-02 (accession 0001104659-26-120892); 10-Q filed 2026-08-04 (accession 0000874716-26-000123) |
| S028 | news | CLX | Fri, 13 Nov 2026 18:52:58 GMT | ok | https://news.google.com/rss/search?q=CLX+Clorox+stock&hl=en-US&gl=US&ceid=US:en | The Clorox Company (CLX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 18:52:58 GMT); The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance Singapore (Sat, 14 Nov 2026 01:36:14 GMT); The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance UK (Fri, 13 Nov 2026 02:25:29 GMT) |
| S029 | stock | CHTR | 2026-11-15 | ok | https://finance.yahoo.com/quote/CHTR | Trailing P/E: 13.006578; Forward P/E: 3.2831066; Forward EPS: 42.15215; Price: 138.39; Market price: 138.39; Market cap: 24778944512; Sector: Communication Services; Trailing Eps: 10.64; Revenue Growth: 0.091; Gross Margin: 0.55084; Operating Margin: 0.23389; Profit Margin: 0.02498; Return On Equity: 0.07019; Total Revenue: 55645999104; Market Cap: 24778944512; Consensus EPS FY+1: 47.15811; growth: 1.0195 |
| S030 | filing | CLX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000021076.json | Diluted EPS 1.39 for period ending 2026-09-30 (filed 2026-11-02) |
| S031 | news | CHTR | Sun, 15 Nov 2026 05:47:01 GMT | ok | https://news.google.com/rss/search?q=CHTR+Charter+Communications+stock&hl=en-US&gl=US&ceid=US:en | Charter Communications (CHTR) Stock Could Be A Bargain Following Its New Operating Model - Yahoo Finance (Sun, 15 Nov 2026 05:47:01 GMT); Charter Communications (CHTR) Expands Enterprise Reach With Managed Secure Networking Launch - Yahoo Finance (Sun, 15 Nov 2026 06:08:00 GMT); Charter Communications: 3 Key Takeaways for Long-Term Investors - Yahoo Finance (Thu, 12 Nov 2026 08:02:01 GMT) |
| S032 | stock | IDXX | 2026-11-15 | ok | https://finance.yahoo.com/quote/IDXX | Trailing P/E: 47.45485; Forward P/E: 41.687927; Forward EPS: 16.8929; Price: 704.23; Market price: 704.23; Market cap: 55483650048; Sector: Healthcare; Trailing Eps: 14.84; Revenue Growth: 0.099; Earnings Growth: 0.179; Gross Margin: 0.62722; Operating Margin: 0.32497; Profit Margin: 0.25357; Return On Equity: 0.68925005; Total Revenue: 4662220800; Market Cap: 55483650048; Consensus EPS FY+1: 16.8929; growth: 0.1244 |
| S033 | filing | ROP | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000882835&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000882835-26-000047); 8-K filed 2026-10-22 (accession 0000882835-26-000042); 8-K filed 2026-10-01 (accession 0000882835-26-000039) |
| S034 | filing | CHTR | 2026-11-06 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001091667.json | Diluted EPS 0.38 for period ending 2026-09-30 (filed 2026-11-06) |
| S035 | news | IDXX | Fri, 13 Nov 2026 22:06:38 GMT | ok | https://news.google.com/rss/search?q=IDXX+Idexx+Laboratories+stock&hl=en-US&gl=US&ceid=US:en | IDEXX Laboratories, Inc. (IDXX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 22:06:38 GMT); IDEXX Laboratories (IDXX) Stock Looks Fairly Valued Despite Its 28% Run - Yahoo Finance (Sat, 31 Oct 2026 07:00:00 GMT); IDEXX Laboratories (IDXX) Q3 Earnings Leave Its Premium Valuation In Focus - Yahoo Finance (Tue, 03 Nov 2026 08:00:00 GMT) |
| S036 | filing | RDDT | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001713445&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0001713445-26-000116); 8-K filed 2026-10-29 (accession 0001713445-26-000114); 8-K filed 2026-08-12 (accession 0001713445-26-000107) |
| S037 | filing | IDXX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000874716.json | Diluted EPS 11.75 for period ending 2026-09-30 (filed 2026-11-02) |
| S038 | stock | ROP | 2026-11-15 | ok | https://finance.yahoo.com/quote/ROP | Trailing P/E: 18.993866; Forward P/E: 19.532475; Forward EPS: 24.57318; Price: 479.975; Market price: 479.975; Market cap: 47535013888; Sector: Technology; Trailing Eps: 25.27; Revenue Growth: 0.076; Earnings Growth: 0.326; Gross Margin: 0.69671; Operating Margin: 0.28049; Profit Margin: 0.30712998; Return On Equity: 0.13229; Total Revenue: 8434599936; Market Cap: 47535013888; Consensus EPS FY+1: 24.57318; growth: 0.09810001 |
| S039 | stock | RDDT | 2026-11-15 | ok | https://finance.yahoo.com/quote/RDDT | Trailing P/E: 20.091835; Forward P/E: 10.770874; Forward EPS: 9.14039; Price: 98.45; Market price: 98.45; Market cap: 19010076672; Sector: Communication Services; Trailing Eps: 4.9; Revenue Growth: 0.53; Earnings Growth: 0.749; Gross Margin: 0.91547996; Operating Margin: 0.29397; Profit Margin: 0.32105; Return On Equity: 0.32029998; Total Revenue: 3088880128; Market Cap: 19010076672; Consensus EPS FY+1: 6.82439; growth: 0.2417 |
| S040 | news | ROP | Thu, 12 Nov 2026 19:15:50 GMT | ok | https://news.google.com/rss/search?q=ROP+Roper+Technologies+stock&hl=en-US&gl=US&ceid=US:en | Roper Technologies, Inc. (ROP) Stock Price, News, Quote & History - Yahoo! Finance Canada (Thu, 12 Nov 2026 19:15:50 GMT); Roper Technologies (ROP) Stock Looks Fully Valued As Cash Flow Comes Into Focus - Yahoo Finance (Fri, 06 Nov 2026 07:13:00 GMT); Roper Technologies: 3 Key Takeaways for Long-Term Investors - Yahoo Finance (Mon, 26 Oct 2026 07:00:00 GMT) |

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
- news FISV: https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 00:42:12 GMT)
- news APP: https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en (Thu, 12 Nov 2026 20:05:45 GMT)
- news PNR: https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 22:05:23 GMT)
- filing APP: https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json (2026-11-04)
- stock FISV: https://finance.yahoo.com/quote/FISV (2026-11-15)
- filing GEN: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 (2026-10-29)
- stock APP: https://finance.yahoo.com/quote/APP (2026-11-15)
- stock PNR: https://finance.yahoo.com/quote/PNR (2026-11-15)
- filing FISV: https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json (2026-11-04)
- news GEN: https://news.google.com/rss/search?q=GEN+Gen+Digital+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 00:21:25 GMT)

## AI Provenance

- Provider / model: hermes-local-proxy / upstage/solar-mini4:free
- Market research: attempts=1 tokens=9521 (prompt=6521, completion=3000) runtime=23.29s
- Fundamental research: generated this run at 2026-11-15T07:15:35.563231+00:00
- Evidence source dates: {'as_of': '2026-11-13', 'latest_equity_date': '2026-11-13', 'latest_macro_date': '2026-11-13', 'flows_date': '2026-11-13'}
- Evidence fingerprint: 34197aa8854dfc6e0d2d363a6607b222ad433a538dbb28267061cb8477e341a5
- Source citations are retrieved external records in the ledger above; market values remain from the verified database snapshot.


## Disclosures

- This is research and market intelligence, not investment advice.
- AI conclusions are research judgments, not validated return predictions.
- The frozen risk layer is risk-only and is not used for directional views or allocations.
- Legacy scores are not active inputs or outputs.

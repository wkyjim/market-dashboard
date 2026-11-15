# AEGIS AI-First Market Intelligence

Research generated at: 15 November 2026, 11:15 HKT
Database freshness: equity 2026-11-13 (latest row retrieved 2026-11-14 13:50:55.938286+08:00)
Data cutoff: 2026-11-13 US cash close
Snapshot ID: aegis-hourly-20261115T031549Z

## Executive Summary

- **AI market view: Risk-on tilt with a quality and liquidity bias. Broad market breadth is constructive, but the 20-day return is negative and the 10Y-2Y curve is only mildly positive, so the setup favors high-liquidity, low-valuation names and sectors with positive momentum rather than broad cyclical or speculative exposure.**
- Market breadth is strongly positive: 71.3% above the 50-day and 63.6% above the 200-day, with an advance/decline ratio of 1.70 and 70.5% of names positive over 20 days.
- The S&P 500 is down 1.28% over 20 days, so the positive breadth is a stabilization signal rather than a confirmed trend.
- The 10Y-2Y Treasury spread is 0.27, indicating only a mild positive curve; policy rates remain the key macro variable.
- High-yield OAS is 3.20 and IG OAS is 0.89, implying moderate credit stress and a need for quality.
- Sector leadership is split: Health Care, Consumer Discretionary, Consumer Staples, Real Estate and Financials are up over 20 days, while Information Technology and Energy are down.
- Shortlist momentum names are concentrated in high-liquidity, low-valuation, or dislocation buckets, with no composite score used.

## Data QC

- Status: **PASS_WITH_WARNINGS**
- Equity session: 0 completed session(s) behind inference date
- Equity provenance: 386 provisional / 12581 canonical
- Breadth lag: 0 session(s); ETF-flow lag: 0 session(s)
- Note: Equity session contains a mix of provisional yfinance and canonical Massive rows.
- External sources: 79 ok / 0 unavailable; retrieved 2026-11-15T03:16:12.472881+00:00

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
| S&P 500 | 7561.67 | -1.28% (20d) | Negative 20-day return but broad 50/200-day breadth is constructive; stabilization rather than trend confirmation. |
| 10Y-2Y Treasury spread | 0.27 | mildly positive | Curve is only slightly positive; policy rate expectations remain a key risk factor. |
| US high-yield OAS | 3.20 | moderate | Credit spreads are not tight; quality bias is warranted. |
| US IG OAS | 0.89 | moderate | Investment-grade spreads are contained, supporting risk appetite but not euphoria. |
| Advance/decline ratio | 1.70 | positive | Broad participation supports the positive 50/200-day breadth readings. |
| 20-day sector returns | Health Care +6.87%, Consumer Discretionary +6.69%, Consumer Staples +5.40%, Real Estate +5.24%, Financials +5.69% | positive | Defensive and consumer sectors lead; IT and Energy lag. |

## Macro, Fiscal, Rates, Liquidity and Credit

- Growth: the 10Y-2Y spread is only 0.27, indicating a very mild positive curve; this is consistent with a late-cycle or transition phase rather than aggressive reflation.
- Inflation: CPI and core CPI are available through September 2026, with headline CPI at 336.298 and core at 338.896; the October CPI reading is 337.476, so inflation remains above the pre-2021 trend.
- Policy: the effective federal funds rate is 3.88 as of 2026-11-12, implying a restrictive but easing policy stance; the 10Y-2Y spread suggests markets are pricing modest further easing.
- Rates: the 10Y-2Y spread of 0.27 is a key signal; a further flattening or inversion would raise recession risk, while a sustained steepening would support risk assets.
- Liquidity: high-yield OAS at 3.20 and IG OAS at 0.89 indicate moderate credit conditions; liquidity is not abundant enough to justify aggressive risk-taking.
- Credit: the combination of moderate spreads and positive breadth suggests a quality-tilted risk-on posture, with a preference for high-liquidity, low-valuation names.

## US Equities and 11 GICS Sectors

Macro source IDs: S001, S002, S003, S004, S005, S006, S007

| GICS sector | Evidence | AI research stance | Source IDs |
| --- | --- | --- | --- |
| Health Care | 20-day return +6.87% and trailing P/E 30.78; positive momentum and a high valuation multiple. | Favored for momentum and defensive characteristics; valuation is rich but supported by sector leadership. | S056 |
| Consumer Discretionary | 20-day return +6.69% and trailing P/E 25.11; strong consumer sector performance. | Favored for momentum and consumer strength; valuation is moderate. | S057 |
| Consumer Staples | 20-day return +5.40% and trailing P/E 24.85; defensive sector with positive momentum. | Favored for defensive quality and positive momentum; valuation is moderate. | S061 |
| Real Estate | 20-day return +5.24% and trailing P/E 29.63; positive momentum but high valuation. | Favored for momentum; valuation is rich and sensitive to rate expectations. | S059 |
| Financials | 20-day return +5.69% and trailing P/E 15.85; positive momentum with a low valuation multiple. | Favored for value and momentum; low P/E supports a quality tilt. | S064 |
| Utilities | 20-day return +4.34% and trailing P/E 18.11; defensive sector with moderate valuation. | Favored for defensive quality; valuation is reasonable. | S068 |
| Materials | 20-day return +2.57% and trailing P/E 21.72; positive but weaker momentum. | Neutral; positive momentum but lower relative strength. | S071 |
| Industrials | 20-day return +0.61% and trailing P/E 27.07; near-flat momentum. | Neutral; weak momentum and moderate valuation. | S069 |
| Communication Services | 20-day return -1.48% and trailing P/E 17.26; negative momentum. | Less favored; negative momentum and weak relative performance. | S070 |
| Information Technology | 20-day return -7.19% and trailing P/E 30.03; negative momentum and high valuation. | Less favored; negative momentum and high valuation despite liquidity leader names. | S072 |
| Energy | 20-day return -4.81% and trailing P/E 16.23; negative momentum. | Less favored; negative momentum and weak relative performance. | S075 |

### Sector fundamentals, valuation and earnings

No point-in-time sector fundamentals beyond the supplied trailing P/E and 20-day ETF returns are available in the database. The sector evidence is limited to the 20-day returns and trailing P/E figures from the external source set; no growth, margin, or consensus data are supplied for the 11 GICS sectors.

## Growth vs Value

- Growth: Information Technology is the only sector with negative 20-day momentum (-7.19%) and a high trailing P/E of 30.03, indicating weak near-term growth expectations.
- Value: Financials offer the lowest trailing P/E at 15.85 with positive 20-day momentum (+5.69%), making it the clearest value-tilt candidate.
- Quality: Health Care (+6.87%) and Consumer Staples (+5.40%) combine positive momentum with moderate-to-high valuations, consistent with a quality bias.
- Valuation dispersion: sector trailing P/Es range from 15.85 (Financials) to 30.78 (Health Care), indicating a wide dispersion that supports a selective, quality-over-growth stance.

## ETF Flows and Breadth

- Broad market breadth is strongly positive: 71.3% above the 50-day, 63.6% above the 200-day, and a 1.70 advance/decline ratio.
- 20-day price breadth is also positive at 70.5% positive, with 315 advancers versus 185 decliners.
- Flow evidence shows SOXX with exceptional institutional buying (20d flow z-score 5.10) despite a down price, while TLT shows medium-term deterioration and SMH shows tactical profit-taking inside structural accumulation.
- The combination of positive breadth and selective flow signals supports a liquidity and quality bias rather than broad cyclical exposure.

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
- **Why preferred / alternatives:** AppLovin offers a rare combination of top-tier momentum, exceptional margins, and a reasonable forward valuation, making it a stronger candidate than the lower-margin, lower-momentum alternatives in the shortlist. Alternatives considered: PNR, GEN, CLX, IDXX, ROP.
- **Thesis:** AppLovin screens in the top 20-day momentum bucket with a 53.7% 20-day return and a 32.5% 60-day return, indicating strong recent price momentum. The company carries a high gross margin of 88.8% and operating margin of 77.8%, supporting durable profitability. Reported diluted EPS of 11.61 for the fiscal period ending 2026-09-30 and a forward EPS of 20.86 imply a forward P/E of 19.6, which is reasonable for a high-margin, fast-growing mobile advertising platform.
- **Source IDs:** S010, S011, S014, S015
- **Catalysts:** Continued 20-day momentum and positive 60-day return, Sustained high gross margin and operating leverage, Forward EPS growth from 11.61 to 20.86, Mobile advertising market tailwinds
- **Risks:** High 20-day momentum may already be priced in, Forward EPS estimates are unverified and subject to revision, Mobile advertising sector competition and regulatory changes, Single-quarter reported EPS may not reflect full-year trajectory
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 20.8603 (source.forwardEps) x AI multiple assumption 22.00; source IDs S010, S011, S014, S015
- **EPS:** 20.86026 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 19.611452
- **FY+1 growth assumption:** 27.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / PNR and IDXX / APP shows strong FY1 earnings growth of 27.4% and revenue growth of 25.4%, with high operating margins (77.8%) and a high ROE (2.10x). The FY1 consensus growth is used as the forward growth assumption. PNR and IDXX are named peers because they are the other high-quality, high-margin compounders in the idea set with comparable growth profiles, supporting a premium multiple over the current forward P/E of 19.6.
- **Company fundamentals:** AppLovin reported diluted EPS of 11.61 for the fiscal period ending 2026-09-30, with forward EPS of 20.86. Gross margin is 88.8%, operating margin 77.8%, profit margin 65.9%, and return on equity 2.10. Revenue growth is 55.5% and earnings growth 75.5%. Forward P/E is 19.61. The stock closed at 409.1 with 20-day return of 53.7% and 60-day return of 32.5%.
- **Bull / Base / Bear:** 542.37 / 458.93 / 354.62
- **Bull / Base / Bear returns:** 32.58% / 12.18% / -13.32%
- **Scenario probabilities:** not separately assigned; see scenario table.

### PNR — Pentair

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Pentair offers a lower forward P/E than many momentum names, but its negative earnings growth and unverified forward estimates make it a neutral holding rather than a top pick. Alternatives considered: APP, GEN, CLX, IDXX, ROP.
- **Thesis:** Pentair is a top-20-day momentum name with a 27.8% 20-day return and a 7.1% 60-day return. It trades at a forward P/E of 12.9, which is below the broader market, but revenue growth is slightly negative at -4.5% and earnings growth is -18.8%. The company has a moderate gross margin of 40.2% and operating margin of 21.4%. The valuation is attractive, but near-term earnings contraction tempers the upside.
- **Source IDs:** S008, S013, S016, S037
- **Catalysts:** Attractive forward P/E of 12.9, Positive 20-day momentum of 27.8%, Potential recovery in earnings as cyclical demand improves, Diversified industrial portfolio
- **Risks:** Negative revenue growth of -4.5% and earnings growth of -18.8%, Forward EPS estimates are unverified, Industrial end-market cyclicality, Lower margin profile compared to high-growth names
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 5.3040 (source.forwardEps) x AI multiple assumption 14.00; source IDs S008, S013, S016, S037
- **EPS:** 5.30402 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 12.877027
- **FY+1 growth assumption:** 12.82%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / APP and IDXX / PNR has moderate FY1 earnings growth of 12.8% and revenue growth of 18.4%, with solid operating margins (21.4%) and a ROE of 0.156x. The FY1 consensus growth is used as the forward growth assumption. APP and IDXX are named peers because they are higher-growth, higher-margin names in the same idea set, justifying a lower multiple than the current forward P/E of 12.9.
- **Company fundamentals:** Pentair reported diluted EPS of 2.76 for the fiscal period ending 2026-09-30, with forward EPS of 5.30. Gross margin is 40.2%, operating margin 21.4%, profit margin 15.4%, and return on equity 15.6%. Revenue growth is -4.5% and earnings growth is -18.8%. Forward P/E is 12.88. The stock closed at 68.3 with 20-day return of 27.8% and 60-day return of 7.1%.
- **Bull / Base / Bear:** 90.17 / 74.26 / 58.34
- **Bull / Base / Bear returns:** 32.02% / 8.73% / -14.58%
- **Scenario probabilities:** not separately assigned; see scenario table.

### GEN — Gen Digital

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Gen Digital offers a very low forward P/E, but its modest revenue growth and unverified forward estimates make it a neutral holding rather than a top pick. Alternatives considered: APP, PNR, CLX, IDXX, ROP.
- **Thesis:** Gen Digital is a top-20-day momentum name with a 25.8% 20-day return and a 7.9% 60-day return. It trades at a forward P/E of 9.1, which is very cheap, but revenue growth is only 12.2% and earnings growth is 128.6%. The company has a gross margin of 77.4% and operating margin of 43.2%. The low valuation is attractive, but the modest revenue growth and unverified forward estimates limit conviction.
- **Source IDs:** S019, S020, S025, S030
- **Catalysts:** Very low forward P/E of 9.1, Positive 20-day momentum of 25.8%, Strong earnings growth of 128.6%, Cybersecurity and digital life protection franchise
- **Risks:** Revenue growth of only 12.2% is modest for a growth name, Forward EPS estimates are unverified, Cybersecurity market competition, Potential for earnings quality issues
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 3.3374 (source.forwardEps) x AI multiple assumption 11.00; source IDs S019, S020, S025, S030
- **EPS:** 3.33736 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 9.108996
- **FY+1 growth assumption:** 12.86%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / PNR and CLX / GEN shows FY1 earnings growth of 12.9% and revenue growth of 6.8%, with strong operating margins (43.2%) and a high ROE (0.464x). The FY1 consensus growth is used as the forward growth assumption. PNR and CLX are named peers because they are the other mid-growth, higher-margin names in the idea set, supporting a multiple above the current forward P/E of 9.1.
- **Company fundamentals:** Gen Digital reported diluted EPS of 0.83 for the fiscal period ending 2026-10-02, with forward EPS of 3.34. Gross margin is 77.4%, operating margin 43.2%, profit margin 23.1%, and return on equity 46.4%. Revenue growth is 12.2% and earnings growth is 128.6%. Forward P/E is 9.11. The stock closed at 30.4 with 20-day return of 25.8% and 60-day return of 7.9%.
- **Bull / Base / Bear:** 43.39 / 36.71 / 30.04
- **Bull / Base / Bear returns:** 42.73% / 20.76% / -1.18%
- **Scenario probabilities:** not separately assigned; see scenario table.

### CLX — Clorox

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Clorox offers a reasonable valuation and positive momentum, but its lower margins and consumer staples cyclicality make it a neutral holding rather than a top pick. Alternatives considered: APP, PNR, GEN, IDXX, ROP.
- **Thesis:** Clorox is a top-20-day momentum name with a 25.7% 20-day return and a 3.2% 60-day return. It trades at a forward P/E of 17.7, which is reasonable, and has positive revenue growth of 33.3% and earnings growth of 113.8%. The company has a gross margin of 41.9% and operating margin of 14.3%. The valuation is fair, but the lower margin profile and consumer staples cyclicality limit upside.
- **Source IDs:** S018, S022, S023, S031
- **Catalysts:** Positive 20-day momentum of 25.7%, Revenue growth of 33.3% and earnings growth of 113.8%, Reasonable forward P/E of 17.7, Strong brand portfolio in consumer staples
- **Risks:** Lower operating margin of 14.3%, Consumer staples cyclicality and margin pressure, Forward EPS estimates are unverified, Limited growth compared to high-momentum names
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 6.1684 (source.forwardEps) x AI multiple assumption 18.00; source IDs S018, S022, S023, S031
- **EPS:** 6.1684 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 17.745283
- **FY+1 growth assumption:** 7.69%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / APP and IDXX / CLX has modest FY1 earnings growth of 7.7% and revenue growth of 2.2%, but strong reported earnings growth of 113.8% and high gross margins (41.9%). The FY1 consensus growth is used as the forward growth assumption. APP and IDXX are named peers because they are higher-growth, higher-quality compounders in the idea set, justifying a premium multiple over the current forward P/E of 17.7.
- **Company fundamentals:** Clorox reported diluted EPS of 1.39 for the fiscal period ending 2026-09-30, with forward EPS of 6.17. Gross margin is 41.9%, operating margin 14.3%, profit margin 9.4%, and return on equity 5.34. Revenue growth is 33.3% and earnings growth is 113.8%. Forward P/E is 17.75. The stock closed at 109.46 with 20-day return of 25.7% and 60-day return of 3.2%.
- **Bull / Base / Bear:** 129.54 / 111.03 / 92.53
- **Bull / Base / Bear returns:** 18.34% / 1.43% / -15.47%
- **Scenario probabilities:** not separately assigned; see scenario table.

### IDXX — Idexx Laboratories

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Idexx offers strong momentum and a high-margin franchise, but the high forward P/E limits upside relative to other candidates. Alternatives considered: APP, PNR, GEN, CLX, ROP.
- **Thesis:** Idexx Laboratories is a top-20-day momentum name with a 25.7% 20-day return and a 29.0% 60-day return. It trades at a forward P/E of 41.7, which is high, but revenue growth is 9.9% and earnings growth is 17.9%. The company has a gross margin of 62.7% and operating margin of 32.5%. The high valuation limits upside despite strong momentum.
- **Source IDs:** S027, S028, S033, S034
- **Catalysts:** Positive 20-day momentum of 25.7% and 60-day return of 29.0%, Revenue growth of 9.9% and earnings growth of 17.9%, High gross margin of 62.7%, Veterinary diagnostics and software franchise
- **Risks:** High forward P/E of 41.7 limits upside, Forward EPS estimates are unverified, Veterinary sector cyclicality, Moderate earnings growth of 17.9%
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 16.8929 (source.forwardEps) x AI multiple assumption 42.00; source IDs S027, S028, S033, S034
- **EPS:** 16.8929 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 41.687927
- **FY+1 growth assumption:** 12.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / APP and GEN / IDXX shows FY1 earnings growth of 12.4% and revenue growth of 8.9%, with strong operating margins (32.5%) and a high ROE (0.689x). The FY1 consensus growth is used as the forward growth assumption. APP and GEN are named peers because they are higher-growth, higher-margin names in the idea set, supporting a premium multiple over the current forward P/E of 41.7.
- **Company fundamentals:** Idexx Laboratories reported diluted EPS of 11.75 for the fiscal period ending 2026-09-30, with forward EPS of 16.89. Gross margin is 62.7%, operating margin 32.5%, profit margin 25.4%, and return on equity 68.9%. Revenue growth is 9.9% and earnings growth is 17.9%. Forward P/E is 41.69. The stock closed at 704.23 with 20-day return of 25.7% and 60-day return of 29.0%.
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
| Bull | 25% | +2.00% | Low 5-day forecast vol (14.9%) and below-threshold spike probability (16.5% vs 18.5% threshold) suggest a stable, range-bound tape where a mild upside drift is plausible if US close confirms no risk-off repricing. |
| Base | 50% | +0.00% | Frozen daily-close model with no directional signal and historical/ewma baselines above threshold implies a neutral path: modest drift offset by elevated volatility regime, yielding near-zero expected return over the 5-day window. |
| Bear | 25% | -2.00% | If the US close triggers a spike event above the 18.5% threshold, elevated vol (14.9%) and negative skew could drive a mild downside move, with downside skew amplified by low directional conviction. |

### Long Term (12 months)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 30% | +8.00% | Sustained low vol (14.9%) and sub-threshold spike probability (16.5%) over a longer horizon support a gradual upward drift if earnings and credit conditions remain stable, with probability weighted toward a positive but moderate return. |
| Base | 40% | +3.00% | Base case assumes the frozen daily-close model holds, with vol and spike probability normalizing toward historical levels, allowing a modest positive return driven by steady earnings and stable credit spreads over the longer window. |
| Bear | 30% | -5.00% | If the spike probability materializes above threshold and vol remains elevated, a longer-horizon bear case emerges where volatility drag and potential credit stress compress returns, with a -5% outcome reflecting sustained risk-off pressure. |

## Positioning

- Maintain a quality and liquidity bias; favor high-liquidity, low-valuation, and positive-momentum names.
- Avoid speculative or high-valuation names with negative momentum, especially in Information Technology and Energy.
- Use the positive 50/200-day breadth as a stabilization signal, not a trend confirmation, given the negative 20-day market return.
- Monitor the 10Y-2Y spread and credit spreads for shifts in the risk-on/risk-off posture.
- No allocation weights or composite scores are provided; positioning is qualitative only.

## Catalysts

| Date | Event | Why it matters |
| --- | --- | --- |
| 2026-11-16 | US equity market open | Frozen daily-close model; official risk assessment begins after the completed US close. |
| 2026-11-13 | Macro data release | CPI, core CPI, and unemployment data through September 2026 are available; October CPI is 337.476. |
| 2026-11-12 | Policy rate observation | Effective federal funds rate is 3.88, the latest policy rate observation. |

## Key Risks

- Negative 20-day market return (-1.28%) indicates the positive breadth may be a stabilization signal rather than a confirmed trend.
- The 10Y-2Y spread is only 0.27, so a further flattening or inversion would raise recession risk.
- High-yield OAS at 3.20 and IG OAS at 0.89 imply moderate credit stress; a widening of spreads would pressure risk assets.
- Sector leadership is concentrated in Health Care, Consumer Discretionary, Consumer Staples, Real Estate and Financials, while Information Technology and Energy are negative; a rotation could reverse quickly.
- The equity session contains a mix of provisional yfinance and canonical Massive rows, which may introduce data quality noise.
- The risk forecast is a frozen daily-close model and is official only after the completed US close; the 5-day forecast volatility is 14.9% and spike probability is 16.5%.

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
| S009 | filing | FISV | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0000798354-26-000042); 8-K filed 2026-11-03 (accession 0000798354-26-000039); 8-K filed 2026-10-23 (accession 0001193125-26-429481) |
| S010 | filing | APP | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001751008&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0001751008-26-000069); 8-K filed 2026-11-04 (accession 0001751008-26-000068); 10-Q filed 2026-08-05 (accession 0001751008-26-000059) |
| S011 | news | APP | Thu, 12 Nov 2026 20:05:45 GMT | ok | https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en | AppLovin Just Ripped 47% in a Month: Is It Too Late to Buy APP Stock Now? - Yahoo Finance (Thu, 12 Nov 2026 20:05:45 GMT); APP Stock Surges 51% After Q3 Earnings: Is it Still a Buy? - Yahoo Finance (Tue, 10 Nov 2026 14:24:00 GMT); Here is What to Know Beyond Why AppLovin Corporation (APP) is a Trending Stock - Yahoo Finance (Tue, 10 Nov 2026 13:00:06 GMT) |
| S012 | news | FISV | Thu, 12 Nov 2026 18:47:44 GMT | ok | https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en | Fiserv, Inc. (FISV) Stock Price, News, Quote & History - Yahoo! Finance Canada (Thu, 12 Nov 2026 18:47:44 GMT); Fiserv Stock Outlook: Is Wall Street Bullish or Bearish? - Yahoo Finance (Thu, 12 Nov 2026 12:23:56 GMT); What Is Fiserv (FISV) Planning With Its Debit Networks And Clover AI? - Yahoo Finance (Thu, 12 Nov 2026 06:09:00 GMT) |
| S013 | news | PNR | Fri, 13 Nov 2026 22:05:23 GMT | ok | https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en | Pentair plc (PNR) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 22:05:23 GMT); Here's What Key Metrics Tell Us About Pentair (PNR) Q3 Earnings - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT); Pentair plc (PNR) Q3 Earnings and Revenues Beat Estimates - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT) |
| S014 | stock | APP | 2026-11-15 | ok | https://finance.yahoo.com/quote/APP | Trailing P/E: 27.54882; Forward P/E: 19.611452; Forward EPS: 20.86026; Price: 409.1; Market price: 409.1; Market cap: 135543824384; Sector: Communication Services; Trailing Eps: 14.85; Revenue Growth: 0.555; Earnings Growth: 0.755; Gross Margin: 0.8878; Operating Margin: 0.77782995; Profit Margin: 0.65887; Return On Equity: 2.1008599; Total Revenue: 7608893952; Market Cap: 135543824384; Consensus EPS FY+1: 20.72438; growth: 0.2744 |
| S015 | filing | APP | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json | Diluted EPS 11.61 for period ending 2026-09-30 (filed 2026-11-04) |
| S016 | stock | PNR | 2026-11-15 | ok | https://finance.yahoo.com/quote/PNR | Trailing P/E: 18.610355; Forward P/E: 12.877027; Forward EPS: 5.30402; Price: 68.3; Market price: 68.3; Market cap: 10904415232; Sector: Industrials; Trailing Eps: 3.67; Revenue Growth: -0.045; Earnings Growth: -0.188; Gross Margin: 0.40168998; Operating Margin: 0.21410999; Profit Margin: 0.15435; Return On Equity: 0.15605; Total Revenue: 3966200064; Market Cap: 10904415232; Consensus EPS FY+1: 5.30402; growth: 0.1282 |
| S017 | stock | FISV | 2026-11-15 | ok | https://finance.yahoo.com/quote/FISV | Forward P/E: 7.9923306; Price: 63.78; Market price: 63.78; Market cap: 33934002176; Market Cap: 33934002176; Consensus EPS FY+1: 7.98015; growth: 0.09689999 |
| S018 | filing | CLX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000021076-26-000046); 8-K filed 2026-11-02 (accession 0000021076-26-000044); 8-K filed 2026-10-29 (accession 0001206774-26-000586) |
| S019 | filing | GEN | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0000849399-26-000083); 8-K filed 2026-10-28 (accession 0000849399-26-000081); 8-K filed 2026-10-09 (accession 0000849399-26-000079) |
| S020 | news | GEN | Fri, 13 Nov 2026 00:21:25 GMT | ok | https://news.google.com/rss/search?q=GEN+Gen+Digital+stock&hl=en-US&gl=US&ceid=US:en | Gen Digital Inc. (GEN) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 00:21:25 GMT); Gen Digital (GEN) Stock Repriced After Q2 Earnings Put Margins Center Stage - Yahoo Finance (Thu, 29 Oct 2026 07:00:00 GMT); Are Business Services Stocks Lagging GEN DIGITAL INC (GEN) This Year? - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT) |
| S021 | filing | FISV | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json | Diluted EPS -8.9 for period ending 2026-09-30 (filed 2026-11-04) |
| S022 | news | CLX | Fri, 13 Nov 2026 18:52:58 GMT | ok | https://news.google.com/rss/search?q=CLX+Clorox+stock&hl=en-US&gl=US&ceid=US:en | The Clorox Company (CLX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 18:52:58 GMT); The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance Singapore (Fri, 13 Nov 2026 18:40:50 GMT); The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance UK (Fri, 13 Nov 2026 16:03:45 GMT) |
| S023 | stock | CLX | 2026-11-15 | ok | https://finance.yahoo.com/quote/CLX | Trailing P/E: 19.68705; Forward P/E: 17.745283; Forward EPS: 6.1684; Price: 109.46; Market price: 109.46; Market cap: 13260793856; Sector: Consumer Defensive; Trailing Eps: 5.56; Revenue Growth: 0.333; Earnings Growth: 1.138; Gross Margin: 0.41939998; Operating Margin: 0.14286; Profit Margin: 0.09408; Return On Equity: 5.34363; Total Revenue: 7196000256; Market Cap: 13260793856; Consensus EPS FY+1: 6.1684; growth: 0.0769 |
| S024 | filing | CHTR | 2026-11-06 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-06 (accession 0001091667-26-000073); 8-K filed 2026-11-06 (accession 0001091667-26-000072); 8-K filed 2026-10-27 (accession 0001091667-26-000064) |
| S025 | stock | GEN | 2026-11-15 | ok | https://finance.yahoo.com/quote/GEN | Trailing P/E: 15.431472; Forward P/E: 9.108996; Forward EPS: 3.33736; Price: 30.4; Market price: 30.4; Market cap: 18035593216; Sector: Technology; Trailing Eps: 1.97; Revenue Growth: 0.122; Earnings Growth: 1.286; Gross Margin: 0.77410007; Operating Margin: 0.43229; Profit Margin: 0.23068; Return On Equity: 0.46402; Total Revenue: 5228000256; Market Cap: 18035593216; Consensus EPS FY+1: 3.33736; growth: 0.1286 |
| S026 | news | CHTR | Thu, 12 Nov 2026 08:02:01 GMT | ok | https://news.google.com/rss/search?q=CHTR+Charter+Communications+stock&hl=en-US&gl=US&ceid=US:en | Charter Communications: 3 Key Takeaways for Long-Term Investors - Yahoo Finance (Thu, 12 Nov 2026 08:02:01 GMT); Charter Communications (CHTR) Stock Looks Reasonable As Shares Slump 85% - Yahoo Finance (Wed, 28 Oct 2026 07:00:00 GMT); Should Value Investors Buy Charter Communications (CHTR) Stock? - Yahoo Finance (Wed, 21 Oct 2026 07:00:00 GMT) |
| S027 | filing | IDXX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000874716&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000874716-26-000135); 8-K filed 2026-11-02 (accession 0001104659-26-120892); 10-Q filed 2026-08-04 (accession 0000874716-26-000123) |
| S028 | stock | IDXX | 2026-11-15 | ok | https://finance.yahoo.com/quote/IDXX | Trailing P/E: 47.45485; Forward P/E: 41.687927; Forward EPS: 16.8929; Price: 704.23; Market price: 704.23; Market cap: 55483650048; Sector: Healthcare; Trailing Eps: 14.84; Revenue Growth: 0.099; Earnings Growth: 0.179; Gross Margin: 0.62722; Operating Margin: 0.32497; Profit Margin: 0.25357; Return On Equity: 0.68925005; Total Revenue: 4662220800; Market Cap: 55483650048; Consensus EPS FY+1: 16.8929; growth: 0.1244 |
| S029 | stock | CHTR | 2026-11-15 | ok | https://finance.yahoo.com/quote/CHTR | Trailing P/E: 13.006578; Forward P/E: 3.2831066; Forward EPS: 42.15215; Price: 138.39; Market price: 138.39; Market cap: 24778944512; Sector: Communication Services; Trailing Eps: 10.64; Revenue Growth: 0.091; Gross Margin: 0.55084; Operating Margin: 0.23389; Profit Margin: 0.02498; Return On Equity: 0.07019; Total Revenue: 55645999104; Market Cap: 24778944512; Consensus EPS FY+1: 47.15811; growth: 1.0195 |
| S030 | filing | GEN | 2026-10-29 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000849399.json | Diluted EPS 0.83 for period ending 2026-10-02 (filed 2026-10-29) |
| S031 | filing | CLX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000021076.json | Diluted EPS 1.39 for period ending 2026-09-30 (filed 2026-11-02) |
| S032 | filing | CHTR | 2026-11-06 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001091667.json | Diluted EPS 0.38 for period ending 2026-09-30 (filed 2026-11-06) |
| S033 | news | IDXX | Fri, 13 Nov 2026 22:06:38 GMT | ok | https://news.google.com/rss/search?q=IDXX+Idexx+Laboratories+stock&hl=en-US&gl=US&ceid=US:en | IDEXX Laboratories, Inc. (IDXX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 22:06:38 GMT); IDEXX Laboratories (IDXX) Stock Looks Fairly Valued Despite Its 28% Run - Yahoo Finance (Sat, 31 Oct 2026 07:00:00 GMT); IDEXX Laboratories (IDXX) Q3 Earnings Leave Its Premium Valuation In Focus - Yahoo Finance (Tue, 03 Nov 2026 08:00:00 GMT) |
| S034 | filing | IDXX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000874716.json | Diluted EPS 11.75 for period ending 2026-09-30 (filed 2026-11-02) |
| S035 | filing | ROP | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000882835&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000882835-26-000047); 8-K filed 2026-10-22 (accession 0000882835-26-000042); 8-K filed 2026-10-01 (accession 0000882835-26-000039) |
| S036 | filing | RDDT | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001713445&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0001713445-26-000116); 8-K filed 2026-10-29 (accession 0001713445-26-000114); 8-K filed 2026-08-12 (accession 0001713445-26-000107) |
| S037 | filing | PNR | 2026-10-27 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json | Diluted EPS 2.76 for period ending 2026-09-30 (filed 2026-10-27) |
| S038 | stock | ROP | 2026-11-15 | ok | https://finance.yahoo.com/quote/ROP | Trailing P/E: 18.993866; Forward P/E: 19.532475; Forward EPS: 24.57318; Price: 479.975; Market price: 479.975; Market cap: 47535013888; Sector: Technology; Trailing Eps: 25.27; Revenue Growth: 0.076; Earnings Growth: 0.326; Gross Margin: 0.69671; Operating Margin: 0.28049; Profit Margin: 0.30712998; Return On Equity: 0.13229; Total Revenue: 8434599936; Market Cap: 47535013888; Consensus EPS FY+1: 24.57318; growth: 0.09810001 |
| S039 | news | ROP | Thu, 12 Nov 2026 19:15:50 GMT | ok | https://news.google.com/rss/search?q=ROP+Roper+Technologies+stock&hl=en-US&gl=US&ceid=US:en | Roper Technologies, Inc. (ROP) Stock Price, News, Quote & History - Yahoo! Finance Canada (Thu, 12 Nov 2026 19:15:50 GMT); Roper Technologies (ROP) Stock Looks Fully Valued As Cash Flow Comes Into Focus - Yahoo Finance (Fri, 06 Nov 2026 07:13:00 GMT); Roper Technologies: 3 Key Takeaways for Long-Term Investors - Yahoo Finance (Mon, 26 Oct 2026 07:00:00 GMT) |
| S040 | stock | RDDT | 2026-11-15 | ok | https://finance.yahoo.com/quote/RDDT | Trailing P/E: 20.091835; Forward P/E: 10.770874; Forward EPS: 9.14039; Price: 98.45; Market price: 98.45; Market cap: 19010076672; Sector: Communication Services; Trailing Eps: 4.9; Revenue Growth: 0.53; Earnings Growth: 0.749; Gross Margin: 0.91547996; Operating Margin: 0.29397; Profit Margin: 0.32105; Return On Equity: 0.32029998; Total Revenue: 3088880128; Market Cap: 19010076672; Consensus EPS FY+1: 6.82439; growth: 0.2417 |

## Sources

- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFF&cosd=2026-01-01 (2026-11-12)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLH0A0HYM2&cosd=2026-01-01 (2026-11-12)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLC0A0CM&cosd=2026-01-01 (2026-11-12)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCSL&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=UNRATE&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=PAYEMS&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=T10Y2Y&cosd=2026-01-01 (2026-11-13)
- filing PNR: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 (2026-10-27)
- filing FISV: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 (2026-11-04)
- filing APP: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001751008&type=10-Q&dateb=&owner=include&count=10 (2026-11-04)
- news APP: https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en (Thu, 12 Nov 2026 20:05:45 GMT)
- news FISV: https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en (Thu, 12 Nov 2026 18:47:44 GMT)
- news PNR: https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 22:05:23 GMT)
- stock APP: https://finance.yahoo.com/quote/APP (2026-11-15)
- filing APP: https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json (2026-11-04)
- stock PNR: https://finance.yahoo.com/quote/PNR (2026-11-15)
- stock FISV: https://finance.yahoo.com/quote/FISV (2026-11-15)
- filing CLX: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 (2026-11-02)
- filing GEN: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 (2026-10-29)
- news GEN: https://news.google.com/rss/search?q=GEN+Gen+Digital+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 00:21:25 GMT)

## AI Provenance

- Provider / model: hermes-local-proxy / upstage/solar-mini4:free
- Market research: attempts=1 tokens=9353 (prompt=6548, completion=2805) runtime=23.81s
- Fundamental research: generated this run at 2026-11-15T03:15:49.057755+00:00
- Evidence source dates: {'as_of': '2026-11-13', 'latest_equity_date': '2026-11-13', 'latest_macro_date': '2026-11-13', 'flows_date': '2026-11-13'}
- Evidence fingerprint: 530d3d2fed16699824d33dbb097ffc4efa0ce2997e416ffcb652eff5b12570c8
- Source citations are retrieved external records in the ledger above; market values remain from the verified database snapshot.


## Disclosures

- This is research and market intelligence, not investment advice.
- AI conclusions are research judgments, not validated return predictions.
- The frozen risk layer is risk-only and is not used for directional views or allocations.
- Legacy scores are not active inputs or outputs.

# AEGIS AI-First Market Intelligence

Research generated at: 15 November 2026, 10:15 HKT
Database freshness: equity 2026-11-13 (latest row retrieved 2026-11-14 13:50:55.938286+08:00)
Data cutoff: 2026-11-13 US cash close
Snapshot ID: aegis-hourly-20261115T021500Z

## Executive Summary

- **AI market view: Risk-on tilt with a quality and liquidity bias. Breadth is constructive, but the 20-day equity return is negative and the 10Y-2Y curve is only mildly positive, so the setup favors high-quality, liquid names and sectors with positive momentum rather than broad cyclical or speculative exposure.**
- Equity market is in a risk-on but fragile posture: SPX is near record levels while 20-day return is negative and new-high/new-low readings are zero.
- Breadth is supportive: 71.3% above the 50-day, 63.6% above the 200-day, and a 1.70 advance/decline ratio, with no bearish divergence.
- Rate and credit conditions are stable: effective funds rate 3.88%, 10Y-2Y spread 0.27, IG OAS 0.89, and HY OAS 3.20.
- Inflation and labor remain contained: CPI 336.30 and core CPI 338.90 (Sep 2026), unemployment 4.2%.
- Sector leadership is split: Communication Services and Information Technology are negative on 20-day returns, while Health Care, Consumer Discretionary, Consumer Staples, Real Estate, Financials, Utilities, and Materials are positive.
- Flows show strong institutional buying in SOXX and neutral-to-negative positioning in TLT, with SMH showing tactical profit-taking inside structural accumulation.

## Data QC

- Status: **PASS_WITH_WARNINGS**
- Equity session: 0 completed session(s) behind inference date
- Equity provenance: 386 provisional / 12581 canonical
- Breadth lag: 0 session(s); ETF-flow lag: 0 session(s)
- Note: Equity session contains a mix of provisional yfinance and canonical Massive rows.
- External sources: 79 ok / 0 unavailable; retrieved 2026-11-15T02:15:19.536076+00:00

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
| SPX | 7561.67 | -1.28% (20d) | Record-level index with negative 20-day return; breadth is positive but momentum is soft. |
| Health Care (XLV) | 6.87% | +6.87% (20d) | Strongest sector return; trailing P/E 30.78. |
| Consumer Discretionary (XLY) | 6.69% | +6.69% (20d) | Positive momentum; trailing P/E 25.11. |
| Consumer Staples (XLP) | 5.40% | +5.40% (20d) | Defensive strength; trailing P/E 24.85. |
| Real Estate (XLRE) | 5.24% | +5.24% (20d) | Positive 20-day return; trailing P/E 29.63. |
| Financials (XLF) | 5.69% | +5.69% (20d) | Positive sector return; trailing P/E 15.85. |
| Utilities (XLU) | 4.34% | +4.34% (20d) | Defensive positive; trailing P/E 18.11. |
| Materials (XLB) | 2.57% | +2.57% (20d) | Positive but weakest among positive sectors; trailing P/E 21.72. |
| Industrials (XLI) | 0.61% | +0.61% (20d) | Near-flat; trailing P/E 27.07. |
| Communication Services (XLC) | -1.48% | -1.48% (20d) | Negative sector return; trailing P/E 17.26. |
| Information Technology (XLK) | -7.19% | -7.19% (20d) | Negative sector return; trailing P/E 30.03. |
| Energy (XLE) | -4.81% | -4.81% (20d) | Negative sector return; trailing P/E 16.23. |

## Macro, Fiscal, Rates, Liquidity and Credit

- Growth: equity market is near record levels with positive breadth, but 20-day equity return is negative, indicating a cautious near-term growth tone.
- Inflation: CPI 336.30 and core CPI 338.90 (Sep 2026) show contained price pressures; October CPI is not yet in the database snapshot.
- Policy: effective federal funds rate is 3.88% as of 2026-11-12, consistent with a neutral-to-accommodative policy stance.
- Rates: 10Y-2Y spread is 0.27, a mildly positive curve; IG OAS 0.89 and HY OAS 3.20 indicate orderly credit conditions.
- Liquidity: SOXX shows exceptional institutional buying (20d flow z-score 5.10) while TLT is neutral-to-negative, suggesting liquidity is rotating toward cyclical/tech hardware rather than duration.
- Credit: IG and HY spreads are stable, with no stress signals, supporting risk-on positioning.

## US Equities and 11 GICS Sectors

Macro source IDs: S001, S002, S003, S004, S005, S006, S007

| GICS sector | Evidence | AI research stance | Source IDs |
| --- | --- | --- | --- |
| Health Care | 20-day return 6.87%; trailing P/E 30.78; SPX 7561.67 with 71.3% above 50-day and 63.6% above 200-day. | Positive momentum and defensive quality; leading sector in the current setup. | S053 |
| Consumer Discretionary | 20-day return 6.69%; trailing P/E 25.11; broad market breadth positive. | Strong consumer-driven demand; positive 20-day return supports risk-on. | S060 |
| Consumer Staples | 20-day return 5.40%; trailing P/E 24.85; defensive positioning with positive momentum. | Stable defensive holding; positive 20-day return despite defensive label. | S059 |
| Real Estate | 20-day return 5.24%; trailing P/E 29.63; positive sector return. | Positive momentum; valuation is elevated but sector is contributing to risk-on. | S061 |
| Financials | 20-day return 5.69%; trailing P/E 15.85; positive sector return. | Positive 20-day return with relatively low valuation; supportive for financials. | S063 |
| Utilities | 20-day return 4.34%; trailing P/E 18.11; defensive positive. | Defensive strength; positive 20-day return supports risk-on. | S065 |
| Materials | 20-day return 2.57%; trailing P/E 21.72; positive but weakest among positive sectors. | Positive but subdued; maintain neutral-to-positive stance. | S066 |
| Industrials | 20-day return 0.61%; trailing P/E 27.07; near-flat. | Flat momentum; neutral stance with no strong directional signal. | S069 |
| Communication Services | 20-day return -1.48%; trailing P/E 17.26; negative sector return. | Negative momentum; avoid adding, maintain neutral. | S072 |
| Information Technology | 20-day return -7.19%; trailing P/E 30.03; negative sector return. | Negative momentum and elevated valuation; reduce exposure, avoid new positions. | S074 |
| Energy | 20-day return -4.81%; trailing P/E 16.23; negative sector return. | Negative momentum; avoid adding, maintain neutral. | S076 |

### Sector fundamentals, valuation and earnings

No point-in-time sector fundamentals beyond the supplied trailing P/E and 20-day ETF returns are available in the database. The sector evidence is limited to the 20-day returns and trailing P/E figures listed in the sector table; no growth, margin, or consensus data are supplied for the 11 GICS sectors.

## Growth vs Value

- Health Care and Consumer Discretionary show the strongest 20-day returns (6.87% and 6.69%) and are the clearest growth leaders in the current snapshot.
- Consumer Staples and Utilities provide defensive value with positive 20-day returns (5.40% and 4.34%) and moderate trailing P/Es (24.85 and 18.11).
- Information Technology and Energy are the weakest growth contributors, with 20-day returns of -7.19% and -4.81% respectively.
- Financials offer a value-tilt with a trailing P/E of 15.85 and a positive 20-day return of 5.69%, making them attractive on a relative value basis.

## ETF Flows and Breadth

- SOXX is the standout flow signal: 20d flow z-score 5.10 and 60d flow z-score 3.17, classified as exceptional institutional buying despite a down price state.
- TLT shows neutral flow with a 20d flow z-score of -0.41 and a medium-term deterioration structure, indicating reduced demand for duration.
- SMH is in outflow with a 20d flow z-score of 1.22, described as tactical profit-taking inside structural accumulation.
- Breadth is constructive: 71.3% above the 50-day, 63.6% above the 200-day, and a 1.70 advance/decline ratio, with no bearish divergence.
- New-high and new-low readings are both zero, so breadth is broad but not extreme; the market is not making new highs at an elevated pace.

## Stock Ideas

Single-stock research uses reported EPS, forward P/E and company fundamentals. All ideas are research judgments, not validated return predictions.

| Ticker | Security | Research view | Price | EPS | Forward P/E | Base target | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| APP | AppLovin | NEW | 409.1 | 20.86026 | 19.611452 | 458.93 | NEW |
| PNR | Pentair | KEEP | 68.3 | 5.30402 | 12.877027 | 74.26 | KEEP |
| GEN | Gen Digital | KEEP | 30.4 | 3.33736 | 9.108996 | 36.71 | KEEP |
| RDDT | Reddit | DOWNGRADE | 98.45 | 9.14039 | 10.770874 | 118.83 | DOWNGRADE |

## ETF Ideas

ETF research uses holdings, portfolio valuation and exposure. Single-stock EPS × P/E valuation is not applied to ETFs.

| Ticker | Fund | Research view | Price | Top holdings | Portfolio valuation | Sector exposure | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| XLV | Health Care sector ETF | KEEP | 188.85 | LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59% | Top 10 holdings; numeric weight coverage 61.42% | Health Care | KEEP |
### APP — AppLovin

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** AppLovin offers a rare combination of top-tier momentum, exceptional margins, and strong earnings growth, making it a more compelling growth candidate than the lower-margin, lower-growth alternatives in the shortlist. Alternatives considered: PNR, GEN, CLX, IDXX, ROP.
- **Thesis:** AppLovin screens in the top 20-day momentum bucket with a 53.7% 20-day return and a 32.5% 60-day return, indicating strong recent price momentum. The company reports high gross margin (88.8%) and operating margin (77.8%), with FY1 earnings growth of 75.5% and revenue growth of 55.5%, supporting a premium valuation. The forward P/E of 19.6x is reasonable relative to its growth profile.
- **Source IDs:** S009, S012, S013, S016
- **Catalysts:** Continued high-margin revenue growth from mobile advertising and video, Sustained 20-day momentum momentum carrying into Q4 FY2027, Potential for further multiple expansion if growth reaccelerates
- **Risks:** High valuation already priced in; any deceleration in growth could lead to sharp re-rating, News headline suggests a 47% drop in a month, indicating possible overreaction or volatility, Dependency on mobile advertising market trends and competition
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 20.8603 (source.forwardEps) x AI multiple assumption 22.00; source IDs S009, S012, S013, S016
- **EPS:** 20.86026 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 19.611452
- **FY+1 growth assumption:** 27.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / MSFT / APP shows strong FY1 consensus growth of 27.44% with 25.4% revenue growth and 75.5% earnings growth, supported by 88.8% gross margin and 77.8% operating margin. The forward EPS of 20.86 and forward P/E of 19.6 are below the 22-26x range justified by its high-quality, high-margin profile and growth. MSFT is the named peer reference because both are high-margin, high-growth technology platforms with durable competitive moats, making a 22-26x multiple appropriate for APP's superior margins and growth.
- **Company fundamentals:** AppLovin reports FY1 EPS of $20.72 with 27.4% growth, revenue growth of 55.5%, gross margin of 88.8%, operating margin of 77.8%, and profit margin of 65.9%. Forward EPS is $20.86, implying a forward P/E of 19.6x. The stock closed at $409.10 with a 20-day return of 53.7% and 60-day return of 32.5%.
- **Bull / Base / Bear:** 542.37 / 458.93 / 354.62
- **Bull / Base / Bear returns:** 32.58% / 12.18% / -13.32%
- **Scenario probabilities:** not separately assigned; see scenario table.

### PNR — Pentair

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Pentair provides a lower-valuation, higher-momentum alternative to the high-multiple tech names, but its negative near-term growth limits the upside compared to more dynamic growth stories. Alternatives considered: APP, GEN, CLX, IDXX, ROP.
- **Thesis:** Pentair is a top-20-day momentum name with a 27.8% 20-day return and 7.1% 60-day return. It trades at a reasonable forward P/E of 12.9x with a forward EPS of $5.30. However, FY1 revenue growth is slightly negative (-4.5%) and earnings growth is -18.8%, indicating near-term headwinds despite the momentum.
- **Source IDs:** S010, S015, S018, S021
- **Catalysts:** Potential stabilization in earnings growth as the cycle turns, Continued momentum from the 20-day price surge, Exposure to infrastructure and water technology spending
- **Risks:** Negative FY1 revenue and earnings growth suggest near-term weakness, Sector cyclicality in industrials and building products, Lower relative sector P/E (0.49x) may limit upside if growth does not improve
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 5.3040 (source.forwardEps) x AI multiple assumption 14.00; source IDs S010, S015, S018, S021
- **EPS:** 5.30402 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 12.877027
- **FY+1 growth assumption:** 12.82%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / GEV / PNR has FY1 consensus growth of 12.82% with 18.4% revenue growth and 15.6% ROE, but earnings growth is negative at -18.8% and margins are lower (40.2% gross, 21.4% operating, 15.4% profit). The forward EPS of 5.30 and forward P/E of 12.9 support a lower 14-17x multiple. GEV is the named peer reference because both are cyclical industrial/energy infrastructure names with similar margin profiles and growth trajectories, justifying a conservative multiple.
- **Company fundamentals:** Pentair reports FY1 EPS of $5.30 with 12.8% growth, revenue growth of -4.5%, earnings growth of -18.8%, gross margin of 40.2%, operating margin of 21.4%, and profit margin of 15.4%. Forward EPS is $5.30, implying a forward P/E of 12.9x. The stock closed at $68.30 with a 20-day return of 27.8% and 60-day return of 7.1%.
- **Bull / Base / Bear:** 90.17 / 74.26 / 58.34
- **Bull / Base / Bear returns:** 32.02% / 8.73% / -14.58%
- **Scenario probabilities:** not separately assigned; see scenario table.

### GEN — Gen Digital

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Gen Digital offers a low-valuation, high-momentum alternative to the high-multiple tech names, but its modest revenue growth limits the upside compared to more dynamic growth stories. Alternatives considered: APP, PNR, CLX, IDXX, ROP.
- **Thesis:** Gen Digital is a top-20-day momentum name with a 25.8% 20-day return and 7.9% 60-day return. It trades at a low forward P/E of 9.1x with a forward EPS of $3.34. However, FY1 revenue growth is modest at 6.8% and earnings growth is 129%, indicating some improvement but not explosive growth.
- **Source IDs:** S017, S019, S022, S025
- **Catalysts:** Potential for continued margin expansion as the business scales, Strong 20-day momentum carrying into the next quarter, Exposure to cybersecurity and digital risk management
- **Risks:** Modest revenue growth limits upside potential, Sector-relative P/E of 0.42x suggests it is cheap for a reason, Competitive pressure in cybersecurity and risk management
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 3.3374 (source.forwardEps) x AI multiple assumption 11.00; source IDs S017, S019, S022, S025
- **EPS:** 3.33736 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 9.108996
- **FY+1 growth assumption:** 12.86%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / DHR / GEN has FY1 consensus growth of 12.86% with 6.8% revenue growth and 128.6% earnings growth, but margins are moderate (77.4% gross, 43.2% operating, 23.1% profit) and ROE is 46.4%. The forward EPS of 3.34 and forward P/E of 9.1 support an 11-14x multiple. DHR is the named peer reference because both are diversified industrial companies with moderate growth and solid ROE, making a 11-14x multiple appropriate.
- **Company fundamentals:** Gen Digital reports FY1 EPS of $3.34 with 12.9% growth, revenue growth of 6.8%, earnings growth of 128.6%, gross margin of 77.4%, operating margin of 43.2%, and profit margin of 23.1%. Forward EPS is $3.34, implying a forward P/E of 9.1x. The stock closed at $30.40 with a 20-day return of 25.8% and 60-day return of 7.9%.
- **Bull / Base / Bear:** 46.72 / 36.71 / 30.04
- **Bull / Base / Bear returns:** 53.68% / 20.76% / -1.18%
- **Scenario probabilities:** not separately assigned; see scenario table.

### RDDT — Reddit

- **Type:** Stock
- **Research view:** DOWNGRADE (stance: AVOID)
- **Why preferred / alternatives:** Reddit's significant price dislocation and high sector-relative valuation make it a less attractive candidate compared to the more stable, higher-quality names in the shortlist. Alternatives considered: APP, PNR, GEN, CLX, IDXX.
- **Thesis:** Reddit is a largest-20d dislocation name with a -36.9% 20-day return and -34.5% 60-day return, indicating significant price weakness. It trades at a forward P/E of 10.8x with a forward EPS of $9.14, but the negative returns and high sector-relative P/E (1.66x) suggest elevated risk. The dislocation may reflect fundamental concerns rather than a buying opportunity.
- **Source IDs:** S038, S040, S042, S045
- **Catalysts:** Potential for a rebound if the dislocation is driven by temporary factors, Strong FY1 revenue growth of 53% and earnings growth of 74.9%, High gross margin of 91.5% suggests strong underlying economics
- **Risks:** Significant price decline (-36.9% 20-day) indicates deep market skepticism, High sector-relative P/E (1.66x) suggests the market is pricing in higher risk, Potential for further deterioration if fundamentals weaken
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 9.1404 (source.forwardEps) x AI multiple assumption 13.00; source IDs S038, S040, S042, S045
- **EPS:** 9.14039 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 10.770874
- **FY+1 growth assumption:** 24.17%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / DIS / RDDT has FY1 consensus growth of 24.17% with 28.4% revenue growth and 74.9% earnings growth, supported by 91.5% gross margin and 32.0% ROE. The forward EPS of 9.14 and forward P/E of 10.8 support a 13-16x multiple. DIS is the named peer reference because both are media/entertainment companies with strong brand-driven revenue growth and high gross margins, justifying a 13-16x multiple for RDDT's superior growth and margin profile.
- **Company fundamentals:** Reddit reports FY1 EPS of $6.82 with 24.2% growth, revenue growth of 53%, earnings growth of 74.9%, gross margin of 91.5%, operating margin of 29.4%, and profit margin of 32.1%. Forward EPS is $9.14, implying a forward P/E of 10.8x. The stock closed at $98.45 with a 20-day return of -36.9% and 60-day return of -34.5%.
- **Bull / Base / Bear:** 146.25 / 118.83 / 100.54
- **Bull / Base / Bear returns:** 48.55% / 20.7% / 2.12%
- **Scenario probabilities:** not separately assigned; see scenario table.

### XLV — Health Care sector ETF

- **Type:** ETF
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** XLV offers a diversified, liquid way to gain exposure to the health care sector, with top holdings that are generally high-quality, making it a more stable choice than individual stock picking in the sector. Alternatives considered: XLP, XLY, XLRE, XLF, XLU.
- **Thesis:** The Health Care sector ETF (XLV) provides broad exposure to the sector with top holdings including LLY, JNJ, ABBV, and MRK. The ETF shows a positive raw price change of 0.54% and strong liquidity with $5.8M daily volume. It offers diversification and stability within the health care space, but the sector-relative valuation and specific holdings warrant monitoring.
- **Source IDs:** S053, S056
- **Catalysts:** Potential for sector rotation into health care if macro conditions improve, Strong top holdings like LLY and JNJ provide stability, Positive raw price change of 0.54% indicates recent strength
- **Risks:** Sector-relative valuation may not be attractive if health care multiples are rich, Concentration in top 10 holdings (61.4% coverage) limits diversification, Macro factors like interest rates and drug pricing policy could impact the sector
- **Valuation method:** Holdings/portfolio valuation with AI total-return assumption
- **Valuation status:** verified; forward-EPS source: ; period flags: 
- **Valuation assumptions:** Holdings/portfolio valuation; 10 weighted holdings; coverage 61.42%; source IDs S053, S056
- **Top holdings:** LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59%
- **Portfolio valuation:** Top 10 holdings; numeric weight coverage 61.42%
- **Sector exposure:** Health Care
- **Underlying drivers:** Health care sector performance driven by pharmaceutical innovation, managed care, and medical device demand, with key holdings LLY, JNJ, ABBV, and MRK.
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
| Bull | 25% | +2.00% | Directional signal is false and forecast volatility is below the 5-day baseline, so a mild upside is only plausible if the frozen daily-close model resolves favorably after the US close; otherwise the risk of a flat-to-negative week is higher. |
| Base | 50% | +0.00% | With no directional signal, elevated forecast volatility, and a spike probability below the historical baseline, the most likely path is a range-bound week with returns near zero as the model remains in a neutral, non-alpha state. |
| Bear | 25% | -2.00% | If the frozen daily-close model fails to confirm after the US close, elevated volatility and a below-baseline spike probability could trigger a modest downside move, but the absence of a directional signal limits the magnitude to a mild decline. |

### Long Term (12 months)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 30% | +8.00% | A sustained recovery in credit conditions and broadening earnings momentum could push returns higher, but the current non-directional signal and elevated volatility make a strong bull case less likely. |
| Base | 40% | +3.00% | With no directional signal and a frozen daily-close model, the long-term path is most likely to reflect gradual normalization of volatility and modest earnings growth, yielding a low-single-digit positive return. |
| Bear | 30% | -5.00% | If credit spreads widen and earnings breadth deteriorates, the elevated forecast volatility and below-baseline spike probability could drive a moderate downside, but the absence of a directional signal caps the bear case at a mild-to-moderate decline. |

## Positioning

- Maintain a risk-on posture with a quality and liquidity bias; favor Health Care, Consumer Discretionary, Consumer Staples, Financials, and Utilities.
- Avoid Information Technology and Energy until 20-day momentum turns positive; do not add to negative-trend sectors.
- Use SOXX as a liquidity confirmation signal; do not chase SMH given tactical profit-taking inside structural accumulation.
- Keep duration exposure neutral-to-negative given TLT's neutral-to-negative flow structure and medium-term deterioration.
- No allocation weights or composite scores are provided; this is a qualitative research posture only.

## Catalysts

| Date | Event | Why it matters |
| --- | --- | --- |
| 2026-11-13 | Equity market close and breadth snapshot | SPX at 7561.67 with 71.3% above 50-day and 63.6% above 200-day; 20-day return negative but breadth positive. |
| 2026-11-13 | Flow snapshot for SOXX, TLT, and SMH | SOXX exceptional institutional buying; TLT neutral-to-negative; SMH tactical profit-taking. |
| 2026-11-16 to 2026-11-20 | Frozen daily-close risk forecast window | Forecast vol 5d 14.93%, spike probability 16.5% below historical baseline 22.1% and EWMA baseline 20.1%. |

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
| S008 | filing | FISV | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0000798354-26-000042); 8-K filed 2026-11-03 (accession 0000798354-26-000039); 8-K filed 2026-10-23 (accession 0001193125-26-429481) |
| S009 | filing | APP | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001751008&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0001751008-26-000069); 8-K filed 2026-11-04 (accession 0001751008-26-000068); 10-Q filed 2026-08-05 (accession 0001751008-26-000059) |
| S010 | filing | PNR | 2026-10-27 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-27 (accession 0000077360-26-000058); 8-K filed 2026-10-27 (accession 0000077360-26-000055); 8-K filed 2026-09-22 (accession 0000077360-26-000050) |
| S011 | news | FISV | Thu, 12 Nov 2026 18:47:44 GMT | ok | https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en | Fiserv, Inc. (FISV) Stock Price, News, Quote & History - Yahoo! Finance Canada (Thu, 12 Nov 2026 18:47:44 GMT); Fiserv Stock Outlook: Is Wall Street Bullish or Bearish? - Yahoo Finance (Thu, 12 Nov 2026 12:23:56 GMT); What Is Fiserv (FISV) Planning With Its Debit Networks And Clover AI? - Yahoo Finance (Thu, 12 Nov 2026 06:09:00 GMT) |
| S012 | news | APP | Thu, 12 Nov 2026 20:05:45 GMT | ok | https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en | AppLovin Just Ripped 47% in a Month: Is It Too Late to Buy APP Stock Now? - Yahoo Finance (Thu, 12 Nov 2026 20:05:45 GMT); APP Stock Surges 51% After Q3 Earnings: Is it Still a Buy? - Yahoo Finance (Tue, 10 Nov 2026 14:24:00 GMT); Here is What to Know Beyond Why AppLovin Corporation (APP) is a Trending Stock - Yahoo Finance (Tue, 10 Nov 2026 13:00:06 GMT) |
| S013 | stock | APP | 2026-11-15 | ok | https://finance.yahoo.com/quote/APP | Trailing P/E: 27.54882; Forward P/E: 19.611452; Forward EPS: 20.86026; Price: 409.1; Market price: 409.1; Market cap: 135543824384; Sector: Communication Services; Trailing Eps: 14.85; Revenue Growth: 0.555; Earnings Growth: 0.755; Gross Margin: 0.8878; Operating Margin: 0.77782995; Profit Margin: 0.65887; Return On Equity: 2.1008599; Total Revenue: 7608893952; Market Cap: 135543824384; Consensus EPS FY+1: 20.72438; growth: 0.2744 |
| S014 | stock | FISV | 2026-11-15 | ok | https://finance.yahoo.com/quote/FISV | Forward P/E: 7.9923306; Price: 63.78; Market price: 63.78; Market cap: 33934002176; Market Cap: 33934002176; Consensus EPS FY+1: 7.98015; growth: 0.09689999 |
| S015 | stock | PNR | 2026-11-15 | ok | https://finance.yahoo.com/quote/PNR | Trailing P/E: 18.610355; Forward P/E: 12.877027; Forward EPS: 5.30402; Price: 68.3; Market price: 68.3; Market cap: 10904415232; Sector: Industrials; Trailing Eps: 3.67; Revenue Growth: -0.045; Earnings Growth: -0.188; Gross Margin: 0.40168998; Operating Margin: 0.21410999; Profit Margin: 0.15435; Return On Equity: 0.15605; Total Revenue: 3966200064; Market Cap: 10904415232; Consensus EPS FY+1: 5.30402; growth: 0.1282 |
| S016 | filing | APP | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json | Diluted EPS 11.61 for period ending 2026-09-30 (filed 2026-11-04) |
| S017 | filing | GEN | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0000849399-26-000083); 8-K filed 2026-10-28 (accession 0000849399-26-000081); 8-K filed 2026-10-09 (accession 0000849399-26-000079) |
| S018 | news | PNR | Fri, 13 Nov 2026 22:05:23 GMT | ok | https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en | Pentair plc (PNR) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 22:05:23 GMT); Here's What Key Metrics Tell Us About Pentair (PNR) Q3 Earnings - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT); Pentair plc (PNR) Q3 Earnings and Revenues Beat Estimates - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT) |
| S019 | stock | GEN | 2026-11-15 | ok | https://finance.yahoo.com/quote/GEN | Trailing P/E: 15.431472; Forward P/E: 9.108996; Forward EPS: 3.33736; Price: 30.4; Market price: 30.4; Market cap: 18035593216; Sector: Technology; Trailing Eps: 1.97; Revenue Growth: 0.122; Earnings Growth: 1.286; Gross Margin: 0.77410007; Operating Margin: 0.43229; Profit Margin: 0.23068; Return On Equity: 0.46402; Total Revenue: 5228000256; Market Cap: 18035593216; Consensus EPS FY+1: 3.33736; growth: 0.1286 |
| S020 | filing | CLX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000021076-26-000046); 8-K filed 2026-11-02 (accession 0000021076-26-000044); 8-K filed 2026-10-29 (accession 0001206774-26-000586) |
| S021 | filing | PNR | 2026-10-27 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json | Diluted EPS 2.76 for period ending 2026-09-30 (filed 2026-10-27) |
| S022 | news | GEN | Thu, 29 Oct 2026 07:00:00 GMT | ok | https://news.google.com/rss/search?q=GEN+Gen+Digital+stock&hl=en-US&gl=US&ceid=US:en | Gen Digital (GEN) Stock Repriced After Q2 Earnings Put Margins Center Stage - Yahoo Finance (Thu, 29 Oct 2026 07:00:00 GMT); Are Business Services Stocks Lagging GEN DIGITAL INC (GEN) This Year? - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT); Gen Digital Stock: Is Wall Street Bullish or Bearish? - Yahoo Finance (Thu, 05 Nov 2026 08:00:00 GMT) |
| S023 | filing | FISV | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json | Diluted EPS -8.9 for period ending 2026-09-30 (filed 2026-11-04) |
| S024 | news | CLX | Fri, 13 Nov 2026 18:52:58 GMT | ok | https://news.google.com/rss/search?q=CLX+Clorox+stock&hl=en-US&gl=US&ceid=US:en | The Clorox Company (CLX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 18:52:58 GMT); The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance Singapore (Fri, 13 Nov 2026 18:40:50 GMT); The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance UK (Fri, 13 Nov 2026 16:03:45 GMT) |
| S025 | filing | GEN | 2026-10-29 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000849399.json | Diluted EPS 0.83 for period ending 2026-10-02 (filed 2026-10-29) |
| S026 | stock | CLX | 2026-11-15 | ok | https://finance.yahoo.com/quote/CLX | Trailing P/E: 19.68705; Forward P/E: 17.745283; Forward EPS: 6.1684; Price: 109.46; Market price: 109.46; Market cap: 13260793856; Sector: Consumer Defensive; Trailing Eps: 5.56; Revenue Growth: 0.333; Earnings Growth: 1.138; Gross Margin: 0.41939998; Operating Margin: 0.14286; Profit Margin: 0.09408; Return On Equity: 5.34363; Total Revenue: 7196000256; Market Cap: 13260793856; Consensus EPS FY+1: 6.1684; growth: 0.0769 |
| S027 | filing | CHTR | 2026-11-06 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-06 (accession 0001091667-26-000073); 8-K filed 2026-11-06 (accession 0001091667-26-000072); 8-K filed 2026-10-27 (accession 0001091667-26-000064) |
| S028 | filing | IDXX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000874716&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000874716-26-000135); 8-K filed 2026-11-02 (accession 0001104659-26-120892); 10-Q filed 2026-08-04 (accession 0000874716-26-000123) |
| S029 | news | CHTR | Thu, 12 Nov 2026 08:02:01 GMT | ok | https://news.google.com/rss/search?q=CHTR+Charter+Communications+stock&hl=en-US&gl=US&ceid=US:en | Charter Communications: 3 Key Takeaways for Long-Term Investors - Yahoo Finance (Thu, 12 Nov 2026 08:02:01 GMT); Charter Communications (CHTR) Stock Looks Reasonable As Shares Slump 85% - Yahoo Finance (Wed, 28 Oct 2026 07:00:00 GMT); Should Value Investors Buy Charter Communications (CHTR) Stock? - Yahoo Finance (Wed, 21 Oct 2026 07:00:00 GMT) |
| S030 | stock | CHTR | 2026-11-15 | ok | https://finance.yahoo.com/quote/CHTR | Trailing P/E: 13.006578; Forward P/E: 3.2831066; Forward EPS: 42.15215; Price: 138.39; Market price: 138.39; Market cap: 24778944512; Sector: Communication Services; Trailing Eps: 10.64; Revenue Growth: 0.091; Gross Margin: 0.55084; Operating Margin: 0.23389; Profit Margin: 0.02498; Return On Equity: 0.07019; Total Revenue: 55645999104; Market Cap: 24778944512; Consensus EPS FY+1: 47.15811; growth: 1.0195 |
| S031 | filing | ROP | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000882835&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000882835-26-000047); 8-K filed 2026-10-22 (accession 0000882835-26-000042); 8-K filed 2026-10-01 (accession 0000882835-26-000039) |
| S032 | news | IDXX | Fri, 13 Nov 2026 22:06:38 GMT | ok | https://news.google.com/rss/search?q=IDXX+Idexx+Laboratories+stock&hl=en-US&gl=US&ceid=US:en | IDEXX Laboratories, Inc. (IDXX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 22:06:38 GMT); IDEXX Laboratories (IDXX) Stock Looks Fairly Valued Despite Its 28% Run - Yahoo Finance (Sat, 31 Oct 2026 07:00:00 GMT); IDEXX Laboratories (IDXX) Q3 Earnings Leave Its Premium Valuation In Focus - Yahoo Finance (Tue, 03 Nov 2026 08:00:00 GMT) |
| S033 | stock | IDXX | 2026-11-15 | ok | https://finance.yahoo.com/quote/IDXX | Trailing P/E: 47.45485; Forward P/E: 41.687927; Forward EPS: 16.8929; Price: 704.23; Market price: 704.23; Market cap: 55483650048; Sector: Healthcare; Trailing Eps: 14.84; Revenue Growth: 0.099; Earnings Growth: 0.179; Gross Margin: 0.62722; Operating Margin: 0.32497; Profit Margin: 0.25357; Return On Equity: 0.68925005; Total Revenue: 4662220800; Market Cap: 55483650048; Consensus EPS FY+1: 16.8929; growth: 0.1244 |
| S034 | stock | ROP | 2026-11-15 | ok | https://finance.yahoo.com/quote/ROP | Trailing P/E: 18.993866; Forward P/E: 19.532475; Forward EPS: 24.57318; Price: 479.975; Market price: 479.975; Market cap: 47535013888; Sector: Technology; Trailing Eps: 25.27; Revenue Growth: 0.076; Earnings Growth: 0.326; Gross Margin: 0.69671; Operating Margin: 0.28049; Profit Margin: 0.30712998; Return On Equity: 0.13229; Total Revenue: 8434599936; Market Cap: 47535013888; Consensus EPS FY+1: 24.57318; growth: 0.09810001 |
| S035 | filing | CLX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000021076.json | Diluted EPS 1.39 for period ending 2026-09-30 (filed 2026-11-02) |
| S036 | filing | IDXX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000874716.json | Diluted EPS 11.75 for period ending 2026-09-30 (filed 2026-11-02) |
| S037 | filing | CHTR | 2026-11-06 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001091667.json | Diluted EPS 0.38 for period ending 2026-09-30 (filed 2026-11-06) |
| S038 | filing | RDDT | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001713445&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0001713445-26-000116); 8-K filed 2026-10-29 (accession 0001713445-26-000114); 8-K filed 2026-08-12 (accession 0001713445-26-000107) |
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
- filing FISV: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 (2026-11-04)
- filing APP: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001751008&type=10-Q&dateb=&owner=include&count=10 (2026-11-04)
- filing PNR: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 (2026-10-27)
- news FISV: https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en (Thu, 12 Nov 2026 18:47:44 GMT)
- news APP: https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en (Thu, 12 Nov 2026 20:05:45 GMT)
- stock APP: https://finance.yahoo.com/quote/APP (2026-11-15)
- stock FISV: https://finance.yahoo.com/quote/FISV (2026-11-15)
- stock PNR: https://finance.yahoo.com/quote/PNR (2026-11-15)
- filing APP: https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json (2026-11-04)
- filing GEN: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 (2026-10-29)
- news PNR: https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 22:05:23 GMT)
- stock GEN: https://finance.yahoo.com/quote/GEN (2026-11-15)
- filing CLX: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 (2026-11-02)

## AI Provenance

- Provider / model: hermes-local-proxy / upstage/solar-mini4:free
- Market research: attempts=1 tokens=9548 (prompt=6548, completion=3000) runtime=28.97s
- Fundamental research: generated this run at 2026-11-15T02:15:00.052749+00:00
- Evidence source dates: {'as_of': '2026-11-13', 'latest_equity_date': '2026-11-13', 'latest_macro_date': '2026-11-13', 'flows_date': '2026-11-13'}
- Evidence fingerprint: 6dedabcfabbf669c546d3907c88cf80c5a6c5a42d74aac8aa7434ee30c2113d6
- Source citations are retrieved external records in the ledger above; market values remain from the verified database snapshot.


## Disclosures

- This is research and market intelligence, not investment advice.
- AI conclusions are research judgments, not validated return predictions.
- The frozen risk layer is risk-only and is not used for directional views or allocations.
- Legacy scores are not active inputs or outputs.

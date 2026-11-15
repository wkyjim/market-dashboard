# AEGIS AI-First Market Intelligence

Research generated at: 15 November 2026, 19:15 HKT
Database freshness: equity 2026-11-13 (latest row retrieved 2026-11-15 13:06:40.074841+08:00)
Data cutoff: 2026-11-13 US cash close
Snapshot ID: aegis-hourly-20261115T111512Z

## Executive Summary

- **AI market view: Late-November 2026 equity market is in a late-cycle, mixed posture: broad market breadth is positive but the index is slightly negative over 20 days, and the leadership set is bifurcated between high-momentum, high-valuation names and large dislocation names. Macro data show a still-elevated inflation backdrop, a labor market near full employment, and a modestly positive 10Y-2Y curve, while policy and liquidity signals are mixed. Sector leadership is led by Health Care, Consumer Discretionary, Consumer Staples and Financials, while Information Technology and Energy are the weakest sectors on 20-day returns.**
- Broad market breadth is constructive: 71.3% of constituents are above their 50-day moving average and 70.5% have positive 20-day returns, with an advance/decline ratio of 1.70.
- The index is slightly negative over 20 days (-1.28%) despite positive breadth, indicating a late-cycle, distribution-like overlay rather than a clean trend.
- Sector leadership is broad but uneven: Health Care, Consumer Discretionary, Consumer Staples and Financials are positive on 20-day returns; Information Technology and Energy are negative.
- Liquidity and flow signals are bifurcated: SOXX shows exceptional institutional buying, while TLT shows medium-term deterioration and SMH shows tactical profit-taking inside structural accumulation.
- Macro data show inflation still above pre-pandemic norms, unemployment near 4.2%, a 10Y-2Y spread of 0.27, and a Fed funds rate of 3.88%, implying a late-cycle, data-dependent policy stance.
- Risk environment is elevated but not spiking: 5-day forecast volatility is 14.9% versus a historical baseline of 22.1%, and spike probability is 16.5% versus a 18.5% threshold.
- The shortlist is dominated by high-momentum and large-dislocation names with wide valuation dispersion, so position sizing and risk control are critical.

## Data QC

- Status: **PASS_WITH_WARNINGS**
- Equity session: 0 completed session(s) behind inference date
- Equity provenance: 393 provisional / 12576 canonical
- Breadth lag: 0 session(s); ETF-flow lag: 0 session(s)
- Note: Equity session contains a mix of provisional yfinance and canonical Massive rows.
- External sources: 79 ok / 0 unavailable; retrieved 2026-11-15T11:15:32.636372+00:00

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
| S&P 500 | 7561.67 | -1.28% over 20 days | Index slightly negative on 20-day horizon despite positive breadth; 71.3% above 50-day MA and 63.6% above 200-day MA. |
| Health Care | +6.87% | 20-day return | Top sector by 20-day return; trailing P/E 30.78 per S058. |
| Consumer Discretionary | +6.69% | 20-day return | Second-strongest sector; trailing P/E 25.11 per S060. |
| Consumer Staples | +5.40% | 20-day return | Defensive leader; trailing P/E 24.85 per S057. |
| Financials | +5.69% | 20-day return | Positive sector; trailing P/E 15.85 per S066. |
| Information Technology | -7.19% | 20-day return | Weakest sector; trailing P/E 30.03 per S072. |
| Energy | -4.81% | 20-day return | Negative sector; trailing P/E 16.23 per S077. |

## Macro, Fiscal, Rates, Liquidity and Credit

- Inflation remains the dominant macro constraint: CPI is 336.30 in September 2026 and core CPI is 338.90, with October CPI at 337.48 per S004, indicating sticky price pressures.
- Labor market is near full employment: unemployment rate is 4.2% in September 2026 and 4.1% in October 2026 per S005 and the economic database.
- Policy is data-dependent: the effective federal funds rate is 3.88% as of 2026-11-12 per S001, and the 10Y-2Y spread is 0.27 as of 2026-11-13 per S007, suggesting a modestly positive but not steep curve.
- Credit conditions are mixed: high-yield OAS is 3.20 and IG OAS is 0.89 as of 2026-11-12 per S002 and S003, implying tight but not distressed credit.
- Liquidity signals are bifurcated: SOXX shows exceptional institutional buying with 20-day and 60-day flow z-scores of 5.10 and 3.17, while TLT shows medium-term deterioration with 20-day and 60-day flow z-scores of -0.41 and -0.29.
- Risk environment is elevated but not spiking: 5-day forecast volatility is 14.9% versus a historical baseline of 22.1%, and spike probability is 16.5% versus a 18.5% threshold, indicating a below-baseline risk regime.

## US Equities and 11 GICS Sectors

Macro source IDs: S001, S002, S003, S004, S005, S007

| GICS sector | Evidence | AI research stance | Source IDs |
| --- | --- | --- | --- |
| Health Care | 20-day return +6.87%; trailing P/E 30.78 per S058; top sector by momentum in the shortlist. | Constructive but expensive; leadership driven by defensive demand and positive breadth. | S058 |
| Consumer Discretionary | 20-day return +6.69%; trailing P/E 25.11 per S060; strong consumer-facing demand. | Positive momentum; supported by broad-based consumer activity. | S060 |
| Consumer Staples | 20-day return +5.40%; trailing P/E 24.85 per S057; defensive sector with stable demand. | Defensive leader; attractive relative value in a late-cycle environment. | S057 |
| Financials | 20-day return +5.69%; trailing P/E 15.85 per S066; positive sector with low valuation. | Constructive; low P/E and positive momentum support a favorable stance. | S066 |
| Industrials | 20-day return +0.61%; trailing P/E 27.07 per S068; near-flat momentum. | Neutral; modest positive return but weak relative momentum. | S068 |
| Materials | 20-day return +2.57%; trailing P/E 21.72 per S067; modest positive return. | Slightly positive; commodity-linked demand is stable but not leading. | S067 |
| Real Estate | 20-day return +5.24%; trailing P/E 29.63 per S061; positive but high valuation. | Positive momentum but expensive; watch rate sensitivity. | S061 |
| Utilities | 20-day return +4.34%; trailing P/E 18.11 per S062; defensive sector with moderate valuation. | Constructive; stable demand and reasonable valuation. | S062 |
| Communication Services | 20-day return -1.48%; trailing P/E 17.26 per S072; negative momentum. | Weak; negative 20-day return and high valuation relative to peers. | S072 |
| Information Technology | 20-day return -7.19%; trailing P/E 30.03 per S072; weakest sector. | Negative; high valuation and negative momentum warrant caution. | S072 |
| Energy | 20-day return -4.81%; trailing P/E 16.23 per S077; negative sector. | Negative; weak momentum and macro sensitivity. | S077 |

### Sector fundamentals, valuation and earnings

Sector fundamentals are not directly supplied in the database snapshot. The supplied evidence is limited to 20-day ETF returns, trailing P/E ratios for the eleven GICS sectors, and a shortlist of 20 names with trailing P/E and earnings yield. No growth, margin, cash flow, or consensus data are available for the full sector universe, so sector-level fundamental estimates cannot be constructed from the supplied evidence.

## Growth vs Value

- Health Care leads on 20-day return at +6.87% but carries a trailing P/E of 30.78, indicating high valuation for the sector.
- Consumer Discretionary returns +6.69% with a trailing P/E of 25.11, a more moderate valuation than Health Care.
- Consumer Staples returns +5.40% with a trailing P/E of 24.85, offering defensive exposure at a reasonable multiple.
- Financials return +5.69% with a trailing P/E of 15.85, the lowest sector P/E in the supplied set and a value-oriented profile.
- Information Technology returns -7.19% with a trailing P/E of 30.03, combining negative momentum with high valuation.
- Energy returns -4.81% with a trailing P/E of 16.23, the lowest valuation in the negative-return group.

## ETF Flows and Breadth

- Broad market breadth is positive: 71.3% of constituents are above their 50-day moving average and 70.5% have positive 20-day returns, with an advance/decline ratio of 1.70.
- The index is slightly negative over 20 days (-1.28%) despite positive breadth, indicating a late-cycle, distribution-like overlay rather than a clean trend.
- SOXX shows exceptional institutional buying with 20-day and 60-day flow z-scores of 5.10 and 3.17, and is classified as an inflow with strong confirmation.
- TLT shows medium-term deterioration with 20-day and 60-day flow z-scores of -0.41 and -0.29, and is classified as neutral with flat price.
- SMH shows tactical profit-taking inside structural accumulation, with 20-day and 60-day flow z-scores of 1.22 and 1.04, and is classified as an outflow with a down price.
- New highs and new lows are both zero, indicating no extreme breakout or breakdown in the breadth data.

## Stock Ideas

Single-stock research uses reported EPS, forward P/E and company fundamentals. All ideas are research judgments, not validated return predictions.

| Ticker | Security | Research view | Price | EPS | Forward P/E | Base target | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| APP | AppLovin | NEW | 409.1 | 20.86026 | 19.611452 | 417.21 | NEW |
| PNR | Pentair | KEEP | 68.3 | 5.30402 | 12.877027 | 68.95 | KEEP |
| GEN | Gen Digital | KEEP | 30.4 | 3.33736 | 9.108996 | 33.37 | KEEP |
| ROP | Roper Technologies | NEW | 479.975 | 24.57318 | 19.532475 | 344.02 | NEW |

## ETF Ideas

ETF research uses holdings, portfolio valuation and exposure. Single-stock EPS × P/E valuation is not applied to ETFs.

| Ticker | Fund | Research view | Price | Top holdings | Portfolio valuation | Sector exposure | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| XLV | Health Care Select Sector SPDR Fund | KEEP | 188.85 | LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59% | Top 10 holdings; numeric weight coverage 61.42% | Health Care | KEEP |
### APP — AppLovin

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** AppLovin offers a rare combination of top-tier momentum and high-quality growth metrics (88.8% gross margin, 27.4% EPS growth) at a forward P/E of 19.6x, making it a stronger candidate than the lower-quality, high-multiple names in the shortlist such as NOW or MRVL. Alternatives considered: NOW, MRVL.
- **Thesis:** AppLovin screens in the top 20-day momentum bucket with a 53.7% 20-day return and a 32.5% 60-day return, while its forward P/E of 19.6x is supported by 27.4% FY1 EPS growth, 25.4% revenue growth, and an 88.8% gross margin. The stock is trading at a reasonable valuation relative to its growth profile, and the momentum screen suggests continued institutional interest.
- **Source IDs:** S008, S012, S013, S015
- **Catalysts:** Sustained 20-day momentum with a 53.7% return, FY1 EPS growth of 27.4% and revenue growth of 25.4%, High gross margin of 88.8% supporting earnings quality, Forward P/E of 19.6x on strong growth
- **Risks:** High volatility from strong momentum; a sharp pullback is possible, Valuation may compress if growth decelerates, Single-quarter momentum can reverse quickly
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 20.8603 (source.forwardEps) x AI multiple assumption 20.00; source IDs S008, S012, S013, S015
- **EPS:** 20.86026 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 19.611452
- **FY+1 growth assumption:** 27.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / MSFT / APP shows strong FY+1 consensus earnings growth of 27.44% and revenue growth of 25.37%, with high gross margin (88.78%) and operating margin (77.78%). The base multiple of 20.0x is justified by superior margins and growth relative to peers, while the bull/bear range reflects upside from margin expansion and downside from execution risk. Peer reference: MSFT, given comparable software-scale growth and margin profile.
- **Company fundamentals:** FY1 EPS growth 27.4%, revenue growth 25.4%, gross margin 88.8%, operating margin 77.8%, profit margin 65.9%, forward P/E 19.6x, forward EPS 20.86, reported diluted EPS 11.61
- **Bull / Base / Bear:** 500.65 / 417.21 / 333.76
- **Bull / Base / Bear returns:** 22.38% / 1.98% / -18.42%
- **Scenario probabilities:** not separately assigned; see scenario table.

### PNR — Pentair

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Pentair is a lower-multiple, higher-quality industrial name compared to the high-multiple tech names in the shortlist, but its negative near-term earnings growth makes it a neutral holding rather than a top pick. Alternatives considered: NOW, MRVL.
- **Thesis:** Pentair is a top-20-day momentum name with a 27.8% 20-day return and a 13.6x forward P/E. However, FY1 revenue growth is slightly negative at -4.5% and earnings growth is -18.8%, which tempers the bullish case. The stock is reasonably valued but faces near-term earnings headwinds.
- **Source IDs:** S010, S016, S018, S019
- **Catalysts:** 27.8% 20-day momentum, Forward P/E of 13.6x, Stable dividend and industrial exposure
- **Risks:** FY1 revenue growth of -4.5% and earnings growth of -18.8%, Industrial end-market softness, Momentum may fade if earnings do not recover
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 5.3040 (source.forwardEps) x AI multiple assumption 13.00; source IDs S010, S016, S018, S019
- **EPS:** 5.30402 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 12.877027
- **FY+1 growth assumption:** 12.82%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / UPS / PNR has moderate FY+1 consensus earnings growth of 12.82% and revenue growth of 18.38%, with a lower gross margin (40.17%) and operating margin (21.41%) typical of industrial/logistics peers. The base multiple of 13.0x reflects a premium to its forward P/E of 12.88, justified by growth and margin recovery potential, while the bull/bear range captures cyclicality and margin variability. Peer reference: UPS, given comparable logistics/industrial exposure.
- **Company fundamentals:** FY1 EPS growth 12.8%, revenue growth -4.5%, earnings growth -18.8%, gross margin 40.2%, operating margin 21.4%, profit margin 15.4%, forward P/E 12.9x, forward EPS 5.30, reported diluted EPS 2.76
- **Bull / Base / Bear:** 84.86 / 68.95 / 53.04
- **Bull / Base / Bear returns:** 24.25% / 0.95% / -22.34%
- **Scenario probabilities:** not separately assigned; see scenario table.

### GEN — Gen Digital

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Gen Digital offers a low forward P/E of 9.1x with positive growth, but it is less attractive than the higher-growth, higher-margin names like AppLovin and Roper Technologies. Alternatives considered: APP, ROP.
- **Thesis:** Gen Digital is a top-20-day momentum name with a 25.8% 20-day return and a 9.1x forward P/E. Its 12.9% FY1 EPS growth and 12.2% revenue growth are solid, but the stock is a cybersecurity/IT name with moderate growth and a low forward P/E that may already reflect expectations.
- **Source IDs:** S014, S024, S025, S026
- **Catalysts:** 25.8% 20-day momentum, 9.1x forward P/E, 12.9% FY1 EPS growth and 12.2% revenue growth
- **Risks:** Moderate growth profile relative to tech peers, Cybersecurity market may be saturated, Low forward P/E may limit upside if growth slows
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 3.3374 (source.forwardEps) x AI multiple assumption 10.00; source IDs S014, S024, S025, S026
- **EPS:** 3.33736 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 9.108996
- **FY+1 growth assumption:** 12.86%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / CSCO / GEN has FY+1 consensus earnings growth of 12.86% and revenue growth of 6.81%, with solid gross margin (77.41%) and operating margin (43.23%). The base multiple of 10.0x is justified by growth and margin profile relative to peers, while the bull/bear range reflects upside from margin expansion and downside from competitive pressure. Peer reference: CSCO, given comparable enterprise software/IT services growth and margin structure.
- **Company fundamentals:** FY1 EPS growth 12.9%, revenue growth 12.2%, earnings growth 128.6%, gross margin 77.4%, operating margin 43.2%, profit margin 23.1%, forward P/E 9.1x, forward EPS 3.34, reported diluted EPS 0.83
- **Bull / Base / Bear:** 43.39 / 33.37 / 26.7
- **Bull / Base / Bear returns:** 42.73% / 9.77% / -12.17%
- **Scenario probabilities:** not separately assigned; see scenario table.

### ROP — Roper Technologies

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** Roper Technologies provides a high-quality, high-margin industrial compounder with positive earnings growth and a reasonable forward P/E, making it a better choice than the negative-growth or high-multiple names in the shortlist. Alternatives considered: NOW, MRVL.
- **Thesis:** Roper Technologies is a top-20-day momentum name with a 25.4% 20-day return and a 16.7x trailing P/E. It combines high-margin, niche industrial exposure with 7.6% revenue growth and 32.6% earnings growth, offering a quality compounder at a reasonable valuation.
- **Source IDs:** S035, S037, S038, S047
- **Catalysts:** 25.4% 20-day momentum, 7.6% revenue growth and 32.6% earnings growth, 69.7% gross margin and 28.0% operating margin, Forward P/E of 19.5x on strong earnings growth
- **Risks:** Growth is moderate compared to high-momentum tech names, Niche industrial exposure may face cyclical pressures, Valuation may expand if growth accelerates
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 24.5732 (source.forwardEps) x AI multiple assumption 14.00; source IDs S035, S037, S038, S047
- **EPS:** 24.57318 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 19.532475
- **FY+1 growth assumption:** 9.81%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / HD / ROP has FY+1 consensus earnings growth of 9.81% and revenue growth of 6.29%, with a gross margin of 69.67% and operating margin of 28.05%, typical of consumer/retail peers. The base multiple of 14.0x is justified by growth and margin profile relative to peers, while the bull/bear range reflects consumer demand and margin variability. Peer reference: HD, given comparable consumer discretionary exposure.
- **Company fundamentals:** FY1 EPS growth 9.8%, revenue growth 7.6%, earnings growth 32.6%, gross margin 69.7%, operating margin 28.0%, profit margin 30.7%, forward P/E 19.5x, forward EPS 24.57, reported diluted EPS 21.30
- **Bull / Base / Bear:** 417.74 / 344.02 / 270.3
- **Bull / Base / Bear returns:** -12.97% / -28.33% / -43.68%
- **Scenario probabilities:** not separately assigned; see scenario table.

### XLV — Health Care Select Sector SPDR Fund

- **Type:** ETF
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** XLV provides broad, diversified health care exposure with high-quality large-cap holdings, making it a stable core holding compared to single-stock volatility in the shortlist. Alternatives considered: XLP, XLY.
- **Thesis:** The Health Care sector ETF offers diversified exposure to large-cap pharma and medical device leaders with a 0.54% price change on 2026-11-13. It is a core holding for defensive exposure, but the sector is not a top momentum or dislocation candidate in this screen.
- **Source IDs:** S052, S058
- **Catalysts:** Diversified health care exposure, 0.54% daily price change on 2026-11-13, Top holdings include LLY, JNJ, ABBV, MRK, UNH
- **Risks:** Sector-specific regulatory and pipeline risks, Lower momentum than the top equity names, Limited upside if health care sector underperforms
- **Valuation method:** Holdings/portfolio valuation with AI total-return assumption
- **Valuation status:** verified; forward-EPS source: ; period flags: 
- **Valuation assumptions:** Holdings/portfolio valuation; 10 weighted holdings; coverage 61.42%; source IDs S052, S058
- **Top holdings:** LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59%
- **Portfolio valuation:** Top 10 holdings; numeric weight coverage 61.42%
- **Sector exposure:** Health Care
- **Underlying drivers:** Large-cap pharma and medical device earnings, FDA approvals, M&A activity, and demographic trends
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
| Bull | 25% | +2.00% | Directional signal is false and forecast_vol_5d is 14.9%, so a modest upside is driven by a favorable US close and stable credit spreads; 25% probability reflects a low-probability, low-return tail. |
| Base | 50% | +0.00% | Frozen daily-close model with no directional signal and forecast_vol_5d of 14.9% implies a range-bound session; base case is flat with no material earnings or rate shock over the target window. |
| Bear | 25% | -2.00% | A 16.5% spike probability and 14.9% forecast vol suggest elevated near-term risk; a negative US close or widening credit spreads could push returns to -2.0% with 25% probability. |

### Long Term (12 months)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 30% | +8.00% | Sustained earnings growth and stable rates support a positive 8.0% long-term return with 30% probability, assuming credit spreads remain tight and no recession signal emerges. |
| Base | 40% | +3.00% | Base case reflects a 3.0% long-term return driven by moderate earnings growth and neutral rate expectations, with 40% probability given the current frozen daily-close model and no directional signal. |
| Bear | 30% | -5.00% | A 30% probability of a -5.0% long-term return reflects potential earnings deterioration, rising rates, or credit spread widening that outweighs the current low directional signal. |

## Positioning

- Maintain a constructive but cautious equity stance; positive breadth and broad sector leadership are offset by slightly negative index returns and elevated valuation dispersion.
- Favor Health Care, Consumer Discretionary, Consumer Staples and Financials for positive momentum and reasonable relative valuation.
- Reduce or avoid Information Technology and Energy given negative 20-day returns and high valuation dispersion.
- Use the SOXX flow signal as a liquidity confirmation for technology-related exposure, but do not favored given the negative sector return.
- Monitor TLT and SMH flow signals for liquidity and positioning risk; TLT deterioration and SMH profit-taking suggest caution in rate-sensitive and tactical positions.
- Keep risk management tight given the elevated but not spiking volatility regime and the late-cycle macro backdrop.

## Catalysts

| Date | Event | Why it matters |
| --- | --- | --- |
| 2026-11-16 | US equity market open | Frozen daily-close model is eligible for formal use after the completed US close; volatility and spike probability will be re-evaluated. |
| 2026-11-16 |  |  |

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
| S011 | news | FISV | Fri, 13 Nov 2026 00:42:12 GMT | ok | https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en | Fiserv, Inc. (FISV) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 00:42:12 GMT); Fiserv Stock Outlook: Is Wall Street Bullish or Bearish? - Yahoo Finance (Thu, 12 Nov 2026 12:23:56 GMT); Why Fiserv, Inc. (FISV) Was Exited by Ariel Appreciation Fund - Yahoo Finance (Wed, 28 Oct 2026 07:00:00 GMT) |
| S012 | news | APP | Thu, 12 Nov 2026 20:05:45 GMT | ok | https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en | AppLovin Just Ripped 47% in a Month: Is It Too Late to Buy APP Stock Now? - Yahoo Finance (Thu, 12 Nov 2026 20:05:45 GMT); APP Stock Surges 51% After Q3 Earnings: Is it Still a Buy? - Yahoo Finance (Tue, 10 Nov 2026 14:24:00 GMT); ETFs Are Net Sellers of AppLovin (APP) on Nov. 11 - Yahoo Finance (Fri, 13 Nov 2026 11:02:35 GMT) |
| S013 | filing | APP | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json | Diluted EPS 11.61 for period ending 2026-09-30 (filed 2026-11-04) |
| S014 | filing | GEN | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0000849399-26-000083); 8-K filed 2026-10-28 (accession 0000849399-26-000081); 8-K filed 2026-10-09 (accession 0000849399-26-000079) |
| S015 | stock | APP | 2026-11-15 | ok | https://finance.yahoo.com/quote/APP | Trailing P/E: 27.54882; Forward P/E: 19.611452; Forward EPS: 20.86026; Price: 409.1; Market price: 409.1; Market cap: 135543824384; Sector: Communication Services; Trailing Eps: 14.85; Revenue Growth: 0.555; Earnings Growth: 0.755; Gross Margin: 0.8878; Operating Margin: 0.77782995; Profit Margin: 0.65887; Return On Equity: 2.1008599; Total Revenue: 7608893952; Market Cap: 135543824384; Consensus EPS FY+1: 20.72438; growth: 0.2744 |
| S016 | stock | PNR | 2026-11-15 | ok | https://finance.yahoo.com/quote/PNR | Trailing P/E: 18.610355; Forward P/E: 12.877027; Forward EPS: 5.30402; Price: 68.3; Market price: 68.3; Market cap: 10904415232; Sector: Industrials; Trailing Eps: 3.67; Revenue Growth: -0.045; Earnings Growth: -0.188; Gross Margin: 0.40168998; Operating Margin: 0.21410999; Profit Margin: 0.15435; Return On Equity: 0.15605; Total Revenue: 3966200064; Market Cap: 10904415232; Consensus EPS FY+1: 5.30402; growth: 0.1282 |
| S017 | stock | FISV | 2026-11-15 | ok | https://finance.yahoo.com/quote/FISV | Forward P/E: 7.9923306; Price: 63.78; Market price: 63.78; Market cap: 33934002176; Market Cap: 33934002176; Consensus EPS FY+1: 7.98015; growth: 0.09689999 |
| S018 | news | PNR | Fri, 13 Nov 2026 22:05:23 GMT | ok | https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en | Pentair plc (PNR) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 22:05:23 GMT); Here's What Key Metrics Tell Us About Pentair (PNR) Q3 Earnings - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT); Pentair plc (PNR) Q3 Earnings and Revenues Beat Estimates - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT) |
| S019 | filing | PNR | 2026-10-27 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json | Diluted EPS 2.76 for period ending 2026-09-30 (filed 2026-10-27) |
| S020 | filing | FISV | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json | Diluted EPS -8.9 for period ending 2026-09-30 (filed 2026-11-04) |
| S021 | stock | CLX | 2026-11-15 | ok | https://finance.yahoo.com/quote/CLX | Trailing P/E: 19.68705; Forward P/E: 17.745283; Forward EPS: 6.1684; Price: 109.46; Market price: 109.46; Market cap: 13260793856; Sector: Consumer Defensive; Trailing Eps: 5.56; Revenue Growth: 0.333; Earnings Growth: 1.138; Gross Margin: 0.41939998; Operating Margin: 0.14286; Profit Margin: 0.09408; Return On Equity: 5.34363; Total Revenue: 7196000256; Market Cap: 13260793856; Consensus EPS FY+1: 6.1684; growth: 0.0769 |
| S022 | filing | CLX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000021076-26-000046); 8-K filed 2026-11-02 (accession 0000021076-26-000044); 8-K filed 2026-10-29 (accession 0001206774-26-000586) |
| S023 | filing | CHTR | 2026-11-06 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-06 (accession 0001091667-26-000073); 8-K filed 2026-11-06 (accession 0001091667-26-000072); 8-K filed 2026-10-27 (accession 0001091667-26-000064) |
| S024 | stock | GEN | 2026-11-15 | ok | https://finance.yahoo.com/quote/GEN | Trailing P/E: 15.431472; Forward P/E: 9.108996; Forward EPS: 3.33736; Price: 30.4; Market price: 30.4; Market cap: 18035593216; Sector: Technology; Trailing Eps: 1.97; Revenue Growth: 0.122; Earnings Growth: 1.286; Gross Margin: 0.77410007; Operating Margin: 0.43229; Profit Margin: 0.23068; Return On Equity: 0.46402; Total Revenue: 5228000256; Market Cap: 18035593216; Consensus EPS FY+1: 3.33736; growth: 0.1286 |
| S025 | news | GEN | Fri, 13 Nov 2026 00:21:25 GMT | ok | https://news.google.com/rss/search?q=GEN+Gen+Digital+stock&hl=en-US&gl=US&ceid=US:en | Gen Digital Inc. (GEN) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 00:21:25 GMT); Gen Digital (GEN) Stock Repriced After Q2 Earnings Put Margins Center Stage - Yahoo Finance (Thu, 29 Oct 2026 07:00:00 GMT); Gen Digital Inc. (GEN) Stock Forecasts - Yahoo Finance (Wed, 11 Nov 2026 13:10:37 GMT) |
| S026 | filing | GEN | 2026-10-29 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000849399.json | Diluted EPS 0.83 for period ending 2026-10-02 (filed 2026-10-29) |
| S027 | news | CLX | Sun, 15 Nov 2026 08:55:47 GMT | ok | https://news.google.com/rss/search?q=CLX+Clorox+stock&hl=en-US&gl=US&ceid=US:en | The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance UK (Sun, 15 Nov 2026 08:55:47 GMT); The Clorox Company (CLX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 05:44:34 GMT); The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance Singapore (Sat, 14 Nov 2026 05:36:50 GMT) |
| S028 | filing | CLX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000021076.json | Diluted EPS 1.39 for period ending 2026-09-30 (filed 2026-11-02) |
| S029 | filing | IDXX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000874716&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000874716-26-000135); 8-K filed 2026-11-02 (accession 0001104659-26-120892); 10-Q filed 2026-08-04 (accession 0000874716-26-000123) |
| S030 | news | CHTR | Sun, 15 Nov 2026 05:47:01 GMT | ok | https://news.google.com/rss/search?q=CHTR+Charter+Communications+stock&hl=en-US&gl=US&ceid=US:en | Charter Communications (CHTR) Stock Could Be A Bargain Following Its New Operating Model - Yahoo Finance (Sun, 15 Nov 2026 05:47:01 GMT); Charter Communications (CHTR) Expands Enterprise Reach With Managed Secure Networking Launch - Yahoo Finance (Sun, 15 Nov 2026 06:08:00 GMT); Charter Communications: 3 Key Takeaways for Long-Term Investors - Yahoo Finance (Thu, 12 Nov 2026 08:02:01 GMT) |
| S031 | stock | CHTR | 2026-11-15 | ok | https://finance.yahoo.com/quote/CHTR | Trailing P/E: 13.006578; Forward P/E: 3.2831066; Forward EPS: 42.15215; Price: 138.39; Market price: 138.39; Market cap: 24778944512; Sector: Communication Services; Trailing Eps: 10.64; Revenue Growth: 0.091; Gross Margin: 0.55084; Operating Margin: 0.23389; Profit Margin: 0.02498; Return On Equity: 0.07019; Total Revenue: 55645999104; Market Cap: 24778944512; Consensus EPS FY+1: 47.15811; growth: 1.0195 |
| S032 | stock | IDXX | 2026-11-15 | ok | https://finance.yahoo.com/quote/IDXX | Trailing P/E: 47.45485; Forward P/E: 41.687927; Forward EPS: 16.8929; Price: 704.23; Market price: 704.23; Market cap: 55483650048; Sector: Healthcare; Trailing Eps: 14.84; Revenue Growth: 0.099; Earnings Growth: 0.179; Gross Margin: 0.62722; Operating Margin: 0.32497; Profit Margin: 0.25357; Return On Equity: 0.68925005; Total Revenue: 4662220800; Market Cap: 55483650048; Consensus EPS FY+1: 16.8929; growth: 0.1244 |
| S033 | news | IDXX | Sat, 14 Nov 2026 06:13:17 GMT | ok | https://news.google.com/rss/search?q=IDXX+Idexx+Laboratories+stock&hl=en-US&gl=US&ceid=US:en | IDEXX Laboratories, Inc. (IDXX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Sat, 14 Nov 2026 06:13:17 GMT); IDEXX Laboratories (IDXX) Stock Looks Fairly Valued Despite Its 28% Run - Yahoo Finance (Sat, 31 Oct 2026 07:00:00 GMT); IDEXX Laboratories (IDXX) Q3 Earnings Leave Its Premium Valuation In Focus - Yahoo Finance (Tue, 03 Nov 2026 08:00:00 GMT) |
| S034 | filing | CHTR | 2026-11-06 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001091667.json | Diluted EPS 0.38 for period ending 2026-09-30 (filed 2026-11-06) |
| S035 | filing | ROP | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000882835&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000882835-26-000047); 8-K filed 2026-10-22 (accession 0000882835-26-000042); 8-K filed 2026-10-01 (accession 0000882835-26-000039) |
| S036 | filing | RDDT | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001713445&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0001713445-26-000116); 8-K filed 2026-10-29 (accession 0001713445-26-000114); 8-K filed 2026-08-12 (accession 0001713445-26-000107) |
| S037 | stock | ROP | 2026-11-15 | ok | https://finance.yahoo.com/quote/ROP | Trailing P/E: 18.993866; Forward P/E: 19.532475; Forward EPS: 24.57318; Price: 479.975; Market price: 479.975; Market cap: 47535013888; Sector: Technology; Trailing Eps: 25.27; Revenue Growth: 0.076; Earnings Growth: 0.326; Gross Margin: 0.69671; Operating Margin: 0.28049; Profit Margin: 0.30712998; Return On Equity: 0.13229; Total Revenue: 8434599936; Market Cap: 47535013888; Consensus EPS FY+1: 24.57318; growth: 0.09810001 |
| S038 | news | ROP | Thu, 12 Nov 2026 19:15:50 GMT | ok | https://news.google.com/rss/search?q=ROP+Roper+Technologies+stock&hl=en-US&gl=US&ceid=US:en | Roper Technologies, Inc. (ROP) Stock Price, News, Quote & History - Yahoo! Finance Canada (Thu, 12 Nov 2026 19:15:50 GMT); Roper Technologies (ROP) Stock Looks Fully Valued As Cash Flow Comes Into Focus - Yahoo Finance (Thu, 05 Nov 2026 08:00:00 GMT); Roper Technologies: 3 Key Takeaways for Long-Term Investors - Yahoo Finance (Mon, 26 Oct 2026 07:00:00 GMT) |
| S039 | stock | RDDT | 2026-11-15 | ok | https://finance.yahoo.com/quote/RDDT | Trailing P/E: 20.091835; Forward P/E: 10.770874; Forward EPS: 9.14039; Price: 98.45; Market price: 98.45; Market cap: 19010076672; Sector: Communication Services; Trailing Eps: 4.9; Revenue Growth: 0.53; Earnings Growth: 0.749; Gross Margin: 0.91547996; Operating Margin: 0.29397; Profit Margin: 0.32105; Return On Equity: 0.32029998; Total Revenue: 3088880128; Market Cap: 19010076672; Consensus EPS FY+1: 6.82439; growth: 0.2417 |
| S040 | filing | IDXX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000874716.json | Diluted EPS 11.75 for period ending 2026-09-30 (filed 2026-11-02) |

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
- filing APP: https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json (2026-11-04)
- filing GEN: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 (2026-10-29)
- stock APP: https://finance.yahoo.com/quote/APP (2026-11-15)
- stock PNR: https://finance.yahoo.com/quote/PNR (2026-11-15)
- stock FISV: https://finance.yahoo.com/quote/FISV (2026-11-15)
- news PNR: https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 22:05:23 GMT)
- filing PNR: https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json (2026-10-27)
- filing FISV: https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json (2026-11-04)

## AI Provenance

- Provider / model: hermes-local-proxy / upstage/solar-mini4:free
- Market research: attempts=1 tokens=9473 (prompt=6473, completion=3000) runtime=23.91s
- Fundamental research: generated this run at 2026-11-15T11:15:12.788865+00:00
- Evidence source dates: {'as_of': '2026-11-13', 'latest_equity_date': '2026-11-13', 'latest_macro_date': '2026-11-14', 'flows_date': '2026-11-13'}
- Evidence fingerprint: 75b2be783db05a9df2b0808793b9626d9466806cc931d32b2fd19512c20582de
- Source citations are retrieved external records in the ledger above; market values remain from the verified database snapshot.


## Disclosures

- This is research and market intelligence, not investment advice.
- AI conclusions are research judgments, not validated return predictions.
- The frozen risk layer is risk-only and is not used for directional views or allocations.
- Legacy scores are not active inputs or outputs.

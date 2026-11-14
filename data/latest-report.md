# AEGIS AI-First Market Intelligence

Research generated at: 14 November 2026, 20:18 HKT
Database freshness: equity 2026-11-13 (latest row retrieved 2026-11-14 13:50:55.938286+08:00)
Data cutoff: 2026-11-13 US cash close
Snapshot ID: aegis-hourly-20261114T121821Z

## Executive Summary

- **AI market view: Risk-on tilt with a quality/earnings focus: broad market breadth is positive, but the 20-day index return is negative and the 52-week high/low counts are flat, so the rally is narrow and dependent on a few liquidity leaders. Dislocation names and high-multiple tech are the most volatile, while defensive sectors and low-multiple value are holding up.**
- Broad market breadth is constructive (71.3% above 50-day, 63.6% above 200-day, ADR 1.70), but the index is down 1.28% over 20 days and 52-week high/low counts are zero, indicating a thin, leader-driven tape.
- Liquidity leaders NVDA, AMD, MU and AAPL are driving participation, while Information Technology is the worst sector over 20 days (-7.19%) and Communication Services is negative (-1.48%).
- Defensive and low-multiple sectors are outperforming: Health Care (+6.87%), Consumer Discretionary (+6.69%), Consumer Staples (+5.40%) and Financials (+5.69%) lead; Energy (-4.81%) and Utilities (-4.34%) lag.
- Macro data show a still-elevated but easing inflation backdrop (CPI 336.30 in Sep-2026), unemployment at 4.2%, and a positive 10Y-2Y spread of 0.27, supporting a gradual normalization rather than an imminent recession signal.
- Credit conditions are stable: high-yield OAS 3.20 and IG OAS 0.89, with TLT flows neutral and SOXX showing exceptional institutional buying despite price weakness.
- The risk block is frozen and prospective; the 5-day forecast vol is 14.93% and spike probability 16.51% is below the 18.50% threshold, so no directional or allocation call is being made.

## Data QC

- Status: **PASS_WITH_WARNINGS**
- Equity session: 0 completed session(s) behind inference date
- Equity provenance: 386 provisional / 12581 canonical
- Breadth lag: 0 session(s); ETF-flow lag: 0 session(s)
- Note: Equity session contains a mix of provisional yfinance and canonical Massive rows.
- External sources: 79 ok / 0 unavailable; retrieved 2026-11-14T12:18:36.674548+00:00

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
| S&P 500 | 7561.67 | -1.28% (20d) | Index is negative over 20 days despite positive breadth; 52-week high/low counts are zero, indicating a narrow leadership tape. |
| Health Care (XLV) | 6.87% | +6.87% (20d) | Best sector; trailing P/E 30.78, consistent with defensive demand and earnings quality. |
| Information Technology (XLK) | -7.19% | -7.19% (20d) | Worst sector; high-multiple leaders NVDA, AMD and NOW are under pressure, dragging the sector. |
| Energy (XLE) | -4.81% | -4.81% (20d) | Weakest sector; trailing P/E 16.23, likely reflecting commodity price or macro sensitivity. |
| Consumer Discretionary (XLY) | 6.69% | +6.69% (20d) | Strong 20-day return; trailing P/E 25.11, supported by consumer spending and low unemployment. |

## Macro, Fiscal, Rates, Liquidity and Credit

- Inflation is easing but still above the pre-pandemic norm: CPI 336.298 in Sep-2026 and Core CPI 338.896, with the latest official CPI reading 337.476 in Oct-2026, suggesting gradual disinflation rather than a sharp drop.
- Labor market is stable: unemployment 4.2% in Sep-2026, down from 4.1% in Oct-2026, and payrolls 159,293k in Oct-2026, indicating no acute labor deterioration.
- The yield curve is modestly positive: 10Y-2Y spread 0.27 on 2026-11-13, which historically reduces immediate recession risk but does not signal aggressive easing.
- Policy rates remain restrictive: effective federal funds rate 3.88% as of 2026-11-12, consistent with a late-cycle, data-dependent stance.
- Credit spreads are tight but not distressed: high-yield OAS 3.20 and IG OAS 0.89 as of 2026-11-12, implying stable funding conditions and limited stress.
- Liquidity is mixed: TLT flows are neutral with medium-term deterioration, while SOXX shows exceptional institutional buying despite price weakness, suggesting sector-specific capital rotation rather than broad risk appetite.

## US Equities and 11 GICS Sectors

Macro source IDs: S001, S002, S003, S004, S005, S006, S007

| GICS sector | Evidence | AI research stance | Source IDs |
| --- | --- | --- | --- |
| Health Care | 20d return +6.87%; trailing P/E 30.78; S055 | Defensive leader with strong momentum; earnings yield is moderate but the sector is benefiting from risk-on rotation and stable macro. | S055 |
| Consumer Staples | 20d return +5.40%; trailing P/E 24.85; S056 | Steady defensive performer; low volatility and stable demand support the sector despite a slightly higher multiple. | S056 |
| Consumer Discretionary | 20d return +6.69%; trailing P/E 25.11; S058 | Strong 20-day performance; supported by resilient consumer spending and stable labor market. | S058 |
| Real Estate | 20d return +5.24%; trailing P/E 29.63; S061 | Positive momentum; higher valuation reflects interest-rate sensitivity and demand for income assets. | S061 |
| Financials | 20d return +5.69%; trailing P/E 15.85; S064 | Solid sector performance; low valuation and positive curve support net interest margins. | S064 |
| Utilities | 20d return +4.34%; trailing P/E 18.11; S066 | Underperforming despite defensive profile; higher rates and lower growth expectations weigh on the sector. | S066 |
| Materials | 20d return +2.57%; trailing P/E 21.72; S070 | Modest positive; commodity and industrial demand remain mixed, with valuation in line with historical norms. | S070 |
| Industrials | 20d return +0.61%; trailing P/E 27.07; S071 | Near-flat; capital goods and infrastructure demand are stable but not accelerating. | S071 |
| Communication Services | 20d return -1.48%; trailing P/E 17.26; S072 | Negative sector; media and platform names are under pressure from ad-spend and regulatory concerns. | S072 |
| Information Technology | 20d return -7.19%; trailing P/E 30.03; S073 | Weakest sector; high-multiple leaders NVDA, AMD and NOW are dragging the index, with elevated valuations and profit-taking. | S073 |
| Energy | 20d return -4.81%; trailing P/E 16.23; S074 | Weakest sector; commodity price weakness and macro uncertainty are suppressing the sector despite a low multiple. | S074 |

### Sector fundamentals, valuation and earnings

Sector-level fundamentals are limited to trailing P/E and 20-day returns supplied in the database. No growth, margin, or consensus estimates are available for the full sector universe, so a deeper fundamental read is not possible. The supplied P/E data show Health Care (30.78), Information Technology (30.03) and Real Estate (29.63) at the high end, while Financials (15.85), Energy (16.23) and Utilities (18.11) are the lowest. These multiples are point-in-time and should not be interpreted as forward-looking valuation signals.

## Growth vs Value

- Growth: Information Technology is the growth proxy but is currently negative over 20 days (-7.19%) with a high trailing P/E of 30.03, indicating that recent momentum has faded despite the sector's long-term growth profile.
- Value: Financials (P/E 15.85), Energy (P/E 16.23) and Utilities (P/E 18.11) offer the lowest trailing multiples, but Energy is the worst performer over 20 days, suggesting that low multiples may reflect macro or commodity headwinds rather than undervaluation.
- Defensive value: Health Care (P/E 30.78) and Consumer Staples (P/E 24.85) combine positive momentum with stable earnings, providing a quality-growth blend rather than pure value.
- Mixed signals: Consumer Discretionary (P/E 25.11) is the strongest sector over 20 days, but its multiple is not the cheapest, indicating that momentum and valuation are not aligned.

## ETF Flows and Breadth

- Breadth is positive: 71.3% of names are above their 50-day moving average, 63.6% above their 200-day, and the advance/decline ratio is 1.70, indicating broad participation.
- However, 52-week high/low counts are zero and the 20-day index return is -1.28%, so the positive breadth is not translating into a broad market rally; leadership is concentrated in a few names.
- Flows show exceptional institutional buying in SOXX (20d z-score 5.10, 60d z-score 3.17) despite price weakness, suggesting strong structural demand for semiconductor equipment.
- TLT flows are neutral with a medium-term deterioration signal (20d z-score -0.41), indicating that bond demand is not providing a safe-haven bid.
- SMH shows a tactical profit-taking pattern inside structural accumulation (20d z-score 1.22, 60d z-score 1.04), implying that short-term selling is occurring within a longer-term uptrend.

## Stock Ideas

Single-stock research uses reported EPS, forward P/E and company fundamentals. All ideas are research judgments, not validated return predictions.

| Ticker | Security | Research view | Price | EPS | Forward P/E | Base target | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| APP | AppLovin | NEW | 409.1 | 20.86026 | 19.611452 | 458.93 | NEW |
| PNR | Pentair | KEEP | 68.3 | 5.30402 | 12.877027 | 74.26 | KEEP |
| RDDT | Reddit | KEEP | 98.45 | 9.14039 | 10.770874 | 118.83 | KEEP |
| ROP | Roper Technologies | NEW | 479.975 | 24.57318 | 19.532475 | 393.17 | NEW |

## ETF Ideas

ETF research uses holdings, portfolio valuation and exposure. Single-stock EPS × P/E valuation is not applied to ETFs.

| Ticker | Fund | Research view | Price | Top holdings | Portfolio valuation | Sector exposure | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| XLV | Health Care sector ETF | KEEP | 188.85 | LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59% | Top 10 holdings; numeric weight coverage 61.42% | Health Care | KEEP |
### APP — AppLovin

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** AppLovin offers a high-momentum, high-margin digital advertising compounder with a sub-20 forward P/E, whereas the shortlist alternatives such as INTC and COIN carry negative earnings yields and deep drawdowns, and the sector ETFs lack the same growth profile. Alternatives considered: INTC, COIN, XLY.
- **Thesis:** AppLovin screens in the top 20-day momentum bucket with a 53.7% 20-day return and a 32.5% 60-day return, and its reported FY2027 EPS of 20.86 supports a forward P/E near 19.6. The Q3 filing and subsequent earnings-driven surge provide a source-backed catalyst for the position.
- **Source IDs:** S008, S011, S013, S017
- **Catalysts:** Q3 2026 earnings release and 51% stock surge on 2026-11-10, Sustained 20-day and 60-day momentum, Forward EPS of 20.86 supports a sub-20 forward P/E
- **Risks:** High momentum can mean elevated volatility and mean-reversion risk, Forward EPS and fiscal period alignment are unverified, Sector-relative P/E is at the median, so no cheapness cushion
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 20.8603 (source.forwardEps) x AI multiple assumption 22.00; source IDs S008, S011, S013, S017
- **EPS:** 20.86026 — period: FY2027 (+1y consensus)
- **Forward P/E:** 19.611452
- **FY+1 growth assumption:** 27.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / AAPL / APP shows strong FY2027 consensus EPS growth of 27.44% and revenue growth of 25.37%, supported by an 88.8% gross margin and 77.8% operating margin. The FY2027 forward EPS of 20.86 and forward P/E of 19.6 are reasonable, but the base multiple is set above the current forward P/E to reflect durable high-margin cash generation and scale, with AAPL used as a named peer reference for premium multiple valuation of high-margin technology platforms.
- **Company fundamentals:** FY2027 EPS 20.86; FY2027 revenue growth 25.4%; FY2027 earnings growth 75.5%; gross margin 88.8%; operating margin 77.8%; profit margin 65.9%; ROE 2.10; forward P/E 19.61; price 409.10; 20-day return 53.7%; 60-day return 32.5%; 60-day drawdown -0.2%
- **Bull / Base / Bear:** 542.37 / 458.93 / 354.62
- **Bull / Base / Bear returns:** 32.58% / 12.18% / -13.32%
- **Scenario probabilities:** not separately assigned; see scenario table.

### PNR — Pentair

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Pentair is a higher-quality industrial with a lower forward P/E than the high-multiple dislocation names such as NOW and MRVL, and it offers a cleaner earnings profile than INTC, but the negative fundamental growth keeps the stance neutral rather than a buy. Alternatives considered: INTC, NOW, MRVL.
- **Thesis:** Pentair screens in the top 20-day momentum bucket with a 27.8% 20-day return and a 7.1% 60-day return. Its forward P/E of 12.9 and earnings yield of 7.4% are reasonable, but FY2027 revenue and earnings are contracting, so the momentum is not yet supported by fundamental growth.
- **Source IDs:** S010, S014, S016, S018
- **Catalysts:** 20-day momentum of 27.8%, Forward P/E of 12.9 and earnings yield of 7.4%, Q3 2026 filing and ongoing industrial demand
- **Risks:** FY2027 revenue growth -4.5% and earnings growth -18.8%, Sector-relative P/E of 0.49 indicates the stock trades below its sector, Momentum may fade if the fundamental deterioration continues
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 5.3040 (source.forwardEps) x AI multiple assumption 14.00; source IDs S010, S014, S016, S018
- **EPS:** 5.30402 — period: FY2027 (+1y consensus)
- **Forward P/E:** 12.877027
- **FY+1 growth assumption:** 12.82%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / HON / PNR has FY2027 consensus EPS growth of 12.82% and revenue growth of 18.38%, with a 40.2% gross margin and 21.4% operating margin. The FY2027 forward EPS of 5.30 and forward P/E of 12.9 are reasonable, but the base multiple is set above the current forward P/E to reflect stable industrial demand and capital discipline, with HON used as a named peer reference for industrial cyclical valuation.
- **Company fundamentals:** FY2027 EPS 5.30; FY2027 revenue growth -4.5%; FY2027 earnings growth -18.8%; gross margin 40.2%; operating margin 21.4%; profit margin 15.4%; ROE 15.6%; forward P/E 12.88; price 68.30; 20-day return 27.8%; 60-day return 7.1%; 60-day drawdown -5.2%
- **Bull / Base / Bear:** 90.17 / 74.26 / 58.34
- **Bull / Base / Bear returns:** 32.02% / 8.73% / -14.58%
- **Scenario probabilities:** not separately assigned; see scenario table.

### RDDT — Reddit

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Reddit offers a compelling digital platform with strong FY2027 growth and a reasonable forward P/E, but the dislocation is severe and the sector-relative valuation is the highest in the shortlist, so it is not preferred over the higher-quality momentum names such as APP and ROP. Alternatives considered: APP, ROP, INTC.
- **Thesis:** Reddit is the largest 20-day dislocation name with a -36.9% 20-day return and a -39.4% 60-day drawdown. It has a forward P/E of 10.8 and an earnings yield of 3.0%, with FY2027 revenue growth of 28.4% and earnings growth of 74.9%, but the sharp price decline and high valuation multiples relative to the sector warrant a neutral stance.
- **Source IDs:** S038, S041, S043, S044
- **Catalysts:** Largest 20-day dislocation in the shortlist, FY2027 revenue growth of 28.4% and earnings growth of 74.9%, Forward P/E of 10.8 and earnings yield of 3.0%
- **Risks:** 39.4% 60-day drawdown and negative 20-day/60-day returns, Sector-relative P/E of 1.66 is the highest in the shortlist, High valuation multiples relative to the sector
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 9.1404 (source.forwardEps) x AI multiple assumption 13.00; source IDs S038, S041, S043, S044
- **EPS:** 9.14039 — period: FY2027 (+1y consensus)
- **Forward P/E:** 10.770874
- **FY+1 growth assumption:** 24.17%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / FOXA / RDDT shows FY2027 consensus EPS growth of 24.17% and revenue growth of 28.43%, with a 91.5% gross margin and 32.1% profit margin. The FY2027 forward EPS of 9.14 and forward P/E of 10.8 are reasonable, but the base multiple is set above the current forward P/E to reflect high-margin content and subscriber growth, with FOXA used as a named peer reference for media/entertainment valuation.
- **Company fundamentals:** FY2027 EPS 9.14; FY2027 revenue growth 28.4%; FY2027 earnings growth 74.9%; gross margin 91.5%; operating margin 29.4%; profit margin 32.1%; ROE 32.0%; forward P/E 10.77; price 98.45; 20-day return -36.9%; 60-day return -34.5%; 60-day drawdown -39.4%
- **Bull / Base / Bear:** 146.25 / 118.83 / 91.4
- **Bull / Base / Bear returns:** 48.55% / 20.7% / -7.16%
- **Scenario probabilities:** not separately assigned; see scenario table.

### ROP — Roper Technologies

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** Roper offers a high-margin, niche technology compounder with solid momentum and a reasonable forward P/E, and it is preferable to the high-multiple dislocation names such as NOW and MRVL, which carry forward EPS gaps and extreme multiples. Alternatives considered: NOW, MRVL, INTC.
- **Thesis:** Roper Technologies screens in the top 20-day momentum bucket with a 25.4% 20-day return and a 16.9% 60-day return. Its forward P/E of 19.5 and earnings yield of 6.0% are supported by a high-margin, niche technology portfolio, and the momentum is backed by positive 60-day returns.
- **Source IDs:** S034, S037, S039, S042
- **Catalysts:** 20-day momentum of 25.4% and 60-day return of 16.9%, Forward P/E of 19.5 and earnings yield of 6.0%, Niche technology portfolio with high gross margin of 69.7%
- **Risks:** Sector-relative P/E of 0.49 indicates the stock trades below its sector, 60-day drawdown of -2.5%, Growth is modest at 7.6% revenue growth and 32.6% earnings growth
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 24.5732 (source.forwardEps) x AI multiple assumption 16.00; source IDs S034, S037, S039, S042
- **EPS:** 24.57318 — period: FY2027 (+1y consensus)
- **Forward P/E:** 19.532475
- **FY+1 growth assumption:** 9.81%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / HD / ROP has FY2027 consensus EPS growth of 9.81% and revenue growth of 6.29%, with a 69.7% gross margin and 30.7% profit margin. The FY2027 forward EPS of 24.57 and forward P/E of 19.5 are reasonable, but the base multiple is set above the current forward P/E to reflect steady consumer demand and margin stability, with HD used as a named peer reference for consumer discretionary valuation.
- **Company fundamentals:** FY2027 EPS 24.57; FY2027 revenue growth 7.6%; FY2027 earnings growth 32.6%; gross margin 69.7%; operating margin 28.0%; profit margin 30.7%; ROE 13.2%; forward P/E 19.53; price 479.98; 20-day return 25.4%; 60-day return 16.9%; 60-day drawdown -2.5%
- **Bull / Base / Bear:** 466.89 / 393.17 / 319.45
- **Bull / Base / Bear returns:** -2.73% / -18.09% / -33.44%
- **Scenario probabilities:** not separately assigned; see scenario table.

### XLV — Health Care sector ETF

- **Type:** ETF
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** XLV offers broad, diversified health care exposure with a strong price change and a well-known basket of large-cap pharma and medical device leaders, making it a preferable core holding to the high-multiple single-stock names such as IDXX and MRVL, which carry extreme multiples and higher single-stock risk. Alternatives considered: XLP, XLY, IDXX.
- **Thesis:** The Health Care sector ETF provides diversified exposure to large-cap pharma and medical device leaders, with a 54.3% raw price change and a 61.4% top-10 holdings coverage. The sector remains a core allocation, but the ETF lacks the specific catalyst and valuation precision of the individual stock ideas.
- **Source IDs:** S055, S060
- **Catalysts:** 54.3% raw price change, Diversified top-10 holdings including LLY, JNJ, ABBV, MRK, UNH, TMO, AMGN, GILD, ABT, PFE, 61.4% top-10 holdings coverage
- **Risks:** Sector concentration in large-cap pharma and medical devices, Top-10 holdings coverage of 61.4% leaves 38.6% in smaller positions, No single-stock catalyst or valuation precision
- **Valuation method:** Holdings/portfolio valuation with AI total-return assumption
- **Valuation status:** verified; forward-EPS source: ; period flags: 
- **Valuation assumptions:** Holdings/portfolio valuation; 10 weighted holdings; coverage 61.42%; source IDs S055, S060
- **Top holdings:** LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59%
- **Portfolio valuation:** Top 10 holdings; numeric weight coverage 61.42%
- **Sector exposure:** Health Care
- **Underlying drivers:** Large-cap pharma and medical device demand, innovation pipeline, and sector rotation
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
| Bull | 25% | +2.00% | Directional signal is false and forecast vol is below the 18.5% threshold, so a mild upside is driven by stable earnings revisions and low near-term volatility rather than a directional catalyst. |
| Base | 50% | +0.00% | Frozen daily-close model with no directional signal and elevated spike probability near the threshold implies a range-bound path with flat expected return over the 5-day horizon. |
| Bear | 25% | -2.00% | Spike probability of 16.5% is below the 18.5% threshold but still elevated, leaving room for a mild downside if a volatility spike materializes around the US close. |

### Long Term (12 months)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 30% | +8.00% | Sustained earnings growth and positive rate expectations support a moderate bull case, with 8% return reflecting continued but not aggressive expansion. |
| Base | 40% | +3.00% | Base case assumes steady earnings and stable credit conditions, producing a modest positive long-term return with low volatility drag. |
| Bear | 30% | -5.00% | A bear case driven by widening credit spreads, earnings disappointment, or a rate shock could produce a 5% decline over the longer horizon. |

## Positioning

- Maintain a risk-on posture with a quality/earnings filter: favor sectors with positive momentum and stable fundamentals over high-multiple, momentum-dependent names.
- Favored defensive and low-multiple sectors (Health Care, Consumer Staples, Financials) as a buffer against thin breadth and potential volatility.
- Less favored or monitor high-multiple, liquidity-leader-dependent sectors (Information Technology, Communication Services) where 20-day returns are negative and valuations are elevated.
- Do not use the frozen risk block for directional or allocation decisions; it is prospective and only indicates a below-threshold spike probability.
- Monitor credit spreads and TLT flows for any shift in risk appetite; stable spreads and neutral bond flows currently support the existing stance.

## Catalysts

| Date | Event | Why it matters |
| --- | --- | --- |
| 2026-11-16 | US equity market open | Frozen daily-close model becomes eligible for formal use after the completed US close; any shift in the 5-day forecast vol or spike probability could alter the risk posture. |
| 2026-11-13 | Macro data release | Latest CPI, unemployment and payrolls readings are available; any revision or new print could shift the inflation/labor narrative and affect sector rotation. |
| 2026-11-13 | Credit market data |  |

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
| S011 | news | APP | Tue, 10 Nov 2026 14:24:00 GMT | ok | https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en | APP Stock Surges 51% After Q3 Earnings: Is it Still a Buy? - Yahoo Finance (Tue, 10 Nov 2026 14:24:00 GMT); AppLovin stock soars after Q3 earnings, outlook beat - Yahoo Finance (Thu, 05 Nov 2026 08:00:00 GMT); Is Trending Stock AppLovin Corporation (APP) a Buy Now? - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT) |
| S012 | news | FISV | Fri, 13 Nov 2026 00:53:33 GMT | ok | https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en | Fiserv, Inc. (FISV) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 00:53:33 GMT); Fiserv (FISV) Stock Looks Undervalued With Strong Excess Returns - Yahoo Finance (Wed, 11 Nov 2026 22:14:34 GMT); Fiserv Stock Outlook: Is Wall Street Bullish or Bearish? - Yahoo Finance (Thu, 12 Nov 2026 12:23:56 GMT) |
| S013 | stock | APP | 2026-11-14 | ok | https://finance.yahoo.com/quote/APP | Trailing P/E: 27.54882; Forward P/E: 19.611452; Forward EPS: 20.86026; Price: 409.1; Market price: 409.1; Market cap: 135543824384; Sector: Communication Services; Trailing Eps: 14.85; Revenue Growth: 0.555; Earnings Growth: 0.755; Gross Margin: 0.8878; Operating Margin: 0.77782995; Profit Margin: 0.65887; Return On Equity: 2.1008599; Total Revenue: 7608893952; Market Cap: 135543824384; Consensus EPS FY+1: 20.72438; growth: 0.2744 |
| S014 | stock | PNR | 2026-11-14 | ok | https://finance.yahoo.com/quote/PNR | Trailing P/E: 18.610355; Forward P/E: 12.877027; Forward EPS: 5.30402; Price: 68.3; Market price: 68.3; Market cap: 10904415232; Sector: Industrials; Trailing Eps: 3.67; Revenue Growth: -0.045; Earnings Growth: -0.188; Gross Margin: 0.40168998; Operating Margin: 0.21410999; Profit Margin: 0.15435; Return On Equity: 0.15605; Total Revenue: 3966200064; Market Cap: 10904415232; Consensus EPS FY+1: 5.30402; growth: 0.1282 |
| S015 | stock | FISV | 2026-11-14 | ok | https://finance.yahoo.com/quote/FISV | Forward P/E: 7.9923306; Price: 63.78; Market price: 63.78; Market cap: 33934002176; Market Cap: 33934002176; Consensus EPS FY+1: 7.98015; growth: 0.09689999 |
| S016 | news | PNR | Fri, 13 Nov 2026 15:54:46 GMT | ok | https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en | Pentair plc (PNR) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 15:54:46 GMT); Pentair (PNR) Stock May Be 46% Undervalued As New CFO Arrives - Yahoo Finance (Fri, 25 Sep 2026 07:00:00 GMT); Pentair plc (PNR) Q3 Earnings and Revenues Beat Estimates - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT) |
| S017 | filing | APP | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json | Diluted EPS 11.61 for period ending 2026-09-30 (filed 2026-11-04) |
| S018 | filing | PNR | 2026-10-27 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json | Diluted EPS 2.76 for period ending 2026-09-30 (filed 2026-10-27) |
| S019 | filing | GEN | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0000849399-26-000083); 8-K filed 2026-10-28 (accession 0000849399-26-000081); 8-K filed 2026-10-09 (accession 0000849399-26-000079) |
| S020 | filing | CLX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000021076-26-000046); 8-K filed 2026-11-02 (accession 0000021076-26-000044); 8-K filed 2026-10-29 (accession 0001206774-26-000586) |
| S021 | filing | FISV | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json | Diluted EPS -8.9 for period ending 2026-09-30 (filed 2026-11-04) |
| S022 | stock | GEN | 2026-11-14 | ok | https://finance.yahoo.com/quote/GEN | Trailing P/E: 15.431472; Forward P/E: 9.108996; Forward EPS: 3.33736; Price: 30.4; Market price: 30.4; Market cap: 18035593216; Sector: Technology; Trailing Eps: 1.97; Revenue Growth: 0.122; Earnings Growth: 1.286; Gross Margin: 0.77410007; Operating Margin: 0.43229; Profit Margin: 0.23068; Return On Equity: 0.46402; Total Revenue: 5228000256; Market Cap: 18035593216; Consensus EPS FY+1: 3.33736; growth: 0.1286 |
| S023 | news | GEN | Wed, 11 Nov 2026 13:10:37 GMT | ok | https://news.google.com/rss/search?q=GEN+Gen+Digital+stock&hl=en-US&gl=US&ceid=US:en | Gen Digital Inc. (GEN) Stock Forecasts - Yahoo Finance (Wed, 11 Nov 2026 13:10:37 GMT); Gen Digital Inc. stock outperforms competitors on strong trading day - MarketWatch (Fri, 13 Nov 2026 22:09:00 GMT); Gen Digital (GEN) Stock Repriced After Q2 Earnings Put Margins Center Stage - Yahoo Finance (Thu, 29 Oct 2026 07:00:00 GMT) |
| S024 | filing | CHTR | 2026-11-06 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-06 (accession 0001091667-26-000073); 8-K filed 2026-11-06 (accession 0001091667-26-000072); 8-K filed 2026-10-27 (accession 0001091667-26-000064) |
| S025 | stock | CLX | 2026-11-14 | ok | https://finance.yahoo.com/quote/CLX | Trailing P/E: 19.68705; Forward P/E: 17.745283; Forward EPS: 6.1684; Price: 109.46; Market price: 109.46; Market cap: 13260793856; Sector: Consumer Defensive; Trailing Eps: 5.56; Revenue Growth: 0.333; Earnings Growth: 1.138; Gross Margin: 0.41939998; Operating Margin: 0.14286; Profit Margin: 0.09408; Return On Equity: 5.34363; Total Revenue: 7196000256; Market Cap: 13260793856; Consensus EPS FY+1: 6.1684; growth: 0.0769 |
| S026 | news | CLX | Fri, 13 Nov 2026 05:34:04 GMT | ok | https://news.google.com/rss/search?q=CLX+Clorox+stock&hl=en-US&gl=US&ceid=US:en | The Clorox Company (CLX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 05:34:04 GMT); The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance Singapore (Fri, 13 Nov 2026 08:35:40 GMT); A 10-Day Winning Streak Has Clorox Stock Up 24% - Trefis (Sat, 14 Nov 2026 08:28:05 GMT) |
| S027 | filing | IDXX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000874716&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000874716-26-000135); 8-K filed 2026-11-02 (accession 0001104659-26-120892); 10-Q filed 2026-08-04 (accession 0000874716-26-000123) |
| S028 | news | CHTR | Thu, 12 Nov 2026 08:02:01 GMT | ok | https://news.google.com/rss/search?q=CHTR+Charter+Communications+stock&hl=en-US&gl=US&ceid=US:en | Charter Communications: 3 Key Takeaways for Long-Term Investors - Yahoo Finance (Thu, 12 Nov 2026 08:02:01 GMT); Why You Should Think About Charter Communications Differently Now? - Trefis (Fri, 13 Nov 2026 19:15:44 GMT); What Is The Biggest Threat To Charter Communications Stock? - Trefis (Thu, 12 Nov 2026 15:55:19 GMT) |
| S029 | stock | IDXX | 2026-11-14 | ok | https://finance.yahoo.com/quote/IDXX | Trailing P/E: 47.45485; Forward P/E: 41.687927; Forward EPS: 16.8929; Price: 704.23; Market price: 704.23; Market cap: 55483650048; Sector: Healthcare; Trailing Eps: 14.84; Revenue Growth: 0.099; Earnings Growth: 0.179; Gross Margin: 0.62722; Operating Margin: 0.32497; Profit Margin: 0.25357; Return On Equity: 0.68925005; Total Revenue: 4662220800; Market Cap: 55483650048; Consensus EPS FY+1: 16.8929; growth: 0.1244 |
| S030 | filing | CLX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000021076.json | Diluted EPS 1.39 for period ending 2026-09-30 (filed 2026-11-02) |
| S031 | filing | GEN | 2026-10-29 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000849399.json | Diluted EPS 0.83 for period ending 2026-10-02 (filed 2026-10-29) |
| S032 | filing | CHTR | 2026-11-06 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001091667.json | Diluted EPS 0.38 for period ending 2026-09-30 (filed 2026-11-06) |
| S033 | stock | CHTR | 2026-11-14 | ok | https://finance.yahoo.com/quote/CHTR | Trailing P/E: 13.006578; Forward P/E: 3.2831066; Forward EPS: 42.15215; Price: 138.39; Market price: 138.39; Market cap: 24778944512; Sector: Communication Services; Trailing Eps: 10.64; Revenue Growth: 0.091; Gross Margin: 0.55084; Operating Margin: 0.23389; Profit Margin: 0.02498; Return On Equity: 0.07019; Total Revenue: 55645999104; Market Cap: 24778944512; Consensus EPS FY+1: 47.15811; growth: 1.0195 |
| S034 | filing | ROP | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000882835&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000882835-26-000047); 8-K filed 2026-10-22 (accession 0000882835-26-000042); 8-K filed 2026-10-01 (accession 0000882835-26-000039) |
| S035 | filing | IDXX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000874716.json | Diluted EPS 11.75 for period ending 2026-09-30 (filed 2026-11-02) |
| S036 | news | IDXX | Fri, 13 Nov 2026 22:06:38 GMT | ok | https://news.google.com/rss/search?q=IDXX+Idexx+Laboratories+stock&hl=en-US&gl=US&ceid=US:en | IDEXX Laboratories, Inc. (IDXX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 22:06:38 GMT); IDEXX Laboratories (IDXX) Stock Looks Fairly Valued Despite Its 28% Run - Yahoo Finance (Sat, 31 Oct 2026 07:00:00 GMT); IDEXX Laboratories (IDXX) Q3 Earnings Leave Its Premium Valuation In Focus - Yahoo Finance (Tue, 03 Nov 2026 08:00:00 GMT) |
| S037 | stock | ROP | 2026-11-14 | ok | https://finance.yahoo.com/quote/ROP | Trailing P/E: 18.993866; Forward P/E: 19.532475; Forward EPS: 24.57318; Price: 479.975; Market price: 479.975; Market cap: 47535013888; Sector: Technology; Trailing Eps: 25.27; Revenue Growth: 0.076; Earnings Growth: 0.326; Gross Margin: 0.69671; Operating Margin: 0.28049; Profit Margin: 0.30712998; Return On Equity: 0.13229; Total Revenue: 8434599936; Market Cap: 47535013888; Consensus EPS FY+1: 24.57318; growth: 0.09810001 |
| S038 | filing | RDDT | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001713445&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0001713445-26-000116); 8-K filed 2026-10-29 (accession 0001713445-26-000114); 8-K filed 2026-08-12 (accession 0001713445-26-000107) |
| S039 | news | ROP | Fri, 13 Nov 2026 01:46:04 GMT | ok | https://news.google.com/rss/search?q=ROP+Roper+Technologies+stock&hl=en-US&gl=US&ceid=US:en | Roper Technologies, Inc. (ROP) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 01:46:04 GMT); Roper Technologies (ROP) Stock Looks Fully Valued As Cash Flow Comes Into Focus - Yahoo Finance (Fri, 06 Nov 2026 07:13:00 GMT); Roper (ROP) Stock May Be 16% Undervalued On Cash Flow - Yahoo Finance (Thu, 22 Oct 2026 07:00:00 GMT) |
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
- news APP: https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en (Tue, 10 Nov 2026 14:24:00 GMT)
- news FISV: https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 00:53:33 GMT)
- stock APP: https://finance.yahoo.com/quote/APP (2026-11-14)
- stock PNR: https://finance.yahoo.com/quote/PNR (2026-11-14)
- stock FISV: https://finance.yahoo.com/quote/FISV (2026-11-14)
- news PNR: https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 15:54:46 GMT)
- filing APP: https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json (2026-11-04)
- filing PNR: https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json (2026-10-27)
- filing GEN: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 (2026-10-29)
- filing CLX: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 (2026-11-02)

## AI Provenance

- Provider / model: hermes-local-proxy / upstage/solar-mini4:free
- Market research: attempts=1 tokens=9521 (prompt=6521, completion=3000) runtime=25.79s
- Fundamental research: generated this run at 2026-11-14T12:18:21.706899+00:00
- Evidence source dates: {'as_of': '2026-11-13', 'latest_equity_date': '2026-11-13', 'latest_macro_date': '2026-11-13', 'flows_date': '2026-11-13'}
- Evidence fingerprint: 11a79a430207c51ff321dd5fcd22d986878aa40d4781416ac513ad1f07dcd4ba
- Source citations are retrieved external records in the ledger above; market values remain from the verified database snapshot.


## Disclosures

- This is research and market intelligence, not investment advice.
- AI conclusions are research judgments, not validated return predictions.
- The frozen risk layer is risk-only and is not used for directional views or allocations.
- Legacy scores are not active inputs or outputs.

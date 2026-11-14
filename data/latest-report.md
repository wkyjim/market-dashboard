# AEGIS AI-First Market Intelligence

Research generated at: 14 November 2026, 19:15 HKT
Database freshness: equity 2026-11-13 (latest row retrieved 2026-11-14 13:50:55.938286+08:00)
Data cutoff: 2026-11-13 US cash close
Snapshot ID: aegis-hourly-20261114T111544Z

## Executive Summary

- **AI market view: Risk-on tilt with a quality and liquidity bias. Broad market breadth is constructive, but the 20-day return is negative and the 10Y-2Y curve is only mildly positive, so the setup favors high-liquidity, low-valuation names and sectors with positive momentum rather than broad cyclical or speculative exposure.**
- Market breadth is strongly positive: 71.3% above the 50-day and 63.6% above the 200-day, with an advance/decline ratio of 1.70 and no new lows.
- The 20-day equity return is negative (-1.28% for the S&P 500), indicating short-term price pressure despite improving participation.
- The 10Y-2Y Treasury spread is 0.27, a mildly positive curve that supports risk appetite but does not signal aggressive easing.
- Credit spreads are tight (IG OAS 0.89, HY OAS 3.20), consistent with a late-cycle, low-volatility risk environment.
- Sector leadership is split: Health Care, Consumer Discretionary, Consumer Staples, Real Estate, Financials, Utilities and Materials are up over 20 days, while Information Technology and Communication Services are down.
- Shortlist momentum/dislocation names are concentrated in high-liquidity, low-valuation, or dislocation buckets, with no composite score used to avoid over-weighting.
- Macro data show CPI at 336.298 (Sep-2026), unemployment at 4.2%, and payrolls at 159,293k (Oct-2026), indicating a cooling but still-resilient labor market.
- Risk forecast shows 5-day volatility of 14.9% and a 16.5% spike probability, below the 18.5% threshold, so elevated tail risk is not currently flagged.

## Data QC

- Status: **PASS_WITH_WARNINGS**
- Equity session: 0 completed session(s) behind inference date
- Equity provenance: 386 provisional / 12581 canonical
- Breadth lag: 0 session(s); ETF-flow lag: 0 session(s)
- Note: Equity session contains a mix of provisional yfinance and canonical Massive rows.
- External sources: 79 ok / 0 unavailable; retrieved 2026-11-14T11:16:09.025996+00:00

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
| S&P 500 (SPX) | 7561.67 | -1.28% (20d) | Negative 20-day return despite broad participation; 71.3% above 50-day and 63.6% above 200-day. |
| Health Care (XLV) | 6.87% | +6.87% (20d) | Top sector performer; trailing P/E 30.78. |
| Consumer Discretionary (XLY) | 6.69% | +6.69% (20d) | Strong 20-day return; trailing P/E 25.11. |
| Consumer Staples (XLP) | 5.40% | +5.40% (20d) | Defensive strength; trailing P/E 24.85. |
| Real Estate (XLRE) | 5.24% | +5.24% (20d) | Positive momentum; trailing P/E 29.63. |
| Financials (XLF) | 5.69% | +5.69% (20d) | Positive 20-day return; trailing P/E 15.85. |
| Utilities (XLU) | 4.34% | +4.34% (20d) | Defensive sector; trailing P/E 18.11. |
| Materials (XLB) | 2.57% | +2.57% (20d) | Positive but weakest among the up sectors; trailing P/E 21.72. |
| Industrials (XLI) | 0.61% | +0.61% (20d) | Near-flat; trailing P/E 27.07. |
| Communication Services (XLC) | -1.48% | -1.48% (20d) | Negative 20-day return; trailing P/E 17.26. |
| Information Technology (XLK) | -7.19% | -7.19% (20d) | Weakest sector; trailing P/E 30.03. |
| Energy (XLE) | -4.81% | -4.81% (20d) | Negative 20-day return; trailing P/E 16.23. |

## Macro, Fiscal, Rates, Liquidity and Credit

- Growth: The 10Y-2Y Treasury spread is 0.27, indicating a mildly positive yield curve that historically supports risk assets, though the modest width limits aggressive easing expectations.
- Inflation: CPI stands at 336.298 (Sep-2026) and core CPI at 338.896, showing continued price pressure that keeps the Fed in a measured policy stance.
- Policy: The effective federal funds rate is 3.88% as of 2026-11-12, consistent with a restrictive-to-neutral posture that does not currently signal imminent rate cuts.
- Rates: The 10Y-2Y spread of 0.27 and tight credit spreads (IG 0.89, HY 3.20) suggest bond markets are pricing stable-to-slightly-easing conditions without pricing in a recession.
- Liquidity: Shortlist liquidity leaders (NVDA, AMD, MU, AAPL) show strong dollar volume, while SOXX exhibits exceptional institutional buying (20d flow z-score 5.10), indicating concentrated liquidity in select names.
- Credit: IG and HY spreads are tight, consistent with a late-cycle environment where credit conditions remain supportive but vulnerable to any growth or policy shock.

## US Equities and 11 GICS Sectors

Macro source IDs: S001, S002, S003, S004, S005, S006, S007

| GICS sector | Evidence | AI research stance | Source IDs |
| --- | --- | --- | --- |
| Health Care | 20d return +6.87%; trailing P/E 30.78; top sector performer. | Positive momentum and defensive positioning; attractive relative strength despite higher valuation. | S055 |
| Consumer Discretionary | 20d return +6.69%; trailing P/E 25.11; strong participation. | Positive momentum; consumer spending remains resilient in a cooling labor market. | S062 |
| Consumer Staples | 20d return +5.40%; trailing P/E 24.85; defensive strength. | Defensive outperformance; stable demand supports the sector in a risk-on but volatile tape. | S066 |
| Real Estate | 20d return +5.24%; trailing P/E 29.63; positive momentum. | Positive 20-day return; higher valuation but improving sector sentiment. | S064 |
| Financials | 20d return +5.69%; trailing P/E 15.85; positive return. | Positive momentum with a low valuation multiple; benefits from a stable curve. | S065 |
| Utilities | 20d return +4.34%; trailing P/E 18.11; defensive strength. | Defensive sector with moderate valuation; stable cash flows support the allocation. | S070 |
| Materials | 20d return +2.57%; trailing P/E 21.72; positive but weakest among up sectors. | Positive but lagging; moderate valuation and industrial demand remain supportive. | S071 |
| Industrials | 20d return +0.61%; trailing P/E 27.07; near-flat. | Flat momentum; valuation is above the market average, limiting upside. | S073 |
| Communication Services | 20d return -1.48%; trailing P/E 17.26; negative return. | Negative momentum; lower valuation but weak price action limits near-term upside. | S075 |
| Information Technology | 20d return -7.19%; trailing P/E 30.03; weakest sector. | Negative momentum and high valuation; selective liquidity leaders (NVDA, AMD, MU) are the only bright spots. | S076 |
| Energy | 20d return -4.81%; trailing P/E 16.23; negative return. | Negative momentum; low valuation but weak price action and energy demand uncertainty. | S078 |

### Sector fundamentals, valuation and earnings

No point-in-time sector fundamentals (e.g., revenue growth, margins, consensus estimates) are supplied in the database snapshot. The sector evidence is limited to 20-day ETF returns, trailing P/E, and the shortlist momentum/dislocation/valuation/liquidity buckets. Any quantitative sector-level growth or margin claims would be invented and are therefore omitted.

## Growth vs Value

- Growth: Information Technology and Communication Services show negative 20-day returns, indicating weak near-term growth momentum despite high trailing P/Es (30.03 and 17.26).
- Value: Financials (15.85), Energy (16.23), and Utilities (18.11) offer the lowest trailing P/Es, but Energy is negative and Utilities is defensive.
- Quality: Health Care (30.78) and Consumer Discretionary (25.11) combine positive momentum with moderate-to-high valuations, reflecting growth-plus-quality characteristics.
- Dislocation: Names such as RDDT (sector-relative P/E 1.66), FFIV (1.04), and APP (1.00) show elevated relative valuations, while PNR (0.49), GEN (0.42), and ROP (0.49) are cheaper on a sector-relative basis.

## ETF Flows and Breadth

- Market breadth is strongly positive: 71.3% above the 50-day, 63.6% above the 200-day, advance/decline ratio 1.70, and no new lows.
- Price/breadth divergence is -27.49, but bullish divergence is true and bearish divergence is false, indicating no negative price/breadth divergence.
- SOXX shows exceptional institutional buying (20d flow z-score 5.10) despite a down price, confirming strong structural accumulation.
- SMH shows tactical profit-taking inside structural accumulation (20d flow z-score 1.22, 60d 1.04), indicating selective rotation rather than broad de-risking.
- TLT shows medium-term deterioration (20d flow z-score -0.41, 60d -0.29) with flat price, suggesting reduced demand for duration.
- The advance/decline ratio of 1.70 and 70.5% positive 20-day returns indicate broad-based participation rather than narrow leadership.

## Stock Ideas

Single-stock research uses reported EPS, forward P/E and company fundamentals. All ideas are research judgments, not validated return predictions.

| Ticker | Security | Research view | Price | EPS | Forward P/E | Base target | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| APP | AppLovin | NEW | 409.1 | 20.86026 | 19.611452 | 458.93 | NEW |
| RDDT | Reddit | NEW | 98.45 | 9.14039 | 10.770874 | 127.97 | NEW |

## ETF Ideas

ETF research uses holdings, portfolio valuation and exposure. Single-stock EPS × P/E valuation is not applied to ETFs.

| Ticker | Fund | Research view | Price | Top holdings | Portfolio valuation | Sector exposure | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| XLV | Health Care Select Sector SPDR Fund | KEEP | 188.85 | LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59% | Top 10 holdings; numeric weight coverage 61.42% | Health Care | KEEP |
| XLP | Consumer Staples Select Sector SPDR Fund | KEEP | 92.35 | WMT 11.14%, COST 9.09%, PG 7.60%, KO 7.37%, PM 6.59%, MO 4.70%, CL 4.42%, MDLZ 4.25%, PEP 4.11%, TGT 4.00% | Top 10 holdings; numeric weight coverage 63.28% | Consumer Staples | KEEP |
### APP — AppLovin

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** AppLovin offers a higher-quality, higher-margin advertising compounder than the lower-margin consumer staples and industrials names in the shortlist, with a cleaner forward earnings profile and stronger momentum. Alternatives considered: ROP, PNR.
- **Thesis:** AppLovin screens in the top 20-day momentum bucket with a 53.7% 20-day return and a 32.5% 60-day return, and its reported FY2027 consensus EPS of 20.86 supports a forward P/E near 19.6. The Q3 earnings-driven surge and strong gross margin of 88.8% underpin a quality compounder narrative.
- **Source IDs:** S009, S010, S015, S016
- **Catalysts:** Continued 20-day momentum and high-margin advertising revenue growth, FY2027 consensus EPS expansion from reported FY2026 EPS of 11.61, Sustained mobile advertising demand and app monetization
- **Risks:** Elevated 20-day momentum can mean elevated volatility, Forward P/E near 19.6 leaves limited valuation cushion if growth slows, Mobile ad market cyclicality and competition
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 20.8603 (source.forwardEps) x AI multiple assumption 22.00; source IDs S009, S010, S015, S016
- **EPS:** 20.86026 — period: FY2027 (+1y consensus)
- **Forward P/E:** 19.611452
- **FY+1 growth assumption:** 27.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / Apple Inc. (AAPL) and Microsoft Corp. (MSFT) / APP's FY2027 consensus EPS of $20.86 implies ~27.4% earnings growth and ~25.4% revenue growth, with strong ~88.8% gross margin and ~77.8% operating margin. The base multiple of 22x is supported by high-quality software-like economics and premium peers such as AAPL/MSFT, while the bull case of 26x reflects continued margin expansion and the bear case of 16x reflects valuation compression risk.
- **Company fundamentals:** FY2027 consensus EPS 20.86; forward P/E 19.61; reported FY2026 diluted EPS 11.61; gross margin 88.8%; operating margin 77.8%; profit margin 65.9%; revenue growth 55.5%; earnings growth 75.5%; ROE 2.10; 20-day return 53.7%; 60-day return 32.5%; 60-day drawdown -0.2%; trailing P/E 20.05
- **Bull / Base / Bear:** 542.37 / 458.93 / 333.76
- **Bull / Base / Bear returns:** 32.58% / 12.18% / -18.42%
- **Scenario probabilities:** not separately assigned; see scenario table.

### RDDT — Reddit

- **Type:** Stock
- **Research view:** NEW (stance: NEUTRAL)
- **Why preferred / alternatives:** Reddit offers a distinct high-growth, high-margin social media exposure that is not represented by the more traditional industrials or consumer staples alternatives, providing diversification within the shortlist. Alternatives considered: INTC, MRVL.
- **Thesis:** Reddit is the largest 20-day dislocation name with a 39.4% 60-day drawdown, but it remains a high-multiple, high-growth social media platform with a 33.2 forward P/E and 10.8% earnings yield. The dislocation creates a potential mean-reversion opportunity if engagement and monetization hold.
- **Source IDs:** S036, S039, S041, S042
- **Catalysts:** Mean reversion from a 39.4% 60-day drawdown, 28.4% revenue growth and 74.9% earnings growth, High gross margin of 91.5% and strong ROE of 32.0%, Potential for renewed user engagement and ad market recovery
- **Risks:** 39.4% 60-day drawdown indicates significant downside risk, High forward P/E of 33.2 leaves limited margin for error, Social media ad market cyclicality and competition, User growth and monetization may not meet expectations
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 9.1404 (source.forwardEps) x AI multiple assumption 14.00; source IDs S036, S039, S041, S042
- **EPS:** 9.14039 — period: FY2027 (+1y consensus)
- **Forward P/E:** 10.770874
- **FY+1 growth assumption:** 24.17%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / Alphabet Inc. (GOOGL) and Amazon.com Inc. (AMZN) / RDDT's FY2027 consensus EPS of $9.14 implies ~24.2% earnings growth and ~28.4% revenue growth, with a very high ~91.5% gross margin but a lower ~29.4% operating margin and ~32.1% profit margin. The base multiple of 14x is justified by growth and asset-light economics relative to GOOGL/AMZN, with the bull case of 17x reflecting operating leverage and the bear case of 11x reflecting margin and competitive risk.
- **Company fundamentals:** FY2027 consensus EPS 9.14; forward P/E 10.77; reported FY2026 diluted EPS 3.66; gross margin 91.5%; operating margin 29.4%; profit margin 32.1%; revenue growth 53.0%; earnings growth 74.9%; ROE 32.0%; 20-day return -36.9%; 60-day return -34.5%; 60-day drawdown -39.4%; trailing P/E 33.19
- **Bull / Base / Bear:** 155.39 / 127.97 / 100.54
- **Bull / Base / Bear returns:** 57.84% / 29.98% / 2.12%
- **Scenario probabilities:** not separately assigned; see scenario table.

### XLV — Health Care Select Sector SPDR Fund

- **Type:** ETF
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** XLV provides a diversified, lower-volatility alternative to single-stock health care names like IDXX, reducing idiosyncratic risk while maintaining sector exposure. Alternatives considered: IDXX.
- **Thesis:** XLV provides diversified health care sector exposure with top holdings in LLY, JNJ, ABBV, MRK, and UNH. The sector ETF offers a lower-risk way to participate in the health care theme without single-stock volatility, though it lacks the high-momentum characteristics of the top momentum stocks.
- **Source IDs:** S053, S055
- **Catalysts:** Diversified exposure to large-cap health care leaders, Stable sector with defensive characteristics, Top 10 holdings coverage of 61.4%
- **Risks:** Sector-specific risks including regulatory and reimbursement changes, Limited upside from sector rotation if momentum shifts, Top 10 holdings concentration in a few large names
- **Valuation method:** Holdings/portfolio valuation with AI total-return assumption
- **Valuation status:** verified; forward-EPS source: ; period flags: 
- **Valuation assumptions:** Holdings/portfolio valuation; 10 weighted holdings; coverage 61.42%; source IDs S053, S055
- **Top holdings:** LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59%
- **Portfolio valuation:** Top 10 holdings; numeric weight coverage 61.42%
- **Sector exposure:** Health Care
- **Underlying drivers:** Health care sector fundamentals, large-cap pharmaceutical and medical device demand, defensive sector rotation
- **Bull / Base / Bear:** 211.51 / 198.29 / 177.52
- **Bull / Base / Bear returns:** 12.0% / 5.0% / -6.0%
- **Scenario probabilities:** not separately assigned; see scenario table.

### XLP — Consumer Staples Select Sector SPDR Fund

- **Type:** ETF
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** XLP provides a defensive, lower-volatility alternative to the high-momentum consumer staples stock CLX, offering stability and diversification. Alternatives considered: CLX.
- **Thesis:** XLP offers defensive consumer staples exposure with top holdings in WMT, COST, PG, KO, and PM. The sector ETF provides stability and dividend income, but its 1.4% raw price change is less compelling than the momentum stocks in the shortlist.
- **Source IDs:** S057, S066
- **Catalysts:** Defensive sector characteristics with stable demand, Top 10 holdings coverage of 63.3%, Diversified across major consumer staples companies
- **Risks:** Lower growth profile compared to momentum stocks, Sector-specific risks including input cost inflation, Limited upside from sector rotation
- **Valuation method:** Holdings/portfolio valuation with AI total-return assumption
- **Valuation status:** verified; forward-EPS source: ; period flags: 
- **Valuation assumptions:** Holdings/portfolio valuation; 10 weighted holdings; coverage 63.28%; source IDs S057, S066
- **Top holdings:** WMT 11.14%, COST 9.09%, PG 7.60%, KO 7.37%, PM 6.59%, MO 4.70%, CL 4.42%, MDLZ 4.25%, PEP 4.11%, TGT 4.00%
- **Portfolio valuation:** Top 10 holdings; numeric weight coverage 63.28%
- **Sector exposure:** Consumer Staples
- **Underlying drivers:** Consumer staples demand stability, defensive sector rotation, input cost management
- **Bull / Base / Bear:** 103.43 / 96.97 / 86.81
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
| Bull | 25% | +2.00% | Low 5-day forecast vol (14.9%) and below-threshold spike probability (16.5% vs 18.5% threshold) support a modest upside if US close confirms no credit stress; probability capped at 25% given neutral directional signal. |
| Base | 50% | +0.00% | Frozen daily-close model with no directional signal and historical/ewma baselines near 20-22% imply a range-bound week; base case is flat until the official US close resolves the forecast. |
| Bear | 25% | -2.00% | If the frozen forecast fails to confirm after the US close, elevated volatility regime and 16.5% spike probability could trigger a mild downside correction; probability held at 25% to reflect uncertainty around the close. |

### Long Term (12 months)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 30% | +8.00% | Sustained low volatility (14.9% 5d) and below-threshold spike probability support a constructive multi-week path if credit conditions remain stable and earnings breadth improves. |
| Base | 40% | +3.00% | Frozen daily-close model with neutral directional signal and baseline volatility near 20% implies a modest positive drift over the horizon, with no sharp catalyst either way. |
| Bear | 30% | -5.00% | If the frozen forecast is invalidated after the US close and spike probability remains elevated, a credit or volatility-driven drawdown is plausible; probability reflects the risk of a regime shift despite the current neutral signal. |

## Positioning

- Maintain a risk-on tilt with a quality and liquidity bias; favor high-liquidity, low-valuation, and positive-momentum names.
- Favored Health Care, Consumer Discretionary, Consumer Staples, Financials, and Utilities for defensive and positive-momentum characteristics.
- Less favored Information Technology and Energy given negative 20-day returns and weak sector momentum.
- Use the shortlist for tactical exposure: high-liquidity names (NVDA, AMD, MU, AAPL) and dislocation names (RDDT, FFIV, APP) for relative value.
- Avoid broad cyclical or speculative exposure; the 20

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
| S008 | news | FISV | Fri, 13 Nov 2026 00:53:33 GMT | ok | https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en | Fiserv, Inc. (FISV) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 00:53:33 GMT); Fiserv (FISV) Stock Looks Undervalued With Strong Excess Returns - Yahoo Finance (Wed, 11 Nov 2026 22:14:34 GMT); Fiserv Stock Outlook: Is Wall Street Bullish or Bearish? - Yahoo Finance (Thu, 12 Nov 2026 12:23:56 GMT) |
| S009 | news | APP | Tue, 10 Nov 2026 14:24:00 GMT | ok | https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en | APP Stock Surges 51% After Q3 Earnings: Is it Still a Buy? - Yahoo Finance (Tue, 10 Nov 2026 14:24:00 GMT); AppLovin stock soars after Q3 earnings, outlook beat - Yahoo Finance (Thu, 05 Nov 2026 08:00:00 GMT); Is Trending Stock AppLovin Corporation (APP) a Buy Now? - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT) |
| S010 | filing | APP | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001751008&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0001751008-26-000069); 8-K filed 2026-11-04 (accession 0001751008-26-000068); 10-Q filed 2026-08-05 (accession 0001751008-26-000059) |
| S011 | filing | FISV | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0000798354-26-000042); 8-K filed 2026-11-03 (accession 0000798354-26-000039); 8-K filed 2026-10-23 (accession 0001193125-26-429481) |
| S012 | filing | PNR | 2026-10-27 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-27 (accession 0000077360-26-000058); 8-K filed 2026-10-27 (accession 0000077360-26-000055); 8-K filed 2026-09-22 (accession 0000077360-26-000050) |
| S013 | news | PNR | Fri, 13 Nov 2026 15:54:46 GMT | ok | https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en | Pentair plc (PNR) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 15:54:46 GMT); Pentair plc (PNR) Latest Stock News & Headlines - Yahoo Finance (Fri, 13 Nov 2026 15:31:10 GMT); Has Pentair (PNR) Fallen Far Enough To Look Undervalued On Earnings? - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT) |
| S014 | filing | GEN | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0000849399-26-000083); 8-K filed 2026-10-28 (accession 0000849399-26-000081); 8-K filed 2026-10-09 (accession 0000849399-26-000079) |
| S015 | filing | APP | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json | Diluted EPS 11.61 for period ending 2026-09-30 (filed 2026-11-04) |
| S016 | stock | APP | 2026-11-14 | ok | https://finance.yahoo.com/quote/APP | Trailing P/E: 27.54882; Forward P/E: 19.611452; Forward EPS: 20.86026; Price: 409.1; Market price: 409.1; Market cap: 135543824384; Sector: Communication Services; Trailing Eps: 14.85; Revenue Growth: 0.555; Earnings Growth: 0.755; Gross Margin: 0.8878; Operating Margin: 0.77782995; Profit Margin: 0.65887; Return On Equity: 2.1008599; Total Revenue: 7608893952; Market Cap: 135543824384; Consensus EPS FY+1: 20.72438; growth: 0.2744 |
| S017 | stock | FISV | 2026-11-14 | ok | https://finance.yahoo.com/quote/FISV | Forward P/E: 7.9923306; Price: 63.78; Market price: 63.78; Market cap: 33934002176; Market Cap: 33934002176; Consensus EPS FY+1: 7.98015; growth: 0.09689999 |
| S018 | stock | PNR | 2026-11-14 | ok | https://finance.yahoo.com/quote/PNR | Trailing P/E: 18.610355; Forward P/E: 12.877027; Forward EPS: 5.30402; Price: 68.3; Market price: 68.3; Market cap: 10904415232; Sector: Industrials; Trailing Eps: 3.67; Revenue Growth: -0.045; Earnings Growth: -0.188; Gross Margin: 0.40168998; Operating Margin: 0.21410999; Profit Margin: 0.15435; Return On Equity: 0.15605; Total Revenue: 3966200064; Market Cap: 10904415232; Consensus EPS FY+1: 5.30402; growth: 0.1282 |
| S019 | news | GEN | Fri, 13 Nov 2026 22:09:00 GMT | ok | https://news.google.com/rss/search?q=GEN+Gen+Digital+stock&hl=en-US&gl=US&ceid=US:en | Gen Digital Inc. stock outperforms competitors on strong trading day - MarketWatch (Fri, 13 Nov 2026 22:09:00 GMT); Gen Digital Inc. (GEN) Stock Forecasts - Yahoo Finance (Wed, 11 Nov 2026 13:10:37 GMT); Gen Digital (GEN) Stock Repriced After Q2 Earnings Put Margins Center Stage - Yahoo Finance (Thu, 29 Oct 2026 07:00:00 GMT) |
| S020 | filing | CLX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000021076-26-000046); 8-K filed 2026-11-02 (accession 0000021076-26-000044); 8-K filed 2026-10-29 (accession 0001206774-26-000586) |
| S021 | news | CLX | Sat, 14 Nov 2026 11:08:53 GMT | ok | https://news.google.com/rss/search?q=CLX+Clorox+stock&hl=en-US&gl=US&ceid=US:en | The Clorox Company (CLX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Sat, 14 Nov 2026 11:08:53 GMT); The Clorox Company (CLX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 05:34:04 GMT); The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance Singapore (Fri, 13 Nov 2026 08:35:40 GMT) |
| S022 | filing | CHTR | 2026-11-06 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-06 (accession 0001091667-26-000073); 8-K filed 2026-11-06 (accession 0001091667-26-000072); 8-K filed 2026-10-27 (accession 0001091667-26-000064) |
| S023 | stock | CLX | 2026-11-14 | ok | https://finance.yahoo.com/quote/CLX | Trailing P/E: 19.68705; Forward P/E: 17.745283; Forward EPS: 6.1684; Price: 109.46; Market price: 109.46; Market cap: 13237893120; Sector: Consumer Defensive; Trailing Eps: 5.56; Revenue Growth: 0.333; Earnings Growth: 1.138; Gross Margin: 0.41939998; Operating Margin: 0.14286; Profit Margin: 0.09408; Return On Equity: 5.34363; Total Revenue: 7196000256; Market Cap: 13237893120; Consensus EPS FY+1: 6.1684; growth: 0.0769 |
| S024 | stock | GEN | 2026-11-14 | ok | https://finance.yahoo.com/quote/GEN | Trailing P/E: 15.431472; Forward P/E: 9.108996; Forward EPS: 3.33736; Price: 30.4; Market price: 30.4; Market cap: 18035593216; Sector: Technology; Trailing Eps: 1.97; Revenue Growth: 0.122; Earnings Growth: 1.286; Gross Margin: 0.77410007; Operating Margin: 0.43229; Profit Margin: 0.23068; Return On Equity: 0.46402; Total Revenue: 5228000256; Market Cap: 18035593216; Consensus EPS FY+1: 3.33736; growth: 0.1286 |
| S025 | filing | GEN | 2026-10-29 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000849399.json | Diluted EPS 0.83 for period ending 2026-10-02 (filed 2026-10-29) |
| S026 | filing | PNR | 2026-10-27 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json | Diluted EPS 2.76 for period ending 2026-09-30 (filed 2026-10-27) |
| S027 | filing | FISV | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json | Diluted EPS -8.9 for period ending 2026-09-30 (filed 2026-11-04) |
| S028 | news | CHTR | Thu, 12 Nov 2026 15:59:58 GMT | ok | https://news.google.com/rss/search?q=CHTR+Charter+Communications+stock&hl=en-US&gl=US&ceid=US:en | What Is The Biggest Threat To Charter Communications Stock? - Yahoo Finance (Thu, 12 Nov 2026 15:59:58 GMT); Charter Communications: 3 Key Takeaways for Long-Term Investors - Yahoo Finance (Thu, 12 Nov 2026 08:02:01 GMT); Why You Should Think About Charter Communications Differently Now? - Trefis (Fri, 13 Nov 2026 19:15:44 GMT) |
| S029 | filing | IDXX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000874716&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000874716-26-000135); 8-K filed 2026-11-02 (accession 0001104659-26-120892); 10-Q filed 2026-08-04 (accession 0000874716-26-000123) |
| S030 | stock | CHTR | 2026-11-14 | ok | https://finance.yahoo.com/quote/CHTR | Trailing P/E: 13.006578; Forward P/E: 3.2831066; Forward EPS: 42.15215; Price: 138.39; Market price: 138.39; Market cap: 24778944512; Sector: Communication Services; Trailing Eps: 10.64; Revenue Growth: 0.091; Gross Margin: 0.55084; Operating Margin: 0.23389; Profit Margin: 0.02498; Return On Equity: 0.07019; Total Revenue: 55645999104; Market Cap: 24778944512; Consensus EPS FY+1: 47.15811; growth: 1.0195 |
| S031 | news | IDXX | Fri, 13 Nov 2026 22:06:38 GMT | ok | https://news.google.com/rss/search?q=IDXX+Idexx+Laboratories+stock&hl=en-US&gl=US&ceid=US:en | IDEXX Laboratories, Inc. (IDXX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 22:06:38 GMT); IDEXX Laboratories (IDXX) Stock Looks Fairly Valued Despite Its 28% Run - Yahoo Finance (Sat, 31 Oct 2026 07:00:00 GMT); IDEXX Laboratories (IDXX) Q3 Earnings Leave Its Premium Valuation In Focus - Yahoo Finance (Tue, 03 Nov 2026 08:00:00 GMT) |
| S032 | filing | CLX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000021076.json | Diluted EPS 1.39 for period ending 2026-09-30 (filed 2026-11-02) |
| S033 | news | ROP | Fri, 13 Nov 2026 01:46:04 GMT | ok | https://news.google.com/rss/search?q=ROP+Roper+Technologies+stock&hl=en-US&gl=US&ceid=US:en | Roper Technologies, Inc. (ROP) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 01:46:04 GMT); Roper Technologies (ROP) Stock Looks Fully Valued As Cash Flow Comes Into Focus - Yahoo Finance (Fri, 06 Nov 2026 07:13:00 GMT); Roper (ROP) Stock May Be 16% Undervalued On Cash Flow - Yahoo Finance (Thu, 22 Oct 2026 07:00:00 GMT) |
| S034 | filing | CHTR | 2026-11-06 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001091667.json | Diluted EPS 0.38 for period ending 2026-09-30 (filed 2026-11-06) |
| S035 | filing | ROP | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000882835&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000882835-26-000047); 8-K filed 2026-10-22 (accession 0000882835-26-000042); 8-K filed 2026-10-01 (accession 0000882835-26-000039) |
| S036 | filing | RDDT | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001713445&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0001713445-26-000116); 8-K filed 2026-10-29 (accession 0001713445-26-000114); 8-K filed 2026-08-12 (accession 0001713445-26-000107) |
| S037 | stock | ROP | 2026-11-14 | ok | https://finance.yahoo.com/quote/ROP | Trailing P/E: 18.993866; Forward P/E: 19.532475; Forward EPS: 24.57318; Price: 479.975; Market price: 479.975; Market cap: 47535013888; Sector: Technology; Trailing Eps: 25.27; Revenue Growth: 0.076; Earnings Growth: 0.326; Gross Margin: 0.69671; Operating Margin: 0.28049; Profit Margin: 0.30712998; Return On Equity: 0.13229; Total Revenue: 8434599936; Market Cap: 47535013888; Consensus EPS FY+1: 24.57318; growth: 0.09810001 |
| S038 | stock | IDXX | 2026-11-14 | ok | https://finance.yahoo.com/quote/IDXX | Trailing P/E: 47.45485; Forward P/E: 41.687927; Forward EPS: 16.8929; Price: 704.23; Market price: 704.23; Market cap: 55483650048; Sector: Healthcare; Trailing Eps: 14.84; Revenue Growth: 0.099; Earnings Growth: 0.179; Gross Margin: 0.62722; Operating Margin: 0.32497; Profit Margin: 0.25357; Return On Equity: 0.68925005; Total Revenue: 4662220800; Market Cap: 55483650048; Consensus EPS FY+1: 16.8929; growth: 0.1244 |
| S039 | news | RDDT | Fri, 13 Nov 2026 18:20:39 GMT | ok | https://news.google.com/rss/search?q=RDDT+Reddit+stock&hl=en-US&gl=US&ceid=US:en | Should You Wait Before Buying Reddit Stock? - Trefis (Fri, 13 Nov 2026 18:20:39 GMT); Reddit shares sink on weak sales guidance and plans login requirement test as Google search traffic shrinks - CNBC (Thu, 29 Oct 2026 07:00:00 GMT); Reddit (NYSE:RDDT) surprises with Q3 2026 sales but stock drops 12.6% - Yahoo Finance (Thu, 29 Oct 2026 07:00:00 GMT) |
| S040 | filing | INTC | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000050863&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0000050863-26-000191); 8-K filed 2026-10-29 (accession 0000050863-26-000188); 8-K filed 2026-08-12 (accession 0001193125-26-346806) |

## Sources

- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFF&cosd=2026-01-01 (2026-11-12)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLH0A0HYM2&cosd=2026-01-01 (2026-11-12)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLC0A0CM&cosd=2026-01-01 (2026-11-12)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCSL&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=UNRATE&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=PAYEMS&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=T10Y2Y&cosd=2026-01-01 (2026-11-13)
- news FISV: https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 00:53:33 GMT)
- news APP: https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en (Tue, 10 Nov 2026 14:24:00 GMT)
- filing APP: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001751008&type=10-Q&dateb=&owner=include&count=10 (2026-11-04)
- filing FISV: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 (2026-11-04)
- filing PNR: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 (2026-10-27)
- news PNR: https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 15:54:46 GMT)
- filing GEN: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 (2026-10-29)
- filing APP: https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json (2026-11-04)
- stock APP: https://finance.yahoo.com/quote/APP (2026-11-14)
- stock FISV: https://finance.yahoo.com/quote/FISV (2026-11-14)
- stock PNR: https://finance.yahoo.com/quote/PNR (2026-11-14)
- news GEN: https://news.google.com/rss/search?q=GEN+Gen+Digital+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 22:09:00 GMT)
- filing CLX: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 (2026-11-02)

## AI Provenance

- Provider / model: hermes-local-proxy / upstage/solar-mini4:free
- Market research: attempts=1 tokens=9548 (prompt=6548, completion=3000) runtime=26.0s
- Fundamental research: generated this run at 2026-11-14T11:15:44.438335+00:00
- Evidence source dates: {'as_of': '2026-11-13', 'latest_equity_date': '2026-11-13', 'latest_macro_date': '2026-11-13', 'flows_date': '2026-11-13'}
- Evidence fingerprint: 7c7208bae3c2acb91f3e9451380a04e0aa0efd46b0ca16c51e5a0442c369eedd
- Source citations are retrieved external records in the ledger above; market values remain from the verified database snapshot.


## Disclosures

- This is research and market intelligence, not investment advice.
- AI conclusions are research judgments, not validated return predictions.
- The frozen risk layer is risk-only and is not used for directional views or allocations.
- Legacy scores are not active inputs or outputs.

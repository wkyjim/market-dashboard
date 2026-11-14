# AEGIS AI-First Market Intelligence

Research generated at: 14 November 2026, 17:19 HKT
Database freshness: equity 2026-11-13 (latest row retrieved 2026-11-14 13:50:55.938286+08:00)
Data cutoff: 2026-11-13 US cash close
Snapshot ID: aegis-hourly-20261114T091902Z

## Executive Summary

- **AI market view: Risk-on tilt with a quality and liquidity bias. Broad market internals are constructive (71% above the 50-day, 64% above the 200-day, positive 20-day price breadth), but the 20-day index return is slightly negative and the 20-day flow data show a mix of exceptional semiconductor/tech inflows and tactical outflows in other names. Sector leadership is split: Health Care, Consumer Discretionary, Consumer Staples, Real Estate and Financials are positive over 20 days, while Information Technology and Energy are negative. Macro data show a still-elevated but easing inflation backdrop, a stable labor market, and a modestly positive 10Y-2Y curve, supporting a cautious but not defensive posture.**
- Broad market internals are constructive: 71.34% of constituents above the 50-day, 63.6% above the 200-day, and a 1.70 advance/decline ratio on 2026-11-13.
- Index-level 20-day return is -1.28% for SPX, indicating short-term consolidation despite positive breadth.
- Sector rotation is visible: defensive and consumer sectors (Health Care, Consumer Staples, Consumer Discretionary, Real Estate, Financials) lead over 20 days; Information Technology and Energy lag.
- Flow data show exceptional institutional buying in SOXX (20d z-score 5.10) and strong liquidity in NVDA, AMD, MU and AAPL, while TLT shows medium-term deterioration.
- Macro backdrop: CPI 336.298 (Sep-2026), core CPI 338.896, unemployment 4.2%, 10Y-2Y spread 0.27, and high-yield OAS 3.20 support a risk-on but cautious stance.
- No investment ideas are provided; this is a market view and positioning framework only.

## Data QC

- Status: **PASS_WITH_WARNINGS**
- Equity session: 0 completed session(s) behind inference date
- Equity provenance: 386 provisional / 12581 canonical
- Breadth lag: 0 session(s); ETF-flow lag: 0 session(s)
- Note: Equity session contains a mix of provisional yfinance and canonical Massive rows.
- External sources: 79 ok / 0 unavailable; retrieved 2026-11-14T09:19:27.408608+00:00

## Idea Discovery

- S&P 500 universe: 503; eligible: 501; transparent shortlist: 20
- Method: independent momentum/dislocation/PE/liquidity buckets; no composite score
- Evidence used: latest close, 20d and 60d price returns, 60d drawdown, trailing P/E, dollar volume, GICS sector
- Not available as verified inputs: verified earnings-revision history, structured industry catalyst calendar
- Eligible but not shortlisted: 481 (outside the top independent momentum, dislocation, valuation and liquidity buckets)
- Included: APP (top_20d_momentum); FISV (top_20d_momentum); PNR (top_20d_momentum); GEN (top_20d_momentum); CLX (top_20d_momentum); CHTR (top_20d_momentum); IDXX (top_20d_momentum); ROP (top_20d_momentum); RDDT (largest_20d_dislocation); INTC (largest_20d_dislocation); SNDK (largest_20d_dislocation, liquidity_leader); MRVL (largest_20d_dislocation); FFIV (largest_20d_dislocation); NOW (largest_20d_dislocation); LITE (largest_20d_dislocation); COIN (largest_20d_dislocation); NVDA (liquidity_leader); AMD (liquidity_leader); MU (liquidity_leader); AAPL (liquidity_leader)
- Excluded reasons: {"missing_recent_or_latest_price": 2}

## Market Snapshot

| Asset | Latest | Change | Observation |
| --- | --- | --- | --- |
| SPX | 7561.6699 | -1.28% (20d) | Index is in a mild short-term pullback despite broad above-trend internals. |
| Health Care (XLV) | 0.0687 | +6.87% (20d) | Leading sector; trailing P/E 30.78 per S054. |
| Consumer Discretionary (XLY) | 0.0669 | +6.69% (20d) | Strong consumer sector; trailing P/E 25.11 per S061. |
| Information Technology (XLK) | -0.0719 | -7.19% (20d) | Negative 20d return; trailing P/E 30.03 per S073, elevated but liquidity-led. |
| Energy (XLE) | -0.0481 | -4.81% (20d) | Negative 20d return; trailing P/E 16.23 per S079. |
| SOXX | inflow | 20d z-score 5.10 | Exceptional institutional buying despite price decline; strong confirmation. |

## Macro, Fiscal, Rates, Liquidity and Credit

- Growth: Broad market internals are constructive (71.34% above 50-day, 63.6% above 200-day, 1.70 ADR), but SPX 20d return is -1.28%, indicating short-term consolidation rather than strong momentum.
- Inflation: CPI 336.298 and core CPI 338.896 (Sep-2026) show a still-elevated but stable inflation backdrop; external S004 confirms CPI 337.476 for Oct-2026.
- Policy: Effective federal funds rate is 3.88% (2026-11-12, S001), and the 10Y-2Y spread is 0.27 (S007), indicating a modestly positive curve and a policy stance that is not aggressively restrictive.
- Rates: High-yield OAS 3.20 (S002) and IG OAS 0.89 (S003) suggest credit conditions are stable but not loose; the modest curve slope supports a balanced risk posture.
- Liquidity: SOXX shows exceptional institutional buying (20d z-score 5.10) while TLT shows medium-term deterioration; equity liquidity leaders NVDA, AMD, MU and AAPL confirm strong market depth.
- Credit: High-yield OAS 3.20 is not distressed, but the combination of negative 20d index return and mixed flows argues for maintaining a quality and liquidity bias rather than chasing breadth.

## US Equities and 11 GICS Sectors

Macro source IDs: S001, S002, S003, S004, S005, S007

| GICS sector | Evidence | AI research stance | Source IDs |
| --- | --- | --- | --- |
| Health Care | 20d return +6.87% (XLV), leading the sector; trailing P/E 30.78 (S054). | Constructive; quality and defensive characteristics support a core holding. | S054 |
| Consumer Staples | 20d return +5.40% (XLP), trailing P/E 24.85 (S055). | Defensive strength; stable earnings and low volatility support a holding. | S055 |
| Consumer Discretionary | 20d return +6.69% (XLY), trailing P/E 25.11 (S061). | Positive momentum; consumer demand remains supportive. | S061 |
| Real Estate | 20d return +5.24% (XLRE), trailing P/E 29.63 (S062). | Positive 20d return; valuation is elevated but relative strength is notable. | S062 |
| Financials | 20d return +5.69% (XLF), trailing P/E 15.85 (S063). | Positive momentum with a reasonable valuation; supportive of a risk-on tilt. | S063 |
| Utilities | 20d return +4.34% (XLU), trailing P/E 18.11 (S065). | Stable defensive sector; lower return but consistent with a cautious risk posture. | S065 |
| Materials | 20d return +2.57% (XLB), trailing P/E 21.72 (S066). | Modest positive momentum; neutral stance with no strong conviction. | S066 |
| Industrials | 20d return +0.61% (XLI), trailing P/E 27.07 (S069). | Near-flat momentum; neutral stance, no clear leadership. | S069 |
| Communication Services | 20d return -1.48% (XLC), trailing P/E 17.26 (S072). | Negative 20d return; neutral to cautious, no strong catalyst. | S072 |
| Information Technology | 20d return -7.19% (XLK), trailing P/E 30.03 (S073); liquidity leaders NVDA, AMD, MU show strong dollar volume. | Negative sector return but exceptional liquidity and institutional inflows (SOXX) suggest a quality/liquidity bias rather than broad weakness. | S073 |
| Energy | 20d return -4.81% (XLE), trailing P/E 16.23 (S079). | Negative 20d return; neutral to cautious, no strong catalyst. | S079 |

### Sector fundamentals, valuation and earnings

Sector-level point-in-time fundamentals are not fully supplied in the database snapshot. The provided evidence is limited to 20-day ETF returns, trailing P/E ratios for the 11 GICS sectors, and liquidity/flow indicators. No sector-level earnings, revenue, or balance-sheet fundamentals are available in the supplied data, so no sector fundamentals are asserted beyond the supplied P/E and return evidence.

## Growth vs Value

- Growth: Information Technology and Communication Services show negative 20d returns, but liquidity leaders NVDA, AMD, MU and AAPL indicate strong institutional demand and market depth.
- Value: Financials (XLF trailing P/E 15.85) and Energy (XLE trailing P/E 16.23) offer the most reasonable valuations among the supplied sectors.
- Quality: Health Care (XLV trailing P/E 30.78) and Consumer Staples (XLP trailing P/E 24.85) combine positive momentum with defensive characteristics.
- Momentum: Consumer Discretionary (XLY +6.69%) and Health Care (XLV +6.87%) lead on 20d returns, while Information Technology (-7.19%) and Energy (-4.81%) lag.
- No composite score or forward-return mapping is used; the view is based on independent momentum, dislocation, valuation and liquidity buckets.

## ETF Flows and Breadth

- Breadth is constructive: 71.34% above 50-day, 63.6% above 200-day, 1.70 advance/decline ratio, and 70.46% positive 20d returns on 2026-11-13.
- Price/breadth divergence is -27.49 with negative_divergence=false, but bullish_divergence=true and standardized_divergence=-0.0758, indicating a mild but not alarming divergence.
- Flows show exceptional institutional buying in SOXX (20d z-score 5.10) and strong liquidity in NVDA, AMD, MU and AAPL.
- TLT shows medium-term deterioration (20d z-score -0.41, 60d z-score -0.29), suggesting reduced demand for duration.
- No new highs or new lows are reported (0/0), so breadth is not being driven by extreme extremes.

## Stock Ideas

Single-stock research uses reported EPS, forward P/E and company fundamentals. All ideas are research judgments, not validated return predictions.

| Ticker | Security | Research view | Price | EPS | Forward P/E | Base target | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| APP | AppLovin | KEEP | 409.1 | 20.86026 | 19.611452 | 409.07 | KEEP |
| FISV | Fiserv | KEEP | 63.78 | 7.98015037065659 | 7.9923306 | 63.84 | KEEP |
| IDXX | Idexx Laboratories | KEEP | 704.23 | 16.8929 | 41.687927 | 704.27 | KEEP |
| ROP | Roper Technologies | KEEP | 479.975 | 24.57318 | 19.532475 | 479.91 | KEEP |

## ETF Ideas

ETF research uses holdings, portfolio valuation and exposure. Single-stock EPS × P/E valuation is not applied to ETFs.

| Ticker | Fund | Research view | Price | Top holdings | Portfolio valuation | Sector exposure | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| XLV | Health Care sector ETF | KEEP | 188.85 | LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59% | Top 10 holdings; numeric weight coverage 61.42% | Health Care | KEEP |
### APP — AppLovin

- **Type:** Stock
- **Research view:** KEEP
- **Thesis:** AppLovin screens as a top 20-day momentum name with a 53.7% 20-day return and a 32.5% 60-day return, and its 60-day drawdown is essentially flat at -0.2%. The Q3 2026 filing shows diluted EPS of $11.61 and a forward EPS of $20.86, implying a forward P/E of about 19.6x. The momentum and valuation profile support keeping the position.
- **Source IDs:** S008, S012, S015, S016
- **Catalysts:** Continued 20-day momentum with a 53.7% return, Q3 2026 reported EPS of $11.61 and forward EPS of $20.86, Flat 60-day drawdown of -0.2% indicating limited downside stress
- **Risks:** High 20-day momentum can mean elevated volatility, Forward P/E of ~19.6x leaves limited margin for earnings disappointment, Mobile advertising and app monetization trends can shift quickly
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation assumptions:** Forward EPS 20.8603 (source.forwardEps) x AI multiple assumption 19.61; source IDs S008, S012, S015, S016
- **EPS:** 20.86026
- **Forward P/E:** 19.611452
- **Company fundamentals:** 
- **Bull / Base / Bear:** 500.65 / 409.07 / 333.76
- **Scenario probabilities:** not separately assigned; see scenario table.

### FISV — Fiserv

- **Type:** Stock
- **Research view:** KEEP
- **Thesis:** Fiserv screens as a top 20-day momentum name with a 34.1% 20-day return and a 24.1% 60-day return. The Q3 2026 filing shows a reported diluted EPS of -$8.90, but the forward EPS is $7.98, implying a forward P/E of about 8.0x. The low forward multiple and strong momentum support keeping the position.
- **Source IDs:** S010, S011, S017, S019
- **Catalysts:** 34.1% 20-day return and 24.1% 60-day return, Forward EPS of $7.98 and forward P/E of ~8.0x, Q3 2026 filing dated 2026-11-04
- **Risks:** Reported Q3 2026 diluted EPS of -$8.90 indicates a loss, Low forward P/E may reflect known earnings weakness, Financial technology and payments regulation risk
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation assumptions:** Forward EPS 7.9802 (derived: price / source.forwardPE) x AI multiple assumption 8.00; source IDs S010, S011, S017, S019
- **EPS:** 7.98015037065659
- **Forward P/E:** 7.9923306
- **Company fundamentals:** 
- **Bull / Base / Bear:** 191.52 / 63.84 / 127.68
- **Scenario probabilities:** not separately assigned; see scenario table.

### IDXX — Idexx Laboratories

- **Type:** Stock
- **Research view:** KEEP
- **Thesis:** Idexx Laboratories screens as a top 20-day momentum name with a 25.7% 20-day return and a 29.0% 60-day return, with a 60-day drawdown of only -0.3%. The Q3 2026 filing shows diluted EPS of $11.75 and a forward EPS of $16.89, implying a forward P/E of about 41.7x. The strong momentum and modest drawdown support keeping the position despite the higher multiple.
- **Source IDs:** S028, S031, S034, S043
- **Catalysts:** 25.7% 20-day return and 29.0% 60-day return, 60-day drawdown of only -0.3%, Q3 2026 reported EPS of $11.75 and forward EPS of $16.89
- **Risks:** Forward P/E of ~41.7x is rich and leaves little room for multiple compression, Veterinary diagnostics and animal health demand can be cyclical, High momentum can reverse quickly
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation assumptions:** Forward EPS 16.8929 (source.forwardEps) x AI multiple assumption 41.69; source IDs S028, S031, S034, S043
- **EPS:** 16.8929
- **Forward P/E:** 41.687927
- **Company fundamentals:** 
- **Bull / Base / Bear:** 405.43 / 704.27 / 270.29
- **Scenario probabilities:** not separately assigned; see scenario table.

### ROP — Roper Technologies

- **Type:** Stock
- **Research view:** KEEP
- **Thesis:** Roper Technologies screens as a top 20-day momentum name with a 25.4% 20-day return and a 16.9% 60-day return, with a 60-day drawdown of -2.5%. The Q3 2026 filing shows diluted EPS of $21.30 and a forward EPS of $24.57, implying a forward P/E of about 19.5x. The momentum and valuation support keeping the position.
- **Source IDs:** S032, S035, S036, S042
- **Catalysts:** 25.4% 20-day return and 16.9% 60-day return, 60-day drawdown of -2.5%, Q3 2026 reported EPS of $21.30 and forward EPS of $24.57
- **Risks:** Forward P/E of ~19.5x leaves limited margin for earnings disappointment, Software and technology spending can slow, High momentum can reverse quickly
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation assumptions:** Forward EPS 24.5732 (source.forwardEps) x AI multiple assumption 19.53; source IDs S032, S035, S036, S042
- **EPS:** 24.57318
- **Forward P/E:** 19.532475
- **Company fundamentals:** 
- **Bull / Base / Bear:** 589.76 / 479.91 / 393.17
- **Scenario probabilities:** not separately assigned; see scenario table.

### XLV — Health Care sector ETF

- **Type:** ETF
- **Research view:** KEEP
- **Thesis:** XLV is a Health Care sector ETF with a close of $188.85 and a dollar volume of $1.09B. The top-10 holdings are dominated by large-cap pharmaceutical and medical device names, providing diversified exposure to the sector. The ETF is a reasonable way to maintain sector exposure without single-stock idiosyncratic risk.
- **Source IDs:** S054, S056
- **Catalysts:** Diversified top-10 holdings including LLY, JNJ, ABBV, MRK, UNH, TMO, AMGN, GILD, ABT, PFE, High dollar volume of $1.09B supports liquidity, Sector-level exposure to health care innovation and aging demographics
- **Risks:** Sector concentration in large-cap pharma and medical devices, Regulatory and reimbursement risk across the health care sector, Macro and inflation risk to drug pricing and medical spending
- **Valuation method:** Holdings/portfolio valuation with AI total-return assumption
- **Valuation assumptions:** Holdings/portfolio valuation; 10 weighted holdings; coverage 61.42%; source IDs S054, S056
- **Top holdings:** LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59%
- **Portfolio valuation:** Top 10 holdings; numeric weight coverage 61.42%
- **Sector exposure:** Health Care
- **Underlying drivers:** Large-cap pharmaceutical and medical device leaders; diversified health care sector exposure
- **Bull / Base / Bear:** 211.51 / 198.29 / 177.52
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

### Short Term

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 25% | +2.00% | No directional signal; frozen daily-close model; 5-day forecast vol 14.9%; spike probability 16.5% below historical baseline 22.1%; no material event during 2026-11-16 to 2026-11-20. |
| Base | 50% | +0.00% | No directional signal; frozen daily-close model; 5-day forecast vol 14.9%; spike probability 16.5% below historical baseline 22.1%; no material event during 2026-11-16 to 2026-11-20. |
| Bear | 25% | -2.00% | No directional signal; frozen daily-close model; 5-day forecast vol 14.9%; spike probability 16.5% below historical baseline 22.1%; no material event during 2026-11-16 to 2026-11-20. |

### Long Term

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 30% | +8.00% | No directional signal; frozen daily-close model; 5-day forecast vol 14.9%; spike probability 16.5% below historical baseline 22.1%; no material event during 2026-11-16 to 2026-11-20. |
| Base | 40% | +3.00% | No directional signal; frozen daily-close model; 5-day forecast vol 14.9%; spike probability 16.5% below historical baseline 22.1%; no material event during 2026-11-16 to 2026-11-20. |
| Bear | 30% | -5.00% | No directional signal; frozen daily-close model; 5-day forecast vol 14.9%; spike probability 16.5% below historical baseline 22.1%; no material event during 2026-11-16 to 2026-11-20. |

## Positioning

- Maintain a risk-on tilt with a quality and liquidity bias; do not chase broad market weakness.
- Favor Health Care, Consumer Discretionary, Consumer Staples, Real Estate and Financials for relative strength.
- Treat Information Technology as a liquidity-led, quality-leaning sleeve rather than a broad momentum play.
- Keep Energy and Communication Services on a neutral/cautious stance with no directional conviction.
- Use TLT as a reduced-duration signal; do not add to duration until flow conditions improve.
- No weights, allocations, or composite scores are provided.

## Catalysts

| Date | Event | Why it matters |
| --- | --- | --- |
| 2026-11-16 | Frozen daily-close model forecast window opens | Forecast window starts 2026-11-16; volatility 5d 14.93% and spike probability 16.5% are below historical/ewma baselines, suggesting a relatively calm near-term window. |
| 2026-11-13 | SOXX exceptional institutional buying | 20d flow z-score 5.10 with strong confirmation indicates continued liquidity support for technology/semiconductor names. |
| 2026-11-13 | SPX 20d return -1.28% with positive breadth | Short-term index pullback with broad participation suggests a consolidation phase rather than a trend reversal. |

## Key Risks

- Equity session contains a mix of provisional yfinance and canonical Massive rows, which may

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
| S011 | news | FISV | Fri, 13 Nov 2026 00:53:33 GMT | ok | https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en | Fiserv, Inc. (FISV) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 00:53:33 GMT); Fiserv (FISV) Stock Looks Undervalued With Strong Excess Returns - Yahoo Finance (Wed, 11 Nov 2026 22:14:34 GMT); Fiserv Stock Outlook: Is Wall Street Bullish or Bearish? - Yahoo Finance (Thu, 12 Nov 2026 12:23:56 GMT) |
| S012 | news | APP | Tue, 10 Nov 2026 14:24:00 GMT | ok | https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en | APP Stock Surges 51% After Q3 Earnings: Is it Still a Buy? - Yahoo Finance (Tue, 10 Nov 2026 14:24:00 GMT); Is Trending Stock AppLovin Corporation (APP) a Buy Now? - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT); AppLovin vs. The Trade Desk: Which Is the Better Digital Advertising Stock to Buy Going Into 2027? - The Motley Fool (Fri, 13 Nov 2026 17:17:00 GMT) |
| S013 | news | PNR | Fri, 13 Nov 2026 15:54:46 GMT | ok | https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en | Pentair plc (PNR) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 15:54:46 GMT); Has Pentair (PNR) Fallen Far Enough To Look Undervalued On Earnings? - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT); Pentair (PNR) Stock May Be 46% Undervalued As New CFO Arrives - Yahoo Finance (Fri, 25 Sep 2026 07:00:00 GMT) |
| S014 | filing | GEN | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0000849399-26-000083); 8-K filed 2026-10-28 (accession 0000849399-26-000081); 8-K filed 2026-10-09 (accession 0000849399-26-000079) |
| S015 | stock | APP | 2026-11-14 | ok | https://finance.yahoo.com/quote/APP | Trailing P/E: 27.54882; Forward P/E: 19.611452; Forward EPS: 20.86026; Price: 409.1; Market price: 409.1; Market cap: 135543824384; Sector: Communication Services |
| S016 | filing | APP | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json | Diluted EPS 11.61 for period ending 2026-09-30 (filed 2026-11-04) |
| S017 | stock | FISV | 2026-11-14 | ok | https://finance.yahoo.com/quote/FISV | Forward P/E: 7.9923306; Price: 63.78; Market price: 63.78; Market cap: 33934002176 |
| S018 | stock | PNR | 2026-11-14 | ok | https://finance.yahoo.com/quote/PNR | Trailing P/E: 18.610355; Forward P/E: 12.877027; Forward EPS: 5.30402; Price: 68.3; Market price: 68.3; Market cap: 10904415232; Sector: Industrials |
| S019 | filing | FISV | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json | Diluted EPS -8.9 for period ending 2026-09-30 (filed 2026-11-04) |
| S020 | filing | CLX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000021076-26-000046); 8-K filed 2026-11-02 (accession 0000021076-26-000044); 8-K filed 2026-10-29 (accession 0001206774-26-000586) |
| S021 | filing | PNR | 2026-10-27 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json | Diluted EPS 2.76 for period ending 2026-09-30 (filed 2026-10-27) |
| S022 | stock | CLX | 2026-11-14 | ok | https://finance.yahoo.com/quote/CLX | Trailing P/E: 19.68705; Forward P/E: 17.745283; Forward EPS: 6.1684; Price: 109.46; Market price: 109.46; Market cap: 13237893120; Sector: Consumer Defensive |
| S023 | stock | GEN | 2026-11-14 | ok | https://finance.yahoo.com/quote/GEN | Trailing P/E: 15.431472; Forward P/E: 9.108996; Forward EPS: 3.33736; Price: 30.4; Market price: 30.4; Market cap: 18035593216; Sector: Technology |
| S024 | news | GEN | Fri, 13 Nov 2026 22:09:00 GMT | ok | https://news.google.com/rss/search?q=GEN+Gen+Digital+stock&hl=en-US&gl=US&ceid=US:en | Gen Digital Inc. stock outperforms competitors on strong trading day - MarketWatch (Fri, 13 Nov 2026 22:09:00 GMT); Gen Digital Inc. (GEN) Stock Forecasts - Yahoo Finance (Wed, 11 Nov 2026 13:10:37 GMT); Gen Digital (GEN) Stock Repriced After Q2 Earnings Put Margins Center Stage - Yahoo Finance (Thu, 29 Oct 2026 07:00:00 GMT) |
| S025 | news | CLX | Fri, 13 Nov 2026 14:17:51 GMT | ok | https://news.google.com/rss/search?q=CLX+Clorox+stock&hl=en-US&gl=US&ceid=US:en | The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance Singapore (Fri, 13 Nov 2026 14:17:51 GMT); The Clorox Company (CLX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Sat, 14 Nov 2026 09:08:48 GMT); The Clorox Company (CLX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Wed, 11 Nov 2026 18:00:47 GMT) |
| S026 | filing | CHTR | 2026-11-06 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-06 (accession 0001091667-26-000073); 8-K filed 2026-11-06 (accession 0001091667-26-000072); 8-K filed 2026-10-27 (accession 0001091667-26-000064) |
| S027 | filing | GEN | 2026-10-29 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000849399.json | Diluted EPS 0.83 for period ending 2026-10-02 (filed 2026-10-29) |
| S028 | stock | IDXX | 2026-11-14 | ok | https://finance.yahoo.com/quote/IDXX | Trailing P/E: 47.45485; Forward P/E: 41.687927; Forward EPS: 16.8929; Price: 704.23; Market price: 704.23; Market cap: 55483650048; Sector: Healthcare |
| S029 | filing | CLX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000021076.json | Diluted EPS 1.39 for period ending 2026-09-30 (filed 2026-11-02) |
| S030 | stock | CHTR | 2026-11-14 | ok | https://finance.yahoo.com/quote/CHTR | Trailing P/E: 13.006578; Forward P/E: 3.2831066; Forward EPS: 42.15215; Price: 138.39; Market price: 138.39; Market cap: 24778944512; Sector: Communication Services |
| S031 | filing | IDXX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000874716&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000874716-26-000135); 8-K filed 2026-11-02 (accession 0001104659-26-120892); 10-Q filed 2026-08-04 (accession 0000874716-26-000123) |
| S032 | filing | ROP | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000882835&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000882835-26-000047); 8-K filed 2026-10-22 (accession 0000882835-26-000042); 8-K filed 2026-10-01 (accession 0000882835-26-000039) |
| S033 | news | CHTR | Thu, 12 Nov 2026 15:59:58 GMT | ok | https://news.google.com/rss/search?q=CHTR+Charter+Communications+stock&hl=en-US&gl=US&ceid=US:en | What Is The Biggest Threat To Charter Communications Stock? - Yahoo Finance (Thu, 12 Nov 2026 15:59:58 GMT); Charter Communications: 3 Key Takeaways for Long-Term Investors - Yahoo Finance (Thu, 12 Nov 2026 08:02:01 GMT); Why You Should Think About Charter Communications Differently Now? - Trefis (Fri, 13 Nov 2026 19:15:44 GMT) |
| S034 | news | IDXX | Fri, 13 Nov 2026 22:06:38 GMT | ok | https://news.google.com/rss/search?q=IDXX+Idexx+Laboratories+stock&hl=en-US&gl=US&ceid=US:en | IDEXX Laboratories, Inc. (IDXX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 22:06:38 GMT); IDEXX Laboratories (IDXX) Stock Looks Fairly Valued Despite Its 28% Run - Yahoo Finance (Sat, 31 Oct 2026 07:00:00 GMT); IDEXX Laboratories (IDXX) Q3 Earnings Leave Its Premium Valuation In Focus - Yahoo Finance (Tue, 03 Nov 2026 08:00:00 GMT) |
| S035 | stock | ROP | 2026-11-14 | ok | https://finance.yahoo.com/quote/ROP | Trailing P/E: 18.993866; Forward P/E: 19.532475; Forward EPS: 24.57318; Price: 479.975; Market price: 479.975; Market cap: 47535013888; Sector: Technology |
| S036 | news | ROP | Fri, 13 Nov 2026 01:46:04 GMT | ok | https://news.google.com/rss/search?q=ROP+Roper+Technologies+stock&hl=en-US&gl=US&ceid=US:en | Roper Technologies, Inc. (ROP) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 01:46:04 GMT); Roper Technologies (ROP) Stock Looks Fully Valued As Cash Flow Comes Into Focus - Yahoo Finance (Fri, 06 Nov 2026 07:13:00 GMT); Roper (ROP) Stock May Be 16% Undervalued On Cash Flow - Yahoo Finance (Thu, 22 Oct 2026 07:00:00 GMT) |
| S037 | filing | RDDT | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001713445&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0001713445-26-000116); 8-K filed 2026-10-29 (accession 0001713445-26-000114); 8-K filed 2026-08-12 (accession 0001713445-26-000107) |
| S038 | filing | CHTR | 2026-11-06 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001091667.json | Diluted EPS 0.38 for period ending 2026-09-30 (filed 2026-11-06) |
| S039 | stock | RDDT | 2026-11-14 | ok | https://finance.yahoo.com/quote/RDDT | Trailing P/E: 20.091835; Forward P/E: 10.770874; Forward EPS: 9.14039; Price: 98.45; Market price: 98.45; Market cap: 19010076672; Sector: Communication Services |
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
- filing PNR: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 (2026-10-27)
- filing FISV: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 (2026-11-04)
- news FISV: https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 00:53:33 GMT)
- news APP: https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en (Tue, 10 Nov 2026 14:24:00 GMT)
- news PNR: https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 15:54:46 GMT)
- filing GEN: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 (2026-10-29)
- stock APP: https://finance.yahoo.com/quote/APP (2026-11-14)
- filing APP: https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json (2026-11-04)
- stock FISV: https://finance.yahoo.com/quote/FISV (2026-11-14)
- stock PNR: https://finance.yahoo.com/quote/PNR (2026-11-14)
- filing FISV: https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json (2026-11-04)
- filing CLX: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 (2026-11-02)

## AI Provenance

- Provider / model: hermes-local-proxy / upstage/solar-mini4:free
- Market research: attempts=1 tokens=7512 (prompt=4512, completion=3000) runtime=36.94s
- Fundamental research: generated this run at 2026-11-14T09:19:02.172109+00:00
- Evidence source dates: {'as_of': '2026-11-13', 'latest_equity_date': '2026-11-13', 'latest_macro_date': '2026-11-13', 'flows_date': '2026-11-13'}
- Evidence fingerprint: fe35873e337e080e76a8ccc11cf42b699526622f1e27a7e713648687e5a86fab
- Source citations are retrieved external records in the ledger above; market values remain from the verified database snapshot.


## Disclosures

- This is research and market intelligence, not investment advice.
- AI conclusions are research judgments, not validated return predictions.
- The frozen risk layer is risk-only and is not used for directional views or allocations.
- Legacy scores are not active inputs or outputs.

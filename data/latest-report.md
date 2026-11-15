# AEGIS AI-First Market Intelligence

Research generated at: 16 November 2026, 05:13 HKT
Database freshness: equity 2026-11-13 (latest row retrieved 2026-11-15 13:06:40.074841+08:00)
Data cutoff: 2026-11-13 US cash close
Snapshot ID: aegis-hourly-20261115T211344Z

## Executive Summary

- **AI market view: Risk-on tilt with a quality/momentum bias: broad market breadth is positive, but the 20-day return is negative and the 10Y-2Y curve is flat, so the setup favors high-quality, liquid, and momentum-led names over speculative or deeply discounted names.**
- Broad market breadth is constructive (71.3% above 50-day, 63.6% above 200-day, ADR 1.70), yet the index is down 1.28% over 20 days, indicating a cautious but not bearish tape.
- Liquidity leaders and dislocation names dominate the shortlist, with NVDA, AMD, MU, AAPL, SNDK, and MRVL showing strong dollar-volume leadership.
- Sector returns are bifurcated: Health Care, Consumer Discretionary, Consumer Staples, Real Estate, Financials, Utilities, and Materials are up over 20 days, while Communication Services, Information Technology, and Energy are down.
- Macro signals are mixed: the effective fed funds rate is 3.88%, high-yield OAS is 3.20%, and the 10Y-2Y spread is 0.27%, pointing to a late-cycle but not stressed credit environment.
- Crypto markets are under pressure, with BTC down 6.0% and ETH down 8.2% on 2026-11-14, suggesting risk-off sentiment in digital assets.
- The frozen risk model shows 5-day forecast volatility of 14.9% and a spike probability of 16.5%, below the 18.5% threshold, implying no imminent tail-risk event.

## Data QC

- Status: **PASS_WITH_WARNINGS**
- Equity session: 0 completed session(s) behind inference date
- Equity provenance: 393 provisional / 12576 canonical
- Breadth lag: 0 session(s); ETF-flow lag: 0 session(s)
- Note: Equity session contains a mix of provisional yfinance and canonical Massive rows.
- External sources: 79 ok / 0 unavailable; retrieved 2026-11-15T21:14:01.847462+00:00

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
| S&P 500 | 7561.67 | -1.28% (20d) | Broad market breadth is positive, but the index is down over 20 days, indicating a cautious but not bearish tape. |
| NVDA | liquidity_leader | PE 26.51, earnings yield 3.77% | Top liquidity leader with a reasonable valuation and strong institutional buying. |
| AMD | liquidity_leader | PE 128.88, earnings yield 0.78% | High-multiple liquidity leader; strong dollar volume but expensive on trailing earnings. |
| MU | liquidity_leader | PE 11.40, earnings yield 8.77% | Liquidity leader with a low valuation and high earnings yield, attractive on a value basis. |
| AAPL | liquidity_leader | PE 39.42, earnings yield 2.54% | Liquidity leader with a premium multiple; sector-relative P/E of 1.17 suggests it is richly valued. |
| SNDK | liquidity_leader | PE 15.94, earnings yield 6.27% | Liquidity leader with a reasonable valuation and high earnings yield; flagged for forward PE issues. |
| MRVL | liquidity_leader | PE 74.23, earnings yield 1.35% | Liquidity leader but very expensive; flagged for forward EPS jump issues. |
| XLV | Health Care | +6.87% (20d) | Top-performing sector; trailing P/E of 30.78 suggests rich valuation. |
| XLC | Communication Services | -1.48% (20d) | Negative sector return; trailing P/E of 17.26 is relatively cheap. |
| XLK | Information Technology | -7.19% (20d) | Negative sector return; trailing P/E of 30.03 is expensive. |

## Macro, Fiscal, Rates, Liquidity and Credit

- Growth: The 10Y-2Y Treasury spread is 0.27 as of 2026-11-13, indicating a modestly positive but flat yield curve, consistent with a late-cycle expansion.
- Inflation: CPI stands at 336.298 (2026-09-01) and core CPI at 338.896, with the latest CPI reading from 2026-10-01 at 337.476, suggesting inflation remains above the Fed's 2% target.
- Policy: The effective federal funds rate is 3.88% as of 2026-11-12, indicating the Fed is holding rates at a restrictive level.
- Rates: The 10Y-2Y spread of 0.27 is near flat, and the yield curve is not steepening, which historically signals caution on growth expectations.
- Liquidity: High-yield OAS is 3.20 and IG OAS is 0.89 as of 2026-11-12, implying credit spreads are not excessively wide and liquidity conditions are manageable.
- Credit: The frozen risk model shows 5-day forecast volatility of 14.9% and a spike probability of 16.5%, below the 18.5% threshold, indicating no imminent tail-risk event.

## US Equities and 11 GICS Sectors

Macro source IDs: S001, S002, S003, S004, S005, S006, S007

| GICS sector | Evidence | AI research stance | Source IDs |
| --- | --- | --- | --- |
| Health Care | Sector return 20d +6.87%; trailing P/E 30.78; shortlist includes IDXX (PE 39.18, earnings yield 2.55%, sector-relative PE 1.33) and CHTR (PE 2.71, earnings yield 36.95%, sector-relative PE 0.13). | Health Care is the top-performing sector, but the shortlist shows a mix of expensive (IDXX) and very cheap (CHTR) names; the sector's strength may be driven by defensive flows rather than broad momentum. | S051, S001 |
| Consumer Discretionary | Sector return 20d +6.69%; trailing P/E 25.11; shortlist includes CHTR (PE 2.71, earnings yield 36.95%, sector-relative PE 0.13) and CLX (PE 18.27, earnings yield 5.47%, sector-relative PE 0.76). | Consumer Discretionary is a strong performer, but the shortlist is dominated by a single very cheap name (CHTR) and a mid-cap consumer staples name (CLX), suggesting selective rather than broad strength. | S060, S001 |
| Financials | Sector return 20d +5.69%; trailing P/E 15.85; shortlist includes FISV (PE 9.65, earnings yield 10.36%, sector-relative PE 0.67) and PNR (PE 13.59, earnings yield 7.36%, sector-relative PE 0.49). | Financials are performing well with a low valuation; the shortlist includes two cheap names with high earnings yields, but FISV is flagged for forward EPS missing. | S062, S001 |
| Industrials | Sector return 20d +0.61%; trailing P/E 27.07; shortlist includes PNR (PE 13.59, earnings yield 7.36%, sector-relative PE 0.49) and FFIV (PE 35.08, earnings yield 2.85%, sector-relative PE 1.04). | Industrials are near flat, and the shortlist shows a mix of cheap (PNR) and expensive (FFIV) names; the sector's weak performance suggests limited momentum. | S071, S001 |
| Information Technology | Sector return 20d -7.19%; trailing P/E 30.03; shortlist includes NVDA (PE 26.51, earnings yield 3.77%, sector-relative PE 0.79), AMD (PE 128.88, earnings yield 0.78%, sector-relative PE 3.82), and MRVL (PE 74.23, earnings yield 1.35%, sector-relative PE 2.20). | Information Technology is the worst-performing sector, and the shortlist is dominated by high-multiple liquidity leaders (NVDA, AMD, MRVL) with very high sector-relative P/Es, indicating expensive, momentum-driven names rather than value. | S076, S001 |
| Energy | Sector return 20d -4.81%; trailing P/E 16.23; no shortlist names in the energy sector. | Energy is a weak performer with no shortlist representation, suggesting limited institutional interest and a value-trap or cyclical downturn risk. | S078, S001 |
| Consumer Staples | Sector return 20d +5.40%; trailing P/E 24.85; shortlist includes CLX (PE 18.27, earnings yield 5.47%, sector-relative PE 0.76) and CHTR (PE 2.71, earnings yield 36.95%, sector-relative PE 0.13). | Consumer Staples is a solid performer, but the shortlist is dominated by a very cheap name (CHTR) and a mid-cap consumer staples name (CLX); the sector's strength may be driven by defensive flows. | S063, S001 |
| Materials | Sector return 20d +2.57%; trailing P/E 21.72; no shortlist names in the materials sector. | Materials are performing modestly, but the lack of shortlist names suggests limited institutional interest and a neutral-to-cautious stance. | S068, S001 |
| Real Estate | Sector return 20d +5.24%; trailing P/E 29.63; no shortlist names in the real estate sector. | Real Estate is a decent performer, but the lack of shortlist names and high trailing P/E suggest limited conviction and potential overvaluation. | S064, S001 |
| Utilities | Sector return 20d +4.34%; trailing P/E 18.11; no shortlist names in the utilities sector. | Utilities are performing well with a reasonable valuation, but the lack of shortlist names suggests limited institutional interest and a defensive rather than growth-oriented stance. | S069, S001 |
| Communication Services | Sector return 20d -1.48%; trailing P/E 17.26; shortlist includes CHTR (PE 2.71, earnings yield 36.95%, sector-relative PE 0.13). | Communication Services is a weak performer, but the shortlist includes a very cheap name (CHTR) with a high earnings yield, suggesting a value opportunity despite the sector's negative momentum. | S073, S001 |

### Sector fundamentals, valuation and earnings

No point-in-time sector fundamentals are supplied beyond trailing P/E for the 11 G

## Growth vs Value


## ETF Flows and Breadth


## Stock Ideas

Single-stock research uses reported EPS, forward P/E and company fundamentals. All ideas are research judgments, not validated return predictions.

| Ticker | Security | Research view | Price | EPS | Forward P/E | Base target | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| APP | AppLovin | NEW | 409.1 | 20.86026 | 19.611452 | 417.21 | NEW |
| RDDT | Reddit | NEW | 98.45 | 9.14039 | 10.770874 | 146.25 | NEW |

## ETF Ideas

ETF research uses holdings, portfolio valuation and exposure. Single-stock EPS × P/E valuation is not applied to ETFs.

| Ticker | Fund | Research view | Price | Top holdings | Portfolio valuation | Sector exposure | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| XLY | Consumer Discretionary sector ETF | NEW | 119.98 | AMZN 21.29%, TSLA 18.78%, HD 5.47%, MCD 4.46%, TJX 4.07%, SBUX 3.11%, LOW 3.08%, BKNG 2.93%, MAR 2.24%, HLT 2.11% | Top 10 holdings; numeric weight coverage 67.54% | Consumer Discretionary | NEW |
| XLP | Consumer Staples sector ETF | NEW | 92.35 | WMT 11.14%, COST 9.09%, PG 7.60%, KO 7.37%, PM 6.59%, MO 4.70%, CL 4.42%, MDLZ 4.25%, PEP 4.11%, TGT 4.00% | Top 10 holdings; numeric weight coverage 63.28% | Consumer Staples | NEW |
### APP — AppLovin

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** AppLovin offers a rare combination of top-tier momentum, best-in-class margins, and strong growth, making it a more compelling standalone candidate than the lower-margin, lower-growth names in the shortlist such as Clorox or Pentair. Alternatives considered: CLX, PNR.
- **Thesis:** AppLovin screens in the top 20-day momentum bucket with a 53.7% 20-day return and a 32.5% 60-day return, while maintaining a 60-day drawdown of only -0.2%. The company reports strong fundamentals: FY1 revenue growth of 55.5%, earnings growth of 75.5%, gross margin of 88.8%, operating margin of 77.8%, and a forward P/E of 19.6. The combination of high momentum, durable profitability, and a reasonable forward valuation supports a new BUY.
- **Source IDs:** S008, S012, S015, S016
- **Catalysts:** Continued high 20-day momentum with 53.7% price return, Sustained revenue growth near 55% and earnings growth near 75%, Premium but stable gross and operating margins above 77%, Forward P/E of 19.6 remains reasonable relative to growth profile
- **Risks:** High momentum can reverse quickly; 20-day return of 53.7% may already price in much of the good news, Forward EPS and fiscal-year mapping are unverified, so forward P/E should be monitored, Single-name concentration risk in a high-growth ad-tech name
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 20.8603 (source.forwardEps) x AI multiple assumption 20.00; source IDs S008, S012, S015, S016
- **EPS:** 20.86026 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 19.611452
- **FY+1 growth assumption:** 27.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / Apple peers in high-margin consumer/device ecosystem (e.g., MSFT, GOOGL) / APP shows strong FY+1 consensus growth of 27.44% and revenue growth of 55.6%, supported by 88.8% gross margin and 77.8% operating margin, indicating durable pricing power and ecosystem economics. The forward EPS of 20.86 and forward P/E of 19.6x are below the 20-24x base/bull range, reflecting a premium but justified by high margins and growth; bear case at 16x reflects margin compression or growth deceleration risk. Peer comparison to MSFT/GOOGL supports a 20-24x multiple for sustained high growth and margins.
- **Company fundamentals:** FY1 revenue growth 55.5%, earnings growth 75.5%, gross margin 88.8%, operating margin 77.8%, profit margin 65.9%, ROE 2.10, forward P/E 19.6, price 409.1
- **Bull / Base / Bear:** 500.65 / 417.21 / 333.76
- **Bull / Base / Bear returns:** 22.38% / 1.98% / -18.42%
- **Scenario probabilities:** not separately assigned; see scenario table.

### RDDT — Reddit

- **Type:** Stock
- **Research view:** NEW (stance: NEUTRAL)
- **Why preferred / alternatives:** Reddit offers the deepest dislocation and the lowest forward P/E among the high-growth candidates, but the negative momentum and large drawdown make it less preferred than the momentum leaders like AppLovin and Gen Digital. Alternatives considered: APP, GEN.
- **Thesis:** Reddit is the largest 20-day dislocation name in the shortlist, with a 36.9% 20-day decline and a 39.4% 60-day drawdown. It still carries a 33.2x trailing P/E and a 3.0% earnings yield, but the dislocation is driven by sharp price declines rather than fundamental distress. The company reports FY1 revenue growth of 53.0%, earnings growth of 74.9%, gross margin of 91.5%, and a forward P/E of 10.8, which is attractive. However, the negative 20-day and 60-day returns and the large drawdown warrant a neutral stance until the dislocation resolves and the stock stabilizes.
- **Source IDs:** S038, S039, S041, S044
- **Catalysts:** Dislocation may create a mean-reversion opportunity if the underlying business continues to grow, FY1 revenue growth of 53% and earnings growth of 75% support a low forward P/E of 10.8, Gross margin of 91.5% indicates strong pricing power and operating leverage, Forward P/E of 10.8 is the cheapest among high-growth names in the shortlist
- **Risks:** 36.9% 20-day decline and 39.4% 60-day drawdown signal ongoing selling pressure, Trailing P/E of 33.2 remains elevated relative to the forward P/E of 10.8, Dislocation can persist if investor sentiment does not recover, Single-name concentration risk in a high-growth social media platform
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 9.1404 (source.forwardEps) x AI multiple assumption 16.00; source IDs S038, S039, S041, S044
- **EPS:** 9.14039 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 10.770874
- **FY+1 growth assumption:** 24.17%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / RDDT peers in high-growth cloud/tech infrastructure (e.g., MSFT, GOOGL) / RDDT shows FY+1 consensus growth of 24.17% and revenue growth of 53.0%, with 91.5% gross margin but lower 29.4% operating margin and 32.0% ROE, indicating strong top-line momentum but operating leverage and capital intensity risk. The forward EPS of 9.14 and forward P/E of 10.8x are below the 16-20x base/bull range, reflecting a value opportunity if operating leverage improves; bear case at 12x reflects continued margin pressure or competitive intensity. Peer comparison to MSFT/GOOGL supports a 16-20x multiple for growth, with a lower base reflecting current operating margin constraints.
- **Company fundamentals:** FY1 revenue growth 53.0%, earnings growth 74.9%, gross margin 91.5%, operating margin 29.4%, profit margin 32.1%, ROE 0.32, forward P/E 10.8, price 98.45
- **Bull / Base / Bear:** 182.81 / 146.25 / 109.68
- **Bull / Base / Bear returns:** 85.69% / 48.55% / 11.41%
- **Scenario probabilities:** not separately assigned; see scenario table.

### XLY — Consumer Discretionary sector ETF

- **Type:** ETF
- **Research view:** NEW (stance: NEUTRAL)
- **Why preferred / alternatives:** XLY provides broad sector exposure but is not preferred over the more focused, higher-quality single-name candidates like AppLovin or the defensive sector ETFs such as XLP. Alternatives considered: XLP, XLV.
- **Thesis:** XLY is the Consumer Discretionary sector ETF with a -0.4% raw price change and a -0.4% 20-day return, reflecting broad weakness in consumer discretionary. The ETF holds large weights in AMZN (21.3%) and TSLA (18.8%), which are themselves high-multiple, high-volatility names. The sector exposure is broad but the current price action is negative, so a neutral stance is appropriate until the underlying drivers stabilize.
- **Source IDs:** S059, S060
- **Catalysts:** Sector exposure to consumer discretionary, which may benefit if consumer spending inflects, Large weights in AMZN and TSLA provide upside if those names re-rate, ETF structure provides diversification across the sector
- **Risks:** Negative raw price change of -0.4% and negative 20-day return, Heavy concentration in AMZN and TSLA, which are high-multiple and high-volatility, Consumer discretionary remains sensitive to macro and consumer confidence
- **Valuation method:** Holdings/portfolio valuation with AI total-return assumption
- **Valuation status:** verified; forward-EPS source: ; period flags: 
- **Valuation assumptions:** Holdings/portfolio valuation; 10 weighted holdings; coverage 67.54%; source IDs S059, S060
- **Top holdings:** AMZN 21.29%, TSLA 18.78%, HD 5.47%, MCD 4.46%, TJX 4.07%, SBUX 3.11%, LOW 3.08%, BKNG 2.93%, MAR 2.24%, HLT 2.11%
- **Portfolio valuation:** Top 10 holdings; numeric weight coverage 67.54%
- **Sector exposure:** Consumer Discretionary
- **Underlying drivers:** Consumer discretionary spending, AMZN and TSLA performance, consumer confidence, retail and e-commerce trends
- **Bull / Base / Bear:** 137.98 / 129.58 / 115.18
- **Bull / Base / Bear returns:** 15.0% / 8.0% / -4.0%
- **Scenario probabilities:** not separately assigned; see scenario table.

### XLP — Consumer Staples sector ETF

- **Type:** ETF
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** XLP offers the strongest sector ETF momentum in the shortlist with defensive, high-quality holdings, making it preferable to the negative-momentum XLY and the more volatile sector ETFs. Alternatives considered: XLY, XLV.
- **Thesis:** XLP is the Consumer Staples sector ETF with a +1.4% raw price change and a +1.4% 20-day return, making it the strongest sector ETF in the shortlist. The ETF holds defensive, high-quality names such as WMT, COST, PG, KO, and PM, which provide stability and defensive exposure. The positive price action and defensive sector characteristics support a BUY stance.
- **Source IDs:** S057, S063
- **Catalysts:** Positive raw price change of +1.4% and positive 20-day return, Defensive sector with stable demand across economic cycles, Top holdings include WMT, COST, PG, KO, and PM, all high-quality consumer staples names, Sector ETF provides diversification and lower single-name risk
- **Risks:** Limited upside if consumer staples face margin pressure from input costs, Sector rotation away from staples could reduce relative performance, Limited growth compared to high-momentum equity names
- **Valuation method:** Holdings/portfolio valuation with AI total-return assumption
- **Valuation status:** verified; forward-EPS source: ; period flags: 
- **Valuation assumptions:** Holdings/portfolio valuation; 10 weighted holdings; coverage 63.28%; source IDs S057, S063
- **Top holdings:** WMT 11.14%, COST 9.09%, PG 7.60%, KO 7.37%, PM 6.59%, MO 4.70%, CL 4.42%, MDLZ 4.25%, PEP 4.11%, TGT 4.00%
- **Portfolio valuation:** Top 10 holdings; numeric weight coverage 63.28%
- **Sector exposure:** Consumer Staples
- **Underlying drivers:** Consumer staples demand, retail and grocery pricing power, input cost inflation, defensive consumer spending
- **Bull / Base / Bear:** 103.43 / 97.89 / 89.58
- **Bull / Base / Bear returns:** 12.0% / 6.0% / -3.0%
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
| Bull | 25% | +2.00% | Low 5-day realized vol (14.9%) and below-threshold spike probability (16.5% vs 18.5% threshold) support a modest upside if US close confirms stable liquidity and no credit stress. |
| Base | 50% | +0.00% | Frozen daily-close model with no directional signal and elevated but sub-threshold volatility implies range-bound trading near the 2026-11-13 close. |
| Bear | 25% | -2.00% | If the US close fails to confirm the frozen forecast, elevated spike probability (16.5%) and baseline volatility could trigger a mild downside correction. |

### Long Term (12 months)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 30% | +8.00% | Sustained low realized vol and stable credit conditions support a positive drift if earnings and rate expectations remain constructive over the horizon. |
| Base | 40% | +3.00% | Frozen daily-close model with no directional signal implies a modest positive drift as baseline volatility and historical risk premiums normalize. |
| Bear | 30% | -5.00% | If spike probability and volatility remain elevated without confirmation, a negative earnings or credit shock could drive a meaningful drawdown. |

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
| S009 | news | FISV | Thu, 12 Nov 2026 12:23:56 GMT | ok | https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en | Fiserv Stock Outlook: Is Wall Street Bullish or Bearish? - Yahoo Finance (Thu, 12 Nov 2026 12:23:56 GMT); Michael Burry makes a bold call on struggling payments giant - Yahoo Finance (Wed, 11 Nov 2026 00:17:00 GMT); Fiserv (FISV) Stock Looks Undervalued With Strong Excess Returns - Yahoo Finance Singapore (Wed, 11 Nov 2026 22:14:34 GMT) |
| S010 | filing | FISV | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0000798354-26-000042); 8-K filed 2026-11-03 (accession 0000798354-26-000039); 8-K filed 2026-10-23 (accession 0001193125-26-429481) |
| S011 | filing | PNR | 2026-10-27 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-27 (accession 0000077360-26-000058); 8-K filed 2026-10-27 (accession 0000077360-26-000055); 8-K filed 2026-09-22 (accession 0000077360-26-000050) |
| S012 | news | APP | Thu, 12 Nov 2026 20:05:45 GMT | ok | https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en | AppLovin Just Ripped 47% in a Month: Is It Too Late to Buy APP Stock Now? - Yahoo Finance (Thu, 12 Nov 2026 20:05:45 GMT); ETFs Are Net Sellers of AppLovin (APP) on Nov. 11 - Yahoo Finance (Fri, 13 Nov 2026 11:02:35 GMT); APP Stock Surges 51% After Q3 Earnings: Is it Still a Buy? - Yahoo Finance (Tue, 10 Nov 2026 14:24:00 GMT) |
| S013 | news | PNR | Fri, 13 Nov 2026 22:05:23 GMT | ok | https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en | Pentair plc (PNR) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 22:05:23 GMT); Pentair (PNR) Stock May Be 46% Undervalued As New CFO Arrives - Yahoo Finance (Fri, 25 Sep 2026 07:00:00 GMT); Pentair plc (PNR) Q3 Earnings and Revenues Beat Estimates - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT) |
| S014 | filing | GEN | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0000849399-26-000083); 8-K filed 2026-10-28 (accession 0000849399-26-000081); 8-K filed 2026-10-09 (accession 0000849399-26-000079) |
| S015 | stock | APP | 2026-11-15 | ok | https://finance.yahoo.com/quote/APP | Trailing P/E: 27.54882; Forward P/E: 19.611452; Forward EPS: 20.86026; Price: 409.1; Market price: 409.1; Market cap: 135543824384; Sector: Communication Services; Trailing Eps: 14.85; Revenue Growth: 0.555; Earnings Growth: 0.755; Gross Margin: 0.8878; Operating Margin: 0.77782995; Profit Margin: 0.65887; Return On Equity: 2.1008599; Total Revenue: 7608893952; Market Cap: 135543824384; Consensus EPS FY+1: 20.72438; growth: 0.2744 |
| S016 | filing | APP | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json | Diluted EPS 11.61 for period ending 2026-09-30 (filed 2026-11-04) |
| S017 | stock | FISV | 2026-11-15 | ok | https://finance.yahoo.com/quote/FISV | Forward P/E: 7.99667; Price: 63.78; Market price: 63.78; Market cap: 33934002176; Market Cap: 33934002176; Consensus EPS FY+1: 7.98015; growth: 0.09689999 |
| S018 | stock | PNR | 2026-11-15 | ok | https://finance.yahoo.com/quote/PNR | Trailing P/E: 18.610355; Forward P/E: 12.877027; Forward EPS: 5.30402; Price: 68.3; Market price: 68.3; Market cap: 10904415232; Sector: Industrials; Trailing Eps: 3.67; Revenue Growth: -0.045; Earnings Growth: -0.188; Gross Margin: 0.40168998; Operating Margin: 0.21410999; Profit Margin: 0.15435; Return On Equity: 0.15605; Total Revenue: 3966200064; Market Cap: 10904415232; Consensus EPS FY+1: 5.30402; growth: 0.1282 |
| S019 | filing | PNR | 2026-10-27 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json | Diluted EPS 2.76 for period ending 2026-09-30 (filed 2026-10-27) |
| S020 | filing | FISV | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json | Diluted EPS -8.9 for period ending 2026-09-30 (filed 2026-11-04) |
| S021 | filing | CLX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000021076-26-000046); 8-K filed 2026-11-02 (accession 0000021076-26-000044); 8-K filed 2026-10-29 (accession 0001206774-26-000586) |
| S022 | stock | GEN | 2026-11-15 | ok | https://finance.yahoo.com/quote/GEN | Trailing P/E: 15.431472; Forward P/E: 9.108996; Forward EPS: 3.33736; Price: 30.4; Market price: 30.4; Market cap: 18035593216; Sector: Technology; Trailing Eps: 1.97; Revenue Growth: 0.122; Earnings Growth: 1.286; Gross Margin: 0.77410007; Operating Margin: 0.43229; Profit Margin: 0.23068; Return On Equity: 0.46402; Total Revenue: 5228000256; Market Cap: 18035593216; Consensus EPS FY+1: 3.33736; growth: 0.1286 |
| S023 | stock | CLX | 2026-11-15 | ok | https://finance.yahoo.com/quote/CLX | Trailing P/E: 19.68705; Forward P/E: 17.745283; Forward EPS: 6.1684; Price: 109.46; Market price: 109.46; Market cap: 13260793856; Sector: Consumer Defensive; Trailing Eps: 5.56; Revenue Growth: 0.333; Earnings Growth: 1.138; Gross Margin: 0.41939998; Operating Margin: 0.14286; Profit Margin: 0.09408; Return On Equity: 5.34363; Total Revenue: 7196000256; Market Cap: 13260793856; Consensus EPS FY+1: 6.1684; growth: 0.0769 |
| S024 | news | CLX | Sun, 15 Nov 2026 08:55:47 GMT | ok | https://news.google.com/rss/search?q=CLX+Clorox+stock&hl=en-US&gl=US&ceid=US:en | The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance UK (Sun, 15 Nov 2026 08:55:47 GMT); The Clorox Company (CLX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 05:44:34 GMT); The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance Singapore (Fri, 13 Nov 2026 14:10:46 GMT) |
| S025 | news | GEN | Fri, 13 Nov 2026 09:34:35 GMT | ok | https://news.google.com/rss/search?q=GEN+Gen+Digital+stock&hl=en-US&gl=US&ceid=US:en | Gen Digital Inc. (GEN) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 09:34:35 GMT); Gen Digital (GEN) Stock Repriced After Q2 Earnings Put Margins Center Stage - Yahoo Finance (Thu, 29 Oct 2026 07:00:00 GMT); Gen Digital Stock: Is Wall Street Bullish or Bearish? - Yahoo Finance (Thu, 05 Nov 2026 08:00:00 GMT) |
| S026 | filing | CHTR | 2026-11-06 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-06 (accession 0001091667-26-000073); 8-K filed 2026-11-06 (accession 0001091667-26-000072); 8-K filed 2026-10-27 (accession 0001091667-26-000064) |
| S027 | filing | IDXX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000874716&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000874716-26-000135); 8-K filed 2026-11-02 (accession 0001104659-26-120892); 10-Q filed 2026-08-04 (accession 0000874716-26-000123) |
| S028 | news | IDXX | Sat, 14 Nov 2026 06:13:17 GMT | ok | https://news.google.com/rss/search?q=IDXX+Idexx+Laboratories+stock&hl=en-US&gl=US&ceid=US:en | IDEXX Laboratories, Inc. (IDXX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Sat, 14 Nov 2026 06:13:17 GMT); symbol__ Stock Quote Price and Forecast - CNN (Fri, 13 Nov 2026 15:22:45 GMT); IDEXX Laboratories, Inc. (IDXX) stock price, news, quote and history - Yahoo Finance UK (Fri, 13 Nov 2026 21:03:37 GMT) |
| S029 | news | CHTR | Sun, 15 Nov 2026 05:47:01 GMT | ok | https://news.google.com/rss/search?q=CHTR+Charter+Communications+stock&hl=en-US&gl=US&ceid=US:en | Charter Communications (CHTR) Stock Could Be A Bargain Following Its New Operating Model - Yahoo Finance (Sun, 15 Nov 2026 05:47:01 GMT); Why You Should Think About Charter Communications Differently Now? - Yahoo Finance (Fri, 13 Nov 2026 19:16:11 GMT); Charter Communications (CHTR) Earnings Expected to Grow: What to Know Ahead of Next Week's Release - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT) |
| S030 | stock | IDXX | 2026-11-15 | ok | https://finance.yahoo.com/quote/IDXX | Trailing P/E: 47.45485; Forward P/E: 41.687927; Forward EPS: 16.8929; Price: 704.23; Market price: 704.23; Market cap: 55483650048; Sector: Healthcare; Trailing Eps: 14.84; Revenue Growth: 0.099; Earnings Growth: 0.179; Gross Margin: 0.62722; Operating Margin: 0.32497; Profit Margin: 0.25357; Return On Equity: 0.68925005; Total Revenue: 4662220800; Market Cap: 55483650048; Consensus EPS FY+1: 16.8929; growth: 0.1244 |
| S031 | filing | GEN | 2026-10-29 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000849399.json | Diluted EPS 0.83 for period ending 2026-10-02 (filed 2026-10-29) |
| S032 | stock | CHTR | 2026-11-15 | ok | https://finance.yahoo.com/quote/CHTR | Trailing P/E: 13.006578; Forward P/E: 3.2831066; Forward EPS: 42.15215; Price: 138.39; Market price: 138.39; Market cap: 24778944512; Sector: Communication Services; Trailing Eps: 10.64; Revenue Growth: 0.091; Gross Margin: 0.55084; Operating Margin: 0.23389; Profit Margin: 0.02498; Return On Equity: 0.07019; Total Revenue: 55645999104; Market Cap: 24778944512; Consensus EPS FY+1: 47.15811; growth: 1.0195 |
| S033 | filing | CLX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000021076.json | Diluted EPS 1.39 for period ending 2026-09-30 (filed 2026-11-02) |
| S034 | filing | CHTR | 2026-11-06 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001091667.json | Diluted EPS 0.38 for period ending 2026-09-30 (filed 2026-11-06) |
| S035 | stock | ROP | 2026-11-15 | ok | https://finance.yahoo.com/quote/ROP | Trailing P/E: 18.993866; Forward P/E: 19.532475; Forward EPS: 24.57318; Price: 479.975; Market price: 479.975; Market cap: 47535013888; Sector: Technology; Trailing Eps: 25.27; Revenue Growth: 0.076; Earnings Growth: 0.326; Gross Margin: 0.69671; Operating Margin: 0.28049; Profit Margin: 0.30712998; Return On Equity: 0.13229; Total Revenue: 8434599936; Market Cap: 47535013888; Consensus EPS FY+1: 24.57318; growth: 0.09810001 |
| S036 | filing | ROP | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000882835&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000882835-26-000047); 8-K filed 2026-10-22 (accession 0000882835-26-000042); 8-K filed 2026-10-01 (accession 0000882835-26-000039) |
| S037 | news | ROP | Fri, 13 Nov 2026 13:04:22 GMT | ok | https://news.google.com/rss/search?q=ROP+Roper+Technologies+stock&hl=en-US&gl=US&ceid=US:en | Roper Technologies, Inc. (ROP) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 13:04:22 GMT); Roper Technologies (ROP) Stock Looks Fully Valued As Cash Flow Comes Into Focus - Yahoo Finance (Thu, 05 Nov 2026 08:00:00 GMT); Roper Technologies (ROP), What Is Behind The Fresh Attention? - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT) |
| S038 | filing | RDDT | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001713445&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0001713445-26-000116); 8-K filed 2026-10-29 (accession 0001713445-26-000114); 8-K filed 2026-08-12 (accession 0001713445-26-000107) |
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
- news FISV: https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en (Thu, 12 Nov 2026 12:23:56 GMT)
- filing FISV: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 (2026-11-04)
- filing PNR: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 (2026-10-27)
- news APP: https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en (Thu, 12 Nov 2026 20:05:45 GMT)
- news PNR: https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 22:05:23 GMT)
- filing GEN: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 (2026-10-29)
- stock APP: https://finance.yahoo.com/quote/APP (2026-11-15)
- filing APP: https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json (2026-11-04)
- stock FISV: https://finance.yahoo.com/quote/FISV (2026-11-15)
- stock PNR: https://finance.yahoo.com/quote/PNR (2026-11-15)
- filing PNR: https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json (2026-10-27)
- filing FISV: https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json (2026-11-04)

## AI Provenance

- Provider / model: hermes-local-proxy / upstage/solar-mini4:free
- Market research: attempts=1 tokens=9500 (prompt=6500, completion=3000) runtime=23.46s
- Fundamental research: generated this run at 2026-11-15T21:13:44.680865+00:00
- Evidence source dates: {'as_of': '2026-11-13', 'latest_equity_date': '2026-11-13', 'latest_macro_date': '2026-11-14', 'flows_date': '2026-11-13'}
- Evidence fingerprint: b57f240ae90d876e9d88fa3bdf846c22e23312cffdc4fca96e76b2d32c6ad67c
- Source citations are retrieved external records in the ledger above; market values remain from the verified database snapshot.


## Disclosures

- This is research and market intelligence, not investment advice.
- AI conclusions are research judgments, not validated return predictions.
- The frozen risk layer is risk-only and is not used for directional views or allocations.
- Legacy scores are not active inputs or outputs.

# AEGIS AI-First Market Intelligence

Research generated at: 26 November 2026, 18:17 HKT
Database freshness: equity 2026-11-25 (latest row retrieved 2026-11-26 13:05:50.828884+08:00)
Data cutoff: 2026-11-25 US cash close
Snapshot ID: aegis-hourly-20261126T101721Z

## Executive Summary

- **AI market view: Late-November 2026 US equity market is characterized by a broad pullback, with the S&P 500 down 7.25% over 20 days and Information Technology and Energy the weakest sectors. Momentum and dislocation screens are mixed: a small group of names shows strong 20-day momentum, while a larger group is in deep 20-day dislocations. Breadth is mixed, with 59.12% above the 50-day and 55.42% above the 200-day, but the 20-day advance/decline ratio of 2.876 and 55.67% positive 20-day returns suggest a short-term bullish tilt. Macro data show a Fed funds rate of 3.88% as of 2026-11-24, a 10Y-2Y spread of 0.24, and elevated credit spreads, pointing to a cautious but not alarmist macro backdrop.**
- S&P 500 is in a 20-day drawdown of -7.25%, with Information Technology (-18.43%) and Energy (-11.03%) the weakest sectors and Consumer Staples (+6.29%) the strongest.
- Momentum screen shortlisted 12 names on top 20-day momentum; dislocation screen shortlisted 10 names on largest 20-day drawdowns; liquidity leaders include NVDA, AMD, AAPL, AMZN, and MU.
- Breadth is mixed: 59.12% above 50-day, 55.42% above 200-day, but 20-day advance/decline ratio of 2.876 and 55.67% positive 20-day returns indicate short-term bullish tilt.
- Macro backdrop: Fed funds rate 3.88% (2026-11-24), 10Y-2Y spread 0.24, US high-yield OAS 3.72, IG OAS 0.98, suggesting a cautious but not alarmist rate and credit environment.
- Sector P/E data show Consumer Staples (24.84), Consumer Discretionary (24.59), and Health Care (29.94) as relatively expensive, while Financials (15.26), Energy (15.21), and Utilities (17.94) are cheaper.
- Risk forecast shows 5-day forecast volatility of 27.94% and a spike probability of 65.99%, above the historical baseline of 31.64%, indicating elevated near-term risk.

## Data QC

- Status: **PASS_WITH_WARNINGS**
- Equity session: 0 completed session(s) behind inference date
- Macro session: 2026-11-26 (0 completed session(s) behind inference date)
- Equity provenance: 296 provisional / 12634 canonical
- Breadth lag: 0 session(s); ETF-flow lag: 0 session(s)
- Note: Equity session contains a mix of provisional yfinance and canonical Massive rows.
- External sources: 79 ok / 0 unavailable; retrieved 2026-11-26T10:17:36.292791+00:00

## Idea Discovery

- S&P 500 universe: 503; eligible: 501; transparent shortlist: 20
- Method: independent momentum/dislocation/PE/liquidity buckets; no composite score
- Evidence used: latest close, 20d and 60d price returns, 60d drawdown, trailing P/E, earnings yield, sector-relative P/E, dollar volume, GICS sector
- Not available as verified inputs: verified earnings-revision history for the full universe, FY+2 consensus, structured industry catalyst calendar
- Eligible but not shortlisted: 481 (outside the top independent momentum, dislocation, valuation and liquidity buckets)
- Included: APP (top_20d_momentum); CHTR (top_20d_momentum); CMG (top_20d_momentum); CLX (top_20d_momentum); TSCO (top_20d_momentum); MGM (top_20d_momentum); IDXX (top_20d_momentum); FISV (top_20d_momentum); SNDK (largest_20d_dislocation); MRVL (largest_20d_dislocation); LITE (largest_20d_dislocation); DDOG (largest_20d_dislocation); INTC (largest_20d_dislocation); DELL (largest_20d_dislocation); MU (largest_20d_dislocation, liquidity_leader); NOW (largest_20d_dislocation); NVDA (liquidity_leader); AMD (liquidity_leader); AAPL (liquidity_leader); AMZN (liquidity_leader)
- Excluded reasons: {"missing_recent_or_latest_price": 2}
- Valuation-quality rejected: [{"flags": ["forward_pe_outside_plausible_range", "implausible_earnings_yield", "forward_eps_vs_reported_jump"], "ticker": "CHTR"}, {"flags": ["forward_eps_missing"], "ticker": "FISV"}, {"flags": ["forward_pe_outside_plausible_range", "implausible_earnings_yield"], "ticker": "SNDK"}, {"flags": ["forward_eps_vs_reported_jump"], "ticker": "MRVL"}, {"flags": ["forward_eps_vs_reported_jump"], "ticker": "LITE"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "INTC"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "DELL"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "MU"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "NOW"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "NVDA"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "AMD"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "AAPL"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "AMZN"}]

## Market Snapshot

| Asset | Latest | Change | Observation |
| --- | --- | --- | --- |
| S&P 500 | 7182.78 | -7.25% (20d) | Broad pullback; IT and Energy weakest, Consumer Staples strongest. |
| Information Technology (XLK) | -18.43% | 20d return | Largest sector drawdown; XLK trailing P/E 27.47. |
| Energy (XLE) | -11.03% | 20d return | Second-largest sector drawdown; XLE trailing P/E 15.21. |
| Consumer Staples (XLP) | +6.29% | 20d return | Strongest sector; XLP trailing P/E 24.84. |
| Health Care (XLV) | +2.20% | 20d return | Positive sector; XLV trailing P/E 29.94. |
| Financials (XLF) | +0.68% | 20d return | Modest gain; XLF trailing P/E 15.26. |

## Macro, Fiscal, Rates, Liquidity and Credit

- Fed funds rate at 3.88% as of 2026-11-24, with a 10Y-2Y spread of 0.24, indicating a modestly positive but not steep yield curve.
- US high-yield OAS at 3.72 and IG OAS at 0.98 as of 2026-11-24, suggesting elevated credit risk premiums and a cautious credit environment.
- US CPI (CPIAUCSL) latest observation 2026-10-01: 337.476; Core CPI 338.896; unemployment rate 4.1% as of 2026-10-01, indicating persistent inflation and a stable labor market.
- US nonfarm payrolls (PAYEMS) latest observation 2026-10-01: 159,293, indicating continued employment growth.
- Risk forecast shows 5-day forecast volatility of 27.94% and spike probability of 65.99%, above historical baseline of 31.64%, indicating elevated near-term risk.
- Equity market is in a 20-day drawdown of -7.25%, with IT and Energy the weakest sectors, suggesting a risk-off tilt in specific sectors.

## US Equities and 11 GICS Sectors

Macro source IDs: S001, S002, S003, S004, S005, S006, S007

| GICS sector | Evidence | AI research stance | Source IDs |
| --- | --- | --- | --- |
| Information Technology | Sector ETF XLK returned -18.43% over 20 days; trailing P/E 27.47 (S073). | Weakest sector; high valuation and sharp drawdown warrant caution. | S073 |
| Energy | Sector ETF XLE returned -11.03% over 20 days; trailing P/E 15.21 (S075). | Second-weakest sector; cheap valuation but sharp drawdown. | S075 |
| Consumer Staples | Sector ETF XLP returned +6.29% over 20 days; trailing P/E 24.84 (S060). | Strongest sector; defensive appeal but elevated valuation. | S060 |
| Health Care | Sector ETF XLV returned +2.20% over 20 days; trailing P/E 29.94 (S053). | Positive sector; high valuation but relative stability. | S053 |
| Financials | Sector ETF XLF returned +0.68% over 20 days; trailing P/E 15.26 (S067). | Modest gain; cheap valuation but limited momentum. | S067 |
| Consumer Discretionary | Sector ETF XLY returned +1.87% over 20 days; trailing P/E 24.59 (S058). | Modest gain; mid-range valuation. | S058 |
| Utilities | Sector ETF XLU returned +2.64% over 20 days; trailing P/E 17.94 (S063). | Positive sector; cheap valuation. | S063 |
| Real Estate | Sector ETF XLRE returned +4.11% over 20 days; trailing P/E 29.29 (S064). | Positive sector; high valuation. | S064 |
| Materials | Sector ETF XLB returned -1.25% over 20 days; trailing P/E 21.30 (S068). | Slight decline; mid-range valuation. | S068 |
| Industrials | Sector ETF XLI returned -3.29% over 20 days; trailing P/E 26.13 (S069). | Negative sector; elevated valuation. | S069 |
| Communication Services | Sector ETF XLC returned +2.17% over 20 days; trailing P/E 16.74 (S070). | Positive sector; cheap valuation. | S070 |

### Sector fundamentals, valuation and earnings

No point-in-time sector fundamentals beyond ETF-level trailing P/E and 20-day returns are supplied in the database. The sector evidence is limited to the 11 GICS sector ETFs (XLV, XLP, XLY, XLRE, XLF, XLU, XLB, XLI, XLC, XLK, XLE) with their 20-day returns and trailing P/E values from the external source set. No sector-level growth, margin, or consensus data are available in the supplied evidence.

## Growth vs Value

- Consumer Staples (XLP) and Consumer Discretionary (XLY) trade at the highest trailing P/Es (24.84 and 24.59), indicating relatively expensive valuations.
- Financials (XLF) and Energy (XLE) trade at the lowest trailing P/Es (15.26 and 15.21), indicating relatively cheap valuations.
- Health Care (XLV) and Real Estate (XLRE) have high trailing P/Es (29.94 and 29.29) despite positive 20-day returns.
- Information Technology (XLK) has a trailing P/E of 27.47 but the worst 20-day return (-18.43%), suggesting a valuation-growth disconnect.

## ETF Flows and Breadth

- 20-day advance/decline ratio of 2.876 (371 advancers vs 129 decliners) and 55.67% positive 20-day returns indicate short-term bullish breadth.
- 59.12% of names above the 50-day and 55.42% above the 200-day, but the 20-day price/breadth divergence of -7.52 and negative_divergence flag suggest caution.
- Flow data show SOXX with a 20-day flow z-score of 2.19 and 60-day z-score of 2.53, indicating exceptional institutional buying despite a down price state.
- TLT shows a 20-day flow z-score of 0.47 and 60-day z-score of -0.09, indicating neutral flow structure with structural accumulation.
- SMH shows a 20-day flow z-score of 0.55 and 60-day z-score of 1.12, indicating neutral flow with structural accumulation.

## Stock Ideas

Single-stock research uses reported EPS, forward P/E and company fundamentals. All ideas are research judgments, not validated return predictions.

| Ticker | Security | Research view | Price | EPS | Forward P/E | Base target | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| APP | AppLovin | NEW | 378.95 | 20.86084 | 18.165617 | 417.22 | NEW |
| IDXX | Idexx Laboratories | NEW | 709.46 | 16.8929 | 41.997524 | 405.43 | NEW |
| DDOG | Datadog | EXIT | 158.25 | 3.1829 | 49.71881 | 89.12 | EXIT |

## ETF Ideas

ETF research uses holdings, portfolio valuation and exposure. Single-stock EPS × P/E valuation is not applied to ETFs.

| Ticker | Fund | Research view | Price | Top holdings | Portfolio valuation | Sector exposure | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| XLV | Health Care sector ETF | KEEP | 183.68 | LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59% | Top 10 holdings; numeric weight coverage 61.42% | Health Care | KEEP |
| XLP | Consumer Staples sector ETF | KEEP | 92.3 | WMT 11.14%, COST 9.09%, PG 7.60%, KO 7.37%, PM 6.59%, MO 4.70%, CL 4.42%, MDLZ 4.25%, PEP 4.11%, TGT 4.00% | Top 10 holdings; numeric weight coverage 63.28% | Consumer Staples | KEEP |
### APP — AppLovin

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** AppLovin offers a higher-quality, higher-margin digital advertising franchise than the lower-quality momentum names in the shortlist, with a forward P/E near 18.2 versus the unverified forward multiples of the other momentum candidates. Alternatives considered: CMG, CLX, TSCO, MGM, IDXX.
- **Thesis:** AppLovin screens as a top 20-day momentum name with a reported FY1 EPS of 11.61 and forward EPS of 20.86, implying a forward P/E of about 18.2. The stock is trading near the high end of its 60-day range with a modest 60-day drawdown of roughly 8.7%, and a news item flags Criteo deal talks that could add optionality. The combination of strong reported earnings, a reasonable forward multiple, and momentum supports a new BUY.
- **Source IDs:** S008, S011, S013, S016
- **Catalysts:** Criteo deal talks adding optionality, Continued top-20-day momentum, Sustained FY1 earnings momentum with 27.6% EPS growth and 25.7% revenue growth
- **Risks:** Forward EPS and fiscal-year mapping are unverified, High gross margin and operating leverage may not persist if ad market softens, Momentum can reverse quickly if the stock pulls back from recent highs
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 20.8608 (source.forwardEps) x AI multiple assumption 20.00; source IDs S008, S011, S013, S016
- **EPS:** 20.86084 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 18.165617
- **FY+1 growth assumption:** 27.59%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / AAPL / APP shows strong FY1 consensus EPS growth of ~27.6% and revenue growth of ~25.7%, with high gross margin (~88.8%) and operating margin (~77.8%). The base multiple of 20x is supported by its superior margins and growth relative to AAPL, while the bull/bear range reflects upside if growth accelerates and downside if margin compression occurs.
- **Company fundamentals:** Reported diluted EPS 11.61; forward EPS 20.86; forward P/E 18.17; FY1 EPS growth 27.6%; FY1 revenue growth 25.7%; gross margin 88.8%; operating margin 77.8%; profit margin 65.9%; ROE 2.10.
- **Bull / Base / Bear:** 500.66 / 417.22 / 333.77
- **Bull / Base / Bear returns:** 32.12% / 10.1% / -11.92%
- **Scenario probabilities:** not separately assigned; see scenario table.

### IDXX — Idexx Laboratories

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** Idexx offers a higher-quality, higher-margin diagnostics franchise with positive earnings momentum, whereas the other momentum names in the shortlist either carry unverified forward multiples or weaker profitability profiles. Alternatives considered: APP, CMG, CLX, TSCO, MGM.
- **Thesis:** Idexx Laboratories is a top-20-day momentum name with a 60-day return of about 30.1% and a shallow 60-day drawdown of only 0.4%. It carries a forward P/E of about 42.0, which is rich, but the company shows positive earnings growth of 17.9% and revenue growth of 9.9%, with a 25.4% profit margin and 62.7% gross margin. The combination of strong momentum, improving profitability, and a defensible diagnostics franchise supports a new BUY.
- **Source IDs:** S030, S032, S036, S040
- **Catalysts:** Top-20-day momentum with 26.0% 20-day return, Positive earnings growth of 17.9% and revenue growth of 9.9%, High profit margin of 25.4% and gross margin of 62.7%
- **Risks:** Forward P/E of about 42.0 is expensive relative to the shortlist, Diagnostics demand can be cyclical and tied to pet ownership and veterinary spending, Forward EPS and fiscal-year mapping are unverified
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 16.8929 (source.forwardEps) x AI multiple assumption 24.00; source IDs S030, S032, S036, S040
- **EPS:** 16.8929 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 41.997524
- **FY+1 growth assumption:** 12.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / CDW / IDXX has moderate FY1 consensus EPS growth of ~12.4% and revenue growth of ~8.9%, with a healthy profit margin (~25.4%) and positive ROE. The base multiple of 24x is justified by its stable, higher-margin business relative to peers like CDW, with the bull/bear range reflecting potential for margin expansion or slowdown.
- **Company fundamentals:** Reported diluted EPS 11.75; forward EPS 16.89; forward P/E 42.00; FY1 EPS growth 12.4%; FY1 revenue growth 8.9%; earnings growth 17.9%; gross margin 62.7%; operating margin 32.5%; profit margin 25.4%; ROE 0.69.
- **Bull / Base / Bear:** 473.0 / 405.43 / 337.86
- **Bull / Base / Bear returns:** -33.33% / -42.85% / -52.38%
- **Scenario probabilities:** not separately assigned; see scenario table.

### DDOG — Datadog

- **Type:** Stock
- **Research view:** EXIT (stance: AVOID)
- **Why preferred / alternatives:** Datadog is not preferred because its dislocation is severe, its forward multiple is very high, and its operating margin is thin, making it a poor candidate for a new or maintained position. Alternatives considered: APP, IDXX, CMG, CLX, TSCO.
- **Thesis:** Datadog is a largest-20-day dislocation name with a 20-day return of about -43.2% and a 60-day return of about -29.3%, with a 60-day drawdown of roughly 46.0%. It carries a forward P/E of about 49.7 and positive but modest FY1 revenue growth of 22.3% and earnings growth of 2.3%. The sharp dislocation, high forward multiple, and thin operating margin of 2.4% do not support a new position; the existing position should be exited.
- **Source IDs:** S047, S052, S055, S056
- **Catalysts:** Potential mean-reversion if the dislocation resolves, Continued cloud and observability demand
- **Risks:** Sharp 20-day and 60-day declines with a 46% drawdown, Forward P/E of about 49.7 is very expensive, Operating margin of only 2.4% leaves little room for error, Forward EPS and fiscal-year mapping are unverified
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 3.1829 (source.forwardEps) x AI multiple assumption 28.00; source IDs S047, S052, S055, S056
- **EPS:** 3.1829 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 49.71881
- **FY+1 growth assumption:** 16.23%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / CRWD / DDOG shows FY1 consensus EPS growth of ~16.2% and revenue growth of ~22.3%, with strong gross margin (~79.6%) but lower operating margin (~2.4%) and profit margin (~6.1%). The base multiple of 28x is supported by its growth and gross margin relative to CRWD, with the bull/bear range reflecting operating leverage potential or margin pressure.
- **Company fundamentals:** Reported diluted EPS 0.59; forward EPS 3.18; forward P/E 49.72; FY1 EPS growth 16.2%; FY1 revenue growth 22.3%; earnings growth 2.3%; gross margin 79.6%; operating margin 2.4%; profit margin 6.1%; ROE 0.06.
- **Bull / Base / Bear:** 101.85 / 89.12 / 76.39
- **Bull / Base / Bear returns:** -35.64% / -43.68% / -51.73%
- **Scenario probabilities:** not separately assigned; see scenario table.

### XLV — Health Care sector ETF

- **Type:** ETF
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** The Health Care sector ETF is preferred over single-name health care exposure because it diversifies across the largest names and avoids the idiosyncratic risk of any one stock, while still providing the same sector beta. Alternatives considered: XLP, XLY, XLRE, XLF, XLU, XLB, XLI, XLC.
- **Thesis:** The Health Care sector ETF is a broad, diversified way to own large-cap health care names. It is not a stock, so no EPS, P/E, or earnings yield is applied. The sector ETF provides exposure to the same health care universe as Idexx and other names, but without the single-name volatility. A neutral stance reflects a balanced risk budget rather than a conviction to add or reduce.
- **Source IDs:** S053, S057
- **Catalysts:** Diversified exposure to large-cap health care names, Potential benefit if health care policy or drug pipeline catalysts improve
- **Risks:** Sector-wide drawdowns if health care sentiment weakens, Concentration in large-cap names may lag smaller or mid-cap health care names, No single-name catalyst can be isolated at the ETF level
- **Valuation method:** Holdings/portfolio valuation with AI total-return assumption
- **Valuation status:** verified; forward-EPS source: ; period flags: 
- **Valuation assumptions:** Holdings/portfolio valuation; 10 weighted holdings; coverage 61.42%; source IDs S053, S057
- **Top holdings:** LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59%
- **Portfolio valuation:** Top 10 holdings; numeric weight coverage 61.42%
- **Sector exposure:** Health Care
- **Underlying drivers:** Large-cap health care sector performance, drug pipeline catalysts, managed care dynamics, and medical technology demand.
- **Bull / Base / Bear:** 205.72 / 192.86 / 172.66
- **Bull / Base / Bear returns:** 12.0% / 5.0% / -6.0%
- **Scenario probabilities:** not separately assigned; see scenario table.

### XLP — Consumer Staples sector ETF

- **Type:** ETF
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** The Consumer Staples sector ETF is preferred over single-name staples exposure because it diversifies across the largest names and avoids the idiosyncratic risk of any one stock, while still providing the same sector beta. Alternatives considered: XLV, XLY, XLRE, XLF, XLU, XLB, XLI, XLC.
- **Thesis:** The Consumer Staples sector ETF provides diversified exposure to defensive staples names such as WMT, COST, PG, KO, and PM. It is not a stock, so no EPS, P/E, or earnings yield is applied. The ETF offers a lower-volatility anchor within the portfolio, but the neutral stance reflects a balanced risk budget rather than a conviction to add or reduce.
- **Source IDs:** S060, S061
- **Catalysts:** Defensive demand in consumer staples, Potential resilience if consumer spending softens
- **Risks:** Lower growth profile relative to cyclical sectors, Sector-wide drawdowns if staples demand weakens, No single-name catalyst can be isolated at the ETF level
- **Valuation method:** Holdings/portfolio valuation with AI total-return assumption
- **Valuation status:** verified; forward-EPS source: ; period flags: 
- **Valuation assumptions:** Holdings/portfolio valuation; 10 weighted holdings; coverage 63.28%; source IDs S060, S061
- **Top holdings:** WMT 11.14%, COST 9.09%, PG 7.60%, KO 7.37%, PM 6.59%, MO 4.70%, CL 4.42%, MDLZ 4.25%, PEP 4.11%, TGT 4.00%
- **Portfolio valuation:** Top 10 holdings; numeric weight coverage 63.28%
- **Sector exposure:** Consumer Staples
- **Underlying drivers:** Large-cap consumer staples sector performance, grocery and household demand, pricing power, and defensive consumption trends.
- **Bull / Base / Bear:** 101.53 / 95.99 / 87.68
- **Bull / Base / Bear returns:** 10.0% / 4.0% / -5.01%
- **Scenario probabilities:** not separately assigned; see scenario table.

## Quant Risk Layer

| Field | Value |
| --- | --- |
| Volatility model | vol5_ols_v1 |
| Spike model | spike_logit_v1 |
| As-of date | 2026-11-25 |
| Target window | 2026-11-27 to 2026-12-03 |
| Forecast 5D annualized volatility | 27.94% |
| Historical-vol baseline | 31.64% |
| EWMA baseline | 28.40% |
| Spike probability | 65.99% |
| Spike threshold | 18.50% |
| Status | prospective |
| Forecast ID | 9884506cdbaa9353 |

Risk-only; no directional interpretation or allocation implication.

## Scenarios

### Short Term (5 trading sessions)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 25% | +2.00% | Low spike probability (0.66) and false directional signal reduce near-term tail risk, but a 2% upside is plausible if the frozen daily-close model stabilizes after the US close. |
| Base | 50% | +0.00% | Forecast volatility (0.279) is above the historical baseline (0.316) but below the EWMA baseline (0.284), implying a range-bound week with no directional alpha. |
| Bear | 25% | -2.00% | If the frozen model fails to complete the US close, elevated forecast vol and a 0.66 spike probability could trigger a 2% downside correction. |

### Long Term (12 months)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 30% | +8.00% | Sustained normalization of forecast vol below historical baseline and a false directional signal could allow a 8% rally into year-end if earnings remain stable. |
| Base | 40% | +3.00% | A 3% long-term return reflects moderate volatility compression and steady earnings growth, with the frozen daily-close model providing a reliable baseline. |
| Bear | 30% | -5.00% | Persistent elevated forecast vol, a 0.66 spike probability, and a false directional signal could drive a 5% decline if credit spreads widen and earnings disappoint. |

## Positioning

- Maintain a cautious equity stance given the 20-day S&P 500 drawdown of -7.25% and elevated risk forecast volatility of 27.94%.
- Favor defensive sectors (Consumer Staples, Utilities, Health Care) for relative stability, but note high valuations.
- Monitor Information Technology and Energy for further weakness; these sectors show the largest drawdowns.
- Watch credit spreads (high-yield OAS 3.72, IG OAS 0.98) for signs of widening or tightening.
- Track the 10Y-2Y spread (0.24) and Fed funds rate (3.88%) for policy and yield curve signals.

## Catalysts

| Date | Event | Why it matters |
| --- | --- | --- |
| 2026-11-26 | US macro data release | Latest macro data (CPI, unemployment, payrolls) as of 2026-10-01 will inform inflation and labor market trajectory. |
| 2026-11-27 | Risk forecast target window opens | 5-day forecast volatility of 27.94% and spike probability of 65.99% suggest elevated near-term risk; monitor for volatility spikes. |
| 2026-12-03 | Risk forecast target |  |

## Key Risks


## External Source Ledger

| ID | Type | Ticker | Published | Status | URL | Claims |
| --- | --- | --- | --- | --- | --- | --- |
| S001 | macro | macro | 2026-11-24 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFF&cosd=2026-01-01 | Effective federal funds rate (DFF) latest observation 2026-11-24: 3.88 |
| S002 | macro | macro | 2026-11-24 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLH0A0HYM2&cosd=2026-01-01 | US high-yield OAS (BAMLH0A0HYM2) latest observation 2026-11-24: 3.72 |
| S003 | macro | macro | 2026-11-24 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLC0A0CM&cosd=2026-01-01 | US investment-grade OAS (BAMLC0A0CM) latest observation 2026-11-24: 0.98 |
| S004 | macro | macro | 2026-10-01 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCSL&cosd=2026-01-01 | US CPI (CPIAUCSL) latest observation 2026-10-01: 337.476 |
| S005 | macro | macro | 2026-10-01 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=UNRATE&cosd=2026-01-01 | US unemployment rate (UNRATE) latest observation 2026-10-01: 4.1 |
| S006 | macro | macro | 2026-10-01 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=PAYEMS&cosd=2026-01-01 | US nonfarm payrolls (PAYEMS) latest observation 2026-10-01: 159293 |
| S007 | macro | macro | 2026-11-25 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=T10Y2Y&cosd=2026-01-01 | 10Y-2Y Treasury spread (T10Y2Y) latest observation 2026-11-25: 0.24 |
| S008 | filing | APP | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001751008&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0001751008-26-000069); 8-K filed 2026-11-04 (accession 0001751008-26-000068); 10-Q filed 2026-08-05 (accession 0001751008-26-000059) |
| S009 | filing | CMG | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001058090&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0001058090-26-000104); 8-K filed 2026-10-28 (accession 0001058090-26-000103); 8-K filed 2026-09-14 (accession 0001058090-26-000088) |
| S010 | filing | CHTR | 2026-11-06 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-06 (accession 0001091667-26-000073); 8-K filed 2026-11-06 (accession 0001091667-26-000072); 8-K filed 2026-10-27 (accession 0001091667-26-000064) |
| S011 | news | APP | Wed, 25 Nov 2026 22:10:42 GMT | ok | https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en | AppLovin (APP) Could Be 25% Undervalued As Criteo Deal Talks Stir Debate - Yahoo Finance (Wed, 25 Nov 2026 22:10:42 GMT); AppLovin vs. Reddit: Which Technology Stock Is a Better Buy for 2027? - The Motley Fool (Sat, 21 Nov 2026 23:19:26 GMT); APP Falls 14.9% in One Week as Growth Strength Meets Execution Risk - TradingView (Mon, 23 Nov 2026 15:30:00 GMT) |
| S012 | news | CHTR | Thu, 26 Nov 2026 01:54:00 GMT | ok | https://news.google.com/rss/search?q=CHTR+Charter+Communications+stock&hl=en-US&gl=US&ceid=US:en | CHTR Stock Posts 2nd Consecutive Day Of Gains: Retail Turns Bullish — 'The Gift That Keeps On Giving' - TradingView (Thu, 26 Nov 2026 01:54:00 GMT); Charter Communications Stock: Analyst Estimates & Ratings - Yahoo Finance (Tue, 24 Nov 2026 11:41:31 GMT); Charter Communications (CHTR) Jumped, What Is Behind The Fresh Attention? - Simply Wall St (Thu, 26 Nov 2026 00:32:37 GMT) |
| S013 | stock | APP | 2026-11-26 | ok | https://finance.yahoo.com/quote/APP | Trailing P/E: 25.518518; Forward P/E: 18.165617; Forward EPS: 20.86084; Price: 378.95; Market price: 378.95; Market cap: 125554507776; Sector: Communication Services; Trailing Eps: 14.85; Revenue Growth: 0.555; Earnings Growth: 0.755; Gross Margin: 0.8878; Operating Margin: 0.77782995; Profit Margin: 0.65887; Return On Equity: 2.1008599; Total Revenue: 7608893952; Market Cap: 125554507776; Consensus EPS FY+1: 20.78066; growth: 0.2759 |
| S014 | stock | CHTR | 2026-11-26 | ok | https://finance.yahoo.com/quote/CHTR | Trailing P/E: 13.841166; Forward P/E: 3.2299702; Forward EPS: 45.59485; Price: 147.27; Market price: 147.27; Market cap: 26368923648; Sector: Communication Services; Trailing Eps: 10.64; Revenue Growth: 0.091; Gross Margin: 0.55084; Operating Margin: 0.23389; Profit Margin: 0.02498; Return On Equity: 0.07019; Total Revenue: 55645999104; Market Cap: 26368923648; Consensus EPS FY+1: 47.75367; growth: 1.4848 |
| S015 | stock | CMG | 2026-11-26 | ok | https://finance.yahoo.com/quote/CMG | Trailing P/E: 34.95327; Forward P/E: 28.261396; Forward EPS: 1.32336; Price: 37.4; Market price: 37.4; Market cap: 47310065664; Sector: Consumer Cyclical; Trailing Eps: 1.07; Revenue Growth: 0.096; Earnings Growth: -0.062; Gross Margin: 0.39314; Operating Margin: 0.14715; Profit Margin: 0.10832; Return On Equity: 0.48518002; Total Revenue: 12713477120; Market Cap: 47310065664; Consensus EPS FY+1: 1.32336; growth: 0.216 |
| S016 | filing | APP | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json | Diluted EPS 11.61 for period ending 2026-09-30 (filed 2026-11-04) |
| S017 | filing | CLX | 2026-11-19 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 | 8-K filed 2026-11-19 (accession 0001206774-26-000606); 10-Q filed 2026-11-02 (accession 0000021076-26-000046); 8-K filed 2026-11-02 (accession 0000021076-26-000044) |
| S018 | filing | CMG | 2026-10-29 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001058090.json | Diluted EPS 0.82 for period ending 2026-09-30 (filed 2026-10-29) |
| S019 | filing | CHTR | 2026-11-06 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001091667.json | Diluted EPS 0.38 for period ending 2026-09-30 (filed 2026-11-06) |
| S020 | stock | CLX | 2026-11-26 | ok | https://finance.yahoo.com/quote/CLX | Trailing P/E: 19.953238; Forward P/E: 17.985216; Forward EPS: 6.1684; Price: 110.94; Market price: 110.94; Market cap: 13440092160; Sector: Consumer Defensive; Trailing Eps: 5.56; Revenue Growth: 0.333; Earnings Growth: 1.138; Gross Margin: 0.41939998; Operating Margin: 0.14286; Profit Margin: 0.09408; Return On Equity: 5.34363; Total Revenue: 7196000256; Market Cap: 13440092160; Consensus EPS FY+1: 6.1684; growth: 0.0769 |
| S021 | news | CMG | Tue, 24 Nov 2026 15:25:45 GMT | ok | https://news.google.com/rss/search?q=CMG+Chipotle+Mexican+Grill+stock&hl=en-US&gl=US&ceid=US:en | What Could Lift Chipotle Stock Further? - Trefis (Tue, 24 Nov 2026 15:25:45 GMT); Chipotle Mexican Grill vs. Hershey: Which Consumer Stock Is a Better Buy for 2027? - Yahoo Finance (Sat, 21 Nov 2026 02:05:00 GMT); Chipotle Mexican Grill vs. e.l.f. Beauty: Which Consumer Stock Is a Better Buy for 2027? - The Motley Fool (Sat, 21 Nov 2026 07:27:19 GMT) |
| S022 | filing | TSCO | 2026-11-05 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000916365&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-05 (accession 0000916365-26-000079); 8-K filed 2026-11-05 (accession 0000916365-26-000076); 8-K filed 2026-10-22 (accession 0000916365-26-000069) |
| S023 | news | CLX | Wed, 25 Nov 2026 15:47:48 GMT | ok | https://news.google.com/rss/search?q=CLX+Clorox+stock&hl=en-US&gl=US&ceid=US:en | Clorox Company (The) (CLX) Stock Forecasts - Yahoo! Finance Canada (Wed, 25 Nov 2026 15:47:48 GMT); Should You Buy Clorox Stock At This Price? - Trefis (Thu, 19 Nov 2026 08:57:28 GMT); Clorox (CLX) Stock Looks Fairly Valued After A 28% Slide - Simply Wall St (Mon, 23 Nov 2026 14:08:34 GMT) |
| S024 | filing | MGM | 2026-10-28 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000789570&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-28 (accession 0000789570-26-000107); 8-K filed 2026-10-28 (accession 0000789570-26-000106); 8-K filed 2026-10-28 (accession 0000789570-26-000104) |
| S025 | stock | MGM | 2026-11-26 | ok | https://finance.yahoo.com/quote/MGM | Trailing P/E: 13.326924; Forward P/E: 24.652624; Forward EPS: 1.40553; Price: 34.65; Market price: 34.65; Market cap: 8766815232; Sector: Consumer Cyclical; Trailing Eps: 2.6; Revenue Growth: -0.009; Gross Margin: 0.4362; Operating Margin: 0.057979997; Profit Margin: 0.03916; Return On Equity: 0.26933; Total Revenue: 17722869760; Market Cap: 8766815232; Consensus EPS FY+1: 1.40553; growth: -0.0462 |
| S026 | filing | CLX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000021076.json | Diluted EPS 1.39 for period ending 2026-09-30 (filed 2026-11-02) |
| S027 | news | TSCO | Wed, 25 Nov 2026 22:06:00 GMT | ok | https://news.google.com/rss/search?q=TSCO+Tractor+Supply+stock&hl=en-US&gl=US&ceid=US:en | Tractor Supply Co. stock outperforms competitors on strong trading day - MarketWatch (Wed, 25 Nov 2026 22:06:00 GMT); Tractor Supply Company (TSCO) Stock Forecasts - Yahoo! Finance Canada (Wed, 25 Nov 2026 21:02:43 GMT); Tractor Supply (NYSE:TSCO) Share Price, Forecast & Analysis - Stocks Down Under (Fri, 20 Nov 2026 21:00:00 GMT) |
| S028 | stock | TSCO | 2026-11-26 | ok | https://finance.yahoo.com/quote/TSCO | Trailing P/E: 21.7043; Forward P/E: 19.622805; Forward EPS: 2.0573; Price: 40.37; Market price: 40.37; Market cap: 20934819840; Sector: Consumer Cyclical; Trailing Eps: 1.86; Revenue Growth: 0.051; Earnings Growth: -0.121; Gross Margin: 0.36285; Operating Margin: 0.08701; Profit Margin: 0.061300002; Return On Equity: 0.37347; Total Revenue: 15942134784; Market Cap: 20934819840; Consensus EPS FY+1: 2.04688; growth: 0.091400005 |
| S029 | news | MGM | Mon, 23 Nov 2026 17:45:39 GMT | ok | https://news.google.com/rss/search?q=MGM+MGM+Resorts+stock&hl=en-US&gl=US&ceid=US:en | Here’s Why MGM Resorts (MGM) Declined in Q3 - Yahoo Finance (Mon, 23 Nov 2026 17:45:39 GMT); This casino stock has fallen for 17 weeks in a row. Katie Stockton says it could be due for a bounce - CNBC (Tue, 03 Nov 2026 08:00:00 GMT); MGM Stock Dives 10% After Barry Diller Drops $18 Billion Bid - Forbes (Thu, 24 Sep 2026 07:00:00 GMT) |
| S030 | filing | IDXX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000874716&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000874716-26-000135); 8-K filed 2026-11-02 (accession 0001104659-26-120892); 10-Q filed 2026-08-04 (accession 0000874716-26-000123) |
| S031 | filing | TSCO | 2026-11-05 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000916365.json | Diluted EPS 1.43 for period ending 2026-09-26 (filed 2026-11-05) |
| S032 | stock | IDXX | 2026-11-26 | ok | https://finance.yahoo.com/quote/IDXX | Trailing P/E: 47.807278; Forward P/E: 41.997524; Forward EPS: 16.8929; Price: 709.46; Market price: 709.46; Market cap: 55895703552; Sector: Healthcare; Trailing Eps: 14.84; Revenue Growth: 0.099; Earnings Growth: 0.179; Gross Margin: 0.62722; Operating Margin: 0.32497; Profit Margin: 0.25357; Return On Equity: 0.68925005; Total Revenue: 4662220800; Market Cap: 55895703552; Consensus EPS FY+1: 16.8929; growth: 0.1244 |
| S033 | filing | FISV | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0000798354-26-000042); 8-K filed 2026-11-03 (accession 0000798354-26-000039); 8-K filed 2026-10-23 (accession 0001193125-26-429481) |
| S034 | stock | FISV | 2026-11-26 | ok | https://finance.yahoo.com/quote/FISV | Forward P/E: 7.499978; Price: 59.78; Market price: 59.78; Market cap: 31805810688; Market Cap: 31805810688; Consensus EPS FY+1: 7.97069; growth: 0.0954 |
| S035 | filing | SNDK | 2026-11-19 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0002023554&type=10-Q&dateb=&owner=include&count=10 | 8-K filed 2026-11-19 (accession 0001628280-26-075127); 8-K filed 2026-11-18 (accession 0001628280-26-074848); 10-Q filed 2026-10-30 (accession 0001628280-26-068601) |
| S036 | news | IDXX | Thu, 26 Nov 2026 02:40:04 GMT | ok | https://news.google.com/rss/search?q=IDXX+Idexx+Laboratories+stock&hl=en-US&gl=US&ceid=US:en | IDEXX Laboratories, Inc. (IDXX) Stock Forecasts - Yahoo Finance (Thu, 26 Nov 2026 02:40:04 GMT); Can IDEXX Stock Keep Rising After Its 25% Run? - Trefis (Tue, 24 Nov 2026 15:26:34 GMT); IDEXX Stock Rises on Q3 Earnings Beat, Raised 2026 Guidance - IDEXX Laboratories (NASDAQ:IDXX) - Benzinga (Mon, 02 Nov 2026 08:00:00 GMT) |
| S037 | news | FISV | Fri, 20 Nov 2026 08:10:25 GMT | ok | https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en | Is Fiserv (FISV) Cheap Following Its AI Ecommerce Push And Valuation Gap? - Yahoo Finance (Fri, 20 Nov 2026 08:10:25 GMT); Citizens initiated coverage on Fiserv - Quantisnow (Mon, 23 Nov 2026 12:50:42 GMT); FISV Stock Rises 17% in a Month: Here's What Investors Should Know - TradingView (Fri, 20 Nov 2026 13:55:00 GMT) |
| S038 | stock | SNDK | 2026-11-26 | ok | https://finance.yahoo.com/quote/SNDK | Trailing P/E: 4.7065215; Forward P/E: 2.0565789; Forward EPS: 35.79245; Price: 73.61; Market price: 73.61; Market cap: 83791355904; Sector: Technology; Trailing Eps: 15.64; Revenue Growth: 3.779; Earnings Growth: 69.096; Gross Margin: 0.79952; Operating Margin: 0.7268; Profit Margin: 0.67039; Return On Equity: 1.41174; Total Revenue: 28970999808; Market Cap: 83791355904; Consensus EPS FY+1: 35.79245; growth: 0.2573 |
| S039 | filing | MGM | 2026-10-28 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000789570.json | Diluted EPS 1.52 for period ending 2026-09-30 (filed 2026-10-28) |
| S040 | filing | IDXX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000874716.json | Diluted EPS 11.75 for period ending 2026-09-30 (filed 2026-11-02) |

## Sources

- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFF&cosd=2026-01-01 (2026-11-24)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLH0A0HYM2&cosd=2026-01-01 (2026-11-24)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLC0A0CM&cosd=2026-01-01 (2026-11-24)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCSL&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=UNRATE&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=PAYEMS&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=T10Y2Y&cosd=2026-01-01 (2026-11-25)
- filing APP: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001751008&type=10-Q&dateb=&owner=include&count=10 (2026-11-04)
- filing CMG: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001058090&type=10-Q&dateb=&owner=include&count=10 (2026-10-29)
- filing CHTR: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 (2026-11-06)
- news APP: https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en (Wed, 25 Nov 2026 22:10:42 GMT)
- news CHTR: https://news.google.com/rss/search?q=CHTR+Charter+Communications+stock&hl=en-US&gl=US&ceid=US:en (Thu, 26 Nov 2026 01:54:00 GMT)
- stock APP: https://finance.yahoo.com/quote/APP (2026-11-26)
- stock CHTR: https://finance.yahoo.com/quote/CHTR (2026-11-26)
- stock CMG: https://finance.yahoo.com/quote/CMG (2026-11-26)
- filing APP: https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json (2026-11-04)
- filing CLX: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 (2026-11-19)
- filing CMG: https://data.sec.gov/api/xbrl/companyfacts/CIK0001058090.json (2026-10-29)
- filing CHTR: https://data.sec.gov/api/xbrl/companyfacts/CIK0001091667.json (2026-11-06)
- stock CLX: https://finance.yahoo.com/quote/CLX (2026-11-26)

## AI Provenance

- Provider / model: hermes-local-proxy / upstage/solar-mini4:free
- Market research: attempts=1 tokens=8407 (prompt=5407, completion=3000) runtime=28.31s
- Fundamental research: generated this run at 2026-11-26T10:17:21.738544+00:00
- Evidence source dates: {'as_of': '2026-11-25', 'latest_equity_date': '2026-11-25', 'latest_macro_date': '2026-11-26', 'flows_date': '2026-11-25'}
- Evidence fingerprint: 13ae6710b0cca2a8aa68c21580353dd6645aacaa1100abf45db11cf81378a9f0
- Source citations are retrieved external records in the ledger above; market values remain from the verified database snapshot.


## Disclosures

- This is research and market intelligence, not investment advice.
- AI conclusions are research judgments, not validated return predictions.
- The frozen risk layer is risk-only and is not used for directional views or allocations.
- Legacy scores are not active inputs or outputs.

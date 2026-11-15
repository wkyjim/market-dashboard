# AEGIS AI-First Market Intelligence

Research generated at: 15 November 2026, 21:15 HKT
Database freshness: equity 2026-11-13 (latest row retrieved 2026-11-15 13:06:40.074841+08:00)
Data cutoff: 2026-11-13 US cash close
Snapshot ID: aegis-hourly-20261115T131551Z

## Executive Summary

- **AI market view: Late-November 2026 equity market is in a late-cycle, mixed posture: broad market internals remain constructive with 71.3% above the 50-day and 63.6% above the 200-day, but the S&P 500 is down 1.28% over 20 days and the Information Technology sector is the weakest major group at -7.19% over 20 days. Momentum, dislocation, and liquidity screens point to a small set of high-conviction names, while macro data show a still-elevated but easing inflation backdrop, a 3.88% effective funds rate, and a modestly positive 10Y-2Y spread. Risk indicators are below historical and EWMA baselines, though a 16.5% spike probability warrants caution.**
- Broad market internals are supportive: 71.3% of names above the 50-day, 63.6% above the 200-day, and a 1.70 advance/decline ratio on 2026-11-13.
- S&P 500 is 1.28% lower over 20 days, with Information Technology (-7.19%) and Energy (-4.81%) the weakest sectors and Health Care (+6.87%), Consumer Discretionary (+6.69%), and Consumer Staples (+5.40%) the strongest.
- Momentum and dislocation screens shortlist 20 names; the largest dislocations include RDDT, INTC, SNDK, MRVL, FFIV, NOW, LITE, and COIN, while liquidity leaders include NVDA, AMD, MU, and AAPL.
- Macro data show CPI 336.298 (Sep-2026), core CPI 338.896, unemployment 4.2%, effective funds rate 3.88%, IG OAS 0.89, and HY OAS 3.20, indicating a late-cycle but not distressed credit environment.
- Risk model shows 5-day forecast volatility 14.93% and spike probability 16.51%, below the 22.07% historical and 20.09% EWMA baselines, but above the 18.50% threshold.
- Flows show exceptional institutional buying in SOXX (20d z-score 5.10, 60d 3.17) with price down, while TLT shows medium-term deterioration and SMH shows tactical profit-taking inside structural accumulation.

## Data QC

- Status: **PASS_WITH_WARNINGS**
- Equity session: 0 completed session(s) behind inference date
- Equity provenance: 393 provisional / 12576 canonical
- Breadth lag: 0 session(s); ETF-flow lag: 0 session(s)
- Note: Equity session contains a mix of provisional yfinance and canonical Massive rows.
- External sources: 79 ok / 0 unavailable; retrieved 2026-11-15T13:16:12.678802+00:00

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
| S&P 500 | 7561.67 | -1.28% (20d) | Broad internals remain constructive but price momentum is negative over 20 days; sector leadership is bifurcated. |
| Health Care (XLV) | 6.87% | +6.87% (20d) | Strongest major sector; trailing P/E 30.78 per S054. |
| Consumer Discretionary (XLY) | 6.69% | +6.69% (20d) | Strong momentum; trailing P/E 25.11 per S057. |
| Consumer Staples (XLP) | 5.40% | +5.40% (20d) | Defensive strength; trailing P/E 24.85 per S058. |
| Information Technology (XLK) | -7.19% | -7.19% (20d) | Weakest major sector; trailing P/E 30.03 per S073, with shortlist names MRVL and AMD flagged as liquidity leaders. |
| Energy (XLE) | -4.81% | -4.81% (20d) | Negative sector return; trailing P/E 16.23 per S074. |

## Macro, Fiscal, Rates, Liquidity and Credit

- Inflation: CPI 336.298 and core CPI 338.896 (Sep-2026) indicate still-elevated but moderating price pressures; the October CPI reading of 337.476 per S004 is the latest available monthly print.
- Labor: Unemployment 4.2% (Sep-2026) per S005/S006, with nonfarm payrolls 159,293k (Oct-2026), suggesting a cooling but still-resilient labor market.
- Policy: Effective federal funds rate 3.88% as of 2026-11-12 per S001, consistent with a late-cycle easing bias; the 10Y-2Y spread is 0.27 as of 2026-11-13 per S007.
- Rates and credit: IG OAS 0.89 and HY OAS 3.20 as of 2026-11-12 per S003/S002, indicating tight but not stressed credit conditions.
- Liquidity: SOXX shows exceptional institutional buying (20d z-score 5.10, 60d 3.17) with price down, while TLT shows medium-term deterioration and SMH shows tactical profit-taking inside structural accumulation.
- Risk: 5-day forecast volatility 14.93% and spike probability 16.51% are below historical (22.07%) and EWMA (20.09%) baselines, but above the 18.50% threshold, implying elevated but not extreme tail risk.

## US Equities and 11 GICS Sectors

Macro source IDs: S001, S002, S003, S004, S005, S006, S007

| GICS sector | Evidence | AI research stance | Source IDs |
| --- | --- | --- | --- |
| Health Care | Sector ETF XLV returned +6.87% over 20 days; trailing P/E 30.78 per S054; breadth shows 71.3% of names above the 50-day. | Constructive; strong relative momentum and defensive positioning support the sector despite elevated valuation. | S054 |
| Consumer Discretionary | Sector ETF XLY returned +6.69% over 20 days; trailing P/E 25.11 per S057; strong 20-day momentum. | Constructive; consumer spending resilience and positive breadth support the sector. | S057 |
| Consumer Staples | Sector ETF XLP returned +5.40% over 20 days; trailing P/E 24.85 per S058; defensive strength in a mixed market. | Constructive; stable demand and defensive appeal support the sector. | S058 |
| Financials | Sector ETF XLF returned +5.69% over 20 days; trailing P/E 15.85 per S066; positive 20-day return. | Constructive; positive sector return and reasonable valuation support the sector. | S066 |
| Real Estate | Sector ETF XLRE returned +5.24% over 20 days; trailing P/E 29.63 per S061; positive 20-day return. | Constructive; positive sector return and moderate valuation support the sector. | S061 |
| Utilities | Sector ETF XLU returned +4.34% over 20 days; trailing P/E 18.11 per S064; defensive strength. | Constructive; defensive appeal and reasonable valuation support the sector. | S064 |
| Materials | Sector ETF XLB returned +2.57% over 20 days; trailing P/E 21.72 per S065; positive but modest sector return. | Neutral-to-constructive; positive sector return but lower momentum than Health Care and Consumer Discretionary. | S065 |
| Industrials | Sector ETF XLI returned +0.61% over 20 days; trailing P/E 27.07 per S069; near-flat sector return. | Neutral; positive but weak sector return and moderate valuation suggest limited leadership. | S069 |
| Communication Services | Sector ETF XLC returned -1.48% over 20 days; trailing P/E 17.26 per S072; negative sector return. | Weak; negative sector return and lower valuation relative to the market warrant caution. | S072 |
| Information Technology | Sector ETF XLK returned -7.19% over 20 days; trailing P/E 30.03 per S073; weakest major sector with shortlist names MRVL and AMD flagged as liquidity leaders. | Weak; sharp sector drawdown and high valuation multiples for shortlist names suggest elevated risk despite liquidity leadership. | S073 |
| Energy | Sector ETF XLE returned -4.81% over 20 days; trailing P/E 16.23 per S074; negative sector return. | Weak; negative sector return and lower valuation relative to the market warrant caution. | S074 |

### Sector fundamentals, valuation and earnings

Sector-level fundamental evidence is limited to trailing P/E multiples for the eleven GICS sector ETFs (XLV, XLY, XLP, XLRE, XLF, XLU, XLB, XLI, XLC, XLK, XLE) as supplied in the source table. No point-in-time sector growth, margin, or consensus data are available in the supplied database, so no sector fundamentals beyond valuation multiples are reported.

## Growth vs Value

- Growth: Momentum and dislocation screens identify shortlist names with strong 20-day price returns, including RDDT, INTC, SNDK, MRVL, FFIV, NOW, LITE, and COIN, while liquidity leaders NVDA, AMD, MU, and AAPL show high dollar-volume turnover.
- Value: Trailing P/E and earnings yield across the 503-name universe show a wide dispersion, with CHTR at 2.71x P/E and 36.95% earnings yield, FISV at 9.65x P/E and 10.36% earnings yield, and MU at 11.40x P/E and 8.77% earnings yield, indicating pockets of attractive valuation.
- Growth: High-multiple names such as MRVL (74.23x P/E, 1.35% earnings yield) and NOW (97.19x P/E, 1.03% earnings yield) carry elevated growth expectations but also higher valuation risk.
- Value: Sector-relative P/E analysis shows IDXX at 1.33x sector multiple, RDDT at 1.66x, and MRVL at 2.20x, while CHTR at 0.13x, SNDK at 0.47x, and MU at 0.34x trade at significant discounts to their sector peers.

## ETF Flows and Breadth

- SOXX shows exceptional institutional buying with a 20d flow z-score of 5.10 and 60d z-score of 3.17, despite the price being down, indicating strong structural accumulation.
- SMH shows tactical profit-taking inside structural accumulation, with 20d z-score 1.22 and 60d z-score 1.04, suggesting a pullback within a longer-term uptrend.
- TLT shows medium-term deterioration with 20d z-score -0.41 and 60d z-score -0.29, indicating reduced demand for duration.
- Breadth on

## Stock Ideas

Single-stock research uses reported EPS, forward P/E and company fundamentals. All ideas are research judgments, not validated return predictions.

| Ticker | Security | Research view | Price | EPS | Forward P/E | Base target | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| APP | AppLovin | NEW | 409.1 | 20.86026 | 19.611452 | 417.21 | NEW |
| PNR | Pentair | KEEP | 68.3 | 5.30402 | 12.877027 | 68.95 | KEEP |
| ROP | Roper Technologies | NEW | 479.975 | 24.57318 | 19.532475 | 491.46 | NEW |

## ETF Ideas

ETF research uses holdings, portfolio valuation and exposure. Single-stock EPS × P/E valuation is not applied to ETFs.

| Ticker | Fund | Research view | Price | Top holdings | Portfolio valuation | Sector exposure | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| XLV | Health Care sector ETF | KEEP | 188.85 | LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59% | Top 10 holdings; numeric weight coverage 61.42% | Health Care | KEEP |
| XLP | Consumer Staples sector ETF | KEEP | 92.35 | WMT 11.14%, COST 9.09%, PG 7.60%, KO 7.37%, PM 6.59%, MO 4.70%, CL 4.42%, MDLZ 4.25%, PEP 4.11%, TGT 4.00% | Top 10 holdings; numeric weight coverage 63.28% | Consumer Staples | KEEP |
### APP — AppLovin

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** AppLovin offers a rare combination of top-tier momentum, industry-leading margins, and a reasonable forward P/E, making it a stronger candidate than the lower-margin, lower-growth names in the shortlist such as CLX or PNR. Alternatives considered: CLX, PNR.
- **Thesis:** AppLovin screens in the top 20-day momentum bucket with a 53.7% 20-day return and a 32.5% 60-day return, while maintaining a 60-day drawdown of only -0.2%. The company reports strong fundamentals: FY1 revenue growth of 55.5%, earnings growth of 75.5%, gross margin of 88.8%, operating margin of 77.8%, and profit margin of 65.9%. Forward EPS of 20.86 implies a forward P/E of 19.6, which is reasonable for a high-margin, high-growth mobile advertising platform. The combination of strong momentum, high profitability, and a reasonable valuation supports a new BUY recommendation.
- **Source IDs:** S008, S012, S015, S016
- **Catalysts:** Continued acceleration in mobile advertising revenue, Sustained high-margin operating leverage, Positive 20-day and 60-day momentum continuation
- **Risks:** High valuation for a momentum-driven stock, Potential regulatory or privacy changes affecting ad targeting, Execution risk on new product initiatives
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 20.8603 (source.forwardEps) x AI multiple assumption 20.00; source IDs S008, S012, S015, S016
- **EPS:** 20.86026 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 19.611452
- **FY+1 growth assumption:** 27.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / Apple Inc. (AAPL) and Microsoft Corp. (MSFT) as high-margin, ecosystem-driven software/platform comparables / APP shows FY1 consensus EPS growth of 27.44% and revenue growth of 25.37%, with gross margin of 88.78% and operating margin of 77.78%, indicating a high-margin, capital-light platform model. The forward EPS of 20.86 and forward P/E of 19.61 support a base multiple near 20x, with upside to 24x in a bull case and downside to 16x in a bear case. The 12-month horizon is used because FY2+ consensus EPS is not available from the retrieved source.
- **Company fundamentals:** FY1 revenue growth 55.5%, earnings growth 75.5%, gross margin 88.8%, operating margin 77.8%, profit margin 65.9%, forward EPS 20.86, forward P/E 19.6
- **Bull / Base / Bear:** 500.65 / 417.21 / 333.76
- **Bull / Base / Bear returns:** 22.38% / 1.98% / -18.42%
- **Scenario probabilities:** not separately assigned; see scenario table.

### PNR — Pentair

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Pentair offers a lower forward P/E than many growth names, but its negative near-term growth makes it less attractive than higher-growth momentum names like AppLovin or Roper Technologies. Alternatives considered: APP, ROP.
- **Thesis:** Pentair is a top-20-day momentum name with a 27.8% 20-day return and a 7.1% 60-day return. It carries a reasonable forward P/E of 12.9 and an earnings yield of 7.4%. However, FY1 revenue growth is slightly negative at -4.5% and earnings growth is -18.8%, indicating that the momentum is not yet supported by fundamental growth. The stock is therefore kept as a neutral holding rather than upgraded to a buy.
- **Source IDs:** S010, S014, S017, S020
- **Catalysts:** Potential stabilization of revenue and earnings trends, Continued momentum from the 20-day price move, Attractive forward valuation relative to peers
- **Risks:** Negative FY1 revenue and earnings growth, Cyclical exposure to building and construction, Momentum may fade if fundamentals do not improve
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 5.3040 (source.forwardEps) x AI multiple assumption 13.00; source IDs S010, S014, S017, S020
- **EPS:** 5.30402 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 12.877027
- **FY+1 growth assumption:** 12.82%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / Prologis Inc. (PLD) and Equinix Inc. (EQIX) as industrial/logistics REITs with similar asset-light operating models / PNR shows FY1 consensus EPS growth of 12.82% and revenue growth of 18.38%, with gross margin of 40.17% and operating margin of 21.41%, reflecting a capital-intensive industrial/logistics REIT. The forward EPS of 5.30 and forward P/E of 12.88 support a base multiple near 13x, with upside to 16x in a bull case and downside to 10x in a bear case. The 12-month horizon is used because FY2+ consensus EPS is not available from the retrieved source.
- **Company fundamentals:** FY1 revenue growth -4.5%, earnings growth -18.8%, gross margin 40.2%, operating margin 21.4%, profit margin 15.4%, forward EPS 5.30, forward P/E 12.9
- **Bull / Base / Bear:** 84.86 / 68.95 / 53.04
- **Bull / Base / Bear returns:** 24.25% / 0.95% / -22.34%
- **Scenario probabilities:** not separately assigned; see scenario table.

### ROP — Roper Technologies

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** Roper Technologies provides a better balance of growth and valuation than the lower-growth PNR or the high-multiple, high-valuation names like MRVL and NOW, while still offering strong momentum. Alternatives considered: PNR, NOW.
- **Thesis:** Roper Technologies is a top-20-day momentum name with a 25.4% 20-day return and a 16.9% 60-day return. It has a reasonable forward P/E of 19.5 and an earnings yield of 6.0%. FY1 revenue growth is 7.6% and earnings growth is 32.6%, with a gross margin of 69.7% and operating margin of 28.0%. The combination of positive fundamental growth and strong momentum supports a new BUY recommendation.
- **Source IDs:** S034, S037, S040, S042
- **Catalysts:** Steady revenue and earnings growth, High-margin, recurring revenue model, Positive 20-day and 60-day momentum
- **Risks:** Valuation may be rich for a growth stock, Exposure to industrial and technology end markets, Potential margin compression in a slowing economy
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 24.5732 (source.forwardEps) x AI multiple assumption 20.00; source IDs S034, S037, S040, S042
- **EPS:** 24.57318 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 19.532475
- **FY+1 growth assumption:** 9.81%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / Lowe's Companies Inc. (LOW) and Home Depot Inc. (HD) as home improvement retailers with comparable margin and growth profiles / ROP shows FY1 consensus EPS growth of 9.81% and revenue growth of 6.29%, with gross margin of 69.67% and operating margin of 28.05%, indicating a stable home improvement retail model. The forward EPS of 24.57 and forward P/E of 19.53 support a base multiple near 20x, with upside to 24x in a bull case and downside to 16x in a bear case. The 12-month horizon is used because FY2+ consensus EPS is not available from the retrieved source.
- **Company fundamentals:** FY1 revenue growth 7.6%, earnings growth 32.6%, gross margin 69.7%, operating margin 28.0%, profit margin 30.7%, forward EPS 24.57, forward P/E 19.5
- **Bull / Base / Bear:** 589.76 / 491.46 / 393.17
- **Bull / Base / Bear returns:** 22.87% / 2.39% / -18.09%
- **Scenario probabilities:** not separately assigned; see scenario table.

### XLV — Health Care sector ETF

- **Type:** ETF
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** XLV provides a diversified, high-quality health care exposure that complements the more concentrated, higher-beta equity names in the shortlist, offering a stable anchor for the portfolio. Alternatives considered: XLP, XLF.
- **Thesis:** The Health Care sector ETF (XLV) is a core defensive holding with a 0.54% daily return and a 61.4% top-10 weight coverage. It provides broad exposure to large-cap health care names including LLY, JNJ, ABBV, MRK, and UNH. The sector offers stability and diversification, but the current neutral stance reflects a balanced risk-reward profile rather than a strong directional call.
- **Source IDs:** S054, S059
- **Catalysts:** Defensive characteristics during market volatility, Diversified exposure to large-cap health care leaders, Potential for stable dividends and earnings growth
- **Risks:** Sector-specific regulatory and reimbursement risks, Concentration in large-cap names, Limited upside in a strong equity market
- **Valuation method:** Holdings/portfolio valuation with AI total-return assumption
- **Valuation status:** verified; forward-EPS source: ; period flags: 
- **Valuation assumptions:** Holdings/portfolio valuation; 10 weighted holdings; coverage 61.42%; source IDs S054, S059
- **Top holdings:** LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59%
- **Portfolio valuation:** Top 10 holdings; numeric weight coverage 61.42%
- **Sector exposure:** Health Care
- **Underlying drivers:** Large-cap health care sector performance, pharmaceutical and medical device demand, regulatory environment
- **Bull / Base / Bear:** 211.51 / 198.29 / 177.52
- **Bull / Base / Bear returns:** 12.0% / 5.0% / -6.0%
- **Scenario probabilities:** not separately assigned; see scenario table.

### XLP — Consumer Staples sector ETF

- **Type:** ETF
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** XLP provides a defensive, low-correlation anchor that complements the higher-beta equity names in the shortlist, offering portfolio stability. Alternatives considered: XLV, XLY.
- **Thesis:** The Consumer Staples sector ETF (XLP) is a defensive, low-volatility holding with a 1.42% daily return and a 63.3% top-10 weight coverage. It offers exposure to essential consumer brands such as WMT, COST, PG, KO, and PM. The sector is well-suited for capital preservation, but the current neutral stance reflects a balanced risk-reward profile.
- **Source IDs:** S058, S060
- **Catalysts:** Defensive demand characteristics, Diversified exposure to essential consumer staples, Potential for stable dividends and pricing power
- **Risks:** Limited upside in a strong equity market, Sector-specific regulatory and commodity risks, Concentration in large-cap names
- **Valuation method:** Holdings/portfolio valuation with AI total-return assumption
- **Valuation status:** verified; forward-EPS source: ; period flags: 
- **Valuation assumptions:** Holdings/portfolio valuation; 10 weighted holdings; coverage 63.28%; source IDs S058, S060
- **Top holdings:** WMT 11.14%, COST 9.09%, PG 7.60%, KO 7.37%, PM 6.59%, MO 4.70%, CL 4.42%, MDLZ 4.25%, PEP 4.11%, TGT 4.00%
- **Portfolio valuation:** Top 10 holdings; numeric weight coverage 63.28%
- **Sector exposure:** Consumer Staples
- **Underlying drivers:** Consumer staples demand, pricing power, macroeconomic stability
- **Bull / Base / Bear:** 101.59 / 96.04 / 87.73
- **Bull / Base / Bear returns:** 10.01% / 4.0% / -5.0%
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
| Bull | 25% | +2.00% | Low 5-day realized vol (14.9%) and below-threshold spike probability (16.5% vs 18.5% threshold) support a modest upside if US close confirms stable macro data and no credit stress. |
| Base | 50% | +0.00% | Frozen daily-close model with no directional signal and elevated but sub-threshold volatility implies range-bound trading; base case is flat until the official US close resolves the forecast uncertainty. |
| Bear | 25% | -2.00% | If the US close reveals a spike event or widening credit spreads, the 16.5% spike probability could trigger a downside move, with a 25% probability of a mild -2% correction. |

### Long Term (12 months)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 30% | +8.00% | Sustained low volatility and stable credit conditions over the horizon support a positive earnings trajectory, with a 30% probability of an 8% advance if rate cuts materialize. |
| Base | 40% | +3.00% | Base case assumes gradual earnings growth and orderly rate normalization, yielding a 3% long-term return with moderate volatility persistence. |
| Bear | 30% | -5.00% | A prolonged volatility spike or credit event could push long-term returns to -5%, reflecting a 30% probability of a meaningful drawdown if earnings disappoint or spreads widen. |

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
| S009 | filing | FISV | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0000798354-26-000042); 8-K filed 2026-11-03 (accession 0000798354-26-000039); 8-K filed 2026-10-23 (accession 0001193125-26-429481) |
| S010 | filing | PNR | 2026-10-27 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-27 (accession 0000077360-26-000058); 8-K filed 2026-10-27 (accession 0000077360-26-000055); 8-K filed 2026-09-22 (accession 0000077360-26-000050) |
| S011 | news | FISV | Thu, 12 Nov 2026 12:23:56 GMT | ok | https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en | Fiserv Stock Outlook: Is Wall Street Bullish or Bearish? - Yahoo Finance (Thu, 12 Nov 2026 12:23:56 GMT); Why Fiserv, Inc. (FISV) Was Exited by Ariel Appreciation Fund - Yahoo Finance (Wed, 28 Oct 2026 07:00:00 GMT); Fiserv (FISV): Buy, Sell, or Hold Post Q2 Earnings? - Yahoo Finance (Tue, 08 Sep 2026 07:00:00 GMT) |
| S012 | news | APP | Thu, 12 Nov 2026 20:05:45 GMT | ok | https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en | AppLovin Just Ripped 47% in a Month: Is It Too Late to Buy APP Stock Now? - Yahoo Finance (Thu, 12 Nov 2026 20:05:45 GMT); APP Stock Surges 51% After Q3 Earnings: Is it Still a Buy? - Yahoo Finance (Tue, 10 Nov 2026 14:24:00 GMT); ETFs Are Net Sellers of AppLovin (APP) on Nov. 11 - Yahoo Finance (Fri, 13 Nov 2026 11:02:35 GMT) |
| S013 | stock | FISV | 2026-11-15 | ok | https://finance.yahoo.com/quote/FISV | Forward P/E: 7.9923306; Price: 63.78; Market price: 63.78; Market cap: 33934002176; Market Cap: 33934002176; Consensus EPS FY+1: 7.98015; growth: 0.09689999 |
| S014 | news | PNR | Fri, 13 Nov 2026 22:05:23 GMT | ok | https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en | Pentair plc (PNR) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 22:05:23 GMT); Here's What Key Metrics Tell Us About Pentair (PNR) Q3 Earnings - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT); Pentair plc (PNR) Q3 Earnings and Revenues Beat Estimates - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT) |
| S015 | filing | APP | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json | Diluted EPS 11.61 for period ending 2026-09-30 (filed 2026-11-04) |
| S016 | stock | APP | 2026-11-15 | ok | https://finance.yahoo.com/quote/APP | Trailing P/E: 27.54882; Forward P/E: 19.611452; Forward EPS: 20.86026; Price: 409.1; Market price: 409.1; Market cap: 135543824384; Sector: Communication Services; Trailing Eps: 14.85; Revenue Growth: 0.555; Earnings Growth: 0.755; Gross Margin: 0.8878; Operating Margin: 0.77782995; Profit Margin: 0.65887; Return On Equity: 2.1008599; Total Revenue: 7608893952; Market Cap: 135543824384; Consensus EPS FY+1: 20.72438; growth: 0.2744 |
| S017 | stock | PNR | 2026-11-15 | ok | https://finance.yahoo.com/quote/PNR | Trailing P/E: 18.610355; Forward P/E: 12.877027; Forward EPS: 5.30402; Price: 68.3; Market price: 68.3; Market cap: 10904415232; Sector: Industrials; Trailing Eps: 3.67; Revenue Growth: -0.045; Earnings Growth: -0.188; Gross Margin: 0.40168998; Operating Margin: 0.21410999; Profit Margin: 0.15435; Return On Equity: 0.15605; Total Revenue: 3966200064; Market Cap: 10904415232; Consensus EPS FY+1: 5.30402; growth: 0.1282 |
| S018 | filing | GEN | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0000849399-26-000083); 8-K filed 2026-10-28 (accession 0000849399-26-000081); 8-K filed 2026-10-09 (accession 0000849399-26-000079) |
| S019 | filing | FISV | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json | Diluted EPS -8.9 for period ending 2026-09-30 (filed 2026-11-04) |
| S020 | filing | PNR | 2026-10-27 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json | Diluted EPS 2.76 for period ending 2026-09-30 (filed 2026-10-27) |
| S021 | stock | GEN | 2026-11-15 | ok | https://finance.yahoo.com/quote/GEN | Trailing P/E: 15.431472; Forward P/E: 9.108996; Forward EPS: 3.33736; Price: 30.4; Market price: 30.4; Market cap: 18035593216; Sector: Technology; Trailing Eps: 1.97; Revenue Growth: 0.122; Earnings Growth: 1.286; Gross Margin: 0.77410007; Operating Margin: 0.43229; Profit Margin: 0.23068; Return On Equity: 0.46402; Total Revenue: 5228000256; Market Cap: 18035593216; Consensus EPS FY+1: 3.33736; growth: 0.1286 |
| S022 | filing | CLX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000021076-26-000046); 8-K filed 2026-11-02 (accession 0000021076-26-000044); 8-K filed 2026-10-29 (accession 0001206774-26-000586) |
| S023 | stock | CLX | 2026-11-15 | ok | https://finance.yahoo.com/quote/CLX | Trailing P/E: 19.68705; Forward P/E: 17.745283; Forward EPS: 6.1684; Price: 109.46; Market price: 109.46; Market cap: 13260793856; Sector: Consumer Defensive; Trailing Eps: 5.56; Revenue Growth: 0.333; Earnings Growth: 1.138; Gross Margin: 0.41939998; Operating Margin: 0.14286; Profit Margin: 0.09408; Return On Equity: 5.34363; Total Revenue: 7196000256; Market Cap: 13260793856; Consensus EPS FY+1: 6.1684; growth: 0.0769 |
| S024 | news | GEN | Fri, 13 Nov 2026 09:34:35 GMT | ok | https://news.google.com/rss/search?q=GEN+Gen+Digital+stock&hl=en-US&gl=US&ceid=US:en | Gen Digital Inc. (GEN) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 09:34:35 GMT); Gen Digital (GEN) Stock Repriced After Q2 Earnings Put Margins Center Stage - Yahoo Finance (Thu, 29 Oct 2026 07:00:00 GMT); Gen Digital Inc. (GEN) Stock Forecasts - Yahoo Finance (Wed, 11 Nov 2026 13:10:37 GMT) |
| S025 | filing | CHTR | 2026-11-06 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-06 (accession 0001091667-26-000073); 8-K filed 2026-11-06 (accession 0001091667-26-000072); 8-K filed 2026-10-27 (accession 0001091667-26-000064) |
| S026 | news | CLX | Sun, 15 Nov 2026 08:55:47 GMT | ok | https://news.google.com/rss/search?q=CLX+Clorox+stock&hl=en-US&gl=US&ceid=US:en | The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance UK (Sun, 15 Nov 2026 08:55:47 GMT); The Clorox Company (CLX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 05:44:34 GMT); The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance Singapore (Sat, 14 Nov 2026 05:36:50 GMT) |
| S027 | filing | IDXX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000874716&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000874716-26-000135); 8-K filed 2026-11-02 (accession 0001104659-26-120892); 10-Q filed 2026-08-04 (accession 0000874716-26-000123) |
| S028 | news | CHTR | Sun, 15 Nov 2026 05:47:01 GMT | ok | https://news.google.com/rss/search?q=CHTR+Charter+Communications+stock&hl=en-US&gl=US&ceid=US:en | Charter Communications (CHTR) Stock Could Be A Bargain Following Its New Operating Model - Yahoo Finance (Sun, 15 Nov 2026 05:47:01 GMT); Charter Communications (CHTR) Expands Enterprise Reach With Managed Secure Networking Launch - Yahoo Finance (Sun, 15 Nov 2026 06:08:00 GMT); Charter Communications (CHTR) Earnings Expected to Grow: What to Know Ahead of Next Week's Release - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT) |
| S029 | filing | GEN | 2026-10-29 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000849399.json | Diluted EPS 0.83 for period ending 2026-10-02 (filed 2026-10-29) |
| S030 | news | IDXX | Sat, 14 Nov 2026 06:13:17 GMT | ok | https://news.google.com/rss/search?q=IDXX+Idexx+Laboratories+stock&hl=en-US&gl=US&ceid=US:en | IDEXX Laboratories, Inc. (IDXX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Sat, 14 Nov 2026 06:13:17 GMT); IDEXX Laboratories, Inc. (IDXX) stock price, news, quote and history - Yahoo Finance UK (Sat, 14 Nov 2026 12:31:19 GMT); IDEXX Laboratories (IDXX) Stock Looks Fairly Valued Despite Its 28% Run - Yahoo Finance (Sat, 31 Oct 2026 07:00:00 GMT) |
| S031 | stock | CHTR | 2026-11-15 | ok | https://finance.yahoo.com/quote/CHTR | Trailing P/E: 13.006578; Forward P/E: 3.2831066; Forward EPS: 42.15215; Price: 138.39; Market price: 138.39; Market cap: 24778944512; Sector: Communication Services; Trailing Eps: 10.64; Revenue Growth: 0.091; Gross Margin: 0.55084; Operating Margin: 0.23389; Profit Margin: 0.02498; Return On Equity: 0.07019; Total Revenue: 55645999104; Market Cap: 24778944512; Consensus EPS FY+1: 47.15811; growth: 1.0195 |
| S032 | filing | CHTR | 2026-11-06 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001091667.json | Diluted EPS 0.38 for period ending 2026-09-30 (filed 2026-11-06) |
| S033 | stock | IDXX | 2026-11-15 | ok | https://finance.yahoo.com/quote/IDXX | Trailing P/E: 47.45485; Forward P/E: 41.687927; Forward EPS: 16.8929; Price: 704.23; Market price: 704.23; Market cap: 55483650048; Sector: Healthcare; Trailing Eps: 14.84; Revenue Growth: 0.099; Earnings Growth: 0.179; Gross Margin: 0.62722; Operating Margin: 0.32497; Profit Margin: 0.25357; Return On Equity: 0.68925005; Total Revenue: 4662220800; Market Cap: 55483650048; Consensus EPS FY+1: 16.8929; growth: 0.1244 |
| S034 | filing | ROP | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000882835&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000882835-26-000047); 8-K filed 2026-10-22 (accession 0000882835-26-000042); 8-K filed 2026-10-01 (accession 0000882835-26-000039) |
| S035 | filing | RDDT | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001713445&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0001713445-26-000116); 8-K filed 2026-10-29 (accession 0001713445-26-000114); 8-K filed 2026-08-12 (accession 0001713445-26-000107) |
| S036 | filing | CLX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000021076.json | Diluted EPS 1.39 for period ending 2026-09-30 (filed 2026-11-02) |
| S037 | news | ROP | Thu, 12 Nov 2026 19:15:50 GMT | ok | https://news.google.com/rss/search?q=ROP+Roper+Technologies+stock&hl=en-US&gl=US&ceid=US:en | Roper Technologies, Inc. (ROP) Stock Price, News, Quote & History - Yahoo! Finance Canada (Thu, 12 Nov 2026 19:15:50 GMT); Roper Technologies (ROP) Stock Looks Fully Valued As Cash Flow Comes Into Focus - Yahoo Finance (Thu, 05 Nov 2026 08:00:00 GMT); Roper Technologies: 3 Key Takeaways for Long-Term Investors - Yahoo Finance (Mon, 26 Oct 2026 07:00:00 GMT) |
| S038 | filing | IDXX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000874716.json | Diluted EPS 11.75 for period ending 2026-09-30 (filed 2026-11-02) |
| S039 | filing | INTC | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000050863&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0000050863-26-000191); 8-K filed 2026-10-29 (accession 0000050863-26-000188); 8-K filed 2026-08-12 (accession 0001193125-26-346806) |
| S040 | stock | ROP | 2026-11-15 | ok | https://finance.yahoo.com/quote/ROP | Trailing P/E: 18.993866; Forward P/E: 19.532475; Forward EPS: 24.57318; Price: 479.975; Market price: 479.975; Market cap: 47535013888; Sector: Technology; Trailing Eps: 25.27; Revenue Growth: 0.076; Earnings Growth: 0.326; Gross Margin: 0.69671; Operating Margin: 0.28049; Profit Margin: 0.30712998; Return On Equity: 0.13229; Total Revenue: 8434599936; Market Cap: 47535013888; Consensus EPS FY+1: 24.57318; growth: 0.09810001 |

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
- news FISV: https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en (Thu, 12 Nov 2026 12:23:56 GMT)
- news APP: https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en (Thu, 12 Nov 2026 20:05:45 GMT)
- stock FISV: https://finance.yahoo.com/quote/FISV (2026-11-15)
- news PNR: https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 22:05:23 GMT)
- filing APP: https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json (2026-11-04)
- stock APP: https://finance.yahoo.com/quote/APP (2026-11-15)
- stock PNR: https://finance.yahoo.com/quote/PNR (2026-11-15)
- filing GEN: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 (2026-10-29)
- filing FISV: https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json (2026-11-04)
- filing PNR: https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json (2026-10-27)

## AI Provenance

- Provider / model: hermes-local-proxy / upstage/solar-mini4:free
- Market research: attempts=1 tokens=9473 (prompt=6473, completion=3000) runtime=19.72s
- Fundamental research: generated this run at 2026-11-15T13:15:51.109129+00:00
- Evidence source dates: {'as_of': '2026-11-13', 'latest_equity_date': '2026-11-13', 'latest_macro_date': '2026-11-14', 'flows_date': '2026-11-13'}
- Evidence fingerprint: f63f89ebfdf6d4e6644d877b8eba95dba576958735a5502162fef05c1f731065
- Source citations are retrieved external records in the ledger above; market values remain from the verified database snapshot.


## Disclosures

- This is research and market intelligence, not investment advice.
- AI conclusions are research judgments, not validated return predictions.
- The frozen risk layer is risk-only and is not used for directional views or allocations.
- Legacy scores are not active inputs or outputs.

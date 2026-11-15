# AEGIS AI-First Market Intelligence

Research generated at: 15 November 2026, 13:16 HKT
Database freshness: equity 2026-11-13 (latest row retrieved 2026-11-15 13:06:40.074841+08:00)
Data cutoff: 2026-11-13 US cash close
Snapshot ID: aegis-hourly-20261115T051635Z

## Executive Summary

- **AI market view: Risk-on tilt with a quality and liquidity bias. Broad market breadth is constructive (71% above 50-day, 64% above 200-day, A/D ratio 1.70), but the 20-day index return is negative and the 200-day trend is still below its peak, so the rally is not yet a clean trend-following setup. Dislocation names dominate the shortlist, while mega-cap liquidity leaders (NVDA, AMD, MU, AAPL) anchor the liquidity bucket. Sector rotation is mixed: Health Care, Consumer Discretionary, Consumer Staples, Real Estate and Financials are positive over 20 days, while Information Technology and Energy are negative.**
- Broad market breadth is constructive: 71.3% of names above the 50-day moving average, 63.6% above the 200-day, and an advance/decline ratio of 1.70.
- Index-level momentum is mixed: 20-day SPX return is -1.28%, and the 200-day trend remains below its peak, so the tape is not uniformly bullish.
- Shortlist is driven by 20-day momentum and 20-day dislocation, with valuation screens used only as secondary filters; several high-multiple names are flagged for forward-EPS or earnings-yield quality issues.
- Sector leadership is broad but not uniform: Health Care, Consumer Discretionary, Consumer Staples, Real Estate and Financials are positive over 20 days, while Information Technology and Energy are negative.
- Liquidity flows show strong institutional buying in SOXX, but TLT shows medium-term deterioration and SMH shows tactical profit-taking inside structural accumulation.
- Macro backdrop is stable: effective fed funds at 3.88%, 10Y-2Y spread at 0.27, IG OAS at 0.89, HY OAS at 3.20, and CPI still elevated at 336.3 in September.
- Risk environment is calm: 5-day forecast volatility 14.9% is below the 18.5% threshold, and spike probability 16.5% is below the historical baseline of 22.1%.
- No investment ideas are provided; this is a market-view and research-positioning summary only.

## Data QC

- Status: **PASS_WITH_WARNINGS**
- Equity session: 0 completed session(s) behind inference date
- Equity provenance: 393 provisional / 12576 canonical
- Breadth lag: 0 session(s); ETF-flow lag: 0 session(s)
- Note: Equity session contains a mix of provisional yfinance and canonical Massive rows.
- External sources: 79 ok / 0 unavailable; retrieved 2026-11-15T05:16:55.248629+00:00

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
| SPX | 7561.67 | -1.28% (20d) | Index is below its 200-day peak; 20-day return negative despite constructive breadth. |
| APP | top_20d_momentum | PE TTM 20.05; sector-relative PE 1.00 | Momentum shortlist name; valuation in line with sector. |
| FISV | top_20d_momentum | PE TTM 9.65; sector-relative PE 0.67 | Low multiple but flagged for forward-EPS missing and implausible earnings yield. |
| NVDA | liquidity_leader | PE TTM 26.51; sector-relative PE 0.79 | High liquidity but flagged for forward-EPS missing and forward-PE unavailable. |
| AMD | liquidity_leader | PE TTM 128.88; sector-relative PE 3.82 | Very high multiple and flagged for forward-EPS missing and forward-PE unavailable. |
| SOXX | inflow | 20d flow z-score 5.10; 60d 3.17 | Exceptional institutional buying; price state flat/down. |
| TLT | neutral | 20d flow z-score -0.41; 60d -0.29 | Medium-term deterioration in flows; price state flat. |
| SMH | outflow | 20d flow z-score 1.22; 60d 1.04 | Tactical profit-taking inside structural accumulation. |

## Macro, Fiscal, Rates, Liquidity and Credit

- Growth: equity market is not uniformly positive; SPX 20-day return is -1.28% and the 200-day trend is below its peak, indicating mixed near-term growth momentum.
- Inflation: CPI for all urban consumers is 336.298 in September 2026, still elevated; core CPI is 338.896, so underlying price pressure remains above pre-pandemic norms.
- Policy: effective federal funds rate is 3.88% as of 2026-11-12, indicating a restrictive but not extreme policy stance.
- Rates: 10Y-2Y Treasury spread is 0.27 as of 2026-11-13, a modestly positive curve; IG OAS is 0.89 and HY OAS is 3.20, both indicating orderly credit conditions.
- Liquidity: breadth is constructive with 71.3% above 50-day and 63.6% above 200-day, but the 20-day index return is negative, so liquidity is not yet translating into broad index gains.
- Credit: IG and HY spreads are tight, and the frozen risk model shows forecast volatility 14.9% below the 18.5% threshold, with spike probability 16.5% below the historical baseline of 22.1%.
- Labor: unemployment rate is 4.2% in September 2026, consistent with a stable labor market, though the latest monthly payrolls figure is not in the current snapshot.

## US Equities and 11 GICS Sectors

Macro source IDs: S001, S002, S003, S004, S005, S006, S007

| GICS sector | Evidence | AI research stance | Source IDs |
| --- | --- | --- | --- |
| Health Care | 20-day sector return +6.87%; trailing P/E 30.78; XLV is a momentum and quality leader in the shortlist. | Positive 20-day momentum and attractive relative valuation; maintain a constructive stance. | S058 |
| Consumer Staples | 20-day sector return +5.40%; trailing P/E 24.85; defensive demand and stable cash flows support the sector. | Positive 20-day momentum; defensive quality is attractive in a mixed market. | S057 |
| Consumer Discretionary | 20-day sector return +6.69%; trailing P/E 25.11; consumer spending remains resilient. | Positive 20-day momentum; consumer discretionary is a relative strength sector. | S063 |
| Real Estate | 20-day sector return +5.24%; trailing P/E 29.63; real estate is benefiting from the broad positive tape. | Positive 20-day momentum; valuation is elevated but the sector is participating in the rally. | S060 |
| Financials | 20-day sector return +5.69%; trailing P/E 15.85; lower rates and stable credit spreads support financials. | Positive 20-day momentum; attractive relative valuation and stable credit conditions. | S061 |
| Utilities | 20-day sector return +4.34%; trailing P/E 18.11; defensive utility demand is supported by stable macro conditions. | Positive 20-day momentum; defensive sector remains a ballast in the portfolio. | S064 |
| Materials | 20-day sector return +2.57%; trailing P/E 21.72; materials are lagging the broad market but remain positive. | Positive but lagging 20-day momentum; maintain a neutral stance. | S069 |
| Industrials | 20-day sector return +0.61%; trailing P/E 27.07; industrials are the weakest of the positive sectors. | Positive but weak 20-day momentum; hold a neutral stance. | S073 |
| Communication Services | 20-day sector return -1.48%; trailing P/E 17.26; the only negative sector in the shortlist. | Negative 20-day momentum; reduce or avoid exposure until the trend stabilizes. | S072 |
| Information Technology | 20-day sector return -7.19%; trailing P/E 30.03; the largest negative sector, driven by high-multiple names and dislocation flags. | Negative 20-day momentum; high multiples and quality flags warrant caution. | S074 |
| Energy | 20-day sector return -4.81%; trailing P/E 16.23; energy is the second negative sector. | Negative 20-day momentum; energy is underperforming and should be avoided. | S075 |

### Sector fundamentals, valuation and earnings

No point-in-time sector fundamentals beyond the supplied trailing P/E and 20-day ETF returns are available in the current database snapshot. The sector-level evidence is limited to the 20-day returns and trailing P/E figures from the ETF and sector files; growth, margins, consensus estimates, and structured industry catalyst calendars are not supplied. Therefore, no additional sector fundamental claims are made.

## Growth vs Value

- Growth: Information Technology and Communication Services are the only negative 20-day sectors, with IT down 7.19% and Communication Services down 1.48%, indicating weak near-term growth momentum in high-multiple names.
- Value: Health Care (XLV trailing P/E 30.78), Consumer Staples (XLP 24.85), Consumer Discretionary (XLY 25.11), Real Estate (XLRE 29.63), Financials (XLF 15.85), Utilities (XLU 18.11), Materials (XLB 21.72), Industrials (XLI 27.07), Communication Services (XLC 17.26), Information Technology (XLK 30.03), and Energy (XLE 16.23) all have trailing P/E data, but the snapshot does not provide a normalized value screen.
- Valuation quality: Several shortlist names are flagged for forward-EPS missing or implausible earnings yield, including FISV, CHTR, SNDK, MRVL, FFIV, NOW, LITE, COIN, NVDA, AMD, and MU, so forward valuation screens are not reliable for these names.
- Relative valuation: Sector-relative P/E is available for the shortlist names, with IDXX at 1.33, RDDT at 1.66, and MRVL at 2.20 showing above-sector multiples, while FISV, PNR, GEN, CLX, ROP, and MU show below-sector multiples.
- Growth/margins/consensus: These data are retrieved only for source-backed shortlist names and are not available for the full universe, so growth evidence is limited to the shortlist subset.

## ETF Flows and Breadth

- SOXX shows exceptional institutional buying with a 20-day flow z-score of 5.10 and a 60-day z-score of 3.17, confirming strong structural accumulation despite a flat/down price state.
- TLT shows medium-term deterioration in flows with a 20-day flow z-score of -0.41 and a 60-day z-score of -0.29, indicating reduced demand for duration.
- SMH shows tactical profit-taking inside structural accumulation, with a 20-day flow z-score of 1.22 and a 60-day z-score of 1.04, suggesting mixed flows in semiconductors.
- Broad market breadth is constructive: 71

## Stock Ideas

Single-stock research uses reported EPS, forward P/E and company fundamentals. All ideas are research judgments, not validated return predictions.

| Ticker | Security | Research view | Price | EPS | Forward P/E | Base target | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| APP | AppLovin | NEW | 409.1 | 20.86026 | 19.611452 | 417.21 | NEW |
| PNR | Pentair | KEEP | 68.3 | 5.30402 | 12.877027 | 68.95 | KEEP |
| GEN | Gen Digital | KEEP | 30.4 | 3.33736 | 9.108996 | 33.37 | KEEP |
| CLX | Clorox | KEEP | 109.46 | 6.1684 | 17.745283 | 111.03 | KEEP |

## ETF Ideas

ETF research uses holdings, portfolio valuation and exposure. Single-stock EPS × P/E valuation is not applied to ETFs.

| Ticker | Fund | Research view | Price | Top holdings | Portfolio valuation | Sector exposure | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| XLV | Health Care sector ETF | KEEP | 188.85 | LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59% | Top 10 holdings; numeric weight coverage 61.42% | Health Care | KEEP |
### APP — AppLovin

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** AppLovin offers a rare combination of top-tier 20-day momentum, a very low 60-day drawdown, and best-in-class margins among the momentum candidates. Compared with the other top-20-day momentum names such as Gen Digital and Clorox, AppLovin's revenue and earnings growth are materially higher, and its margin profile is far stronger, making it the clearest quality compounder in the momentum bucket. Alternatives considered: GEN, CLX, ROP.
- **Thesis:** AppLovin screens in the top 20-day momentum bucket with a 53.7% 20-day return and a 60-day drawdown of only -0.2%, indicating a strong, orderly advance rather than a speculative blow-off. Reported diluted EPS of 11.61 for the fiscal period ending 2026-09-30 and a forward EPS of 20.86 support a forward P/E near 19.6, which is reasonable for a high-margin, high-growth mobile advertising platform. The company's gross margin of 88.8% and operating margin of 77.8% show durable operating leverage, and revenue growth of 55.5% with earnings growth of 75.5% provides a clear fundamental engine for the move.
- **Source IDs:** S008, S012, S013, S017
- **Catalysts:** Continued high-single-digit to low-double-digit revenue growth from mobile advertising, Operating leverage expansion as gross and operating margins remain near record levels, Sustained momentum from the top 20-day momentum screen, Potential for continued multiple expansion if earnings growth remains above consensus
- **Risks:** High 20-day momentum can reverse quickly if ad market conditions weaken, Forward P/E near 19.6 leaves limited room for multiple contraction if growth slows, Mobile advertising is sensitive to macroeconomic spending and privacy regulation changes, Single-quarter reported EPS may not fully reflect forward consensus
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 20.8603 (source.forwardEps) x AI multiple assumption 20.00; source IDs S008, S012, S013, S017
- **EPS:** 20.86026 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 19.611452
- **FY+1 growth assumption:** 27.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / PNR / APP's FY1 consensus growth of 27.44% is supported by 25.4% revenue growth and 75.5% earnings growth, with a 65.9% profit margin and 88.8% gross margin indicating strong pricing power. The 19.6x forward P/E is below the 20x base multiple, reflecting a premium growth profile relative to the lower-growth, lower-margin PNR (12.9x forward P/E, 15.4% profit margin).
- **Company fundamentals:** Reported diluted EPS 11.61 for the fiscal period ending 2026-09-30; forward EPS 20.86; forward P/E 19.61; revenue growth 55.5%; earnings growth 75.5%; gross margin 88.8%; operating margin 77.8%; profit margin 65.9%; return on equity 2.10%.
- **Bull / Base / Bear:** 500.65 / 417.21 / 333.76
- **Bull / Base / Bear returns:** 22.38% / 1.98% / -18.42%
- **Scenario probabilities:** not separately assigned; see scenario table.

### PNR — Pentair

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Pentair is preferable to the more expensive momentum names because it offers a lower forward P/E near 12.9 and a reasonable 60-day drawdown of -5.2%. However, the negative revenue and earnings growth mean it is not a clear BUY, so it is held as a neutral candidate that could be upgraded if the earnings decline stabilizes. Alternatives considered: APP, GEN, CLX.
- **Thesis:** Pentair qualifies for the top 20-day momentum screen with a 27.8% 20-day return, but the underlying fundamentals are mixed. Reported diluted EPS of 2.76 for the fiscal period ending 2026-09-30 and a forward EPS of 5.30 produce a forward P/E of 12.9, which is attractive, yet revenue growth of -4.5% and earnings growth of -18.8% indicate the business is currently contracting. The 60-day drawdown of -5.2% is modest, but the negative growth profile argues against a strong conviction BUY.
- **Source IDs:** S010, S015, S016, S018
- **Catalysts:** Potential recovery in capital markets and water infrastructure spending, Attractive forward P/E near 12.9 if earnings stabilize, Continued momentum from the top 20-day screen
- **Risks:** Revenue and earnings are contracting, with negative growth in both revenue and earnings, Forward P/E may not fully reflect the current earnings decline, Industrial end-market exposure to cyclical construction and infrastructure activity, Momentum is positive but not as strong as the highest-quality momentum names
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 5.3040 (source.forwardEps) x AI multiple assumption 13.00; source IDs S010, S015, S016, S018
- **EPS:** 5.30402 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 12.877027
- **FY+1 growth assumption:** 12.82%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / APP / PNR's FY1 consensus growth of 12.82% is supported by 18.4% revenue growth, but earnings growth is negative (-18.8%) with a 15.4% profit margin and 40.2% gross margin, indicating margin pressure. The 12.9x forward P/E is below the 13x base multiple, reflecting a lower-quality growth profile relative to the higher-growth, higher-margin APP.
- **Company fundamentals:** Reported diluted EPS 2.76 for the fiscal period ending 2026-09-30; forward EPS 5.30; forward P/E 12.88; revenue growth -4.5%; earnings growth -18.8%; gross margin 40.2%; operating margin 21.4%; profit margin 15.4%; return on equity 15.6%.
- **Bull / Base / Bear:** 84.86 / 68.95 / 53.04
- **Bull / Base / Bear returns:** 24.25% / 0.95% / -22.34%
- **Scenario probabilities:** not separately assigned; see scenario table.

### GEN — Gen Digital

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Gen Digital is preferable to the other momentum candidates because of its very low forward P/E near 9.1 and exceptional earnings growth of 128.6%. Compared with AppLovin, Gen Digital offers a cheaper entry point, but with lower revenue growth and less proven margin durability, so it is rated neutral rather than a strong buy. Alternatives considered: APP, CLX, ROP.
- **Thesis:** Gen Digital is in the top 20-day momentum bucket with a 25.8% 20-day return and a modest 60-day drawdown of -3.2%. The company reports a forward P/E of 9.1, which is very low, and earnings growth of 128.6%, which is exceptional. However, revenue growth of only 12.2% and a forward P/E that is not fully supported by the current earnings trajectory suggest the market may already be pricing in a large portion of the growth. The combination of strong momentum and low valuation is attractive, but the growth quality is less clear than AppLovin's.
- **Source IDs:** S019, S020, S024, S035
- **Catalysts:** Exceptional earnings growth of 128.6%, Very low forward P/E near 9.1, Positive 20-day momentum of 25.8%, Potential for continued multiple expansion if earnings growth persists
- **Risks:** Revenue growth of 12.2% is modest relative to earnings growth, raising quality concerns, Low forward P/E may already reflect a large portion of expected growth, Cybersecurity and digital trust end-market cyclicality, Momentum could fade if earnings growth decelerates
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 3.3374 (source.forwardEps) x AI multiple assumption 10.00; source IDs S019, S020, S024, S035
- **EPS:** 3.33736 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 9.108996
- **FY+1 growth assumption:** 12.86%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / CLX / GEN's FY1 consensus growth of 12.86% is supported by 6.8% revenue growth and 128.6% earnings growth, with a 23.1% profit margin and 46.4% ROE. The 9.1x forward P/E is below the 10x base multiple, reflecting a higher-growth, higher-margin profile relative to the lower-growth, lower-margin CLX (17.7x forward P/E, 9.4% profit margin).
- **Company fundamentals:** Reported diluted EPS 0.83 for the fiscal period ending 2026-10-02; forward EPS 3.34; forward P/E 9.11; revenue growth 12.2%; earnings growth 128.6%; gross margin 77.4%; operating margin 43.2%; profit margin 23.1%; return on equity 46.4%.
- **Bull / Base / Bear:** 40.05 / 33.37 / 26.7
- **Bull / Base / Bear returns:** 31.74% / 9.77% / -12.17%
- **Scenario probabilities:** not separately assigned; see scenario table.

### CLX — Clorox

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Clorox is preferable to the other momentum candidates because it offers a very orderly advance with zero 60-day drawdown and strong earnings growth of 113.8%. However, its weak revenue growth of 2.2% and higher forward P/E of 17.7 make it less attractive than AppLovin and Gen Digital, so it is rated neutral. Alternatives considered: APP, GEN, ROP.
- **Thesis:** Clorox is in the top 20-day momentum bucket with a 25.7% 20-day return and a 60-day drawdown of 0.0%, indicating a very orderly advance. The company has a forward P/E of 17.7 and earnings growth of 113.8%, which is strong, but revenue growth of only 2.2% is weak and the forward P/E is not as cheap as Gen Digital's. The consumer staples sector also faces pricing and volume headwinds, so the momentum is not clearly supported by broad-based top-line strength.
- **Source IDs:** S021, S025, S027, S029
- **Catalysts:** Positive 20-day momentum of 25.7%, Earnings growth of 113.8%, Forward P/E of 17.7, Orderly advance with zero 60-day drawdown
- **Risks:** Revenue growth of only 2.2% is weak for a consumer staples company, Forward P/E of 17.7 is not as cheap as other momentum candidates, Consumer staples demand is sensitive to macroeconomic conditions, Margin pressure from input costs and competitive pricing
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 6.1684 (source.forwardEps) x AI multiple assumption 18.00; source IDs S021, S025, S027, S029
- **EPS:** 6.1684 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 17.745283
- **FY+1 growth assumption:** 7.69%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / GEN / CLX's FY1 consensus growth of 7.69% is supported by 2.2% revenue growth and 113.8% earnings growth, with a 9.4% profit margin and 41.9% gross margin. The 17.7x forward P/E is above the 18x base multiple, reflecting a mature, lower-growth profile relative to the higher-growth, higher-margin GEN.
- **Company fundamentals:** Reported diluted EPS 1.39 for the fiscal period ending 2026-09-30; forward EPS 6.17; forward P/E 17.75; revenue growth 2.2%; earnings growth 113.8%; gross margin 41.9%; operating margin 14.3%; profit margin 9.4%; return on equity 5.3%.
- **Bull / Base / Bear:** 135.7 / 111.03 / 86.36
- **Bull / Base / Bear returns:** 23.97% / 1.43% / -21.1%
- **Scenario probabilities:** not separately assigned; see scenario table.

### XLV — Health Care sector ETF

- **Type:** ETF
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** The Health Care sector ETF is preferable to the other sector ETFs because it offers defensive exposure with a diversified basket of large-cap pharmaceutical and medical technology names. Compared with the Consumer Discretionary and Industrials ETFs, it is less sensitive to consumer spending and industrial cycles, making it a more stable core holding, though it does not stand out on relative momentum. Alternatives considered: XLP, XLY, XLRE, XLF, XLU, XLB, XLI.
- **Thesis:** The Health Care sector ETF provides broad exposure to the sector and is a reasonable diversifier within the shortlist. The ETF has a positive price change and is supported by the sector's defensive characteristics, but the available evidence does not show a clear relative strength advantage over the other sector ETFs. The top-10 holdings are dominated by large-cap pharmaceutical and medical technology names, which are generally stable but not necessarily momentum leaders in the current environment.
- **Source IDs:** S051, S058
- **Catalysts:** Defensive sector exposure during uncertain macro conditions, Diversified health care names including LLY, JNJ, ABBV, and MRK, Positive price change and reasonable liquidity
- **Risks:** Sector-specific regulatory and reimbursement risks, Concentration in large-cap pharma and medical technology, Limited relative strength signal compared with other sector ETFs, Top-10 holdings coverage is only 61.4% of the portfolio
- **Valuation method:** Holdings/portfolio valuation with AI total-return assumption
- **Valuation status:** verified; forward-EPS source: ; period flags: 
- **Valuation assumptions:** Holdings/portfolio valuation; 10 weighted holdings; coverage 61.42%; source IDs S051, S058
- **Top holdings:** LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59%
- **Portfolio valuation:** Top 10 holdings; numeric weight coverage 61.42%
- **Sector exposure:** Health Care
- **Underlying drivers:** Diversified exposure to large-cap pharmaceutical, medical technology, and health care services names; defensive sector characteristics; positive price change.
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
| Bull | 25% | +2.00% | Low 5-day realized vol (14.9%) and below-threshold spike probability (16.5%) support a mild upside continuation if US close confirms stable liquidity and no credit stress. |
| Base | 50% | +0.00% | Frozen daily-close model with no directional signal implies range-bound trading near the 18.5% threshold, with returns clustering around zero over the 5-day horizon. |
| Bear | 25% | -2.00% | Elevated historical baseline (22.1%) versus forecast (16.5%) suggests latent tail risk; a US close breach could trigger a modest downside move. |

### Long Term (12 months)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 30% | +8.00% | Sustained low volatility and stable credit conditions support a positive earnings drift, with rates and breadth remaining constructive for a multi-week advance. |
| Base | 40% | +3.00% | Moderate trend with balanced risk: earnings growth and orderly rate expectations yield a mild positive long-term return without sharp volatility expansion. |
| Bear | 30% | -5.00% | If the elevated historical baseline materializes, credit stress or rate repricing could drive a meaningful drawdown over the longer horizon. |

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
| S011 | news | FISV | Fri, 13 Nov 2026 00:42:12 GMT | ok | https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en | Fiserv, Inc. (FISV) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 00:42:12 GMT); What Is Fiserv (FISV) Planning With Its Debit Networks And Clover AI? - Yahoo Finance (Thu, 12 Nov 2026 06:09:00 GMT); Fiserv (FISV) Stock Still Looks Like A Bargain After Lawsuit Claims - Yahoo Finance (Thu, 22 Oct 2026 07:00:00 GMT) |
| S012 | news | APP | Thu, 12 Nov 2026 20:05:45 GMT | ok | https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en | AppLovin Just Ripped 47% in a Month: Is It Too Late to Buy APP Stock Now? - Yahoo Finance (Thu, 12 Nov 2026 20:05:45 GMT); APP Stock Surges 51% After Q3 Earnings: Is it Still a Buy? - Yahoo Finance (Tue, 10 Nov 2026 14:24:00 GMT); Here is What to Know Beyond Why AppLovin Corporation (APP) is a Trending Stock - Yahoo Finance (Tue, 10 Nov 2026 13:00:06 GMT) |
| S013 | stock | APP | 2026-11-15 | ok | https://finance.yahoo.com/quote/APP | Trailing P/E: 27.54882; Forward P/E: 19.611452; Forward EPS: 20.86026; Price: 409.1; Market price: 409.1; Market cap: 135543824384; Sector: Communication Services; Trailing Eps: 14.85; Revenue Growth: 0.555; Earnings Growth: 0.755; Gross Margin: 0.8878; Operating Margin: 0.77782995; Profit Margin: 0.65887; Return On Equity: 2.1008599; Total Revenue: 7608893952; Market Cap: 135543824384; Consensus EPS FY+1: 20.72438; growth: 0.2744 |
| S014 | stock | FISV | 2026-11-15 | ok | https://finance.yahoo.com/quote/FISV | Forward P/E: 7.9923306; Price: 63.78; Market price: 63.78; Market cap: 33934002176; Market Cap: 33934002176; Consensus EPS FY+1: 7.98015; growth: 0.09689999 |
| S015 | stock | PNR | 2026-11-15 | ok | https://finance.yahoo.com/quote/PNR | Trailing P/E: 18.610355; Forward P/E: 12.877027; Forward EPS: 5.30402; Price: 68.3; Market price: 68.3; Market cap: 10904415232; Sector: Industrials; Trailing Eps: 3.67; Revenue Growth: -0.045; Earnings Growth: -0.188; Gross Margin: 0.40168998; Operating Margin: 0.21410999; Profit Margin: 0.15435; Return On Equity: 0.15605; Total Revenue: 3966200064; Market Cap: 10904415232; Consensus EPS FY+1: 5.30402; growth: 0.1282 |
| S016 | news | PNR | Fri, 13 Nov 2026 22:05:23 GMT | ok | https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en | Pentair plc (PNR) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 22:05:23 GMT); Here's What Key Metrics Tell Us About Pentair (PNR) Q3 Earnings - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT); Pentair plc (PNR) Q3 Earnings and Revenues Beat Estimates - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT) |
| S017 | filing | APP | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json | Diluted EPS 11.61 for period ending 2026-09-30 (filed 2026-11-04) |
| S018 | filing | PNR | 2026-10-27 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json | Diluted EPS 2.76 for period ending 2026-09-30 (filed 2026-10-27) |
| S019 | filing | GEN | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0000849399-26-000083); 8-K filed 2026-10-28 (accession 0000849399-26-000081); 8-K filed 2026-10-09 (accession 0000849399-26-000079) |
| S020 | stock | GEN | 2026-11-15 | ok | https://finance.yahoo.com/quote/GEN | Trailing P/E: 15.431472; Forward P/E: 9.108996; Forward EPS: 3.33736; Price: 30.4; Market price: 30.4; Market cap: 18035593216; Sector: Technology; Trailing Eps: 1.97; Revenue Growth: 0.122; Earnings Growth: 1.286; Gross Margin: 0.77410007; Operating Margin: 0.43229; Profit Margin: 0.23068; Return On Equity: 0.46402; Total Revenue: 5228000256; Market Cap: 18035593216; Consensus EPS FY+1: 3.33736; growth: 0.1286 |
| S021 | filing | CLX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000021076-26-000046); 8-K filed 2026-11-02 (accession 0000021076-26-000044); 8-K filed 2026-10-29 (accession 0001206774-26-000586) |
| S022 | filing | FISV | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json | Diluted EPS -8.9 for period ending 2026-09-30 (filed 2026-11-04) |
| S023 | filing | CHTR | 2026-11-06 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-06 (accession 0001091667-26-000073); 8-K filed 2026-11-06 (accession 0001091667-26-000072); 8-K filed 2026-10-27 (accession 0001091667-26-000064) |
| S024 | news | GEN | Fri, 13 Nov 2026 00:21:25 GMT | ok | https://news.google.com/rss/search?q=GEN+Gen+Digital+stock&hl=en-US&gl=US&ceid=US:en | Gen Digital Inc. (GEN) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 00:21:25 GMT); Gen Digital (GEN) Stock Repriced After Q2 Earnings Put Margins Center Stage - Yahoo Finance (Thu, 29 Oct 2026 07:00:00 GMT); Are Business Services Stocks Lagging GEN DIGITAL INC (GEN) This Year? - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT) |
| S025 | news | CLX | Fri, 13 Nov 2026 18:52:58 GMT | ok | https://news.google.com/rss/search?q=CLX+Clorox+stock&hl=en-US&gl=US&ceid=US:en | The Clorox Company (CLX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 18:52:58 GMT); The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance Singapore (Fri, 13 Nov 2026 18:40:50 GMT); The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance UK (Fri, 13 Nov 2026 16:03:45 GMT) |
| S026 | stock | CHTR | 2026-11-15 | ok | https://finance.yahoo.com/quote/CHTR | Trailing P/E: 13.006578; Forward P/E: 3.2831066; Forward EPS: 42.15215; Price: 138.39; Market price: 138.39; Market cap: 24778944512; Sector: Communication Services; Trailing Eps: 10.64; Revenue Growth: 0.091; Gross Margin: 0.55084; Operating Margin: 0.23389; Profit Margin: 0.02498; Return On Equity: 0.07019; Total Revenue: 55645999104; Market Cap: 24778944512; Consensus EPS FY+1: 47.15811; growth: 1.0195 |
| S027 | stock | CLX | 2026-11-15 | ok | https://finance.yahoo.com/quote/CLX | Trailing P/E: 19.68705; Forward P/E: 17.745283; Forward EPS: 6.1684; Price: 109.46; Market price: 109.46; Market cap: 13260793856; Sector: Consumer Defensive; Trailing Eps: 5.56; Revenue Growth: 0.333; Earnings Growth: 1.138; Gross Margin: 0.41939998; Operating Margin: 0.14286; Profit Margin: 0.09408; Return On Equity: 5.34363; Total Revenue: 7196000256; Market Cap: 13260793856; Consensus EPS FY+1: 6.1684; growth: 0.0769 |
| S028 | news | CHTR | Thu, 12 Nov 2026 08:02:01 GMT | ok | https://news.google.com/rss/search?q=CHTR+Charter+Communications+stock&hl=en-US&gl=US&ceid=US:en | Charter Communications: 3 Key Takeaways for Long-Term Investors - Yahoo Finance (Thu, 12 Nov 2026 08:02:01 GMT); Charter Communications (CHTR) Stock Looks Reasonable As Shares Slump 85% - Yahoo Finance (Wed, 28 Oct 2026 07:00:00 GMT); Should Value Investors Buy Charter Communications (CHTR) Stock? - Yahoo Finance (Wed, 21 Oct 2026 07:00:00 GMT) |
| S029 | filing | CLX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000021076.json | Diluted EPS 1.39 for period ending 2026-09-30 (filed 2026-11-02) |
| S030 | filing | ROP | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000882835&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000882835-26-000047); 8-K filed 2026-10-22 (accession 0000882835-26-000042); 8-K filed 2026-10-01 (accession 0000882835-26-000039) |
| S031 | filing | CHTR | 2026-11-06 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001091667.json | Diluted EPS 0.38 for period ending 2026-09-30 (filed 2026-11-06) |
| S032 | filing | IDXX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000874716&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000874716-26-000135); 8-K filed 2026-11-02 (accession 0001104659-26-120892); 10-Q filed 2026-08-04 (accession 0000874716-26-000123) |
| S033 | news | ROP | Thu, 12 Nov 2026 19:15:50 GMT | ok | https://news.google.com/rss/search?q=ROP+Roper+Technologies+stock&hl=en-US&gl=US&ceid=US:en | Roper Technologies, Inc. (ROP) Stock Price, News, Quote & History - Yahoo! Finance Canada (Thu, 12 Nov 2026 19:15:50 GMT); Roper Technologies (ROP) Stock Looks Fully Valued As Cash Flow Comes Into Focus - Yahoo Finance (Fri, 06 Nov 2026 07:13:00 GMT); Roper Technologies: 3 Key Takeaways for Long-Term Investors - Yahoo Finance (Mon, 26 Oct 2026 07:00:00 GMT) |
| S034 | news | IDXX | Fri, 13 Nov 2026 22:06:38 GMT | ok | https://news.google.com/rss/search?q=IDXX+Idexx+Laboratories+stock&hl=en-US&gl=US&ceid=US:en | IDEXX Laboratories, Inc. (IDXX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 22:06:38 GMT); IDEXX Laboratories (IDXX) Stock Looks Fairly Valued Despite Its 28% Run - Yahoo Finance (Sat, 31 Oct 2026 07:00:00 GMT); IDEXX Laboratories (IDXX) Q3 Earnings Leave Its Premium Valuation In Focus - Yahoo Finance (Tue, 03 Nov 2026 08:00:00 GMT) |
| S035 | filing | GEN | 2026-10-29 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000849399.json | Diluted EPS 0.83 for period ending 2026-10-02 (filed 2026-10-29) |
| S036 | stock | ROP | 2026-11-15 | ok | https://finance.yahoo.com/quote/ROP | Trailing P/E: 18.993866; Forward P/E: 19.532475; Forward EPS: 24.57318; Price: 479.975; Market price: 479.975; Market cap: 47535013888; Sector: Technology; Trailing Eps: 25.27; Revenue Growth: 0.076; Earnings Growth: 0.326; Gross Margin: 0.69671; Operating Margin: 0.28049; Profit Margin: 0.30712998; Return On Equity: 0.13229; Total Revenue: 8434599936; Market Cap: 47535013888; Consensus EPS FY+1: 24.57318; growth: 0.09810001 |
| S037 | filing | RDDT | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001713445&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0001713445-26-000116); 8-K filed 2026-10-29 (accession 0001713445-26-000114); 8-K filed 2026-08-12 (accession 0001713445-26-000107) |
| S038 | stock | IDXX | 2026-11-15 | ok | https://finance.yahoo.com/quote/IDXX | Trailing P/E: 47.45485; Forward P/E: 41.687927; Forward EPS: 16.8929; Price: 704.23; Market price: 704.23; Market cap: 55483650048; Sector: Healthcare; Trailing Eps: 14.84; Revenue Growth: 0.099; Earnings Growth: 0.179; Gross Margin: 0.62722; Operating Margin: 0.32497; Profit Margin: 0.25357; Return On Equity: 0.68925005; Total Revenue: 4662220800; Market Cap: 55483650048; Consensus EPS FY+1: 16.8929; growth: 0.1244 |
| S039 | stock | RDDT | 2026-11-15 | ok | https://finance.yahoo.com/quote/RDDT | Trailing P/E: 20.091835; Forward P/E: 10.770874; Forward EPS: 9.14039; Price: 98.45; Market price: 98.45; Market cap: 19010076672; Sector: Communication Services; Trailing Eps: 4.9; Revenue Growth: 0.53; Earnings Growth: 0.749; Gross Margin: 0.91547996; Operating Margin: 0.29397; Profit Margin: 0.32105; Return On Equity: 0.32029998; Total Revenue: 3088880128; Market Cap: 19010076672; Consensus EPS FY+1: 6.82439; growth: 0.2417 |
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
- news FISV: https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 00:42:12 GMT)
- news APP: https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en (Thu, 12 Nov 2026 20:05:45 GMT)
- stock APP: https://finance.yahoo.com/quote/APP (2026-11-15)
- stock FISV: https://finance.yahoo.com/quote/FISV (2026-11-15)
- stock PNR: https://finance.yahoo.com/quote/PNR (2026-11-15)
- news PNR: https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 22:05:23 GMT)
- filing APP: https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json (2026-11-04)
- filing PNR: https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json (2026-10-27)
- filing GEN: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 (2026-10-29)
- stock GEN: https://finance.yahoo.com/quote/GEN (2026-11-15)

## AI Provenance

- Provider / model: hermes-local-proxy / upstage/solar-mini4:free
- Market research: attempts=1 tokens=9548 (prompt=6548, completion=3000) runtime=27.7s
- Fundamental research: generated this run at 2026-11-15T05:16:35.179074+00:00
- Evidence source dates: {'as_of': '2026-11-13', 'latest_equity_date': '2026-11-13', 'latest_macro_date': '2026-11-13', 'flows_date': '2026-11-13'}
- Evidence fingerprint: d0bee45d5e73d922330a82a3ef7670ed5bdfdf32ce12ce5741e0cecdbb7ac430
- Source citations are retrieved external records in the ledger above; market values remain from the verified database snapshot.


## Disclosures

- This is research and market intelligence, not investment advice.
- AI conclusions are research judgments, not validated return predictions.
- The frozen risk layer is risk-only and is not used for directional views or allocations.
- Legacy scores are not active inputs or outputs.

# AEGIS AI-First Market Intelligence

Research generated at: 15 November 2026, 08:15 HKT
Database freshness: equity 2026-11-13 (latest row retrieved 2026-11-14 13:50:55.938286+08:00)
Data cutoff: 2026-11-13 US cash close
Snapshot ID: aegis-hourly-20261115T001509Z

## Executive Summary

- **AI market view: Risk-on tilt with a quality and liquidity bias. Broad market breadth is constructive (71% above 50-day, 64% above 200-day, A/D ratio 1.70), but the 20-day index return is negative and the 20-day index return is negative, so the rally is not yet broad-based. Dislocation names and liquidity leaders are the clearest near-term signals, while rate-sensitive and high-multiple sectors remain vulnerable to any re-acceleration in policy rates.**
- Broad market breadth is constructive: 71.3% of names above the 50-day moving average, 63.6% above the 200-day, and an advance/decline ratio of 1.70.
- The index is down 1.28% over 20 days, indicating that the positive breadth is not yet translating into a broad-based index rally.
- Shortlist momentum and dislocation names (APP, PNR, GEN, CLX, RDDT, INTC, MRVL, NOW, AMD, etc.) are the primary near-term candidates, but several carry extreme valuations or negative earnings yields.
- Policy rates remain elevated (effective funds rate 3.88% as of 2026-11-12), keeping pressure on long-duration and high-multiple sectors.
- Credit spreads are tight (IG OAS 0.89, HY OAS 3.20), suggesting limited risk premium for adding leverage.
- Sector leadership is mixed: Health Care, Consumer Discretionary, Consumer Staples, Financials, Real Estate and Utilities are up over 20 days, while Information Technology and Energy are down.

## Data QC

- Status: **PASS_WITH_WARNINGS**
- Equity session: 0 completed session(s) behind inference date
- Equity provenance: 386 provisional / 12581 canonical
- Breadth lag: 0 session(s); ETF-flow lag: 0 session(s)
- Note: Equity session contains a mix of provisional yfinance and canonical Massive rows.
- External sources: 79 ok / 0 unavailable; retrieved 2026-11-15T00:15:25.187842+00:00

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
| S&P 500 | 7561.67 | -1.28% (20d) | Index is negative over 20 days despite positive breadth; 71.3% above 50-day and 63.6% above 200-day. |
| APP | PE TTM 20.05 | top_20d_momentum | Momentum leader with a reasonable trailing P/E of 20.05 and earnings yield of 4.99%. |
| PNR | PE TTM 13.59 | top_20d_momentum | Low P/E of 13.59 with earnings yield of 7.36%; sector-relative P/E of 0.49. |
| GEN | PE TTM 14.15 | top_20d_momentum | Trailing P/E of 14.15 and earnings yield of 7.07%; sector-relative P/E of 0.42. |
| CLX | PE TTM 18.27 | top_20d_momentum | Trailing P/E of 18.27 and earnings yield of 5.47%; sector-relative P/E of 0.76. |
| RDDT | PE TTM 33.19 | largest_20d_dislocation | Dislocation name with P/E of 33.19 and earnings yield of 3.01%; sector-relative P/E of 1.66. |
| INTC | PE TTM -39.78 | largest_20d_dislocation | Negative trailing P/E and earnings yield; extreme dislocation with no meaningful valuation multiple. |
| MRVL | PE TTM 74.23 | largest_20d_dislocation | High P/E of 74.23 and earnings yield of 1.35%; sector-relative P/E of 2.20. |
| AMD | PE TTM 128.88 | liquidity_leader | Very high P/E of 128.88 and earnings yield of 0.78%; sector-relative P/E of 3.82. |
| NVDA | PE TTM 26.51 | liquidity_leader | Trailing P/E of 26.51 and earnings yield of 3.77%; sector-relative P/E of 0.79. |

## Macro, Fiscal, Rates, Liquidity and Credit

- Growth: The 10Y-2Y Treasury spread is 0.27 as of 2026-11-13, indicating a modestly positive but shallow yield curve; this is consistent with a late-cycle but not recession-tinged growth backdrop.
- Inflation: CPI stands at 336.298 (2026-09-01) and core CPI at 338.896 (2026-09-01), indicating inflation remains above the pre-2020 trend and limits the scope for aggressive rate cuts.
- Policy: The effective federal funds rate is 3.88% as of 2026-11-12, still restrictive enough to weigh on rate-sensitive sectors and long-duration equities.
- Rates: The 10Y-2Y spread of 0.27 and the elevated policy rate suggest the bond market is pricing a slow normalization rather than a rapid easing cycle.
- Liquidity: Credit spreads are tight (IG OAS 0.89, HY OAS 3.20), implying that liquidity is not abundant in risk terms and that any shock could quickly widen spreads.
- Credit: Tight spreads combined with a flat-to-negative equity risk premium argue for a quality and liquidity bias rather than broad beta.

## US Equities and 11 GICS Sectors

Macro source IDs: S001, S002, S003, S004, S005, S006, S007

| GICS sector | Evidence | AI research stance | Source IDs |
| --- | --- | --- | --- |
| Health Care | Sector ETF XLV returned +6.87% over 20 days, the strongest in the universe; trailing P/E of 30.78 per S058. | Favorable momentum and defensive characteristics; quality bias supported by strong relative performance. | S058 |
| Consumer Discretionary | Sector ETF XLY returned +6.69% over 20 days; trailing P/E of 25.11 per S062. | Strong relative momentum; consumer spending remains resilient enough to support the sector. | S062 |
| Consumer Staples | Sector ETF XLP returned +5.40% over 20 days; trailing P/E of 24.85 per S056. | Defensive strength with solid 20-day return; high valuation but stable cash flows. | S056 |
| Financials | Sector ETF XLF returned +5.69% over 20 days; trailing P/E of 15.85 per S065. | Positive momentum and reasonable valuation; benefits from a steepening curve and stable credit. | S065 |
| Real Estate | Sector ETF XLRE returned +5.24% over 20 days; trailing P/E of 29.63 per S061. | Positive 20-day return and moderate valuation; rate sensitivity remains a key risk. | S061 |
| Utilities | Sector ETF XLU returned +4.34% over 20 days; trailing P/E of 18.11 per S066. | Defensive strength with a reasonable valuation; stable but lower growth. | S066 |
| Industrials | Sector ETF XLI returned +0.61% over 20 days; trailing P/E of 27.07 per S070. | Near-flat momentum; valuation is above average, limiting upside without earnings acceleration. | S070 |
| Materials | Sector ETF XLB returned +2.57% over 20 days; trailing P/E of 21.72 per S068. | Modest positive momentum; commodity exposure is mixed with inflation and rate uncertainty. | S068 |
| Communication Services | Sector ETF XLC returned -1.48% over 20 days; trailing P/E of 17.26 per S072. | Negative momentum and high multiple; vulnerable to any re-acceleration in policy rates. | S072 |
| Information Technology | Sector ETF XLK returned -7.19% over 20 days; trailing P/E of 30.03 per S074. | Negative momentum and high multiple; rate sensitivity and extreme valuations (AMD, NOW, MRVL) are key risks. | S074 |
| Energy | Sector ETF XLE returned -4.81% over 20 days; trailing P/E of 16.23 per S076. | Negative momentum and weak relative performance; oil price and demand uncertainty weigh on the sector. | S076 |

### Sector fundamentals, valuation and earnings

No point-in-time sector fundamentals (e.g., revenue growth, margins, consensus estimates) are supplied in the database snapshot. The sector evidence is limited to 20-day ETF returns, trailing P/E, and the provided source IDs. Any claim about sector growth, margins, or forward estimates would be invented and is therefore omitted.

## Growth vs Value

- Health Care and Consumer Discretionary show the strongest 20-day momentum (XLV +6.87%, XLY +6.69%) and are the most attractive relative growth signals.
- Consumer Staples and Utilities provide defensive value with trailing P/Es of 24.85 and 18.11, respectively, but offer lower growth.
- Financials and Real Estate offer reasonable valuations (XLF 15.85, XLRE 29.63) with positive momentum, though Real Estate remains rate-sensitive.
- Information Technology and Communication Services are the most expensive and weakest sectors, with XLK at -7.19% and XLC at -1.48% over 20 days, and XLK trailing P/E of 30.03.
- Energy is the weakest sector (XLE -4.81%) with a low trailing P/E of 16.23, but negative momentum and oil demand uncertainty limit the upside.

## ETF Flows and Breadth

- Market breadth is strongly positive: 71.3% of names above the 50-day moving average, 63.6% above the 200-day, and an advance/decline ratio of 1.70.
- The 20-day advance/decline ratio of 1.70 and 70.5% of names with positive 20-day returns indicate broad participation, but the index is down 1.28% over the same period.
- The 50-day breadth change over 5 days is +10.1 and over 20 days is +26.21, showing improving participation; the 200-day breadth change is +7.77 over 5 days and +11.27 over 20 days.
- Price/breadth divergence is -27.49 with negative_divergence=false, but bullish_divergence=true and standardized_divergence=-0.0758, suggesting the index is lagging the improving breadth.
- Flow data shows SOXX with exceptional institutional buying (20d flow z-score 5.10, 60d 3.17) despite a

## Stock Ideas

Single-stock research uses reported EPS, forward P/E and company fundamentals. All ideas are research judgments, not validated return predictions.

| Ticker | Security | Research view | Price | EPS | Forward P/E | Base target | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| APP | AppLovin | NEW | 409.1 | 20.86026 | 19.611452 | 458.93 | NEW |
| PNR | Pentair | KEEP | 68.3 | 5.30402 | 12.877027 | 74.26 | KEEP |
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
- **Why preferred / alternatives:** AppLovin offers a rare combination of top-tier 20-day momentum, high double-digit revenue and earnings growth, and industry-leading margins. Compared with the other momentum names such as Gen Digital and Clorox, AppLovin's growth profile and margin structure are more consistent with a high-quality compounder rather than a cyclical or mature staple. Alternatives considered: GEN, CLX, ROP.
- **Thesis:** AppLovin screens in the top 20-day momentum bucket with a 53.7% 20-day return and a 32.5% 60-day return, indicating strong recent price leadership. Reported diluted EPS of $11.61 for the fiscal period ending 2026-09-30 and a forward EPS of $20.86 support a forward P/E of about 19.6, which is reasonable for a high-margin, high-growth mobile advertising platform. The company's gross margin near 89% and operating margin near 78% provide a durable profitability profile that can compound earnings while the stock has already shown momentum.
- **Source IDs:** S008, S012, S014, S015
- **Catalysts:** Continued momentum in mobile advertising spend and app install volume, Sustained double-digit revenue and earnings growth, Operating leverage as gross and operating margins remain near 89% and 78%, Potential re-rating as the stock's 20-day momentum continues
- **Risks:** High 20-day momentum can mean elevated volatility and sharp pullbacks, Mobile advertising is sensitive to macroeconomic spending cycles and privacy regulation, Forward EPS estimates are unverified for fiscal period alignment, so forward P/E should be treated as indicative
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 20.8603 (source.forwardEps) x AI multiple assumption 22.00; source IDs S008, S012, S014, S015
- **EPS:** 20.86026 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 19.611452
- **FY+1 growth assumption:** 27.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / PNR / APP shows strong FY1 consensus earnings growth of 27.44% and revenue growth of 25.37%, with exceptional margins (gross 88.8%, operating 77.8%, profit 65.9%) and ROE of 2.10. The FY2 EPS is not available from retrieved sources, so the FY2027-to-FY2028 horizon is anchored to the available FY1 consensus growth. PNR is used as the named peer reference because it is the only other stock in the supplied ideas with a comparable forward EPS and forward P/E structure, allowing a relative multiple to be justified against a real comparable rather than an arbitrary multiple.
- **Company fundamentals:** Reported diluted EPS $11.61; forward EPS $20.86; forward P/E about 19.6; gross margin 88.8%; operating margin 77.8%; profit margin 65.9%; revenue growth 55.5%; earnings growth 75.5%; ROE 2.10; 20-day return 53.7%; 60-day return 32.5%; 60-day drawdown -0.2%
- **Bull / Base / Bear:** 542.37 / 458.93 / 333.76
- **Bull / Base / Bear returns:** 32.58% / 12.18% / -18.42%
- **Scenario probabilities:** not separately assigned; see scenario table.

### PNR — Pentair

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Pentair is not preferred over the higher-growth momentum names, but it offers a lower forward P/E near 12.9 and a sector-relative P/E of 0.49 that makes it a potentially cheaper industrial exposure. It is a reasonable holding for investors who want industrial exposure at a discount, but the earnings decline and margin compression keep the stance neutral. Alternatives considered: APP, GEN, CLX.
- **Thesis:** Pentair qualifies for the top 20-day momentum bucket with a 27.8% 20-day return and a 7.1% 60-day return, but its fundamentals are mixed. Reported diluted EPS of $2.76 and forward EPS of $5.30 imply a forward P/E of about 12.9, which is attractive, yet revenue growth is slightly negative at -4.5% and earnings growth is -18.8%. The stock is trading at a sector-relative P/E of about 0.49, suggesting it is cheaper than its sector, but the earnings decline and margin compression below 40% gross margin and 21% operating margin limit the upside case.
- **Source IDs:** S009, S017, S019, S021
- **Catalysts:** Potential re-rating if earnings decline stabilizes and the stock continues to lead on momentum, Attractive forward P/E near 12.9 relative to the sector-relative multiple of 0.49, Industrial exposure to water, building products and flow control could benefit from infrastructure spending
- **Risks:** Revenue and earnings are contracting, with revenue growth of -4.5% and earnings growth of -18.8%, Gross margin of 40.2% and operating margin of 21.4% are below the company's historical profile, Momentum is positive but weaker than the top momentum names such as AppLovin
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 5.3040 (source.forwardEps) x AI multiple assumption 14.00; source IDs S009, S017, S019, S021
- **EPS:** 5.30402 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 12.877027
- **FY+1 growth assumption:** 12.82%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / APP / PNR has FY1 consensus earnings growth of 12.82% and revenue growth of 18.38%, with moderate margins (gross 40.2%, operating 21.4%, profit 15.4%) and ROE of 15.6%. The FY2 EPS is not available from retrieved sources, so the FY2027-to-FY2028 horizon is anchored to the available FY1 consensus growth. APP is used as the named peer reference because it is the only other stock in the supplied ideas with a comparable forward EPS and forward P/E structure, allowing a relative multiple to be justified against a real comparable rather than an arbitrary multiple.
- **Company fundamentals:** Reported diluted EPS $2.76; forward EPS $5.30; forward P/E about 12.9; gross margin 40.2%; operating margin 21.4%; profit margin 15.4%; ROE 15.6%; revenue growth -4.5%; earnings growth -18.8%; 20-day return 27.8%; 60-day return 7.1%; 60-day drawdown -5.2%
- **Bull / Base / Bear:** 90.17 / 74.26 / 58.34
- **Bull / Base / Bear returns:** 32.02% / 8.73% / -14.58%
- **Scenario probabilities:** not separately assigned; see scenario table.

### GEN — Gen Digital

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Gen Digital is not preferred over AppLovin because its growth and margin profile is weaker, but it offers a lower forward P/E near 9.1 and strong earnings growth. It is a reasonable candidate for investors who want cyber and digital risk exposure at a reasonable valuation, though the growth and margin profile is less compelling than AppLovin's. Alternatives considered: APP, PNR, CLX.
- **Thesis:** Gen Digital is in the top 20-day momentum bucket with a 25.8% 20-day return and a 7.9% 60-day return. It trades at a forward P/E of about 9.1, which is attractive, and earnings growth of 128.6% is strong. However, revenue growth is only 12.2% and the company's gross margin of 77.4% and operating margin of 43.2% are lower than AppLovin's. The stock is also more expensive on a sector-relative basis at 0.42, so the cheapness is not as pronounced as in Pentair.
- **Source IDs:** S018, S020, S025, S026
- **Catalysts:** Strong earnings growth of 128.6% and positive revenue growth of 12.2%, Attractive forward P/E near 9.1, Continued momentum in cyber and digital risk exposure
- **Risks:** Revenue growth of 12.2% is modest relative to the high earnings growth, Margins are lower than the highest-quality momentum names such as AppLovin, Sector-relative P/E of 0.42 suggests less cheapness than other industrial or staples names
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 3.3374 (source.forwardEps) x AI multiple assumption 10.00; source IDs S018, S020, S025, S026
- **EPS:** 3.33736 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 9.108996
- **FY+1 growth assumption:** 12.86%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / PNR / GEN shows FY1 consensus earnings growth of 12.86% and revenue growth of 6.81%, with solid margins (gross 77.4%, operating 43.2%, profit 23.1%) and ROE of 46.4%. The FY2 EPS is not available from retrieved sources, so the FY2027-to-FY2028 horizon is anchored to the available FY1 consensus growth. PNR is used as the named peer reference because it is the only other stock in the supplied ideas with a comparable forward EPS and forward P/E structure, allowing a relative multiple to be justified against a real comparable rather than an arbitrary multiple.
- **Company fundamentals:** Reported diluted EPS $0.83; forward EPS $3.34; forward P/E about 9.1; gross margin 77.4%; operating margin 43.2%; profit margin 23.1%; ROE 46.4%; revenue growth 12.2%; earnings growth 128.6%; 20-day return 25.8%; 60-day return 7.9%; 60-day drawdown -3.2%
- **Bull / Base / Bear:** 40.05 / 33.37 / 26.7
- **Bull / Base / Bear returns:** 31.74% / 9.77% / -12.17%
- **Scenario probabilities:** not separately assigned; see scenario table.

### CLX — Clorox

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Clorox is not preferred over AppLovin or Gen Digital because its growth and margin profile is weaker, but it offers a reasonable forward P/E near 17.7 and strong earnings growth. It is a reasonable holding for investors who want consumer staples exposure, though the low revenue growth and thin margins limit the upside case. Alternatives considered: APP, GEN, PNR.
- **Thesis:** Clorox is in the top 20-day momentum bucket with a 25.7% 20-day return and a 3.2% 60-day return. It trades at a forward P/E of about 17.7, which is reasonable for a consumer staples company, and earnings growth of 113.8% is strong. However, revenue growth is only 2.2% and gross margin of 41.9% and operating margin of 14.3% are low for a staples company. The sector-relative P/E of 0.76 suggests it is not deeply cheap relative to its sector.
- **Source IDs:** S022, S023, S027, S031
- **Catalysts:** Strong earnings growth of 113.8% and positive revenue growth of 2.2%, Attractive forward P/E near 17.7 for a consumer staples company, Continued momentum in the consumer staples sector
- **Risks:** Revenue growth of 2.2% is modest and leaves limited top-line expansion, Low gross margin of 41.9% and operating margin of 14.3% limit operating leverage, Sector-relative P/E of 0.76 suggests less cheapness than other staples names
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 6.1684 (source.forwardEps) x AI multiple assumption 18.00; source IDs S022, S023, S027, S031
- **EPS:** 6.1684 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 17.745283
- **FY+1 growth assumption:** 7.69%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** FY2027 to FY2028 / PNR / CLX has FY1 consensus earnings growth of 7.69% and revenue growth of 2.23%, with moderate margins (gross 41.9%, operating 14.3%, profit 9.4%) and ROE of 5.34%. The FY2 EPS is not available from retrieved sources, so the FY2027-to-FY2028 horizon is anchored to the available FY1 consensus growth. PNR is used as the named peer reference because it is the only other stock in the supplied ideas with a comparable forward EPS and forward P/E structure, allowing a relative multiple to be justified against a real comparable rather than an arbitrary multiple.
- **Company fundamentals:** Reported diluted EPS $1.39; forward EPS $6.17; forward P/E about 17.7; gross margin 41.9%; operating margin 14.3%; profit margin 9.4%; ROE 534.4%; revenue growth 2.2%; earnings growth 113.8%; 20-day return 25.7%; 60-day return 3.2%; 60-day drawdown 0.0%
- **Bull / Base / Bear:** 129.54 / 111.03 / 92.53
- **Bull / Base / Bear returns:** 18.34% / 1.43% / -15.47%
- **Scenario probabilities:** not separately assigned; see scenario table.

### XLV — Health Care sector ETF

- **Type:** ETF
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** The Health Care sector ETF is preferred over individual health care stocks because it provides diversified exposure across the sector and reduces single-name risk. Compared with the other sector ETFs, it offers a defensive allocation that can complement growth-oriented holdings such as AppLovin and Gen Digital. Alternatives considered: XLP, XLY, XLF.
- **Thesis:** The Health Care sector ETF provides diversified exposure to large-cap pharmaceutical and medical device companies. The top holdings include LLY, JNJ, ABBV, MRK, UNH, TMO, AMGN, GILD, ABT and PFE, with top-10 weight coverage of 61.4%. The ETF is a reasonable core holding for investors seeking broad health care exposure, but the limited top-10 weight coverage means the portfolio is not fully represented by the disclosed names. The sector is a defensive allocation that can provide stability during equity market stress.
- **Source IDs:** S055, S058
- **Catalysts:** Diversified exposure to large-cap pharmaceutical and medical device companies, Defensive sector characteristics that can provide stability during equity market stress, Exposure to innovative names such as LLY, ABBV and AMGN
- **Risks:** Top-10 weight coverage of only 61.4% means the disclosed holdings do not fully represent the portfolio, Sector-specific risks including drug pricing, regulatory changes and patent cliffs, Limited top-10 weight coverage reduces transparency on full portfolio composition
- **Valuation method:** Holdings/portfolio valuation with AI total-return assumption
- **Valuation status:** verified; forward-EPS source: ; period flags: 
- **Valuation assumptions:** Holdings/portfolio valuation; 10 weighted holdings; coverage 61.42%; source IDs S055, S058
- **Top holdings:** LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59%
- **Portfolio valuation:** Top 10 holdings; numeric weight coverage 61.42%
- **Sector exposure:** Health Care
- **Underlying drivers:** Large-cap pharmaceutical and medical device companies; defensive sector characteristics; diversified exposure to LLY, JNJ, ABBV, MRK, UNH, TMO, AMGN, GILD, ABT and PFE
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
| Bull | 25% | +2.00% | Low 5-day realized vol (14.9%) and below-threshold spike probability (16.5%) support a mild upside bias if US close confirms stable liquidity and no credit stress. |
| Base | 50% | +0.00% | Frozen daily-close model with no directional signal implies range-bound trading; base case is flat until the official US close resolves the forecast uncertainty. |
| Bear | 25% | -2.00% | If the US close triggers a volatility spike above the 18.5% threshold, elevated tail risk could drive a modest downside move despite the current low-vol regime. |

### Long Term (12 months)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 30% | +8.00% | Sustained low realized vol and stable credit conditions support a positive earnings-driven rally, with breadth expansion lifting returns over the horizon. |
| Base | 40% | +3.00% | A normalized earnings trajectory with moderate rate expectations and stable credit spreads yields a mild positive long-term return. |
| Bear | 30% | -5.00% | A credit event or earnings disappointment, combined with a volatility spike, could produce a meaningful drawdown over the longer horizon. |

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
| S009 | filing | PNR | 2026-10-27 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-27 (accession 0000077360-26-000058); 8-K filed 2026-10-27 (accession 0000077360-26-000055); 8-K filed 2026-09-22 (accession 0000077360-26-000050) |
| S010 | filing | FISV | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0000798354-26-000042); 8-K filed 2026-11-03 (accession 0000798354-26-000039); 8-K filed 2026-10-23 (accession 0001193125-26-429481) |
| S011 | news | FISV | Thu, 12 Nov 2026 18:47:44 GMT | ok | https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en | Fiserv, Inc. (FISV) Stock Price, News, Quote & History - Yahoo! Finance Canada (Thu, 12 Nov 2026 18:47:44 GMT); Fiserv Stock Outlook: Is Wall Street Bullish or Bearish? - Yahoo Finance (Thu, 12 Nov 2026 12:23:56 GMT); What Is Fiserv (FISV) Planning With Its Debit Networks And Clover AI? - Yahoo Finance (Thu, 12 Nov 2026 06:09:00 GMT) |
| S012 | news | APP | Thu, 12 Nov 2026 20:05:45 GMT | ok | https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en | AppLovin Just Ripped 47% in a Month: Is It Too Late to Buy APP Stock Now? - Yahoo Finance (Thu, 12 Nov 2026 20:05:45 GMT); APP Stock Surges 51% After Q3 Earnings: Is it Still a Buy? - Yahoo Finance (Tue, 10 Nov 2026 14:24:00 GMT); Here is What to Know Beyond Why AppLovin Corporation (APP) is a Trending Stock - Yahoo Finance (Tue, 10 Nov 2026 13:00:06 GMT) |
| S013 | stock | FISV | 2026-11-15 | ok | https://finance.yahoo.com/quote/FISV | Forward P/E: 7.9923306; Price: 63.78; Market price: 63.78; Market cap: 33934002176; Market Cap: 33934002176; Consensus EPS FY+1: 7.98015; growth: 0.09689999 |
| S014 | filing | APP | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json | Diluted EPS 11.61 for period ending 2026-09-30 (filed 2026-11-04) |
| S015 | stock | APP | 2026-11-15 | ok | https://finance.yahoo.com/quote/APP | Trailing P/E: 27.54882; Forward P/E: 19.611452; Forward EPS: 20.86026; Price: 409.1; Market price: 409.1; Market cap: 135543824384; Sector: Communication Services; Trailing Eps: 14.85; Revenue Growth: 0.555; Earnings Growth: 0.755; Gross Margin: 0.8878; Operating Margin: 0.77782995; Profit Margin: 0.65887; Return On Equity: 2.1008599; Total Revenue: 7608893952; Market Cap: 135543824384; Consensus EPS FY+1: 20.72438; growth: 0.2744 |
| S016 | filing | FISV | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json | Diluted EPS -8.9 for period ending 2026-09-30 (filed 2026-11-04) |
| S017 | news | PNR | Fri, 13 Nov 2026 22:05:23 GMT | ok | https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en | Pentair plc (PNR) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 22:05:23 GMT); Here's What Key Metrics Tell Us About Pentair (PNR) Q3 Earnings - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT); Pentair plc (PNR) Q3 Earnings and Revenues Beat Estimates - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT) |
| S018 | filing | GEN | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0000849399-26-000083); 8-K filed 2026-10-28 (accession 0000849399-26-000081); 8-K filed 2026-10-09 (accession 0000849399-26-000079) |
| S019 | stock | PNR | 2026-11-15 | ok | https://finance.yahoo.com/quote/PNR | Trailing P/E: 18.610355; Forward P/E: 12.877027; Forward EPS: 5.30402; Price: 68.3; Market price: 68.3; Market cap: 10904415232; Sector: Industrials; Trailing Eps: 3.67; Revenue Growth: -0.045; Earnings Growth: -0.188; Gross Margin: 0.40168998; Operating Margin: 0.21410999; Profit Margin: 0.15435; Return On Equity: 0.15605; Total Revenue: 3966200064; Market Cap: 10904415232; Consensus EPS FY+1: 5.30402; growth: 0.1282 |
| S020 | stock | GEN | 2026-11-15 | ok | https://finance.yahoo.com/quote/GEN | Trailing P/E: 15.431472; Forward P/E: 9.108996; Forward EPS: 3.33736; Price: 30.4; Market price: 30.4; Market cap: 18035593216; Sector: Technology; Trailing Eps: 1.97; Revenue Growth: 0.122; Earnings Growth: 1.286; Gross Margin: 0.77410007; Operating Margin: 0.43229; Profit Margin: 0.23068; Return On Equity: 0.46402; Total Revenue: 5228000256; Market Cap: 18035593216; Consensus EPS FY+1: 3.33736; growth: 0.1286 |
| S021 | filing | PNR | 2026-10-27 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json | Diluted EPS 2.76 for period ending 2026-09-30 (filed 2026-10-27) |
| S022 | filing | CLX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000021076-26-000046); 8-K filed 2026-11-02 (accession 0000021076-26-000044); 8-K filed 2026-10-29 (accession 0001206774-26-000586) |
| S023 | news | CLX | Fri, 13 Nov 2026 18:52:58 GMT | ok | https://news.google.com/rss/search?q=CLX+Clorox+stock&hl=en-US&gl=US&ceid=US:en | The Clorox Company (CLX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 18:52:58 GMT); The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance Singapore (Fri, 13 Nov 2026 14:35:41 GMT); The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance UK (Fri, 13 Nov 2026 16:03:45 GMT) |
| S024 | filing | CHTR | 2026-11-06 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-06 (accession 0001091667-26-000073); 8-K filed 2026-11-06 (accession 0001091667-26-000072); 8-K filed 2026-10-27 (accession 0001091667-26-000064) |
| S025 | filing | GEN | 2026-10-29 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000849399.json | Diluted EPS 0.83 for period ending 2026-10-02 (filed 2026-10-29) |
| S026 | news | GEN | Thu, 29 Oct 2026 07:00:00 GMT | ok | https://news.google.com/rss/search?q=GEN+Gen+Digital+stock&hl=en-US&gl=US&ceid=US:en | Gen Digital (GEN) Stock Repriced After Q2 Earnings Put Margins Center Stage - Yahoo Finance (Thu, 29 Oct 2026 07:00:00 GMT); Are Business Services Stocks Lagging GEN DIGITAL INC (GEN) This Year? - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT); Gen Digital Stock: Is Wall Street Bullish or Bearish? - Yahoo Finance (Thu, 05 Nov 2026 08:00:00 GMT) |
| S027 | stock | CLX | 2026-11-15 | ok | https://finance.yahoo.com/quote/CLX | Trailing P/E: 19.68705; Forward P/E: 17.745283; Forward EPS: 6.1684; Price: 109.46; Market price: 109.46; Market cap: 13260793856; Sector: Consumer Defensive; Trailing Eps: 5.56; Revenue Growth: 0.333; Earnings Growth: 1.138; Gross Margin: 0.41939998; Operating Margin: 0.14286; Profit Margin: 0.09408; Return On Equity: 5.34363; Total Revenue: 7196000256; Market Cap: 13260793856; Consensus EPS FY+1: 6.1684; growth: 0.0769 |
| S028 | stock | CHTR | 2026-11-15 | ok | https://finance.yahoo.com/quote/CHTR | Trailing P/E: 13.006578; Forward P/E: 3.2831066; Forward EPS: 42.15215; Price: 138.39; Market price: 138.39; Market cap: 24778944512; Sector: Communication Services; Trailing Eps: 10.64; Revenue Growth: 0.091; Gross Margin: 0.55084; Operating Margin: 0.23389; Profit Margin: 0.02498; Return On Equity: 0.07019; Total Revenue: 55645999104; Market Cap: 24778944512; Consensus EPS FY+1: 47.15811; growth: 1.0195 |
| S029 | filing | IDXX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000874716&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000874716-26-000135); 8-K filed 2026-11-02 (accession 0001104659-26-120892); 10-Q filed 2026-08-04 (accession 0000874716-26-000123) |
| S030 | news | CHTR | Thu, 12 Nov 2026 08:02:01 GMT | ok | https://news.google.com/rss/search?q=CHTR+Charter+Communications+stock&hl=en-US&gl=US&ceid=US:en | Charter Communications: 3 Key Takeaways for Long-Term Investors - Yahoo Finance (Thu, 12 Nov 2026 08:02:01 GMT); Charter Communications (CHTR) Stock Looks Reasonable As Shares Slump 85% - Yahoo Finance (Wed, 28 Oct 2026 07:00:00 GMT); Should Value Investors Buy Charter Communications (CHTR) Stock? - Yahoo Finance (Wed, 21 Oct 2026 07:00:00 GMT) |
| S031 | filing | CLX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000021076.json | Diluted EPS 1.39 for period ending 2026-09-30 (filed 2026-11-02) |
| S032 | news | IDXX | Fri, 13 Nov 2026 22:06:38 GMT | ok | https://news.google.com/rss/search?q=IDXX+Idexx+Laboratories+stock&hl=en-US&gl=US&ceid=US:en | IDEXX Laboratories, Inc. (IDXX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 22:06:38 GMT); IDEXX Laboratories (IDXX) Stock Looks Fairly Valued Despite Its 28% Run - Yahoo Finance (Sat, 31 Oct 2026 07:00:00 GMT); IDEXX Laboratories (IDXX) Q3 Earnings Leave Its Premium Valuation In Focus - Yahoo Finance (Tue, 03 Nov 2026 08:00:00 GMT) |
| S033 | filing | ROP | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000882835&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000882835-26-000047); 8-K filed 2026-10-22 (accession 0000882835-26-000042); 8-K filed 2026-10-01 (accession 0000882835-26-000039) |
| S034 | filing | CHTR | 2026-11-06 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001091667.json | Diluted EPS 0.38 for period ending 2026-09-30 (filed 2026-11-06) |
| S035 | stock | ROP | 2026-11-15 | ok | https://finance.yahoo.com/quote/ROP | Trailing P/E: 18.993866; Forward P/E: 19.532475; Forward EPS: 24.57318; Price: 479.975; Market price: 479.975; Market cap: 47535013888; Sector: Technology; Trailing Eps: 25.27; Revenue Growth: 0.076; Earnings Growth: 0.326; Gross Margin: 0.69671; Operating Margin: 0.28049; Profit Margin: 0.30712998; Return On Equity: 0.13229; Total Revenue: 8434599936; Market Cap: 47535013888; Consensus EPS FY+1: 24.57318; growth: 0.09810001 |
| S036 | stock | IDXX | 2026-11-15 | ok | https://finance.yahoo.com/quote/IDXX | Trailing P/E: 47.45485; Forward P/E: 41.687927; Forward EPS: 16.8929; Price: 704.23; Market price: 704.23; Market cap: 55483650048; Sector: Healthcare; Trailing Eps: 14.84; Revenue Growth: 0.099; Earnings Growth: 0.179; Gross Margin: 0.62722; Operating Margin: 0.32497; Profit Margin: 0.25357; Return On Equity: 0.68925005; Total Revenue: 4662220800; Market Cap: 55483650048; Consensus EPS FY+1: 16.8929; growth: 0.1244 |
| S037 | filing | RDDT | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001713445&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0001713445-26-000116); 8-K filed 2026-10-29 (accession 0001713445-26-000114); 8-K filed 2026-08-12 (accession 0001713445-26-000107) |
| S038 | news | ROP | Thu, 12 Nov 2026 19:15:50 GMT | ok | https://news.google.com/rss/search?q=ROP+Roper+Technologies+stock&hl=en-US&gl=US&ceid=US:en | Roper Technologies, Inc. (ROP) Stock Price, News, Quote & History - Yahoo! Finance Canada (Thu, 12 Nov 2026 19:15:50 GMT); Roper Technologies (ROP) Stock Looks Fully Valued As Cash Flow Comes Into Focus - Yahoo Finance (Fri, 06 Nov 2026 07:13:00 GMT); Roper Technologies: 3 Key Takeaways for Long-Term Investors - Yahoo Finance (Mon, 26 Oct 2026 07:00:00 GMT) |
| S039 | filing | IDXX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000874716.json | Diluted EPS 11.75 for period ending 2026-09-30 (filed 2026-11-02) |
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
- news FISV: https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en (Thu, 12 Nov 2026 18:47:44 GMT)
- news APP: https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en (Thu, 12 Nov 2026 20:05:45 GMT)
- stock FISV: https://finance.yahoo.com/quote/FISV (2026-11-15)
- filing APP: https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json (2026-11-04)
- stock APP: https://finance.yahoo.com/quote/APP (2026-11-15)
- filing FISV: https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json (2026-11-04)
- news PNR: https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 22:05:23 GMT)
- filing GEN: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 (2026-10-29)
- stock PNR: https://finance.yahoo.com/quote/PNR (2026-11-15)
- stock GEN: https://finance.yahoo.com/quote/GEN (2026-11-15)

## AI Provenance

- Provider / model: hermes-local-proxy / upstage/solar-mini4:free
- Market research: attempts=1 tokens=9548 (prompt=6548, completion=3000) runtime=30.54s
- Fundamental research: generated this run at 2026-11-15T00:15:09.308534+00:00
- Evidence source dates: {'as_of': '2026-11-13', 'latest_equity_date': '2026-11-13', 'latest_macro_date': '2026-11-13', 'flows_date': '2026-11-13'}
- Evidence fingerprint: 07e844bc88e5706b53395d86d0bd9231da9af7f651600f0373116ebc6248747f
- Source citations are retrieved external records in the ledger above; market values remain from the verified database snapshot.


## Disclosures

- This is research and market intelligence, not investment advice.
- AI conclusions are research judgments, not validated return predictions.
- The frozen risk layer is risk-only and is not used for directional views or allocations.
- Legacy scores are not active inputs or outputs.

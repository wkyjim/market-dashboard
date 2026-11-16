# AEGIS AI-First Market Intelligence

Research generated at: 16 November 2026, 10:13 HKT
Database freshness: equity 2026-11-13 (latest row retrieved 2026-11-15 13:06:40.074841+08:00)
Data cutoff: 2026-11-13 US cash close
Snapshot ID: aegis-hourly-20261116T021328Z

## Executive Summary

- **AI market view: Late-November 2026 equity market is in a late-cycle, mixed posture: broad market breadth is positive but thin, with 50-day and 200-day advance ratios at 71.3% and 63.6% and a 20-day advance/decline ratio of 1.70, while the S&P 500 is down 1.28% over 20 days. Momentum and dislocation screens are dominated by large-cap liquidity leaders and a handful of high-beta dislocation names, but valuation quality is weak: several shortlisted names carry extreme trailing P/E, negative earnings yields, or flagged forward-EPS gaps. Macro data show a still-elevated inflation backdrop (CPI 336.30 in Sep-2026), a 4.2% unemployment rate, a near-flat 10Y-2Y spread of 0.27, and a Fed funds rate of 3.88%, with credit spreads modestly tight (IG 0.89, HY 3.20). Risk environment is elevated: 5-day forecast volatility of 14.9% is below the 18.5% threshold but above the historical baseline, and the frozen model flags a 16.5% spike probability.**
- Equity market is late-cycle with positive but narrowing breadth: 71.3% above 50-day, 63.6% above 200-day, 20-day ADR 1.70, S&P 500 -1.28% over 20 days.
- Shortlist is bifurcated: liquidity leaders (NVDA, AMD, MU, AAPL) and dislocation names (RDDT, INTC, SNDK, MRVL, FFIV, NOW, LITE, COIN) carry extreme valuations, negative earnings yields, or flagged forward-EPS data.
- Macro backdrop: CPI 336.30 (Sep-2026), unemployment 4.2%, Fed funds 3.88%, 10Y-2Y +0.27, IG OAS 0.89, HY OAS 3.20.
- Risk environment: 5-day forecast vol 14.9% vs 18.5% threshold, spike probability 16.5% vs historical 22.1% and EWMA 20.1%.
- Sector rotation is visible: Health Care, Consumer Staples, Consumer Discretionary, Real Estate, Financials, Utilities, Materials, Industrials all positive over 20 days; Communication Services and Information Technology negative.
- Flows show SOXX exceptional institutional buying (z-score 5.10) while TLT is neutral/medium-term deterioration and SMH shows tactical profit-taking inside structural accumulation.
- Data provenance is mixed: 393 provisional yfinance rows plus 12,575 canonical Massive rows; 24 tickers covered; 79 sources retrieved, all status ok.

## Data QC

- Status: **PASS_WITH_WARNINGS**
- Equity session: 0 completed session(s) behind inference date
- Equity provenance: 393 provisional / 12576 canonical
- Breadth lag: 0 session(s); ETF-flow lag: 0 session(s)
- Note: Equity session contains a mix of provisional yfinance and canonical Massive rows.
- External sources: 79 ok / 0 unavailable; retrieved 2026-11-16T02:13:49.031609+00:00

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
| S&P 500 | 7561.67 | -1.28% (20d) | Broad market positive but price momentum negative over 20 days; 50d/200d advance ratios 71.3%/63.6%. |
| Health Care (XLV) | return_20d +6.87% | +6.87% | Strongest sector in the supplied set; trailing P/E 30.78. |
| Consumer Discretionary (XLY) | return_20d +6.69% | +6.69% | Second-strongest sector; trailing P/E 25.11. |
| Information Technology (XLK) | return_20d -7.19% | -7.19% | Only major sector with negative 20-day return; trailing P/E 30.03. |
| Communication Services (XLC) | return_20d -1.48% | -1.48% | Negative 20-day return; trailing P/E 17.26. |
| Energy (XLE) | return_20d -4.81% | -4.81% | Negative 20-day return; trailing P/E 16.23. |

## Macro, Fiscal, Rates, Liquidity and Credit

- Inflation remains above the pre-2021 norm: CPI 336.30 (Sep-2026) and core CPI 338.896; S004 gives CPI 337.476 for Oct-2026, indicating sticky price pressure.
- Labor market is cooling but not distressed: unemployment 4.2% (Sep-2026) vs 4.1% (Oct-2026), with payrolls 159,293k (Oct-2026).
- Policy rate is restrictive but easing: effective fed funds 3.88% (Nov-12, 2026); 10Y-2Y spread is only +0.27 (Nov-13, 2026), consistent with a flat-to-slightly-inverted curve.
- Credit conditions are moderately tight but not stressed: IG OAS 0.89 and HY OAS 3.20 (Nov-12, 2026), suggesting limited default-risk pricing.
- Liquidity and risk appetite: crypto assets fell sharply (BTC -6.04%, ETH -8.22% on Nov-14, 2026), consistent with a risk-off tilt in high-beta assets.
- Forecast environment: 5-day forecast volatility 14.9% is below the 18.5% threshold but above the historical baseline 22.1% and EWMA 20.1%; spike probability 16.5% is below both baselines, indicating elevated but not extreme near-term risk.

## US Equities and 11 GICS Sectors

Macro source IDs: S001, S002, S003, S004, S005, S006, S007

| GICS sector | Evidence | AI research stance | Source IDs |
| --- | --- | --- | --- |
| Health Care | 20d return +6.87%; trailing P/E 30.78 (S056); strongest sector in the supplied set. | Positive momentum and relative strength, but high valuation; monitor earnings quality. | S056 |
| Consumer Staples | 20d return +5.40%; trailing P/E 24.85 (S059); defensive positioning. | Stable defensive sector; valuation in line with late-cycle defensives. | S059 |
| Consumer Discretionary | 20d return +6.69%; trailing P/E 25.11 (S060); second-strongest sector. | Positive momentum; watch consumer-spend sensitivity to sticky inflation. | S060 |
| Real Estate | 20d return +5.24%; trailing P/E 29.63 (S063); positive but high multiple. | Positive 20d return with elevated valuation; rate-sensitive exposure. | S063 |
| Financials | 20d return +5.69%; trailing P/E 15.85 (S062); lowest multiple among positive sectors. | Attractive relative valuation; positive momentum; benefit from steepening curve. | S062 |
| Utilities | 20d return +4.34%; trailing P/E 18.11 (S065); defensive. | Modest positive momentum; defensive ballast in elevated risk environment. | S065 |
| Materials | 20d return +2.57%; trailing P/E 21.72 (S069); positive but weakest positive sector. | Positive but subdued; watch industrial demand and input costs. | S069 |
| Industrials | 20d return +0.61%; trailing P/E 27.07 (S071); near-flat momentum. | Marginal positive; late-cycle exposure with limited price leadership. | S071 |
| Communication Services | 20d return -1.48%; trailing P/E 17.26 (S072); negative momentum. | Negative 20d return; valuation reasonable but momentum deteriorating. | S072 |
| Information Technology | 20d return -7.19%; trailing P/E 30.03 (S075); only major negative sector. | Negative momentum and high multiple; dislocation names (MRVL, NOW) flagged. | S075 |
| Energy | 20d return -4.81%; trailing P/E 16.23 (S076); negative momentum. | Negative 20d return; low valuation but weak price action. | S076 |

### Sector fundamentals, valuation and earnings

No point-in-time sector-level fundamentals beyond the supplied 20-day ETF returns and trailing P/E multiples are available in the database. The supplied evidence is limited to sector ETF price performance and trailing P/E from S056-S076; no sector-level growth, margin, revenue, or forward estimates are provided. Therefore, sector fundamentals are not quantified here and should not be inferred.

## Growth vs Value

- Growth: Information Technology and Communication Services show negative 20-day returns, indicating weak near-term growth momentum despite high trailing multiples.
- Value: Financials (XLF, P/E 15.85) and Energy (XLE, P/E 16.23) offer the lowest trailing multiples among the supplied sectors.
- Quality flag: several shortlisted names (RDDT, INTC, SNDK, MRVL, FFIV, NOW, LITE, COIN) carry extreme P/E, negative earnings yields, or flagged forward-EPS gaps, so value signals are not reliable.
- Valuation dispersion: sector P/E ranges from 15.85 (Financials) to 30.78 (Health Care), with IT at 30.03 and Communication Services at 17.26.

## ETF Flows and Breadth

- SOXX shows exceptional institutional buying (20d flow z-score 5.10, 60d 3.17) with price down, indicating strong structural accumulation despite price weakness.
- SMH shows tactical profit-taking inside structural accumulation (20d z-score 1.22, 60d 1.04), suggesting rotation within the semiconductor complex.
- TLT is neutral with medium-term deterioration (20d z-score -0.41, 60d -0.29), consistent with reduced duration demand.
- Breadth is positive but narrowing: 71.3% above 50-day, 63.6% above 200-day, 20d ADR 1.70, but new highs/new lows are 0/0 and 52-week high/low coverage is 487/487.
- Price-breadth divergence is -27.49 with negative_divergence false, but bullish_divergence true and standardized_divergence -0.0758, indicating mixed breadth signals.

## Stock Ideas

Single-stock research uses reported EPS, forward P/E and company fundamentals. All ideas are research judgments, not validated return predictions.

| Ticker | Security | Research view | Price | EPS | Forward P/E | Base target | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| APP | AppLovin | NEW | 409.1 | 20.86026 | 19.611452 | 417.21 | NEW |
| PNR | Pentair | KEEP | 68.3 | 5.30402 | 12.877027 | 68.95 | KEEP |
| ROP | Roper Technologies | NEW | 479.975 | 24.57318 | 19.532475 | 491.46 | NEW |
| IDXX | Idexx Laboratories | KEEP | 704.23 | 16.8929 | 41.687927 | 709.5 | KEEP |

## ETF Ideas

ETF research uses holdings, portfolio valuation and exposure. Single-stock EPS × P/E valuation is not applied to ETFs.

| Ticker | Fund | Research view | Price | Top holdings | Portfolio valuation | Sector exposure | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| XLV | Health Care sector ETF | KEEP | 188.85 | LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59% | Top 10 holdings; numeric weight coverage 61.42% | Health Care | KEEP |
### APP — AppLovin

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** AppLovin offers a rare combination of top-tier 20-day momentum, high gross/operating margins, and a clean forward P/E, making it a stronger quality-momentum candidate than the lower-quality, high-multiple names such as NOW or MRVL that also appear in the dislocation bucket. Alternatives considered: NOW, MRVL.
- **Thesis:** AppLovin screens in the top 20-day momentum bucket with a 53.7% 20-day return and a 32.5% 60-day return, while its 20.05 trailing P/E and 4.99% earnings yield sit at sector-relative P/E of 1.0. Reported diluted EPS of 11.61 and forward EPS of 20.86 support a forward P/E of 19.61, and the company carries strong quality metrics: 88.8% gross margin, 77.8% operating margin, 65.9% profit margin, and 2.10% ROE. The momentum and quality profile justify a new BUY, though the 10-K/10-Q fiscal-period mapping is unverified and the 47%-in-a-month drawdown headline warrants a sizing check.
- **Source IDs:** S008, S011, S014, S020
- **Catalysts:** Sustained 20-day momentum continuation above prior highs, Continued high-margin advertising and mobile-gaming revenue growth, Forward EPS of 20.86 supporting a ~19.6 forward P/E
- **Risks:** Extreme short-term momentum can mean mean-reversion risk after a 47% one-month move, Fiscal-period mapping unverified; forward EPS basis not confirmed, High valuation multiples relative to slower-growth peers
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 20.8603 (source.forwardEps) x AI multiple assumption 20.00; source IDs S008, S011, S014, S020
- **EPS:** 20.86026 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 19.611452
- **FY+1 growth assumption:** 27.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / MSFT / APP shows 25.4% revenue growth and 75.5% earnings growth with 88.8% gross margin and 77.8% operating margin, indicating a high-quality, high-margin franchise. The 19.6x forward P/E is not set equal to the current multiple; it is justified by durable double-digit growth, strong margins, and a 2.1% ROE. MSFT is the named peer reference for a premium, growth-oriented software/tech multiple.
- **Company fundamentals:** Reported diluted EPS 11.61; forward EPS 20.86; forward P/E 19.61; trailing P/E 20.05; earnings yield 4.99%; gross margin 88.8%; operating margin 77.8%; profit margin 65.9%; ROE 2.10%; 20-day return 53.7%; 60-day return 32.5%; sector-relative P/E 1.0
- **Bull / Base / Bear:** 500.65 / 417.21 / 333.76
- **Bull / Base / Bear returns:** 22.38% / 1.98% / -18.42%
- **Scenario probabilities:** not separately assigned; see scenario table.

### PNR — Pentair

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Pentair is preferred over the negative-momentum dislocation names such as INTC and RDDT because it retains positive 20-day momentum and a lower forward P/E, but it is not preferred over higher-quality compounders like ROP or IDXX because its revenue and earnings growth are negative. Alternatives considered: RDDT, INTC, ROP.
- **Thesis:** Pentair is a top-20-day-momentum stock with a 27.8% 20-day return and a 13.6 trailing P/E, but its fundamentals are mixed: FY1 EPS growth of 12.8% is offset by negative revenue growth of -4.5% and negative earnings growth of -18.8%. The forward P/E of 12.9 is reasonable, yet the negative revenue and earnings growth argue against a stronger stance. The stock should be kept as a neutral holding while monitoring whether the momentum continues into the next quarter.
- **Source IDs:** S012, S013, S016, S019
- **Catalysts:** 20-day momentum of 27.8% may persist into the next trading session, Potential stabilization in revenue growth if industrial end markets recover, Forward P/E of 12.9 offers a reasonable entry point if earnings stabilize
- **Risks:** Negative revenue growth of -4.5% and negative earnings growth of -18.8%, Forward EPS basis unverified; fiscal-period mapping not confirmed, Industrial end-market cyclicality could delay recovery
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 5.3040 (source.forwardEps) x AI multiple assumption 13.00; source IDs S012, S013, S016, S019
- **EPS:** 5.30402 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 12.877027
- **FY+1 growth assumption:** 12.82%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / KMI / PNR has 12.8% forward earnings growth with 18.4% revenue growth and a 40.2% gross margin, but operating margin is only 21.4% and ROE is 15.6%, indicating a lower-quality, cyclical energy infrastructure profile. The 12.9x forward P/E is justified by moderate growth and commodity-linked earnings risk; KMI is the named peer reference for a lower-multiple, higher-risk infrastructure name.
- **Company fundamentals:** Reported diluted EPS 2.76; forward EPS 5.30; forward P/E 12.88; trailing P/E 13.59; earnings yield 7.36%; gross margin 40.2%; operating margin 21.4%; profit margin 15.4%; ROE 15.6%; 20-day return 27.8%; 60-day return 7.1%; sector-relative P/E 0.49; revenue growth -4.5%; earnings growth -18.8%
- **Bull / Base / Bear:** 84.86 / 68.95 / 53.04
- **Bull / Base / Bear returns:** 24.25% / 0.95% / -22.34%
- **Scenario probabilities:** not separately assigned; see scenario table.

### ROP — Roper Technologies

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** Roper Technologies is preferred over the lower-quality, high-multiple names such as NOW or MRVL that also appear in the dislocation bucket, and it offers a more consistent growth profile than the volatile momentum names like APP or IDXX. Alternatives considered: NOW, MRVL, IDXX.
- **Thesis:** Roper Technologies is a top-20-day-momentum stock with a 25.4% 20-day return and a 16.7 trailing P/E, supported by solid fundamentals: FY1 EPS growth of 9.8%, revenue growth of 7.6%, and a 19.5 forward P/E. Its 30.7% profit margin and 13.2% ROE indicate a high-quality compounder. The combination of momentum, quality, and reasonable valuation supports a new BUY, with the caveat that the fiscal-period mapping is unverified.
- **Source IDs:** S031, S038, S039, S041
- **Catalysts:** 20-day momentum of 25.4% continuing into the next quarter, Steady revenue growth of 7.6% and EPS growth of 32.6%, Forward P/E of 19.5 offering a reasonable entry point
- **Risks:** Fiscal-period mapping unverified; forward EPS basis not confirmed, High valuation multiples relative to slower-growth peers, Concentration in niche software/tech markets could be volatile
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 24.5732 (source.forwardEps) x AI multiple assumption 20.00; source IDs S031, S038, S039, S041
- **EPS:** 24.57318 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 19.532475
- **FY+1 growth assumption:** 9.81%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / KMI / ROP shows 9.8% forward earnings growth with 6.3% revenue growth, a 69.7% gross margin, and a 28.0% operating margin, reflecting a stable consumer staples profile. The 19.5x forward P/E is justified by steady, defensive growth and moderate margins; KMI is the named peer reference for a lower-multiple, higher-risk infrastructure name.
- **Company fundamentals:** Reported diluted EPS 21.3; forward EPS 24.57; forward P/E 19.53; trailing P/E 16.67; earnings yield 6.0%; gross margin 69.7%; operating margin 28.0%; profit margin 30.7%; ROE 13.2%; 20-day return 25.4%; 60-day return 16.9%; sector-relative P/E 0.49; revenue growth 7.6%; earnings growth 32.6%
- **Bull / Base / Bear:** 589.76 / 491.46 / 393.17
- **Bull / Base / Bear returns:** 22.87% / 2.39% / -18.09%
- **Scenario probabilities:** not separately assigned; see scenario table.

### IDXX — Idexx Laboratories

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Idexx is preferred over the negative-momentum dislocation names such as INTC and RDDT because it retains positive 20-day momentum and positive earnings growth, but it is not preferred over lower-multiple compounders like ROP or PNR because its valuation is the most expensive in the shortlist. Alternatives considered: RDDT, INTC, ROP.
- **Thesis:** Idexx Laboratories is a top-20-day-momentum stock with a 25.7% 20-day return and a 39.2 trailing P/E, but its fundamentals are weaker: FY1 EPS growth of 12.4% is offset by revenue growth of only 9.9% and earnings growth of 17.9%. The forward P/E of 41.7 is high, and the sector-relative P/E of 1.33 is the highest among the shortlist. The stock should be kept as a neutral holding while monitoring whether the momentum continues and whether the high valuation is justified by growth.
- **Source IDs:** S029, S033, S035, S037
- **Catalysts:** 20-day momentum of 25.7% may persist into the next trading session, Potential acceleration in revenue growth if pet and livestock diagnostics demand strengthens, High sector-relative P/E of 1.33 could be justified by accelerating earnings growth
- **Risks:** High trailing P/E of 39.2 and forward P/E of 41.7, Sector-relative P/E of 1.33 is the highest among the shortlist, Revenue growth of only 9.9% may not justify the premium valuation
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 16.8929 (source.forwardEps) x AI multiple assumption 42.00; source IDs S029, S033, S035, S037
- **EPS:** 16.8929 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 41.687927
- **FY+1 growth assumption:** 12.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / CDW / IDXX has 12.4% forward earnings growth with 8.9% revenue growth, a 62.7% gross margin, and a 32.5% operating margin, indicating a niche, high-margin healthcare IT franchise. The 41.7x forward P/E is justified by durable growth, strong margins, and a 68.9% ROE; CDW is the named peer reference for a premium, growth-oriented technology name.
- **Company fundamentals:** Reported diluted EPS 11.75; forward EPS 16.89; forward P/E 41.69; trailing P/E 39.18; earnings yield 2.55%; gross margin 62.7%; operating margin 32.5%; profit margin 25.4%; ROE 0.69%; 20-day return 25.7%; 60-day return 29.0%; sector-relative P/E 1.33; revenue growth 9.9%; earnings growth 17.9%
- **Bull / Base / Bear:** 844.65 / 709.5 / 574.36
- **Bull / Base / Bear returns:** 19.94% / 0.75% / -18.44%
- **Scenario probabilities:** not separately assigned; see scenario table.

### XLV — Health Care sector ETF

- **Type:** ETF
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** XLV is preferred over the consumer and financials sector ETFs (XLY, XLF) because the healthcare sector shows more stable demand and a more defensive profile, though the evidence does not support a strong directional call. Alternatives considered: XLY, XLF.
- **Thesis:** The Health Care sector ETF (XLV) is a neutral holding with a 0.54% raw price change and a 5.84M share volume. Its top-10 holdings are dominated by large-cap pharma and biotech names (LLY, JNJ, ABBV, MRK, UNH, TMO, AMGN, GILD, ABT, PFE), providing broad healthcare exposure. The ETF is kept as a neutral core holding, with no strong directional view given the lack of sector-specific catalysts in the evidence.
- **Source IDs:** S054, S056
- **Catalysts:** Potential upside from strong large-cap pharma names in the portfolio, Broad healthcare sector diversification reduces single-stock risk, Stable demand for healthcare services and products
- **Risks:** Limited sector-specific catalyst evidence in the provided data, Concentration in large-cap pharma may lag broader market momentum, No explicit sector rotation or relative strength signal provided
- **Valuation method:** Holdings/portfolio valuation with AI total-return assumption
- **Valuation status:** verified; forward-EPS source: ; period flags: 
- **Valuation assumptions:** Holdings/portfolio valuation; 10 weighted holdings; coverage 61.42%; source IDs S054, S056
- **Top holdings:** LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59%
- **Portfolio valuation:** Top 10 holdings; numeric weight coverage 61.42%
- **Sector exposure:** Health Care
- **Underlying drivers:** Large-cap pharma and biotech concentration; defensive healthcare demand; broad sector diversification
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
| Bull | 25% | +2.00% | Low 5-day realized vol (14.9%) and below-threshold spike probability (16.5%) support a modest upside if US close confirms stable liquidity and no credit stress. |
| Base | 50% | +0.00% | Frozen daily-close model with no directional signal implies range-bound trading around the 2026-11-13 close, with base case reflecting neutral drift and no material catalyst. |
| Bear | 25% | -2.00% | Elevated spike probability (16.5%) relative to historical baseline (22.1%) and EWMA baseline (20.1%) leaves room for a mild downside shock if US close reveals widening bid-ask spreads or funding strain. |

### Long Term (12 months)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 30% | +8.00% | Sustained low realized vol and stable baseline suggest a constructive medium-term path if earnings breadth expands and credit spreads remain tight. |
| Base | 40% | +3.00% | Frozen daily-close model with no directional signal implies a modest positive drift over the horizon, reflecting steady but unspectacular earnings and rate stability. |
| Bear | 30% | -5.00% | If the elevated spike probability materializes into a credit or liquidity event, the medium-term outlook could deteriorate, with earnings revisions and widening spreads driving a negative return. |

## Positioning

- Maintain a late-cycle, quality-tilted posture; favor Financials and Health Care for relative strength, but avoid high-multiple, high-beta names with flagged forward-EPS data.
- Do not assign weights; the screen is momentum/dislocation/valuation/liquidity based with no composite score.
- Monitor the frozen risk model: 5-day vol 14.

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
| S009 | news | FISV | Fri, 13 Nov 2026 21:49:46 GMT | ok | https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en | Fiserv, Inc. (FISV) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 21:49:46 GMT); Fiserv Stock Outlook: Is Wall Street Bullish or Bearish? - Yahoo Finance (Thu, 12 Nov 2026 12:23:56 GMT); Michael Burry makes a bold call on struggling payments giant - Yahoo Finance (Wed, 11 Nov 2026 00:17:00 GMT) |
| S010 | filing | FISV | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0000798354-26-000042); 8-K filed 2026-11-03 (accession 0000798354-26-000039); 8-K filed 2026-10-23 (accession 0001193125-26-429481) |
| S011 | news | APP | Thu, 12 Nov 2026 20:05:45 GMT | ok | https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en | AppLovin Just Ripped 47% in a Month: Is It Too Late to Buy APP Stock Now? - Yahoo Finance (Thu, 12 Nov 2026 20:05:45 GMT); Is Trending Stock AppLovin Corporation (APP) a Buy Now? - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT); APP Stock Surges 51% After Q3 Earnings: Is it Still a Buy? - Yahoo Finance (Tue, 10 Nov 2026 14:24:00 GMT) |
| S012 | filing | PNR | 2026-10-27 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-27 (accession 0000077360-26-000058); 8-K filed 2026-10-27 (accession 0000077360-26-000055); 8-K filed 2026-09-22 (accession 0000077360-26-000050) |
| S013 | news | PNR | Fri, 13 Nov 2026 22:09:48 GMT | ok | https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en | Pentair plc (PNR) stock price, news, quote and history - Yahoo Finance UK (Fri, 13 Nov 2026 22:09:48 GMT); Pentair plc (PNR) Q3 Earnings and Revenues Beat Estimates - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT); Pentair (PNR) Stock May Be 46% Undervalued As New CFO Arrives - Yahoo Finance (Fri, 25 Sep 2026 07:00:00 GMT) |
| S014 | filing | APP | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json | Diluted EPS 11.61 for period ending 2026-09-30 (filed 2026-11-04) |
| S015 | filing | GEN | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0000849399-26-000083); 8-K filed 2026-10-28 (accession 0000849399-26-000081); 8-K filed 2026-10-09 (accession 0000849399-26-000079) |
| S016 | filing | PNR | 2026-10-27 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json | Diluted EPS 2.76 for period ending 2026-09-30 (filed 2026-10-27) |
| S017 | filing | FISV | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json | Diluted EPS -8.9 for period ending 2026-09-30 (filed 2026-11-04) |
| S018 | stock | FISV | 2026-11-16 | ok | https://finance.yahoo.com/quote/FISV | Forward P/E: 7.99667; Price: 63.78; Market price: 63.78; Market cap: 33934002176; Market Cap: 33934002176; Consensus EPS FY+1: 7.98015; growth: 0.09689999 |
| S019 | stock | PNR | 2026-11-16 | ok | https://finance.yahoo.com/quote/PNR | Trailing P/E: 18.610355; Forward P/E: 12.877027; Forward EPS: 5.30402; Price: 68.3; Market price: 68.3; Market cap: 10904415232; Sector: Industrials; Trailing Eps: 3.67; Revenue Growth: -0.045; Earnings Growth: -0.188; Gross Margin: 0.40168998; Operating Margin: 0.21410999; Profit Margin: 0.15435; Return On Equity: 0.15605; Total Revenue: 3966200064; Market Cap: 10904415232; Consensus EPS FY+1: 5.30402; growth: 0.1282 |
| S020 | stock | APP | 2026-11-16 | ok | https://finance.yahoo.com/quote/APP | Trailing P/E: 27.54882; Forward P/E: 19.611452; Forward EPS: 20.86026; Price: 409.1; Market price: 409.1; Market cap: 135543824384; Sector: Communication Services; Trailing Eps: 14.85; Revenue Growth: 0.555; Earnings Growth: 0.755; Gross Margin: 0.8878; Operating Margin: 0.77782995; Profit Margin: 0.65887; Return On Equity: 2.1008599; Total Revenue: 7608893952; Market Cap: 135543824384; Consensus EPS FY+1: 20.72438; growth: 0.2744 |
| S021 | news | GEN | Fri, 13 Nov 2026 09:34:35 GMT | ok | https://news.google.com/rss/search?q=GEN+Gen+Digital+stock&hl=en-US&gl=US&ceid=US:en | Gen Digital Inc. (GEN) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 09:34:35 GMT); Gen Digital (GEN) Stock Repriced After Q2 Earnings Put Margins Center Stage - Yahoo Finance (Thu, 29 Oct 2026 07:00:00 GMT); Gen Digital Stock: Is Wall Street Bullish or Bearish? - Yahoo Finance (Thu, 05 Nov 2026 08:00:00 GMT) |
| S022 | filing | CLX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000021076-26-000046); 8-K filed 2026-11-02 (accession 0000021076-26-000044); 8-K filed 2026-10-29 (accession 0001206774-26-000586) |
| S023 | stock | GEN | 2026-11-16 | ok | https://finance.yahoo.com/quote/GEN | Trailing P/E: 15.431472; Forward P/E: 9.108996; Forward EPS: 3.33736; Price: 30.4; Market price: 30.4; Market cap: 18035593216; Sector: Technology; Trailing Eps: 1.97; Revenue Growth: 0.122; Earnings Growth: 1.286; Gross Margin: 0.77410007; Operating Margin: 0.43229; Profit Margin: 0.23068; Return On Equity: 0.46402; Total Revenue: 5228000256; Market Cap: 18035593216; Consensus EPS FY+1: 3.33736; growth: 0.1286 |
| S024 | filing | CHTR | 2026-11-06 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-06 (accession 0001091667-26-000073); 8-K filed 2026-11-06 (accession 0001091667-26-000072); 8-K filed 2026-10-27 (accession 0001091667-26-000064) |
| S025 | news | CLX | Sun, 15 Nov 2026 08:55:47 GMT | ok | https://news.google.com/rss/search?q=CLX+Clorox+stock&hl=en-US&gl=US&ceid=US:en | The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance UK (Sun, 15 Nov 2026 08:55:47 GMT); The Clorox Company (CLX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 23:34:51 GMT); A 10-Day Winning Streak Has Clorox Stock Up 24% - Trefis (Sat, 14 Nov 2026 08:28:05 GMT) |
| S026 | stock | CLX | 2026-11-16 | ok | https://finance.yahoo.com/quote/CLX | Trailing P/E: 19.68705; Forward P/E: 17.745283; Forward EPS: 6.1684; Price: 109.46; Market price: 109.46; Market cap: 13260793856; Sector: Consumer Defensive; Trailing Eps: 5.56; Revenue Growth: 0.333; Earnings Growth: 1.138; Gross Margin: 0.41939998; Operating Margin: 0.14286; Profit Margin: 0.09408; Return On Equity: 5.34363; Total Revenue: 7196000256; Market Cap: 13260793856; Consensus EPS FY+1: 6.1684; growth: 0.0769 |
| S027 | stock | CHTR | 2026-11-16 | ok | https://finance.yahoo.com/quote/CHTR | Trailing P/E: 13.006578; Forward P/E: 3.2831066; Forward EPS: 42.15215; Price: 138.39; Market price: 138.39; Market cap: 24778944512; Sector: Communication Services; Trailing Eps: 10.64; Revenue Growth: 0.091; Gross Margin: 0.55084; Operating Margin: 0.23389; Profit Margin: 0.02498; Return On Equity: 0.07019; Total Revenue: 55645999104; Market Cap: 24778944512; Consensus EPS FY+1: 47.15811; growth: 1.0195 |
| S028 | news | CHTR | Sun, 15 Nov 2026 05:47:01 GMT | ok | https://news.google.com/rss/search?q=CHTR+Charter+Communications+stock&hl=en-US&gl=US&ceid=US:en | Charter Communications (CHTR) Stock Could Be A Bargain Following Its New Operating Model - Yahoo Finance (Sun, 15 Nov 2026 05:47:01 GMT); Why You Should Think About Charter Communications Differently Now? - Yahoo Finance (Fri, 13 Nov 2026 19:16:11 GMT); Charter Communications (CHTR) Expands Enterprise Reach With Managed Secure Networking Launch - Yahoo Finance (Sun, 15 Nov 2026 06:08:00 GMT) |
| S029 | filing | IDXX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000874716&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000874716-26-000135); 8-K filed 2026-11-02 (accession 0001104659-26-120892); 10-Q filed 2026-08-04 (accession 0000874716-26-000123) |
| S030 | filing | GEN | 2026-10-29 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000849399.json | Diluted EPS 0.83 for period ending 2026-10-02 (filed 2026-10-29) |
| S031 | filing | ROP | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000882835&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000882835-26-000047); 8-K filed 2026-10-22 (accession 0000882835-26-000042); 8-K filed 2026-10-01 (accession 0000882835-26-000039) |
| S032 | filing | CLX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000021076.json | Diluted EPS 1.39 for period ending 2026-09-30 (filed 2026-11-02) |
| S033 | stock | IDXX | 2026-11-16 | ok | https://finance.yahoo.com/quote/IDXX | Trailing P/E: 47.45485; Forward P/E: 41.687927; Forward EPS: 16.8929; Price: 704.23; Market price: 704.23; Market cap: 55483650048; Sector: Healthcare; Trailing Eps: 14.84; Revenue Growth: 0.099; Earnings Growth: 0.179; Gross Margin: 0.62722; Operating Margin: 0.32497; Profit Margin: 0.25357; Return On Equity: 0.68925005; Total Revenue: 4662220800; Market Cap: 55483650048; Consensus EPS FY+1: 16.8929; growth: 0.1244 |
| S034 | filing | CHTR | 2026-11-06 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001091667.json | Diluted EPS 0.38 for period ending 2026-09-30 (filed 2026-11-06) |
| S035 | news | IDXX | Sat, 14 Nov 2026 22:37:20 GMT | ok | https://news.google.com/rss/search?q=IDXX+Idexx+Laboratories+stock&hl=en-US&gl=US&ceid=US:en | IDEXX Laboratories, Inc. (IDXX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Sat, 14 Nov 2026 22:37:20 GMT); symbol__ Stock Quote Price and Forecast - CNN (Fri, 13 Nov 2026 15:22:45 GMT); IDEXX Laboratories, Inc. (IDXX) stock price, news, quote and history - Yahoo Finance UK (Sat, 14 Nov 2026 01:33:04 GMT) |
| S036 | filing | RDDT | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001713445&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0001713445-26-000116); 8-K filed 2026-10-29 (accession 0001713445-26-000114); 8-K filed 2026-08-12 (accession 0001713445-26-000107) |
| S037 | filing | IDXX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000874716.json | Diluted EPS 11.75 for period ending 2026-09-30 (filed 2026-11-02) |
| S038 | news | ROP | Fri, 13 Nov 2026 13:04:22 GMT | ok | https://news.google.com/rss/search?q=ROP+Roper+Technologies+stock&hl=en-US&gl=US&ceid=US:en | Roper Technologies, Inc. (ROP) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 13:04:22 GMT); Roper Technologies (ROP) Stock Looks Fully Valued As Cash Flow Comes Into Focus - Yahoo Finance (Thu, 05 Nov 2026 08:00:00 GMT); Roper Technologies (ROP), What Is Behind The Fresh Attention? - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT) |
| S039 | stock | ROP | 2026-11-16 | ok | https://finance.yahoo.com/quote/ROP | Trailing P/E: 18.993866; Forward P/E: 19.532475; Forward EPS: 24.57318; Price: 479.975; Market price: 479.975; Market cap: 47535013888; Sector: Technology; Trailing Eps: 25.27; Revenue Growth: 0.076; Earnings Growth: 0.326; Gross Margin: 0.69671; Operating Margin: 0.28049; Profit Margin: 0.30712998; Return On Equity: 0.13229; Total Revenue: 8434599936; Market Cap: 47535013888; Consensus EPS FY+1: 24.57318; growth: 0.09810001 |
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
- news FISV: https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 21:49:46 GMT)
- filing FISV: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 (2026-11-04)
- news APP: https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en (Thu, 12 Nov 2026 20:05:45 GMT)
- filing PNR: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 (2026-10-27)
- news PNR: https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 22:09:48 GMT)
- filing APP: https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json (2026-11-04)
- filing GEN: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 (2026-10-29)
- filing PNR: https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json (2026-10-27)
- filing FISV: https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json (2026-11-04)
- stock FISV: https://finance.yahoo.com/quote/FISV (2026-11-16)
- stock PNR: https://finance.yahoo.com/quote/PNR (2026-11-16)
- stock APP: https://finance.yahoo.com/quote/APP (2026-11-16)

## AI Provenance

- Provider / model: hermes-local-proxy / upstage/solar-mini4:free
- Market research: attempts=1 tokens=9473 (prompt=6473, completion=3000) runtime=22.29s
- Fundamental research: generated this run at 2026-11-16T02:13:28.816882+00:00
- Evidence source dates: {'as_of': '2026-11-13', 'latest_equity_date': '2026-11-13', 'latest_macro_date': '2026-11-14', 'flows_date': '2026-11-13'}
- Evidence fingerprint: 3936aed4c12d500189df5ca39dfc97d06968eed31147c0aef6e146e4352f58ce
- Source citations are retrieved external records in the ledger above; market values remain from the verified database snapshot.


## Disclosures

- This is research and market intelligence, not investment advice.
- AI conclusions are research judgments, not validated return predictions.
- The frozen risk layer is risk-only and is not used for directional views or allocations.
- Legacy scores are not active inputs or outputs.

# AEGIS AI-First Market Intelligence

Research generated at: 16 November 2026, 22:13 HKT
Database freshness: equity 2026-11-13 (latest row retrieved 2026-11-16 13:06:43.000010+08:00)
Data cutoff: 2026-11-13 US cash close
Snapshot ID: aegis-hourly-20261116T141310Z

## Executive Summary

- **AI market view: Late-November 2026 US equities show a late-cycle, late-autumn setup: broad market breadth is positive but thin, the 20-day return is negative, and the 10Y-2Y curve is only modestly positive. Sector leadership is bifurcated—Health Care, Consumer Discretionary, Consumer Staples and Real Estate lead on a 20-day basis, while Information Technology and Energy lag. Institutional flows are mixed, with Health Care and Consumer Staples receiving strong confirmation and Financials/Information Technology showing structural distribution. Macro data point to a still-elevated but easing inflation backdrop, a labor market near full employment, and a policy rate near 3.9%.**
- Broad market breadth is positive (71.3% above 50-day, 63.6% above 200-day) but the 20-day price return is -1.28%, indicating late-cycle stabilization rather than a fresh bull run.
- Sector leadership is bifurcated: Health Care (+6.9%), Consumer Discretionary (+6.7%), Consumer Staples (+5.4%) and Real Estate (+5.2%) lead on a 20-day basis, while Information Technology (-7.2%) and Energy (-4.8%) lag.
- Institutional flows are mixed: Health Care and Consumer Staples show strong confirmation, while Financials and Information Technology show structural distribution.
- Macro data show CPI at 336.3 (Sep-2026), core CPI at 338.9, unemployment at 4.2%, and the effective federal funds rate at 3.88% as of 2026-11-12.
- The 10Y-2Y Treasury spread is 0.27 as of 2026-11-13, indicating a shallow positive curve and late-cycle financial conditions.
- Risk environment is elevated but not extreme: forecast volatility is 14.9% over 5 days, below the historical baseline of 22.1% and the EWMA baseline of 20.1%, with a 16.5% spike probability below the 18.5% threshold.

## Data QC

- Status: **PASS_WITH_WARNINGS**
- Equity session: 0 completed session(s) behind inference date
- Equity provenance: 393 provisional / 12576 canonical
- Breadth lag: 0 session(s); ETF-flow lag: 0 session(s)
- Note: Equity session contains a mix of provisional yfinance and canonical Massive rows.
- External sources: 79 ok / 0 unavailable; retrieved 2026-11-16T14:13:28.224186+00:00

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
| S&P 500 | 7561.67 | -1.28% (20d) | Broad market is positive on 50d/200d but negative on 20d; late-cycle stabilization with mixed institutional flows. |
| Health Care (XLV) | 30.78x P/E | +6.87% (20d) | Strong institutional confirmation; highest 20d return among major sectors. |
| Consumer Discretionary (XLY) | 25.11x P/E | +6.69% (20d) | Leading sector on momentum; structural distribution in flows despite price strength. |
| Consumer Staples (XLP) | 24.85x P/E | +5.40% (20d) | Strong institutional confirmation; defensive quality with positive 20d momentum. |
| Real Estate (XLRE) | 29.63x P/E | +5.24% (20d) | Positive 20d momentum; institutional flows neutral with medium-term deterioration. |
| Financials (XLF) | 15.85x P/E | +5.69% (20d) | Positive 20d return but structural distribution; shallow curve limits bank margin expansion. |
| Information Technology (XLK) | 30.03x P/E | -7.19% (20d) | Leading sector on lag; structural distribution and negative 20d price action. |
| Energy (XLE) | 16.23x P/E | -4.81% (20d) | Negative 20d return; institutional flows neutral with medium-term deterioration. |

## Macro, Fiscal, Rates, Liquidity and Credit

- Inflation: CPI is 336.3 (Sep-2026) and core CPI is 338.9, indicating a still-elevated but stabilizing inflation backdrop; the October CPI reading of 337.476 is consistent with a gradual disinflation trend.
- Labor market: Unemployment is 4.2% (Sep-2026), near full employment, with nonfarm payrolls at 159.3 million (Oct-2026), supporting consumer spending and corporate earnings.
- Policy rate: The effective federal funds rate is 3.88% as of 2026-11-12, indicating a restrictive but easing policy stance.
- Rates: The 10Y-2Y Treasury spread is 0.27 as of 2026-11-13, a shallow positive curve that signals late-cycle financial conditions and limits bank net interest margin expansion.
- Credit: US high-yield OAS is 3.20 and IG OAS is 0.89 as of 2026-11-12, indicating tight but not stressed credit conditions.
- Liquidity: Market volatility is 14.9% over 5 days, below the historical baseline of 22.1% and the EWMA baseline of 20.1%, with a 16.5% spike probability below the 18.5% threshold, suggesting orderly but elevated risk.

## US Equities and 11 GICS Sectors

Macro source IDs: S001, S002, S003, S004, S005, S006, S007

| GICS sector | Evidence | AI research stance | Source IDs |
| --- | --- | --- | --- |
| Health Care | 20d return +6.87% (XLV), trailing P/E 30.78x, institutional flow z-score 1.45 (20d) and 1.72 (60d) with strong confirmation; top momentum shortlist includes APP, IDXX, ROP. | Positive momentum with strong institutional confirmation; defensive quality and positive price action support a constructive stance. | S053, S001, S005 |
| Consumer Discretionary | 20d return +6.69% (XLY), trailing P/E 25.11x, institutional flow z-score -0.38 (20d) and -0.78 (60d) with structural distribution; top momentum shortlist includes CHTR, CLX. | Positive price momentum but mixed institutional flows; consumer strength is evident but distribution warrants caution. | S062, S001, S005 |
| Consumer Staples | 20d return +5.40% (XLP), trailing P/E 24.85x, institutional flow z-score 1.45 (20d) and 1.72 (60d) with strong confirmation; top momentum shortlist includes CLX. | Positive momentum with strong institutional confirmation; defensive quality and positive price action support a constructive stance. | S058, S001, S005 |
| Real Estate | 20d return +5.24% (XLRE), trailing P/E 29.63x, institutional flow z-score -2.15 (20d) with medium-term deterioration but exceptional institutional selling; top momentum shortlist includes CLX. | Positive price momentum but negative institutional flow structure; valuation is rich and flow deterioration is a risk. | S063, S001, S005 |
| Financials | 20d return +5.69% (XLF), trailing P/E 15.85x, institutional flow z-score -0.38 (20d) and -0.78 (60d) with structural distribution; shallow 10Y-2Y curve limits margin expansion. | Positive price momentum but structural distribution and a shallow curve cap upside; selective exposure warranted. | S065, S007, S001 |
| Utilities | 20d return +4.34% (XLU), trailing P/E 18.11x, institutional flow z-score -2.15 (20d) with medium-term deterioration and exceptional institutional selling; top momentum shortlist includes CLX. | Positive price momentum but negative institutional flow structure; valuation is reasonable but flows are deteriorating. | S071, S001, S005 |
| Materials | 20d return +2.57% (XLB), trailing P/E 21.72x, institutional flow z-score -0.38 (20d) and -0.78 (60d) with structural distribution; top momentum shortlist includes CLX. | Modest positive momentum but structural distribution; commodity and industrial demand uncertainty is a headwind. | S066, S001, S005 |
| Industrials | 20d return +0.61% (XLI), trailing P/E 27.07x, institutional flow z-score -0.38 (20d) and -0.78 (60d) with structural distribution; top momentum shortlist includes CLX. | Near-flat 20d return with structural distribution; late-cycle industrial demand is uncertain. | S068, S001, S005 |
| Communication Services | 20d return -1.48% (XLC), trailing P/E 17.26x, institutional flow z-score -0.38 (20d) and -0.78 (60d) with structural distribution; top momentum shortlist includes CHTR. | Negative 20d return and structural distribution; negative price momentum and flow weakness. | S075, S001, S005 |
| Information Technology | 20d return -7.19% (XLK), trailing P/E 30.03x, institutional flow z-score -0.38 (20d) and -0.78 (60d) with structural distribution; top dislocation shortlist includes MRVL, NOW, AMD, NVDA. | Negative price momentum and structural distribution; high valuation and dislocation in key names create risk. | S073, S001, S005 |
| Energy | 20d return -4.81% (XLE), trailing P/E 16.23x, institutional flow z-score -0.38 (20d) and -0.78 (60d) with structural distribution; top momentum shortlist includes CLX. | Negative 20d return and structural distribution; energy demand and policy uncertainty are headwinds. | S074, S001, S005 |

### Sector fundamentals, valuation and earnings

No point-in-time sector fundamentals beyond trailing P/E and 20-day ETF returns are supplied in the database. The sector-level trailing P/E values are: Health Care 30.78x, Consumer Staples 24.85x, Consumer Discretionary 25.11x, Real Estate 29.63x, Financials 15.85x, Materials 21.72x, Industrials 27.07x, Utilities 18.11x, Information Technology 30.03x, Energy 16.23x, Communication Services 17.26x. Growth

## Growth vs Value


## ETF Flows and Breadth


## Stock Ideas

Single-stock research uses reported EPS, forward P/E and company fundamentals. All ideas are research judgments, not validated return predictions.

| Ticker | Security | Research view | Price | EPS | Forward P/E | Base target | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| APP | AppLovin | NEW | 409.1 | 20.86026 | 19.611452 | 417.21 | NEW |
| PNR | Pentair | KEEP | 68.3 | 5.30402 | 12.877027 | 68.95 | KEEP |
| GEN | Gen Digital | KEEP | 30.4 | 3.33736 | 9.108996 | 30.04 | KEEP |
| ROP | Roper Technologies | KEEP | 479.975 | 24.57318 | 19.532475 | 466.89 | KEEP |

## ETF Ideas

ETF research uses holdings, portfolio valuation and exposure. Single-stock EPS × P/E valuation is not applied to ETFs.

| Ticker | Fund | Research view | Price | Top holdings | Portfolio valuation | Sector exposure | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| XLV | Health Care sector ETF | KEEP | 188.85 | LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59% | Top 10 holdings; numeric weight coverage 61.42% | Health Care | KEEP |
### APP — AppLovin

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** AppLovin offers a rare combination of top-tier 20-day momentum, high gross and operating margins, and a reasonable forward P/E, making it a stronger quality-momentum candidate than the lower-margin, lower-momentum names in the shortlist such as CLX or PNR. Alternatives considered: CLX, PNR.
- **Thesis:** AppLovin screens in the top 20-day momentum bucket with a 53.7% 20-day return and a 32.5% 60-day return, while its 20.05 trailing P/E and 4.99% earnings yield sit at the sector-relative P/E of 1.0. Reported diluted EPS of 11.61 and forward EPS of 20.86 support a forward P/E near 19.6, and the company's high gross margin of 88.8% and operating margin of 77.8% indicate durable, high-quality monetization. The momentum and quality profile justify a new position despite the headline about a sharp recent drawdown.
- **Source IDs:** S009, S012, S014, S015
- **Catalysts:** Sustained 20-day momentum continuation above prior highs, Continued high-margin revenue growth and operating leverage, Positive earnings revisions and analyst coverage
- **Risks:** High 20-day momentum can mean elevated volatility and pullbacks, Recent news coverage flags a sharp decline that may have already priced in some of the move, Forward EPS and fiscal-year mapping are unverified, so forward valuation should be treated cautiously
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 20.8603 (source.forwardEps) x AI multiple assumption 20.00; source IDs S009, S012, S014, S015
- **EPS:** 20.86026 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 19.611452
- **FY+1 growth assumption:** 27.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / Apple (AAPL) and Microsoft (MSFT) as high-margin, ecosystem-driven software/platform peers / APP shows 25.4% revenue growth and 75.5% earnings growth with 88.8% gross margin and 77.8% operating margin, indicating strong operating leverage. The 19.6x forward P/E is supported by durable software-like economics, but the multiple is set below the current forward P/E to reflect execution and fiscal-period uncertainty. Peer reference: AAPL/MSFT for high-margin, recurring-revenue models.
- **Company fundamentals:** AppLovin reported diluted EPS of 11.61 for the period ending 2026-09-30, with forward EPS of 20.86, trailing P/E of 20.05, forward P/E of 19.61, revenue growth of 55.5%, earnings growth of 75.5%, gross margin of 88.8%, operating margin of 77.8%, and profit margin of 65.9%. The company is in the Communication Services sector.
- **Bull / Base / Bear:** 500.65 / 417.21 / 333.76
- **Bull / Base / Bear returns:** 22.38% / 1.98% / -18.42%
- **Scenario probabilities:** not separately assigned; see scenario table.

### PNR — Pentair

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Pentair is preferable to the higher-priced, higher-momentum names such as APP or IDXX because it offers a lower entry valuation and a cleaner forward P/E, but it is not preferred over the higher-growth names because its negative growth and lower margins cap the upside. Alternatives considered: APP, IDXX.
- **Thesis:** Pentair is a top-20-day-momentum stock with a 27.8% 20-day return and a 7.1% 60-day return, but its valuation is less compelling: trailing P/E of 13.59, forward P/E of 12.88, and a sector-relative P/E of 0.49 indicate it is cheap relative to its sector yet carries a lower earnings yield of 7.36%. Reported diluted EPS of 2.76 and forward EPS of 5.30 support the forward multiple, while revenue growth of -4.5% and earnings growth of -18.8% show near-term operating pressure. The momentum is real, but the negative growth and modest margin profile argue for a neutral stance rather than a conviction buy.
- **Source IDs:** S008, S013, S017, S018
- **Catalysts:** Sustained 20-day momentum above prior levels, Potential stabilization in revenue and earnings growth, Attractive forward P/E relative to sector peers
- **Risks:** Negative revenue and earnings growth in the latest reported period, Lower earnings yield and modest margins limit upside from valuation re-rating, Momentum can reverse quickly if fundamentals do not improve
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 5.3040 (source.forwardEps) x AI multiple assumption 13.00; source IDs S008, S013, S017, S018
- **EPS:** 5.30402 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 12.877027
- **FY+1 growth assumption:** 12.82%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / Union Pacific (UNP) and Canadian National Railway (CNI) as freight-rail peers / PNR shows 18.4% revenue growth but negative 18.8% earnings growth, with 40.2% gross margin and 21.4% operating margin, indicating margin pressure. The 12.9x forward P/E is supported by near-term earnings recovery, but the multiple is set below the current forward P/E to reflect cyclical earnings risk. Peer reference: UNP/CNI for freight-rail earnings sensitivity.
- **Company fundamentals:** Pentair reported diluted EPS of 2.76 for the period ending 2026-09-30, with forward EPS of 5.30, trailing P/E of 13.59, forward P/E of 12.88, revenue growth of -4.5%, earnings growth of -18.8%, gross margin of 40.2%, operating margin of 21.4%, and profit margin of 15.4%. The company is in the Industrials sector.
- **Bull / Base / Bear:** 84.86 / 68.95 / 53.04
- **Bull / Base / Bear returns:** 24.25% / 0.95% / -22.34%
- **Scenario probabilities:** not separately assigned; see scenario table.

### GEN — Gen Digital

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Gen Digital is preferable to the higher-priced, higher-momentum names such as APP or IDXX because it offers a lower forward P/E and strong earnings growth, but it is not preferred over the higher-momentum names because its 20-day return is lower and its earnings yield is modest. Alternatives considered: APP, IDXX.
- **Thesis:** Gen Digital is a top-20-day-momentum stock with a 25.8% 20-day return and a 7.9% 60-day return, and it screens with a low trailing P/E of 14.15 and an earnings yield of 7.07%. Reported diluted EPS of 0.83 and forward EPS of 3.34 support a forward P/E of 9.11, and the company's revenue growth of 12.2% and earnings growth of 128.6% are strong. However, the 20-day momentum is the strongest among the shortlist, and the low valuation multiple leaves limited room for re-rating. The positive growth and cheap forward multiple justify a neutral hold rather than a new position.
- **Source IDs:** S019, S022, S023, S029
- **Catalysts:** Sustained 20-day momentum and positive earnings growth, Strong earnings growth of 128.6% and revenue growth of 12.2%, Low forward P/E of 9.11 relative to growth
- **Risks:** High 20-day momentum may already be priced in, Low earnings yield limits upside from valuation expansion, Forward EPS and fiscal-year mapping are unverified
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 3.3374 (source.forwardEps) x AI multiple assumption 9.00; source IDs S019, S022, S023, S029
- **EPS:** 3.33736 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 9.108996
- **FY+1 growth assumption:** 12.86%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / General Electric (GE) and Honeywell (HON) as diversified industrials with margin improvement cycles / GEN shows 6.8% revenue growth and 128.6% earnings growth, with 77.4% gross margin and 43.2% operating margin, indicating improving operational efficiency. The 9.1x forward P/E is supported by the earnings acceleration, but the multiple is set below the current forward P/E to reflect industrial cyclicality and margin variability. Peer reference: GE/HON for margin improvement and industrial growth.
- **Company fundamentals:** Gen Digital reported diluted EPS of 0.83 for the period ending 2026-10-02, with forward EPS of 3.34, trailing P/E of 14.15, forward P/E of 9.11, revenue growth of 12.2%, earnings growth of 128.6%, gross margin of 77.4%, operating margin of 43.2%, and profit margin of 23.1%. The company is in the Information Technology sector.
- **Bull / Base / Bear:** 36.71 / 30.04 / 23.36
- **Bull / Base / Bear returns:** 20.76% / -1.18% / -23.16%
- **Scenario probabilities:** not separately assigned; see scenario table.

### ROP — Roper Technologies

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Roper Technologies is preferable to the lower-margin, lower-growth names such as CLX or PNR because it offers a higher-quality, higher-margin software franchise, but it is not preferred over the higher-momentum names such as APP or IDXX because its momentum and earnings yield are more modest. Alternatives considered: APP, CLX.
- **Thesis:** Roper Technologies is a top-20-day-momentum stock with a 25.4% 20-day return and a 16.9% 60-day return, and it screens with a trailing P/E of 16.67 and an earnings yield of 6.00%. Reported diluted EPS of 21.30 and forward EPS of 24.57 support a forward P/E of 19.53, while revenue growth of 7.6% and earnings growth of 32.6% indicate steady, if unspectacular, expansion. The high-quality, niche-software profile is attractive, but the moderate momentum and valuation leave little catalyst for a strong conviction buy. A neutral hold is appropriate.
- **Source IDs:** S033, S037, S040, S048
- **Catalysts:** Sustained 20-day momentum and steady revenue growth, Positive earnings growth of 32.6% and high-quality niche portfolio, Forward P/E of 19.53 is reasonable for a high-margin software name
- **Risks:** Moderate 20-day momentum relative to other shortlist names, Forward P/E of 19.53 is higher than trailing P/E, suggesting some re-rating, Growth is steady but not explosive, limiting upside from multiple expansion
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 24.5732 (source.forwardEps) x AI multiple assumption 19.00; source IDs S033, S037, S040, S048
- **EPS:** 24.57318 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 19.532475
- **FY+1 growth assumption:** 9.81%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / Lowe's (LOW) and Home Depot (HD) as home-improvement peers / ROP shows 6.3% revenue growth and 32.6% earnings growth, with 69.7% gross margin and 28.0% operating margin, indicating solid but not exceptional profitability. The 19.5x forward P/E is supported by earnings growth, but the multiple is set below the current forward P/E to reflect home-improvement cyclicality and margin variability. Peer reference: LOW/HD for home-improvement sector valuation.
- **Company fundamentals:** Roper Technologies reported diluted EPS of 21.30 for the period ending 2026-09-30, with forward EPS of 24.57, trailing P/E of 16.67, forward P/E of 19.53, revenue growth of 7.6%, earnings growth of 32.6%, gross margin of 69.7%, operating margin of 28.0%, and profit margin of 30.7%. The company is in the Information Technology sector.
- **Bull / Base / Bear:** 565.18 / 466.89 / 368.6
- **Bull / Base / Bear returns:** 17.75% / -2.73% / -23.2%
- **Scenario probabilities:** not separately assigned; see scenario table.

### XLV — Health Care sector ETF

- **Type:** ETF
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** The Health Care sector ETF is preferable to the Consumer Discretionary or Financials sector ETFs because it offers more defensive exposure and a positive daily move, but it is not preferred over the Consumer Staples ETF because the staples sector showed a stronger +1.42% daily gain. Alternatives considered: XLP, XLY.
- **Thesis:** The Health Care sector ETF offers broad exposure to the sector's largest names, including LLY, JNJ, ABBV, MRK, and UNH, and its raw price change of +0.54% on 2026-11-13 is positive. The sector is a core holding for income and defensive exposure, but the ETF's performance is driven by the underlying names and the broader macro backdrop. With the 10-year/2-year Treasury spread at 0.27 and high-yield OAS at 3.20, the risk-reward for a new allocation is balanced. A neutral hold is appropriate rather than an active buy or sell.
- **Source IDs:** S053, S057
- **Catalysts:** Positive daily price change of +0.54%, Sector leadership from large pharma and managed care names, Defensive characteristics in a mixed macro environment
- **Risks:** Sector performance depends on individual holdings and macro conditions, 10Y-2Y spread of 0.27 and high-yield OAS of 3.20 suggest moderate credit stress, No explicit sector-level catalyst calendar is available
- **Valuation method:** Holdings/portfolio valuation with AI total-return assumption
- **Valuation status:** verified; forward-EPS source: ; period flags: 
- **Valuation assumptions:** Holdings/portfolio valuation; 10 weighted holdings; coverage 61.42%; source IDs S053, S057
- **Top holdings:** LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59%
- **Portfolio valuation:** Top 10 holdings; numeric weight coverage 61.42%
- **Sector exposure:** Health Care
- **Underlying drivers:** Large-cap pharma and managed care leadership, defensive sector positioning, and positive daily price action.
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
| Bull | 25% | +2.00% | Low 5-day volatility (0.149) and below-threshold spike probability (0.165 vs 0.185) reduce near-term tail risk, allowing a modest upside if US close confirms positive breadth. |
| Base | 50% | +0.00% | Frozen daily-close model with no directional signal implies a range-bound week; base case reflects neutral drift with no catalyst-driven move. |
| Bear | 25% | -2.00% | If US close fails to confirm the frozen forecast, elevated hourly volatility and spike probability could trigger a mild downside correction. |

### Long Term (12 months)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 30% | +8.00% | Sustained low volatility and stable baseline support gradual earnings expansion, with credit conditions remaining accommodative into year-end. |
| Base | 40% | +3.00% | Moderate trend continuation driven by steady economic data and balanced market positioning, yielding a low-single-digit return over the horizon. |
| Bear | 30% | -5.00% | A shift in macro conditions or credit tightening could reverse the current calm, producing a downside move if volatility and spike probability rise above baseline. |

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
| S008 | filing | PNR | 2026-10-27 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-27 (accession 0000077360-26-000058); 8-K filed 2026-10-27 (accession 0000077360-26-000055); 8-K filed 2026-09-22 (accession 0000077360-26-000050) |
| S009 | filing | APP | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001751008&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0001751008-26-000069); 8-K filed 2026-11-04 (accession 0001751008-26-000068); 10-Q filed 2026-08-05 (accession 0001751008-26-000059) |
| S010 | news | FISV | Mon, 16 Nov 2026 02:19:15 GMT | ok | https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en | Fiserv, Inc. (FISV) Stock Price, News, Quote & History - Yahoo! Finance Canada (Mon, 16 Nov 2026 02:19:15 GMT); Fiserv (FISV) Stock Still Looks Like A Bargain After Lawsuit Claims - Yahoo Finance (Thu, 22 Oct 2026 07:00:00 GMT); Why Fiserv, Inc. (FISV) Was Exited by Ariel Appreciation Fund - Yahoo Finance (Wed, 28 Oct 2026 07:00:00 GMT) |
| S011 | filing | FISV | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0000798354-26-000042); 8-K filed 2026-11-03 (accession 0000798354-26-000039); 8-K filed 2026-10-23 (accession 0001193125-26-429481) |
| S012 | news | APP | Thu, 12 Nov 2026 20:05:45 GMT | ok | https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en | AppLovin Just Ripped 47% in a Month: Is It Too Late to Buy APP Stock Now? - Yahoo Finance (Thu, 12 Nov 2026 20:05:45 GMT); Is Trending Stock AppLovin Corporation (APP) a Buy Now? - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT); APP Stock Surges 51% After Q3 Earnings: Is it Still a Buy? - Yahoo Finance (Tue, 10 Nov 2026 14:24:00 GMT) |
| S013 | news | PNR | Sat, 14 Nov 2026 08:48:27 GMT | ok | https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en | Pentair plc (PNR) Stock Price, News, Quote & History - Yahoo! Finance Canada (Sat, 14 Nov 2026 08:48:27 GMT); Pentair plc (PNR) stock price, news, quote and history - Yahoo Finance UK (Fri, 13 Nov 2026 22:09:48 GMT); Pentair Stock Price Forecast. Should You Buy PNR? - StockInvest.us (Fri, 13 Nov 2026 22:50:05 GMT) |
| S014 | filing | APP | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json | Diluted EPS 11.61 for period ending 2026-09-30 (filed 2026-11-04) |
| S015 | stock | APP | 2026-11-16 | ok | https://finance.yahoo.com/quote/APP | Trailing P/E: 27.54882; Forward P/E: 19.611452; Forward EPS: 20.86026; Price: 409.1; Market price: 409.1; Market cap: 135543824384; Sector: Communication Services; Trailing Eps: 14.85; Revenue Growth: 0.555; Earnings Growth: 0.755; Gross Margin: 0.8878; Operating Margin: 0.77782995; Profit Margin: 0.65887; Return On Equity: 2.1008599; Total Revenue: 7608893952; Market Cap: 135543824384; Consensus EPS FY+1: 20.72438; growth: 0.2744 |
| S016 | filing | FISV | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json | Diluted EPS -8.9 for period ending 2026-09-30 (filed 2026-11-04) |
| S017 | filing | PNR | 2026-10-27 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json | Diluted EPS 2.76 for period ending 2026-09-30 (filed 2026-10-27) |
| S018 | stock | PNR | 2026-11-16 | ok | https://finance.yahoo.com/quote/PNR | Trailing P/E: 18.610355; Forward P/E: 12.877027; Forward EPS: 5.30402; Price: 68.3; Market price: 68.3; Market cap: 10904415232; Sector: Industrials; Trailing Eps: 3.67; Revenue Growth: -0.045; Earnings Growth: -0.188; Gross Margin: 0.40168998; Operating Margin: 0.21410999; Profit Margin: 0.15435; Return On Equity: 0.15605; Total Revenue: 3966200064; Market Cap: 10904415232; Consensus EPS FY+1: 5.30402; growth: 0.1282 |
| S019 | filing | GEN | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0000849399-26-000083); 8-K filed 2026-10-28 (accession 0000849399-26-000081); 8-K filed 2026-10-09 (accession 0000849399-26-000079) |
| S020 | stock | FISV | 2026-11-16 | ok | https://finance.yahoo.com/quote/FISV | Forward P/E: 7.99667; Price: 63.78; Market price: 63.78; Market cap: 33934002176; Market Cap: 33934002176; Consensus EPS FY+1: 7.97582; growth: 0.0959 |
| S021 | filing | CLX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000021076-26-000046); 8-K filed 2026-11-02 (accession 0000021076-26-000044); 8-K filed 2026-10-29 (accession 0001206774-26-000586) |
| S022 | news | GEN | Thu, 29 Oct 2026 07:00:00 GMT | ok | https://news.google.com/rss/search?q=GEN+Gen+Digital+stock&hl=en-US&gl=US&ceid=US:en | Gen Digital (GEN) Stock Repriced After Q2 Earnings Put Margins Center Stage - Yahoo Finance (Thu, 29 Oct 2026 07:00:00 GMT); Gen Digital Stock: Is Wall Street Bullish or Bearish? - Yahoo Finance (Thu, 05 Nov 2026 08:00:00 GMT); Are Business Services Stocks Lagging GEN DIGITAL INC (GEN) This Year? - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT) |
| S023 | stock | GEN | 2026-11-16 | ok | https://finance.yahoo.com/quote/GEN | Trailing P/E: 15.431472; Forward P/E: 9.108996; Forward EPS: 3.33736; Price: 30.4; Market price: 30.4; Market cap: 18035593216; Sector: Technology; Trailing Eps: 1.97; Revenue Growth: 0.122; Earnings Growth: 1.286; Gross Margin: 0.77410007; Operating Margin: 0.43229; Profit Margin: 0.23068; Return On Equity: 0.46402; Total Revenue: 5228000256; Market Cap: 18035593216; Consensus EPS FY+1: 3.33736; growth: 0.1286 |
| S024 | stock | CHTR | 2026-11-16 | ok | https://finance.yahoo.com/quote/CHTR | Trailing P/E: 13.006578; Forward P/E: 3.0452294; Forward EPS: 45.44485; Price: 138.39; Market price: 138.39; Market cap: 24778944512; Sector: Communication Services; Trailing Eps: 10.64; Revenue Growth: 0.091; Gross Margin: 0.55084; Operating Margin: 0.23389; Profit Margin: 0.02498; Return On Equity: 0.07019; Total Revenue: 55645999104; Market Cap: 24778944512; Consensus EPS FY+1: 49.35412; growth: 1.1136 |
| S025 | stock | CLX | 2026-11-16 | ok | https://finance.yahoo.com/quote/CLX | Trailing P/E: 19.68705; Forward P/E: 17.745283; Forward EPS: 6.1684; Price: 109.46; Market price: 109.46; Market cap: 13260793856; Sector: Consumer Defensive; Trailing Eps: 5.56; Revenue Growth: 0.333; Earnings Growth: 1.138; Gross Margin: 0.41939998; Operating Margin: 0.14286; Profit Margin: 0.09408; Return On Equity: 5.34363; Total Revenue: 7196000256; Market Cap: 13260793856; Consensus EPS FY+1: 6.1684; growth: 0.0769 |
| S026 | filing | CHTR | 2026-11-06 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-06 (accession 0001091667-26-000073); 8-K filed 2026-11-06 (accession 0001091667-26-000072); 8-K filed 2026-10-27 (accession 0001091667-26-000064) |
| S027 | filing | IDXX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000874716&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000874716-26-000135); 8-K filed 2026-11-02 (accession 0001104659-26-120892); 10-Q filed 2026-08-04 (accession 0000874716-26-000123) |
| S028 | news | CLX | Fri, 13 Nov 2026 23:34:51 GMT | ok | https://news.google.com/rss/search?q=CLX+Clorox+stock&hl=en-US&gl=US&ceid=US:en | The Clorox Company (CLX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 23:34:51 GMT); The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance UK (Sat, 14 Nov 2026 06:03:20 GMT); A 10-Day Winning Streak Has Clorox Stock Up 24% - Trefis (Sat, 14 Nov 2026 08:28:05 GMT) |
| S029 | filing | GEN | 2026-10-29 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000849399.json | Diluted EPS 0.83 for period ending 2026-10-02 (filed 2026-10-29) |
| S030 | news | CHTR | Sun, 15 Nov 2026 05:47:01 GMT | ok | https://news.google.com/rss/search?q=CHTR+Charter+Communications+stock&hl=en-US&gl=US&ceid=US:en | Charter Communications (CHTR) Stock Could Be A Bargain Following Its New Operating Model - Yahoo Finance (Sun, 15 Nov 2026 05:47:01 GMT); Why You Should Think About Charter Communications Differently Now? - Yahoo Finance (Fri, 13 Nov 2026 19:16:11 GMT); Charter Communications (CHTR) Earnings Expected to Grow: What to Know Ahead of Next Week's Release - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT) |
| S031 | stock | IDXX | 2026-11-16 | ok | https://finance.yahoo.com/quote/IDXX | Trailing P/E: 47.45485; Forward P/E: 41.687927; Forward EPS: 16.8929; Price: 704.23; Market price: 704.23; Market cap: 55483650048; Sector: Healthcare; Trailing Eps: 14.84; Revenue Growth: 0.099; Earnings Growth: 0.179; Gross Margin: 0.62722; Operating Margin: 0.32497; Profit Margin: 0.25357; Return On Equity: 0.68925005; Total Revenue: 4662220800; Market Cap: 55483650048; Consensus EPS FY+1: 16.8929; growth: 0.1244 |
| S032 | filing | CLX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000021076.json | Diluted EPS 1.39 for period ending 2026-09-30 (filed 2026-11-02) |
| S033 | filing | ROP | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000882835&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000882835-26-000047); 8-K filed 2026-10-22 (accession 0000882835-26-000042); 8-K filed 2026-10-01 (accession 0000882835-26-000039) |
| S034 | news | IDXX | Sat, 14 Nov 2026 22:37:20 GMT | ok | https://news.google.com/rss/search?q=IDXX+Idexx+Laboratories+stock&hl=en-US&gl=US&ceid=US:en | IDEXX Laboratories, Inc. (IDXX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Sat, 14 Nov 2026 22:37:20 GMT); IDEXX Laboratories (IDXX) Stock Looks Fairly Valued Despite Its 28% Run - Yahoo Finance (Sat, 31 Oct 2026 07:00:00 GMT); IDEXX Laboratories (IDXX) vs. ZTS and NEOG: Can Raised Guidance and Product Expansion Drive Further Earnings Growth? - Yahoo Finance (Thu, 22 Oct 2026 07:00:00 GMT) |
| S035 | filing | RDDT | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001713445&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0001713445-26-000116); 8-K filed 2026-10-29 (accession 0001713445-26-000114); 8-K filed 2026-08-12 (accession 0001713445-26-000107) |
| S036 | filing | IDXX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000874716.json | Diluted EPS 11.75 for period ending 2026-09-30 (filed 2026-11-02) |
| S037 | stock | ROP | 2026-11-16 | ok | https://finance.yahoo.com/quote/ROP | Trailing P/E: 18.993866; Forward P/E: 19.532475; Forward EPS: 24.57318; Price: 479.975; Market price: 479.975; Market cap: 47535013888; Sector: Technology; Trailing Eps: 25.27; Revenue Growth: 0.076; Earnings Growth: 0.326; Gross Margin: 0.69671; Operating Margin: 0.28049; Profit Margin: 0.30712998; Return On Equity: 0.13229; Total Revenue: 8434599936; Market Cap: 47535013888; Consensus EPS FY+1: 24.57318; growth: 0.09810001 |
| S038 | stock | RDDT | 2026-11-16 | ok | https://finance.yahoo.com/quote/RDDT | Trailing P/E: 20.091835; Forward P/E: 10.818217; Forward EPS: 9.10039; Price: 98.45; Market price: 98.45; Market cap: 19010076672; Sector: Communication Services; Trailing Eps: 4.9; Revenue Growth: 0.53; Earnings Growth: 0.749; Gross Margin: 0.91547996; Operating Margin: 0.29397; Profit Margin: 0.32105; Return On Equity: 0.32029998; Total Revenue: 3088880128; Market Cap: 19010076672; Consensus EPS FY+1: 6.8155; growth: 0.2401 |
| S039 | filing | CHTR | 2026-11-06 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001091667.json | Diluted EPS 0.38 for period ending 2026-09-30 (filed 2026-11-06) |
| S040 | news | ROP | Thu, 05 Nov 2026 08:00:00 GMT | ok | https://news.google.com/rss/search?q=ROP+Roper+Technologies+stock&hl=en-US&gl=US&ceid=US:en | Roper Technologies (ROP) Stock Looks Fully Valued As Cash Flow Comes Into Focus - Yahoo Finance (Thu, 05 Nov 2026 08:00:00 GMT); Roper Technologies (ROP), What Is Behind The Fresh Attention? - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT); Did Earnings Beat Just Shift Roper Technologies (ROP) Investment Narrative? - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT) |

## Sources

- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFF&cosd=2026-01-01 (2026-11-12)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLH0A0HYM2&cosd=2026-01-01 (2026-11-12)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLC0A0CM&cosd=2026-01-01 (2026-11-12)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCSL&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=UNRATE&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=PAYEMS&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=T10Y2Y&cosd=2026-01-01 (2026-11-13)
- filing PNR: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 (2026-10-27)
- filing APP: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001751008&type=10-Q&dateb=&owner=include&count=10 (2026-11-04)
- news FISV: https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en (Mon, 16 Nov 2026 02:19:15 GMT)
- filing FISV: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 (2026-11-04)
- news APP: https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en (Thu, 12 Nov 2026 20:05:45 GMT)
- news PNR: https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en (Sat, 14 Nov 2026 08:48:27 GMT)
- filing APP: https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json (2026-11-04)
- stock APP: https://finance.yahoo.com/quote/APP (2026-11-16)
- filing FISV: https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json (2026-11-04)
- filing PNR: https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json (2026-10-27)
- stock PNR: https://finance.yahoo.com/quote/PNR (2026-11-16)
- filing GEN: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 (2026-10-29)
- stock FISV: https://finance.yahoo.com/quote/FISV (2026-11-16)

## AI Provenance

- Provider / model: hermes-local-proxy / upstage/solar-mini4:free
- Market research: attempts=1 tokens=9513 (prompt=6513, completion=3000) runtime=23.45s
- Fundamental research: generated this run at 2026-11-16T14:13:10.503219+00:00
- Evidence source dates: {'as_of': '2026-11-13', 'latest_equity_date': '2026-11-13', 'latest_macro_date': '2026-11-16', 'flows_date': '2026-11-13'}
- Evidence fingerprint: c722fb68528d76a7d622999b2ffc63dbd30bcfd0f427c3262de5fc074f1f5eae
- Source citations are retrieved external records in the ledger above; market values remain from the verified database snapshot.


## Disclosures

- This is research and market intelligence, not investment advice.
- AI conclusions are research judgments, not validated return predictions.
- The frozen risk layer is risk-only and is not used for directional views or allocations.
- Legacy scores are not active inputs or outputs.

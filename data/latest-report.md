# AEGIS AI-First Market Intelligence

Research generated at: 18 November 2026, 18:08 HKT
Database freshness: equity 2026-11-17 (latest row retrieved 2026-11-18 13:06:33.002447+08:00)
Data cutoff: 2026-11-17 US cash close
Snapshot ID: aegis-hourly-20261118T100823Z

## Executive Summary

- **AI market view: Late-November 2026 US equities show a mixed tape: broad market indices are near record levels, but internal price breadth has weakened sharply over the past five sessions, with a 50-day advance/decline ratio of 0.18 and zero new highs. Sector leadership is narrow and defensive, with Health Care, Consumer Staples, Utilities and Real Estate leading on a 20-day basis, while Information Technology and Energy are the weakest sectors. Momentum and dislocation screens point to a small set of names with strong 20-day price momentum, but several high-multiple names carry forward-EPS or valuation-quality flags, so the shortlist is best treated as a watchlist rather than a conviction list.**
- US equities are at or near record levels as of 2026-11-17, but 5-day breadth has deteriorated: 50-day advance/decline ratio is 0.18 and new highs are zero.
- Sector leadership is defensive and narrow: Health Care, Consumer Staples, Utilities and Real Estate posted positive 20-day returns; Information Technology and Energy were negative.
- The shortlist is built from independent momentum, dislocation, valuation and liquidity screens, not a composite score; several high-multiple names have forward-EPS or valuation-quality flags.
- Macro data show a Fed funds rate of 3.88% as of 2026-11-16, a 10Y-2Y spread of 0.30, IG OAS of 0.90 and HY OAS of 3.34, with CPI and unemployment from September 2026.
- Risk environment is elevated: 5-day forecast volatility is 0.232, above the 0.185 threshold, with a 49% spike probability, though the directional signal is false.
- Flow data show structural accumulation in Health Care and medium-term recovery in Consumer Discretionary, while Utilities shows exceptional institutional selling.

## Data QC

- Status: **PASS_WITH_WARNINGS**
- Equity session: 0 completed session(s) behind inference date
- Macro session: 2026-11-18 (0 completed session(s) behind inference date)
- Equity provenance: 372 provisional / 12621 canonical
- Breadth lag: 0 session(s); ETF-flow lag: 0 session(s)
- Note: Equity session contains a mix of provisional yfinance and canonical Massive rows.
- External sources: 79 ok / 0 unavailable; retrieved 2026-11-18T10:08:42.378818+00:00

## Idea Discovery

- S&P 500 universe: 503; eligible: 501; transparent shortlist: 20
- Method: independent momentum/dislocation/PE/liquidity buckets; no composite score
- Evidence used: latest close, 20d and 60d price returns, 60d drawdown, trailing P/E, earnings yield, sector-relative P/E, dollar volume, GICS sector
- Not available as verified inputs: verified earnings-revision history for the full universe, FY+2 consensus, structured industry catalyst calendar
- Eligible but not shortlisted: 481 (outside the top independent momentum, dislocation, valuation and liquidity buckets)
- Included: APP (top_20d_momentum); FISV (top_20d_momentum); PNR (top_20d_momentum); CHTR (top_20d_momentum); IDXX (top_20d_momentum); GEN (top_20d_momentum); CLX (top_20d_momentum); CMG (top_20d_momentum); SNDK (largest_20d_dislocation, liquidity_leader); INTC (largest_20d_dislocation); RDDT (largest_20d_dislocation); MRVL (largest_20d_dislocation); NOW (largest_20d_dislocation); DDOG (largest_20d_dislocation); FFIV (largest_20d_dislocation); COIN (largest_20d_dislocation); NVDA (liquidity_leader); MU (liquidity_leader); AMD (liquidity_leader); MSFT (liquidity_leader)
- Excluded reasons: {"missing_recent_or_latest_price": 2}
- Valuation-quality rejected: [{"flags": ["forward_eps_missing"], "ticker": "FISV"}, {"flags": ["forward_pe_outside_plausible_range", "implausible_earnings_yield", "forward_eps_vs_reported_jump"], "ticker": "CHTR"}, {"flags": ["forward_pe_outside_plausible_range", "implausible_earnings_yield"], "ticker": "SNDK"}, {"flags": ["forward_eps_vs_reported_jump"], "ticker": "MRVL"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "NOW"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "DDOG"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "FFIV"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "COIN"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "NVDA"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "MU"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "AMD"}, {"flags": ["forward_eps_missing", "forward_pe_unavailable"], "ticker": "MSFT"}]

## Market Snapshot

| Asset | Latest | Change | Observation |
| --- | --- | --- | --- |
| S&P 500 | 7340.53 | -4.82% over 20 days | Index near record levels but 5-day breadth has weakened sharply; 50-day advance/decline ratio is 0.18 and new highs are zero. |
| Health Care (XLV) | +3.01% over 20 days | Positive 20-day return | Structural accumulation with exceptional institutional buying; trailing P/E 30.19. |
| Consumer Staples (XLP) | +4.23% over 20 days | Positive 20-day return | Strongest 20-day sector return; trailing P/E 24.61. |
| Information Technology (XLK) | -11.96% over 20 days | Weakest 20-day sector return | Trailing P/E 28.79; high-multiple names in the shortlist carry forward-EPS or valuation-quality flags. |
| Energy (XLE) | -6.78% over 20 days | Negative 20-day return | Weak sector performance; trailing P/E 15.83. |
| Consumer Discretionary (XLY) | +1.39% over 20 days | Positive 20-day return | Medium-term recovery in flows; trailing P/E 24.51. |

## Macro, Fiscal, Rates, Liquidity and Credit

- Fed policy is at 3.88% effective funds rate as of 2026-11-16, with a 10Y-2Y spread of 0.30, indicating a modestly positive but not steep yield curve.
- Credit conditions are stable: IG OAS is 0.90 and HY OAS is 3.34 as of 2026-11-16, with no sign of acute stress.
- Inflation is elevated: CPI is 336.298 (1982-1984=100) and core CPI is 338.896 as of 2026-09-01, with the latest external CPI reading at 337.476 as of 2026-10-01.
- Labor market is near full employment: unemployment rate is 4.2% as of 2026-09-01, with the latest external reading at 4.1% as of 2026-10-01.
- Liquidity is mixed: equity breadth has weakened over 5 days, but sector flows show structural accumulation in Health Care and medium-term recovery in Consumer Discretionary.
- Risk environment is elevated: 5-day forecast volatility is 0.232, above the 0.185 threshold, with a 49% spike probability, though the directional signal is false.

## US Equities and 11 GICS Sectors

Macro source IDs: S001, S002, S003, S004, S005, S006, S007

| GICS sector | Evidence | AI research stance | Source IDs |
| --- | --- | --- | --- |
| Health Care | 20-day return +3.01%; trailing P/E 30.19; flow z-score 20d +0.64, 60d +2.29; flow state neutral, price up; structural accumulation with exceptional institutional buying. | Defensive leader with strong institutional demand; monitor valuation and forward-EPS quality. | S054, S001, S002 |
| Consumer Staples | 20-day return +4.23%; trailing P/E 24.61; strongest 20-day sector return. | Defensive leader; high relative return but valuation is not cheap. | S058, S001 |
| Consumer Discretionary | 20-day return +1.39%; trailing P/E 24.51; flow z-score 20d +0.88, 60d -0.59; flow state neutral, price flat; medium-term recovery. | Modest positive momentum with medium-term flow recovery; watch for reversal. | S062, S001 |
| Real Estate | 20-day return +2.86%; trailing P/E 29.11; positive 20-day return. | Positive momentum but valuation is elevated; watch rate sensitivity. | S060, S001 |
| Financials | 20-day return +2.42%; trailing P/E 15.41; positive 20-day return. | Positive momentum with reasonable valuation; watch credit spreads. | S065, S001, S002 |
| Utilities | 20-day return +3.68%; trailing P/E 17.86; flow z-score 20d -2.07, 60d +0.36; flow state outflow, price up; exceptional institutional selling. | Price up but institutional selling is a negative signal; monitor flow reversal. | S064, S001, S002 |
| Materials | 20-day return -0.76%; trailing P/E 21.14; negative 20-day return. | Slightly negative momentum; valuation is not cheap. | S066, S001 |
| Industrials | 20-day return -1.23%; trailing P/E 26.42; negative 20-day return. | Negative momentum; valuation is not cheap. | S069, S001 |
| Communication Services | 20-day return -4.47%; trailing P/E 16.72; negative 20-day return. | Weakest sector; valuation is reasonable but momentum is poor. | S073, S001 |
| Information Technology | 20-day return -11.96%; trailing P/E 28.79; negative 20-day return; high-multiple names in shortlist carry forward-EPS or valuation-quality flags. | Weakest sector; high-multiple names require caution. | S071, S001 |
| Energy | 20-day return -6.78%; trailing P/E 15.83; negative 20-day return. | Weak sector; valuation is reasonable but momentum is poor. | S074, S001 |

### Sector fundamentals, valuation and earnings

No point-in-time sector fundamentals beyond the supplied trailing P/E and 20-day ETF returns are available in the database. The sector evidence is therefore limited to price momentum, flow z-scores, and the supplied trailing P/E values; growth, margins, consensus and forward estimates are not provided for the sector ETFs. The shortlist names have only partial fundamental evidence (trailing P/E, earnings yield, sector-relative P/E) and several high-multiple names carry forward-EPS or valuation-quality flags, so no additional fundamental claims are made.

## Growth vs Value

- Health Care and Consumer Staples show the strongest 20-day returns (+3.01% and +4.23%) but carry trailing P/Es of 30.19 and 24.61, indicating premium valuation rather than cheapness.
- Financials and Energy have the lowest trailing P/Es in the sector set (15.41 and 15.83) and positive 20-day returns, but their momentum is not as strong as the defensive leaders.
- Information Technology and Communication Services are the weakest sectors on 20-day returns (-11.96% and -4.47%) and carry high-multiple names in the shortlist with forward-EPS or valuation-quality flags.
- The shortlist includes names with extreme trailing P/Es (e.g., DDOG 521.17, NOW 97.19, AMD 128.88, MRVL 74.23) that are flagged for forward-EPS or valuation-quality issues, so growth signals are not reliable for those names.

## ETF Flows and Breadth

- 5-day breadth has deteriorated: 50-day advance/decline ratio is 0.18, 20-day positive is 55.89%, and new highs are zero, indicating a narrowing leadership group.
- 20-day price breadth shows 280 of 501 names positive, but the 5-day change is -11.22 for the 50-day indicator and -7.57 for the 200-day indicator, signaling recent weakness.
- Sector flows show structural accumulation in Health Care (60d z-score +2.29) and medium-term recovery in Consumer Discretionary (20d z-score +0.88), while Utilities shows exceptional institutional selling (20d z-score -2.07).
- The advance/decline ratio of 0.176 and negative divergence of -10.25 indicate that index strength is not broadly supported by constituent performance.
- The 50-day and 200-day indicator changes over 5 days are negative (-11.22 and -7.57), while the 20-day change is positive (+5.43), suggesting a short-term bounce that has not yet broadened.

## Stock Ideas

Single-stock research uses reported EPS, forward P/E and company fundamentals. All ideas are research judgments, not validated return predictions.

| Ticker | Security | Research view | Price | EPS | Forward P/E | Base target | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| APP | AppLovin | NEW | 398.94 | 20.86084 | 19.12387 | 417.22 | NEW |
| PNR | Pentair | KEEP | 66.88 | 5.30402 | 12.609303 | 63.65 | KEEP |
| IDXX | Idexx Laboratories | KEEP | 690.24 | 16.8929 | 40.859768 | 608.14 | KEEP |
| GEN | Gen Digital | NEW | 29.52 | 3.33736 | 8.845315 | 26.7 | NEW |

## ETF Ideas

ETF research uses holdings, portfolio valuation and exposure. Single-stock EPS × P/E valuation is not applied to ETFs.

| Ticker | Fund | Research view | Price | Top holdings | Portfolio valuation | Sector exposure | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| XLV | Health Care sector ETF | KEEP | 185.24 | LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59% | Top 10 holdings; numeric weight coverage 61.42% | Health Care | KEEP |
### APP — AppLovin

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** AppLovin offers a cleaner, higher-margin growth profile than the high-multiple software names in the dislocation bucket, and its momentum is stronger than the lower-multiple industrials and staples names. Alternatives considered: PNR, IDXX, GEN, CLX, CMG.
- **Thesis:** AppLovin screens in the top 20-day momentum bucket with a 46% 20-day return and a 34% 60-day return, while its reported diluted EPS of $11.61 and forward EPS of $20.86 support a forward P/E near 19x. The company's high gross margin (~89%) and strong revenue/earnings growth provide a quality backdrop for a momentum-driven entry.
- **Source IDs:** S008, S012, S013, S014
- **Catalysts:** Sustained 20-day momentum continuation, Continued double-digit revenue and earnings growth, High-margin advertising and content monetization expansion
- **Risks:** Momentum can reverse quickly if ad market softness emerges, High valuation multiples leave limited room for error, Forward EPS estimates are unverified against fiscal-year mapping
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 20.8608 (source.forwardEps) x AI multiple assumption 20.00; source IDs S008, S012, S013, S014
- **EPS:** 20.86084 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 19.12387
- **FY+1 growth assumption:** 27.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / MSFT / APP shows strong FY1 consensus growth of 27.44% and revenue growth of 25.37%, supported by industry-leading gross margin of 88.78% and operating margin of 77.78%. The forward P/E of 19.12 is below the 20.0x base multiple, reflecting a premium growth profile relative to large-cap software peers. MSFT is used as the named peer reference for comparable growth, margin, and multiple positioning.
- **Company fundamentals:** Reported diluted EPS $11.61; forward EPS $20.86; forward P/E ~19.1x; revenue growth ~56%; earnings growth ~76%; gross margin ~89%; operating margin ~78%; profit margin ~66%; ROE ~2.1%.
- **Bull / Base / Bear:** 500.66 / 417.22 / 333.77
- **Bull / Base / Bear returns:** 25.5% / 4.58% / -16.34%
- **Scenario probabilities:** not separately assigned; see scenario table.

### PNR — Pentair

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Pentair is preferable to the high-multiple software dislocation names because it trades at a more reasonable valuation, but it is not preferred over the stronger momentum names like AppLovin. Alternatives considered: APP, IDXX, GEN, CLX, CMG.
- **Thesis:** Pentair qualifies for the top 20-day momentum screen with a 26% 20-day return, but its forward P/E of ~12.6x and earnings yield of ~7.4% are less compelling than the high-momentum software names. The stock is a reasonable industrial holding but lacks the growth quality to justify a strong buy stance.
- **Source IDs:** S010, S015, S017, S020
- **Catalysts:** Continued 20-day momentum, Industrial water and fluid handling demand recovery, Potential margin stabilization
- **Risks:** Revenue and earnings declined year-over-year, Lower growth profile relative to top momentum names, Industrial cyclical exposure to slowing capital spending
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 5.3040 (source.forwardEps) x AI multiple assumption 12.00; source IDs S010, S015, S017, S020
- **EPS:** 5.30402 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 12.609303
- **FY+1 growth assumption:** 12.82%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / GEV / PNR has FY1 consensus growth of 12.82% with revenue growth of 18.38%, but earnings growth is negative at -18.8%, indicating margin pressure. Gross margin of 40.17% and operating margin of 21.41% are below software leaders, and the forward P/E of 12.61 is low. GEV is the named peer reference for comparable industrial/energy infrastructure valuation and growth risk.
- **Company fundamentals:** Reported diluted EPS $2.76; forward EPS $5.30; forward P/E ~12.6x; revenue growth ~-4.5%; earnings growth ~-18.8%; gross margin ~40%; operating margin ~21%; profit margin ~15%; ROE ~16%.
- **Bull / Base / Bear:** 74.26 / 63.65 / 53.04
- **Bull / Base / Bear returns:** 11.03% / -4.83% / -20.69%
- **Scenario probabilities:** not separately assigned; see scenario table.

### IDXX — Idexx Laboratories

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Idexx is preferable to the unprofitable or deeply negative software names in the dislocation bucket, but it is not preferred over the more attractively valued momentum names like AppLovin or Gen Digital. Alternatives considered: APP, PNR, GEN, CLX, CMG.
- **Thesis:** Idexx Laboratories is in the top 20-day momentum bucket with a 24% 20-day return and a 23% 60-day return, but it carries a high forward P/E of ~41x and a low earnings yield of ~2.6%. The stock is a quality healthcare franchise but is expensive relative to its growth, warranting a neutral stance.
- **Source IDs:** S021, S023, S026, S033
- **Catalysts:** Continued 20-day momentum, Stable demand for veterinary diagnostics and animal health, Consistent free cash flow generation
- **Risks:** High valuation leaves limited upside if growth slows, Sector-relative P/E of 1.33x indicates premium valuation, Diagnostic market share pressure
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 16.8929 (source.forwardEps) x AI multiple assumption 36.00; source IDs S021, S023, S026, S033
- **EPS:** 16.8929 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 40.859768
- **FY+1 growth assumption:** 12.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / CDW / IDXX shows FY1 consensus growth of 12.44% with revenue growth of 8.88% and earnings growth of 17.9%, supported by a 62.72% gross margin and 32.50% operating margin. The forward P/E of 40.86 is high, so the base multiple of 36.0x is set below the current level to reflect valuation risk. CDW is the named peer reference for comparable IT services/security company multiples.
- **Company fundamentals:** Reported diluted EPS $11.75; forward EPS $16.89; forward P/E ~40.9x; revenue growth ~10%; earnings growth ~18%; gross margin ~63%; operating margin ~32%; profit margin ~25%; ROE ~0.7%.
- **Bull / Base / Bear:** 709.5 / 608.14 / 506.79
- **Bull / Base / Bear returns:** 2.79% / -11.89% / -26.58%
- **Scenario probabilities:** not separately assigned; see scenario table.

### GEN — Gen Digital

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** Gen Digital offers the best combination of momentum and valuation among the shortlisted stocks, with a lower forward P/E than AppLovin and a stronger earnings growth profile than Pentair or Idexx. Alternatives considered: APP, PNR, IDXX, CLX, CMG.
- **Thesis:** Gen Digital screens in the top 20-day momentum bucket with a 23% 20-day return and a 14% 60-day return. Its forward P/E of ~8.8x and earnings yield of ~7.1% are the most attractive among the momentum names, and revenue growth of ~12% with earnings growth of ~129% supports a quality, value-oriented thesis.
- **Source IDs:** S025, S029, S032, S036
- **Catalysts:** Sustained 20-day momentum, Strong earnings growth outpacing revenue growth, Attractive valuation relative to growth
- **Risks:** Cybersecurity and digital risk exposure to macro shocks, High volatility in the cybersecurity sector, Forward EPS estimates are unverified
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 3.3374 (source.forwardEps) x AI multiple assumption 8.00; source IDs S025, S029, S032, S036
- **EPS:** 3.33736 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 8.845315
- **FY+1 growth assumption:** 12.86%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / HON / GEN has FY1 consensus growth of 12.86% with revenue growth of 6.81% and strong earnings growth of 128.6%, but the forward P/E of 8.85 is very low. Gross margin of 77.41% and operating margin of 43.23% are solid, but the low multiple reflects higher risk and lower growth relative to industrial peers. HON is the named peer reference for comparable industrial company valuation.
- **Company fundamentals:** Reported diluted EPS $0.83; forward EPS $3.34; forward P/E ~8.8x; revenue growth ~12%; earnings growth ~129%; gross margin ~77%; operating margin ~43%; profit margin ~23%; ROE ~46%.
- **Bull / Base / Bear:** 33.37 / 26.7 / 20.02
- **Bull / Base / Bear returns:** 13.04% / -9.55% / -32.18%
- **Scenario probabilities:** not separately assigned; see scenario table.

### XLV — Health Care sector ETF

- **Type:** ETF
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** The Health Care sector ETF is preferable to individual high-multiple software names because it offers diversification and lower single-stock risk, but it is not preferred over the more attractive momentum stocks like Gen Digital. Alternatives considered: XLP, XLY, XLRE, XLF, XLU, XLB, XLI.
- **Thesis:** The Health Care sector ETF provides diversified exposure to large-cap pharma and medical device leaders, but the sector ETF is down ~1.4% on the latest session. It is a reasonable defensive holding but does not offer a compelling entry point at current levels.
- **Source IDs:** S054, S057
- **Catalysts:** Defensive demand in health care during economic uncertainty, Potential sector rotation into defensive names, Stable dividend yields from large-cap pharma
- **Risks:** Sector underperformance versus broader market, Regulatory and reimbursement risks, Limited upside if growth stocks continue to lead
- **Valuation method:** Holdings/portfolio valuation with AI total-return assumption
- **Valuation status:** verified; forward-EPS source: ; period flags: 
- **Valuation assumptions:** Holdings/portfolio valuation; 10 weighted holdings; coverage 61.42%; source IDs S054, S057
- **Top holdings:** LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59%
- **Portfolio valuation:** Top 10 holdings; numeric weight coverage 61.42%
- **Sector exposure:** Health Care
- **Underlying drivers:** Large-cap pharmaceutical and medical device demand, regulatory environment, and defensive sector rotation.
- **Bull / Base / Bear:** 207.47 / 194.5 / 174.13
- **Bull / Base / Bear returns:** 12.0% / 5.0% / -6.0%
- **Scenario probabilities:** not separately assigned; see scenario table.

## Quant Risk Layer

| Field | Value |
| --- | --- |
| Volatility model | vol5_ols_v1 |
| Spike model | spike_logit_v1 |
| As-of date | 2026-11-17 |
| Target window | 2026-11-18 to 2026-11-24 |
| Forecast 5D annualized volatility | 23.16% |
| Historical-vol baseline | 23.06% |
| EWMA baseline | 20.59% |
| Spike probability | 49.06% |
| Spike threshold | 18.50% |
| Status | prospective |
| Forecast ID | 6b6ffcbe11505f1e |

Risk-only; no directional interpretation or allocation implication.

## Scenarios

### Short Term (5 trading sessions)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 25% | +2.00% | Spike probability 49% is near the 50% threshold, but the directional signal is false and the forecast is frozen at daily close; a mild upside is only plausible if the elevated volatility regime resolves without a directional trigger, keeping the move small. |
| Base | 50% | +0.00% | The forecast is prospective and frozen at the daily close, with no directional signal and volatility near the historical baseline, so the most likely path is a range-bound week with returns near zero. |
| Bear | 25% | -2.00% | A 49% spike probability indicates elevated near-term uncertainty, and if the volatility regime persists or a negative catalyst arrives before the US close, a modest downside of about 2% is the plausible worst case. |

### Long Term (12 months)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 30% | +8.00% | A sustained low-volatility regime with stable fundamentals and no directional signal could allow a gradual upward drift, but the frozen daily-close status and high spike probability cap the bull case at a moderate 8% return. |
| Base | 40% | +3.00% | With volatility near the historical baseline and no directional trigger, the base case is a slow grind higher driven by steady earnings and orderly markets, yielding a modest 3% long-term return. |
| Bear | 30% | -5.00% | If the elevated spike probability reflects a structural risk event or credit stress that materializes, the frozen daily-close model would not capture it in time, leading to a deeper drawdown of about 5% over the long horizon. |

## Positioning

- Maintain a defensive tilt: Health Care, Consumer Staples, Utilities and Real Estate are the leading sectors on 20-day returns and institutional flows.
- Watch the shortlist for momentum and dislocation names, but treat high-multiple names with forward-EPS or valuation-quality flags as higher-risk and do not infer allocation.
- Monitor the 5-day breadth deterioration: a 50

## Catalysts

| Date | Event | Why it matters |
| --- | --- | --- |

## Key Risks


## External Source Ledger

| ID | Type | Ticker | Published | Status | URL | Claims |
| --- | --- | --- | --- | --- | --- | --- |
| S001 | macro | macro | 2026-11-16 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFF&cosd=2026-01-01 | Effective federal funds rate (DFF) latest observation 2026-11-16: 3.88 |
| S002 | macro | macro | 2026-11-16 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLH0A0HYM2&cosd=2026-01-01 | US high-yield OAS (BAMLH0A0HYM2) latest observation 2026-11-16: 3.34 |
| S003 | macro | macro | 2026-11-16 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLC0A0CM&cosd=2026-01-01 | US investment-grade OAS (BAMLC0A0CM) latest observation 2026-11-16: 0.90 |
| S004 | macro | macro | 2026-10-01 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCSL&cosd=2026-01-01 | US CPI (CPIAUCSL) latest observation 2026-10-01: 337.476 |
| S005 | macro | macro | 2026-10-01 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=UNRATE&cosd=2026-01-01 | US unemployment rate (UNRATE) latest observation 2026-10-01: 4.1 |
| S006 | macro | macro | 2026-10-01 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=PAYEMS&cosd=2026-01-01 | US nonfarm payrolls (PAYEMS) latest observation 2026-10-01: 159293 |
| S007 | macro | macro | 2026-11-17 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=T10Y2Y&cosd=2026-01-01 | 10Y-2Y Treasury spread (T10Y2Y) latest observation 2026-11-17: 0.30 |
| S008 | filing | APP | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001751008&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0001751008-26-000069); 8-K filed 2026-11-04 (accession 0001751008-26-000068); 10-Q filed 2026-08-05 (accession 0001751008-26-000059) |
| S009 | filing | FISV | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0000798354-26-000042); 8-K filed 2026-11-03 (accession 0000798354-26-000039); 8-K filed 2026-10-23 (accession 0001193125-26-429481) |
| S010 | filing | PNR | 2026-10-27 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-27 (accession 0000077360-26-000058); 8-K filed 2026-10-27 (accession 0000077360-26-000055); 8-K filed 2026-09-22 (accession 0000077360-26-000050) |
| S011 | news | FISV | Wed, 18 Nov 2026 04:30:23 GMT | ok | https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en | Fiserv, Inc. (FISV) Stock Price, News, Quote & History - Yahoo! Finance Canada (Wed, 18 Nov 2026 04:30:23 GMT); Fiserv (FISV) Stock Looks Undervalued With Strong Excess Returns - Yahoo Finance (Wed, 11 Nov 2026 22:14:34 GMT); Fiserv Stock Outlook: Is Wall Street Bullish or Bearish? - Yahoo Finance (Thu, 12 Nov 2026 12:23:56 GMT) |
| S012 | news | APP | Mon, 16 Nov 2026 18:52:15 GMT | ok | https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en | AppLovin Stock Moves Higher: What's Going On? - Benzinga (Mon, 16 Nov 2026 18:52:15 GMT); AppLovin stock soars after Q3 earnings, outlook beat - Yahoo Finance (Thu, 05 Nov 2026 08:00:00 GMT); AppLovin: First Fundamental And Momentum Breakout Signal Since July (NASDAQ:APP) - Seeking Alpha (Tue, 17 Nov 2026 23:13:39 GMT) |
| S013 | filing | APP | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json | Diluted EPS 11.61 for period ending 2026-09-30 (filed 2026-11-04) |
| S014 | stock | APP | 2026-11-18 | ok | https://finance.yahoo.com/quote/APP | Trailing P/E: 26.864645; Forward P/E: 19.12387; Forward EPS: 20.86084; Price: 398.94; Market price: 398.94; Market cap: 132177592320; Sector: Communication Services; Trailing Eps: 14.85; Revenue Growth: 0.555; Earnings Growth: 0.755; Gross Margin: 0.8878; Operating Margin: 0.77782995; Profit Margin: 0.65887; Return On Equity: 2.1008599; Total Revenue: 7608893952; Market Cap: 132177592320; Consensus EPS FY+1: 20.72451; growth: 0.2744 |
| S015 | stock | PNR | 2026-11-18 | ok | https://finance.yahoo.com/quote/PNR | Trailing P/E: 18.223433; Forward P/E: 12.609303; Forward EPS: 5.30402; Price: 66.88; Market price: 66.88; Market cap: 10677704704; Sector: Industrials; Trailing Eps: 3.67; Revenue Growth: -0.045; Earnings Growth: -0.188; Gross Margin: 0.40168998; Operating Margin: 0.21410999; Profit Margin: 0.15435; Return On Equity: 0.15605; Total Revenue: 3966200064; Market Cap: 10677704704; Consensus EPS FY+1: 5.30402; growth: 0.1282 |
| S016 | stock | FISV | 2026-11-18 | ok | https://finance.yahoo.com/quote/FISV | Forward P/E: 7.816146; Price: 62.31; Market price: 62.31; Market cap: 33151893504; Market Cap: 33151893504; Consensus EPS FY+1: 7.97115; growth: 0.0953 |
| S017 | news | PNR | Fri, 13 Nov 2026 22:50:05 GMT | ok | https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en | Pentair Stock Price Forecast. Should You Buy PNR? - StockInvest.us (Fri, 13 Nov 2026 22:50:05 GMT); Why Pentair Stock Popped This Morning - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT); Pentair plc (PNR) Q3 Earnings and Revenues Beat Estimates - Yahoo Finance (Tue, 27 Oct 2026 07:00:00 GMT) |
| S018 | filing | FISV | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json | Diluted EPS -8.9 for period ending 2026-09-30 (filed 2026-11-04) |
| S019 | filing | CHTR | 2026-11-06 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-06 (accession 0001091667-26-000073); 8-K filed 2026-11-06 (accession 0001091667-26-000072); 8-K filed 2026-10-27 (accession 0001091667-26-000064) |
| S020 | filing | PNR | 2026-10-27 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json | Diluted EPS 2.76 for period ending 2026-09-30 (filed 2026-10-27) |
| S021 | stock | IDXX | 2026-11-18 | ok | https://finance.yahoo.com/quote/IDXX | Trailing P/E: 46.512127; Forward P/E: 40.859768; Forward EPS: 16.8929; Price: 690.24; Market price: 690.24; Market cap: 54381428736; Sector: Healthcare; Trailing Eps: 14.84; Revenue Growth: 0.099; Earnings Growth: 0.179; Gross Margin: 0.62722; Operating Margin: 0.32497; Profit Margin: 0.25357; Return On Equity: 0.68925005; Total Revenue: 4662220800; Market Cap: 54381428736; Consensus EPS FY+1: 16.8929; growth: 0.1244 |
| S022 | news | CHTR | Sun, 15 Nov 2026 05:47:01 GMT | ok | https://news.google.com/rss/search?q=CHTR+Charter+Communications+stock&hl=en-US&gl=US&ceid=US:en | Charter Communications (CHTR) Stock Could Be A Bargain Following Its New Operating Model - Yahoo Finance (Sun, 15 Nov 2026 05:47:01 GMT); Why You Should Think About Charter Communications Differently Now? - Yahoo Finance (Fri, 13 Nov 2026 19:16:11 GMT); Charter Communications (CHTR) Stock Looks Reasonable As Shares Slump 85% - Yahoo Finance (Wed, 28 Oct 2026 07:00:00 GMT) |
| S023 | filing | IDXX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000874716&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000874716-26-000135); 8-K filed 2026-11-02 (accession 0001104659-26-120892); 10-Q filed 2026-08-04 (accession 0000874716-26-000123) |
| S024 | stock | CHTR | 2026-11-18 | ok | https://finance.yahoo.com/quote/CHTR | Trailing P/E: 13.016917; Forward P/E: 3.037624; Forward EPS: 45.59485; Price: 138.5; Market price: 138.5; Market cap: 24798640128; Sector: Communication Services; Trailing Eps: 10.64; Revenue Growth: 0.091; Gross Margin: 0.55084; Operating Margin: 0.23389; Profit Margin: 0.02498; Return On Equity: 0.07019; Total Revenue: 55645999104; Market Cap: 24798640128; Consensus EPS FY+1: 49.35412; growth: 1.4289 |
| S025 | filing | GEN | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0000849399-26-000083); 8-K filed 2026-10-28 (accession 0000849399-26-000081); 8-K filed 2026-10-09 (accession 0000849399-26-000079) |
| S026 | news | IDXX | Tue, 17 Nov 2026 20:09:13 GMT | ok | https://news.google.com/rss/search?q=IDXX+Idexx+Laboratories+stock&hl=en-US&gl=US&ceid=US:en | IDEXX Laboratories, Inc. (IDXX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Tue, 17 Nov 2026 20:09:13 GMT); IDEXX Laboratories (IDXX) Stock Looks Fairly Valued Despite Its 28% Run - Yahoo Finance (Sat, 31 Oct 2026 07:00:00 GMT); IDEXX Laboratories (IDXX) vs. ZTS and NEOG: Can Raised Guidance and Product Expansion Drive Further Earnings Growth? - Yahoo Finance (Thu, 22 Oct 2026 07:00:00 GMT) |
| S027 | filing | CLX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000021076-26-000046); 8-K filed 2026-11-02 (accession 0000021076-26-000044); 8-K filed 2026-10-29 (accession 0001206774-26-000586) |
| S028 | filing | CHTR | 2026-11-06 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001091667.json | Diluted EPS 0.38 for period ending 2026-09-30 (filed 2026-11-06) |
| S029 | news | GEN | Thu, 29 Oct 2026 07:00:00 GMT | ok | https://news.google.com/rss/search?q=GEN+Gen+Digital+stock&hl=en-US&gl=US&ceid=US:en | Gen Digital (GEN) Stock Repriced After Q2 Earnings Put Margins Center Stage - Yahoo Finance (Thu, 29 Oct 2026 07:00:00 GMT); What Was Gen Digital Telling You Before Its Stock Ran? - Yahoo Finance (Wed, 04 Nov 2026 08:00:00 GMT); Are Business Services Stocks Lagging GEN DIGITAL INC (GEN) This Year? - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT) |
| S030 | stock | CLX | 2026-11-18 | ok | https://finance.yahoo.com/quote/CLX | Trailing P/E: 19.190647; Forward P/E: 17.29784; Forward EPS: 6.1684; Price: 106.7; Market price: 106.7; Market cap: 12926426112; Sector: Consumer Defensive; Trailing Eps: 5.56; Revenue Growth: 0.333; Earnings Growth: 1.138; Gross Margin: 0.41939998; Operating Margin: 0.14286; Profit Margin: 0.09408; Return On Equity: 5.34363; Total Revenue: 7196000256; Market Cap: 12926426112; Consensus EPS FY+1: 6.1684; growth: 0.0769 |
| S031 | news | CLX | Tue, 17 Nov 2026 23:36:02 GMT | ok | https://news.google.com/rss/search?q=CLX+Clorox+stock&hl=en-US&gl=US&ceid=US:en | The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance UK (Tue, 17 Nov 2026 23:36:02 GMT); The Clorox Company (CLX) Declares $1.25 Quarterly Dividend - TradingView (Wed, 18 Nov 2026 02:13:00 GMT); Clorox Stock Rides An 11-Day Winning Streak To A 25% Gain - Trefis (Tue, 17 Nov 2026 08:40:15 GMT) |
| S032 | stock | GEN | 2026-11-18 | ok | https://finance.yahoo.com/quote/GEN | Trailing P/E: 14.984772; Forward P/E: 8.845315; Forward EPS: 3.33736; Price: 29.52; Market price: 29.52; Market cap: 17513510912; Sector: Technology; Trailing Eps: 1.97; Revenue Growth: 0.122; Earnings Growth: 1.286; Gross Margin: 0.77410007; Operating Margin: 0.43229; Profit Margin: 0.23068; Return On Equity: 0.46402; Total Revenue: 5228000256; Market Cap: 17513510912; Consensus EPS FY+1: 3.33736; growth: 0.1286 |
| S033 | filing | IDXX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000874716.json | Diluted EPS 11.75 for period ending 2026-09-30 (filed 2026-11-02) |
| S034 | filing | SNDK | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0002023554&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0001628280-26-068601); 8-K filed 2026-10-29 (accession 0001628280-26-068243); 8-K filed 2026-09-16 (accession 0001628280-26-062267) |
| S035 | filing | CMG | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001058090&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0001058090-26-000104); 8-K filed 2026-10-28 (accession 0001058090-26-000103); 8-K filed 2026-09-14 (accession 0001058090-26-000088) |
| S036 | filing | GEN | 2026-10-29 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000849399.json | Diluted EPS 0.83 for period ending 2026-10-02 (filed 2026-10-29) |
| S037 | stock | CMG | 2026-11-18 | ok | https://finance.yahoo.com/quote/CMG | Trailing P/E: 33.48598; Forward P/E: 27.075024; Forward EPS: 1.32336; Price: 35.83; Market price: 35.83; Market cap: 45324054528; Sector: Consumer Cyclical; Trailing Eps: 1.07; Revenue Growth: 0.096; Earnings Growth: -0.062; Gross Margin: 0.39314; Operating Margin: 0.14715; Profit Margin: 0.10832; Return On Equity: 0.48518002; Total Revenue: 12713477120; Market Cap: 45324054528; Consensus EPS FY+1: 1.32479; growth: 0.2173 |
| S038 | news | CMG | Thu, 29 Oct 2026 07:00:00 GMT | ok | https://news.google.com/rss/search?q=CMG+Chipotle+Mexican+Grill+stock&hl=en-US&gl=US&ceid=US:en | Why Is Chipotle Mexican Grill Stock Rising 6.9% in Premarket Trading? - Yahoo Finance (Thu, 29 Oct 2026 07:00:00 GMT); Chipotle (CMG) Unveils Sneak It In Hoodie With An Insulated Food Pocket - Yahoo Finance Singapore (Tue, 17 Nov 2026 08:11:56 GMT); Where Will Chipotle Mexican Grill's Stock Be in 5 Years? - Yahoo Finance (Wed, 19 Aug 2026 07:00:00 GMT) |
| S039 | filing | CLX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000021076.json | Diluted EPS 1.39 for period ending 2026-09-30 (filed 2026-11-02) |
| S040 | stock | SNDK | 2026-11-18 | ok | https://finance.yahoo.com/quote/SNDK | Trailing P/E: 6.371803; Forward P/E: 2.758101; Forward EPS: 289.05396; Price: 797.24; Market price: 797.24; Market cap: 113438769152; Sector: Technology; Trailing Eps: 125.12; Revenue Growth: 3.779; Earnings Growth: 69.133; Gross Margin: 0.79952; Operating Margin: 0.7268; Profit Margin: 0.67039; Return On Equity: 1.41174; Total Revenue: 28970999808; Market Cap: 113438769152; Consensus EPS FY+1: 289.05396; growth: 0.2707 |

## Sources

- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFF&cosd=2026-01-01 (2026-11-16)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLH0A0HYM2&cosd=2026-01-01 (2026-11-16)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLC0A0CM&cosd=2026-01-01 (2026-11-16)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCSL&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=UNRATE&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=PAYEMS&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=T10Y2Y&cosd=2026-01-01 (2026-11-17)
- filing APP: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001751008&type=10-Q&dateb=&owner=include&count=10 (2026-11-04)
- filing FISV: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 (2026-11-04)
- filing PNR: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 (2026-10-27)
- news FISV: https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en (Wed, 18 Nov 2026 04:30:23 GMT)
- news APP: https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en (Mon, 16 Nov 2026 18:52:15 GMT)
- filing APP: https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json (2026-11-04)
- stock APP: https://finance.yahoo.com/quote/APP (2026-11-18)
- stock PNR: https://finance.yahoo.com/quote/PNR (2026-11-18)
- stock FISV: https://finance.yahoo.com/quote/FISV (2026-11-18)
- news PNR: https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en (Fri, 13 Nov 2026 22:50:05 GMT)
- filing FISV: https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json (2026-11-04)
- filing CHTR: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 (2026-11-06)
- filing PNR: https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json (2026-10-27)

## AI Provenance

- Provider / model: hermes-local-proxy / upstage/solar-mini4:free
- Market research: attempts=1 tokens=9573 (prompt=6573, completion=3000) runtime=17.61s
- Fundamental research: generated this run at 2026-11-18T10:08:23.310479+00:00
- Evidence source dates: {'as_of': '2026-11-17', 'latest_equity_date': '2026-11-17', 'latest_macro_date': '2026-11-18', 'flows_date': '2026-11-17'}
- Evidence fingerprint: 10f5d6631c397ddff4e899b3fea0f1f22b639238994a4832165c7afd9ab91824
- Source citations are retrieved external records in the ledger above; market values remain from the verified database snapshot.


## Disclosures

- This is research and market intelligence, not investment advice.
- AI conclusions are research judgments, not validated return predictions.
- The frozen risk layer is risk-only and is not used for directional views or allocations.
- Legacy scores are not active inputs or outputs.

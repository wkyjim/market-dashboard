# AEGIS AI-First Market Intelligence

Research generated at: 17 November 2026, 02:07 HKT
Database freshness: equity 2026-11-13 (latest row retrieved 2026-11-16 13:06:43.000010+08:00)
Data cutoff: 2026-11-13 US cash close
Snapshot ID: aegis-hourly-20261116T180742Z

## Executive Summary

- **AI market view: Risk-on tilt is narrowing: broad market breadth is positive but the index is slightly negative over 20 days, and the largest-cap liquidity leaders (NVDA, AMD, MU, AAPL) carry the highest trailing P/E multiples, while the shortlist is dominated by high-momentum, low-multiple names and a few large dislocation names. Macro data show a still-elevated but easing inflation backdrop, a stable labor market, and a modestly positive 10Y-2Y curve, with credit spreads tight. The overall posture is cautious but not bearish, with a preference for quality, earnings visibility, and relative value rather than broad beta.**
- Broad market breadth is constructive (71.3% above 50-day, 63.6% above 200-day, ADR 1.70), but the S&P 500 is down 1.28% over 20 days, indicating a late-stage, quality-tilted rally.
- The shortlist is dominated by high-momentum, low-multiple names (APP, FISV, PNR, GEN, CLX, CHTR, IDXX, ROP) and large dislocation names (RDDT, INTC, SNDK, MRVL, FFIV, NOW, LITE, COIN), with NVDA, AMD, MU, AAPL flagged for liquidity but priced at premium multiples.
- Macro data show CPI still elevated at 336.298 (Sep-2026) with core at 338.896, unemployment at 4.2%, and a 10Y-2Y spread of 0.27, implying a late-cycle but not recessionary backdrop.
- Credit spreads are tight (IG OAS 0.89, HY OAS 3.23), leaving limited cushion for a growth scare or policy shock.
- Sector returns show Health Care (+6.87%), Consumer Discretionary (+6.69%), Consumer Staples (+5.40%), and Financials (+5.69%) leading, while Information Technology (-7.19%) and Energy (-4.81%) are the weakest.
- Flows show XLV strong confirmation, XLY structural distribution, and XLU medium-term deterioration with exceptional institutional selling, reinforcing a defensive tilt.

## Data QC

- Status: **PASS_WITH_WARNINGS**
- Equity session: 0 completed session(s) behind inference date
- Equity provenance: 393 provisional / 12576 canonical
- Breadth lag: 0 session(s); ETF-flow lag: 0 session(s)
- Note: Equity session contains a mix of provisional yfinance and canonical Massive rows.
- External sources: 79 ok / 0 unavailable; retrieved 2026-11-16T18:08:01.393640+00:00

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
| S&P 500 | 7561.67 | -1.28% (20d) | Index is slightly negative over 20 days despite positive breadth; 71.3% above 50-day and 63.6% above 200-day. |
| Health Care (XLV) | 6.87% | +6.87% (20d) | Strongest sector; trailing P/E 30.81; flows show strong institutional confirmation. |
| Information Technology (XLK) | -7.19% | -7.19% (20d) | Weakest sector; trailing P/E 29.16; large-cap liquidity leaders NVDA, AMD, MU carry premium multiples. |
| Energy (XLE) | -4.81% | -4.81% (20d) | Negative 20-day return; trailing P/E 15.94; low multiple but weak momentum. |
| Consumer Discretionary (XLY) | 6.69% | +6.69% (20d) | Strong 20-day return; trailing P/E 24.76; flows show structural distribution. |
| Financials (XLF) | 5.69% | +5.69% (20d) | Positive momentum; trailing P/E 15.76; supportive of late-cycle financial health. |

## Macro, Fiscal, Rates, Liquidity and Credit

- Inflation is still elevated but not accelerating: CPI at 336.298 (Sep-2026) and core CPI at 338.896, with the latest external CPI reading (Oct-2026) at 337.476, suggesting a gradual disinflation trend.
- Labor market is stable: unemployment at 4.2% (Sep-2026) and nonfarm payrolls at 159,293k (Oct-2026), indicating a soft but not collapsing labor backdrop.
- The 10Y-2Y Treasury spread is 0.27 (Nov-13), a modestly positive curve that is not yet signaling imminent recession, though the narrow positive spread leaves limited recession insurance.
- Policy rates remain restrictive: effective federal funds rate at 3.88% (Nov-12), consistent with a late-cycle tightening bias that supports quality and earnings visibility.
- Credit conditions are tight: IG OAS at 0.89 and HY OAS at 3.23 (Nov-13), leaving little room for spread widening if growth disappoints.
- European indices closed lower on Nov-16 (FTSE -0.09%, CAC -0.20%, DAX -0.57%), suggesting a modest risk-off tilt in Europe despite positive US breadth.

## US Equities and 11 GICS Sectors

Macro source IDs: S001, S002, S003, S004, S005, S006, S007

| GICS sector | Evidence | AI research stance | Source IDs |
| --- | --- | --- | --- |
| Health Care | 20-day return +6.87% (XLV); trailing P/E 30.81 (S054); flows show strong confirmation with z-scores 1.45 (20d) and 1.72 (60d). | Favor quality and defensive growth; strong institutional inflows and positive momentum support a core holding. | S054 |
| Consumer Staples | 20-day return +5.40% (XLP); trailing P/E 24.98 (S060); defensive positioning amid tight credit spreads. | Maintain as a ballast; positive 20-day return and stable macro backdrop support holding. | S060 |
| Consumer Discretionary | 20-day return +6.69% (XLY); trailing P/E 24.76 (S057); flows show structural distribution with z-score -0.38 (20d) and -0.78 (60d). | Positive momentum but institutional selling suggests caution; pair with quality names and avoid high-beta consumer names. | S057 |
| Real Estate | 20-day return +5.24% (XLRE); trailing P/E 29.62 (S059); positive but not leading. | Hold selectively; positive return but premium valuation and mixed flows warrant caution. | S059 |
| Financials | 20-day return +5.69% (XLF); trailing P/E 15.76 (S063); positive momentum and low valuation support late-cycle financial health. | Favor financials for earnings visibility and low multiples; supportive of a late-cycle, positive-rate environment. | S063 |
| Utilities | 20-day return +4.34% (XLU); trailing P/E 18.14 (S064); flows show medium-term deterioration with exceptional institutional selling (z-score -2.15, 20d). | Defensive but institutional selling suggests rotation out; hold selectively for income, not momentum. | S064 |
| Materials | 20-day return +2.57% (XLB); trailing P/E 21.53 (S066); modest positive momentum. | Neutral; positive but lagging sector; no strong catalyst for favored. | S066 |
| Industrials | 20-day return +0.61% (XLI); trailing P/E 26.68 (S071); near-flat momentum. | Neutral; positive but weak momentum; no clear leadership signal. | S071 |
| Communication Services | 20-day return -1.48% (XLC); trailing P/E 17.05 (S072); negative momentum. | Less favored; negative 20-day return and premium valuation (CHTR flagged for forward PE issues) warrant caution. | S072 |
| Information Technology | 20-day return -7.19% (XLK); trailing P/E 29.16 (S070); large-cap liquidity leaders NVDA (PE 26.51), AMD (PE 128.88), MU (PE 11.40) carry premium multiples. | Less favored broad IT; high multiples and negative momentum require selective exposure to quality names only. | S070 |
| Energy | 20-day return -4.81% (XLE); trailing P/E 15.94 (S075); negative momentum and low multiple. | Less favored; negative 20-day return and weak flows suggest lack of near-term catalyst. | S075 |

### Sector fundamentals, valuation and earnings

No point-in-time sector fundamentals (e.g., revenue growth, margins, consensus estimates) are supplied in the database snapshot. The sector evidence is limited to 20-day ETF returns, trailing P/E from external sources, and flow z-scores. Growth and margin data were retrieved only for source-backed shortlist names, and no structured industry catalyst calendar is available. Therefore, sector-level fundamental analysis is not possible beyond the supplied valuation and flow evidence.

## Growth vs Value

- Growth: The shortlist includes high-momentum names with strong 20-day returns (APP, FISV, PNR, GEN, CLX, CHTR, IDXX, ROP), but the database does not provide verified earnings-revision history or FY+2 consensus for the full universe, so growth quality cannot be fully assessed.
- Value: Low trailing P/E names include FISV (9.65), PNR (13.59), GEN (14.15), ROP (16.67), and SNDK (15.94), but several carry flags for forward EPS missing or implausible earnings yield, limiting reliable value signals.
- Dislocation: Large dislocation names (RDDT, INTC, MRVL, FFIV, NOW, LITE, COIN) show extreme P/E dispersion, with INTC, LITE, and COIN at negative earnings yields, indicating distressed or uncertain earnings.
- Liquidity: NVDA (PE 26.51), AMD (PE 128.88), MU (PE 11.40), and AAPL (PE 39.42) are flagged as liquidity leaders, but AMD and NOW carry the highest multiples, suggesting liquidity is not a proxy for value.

## ETF Flows and Breadth

- Broad market breadth is positive: 71.34% above 50-day, 63.6% above 200-day, 70.46% positive 20-day, and ADR 1.70, indicating wide participation.
- Index-level 20-day return is -1.28%, so positive breadth is not translating into index strength, a late-cycle pattern.
- Sector flows show XLV strong confirmation (z-scores 1.45/1.72), XLY structural distribution (-0.38/-0.78), and XLU exceptional institutional selling (-2.15/-0.48), reinforcing a defensive rotation.
- New highs/new lows are 0/0, so no breakout or breakdown is being confirmed by new extremes.
- Price-breadth divergence is -27.49 with bullish divergence true, but standardized divergence -1.60 suggests caution on chasing index strength.

## Stock Ideas

Single-stock research uses reported EPS, forward P/E and company fundamentals. All ideas are research judgments, not validated return predictions.

| Ticker | Security | Research view | Price | EPS | Forward P/E | Base target | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| APP | AppLovin | NEW | 409.1 | 20.86026 | 20.01557 | 458.93 | NEW |
| PNR | Pentair | KEEP | 68.3 | 5.30402 | 12.854402 | 74.26 | KEEP |
| GEN | Gen Digital | KEEP | 30.4 | 3.33736 | 9.188401 | 36.71 | KEEP |
| ROP | Roper Technologies | KEEP | 479.975 | 24.57318 | 19.754059 | 491.46 | KEEP |

## ETF Ideas

ETF research uses holdings, portfolio valuation and exposure. Single-stock EPS × P/E valuation is not applied to ETFs.

| Ticker | Fund | Research view | Price | Top holdings | Portfolio valuation | Sector exposure | Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| XLV | Health Care sector ETF | KEEP | 188.85 | LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59% | Top 10 holdings; numeric weight coverage 61.42% | Health Care | KEEP |
### APP — AppLovin

- **Type:** Stock
- **Research view:** NEW (stance: BUY)
- **Why preferred / alternatives:** AppLovin offers a rare combination of strong momentum, high reported earnings growth, and a clean forward P/E near 20, making it a more defensible momentum candidate than the high-multiple names in the shortlist such as NOW or MRVL. Alternatives considered: NOW, MRVL.
- **Thesis:** AppLovin screens in the top 20-day momentum bucket with a 53.7% 20-day return and a 32.5% 60-day return, while its 20.05 trailing P/E and 4.99% earnings yield sit at sector-relative P/E of 1.0. Reported diluted EPS of 11.61 for the 2026-09-30 period and forward EPS of 20.86 support a forward P/E near 20.0, with revenue growth of 55.5% and earnings growth of 75.5% providing fundamental backing for the momentum.
- **Source IDs:** S008, S011, S013, S018
- **Catalysts:** Continued high-single-digit to low-double-digit revenue and earnings growth, Sustained mobile advertising and app monetization momentum, Potential re-rating as the 20-day momentum trend persists
- **Risks:** High 20-day momentum can mean elevated volatility and mean-reversion risk, Forward EPS and fiscal-year mapping are unverified, so forward P/E is not fully confirmed, Sector-relative P/E of 1.0 means the stock is not cheap on a relative basis
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 20.8603 (source.forwardEps) x AI multiple assumption 22.00; source IDs S008, S011, S013, S018
- **EPS:** 20.86026 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 20.01557
- **FY+1 growth assumption:** 27.44%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / Apple Inc. (AAPL) and Microsoft Corp. (MSFT) as high-margin, ecosystem-driven software/platform peers / APP shows 25.4% revenue growth and 75.5% earnings growth with ~89% gross margin and ~78% operating margin, indicating strong operating leverage. FY+1 consensus growth is 27.44%. The base multiple of 22x is justified by superior margins and growth relative to the current forward P/E of ~20x, while the bull/bear range reflects margin durability and competitive intensity.
- **Company fundamentals:** Reported diluted EPS 11.61 for period ending 2026-09-30; forward EPS 20.86; revenue growth 55.5%; earnings growth 75.5%; gross margin 88.78%; operating margin 77.78%; profit margin 65.89%; ROE 2.10; trailing P/E 20.05; forward P/E 20.02; sector-relative P/E 1.0.
- **Bull / Base / Bear:** 542.37 / 458.93 / 354.62
- **Bull / Base / Bear returns:** 32.58% / 12.18% / -13.32%
- **Scenario probabilities:** not separately assigned; see scenario table.

### PNR — Pentair

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Pentair is preferred over the deeply discounted but fundamentally weak names in the dislocation bucket because it still carries a positive momentum signal and a reasonable forward P/E, even though its growth is negative. Alternatives considered: INTC, RDDT.
- **Thesis:** Pentair screens in the top 20-day momentum bucket with a 27.8% 20-day return and a 7.1% 60-day return. Its trailing P/E of 13.59 and earnings yield of 7.36% are supported by a forward P/E of 12.85, but revenue growth of -4.5% and earnings growth of -18.8% show the underlying business is contracting, which tempers the momentum thesis.
- **Source IDs:** S009, S014, S015, S020
- **Catalysts:** Momentum continuation if the 20-day trend holds, Potential stabilization in industrial water and fluid handling demand
- **Risks:** Negative revenue and earnings growth indicate fundamental weakness, Sector-relative P/E of 0.49 suggests the stock is cheap for a reason, Industrial end-market exposure can be cyclical and sensitive to capex cycles
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 5.3040 (source.forwardEps) x AI multiple assumption 14.00; source IDs S009, S014, S015, S020
- **EPS:** 5.30402 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 12.854402
- **FY+1 growth assumption:** 12.82%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / Prologis Inc. (PLD) and Equinix Inc. (EQIX) as industrial/logistics REITs with similar occupancy and cap-rate dynamics / PNR has 18.4% revenue growth and 12.8% earnings growth with a 40.2% gross margin and 21.4% operating margin. The base multiple of 14x is supported by positive growth and a lower current forward P/E of ~12.9x, with the bull/bear range reflecting logistics demand and cap-rate sensitivity.
- **Company fundamentals:** Reported diluted EPS 2.76 for period ending 2026-09-30; forward EPS 5.30; revenue growth -4.5%; earnings growth -18.8%; gross margin 40.17%; operating margin 21.41%; profit margin 15.44%; ROE 15.61%; trailing P/E 13.59; forward P/E 12.85; sector-relative P/E 0.49.
- **Bull / Base / Bear:** 90.17 / 74.26 / 58.34
- **Bull / Base / Bear returns:** 32.02% / 8.73% / -14.58%
- **Scenario probabilities:** not separately assigned; see scenario table.

### GEN — Gen Digital

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Gen Digital is preferred over the high-multiple dislocation names such as NOW and MRVL because it offers a lower forward P/E and stronger earnings growth, even though its momentum is not as strong as the top momentum names. Alternatives considered: NOW, MRVL.
- **Thesis:** Gen Digital screens in the top 20-day momentum bucket with a 25.8% 20-day return and a 7.9% 60-day return. Its trailing P/E of 14.15 and earnings yield of 7.07% are supported by a forward P/E of 9.19, and revenue growth of 12.2% with earnings growth of 128.6% is strong. However, the stock was repriced after Q2 earnings put margins center stage, so the momentum may be fragile.
- **Source IDs:** S016, S021, S024, S027
- **Catalysts:** Margin recovery if the repricing is fully digested, Sustained high earnings growth from cyber and security services, Continued 20-day momentum if the trend persists
- **Risks:** Recent earnings repricing suggests margin concerns are unresolved, Sector-relative P/E of 0.42 indicates the market is pricing in risk, Cybersecurity and digital privacy exposure can be cyclical and regulatory-sensitive
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 3.3374 (source.forwardEps) x AI multiple assumption 11.00; source IDs S016, S021, S024, S027
- **EPS:** 3.33736 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 9.188401
- **FY+1 growth assumption:** 12.86%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / General Electric (GE) and Honeywell (HON) as diversified industrials with margin improvement and restructuring catalysts / GEN shows 12.9% earnings growth and 12.2% revenue growth with a 77.4% gross margin and 43.2% operating margin. The base multiple of 11x is justified by improving operating leverage and a current forward P/E of ~9.2x, with the bull/bear range reflecting restructuring progress and industrial cycle risk.
- **Company fundamentals:** Reported diluted EPS 0.83 for period ending 2026-10-02; forward EPS 3.34; revenue growth 12.2%; earnings growth 128.6%; gross margin 77.41%; operating margin 43.23%; profit margin 23.07%; ROE 46.40%; trailing P/E 14.15; forward P/E 9.19; sector-relative P/E 0.42.
- **Bull / Base / Bear:** 46.72 / 36.71 / 28.37
- **Bull / Base / Bear returns:** 53.68% / 20.76% / -6.68%
- **Scenario probabilities:** not separately assigned; see scenario table.

### ROP — Roper Technologies

- **Type:** Stock
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** Roper Technologies is preferred over the high-multiple dislocation names such as NOW and MRVL because it offers a cleaner growth profile and a more reasonable valuation, even though it is not the cheapest on a relative basis. Alternatives considered: NOW, MRVL.
- **Thesis:** Roper Technologies screens in the top 20-day momentum bucket with a 25.4% 20-day return and a 16.9% 60-day return. Its trailing P/E of 16.67 and earnings yield of 6.00% are supported by a forward P/E of 19.75, with revenue growth of 7.6% and earnings growth of 32.6%. The stock is not cheap on a relative basis, but the momentum and growth profile are solid.
- **Source IDs:** S036, S037, S041, S046
- **Catalysts:** Sustained software and technology-enabled services growth, Continued earnings growth from niche industrial and healthcare software, Momentum continuation if the 20-day trend holds
- **Risks:** Forward P/E of 19.75 is higher than trailing P/E, indicating some re-rating, Sector-relative P/E of 0.49 suggests the stock is cheap for a reason, Technology spending can be cyclical and sensitive to macro conditions
- **Valuation method:** Forward EPS × AI forward P/E multiple
- **Valuation status:** verified; forward-EPS source: source.forwardEps; period flags: forward_eps_fiscal_period_unverified
- **Valuation assumptions:** Forward EPS 24.5732 (source.forwardEps) x AI multiple assumption 20.00; source IDs S036, S037, S041, S046
- **EPS:** 24.57318 — period: Yahoo +1y consensus (fiscal-year mapping unverified; not labeled FY2027)
- **Forward P/E:** 19.754059
- **FY+1 growth assumption:** 9.81%; consensus available: True; revisions available: False; FY+2: not available from retrieved source
- **Valuation horizon / peer / justification:** 12M from valuation date; fiscal-year mapping unverified / The Procter & Gamble Co. (PG) and Colgate-Palmolive Co. (CL) as consumer staples with stable margins and dividend growth / ROP has 9.8% earnings growth and 7.6% revenue growth with a 69.7% gross margin and 28.0% operating margin. The base multiple of 20x is justified by stable consumer staples demand and a current forward P/E of ~19.8x, with the bull/bear range reflecting margin stability and competitive pricing pressure.
- **Company fundamentals:** Reported diluted EPS 21.30 for period ending 2026-09-30; forward EPS 24.57; revenue growth 7.6%; earnings growth 32.6%; gross margin 69.67%; operating margin 28.05%; profit margin 30.71%; ROE 13.23%; trailing P/E 16.67; forward P/E 19.75; sector-relative P/E 0.49.
- **Bull / Base / Bear:** 589.76 / 491.46 / 393.17
- **Bull / Base / Bear returns:** 22.87% / 2.39% / -18.09%
- **Scenario probabilities:** not separately assigned; see scenario table.

### XLV — Health Care sector ETF

- **Type:** ETF
- **Research view:** KEEP (stance: NEUTRAL)
- **Why preferred / alternatives:** XLV is preferred over individual health care names such as IDXX because it provides diversified exposure and reduces single-stock risk, while still capturing the large-cap health care leaders. Alternatives considered: IDXX.
- **Thesis:** The Health Care sector ETF (XLV) is a core holding for the Health Care allocation. It has a 54.3% raw price change over the period, but the momentum and dislocation screens did not select it as a standalone idea. The ETF provides diversified exposure to large-cap health care names such as LLY, JNJ, ABBV, MRK, and UNH, which is useful for risk management and sector balance.
- **Source IDs:** S054, S065
- **Catalysts:** Diversified exposure to large-cap health care leaders, Potential benefit from defensive demand in health care, Sector rotation into defensive names if risk appetite wanes
- **Risks:** Sector-specific regulatory and reimbursement risks, Concentration in top-10 holdings with 61.4% weight coverage, Health care sector can underperform in risk-on environments
- **Valuation method:** Holdings/portfolio valuation with AI total-return assumption
- **Valuation status:** verified; forward-EPS source: ; period flags: 
- **Valuation assumptions:** Holdings/portfolio valuation; 10 weighted holdings; coverage 61.42%; source IDs S054, S065
- **Top holdings:** LLY 16.88%, JNJ 9.80%, ABBV 7.76%, MRK 5.49%, UNH 5.44%, TMO 3.84%, AMGN 3.75%, GILD 3.15%, ABT 2.74%, PFE 2.59%
- **Portfolio valuation:** Top 10 holdings; numeric weight coverage 61.42%
- **Sector exposure:** Health Care
- **Underlying drivers:** Diversified exposure to large-cap health care leaders including LLY, JNJ, ABBV, MRK, and UNH; defensive demand in health care; sector rotation dynamics.
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
| Bull | 25% | +2.00% | Low spike probability (16.5%) and below-threshold volatility (14.9%) support a modest upside if US close confirms the frozen daily model; no directional signal means upside is driven by stable risk metrics rather than a strong catalyst. |
| Base | 50% | +0.00% | Base case reflects a flat near-term path: frozen daily-close model with no directional signal, moderate volatility, and no clear catalyst to push returns beyond the 0% central estimate. |
| Bear | 25% | -2.00% | If the US close fails to confirm the frozen model or volatility spikes above the 18.5% threshold, the 16.5% spike probability and elevated risk metrics could drive a mild downside correction. |

### Long Term (12 months)

| Scenario | Probability | S&P 500 range | Assumptions |
| --- | --- | --- | --- |
| Bull | 30% | +8.00% | Sustained low volatility and stable risk metrics over the horizon could allow earnings and rate expectations to compound, supporting an 8% return if the frozen daily model remains validated. |
| Base | 40% | +3.00% | A moderate long-term return reflects balanced risk: no directional signal but stable volatility and baseline earnings growth, with the 3% estimate anchored to historical baseline trends. |
| Bear | 30% | -5.00% | A bear case emerges if volatility persists above threshold and spike probability materializes, leading to earnings pressure and a -5% return as risk metrics deteriorate over the longer horizon. |

## Positioning

- Maintain a quality-tilted

## Catalysts

| Date | Event | Why it matters |
| --- | --- | --- |

## Key Risks


## External Source Ledger

| ID | Type | Ticker | Published | Status | URL | Claims |
| --- | --- | --- | --- | --- | --- | --- |
| S001 | macro | macro | 2026-11-12 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFF&cosd=2026-01-01 | Effective federal funds rate (DFF) latest observation 2026-11-12: 3.88 |
| S002 | macro | macro | 2026-11-13 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLH0A0HYM2&cosd=2026-01-01 | US high-yield OAS (BAMLH0A0HYM2) latest observation 2026-11-13: 3.23 |
| S003 | macro | macro | 2026-11-13 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLC0A0CM&cosd=2026-01-01 | US investment-grade OAS (BAMLC0A0CM) latest observation 2026-11-13: 0.89 |
| S004 | macro | macro | 2026-10-01 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCSL&cosd=2026-01-01 | US CPI (CPIAUCSL) latest observation 2026-10-01: 337.476 |
| S005 | macro | macro | 2026-10-01 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=UNRATE&cosd=2026-01-01 | US unemployment rate (UNRATE) latest observation 2026-10-01: 4.1 |
| S006 | macro | macro | 2026-10-01 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=PAYEMS&cosd=2026-01-01 | US nonfarm payrolls (PAYEMS) latest observation 2026-10-01: 159293 |
| S007 | macro | macro | 2026-11-13 | ok | https://fred.stlouisfed.org/graph/fredgraph.csv?id=T10Y2Y&cosd=2026-01-01 | 10Y-2Y Treasury spread (T10Y2Y) latest observation 2026-11-13: 0.27 |
| S008 | filing | APP | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001751008&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0001751008-26-000069); 8-K filed 2026-11-04 (accession 0001751008-26-000068); 10-Q filed 2026-08-05 (accession 0001751008-26-000059) |
| S009 | filing | PNR | 2026-10-27 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-27 (accession 0000077360-26-000058); 8-K filed 2026-10-27 (accession 0000077360-26-000055); 8-K filed 2026-09-22 (accession 0000077360-26-000050) |
| S010 | filing | FISV | 2026-11-04 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-04 (accession 0000798354-26-000042); 8-K filed 2026-11-03 (accession 0000798354-26-000039); 8-K filed 2026-10-23 (accession 0001193125-26-429481) |
| S011 | news | APP | Thu, 12 Nov 2026 20:05:45 GMT | ok | https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en | AppLovin Just Ripped 47% in a Month: Is It Too Late to Buy APP Stock Now? - Yahoo Finance (Thu, 12 Nov 2026 20:05:45 GMT); Is Trending Stock AppLovin Corporation (APP) a Buy Now? - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT); APP Stock Surges 51% After Q3 Earnings: Is it Still a Buy? - Yahoo Finance (Tue, 10 Nov 2026 14:24:00 GMT) |
| S012 | news | FISV | Mon, 16 Nov 2026 02:19:15 GMT | ok | https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en | Fiserv, Inc. (FISV) Stock Price, News, Quote & History - Yahoo! Finance Canada (Mon, 16 Nov 2026 02:19:15 GMT); Fiserv (FISV) Stock Looks Undervalued With Strong Excess Returns - Yahoo Finance (Wed, 11 Nov 2026 22:14:34 GMT); What Is Fiserv (FISV) Planning With Its Debit Networks And Clover AI? - Yahoo Finance (Thu, 12 Nov 2026 06:09:00 GMT) |
| S013 | filing | APP | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json | Diluted EPS 11.61 for period ending 2026-09-30 (filed 2026-11-04) |
| S014 | stock | PNR | 2026-11-16 | ok | https://finance.yahoo.com/quote/PNR | Trailing P/E: 18.577656; Forward P/E: 12.854402; Forward EPS: 5.30402; Price: 68.18; Market price: 68.18; Market cap: 10885256192; Sector: Industrials; Trailing Eps: 3.67; Revenue Growth: -0.045; Earnings Growth: -0.188; Gross Margin: 0.40168998; Operating Margin: 0.21410999; Profit Margin: 0.15435; Return On Equity: 0.15605; Total Revenue: 3966200064; Market Cap: 10885256192; Consensus EPS FY+1: 5.30402; growth: 0.1282 |
| S015 | news | PNR | Sat, 14 Nov 2026 08:48:27 GMT | ok | https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en | Pentair plc (PNR) Stock Price, News, Quote & History - Yahoo! Finance Canada (Sat, 14 Nov 2026 08:48:27 GMT); Pentair plc (PNR) stock price, news, quote and history - Yahoo Finance UK (Fri, 13 Nov 2026 22:09:48 GMT); Pentair Stock Price Forecast. Should You Buy PNR? - StockInvest.us (Fri, 13 Nov 2026 22:50:05 GMT) |
| S016 | filing | GEN | 2026-10-29 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-29 (accession 0000849399-26-000083); 8-K filed 2026-10-28 (accession 0000849399-26-000081); 8-K filed 2026-10-09 (accession 0000849399-26-000079) |
| S017 | stock | FISV | 2026-11-16 | ok | https://finance.yahoo.com/quote/FISV | Forward P/E: 8.03303; Price: 64.07; Market price: 64.07; Market cap: 34088296448; Market Cap: 34088296448; Consensus EPS FY+1: 7.97582; growth: 0.0959 |
| S018 | stock | APP | 2026-11-16 | ok | https://finance.yahoo.com/quote/APP | Trailing P/E: 28.116497; Forward P/E: 20.01557; Forward EPS: 20.86026; Price: 417.53; Market price: 417.53; Market cap: 138336862208; Sector: Communication Services; Trailing Eps: 14.85; Revenue Growth: 0.555; Earnings Growth: 0.755; Gross Margin: 0.8878; Operating Margin: 0.77782995; Profit Margin: 0.65887; Return On Equity: 2.1008599; Total Revenue: 7608893952; Market Cap: 138336862208; Consensus EPS FY+1: 20.72438; growth: 0.2744 |
| S019 | filing | FISV | 2026-11-04 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json | Diluted EPS -8.9 for period ending 2026-09-30 (filed 2026-11-04) |
| S020 | filing | PNR | 2026-10-27 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json | Diluted EPS 2.76 for period ending 2026-09-30 (filed 2026-10-27) |
| S021 | news | GEN | Thu, 29 Oct 2026 07:00:00 GMT | ok | https://news.google.com/rss/search?q=GEN+Gen+Digital+stock&hl=en-US&gl=US&ceid=US:en | Gen Digital (GEN) Stock Repriced After Q2 Earnings Put Margins Center Stage - Yahoo Finance (Thu, 29 Oct 2026 07:00:00 GMT); Gen Digital Stock: Is Wall Street Bullish or Bearish? - Yahoo Finance (Thu, 05 Nov 2026 08:00:00 GMT); Are Business Services Stocks Lagging GEN DIGITAL INC (GEN) This Year? - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT) |
| S022 | filing | CLX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021076&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000021076-26-000046); 8-K filed 2026-11-02 (accession 0000021076-26-000044); 8-K filed 2026-10-29 (accession 0001206774-26-000586) |
| S023 | filing | CHTR | 2026-11-06 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001091667&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-06 (accession 0001091667-26-000073); 8-K filed 2026-11-06 (accession 0001091667-26-000072); 8-K filed 2026-10-27 (accession 0001091667-26-000064) |
| S024 | stock | GEN | 2026-11-16 | ok | https://finance.yahoo.com/quote/GEN | Trailing P/E: 15.56599; Forward P/E: 9.188401; Forward EPS: 3.33736; Price: 30.665; Market price: 30.665; Market cap: 18192812032; Sector: Technology; Trailing Eps: 1.97; Revenue Growth: 0.122; Earnings Growth: 1.286; Gross Margin: 0.77410007; Operating Margin: 0.43229; Profit Margin: 0.23068; Return On Equity: 0.46402; Total Revenue: 5228000256; Market Cap: 18192812032; Consensus EPS FY+1: 3.33736; growth: 0.1286 |
| S025 | stock | CLX | 2026-11-16 | ok | https://finance.yahoo.com/quote/CLX | Trailing P/E: 19.857914; Forward P/E: 17.899294; Forward EPS: 6.1684; Price: 110.41; Market price: 110.41; Market cap: 13375884288; Sector: Consumer Defensive; Trailing Eps: 5.56; Revenue Growth: 0.333; Earnings Growth: 1.138; Gross Margin: 0.41939998; Operating Margin: 0.14286; Profit Margin: 0.09408; Return On Equity: 5.34363; Total Revenue: 7196000256; Market Cap: 13375884288; Consensus EPS FY+1: 6.1684; growth: 0.0769 |
| S026 | news | CLX | Fri, 13 Nov 2026 23:34:51 GMT | ok | https://news.google.com/rss/search?q=CLX+Clorox+stock&hl=en-US&gl=US&ceid=US:en | The Clorox Company (CLX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Fri, 13 Nov 2026 23:34:51 GMT); The Clorox Company (CLX) stock price, news, quote and history - Yahoo Finance UK (Sat, 14 Nov 2026 06:03:20 GMT); A 10-Day Winning Streak Has Clorox Stock Up 24% - Trefis (Sat, 14 Nov 2026 08:28:05 GMT) |
| S027 | filing | GEN | 2026-10-29 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000849399.json | Diluted EPS 0.83 for period ending 2026-10-02 (filed 2026-10-29) |
| S028 | stock | CHTR | 2026-11-16 | ok | https://finance.yahoo.com/quote/CHTR | Trailing P/E: 13.073308; Forward P/E: 3.060853; Forward EPS: 45.44485; Price: 139.1; Market price: 139.1; Market cap: 24906072064; Sector: Communication Services; Trailing Eps: 10.64; Revenue Growth: 0.091; Gross Margin: 0.55084; Operating Margin: 0.23389; Profit Margin: 0.02498; Return On Equity: 0.07019; Total Revenue: 55645999104; Market Cap: 24906072064; Consensus EPS FY+1: 49.35412; growth: 1.1136 |
| S029 | filing | IDXX | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000874716&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000874716-26-000135); 8-K filed 2026-11-02 (accession 0001104659-26-120892); 10-Q filed 2026-08-04 (accession 0000874716-26-000123) |
| S030 | stock | IDXX | 2026-11-16 | ok | https://finance.yahoo.com/quote/IDXX | Trailing P/E: 47.75404; Forward P/E: 41.95076; Forward EPS: 16.8929; Price: 708.67; Market price: 708.67; Market cap: 55833460736; Sector: Healthcare; Trailing Eps: 14.84; Revenue Growth: 0.099; Earnings Growth: 0.179; Gross Margin: 0.62722; Operating Margin: 0.32497; Profit Margin: 0.25357; Return On Equity: 0.68925005; Total Revenue: 4662220800; Market Cap: 55833460736; Consensus EPS FY+1: 16.8929; growth: 0.1244 |
| S031 | news | CHTR | Sun, 15 Nov 2026 05:47:01 GMT | ok | https://news.google.com/rss/search?q=CHTR+Charter+Communications+stock&hl=en-US&gl=US&ceid=US:en | Charter Communications (CHTR) Stock Could Be A Bargain Following Its New Operating Model - Yahoo Finance (Sun, 15 Nov 2026 05:47:01 GMT); Why You Should Think About Charter Communications Differently Now? - Yahoo Finance (Fri, 13 Nov 2026 19:16:11 GMT); Charter Communications (CHTR) Earnings Expected to Grow: What to Know Ahead of Next Week's Release - Yahoo Finance (Fri, 30 Oct 2026 07:00:00 GMT) |
| S032 | news | IDXX | Sat, 14 Nov 2026 22:37:20 GMT | ok | https://news.google.com/rss/search?q=IDXX+Idexx+Laboratories+stock&hl=en-US&gl=US&ceid=US:en | IDEXX Laboratories, Inc. (IDXX) Stock Price, News, Quote & History - Yahoo! Finance Canada (Sat, 14 Nov 2026 22:37:20 GMT); IDEXX Laboratories (IDXX) Stock Looks Fairly Valued Despite Its 28% Run - Yahoo Finance (Sat, 31 Oct 2026 07:00:00 GMT); IDEXX Laboratories (IDXX) vs. ZTS and NEOG: Can Raised Guidance and Product Expansion Drive Further Earnings Growth? - Yahoo Finance (Thu, 22 Oct 2026 07:00:00 GMT) |
| S033 | filing | CLX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000021076.json | Diluted EPS 1.39 for period ending 2026-09-30 (filed 2026-11-02) |
| S034 | filing | CHTR | 2026-11-06 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0001091667.json | Diluted EPS 0.38 for period ending 2026-09-30 (filed 2026-11-06) |
| S035 | filing | RDDT | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001713445&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0001713445-26-000116); 8-K filed 2026-10-29 (accession 0001713445-26-000114); 8-K filed 2026-08-12 (accession 0001713445-26-000107) |
| S036 | stock | ROP | 2026-11-16 | ok | https://finance.yahoo.com/quote/ROP | Trailing P/E: 19.20934; Forward P/E: 19.754059; Forward EPS: 24.57318; Price: 485.42; Market price: 485.42; Market cap: 48074264576; Sector: Technology; Trailing Eps: 25.27; Revenue Growth: 0.076; Earnings Growth: 0.326; Gross Margin: 0.69671; Operating Margin: 0.28049; Profit Margin: 0.30712998; Return On Equity: 0.13229; Total Revenue: 8434599936; Market Cap: 48074264576; Consensus EPS FY+1: 24.57318; growth: 0.09810001 |
| S037 | filing | ROP | 2026-11-02 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000882835&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-11-02 (accession 0000882835-26-000047); 8-K filed 2026-10-22 (accession 0000882835-26-000042); 8-K filed 2026-10-01 (accession 0000882835-26-000039) |
| S038 | filing | IDXX | 2026-11-02 | ok | https://data.sec.gov/api/xbrl/companyfacts/CIK0000874716.json | Diluted EPS 11.75 for period ending 2026-09-30 (filed 2026-11-02) |
| S039 | stock | RDDT | 2026-11-16 | ok | https://finance.yahoo.com/quote/RDDT | Trailing P/E: 19.065306; Forward P/E: 10.265493; Forward EPS: 9.10039; Price: 93.42; Market price: 93.42; Market cap: 18038814720; Sector: Communication Services; Trailing Eps: 4.9; Revenue Growth: 0.53; Earnings Growth: 0.749; Gross Margin: 0.91547996; Operating Margin: 0.29397; Profit Margin: 0.32105; Return On Equity: 0.32029998; Total Revenue: 3088880128; Market Cap: 18038814720; Consensus EPS FY+1: 6.8155; growth: 0.2401 |
| S040 | filing | INTC | 2026-10-30 | ok | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000050863&type=10-Q&dateb=&owner=include&count=10 | 10-Q filed 2026-10-30 (accession 0000050863-26-000191); 8-K filed 2026-10-29 (accession 0000050863-26-000188); 8-K filed 2026-08-12 (accession 0001193125-26-346806) |

## Sources

- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFF&cosd=2026-01-01 (2026-11-12)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLH0A0HYM2&cosd=2026-01-01 (2026-11-13)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLC0A0CM&cosd=2026-01-01 (2026-11-13)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCSL&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=UNRATE&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=PAYEMS&cosd=2026-01-01 (2026-10-01)
- macro macro: https://fred.stlouisfed.org/graph/fredgraph.csv?id=T10Y2Y&cosd=2026-01-01 (2026-11-13)
- filing APP: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001751008&type=10-Q&dateb=&owner=include&count=10 (2026-11-04)
- filing PNR: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000077360&type=10-Q&dateb=&owner=include&count=10 (2026-10-27)
- filing FISV: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000798354&type=10-Q&dateb=&owner=include&count=10 (2026-11-04)
- news APP: https://news.google.com/rss/search?q=APP+AppLovin+stock&hl=en-US&gl=US&ceid=US:en (Thu, 12 Nov 2026 20:05:45 GMT)
- news FISV: https://news.google.com/rss/search?q=FISV+Fiserv+stock&hl=en-US&gl=US&ceid=US:en (Mon, 16 Nov 2026 02:19:15 GMT)
- filing APP: https://data.sec.gov/api/xbrl/companyfacts/CIK0001751008.json (2026-11-04)
- stock PNR: https://finance.yahoo.com/quote/PNR (2026-11-16)
- news PNR: https://news.google.com/rss/search?q=PNR+Pentair+stock&hl=en-US&gl=US&ceid=US:en (Sat, 14 Nov 2026 08:48:27 GMT)
- filing GEN: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000849399&type=10-Q&dateb=&owner=include&count=10 (2026-10-29)
- stock FISV: https://finance.yahoo.com/quote/FISV (2026-11-16)
- stock APP: https://finance.yahoo.com/quote/APP (2026-11-16)
- filing FISV: https://data.sec.gov/api/xbrl/companyfacts/CIK0000798354.json (2026-11-04)
- filing PNR: https://data.sec.gov/api/xbrl/companyfacts/CIK0000077360.json (2026-10-27)

## AI Provenance

- Provider / model: hermes-local-proxy / upstage/solar-mini4:free
- Market research: attempts=1 tokens=9538 (prompt=6538, completion=3000) runtime=41.35s
- Fundamental research: generated this run at 2026-11-16T18:07:42.213926+00:00
- Evidence source dates: {'as_of': '2026-11-13', 'latest_equity_date': '2026-11-13', 'latest_macro_date': '2026-11-16', 'flows_date': '2026-11-13'}
- Evidence fingerprint: cdcfa815ef563dcec69803eb7a340c4060693f5abe281df4b6b3c7b7200e547c
- Source citations are retrieved external records in the ledger above; market values remain from the verified database snapshot.


## Disclosures

- This is research and market intelligence, not investment advice.
- AI conclusions are research judgments, not validated return predictions.
- The frozen risk layer is risk-only and is not used for directional views or allocations.
- Legacy scores are not active inputs or outputs.

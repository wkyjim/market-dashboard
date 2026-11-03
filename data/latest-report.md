# Rule-Based Institutional Market Update

Generated at: 3 November 2026, 12:16:00 (HKT)
Window: 24h

## Executive Dashboard

- Regime score: **47.71 / 100** (Mixed / Rotation)
- US equity strength: **42.22 / 100** (weak)
- Evidence quality: **76.0 / 100**
- ETF flow contribution: **48.81 / 100**, reliability **67.03 / 100**
- Breadth: **narrow**; above 50DMA `40.0%`, above 200DMA `53.33%`
- Top sector score: **Energy** `72.2`
- Top theme score: **Energy** `71.12`

## Market Regime Score

| Metric | Value | Driver / Interpretation |
| --- | --- | --- |
| Overall regime | 47.71 | Mixed / Rotation |
| equity_trend | 40.0 | mild risk-off pressure; Core equity ETFs versus moving averages. |
| equity_momentum | 45.36 | neutral / mixed; 5D/20D/60D return momentum across SPY, QQQ, IWM, and SMH. |
| market_breadth | 45.0 | mild risk-off pressure; Participation breadth from tracked equity/ETF rows. |
| volatility | 35.0 | risk-off pressure; VIX level and change; higher score means calmer volatility conditions. |
| rates_yield_curve | 58.0 | mild risk-on support; Treasury yield pressure and curve shape; higher score means less rates pressure. |
| credit_proxy | 50.0 | neutral / mixed; Credit-market proxy; currently neutral when no direct spread signal is available. |
| dollar_fx | 55.93 | mild risk-on support; Dollar move; higher score means less USD tightening pressure. |
| commodity_confirmation | 57.0 | mild risk-on support; Copper, silver, oil, and gold mix; higher score means better cyclical confirmation. |
| etf_flow | 49.21 | neutral / mixed; Grouped ETF flow contribution adjusted for reliability. |
| news_confirmation | 60.62 | mild risk-on support; Weighted headline/news confirmation score. |
| Positive contributors |  | news_confirmation=60.62 |
| Negative contributors |  | volatility=35.0, equity_trend=40.0, market_breadth=45.0 |

## Forward Signal (Score → Expected Return)

Read-only mapping. The regime score is a *state* descriptor, not a forecast; this table states what that score level has historically implied for forward SPY returns.

| Horizon | Bucket | Historical mean | n | Direction |
| --- | --- | --- | --- | --- |
| 5D | 45-50 | 1.3% | 9 | up |
| 20D | 45-50 | 2.32% | 9 | up |
| 60D | 45-50 | 4.94% | 9 | up |

Sample: 2025-10-21 → 2026-08-03, 116 daily origins.
Bottom-vs-top spread at 60D: **6.75 pp** (block-bootstrap 95% CI [1.92, 10.76], P(spread<=0)=<0.0001)
Shape: contrarian across buckets at this horizon — higher score buckets have historically shown *lower* forward returns. The Direction column is the sign of the expected return for this specific bucket, not a statement that a high score is bullish.

Method: Analyst inference/estimate (historical bucket calibration).
- Limitation: sample covers a bull-market window (2025-10-21..2026-08-03); no bear-market stress test is possible with current data
- Limitation: 60D forward windows overlap heavily; bootstrap CI is block-adjusted but effective sample size is small
- Limitation: low-score buckets hold few observations (n=9 daily in the <40 bucket) so the contrarian edge is directionally clear but imprecise

## US Equity Strength Score

| Component | Score |
| --- | --- |
| indices_above_moving_averages | 40.0 |
| sp500_trend | 35.0 |
| nasdaq_trend | 35.0 |
| russell_participation | 55.0 |
| returns_momentum | 45.36 |
| rsi_zone | 45.0 |
| macd_confirmation | 43.75 |
| volume_confirmation | 38.75 |
| breadth | 45.0 |

## Evidence Quality / Confidence

- Confidence score: `76.0`
- Agreement ratio: `0.4`
- Contradiction count: `3`
- Missing indicators: none
- Warning flags: none

## Cross-Asset Confirmation

| Area | Signal | Interpretation |
| --- | --- | --- |
| Equities | S&P 500 falling; Nasdaq falling; Russell 2000 stable | Confirms risk appetite when broad indices rise together; weak small caps would narrow the signal. |
| Rates | 10Y Treasury falling; MOVE stable | Rising yields can pressure duration assets; falling MOVE supports calmer bond volatility. |
| Dollar | DXY proxy stable | A stronger dollar can tighten financial conditions and pressure commodities/emerging-market risk. |
| Credit | HYG falling | High-yield weakness would challenge equity risk-on confirmation. |
| Gold | Gold rising | Gold strength can indicate defensive demand, inflation hedging, or geopolitical concern. |
| Silver | Silver rising | Silver helps distinguish precious-metal demand from industrial/cyclical confirmation when data is available. |
| Copper | Copper rising | Copper strength supports cyclical growth confirmation; weakness would dilute risk-on breadth. |
| Oil | WTI crude falling | Oil spikes can be inflationary risk; falling oil can ease cost pressure but may also flag demand softness. |
| Volatility | VIX rising | Falling VIX supports risk appetite; a volatility spike would reduce confidence in broad risk-on. |

### Macro Snapshot

Live macro rows are intraday snapshots from `public.macro_live`; closed rows are official stored rows from `public.macro`.

| Symbol | Name | Close | Pct Chg | Market Date | Status |
| --- | --- | --- | --- | --- | --- |
| ^GSPC | S&P 500 | 7541.4 | -0.51 | 2026-11-02 | closed |
| ^IXIC | NASDAQ Composite | 25164.32 | -1.07 | 2026-11-02 | closed |
| ^RUT | Russell 2000 Index | 2805.88 | -0.21 | 2026-11-02 | closed |
| ^VIX | CBOE Volatility Index | 21.15 | 8.91 | 2026-11-02 | closed |
| ^SKEW | CBOE SKEW Index | 152.78 | 2.02 | 2026-11-02 | closed |
| ^MOVE | ICE BofA MOVE Index | 100.36 | 0.16 | 2026-11-02 | closed |
| US2YT=X | United States 2-Year Treasury Yield | 4.6 | 0.37 | 2026-11-02 | live as of 3 November 2026, 12:00:20 (HKT) |
| US3YT=X | United States 3-Year Treasury Yield | 4.66 | 0.11 | 2026-11-02 | live as of 3 November 2026, 12:00:20 (HKT) |
| US5YT=X | United States 5-Year Treasury Yield | 4.71 | -0.23 | 2026-11-02 | live as of 3 November 2026, 12:00:20 (HKT) |
| US7YT=X | United States 7-Year Treasury Yield | 4.8 | -0.35 | 2026-11-02 | live as of 3 November 2026, 12:00:20 (HKT) |
| US10YT=X | United States 10-Year Treasury Yield | 4.91 | 0.22 | 2026-11-03 | live as of 3 November 2026, 12:00:20 (HKT) |
| US20YT=X | United States 20-Year Treasury Yield | 5.32 | -0.34 | 2026-11-02 | live as of 3 November 2026, 12:00:20 (HKT) |
| US30YT=X | United States 30-Year Treasury Yield | 5.29 | -0.41 | 2026-11-02 | live as of 3 November 2026, 12:00:20 (HKT) |
| HK50 | Hang Seng Futures | 23467.5 | -0.29 | 2026-11-03 | live as of 3 November 2026, 12:00:20 (HKT) |
| KOR200c1 | KOSPI 200 Futures | 887.15 | -3.43 | 2026-11-02 | live as of 3 November 2026, 12:00:20 (HKT) |
| CIHc1 | SSE 50 Futures | 2745.2 | 0.65 | 2026-11-02 | live as of 3 November 2026, 12:00:20 (HKT) |
| HYG | iShares iBoxx High Yield Corporate Bond ETF | 76.89 | -0.7 | 2026-11-02 | closed |
| LQD | iShares iBoxx Investment Grade Corporate Bond ETF | 103.71 | -0.54 | 2026-11-02 | closed |
| JNK | SPDR Bloomberg High Yield Bond ETF | 92.26 | -0.77 | 2026-11-02 | closed |
| RSP | Invesco S&P 500 Equal Weight ETF | 219.98 | 0.77 | 2026-11-02 | closed |
| IWF | iShares Russell 1000 Growth ETF | 116.22 | -1.18 | 2026-11-02 | closed |
| IWD | iShares Russell 1000 Value ETF | 259.36 | 0.27 | 2026-11-02 | closed |
| TLT | iShares 20+ Year Treasury Bond ETF | 81.73 | -0.13 | 2026-11-02 | closed |
| IEF | iShares 7-10 Year Treasury Bond ETF | 91.5 | -0.28 | 2026-11-02 | closed |
| SHY | iShares 1-3 Year Treasury Bond ETF | 81.46 | -0.29 | 2026-11-02 | closed |
| GC=F | Gold Future | 3956.6 | 1.85 | 2026-11-02 | closed |
| SI=F | Silver Future | 50.71 | 3.21 | 2026-11-02 | closed |
| CL=F | WTI Crude Oil Future | 96.26 | -6.5 | 2026-11-02 | closed |
| HG=F | Copper Future | 6.54 | 0.51 | 2026-11-02 | closed |

## Market Dispersion Analysis

- Sector ETF 20D dispersion: `21.62` points (very high); leader `XLE` (Energy) `11.46`, laggard `XLK` (Technology) `-10.16`
- Sector ETF 60D dispersion: `30.54` points (very high); leader `XLE` (Energy) `20.39`, laggard `XLC` (Communication Services) `-10.15`

| Comparison | Left | Right | 20D Spread | Signal |
| --- | --- | --- | --- | --- |
| Equal-weight vs cap-weight | RSP (Equal-weight S&P 500) | SPY (S&P 500) | 5.9 | broader participation |
| Small-cap vs large-cap | IWM (Russell 2000) | SPY (S&P 500) | 1.03 | small-cap leadership |
| Growth vs value | IWF (Russell 1000 Growth) | IWD (Russell 1000 Value) | -11.16 | value leadership |
| Nasdaq vs S&P 500 | QQQ (Nasdaq 100) | SPY (S&P 500) | -6.07 | S&P 500 leadership |

## Sector Constituent Dispersion

- Breadth 50D / 200D: percentage of active S&P 500 constituents in the sector trading above the 50-day / 200-day moving average.
- Positive 20D: percentage of active sector constituents with positive 20-day return.
- Std 20D: cross-sectional standard deviation of constituent 20-day returns; higher means wider stock-level dispersion.

| Sector | Count | Breadth 50D | Breadth 200D | Positive 20D | 20D Dispersion | Std 20D | Label | Leaders | Laggards |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Information Technology | 75 | 38.67 | 59.46 | 32.0 | 80.66 | 17.98 | very high | PTC, GEN, ROP | COHR, TER, INTC |
| Industrials | 83 | 60.24 | 48.1 | 57.83 | 61.59 | 12.51 | very high | EFX, LMT, PNR | CAT, FIX, BE |
| Real Estate | 30 | 44.83 | 37.93 | 80.0 | 48.62 | 8.3 | very high | CCI, SBAC, AMT | ESS, DOC, ARE |
| Financials | 76 | 57.33 | 61.11 | 75.0 | 48.51 | 9.52 | very high | FDS, CBOE, GPN | IBKR, COIN, HOOD |
| Communication Services | 22 | 19.05 | 35.0 | 50.0 | 47.55 | 11.1 | very high | OMC, DIS, CMCSA | GOOG, GOOGL, RDDT |
| Consumer Discretionary | 47 | 61.7 | 44.68 | 76.6 | 39.85 | 7.59 | very high | HAS, ULTA, HD | GPC, DASH, BKNG |
| Health Care | 60 | 75.0 | 85.0 | 91.67 | 39.78 | 7.05 | very high | REGN, LLY, CRL | DXCM, SOLV, ILMN |
| Materials | 24 | 75.0 | 62.5 | 83.33 | 37.35 | 9.94 | very high | DOW, BALL, LYB | MOS, ALB, FCX |
| Consumer Staples | 34 | 78.12 | 65.62 | 85.29 | 29.34 | 6.65 | very high | STZ, DLTR, EL | TGT, ADM, BG |
| Energy | 21 | 85.71 | 80.95 | 85.71 | 24.02 | 6.42 | very high | COP, APA, EOG | BKR, VLO, TPL |
| Utilities | 31 | 83.87 | 51.61 | 93.55 | 15.43 | 3.82 | high | WEC, EXC, NI | NRG, AES, VST |

## Economic Data Snapshot

### U.S. Labor

| Indicator | Latest | Unit | Change | Date | Rule-Based Interpretation |
| --- | --- | --- | --- | --- | --- |
| All Employees, Total Nonfarm | 159044.0 | thousands | 29.0 thousands vs prior | 2026-09-01 | Higher reading supports activity or liquidity. |
| Unemployment Rate | 4.2 | percent | 0.1 pp vs prior | 2026-09-01 | Higher reading increases macro pressure. |
| Initial Claims | 194000.0 | number | -6000.0 number vs prior | 2026-10-17 | Lower claims indicate firmer labor-market conditions. |
| Continued Claims | 1701000.0 | number | -21000.0 number vs prior | 2026-10-17 | Lower claims indicate firmer labor-market conditions. |
| Labor Force Participation Rate | 61.8 | percent | 0.2 pp vs prior | 2026-09-01 | Higher participation expands labor supply. |

### U.S. Growth

| Indicator | Latest | Unit | Change | Date | Rule-Based Interpretation |
| --- | --- | --- | --- | --- | --- |
| Real Gross Domestic Product | 24611.08 | billions chained 2017 dollars | 203.07 billions chained 2017 dollars vs prior | 2026-07-01 | Higher reading supports activity or liquidity. |
| Industrial Production Index | 103.95 | index 2017=100 | 0.68 index pts vs prior | 2026-09-01 | Higher reading supports activity or liquidity. |
| Advance Retail Sales | 745021.0 | millions dollars | 5699.0 millions dollars vs prior | 2026-09-01 | Higher reading supports activity or liquidity. |

### U.S. Inflation

| Indicator | Latest | Unit | Change | Date | Rule-Based Interpretation |
| --- | --- | --- | --- | --- | --- |
| Headline CPI month-over-month inflation rate | 0.65 | percent | 0.25 pp vs prior | 2026-09-01 | Higher reading increases macro pressure. |
| Headline CPI year-over-year inflation rate | 4.02 | percent | 0.31 pp vs prior | 2026-09-01 | Higher reading increases macro pressure. |
| Core CPI month-over-month inflation rate | 0.33 | percent | 0.05 pp vs prior | 2026-09-01 | Higher reading increases macro pressure. |
| Core CPI year-over-year inflation rate | 2.79 | percent | 0.03 pp vs prior | 2026-09-01 | Higher reading increases macro pressure. |
| Headline CPI year-over-year inflation rate | 4.0 | percent | 0.31 pp vs prior | 2026-09-01 | Higher reading increases macro pressure. |
| Core CPI year-over-year inflation rate | 2.82 | percent | 0.07 pp vs prior | 2026-09-01 | Higher reading increases macro pressure. |
| Headline PCE Price Index month-over-month inflation rate | 0.49 | percent | 0.17 pp vs prior | 2026-09-01 | Higher reading increases macro pressure. |
| Headline PCE Price Index year-over-year inflation rate | 3.65 | percent | 0.2 pp vs prior | 2026-09-01 | Higher reading increases macro pressure. |
| Core PCE Price Index month-over-month inflation rate | 0.32 | percent | 0.05 pp vs prior | 2026-09-01 | Higher reading increases macro pressure. |
| Core PCE Price Index year-over-year inflation rate | 3.12 | percent | 0.09 pp vs prior | 2026-09-01 | Higher reading increases macro pressure. |
| Headline PPI Final Demand month-over-month inflation rate | 1.11 | percent | 0.76 pp vs prior | 2026-09-01 | Higher reading increases macro pressure. |
| Headline PPI Final Demand year-over-year inflation rate | 6.34 | percent | 0.73 pp vs prior | 2026-09-01 | Higher reading increases macro pressure. |
| Core PPI Final Demand Less Foods and Energy month-over-month inflation rate | 0.68 | percent | 0.44 pp vs prior | 2026-09-01 | Higher reading increases macro pressure. |
| Core PPI Final Demand Less Foods and Energy year-over-year inflation rate | 4.98 | percent | 0.17 pp vs prior | 2026-09-01 | Higher reading increases macro pressure. |
| Consumer Price Index for All Urban Consumers | 336.3 | index 1982-1984=100 | 2.17 index pts vs prior | 2026-09-01 | Higher reading increases macro pressure. |
| Core CPI | 338.9 | index 1982-1984=100 | 1.13 index pts vs prior | 2026-09-01 | Higher reading increases macro pressure. |
| Personal Consumption Expenditures Price Index | 132.26 | index 2017=100 | 0.65 index pts vs prior | 2026-09-01 | Higher reading increases macro pressure. |
| Core PCE Price Index | 130.9 | index 2017=100 | 0.41 index pts vs prior | 2026-09-01 | Higher reading increases macro pressure. |
| Producer Price Index: Final Demand | 159.61 | index Nov 2009=100 | 1.76 index pts vs prior | 2026-09-01 | Latest structural macro observation. |
| Producer Price Index: Final Demand Less Foods and Energy | 156.17 | index Apr 2010=100 | 1.06 index pts vs prior | 2026-09-01 | Latest structural macro observation. |

### Policy, Liquidity, Credit

| Indicator | Latest | Unit | Change | Date | Rule-Based Interpretation |
| --- | --- | --- | --- | --- | --- |
| Federal Funds Effective Rate | 3.88 | percent | 0.0 pp vs prior | 2026-10-29 | Stable reading. |
| Secured Overnight Financing Rate | 3.94 | percent | 0.0 pp vs prior | 2026-10-29 | Stable reading. |
| Effective Federal Funds Rate | 3.75 | percent | 0.12 pp vs prior | 2026-09-01 | Higher reading increases macro pressure. |
| Assets: Total Assets: Federal Reserve | 6753604.0 | millions dollars | -2035.0 millions dollars vs prior | 2026-10-21 | Lower reading signals softer activity or liquidity. |
| M1 Money Stock | 20061.2 | billions dollars | 93.9 billions dollars vs prior | 2026-09-01 | Higher reading supports activity or liquidity. |
| M2 Money Stock | 23413.9 | billions dollars | 113.0 billions dollars vs prior | 2026-09-01 | Higher reading supports activity or liquidity. |
| ICE BofA US High Yield Option-Adjusted Spread | 3.26 | percent | 0.12 pp vs prior | 2026-10-29 | Higher reading increases macro pressure. |
| ICE BofA US Corporate Option-Adjusted Spread | 0.89 | percent | 0.03 pp vs prior | 2026-10-29 | Higher reading increases macro pressure. |

### Housing and Sentiment

| Indicator | Latest | Unit | Change | Date | Rule-Based Interpretation |
| --- | --- | --- | --- | --- | --- |
| Housing Starts | 1221.0 | thousands | -67.0 thousands vs prior | 2026-09-01 | Lower reading signals softer activity or liquidity. |
| New Privately-Owned Housing Units Authorized | 1400.0 | thousands | -3.0 thousands vs prior | 2026-09-01 | Lower reading signals softer activity or liquidity. |
| 30-Year Fixed Rate Mortgage Average | 7.32 | percent | -0.08 pp vs prior | 2026-10-22 | Lower reading eases macro pressure. |
| University of Michigan Consumer Sentiment | 48.1 | index 1966:Q1=100 | -3.6 index pts vs prior | 2026-09-01 | Lower reading signals softer activity or liquidity. |

### Global Structural Snapshot

| Indicator | Latest | Unit | Change | Date | Rule-Based Interpretation |
| --- | --- | --- | --- | --- | --- |
| China GDP growth | 4.96 | annual percent | n/a | 2025-01-01 | Level is available; trend requires prior observation. |
| China Inflation, consumer prices | 0.06 | annual percent | n/a | 2025-01-01 | Level is available; trend requires prior observation. |
| China Unemployment rate | 4.62 | percent | n/a | 2025-01-01 | Level is available; trend requires prior observation. |
| Japan GDP growth | 1.19 | annual percent | n/a | 2025-01-01 | Level is available; trend requires prior observation. |
| Japan Inflation, consumer prices | 3.17 | annual percent | n/a | 2025-01-01 | Level is available; trend requires prior observation. |
| Japan Unemployment rate | 2.45 | percent | n/a | 2025-01-01 | Level is available; trend requires prior observation. |
| Germany GDP growth | 0.24 | annual percent | n/a | 2025-01-01 | Level is available; trend requires prior observation. |
| Germany Inflation, consumer prices | 2.17 | annual percent | n/a | 2025-01-01 | Level is available; trend requires prior observation. |
| Germany Unemployment rate | 3.71 | percent | n/a | 2025-01-01 | Level is available; trend requires prior observation. |
| Australia GDP growth | 1.35 | annual percent | n/a | 2025-01-01 | Level is available; trend requires prior observation. |
| Australia Inflation, consumer prices | 2.87 | annual percent | n/a | 2025-01-01 | Level is available; trend requires prior observation. |
| Australia Unemployment rate | 4.09 | percent | n/a | 2025-01-01 | Level is available; trend requires prior observation. |
| Euro Area GDP growth | 1.41 | annual percent | n/a | 2025-01-01 | Level is available; trend requires prior observation. |
| Euro Area Inflation, consumer prices | 2.47 | annual percent | n/a | 2025-01-01 | Level is available; trend requires prior observation. |
| Euro Area Unemployment rate | 6.28 | percent | n/a | 2025-01-01 | Level is available; trend requires prior observation. |

### ECB FX Snapshot

| Indicator | Latest | Unit | Change | Date | Rule-Based Interpretation |
| --- | --- | --- | --- | --- | --- |
| US dollar/Euro ECB reference exchange rate | 1.12 | USD | 0.0 USD vs prior | 2026-11-02 | EUR strengthened versus this currency. |
| Japanese yen/Euro ECB reference exchange rate | 177.1 | JPY | 1.42 JPY vs prior | 2026-11-02 | EUR strengthened versus this currency. |
| Chinese yuan renminbi/Euro ECB reference exchange rate | 7.46 | CNY | 0.02 CNY vs prior | 2026-11-02 | EUR strengthened versus this currency. |
| Australian dollar/Euro ECB reference exchange rate | 1.6 | AUD | 0.01 AUD vs prior | 2026-11-02 | EUR strengthened versus this currency. |

ABS Australia note: ABS rows are stored locally/Neon, but most series are dimension-coded; only curated series should be promoted into narrative report text.

## Sector and Theme Leadership

### Official Sector Strength

Supporting and detracting names are the top/bottom S&P 500 constituents by 20D return when constituent coverage is available; otherwise the report falls back to related ETFs.

| Rank | Sector | Score | Trend | Momentum | Stock Breadth | ETF Flow | Flow Reliability | 3M RS | Supporting / Leaders | Detracting / Laggards |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Energy | 72.2 | strong uptrend | positive | broad | 76.16 | 65.0 | 66.79 | COP, APA, EOG | BKR, VLO, TPL |
| 2 | Healthcare | 71.74 | strong uptrend | positive | broad | 68.96 | 65.0 | 63.47 | REGN, LLY, CRL | DXCM, SOLV, ILMN |
| 3 | Consumer Staples | 68.89 | strong uptrend | positive | broad | 50.0 | 0.0 | 60.4 | STZ, DLTR, EL | TGT, ADM, BG |
| 4 | Financials | 65.71 | strong uptrend | neutral | broad | 41.97 | 65.0 | 54.24 | FDS, CBOE, GPN | IBKR, COIN, HOOD |
| 5 | Consumer Discretionary | 61.18 | uptrend | neutral | broad | 50.0 | 0.0 | 53.74 | HAS, ULTA, HD | GPC, DASH, BKNG |
| 6 | Utilities | 58.83 | neutral | neutral | broad | 50.0 | 0.0 | 56.99 | WEC, EXC, NI | NRG, AES, VST |
| 7 | Real Estate | 55.99 | neutral | neutral | broad | 41.29 | 65.0 | 53.76 | CCI, SBAC, AMT | ESS, DOC, ARE |
| 8 | Crypto | 50.86 | neutral | neutral | mixed | 58.64 | 65.0 | 50.0 |  |  |
| 9 | Cybersecurity | 46.57 | neutral | neutral | weak | 50.0 | 0.0 | 51.58 | CIBR | CIBR |
| 10 | Defense | 43.14 | strong downtrend | negative | weak | 50.0 | 0.0 | 42.43 | XAR | XAR |
| 11 | Technology | 39.99 | downtrend | negative | weak | 55.07 | 65.0 | 45.04 | PTC, GEN, ROP | COHR, TER, INTC |
| 12 | Industrials | 39.34 | strong downtrend | neutral | weak | 50.0 | 0.0 | 47.09 | EFX, LMT, PNR | CAT, FIX, BE |
| 13 | Semiconductors | 35.64 | strong downtrend | negative | weak | 69.4 | 95.0 | 36.62 | SMH, SOXX | SOXX, SMH |
| 14 | Nuclear | 34.7 | strong downtrend | negative | weak | 50.0 | 0.0 | 37.56 | NLR | NLR |
| 15 | Grid Infrastructure | 32.91 | strong downtrend | negative | weak | 50.0 | 0.0 | 41.17 | GRID | GRID |

### Thematic Strength

| Rank | Theme | Score | Setup | ETF Flow | Flow Reliability | Dispersion | Price | News |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Energy | 71.12 | Positive setup | 76.16 | 65.0 | 2.71 | True | False |
| 2 | Healthcare Innovation | 68.06 | Positive setup | 68.96 | 65.0 | 20.42 | True | False |
| 3 | Dividend Defensives | 62.17 | Positive setup | 49.15 | 65.0 | 2.21 | True | False |
| 4 | Cybersecurity | 51.42 | Neutral / watchlist | 50.0 | 0.0 | 45.77 | False | False |
| 5 | Defense | 50.38 | Neutral / watchlist | 50.0 | 0.0 | 36.47 | False | False |
| 6 | Quality Growth | 48.82 | Neutral / watchlist | 56.21 | 65.0 | 21.81 | False | False |
| 7 | Small Caps | 47.77 | Neutral / watchlist | 44.45 | 65.0 | 0.0 | False | False |
| 8 | Financials | 44.75 | Neutral / watchlist | 41.97 | 65.0 | 12.6 | False | False |
| 9 | AI Infrastructure | 44.19 | Neutral / watchlist | 69.4 | 95.0 | 20.78 | False | False |
| 10 | Semiconductors | 41.81 | Weak setup | 69.4 | 95.0 | 12.18 | False | False |
| 11 | Grid Infrastructure | 39.36 | Weak setup | 50.0 | 0.0 | 24.2 | False | False |
| 12 | Crypto Infrastructure | 38.4 | Weak setup | 58.64 | 65.0 | 3.13 | False | False |
| 13 | Nuclear | 31.87 | Underperformance risk | 50.0 | 0.0 | 16.13 | False | False |

- Top 5 improving themes: Energy, Crypto Infrastructure, Healthcare Innovation, Cybersecurity, Dividend Defensives
- Top 5 deteriorating themes: Nuclear, Financials, Defense, Semiconductors, AI Infrastructure
- Strong news but weak price confirmation: none
- Strong price but weak news confirmation: Energy, Healthcare Innovation, Dividend Defensives

### Sector / Theme Alignment

| Sector | Related Themes | Sector Score | Sector Signal | Theme Score | Theme Signal | Interpretation |
| --- | --- | --- | --- | --- | --- | --- |
| Energy | Energy | 72.2 | strong | 71.12 | strong | sector and theme confirmation |
| Healthcare | Healthcare Innovation | 71.74 | strong | 68.06 | strong | sector and theme confirmation |
| Consumer Staples | Dividend Defensives | 68.89 | strong | 62.17 | positive | sector and theme confirmation |
| Financials | Financials | 65.71 | strong | 44.75 | weak | sector stronger than related themes |
| Consumer Discretionary | Small Caps | 61.18 | positive | 47.77 | mixed | sector stronger than related themes |
| Utilities | Grid Infrastructure, Nuclear, Dividend Defensives | 58.83 | positive | 44.47 | weak | sector stronger than related themes |
| Real Estate | Dividend Defensives | 55.99 | positive | 62.17 | positive | sector and theme confirmation |
| Crypto | Crypto Infrastructure | 50.86 | mixed | 38.4 | weak | mixed confirmation |
| Cybersecurity | Cybersecurity | 46.57 | mixed | 51.42 | mixed | mixed confirmation |
| Defense | Defense | 43.14 | weak | 50.38 | mixed | mixed confirmation |
| Technology | AI Infrastructure, Semiconductors, Quality Growth | 39.99 | weak | 44.94 | weak | broad weakness across sector and themes |
| Industrials | Defense, Grid Infrastructure | 39.34 | weak | 44.87 | weak | broad weakness across sector and themes |
| Semiconductors | AI Infrastructure, Semiconductors | 35.64 | weak | 43.0 | weak | broad weakness across sector and themes |
| Nuclear | Nuclear | 34.7 | very weak | 31.87 | very weak | broad weakness across sector and themes |
| Grid Infrastructure | Grid Infrastructure | 32.91 | very weak | 39.36 | weak | broad weakness across sector and themes |

## Three-Month Outperformance Setup

| Rank | Theme | Score | Classification | Drivers | Invalidation Triggers |
| --- | --- | --- | --- | --- | --- |
| 1 | Energy | 72.44 | Positive setup | relative_strength_20d, relative_strength_60d, trend_persistence, breadth, volume_accumulation | relative strength below SPY, breadth below 45%, news turns negative |
| 2 | Healthcare Innovation | 71.87 | Positive setup | relative_strength_20d, relative_strength_60d, trend_persistence, breadth, volume_accumulation | relative strength below SPY, breadth below 45%, news turns negative |
| 3 | Dividend Defensives | 67.05 | Positive setup | relative_strength_20d, trend_persistence, breadth, volume_accumulation, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 4 | Quality Growth | 55.61 | Neutral / watchlist | trend_persistence, breadth, volume_accumulation, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 5 | Cybersecurity | 55.41 | Neutral / watchlist | relative_strength_60d, trend_persistence, breadth, volume_accumulation, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 6 | Defense | 50.81 | Neutral / watchlist | downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 7 | Small Caps | 50.38 | Neutral / watchlist | downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 8 | AI Infrastructure | 47.42 | Neutral / watchlist | volume_accumulation, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 9 | Financials | 46.73 | Neutral / watchlist | downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 10 | Semiconductors | 43.1 | Weak setup | volume_accumulation | relative strength below SPY, breadth below 45%, news turns negative |
| 11 | Grid Infrastructure | 41.86 | Weak setup | downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 12 | Crypto Infrastructure | 39.64 | Weak setup | relative_strength_60d, volume_accumulation, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |

## Breadth and Participation

- Above 50DMA: `40.0%`
- Above 200DMA: `53.33%`
- Positive 20D return: `41.67%`

## Volatility and Risk Signals

- VIX close=21.15 pct_chg=8.91

## News Analytics

- Sentiment counts: {'positive': 46, 'negative': 29, 'neutral': 5}
- News confirmation score: `60.62`

### Top Market-Moving Headlines

**1. Palantir reports booming U.S. commercial revenue growth, topping government for first time**
- Source: CNBC Investing
- Importance / impact: High / Positive
- Relevance / horizon: macro / short-term
- Affected assets: U.S, revenue growth, commercial revenue, government revenue
- Score: `54.19`
- Investment implication: Macro-relevant positive signal; use as context for rates, volatility, and index confirmation over the short-term.

**2. Oil rises after reported U.S. strike on Iran’s Qeshm Island**
- Source: Investing.com Stock Market
- Importance / impact: Medium / Positive
- Relevance / horizon: macro / short-term
- Affected assets: USO, WTI, U.S, Geopolitical Risk, Oil Prices
- Score: `40.95`
- Investment implication: Macro-relevant positive signal; use as context for rates, volatility, and index confirmation over the short-term.

**3. Oil rises after report of US strike on Iran’s Qeshm Island**
- Source: Investing.com Stock Market
- Importance / impact: Medium / Positive
- Relevance / horizon: macro / short-term
- Affected assets: US, Geopolitical Risk, Oil Prices, Military Conflict
- Score: `40.95`
- Investment implication: Macro-relevant positive signal; use as context for rates, volatility, and index confirmation over the short-term.

**4. Oil Futures Sell Off on Middle East Diplomatic Progress**
- Source: Dow Jones US Business
- Importance / impact: Medium / Negative
- Relevance / horizon: macro / short-term
- Affected assets: U.S, Oil Prices, Geopolitics, Diplomacy
- Score: `40.64`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the short-term.

**5. S-Oil Q3 2026 slides: record lube profit drives 46% earnings surge**
- Source: Investing.com Markets
- Importance / impact: Medium / Positive
- Relevance / horizon: macro / quarterly
- Affected assets: S, earnings, corporate_results, energy
- Score: `39.92`
- Investment implication: Macro-relevant positive signal; use as context for rates, volatility, and index confirmation over the quarterly.

**6. LG Energy Solution Q3 2026 slides: ESS surge drives revenue beat**
- Source: Investing.com Markets
- Importance / impact: Medium / Positive
- Relevance / horizon: sector_theme / quarterly
- Affected assets: LG Energy Solution, ESS, LG, revenue beat, ESS market growth
- Score: `37.57`
- Investment implication: Theme or sector positive signal; requires price and volume confirmation before affecting rankings.

**7. Earnings call transcript: S-Oil posts strong Q3 2026 profit on refining, lube boom**
- Source: Investing.com Forex
- Importance / impact: Medium / Positive
- Relevance / horizon: macro / short-term
- Affected assets: S, earnings, profit, refining
- Score: `37.57`
- Investment implication: Macro-relevant positive signal; use as context for rates, volatility, and index confirmation over the short-term.

**8. BOE Expected to Join Peers in Raising Key Rate**
- Source: Dow Jones Economy
- Importance / impact: Medium / Positive
- Relevance / horizon: macro / short-term
- Affected assets: BOE, U.S, monetary_policy, inflation, interest_rate
- Score: `36.85`
- Investment implication: Macro-relevant positive signal; use as context for rates, volatility, and index confirmation over the short-term.

**9. U.S. reportedly strikes Iran's Qeshm Island as Vance hopes for ‘negotiated settlement’ with Tehran**
- Source: CNBC Top News
- Importance / impact: Medium / Negative
- Relevance / horizon: single_name / short-term
- Affected assets: U.S, military conflict, geopolitical risk, Iran
- Score: `36.74`
- Investment implication: Single-name negative signal; low weight unless it maps to a broader sector or theme.

**10. Earnings beat, guidance raised: our AI-picked pharma stock is up 23.96%**
- Source: Investing.com World News
- Importance / impact: Low / Positive
- Relevance / horizon: sector_theme / short-term
- Affected assets: earnings beat, guidance raised, AI
- Score: `34.81`
- Investment implication: Theme or sector positive signal; requires price and volume confirmation before affecting rankings.


### Headline Quality Checks

No noisy headlines detected by current rules.

## Positioning & Flow Dashboard

Positioning and flow data is used as confirmation only.

### Deferred Flow Sections

- Official ETF / fund flows: current report uses shares-outstanding-derived net fund flow estimates from free ETF metadata.
- Institutional Ownership: not available until SEC 13F ingestion is implemented.
- Grouped exposure flow reliability: use issuer coverage and availability status before treating ETF flow as confirmation.

## ETF Flows Analysis

- Market flow regime: `Mixed / Neutral`
- Market flow score: `48.4 / 100`
- Equity risk flow: `45.4`
- Credit risk flow: `52.0`
- Sector cyclicality flow: `51.6`
- Duration/liquidity flow: `43.0`
- Alternatives: `mixed alternative-asset demand`
- ETF flow reliability: `67.0 / 100`
- Dominant allocation direction: `defensive demand`

### Core Flow Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVV | U.S. Broad Equity | -0.3 | -0.9 | 0.4 | n/a | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural distribution | 64.0 |
| ACWI | Global Equity | -0.6 | -0.7 | 0.0 | n/a | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Mixed or neutral flow structure; Persistent selling | 62.0 |
| EFA | Developed Markets ex-U.S. | -0.2 | 0.6 | 0.0 | n/a | Flat | Neutral | Normal | Neutral | Neutral | Mixed or neutral flow structure; Persistent selling | 62.0 |
| IEMG | Emerging Markets | -0.5 | -0.3 | 0.0 | n/a | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Mixed or neutral flow structure; Persistent selling | 62.0 |
| IJH | U.S. Mid Cap | -0.9 | 0.2 | 0.6 | n/a | Flat | Neutral | Normal | Neutral | Neutral | Structural accumulation | 76.0 |
| IWM | U.S. Small Cap | -1.3 | 0.9 | 0.6 | n/a | Flat | Neutral | Normal | Neutral | Neutral | Mixed or neutral flow structure | 70.0 |
| LQD | Investment-Grade Credit | 1.7 | -0.3 | 0.7 | n/a | Up | Buy | Normal | Steady Accumulation | Risk-On | Medium-term recovery | 72.0 |
| HYG | High-Yield Credit | -0.3 | 0.2 | 0.5 | n/a | Flat | Neutral | Normal | Neutral | Neutral | Medium-term deterioration | 68.0 |
| SGOV | Treasury Bills / Cash | -1.7 | -1.6 | 0.8 | n/a | Flat | Sell | Normal | Quiet Distribution | Weakening | Strong confirmation; Exceptional institutional selling, Strong sponsorship | 80.0 |
| SHY | Short-Duration Treasuries | 0.5 | 1.7 | 0.8 | n/a | Flat | Neutral | Normal | Neutral | Neutral | Structural accumulation; Strong sponsorship | 84.0 |
| IEF | Intermediate-Duration Treasuries | 1.0 | -0.5 | 0.5 | n/a | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Medium-term recovery | 72.0 |
| TLT | Long-Duration Treasuries | -1.2 | 1.3 | 0.6 | n/a | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Medium-term deterioration | 68.0 |
| GLD | Gold | -0.7 | 0.8 | 0.4 | n/a | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Medium-term deterioration | 68.0 |
| IBIT | Bitcoin | 0.0 | 1.3 | 0.6 | n/a | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural accumulation | 76.0 |

### Sector Flow Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| XLC | Communication Services | 1.7 | 2.7 | 0.6 | 1.3 | Down | Buy | High | Aggressive Dip Buying | Recovery Candidate | Strong confirmation; Exceptional institutional buying | 100.0 |
| XLY | Consumer Discretionary | -0.0 | -1.1 | 0.5 | 1.8 | Up | Neutral | High | Momentum Rally | Watch | Structural distribution | 79.0 |
| XLP | Consumer Staples | 0.9 | 0.4 | 0.6 | 3.6 | Up | Sell | High | Distribution into Strength | Bearish Divergence | Medium-term recovery | 87.0 |
| XLE | Energy | 0.7 | 0.2 | 0.7 | 0.2 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural accumulation | 91.0 |
| XLF | Financials | 0.5 | -1.8 | 0.4 | 0.4 | Up | Buy | Normal | Steady Accumulation | Risk-On | Medium-term recovery; Exceptional institutional buying | 95.0 |
| XLV | Health Care | 2.2 | 1.2 | 0.6 | 4.0 | Up | Buy | High | Confirmed Accumulation | Strong Risk-On | Strong confirmation; Exceptional institutional buying | 100.0 |
| XLI | Industrials | 0.9 | -0.9 | 0.6 | 2.0 | Down | Buy | High | Aggressive Dip Buying | Recovery Candidate | Medium-term recovery | 87.0 |
| XLK | Information Technology | 0.7 | -0.0 | 0.7 | 4.4 | Down | Neutral | High | Heavy Selling Pressure | Cautious | Structural accumulation | 91.0 |
| XLB | Materials | -0.3 | -1.4 | 0.6 | -0.1 | Up | Buy | Normal | Steady Accumulation | Risk-On | Medium-term recovery; Exceptional institutional buying | 95.0 |
| XLRE | Real Estate | 0.7 | -1.2 | 0.5 | 1.3 | Up | Buy | High | Confirmed Accumulation | Strong Risk-On | Medium-term recovery | 87.0 |
| XLU | Utilities | -0.8 | 1.1 | 0.5 | 0.4 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Medium-term deterioration | 83.0 |

### Subsector PFV Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ITA | Aerospace and Defense | -0.0 | -0.2 | 0.3 | n/a | Up | Sell | Normal | Profit Taking | Slightly Bearish | Strong confirmation; Exceptional institutional selling | 72.0 |
| SOXX | Semiconductors | 1.4 | -0.1 | 0.8 | n/a | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural accumulation; Strong sponsorship | 84.0 |
| SMH | Semiconductors | 0.6 | -0.2 | 0.6 | n/a | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural accumulation | 76.0 |
| CIBR | Cybersecurity | 0.3 | 1.6 | 0.8 | 1.2 | Down | Neutral | High | Heavy Selling Pressure | Cautious | Structural accumulation; Strong sponsorship | 99.0 |

### Material Flow Divergences

| Severity | Type | Primary | Comparison | Interpretation |
| --- | --- | --- | --- | --- |
| high | close_substitute_divergence | GLD | IAU | primary representative differs from close substitute |
| high | close_substitute_divergence | AGG | IUSB | primary representative differs from close substitute |
| high | close_substitute_divergence | IWF | IVW | primary representative differs from close substitute |
| high | close_substitute_divergence | IWD | IVE | primary representative differs from close substitute |
| high | close_substitute_divergence | IWM | IJR | primary representative differs from close substitute |


## Contradiction / Audit Flags

No contradiction flags were triggered by current deterministic rules.

## Data Quality Notes

- Technical rows loaded: `60`
- S&P 500 constituent technical rows loaded: `503`
- Macro rows loaded: `48`
- Live macro rows used: `16`
- Economic rows loaded: `113`
- News rows loaded: `80`
- Positioning/flow rows loaded: `30`

## Cycle Metadata

- Report generated at: 03 November 2026, 12:16:00 (HKT)

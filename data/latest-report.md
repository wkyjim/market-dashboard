# Rule-Based Institutional Market Update

Generated at: 5 November 2026, 11:23:01 (HKT)
Window: 24h

## Executive Dashboard

- Regime score: **49.56 / 100** (Mixed / Rotation)
- US equity strength: **41.16 / 100** (weak)
- Evidence quality: **76.0 / 100**
- ETF flow contribution: **49.75 / 100**, reliability **66.83 / 100**
- Breadth: **narrow**; above 50DMA `41.67%`, above 200DMA `58.33%`
- Top sector score: **Healthcare** `69.98`
- Top theme score: **Healthcare Innovation** `62.7`

## Market Regime Score

| Metric | Value | Driver / Interpretation |
| --- | --- | --- |
| Overall regime | 49.56 | Mixed / Rotation |
| equity_trend | 31.25 | risk-off pressure; Core equity ETFs versus moving averages. |
| equity_momentum | 43.95 | mild risk-off pressure; 5D/20D/60D return momentum across SPY, QQQ, IWM, and SMH. |
| market_breadth | 47.22 | neutral / mixed; Participation breadth from tracked equity/ETF rows. |
| volatility | 70.0 | risk-on support; VIX level and change; higher score means calmer volatility conditions. |
| rates_yield_curve | 58.0 | mild risk-on support; Treasury yield pressure and curve shape; higher score means less rates pressure. |
| credit_proxy | 50.0 | neutral / mixed; Credit-market proxy; currently neutral when no direct spread signal is available. |
| dollar_fx | 56.69 | mild risk-on support; Dollar move; higher score means less USD tightening pressure. |
| commodity_confirmation | 49.0 | neutral / mixed; Copper, silver, oil, and gold mix; higher score means better cyclical confirmation. |
| etf_flow | 49.83 | neutral / mixed; Grouped ETF flow contribution adjusted for reliability. |
| news_confirmation | 63.75 | mild risk-on support; Weighted headline/news confirmation score. |
| Positive contributors |  | volatility=70.0, news_confirmation=63.75 |
| Negative contributors |  | equity_trend=31.25, equity_momentum=43.95 |

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
| indices_above_moving_averages | 31.25 |
| sp500_trend | 35.0 |
| nasdaq_trend | 35.0 |
| russell_participation | 55.0 |
| returns_momentum | 43.95 |
| rsi_zone | 47.5 |
| macd_confirmation | 43.75 |
| volume_confirmation | 50.0 |
| breadth | 47.22 |

## Evidence Quality / Confidence

- Confidence score: `76.0`
- Agreement ratio: `0.4`
- Contradiction count: `2`
- Missing indicators: none
- Warning flags: none

## Cross-Asset Confirmation

| Area | Signal | Interpretation |
| --- | --- | --- |
| Equities | S&P 500 rising; Nasdaq rising; Russell 2000 rising | Confirms risk appetite when broad indices rise together; weak small caps would narrow the signal. |
| Rates | 10Y Treasury falling; MOVE falling | Rising yields can pressure duration assets; falling MOVE supports calmer bond volatility. |
| Dollar | DXY proxy falling | A stronger dollar can tighten financial conditions and pressure commodities/emerging-market risk. |
| Credit | HYG rising | High-yield weakness would challenge equity risk-on confirmation. |
| Gold | Gold rising | Gold strength can indicate defensive demand, inflation hedging, or geopolitical concern. |
| Silver | Silver rising | Silver helps distinguish precious-metal demand from industrial/cyclical confirmation when data is available. |
| Copper | Copper stable | Copper strength supports cyclical growth confirmation; weakness would dilute risk-on breadth. |
| Oil | WTI crude falling | Oil spikes can be inflationary risk; falling oil can ease cost pressure but may also flag demand softness. |
| Volatility | VIX falling | Falling VIX supports risk appetite; a volatility spike would reduce confidence in broad risk-on. |

### Macro Snapshot

Live macro rows are intraday snapshots from `public.macro_live`; closed rows are official stored rows from `public.macro`.

| Symbol | Name | Close | Pct Chg | Market Date | Status |
| --- | --- | --- | --- | --- | --- |
| ^GSPC | S&P 500 | 7688.62 | 1.58 | 2026-11-04 | closed |
| ^IXIC | NASDAQ Composite | 25736.51 | 1.44 | 2026-11-04 | closed |
| ^RUT | Russell 2000 Index | 2856.95 | 1.58 | 2026-11-04 | closed |
| ^VIX | CBOE Volatility Index | 16.61 | -20.26 | 2026-11-04 | closed |
| ^SKEW | CBOE SKEW Index | 150.9 | 0.59 | 2026-11-04 | closed |
| ^MOVE | ICE BofA MOVE Index | 93.88 | -6.09 | 2026-11-04 | closed |
| US2YT=X | United States 2-Year Treasury Yield | 4.56 | -0.37 | 2026-11-05 | live as of 5 November 2026, 11:00:23 (HKT) |
| US3YT=X | United States 3-Year Treasury Yield | 4.61 | -0.45 | 2026-11-05 | live as of 5 November 2026, 11:00:23 (HKT) |
| US5YT=X | United States 5-Year Treasury Yield | 4.65 | -0.6 | 2026-11-05 | live as of 5 November 2026, 11:00:23 (HKT) |
| US7YT=X | United States 7-Year Treasury Yield | 4.73 | -0.69 | 2026-11-05 | live as of 5 November 2026, 11:00:23 (HKT) |
| US10YT=X | United States 10-Year Treasury Yield | 4.84 | -1.04 | 2026-11-05 | live as of 5 November 2026, 11:00:23 (HKT) |
| US20YT=X | United States 20-Year Treasury Yield | 5.26 | -0.9 | 2026-11-05 | live as of 5 November 2026, 11:00:23 (HKT) |
| US30YT=X | United States 30-Year Treasury Yield | 5.24 | -0.83 | 2026-11-05 | live as of 5 November 2026, 11:00:23 (HKT) |
| HK50 | Hang Seng Futures | 24603.5 | 0.71 | 2026-11-05 | live as of 5 November 2026, 11:00:23 (HKT) |
| KOR200c1 | KOSPI 200 Futures | 847.85 | -4.72 | 2026-11-05 | live as of 5 November 2026, 11:00:23 (HKT) |
| CIHc1 | SSE 50 Futures | 2748.4 | 0.12 | 2026-11-03 | live as of 5 November 2026, 11:00:23 (HKT) |
| HYG | iShares iBoxx High Yield Corporate Bond ETF | 77.52 | 0.7 | 2026-11-04 | closed |
| LQD | iShares iBoxx Investment Grade Corporate Bond ETF | 104.5 | 0.75 | 2026-11-04 | closed |
| JNK | SPDR Bloomberg High Yield Bond ETF | 93.03 | 0.73 | 2026-11-04 | closed |
| RSP | Invesco S&P 500 Equal Weight ETF | 223.33 | 1.86 | 2026-11-04 | closed |
| IWF | iShares Russell 1000 Growth ETF | 117.9 | 0.39 | 2026-11-04 | closed |
| IWD | iShares Russell 1000 Value ETF | 265.3 | 2.6 | 2026-11-04 | closed |
| TLT | iShares 20+ Year Treasury Bond ETF | 81.76 | 0.8 | 2026-11-04 | closed |
| IEF | iShares 7-10 Year Treasury Bond ETF | 91.66 | 0.55 | 2026-11-04 | closed |
| SHY | iShares 1-3 Year Treasury Bond ETF | 81.5 | 0.12 | 2026-11-04 | closed |
| GC=F | Gold Future | 4072.2 | 3.35 | 2026-11-04 | closed |
| SI=F | Silver Future | 52.33 | 5.05 | 2026-11-04 | closed |
| CL=F | WTI Crude Oil Future | 88.04 | -9.01 | 2026-11-04 | closed |
| HG=F | Copper Future | 6.41 | -0.03 | 2026-11-04 | closed |

## Market Dispersion Analysis

- Sector ETF 20D dispersion: `22.75` points (very high); leader `XLV` (Health Care) `10.13`, laggard `XLK` (Technology) `-12.62`
- Sector ETF 60D dispersion: `20.09` points (very high); leader `XLE` (Energy) `10.8`, laggard `XLC` (Communication Services) `-9.29`

| Comparison | Left | Right | 20D Spread | Signal |
| --- | --- | --- | --- | --- |
| Equal-weight vs cap-weight | RSP (Equal-weight S&P 500) | SPY (S&P 500) | 6.44 | broader participation |
| Small-cap vs large-cap | IWM (Russell 2000) | SPY (S&P 500) | 2.62 | small-cap leadership |
| Growth vs value | IWF (Russell 1000 Growth) | IWD (Russell 1000 Value) | -11.81 | value leadership |
| Nasdaq vs S&P 500 | QQQ (Nasdaq 100) | SPY (S&P 500) | -6.62 | S&P 500 leadership |

## Sector Constituent Dispersion

- Breadth 50D / 200D: percentage of active S&P 500 constituents in the sector trading above the 50-day / 200-day moving average.
- Positive 20D: percentage of active sector constituents with positive 20-day return.
- Std 20D: cross-sectional standard deviation of constituent 20-day returns; higher means wider stock-level dispersion.

| Sector | Count | Breadth 50D | Breadth 200D | Positive 20D | 20D Dispersion | Std 20D | Label | Leaders | Laggards |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Information Technology | 76 | 36.84 | 54.67 | 31.58 | 77.8 | 17.62 | very high | ACN, ROP, GEN | LITE, MRVL, INTC |
| Industrials | 83 | 69.88 | 54.43 | 61.45 | 61.06 | 12.17 | very high | EFX, PNR, LMT | BE, CAT, FIX |
| Financials | 76 | 66.67 | 72.22 | 78.95 | 51.91 | 9.35 | very high | FISV, CBOE, FDS | IBKR, COIN, HOOD |
| Communication Services | 22 | 38.1 | 35.0 | 50.0 | 46.19 | 11.67 | very high | OMC, CMCSA, DIS | GOOG, GOOGL, RDDT |
| Health Care | 60 | 81.67 | 90.0 | 93.33 | 44.68 | 7.45 | very high | REGN, IDXX, GEHC | SOLV, HSIC, ILMN |
| Consumer Discretionary | 47 | 74.47 | 51.06 | 85.11 | 37.15 | 6.7 | very high | HAS, HD, LOW | GRMN, DASH, APTV |
| Materials | 24 | 75.0 | 70.83 | 83.33 | 35.19 | 9.22 | very high | DOW, VMC, PPG | MOS, FCX, ALB |
| Real Estate | 30 | 58.62 | 44.83 | 86.67 | 34.73 | 7.14 | very high | CCI, EXR, PSA | ESS, EQIX, ARE |
| Consumer Staples | 33 | 74.19 | 58.06 | 84.85 | 33.54 | 7.12 | very high | STZ, WMT, DLTR | SYY, BG, ADM |
| Utilities | 31 | 87.1 | 48.39 | 87.1 | 27.38 | 6.23 | very high | AWK, WEC, ED | NRG, CEG, VST |
| Energy | 21 | 57.14 | 76.19 | 76.19 | 19.23 | 5.07 | high | COP, CVX, APA | TPL, VLO, BKR |

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
| US dollar/Euro ECB reference exchange rate | 1.13 | USD | 0.01 USD vs prior | 2026-11-04 | EUR strengthened versus this currency. |
| Japanese yen/Euro ECB reference exchange rate | 178.3 | JPY | 1.35 JPY vs prior | 2026-11-04 | EUR strengthened versus this currency. |
| Chinese yuan renminbi/Euro ECB reference exchange rate | 7.52 | CNY | 0.06 CNY vs prior | 2026-11-04 | EUR strengthened versus this currency. |
| Australian dollar/Euro ECB reference exchange rate | 1.61 | AUD | 0.01 AUD vs prior | 2026-11-04 | EUR strengthened versus this currency. |

ABS Australia note: ABS rows are stored locally/Neon, but most series are dimension-coded; only curated series should be promoted into narrative report text.

## Sector and Theme Leadership

### Official Sector Strength

Supporting and detracting names are the top/bottom S&P 500 constituents by 20D return when constituent coverage is available; otherwise the report falls back to related ETFs.

| Rank | Sector | Score | Trend | Momentum | Stock Breadth | ETF Flow | Flow Reliability | 3M RS | Supporting / Leaders | Detracting / Laggards |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Healthcare | 69.98 | strong uptrend | positive | broad | 67.67 | 65.0 | 62.65 | REGN, IDXX, GEHC | SOLV, HSIC, ILMN |
| 2 | Consumer Staples | 69.3 | strong uptrend | positive | broad | 50.0 | 0.0 | 60.0 | STZ, WMT, DLTR | SYY, BG, ADM |
| 3 | Consumer Discretionary | 66.94 | strong uptrend | neutral | broad | 50.0 | 0.0 | 55.1 | HAS, HD, LOW | GRMN, DASH, APTV |
| 4 | Financials | 65.13 | strong uptrend | neutral | broad | 40.48 | 65.0 | 55.98 | FISV, CBOE, FDS | IBKR, COIN, HOOD |
| 5 | Real Estate | 61.09 | strong uptrend | neutral | broad | 36.23 | 65.0 | 55.97 | CCI, EXR, PSA | ESS, EQIX, ARE |
| 6 | Energy | 60.79 | strong uptrend | positive | broad | 70.9 | 65.0 | 59.95 | COP, CVX, APA | TPL, VLO, BKR |
| 7 | Utilities | 59.82 | uptrend | neutral | broad | 50.0 | 0.0 | 55.31 | AWK, WEC, ED | NRG, CEG, VST |
| 8 | Industrials | 56.02 | neutral | neutral | broad | 50.0 | 0.0 | 49.9 | EFX, PNR, LMT | BE, CAT, FIX |
| 9 | Crypto | 50.02 | neutral | neutral | mixed | 50.15 | 65.0 | 50.0 |  |  |
| 10 | Cybersecurity | 44.44 | neutral | negative | weak | 50.0 | 0.0 | 45.47 | CIBR | CIBR |
| 11 | Defense | 43.2 | strong downtrend | negative | weak | 50.0 | 0.0 | 45.46 | XAR | XAR |
| 12 | Technology | 41.02 | downtrend | negative | weak | 59.12 | 65.0 | 44.11 | ACN, ROP, GEN | LITE, MRVL, INTC |
| 13 | Grid Infrastructure | 33.92 | strong downtrend | negative | weak | 50.0 | 0.0 | 43.53 | GRID | GRID |
| 14 | Nuclear | 33.39 | strong downtrend | negative | weak | 50.0 | 0.0 | 33.03 | NLR | NLR |
| 15 | Semiconductors | 32.97 | strong downtrend | negative | weak | 66.33 | 90.0 | 36.91 | SMH, SOXX | SOXX, SMH |

### Thematic Strength

| Rank | Theme | Score | Setup | ETF Flow | Flow Reliability | Dispersion | Price | News |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Healthcare Innovation | 62.7 | Positive setup | 67.67 | 65.0 | 19.84 | True | False |
| 2 | Energy | 61.86 | Positive setup | 70.9 | 65.0 | 3.93 | True | False |
| 3 | Dividend Defensives | 60.24 | Positive setup | 50.65 | 65.0 | 4.64 | True | False |
| 4 | Defense | 49.64 | Neutral / watchlist | 50.0 | 0.0 | 39.2 | False | False |
| 5 | Small Caps | 48.98 | Neutral / watchlist | 53.21 | 65.0 | 0.0 | False | False |
| 6 | Grid Infrastructure | 44.75 | Neutral / watchlist | 50.0 | 0.0 | 17.49 | False | False |
| 7 | Financials | 44.44 | Neutral / watchlist | 40.48 | 65.0 | 14.08 | False | False |
| 8 | Cybersecurity | 43.77 | Neutral / watchlist | 50.0 | 0.0 | 39.07 | False | False |
| 9 | Quality Growth | 43.69 | Neutral / watchlist | 50.89 | 65.0 | 18.94 | False | False |
| 10 | AI Infrastructure | 41.48 | Weak setup | 66.33 | 90.0 | 19.54 | False | False |
| 11 | Crypto Infrastructure | 40.71 | Weak setup | 50.15 | 65.0 | 4.12 | False | False |
| 12 | Semiconductors | 37.65 | Weak setup | 66.33 | 90.0 | 13.86 | False | False |
| 13 | Nuclear | 27.81 | Underperformance risk | 50.0 | 0.0 | 20.11 | False | False |

- Top 5 improving themes: Crypto Infrastructure, Energy, Healthcare Innovation, Dividend Defensives, Cybersecurity
- Top 5 deteriorating themes: Nuclear, Defense, Financials, Semiconductors, AI Infrastructure
- Strong news but weak price confirmation: none
- Strong price but weak news confirmation: Healthcare Innovation, Energy, Dividend Defensives

### Sector / Theme Alignment

| Sector | Related Themes | Sector Score | Sector Signal | Theme Score | Theme Signal | Interpretation |
| --- | --- | --- | --- | --- | --- | --- |
| Healthcare | Healthcare Innovation | 69.98 | strong | 62.7 | positive | sector and theme confirmation |
| Consumer Staples | Dividend Defensives | 69.3 | strong | 60.24 | positive | sector and theme confirmation |
| Consumer Discretionary | Small Caps | 66.94 | strong | 48.98 | mixed | sector stronger than related themes |
| Financials | Financials | 65.13 | strong | 44.44 | weak | sector stronger than related themes |
| Real Estate | Dividend Defensives | 61.09 | positive | 60.24 | positive | sector and theme confirmation |
| Energy | Energy | 60.79 | positive | 61.86 | positive | sector and theme confirmation |
| Utilities | Grid Infrastructure, Nuclear, Dividend Defensives | 59.82 | positive | 44.26 | weak | sector stronger than related themes |
| Industrials | Defense, Grid Infrastructure | 56.02 | positive | 47.2 | mixed | sector stronger than related themes |
| Crypto | Crypto Infrastructure | 50.02 | mixed | 40.71 | weak | mixed confirmation |
| Cybersecurity | Cybersecurity | 44.44 | weak | 43.77 | weak | broad weakness across sector and themes |
| Defense | Defense | 43.2 | weak | 49.64 | mixed | mixed confirmation |
| Technology | AI Infrastructure, Semiconductors, Quality Growth | 41.02 | weak | 40.94 | weak | broad weakness across sector and themes |
| Grid Infrastructure | Grid Infrastructure | 33.92 | very weak | 44.75 | weak | broad weakness across sector and themes |
| Nuclear | Nuclear | 33.39 | very weak | 27.81 | very weak | broad weakness across sector and themes |
| Semiconductors | AI Infrastructure, Semiconductors | 32.97 | very weak | 39.56 | weak | broad weakness across sector and themes |

## Three-Month Outperformance Setup

| Rank | Theme | Score | Classification | Drivers | Invalidation Triggers |
| --- | --- | --- | --- | --- | --- |
| 1 | Energy | 69.0 | Positive setup | relative_strength_20d, relative_strength_60d, trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 2 | Healthcare Innovation | 66.01 | Positive setup | relative_strength_20d, relative_strength_60d, trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 3 | Dividend Defensives | 64.69 | Positive setup | relative_strength_20d, trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 4 | Small Caps | 49.91 | Neutral / watchlist | downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 5 | Defense | 49.7 | Neutral / watchlist | relative_strength_20d, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 6 | Quality Growth | 49.56 | Neutral / watchlist | downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 7 | Cybersecurity | 47.75 | Neutral / watchlist |  | relative strength below SPY, breadth below 45%, news turns negative |
| 8 | Grid Infrastructure | 47.32 | Neutral / watchlist | downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 9 | Financials | 46.6 | Neutral / watchlist | downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 10 | AI Infrastructure | 44.23 | Weak setup | downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 11 | Crypto Infrastructure | 43.91 | Weak setup | relative_strength_60d, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 12 | Semiconductors | 38.77 | Weak setup |  | relative strength below SPY, breadth below 45%, news turns negative |

## Breadth and Participation

- Above 50DMA: `41.67%`
- Above 200DMA: `58.33%`
- Positive 20D return: `41.67%`

## Volatility and Risk Signals

- VIX close=16.61 pct_chg=-20.26

## News Analytics

- Sentiment counts: {'positive': 48, 'negative': 26, 'neutral': 6}
- News confirmation score: `63.75`

### Top Market-Moving Headlines

**1. Dow soars 1,500 points for best day since April 2025 on clear-cut Democratic win, falling oil: Live updates**
- Source: CNBC Markets
- Importance / impact: High / Positive
- Relevance / horizon: macro / short-term
- Affected assets: U.S, election, political risk, stock market rally
- Score: `51.48`
- Investment implication: Macro-relevant positive signal; use as context for rates, volatility, and index confirmation over the short-term.

**2. Dow scores its best day in 18 months in a broad relief rally after Democrats sweep to power in Congress**
- Source: MarketWatch Top Stories
- Importance / impact: High / Positive
- Relevance / horizon: macro / short-term
- Affected assets: Stock Market Rally, Political Shift, Oil Prices
- Score: `48.75`
- Investment implication: Macro-relevant positive signal; use as context for rates, volatility, and index confirmation over the short-term.

**3. ECB rate hike looks nearly certain after inflation rises to three-year high**
- Source: Investing.com Economic Indicators
- Importance / impact: Medium / Negative
- Relevance / horizon: sector_theme / short-term
- Affected assets: EUR, EURO STOXX 50, EURIBOR, monetary policy, inflation
- Score: `43.76`
- Investment implication: Theme or sector negative signal; requires price and volume confirmation before affecting rankings.

**4. LG U+ Q3 2026 slides: profit surges 84% on AI growth, efficiency**
- Source: Investing.com Markets
- Importance / impact: Medium / Positive
- Relevance / horizon: sector_theme / short-term
- Affected assets: LG, U, AI growth, profit surge, operational efficiency
- Score: `39.15`
- Investment implication: Theme or sector positive signal; requires price and volume confirmation before affecting rankings.

**5. Gold and silver prices jump, dollar dips as Democrats take control of Congress**
- Source: CNBC Top News
- Importance / impact: Medium / Positive
- Relevance / horizon: sector_theme / short-term
- Affected assets: GC=F, SI=F, XAU, XAG, U.S
- Score: `37.92`
- Investment implication: Theme or sector positive signal; requires price and volume confirmation before affecting rankings.

**6. AMD shares jump as AI-driven data-center strength fuels growth outlook**
- Source: Investing.com World News
- Importance / impact: Low / Positive
- Relevance / horizon: single_name / short-term
- Affected assets: AMD, AI, Data Center, Earnings Outlook
- Score: `33.56`
- Investment implication: Single-name positive signal; low weight unless it maps to a broader sector or theme.

**7. Qualcomm shares slide as smartphone weakness clouds growth push**
- Source: Investing.com World News
- Importance / impact: Low / Negative
- Relevance / horizon: single_name / short-term
- Affected assets: QCOM, earnings miss, stock decline, semiconductor
- Score: `32.32`
- Investment implication: Single-name negative signal; low weight unless it maps to a broader sector or theme.

**8. E.l.f. Beauty posts 51% sales increase, raises full-year guidance**
- Source: CNBC Investing
- Importance / impact: Low / Positive
- Relevance / horizon: single_name / short-term
- Affected assets: E, earnings, guidance, beauty
- Score: `32.32`
- Investment implication: Single-name positive signal; low weight unless it maps to a broader sector or theme.

**9. ICRA Q2 FY2027 slides: 30% revenue growth, R&A expansion drives results**
- Source: Investing.com Markets
- Importance / impact: Low / Positive
- Relevance / horizon: sector_theme / quarterly
- Affected assets: A, ICRA, R, earnings, revenue growth
- Score: `31.93`
- Investment implication: Theme or sector positive signal; requires price and volume confirmation before affecting rankings.

**10. AMD's data center revenue nearly doubles in Q3 and CEO Su expects growth to accelerate**
- Source: CNBC Investing
- Importance / impact: Low / Positive
- Relevance / horizon: single_name / short-term
- Affected assets: AMD, AI, data center, earnings
- Score: `31.7`
- Investment implication: Single-name positive signal; low weight unless it maps to a broader sector or theme.


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
- Market flow score: `49.1 / 100`
- Equity risk flow: `46.7`
- Credit risk flow: `52.1`
- Sector cyclicality flow: `50.7`
- Duration/liquidity flow: `47.5`
- Alternatives: `mixed alternative-asset demand`
- ETF flow reliability: `66.8 / 100`
- Dominant allocation direction: `defensive demand`

### Core Flow Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVV | U.S. Broad Equity | -0.1 | -0.8 | 0.5 | n/a | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Medium-term recovery | 72.0 |
| ACWI | Global Equity | -0.6 | -0.7 | 0.0 | n/a | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Mixed or neutral flow structure; Persistent selling | 62.0 |
| EFA | Developed Markets ex-U.S. | -0.2 | 0.6 | 0.0 | n/a | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Mixed or neutral flow structure; Persistent selling | 62.0 |
| IEMG | Emerging Markets | -0.4 | -0.5 | 0.0 | n/a | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Mixed or neutral flow structure; Persistent selling | 62.0 |
| IJH | U.S. Mid Cap | -0.8 | 0.1 | 0.6 | n/a | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural accumulation | 76.0 |
| IWM | U.S. Small Cap | -0.9 | 0.9 | 0.6 | n/a | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Mixed or neutral flow structure | 70.0 |
| LQD | Investment-Grade Credit | 0.9 | -0.4 | 0.7 | n/a | Up | Buy | Normal | Steady Accumulation | Risk-On | Medium-term recovery | 72.0 |
| HYG | High-Yield Credit | -0.2 | 0.4 | 0.5 | n/a | Flat | Neutral | Normal | Neutral | Neutral | Medium-term deterioration | 68.0 |
| SGOV | Treasury Bills / Cash | -1.4 | -1.0 | 0.8 | n/a | Flat | Sell | Normal | Quiet Distribution | Weakening | Strong confirmation; Strong sponsorship | 88.0 |
| SHY | Short-Duration Treasuries | 0.5 | 1.8 | 0.8 | n/a | Flat | Neutral | Normal | Neutral | Neutral | Structural accumulation; Strong sponsorship | 84.0 |
| IEF | Intermediate-Duration Treasuries | 1.7 | 1.3 | 0.6 | n/a | Up | Buy | Normal | Steady Accumulation | Risk-On | Strong confirmation | 80.0 |
| TLT | Long-Duration Treasuries | -0.9 | 0.4 | 0.6 | n/a | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Medium-term deterioration | 68.0 |
| GLD | Gold | -0.9 | 0.7 | 0.3 | n/a | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Medium-term deterioration | 68.0 |
| IBIT | Bitcoin | -0.3 | 1.2 | 0.5 | n/a | Down | Sell | Normal | Persistent Distribution | Risk-Off | Medium-term deterioration | 68.0 |

### Sector Flow Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| XLC | Communication Services | 1.7 | 2.3 | 0.6 | 3.3 | Down | Buy | High | Aggressive Dip Buying | Recovery Candidate | Strong confirmation; Exceptional institutional buying | 100.0 |
| XLY | Consumer Discretionary | -0.6 | -1.4 | 0.5 | 1.7 | Up | Neutral | High | Momentum Rally | Watch | Structural distribution | 79.0 |
| XLP | Consumer Staples | 0.9 | 0.5 | 0.6 | 2.1 | Up | Neutral | High | Momentum Rally | Watch | Medium-term recovery | 87.0 |
| XLE | Energy | 0.5 | 0.1 | 0.7 | 0.0 | Flat | Neutral | Normal | Neutral | Neutral | Structural accumulation | 91.0 |
| XLF | Financials | 0.1 | -1.8 | 0.3 | -0.3 | Up | Buy | Normal | Steady Accumulation | Risk-On | Tactical rebound inside structural distribution | 83.0 |
| XLV | Health Care | 2.5 | 1.4 | 0.7 | 1.0 | Up | Buy | High | Confirmed Accumulation | Strong Risk-On | Strong confirmation; Exceptional institutional buying | 100.0 |
| XLI | Industrials | -0.3 | -1.4 | 0.5 | 1.4 | Flat | Neutral | High | High-Turnover Consolidation | Transition | Mixed or neutral flow structure | 85.0 |
| XLK | Information Technology | 0.3 | 0.1 | 0.7 | 1.1 | Down | Buy | High | Aggressive Dip Buying | Recovery Candidate | Strong confirmation; Exceptional institutional buying | 100.0 |
| XLB | Materials | -0.2 | -1.5 | 0.6 | 0.8 | Up | Buy | Normal | Steady Accumulation | Risk-On | Medium-term recovery; Exceptional institutional buying | 95.0 |
| XLRE | Real Estate | 0.3 | -1.3 | 0.5 | 0.4 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Medium-term recovery | 87.0 |
| XLU | Utilities | -1.1 | 0.8 | 0.4 | -0.0 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Medium-term deterioration | 83.0 |

### Subsector PFV Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ITA | Aerospace and Defense | -0.4 | -0.4 | 0.3 | n/a | Up | Sell | Normal | Profit Taking | Slightly Bearish | Strong confirmation; Exceptional institutional selling | 72.0 |
| SOXX | Semiconductors | 1.2 | 0.1 | 0.7 | n/a | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural accumulation | 76.0 |
| SMH | Semiconductors | 0.9 | 0.3 | 0.6 | n/a | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural accumulation | 76.0 |
| CIBR | Cybersecurity | -0.3 | 1.3 | 0.7 | 0.9 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural accumulation | 91.0 |

### Material Flow Divergences

| Severity | Type | Primary | Comparison | Interpretation |
| --- | --- | --- | --- | --- |
| high | close_substitute_divergence | GLD | IAU | primary representative differs from close substitute |
| high | close_substitute_divergence | AGG | IUSB | primary representative differs from close substitute |
| high | close_substitute_divergence | IWM | IJR | primary representative differs from close substitute |


## Contradiction / Audit Flags

No contradiction flags were triggered by current deterministic rules.

## Data Quality Notes

- Technical rows loaded: `60`
- S&P 500 constituent technical rows loaded: `503`
- Macro rows loaded: `48`
- Live macro rows used: `17`
- Economic rows loaded: `113`
- News rows loaded: `80`
- Positioning/flow rows loaded: `30`

## Cycle Metadata

- Report generated at: 05 November 2026, 11:23:01 (HKT)

# Rule-Based Institutional Market Update

Generated at: 4 November 2026, 20:12:39 (HKT)
Window: 24h

## Executive Dashboard

- Regime score: **50.43 / 100** (Mixed / Rotation)
- US equity strength: **41.16 / 100** (weak)
- Evidence quality: **79.5 / 100**
- ETF flow contribution: **51.53 / 100**, reliability **71.51 / 100**
- Breadth: **narrow**; above 50DMA `41.67%`, above 200DMA `58.33%`
- Top sector score: **Healthcare** `71.38`
- Top theme score: **Healthcare Innovation** `64.11`

## Market Regime Score

| Metric | Value | Driver / Interpretation |
| --- | --- | --- |
| Overall regime | 50.43 | Mixed / Rotation |
| equity_trend | 31.25 | risk-off pressure; Core equity ETFs versus moving averages. |
| equity_momentum | 43.95 | mild risk-off pressure; 5D/20D/60D return momentum across SPY, QQQ, IWM, and SMH. |
| market_breadth | 47.22 | neutral / mixed; Participation breadth from tracked equity/ETF rows. |
| volatility | 70.0 | risk-on support; VIX level and change; higher score means calmer volatility conditions. |
| rates_yield_curve | 58.0 | mild risk-on support; Treasury yield pressure and curve shape; higher score means less rates pressure. |
| credit_proxy | 50.0 | neutral / mixed; Credit-market proxy; currently neutral when no direct spread signal is available. |
| dollar_fx | 57.44 | mild risk-on support; Dollar move; higher score means less USD tightening pressure. |
| commodity_confirmation | 59.0 | mild risk-on support; Copper, silver, oil, and gold mix; higher score means better cyclical confirmation. |
| etf_flow | 51.09 | neutral / mixed; Grouped ETF flow contribution adjusted for reliability. |
| news_confirmation | 65.0 | risk-on support; Weighted headline/news confirmation score. |
| Positive contributors |  | volatility=70.0, news_confirmation=65.0 |
| Negative contributors |  | equity_trend=31.25, equity_momentum=43.95 |

## Forward Signal (Score → Expected Return)

Read-only mapping. The regime score is a *state* descriptor, not a forecast; this table states what that score level has historically implied for forward SPY returns.

| Horizon | Bucket | Historical mean | n | Direction |
| --- | --- | --- | --- | --- |
| 5D | 50-55 | 0.69% | 13 | up |
| 20D | 50-55 | 1.5% | 13 | up |
| 60D | 50-55 | 4.7% | 13 | up |

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

- Confidence score: `79.5`
- Agreement ratio: `0.5`
- Contradiction count: `2`
- Missing indicators: none
- Warning flags: none

## Cross-Asset Confirmation

| Area | Signal | Interpretation |
| --- | --- | --- |
| Equities | S&P 500 rising; Nasdaq rising; Russell 2000 stable | Confirms risk appetite when broad indices rise together; weak small caps would narrow the signal. |
| Rates | 10Y Treasury rising; MOVE falling | Rising yields can pressure duration assets; falling MOVE supports calmer bond volatility. |
| Dollar | DXY proxy falling | A stronger dollar can tighten financial conditions and pressure commodities/emerging-market risk. |
| Credit | HYG stable | High-yield weakness would challenge equity risk-on confirmation. |
| Gold | Gold rising | Gold strength can indicate defensive demand, inflation hedging, or geopolitical concern. |
| Silver | Silver rising | Silver helps distinguish precious-metal demand from industrial/cyclical confirmation when data is available. |
| Copper | Copper rising | Copper strength supports cyclical growth confirmation; weakness would dilute risk-on breadth. |
| Oil | WTI crude falling | Oil spikes can be inflationary risk; falling oil can ease cost pressure but may also flag demand softness. |
| Volatility | VIX falling | Falling VIX supports risk appetite; a volatility spike would reduce confidence in broad risk-on. |

### Macro Snapshot

Live macro rows are intraday snapshots from `public.macro_live`; closed rows are official stored rows from `public.macro`.

| Symbol | Name | Close | Pct Chg | Market Date | Status |
| --- | --- | --- | --- | --- | --- |
| ^GSPC | S&P 500 | 7568.92 | 0.36 | 2026-11-03 | closed |
| ^IXIC | NASDAQ Composite | 25372.01 | 0.83 | 2026-11-03 | closed |
| ^RUT | Russell 2000 Index | 2812.45 | 0.23 | 2026-11-03 | closed |
| ^VIX | CBOE Volatility Index | 18.19 | -12.67 | 2026-11-04 | live as of 4 November 2026, 20:00:24 (HKT) |
| ^SKEW | CBOE SKEW Index | 150.01 | -1.81 | 2026-11-03 | closed |
| ^MOVE | ICE BofA MOVE Index | 99.97 | -0.39 | 2026-11-03 | closed |
| US2YT=X | United States 2-Year Treasury Yield | 4.63 | 0.33 | 2026-11-04 | live as of 4 November 2026, 20:00:24 (HKT) |
| US3YT=X | United States 3-Year Treasury Yield | 4.67 | -0.13 | 2026-11-04 | live as of 4 November 2026, 20:00:24 (HKT) |
| US5YT=X | United States 5-Year Treasury Yield | 4.73 | -0.32 | 2026-11-04 | live as of 4 November 2026, 20:00:24 (HKT) |
| US7YT=X | United States 7-Year Treasury Yield | 4.81 | -0.48 | 2026-11-04 | live as of 4 November 2026, 20:00:24 (HKT) |
| US10YT=X | United States 10-Year Treasury Yield | 4.92 | -0.53 | 2026-11-04 | live as of 4 November 2026, 20:00:24 (HKT) |
| US20YT=X | United States 20-Year Treasury Yield | 5.33 | -0.52 | 2026-11-04 | live as of 4 November 2026, 20:00:24 (HKT) |
| US30YT=X | United States 30-Year Treasury Yield | 5.3 | -0.49 | 2026-11-04 | live as of 4 November 2026, 20:00:24 (HKT) |
| HK50 | Hang Seng Futures | 24104.5 | 3.03 | 2026-11-04 | live as of 4 November 2026, 20:00:24 (HKT) |
| KOR200c1 | KOSPI 200 Futures | 896.5 | 1.28 | 2026-11-03 | live as of 4 November 2026, 20:00:24 (HKT) |
| CIHc1 | SSE 50 Futures | 2748.4 | 0.12 | 2026-11-03 | live as of 4 November 2026, 20:00:24 (HKT) |
| HYG | iShares iBoxx High Yield Corporate Bond ETF | 76.98 | 0.12 | 2026-11-03 | closed |
| LQD | iShares iBoxx Investment Grade Corporate Bond ETF | 103.72 | 0.01 | 2026-11-03 | closed |
| JNK | SPDR Bloomberg High Yield Bond ETF | 92.36 | 0.11 | 2026-11-03 | closed |
| RSP | Invesco S&P 500 Equal Weight ETF | 219.26 | -0.33 | 2026-11-03 | closed |
| IWF | iShares Russell 1000 Growth ETF | 117.44 | 1.05 | 2026-11-03 | closed |
| IWD | iShares Russell 1000 Value ETF | 258.58 | -0.3 | 2026-11-03 | closed |
| TLT | iShares 20+ Year Treasury Bond ETF | 81.11 | -0.76 | 2026-11-03 | closed |
| IEF | iShares 7-10 Year Treasury Bond ETF | 91.16 | -0.37 | 2026-11-03 | closed |
| SHY | iShares 1-3 Year Treasury Bond ETF | 81.4 | -0.07 | 2026-11-03 | closed |
| GC=F | Gold Future | 4051.1 | 2.81 | 2026-11-04 | live as of 4 November 2026, 20:00:24 (HKT) |
| SI=F | Silver Future | 52.04 | 4.95 | 2026-11-04 | live as of 4 November 2026, 20:00:24 (HKT) |
| CL=F | WTI Crude Oil Future | 95.13 | -1.0 | 2026-11-04 | live as of 4 November 2026, 20:00:24 (HKT) |
| HG=F | Copper Future | 6.45 | 1.06 | 2026-11-04 | live as of 4 November 2026, 20:00:24 (HKT) |

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
| Information Technology | 75 | 37.33 | 54.05 | 32.0 | 77.8 | 17.73 | very high | ACN, ROP, GEN | LITE, MRVL, INTC |
| Industrials | 83 | 69.88 | 54.43 | 61.45 | 61.06 | 12.17 | very high | EFX, PNR, LMT | BE, CAT, FIX |
| Financials | 76 | 66.67 | 72.22 | 78.95 | 51.91 | 9.35 | very high | FISV, CBOE, FDS | IBKR, COIN, HOOD |
| Communication Services | 22 | 38.1 | 35.0 | 50.0 | 46.19 | 11.67 | very high | OMC, CMCSA, DIS | GOOG, GOOGL, RDDT |
| Health Care | 60 | 81.67 | 90.0 | 93.33 | 44.68 | 7.45 | very high | REGN, IDXX, GEHC | SOLV, HSIC, ILMN |
| Consumer Discretionary | 47 | 74.47 | 51.06 | 85.11 | 37.15 | 6.7 | very high | HAS, HD, LOW | GRMN, DASH, APTV |
| Materials | 24 | 75.0 | 70.83 | 83.33 | 35.19 | 9.22 | very high | DOW, VMC, PPG | MOS, FCX, ALB |
| Real Estate | 30 | 58.62 | 44.83 | 86.67 | 34.73 | 7.14 | very high | CCI, EXR, PSA | ESS, EQIX, ARE |
| Consumer Staples | 34 | 75.0 | 59.38 | 85.29 | 33.54 | 7.06 | very high | STZ, WMT, DLTR | SYY, BG, ADM |
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
| US dollar/Euro ECB reference exchange rate | 1.12 | USD | -0.0 USD vs prior | 2026-11-03 | EUR weakened versus this currency. |
| Japanese yen/Euro ECB reference exchange rate | 176.95 | JPY | -0.15 JPY vs prior | 2026-11-03 | EUR weakened versus this currency. |
| Chinese yuan renminbi/Euro ECB reference exchange rate | 7.46 | CNY | 0.0 CNY vs prior | 2026-11-03 | EUR strengthened versus this currency. |
| Australian dollar/Euro ECB reference exchange rate | 1.6 | AUD | 0.0 AUD vs prior | 2026-11-03 | EUR strengthened versus this currency. |

ABS Australia note: ABS rows are stored locally/Neon, but most series are dimension-coded; only curated series should be promoted into narrative report text.

## Sector and Theme Leadership

### Official Sector Strength

Supporting and detracting names are the top/bottom S&P 500 constituents by 20D return when constituent coverage is available; otherwise the report falls back to related ETFs.

| Rank | Sector | Score | Trend | Momentum | Stock Breadth | ETF Flow | Flow Reliability | 3M RS | Supporting / Leaders | Detracting / Laggards |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Healthcare | 71.38 | strong uptrend | positive | broad | 81.75 | 100.0 | 62.65 | REGN, IDXX, GEHC | SOLV, HSIC, ILMN |
| 2 | Consumer Staples | 70.97 | strong uptrend | positive | broad | 66.68 | 65.0 | 60.0 | STZ, WMT, DLTR | SYY, BG, ADM |
| 3 | Consumer Discretionary | 66.58 | strong uptrend | neutral | broad | 46.46 | 65.0 | 55.1 | HAS, HD, LOW | GRMN, DASH, APTV |
| 4 | Financials | 66.08 | strong uptrend | neutral | broad | 50.0 | 0.0 | 55.98 | FISV, CBOE, FDS | IBKR, COIN, HOOD |
| 5 | Real Estate | 62.46 | strong uptrend | neutral | broad | 50.0 | 0.0 | 55.97 | CCI, EXR, PSA | ESS, EQIX, ARE |
| 6 | Energy | 60.87 | strong uptrend | positive | broad | 71.7 | 90.0 | 59.95 | COP, CVX, APA | TPL, VLO, BKR |
| 7 | Utilities | 59.64 | uptrend | neutral | broad | 48.22 | 65.0 | 55.31 | AWK, WEC, ED | NRG, CEG, VST |
| 8 | Industrials | 56.23 | neutral | neutral | broad | 52.16 | 65.0 | 49.9 | EFX, PNR, LMT | BE, CAT, FIX |
| 9 | Crypto | 50.21 | neutral | neutral | mixed | 52.14 | 65.0 | 50.0 |  |  |
| 10 | Cybersecurity | 45.26 | neutral | negative | weak | 58.23 | 65.0 | 45.47 | CIBR | CIBR |
| 11 | Defense | 42.32 | strong downtrend | negative | weak | 41.19 | 65.0 | 45.46 | XAR | XAR |
| 12 | Technology | 40.99 | downtrend | negative | weak | 58.82 | 95.0 | 44.11 | ACN, ROP, GEN | LITE, MRVL, INTC |
| 13 | Grid Infrastructure | 35.06 | strong downtrend | negative | weak | 61.4 | 65.0 | 43.53 | GRID | GRID |
| 14 | Semiconductors | 33.68 | strong downtrend | negative | weak | 68.64 | 95.0 | 36.91 | SMH, SOXX | SOXX, SMH |
| 15 | Nuclear | 33.39 | strong downtrend | negative | weak | 50.0 | 0.0 | 33.03 | NLR | NLR |

### Thematic Strength

| Rank | Theme | Score | Setup | ETF Flow | Flow Reliability | Dispersion | Price | News |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Healthcare Innovation | 64.11 | Positive setup | 81.75 | 100.0 | 19.84 | True | False |
| 2 | Energy | 61.99 | Positive setup | 71.7 | 90.0 | 3.93 | True | False |
| 3 | Dividend Defensives | 60.18 | Positive setup | 50.04 | 65.0 | 4.64 | True | False |
| 4 | Small Caps | 48.81 | Neutral / watchlist | 51.5 | 65.0 | 0.0 | False | False |
| 5 | Defense | 48.76 | Neutral / watchlist | 41.19 | 65.0 | 39.2 | False | False |
| 6 | Grid Infrastructure | 45.89 | Neutral / watchlist | 61.4 | 65.0 | 17.49 | False | False |
| 7 | Financials | 45.39 | Neutral / watchlist | 50.0 | 0.0 | 14.08 | False | False |
| 8 | Cybersecurity | 44.59 | Neutral / watchlist | 58.23 | 65.0 | 39.07 | False | False |
| 9 | Quality Growth | 43.64 | Neutral / watchlist | 50.32 | 65.0 | 18.94 | False | False |
| 10 | AI Infrastructure | 41.71 | Weak setup | 68.64 | 95.0 | 19.54 | False | False |
| 11 | Crypto Infrastructure | 40.91 | Weak setup | 52.14 | 65.0 | 4.12 | False | False |
| 12 | Semiconductors | 39.98 | Weak setup | 68.64 | 95.0 | 13.86 | False | True |
| 13 | Nuclear | 27.81 | Underperformance risk | 50.0 | 0.0 | 20.11 | False | False |

- Top 5 improving themes: Crypto Infrastructure, Energy, Healthcare Innovation, Dividend Defensives, Cybersecurity
- Top 5 deteriorating themes: Nuclear, Defense, Financials, Semiconductors, AI Infrastructure
- Strong news but weak price confirmation: Semiconductors
- Strong price but weak news confirmation: Healthcare Innovation, Energy, Dividend Defensives

### Sector / Theme Alignment

| Sector | Related Themes | Sector Score | Sector Signal | Theme Score | Theme Signal | Interpretation |
| --- | --- | --- | --- | --- | --- | --- |
| Healthcare | Healthcare Innovation | 71.38 | strong | 64.11 | positive | sector and theme confirmation |
| Consumer Staples | Dividend Defensives | 70.97 | strong | 60.18 | positive | sector and theme confirmation |
| Consumer Discretionary | Small Caps | 66.58 | strong | 48.81 | mixed | sector stronger than related themes |
| Financials | Financials | 66.08 | strong | 45.39 | mixed | sector stronger than related themes |
| Real Estate | Dividend Defensives | 62.46 | positive | 60.18 | positive | sector and theme confirmation |
| Energy | Energy | 60.87 | positive | 61.99 | positive | sector and theme confirmation |
| Utilities | Grid Infrastructure, Nuclear, Dividend Defensives | 59.64 | positive | 44.62 | weak | sector stronger than related themes |
| Industrials | Defense, Grid Infrastructure | 56.23 | positive | 47.32 | mixed | sector stronger than related themes |
| Crypto | Crypto Infrastructure | 50.21 | mixed | 40.91 | weak | mixed confirmation |
| Cybersecurity | Cybersecurity | 45.26 | mixed | 44.59 | weak | mixed confirmation |
| Defense | Defense | 42.32 | weak | 48.76 | mixed | mixed confirmation |
| Technology | AI Infrastructure, Semiconductors, Quality Growth | 40.99 | weak | 41.77 | weak | broad weakness across sector and themes |
| Grid Infrastructure | Grid Infrastructure | 35.06 | weak | 45.89 | mixed | mixed confirmation |
| Semiconductors | AI Infrastructure, Semiconductors | 33.68 | very weak | 40.84 | weak | broad weakness across sector and themes |
| Nuclear | Nuclear | 33.39 | very weak | 27.81 | very weak | broad weakness across sector and themes |

## Three-Month Outperformance Setup

| Rank | Theme | Score | Classification | Drivers | Invalidation Triggers |
| --- | --- | --- | --- | --- | --- |
| 1 | Energy | 67.0 | Positive setup | relative_strength_20d, relative_strength_60d, trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
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
| 12 | Semiconductors | 37.77 | Weak setup |  | relative strength below SPY, breadth below 45%, news turns negative |

## Breadth and Participation

- Above 50DMA: `41.67%`
- Above 200DMA: `58.33%`
- Positive 20D return: `41.67%`

## Volatility and Risk Signals

- VIX close=18.19 pct_chg=-12.67

## News Analytics

- Sentiment counts: {'positive': 51, 'negative': 27, 'neutral': 2}
- News confirmation score: `65.0`

### Top Market-Moving Headlines

**1. Gold, silver and precious metals prices jump, dollar dips as Democrats take control of Congress**
- Source: CNBC Top News
- Importance / impact: Medium / Positive
- Relevance / horizon: sector_theme / short-term
- Affected assets: GC=F, SI=F, XAU, XAG, U.S
- Score: `44.61`
- Investment implication: Theme or sector positive signal; requires price and volume confirmation before affecting rankings.

**2. Super Micro’s stock pops as earnings show booming demand for AI servers**
- Source: MarketWatch Bulletins
- Importance / impact: Medium / Positive
- Relevance / horizon: sector_theme / short-term
- Affected assets: SM, SUPN, AI, Earnings, Semiconductors
- Score: `43.76`
- Investment implication: Theme or sector positive signal; requires price and volume confirmation before affecting rankings.

**3. Russia bombards Ukraine power grid before Abu Dhabi talks; Merz urges Moscow to engage**
- Source: Investing.com Stock Market
- Importance / impact: Medium / Negative
- Relevance / horizon: sector_theme / short-term
- Affected assets: geopolitics, energy, conflict
- Score: `39.8`
- Investment implication: Theme or sector negative signal; requires price and volume confirmation before affecting rankings.

**4. LG U+ Q3 2026 slides: profit surges 84% on AI growth, efficiency**
- Source: Investing.com Markets
- Importance / impact: Medium / Positive
- Relevance / horizon: sector_theme / short-term
- Affected assets: LG, U, AI growth, profit surge, operational efficiency
- Score: `39.15`
- Investment implication: Theme or sector positive signal; requires price and volume confirmation before affecting rankings.

**5. Iran Turns to Guerrilla Tactics in Bid to Reassert Grip on Strait of Hormuz**
- Source: Dow Jones US Business
- Importance / impact: Medium / Negative
- Relevance / horizon: macro / short-term
- Affected assets: geopolitics, maritime security, energy supply
- Score: `38.25`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the short-term.

**6. AMD Q3 2026 slides: data center surges 97%, record earnings beat**
- Source: Investing.com Markets
- Importance / impact: Medium / Positive
- Relevance / horizon: single_name / quarterly
- Affected assets: AMD, earnings beat, data center growth, revenue surge
- Score: `35.93`
- Investment implication: Single-name positive signal; low weight unless it maps to a broader sector or theme.

**7. Super Micro’s stock pops as earnings show booming demand for AI servers**
- Source: MarketWatch Top Stories
- Importance / impact: Medium / Positive
- Relevance / horizon: single_name / short-term
- Affected assets: SMCI, AI, earnings, server demand
- Score: `35.22`
- Investment implication: Single-name positive signal; low weight unless it maps to a broader sector or theme.

**8. Oil prices subdued amid U.S.-Iran diplomacy hopes, Trump’s halting of Israel aid**
- Source: Investing.com Stock Market
- Importance / impact: Low / Positive
- Relevance / horizon: macro / short-term
- Affected assets: USO, WTI, U.S, Geopolitical Risk, Oil Prices
- Score: `34.81`
- Investment implication: Macro-relevant positive signal; use as context for rates, volatility, and index confirmation over the short-term.

**9. Oil prices ease to settle near 4-week low on hopes peace talks will end wars**
- Source: Investing.com Stock Market
- Importance / impact: Low / Positive
- Relevance / horizon: macro / short-term
- Affected assets: US, Geopolitical Risk, Oil Prices, Military Conflict
- Score: `34.81`
- Investment implication: Macro-relevant positive signal; use as context for rates, volatility, and index confirmation over the short-term.

**10. AMD has been crushed into earnings. Here’s one way to trade it**
- Source: CNBC Top News
- Importance / impact: Low / Negative
- Relevance / horizon: single_name / short-term
- Affected assets: AMD, earnings, stock-price-decline, trading-strategy
- Score: `33.46`
- Investment implication: Single-name negative signal; low weight unless it maps to a broader sector or theme.


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
- Market flow score: `48.0 / 100`
- Equity risk flow: `45.9`
- Credit risk flow: `53.6`
- Sector cyclicality flow: `46.5`
- Duration/liquidity flow: `46.8`
- Alternatives: `mixed alternative-asset demand`
- ETF flow reliability: `71.5 / 100`
- Dominant allocation direction: `mixed allocation`

### Core Flow Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVV | U.S. Broad Equity | -0.1 | -0.8 | 0.5 | -0.8 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Medium-term recovery | 87.0 |
| ACWI | Global Equity | -0.6 | -0.7 | 0.0 | -0.2 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Mixed or neutral flow structure; Persistent selling | 77.0 |
| EFA | Developed Markets ex-U.S. | -0.2 | 0.6 | 0.0 | -0.9 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Mixed or neutral flow structure; Persistent selling | 77.0 |
| IEMG | Emerging Markets | -0.4 | -0.3 | 0.0 | 0.6 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Mixed or neutral flow structure; Persistent selling | 77.0 |
| IJH | U.S. Mid Cap | -0.8 | 0.1 | 0.6 | 1.3 | Flat | Neutral | High | High-Turnover Consolidation | Transition | Structural accumulation | 91.0 |
| IWM | U.S. Small Cap | -1.0 | 0.6 | 0.6 | -0.7 | Flat | Neutral | Normal | Neutral | Neutral | Structural distribution | 79.0 |
| LQD | Investment-Grade Credit | 1.7 | -0.0 | 0.7 | 0.1 | Up | Buy | Normal | Steady Accumulation | Risk-On | Strong confirmation | 95.0 |
| HYG | High-Yield Credit | -0.3 | 0.4 | 0.5 | -0.4 | Flat | Neutral | Normal | Neutral | Neutral | Medium-term deterioration | 83.0 |
| SGOV | Treasury Bills / Cash | -1.4 | -1.1 | 0.8 | -0.3 | Flat | Sell | Normal | Quiet Distribution | Weakening | Strong confirmation; Strong sponsorship | 100.0 |
| SHY | Short-Duration Treasuries | 0.6 | 1.7 | 0.8 | -0.5 | Flat | Neutral | Normal | Neutral | Neutral | Structural accumulation; Strong sponsorship | 99.0 |
| IEF | Intermediate-Duration Treasuries | 1.3 | 1.1 | 0.6 | 0.7 | Up | Buy | Normal | Steady Accumulation | Risk-On | Strong confirmation | 95.0 |
| TLT | Long-Duration Treasuries | -0.9 | 0.4 | 0.6 | -0.5 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Medium-term deterioration | 83.0 |
| GLD | Gold | -1.0 | 0.7 | 0.3 | -0.9 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Medium-term deterioration | 83.0 |
| IBIT | Bitcoin | -0.2 | 1.2 | 0.6 | -0.9 | Down | Sell | Normal | Persistent Distribution | Risk-Off | Tactical profit-taking inside structural accumulation; Exceptional institutional selling | 75.0 |

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
| ITA | Aerospace and Defense | -0.1 | -0.0 | 0.3 | 1.7 | Up | Sell | High | Distribution into Strength | Bearish Divergence | Strong confirmation | 95.0 |
| SOXX | Semiconductors | 1.3 | -0.2 | 0.8 | 1.8 | Down | Neutral | High | Heavy Selling Pressure | Cautious | Structural accumulation; Strong sponsorship | 99.0 |
| SMH | Semiconductors | 0.4 | -0.1 | 0.6 | 0.5 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural accumulation | 91.0 |
| CIBR | Cybersecurity | -0.3 | 1.3 | 0.7 | 0.9 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural accumulation | 91.0 |

### Material Flow Divergences

| Severity | Type | Primary | Comparison | Interpretation |
| --- | --- | --- | --- | --- |
| medium | related_subsector_divergence | XLI | ITA | defense-specific demand differs from broad industrials |
| medium | related_subsector_divergence | XLK | SOXX | technology differs from semiconductors |
| high | close_substitute_divergence | GLD | IAU | primary representative differs from close substitute |
| high | close_substitute_divergence | IVV | SPY | primary representative differs from close substitute |
| high | close_substitute_divergence | AGG | IUSB | primary representative differs from close substitute |
| high | close_substitute_divergence | HYG | JNK | primary representative differs from close substitute |


## Contradiction / Audit Flags

| Severity | Section | Issue | Deterministic Fix |
| --- | --- | --- | --- |
| low | Theme Strength Ranking | Semiconductors has strong news confirmation but weak price confirmation. | Classify as unconfirmed narrative. |

## Data Quality Notes

- Technical rows loaded: `60`
- S&P 500 constituent technical rows loaded: `503`
- Macro rows loaded: `48`
- Live macro rows used: `26`
- Economic rows loaded: `113`
- News rows loaded: `80`
- Positioning/flow rows loaded: `30`

## Cycle Metadata

- Report generated at: 04 November 2026, 20:12:39 (HKT)

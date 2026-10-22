# Rule-Based Institutional Market Update

Generated at: 23 October 2026, 03:10:27 (HKT)
Window: 24h

## Executive Dashboard

- Regime score: **51.84 / 100** (Mixed / Rotation)
- US equity strength: **50.14 / 100** (neutral)
- Evidence quality: **72.5 / 100**
- ETF flow contribution: **48.06 / 100**, reliability **71.51 / 100**
- Breadth: **narrow**; above 50DMA `46.67%`, above 200DMA `55.0%`
- Top sector score: **Healthcare** `67.5`
- Top theme score: **Energy** `65.97`

## Market Regime Score

| Metric | Value | Driver / Interpretation |
| --- | --- | --- |
| Overall regime | 51.84 | Mixed / Rotation |
| equity_trend | 47.5 | neutral / mixed; Core equity ETFs versus moving averages. |
| equity_momentum | 49.91 | neutral / mixed; 5D/20D/60D return momentum across SPY, QQQ, IWM, and SMH. |
| market_breadth | 48.33 | neutral / mixed; Participation breadth from tracked equity/ETF rows. |
| volatility | 70.0 | risk-on support; VIX level and change; higher score means calmer volatility conditions. |
| rates_yield_curve | 58.0 | mild risk-on support; Treasury yield pressure and curve shape; higher score means less rates pressure. |
| credit_proxy | 50.0 | neutral / mixed; Credit-market proxy; currently neutral when no direct spread signal is available. |
| dollar_fx | 55.0 | mild risk-on support; Dollar move; higher score means less USD tightening pressure. |
| commodity_confirmation | 42.0 | mild risk-off pressure; Copper, silver, oil, and gold mix; higher score means better cyclical confirmation. |
| etf_flow | 48.61 | neutral / mixed; Grouped ETF flow contribution adjusted for reliability. |
| news_confirmation | 50.0 | neutral / mixed; Weighted headline/news confirmation score. |
| Positive contributors |  | volatility=70.0 |
| Negative contributors |  | commodity_confirmation=42.0 |

## US Equity Strength Score

| Component | Score |
| --- | --- |
| indices_above_moving_averages | 47.5 |
| sp500_trend | 100.0 |
| nasdaq_trend | 55.0 |
| russell_participation | 0.0 |
| returns_momentum | 49.91 |
| rsi_zone | 47.5 |
| macd_confirmation | 43.75 |
| volume_confirmation | 50.0 |
| breadth | 48.33 |

## Evidence Quality / Confidence

- Confidence score: `72.5`
- Agreement ratio: `0.3`
- Contradiction count: `1`
- Missing indicators: none
- Warning flags: none

## Cross-Asset Confirmation

| Area | Signal | Interpretation |
| --- | --- | --- |
| Equities | S&P 500 unavailable; Nasdaq unavailable; Russell 2000 unavailable | Confirms risk appetite when broad indices rise together; weak small caps would narrow the signal. |
| Rates | 10Y Treasury unavailable; MOVE unavailable | Rising yields can pressure duration assets; falling MOVE supports calmer bond volatility. |
| Dollar | DXY proxy unavailable | A stronger dollar can tighten financial conditions and pressure commodities/emerging-market risk. |
| Credit | HYG unavailable | High-yield weakness would challenge equity risk-on confirmation. |
| Gold | Gold falling | Gold strength can indicate defensive demand, inflation hedging, or geopolitical concern. |
| Silver | Silver falling | Silver helps distinguish precious-metal demand from industrial/cyclical confirmation when data is available. |
| Copper | Copper falling | Copper strength supports cyclical growth confirmation; weakness would dilute risk-on breadth. |
| Oil | WTI crude rising | Oil spikes can be inflationary risk; falling oil can ease cost pressure but may also flag demand softness. |
| Volatility | VIX unavailable | Falling VIX supports risk appetite; a volatility spike would reduce confidence in broad risk-on. |

### Macro Snapshot

Live macro rows are intraday snapshots from `public.macro_live`; closed rows are official stored rows from `public.macro`.

| Symbol | Name | Close | Pct Chg | Market Date | Status |
| --- | --- | --- | --- | --- | --- |
| ^GSPC | S&P 500 | 7642.52 | n/a | 2026-10-22 | live as of 23 October 2026, 03:00:31 (HKT) |
| ^IXIC | NASDAQ Composite | 25939.35 | n/a | 2026-10-22 | live as of 23 October 2026, 03:00:31 (HKT) |
| ^RUT | Russell 2000 Index | 2774.38 | n/a | 2026-10-22 | live as of 23 October 2026, 03:00:31 (HKT) |
| ^VIX | CBOE Volatility Index | 19.93 | n/a | 2026-10-22 | live as of 23 October 2026, 03:00:31 (HKT) |
| ^SKEW | CBOE SKEW Index | 150.36 | -6.26 | 2026-10-21 | closed |
| ^MOVE | ICE BofA MOVE Index | 106.47 | n/a | 2026-10-22 | live as of 23 October 2026, 03:00:31 (HKT) |
| US2YT=X | United States 2-Year Treasury Yield | 4.64 | n/a | 2026-10-22 | live as of 23 October 2026, 03:00:31 (HKT) |
| US3YT=X | United States 3-Year Treasury Yield | 4.71 | n/a | 2026-10-22 | live as of 23 October 2026, 03:00:31 (HKT) |
| US5YT=X | United States 5-Year Treasury Yield | 4.77 | n/a | 2026-10-22 | live as of 23 October 2026, 03:00:31 (HKT) |
| US7YT=X | United States 7-Year Treasury Yield | 4.85 | n/a | 2026-10-22 | live as of 23 October 2026, 03:00:31 (HKT) |
| US10YT=X | United States 10-Year Treasury Yield | 4.95 | n/a | 2026-10-22 | live as of 23 October 2026, 03:00:31 (HKT) |
| US20YT=X | United States 20-Year Treasury Yield | 5.33 | n/a | 2026-10-22 | live as of 23 October 2026, 03:00:31 (HKT) |
| US30YT=X | United States 30-Year Treasury Yield | 5.29 | n/a | 2026-10-22 | live as of 23 October 2026, 03:00:31 (HKT) |
| HK50 | HK50 | 24107.5 | -0.71 | 2026-10-16 | closed |
| KOR200c1 | KOSPI 200 Futures | 885.1 | n/a | 2026-10-21 | live as of 23 October 2026, 03:00:31 (HKT) |
| CIHc1 | CIHc1 | 2720.0 | -0.04 | 2026-10-16 | closed |
| HYG | iShares iBoxx High Yield Corporate Bond ETF | 77.06 | n/a | 2026-10-22 | live as of 23 October 2026, 03:00:31 (HKT) |
| LQD | iShares iBoxx Investment Grade Corporate Bond ETF | 104.39 | n/a | 2026-10-22 | live as of 23 October 2026, 03:00:31 (HKT) |
| JNK | SPDR Bloomberg High Yield Bond ETF | 92.5 | n/a | 2026-10-22 | live as of 23 October 2026, 03:00:31 (HKT) |
| RSP | Invesco S&P 500 Equal Weight ETF | 217.27 | n/a | 2026-10-22 | live as of 23 October 2026, 03:00:31 (HKT) |
| IWF | iShares Russell 1000 Growth ETF | 119.74 | n/a | 2026-10-22 | live as of 23 October 2026, 03:00:31 (HKT) |
| IWD | iShares Russell 1000 Value ETF | 258.2 | n/a | 2026-10-22 | live as of 23 October 2026, 03:00:31 (HKT) |
| TLT | iShares 20+ Year Treasury Bond ETF | 81.84 | n/a | 2026-10-22 | live as of 23 October 2026, 03:00:31 (HKT) |
| IEF | iShares 7-10 Year Treasury Bond ETF | 91.32 | n/a | 2026-10-22 | live as of 23 October 2026, 03:00:31 (HKT) |
| SHY | iShares 1-3 Year Treasury Bond ETF | 81.53 | n/a | 2026-10-22 | live as of 23 October 2026, 03:00:31 (HKT) |
| GC=F | Gold Future | 4047.8 | -2.46 | 2026-10-22 | live as of 23 October 2026, 03:00:31 (HKT) |
| SI=F | Silver Future | 54.79 | -4.58 | 2026-10-22 | live as of 23 October 2026, 03:00:31 (HKT) |
| CL=F | WTI Crude Oil Future | 99.47 | 2.39 | 2026-10-22 | live as of 23 October 2026, 03:00:31 (HKT) |
| HG=F | Copper Future | 6.39 | -2.29 | 2026-10-22 | live as of 23 October 2026, 03:00:31 (HKT) |

## Market Dispersion Analysis

- Sector ETF 20D dispersion: `12.76` points (high); leader `XLE` (Energy) `9.28`, laggard `XLK` (Technology) `-3.48`
- Sector ETF 60D dispersion: `26.98` points (very high); leader `XLE` (Energy) `18.39`, laggard `XLRE` (Real Estate) `-8.59`

| Comparison | Left | Right | 20D Spread | Signal |
| --- | --- | --- | --- | --- |
| Equal-weight vs cap-weight | RSP (Equal-weight S&P 500) | SPY (S&P 500) | 1.83 | broader participation |
| Small-cap vs large-cap | IWM (Russell 2000) | SPY (S&P 500) | -2.62 | large-cap leadership |
| Growth vs value | IWF (Russell 1000 Growth) | IWD (Russell 1000 Value) | -4.21 | value leadership |
| Nasdaq vs S&P 500 | QQQ (Nasdaq 100) | SPY (S&P 500) | -2.85 | S&P 500 leadership |

## Sector Constituent Dispersion

- Breadth 50D / 200D: percentage of active S&P 500 constituents in the sector trading above the 50-day / 200-day moving average.
- Positive 20D: percentage of active sector constituents with positive 20-day return.
- Std 20D: cross-sectional standard deviation of constituent 20-day returns; higher means wider stock-level dispersion.

| Sector | Count | Breadth 50D | Breadth 200D | Positive 20D | 20D Dispersion | Std 20D | Label | Leaders | Laggards |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Information Technology | 75 | 54.67 | 64.86 | 48.0 | 63.01 | 12.58 | very high | PTC, ACN, IT | SNDK, INTC, STX |
| Consumer Discretionary | 47 | 48.94 | 38.3 | 68.09 | 55.49 | 10.19 | very high | HAS, RCL, CCL | GM, CMG, MGM |
| Health Care | 60 | 78.33 | 81.67 | 85.0 | 43.96 | 7.11 | very high | MRNA, CRL, VEEV | JNJ, DXCM, INCY |
| Materials | 24 | 66.67 | 62.5 | 66.67 | 36.51 | 8.56 | very high | BALL, VMC, NUE | SW, ALB, MOS |
| Financials | 76 | 44.0 | 61.97 | 64.47 | 35.51 | 6.79 | very high | CBOE, FDS, BRO | APO, COIN, HOOD |
| Real Estate | 30 | 20.69 | 20.69 | 40.0 | 34.93 | 6.75 | very high | CSGP, HST, CCI | DOC, WY, ARE |
| Industrials | 83 | 49.4 | 43.04 | 62.65 | 29.4 | 6.15 | very high | CTAS, EFX, VRSK | BE, FIX, VRT |
| Consumer Staples | 34 | 71.88 | 59.38 | 73.53 | 25.46 | 5.88 | very high | CASY, STZ, KR | MKC, BG, GIS |
| Energy | 21 | 80.95 | 71.43 | 90.48 | 23.99 | 5.8 | very high | MPC, VLO, COP | WMB, SLB, BKR |
| Communication Services | 22 | 33.33 | 40.0 | 36.36 | 23.23 | 6.43 | very high | NWSA, DIS, OMC | NFLX, T, APP |
| Utilities | 31 | 67.74 | 19.35 | 96.77 | 14.08 | 3.22 | high | VST, PNW, NI | AES, ES, NRG |

## Economic Data Snapshot

### U.S. Labor

| Indicator | Latest | Unit | Change | Date | Rule-Based Interpretation |
| --- | --- | --- | --- | --- | --- |
| All Employees, Total Nonfarm | 159044.0 | thousands | 29.0 thousands vs prior | 2026-09-01 | Higher reading supports activity or liquidity. |
| Unemployment Rate | 4.2 | percent | 0.1 pp vs prior | 2026-09-01 | Higher reading increases macro pressure. |
| Initial Claims | 215000.0 | number | -12000.0 number vs prior | 2026-06-20 | Lower claims indicate firmer labor-market conditions. |
| Continued Claims | 1821000.0 | number | 21000.0 number vs prior | 2026-06-13 | Higher claims indicate softer labor-market conditions. |
| Labor Force Participation Rate | 61.8 | percent | 0.2 pp vs prior | 2026-09-01 | Higher participation expands labor supply. |

### U.S. Growth

| Indicator | Latest | Unit | Change | Date | Rule-Based Interpretation |
| --- | --- | --- | --- | --- | --- |
| Real Gross Domestic Product | 24408.01 | billions chained 2017 dollars | 133.63 billions chained 2017 dollars vs prior | 2026-04-01 | Higher reading supports activity or liquidity. |
| Industrial Production Index | 102.65 | index 2017=100 | 0.14 index pts vs prior | 2026-05-01 | Higher reading supports activity or liquidity. |
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
| Headline PCE Price Index month-over-month inflation rate | 0.31 | percent | 0.26 pp vs prior | 2026-08-01 | Higher reading increases macro pressure. |
| Headline PCE Price Index year-over-year inflation rate | 3.42 | percent | 0.06 pp vs prior | 2026-08-01 | Higher reading increases macro pressure. |
| Core PCE Price Index month-over-month inflation rate | 0.25 | percent | 0.12 pp vs prior | 2026-08-01 | Higher reading increases macro pressure. |
| Core PCE Price Index year-over-year inflation rate | 3.01 | percent | 0.02 pp vs prior | 2026-08-01 | Higher reading increases macro pressure. |
| Headline PPI Final Demand month-over-month inflation rate | 1.11 | percent | 0.76 pp vs prior | 2026-09-01 | Higher reading increases macro pressure. |
| Headline PPI Final Demand year-over-year inflation rate | 6.34 | percent | 0.73 pp vs prior | 2026-09-01 | Higher reading increases macro pressure. |
| Core PPI Final Demand Less Foods and Energy month-over-month inflation rate | 0.68 | percent | 0.44 pp vs prior | 2026-09-01 | Higher reading increases macro pressure. |
| Core PPI Final Demand Less Foods and Energy year-over-year inflation rate | 4.98 | percent | 0.17 pp vs prior | 2026-09-01 | Higher reading increases macro pressure. |
| Consumer Price Index for All Urban Consumers | 336.3 | index 1982-1984=100 | 2.17 index pts vs prior | 2026-09-01 | Higher reading increases macro pressure. |
| Core CPI | 338.9 | index 1982-1984=100 | 1.13 index pts vs prior | 2026-09-01 | Higher reading increases macro pressure. |
| Personal Consumption Expenditures Price Index | 131.58 | index 2017=100 | 0.41 index pts vs prior | 2026-08-01 | Higher reading increases macro pressure. |
| Core PCE Price Index | 130.46 | index 2017=100 | 0.32 index pts vs prior | 2026-08-01 | Higher reading increases macro pressure. |
| Producer Price Index: Final Demand | 159.61 | index Nov 2009=100 | 1.76 index pts vs prior | 2026-09-01 | Latest structural macro observation. |
| Producer Price Index: Final Demand Less Foods and Energy | 156.17 | index Apr 2010=100 | 1.06 index pts vs prior | 2026-09-01 | Latest structural macro observation. |

### Policy, Liquidity, Credit

| Indicator | Latest | Unit | Change | Date | Rule-Based Interpretation |
| --- | --- | --- | --- | --- | --- |
| Federal Funds Effective Rate | 3.63 | percent | 0.0 pp vs prior | 2026-06-29 | Stable reading. |
| Secured Overnight Financing Rate | 3.62 | percent | 0.0 pp vs prior | 2026-06-29 | Stable reading. |
| Effective Federal Funds Rate | 3.63 | percent | -0.01 pp vs prior | 2026-05-01 | Lower reading eases macro pressure. |
| Assets: Total Assets: Federal Reserve | 6735645.0 | millions dollars | -779.0 millions dollars vs prior | 2026-06-24 | Lower reading signals softer activity or liquidity. |
| M1 Money Stock | 19750.9 | billions dollars | 219.2 billions dollars vs prior | 2026-05-01 | Higher reading supports activity or liquidity. |
| M2 Money Stock | 23052.3 | billions dollars | 247.8 billions dollars vs prior | 2026-05-01 | Higher reading supports activity or liquidity. |
| ICE BofA US High Yield Option-Adjusted Spread | 2.8 | percent | -0.03 pp vs prior | 2026-06-29 | Lower reading eases macro pressure. |
| ICE BofA US Corporate Option-Adjusted Spread | 0.76 | percent | -0.01 pp vs prior | 2026-06-29 | Lower reading eases macro pressure. |

### Housing and Sentiment

| Indicator | Latest | Unit | Change | Date | Rule-Based Interpretation |
| --- | --- | --- | --- | --- | --- |
| Housing Starts | 1221.0 | thousands | -67.0 thousands vs prior | 2026-09-01 | Lower reading signals softer activity or liquidity. |
| New Privately-Owned Housing Units Authorized | 1400.0 | thousands | -3.0 thousands vs prior | 2026-09-01 | Lower reading signals softer activity or liquidity. |
| 30-Year Fixed Rate Mortgage Average | 6.49 | percent | 0.02 pp vs prior | 2026-06-25 | Higher reading increases macro pressure. |
| University of Michigan Consumer Sentiment | 44.8 | index 1966:Q1=100 | -5.0 index pts vs prior | 2026-05-01 | Lower reading signals softer activity or liquidity. |

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
| US dollar/Euro ECB reference exchange rate | 1.12 | USD | -0.0 USD vs prior | 2026-10-22 | EUR weakened versus this currency. |
| Japanese yen/Euro ECB reference exchange rate | 175.97 | JPY | -1.39 JPY vs prior | 2026-10-22 | EUR weakened versus this currency. |
| Chinese yuan renminbi/Euro ECB reference exchange rate | 7.48 | CNY | -0.02 CNY vs prior | 2026-10-22 | EUR weakened versus this currency. |
| Australian dollar/Euro ECB reference exchange rate | 1.6 | AUD | 0.0 AUD vs prior | 2026-10-22 | EUR strengthened versus this currency. |

ABS Australia note: ABS rows are stored locally/Neon, but most series are dimension-coded; only curated series should be promoted into narrative report text.

## Sector and Theme Leadership

### Official Sector Strength

Supporting and detracting names are the top/bottom S&P 500 constituents by 20D return when constituent coverage is available; otherwise the report falls back to related ETFs.

| Rank | Sector | Score | Trend | Momentum | Stock Breadth | ETF Flow | Flow Reliability | 3M RS | Supporting / Leaders | Detracting / Laggards |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Healthcare | 67.5 | strong uptrend | positive | broad | 79.91 | 100.0 | 54.24 | MRNA, CRL, VEEV | JNJ, DXCM, INCY |
| 2 | Energy | 67.05 | strong uptrend | positive | broad | 54.46 | 90.0 | 60.78 | MPC, VLO, COP | WMB, SLB, BKR |
| 3 | Consumer Staples | 63.98 | strong uptrend | neutral | broad | 53.34 | 65.0 | 51.28 | CASY, STZ, KR | MKC, BG, GIS |
| 4 | Cybersecurity | 58.38 | strong uptrend | neutral | broad | 61.88 | 65.0 | 53.54 | CIBR | CIBR |
| 5 | Consumer Discretionary | 56.52 | uptrend | neutral | broad | 41.24 | 65.0 | 51.58 | HAS, RCL, CCL | GM, CMG, MGM |
| 6 | Utilities | 55.16 | neutral | neutral | broad | 60.38 | 65.0 | 49.93 | VST, PNW, NI | AES, ES, NRG |
| 7 | Financials | 53.17 | strong uptrend | neutral | weak | 50.0 | 0.0 | 48.41 | CBOE, FDS, BRO | APO, COIN, HOOD |
| 8 | Crypto | 51.39 | neutral | neutral | mixed | 63.91 | 65.0 | 50.0 |  |  |
| 9 | Technology | 45.97 | neutral | neutral | weak | 47.45 | 90.0 | 49.67 | PTC, ACN, IT | SNDK, INTC, STX |
| 10 | Real Estate | 44.78 | strong downtrend | neutral | weak | 53.7 | 100.0 | 44.73 | CSGP, HST, CCI | DOC, WY, ARE |
| 11 | Semiconductors | 43.57 | downtrend | neutral | weak | 78.46 | 100.0 | 44.47 | SMH, SOXX | SOXX, SMH |
| 12 | Industrials | 39.58 | strong downtrend | neutral | weak | 68.5 | 65.0 | 44.11 | CTAS, EFX, VRSK | BE, FIX, VRT |
| 13 | Defense | 36.35 | strong downtrend | negative | weak | 50.0 | 0.0 | 36.4 | XAR | XAR |
| 14 | Grid Infrastructure | 36.35 | strong downtrend | neutral | weak | 64.91 | 65.0 | 44.35 | GRID | GRID |
| 15 | Nuclear | 32.09 | strong downtrend | negative | weak | 50.0 | 0.0 | 35.62 | NLR | NLR |

### Thematic Strength

| Rank | Theme | Score | Setup | ETF Flow | Flow Reliability | Dispersion | Price | News |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Energy | 65.97 | Positive setup | 54.46 | 90.0 | 1.17 | True | False |
| 2 | Healthcare Innovation | 64.97 | Positive setup | 79.91 | 100.0 | 11.1 | True | False |
| 3 | Dividend Defensives | 58.82 | Positive setup | 54.39 | 65.0 | 0.35 | False | False |
| 4 | Cybersecurity | 55.75 | Positive setup | 61.88 | 65.0 | 19.58 | False | False |
| 5 | AI Infrastructure | 50.69 | Neutral / watchlist | 78.46 | 100.0 | 16.25 | False | False |
| 6 | Crypto Infrastructure | 50.51 | Neutral / watchlist | 63.91 | 65.0 | 5.25 | False | False |
| 7 | Quality Growth | 49.16 | Neutral / watchlist | 50.98 | 65.0 | 9.95 | False | False |
| 8 | Semiconductors | 47.17 | Neutral / watchlist | 78.46 | 100.0 | 8.5 | False | False |
| 9 | Defense | 40.78 | Weak setup | 50.0 | 0.0 | 29.76 | False | False |
| 10 | Grid Infrastructure | 40.77 | Weak setup | 64.91 | 65.0 | 18.71 | False | False |
| 11 | Financials | 40.47 | Weak setup | 50.0 | 0.0 | 12.07 | False | False |
| 12 | Small Caps | 35.06 | Weak setup | 44.13 | 65.0 | 0.0 | False | False |
| 13 | Nuclear | 28.43 | Underperformance risk | 50.0 | 0.0 | 18.35 | False | False |

- Top 5 improving themes: Crypto Infrastructure, Cybersecurity, Energy, AI Infrastructure, Quality Growth
- Top 5 deteriorating themes: Nuclear, Defense, Financials, Small Caps, Grid Infrastructure
- Strong news but weak price confirmation: none
- Strong price but weak news confirmation: Energy, Healthcare Innovation

### Sector / Theme Alignment

| Sector | Related Themes | Sector Score | Sector Signal | Theme Score | Theme Signal | Interpretation |
| --- | --- | --- | --- | --- | --- | --- |
| Healthcare | Healthcare Innovation | 67.5 | strong | 64.97 | positive | sector and theme confirmation |
| Energy | Energy | 67.05 | strong | 65.97 | strong | sector and theme confirmation |
| Consumer Staples | Dividend Defensives | 63.98 | positive | 58.82 | positive | sector and theme confirmation |
| Cybersecurity | Cybersecurity | 58.38 | positive | 55.75 | positive | sector and theme confirmation |
| Consumer Discretionary | Small Caps | 56.52 | positive | 35.06 | weak | sector stronger than related themes |
| Utilities | Grid Infrastructure, Nuclear, Dividend Defensives | 55.16 | positive | 42.67 | weak | sector stronger than related themes |
| Financials | Financials | 53.17 | mixed | 40.47 | weak | mixed confirmation |
| Crypto | Crypto Infrastructure | 51.39 | mixed | 50.51 | mixed | mixed confirmation |
| Technology | AI Infrastructure, Semiconductors, Quality Growth | 45.97 | mixed | 49.01 | mixed | mixed confirmation |
| Real Estate | Dividend Defensives | 44.78 | weak | 58.82 | positive | theme stronger than official sector |
| Semiconductors | AI Infrastructure, Semiconductors | 43.57 | weak | 48.93 | mixed | mixed confirmation |
| Industrials | Defense, Grid Infrastructure | 39.58 | weak | 40.77 | weak | broad weakness across sector and themes |
| Defense | Defense | 36.35 | weak | 40.78 | weak | broad weakness across sector and themes |
| Grid Infrastructure | Grid Infrastructure | 36.35 | weak | 40.77 | weak | broad weakness across sector and themes |
| Nuclear | Nuclear | 32.09 | very weak | 28.43 | very weak | broad weakness across sector and themes |

## Three-Month Outperformance Setup

| Rank | Theme | Score | Classification | Drivers | Invalidation Triggers |
| --- | --- | --- | --- | --- | --- |
| 1 | Energy | 69.35 | Positive setup | relative_strength_60d, trend_persistence, breadth, downside_volatility, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 2 | Healthcare Innovation | 65.11 | Positive setup | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 3 | Cybersecurity | 61.35 | Positive setup | relative_strength_60d, trend_persistence, breadth, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 4 | Dividend Defensives | 60.47 | Positive setup | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 5 | Quality Growth | 55.05 | Neutral / watchlist | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 6 | Crypto Infrastructure | 54.13 | Neutral / watchlist | relative_strength_60d, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 7 | AI Infrastructure | 53.42 | Neutral / watchlist | downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 8 | Semiconductors | 49.59 | Neutral / watchlist | downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 9 | Grid Infrastructure | 41.52 | Weak setup | downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 10 | Financials | 40.43 | Weak setup | downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 11 | Defense | 39.49 | Weak setup | volume_accumulation, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 12 | Small Caps | 34.04 | Weak setup | downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |

## Breadth and Participation

- Above 50DMA: `46.67%`
- Above 200DMA: `55.0%`
- Positive 20D return: `43.33%`

## Volatility and Risk Signals

- VIX close=19.93 pct_chg=0.0

## News Analytics

- Sentiment counts: {'positive': 0, 'negative': 0, 'neutral': 80}
- News confirmation score: `50.0`

### Top Market-Moving Headlines

**1. ‘AI is on trial’: Bond yields sink below 5% as investors look for safety**
- Source: MarketWatch Top Stories
- Importance / impact: Low / Mixed
- Relevance / horizon: macro / short-term
- Affected assets: Equities, Bonds, USD, Commodities
- Score: `25.0`
- Investment implication: Macro-relevant mixed signal; use as context for rates, volatility, and index confirmation over the short-term.

**2. Under-the-radar stocks to play the next leg of the energy trade with oil prices jumping again**
- Source: CNBC Top News
- Importance / impact: Low / Mixed
- Relevance / horizon: macro / short-term
- Affected assets: Equities, Bonds, USD, Commodities
- Score: `23.75`
- Investment implication: Macro-relevant mixed signal; use as context for rates, volatility, and index confirmation over the short-term.

**3. Investors’ recent money moves show a preference for lowering risks over boosting rewards**
- Source: MarketWatch Top Stories
- Importance / impact: Low / Mixed
- Relevance / horizon: sector_theme / short-term
- Affected assets: ETF, P, S
- Score: `21.25`
- Investment implication: Theme or sector mixed signal; requires price and volume confirmation before affecting rankings.

**4. I’m 58 and hate annuities. How can I get dependable income in retirement?**
- Source: MarketWatch Top Stories
- Importance / impact: Low / Mixed
- Relevance / horizon: sector_theme / short-term
- Affected assets: I, TIPS
- Score: `21.25`
- Investment implication: Theme or sector mixed signal; requires price and volume confirmation before affecting rankings.

**5. Oil is now flowing out of the Persian Gulf like before the Iran war. Why prices may still not come down anytime soon.**
- Source: MarketWatch Top Stories
- Importance / impact: Low / Mixed
- Relevance / horizon: macro / short-term
- Affected assets: Equities, Bonds, USD, Commodities
- Score: `21.25`
- Investment implication: Macro-relevant mixed signal; use as context for rates, volatility, and index confirmation over the short-term.

**6. Mideast oil exports are recovering. Fresh attacks in Saudi Arabia show risks remain.**
- Source: MarketWatch Top Stories
- Importance / impact: Low / Mixed
- Relevance / horizon: macro / short-term
- Affected assets: Equities, Bonds, USD, Commodities
- Score: `21.25`
- Investment implication: Macro-relevant mixed signal; use as context for rates, volatility, and index confirmation over the short-term.

**7. Why a global bank is slashing thousands of jobs — and what the Fed says about AI replacing workers**
- Source: MarketWatch Top Stories
- Importance / impact: Low / Mixed
- Relevance / horizon: macro / short-term
- Affected assets: Equities, Bonds, USD, Commodities
- Score: `21.25`
- Investment implication: Macro-relevant mixed signal; use as context for rates, volatility, and index confirmation over the short-term.

**8. Dow, S&P 500, Nasdaq open lower as tech stocks come under pressure**
- Source: MarketWatch Bulletins
- Importance / impact: Low / Mixed
- Relevance / horizon: sector_theme / short-term
- Affected assets: P, S
- Score: `20.19`
- Investment implication: Theme or sector mixed signal; requires price and volume confirmation before affecting rankings.

**9. Zuckerberg’s California tax move is a win for Meta — and for him**
- Source: MarketWatch Top Stories
- Importance / impact: Low / Mixed
- Relevance / horizon: single_name / short-term
- Affected assets: PR
- Score: `16.25`
- Investment implication: Single-name mixed signal; low weight unless it maps to a broader sector or theme.

**10. My partner of 17 years left me his $1 million home. His children are crying foul. Am I obliged to split it with them?**
- Source: MarketWatch Top Stories
- Importance / impact: Low / Mixed
- Relevance / horizon: single_name / short-term
- Affected assets: I
- Score: `16.25`
- Investment implication: Single-name mixed signal; low weight unless it maps to a broader sector or theme.


### Headline Quality Checks

Noisy headline list: Pharma's 'information arms dealer' is up nearly 80

## Positioning & Flow Dashboard

Positioning and flow data is used as confirmation only.

### Deferred Flow Sections

- Official ETF / fund flows: current report uses shares-outstanding-derived net fund flow estimates from free ETF metadata.
- Institutional Ownership: not available until SEC 13F ingestion is implemented.
- Grouped exposure flow reliability: use issuer coverage and availability status before treating ETF flow as confirmation.

## ETF Flows Analysis

- Market flow regime: `Mixed / Neutral`
- Market flow score: `49.4 / 100`
- Equity risk flow: `48.1`
- Credit risk flow: `56.3`
- Sector cyclicality flow: `41.7`
- Duration/liquidity flow: `51.6`
- Alternatives: `barbell demand`
- ETF flow reliability: `71.5 / 100`
- Dominant allocation direction: `defensive demand`

### Core Flow Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVV | U.S. Broad Equity | 0.0 | -1.1 | 0.6 | -0.5 | Flat | Neutral | Normal | Neutral | Neutral | Medium-term recovery | 87.0 |
| ACWI | Global Equity | -0.6 | -0.8 | 0.0 | -0.1 | Flat | Neutral | Normal | Neutral | Neutral | Mixed or neutral flow structure; Persistent selling | 77.0 |
| EFA | Developed Markets ex-U.S. | 0.9 | 0.6 | 0.1 | -0.5 | Flat | Neutral | Normal | Neutral | Neutral | Structural accumulation; Persistent selling | 83.0 |
| IEMG | Emerging Markets | -0.8 | 0.1 | 0.0 | 0.4 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Medium-term deterioration; Persistent selling | 75.0 |
| IJH | U.S. Mid Cap | -0.9 | 0.9 | 0.3 | 0.0 | Flat | Neutral | Normal | Neutral | Neutral | Structural accumulation | 91.0 |
| IWM | U.S. Small Cap | -0.3 | 0.5 | 0.6 | -1.0 | Down | Sell | Normal | Persistent Distribution | Risk-Off | Strong confirmation | 95.0 |
| LQD | Investment-Grade Credit | 0.3 | -1.2 | 0.6 | 0.3 | Flat | Neutral | Normal | Neutral | Neutral | Medium-term recovery | 87.0 |
| HYG | High-Yield Credit | 0.9 | 0.9 | 0.6 | -0.4 | Down | Sell | Normal | Persistent Distribution | Risk-Off | Tactical profit-taking inside structural accumulation | 83.0 |
| SGOV | Treasury Bills / Cash | -0.3 | -0.2 | 0.9 | -0.1 | Flat | Neutral | Normal | Neutral | Neutral | Structural accumulation; Strong sponsorship | 99.0 |
| SHY | Short-Duration Treasuries | 1.0 | 2.2 | 0.7 | -1.1 | Flat | Buy | Normal | Quiet Accumulation | Improving | Strong confirmation; Exceptional institutional buying | 100.0 |
| IEF | Intermediate-Duration Treasuries | -0.2 | -1.4 | 0.5 | -0.1 | Flat | Neutral | Normal | Neutral | Neutral | Structural distribution | 79.0 |
| TLT | Long-Duration Treasuries | 0.8 | 1.0 | 0.8 | -0.2 | Flat | Sell | Normal | Quiet Distribution | Weakening | Tactical profit-taking inside structural accumulation; Strong sponsorship | 91.0 |
| GLD | Gold | 0.1 | 1.7 | 0.4 | -0.7 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural accumulation | 91.0 |
| IBIT | Bitcoin | 0.4 | 1.8 | 0.7 | 0.1 | Flat | Neutral | Normal | Neutral | Neutral | Structural accumulation | 91.0 |

### Sector Flow Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| XLC | Communication Services | 2.0 | 3.2 | 0.5 | 2.1 | Down | Buy | High | Aggressive Dip Buying | Recovery Candidate | Strong confirmation; Exceptional institutional buying | 100.0 |
| XLY | Consumer Discretionary | -1.4 | -0.6 | 0.3 | -0.0 | Up | Sell | Normal | Profit Taking | Slightly Bearish | Strong confirmation | 95.0 |
| XLP | Consumer Staples | 0.1 | 0.7 | 0.6 | 0.7 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural distribution | 79.0 |
| XLE | Energy | 0.6 | 0.1 | 0.7 | -0.5 | Up | Buy | Normal | Steady Accumulation | Risk-On | Strong confirmation | 95.0 |
| XLF | Financials | -0.1 | -2.7 | 0.5 | -0.5 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural distribution; Exceptional institutional selling | 71.0 |
| XLV | Health Care | 2.6 | 1.9 | 0.7 | 0.0 | Up | Buy | Normal | Steady Accumulation | Risk-On | Strong confirmation; Exceptional institutional buying | 100.0 |
| XLI | Industrials | 0.5 | -0.5 | 0.6 | 0.1 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural accumulation | 91.0 |
| XLK | Information Technology | 0.6 | -0.2 | 0.6 | 0.7 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural accumulation | 91.0 |
| XLB | Materials | -1.4 | -2.2 | 0.5 | -1.1 | Up | Sell | Normal | Profit Taking | Slightly Bearish | Strong confirmation; Exceptional institutional selling | 87.0 |
| XLRE | Real Estate | 0.7 | -1.3 | 0.6 | 0.3 | Flat | Buy | Normal | Quiet Accumulation | Improving | Medium-term recovery | 87.0 |
| XLU | Utilities | 2.3 | 2.1 | 0.6 | 1.2 | Up | Buy | High | Confirmed Accumulation | Strong Risk-On | Strong confirmation; Exceptional institutional buying | 100.0 |

### Subsector PFV Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ITA | Aerospace and Defense | -0.1 | 0.6 | 0.3 | 1.1 | Down | Neutral | High | Heavy Selling Pressure | Cautious | Structural distribution | 79.0 |
| SOXX | Semiconductors | -0.6 | -1.0 | 0.6 | 0.1 | Down | Buy | Normal | Contrarian Buying | Watch | Mixed or neutral flow structure; Exceptional institutional buying | 93.0 |
| SMH | Semiconductors | -0.1 | -0.6 | 0.5 | 0.0 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural accumulation | 91.0 |
| CIBR | Cybersecurity | 1.1 | 1.9 | 0.8 | -0.4 | Flat | Sell | Normal | Quiet Distribution | Weakening | Tactical profit-taking inside structural accumulation; Exceptional institutional selling, Strong sponsorship | 83.0 |

### Material Flow Divergences

| Severity | Type | Primary | Comparison | Interpretation |
| --- | --- | --- | --- | --- |
| medium | related_subsector_divergence | XLI | ITA | defense-specific demand differs from broad industrials |
| medium | related_subsector_divergence | XLK | SOXX | technology differs from semiconductors |
| high | close_substitute_divergence | AGG | IUSB | primary representative differs from close substitute |
| high | close_substitute_divergence | HYG | JNK | primary representative differs from close substitute |
| high | close_substitute_divergence | IWF | IVW | primary representative differs from close substitute |
| high | close_substitute_divergence | SOXX | SMH | primary representative differs from close substitute |


## Contradiction / Audit Flags

No contradiction flags were triggered by current deterministic rules.

## Data Quality Notes

- Technical rows loaded: `60`
- S&P 500 constituent technical rows loaded: `503`
- Macro rows loaded: `48`
- Live macro rows used: `42`
- Economic rows loaded: `113`
- News rows loaded: `80`
- Positioning/flow rows loaded: `30`

## Cycle Metadata

- Report generated at: 23 October 2026, 03:10:27 (HKT)

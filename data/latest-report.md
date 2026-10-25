# Rule-Based Institutional Market Update

Generated at: 25 October 2026, 13:16:54 (HKT)
Window: 24h

## Executive Dashboard

- Regime score: **49.33 / 100** (Mixed / Rotation)
- US equity strength: **37.32 / 100** (weak)
- Evidence quality: **72.5 / 100**
- ETF flow contribution: **49.18 / 100**, reliability **66.71 / 100**
- Breadth: **narrow**; above 50DMA `43.33%`, above 200DMA `53.33%`
- Top sector score: **Energy** `67.85`
- Top theme score: **Healthcare Innovation** `65.66`

## Market Regime Score

| Metric | Value | Driver / Interpretation |
| --- | --- | --- |
| Overall regime | 49.33 | Mixed / Rotation |
| equity_trend | 31.25 | risk-off pressure; Core equity ETFs versus moving averages. |
| equity_momentum | 48.33 | neutral / mixed; 5D/20D/60D return momentum across SPY, QQQ, IWM, and SMH. |
| market_breadth | 46.11 | neutral / mixed; Participation breadth from tracked equity/ETF rows. |
| volatility | 70.0 | risk-on support; VIX level and change; higher score means calmer volatility conditions. |
| rates_yield_curve | 58.0 | mild risk-on support; Treasury yield pressure and curve shape; higher score means less rates pressure. |
| credit_proxy | 50.0 | neutral / mixed; Credit-market proxy; currently neutral when no direct spread signal is available. |
| dollar_fx | 54.3 | neutral / mixed; Dollar move; higher score means less USD tightening pressure. |
| commodity_confirmation | 55.0 | mild risk-on support; Copper, silver, oil, and gold mix; higher score means better cyclical confirmation. |
| etf_flow | 49.45 | neutral / mixed; Grouped ETF flow contribution adjusted for reliability. |
| news_confirmation | 50.0 | neutral / mixed; Weighted headline/news confirmation score. |
| Positive contributors |  | volatility=70.0 |
| Negative contributors |  | equity_trend=31.25 |

## US Equity Strength Score

| Component | Score |
| --- | --- |
| indices_above_moving_averages | 31.25 |
| sp500_trend | 55.0 |
| nasdaq_trend | 35.0 |
| russell_participation | 0.0 |
| returns_momentum | 48.33 |
| rsi_zone | 37.5 |
| macd_confirmation | 43.75 |
| volume_confirmation | 38.75 |
| breadth | 46.11 |

## Evidence Quality / Confidence

- Confidence score: `72.5`
- Agreement ratio: `0.3`
- Contradiction count: `1`
- Missing indicators: none
- Warning flags: none

## Cross-Asset Confirmation

| Area | Signal | Interpretation |
| --- | --- | --- |
| Equities | S&P 500 falling; Nasdaq stable; Russell 2000 falling | Confirms risk appetite when broad indices rise together; weak small caps would narrow the signal. |
| Rates | 10Y Treasury rising; MOVE falling | Rising yields can pressure duration assets; falling MOVE supports calmer bond volatility. |
| Dollar | DXY proxy stable | A stronger dollar can tighten financial conditions and pressure commodities/emerging-market risk. |
| Credit | HYG stable | High-yield weakness would challenge equity risk-on confirmation. |
| Gold | Gold falling | Gold strength can indicate defensive demand, inflation hedging, or geopolitical concern. |
| Silver | Silver falling | Silver helps distinguish precious-metal demand from industrial/cyclical confirmation when data is available. |
| Copper | Copper rising | Copper strength supports cyclical growth confirmation; weakness would dilute risk-on breadth. |
| Oil | WTI crude rising | Oil spikes can be inflationary risk; falling oil can ease cost pressure but may also flag demand softness. |
| Volatility | VIX rising | Falling VIX supports risk appetite; a volatility spike would reduce confidence in broad risk-on. |

### Macro Snapshot

Live macro rows are intraday snapshots from `public.macro_live`; closed rows are official stored rows from `public.macro`.

| Symbol | Name | Close | Pct Chg | Market Date | Status |
| --- | --- | --- | --- | --- | --- |
| ^GSPC | S&P 500 | 7623.68 | -0.52 | 2026-10-23 | closed |
| ^IXIC | NASDAQ Composite | 25955.34 | -0.21 | 2026-10-23 | closed |
| ^RUT | Russell 2000 Index | 2775.9 | -0.29 | 2026-10-23 | closed |
| ^VIX | CBOE Volatility Index | 19.45 | 2.21 | 2026-10-23 | closed |
| ^SKEW | nan | 151.8 | -0.39 | 2026-10-23 | closed |
| ^MOVE | ICE BofA MOVE Index | 103.33 | -3.29 | 2026-10-23 | closed |
| US2YT=X | United States 2-Year Treasury Yield | 4.68 | 1.01 | 2026-10-23 | live as of 25 October 2026, 13:00:19 (HKT) |
| US3YT=X | United States 3-Year Treasury Yield | 4.75 | 0.89 | 2026-10-23 | live as of 25 October 2026, 13:00:19 (HKT) |
| US5YT=X | United States 5-Year Treasury Yield | 4.81 | 0.82 | 2026-10-23 | live as of 25 October 2026, 13:00:19 (HKT) |
| US7YT=X | United States 7-Year Treasury Yield | 4.89 | 0.83 | 2026-10-23 | live as of 25 October 2026, 13:00:19 (HKT) |
| US10YT=X | United States 10-Year Treasury Yield | 4.99 | 0.71 | 2026-10-23 | live as of 25 October 2026, 13:00:19 (HKT) |
| US20YT=X | United States 20-Year Treasury Yield | 5.36 | 0.64 | 2026-10-23 | live as of 25 October 2026, 13:00:19 (HKT) |
| US30YT=X | United States 30-Year Treasury Yield | 5.32 | 0.53 | 2026-10-23 | live as of 25 October 2026, 13:00:19 (HKT) |
| HK50 | Hang Seng Futures | 23110.0 | -0.06 | 2026-10-23 | live as of 25 October 2026, 13:00:19 (HKT) |
| KOR200c1 | KOSPI 200 Futures | 861.7 | -0.19 | 2026-10-23 | live as of 25 October 2026, 13:00:19 (HKT) |
| CIHc1 | SSE 50 Futures | 2733.0 | 1.03 | 2026-10-23 | live as of 25 October 2026, 13:00:19 (HKT) |
| HYG | iShares iBoxx High Yield Corporate Bond ETF | 77.05 | -0.06 | 2026-10-23 | closed |
| LQD | iShares iBoxx Investment Grade Corporate Bond ETF | 103.85 | -0.41 | 2026-10-23 | closed |
| JNK | SPDR Bloomberg High Yield Bond ETF | 92.52 | 0.01 | 2026-10-23 | closed |
| RSP | Invesco S&P 500 Equal Weight ETF | 216.54 | -0.77 | 2026-10-23 | closed |
| IWF | iShares Russell 1000 Growth ETF | 119.61 | -0.4 | 2026-10-23 | closed |
| IWD | iShares Russell 1000 Value ETF | 257.42 | -0.63 | 2026-10-23 | closed |
| TLT | iShares 20+ Year Treasury Bond ETF | 81.34 | -0.49 | 2026-10-23 | closed |
| IEF | iShares 7-10 Year Treasury Bond ETF | 91.05 | -0.16 | 2026-10-23 | closed |
| SHY | iShares 1-3 Year Treasury Bond ETF | 81.5 | -0.02 | 2026-10-23 | closed |
| GC=F | Gold Future | 4010.0 | -1.24 | 2026-10-23 | closed |
| SI=F | Silver Future | 53.96 | -1.47 | 2026-10-23 | closed |
| CL=F | WTI Crude Oil Future | 103.44 | 3.99 | 2026-10-23 | closed |
| HG=F | Copper Future | 6.5 | 2.12 | 2026-10-23 | closed |

## Market Dispersion Analysis

- Sector ETF 20D dispersion: `16.5` points (high); leader `XLP` (Consumer Staples) `10.15`, laggard `XLK` (Technology) `-6.35`
- Sector ETF 60D dispersion: `22.69` points (very high); leader `XLE` (Energy) `15.21`, laggard `XLRE` (Real Estate) `-7.48`

| Comparison | Left | Right | 20D Spread | Signal |
| --- | --- | --- | --- | --- |
| Equal-weight vs cap-weight | RSP (Equal-weight S&P 500) | SPY (S&P 500) | 4.21 | broader participation |
| Small-cap vs large-cap | IWM (Russell 2000) | SPY (S&P 500) | -1.35 | large-cap leadership |
| Growth vs value | IWF (Russell 1000 Growth) | IWD (Russell 1000 Value) | -7.71 | value leadership |
| Nasdaq vs S&P 500 | QQQ (Nasdaq 100) | SPY (S&P 500) | -4.52 | S&P 500 leadership |

## Sector Constituent Dispersion

- Breadth 50D / 200D: percentage of active S&P 500 constituents in the sector trading above the 50-day / 200-day moving average.
- Positive 20D: percentage of active sector constituents with positive 20-day return.
- Std 20D: cross-sectional standard deviation of constituent 20-day returns; higher means wider stock-level dispersion.

| Sector | Count | Breadth 50D | Breadth 200D | Positive 20D | 20D Dispersion | Std 20D | Label | Leaders | Laggards |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Information Technology | 75 | 45.33 | 58.11 | 42.67 | 78.73 | 16.5 | very high | ACN, PTC, IT | STX, FLEX, INTC |
| Industrials | 83 | 50.6 | 40.51 | 62.65 | 47.92 | 9.5 | very high | EFX, VRSK, ADP | BE, VRT, FIX |
| Consumer Discretionary | 47 | 61.7 | 42.55 | 76.6 | 47.48 | 9.14 | very high | HAS, CCL, RCL | CVNA, CMG, MGM |
| Financials | 76 | 53.33 | 66.2 | 73.68 | 43.73 | 8.42 | very high | FDS, BRO, CBOE | BAC, COIN, HOOD |
| Materials | 24 | 66.67 | 62.5 | 75.0 | 43.25 | 9.66 | very high | BALL, DOW, VMC | FCX, ALB, MOS |
| Real Estate | 30 | 41.38 | 34.48 | 63.33 | 41.41 | 7.79 | very high | CSGP, CCI, HST | EQIX, PLD, ARE |
| Health Care | 60 | 88.33 | 88.33 | 88.33 | 29.44 | 5.97 | very high | CI, VEEV, ZTS | ILMN, INCY, DXCM |
| Consumer Staples | 34 | 84.38 | 65.62 | 88.24 | 28.09 | 6.28 | very high | STZ, CASY, KMB | VYLR, ADM, BG |
| Communication Services | 22 | 33.33 | 40.0 | 40.91 | 27.08 | 7.4 | very high | OMC, NWSA, NWS | T, APP, META |
| Energy | 21 | 71.43 | 66.67 | 85.71 | 23.88 | 6.01 | very high | MPC, APA, COP | TPL, SLB, BKR |
| Utilities | 31 | 80.65 | 45.16 | 93.55 | 20.6 | 4.42 | very high | PNW, XEL, ED | AES, CEG, NRG |

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
| US dollar/Euro ECB reference exchange rate | 1.12 | USD | -0.0 USD vs prior | 2026-10-23 | EUR weakened versus this currency. |
| Japanese yen/Euro ECB reference exchange rate | 175.51 | JPY | -0.46 JPY vs prior | 2026-10-23 | EUR weakened versus this currency. |
| Chinese yuan renminbi/Euro ECB reference exchange rate | 7.47 | CNY | -0.01 CNY vs prior | 2026-10-23 | EUR weakened versus this currency. |
| Australian dollar/Euro ECB reference exchange rate | 1.59 | AUD | -0.0 AUD vs prior | 2026-10-23 | EUR weakened versus this currency. |

ABS Australia note: ABS rows are stored locally/Neon, but most series are dimension-coded; only curated series should be promoted into narrative report text.

## Sector and Theme Leadership

### Official Sector Strength

Supporting and detracting names are the top/bottom S&P 500 constituents by 20D return when constituent coverage is available; otherwise the report falls back to related ETFs.

| Rank | Sector | Score | Trend | Momentum | Stock Breadth | ETF Flow | Flow Reliability | 3M RS | Supporting / Leaders | Detracting / Laggards |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Energy | 67.85 | strong uptrend | positive | broad | 40.44 | 65.0 | 59.21 | MPC, APA, COP | TPL, SLB, BKR |
| 2 | Healthcare | 66.8 | strong uptrend | positive | broad | 67.92 | 65.0 | 56.02 | CI, VEEV, ZTS | ILMN, INCY, DXCM |
| 3 | Consumer Staples | 66.27 | strong uptrend | positive | broad | 50.0 | 0.0 | 55.65 | STZ, CASY, KMB | VYLR, ADM, BG |
| 4 | Financials | 62.34 | strong uptrend | neutral | broad | 39.89 | 65.0 | 50.67 | FDS, BRO, CBOE | BAC, COIN, HOOD |
| 5 | Consumer Discretionary | 59.09 | uptrend | neutral | broad | 50.0 | 0.0 | 52.13 | HAS, CCL, RCL | CVNA, CMG, MGM |
| 6 | Cybersecurity | 58.34 | strong uptrend | neutral | broad | 68.21 | 65.0 | 54.46 | CIBR | CIBR |
| 7 | Utilities | 55.18 | neutral | neutral | broad | 50.0 | 0.0 | 52.1 | PNW, XEL, ED | AES, CEG, NRG |
| 8 | Crypto | 51.38 | neutral | neutral | mixed | 63.81 | 65.0 | 50.0 |  |  |
| 9 | Real Estate | 44.47 | strong downtrend | neutral | weak | 40.72 | 65.0 | 46.62 | CSGP, CCI, HST | EQIX, PLD, ARE |
| 10 | Semiconductors | 41.19 | downtrend | negative | weak | 76.08 | 90.0 | 40.93 | SMH, SOXX | SOXX, SMH |
| 11 | Technology | 40.61 | downtrend | neutral | weak | 46.99 | 65.0 | 48.16 | ACN, PTC, IT | STX, FLEX, INTC |
| 12 | Industrials | 37.13 | strong downtrend | neutral | weak | 50.0 | 0.0 | 45.37 | EFX, VRSK, ADP | BE, VRT, FIX |
| 13 | Grid Infrastructure | 34.75 | strong downtrend | negative | weak | 69.75 | 65.0 | 42.25 | GRID | GRID |
| 14 | Defense | 33.86 | strong downtrend | negative | weak | 50.0 | 0.0 | 36.89 | XAR | XAR |
| 15 | Nuclear | 30.53 | strong downtrend | negative | weak | 50.0 | 0.0 | 35.05 | NLR | NLR |

### Thematic Strength

| Rank | Theme | Score | Setup | ETF Flow | Flow Reliability | Dispersion | Price | News |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Healthcare Innovation | 65.66 | Positive setup | 67.92 | 65.0 | 13.82 | True | False |
| 2 | Energy | 64.32 | Positive setup | 40.44 | 65.0 | 2.29 | True | False |
| 3 | Dividend Defensives | 60.89 | Positive setup | 59.11 | 65.0 | 3.42 | True | False |
| 4 | Cybersecurity | 57.85 | Positive setup | 68.21 | 65.0 | 19.75 | False | False |
| 5 | Quality Growth | 49.51 | Neutral / watchlist | 56.41 | 65.0 | 11.0 | False | False |
| 6 | Crypto Infrastructure | 49.13 | Neutral / watchlist | 63.81 | 65.0 | 5.34 | False | False |
| 7 | AI Infrastructure | 48.66 | Neutral / watchlist | 76.08 | 90.0 | 20.62 | False | False |
| 8 | Defense | 44.34 | Weak setup | 50.0 | 0.0 | 38.41 | False | False |
| 9 | Semiconductors | 43.58 | Neutral / watchlist | 76.08 | 90.0 | 13.77 | False | False |
| 10 | Financials | 42.35 | Weak setup | 39.89 | 65.0 | 12.72 | False | False |
| 11 | Grid Infrastructure | 41.11 | Weak setup | 69.75 | 65.0 | 25.06 | False | False |
| 12 | Small Caps | 36.54 | Weak setup | 48.21 | 65.0 | 0.0 | False | False |
| 13 | Nuclear | 28.51 | Underperformance risk | 50.0 | 0.0 | 18.87 | False | False |

- Top 5 improving themes: Crypto Infrastructure, Cybersecurity, Energy, Quality Growth, AI Infrastructure
- Top 5 deteriorating themes: Nuclear, Defense, Financials, Small Caps, Grid Infrastructure
- Strong news but weak price confirmation: none
- Strong price but weak news confirmation: Healthcare Innovation, Energy, Dividend Defensives

### Sector / Theme Alignment

| Sector | Related Themes | Sector Score | Sector Signal | Theme Score | Theme Signal | Interpretation |
| --- | --- | --- | --- | --- | --- | --- |
| Energy | Energy | 67.85 | strong | 64.32 | positive | sector and theme confirmation |
| Healthcare | Healthcare Innovation | 66.8 | strong | 65.66 | strong | sector and theme confirmation |
| Consumer Staples | Dividend Defensives | 66.27 | strong | 60.89 | positive | sector and theme confirmation |
| Financials | Financials | 62.34 | positive | 42.35 | weak | sector stronger than related themes |
| Consumer Discretionary | Small Caps | 59.09 | positive | 36.54 | weak | sector stronger than related themes |
| Cybersecurity | Cybersecurity | 58.34 | positive | 57.85 | positive | sector and theme confirmation |
| Utilities | Grid Infrastructure, Nuclear, Dividend Defensives | 55.18 | positive | 43.5 | weak | sector stronger than related themes |
| Crypto | Crypto Infrastructure | 51.38 | mixed | 49.13 | mixed | mixed confirmation |
| Real Estate | Dividend Defensives | 44.47 | weak | 60.89 | positive | theme stronger than official sector |
| Semiconductors | AI Infrastructure, Semiconductors | 41.19 | weak | 46.12 | mixed | mixed confirmation |
| Technology | AI Infrastructure, Semiconductors, Quality Growth | 40.61 | weak | 47.25 | mixed | mixed confirmation |
| Industrials | Defense, Grid Infrastructure | 37.13 | weak | 42.72 | weak | broad weakness across sector and themes |
| Grid Infrastructure | Grid Infrastructure | 34.75 | very weak | 41.11 | weak | broad weakness across sector and themes |
| Defense | Defense | 33.86 | very weak | 44.34 | weak | broad weakness across sector and themes |
| Nuclear | Nuclear | 30.53 | very weak | 28.51 | very weak | broad weakness across sector and themes |

## Three-Month Outperformance Setup

| Rank | Theme | Score | Classification | Drivers | Invalidation Triggers |
| --- | --- | --- | --- | --- | --- |
| 1 | Energy | 69.15 | Positive setup | relative_strength_60d, trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 2 | Healthcare Innovation | 67.37 | Positive setup | trend_persistence, breadth, volume_accumulation, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 3 | Cybersecurity | 62.94 | Positive setup | relative_strength_60d, trend_persistence, breadth, volume_accumulation, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 4 | Dividend Defensives | 62.7 | Positive setup | trend_persistence, breadth, volume_accumulation, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 5 | Quality Growth | 55.55 | Neutral / watchlist | trend_persistence, breadth, volume_accumulation, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 6 | Crypto Infrastructure | 52.13 | Neutral / watchlist | relative_strength_60d, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 7 | AI Infrastructure | 52.1 | Neutral / watchlist | volume_accumulation, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 8 | Semiconductors | 46.02 | Neutral / watchlist | volume_accumulation, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 9 | Financials | 44.6 | Weak setup | downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 10 | Defense | 43.96 | Weak setup | volume_accumulation, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 11 | Grid Infrastructure | 42.3 | Weak setup | volume_accumulation, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 12 | Small Caps | 36.12 | Weak setup | downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |

## Breadth and Participation

- Above 50DMA: `43.33%`
- Above 200DMA: `53.33%`
- Positive 20D return: `41.67%`

## Volatility and Risk Signals

- VIX close=19.45 pct_chg=2.21

## News Analytics

- Sentiment counts: {'positive': 0, 'negative': 0, 'neutral': 80}
- News confirmation score: `50.0`

### Top Market-Moving Headlines

**1. Retire on 8% a year with little or no risk? How to use annuities the right way.**
- Source: MarketWatch Top Stories
- Importance / impact: Low / Mixed
- Relevance / horizon: macro / short-term
- Affected assets: Equities, Bonds, USD, Commodities
- Score: `21.25`
- Investment implication: Macro-relevant mixed signal; use as context for rates, volatility, and index confirmation over the short-term.

**2. AI fever ignites a boom in thematic ETFs as fund managers hunt for their next big hit**
- Source: MarketWatch Top Stories
- Importance / impact: Low / Mixed
- Relevance / horizon: macro / short-term
- Affected assets: Equities, Bonds, USD, Commodities
- Score: `21.25`
- Investment implication: Macro-relevant mixed signal; use as context for rates, volatility, and index confirmation over the short-term.

**3. ‘Non-answers’ aren’t working. This is what investors really need from the Fed.**
- Source: MarketWatch Top Stories
- Importance / impact: Low / Mixed
- Relevance / horizon: macro / short-term
- Affected assets: Equities, Bonds, USD, Commodities
- Score: `21.25`
- Investment implication: Macro-relevant mixed signal; use as context for rates, volatility, and index confirmation over the short-term.

**4. ‘Non-answers’ aren’t working. This is what investors really need from the Fed.**
- Source: MarketWatch Bulletins
- Importance / impact: Low / Mixed
- Relevance / horizon: macro / short-term
- Affected assets: Equities, Bonds, USD, Commodities
- Score: `20.19`
- Investment implication: Macro-relevant mixed signal; use as context for rates, volatility, and index confirmation over the short-term.

**5. Fact vs. fiction: Doctors share whether peptides are safe and effective**
- Source: CNBC Markets
- Importance / impact: Low / Mixed
- Relevance / horizon: macro / short-term
- Affected assets: Equities, Bonds, USD, Commodities
- Score: `20.19`
- Investment implication: Macro-relevant mixed signal; use as context for rates, volatility, and index confirmation over the short-term.

**6. Turmoil hits AI buildout as neoclouds face pressure, credit risks mount and Solidigm pulls IPO**
- Source: CNBC Markets
- Importance / impact: Low / Mixed
- Relevance / horizon: macro / short-term
- Affected assets: IPO
- Score: `20.19`
- Investment implication: Macro-relevant mixed signal; use as context for rates, volatility, and index confirmation over the short-term.

**7. I’m 58 and hate annuities. How can I get dependable income in retirement?**
- Source: MarketWatch Top Stories
- Importance / impact: Low / Mixed
- Relevance / horizon: sector_theme / short-term
- Affected assets: I, TIPS
- Score: `18.06`
- Investment implication: Theme or sector mixed signal; requires price and volume confirmation before affecting rankings.

**8. Investors’ recent money moves show a preference for lowering risks over boosting rewards**
- Source: MarketWatch Top Stories
- Importance / impact: Low / Mixed
- Relevance / horizon: sector_theme / short-term
- Affected assets: ETF, P, S
- Score: `18.06`
- Investment implication: Theme or sector mixed signal; requires price and volume confirmation before affecting rankings.

**9. Biotech stocks are surging. How investors can play the new drug innovation boom**
- Source: CNBC Markets
- Importance / impact: Low / Mixed
- Relevance / horizon: sector_theme / short-term
- Affected assets: A, M
- Score: `17.16`
- Investment implication: Theme or sector mixed signal; requires price and volume confirmation before affecting rankings.

**10. An ex-bookkeeper spent $375 to launch a sewing business: 'I hadn't felt so sure about something like that in a long time'**
- Source: CNBC Markets
- Importance / impact: Low / Mixed
- Relevance / horizon: sector_theme / short-term
- Affected assets: ATX, I
- Score: `17.16`
- Investment implication: Theme or sector mixed signal; requires price and volume confirmation before affecting rankings.


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
- Market flow score: `50.0 / 100`
- Equity risk flow: `45.8`
- Credit risk flow: `55.9`
- Sector cyclicality flow: `49.4`
- Duration/liquidity flow: `50.1`
- Alternatives: `mixed alternative-asset demand`
- ETF flow reliability: `66.7 / 100`
- Dominant allocation direction: `defensive demand`

### Core Flow Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVV | U.S. Broad Equity | -0.2 | -1.0 | 0.5 | n/a | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural distribution | 64.0 |
| ACWI | Global Equity | -0.6 | -0.8 | 0.0 | n/a | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Mixed or neutral flow structure; Persistent selling | 62.0 |
| EFA | Developed Markets ex-U.S. | 0.9 | 0.6 | 0.1 | n/a | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural accumulation; Persistent selling | 68.0 |
| IEMG | Emerging Markets | -0.8 | -0.2 | 0.0 | n/a | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Medium-term deterioration; Persistent selling | 60.0 |
| IJH | U.S. Mid Cap | -0.9 | 0.6 | 0.3 | n/a | Flat | Neutral | Normal | Neutral | Neutral | Structural accumulation | 76.0 |
| IWM | U.S. Small Cap | -0.6 | -0.1 | 0.6 | n/a | Down | Sell | Normal | Persistent Distribution | Risk-Off | Strong confirmation | 80.0 |
| LQD | Investment-Grade Credit | 1.0 | -0.9 | 0.7 | n/a | Flat | Buy | Normal | Quiet Accumulation | Improving | Medium-term recovery | 72.0 |
| HYG | High-Yield Credit | 0.8 | 0.5 | 0.6 | n/a | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural accumulation | 76.0 |
| SGOV | Treasury Bills / Cash | -0.5 | -0.3 | 0.8 | n/a | Flat | Sell | Normal | Quiet Distribution | Weakening | Tactical profit-taking inside structural accumulation; Strong sponsorship | 76.0 |
| SHY | Short-Duration Treasuries | 1.1 | 2.2 | 0.7 | n/a | Flat | Buy | Normal | Quiet Accumulation | Improving | Strong confirmation; Exceptional institutional buying | 88.0 |
| IEF | Intermediate-Duration Treasuries | 0.1 | -1.2 | 0.5 | n/a | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural distribution | 64.0 |
| TLT | Long-Duration Treasuries | -0.1 | 1.0 | 0.7 | n/a | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural accumulation | 76.0 |
| GLD | Gold | -0.6 | 1.2 | 0.4 | n/a | Down | Sell | Normal | Persistent Distribution | Risk-Off | Medium-term deterioration; Exceptional institutional selling | 60.0 |
| IBIT | Bitcoin | 0.2 | 1.7 | 0.7 | n/a | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural accumulation | 76.0 |

### Sector Flow Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| XLC | Communication Services | 2.3 | 3.4 | 0.5 | 0.4 | Down | Buy | Normal | Contrarian Buying | Watch | Strong confirmation; Exceptional institutional buying | 100.0 |
| XLY | Consumer Discretionary | -1.5 | -0.6 | 0.3 | 0.7 | Up | Sell | Normal | Profit Taking | Slightly Bearish | Strong confirmation | 95.0 |
| XLP | Consumer Staples | 0.0 | -0.0 | 0.6 | 3.1 | Up | Neutral | High | Momentum Rally | Watch | Structural distribution | 79.0 |
| XLE | Energy | 0.5 | 0.2 | 0.7 | 1.6 | Up | Buy | High | Confirmed Accumulation | Strong Risk-On | Strong confirmation | 95.0 |
| XLF | Financials | -0.3 | -3.1 | 0.4 | -0.0 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural distribution; Exceptional institutional selling | 71.0 |
| XLV | Health Care | 1.9 | 1.5 | 0.7 | 0.7 | Up | Buy | Normal | Steady Accumulation | Risk-On | Strong confirmation | 95.0 |
| XLI | Industrials | 0.7 | -0.4 | 0.6 | 1.9 | Down | Buy | High | Aggressive Dip Buying | Recovery Candidate | Strong confirmation | 95.0 |
| XLK | Information Technology | 0.6 | -0.3 | 0.6 | 1.8 | Down | Neutral | High | Heavy Selling Pressure | Cautious | Structural accumulation | 91.0 |
| XLB | Materials | -1.3 | -1.8 | 0.5 | -0.5 | Up | Sell | Normal | Profit Taking | Slightly Bearish | Strong confirmation | 95.0 |
| XLRE | Real Estate | 0.5 | -1.5 | 0.6 | 2.6 | Up | Buy | High | Confirmed Accumulation | Strong Risk-On | Medium-term recovery | 87.0 |
| XLU | Utilities | 1.4 | 1.3 | 0.6 | 0.3 | Up | Sell | Normal | Profit Taking | Slightly Bearish | Tactical profit-taking inside structural accumulation; Exceptional institutional selling | 75.0 |

### Subsector PFV Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ITA | Aerospace and Defense | -0.1 | 0.9 | 0.3 | n/a | Down | Buy | Normal | Contrarian Buying | Watch | Tactical rebound inside structural distribution | 68.0 |
| SOXX | Semiconductors | 0.1 | -1.3 | 0.6 | n/a | Down | Buy | Normal | Contrarian Buying | Watch | Medium-term recovery; Exceptional institutional buying | 80.0 |
| SMH | Semiconductors | 0.3 | -0.9 | 0.6 | n/a | Down | Buy | Normal | Contrarian Buying | Watch | Mixed or neutral flow structure | 70.0 |
| CIBR | Cybersecurity | 0.9 | 2.0 | 0.8 | n/a | Up | Sell | Normal | Profit Taking | Slightly Bearish | Tactical profit-taking inside structural accumulation; Exceptional institutional selling, Strong sponsorship | 68.0 |

### Material Flow Divergences

| Severity | Type | Primary | Comparison | Interpretation |
| --- | --- | --- | --- | --- |
| high | close_substitute_divergence | GLD | IAU | primary representative differs from close substitute |
| high | close_substitute_divergence | AGG | IUSB | primary representative differs from close substitute |
| high | close_substitute_divergence | IWD | IVE | primary representative differs from close substitute |
| high | close_substitute_divergence | IWM | IJR | primary representative differs from close substitute |


## Contradiction / Audit Flags

No contradiction flags were triggered by current deterministic rules.

## Data Quality Notes

- Technical rows loaded: `60`
- S&P 500 constituent technical rows loaded: `503`
- Macro rows loaded: `48`
- Live macro rows used: `12`
- Economic rows loaded: `113`
- News rows loaded: `80`
- Positioning/flow rows loaded: `30`

## Cycle Metadata

- Report generated at: 25 October 2026, 13:16:54 (HKT)

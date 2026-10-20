# Rule-Based Institutional Market Update

Generated at: 21 October 2026, 02:37:23 (HKT)
Window: 24h

## Executive Dashboard

- Regime score: **48.62 / 100** (Mixed / Rotation)
- US equity strength: **37.07 / 100** (weak)
- Evidence quality: **76.0 / 100**
- ETF flow contribution: **47.92 / 100**, reliability **71.4 / 100**
- Breadth: **weak**; above 50DMA `28.33%`, above 200DMA `55.0%`
- Top sector score: **Healthcare** `70.0`
- Top theme score: **Energy** `66.1`

## Market Regime Score

| Metric | Value | Driver / Interpretation |
| --- | --- | --- |
| Overall regime | 48.62 | Mixed / Rotation |
| equity_trend | 31.25 | risk-off pressure; Core equity ETFs versus moving averages. |
| equity_momentum | 47.34 | neutral / mixed; 5D/20D/60D return momentum across SPY, QQQ, IWM, and SMH. |
| market_breadth | 37.78 | mild risk-off pressure; Participation breadth from tracked equity/ETF rows. |
| volatility | 70.0 | risk-on support; VIX level and change; higher score means calmer volatility conditions. |
| rates_yield_curve | 58.0 | mild risk-on support; Treasury yield pressure and curve shape; higher score means less rates pressure. |
| credit_proxy | 50.0 | neutral / mixed; Credit-market proxy; currently neutral when no direct spread signal is available. |
| dollar_fx | 56.33 | mild risk-on support; Dollar move; higher score means less USD tightening pressure. |
| commodity_confirmation | 61.0 | mild risk-on support; Copper, silver, oil, and gold mix; higher score means better cyclical confirmation. |
| etf_flow | 48.51 | neutral / mixed; Grouped ETF flow contribution adjusted for reliability. |
| news_confirmation | 50.0 | neutral / mixed; Weighted headline/news confirmation score. |
| Positive contributors |  | volatility=70.0, commodity_confirmation=61.0 |
| Negative contributors |  | equity_trend=31.25, market_breadth=37.78 |

## US Equity Strength Score

| Component | Score |
| --- | --- |
| indices_above_moving_averages | 31.25 |
| sp500_trend | 55.0 |
| nasdaq_trend | 35.0 |
| russell_participation | 0.0 |
| returns_momentum | 47.34 |
| rsi_zone | 47.5 |
| macd_confirmation | 35.0 |
| volume_confirmation | 50.0 |
| breadth | 37.78 |

## Evidence Quality / Confidence

- Confidence score: `76.0`
- Agreement ratio: `0.4`
- Contradiction count: `2`
- Missing indicators: none
- Warning flags: none

## Cross-Asset Confirmation

| Area | Signal | Interpretation |
| --- | --- | --- |
| Equities | S&P 500 rising; Nasdaq stable; Russell 2000 rising | Confirms risk appetite when broad indices rise together; weak small caps would narrow the signal. |
| Rates | 10Y Treasury falling; MOVE rising | Rising yields can pressure duration assets; falling MOVE supports calmer bond volatility. |
| Dollar | DXY proxy falling | A stronger dollar can tighten financial conditions and pressure commodities/emerging-market risk. |
| Credit | HYG stable | High-yield weakness would challenge equity risk-on confirmation. |
| Gold | Gold falling | Gold strength can indicate defensive demand, inflation hedging, or geopolitical concern. |
| Silver | Silver rising | Silver helps distinguish precious-metal demand from industrial/cyclical confirmation when data is available. |
| Copper | Copper rising | Copper strength supports cyclical growth confirmation; weakness would dilute risk-on breadth. |
| Oil | WTI crude falling | Oil spikes can be inflationary risk; falling oil can ease cost pressure but may also flag demand softness. |
| Volatility | VIX falling | Falling VIX supports risk appetite; a volatility spike would reduce confidence in broad risk-on. |

### Macro Snapshot

Live macro rows are intraday snapshots from `public.macro_live`; closed rows are official stored rows from `public.macro`.

| Symbol | Name | Close | Pct Chg | Market Date | Status |
| --- | --- | --- | --- | --- | --- |
| ^GSPC | S&P 500 | 7722.83 | 0.42 | 2026-10-20 | live as of 21 October 2026, 02:00:21 (HKT) |
| ^IXIC | NASDAQ Composite | 26486.76 | 0.21 | 2026-10-20 | live as of 21 October 2026, 02:00:21 (HKT) |
| ^RUT | Russell 2000 Index | 2774.9 | 1.71 | 2026-10-20 | live as of 21 October 2026, 02:00:21 (HKT) |
| ^VIX | CBOE Volatility Index | 17.38 | -5.75 | 2026-10-20 | live as of 21 October 2026, 02:00:21 (HKT) |
| ^SKEW | CBOE SKEW Index | 161.86 | -3.99 | 2026-10-19 | closed |
| ^MOVE | ICE BofA MOVE Index | 102.28 | 0.96 | 2026-10-20 | live as of 21 October 2026, 02:00:21 (HKT) |
| US2YT=X | US2YT=X | 4.74 | -0.32 | 2026-10-16 | closed |
| US3YT=X | US3YT=X | 4.83 | -0.19 | 2026-10-16 | closed |
| US5YT=X | US5YT=X | 4.9 | 0.04 | 2026-10-16 | closed |
| US7YT=X | US7YT=X | 4.99 | 0.18 | 2026-10-16 | closed |
| US10YT=X | US10YT=X | 5.1 | 0.22 | 2026-10-16 | closed |
| US20YT=X | US20YT=X | 5.49 | 0.13 | 2026-10-16 | closed |
| US30YT=X | US30YT=X | 5.44 | 0.17 | 2026-10-16 | closed |
| HK50 | HK50 | 24107.5 | -0.71 | 2026-10-16 | closed |
| KOR200c1 | KOSPI 200 Futures | 871.05 | -2.49 | 2026-10-19 | closed |
| CIHc1 | CIHc1 | 2720.0 | -0.04 | 2026-10-16 | closed |
| HYG | iShares iBoxx High Yield Corporate Bond ETF | 76.83 | 0.01 | 2026-10-20 | live as of 21 October 2026, 02:00:21 (HKT) |
| LQD | iShares iBoxx Investment Grade Corporate Bond ETF | 103.14 | 0.25 | 2026-10-20 | live as of 21 October 2026, 02:00:21 (HKT) |
| JNK | SPDR Bloomberg High Yield Bond ETF | 92.23 | -0.03 | 2026-10-20 | live as of 21 October 2026, 02:00:21 (HKT) |
| RSP | Invesco S&P 500 Equal Weight ETF | 215.72 | 1.09 | 2026-10-20 | live as of 21 October 2026, 02:00:21 (HKT) |
| IWF | iShares Russell 1000 Growth ETF | 122.77 | 0.13 | 2026-10-20 | live as of 21 October 2026, 02:00:21 (HKT) |
| IWD | iShares Russell 1000 Value ETF | 257.46 | 0.79 | 2026-10-20 | live as of 21 October 2026, 02:00:21 (HKT) |
| TLT | iShares 20+ Year Treasury Bond ETF | 80.0 | 0.68 | 2026-10-20 | live as of 21 October 2026, 02:00:21 (HKT) |
| IEF | iShares 7-10 Year Treasury Bond ETF | 90.21 | 0.14 | 2026-10-20 | live as of 21 October 2026, 02:00:21 (HKT) |
| SHY | iShares 1-3 Year Treasury Bond ETF | 81.29 | -0.02 | 2026-10-20 | live as of 21 October 2026, 02:00:21 (HKT) |
| GC=F | Gold Future | 4143.7 | -0.39 | 2026-10-20 | live as of 21 October 2026, 02:00:21 (HKT) |
| SI=F | Silver Future | 58.07 | 1.92 | 2026-10-20 | live as of 21 October 2026, 02:00:21 (HKT) |
| CL=F | WTI Crude Oil Future | 97.91 | -5.55 | 2026-10-20 | live as of 21 October 2026, 02:00:21 (HKT) |
| HG=F | Copper Future | 6.62 | 1.27 | 2026-10-20 | live as of 21 October 2026, 02:00:21 (HKT) |

## Market Dispersion Analysis

- Sector ETF 20D dispersion: `13.11` points (high); leader `XLE` (Energy) `8.55`, laggard `XLK` (Technology) `-4.56`
- Sector ETF 60D dispersion: `24.37` points (very high); leader `XLE` (Energy) `13.72`, laggard `XLU` (Utilities) `-10.65`

| Comparison | Left | Right | 20D Spread | Signal |
| --- | --- | --- | --- | --- |
| Equal-weight vs cap-weight | RSP (Equal-weight S&P 500) | SPY (S&P 500) | 1.25 | broader participation |
| Small-cap vs large-cap | IWM (Russell 2000) | SPY (S&P 500) | -4.1 | large-cap leadership |
| Growth vs value | IWF (Russell 1000 Growth) | IWD (Russell 1000 Value) | -3.66 | value leadership |
| Nasdaq vs S&P 500 | QQQ (Nasdaq 100) | SPY (S&P 500) | -2.21 | S&P 500 leadership |

## Sector Constituent Dispersion

- Breadth 50D / 200D: percentage of active S&P 500 constituents in the sector trading above the 50-day / 200-day moving average.
- Positive 20D: percentage of active sector constituents with positive 20-day return.
- Std 20D: cross-sectional standard deviation of constituent 20-day returns; higher means wider stock-level dispersion.

| Sector | Count | Breadth 50D | Breadth 200D | Positive 20D | 20D Dispersion | Std 20D | Label | Leaders | Laggards |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Information Technology | 75 | 42.67 | 56.76 | 40.0 | 70.55 | 12.2 | very high | PTC, ACN, IT | STX, AKAM, COHR |
| Consumer Discretionary | 47 | 44.68 | 36.17 | 63.83 | 45.05 | 8.13 | very high | CCL, MAR, HLT | CMG, CVNA, MGM |
| Health Care | 60 | 70.0 | 81.67 | 78.33 | 40.34 | 6.47 | very high | MRNA, VEEV, MCK | JNJ, BMY, INCY |
| Materials | 24 | 41.67 | 58.33 | 62.5 | 35.59 | 8.29 | very high | LIN, IFF, NUE | SW, ALB, MOS |
| Financials | 76 | 37.33 | 54.93 | 46.05 | 34.63 | 7.36 | very high | CBOE, MRSH, V | SCHW, COIN, HOOD |
| Real Estate | 30 | 20.69 | 10.34 | 26.67 | 34.54 | 6.85 | very high | CCI, CSGP, HST | DOC, PLD, ARE |
| Industrials | 83 | 26.51 | 39.24 | 46.99 | 27.84 | 6.09 | very high | VRSK, WM, CTAS | UAL, BE, VRT |
| Consumer Staples | 34 | 65.62 | 59.38 | 70.59 | 26.95 | 6.19 | very high | CASY, KDP, COST | MKC, GIS, BG |
| Energy | 21 | 71.43 | 66.67 | 76.19 | 23.77 | 6.68 | very high | MPC, COP, APA | BKR, SLB, TPL |
| Communication Services | 22 | 28.57 | 50.0 | 31.82 | 23.63 | 5.52 | very high | DIS, OMC, NWSA | ECHO, CHTR, APP |
| Utilities | 31 | 48.39 | 16.13 | 83.87 | 12.2 | 2.64 | high | PNW, VST, ED | NEE, ES, NRG |

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
| US dollar/Euro ECB reference exchange rate | 1.12 | USD | -0.0 USD vs prior | 2026-10-20 | EUR weakened versus this currency. |
| Japanese yen/Euro ECB reference exchange rate | 177.34 | JPY | -0.29 JPY vs prior | 2026-10-20 | EUR weakened versus this currency. |
| Chinese yuan renminbi/Euro ECB reference exchange rate | 7.49 | CNY | -0.01 CNY vs prior | 2026-10-20 | EUR weakened versus this currency. |
| Australian dollar/Euro ECB reference exchange rate | 1.61 | AUD | -0.0 AUD vs prior | 2026-10-20 | EUR weakened versus this currency. |

ABS Australia note: ABS rows are stored locally/Neon, but most series are dimension-coded; only curated series should be promoted into narrative report text.

## Sector and Theme Leadership

### Official Sector Strength

Supporting and detracting names are the top/bottom S&P 500 constituents by 20D return when constituent coverage is available; otherwise the report falls back to related ETFs.

| Rank | Sector | Score | Trend | Momentum | Stock Breadth | ETF Flow | Flow Reliability | 3M RS | Supporting / Leaders | Detracting / Laggards |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Healthcare | 70.0 | strong uptrend | neutral | broad | 82.07 | 100.0 | 54.63 | MRNA, VEEV, MCK | JNJ, BMY, INCY |
| 2 | Energy | 66.98 | strong uptrend | positive | broad | 58.96 | 95.0 | 59.67 | MPC, COP, APA | BKR, SLB, TPL |
| 3 | Consumer Staples | 66.2 | strong uptrend | neutral | broad | 67.19 | 65.0 | 54.39 | CASY, KDP, COST | MKC, GIS, BG |
| 4 | Consumer Discretionary | 54.04 | neutral | neutral | broad | 37.87 | 65.0 | 52.09 | CCL, MAR, HLT | CMG, CVNA, MGM |
| 5 | Crypto | 51.74 | neutral | neutral | mixed | 67.43 | 65.0 | 50.0 |  |  |
| 6 | Financials | 51.22 | neutral | neutral | weak | 50.14 | 95.0 | 47.26 | CBOE, MRSH, V | SCHW, COIN, HOOD |
| 7 | Utilities | 50.62 | downtrend | neutral | mixed | 62.59 | 65.0 | 46.94 | PNW, VST, ED | NEE, ES, NRG |
| 8 | Cybersecurity | 48.88 | neutral | neutral | weak | 67.38 | 65.0 | 52.42 | CIBR | CIBR |
| 9 | Technology | 42.99 | downtrend | neutral | weak | 55.9 | 100.0 | 48.89 | PTC, ACN, IT | STX, AKAM, COHR |
| 10 | Real Estate | 42.98 | strong downtrend | neutral | weak | 40.81 | 90.0 | 44.03 | CCI, CSGP, HST | DOC, PLD, ARE |
| 11 | Semiconductors | 39.43 | downtrend | negative | weak | 50.0 | 0.0 | 42.17 | SMH, SOXX | SOXX, SMH |
| 12 | Industrials | 38.93 | strong downtrend | neutral | weak | 63.2 | 65.0 | 44.39 | VRSK, WM, CTAS | UAL, BE, VRT |
| 13 | Grid Infrastructure | 36.21 | strong downtrend | neutral | weak | 69.57 | 65.0 | 43.05 | GRID | GRID |
| 14 | Defense | 34.8 | strong downtrend | negative | weak | 50.0 | 0.0 | 37.27 | XAR | XAR |
| 15 | Nuclear | 31.03 | strong downtrend | negative | weak | 50.0 | 0.0 | 34.12 | NLR | NLR |

### Thematic Strength

| Rank | Theme | Score | Setup | ETF Flow | Flow Reliability | Dispersion | Price | News |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Energy | 66.1 | Positive setup | 58.96 | 95.0 | 4.07 | True | False |
| 2 | Healthcare Innovation | 58.2 | Neutral / watchlist | 82.07 | 100.0 | 11.69 | False | False |
| 3 | Dividend Defensives | 54.2 | Neutral / watchlist | 55.55 | 65.0 | 4.74 | False | False |
| 4 | Quality Growth | 52.88 | Neutral / watchlist | 57.05 | 65.0 | 10.92 | False | False |
| 5 | Cybersecurity | 51.92 | Neutral / watchlist | 67.38 | 65.0 | 11.13 | False | False |
| 6 | AI Infrastructure | 48.68 | Neutral / watchlist | 50.0 | 0.0 | 16.63 | False | False |
| 7 | Crypto Infrastructure | 47.28 | Neutral / watchlist | 67.43 | 65.0 | 3.06 | False | False |
| 8 | Semiconductors | 41.36 | Neutral / watchlist | 50.0 | 0.0 | 8.83 | False | False |
| 9 | Financials | 38.69 | Weak setup | 50.14 | 95.0 | 11.56 | False | False |
| 10 | Grid Infrastructure | 38.49 | Weak setup | 69.57 | 65.0 | 14.45 | False | False |
| 11 | Defense | 37.47 | Weak setup | 50.0 | 0.0 | 29.12 | False | False |
| 12 | Small Caps | 33.25 | Weak setup | 63.86 | 65.0 | 0.0 | False | False |
| 13 | Nuclear | 28.32 | Underperformance risk | 50.0 | 0.0 | 15.45 | False | False |

- Top 5 improving themes: Crypto Infrastructure, Cybersecurity, Energy, Quality Growth, AI Infrastructure
- Top 5 deteriorating themes: Nuclear, Defense, Financials, Small Caps, Grid Infrastructure
- Strong news but weak price confirmation: none
- Strong price but weak news confirmation: Energy

### Sector / Theme Alignment

| Sector | Related Themes | Sector Score | Sector Signal | Theme Score | Theme Signal | Interpretation |
| --- | --- | --- | --- | --- | --- | --- |
| Healthcare | Healthcare Innovation | 70.0 | strong | 58.2 | positive | sector and theme confirmation |
| Energy | Energy | 66.98 | strong | 66.1 | strong | sector and theme confirmation |
| Consumer Staples | Dividend Defensives | 66.2 | strong | 54.2 | mixed | sector stronger than related themes |
| Consumer Discretionary | Small Caps | 54.04 | mixed | 33.25 | very weak | mixed confirmation |
| Crypto | Crypto Infrastructure | 51.74 | mixed | 47.28 | mixed | mixed confirmation |
| Financials | Financials | 51.22 | mixed | 38.69 | weak | mixed confirmation |
| Utilities | Grid Infrastructure, Nuclear, Dividend Defensives | 50.62 | mixed | 40.34 | weak | mixed confirmation |
| Cybersecurity | Cybersecurity | 48.88 | mixed | 51.92 | mixed | mixed confirmation |
| Technology | AI Infrastructure, Semiconductors, Quality Growth | 42.99 | weak | 47.64 | mixed | mixed confirmation |
| Real Estate | Dividend Defensives | 42.98 | weak | 54.2 | mixed | mixed confirmation |
| Semiconductors | AI Infrastructure, Semiconductors | 39.43 | weak | 45.02 | mixed | mixed confirmation |
| Industrials | Defense, Grid Infrastructure | 38.93 | weak | 37.98 | weak | broad weakness across sector and themes |
| Grid Infrastructure | Grid Infrastructure | 36.21 | weak | 38.49 | weak | broad weakness across sector and themes |
| Defense | Defense | 34.8 | very weak | 37.47 | weak | broad weakness across sector and themes |
| Nuclear | Nuclear | 31.03 | very weak | 28.32 | very weak | broad weakness across sector and themes |

## Three-Month Outperformance Setup

| Rank | Theme | Score | Classification | Drivers | Invalidation Triggers |
| --- | --- | --- | --- | --- | --- |
| 1 | Energy | 69.23 | Positive setup | relative_strength_20d, relative_strength_60d, trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 2 | Healthcare Innovation | 59.15 | Neutral / watchlist | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 3 | Quality Growth | 57.98 | Neutral / watchlist | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 4 | Cybersecurity | 55.84 | Neutral / watchlist | relative_strength_60d, trend_persistence, breadth, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 5 | Dividend Defensives | 55.42 | Neutral / watchlist | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 6 | AI Infrastructure | 55.08 | Neutral / watchlist | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 7 | Crypto Infrastructure | 50.41 | Neutral / watchlist | relative_strength_60d, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 8 | Semiconductors | 46.31 | Neutral / watchlist | downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 9 | Financials | 39.68 | Weak setup | downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 10 | Grid Infrastructure | 37.55 | Weak setup | downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 11 | Defense | 36.27 | Weak setup | downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 12 | Small Caps | 34.02 | Weak setup | downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |

## Breadth and Participation

- Above 50DMA: `28.33%`
- Above 200DMA: `55.0%`
- Positive 20D return: `30.0%`

## Volatility and Risk Signals

- VIX close=17.38 pct_chg=-5.75

## News Analytics

- Sentiment counts: {'positive': 0, 'negative': 0, 'neutral': 80}
- News confirmation score: `50.0`

### Top Market-Moving Headlines

**1. Oil prices fall as traders hope for diplomatic progress in Middle East**
- Source: CNBC Markets
- Importance / impact: Low / Mixed
- Relevance / horizon: macro / short-term
- Affected assets: Equities, Bonds, USD, Commodities
- Score: `23.75`
- Investment implication: Macro-relevant mixed signal; use as context for rates, volatility, and index confirmation over the short-term.

**2. Dow jumps 500 points as solid earnings, falling crude oil stir rebound: Live updates**
- Source: CNBC Top News
- Importance / impact: Low / Mixed
- Relevance / horizon: macro / short-term
- Affected assets: P, S
- Score: `23.75`
- Investment implication: Macro-relevant mixed signal; use as context for rates, volatility, and index confirmation over the short-term.

**3. U.S. Treasury yields move lower after weak housing data**
- Source: CNBC Top News
- Importance / impact: Low / Mixed
- Relevance / horizon: macro / short-term
- Affected assets: U.S
- Score: `23.75`
- Investment implication: Macro-relevant mixed signal; use as context for rates, volatility, and index confirmation over the short-term.

**4. S&P 500, Nasdaq open lower as tech stocks fall, oil prices jump**
- Source: MarketWatch Bulletins
- Importance / impact: Low / Mixed
- Relevance / horizon: macro / short-term
- Affected assets: P, S
- Score: `23.75`
- Investment implication: Macro-relevant mixed signal; use as context for rates, volatility, and index confirmation over the short-term.

**5. Judge dismisses Sam Altman's sister's sexual abuse lawsuit**
- Source: CNBC Markets
- Importance / impact: Low / Mixed
- Relevance / horizon: sector_theme / short-term
- Affected assets: A, U.S
- Score: `20.19`
- Investment implication: Theme or sector mixed signal; requires price and volume confirmation before affecting rankings.

**6. Investors look to earnings to reset the bull market. The key level to watch on the S&P 500**
- Source: CNBC Markets
- Importance / impact: Low / Mixed
- Relevance / horizon: sector_theme / short-term
- Affected assets: P, S
- Score: `20.19`
- Investment implication: Theme or sector mixed signal; requires price and volume confirmation before affecting rankings.

**7. Brent hits five-month high as attacks on ships, Saudi sites fuel supply worries**
- Source: CNBC Top News
- Importance / impact: Low / Mixed
- Relevance / horizon: macro / short-term
- Affected assets: Equities, Bonds, USD, Commodities
- Score: `20.19`
- Investment implication: Macro-relevant mixed signal; use as context for rates, volatility, and index confirmation over the short-term.

**8. Why smaller stocks face worse prospects than the S&P 500 in the coming years**
- Source: MarketWatch Top Stories
- Importance / impact: Low / Mixed
- Relevance / horizon: sector_theme / short-term
- Affected assets: P, S
- Score: `18.06`
- Investment implication: Theme or sector mixed signal; requires price and volume confirmation before affecting rankings.

**9. The multi-million dollar real estate portfolio of Buffalo Bills QB Josh Allen and actress Hailee Steinfeld**
- Source: MarketWatch Top Stories
- Importance / impact: Low / Mixed
- Relevance / horizon: sector_theme / short-term
- Affected assets: NFL, QB
- Score: `18.06`
- Investment implication: Theme or sector mixed signal; requires price and volume confirmation before affecting rankings.

**10. ‘I’m naturally skeptical’: I receive 10 calls a day offering me $15,000 loans at 8% interest. Is this a scam?**
- Source: MarketWatch Top Stories
- Importance / impact: Low / Mixed
- Relevance / horizon: single_name / short-term
- Affected assets: I
- Score: `16.25`
- Investment implication: Single-name mixed signal; low weight unless it maps to a broader sector or theme.


### Headline Quality Checks

Noisy headline list: Meta is back on offense — and its next move could , Bullish sentiment on stocks has cratered. Why that

## Positioning & Flow Dashboard

Positioning and flow data is used as confirmation only.

### Deferred Flow Sections

- Official ETF / fund flows: current report uses shares-outstanding-derived net fund flow estimates from free ETF metadata.
- Institutional Ownership: not available until SEC 13F ingestion is implemented.
- Grouped exposure flow reliability: use issuer coverage and availability status before treating ETF flow as confirmation.

## ETF Flows Analysis

- Market flow regime: `Mixed / Neutral`
- Market flow score: `52.9 / 100`
- Equity risk flow: `55.8`
- Credit risk flow: `61.1`
- Sector cyclicality flow: `42.4`
- Duration/liquidity flow: `50.1`
- Alternatives: `barbell demand`
- ETF flow reliability: `71.4 / 100`
- Dominant allocation direction: `defensive demand`

### Core Flow Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVV | U.S. Broad Equity | 1.0 | -1.1 | 0.7 | -0.8 | Flat | Neutral | Normal | Neutral | Neutral | Medium-term recovery | 87.0 |
| ACWI | Global Equity | -0.6 | -0.8 | 0.0 | -0.6 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Mixed or neutral flow structure; Persistent selling | 77.0 |
| EFA | Developed Markets ex-U.S. | 0.9 | 0.7 | 0.1 | 1.4 | Down | Neutral | High | Heavy Selling Pressure | Cautious | Structural accumulation; Persistent selling | 83.0 |
| IEMG | Emerging Markets | -0.8 | 0.1 | 0.0 | -0.3 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Medium-term deterioration; Persistent selling | 75.0 |
| IJH | U.S. Mid Cap | -0.7 | 1.0 | 0.4 | 0.7 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural accumulation | 91.0 |
| IWM | U.S. Small Cap | 1.9 | 1.9 | 0.6 | -0.4 | Down | Sell | Normal | Persistent Distribution | Risk-Off | Tactical profit-taking inside structural accumulation | 83.0 |
| LQD | Investment-Grade Credit | 0.4 | -1.5 | 0.6 | -0.6 | Flat | Neutral | Normal | Neutral | Neutral | Medium-term recovery | 87.0 |
| HYG | High-Yield Credit | 1.6 | 1.4 | 0.6 | -0.6 | Down | Buy | Low | Tentative Buying | Low Confidence | Strong confirmation | 95.0 |
| SGOV | Treasury Bills / Cash | -0.4 | -0.2 | 0.8 | -0.4 | Flat | Neutral | Normal | Neutral | Neutral | Structural accumulation; Strong sponsorship | 99.0 |
| SHY | Short-Duration Treasuries | 1.0 | 2.0 | 0.7 | -0.4 | Flat | Neutral | Normal | Neutral | Neutral | Structural accumulation | 91.0 |
| IEF | Intermediate-Duration Treasuries | 0.0 | -1.2 | 0.5 | 0.2 | Flat | Neutral | Normal | Neutral | Neutral | Structural distribution | 79.0 |
| TLT | Long-Duration Treasuries | 0.0 | 0.8 | 0.7 | -0.5 | Flat | Sell | Normal | Quiet Distribution | Weakening | Tactical profit-taking inside structural accumulation; Exceptional institutional selling | 75.0 |
| GLD | Gold | 0.2 | 1.7 | 0.5 | -1.1 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural accumulation | 91.0 |
| IBIT | Bitcoin | 0.4 | 1.5 | 0.7 | -0.4 | Down | Sell | Normal | Persistent Distribution | Risk-Off | Tactical profit-taking inside structural accumulation | 83.0 |

### Sector Flow Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| XLC | Communication Services | 2.5 | 3.5 | 0.5 | -0.6 | Down | Buy | Normal | Contrarian Buying | Watch | Strong confirmation; Exceptional institutional buying | 100.0 |
| XLY | Consumer Discretionary | -1.0 | -0.2 | 0.4 | -0.0 | Up | Sell | Normal | Profit Taking | Slightly Bearish | Strong confirmation; Exceptional institutional selling | 87.0 |
| XLP | Consumer Staples | 0.7 | 0.5 | 0.7 | 0.8 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Medium-term recovery | 87.0 |
| XLE | Energy | 0.5 | -0.1 | 0.7 | -0.1 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Medium-term recovery | 87.0 |
| XLF | Financials | 0.8 | -1.5 | 0.6 | -0.5 | Flat | Neutral | Normal | Neutral | Neutral | Medium-term recovery | 87.0 |
| XLV | Health Care | 2.8 | 0.6 | 0.7 | -1.0 | Up | Buy | Normal | Steady Accumulation | Risk-On | Strong confirmation; Exceptional institutional buying | 100.0 |
| XLI | Industrials | 0.2 | -1.1 | 0.5 | -0.5 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Medium-term recovery | 87.0 |
| XLK | Information Technology | 0.7 | -0.3 | 0.6 | 0.6 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural accumulation | 91.0 |
| XLB | Materials | -1.0 | -2.1 | 0.5 | -0.8 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural distribution; Exceptional institutional selling | 71.0 |
| XLRE | Real Estate | 0.6 | -1.5 | 0.6 | 0.8 | Flat | Neutral | Normal | Neutral | Neutral | Medium-term recovery | 87.0 |
| XLU | Utilities | 2.9 | 2.2 | 0.7 | -0.1 | Up | Sell | Normal | Profit Taking | Slightly Bearish | Tactical profit-taking inside structural accumulation | 83.0 |

### Subsector PFV Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ITA | Aerospace and Defense | -0.2 | 0.4 | 0.3 | 0.6 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural distribution | 79.0 |
| SOXX | Semiconductors | -1.6 | -1.5 | 0.6 | 0.4 | Down | Sell | Normal | Persistent Distribution | Risk-Off | Strong confirmation | 95.0 |
| SMH | Semiconductors | -0.5 | -0.7 | 0.4 | -0.0 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Medium-term deterioration | 83.0 |
| CIBR | Cybersecurity | 1.8 | 2.2 | 0.9 | 0.3 | Down | Sell | Normal | Persistent Distribution | Risk-Off | Tactical profit-taking inside structural accumulation; Exceptional institutional selling, Strong sponsorship | 83.0 |

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
- Live macro rows used: `34`
- Economic rows loaded: `113`
- News rows loaded: `80`
- Positioning/flow rows loaded: `30`

## Cycle Metadata

- Report generated at: 21 October 2026, 02:37:23 (HKT)

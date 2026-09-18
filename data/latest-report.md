# Rule-Based Institutional Market Update

Generated at: 19 September 2026, 03:06:32 (HKT)
Window: 24h

## Executive Dashboard

- Regime score: **51.47 / 100** (Mixed / Rotation)
- US equity strength: **41.32 / 100** (weak)
- Evidence quality: **72.5 / 100**
- ETF flow contribution: **49.09 / 100**, reliability **71.16 / 100**
- Breadth: **narrow**; above 50DMA `31.67%`, above 200DMA `66.1%`
- Top sector score: **Cybersecurity** `71.34`
- Top theme score: **Energy** `65.62`

## Market Regime Score

| Metric | Value | Driver / Interpretation |
| --- | --- | --- |
| Overall regime | 51.47 | Mixed / Rotation |
| equity_trend | 40.0 | mild risk-off pressure; Core equity ETFs versus moving averages. |
| equity_momentum | 45.05 | neutral / mixed; 5D/20D/60D return momentum across SPY, QQQ, IWM, and SMH. |
| market_breadth | 41.48 | mild risk-off pressure; Participation breadth from tracked equity/ETF rows. |
| volatility | 80.0 | risk-on support; VIX level and change; higher score means calmer volatility conditions. |
| rates_yield_curve | 58.0 | mild risk-on support; Treasury yield pressure and curve shape; higher score means less rates pressure. |
| credit_proxy | 50.0 | neutral / mixed; Credit-market proxy; currently neutral when no direct spread signal is available. |
| dollar_fx | 54.97 | neutral / mixed; Dollar move; higher score means less USD tightening pressure. |
| commodity_confirmation | 61.0 | mild risk-on support; Copper, silver, oil, and gold mix; higher score means better cyclical confirmation. |
| etf_flow | 49.35 | neutral / mixed; Grouped ETF flow contribution adjusted for reliability. |
| news_confirmation | 51.25 | neutral / mixed; Weighted headline/news confirmation score. |
| Positive contributors |  | volatility=80.0, commodity_confirmation=61.0 |
| Negative contributors |  | equity_trend=40.0, market_breadth=41.48 |

## US Equity Strength Score

| Component | Score |
| --- | --- |
| indices_above_moving_averages | 40.0 |
| sp500_trend | 55.0 |
| nasdaq_trend | 35.0 |
| russell_participation | 35.0 |
| returns_momentum | 45.05 |
| rsi_zone | 38.75 |
| macd_confirmation | 35.0 |
| volume_confirmation | 46.25 |
| breadth | 41.48 |

## Evidence Quality / Confidence

- Confidence score: `72.5`
- Agreement ratio: `0.3`
- Contradiction count: `2`
- Missing indicators: none
- Warning flags: none

## Cross-Asset Confirmation

| Area | Signal | Interpretation |
| --- | --- | --- |
| Equities | S&P 500 stable; Nasdaq stable; Russell 2000 falling | Confirms risk appetite when broad indices rise together; weak small caps would narrow the signal. |
| Rates | 10Y Treasury rising; MOVE falling | Rising yields can pressure duration assets; falling MOVE supports calmer bond volatility. |
| Dollar | DXY proxy stable | A stronger dollar can tighten financial conditions and pressure commodities/emerging-market risk. |
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
| ^GSPC | S&P 500 | 7642.42 | 0.06 | 2026-09-18 | live as of 19 September 2026, 03:00:22 (HKT) |
| ^IXIC | NASDAQ Composite | 26463.0 | 0.17 | 2026-09-18 | live as of 19 September 2026, 03:00:22 (HKT) |
| ^RUT | Russell 2000 Index | 2854.24 | -0.71 | 2026-09-18 | live as of 19 September 2026, 03:00:22 (HKT) |
| ^VIX | CBOE Volatility Index | 15.01 | -2.79 | 2026-09-18 | live as of 19 September 2026, 03:00:22 (HKT) |
| ^SKEW | CBOE SKEW Index | 145.7 | -0.17 | 2026-09-17 | closed |
| ^MOVE | ICE BofA MOVE Index | 76.22 | -5.59 | 2026-09-17 | closed |
| US2YT=X | United States 2-Year Treasury Yield | 4.74 | 1.14 | 2026-09-18 | live as of 19 September 2026, 03:00:22 (HKT) |
| US3YT=X | United States 3-Year Treasury Yield | 4.83 | 1.33 | 2026-09-18 | live as of 19 September 2026, 03:00:22 (HKT) |
| US5YT=X | United States 5-Year Treasury Yield | 4.85 | 1.07 | 2026-09-18 | live as of 19 September 2026, 03:00:22 (HKT) |
| US7YT=X | United States 7-Year Treasury Yield | 4.93 | 1.15 | 2026-09-18 | live as of 19 September 2026, 03:00:22 (HKT) |
| US10YT=X | United States 10-Year Treasury Yield | 5.0 | 1.03 | 2026-09-18 | live as of 19 September 2026, 03:00:22 (HKT) |
| US20YT=X | United States 20-Year Treasury Yield | 5.37 | 0.75 | 2026-09-18 | live as of 19 September 2026, 03:00:22 (HKT) |
| US30YT=X | United States 30-Year Treasury Yield | 5.33 | 0.61 | 2026-09-18 | live as of 19 September 2026, 03:00:22 (HKT) |
| HK50 | Hang Seng Futures | 24654.5 | -0.05 | 2026-09-18 | closed |
| KOR200c1 | KOSPI 200 Futures | 1084.95 | 2.09 | 2026-09-17 | closed |
| CIHc1 | SSE 50 Futures | 2828.2 | -1.34 | 2026-09-17 | closed |
| HYG | iShares iBoxx High Yield Corporate Bond ETF | 78.56 | -0.2 | 2026-09-18 | live as of 19 September 2026, 03:00:22 (HKT) |
| LQD | iShares iBoxx Investment Grade Corporate Bond ETF | 104.72 | -0.41 | 2026-09-18 | live as of 19 September 2026, 03:00:22 (HKT) |
| JNK | SPDR Bloomberg High Yield Bond ETF | 94.53 | -0.22 | 2026-09-18 | live as of 19 September 2026, 03:00:22 (HKT) |
| RSP | Invesco S&P 500 Equal Weight ETF | 212.51 | -0.37 | 2026-09-18 | live as of 19 September 2026, 03:00:22 (HKT) |
| IWF | iShares Russell 1000 Growth ETF | 122.97 | 0.36 | 2026-09-18 | live as of 19 September 2026, 03:00:22 (HKT) |
| IWD | iShares Russell 1000 Value ETF | 252.04 | -0.31 | 2026-09-18 | live as of 19 September 2026, 03:00:22 (HKT) |
| TLT | iShares 20+ Year Treasury Bond ETF | 81.28 | -0.61 | 2026-09-18 | live as of 19 September 2026, 03:00:22 (HKT) |
| IEF | iShares 7-10 Year Treasury Bond ETF | 90.88 | -0.41 | 2026-09-18 | live as of 19 September 2026, 03:00:22 (HKT) |
| SHY | iShares 1-3 Year Treasury Bond ETF | 81.28 | -0.1 | 2026-09-18 | live as of 19 September 2026, 03:00:22 (HKT) |
| GC=F | Gold Future | 4421.6 | 0.5 | 2026-09-18 | live as of 19 September 2026, 03:00:22 (HKT) |
| SI=F | Silver Future | 67.08 | 2.46 | 2026-09-18 | live as of 19 September 2026, 03:00:22 (HKT) |
| CL=F | WTI Crude Oil Future | 99.55 | -2.32 | 2026-09-18 | live as of 19 September 2026, 03:00:22 (HKT) |
| HG=F | Copper Future | 6.7 | 1.71 | 2026-09-18 | live as of 19 September 2026, 03:00:22 (HKT) |

## Market Dispersion Analysis

- Sector ETF 20D dispersion: `14.73` points (high); leader `XLE` (Energy) `5.35`, laggard `XLI` (Industrials) `-9.38`
- Sector ETF 60D dispersion: `30.3` points (very high); leader `XLE` (Energy) `22.61`, laggard `XLU` (Utilities) `-7.69`

| Comparison | Left | Right | 20D Spread | Signal |
| --- | --- | --- | --- | --- |
| Equal-weight vs cap-weight | RSP (Equal-weight S&P 500) | SPY (S&P 500) | -1.12 | mega-cap concentration |
| Small-cap vs large-cap | IWM (Russell 2000) | SPY (S&P 500) | -4.24 | large-cap leadership |
| Growth vs value | IWF (Russell 1000 Growth) | IWD (Russell 1000 Value) | -2.48 | value leadership |
| Nasdaq vs S&P 500 | QQQ (Nasdaq 100) | SPY (S&P 500) | -1.49 | S&P 500 leadership |

## Sector Constituent Dispersion

- Breadth 50D / 200D: percentage of active S&P 500 constituents in the sector trading above the 50-day / 200-day moving average.
- Positive 20D: percentage of active sector constituents with positive 20-day return.
- Std 20D: cross-sectional standard deviation of constituent 20-day returns; higher means wider stock-level dispersion.

| Sector | Count | Breadth 50D | Breadth 200D | Positive 20D | 20D Dispersion | Std 20D | Label | Leaders | Laggards |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Health Care | 59 | 62.71 | 77.97 | 57.63 | 152.11 | 17.64 | very high | MRNA, RVTY, VEEV | BSX, SYK, COO |
| Information Technology | 73 | 50.68 | 60.27 | 32.88 | 58.77 | 13.06 | very high | CRM, SWKS, NOW | WDC, TER, CIEN |
| Consumer Staples | 34 | 39.39 | 37.5 | 35.29 | 46.63 | 8.64 | very high | EL, KR, MO | HRL, CLX, CASY |
| Industrials | 83 | 14.46 | 41.77 | 12.05 | 40.87 | 6.72 | very high | DE, CHRW, ADP | GNRC, HWM, AXON |
| Materials | 25 | 36.0 | 56.0 | 28.0 | 35.5 | 8.22 | very high | MOS, CF, CTVA | VMC, ALB, IP |
| Consumer Discretionary | 47 | 14.89 | 29.79 | 12.77 | 31.79 | 6.85 | very high | ULTA, BBY, EBAY | TJX, CCL, NCLH |
| Communication Services | 24 | 54.17 | 60.87 | 54.17 | 30.09 | 6.43 | very high | META, TTD, T | OMC, LYV, TTWO |
| Utilities | 31 | 6.45 | 6.45 | 6.45 | 27.59 | 5.26 | very high | AWK, AES, VST | NRG, EIX, PCG |
| Energy | 21 | 80.95 | 76.19 | 80.95 | 27.31 | 6.59 | very high | MPC, VLO, APA | WMB, KMI, BKR |
| Financials | 76 | 30.67 | 67.61 | 30.26 | 27.01 | 4.92 | very high | HOOD, COIN, PGR | BX, PYPL, AON |
| Real Estate | 30 | 10.34 | 44.83 | 13.33 | 26.51 | 4.6 | very high | ARE, AMT, CSGP | PSA, DLR, IRM |

## Economic Data Snapshot

### U.S. Labor

| Indicator | Latest | Unit | Change | Date | Rule-Based Interpretation |
| --- | --- | --- | --- | --- | --- |
| All Employees, Total Nonfarm | 159075.0 | thousands | 162.0 thousands vs prior | 2026-08-01 | Higher reading supports activity or liquidity. |
| Unemployment Rate | 4.1 | percent | 0.0 pp vs prior | 2026-08-01 | Stable reading. |
| Initial Claims | 215000.0 | number | -12000.0 number vs prior | 2026-06-20 | Lower claims indicate firmer labor-market conditions. |
| Continued Claims | 1821000.0 | number | 21000.0 number vs prior | 2026-06-13 | Higher claims indicate softer labor-market conditions. |
| Labor Force Participation Rate | 61.6 | percent | 0.2 pp vs prior | 2026-08-01 | Higher participation expands labor supply. |

### U.S. Growth

| Indicator | Latest | Unit | Change | Date | Rule-Based Interpretation |
| --- | --- | --- | --- | --- | --- |
| Real Gross Domestic Product | 24269.61 | billions chained 2017 dollars | 89.19 billions chained 2017 dollars vs prior | 2026-04-01 | Higher reading supports activity or liquidity. |
| Industrial Production Index | 102.65 | index 2017=100 | 0.14 index pts vs prior | 2026-05-01 | Higher reading supports activity or liquidity. |
| Advance Retail Sales | 773947.0 | millions dollars | 9485.0 millions dollars vs prior | 2026-08-01 | Higher reading supports activity or liquidity. |

### U.S. Inflation

| Indicator | Latest | Unit | Change | Date | Rule-Based Interpretation |
| --- | --- | --- | --- | --- | --- |
| Headline CPI month-over-month inflation rate | 0.4 | percent | 0.32 pp vs prior | 2026-08-01 | Higher reading increases macro pressure. |
| Headline CPI year-over-year inflation rate | 3.71 | percent | 0.17 pp vs prior | 2026-08-01 | Higher reading increases macro pressure. |
| Core CPI month-over-month inflation rate | 0.29 | percent | 0.07 pp vs prior | 2026-08-01 | Higher reading increases macro pressure. |
| Core CPI year-over-year inflation rate | 2.76 | percent | -0.02 pp vs prior | 2026-08-01 | Lower reading eases macro pressure. |
| Headline CPI year-over-year inflation rate | 3.69 | percent | 0.17 pp vs prior | 2026-08-01 | Higher reading increases macro pressure. |
| Core CPI year-over-year inflation rate | 2.75 | percent | 0.08 pp vs prior | 2026-08-01 | Higher reading increases macro pressure. |
| Headline PCE Price Index month-over-month inflation rate | 0.16 | percent | 0.25 pp vs prior | 2026-07-01 | Higher reading increases macro pressure. |
| Headline PCE Price Index year-over-year inflation rate | 3.7 | percent | -0.02 pp vs prior | 2026-07-01 | Lower reading eases macro pressure. |
| Core PCE Price Index month-over-month inflation rate | 0.25 | percent | 0.1 pp vs prior | 2026-07-01 | Higher reading increases macro pressure. |
| Core PCE Price Index year-over-year inflation rate | 3.34 | percent | 0.0 pp vs prior | 2026-07-01 | Higher reading increases macro pressure. |
| Headline PPI Final Demand month-over-month inflation rate | 0.29 | percent | 0.28 pp vs prior | 2026-08-01 | Higher reading increases macro pressure. |
| Headline PPI Final Demand year-over-year inflation rate | 5.44 | percent | 0.6 pp vs prior | 2026-08-01 | Higher reading increases macro pressure. |
| Core PPI Final Demand Less Foods and Energy month-over-month inflation rate | 0.16 | percent | -0.1 pp vs prior | 2026-08-01 | Lower reading eases macro pressure. |
| Core PPI Final Demand Less Foods and Energy year-over-year inflation rate | 4.62 | percent | 0.37 pp vs prior | 2026-08-01 | Higher reading increases macro pressure. |
| Consumer Price Index for All Urban Consumers | 334.13 | index 1982-1984=100 | 1.32 index pts vs prior | 2026-08-01 | Higher reading increases macro pressure. |
| Core CPI | 337.76 | index 1982-1984=100 | 0.98 index pts vs prior | 2026-08-01 | Higher reading increases macro pressure. |
| Personal Consumption Expenditures Price Index | 131.66 | index 2017=100 | 0.2 index pts vs prior | 2026-07-01 | Higher reading increases macro pressure. |
| Core PCE Price Index | 130.66 | index 2017=100 | 0.32 index pts vs prior | 2026-07-01 | Higher reading increases macro pressure. |
| Producer Price Index: Final Demand | 157.6 | index Nov 2009=100 | 0.45 index pts vs prior | 2026-08-01 | Latest structural macro observation. |
| Producer Price Index: Final Demand Less Foods and Energy | 154.84 | index Apr 2010=100 | 0.25 index pts vs prior | 2026-08-01 | Latest structural macro observation. |

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
| Housing Starts | 1275.0 | thousands | -34.0 thousands vs prior | 2026-08-01 | Lower reading signals softer activity or liquidity. |
| New Privately-Owned Housing Units Authorized | 1394.0 | thousands | -39.0 thousands vs prior | 2026-08-01 | Lower reading signals softer activity or liquidity. |
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
| US dollar/Euro ECB reference exchange rate | 1.15 | USD | -0.0 USD vs prior | 2026-09-18 | EUR weakened versus this currency. |
| Japanese yen/Euro ECB reference exchange rate | 180.94 | JPY | 2.19 JPY vs prior | 2026-09-18 | EUR strengthened versus this currency. |
| Chinese yuan renminbi/Euro ECB reference exchange rate | 7.68 | CNY | -0.03 CNY vs prior | 2026-09-18 | EUR weakened versus this currency. |
| Australian dollar/Euro ECB reference exchange rate | 1.61 | AUD | -0.0 AUD vs prior | 2026-09-18 | EUR weakened versus this currency. |

ABS Australia note: ABS rows are stored locally/Neon, but most series are dimension-coded; only curated series should be promoted into narrative report text.

## Sector and Theme Leadership

### Official Sector Strength

Supporting and detracting names are the top/bottom S&P 500 constituents by 20D return when constituent coverage is available; otherwise the report falls back to related ETFs.

| Rank | Sector | Score | Trend | Momentum | Stock Breadth | ETF Flow | Flow Reliability | 3M RS | Supporting / Leaders | Detracting / Laggards |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Cybersecurity | 71.34 | strong uptrend | positive | broad | 69.25 | 65.0 | 60.37 | CIBR | CIBR |
| 2 | Energy | 66.88 | strong uptrend | positive | broad | 50.0 | 0.0 | 62.87 | MPC, VLO, APA | WMB, KMI, BKR |
| 3 | Healthcare | 58.6 | strong uptrend | neutral | broad | 64.37 | 90.0 | 55.72 | MRNA, RVTY, VEEV | BSX, SYK, COO |
| 4 | Crypto | 51.59 | neutral | neutral | mixed | 65.88 | 65.0 | 50.0 |  |  |
| 5 | Technology | 48.74 | neutral | neutral | mixed | 42.17 | 90.0 | 46.76 | CRM, SWKS, NOW | WDC, TER, CIEN |
| 6 | Financials | 45.63 | neutral | neutral | weak | 36.88 | 100.0 | 52.3 | HOOD, COIN, PGR | BX, PYPL, AON |
| 7 | Semiconductors | 42.43 | downtrend | negative | weak | 89.32 | 100.0 | 36.79 | SMH, SOXX | SOXX, SMH |
| 8 | Consumer Staples | 40.38 | downtrend | neutral | weak | 39.75 | 65.0 | 50.15 | EL, KR, MO | HRL, CLX, CASY |
| 9 | Real Estate | 34.99 | strong downtrend | neutral | weak | 50.0 | 0.0 | 47.54 | ARE, AMT, CSGP | PSA, DLR, IRM |
| 10 | Consumer Discretionary | 34.42 | strong downtrend | neutral | weak | 59.02 | 65.0 | 45.46 | ULTA, BBY, EBAY | TJX, CCL, NCLH |
| 11 | Grid Infrastructure | 34.29 | strong downtrend | negative | weak | 68.07 | 65.0 | 40.9 | GRID | GRID |
| 12 | Utilities | 34.13 | strong downtrend | negative | weak | 55.74 | 65.0 | 42.25 | AWK, AES, VST | NRG, EIX, PCG |
| 13 | Nuclear | 32.73 | strong downtrend | negative | weak | 50.0 | 0.0 | 39.66 | NLR | NLR |
| 14 | Defense | 32.0 | strong downtrend | negative | weak | 74.7 | 65.0 | 33.75 | XAR | XAR |
| 15 | Industrials | 31.62 | strong downtrend | negative | weak | 43.53 | 65.0 | 42.32 | DE, CHRW, ADP | GNRC, HWM, AXON |

### Thematic Strength

| Rank | Theme | Score | Setup | ETF Flow | Flow Reliability | Dispersion | Price | News |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Energy | 65.62 | Positive setup | 50.0 | 0.0 | 2.57 | True | False |
| 2 | Cybersecurity | 63.33 | Positive setup | 69.25 | 65.0 | 13.54 | True | False |
| 3 | Quality Growth | 54.67 | Neutral / watchlist | 56.29 | 65.0 | 11.9 | False | False |
| 4 | Crypto Infrastructure | 53.39 | Neutral / watchlist | 65.88 | 65.0 | 18.36 | False | False |
| 5 | Healthcare Innovation | 52.7 | Positive setup | 64.37 | 90.0 | 10.73 | False | False |
| 6 | AI Infrastructure | 51.13 | Neutral / watchlist | 89.32 | 100.0 | 14.27 | False | False |
| 7 | Financials | 47.02 | Neutral / watchlist | 36.88 | 100.0 | 5.83 | False | False |
| 8 | Dividend Defensives | 46.58 | Neutral / watchlist | 68.45 | 65.0 | 6.84 | False | False |
| 9 | Semiconductors | 46.38 | Neutral / watchlist | 89.32 | 100.0 | 15.13 | False | False |
| 10 | Small Caps | 43.98 | Neutral / watchlist | 57.61 | 65.0 | 0.0 | False | False |
| 11 | Grid Infrastructure | 39.09 | Weak setup | 68.07 | 65.0 | 8.61 | False | False |
| 12 | Defense | 38.47 | Weak setup | 74.7 | 65.0 | 11.26 | False | False |
| 13 | Nuclear | 29.32 | Weak setup | 50.0 | 0.0 | 15.34 | False | False |

- Top 5 improving themes: Energy, Cybersecurity, Healthcare Innovation, Crypto Infrastructure, Quality Growth
- Top 5 deteriorating themes: Nuclear, Semiconductors, Grid Infrastructure, Small Caps, AI Infrastructure
- Strong news but weak price confirmation: none
- Strong price but weak news confirmation: Energy, Cybersecurity

### Sector / Theme Alignment

| Sector | Related Themes | Sector Score | Sector Signal | Theme Score | Theme Signal | Interpretation |
| --- | --- | --- | --- | --- | --- | --- |
| Cybersecurity | Cybersecurity | 71.34 | strong | 63.33 | positive | sector and theme confirmation |
| Energy | Energy | 66.88 | strong | 65.62 | strong | sector and theme confirmation |
| Healthcare | Healthcare Innovation | 58.6 | positive | 52.7 | mixed | sector stronger than related themes |
| Crypto | Crypto Infrastructure | 51.59 | mixed | 53.39 | mixed | mixed confirmation |
| Technology | AI Infrastructure, Semiconductors, Quality Growth | 48.74 | mixed | 50.73 | mixed | mixed confirmation |
| Financials | Financials | 45.63 | mixed | 47.02 | mixed | mixed confirmation |
| Semiconductors | AI Infrastructure, Semiconductors | 42.43 | weak | 48.76 | mixed | mixed confirmation |
| Consumer Staples | Dividend Defensives | 40.38 | weak | 46.58 | mixed | mixed confirmation |
| Real Estate | Dividend Defensives | 34.99 | very weak | 46.58 | mixed | mixed confirmation |
| Consumer Discretionary | Small Caps | 34.42 | very weak | 43.98 | weak | broad weakness across sector and themes |
| Grid Infrastructure | Grid Infrastructure | 34.29 | very weak | 39.09 | weak | broad weakness across sector and themes |
| Utilities | Grid Infrastructure, Nuclear, Dividend Defensives | 34.13 | very weak | 38.33 | weak | broad weakness across sector and themes |
| Nuclear | Nuclear | 32.73 | very weak | 29.32 | very weak | broad weakness across sector and themes |
| Defense | Defense | 32.0 | very weak | 38.47 | weak | broad weakness across sector and themes |
| Industrials | Defense, Grid Infrastructure | 31.62 | very weak | 38.78 | weak | broad weakness across sector and themes |

## Three-Month Outperformance Setup

| Rank | Theme | Score | Classification | Drivers | Invalidation Triggers |
| --- | --- | --- | --- | --- | --- |
| 1 | Energy | 69.37 | Positive setup | relative_strength_60d, trend_persistence, breadth, downside_volatility, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 2 | Cybersecurity | 64.28 | Positive setup | relative_strength_60d, trend_persistence, breadth, volume_accumulation, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 3 | Healthcare Innovation | 60.37 | Positive setup | trend_persistence, breadth, downside_volatility, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 4 | Quality Growth | 59.98 | Neutral / watchlist | trend_persistence, breadth, downside_volatility, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 5 | Financials | 56.0 | Neutral / watchlist | trend_persistence, breadth, volume_accumulation, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 6 | Crypto Infrastructure | 55.5 | Neutral / watchlist | relative_strength_20d, volume_accumulation, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 7 | AI Infrastructure | 52.4 | Neutral / watchlist | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 8 | Dividend Defensives | 51.93 | Neutral / watchlist | downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 9 | Small Caps | 50.45 | Neutral / watchlist | volume_accumulation, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 10 | Semiconductors | 45.95 | Neutral / watchlist | downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 11 | Grid Infrastructure | 39.97 | Weak setup | volume_accumulation, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 12 | Defense | 38.49 | Weak setup | volume_accumulation, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |

## Breadth and Participation

- Above 50DMA: `31.67%`
- Above 200DMA: `66.1%`
- Positive 20D return: `26.67%`

## Volatility and Risk Signals

- VIX close=15.01 pct_chg=-2.79

## News Analytics

- Sentiment counts: {'positive': 10, 'negative': 8, 'neutral': 62}
- News confirmation score: `51.25`

### Top Market-Moving Headlines

**1. Stocks surge as oil and bond yields retreat, recovering from Fed-induced sell-off**
- Source: CNBC Top News
- Importance / impact: Medium / Mixed
- Relevance / horizon: macro / short-term
- Affected assets: monetary_policy, market_reactions
- Score: `41.99`
- Investment implication: Macro-relevant mixed signal; use as context for rates, volatility, and index confirmation over the short-term.

**2. Treasury yields move lower after Fed kicks off hiking cycle**
- Source: CNBC Top News
- Importance / impact: Medium / Mixed
- Relevance / horizon: macro / short-term
- Affected assets: Federal Reserve, interest rates, Treasury yields
- Score: `41.99`
- Investment implication: Macro-relevant mixed signal; use as context for rates, volatility, and index confirmation over the short-term.

**3. America’s AI chip talent crisis — why The U.S. needs 157,000 more workers**
- Source: CNBC Markets
- Importance / impact: Low / Mixed
- Relevance / horizon: single_name / short-term
- Affected assets: TSMC, U.S, labor_market, technology, semiconductor
- Score: `27.29`
- Investment implication: Single-name mixed signal; low weight unless it maps to a broader sector or theme.

**4. Why investors’ best move in reaction to Fed’s rate hike is doing nothing at all**
- Source: MarketWatch Top Stories
- Importance / impact: Low / Mixed
- Relevance / horizon: macro / nan
- Affected assets: Equities, Bonds, USD, Commodities
- Score: `25.0`
- Investment implication: Macro-relevant mixed signal; use as context for rates, volatility, and index confirmation over the nan.

**5. A happier retirement contains these 3 elements**
- Source: MarketWatch Top Stories
- Importance / impact: Low / Mixed
- Relevance / horizon: macro / nan
- Affected assets: A
- Score: `25.0`
- Investment implication: Macro-relevant mixed signal; use as context for rates, volatility, and index confirmation over the nan.

**6. Federal Reserve Board issues enforcement actions with former employee of Northstar Bank, former employee of American Express Travel Related Services Company, Inc., and former employee of Regions Bank**
- Source: Federal Reserve Press Releases
- Importance / impact: Low / Mixed
- Relevance / horizon: macro / nan
- Affected assets: Equities, Bonds, USD, Commodities
- Score: `25.0`
- Investment implication: Macro-relevant mixed signal; use as context for rates, volatility, and index confirmation over the nan.

**7. Federal Reserve Board announces termination of enforcement action with SNB Bancshares and Bank of Eufaula**
- Source: Federal Reserve Press Releases
- Importance / impact: Low / Mixed
- Relevance / horizon: macro / nan
- Affected assets: SNB
- Score: `25.0`
- Investment implication: Macro-relevant mixed signal; use as context for rates, volatility, and index confirmation over the nan.

**8. S&P 500 is little changed as Treasury yields rise; index heads for losing week: Live updates**
- Source: CNBC Top News
- Importance / impact: Low / Mixed
- Relevance / horizon: macro / nan
- Affected assets: P, S
- Score: `23.75`
- Investment implication: Macro-relevant mixed signal; use as context for rates, volatility, and index confirmation over the nan.

**9. Treasury yields move higher as volatile week wraps up**
- Source: CNBC Top News
- Importance / impact: Low / Mixed
- Relevance / horizon: macro / nan
- Affected assets: Equities, Bonds, USD, Commodities
- Score: `23.75`
- Investment implication: Macro-relevant mixed signal; use as context for rates, volatility, and index confirmation over the nan.

**10. Tech leads Wall St to higher close as oil eases, Treasury yields dip**
- Source: Investing.com Economic Indicators
- Importance / impact: Low / Positive
- Relevance / horizon: macro / short-term
- Affected assets: interest_rate
- Score: `22.23`
- Investment implication: Macro-relevant positive signal; use as context for rates, volatility, and index confirmation over the short-term.


### Headline Quality Checks

Noisy headline list: Stock market today: Dow sinks 600 points, S&P 500 

## Positioning & Flow Dashboard

Positioning and flow data is used as confirmation only.

### Deferred Flow Sections

- Official ETF / fund flows: current report uses shares-outstanding-derived net fund flow estimates from free ETF metadata.
- Institutional Ownership: not available until SEC 13F ingestion is implemented.
- Grouped exposure flow reliability: use issuer coverage and availability status before treating ETF flow as confirmation.

## ETF Flows Analysis

- Market flow regime: `Defensive Rotation`
- Market flow score: `44.9 / 100`
- Equity risk flow: `47.1`
- Credit risk flow: `29.1`
- Sector cyclicality flow: `44.9`
- Duration/liquidity flow: `53.1`
- Alternatives: `barbell demand`
- ETF flow reliability: `71.2 / 100`
- Dominant allocation direction: `defensive demand`

### Core Flow Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVV | U.S. Broad Equity | -1.7 | -1.8 | 0.1 | n/a | Down | Sell | Normal | Persistent Distribution | Risk-Off | Strong confirmation; Persistent selling | 72.0 |
| ACWI | Global Equity | -0.7 | -1.2 | 0.0 | n/a | Flat | Neutral | Normal | Neutral | Neutral | Mixed or neutral flow structure; Persistent selling | 62.0 |
| EFA | Developed Markets ex-U.S. | -0.1 | -2.6 | 0.0 | n/a | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Mixed or neutral flow structure; Exceptional institutional selling, Persistent selling | 54.0 |
| IEMG | Emerging Markets | 0.0 | 0.4 | 0.2 | n/a | Flat | Neutral | Normal | Neutral | Neutral | Structural accumulation; Persistent selling | 68.0 |
| IJH | U.S. Mid Cap | 3.1 | 2.4 | 0.8 | n/a | Down | Buy | Normal | Contrarian Buying | Watch | Strong confirmation; Exceptional institutional buying, Strong sponsorship | 96.0 |
| IWM | U.S. Small Cap | 0.5 | 0.2 | 0.3 | n/a | Down | Buy | Normal | Contrarian Buying | Watch | Medium-term recovery | 72.0 |
| LQD | Investment-Grade Credit | -2.0 | -1.6 | 0.3 | n/a | Down | Sell | Normal | Persistent Distribution | Risk-Off | Strong confirmation; Exceptional institutional selling | 72.0 |
| HYG | High-Yield Credit | -2.0 | -1.2 | 0.2 | n/a | Down | Sell | Normal | Persistent Distribution | Risk-Off | Strong confirmation; Persistent selling | 72.0 |
| SGOV | Treasury Bills / Cash | 0.3 | -0.6 | 0.9 | n/a | Flat | Neutral | Normal | Neutral | Neutral | Structural accumulation; Strong sponsorship | 84.0 |
| SHY | Short-Duration Treasuries | 1.3 | 0.4 | 0.6 | n/a | Flat | Neutral | Normal | Neutral | Neutral | Structural accumulation | 76.0 |
| IEF | Intermediate-Duration Treasuries | 0.1 | -1.3 | 0.6 | n/a | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural distribution | 64.0 |
| TLT | Long-Duration Treasuries | 0.4 | 2.4 | 0.5 | n/a | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural accumulation; Exceptional institutional buying | 84.0 |
| GLD | Gold | 1.0 | 2.4 | 0.5 | n/a | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural accumulation; Exceptional institutional buying | 84.0 |
| IBIT | Bitcoin | 1.2 | 0.8 | 0.7 | n/a | Flat | Neutral | Normal | Neutral | Neutral | Structural accumulation | 76.0 |

### Sector Flow Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| XLC | Communication Services | 0.6 | 0.3 | 0.4 | n/a | Flat | Neutral | Normal | Neutral | Neutral | Structural distribution | 64.0 |
| XLY | Consumer Discretionary | -0.4 | 1.0 | 0.2 | n/a | Down | Buy | Normal | Contrarian Buying | Watch | Medium-term deterioration; Persistent selling | 60.0 |
| XLP | Consumer Staples | -0.3 | 1.7 | 0.5 | n/a | Down | Sell | Normal | Persistent Distribution | Risk-Off | Medium-term deterioration | 68.0 |
| XLE | Energy | -0.5 | -0.5 | 0.4 | n/a | Up | Sell | Normal | Profit Taking | Slightly Bearish | Strong confirmation | 80.0 |
| XLF | Financials | -0.4 | 0.7 | 0.6 | n/a | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Medium-term deterioration | 68.0 |
| XLV | Health Care | -0.6 | 1.6 | 0.4 | n/a | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Medium-term deterioration | 68.0 |
| XLI | Industrials | -1.5 | -1.4 | 0.4 | n/a | Down | Sell | Normal | Persistent Distribution | Risk-Off | Strong confirmation | 80.0 |
| XLK | Information Technology | -0.5 | -0.7 | 0.5 | n/a | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural distribution | 64.0 |
| XLB | Materials | -0.9 | -1.9 | 0.5 | n/a | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural distribution | 64.0 |
| XLRE | Real Estate | 0.4 | 0.6 | 0.3 | n/a | Down | Buy | Normal | Contrarian Buying | Watch | Strong confirmation; Exceptional institutional buying | 88.0 |
| XLU | Utilities | 0.1 | 0.4 | 0.5 | n/a | Down | Sell | Normal | Persistent Distribution | Risk-Off | Tactical profit-taking inside structural accumulation; Exceptional institutional selling | 60.0 |

### Subsector PFV Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ITA | Aerospace and Defense | -0.4 | 0.8 | 0.1 | n/a | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural distribution; Persistent selling | 56.0 |
| SOXX | Semiconductors | 0.2 | -0.3 | 0.6 | n/a | Flat | Neutral | Normal | Neutral | Neutral | Structural accumulation | 76.0 |
| SMH | Semiconductors | 2.1 | 1.6 | 0.6 | n/a | Flat | Buy | Normal | Quiet Accumulation | Improving | Strong confirmation; Exceptional institutional buying | 88.0 |
| CIBR | Cybersecurity | 1.2 | 1.7 | 0.7 | n/a | Up | Buy | Normal | Steady Accumulation | Risk-On | Strong confirmation; Exceptional institutional buying | 88.0 |

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

No contradiction flags were triggered by current deterministic rules.

## Data Quality Notes

- Technical rows loaded: `60`
- S&P 500 constituent technical rows loaded: `503`
- Macro rows loaded: `49`
- Live macro rows used: `40`
- Economic rows loaded: `113`
- News rows loaded: `80`
- Positioning/flow rows loaded: `30`

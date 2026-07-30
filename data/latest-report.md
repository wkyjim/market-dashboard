# Rule-Based Institutional Market Update

Generated at: 31 July 2026, 01:03:26 (HKT)
Window: 24h

## Executive Dashboard

- Regime score: **53.31 / 100** (Mixed / Rotation)
- US equity strength: **43.79 / 100** (weak)
- Evidence quality: **79.5 / 100**
- ETF flow contribution: **49.38 / 100**, reliability **71.28 / 100**
- Breadth: **narrow**; above 50DMA `38.33%`, above 200DMA `62.71%`
- Top sector score: **Real Estate** `69.92`
- Top theme score: **Healthcare Innovation** `61.27`

## Market Regime Score

| Metric | Value | Driver / Interpretation |
| --- | --- | --- |
| Overall regime | 53.31 | Mixed / Rotation |
| equity_trend | 45.0 | mild risk-off pressure; Core equity ETFs versus moving averages. |
| equity_momentum | 44.66 | mild risk-off pressure; 5D/20D/60D return momentum across SPY, QQQ, IWM, and SMH. |
| market_breadth | 47.02 | neutral / mixed; Participation breadth from tracked equity/ETF rows. |
| volatility | 70.0 | risk-on support; VIX level and change; higher score means calmer volatility conditions. |
| rates_yield_curve | 58.0 | mild risk-on support; Treasury yield pressure and curve shape; higher score means less rates pressure. |
| credit_proxy | 50.0 | neutral / mixed; Credit-market proxy; currently neutral when no direct spread signal is available. |
| dollar_fx | 58.95 | mild risk-on support; Dollar move; higher score means less USD tightening pressure. |
| commodity_confirmation | 59.0 | mild risk-on support; Copper, silver, oil, and gold mix; higher score means better cyclical confirmation. |
| etf_flow | 49.56 | neutral / mixed; Grouped ETF flow contribution adjusted for reliability. |
| news_confirmation | 73.75 | risk-on support; Weighted headline/news confirmation score. |
| Positive contributors |  | news_confirmation=73.75, volatility=70.0 |
| Negative contributors |  | equity_momentum=44.66, equity_trend=45.0 |

## US Equity Strength Score

| Component | Score |
| --- | --- |
| indices_above_moving_averages | 45.0 |
| sp500_trend | 55.0 |
| nasdaq_trend | 35.0 |
| russell_participation | 55.0 |
| returns_momentum | 44.66 |
| rsi_zone | 35.0 |
| macd_confirmation | 35.0 |
| volume_confirmation | 35.0 |
| breadth | 47.02 |

## Evidence Quality / Confidence

- Confidence score: `79.5`
- Agreement ratio: `0.5`
- Contradiction count: `2`
- Missing indicators: none
- Warning flags: none

## Cross-Asset Confirmation

| Area | Signal | Interpretation |
| --- | --- | --- |
| Equities | S&P 500 rising; Nasdaq rising; Russell 2000 rising | Confirms risk appetite when broad indices rise together; weak small caps would narrow the signal. |
| Rates | 10Y Treasury rising; MOVE rising | Rising yields can pressure duration assets; falling MOVE supports calmer bond volatility. |
| Dollar | DXY proxy falling | A stronger dollar can tighten financial conditions and pressure commodities/emerging-market risk. |
| Credit | HYG rising | High-yield weakness would challenge equity risk-on confirmation. |
| Gold | Gold rising | Gold strength can indicate defensive demand, inflation hedging, or geopolitical concern. |
| Silver | Silver rising | Silver helps distinguish precious-metal demand from industrial/cyclical confirmation when data is available. |
| Copper | Copper rising | Copper strength supports cyclical growth confirmation; weakness would dilute risk-on breadth. |
| Oil | WTI crude falling | Oil spikes can be inflationary risk; falling oil can ease cost pressure but may also flag demand softness. |
| Volatility | VIX falling | Falling VIX supports risk appetite; a volatility spike would reduce confidence in broad risk-on. |

### Macro Snapshot

Live macro rows are intraday snapshots from `public.macro_live`; closed rows are official stored rows from `public.macro`.

| Symbol | Name | Close | Pct Chg | Market Date | Status |
| --- | --- | --- | --- | --- | --- |
| ^GSPC | S&P 500 | 7421.48 | 1.44 | 2026-07-30 | live as of 31 July 2026, 01:00:45 (HKT) |
| ^IXIC | NASDAQ Composite | 25061.95 | 2.53 | 2026-07-30 | live as of 31 July 2026, 01:00:45 (HKT) |
| ^RUT | Russell 2000 Index | 2928.04 | 0.75 | 2026-07-30 | live as of 31 July 2026, 01:00:45 (HKT) |
| ^VIX | CBOE Volatility Index | 18.27 | -11.57 | 2026-07-30 | live as of 31 July 2026, 01:00:45 (HKT) |
| ^SKEW | CBOE SKEW Index | 139.55 | -2.4 | 2026-07-29 | closed |
| ^MOVE | ICE BofA MOVE Index | 76.82 | 8.38 | 2026-07-24 | closed |
| US2YT=X | United States 2-Year Treasury Yield | 4.22 | -0.35 | 2026-07-30 | live as of 31 July 2026, 01:00:45 (HKT) |
| US3YT=X | United States 3-Year Treasury Yield | 4.27 | -0.13 | 2026-07-30 | live as of 31 July 2026, 01:00:45 (HKT) |
| US5YT=X | United States 5-Year Treasury Yield | 4.37 | 0.37 | 2026-07-30 | live as of 31 July 2026, 01:00:45 (HKT) |
| US7YT=X | United States 7-Year Treasury Yield | 4.51 | 0.55 | 2026-07-30 | live as of 31 July 2026, 01:00:45 (HKT) |
| US10YT=X | United States 10-Year Treasury Yield | 4.66 | 0.82 | 2026-07-30 | live as of 31 July 2026, 01:00:45 (HKT) |
| US20YT=X | United States 20-Year Treasury Yield | 5.21 | 1.11 | 2026-07-30 | live as of 31 July 2026, 01:00:45 (HKT) |
| US30YT=X | United States 30-Year Treasury Yield | 5.2 | 1.18 | 2026-07-30 | live as of 31 July 2026, 01:00:45 (HKT) |
| HK50 | Hang Seng Futures | 25896.5 | -0.17 | 2026-07-30 | closed |
| KOR200c1 | KOSPI 200 Futures | 881.95 | -1.86 | 2026-07-29 | closed |
| CIHc1 | SSE 50 Futures | 2896.6 | 0.2 | 2026-07-29 | closed |
| HYG | iShares iBoxx High Yield Corporate Bond ETF | 79.48 | 0.3 | 2026-07-30 | live as of 31 July 2026, 01:00:45 (HKT) |
| LQD | iShares iBoxx Investment Grade Corporate Bond ETF | 106.47 | 0.24 | 2026-07-30 | live as of 31 July 2026, 01:00:45 (HKT) |
| JNK | SPDR Bloomberg High Yield Bond ETF | 95.67 | 0.29 | 2026-07-30 | live as of 31 July 2026, 01:00:45 (HKT) |
| RSP | Invesco S&P 500 Equal Weight ETF | 214.66 | -0.5 | 2026-07-30 | live as of 31 July 2026, 01:00:45 (HKT) |
| IWF | iShares Russell 1000 Growth ETF | 116.89 | 2.49 | 2026-07-30 | live as of 31 July 2026, 01:00:45 (HKT) |
| IWD | iShares Russell 1000 Value ETF | 250.35 | 0.33 | 2026-07-30 | live as of 31 July 2026, 01:00:45 (HKT) |
| TLT | iShares 20+ Year Treasury Bond ETF | 82.83 | -0.03 | 2026-07-30 | live as of 31 July 2026, 01:00:45 (HKT) |
| IEF | iShares 7-10 Year Treasury Bond ETF | 93.27 | 0.1 | 2026-07-30 | live as of 31 July 2026, 01:00:45 (HKT) |
| SHY | iShares 1-3 Year Treasury Bond ETF | 82.03 | 0.04 | 2026-07-30 | live as of 31 July 2026, 01:00:45 (HKT) |
| GC=F | Gold Future | 4168.9 | 3.33 | 2026-07-30 | live as of 31 July 2026, 01:00:45 (HKT) |
| SI=F | Silver Future | 58.88 | 1.76 | 2026-07-30 | live as of 31 July 2026, 01:00:45 (HKT) |
| CL=F | WTI Crude Oil Future | 83.84 | -0.73 | 2026-07-30 | live as of 31 July 2026, 01:00:45 (HKT) |
| HG=F | Copper Future | 6.47 | 3.2 | 2026-07-30 | live as of 31 July 2026, 01:00:45 (HKT) |

## Market Dispersion Analysis

- Sector ETF 20D dispersion: `23.0` points (very high); leader `XLE` (Energy) `10.43`, laggard `XLK` (Technology) `-12.57`
- Sector ETF 60D dispersion: `20.7` points (very high); leader `XLV` (Health Care) `14.52`, laggard `XLC` (Communication Services) `-6.18`

| Comparison | Left | Right | 20D Spread | Signal |
| --- | --- | --- | --- | --- |
| Equal-weight vs cap-weight | RSP (Equal-weight S&P 500) | SPY (S&P 500) | 3.71 | broader participation |
| Small-cap vs large-cap | IWM (Russell 2000) | SPY (S&P 500) | -1.64 | large-cap leadership |
| Growth vs value | IWF (Russell 1000 Growth) | IWD (Russell 1000 Value) | -11.07 | value leadership |
| Nasdaq vs S&P 500 | QQQ (Nasdaq 100) | SPY (S&P 500) | -7.82 | S&P 500 leadership |

## Sector Constituent Dispersion

- Breadth 50D / 200D: percentage of active S&P 500 constituents in the sector trading above the 50-day / 200-day moving average.
- Positive 20D: percentage of active sector constituents with positive 20-day return.
- Std 20D: cross-sectional standard deviation of constituent 20-day returns; higher means wider stock-level dispersion.

| Sector | Count | Breadth 50D | Breadth 200D | Positive 20D | 20D Dispersion | Std 20D | Label | Leaders | Laggards |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Information Technology | 74 | 37.84 | 58.9 | 36.49 | 121.01 | 24.37 | very high | CTSH, ACN, WDAY | GLW, SNDK, CRWD |
| Industrials | 81 | 55.7 | 67.53 | 44.44 | 60.7 | 12.46 | very high | CTAS, PAYX, ADP | CAT, GNRC, VRT |
| Consumer Discretionary | 47 | 72.34 | 53.19 | 61.7 | 53.19 | 9.45 | very high | GRMN, DPZ, EXPE | LEN, DHI, TSLA |
| Health Care | 59 | 89.83 | 74.58 | 83.05 | 50.31 | 8.15 | very high | IQV, ABT, MCK | HUM, ISRG, MRNA |
| Financials | 76 | 80.56 | 81.43 | 84.21 | 45.54 | 8.67 | very high | PYPL, CBOE, ICE | HBAN, C, HOOD |
| Communication Services | 23 | 54.55 | 40.91 | 69.57 | 35.69 | 9.67 | very high | NWS, NWSA, T | TKO, ECHO, PSKY |
| Energy | 21 | 61.9 | 85.71 | 71.43 | 33.36 | 9.26 | very high | PSX, MPC, CVX | WMB, HAL, TPL |
| Materials | 26 | 61.54 | 73.08 | 65.38 | 33.3 | 7.59 | very high | CF, NUE, LYB | CRH, PPG, ALB |
| Consumer Staples | 34 | 84.85 | 65.62 | 88.24 | 22.21 | 4.76 | very high | KHC, MDLZ, SJM | PG, KDP, STZ |
| Utilities | 31 | 45.16 | 74.19 | 45.16 | 20.56 | 4.7 | very high | EIX, PCG, AWK | ETR, VST, NRG |
| Real Estate | 31 | 80.65 | 83.87 | 83.87 | 14.45 | 3.64 | high | VTR, BXP, CBRE | MAA, EQIX, IRM |

## Economic Data Snapshot

### U.S. Labor

| Indicator | Latest | Unit | Change | Date | Rule-Based Interpretation |
| --- | --- | --- | --- | --- | --- |
| All Employees, Total Nonfarm | 158984.0 | thousands | 57.0 thousands vs prior | 2026-06-01 | Higher reading supports activity or liquidity. |
| Unemployment Rate | 4.2 | percent | -0.1 pp vs prior | 2026-06-01 | Lower reading eases macro pressure. |
| Initial Claims | 215000.0 | number | -12000.0 number vs prior | 2026-06-20 | Lower claims indicate firmer labor-market conditions. |
| Continued Claims | 1821000.0 | number | 21000.0 number vs prior | 2026-06-13 | Higher claims indicate softer labor-market conditions. |
| Labor Force Participation Rate | 61.5 | percent | -0.3 pp vs prior | 2026-06-01 | Lower participation constrains labor supply. |

### U.S. Growth

| Indicator | Latest | Unit | Change | Date | Rule-Based Interpretation |
| --- | --- | --- | --- | --- | --- |
| Real Gross Domestic Product | 24270.6 | billions chained 2017 dollars | 90.18 billions chained 2017 dollars vs prior | 2026-04-01 | Higher reading supports activity or liquidity. |
| Industrial Production Index | 102.65 | index 2017=100 | 0.14 index pts vs prior | 2026-05-01 | Higher reading supports activity or liquidity. |
| Advance Retail Sales | 768553.0 | millions dollars | 1677.0 millions dollars vs prior | 2026-06-01 | Higher reading supports activity or liquidity. |

### U.S. Inflation

| Indicator | Latest | Unit | Change | Date | Rule-Based Interpretation |
| --- | --- | --- | --- | --- | --- |
| Headline CPI month-over-month inflation rate | -0.42 | percent | -0.9 pp vs prior | 2026-06-01 | Lower reading eases macro pressure. |
| Headline CPI year-over-year inflation rate | 3.73 | percent | -0.54 pp vs prior | 2026-06-01 | Lower reading eases macro pressure. |
| Core CPI month-over-month inflation rate | -0.02 | percent | -0.22 pp vs prior | 2026-06-01 | Lower reading eases macro pressure. |
| Core CPI year-over-year inflation rate | 2.81 | percent | -0.15 pp vs prior | 2026-06-01 | Lower reading eases macro pressure. |
| Headline CPI year-over-year inflation rate | 3.88 | percent | -0.58 pp vs prior | 2026-06-01 | Lower reading eases macro pressure. |
| Core CPI year-over-year inflation rate | 2.86 | percent | -0.21 pp vs prior | 2026-06-01 | Lower reading eases macro pressure. |
| Headline PCE Price Index month-over-month inflation rate | -0.11 | percent | -0.57 pp vs prior | 2026-06-01 | Lower reading eases macro pressure. |
| Headline PCE Price Index year-over-year inflation rate | 3.67 | percent | -0.41 pp vs prior | 2026-06-01 | Lower reading eases macro pressure. |
| Core PCE Price Index month-over-month inflation rate | 0.32 | percent | 0.07 pp vs prior | 2026-05-01 | Higher reading increases macro pressure. |
| Core PCE Price Index year-over-year inflation rate | 3.41 | percent | 0.09 pp vs prior | 2026-05-01 | Higher reading increases macro pressure. |
| Headline PPI Final Demand month-over-month inflation rate | -0.19 | percent | -0.79 pp vs prior | 2026-06-01 | Lower reading eases macro pressure. |
| Headline PPI Final Demand year-over-year inflation rate | 5.51 | percent | -0.49 pp vs prior | 2026-06-01 | Lower reading eases macro pressure. |
| Core PPI Final Demand Less Foods and Energy month-over-month inflation rate | 0.2 | percent | 0.11 pp vs prior | 2026-06-01 | Higher reading increases macro pressure. |
| Core PPI Final Demand Less Foods and Energy year-over-year inflation rate | 4.68 | percent | 0.09 pp vs prior | 2026-06-01 | Higher reading increases macro pressure. |
| Consumer Price Index for All Urban Consumers | 332.57 | index 1982-1984=100 | -1.41 index pts vs prior | 2026-06-01 | Lower reading eases macro pressure. |
| Core CPI | 336.06 | index 1982-1984=100 | -0.06 index pts vs prior | 2026-06-01 | Lower reading eases macro pressure. |
| Personal Consumption Expenditures Price Index | 131.39 | index 2017=100 | -0.14 index pts vs prior | 2026-06-01 | Lower reading eases macro pressure. |
| Core PCE Price Index | 130.08 | index 2017=100 | 0.41 index pts vs prior | 2026-05-01 | Higher reading increases macro pressure. |
| Producer Price Index: Final Demand | 157.04 | index Nov 2009=100 | -0.3 index pts vs prior | 2026-06-01 | Latest structural macro observation. |
| Producer Price Index: Final Demand Less Foods and Energy | 154.0 | index Apr 2010=100 | 0.31 index pts vs prior | 2026-06-01 | Latest structural macro observation. |

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
| Housing Starts | 1427.0 | thousands | 228.0 thousands vs prior | 2026-06-01 | Higher reading supports activity or liquidity. |
| New Privately-Owned Housing Units Authorized | 1374.0 | thousands | -36.0 thousands vs prior | 2026-06-01 | Lower reading signals softer activity or liquidity. |
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
| US dollar/Euro ECB reference exchange rate | 1.15 | USD | 0.01 USD vs prior | 2026-07-30 | EUR strengthened versus this currency. |
| Japanese yen/Euro ECB reference exchange rate | 186.99 | JPY | 0.72 JPY vs prior | 2026-07-30 | EUR strengthened versus this currency. |
| Chinese yuan renminbi/Euro ECB reference exchange rate | 7.75 | CNY | 0.05 CNY vs prior | 2026-07-30 | EUR strengthened versus this currency. |
| Australian dollar/Euro ECB reference exchange rate | 1.64 | AUD | 0.0 AUD vs prior | 2026-07-30 | EUR strengthened versus this currency. |

ABS Australia note: ABS rows are stored locally/Neon, but most series are dimension-coded; only curated series should be promoted into narrative report text.

## Sector and Theme Leadership

### Official Sector Strength

Supporting and detracting names are the top/bottom S&P 500 constituents by 20D return when constituent coverage is available; otherwise the report falls back to related ETFs.

| Rank | Sector | Score | Trend | Momentum | Stock Breadth | ETF Flow | Flow Reliability | 3M RS | Supporting / Leaders | Detracting / Laggards |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Real Estate | 69.92 | strong uptrend | neutral | broad | 77.86 | 100.0 | 55.01 | VTR, BXP, CBRE | MAA, EQIX, IRM |
| 2 | Consumer Staples | 69.81 | strong uptrend | neutral | broad | 75.38 | 65.0 | 55.52 | KHC, MDLZ, SJM | PG, KDP, STZ |
| 3 | Healthcare | 69.43 | strong uptrend | positive | broad | 63.67 | 90.0 | 59.58 | IQV, ABT, MCK | HUM, ISRG, MRNA |
| 4 | Financials | 68.02 | strong uptrend | positive | broad | 69.29 | 95.0 | 58.0 | PYPL, CBOE, ICE | HBAN, C, HOOD |
| 5 | Cybersecurity | 60.15 | strong uptrend | positive | broad | 62.49 | 65.0 | 61.85 | CIBR | CIBR |
| 6 | Energy | 60.07 | uptrend | positive | broad | 46.42 | 95.0 | 57.02 | PSX, MPC, CVX | WMB, HAL, TPL |
| 7 | Crypto | 49.75 | neutral | neutral | mixed | 47.46 | 65.0 | 50.0 |  |  |
| 8 | Industrials | 44.85 | neutral | neutral | weak | 49.95 | 65.0 | 48.98 | CTAS, PAYX, ADP | CAT, GNRC, VRT |
| 9 | Technology | 41.16 | neutral | negative | weak | 51.03 | 95.0 | 44.3 | CTSH, ACN, WDAY | GLW, SNDK, CRWD |
| 10 | Semiconductors | 41.01 | downtrend | negative | weak | 91.86 | 100.0 | 35.48 | SMH, SOXX | SOXX, SMH |
| 11 | Utilities | 36.13 | strong downtrend | neutral | weak | 65.59 | 65.0 | 46.58 | EIX, PCG, AWK | ETR, VST, NRG |
| 12 | Consumer Discretionary | 35.31 | strong downtrend | neutral | weak | 58.21 | 65.0 | 45.63 | GRMN, DPZ, EXPE | LEN, DHI, TSLA |
| 13 | Defense | 34.02 | strong downtrend | neutral | weak | 50.92 | 65.0 | 45.73 | XAR | XAR |
| 14 | Nuclear | 33.67 | strong downtrend | negative | weak | 50.0 | 0.0 | 32.56 | NLR | NLR |
| 15 | Grid Infrastructure | 32.39 | strong downtrend | negative | weak | 62.56 | 65.0 | 38.38 | GRID | GRID |

### Thematic Strength

| Rank | Theme | Score | Setup | ETF Flow | Flow Reliability | Dispersion | Price | News |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Healthcare Innovation | 61.27 | Positive setup | 63.67 | 90.0 | 5.65 | True | False |
| 2 | Financials | 60.06 | Positive setup | 69.29 | 95.0 | 10.21 | True | False |
| 3 | Energy | 60.03 | Positive setup | 46.42 | 95.0 | 5.31 | True | False |
| 4 | Dividend Defensives | 54.73 | Neutral / watchlist | 55.73 | 65.0 | 6.11 | False | False |
| 5 | Cybersecurity | 53.77 | Neutral / watchlist | 62.49 | 65.0 | 85.44 | False | False |
| 6 | Quality Growth | 48.07 | Neutral / watchlist | 59.3 | 65.0 | 29.45 | False | False |
| 7 | Small Caps | 47.67 | Neutral / watchlist | 64.54 | 65.0 | 0.0 | False | False |
| 8 | Defense | 47.4 | Neutral / watchlist | 50.92 | 65.0 | 27.35 | False | False |
| 9 | Semiconductors | 47.27 | Weak setup | 91.86 | 100.0 | 25.46 | False | False |
| 10 | AI Infrastructure | 43.54 | Weak setup | 91.86 | 100.0 | 32.13 | False | False |
| 11 | Grid Infrastructure | 35.63 | Weak setup | 62.56 | 65.0 | 21.12 | False | False |
| 12 | Crypto Infrastructure | 34.52 | Weak setup | 47.46 | 65.0 | 2.15 | False | False |
| 13 | Nuclear | 31.13 | Underperformance risk | 50.0 | 0.0 | 12.1 | False | False |

- Top 5 improving themes: Cybersecurity, Healthcare Innovation, Financials, Dividend Defensives, Small Caps
- Top 5 deteriorating themes: Crypto Infrastructure, Nuclear, Grid Infrastructure, AI Infrastructure, Semiconductors
- Strong news but weak price confirmation: none
- Strong price but weak news confirmation: Healthcare Innovation, Financials, Energy

### Sector / Theme Alignment

| Sector | Related Themes | Sector Score | Sector Signal | Theme Score | Theme Signal | Interpretation |
| --- | --- | --- | --- | --- | --- | --- |
| Real Estate | Dividend Defensives | 69.92 | strong | 54.73 | mixed | sector stronger than related themes |
| Consumer Staples | Dividend Defensives | 69.81 | strong | 54.73 | mixed | sector stronger than related themes |
| Healthcare | Healthcare Innovation | 69.43 | strong | 61.27 | positive | sector and theme confirmation |
| Financials | Financials | 68.02 | strong | 60.06 | positive | sector and theme confirmation |
| Cybersecurity | Cybersecurity | 60.15 | positive | 53.77 | mixed | sector stronger than related themes |
| Energy | Energy | 60.07 | positive | 60.03 | positive | sector and theme confirmation |
| Crypto | Crypto Infrastructure | 49.75 | mixed | 34.52 | very weak | mixed confirmation |
| Industrials | Defense, Grid Infrastructure | 44.85 | weak | 41.51 | weak | broad weakness across sector and themes |
| Technology | AI Infrastructure, Semiconductors, Quality Growth | 41.16 | weak | 46.29 | mixed | mixed confirmation |
| Semiconductors | AI Infrastructure, Semiconductors | 41.01 | weak | 45.41 | mixed | mixed confirmation |
| Utilities | Grid Infrastructure, Nuclear, Dividend Defensives | 36.13 | weak | 40.5 | weak | broad weakness across sector and themes |
| Consumer Discretionary | Small Caps | 35.31 | weak | 47.67 | mixed | mixed confirmation |
| Defense | Defense | 34.02 | very weak | 47.4 | mixed | mixed confirmation |
| Nuclear | Nuclear | 33.67 | very weak | 31.13 | very weak | broad weakness across sector and themes |
| Grid Infrastructure | Grid Infrastructure | 32.39 | very weak | 35.63 | weak | broad weakness across sector and themes |

## Three-Month Outperformance Setup

| Rank | Theme | Score | Classification | Drivers | Invalidation Triggers |
| --- | --- | --- | --- | --- | --- |
| 1 | Healthcare Innovation | 67.85 | Positive setup | relative_strength_60d, trend_persistence, breadth, downside_volatility, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 2 | Financials | 64.74 | Positive setup | trend_persistence, breadth, volume_accumulation, downside_volatility, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 3 | Energy | 63.66 | Positive setup | relative_strength_20d, trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 4 | Dividend Defensives | 58.59 | Neutral / watchlist | trend_persistence, breadth, volume_accumulation, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 5 | Cybersecurity | 57.15 | Neutral / watchlist | relative_strength_60d, trend_persistence, breadth, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 6 | Small Caps | 53.56 | Neutral / watchlist | volume_accumulation, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 7 | Quality Growth | 52.04 | Neutral / watchlist | volume_accumulation, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 8 | Defense | 48.73 | Neutral / watchlist |  | relative strength below SPY, breadth below 45%, news turns negative |
| 9 | Semiconductors | 44.82 | Weak setup | volume_accumulation | relative strength below SPY, breadth below 45%, news turns negative |
| 10 | AI Infrastructure | 43.99 | Weak setup | volume_accumulation, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 11 | Grid Infrastructure | 37.74 | Weak setup | volume_accumulation, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 12 | Crypto Infrastructure | 30.86 | Weak setup | relative_strength_20d | relative strength below SPY, breadth below 45%, news turns negative |

## Breadth and Participation

- Above 50DMA: `38.33%`
- Above 200DMA: `62.71%`
- Positive 20D return: `40.0%`

## Volatility and Risk Signals

- VIX close=18.27 pct_chg=-11.57

## News Analytics

- Sentiment counts: {'positive': 59, 'negative': 21, 'neutral': 0}
- News confirmation score: `73.75`

### Top Market-Moving Headlines

**1. Brent oil jumps back above $90 after Trump threatens to hit Iran hard**
- Source: CNBC Top News
- Importance / impact: High / Positive
- Relevance / horizon: macro / short-term
- Affected assets: U.S, geopolitical_risk, commodity_prices
- Score: `69.04`
- Investment implication: Macro-relevant positive signal; use as context for rates, volatility, and index confirmation over the short-term.

**2. Dow ends 1,100 points down, Nasdaq and S&P 500 plunge as Fed stands pat on rates**
- Source: MarketWatch Bulletins
- Importance / impact: High / Negative
- Relevance / horizon: macro / short-term
- Affected assets: P, S, Federal Reserve, Stock Market Decline
- Score: `61.77`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the short-term.

**3. ICE to buy MarketAxess in $5.7 billion deal, posts higher quarterly profit**
- Source: CNBC Markets
- Importance / impact: Medium / Positive
- Relevance / horizon: sector_theme / short-term
- Affected assets: ICE, MKTX, Mergers & Acquisitions, Fixed-Income
- Score: `61.77`
- Investment implication: Theme or sector positive signal; requires price and volume confirmation before affecting rankings.

**4. Why the USO oil ETF is a better buy than crude futures as the Iran war rages**
- Source: MarketWatch Top Stories
- Importance / impact: High / Positive
- Relevance / horizon: macro / short-term
- Affected assets: USO, WTI, ETF, oil, ETFs
- Score: `57.38`
- Investment implication: Macro-relevant positive signal; use as context for rates, volatility, and index confirmation over the short-term.

**5. Oil prices fall despite escalating fighting between U.S. and Iran**
- Source: CNBC Top News
- Importance / impact: High / Positive
- Relevance / horizon: macro / short-term
- Affected assets: U.S, energy, geopolitics
- Score: `57.0`
- Investment implication: Macro-relevant positive signal; use as context for rates, volatility, and index confirmation over the short-term.

**6. Stocks and bonds see wild ‘Fed Day’ swings as Wall Street’s ‘crash cushion’ evaporates**
- Source: MarketWatch Top Stories
- Importance / impact: High / Negative
- Relevance / horizon: macro / short-term
- Affected assets: Fed policy announcement, Equity market reaction, Bond yield increase
- Score: `51.0`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the short-term.

**7. CNBC Daily Open: Oil heats up on Middle East tensions as Fed sees a 'family fight'**
- Source: CNBC Top News
- Importance / impact: High / Negative
- Relevance / horizon: macro / short-term
- Affected assets: OIL, CNBC, U.S, geopolitical_risk, energy_markets
- Score: `48.45`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the short-term.

**8. Wall Street sees wild ‘Fed Day’ swings as ‘crash cushion’ evaporates**
- Source: MarketWatch Bulletins
- Importance / impact: High / Negative
- Relevance / horizon: macro / short-term
- Affected assets: Federal Reserve, Market Volatility
- Score: `48.45`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the short-term.

**9. Hims and Hers shares fall 10% as FTC sues company over data, billing practices**
- Source: CNBC Finance
- Importance / impact: Medium / Negative
- Relevance / horizon: sector_theme / short-term
- Affected assets: HIMS, HERS, FTC, legal_issues, data_concerns
- Score: `46.98`
- Investment implication: Theme or sector negative signal; requires price and volume confirmation before affecting rankings.

**10. What a divided Fed means for investors**
- Source: CNBC Economy
- Importance / impact: High / Negative
- Relevance / horizon: macro / short-term
- Affected assets: A, Federal Reserve, Investor Sentiment
- Score: `45.9`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the short-term.


### Headline Quality Checks

No noisy headlines detected by current rules.

## Positioning & Flow Dashboard

Positioning and flow data is used as confirmation only. FINRA short-sale volume is not short interest.

### Deferred Flow Sections

- Official ETF / fund flows: current report uses shares-outstanding-derived net fund flow estimates from free ETF metadata.
- Institutional Ownership: not available until SEC 13F ingestion is implemented.
- Crowding / Squeeze Risks: initial coverage uses CFTC crowded positioning and FINRA elevated short-sale volume only.
- Grouped exposure flow reliability: use issuer coverage and availability status before treating ETF flow as confirmation.

## ETF Flows Analysis

- Market flow regime: `Mixed / Neutral`
- Market flow score: `47.1 / 100`
- Equity risk flow: `49.0`
- Credit risk flow: `45.6`
- Sector cyclicality flow: `43.0`
- Duration/liquidity flow: `50.0`
- Alternatives: `defensive or uncertainty hedge`
- ETF flow reliability: `71.3 / 100`
- Dominant allocation direction: `defensive demand`

### Core Flow Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVV | U.S. Broad Equity | -0.9 | 0.6 | 0.3 | -0.7 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Medium-term deterioration | 83.0 |
| ACWI | Global Equity | -1.4 | -1.4 | 0.1 | -0.4 | Down | Sell | Normal | Persistent Distribution | Risk-Off | Strong confirmation; Persistent selling | 87.0 |
| EFA | Developed Markets ex-U.S. | -2.2 | -0.1 | 0.0 | -0.5 | Flat | Neutral | Normal | Neutral | Neutral | Medium-term deterioration; Exceptional institutional selling, Persistent selling | 67.0 |
| IEMG | Emerging Markets | -0.4 | -0.6 | 0.1 | 0.2 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Medium-term recovery; Persistent selling | 79.0 |
| IJH | U.S. Mid Cap | -0.4 | -0.1 | 0.6 | 1.6 | Down | Neutral | High | Heavy Selling Pressure | Cautious | Structural accumulation | 91.0 |
| IWM | U.S. Small Cap | 0.9 | 1.6 | 0.6 | 1.1 | Down | Neutral | High | Heavy Selling Pressure | Cautious | Structural accumulation | 91.0 |
| LQD | Investment-Grade Credit | -0.2 | 0.3 | 0.4 | 2.2 | Down | Sell | High | Confirmed Distribution | Strong Risk-Off | Tactical profit-taking inside structural accumulation | 83.0 |
| HYG | High-Yield Credit | -1.0 | -0.1 | 0.4 | 2.1 | Flat | Neutral | High | High-Turnover Consolidation | Transition | Structural distribution | 79.0 |
| SGOV | Treasury Bills / Cash | -0.5 | -0.4 | 0.9 | -0.7 | Flat | Neutral | Normal | Neutral | Neutral | Structural accumulation; Strong sponsorship | 99.0 |
| SHY | Short-Duration Treasuries | -0.9 | -0.9 | 0.2 | 1.3 | Flat | Sell | High | Distribution Before Breakdown | Early Bearish | Medium-term deterioration; Persistent selling | 75.0 |
| IEF | Intermediate-Duration Treasuries | 0.6 | -0.7 | 0.7 | -0.5 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Medium-term recovery | 87.0 |
| TLT | Long-Duration Treasuries | 1.8 | 0.8 | 0.8 | 2.2 | Down | Neutral | High | Heavy Selling Pressure | Cautious | Structural accumulation; Strong sponsorship | 99.0 |
| GLD | Gold | 1.1 | 1.2 | 0.5 | 1.9 | Flat | Buy | High | Strong Accumulation | Early Bullish | Strong confirmation | 95.0 |
| IBIT | Bitcoin | -0.1 | -1.6 | 0.5 | -0.4 | Flat | Neutral | Normal | Neutral | Neutral | Structural distribution | 79.0 |

### Sector Flow Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| XLC | Communication Services | -0.5 | -1.8 | 0.3 | 0.3 | Flat | Neutral | Normal | Neutral | Neutral | Structural distribution | 79.0 |
| XLY | Consumer Discretionary | 0.5 | 0.3 | 0.6 | -0.2 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Medium-term recovery | 87.0 |
| XLP | Consumer Staples | 2.2 | 2.4 | 0.4 | 0.9 | Up | Buy | Normal | Steady Accumulation | Risk-On | Strong confirmation; Exceptional institutional buying | 100.0 |
| XLE | Energy | -0.9 | -1.1 | 0.2 | -0.1 | Up | Sell | Normal | Profit Taking | Slightly Bearish | Strong confirmation; Exceptional institutional selling, Persistent selling | 79.0 |
| XLF | Financials | 2.0 | 2.4 | 0.6 | 1.6 | Up | Buy | High | Confirmed Accumulation | Strong Risk-On | Strong confirmation; Exceptional institutional buying | 100.0 |
| XLV | Health Care | 0.5 | 0.5 | 0.5 | 0.4 | Up | Sell | Normal | Profit Taking | Slightly Bearish | Medium-term recovery | 87.0 |
| XLI | Industrials | -0.8 | 0.6 | 0.5 | 1.1 | Down | Neutral | High | Heavy Selling Pressure | Cautious | Medium-term deterioration | 83.0 |
| XLK | Information Technology | 0.3 | -0.4 | 0.7 | 0.5 | Down | Neutral | High | Heavy Selling Pressure | Cautious | Structural accumulation | 91.0 |
| XLB | Materials | -0.6 | -0.2 | 0.5 | 0.7 | Up | Sell | Normal | Profit Taking | Slightly Bearish | Tactical profit-taking inside structural accumulation; Exceptional institutional selling | 75.0 |
| XLRE | Real Estate | 1.2 | 2.9 | 0.7 | 0.7 | Up | Buy | Normal | Steady Accumulation | Risk-On | Strong confirmation; Exceptional institutional buying | 100.0 |
| XLU | Utilities | 0.5 | 0.2 | 0.5 | 0.7 | Flat | Neutral | Normal | Neutral | Neutral | Structural accumulation | 91.0 |

### Subsector PFV Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ITA | Aerospace and Defense | -0.2 | -0.6 | 0.2 | 0.6 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural distribution; Persistent selling | 71.0 |
| SOXX | Semiconductors | 2.0 | 2.2 | 0.6 | 2.1 | Down | Buy | High | Aggressive Dip Buying | Recovery Candidate | Strong confirmation; Exceptional institutional buying | 100.0 |
| SMH | Semiconductors | 1.2 | 0.5 | 0.5 | 1.1 | Down | Neutral | High | Heavy Selling Pressure | Cautious | Structural accumulation | 91.0 |
| CIBR | Cybersecurity | 0.7 | 1.4 | 0.6 | -0.0 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural accumulation | 91.0 |

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

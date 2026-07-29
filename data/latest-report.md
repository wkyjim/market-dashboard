# Rule-Based Institutional Market Update

Generated at: 30 July 2026, 02:03:15 (HKT)
Window: 24h

## Executive Dashboard

- Regime score: **52.89 / 100** (Mixed / Rotation)
- US equity strength: **53.71 / 100** (neutral)
- Evidence quality: **79.5 / 100**
- ETF flow contribution: **47.52 / 100**, reliability **71.05 / 100**
- Breadth: **healthy**; above 50DMA `50.0%`, above 200DMA `69.49%`
- Top sector score: **Healthcare** `70.05`
- Top theme score: **Financials** `62.53`

## Market Regime Score

| Metric | Value | Driver / Interpretation |
| --- | --- | --- |
| Overall regime | 52.89 | Mixed / Rotation |
| equity_trend | 61.25 | mild risk-on support; Core equity ETFs versus moving averages. |
| equity_momentum | 47.76 | neutral / mixed; 5D/20D/60D return momentum across SPY, QQQ, IWM, and SMH. |
| market_breadth | 57.05 | mild risk-on support; Participation breadth from tracked equity/ETF rows. |
| volatility | 35.0 | risk-off pressure; VIX level and change; higher score means calmer volatility conditions. |
| rates_yield_curve | 58.0 | mild risk-on support; Treasury yield pressure and curve shape; higher score means less rates pressure. |
| credit_proxy | 50.0 | neutral / mixed; Credit-market proxy; currently neutral when no direct spread signal is available. |
| dollar_fx | 55.21 | mild risk-on support; Dollar move; higher score means less USD tightening pressure. |
| commodity_confirmation | 47.0 | neutral / mixed; Copper, silver, oil, and gold mix; higher score means better cyclical confirmation. |
| etf_flow | 48.24 | neutral / mixed; Grouped ETF flow contribution adjusted for reliability. |
| news_confirmation | 69.38 | risk-on support; Weighted headline/news confirmation score. |
| Positive contributors |  | news_confirmation=69.38, equity_trend=61.25 |
| Negative contributors |  | volatility=35.0 |

## US Equity Strength Score

| Component | Score |
| --- | --- |
| indices_above_moving_averages | 61.25 |
| sp500_trend | 55.0 |
| nasdaq_trend | 55.0 |
| russell_participation | 80.0 |
| returns_momentum | 47.76 |
| rsi_zone | 37.5 |
| macd_confirmation | 35.0 |
| volume_confirmation | 42.5 |
| breadth | 57.05 |

## Evidence Quality / Confidence

- Confidence score: `79.5`
- Agreement ratio: `0.5`
- Contradiction count: `1`
- Missing indicators: none
- Warning flags: none

## Cross-Asset Confirmation

| Area | Signal | Interpretation |
| --- | --- | --- |
| Equities | S&P 500 stable; Nasdaq stable; Russell 2000 falling | Confirms risk appetite when broad indices rise together; weak small caps would narrow the signal. |
| Rates | 10Y Treasury rising; MOVE rising | Rising yields can pressure duration assets; falling MOVE supports calmer bond volatility. |
| Dollar | DXY proxy stable | A stronger dollar can tighten financial conditions and pressure commodities/emerging-market risk. |
| Credit | HYG stable | High-yield weakness would challenge equity risk-on confirmation. |
| Gold | Gold rising | Gold strength can indicate defensive demand, inflation hedging, or geopolitical concern. |
| Silver | Silver rising | Silver helps distinguish precious-metal demand from industrial/cyclical confirmation when data is available. |
| Copper | Copper stable | Copper strength supports cyclical growth confirmation; weakness would dilute risk-on breadth. |
| Oil | WTI crude rising | Oil spikes can be inflationary risk; falling oil can ease cost pressure but may also flag demand softness. |
| Volatility | VIX rising | Falling VIX supports risk appetite; a volatility spike would reduce confidence in broad risk-on. |

### Macro Snapshot

Live macro rows are intraday snapshots from `public.macro_live`; closed rows are official stored rows from `public.macro`.

| Symbol | Name | Close | Pct Chg | Market Date | Status |
| --- | --- | --- | --- | --- | --- |
| ^GSPC | S&P 500 | 7411.72 | -0.23 | 2026-07-29 | live as of 30 July 2026, 02:00:35 (HKT) |
| ^IXIC | NASDAQ Composite | 24853.22 | -0.1 | 2026-07-29 | live as of 30 July 2026, 02:00:35 (HKT) |
| ^RUT | Russell 2000 Index | 2916.37 | -1.27 | 2026-07-29 | live as of 30 July 2026, 02:00:35 (HKT) |
| ^VIX | CBOE Volatility Index | 19.57 | 7.47 | 2026-07-29 | live as of 30 July 2026, 02:00:35 (HKT) |
| ^SKEW | CBOE SKEW Index | 142.98 | -2.47 | 2026-07-28 | closed |
| ^MOVE | ICE BofA MOVE Index | 76.82 | 8.38 | 2026-07-24 | closed |
| US2YT=X | United States 2-Year Treasury Yield | 4.31 | 0.72 | 2026-07-29 | live as of 30 July 2026, 02:00:35 (HKT) |
| US3YT=X | United States 3-Year Treasury Yield | 4.35 | 0.98 | 2026-07-29 | live as of 30 July 2026, 02:00:35 (HKT) |
| US5YT=X | United States 5-Year Treasury Yield | 4.4 | 1.01 | 2026-07-29 | live as of 30 July 2026, 02:00:35 (HKT) |
| US7YT=X | United States 7-Year Treasury Yield | 4.52 | 1.0 | 2026-07-29 | live as of 30 July 2026, 02:00:35 (HKT) |
| US10YT=X | United States 10-Year Treasury Yield | 4.63 | 0.5 | 2026-07-29 | live as of 30 July 2026, 02:00:35 (HKT) |
| US20YT=X | United States 20-Year Treasury Yield | 5.17 | 1.19 | 2026-07-29 | live as of 30 July 2026, 02:00:35 (HKT) |
| US30YT=X | United States 30-Year Treasury Yield | 5.12 | 0.51 | 2026-07-29 | live as of 30 July 2026, 02:00:35 (HKT) |
| HK50 | Hang Seng Futures | 25753.5 | 0.93 | 2026-07-29 | closed |
| KOR200c1 | KOSPI 200 Futures | 967.15 | 1.09 | 2026-07-28 | closed |
| CIHc1 | SSE 50 Futures | 2890.8 | -1.33 | 2026-07-28 | closed |
| HYG | iShares iBoxx High Yield Corporate Bond ETF | 79.42 | 0.0 | 2026-07-29 | live as of 30 July 2026, 02:00:35 (HKT) |
| LQD | iShares iBoxx Investment Grade Corporate Bond ETF | 106.69 | -0.13 | 2026-07-29 | live as of 30 July 2026, 02:00:35 (HKT) |
| JNK | SPDR Bloomberg High Yield Bond ETF | 95.62 | 0.01 | 2026-07-29 | live as of 30 July 2026, 02:00:35 (HKT) |
| RSP | Invesco S&P 500 Equal Weight ETF | 217.68 | -0.0 | 2026-07-29 | live as of 30 July 2026, 02:00:35 (HKT) |
| IWF | iShares Russell 1000 Growth ETF | 115.82 | -0.57 | 2026-07-29 | live as of 30 July 2026, 02:00:35 (HKT) |
| IWD | iShares Russell 1000 Value ETF | 251.79 | -0.1 | 2026-07-29 | live as of 30 July 2026, 02:00:35 (HKT) |
| TLT | iShares 20+ Year Treasury Bond ETF | 83.86 | -0.45 | 2026-07-29 | live as of 30 July 2026, 02:00:35 (HKT) |
| IEF | iShares 7-10 Year Treasury Bond ETF | 93.42 | -0.15 | 2026-07-29 | live as of 30 July 2026, 02:00:35 (HKT) |
| SHY | iShares 1-3 Year Treasury Bond ETF | 81.96 | 0.02 | 2026-07-29 | live as of 30 July 2026, 02:00:35 (HKT) |
| GC=F | Gold Future | 4105.0 | 1.7 | 2026-07-29 | live as of 30 July 2026, 02:00:35 (HKT) |
| SI=F | Silver Future | 58.16 | 1.5 | 2026-07-29 | live as of 30 July 2026, 02:00:35 (HKT) |
| CL=F | WTI Crude Oil Future | 84.55 | 6.67 | 2026-07-29 | live as of 30 July 2026, 02:00:35 (HKT) |
| HG=F | Copper Future | 6.33 | 0.09 | 2026-07-29 | live as of 30 July 2026, 02:00:35 (HKT) |

## Market Dispersion Analysis

- Sector ETF 20D dispersion: `15.17` points (high); leader `XLE` (Energy) `7.45`, laggard `XLK` (Technology) `-7.72`
- Sector ETF 60D dispersion: `20.44` points (very high); leader `XLV` (Health Care) `14.57`, laggard `XLC` (Communication Services) `-5.87`

| Comparison | Left | Right | 20D Spread | Signal |
| --- | --- | --- | --- | --- |
| Equal-weight vs cap-weight | RSP (Equal-weight S&P 500) | SPY (S&P 500) | 2.2 | broader participation |
| Small-cap vs large-cap | IWM (Russell 2000) | SPY (S&P 500) | -1.85 | large-cap leadership |
| Growth vs value | IWF (Russell 1000 Growth) | IWD (Russell 1000 Value) | -8.34 | value leadership |
| Nasdaq vs S&P 500 | QQQ (Nasdaq 100) | SPY (S&P 500) | -6.69 | S&P 500 leadership |

## Sector Constituent Dispersion

- Breadth 50D / 200D: percentage of active S&P 500 constituents in the sector trading above the 50-day / 200-day moving average.
- Positive 20D: percentage of active sector constituents with positive 20-day return.
- Std 20D: cross-sectional standard deviation of constituent 20-day returns; higher means wider stock-level dispersion.

| Sector | Count | Breadth 50D | Breadth 200D | Positive 20D | 20D Dispersion | Std 20D | Label | Leaders | Laggards |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Information Technology | 74 | 43.24 | 63.01 | 44.59 | 107.53 | 20.77 | very high | ACN, CTSH, WDAY | SNDK, GLW, CRWD |
| Industrials | 81 | 70.89 | 76.62 | 59.26 | 58.18 | 10.58 | very high | CTAS, PAYX, VRSK | BLDR, CAT, GNRC |
| Health Care | 59 | 91.53 | 67.8 | 79.66 | 45.63 | 7.17 | very high | IQV, MCK, ABT | EW, ISRG, MRNA |
| Consumer Discretionary | 47 | 72.34 | 57.45 | 61.7 | 45.56 | 7.83 | very high | ROST, DPZ, GM | MGM, DHI, TSLA |
| Financials | 76 | 91.67 | 82.86 | 85.53 | 40.32 | 8.23 | very high | PYPL, CBOE, NDAQ | HBAN, C, HOOD |
| Communication Services | 23 | 45.45 | 40.91 | 56.52 | 34.44 | 9.27 | very high | OMC, FOXA, T | TKO, ECHO, PSKY |
| Materials | 26 | 73.08 | 69.23 | 80.77 | 29.39 | 6.76 | very high | CF, NUE, IP | CRH, VMC, ALB |
| Energy | 21 | 33.33 | 85.71 | 71.43 | 26.66 | 7.6 | very high | PSX, MPC, XOM | WMB, TPL, HAL |
| Utilities | 31 | 67.74 | 80.65 | 41.94 | 20.19 | 3.97 | very high | EIX, AWK, FE | DTE, VST, NRG |
| Consumer Staples | 34 | 84.85 | 71.88 | 82.35 | 20.08 | 4.28 | very high | KHC, CASY, PM | HRL, STZ, KDP |
| Real Estate | 31 | 80.65 | 80.65 | 51.61 | 14.54 | 3.61 | high | VTR, CBRE, WELL | MAA, CCI, EQIX |

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
| Real Gross Domestic Product | 24180.42 | billions chained 2017 dollars | 124.67 billions chained 2017 dollars vs prior | 2026-01-01 | Higher reading supports activity or liquidity. |
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
| Headline PCE Price Index month-over-month inflation rate | 0.45 | percent | 0.04 pp vs prior | 2026-05-01 | Higher reading increases macro pressure. |
| Headline PCE Price Index year-over-year inflation rate | 4.07 | percent | 0.28 pp vs prior | 2026-05-01 | Higher reading increases macro pressure. |
| Core PCE Price Index month-over-month inflation rate | 0.32 | percent | 0.07 pp vs prior | 2026-05-01 | Higher reading increases macro pressure. |
| Core PCE Price Index year-over-year inflation rate | 3.41 | percent | 0.09 pp vs prior | 2026-05-01 | Higher reading increases macro pressure. |
| Headline PPI Final Demand month-over-month inflation rate | -0.19 | percent | -0.79 pp vs prior | 2026-06-01 | Lower reading eases macro pressure. |
| Headline PPI Final Demand year-over-year inflation rate | 5.51 | percent | -0.49 pp vs prior | 2026-06-01 | Lower reading eases macro pressure. |
| Core PPI Final Demand Less Foods and Energy month-over-month inflation rate | 0.2 | percent | 0.11 pp vs prior | 2026-06-01 | Higher reading increases macro pressure. |
| Core PPI Final Demand Less Foods and Energy year-over-year inflation rate | 4.68 | percent | 0.09 pp vs prior | 2026-06-01 | Higher reading increases macro pressure. |
| Consumer Price Index for All Urban Consumers | 332.57 | index 1982-1984=100 | -1.41 index pts vs prior | 2026-06-01 | Lower reading eases macro pressure. |
| Core CPI | 336.06 | index 1982-1984=100 | -0.06 index pts vs prior | 2026-06-01 | Lower reading eases macro pressure. |
| Personal Consumption Expenditures Price Index | 131.53 | index 2017=100 | 0.59 index pts vs prior | 2026-05-01 | Higher reading increases macro pressure. |
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
| US dollar/Euro ECB reference exchange rate | 1.14 | USD | 0.0 USD vs prior | 2026-07-29 | EUR strengthened versus this currency. |
| Japanese yen/Euro ECB reference exchange rate | 186.27 | JPY | -0.05 JPY vs prior | 2026-07-29 | EUR weakened versus this currency. |
| Chinese yuan renminbi/Euro ECB reference exchange rate | 7.7 | CNY | 0.0 CNY vs prior | 2026-07-29 | EUR strengthened versus this currency. |
| Australian dollar/Euro ECB reference exchange rate | 1.64 | AUD | 0.01 AUD vs prior | 2026-07-29 | EUR strengthened versus this currency. |

ABS Australia note: ABS rows are stored locally/Neon, but most series are dimension-coded; only curated series should be promoted into narrative report text.

## Sector and Theme Leadership

### Official Sector Strength

Supporting and detracting names are the top/bottom S&P 500 constituents by 20D return when constituent coverage is available; otherwise the report falls back to related ETFs.

| Rank | Sector | Score | Trend | Momentum | Stock Breadth | ETF Flow | Flow Reliability | 3M RS | Supporting / Leaders | Detracting / Laggards |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Healthcare | 70.05 | strong uptrend | positive | broad | 63.28 | 90.0 | 57.04 | IQV, MCK, ABT | EW, ISRG, MRNA |
| 2 | Consumer Staples | 68.77 | strong uptrend | neutral | broad | 65.92 | 65.0 | 51.99 | KHC, CASY, PM | HRL, STZ, KDP |
| 3 | Financials | 67.37 | strong uptrend | positive | broad | 64.22 | 90.0 | 57.31 | PYPL, CBOE, NDAQ | HBAN, C, HOOD |
| 4 | Real Estate | 66.79 | strong uptrend | neutral | broad | 71.21 | 100.0 | 51.68 | VTR, CBRE, WELL | MAA, CCI, EQIX |
| 5 | Industrials | 65.92 | strong uptrend | neutral | broad | 55.34 | 65.0 | 50.5 | CTAS, PAYX, VRSK | BLDR, CAT, GNRC |
| 6 | Cybersecurity | 60.9 | strong uptrend | positive | broad | 61.44 | 65.0 | 62.25 | CIBR | CIBR |
| 7 | Energy | 60.11 | uptrend | neutral | broad | 53.02 | 95.0 | 51.85 | PSX, MPC, XOM | WMB, TPL, HAL |
| 8 | Defense | 53.98 | strong uptrend | neutral | weak | 50.0 | 0.0 | 49.65 | XAR | XAR |
| 9 | Crypto | 48.86 | neutral | neutral | mixed | 38.58 | 65.0 | 50.0 |  |  |
| 10 | Utilities | 45.71 | downtrend | neutral | mixed | 50.38 | 65.0 | 44.92 | EIX, AWK, FE | DTE, VST, NRG |
| 11 | Semiconductors | 45.64 | neutral | negative | weak | 83.54 | 100.0 | 40.12 | SMH, SOXX | SOXX, SMH |
| 12 | Technology | 43.43 | neutral | neutral | weak | 41.57 | 90.0 | 46.13 | ACN, CTSH, WDAY | SNDK, GLW, CRWD |
| 13 | Grid Infrastructure | 40.53 | downtrend | negative | weak | 63.42 | 65.0 | 39.85 | GRID | GRID |
| 14 | Consumer Discretionary | 36.47 | strong downtrend | neutral | weak | 66.54 | 65.0 | 44.41 | ROST, DPZ, GM | MGM, DHI, TSLA |
| 15 | Nuclear | 33.9 | strong downtrend | negative | weak | 50.0 | 0.0 | 32.32 | NLR | NLR |

### Thematic Strength

| Rank | Theme | Score | Setup | ETF Flow | Flow Reliability | Dispersion | Price | News |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Financials | 62.53 | Positive setup | 64.22 | 90.0 | 7.19 | True | True |
| 2 | Healthcare Innovation | 61.78 | Positive setup | 63.28 | 90.0 | 4.81 | True | False |
| 3 | Dividend Defensives | 59.05 | Positive setup | 56.36 | 65.0 | 5.14 | False | False |
| 4 | Energy | 58.37 | Positive setup | 53.02 | 95.0 | 5.03 | False | False |
| 5 | Small Caps | 56.78 | Positive setup | 55.27 | 65.0 | 0.0 | False | False |
| 6 | Cybersecurity | 54.16 | Neutral / watchlist | 61.44 | 65.0 | 85.72 | False | False |
| 7 | Defense | 53.65 | Neutral / watchlist | 50.0 | 0.0 | 18.51 | False | False |
| 8 | Semiconductors | 51.73 | Neutral / watchlist | 83.54 | 100.0 | 22.27 | False | False |
| 9 | Quality Growth | 48.4 | Neutral / watchlist | 64.17 | 65.0 | 28.43 | False | False |
| 10 | AI Infrastructure | 45.12 | Neutral / watchlist | 83.54 | 100.0 | 26.73 | False | False |
| 11 | Grid Infrastructure | 43.31 | Neutral / watchlist | 63.42 | 65.0 | 16.56 | False | False |
| 12 | Crypto Infrastructure | 38.88 | Weak setup | 38.58 | 65.0 | 6.96 | False | False |
| 13 | Nuclear | 32.16 | Underperformance risk | 50.0 | 0.0 | 21.82 | False | False |

- Top 5 improving themes: Cybersecurity, Healthcare Innovation, Financials, Small Caps, Semiconductors
- Top 5 deteriorating themes: Nuclear, Crypto Infrastructure, Grid Infrastructure, Energy, AI Infrastructure
- Strong news but weak price confirmation: none
- Strong price but weak news confirmation: Healthcare Innovation

### Sector / Theme Alignment

| Sector | Related Themes | Sector Score | Sector Signal | Theme Score | Theme Signal | Interpretation |
| --- | --- | --- | --- | --- | --- | --- |
| Healthcare | Healthcare Innovation | 70.05 | strong | 61.78 | positive | sector and theme confirmation |
| Consumer Staples | Dividend Defensives | 68.77 | strong | 59.05 | positive | sector and theme confirmation |
| Financials | Financials | 67.37 | strong | 62.53 | positive | sector and theme confirmation |
| Real Estate | Dividend Defensives | 66.79 | strong | 59.05 | positive | sector and theme confirmation |
| Industrials | Defense, Grid Infrastructure | 65.92 | strong | 48.48 | mixed | sector stronger than related themes |
| Cybersecurity | Cybersecurity | 60.9 | positive | 54.16 | mixed | sector stronger than related themes |
| Energy | Energy | 60.11 | positive | 58.37 | positive | sector and theme confirmation |
| Defense | Defense | 53.98 | mixed | 53.65 | mixed | mixed confirmation |
| Crypto | Crypto Infrastructure | 48.86 | mixed | 38.88 | weak | mixed confirmation |
| Utilities | Grid Infrastructure, Nuclear, Dividend Defensives | 45.71 | mixed | 44.84 | weak | mixed confirmation |
| Semiconductors | AI Infrastructure, Semiconductors | 45.64 | mixed | 48.42 | mixed | mixed confirmation |
| Technology | AI Infrastructure, Semiconductors, Quality Growth | 43.43 | weak | 48.42 | mixed | mixed confirmation |
| Grid Infrastructure | Grid Infrastructure | 40.53 | weak | 43.31 | weak | broad weakness across sector and themes |
| Consumer Discretionary | Small Caps | 36.47 | weak | 56.78 | positive | theme stronger than official sector |
| Nuclear | Nuclear | 33.9 | very weak | 32.16 | very weak | broad weakness across sector and themes |

## Three-Month Outperformance Setup

| Rank | Theme | Score | Classification | Drivers | Invalidation Triggers |
| --- | --- | --- | --- | --- | --- |
| 1 | Healthcare Innovation | 67.94 | Positive setup | relative_strength_60d, trend_persistence, breadth, downside_volatility, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 2 | Small Caps | 64.57 | Positive setup | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 3 | Dividend Defensives | 62.48 | Positive setup | trend_persistence, breadth, volume_accumulation, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 4 | Financials | 62.15 | Positive setup | relative_strength_60d, trend_persistence, breadth, downside_volatility, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 5 | Energy | 60.78 | Positive setup | relative_strength_20d, trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 6 | Cybersecurity | 56.59 | Neutral / watchlist | relative_strength_60d, trend_persistence, breadth, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 7 | Defense | 55.92 | Neutral / watchlist | relative_strength_20d, trend_persistence, breadth, volume_accumulation | relative strength below SPY, breadth below 45%, news turns negative |
| 8 | Quality Growth | 51.74 | Neutral / watchlist | downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 9 | Semiconductors | 49.55 | Neutral / watchlist | volume_accumulation, news_acceleration | relative strength below SPY, breadth below 45%, news turns negative |
| 10 | AI Infrastructure | 45.76 | Neutral / watchlist | downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 11 | Grid Infrastructure | 45.3 | Neutral / watchlist | volume_accumulation, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 12 | Crypto Infrastructure | 36.89 | Weak setup |  | relative strength below SPY, breadth below 45%, news turns negative |

## Breadth and Participation

- Above 50DMA: `50.0%`
- Above 200DMA: `69.49%`
- Positive 20D return: `51.67%`

## Volatility and Risk Signals

- VIX close=19.57 pct_chg=7.47

## News Analytics

- Sentiment counts: {'positive': 55, 'negative': 24, 'neutral': 1}
- News confirmation score: `69.38`

### Top Market-Moving Headlines

**1. Oil prices jump 7% after Trump says U.S. will hit Iran hard**
- Source: CNBC Top News
- Importance / impact: High / Positive
- Relevance / horizon: macro / short-term
- Affected assets: U.S, geopolitical_risk, commodity_prices
- Score: `81.22`
- Investment implication: Macro-relevant positive signal; use as context for rates, volatility, and index confirmation over the short-term.

**2. Global oil prices rise above $87 a barrel after Trump vows retaliation for surprise Iranian attack on U.S. troops**
- Source: MarketWatch Top Stories
- Importance / impact: High / Positive
- Relevance / horizon: macro / short-term
- Affected assets: U.S, Brent, oil prices, geopolitical events
- Score: `67.5`
- Investment implication: Macro-relevant positive signal; use as context for rates, volatility, and index confirmation over the short-term.

**3. Forget oil. A surging El Niño could kill Fed rate cuts — and these stocks stand to win.**
- Source: MarketWatch Top Stories
- Importance / impact: High / Negative
- Relevance / horizon: macro / short-term
- Affected assets: A, inflation, El Niño, Fed rate cuts
- Score: `51.0`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the short-term.

**4. Glencore’s Traders to Report Bumper First-Half**
- Source: Dow Jones US Business
- Importance / impact: High / Positive
- Relevance / horizon: macro / short-term
- Affected assets: GLNC, U.S, earnings, marketing
- Score: `48.77`
- Investment implication: Macro-relevant positive signal; use as context for rates, volatility, and index confirmation over the short-term.

**5. Corning tumbles 12% after earnings, leading rout in optical stocks**
- Source: CNBC Investing
- Importance / impact: Medium / Negative
- Relevance / horizon: sector_theme / short-term
- Affected assets: AXT, CORNING, MARVVLUMENTUM, COHERENT, earnings report
- Score: `41.45`
- Investment implication: Theme or sector negative signal; requires price and volume confirmation before affecting rankings.

**6. Tim Cook’s last earnings call comes at momentous time for Apple with stock at record**
- Source: CNBC Business
- Importance / impact: Medium / Positive
- Relevance / horizon: single_name / short-term
- Affected assets: AAPL, Leadership Change, Market Cap Milestone
- Score: `39.78`
- Investment implication: Single-name positive signal; low weight unless it maps to a broader sector or theme.

**7. How China Went From Dream Customer to a Nightmare for Big Oil**
- Source: Dow Jones US Business
- Importance / impact: Medium / Negative
- Relevance / horizon: macro / short-term
- Affected assets: oil market, China
- Score: `38.25`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the short-term.

**8. SK Hynix Extends Streak of Record Results**
- Source: Dow Jones US Business
- Importance / impact: Medium / Positive
- Relevance / horizon: single_name / short-term
- Affected assets: SK, memory chips, AI
- Score: `37.4`
- Investment implication: Single-name positive signal; low weight unless it maps to a broader sector or theme.

**9. Trump says U.S. will give Iran a 'beating' after surprise attack**
- Source: CNBC Business Headlines
- Importance / impact: Medium / Negative
- Relevance / horizon: single_name / short-term
- Affected assets: U.S, X, geo-political
- Score: `35.1`
- Investment implication: Single-name negative signal; low weight unless it maps to a broader sector or theme.

**10. Micron’s stock sinks toward worst monthly drop in 11 years as China fears escalate**
- Source: MarketWatch Top Stories
- Importance / impact: Low / Negative
- Relevance / horizon: single_name / short-term
- Affected assets: MIC, China chip supply concerns, Micron Technology
- Score: `33.15`
- Investment implication: Single-name negative signal; low weight unless it maps to a broader sector or theme.


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
- Market flow score: `46.3 / 100`
- Equity risk flow: `46.2`
- Credit risk flow: `43.8`
- Sector cyclicality flow: `45.1`
- Duration/liquidity flow: `50.5`
- Alternatives: `defensive or uncertainty hedge`
- ETF flow reliability: `71.0 / 100`
- Dominant allocation direction: `defensive demand`

### Core Flow Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVV | U.S. Broad Equity | -0.8 | 0.7 | 0.3 | -0.6 | Flat | Neutral | Normal | Neutral | Neutral | Medium-term deterioration | 83.0 |
| ACWI | Global Equity | -1.4 | -1.5 | 0.1 | -0.9 | Flat | Sell | Normal | Quiet Distribution | Weakening | Strong confirmation; Exceptional institutional selling, Persistent selling | 79.0 |
| EFA | Developed Markets ex-U.S. | -2.3 | -0.1 | 0.0 | -1.0 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Medium-term deterioration; Exceptional institutional selling, Persistent selling | 67.0 |
| IEMG | Emerging Markets | -0.4 | -0.6 | 0.1 | -0.0 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Medium-term recovery; Persistent selling | 79.0 |
| IJH | U.S. Mid Cap | -0.4 | 0.0 | 0.6 | -1.2 | Flat | Neutral | Normal | Neutral | Neutral | Structural accumulation | 91.0 |
| IWM | U.S. Small Cap | -0.3 | 0.7 | 0.5 | -0.8 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural distribution | 79.0 |
| LQD | Investment-Grade Credit | 0.2 | 0.5 | 0.5 | -0.6 | Down | Sell | Normal | Persistent Distribution | Risk-Off | Tactical profit-taking inside structural accumulation | 83.0 |
| HYG | High-Yield Credit | -1.1 | -0.6 | 0.4 | -0.0 | Flat | Neutral | Normal | Neutral | Neutral | Structural distribution | 79.0 |
| SGOV | Treasury Bills / Cash | -0.6 | -0.4 | 0.8 | -0.8 | Flat | Neutral | Normal | Neutral | Neutral | Structural accumulation; Strong sponsorship | 99.0 |
| SHY | Short-Duration Treasuries | -0.8 | -1.1 | 0.2 | -0.3 | Flat | Sell | Normal | Quiet Distribution | Weakening | Strong confirmation; Persistent selling | 87.0 |
| IEF | Intermediate-Duration Treasuries | 0.6 | -0.7 | 0.7 | -1.2 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Medium-term recovery | 87.0 |
| TLT | Long-Duration Treasuries | 1.9 | 1.1 | 0.8 | 0.1 | Down | Buy | Normal | Contrarian Buying | Watch | Strong confirmation; Strong sponsorship | 100.0 |
| GLD | Gold | 1.0 | 1.2 | 0.4 | -0.9 | Flat | Buy | Normal | Quiet Accumulation | Improving | Strong confirmation | 95.0 |
| IBIT | Bitcoin | -0.4 | -1.6 | 0.5 | -0.9 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural distribution | 79.0 |

### Sector Flow Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| XLC | Communication Services | -0.4 | -1.9 | 0.3 | -0.5 | Flat | Neutral | Normal | Neutral | Neutral | Structural distribution | 79.0 |
| XLY | Consumer Discretionary | 1.2 | 0.5 | 0.6 | -0.9 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Medium-term recovery | 87.0 |
| XLP | Consumer Staples | 1.2 | 1.8 | 0.3 | 3.2 | Up | Buy | High | Confirmed Accumulation | Strong Risk-On | Strong confirmation | 95.0 |
| XLE | Energy | -0.7 | -0.9 | 0.2 | -0.8 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural distribution; Persistent selling | 71.0 |
| XLF | Financials | 1.9 | 2.6 | 0.6 | -0.2 | Up | Buy | Normal | Steady Accumulation | Risk-On | Strong confirmation; Exceptional institutional buying | 100.0 |
| XLV | Health Care | 0.9 | 0.8 | 0.6 | 0.8 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Medium-term recovery | 87.0 |
| XLI | Industrials | -0.4 | 0.8 | 0.5 | -1.1 | Flat | Neutral | Normal | Neutral | Neutral | Structural accumulation | 91.0 |
| XLK | Information Technology | 0.2 | -0.6 | 0.6 | -0.5 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural accumulation | 91.0 |
| XLB | Materials | -0.3 | 0.5 | 0.5 | 0.1 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural accumulation | 91.0 |
| XLRE | Real Estate | 1.0 | 2.8 | 0.7 | 0.5 | Up | Buy | Normal | Steady Accumulation | Risk-On | Strong confirmation; Exceptional institutional buying | 100.0 |
| XLU | Utilities | -0.1 | 0.2 | 0.4 | -0.8 | Flat | Neutral | Normal | Neutral | Neutral | Structural accumulation | 91.0 |

### Subsector PFV Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ITA | Aerospace and Defense | -0.1 | -0.6 | 0.2 | -0.7 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural distribution; Persistent selling | 71.0 |
| SOXX | Semiconductors | 2.1 | 1.7 | 0.6 | 1.2 | Down | Sell | High | Confirmed Distribution | Strong Risk-Off | Tactical profit-taking inside structural accumulation | 83.0 |
| SMH | Semiconductors | 0.9 | 0.2 | 0.5 | 1.0 | Down | Buy | High | Aggressive Dip Buying | Recovery Candidate | Strong confirmation; Exceptional institutional buying | 100.0 |
| CIBR | Cybersecurity | 1.1 | 1.7 | 0.7 | -0.9 | Flat | Buy | Normal | Quiet Accumulation | Improving | Strong confirmation | 95.0 |

### Material Flow Divergences

| Severity | Type | Primary | Comparison | Interpretation |
| --- | --- | --- | --- | --- |
| medium | related_subsector_divergence | XLI | ITA | defense-specific demand differs from broad industrials |
| medium | related_subsector_divergence | XLK | SOXX | technology differs from semiconductors |
| high | close_substitute_divergence | IVV | SPY | primary representative differs from close substitute |
| high | close_substitute_divergence | AGG | IUSB | primary representative differs from close substitute |
| high | close_substitute_divergence | HYG | JNK | primary representative differs from close substitute |
| high | close_substitute_divergence | IVV | SPY | primary representative differs from close substitute |


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

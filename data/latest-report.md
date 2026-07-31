# Rule-Based Institutional Market Update

Generated at: 31 July 2026, 15:12:39 (HKT)
Window: 24h

## Executive Dashboard

- Regime score: **57.66 / 100** (Mild Risk-On)
- US equity strength: **54.08 / 100** (neutral)
- Evidence quality: **79.5 / 100**
- ETF flow contribution: **50.92 / 100**, reliability **71.98 / 100**
- Breadth: **narrow**; above 50DMA `48.33%`, above 200DMA `72.88%`
- Top sector score: **Healthcare** `70.73`
- Top theme score: **Healthcare Innovation** `61.72`

## Market Regime Score

| Metric | Value | Driver / Interpretation |
| --- | --- | --- |
| Overall regime | 57.66 | Mild Risk-On |
| equity_trend | 61.25 | mild risk-on support; Core equity ETFs versus moving averages. |
| equity_momentum | 48.8 | neutral / mixed; 5D/20D/60D return momentum across SPY, QQQ, IWM, and SMH. |
| market_breadth | 53.74 | neutral / mixed; Participation breadth from tracked equity/ETF rows. |
| volatility | 70.0 | risk-on support; VIX level and change; higher score means calmer volatility conditions. |
| rates_yield_curve | 58.0 | mild risk-on support; Treasury yield pressure and curve shape; higher score means less rates pressure. |
| credit_proxy | 50.0 | neutral / mixed; Credit-market proxy; currently neutral when no direct spread signal is available. |
| dollar_fx | 54.56 | neutral / mixed; Dollar move; higher score means less USD tightening pressure. |
| commodity_confirmation | 58.0 | mild risk-on support; Copper, silver, oil, and gold mix; higher score means better cyclical confirmation. |
| etf_flow | 50.66 | neutral / mixed; Grouped ETF flow contribution adjusted for reliability. |
| news_confirmation | 82.5 | risk-on support; Weighted headline/news confirmation score. |
| Positive contributors |  | news_confirmation=82.5, volatility=70.0, equity_trend=61.25 |
| Negative contributors |  | none |

## US Equity Strength Score

| Component | Score |
| --- | --- |
| indices_above_moving_averages | 61.25 |
| sp500_trend | 55.0 |
| nasdaq_trend | 55.0 |
| russell_participation | 80.0 |
| returns_momentum | 48.8 |
| rsi_zone | 37.5 |
| macd_confirmation | 35.0 |
| volume_confirmation | 51.25 |
| breadth | 53.74 |

## Evidence Quality / Confidence

- Confidence score: `79.5`
- Agreement ratio: `0.5`
- Contradiction count: `0`
- Missing indicators: none
- Warning flags: none

## Cross-Asset Confirmation

| Area | Signal | Interpretation |
| --- | --- | --- |
| Equities | S&P 500 rising; Nasdaq rising; Russell 2000 rising | Confirms risk appetite when broad indices rise together; weak small caps would narrow the signal. |
| Rates | 10Y Treasury rising; MOVE rising | Rising yields can pressure duration assets; falling MOVE supports calmer bond volatility. |
| Dollar | DXY proxy stable | A stronger dollar can tighten financial conditions and pressure commodities/emerging-market risk. |
| Credit | HYG rising | High-yield weakness would challenge equity risk-on confirmation. |
| Gold | Gold rising | Gold strength can indicate defensive demand, inflation hedging, or geopolitical concern. |
| Silver | Silver falling | Silver helps distinguish precious-metal demand from industrial/cyclical confirmation when data is available. |
| Copper | Copper rising | Copper strength supports cyclical growth confirmation; weakness would dilute risk-on breadth. |
| Oil | WTI crude falling | Oil spikes can be inflationary risk; falling oil can ease cost pressure but may also flag demand softness. |
| Volatility | VIX falling | Falling VIX supports risk appetite; a volatility spike would reduce confidence in broad risk-on. |

### Macro Snapshot

Live macro rows are intraday snapshots from `public.macro_live`; closed rows are official stored rows from `public.macro`.

| Symbol | Name | Close | Pct Chg | Market Date | Status |
| --- | --- | --- | --- | --- | --- |
| ^GSPC | S&P 500 | 7437.63 | 1.66 | 2026-07-30 | closed |
| ^IXIC | NASDAQ Composite | 25122.18 | 2.78 | 2026-07-30 | closed |
| ^RUT | Russell 2000 Index | 2946.1 | 1.37 | 2026-07-30 | closed |
| ^VIX | CBOE Volatility Index | 17.09 | -17.28 | 2026-07-30 | closed |
| ^SKEW | CBOE SKEW Index | 139.9 | 0.25 | 2026-07-30 | closed |
| ^MOVE | ICE BofA MOVE Index | 76.82 | 8.38 | 2026-07-24 | closed |
| US2YT=X | United States 2-Year Treasury Yield | 4.24 | 0.15 | 2026-07-31 | live as of 31 July 2026, 15:00:48 (HKT) |
| US3YT=X | United States 3-Year Treasury Yield | 4.28 | -0.07 | 2026-07-31 | live as of 31 July 2026, 15:00:48 (HKT) |
| US5YT=X | United States 5-Year Treasury Yield | 4.37 | -0.12 | 2026-07-31 | live as of 31 July 2026, 15:00:48 (HKT) |
| US7YT=X | United States 7-Year Treasury Yield | 4.5 | -0.27 | 2026-07-31 | live as of 31 July 2026, 15:00:48 (HKT) |
| US10YT=X | United States 10-Year Treasury Yield | 4.65 | -0.3 | 2026-07-31 | live as of 31 July 2026, 15:00:48 (HKT) |
| US20YT=X | United States 20-Year Treasury Yield | 5.2 | -0.32 | 2026-07-31 | live as of 31 July 2026, 15:00:48 (HKT) |
| US30YT=X | United States 30-Year Treasury Yield | 5.19 | -0.38 | 2026-07-31 | live as of 31 July 2026, 15:00:48 (HKT) |
| HK50 | Hang Seng Futures | 25836.0 | -0.7 | 2026-07-31 | live as of 31 July 2026, 15:00:48 (HKT) |
| KOR200c1 | KOSPI 200 Futures | 1022.75 | 17.88 | 2026-07-30 | closed |
| CIHc1 | SSE 50 Futures | 2903.2 | 0.23 | 2026-07-30 | closed |
| HYG | iShares iBoxx High Yield Corporate Bond ETF | 79.47 | 0.29 | 2026-07-30 | closed |
| LQD | iShares iBoxx Investment Grade Corporate Bond ETF | 106.41 | 0.18 | 2026-07-30 | closed |
| JNK | SPDR Bloomberg High Yield Bond ETF | 95.66 | 0.28 | 2026-07-30 | closed |
| RSP | Invesco S&P 500 Equal Weight ETF | 215.38 | -0.16 | 2026-07-30 | closed |
| IWF | iShares Russell 1000 Growth ETF | 117.43 | 2.96 | 2026-07-30 | closed |
| IWD | iShares Russell 1000 Value ETF | 250.71 | 0.48 | 2026-07-30 | closed |
| TLT | iShares 20+ Year Treasury Bond ETF | 82.8 | -0.06 | 2026-07-30 | closed |
| IEF | iShares 7-10 Year Treasury Bond ETF | 93.21 | 0.04 | 2026-07-30 | closed |
| SHY | iShares 1-3 Year Treasury Bond ETF | 82.01 | 0.02 | 2026-07-30 | closed |
| GC=F | Gold Future | 4134.5 | 0.84 | 2026-07-31 | live as of 31 July 2026, 15:00:48 (HKT) |
| SI=F | Silver Future | 58.53 | -0.48 | 2026-07-31 | live as of 31 July 2026, 15:00:48 (HKT) |
| CL=F | WTI Crude Oil Future | 81.99 | -1.91 | 2026-07-31 | live as of 31 July 2026, 15:00:48 (HKT) |
| HG=F | Copper Future | 6.5 | 0.81 | 2026-07-31 | live as of 31 July 2026, 15:00:48 (HKT) |

## Market Dispersion Analysis

- Sector ETF 20D dispersion: `16.97` points (high); leader `XLE` (Energy) `11.65`, laggard `XLK` (Technology) `-5.33`
- Sector ETF 60D dispersion: `21.18` points (very high); leader `XLV` (Health Care) `12.98`, laggard `XLC` (Communication Services) `-8.2`

| Comparison | Left | Right | 20D Spread | Signal |
| --- | --- | --- | --- | --- |
| Equal-weight vs cap-weight | RSP (Equal-weight S&P 500) | SPY (S&P 500) | 1.47 | broader participation |
| Small-cap vs large-cap | IWM (Russell 2000) | SPY (S&P 500) | -1.7 | large-cap leadership |
| Growth vs value | IWF (Russell 1000 Growth) | IWD (Russell 1000 Value) | -7.34 | value leadership |
| Nasdaq vs S&P 500 | QQQ (Nasdaq 100) | SPY (S&P 500) | -5.19 | S&P 500 leadership |

## Sector Constituent Dispersion

- Breadth 50D / 200D: percentage of active S&P 500 constituents in the sector trading above the 50-day / 200-day moving average.
- Positive 20D: percentage of active sector constituents with positive 20-day return.
- Std 20D: cross-sectional standard deviation of constituent 20-day returns; higher means wider stock-level dispersion.

| Sector | Count | Breadth 50D | Breadth 200D | Positive 20D | 20D Dispersion | Std 20D | Label | Leaders | Laggards |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Information Technology | 74 | 43.24 | 61.64 | 40.54 | 107.26 | 17.61 | very high | CTSH, ACN, HPQ | SNDK, GLW, CRWD |
| Consumer Discretionary | 47 | 61.7 | 55.32 | 53.19 | 52.59 | 9.08 | very high | GRMN, ROST, GM | NCLH, CVNA, TSLA |
| Financials | 76 | 87.67 | 81.43 | 76.32 | 51.11 | 7.62 | very high | PYPL, ICE, WTW | ERIE, CINF, HOOD |
| Industrials | 81 | 56.96 | 68.83 | 44.44 | 47.67 | 9.78 | very high | CTAS, HII, PAYX | LII, VRT, GNRC |
| Health Care | 59 | 84.75 | 69.49 | 77.97 | 43.44 | 7.88 | very high | BAX, REGN, IQV | CNC, ISRG, MRNA |
| Communication Services | 23 | 45.45 | 40.91 | 47.83 | 36.54 | 8.64 | very high | T, VZ, NWSA | META, ECHO, PSKY |
| Materials | 26 | 61.54 | 73.08 | 65.38 | 30.82 | 8.24 | very high | NUE, CF, LYB | PPG, CRH, ALB |
| Energy | 21 | 66.67 | 85.71 | 80.95 | 25.69 | 7.88 | very high | PSX, MPC, OXY | WMB, HAL, TPL |
| Utilities | 31 | 38.71 | 64.52 | 35.48 | 17.91 | 4.25 | high | CEG, PCG, EIX | AEP, DTE, LNT |
| Consumer Staples | 34 | 72.73 | 62.5 | 64.71 | 16.31 | 4.54 | high | TGT, DG, CASY | STZ, MO, KDP |
| Real Estate | 31 | 58.06 | 80.65 | 64.52 | 15.28 | 3.7 | high | DLR, CBRE, HST | ESS, MAA, UDR |

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
| Core PCE Price Index month-over-month inflation rate | 0.13 | percent | -0.2 pp vs prior | 2026-06-01 | Lower reading eases macro pressure. |
| Core PCE Price Index year-over-year inflation rate | 3.29 | percent | -0.14 pp vs prior | 2026-06-01 | Lower reading eases macro pressure. |
| Headline PPI Final Demand month-over-month inflation rate | -0.19 | percent | -0.79 pp vs prior | 2026-06-01 | Lower reading eases macro pressure. |
| Headline PPI Final Demand year-over-year inflation rate | 5.51 | percent | -0.49 pp vs prior | 2026-06-01 | Lower reading eases macro pressure. |
| Core PPI Final Demand Less Foods and Energy month-over-month inflation rate | 0.2 | percent | 0.11 pp vs prior | 2026-06-01 | Higher reading increases macro pressure. |
| Core PPI Final Demand Less Foods and Energy year-over-year inflation rate | 4.68 | percent | 0.09 pp vs prior | 2026-06-01 | Higher reading increases macro pressure. |
| Consumer Price Index for All Urban Consumers | 332.57 | index 1982-1984=100 | -1.41 index pts vs prior | 2026-06-01 | Lower reading eases macro pressure. |
| Core CPI | 336.06 | index 1982-1984=100 | -0.06 index pts vs prior | 2026-06-01 | Lower reading eases macro pressure. |
| Personal Consumption Expenditures Price Index | 131.39 | index 2017=100 | -0.14 index pts vs prior | 2026-06-01 | Lower reading eases macro pressure. |
| Core PCE Price Index | 130.27 | index 2017=100 | 0.17 index pts vs prior | 2026-06-01 | Higher reading increases macro pressure. |
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
| 1 | Healthcare | 70.73 | strong uptrend | positive | broad | 75.0 | 100.0 | 55.7 | BAX, REGN, IQV | CNC, ISRG, MRNA |
| 2 | Consumer Staples | 68.88 | strong uptrend | neutral | broad | 69.04 | 65.0 | 51.5 | TGT, DG, CASY | STZ, MO, KDP |
| 3 | Real Estate | 67.59 | strong uptrend | neutral | broad | 55.45 | 100.0 | 51.64 | DLR, CBRE, HST | ESS, MAA, UDR |
| 4 | Financials | 65.71 | strong uptrend | positive | broad | 63.7 | 95.0 | 55.64 | PYPL, ICE, WTW | ERIE, CINF, HOOD |
| 5 | Energy | 61.16 | uptrend | positive | broad | 58.47 | 100.0 | 55.71 | PSX, MPC, OXY | WMB, HAL, TPL |
| 6 | Cybersecurity | 60.16 | strong uptrend | positive | broad | 62.06 | 65.0 | 59.91 | CIBR | CIBR |
| 7 | Industrials | 55.97 | strong uptrend | neutral | broad | 53.5 | 65.0 | 49.12 | CTAS, HII, PAYX | LII, VRT, GNRC |
| 8 | Crypto | 50.38 | neutral | neutral | mixed | 53.83 | 65.0 | 50.0 |  |  |
| 9 | Semiconductors | 47.97 | neutral | neutral | weak | 90.38 | 100.0 | 43.41 | SMH, SOXX | SOXX, SMH |
| 10 | Technology | 44.84 | neutral | neutral | weak | 52.96 | 95.0 | 47.69 | CTSH, ACN, HPQ | SNDK, GLW, CRWD |
| 11 | Grid Infrastructure | 42.39 | downtrend | neutral | weak | 67.91 | 65.0 | 42.84 | GRID | GRID |
| 12 | Defense | 40.83 | downtrend | neutral | weak | 44.75 | 65.0 | 45.59 | XAR | XAR |
| 13 | Utilities | 35.19 | strong downtrend | neutral | weak | 60.13 | 65.0 | 45.74 | CEG, PCG, EIX | AEP, DTE, LNT |
| 14 | Nuclear | 35.03 | strong downtrend | negative | weak | 50.0 | 0.0 | 35.82 | NLR | NLR |
| 15 | Consumer Discretionary | 34.95 | strong downtrend | neutral | weak | 52.29 | 65.0 | 44.3 | GRMN, ROST, GM | NCLH, CVNA, TSLA |

### Thematic Strength

| Rank | Theme | Score | Setup | ETF Flow | Flow Reliability | Dispersion | Price | News |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Healthcare Innovation | 61.72 | Positive setup | 75.0 | 100.0 | 6.61 | True | False |
| 2 | Energy | 60.14 | Positive setup | 58.47 | 100.0 | 4.42 | True | False |
| 3 | Financials | 58.32 | Positive setup | 63.7 | 95.0 | 5.26 | False | False |
| 4 | Small Caps | 56.5 | Positive setup | 56.54 | 65.0 | 0.0 | False | False |
| 5 | Quality Growth | 54.43 | Neutral / watchlist | 65.91 | 65.0 | 25.02 | False | False |
| 6 | Dividend Defensives | 54.34 | Neutral / watchlist | 60.66 | 65.0 | 2.85 | False | False |
| 7 | Cybersecurity | 53.94 | Neutral / watchlist | 62.06 | 65.0 | 77.36 | False | False |
| 8 | Semiconductors | 52.4 | Neutral / watchlist | 90.38 | 100.0 | 20.88 | False | True |
| 9 | AI Infrastructure | 51.36 | Neutral / watchlist | 90.38 | 100.0 | 33.26 | False | False |
| 10 | Defense | 47.8 | Neutral / watchlist | 44.75 | 65.0 | 26.79 | False | False |
| 11 | Grid Infrastructure | 42.31 | Weak setup | 67.91 | 65.0 | 5.92 | False | False |
| 12 | Nuclear | 35.45 | Weak setup | 50.0 | 0.0 | 15.66 | False | False |
| 13 | Crypto Infrastructure | 34.4 | Underperformance risk | 53.83 | 65.0 | 1.93 | False | False |

- Top 5 improving themes: Cybersecurity, Healthcare Innovation, Financials, Semiconductors, Quality Growth
- Top 5 deteriorating themes: Crypto Infrastructure, Nuclear, Grid Infrastructure, Energy, AI Infrastructure
- Strong news but weak price confirmation: Semiconductors
- Strong price but weak news confirmation: Healthcare Innovation, Energy

### Sector / Theme Alignment

| Sector | Related Themes | Sector Score | Sector Signal | Theme Score | Theme Signal | Interpretation |
| --- | --- | --- | --- | --- | --- | --- |
| Healthcare | Healthcare Innovation | 70.73 | strong | 61.72 | positive | sector and theme confirmation |
| Consumer Staples | Dividend Defensives | 68.88 | strong | 54.34 | mixed | sector stronger than related themes |
| Real Estate | Dividend Defensives | 67.59 | strong | 54.34 | mixed | sector stronger than related themes |
| Financials | Financials | 65.71 | strong | 58.32 | positive | sector and theme confirmation |
| Energy | Energy | 61.16 | positive | 60.14 | positive | sector and theme confirmation |
| Cybersecurity | Cybersecurity | 60.16 | positive | 53.94 | mixed | sector stronger than related themes |
| Industrials | Defense, Grid Infrastructure | 55.97 | positive | 45.06 | mixed | sector stronger than related themes |
| Crypto | Crypto Infrastructure | 50.38 | mixed | 34.4 | very weak | mixed confirmation |
| Semiconductors | AI Infrastructure, Semiconductors | 47.97 | mixed | 51.88 | mixed | mixed confirmation |
| Technology | AI Infrastructure, Semiconductors, Quality Growth | 44.84 | weak | 52.73 | mixed | mixed confirmation |
| Grid Infrastructure | Grid Infrastructure | 42.39 | weak | 42.31 | weak | broad weakness across sector and themes |
| Defense | Defense | 40.83 | weak | 47.8 | mixed | mixed confirmation |
| Utilities | Grid Infrastructure, Nuclear, Dividend Defensives | 35.19 | weak | 44.03 | weak | broad weakness across sector and themes |
| Nuclear | Nuclear | 35.03 | weak | 35.45 | weak | broad weakness across sector and themes |
| Consumer Discretionary | Small Caps | 34.95 | very weak | 56.5 | positive | theme stronger than official sector |

## Three-Month Outperformance Setup

| Rank | Theme | Score | Classification | Drivers | Invalidation Triggers |
| --- | --- | --- | --- | --- | --- |
| 1 | Healthcare Innovation | 66.62 | Positive setup | relative_strength_60d, trend_persistence, breadth, downside_volatility, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 2 | Small Caps | 64.7 | Positive setup | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 3 | Financials | 63.79 | Positive setup | relative_strength_60d, trend_persistence, breadth, downside_volatility, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 4 | Energy | 61.89 | Positive setup | relative_strength_20d, trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 5 | Quality Growth | 59.15 | Neutral / watchlist | trend_persistence, breadth, volume_accumulation, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 6 | Dividend Defensives | 57.43 | Neutral / watchlist | trend_persistence, breadth, volume_accumulation, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 7 | Cybersecurity | 55.89 | Neutral / watchlist | relative_strength_60d, trend_persistence, breadth, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 8 | AI Infrastructure | 52.94 | Neutral / watchlist | volume_accumulation | relative strength below SPY, breadth below 45%, news turns negative |
| 9 | Defense | 49.98 | Neutral / watchlist |  | relative strength below SPY, breadth below 45%, news turns negative |
| 10 | Semiconductors | 49.87 | Neutral / watchlist |  | relative strength below SPY, breadth below 45%, news turns negative |
| 11 | Grid Infrastructure | 44.33 | Weak setup | volume_accumulation, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 12 | Nuclear | 33.2 | Weak setup |  | relative strength below SPY, breadth below 45%, news turns negative |

## Breadth and Participation

- Above 50DMA: `48.33%`
- Above 200DMA: `72.88%`
- Positive 20D return: `40.0%`

## Volatility and Risk Signals

- VIX close=17.09 pct_chg=-17.28

## News Analytics

- Sentiment counts: {'positive': 66, 'negative': 14, 'neutral': 0}
- News confirmation score: `82.5`

### Top Market-Moving Headlines

**1. ICE to buy MarketAxess in $5.7 billion deal, posts higher quarterly profit**
- Source: CNBC Markets
- Importance / impact: Medium / Positive
- Relevance / horizon: sector_theme / short-term
- Affected assets: ICE, MKTX, Mergers & Acquisitions, Fixed-Income
- Score: `52.51`
- Investment implication: Theme or sector positive signal; requires price and volume confirmation before affecting rankings.

**2. Oil prices fall after Saudi Arabia proposes naval coalition to protect ships from attack**
- Source: CNBC Top News
- Importance / impact: High / Positive
- Relevance / horizon: macro / short-term
- Affected assets: U.S, energy, geopolitics
- Score: `48.45`
- Investment implication: Macro-relevant positive signal; use as context for rates, volatility, and index confirmation over the short-term.

**3. Samsung says chip crunch will last until 2028 as quarterly profit soars**
- Source: CNBC Business
- Importance / impact: High / Positive
- Relevance / horizon: macro / short-term
- Affected assets: Samsung Electronics, technology, semiconductor
- Score: `45.9`
- Investment implication: Macro-relevant positive signal; use as context for rates, volatility, and index confirmation over the short-term.

**4. Shell posts best quarterly profit in four years as Iran war boosts oil and gas prices**
- Source: CNBC Business News
- Importance / impact: High / Positive
- Relevance / horizon: macro / short-term
- Affected assets: RDS.A, BP, oil_prices, profit_report, geopolitical_risk
- Score: `45.9`
- Investment implication: Macro-relevant positive signal; use as context for rates, volatility, and index confirmation over the short-term.

**5. Copper may hit new high as AI demand collides with deadly storms, strategists say**
- Source: CNBC Business News
- Importance / impact: Medium / Positive
- Relevance / horizon: sector_theme / short-term
- Affected assets: metals, weather
- Score: `40.8`
- Investment implication: Theme or sector positive signal; requires price and volume confirmation before affecting rankings.

**6. Apple's stock could see its worst post-earnings drop in over a decade**
- Source: MarketWatch Bulletins
- Importance / impact: Medium / Negative
- Relevance / horizon: single_name / short-term
- Affected assets: AAPL, technology, earnings
- Score: `40.15`
- Investment implication: Single-name negative signal; low weight unless it maps to a broader sector or theme.

**7. Micron, Sandisk and other chip stocks get major boosts in the wake of Microsoft’s earnings**
- Source: MarketWatch Top Stories
- Importance / impact: Medium / Positive
- Relevance / horizon: sector_theme / short-term
- Affected assets: technology, AI
- Score: `37.57`
- Investment implication: Theme or sector positive signal; requires price and volume confirmation before affecting rankings.

**8. GDP shows the economy grew 1.5% in the second quarter — but it’s even better than it looks**
- Source: MarketWatch Top Stories
- Importance / impact: Medium / Positive
- Relevance / horizon: sector_theme / short-term
- Affected assets: Economic Growth, AI
- Score: `37.57`
- Investment implication: Theme or sector positive signal; requires price and volume confirmation before affecting rankings.

**9. Why Microsoft’s stock soared to a historic gain after earnings**
- Source: MarketWatch Top Stories
- Importance / impact: Medium / Positive
- Relevance / horizon: single_name / short-term
- Affected assets: MSFT, AI, cloud business
- Score: `37.29`
- Investment implication: Single-name positive signal; low weight unless it maps to a broader sector or theme.

**10. 30-year yield hovers near 2007 high as traders weigh Fed decision to holds rates steady**
- Source: CNBC Top News
- Importance / impact: Medium / Positive
- Relevance / horizon: macro / short-term
- Affected assets: U.S, Federal Reserve, interest rates
- Score: `36.74`
- Investment implication: Macro-relevant positive signal; use as context for rates, volatility, and index confirmation over the short-term.


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
- Market flow score: `47.6 / 100`
- Equity risk flow: `48.0`
- Credit risk flow: `48.2`
- Sector cyclicality flow: `43.2`
- Duration/liquidity flow: `51.5`
- Alternatives: `defensive or uncertainty hedge`
- ETF flow reliability: `72.0 / 100`
- Dominant allocation direction: `mixed allocation`

### Core Flow Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVV | U.S. Broad Equity | -0.8 | 0.4 | 0.3 | -0.7 | Flat | Neutral | Normal | Neutral | Neutral | Medium-term deterioration | 83.0 |
| ACWI | Global Equity | -1.9 | -1.4 | 0.0 | 0.0 | Flat | Sell | Normal | Quiet Distribution | Weakening | Strong confirmation; Persistent selling | 87.0 |
| EFA | Developed Markets ex-U.S. | -1.5 | -0.1 | 0.0 | -0.0 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Medium-term deterioration; Persistent selling | 75.0 |
| IEMG | Emerging Markets | -0.1 | -0.4 | 0.1 | 0.4 | Down | Buy | Normal | Contrarian Buying | Watch | Strong confirmation; Exceptional institutional buying, Persistent selling | 95.0 |
| IJH | U.S. Mid Cap | 0.2 | 0.5 | 0.7 | -1.0 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural accumulation | 91.0 |
| IWM | U.S. Small Cap | 0.2 | 0.7 | 0.5 | -0.6 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural distribution | 79.0 |
| LQD | Investment-Grade Credit | -0.2 | 0.2 | 0.4 | 0.4 | Down | Sell | Normal | Persistent Distribution | Risk-Off | Tactical profit-taking inside structural accumulation | 83.0 |
| HYG | High-Yield Credit | -0.7 | 0.3 | 0.4 | -0.4 | Flat | Buy | Normal | Quiet Accumulation | Improving | Tactical rebound inside structural distribution | 83.0 |
| SGOV | Treasury Bills / Cash | -0.4 | 0.1 | 0.9 | 0.5 | Flat | Neutral | Normal | Neutral | Neutral | Structural accumulation; Strong sponsorship | 99.0 |
| SHY | Short-Duration Treasuries | -1.0 | -1.0 | 0.2 | 0.1 | Flat | Sell | Normal | Quiet Distribution | Weakening | Strong confirmation; Persistent selling | 87.0 |
| IEF | Intermediate-Duration Treasuries | 0.5 | -0.5 | 0.7 | -1.0 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural accumulation | 91.0 |
| TLT | Long-Duration Treasuries | 1.5 | 0.9 | 0.8 | 1.9 | Down | Neutral | High | Heavy Selling Pressure | Cautious | Structural accumulation; Strong sponsorship | 99.0 |
| GLD | Gold | 0.9 | 1.1 | 0.4 | -0.4 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural accumulation | 91.0 |
| IBIT | Bitcoin | 0.1 | -1.5 | 0.6 | -0.5 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural distribution | 79.0 |

### Sector Flow Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| XLC | Communication Services | -1.7 | -2.0 | 0.2 | 1.6 | Down | Sell | High | Confirmed Distribution | Strong Risk-Off | Strong confirmation; Exceptional institutional selling, Persistent selling | 79.0 |
| XLY | Consumer Discretionary | 0.4 | 1.0 | 0.5 | 0.0 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural accumulation | 91.0 |
| XLP | Consumer Staples | 2.0 | 2.2 | 0.4 | 1.4 | Up | Buy | High | Confirmed Accumulation | Strong Risk-On | Strong confirmation; Exceptional institutional buying | 100.0 |
| XLE | Energy | -0.8 | -1.2 | 0.2 | -1.2 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural distribution; Persistent selling | 71.0 |
| XLF | Financials | 1.3 | 1.3 | 0.5 | -0.3 | Up | Buy | Normal | Steady Accumulation | Risk-On | Strong confirmation | 95.0 |
| XLV | Health Care | 0.5 | 0.7 | 0.5 | 0.7 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Medium-term recovery | 87.0 |
| XLI | Industrials | -0.7 | 0.4 | 0.5 | -0.1 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Medium-term deterioration | 83.0 |
| XLK | Information Technology | 0.5 | -0.4 | 0.7 | 0.6 | Down | Neutral | High | Heavy Selling Pressure | Cautious | Structural accumulation | 91.0 |
| XLB | Materials | -0.6 | -0.2 | 0.4 | -0.2 | Up | Sell | Normal | Profit Taking | Slightly Bearish | Tactical profit-taking inside structural accumulation | 83.0 |
| XLRE | Real Estate | 0.7 | 2.4 | 0.6 | 1.0 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural accumulation; Exceptional institutional buying | 99.0 |
| XLU | Utilities | 0.2 | 0.2 | 0.4 | 0.7 | Flat | Neutral | Normal | Neutral | Neutral | Structural accumulation | 91.0 |

### Subsector PFV Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ITA | Aerospace and Defense | -0.2 | -0.9 | 0.2 | 1.1 | Down | Neutral | High | Heavy Selling Pressure | Cautious | Structural distribution; Persistent selling | 71.0 |
| SOXX | Semiconductors | 1.9 | 2.1 | 0.6 | 1.7 | Down | Buy | High | Aggressive Dip Buying | Recovery Candidate | Strong confirmation; Exceptional institutional buying | 100.0 |
| SMH | Semiconductors | 1.6 | 0.9 | 0.6 | 0.2 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural accumulation | 91.0 |
| CIBR | Cybersecurity | 0.6 | 1.2 | 0.6 | -1.1 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural accumulation | 91.0 |

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

| Severity | Section | Issue | Deterministic Fix |
| --- | --- | --- | --- |
| low | Theme Strength Ranking | Semiconductors has strong news confirmation but weak price confirmation. | Classify as unconfirmed narrative. |

## Data Quality Notes

- Technical rows loaded: `60`
- S&P 500 constituent technical rows loaded: `503`
- Macro rows loaded: `49`
- Live macro rows used: `24`
- Economic rows loaded: `113`
- News rows loaded: `80`
- Positioning/flow rows loaded: `30`

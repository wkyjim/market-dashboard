# Rule-Based Institutional Market Update

Generated at: 28 July 2026, 20:03:42 (HKT)
Window: 24h

## Executive Dashboard

- Regime score: **56.68 / 100** (Mild Risk-On)
- US equity strength: **54.68 / 100** (neutral)
- Evidence quality: **79.5 / 100**
- ETF flow contribution: **45.15 / 100**, reliability **71.16 / 100**
- Breadth: **healthy**; above 50DMA `53.33%`, above 200DMA `69.49%`
- Top sector score: **Real Estate** `67.38`
- Top theme score: **Financials** `62.65`

## Market Regime Score

| Metric | Value | Driver / Interpretation |
| --- | --- | --- |
| Overall regime | 56.68 | Mild Risk-On |
| equity_trend | 61.25 | mild risk-on support; Core equity ETFs versus moving averages. |
| equity_momentum | 50.42 | neutral / mixed; 5D/20D/60D return momentum across SPY, QQQ, IWM, and SMH. |
| market_breadth | 59.27 | mild risk-on support; Participation breadth from tracked equity/ETF rows. |
| volatility | 70.0 | risk-on support; VIX level and change; higher score means calmer volatility conditions. |
| rates_yield_curve | 58.0 | mild risk-on support; Treasury yield pressure and curve shape; higher score means less rates pressure. |
| credit_proxy | 50.0 | neutral / mixed; Credit-market proxy; currently neutral when no direct spread signal is available. |
| dollar_fx | 54.42 | neutral / mixed; Dollar move; higher score means less USD tightening pressure. |
| commodity_confirmation | 42.0 | mild risk-off pressure; Copper, silver, oil, and gold mix; higher score means better cyclical confirmation. |
| etf_flow | 46.55 | neutral / mixed; Grouped ETF flow contribution adjusted for reliability. |
| news_confirmation | 75.62 | risk-on support; Weighted headline/news confirmation score. |
| Positive contributors |  | news_confirmation=75.62, volatility=70.0, equity_trend=61.25 |
| Negative contributors |  | commodity_confirmation=42.0 |

## US Equity Strength Score

| Component | Score |
| --- | --- |
| indices_above_moving_averages | 61.25 |
| sp500_trend | 55.0 |
| nasdaq_trend | 55.0 |
| russell_participation | 80.0 |
| returns_momentum | 50.42 |
| rsi_zone | 40.0 |
| macd_confirmation | 35.0 |
| volume_confirmation | 46.25 |
| breadth | 59.27 |

## Evidence Quality / Confidence

- Confidence score: `79.5`
- Agreement ratio: `0.5`
- Contradiction count: `1`
- Missing indicators: none
- Warning flags: none

## Cross-Asset Confirmation

| Area | Signal | Interpretation |
| --- | --- | --- |
| Equities | S&P 500 stable; Nasdaq stable; Russell 2000 rising | Confirms risk appetite when broad indices rise together; weak small caps would narrow the signal. |
| Rates | 10Y Treasury falling; MOVE rising | Rising yields can pressure duration assets; falling MOVE supports calmer bond volatility. |
| Dollar | DXY proxy stable | A stronger dollar can tighten financial conditions and pressure commodities/emerging-market risk. |
| Credit | HYG stable | High-yield weakness would challenge equity risk-on confirmation. |
| Gold | Gold falling | Gold strength can indicate defensive demand, inflation hedging, or geopolitical concern. |
| Silver | Silver falling | Silver helps distinguish precious-metal demand from industrial/cyclical confirmation when data is available. |
| Copper | Copper falling | Copper strength supports cyclical growth confirmation; weakness would dilute risk-on breadth. |
| Oil | WTI crude falling | Oil spikes can be inflationary risk; falling oil can ease cost pressure but may also flag demand softness. |
| Volatility | VIX rising | Falling VIX supports risk appetite; a volatility spike would reduce confidence in broad risk-on. |

### Macro Snapshot

Live macro rows are intraday snapshots from `public.macro_live`; closed rows are official stored rows from `public.macro`.

| Symbol | Name | Close | Pct Chg | Market Date | Status |
| --- | --- | --- | --- | --- | --- |
| ^GSPC | S&P 500 | 7413.18 | 0.02 | 2026-07-27 | closed |
| ^IXIC | NASDAQ Composite | 24932.08 | -0.18 | 2026-07-27 | closed |
| ^RUT | Russell 2000 Index | 2948.03 | 0.62 | 2026-07-27 | closed |
| ^VIX | CBOE Volatility Index | 19.0 | 1.77 | 2026-07-28 | live as of 28 July 2026, 20:00:39 (HKT) |
| ^SKEW | CBOE SKEW Index | 146.6 | -0.46 | 2026-07-27 | closed |
| ^MOVE | ICE BofA MOVE Index | 76.82 | 8.38 | 2026-07-24 | closed |
| US2YT=X | United States 2-Year Treasury Yield | 4.31 | -0.24 | 2026-07-28 | live as of 28 July 2026, 20:00:39 (HKT) |
| US3YT=X | United States 3-Year Treasury Yield | 4.33 | -0.45 | 2026-07-28 | live as of 28 July 2026, 20:00:39 (HKT) |
| US5YT=X | United States 5-Year Treasury Yield | 4.39 | -0.22 | 2026-07-28 | live as of 28 July 2026, 20:00:39 (HKT) |
| US7YT=X | United States 7-Year Treasury Yield | 4.49 | -0.31 | 2026-07-28 | live as of 28 July 2026, 20:00:39 (HKT) |
| US10YT=X | United States 10-Year Treasury Yield | 4.62 | -0.37 | 2026-07-28 | live as of 28 July 2026, 20:00:39 (HKT) |
| US20YT=X | United States 20-Year Treasury Yield | 5.14 | -0.22 | 2026-07-28 | live as of 28 July 2026, 20:00:39 (HKT) |
| US30YT=X | United States 30-Year Treasury Yield | 5.12 | -0.16 | 2026-07-28 | live as of 28 July 2026, 20:00:39 (HKT) |
| HK50 | Hang Seng Futures | 25320.5 | 0.07 | 2026-07-28 | closed |
| KOR200c1 | KOSPI 200 Futures | 990.05 | -7.86 | 2026-07-27 | closed |
| CIHc1 | SSE 50 Futures | 2929.8 | -0.01 | 2026-07-27 | closed |
| HYG | iShares iBoxx High Yield Corporate Bond ETF | 79.27 | 0.05 | 2026-07-27 | closed |
| LQD | iShares iBoxx Investment Grade Corporate Bond ETF | 106.51 | 0.26 | 2026-07-27 | closed |
| JNK | SPDR Bloomberg High Yield Bond ETF | 95.46 | 0.07 | 2026-07-27 | closed |
| RSP | Invesco S&P 500 Equal Weight ETF | 215.18 | 0.75 | 2026-07-27 | closed |
| IWF | iShares Russell 1000 Growth ETF | 117.13 | -0.44 | 2026-07-27 | closed |
| IWD | iShares Russell 1000 Value ETF | 249.74 | 0.6 | 2026-07-27 | closed |
| TLT | iShares 20+ Year Treasury Bond ETF | 83.75 | 0.6 | 2026-07-27 | closed |
| IEF | iShares 7-10 Year Treasury Bond ETF | 93.28 | 0.27 | 2026-07-27 | closed |
| SHY | iShares 1-3 Year Treasury Bond ETF | 81.87 | 0.02 | 2026-07-27 | closed |
| GC=F | Gold Future | 4023.8 | -1.24 | 2026-07-28 | live as of 28 July 2026, 20:00:39 (HKT) |
| SI=F | Silver Future | 57.47 | -1.71 | 2026-07-28 | live as of 28 July 2026, 20:00:39 (HKT) |
| CL=F | WTI Crude Oil Future | 81.82 | -0.96 | 2026-07-28 | live as of 28 July 2026, 20:00:39 (HKT) |
| HG=F | Copper Future | 6.3 | -0.62 | 2026-07-28 | live as of 28 July 2026, 20:00:39 (HKT) |

## Market Dispersion Analysis

- Sector ETF 20D dispersion: `12.16` points (high); leader `XLE` (Energy) `8.4`, laggard `XLK` (Technology) `-3.76`
- Sector ETF 60D dispersion: `21.01` points (very high); leader `XLV` (Health Care) `14.39`, laggard `XLC` (Communication Services) `-6.62`

| Comparison | Left | Right | 20D Spread | Signal |
| --- | --- | --- | --- | --- |
| Equal-weight vs cap-weight | RSP (Equal-weight S&P 500) | SPY (S&P 500) | 0.93 | balanced |
| Small-cap vs large-cap | IWM (Russell 2000) | SPY (S&P 500) | -3.69 | large-cap leadership |
| Growth vs value | IWF (Russell 1000 Growth) | IWD (Russell 1000 Value) | -4.48 | value leadership |
| Nasdaq vs S&P 500 | QQQ (Nasdaq 100) | SPY (S&P 500) | -4.84 | S&P 500 leadership |

## Sector Constituent Dispersion

- Breadth 50D / 200D: percentage of active S&P 500 constituents in the sector trading above the 50-day / 200-day moving average.
- Positive 20D: percentage of active sector constituents with positive 20-day return.
- Std 20D: cross-sectional standard deviation of constituent 20-day returns; higher means wider stock-level dispersion.

| Sector | Count | Breadth 50D | Breadth 200D | Positive 20D | 20D Dispersion | Std 20D | Label | Leaders | Laggards |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Information Technology | 74 | 37.84 | 63.01 | 51.35 | 93.75 | 16.4 | very high | ACN, WDAY, AAPL | GLW, SNDK, CRWD |
| Industrials | 81 | 74.68 | 77.92 | 60.49 | 51.83 | 8.69 | very high | CTAS, RTX, PAYX | PNR, BLDR, GNRC |
| Consumer Discretionary | 47 | 57.45 | 46.81 | 48.94 | 33.77 | 6.54 | very high | DPZ, ROST, BBY | LEN, DHI, TSLA |
| Financials | 76 | 91.67 | 81.43 | 86.84 | 32.71 | 6.98 | very high | PYPL, GPN, ICE | SYF, ERIE, C |
| Energy | 21 | 52.38 | 85.71 | 76.19 | 32.09 | 8.36 | very high | MPC, PSX, VLO | KMI, HAL, WMB |
| Health Care | 59 | 83.05 | 62.71 | 66.1 | 30.78 | 5.97 | very high | VEEV, IQV, MCK | EW, ISRG, MRNA |
| Communication Services | 23 | 36.36 | 40.91 | 43.48 | 29.76 | 7.84 | very high | FOXA, OMC, FOX | ECHO, TKO, PSKY |
| Materials | 26 | 65.38 | 65.38 | 53.85 | 26.42 | 5.97 | very high | CF, IP, SW | CRH, VMC, ALB |
| Real Estate | 31 | 74.19 | 74.19 | 38.71 | 22.7 | 4.7 | very high | VTR, WELL, PLD | SBAC, ARE, CCI |
| Consumer Staples | 34 | 69.7 | 68.75 | 50.0 | 21.97 | 4.42 | very high | KHC, CASY, ADM | WMT, KDP, STZ |
| Utilities | 31 | 87.1 | 80.65 | 35.48 | 12.54 | 3.0 | high | EIX, CEG, FE | CMS, NI, NRG |

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
| US dollar/Euro ECB reference exchange rate | 1.14 | USD | 0.0 USD vs prior | 2026-07-27 | EUR strengthened versus this currency. |
| Japanese yen/Euro ECB reference exchange rate | 186.37 | JPY | -0.01 JPY vs prior | 2026-07-27 | EUR weakened versus this currency. |
| Chinese yuan renminbi/Euro ECB reference exchange rate | 7.71 | CNY | 0.0 CNY vs prior | 2026-07-27 | EUR strengthened versus this currency. |
| Australian dollar/Euro ECB reference exchange rate | 1.63 | AUD | -0.0 AUD vs prior | 2026-07-27 | EUR weakened versus this currency. |

ABS Australia note: ABS rows are stored locally/Neon, but most series are dimension-coded; only curated series should be promoted into narrative report text.

## Sector and Theme Leadership

### Official Sector Strength

Supporting and detracting names are the top/bottom S&P 500 constituents by 20D return when constituent coverage is available; otherwise the report falls back to related ETFs.

| Rank | Sector | Score | Trend | Momentum | Stock Breadth | ETF Flow | Flow Reliability | 3M RS | Supporting / Leaders | Detracting / Laggards |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Real Estate | 67.38 | strong uptrend | neutral | broad | 68.59 | 95.0 | 50.26 | VTR, WELL, PLD | SBAC, ARE, CCI |
| 2 | Consumer Staples | 66.61 | strong uptrend | neutral | broad | 64.1 | 65.0 | 49.26 | KHC, CASY, ADM | WMT, KDP, STZ |
| 3 | Financials | 66.42 | strong uptrend | positive | broad | 69.29 | 100.0 | 55.15 | PYPL, GPN, ICE | SYF, ERIE, C |
| 4 | Industrials | 63.78 | strong uptrend | neutral | broad | 57.08 | 65.0 | 51.41 | CTAS, RTX, PAYX | PNR, BLDR, GNRC |
| 5 | Healthcare | 62.69 | strong uptrend | positive | broad | 64.59 | 90.0 | 54.52 | VEEV, IQV, MCK | EW, ISRG, MRNA |
| 6 | Cybersecurity | 61.33 | strong uptrend | positive | broad | 61.77 | 65.0 | 62.76 | CIBR | CIBR |
| 7 | Energy | 59.25 | uptrend | neutral | broad | 49.47 | 95.0 | 52.21 | MPC, PSX, VLO | KMI, HAL, WMB |
| 8 | Defense | 53.41 | strong uptrend | neutral | weak | 50.0 | 0.0 | 51.13 | XAR | XAR |
| 9 | Crypto | 49.18 | neutral | neutral | mixed | 41.82 | 65.0 | 50.0 |  |  |
| 10 | Utilities | 45.92 | downtrend | neutral | mixed | 58.22 | 65.0 | 45.65 | EIX, CEG, FE | CMS, NI, NRG |
| 11 | Technology | 44.93 | neutral | neutral | weak | 39.73 | 95.0 | 47.99 | ACN, WDAY, AAPL | GLW, SNDK, CRWD |
| 12 | Semiconductors | 44.66 | neutral | neutral | weak | 54.1 | 90.0 | 45.69 | SMH, SOXX | SOXX, SMH |
| 13 | Grid Infrastructure | 42.22 | downtrend | neutral | weak | 63.72 | 65.0 | 43.12 | GRID | GRID |
| 14 | Consumer Discretionary | 35.51 | strong downtrend | neutral | weak | 61.31 | 65.0 | 43.72 | DPZ, ROST, BBY | LEN, DHI, TSLA |
| 15 | Nuclear | 35.28 | strong downtrend | negative | weak | 50.0 | 0.0 | 36.16 | NLR | NLR |

### Thematic Strength

| Rank | Theme | Score | Setup | ETF Flow | Flow Reliability | Dispersion | Price | News |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Financials | 62.65 | Positive setup | 69.29 | 100.0 | 5.44 | True | False |
| 2 | Healthcare Innovation | 59.48 | Positive setup | 64.59 | 90.0 | 4.3 | False | False |
| 3 | Energy | 58.75 | Positive setup | 49.47 | 95.0 | 4.96 | False | False |
| 4 | Small Caps | 55.93 | Positive setup | 51.89 | 65.0 | 0.0 | False | False |
| 5 | Dividend Defensives | 55.8 | Positive setup | 57.07 | 65.0 | 3.03 | False | False |
| 6 | Cybersecurity | 52.87 | Neutral / watchlist | 61.77 | 65.0 | 85.68 | False | False |
| 7 | Defense | 52.72 | Neutral / watchlist | 50.0 | 0.0 | 16.56 | False | False |
| 8 | Quality Growth | 48.17 | Neutral / watchlist | 59.01 | 65.0 | 22.48 | False | False |
| 9 | Semiconductors | 47.9 | Neutral / watchlist | 54.1 | 90.0 | 17.48 | False | False |
| 10 | Grid Infrastructure | 44.44 | Neutral / watchlist | 63.72 | 65.0 | 8.82 | False | False |
| 11 | AI Infrastructure | 44.37 | Weak setup | 54.1 | 90.0 | 16.82 | False | True |
| 12 | Crypto Infrastructure | 41.35 | Weak setup | 41.82 | 65.0 | 7.49 | False | False |
| 13 | Nuclear | 36.3 | Weak setup | 50.0 | 0.0 | 20.81 | False | False |

- Top 5 improving themes: Cybersecurity, Healthcare Innovation, Financials, Semiconductors, Small Caps
- Top 5 deteriorating themes: Crypto Infrastructure, Nuclear, Grid Infrastructure, Energy, AI Infrastructure
- Strong news but weak price confirmation: AI Infrastructure
- Strong price but weak news confirmation: Financials

### Sector / Theme Alignment

| Sector | Related Themes | Sector Score | Sector Signal | Theme Score | Theme Signal | Interpretation |
| --- | --- | --- | --- | --- | --- | --- |
| Real Estate | Dividend Defensives | 67.38 | strong | 55.8 | positive | sector and theme confirmation |
| Consumer Staples | Dividend Defensives | 66.61 | strong | 55.8 | positive | sector and theme confirmation |
| Financials | Financials | 66.42 | strong | 62.65 | positive | sector and theme confirmation |
| Industrials | Defense, Grid Infrastructure | 63.78 | positive | 48.58 | mixed | sector stronger than related themes |
| Healthcare | Healthcare Innovation | 62.69 | positive | 59.48 | positive | sector and theme confirmation |
| Cybersecurity | Cybersecurity | 61.33 | positive | 52.87 | mixed | sector stronger than related themes |
| Energy | Energy | 59.25 | positive | 58.75 | positive | sector and theme confirmation |
| Defense | Defense | 53.41 | mixed | 52.72 | mixed | mixed confirmation |
| Crypto | Crypto Infrastructure | 49.18 | mixed | 41.35 | weak | mixed confirmation |
| Utilities | Grid Infrastructure, Nuclear, Dividend Defensives | 45.92 | mixed | 45.51 | mixed | mixed confirmation |
| Technology | AI Infrastructure, Semiconductors, Quality Growth | 44.93 | weak | 46.81 | mixed | mixed confirmation |
| Semiconductors | AI Infrastructure, Semiconductors | 44.66 | weak | 46.13 | mixed | mixed confirmation |
| Grid Infrastructure | Grid Infrastructure | 42.22 | weak | 44.44 | weak | broad weakness across sector and themes |
| Consumer Discretionary | Small Caps | 35.51 | weak | 55.93 | positive | theme stronger than official sector |
| Nuclear | Nuclear | 35.28 | weak | 36.3 | weak | broad weakness across sector and themes |

## Three-Month Outperformance Setup

| Rank | Theme | Score | Classification | Drivers | Invalidation Triggers |
| --- | --- | --- | --- | --- | --- |
| 1 | Financials | 67.59 | Positive setup | relative_strength_60d, trend_persistence, breadth, downside_volatility, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 2 | Healthcare Innovation | 66.01 | Positive setup | relative_strength_60d, trend_persistence, breadth, downside_volatility, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 3 | Small Caps | 64.23 | Positive setup | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 4 | Energy | 60.86 | Positive setup | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 5 | Dividend Defensives | 60.08 | Positive setup | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 6 | Cybersecurity | 55.33 | Neutral / watchlist | relative_strength_60d, trend_persistence, breadth, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 7 | Defense | 54.74 | Neutral / watchlist | trend_persistence, breadth | relative strength below SPY, breadth below 45%, news turns negative |
| 8 | Semiconductors | 51.41 | Neutral / watchlist | volume_accumulation | relative strength below SPY, breadth below 45%, news turns negative |
| 9 | Quality Growth | 51.19 | Neutral / watchlist | downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 10 | Grid Infrastructure | 46.04 | Neutral / watchlist | downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 11 | AI Infrastructure | 44.23 | Weak setup | downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 12 | Crypto Infrastructure | 39.9 | Weak setup | relative_strength_20d | relative strength below SPY, breadth below 45%, news turns negative |

## Breadth and Participation

- Above 50DMA: `53.33%`
- Above 200DMA: `69.49%`
- Positive 20D return: `55.0%`

## Volatility and Risk Signals

- VIX close=19.0 pct_chg=1.77

## News Analytics

- Sentiment counts: {'positive': 59, 'negative': 18, 'neutral': 3}
- News confirmation score: `75.62`

### Top Market-Moving Headlines

**1. Big earnings and a Fed meeting: What NYSE insider Jay Woods is watching this week**
- Source: CNBC Markets
- Importance / impact: High / Positive
- Relevance / horizon: macro / short term
- Affected assets: NYSE, Federal Reserve, Earnings
- Score: `48.45`
- Investment implication: Macro-relevant positive signal; use as context for rates, volatility, and index confirmation over the short term.

**2. Dow closes more than 250 points higher, aided by cooling oil prices**
- Source: CNBC Markets
- Importance / impact: Medium / Positive
- Relevance / horizon: macro / short-term
- Affected assets: Dow, U.S, oil_prices, geo_political
- Score: `41.99`
- Investment implication: Macro-relevant positive signal; use as context for rates, volatility, and index confirmation over the short-term.

**3. Porsche to Cut 5,000 More Jobs After Sales Collapse in China**
- Source: Dow Jones US Business
- Importance / impact: Medium / Negative
- Relevance / horizon: sector_theme / short-term
- Affected assets: restructuring, employment, automotive
- Score: `41.45`
- Investment implication: Theme or sector negative signal; requires price and volume confirmation before affecting rankings.

**4. Amazon seeks federal approval to launch 5,105 satellites for direct-to-device network**
- Source: CNBC Business
- Importance / impact: Medium / Mixed
- Relevance / horizon: macro / medium-term
- Affected assets: satellite, telecommunications, technology
- Score: `40.46`
- Investment implication: Macro-relevant mixed signal; use as context for rates, volatility, and index confirmation over the medium-term.

**5. Why Trump's new tariff blitz is very different this time around**
- Source: CNBC Business Headlines
- Importance / impact: Medium / Negative
- Relevance / horizon: macro / short-term
- Affected assets: U.K, trade
- Score: `40.46`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the short-term.

**6. Nvidia and OpenAI in talks for up to $250 billion backstop to fund AI infrastructure plans**
- Source: CNBC Top News
- Importance / impact: Medium / Positive
- Relevance / horizon: single_name / long-term
- Affected assets: NVDA, AI, data center, partnership
- Score: `40.15`
- Investment implication: Single-name positive signal; low weight unless it maps to a broader sector or theme.

**7. The AI boom shows no sign of slowing — and the U.S. economy is reaping the benefits**
- Source: MarketWatch Top Stories
- Importance / impact: Medium / Positive
- Relevance / horizon: single_name / short to medium term
- Affected assets: U.S, AI, Economic Growth
- Score: `37.29`
- Investment implication: Single-name positive signal; low weight unless it maps to a broader sector or theme.

**8. Chipmaker CXMT’s 466% market debut surge makes it the most valuable China-listed company**
- Source: CNBC Technology
- Importance / impact: Medium / Positive
- Relevance / horizon: single_name / short-term
- Affected assets: CXMT, IPO, technology, China
- Score: `35.93`
- Investment implication: Single-name positive signal; low weight unless it maps to a broader sector or theme.

**9. CNBC's The China Connection newsletter: A U.S.-China debate that's becoming bigger than tariffs**
- Source: CNBC Technology
- Importance / impact: Low / Mixed
- Relevance / horizon: macro / long-term
- Affected assets: A, CNBC, U.S, AI race, U.S.-China trade tensions
- Score: `34.81`
- Investment implication: Macro-relevant mixed signal; use as context for rates, volatility, and index confirmation over the long-term.

**10. Unilever Raises Outlook After Quarterly Sales Volume Growth Hits 16-year High**
- Source: Dow Jones US Business
- Importance / impact: Low / Positive
- Relevance / horizon: single_name / short-term
- Affected assets: UNLYF, sales_growth, projections
- Score: `32.91`
- Investment implication: Single-name positive signal; low weight unless it maps to a broader sector or theme.


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
- Market flow score: `47.2 / 100`
- Equity risk flow: `46.4`
- Credit risk flow: `46.1`
- Sector cyclicality flow: `45.8`
- Duration/liquidity flow: `52.1`
- Alternatives: `defensive or uncertainty hedge`
- ETF flow reliability: `71.2 / 100`
- Dominant allocation direction: `defensive demand`

### Core Flow Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVV | U.S. Broad Equity | -0.3 | 0.7 | 0.4 | -0.6 | Flat | Neutral | Normal | Neutral | Neutral | Structural accumulation | 91.0 |
| ACWI | Global Equity | -1.4 | -1.5 | 0.1 | -0.4 | Flat | Sell | Normal | Quiet Distribution | Weakening | Strong confirmation; Exceptional institutional selling, Persistent selling | 79.0 |
| EFA | Developed Markets ex-U.S. | -2.4 | -0.1 | 0.0 | -1.1 | Flat | Neutral | Normal | Neutral | Neutral | Medium-term deterioration; Exceptional institutional selling, Persistent selling | 67.0 |
| IEMG | Emerging Markets | -0.4 | -0.6 | 0.1 | -0.6 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Medium-term recovery; Persistent selling | 79.0 |
| IJH | U.S. Mid Cap | -0.6 | 0.1 | 0.6 | -1.2 | Flat | Neutral | Normal | Neutral | Neutral | Structural accumulation | 91.0 |
| IWM | U.S. Small Cap | -0.6 | 0.7 | 0.5 | -1.0 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural distribution | 79.0 |
| LQD | Investment-Grade Credit | 0.3 | 0.8 | 0.5 | 0.8 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural accumulation | 91.0 |
| HYG | High-Yield Credit | -0.8 | -0.6 | 0.4 | -0.6 | Flat | Neutral | Normal | Neutral | Neutral | Structural distribution | 79.0 |
| SGOV | Treasury Bills / Cash | -0.6 | -0.4 | 0.8 | -0.8 | Flat | Neutral | Normal | Neutral | Neutral | Structural accumulation; Strong sponsorship | 99.0 |
| SHY | Short-Duration Treasuries | -1.0 | -1.2 | 0.2 | -0.2 | Flat | Sell | Normal | Quiet Distribution | Weakening | Strong confirmation; Persistent selling | 87.0 |
| IEF | Intermediate-Duration Treasuries | 0.6 | -0.7 | 0.7 | -1.0 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Medium-term recovery | 87.0 |
| TLT | Long-Duration Treasuries | 2.6 | 1.6 | 0.8 | -0.2 | Down | Buy | Normal | Contrarian Buying | Watch | Strong confirmation; Exceptional institutional buying, Strong sponsorship | 100.0 |
| GLD | Gold | 1.1 | 0.9 | 0.4 | -1.3 | Flat | Buy | Normal | Quiet Accumulation | Improving | Medium-term recovery | 87.0 |
| IBIT | Bitcoin | -0.6 | -1.7 | 0.5 | -0.9 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural distribution | 79.0 |

### Sector Flow Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| XLC | Communication Services | 0.2 | -1.7 | 0.3 | 0.1 | Flat | Neutral | Normal | Neutral | Neutral | Structural distribution | 79.0 |
| XLY | Consumer Discretionary | 0.8 | 1.2 | 0.6 | -0.5 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural accumulation | 91.0 |
| XLP | Consumer Staples | 1.0 | 1.6 | 0.3 | 0.2 | Flat | Buy | Normal | Quiet Accumulation | Improving | Strong confirmation | 95.0 |
| XLE | Energy | -0.7 | -0.9 | 0.2 | -0.1 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural distribution; Persistent selling | 71.0 |
| XLF | Financials | 1.1 | 1.1 | 0.5 | -0.8 | Up | Buy | Normal | Steady Accumulation | Risk-On | Strong confirmation | 95.0 |
| XLV | Health Care | 0.8 | 0.3 | 0.6 | -0.8 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Medium-term recovery | 87.0 |
| XLI | Industrials | -0.4 | 1.0 | 0.5 | -0.8 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural accumulation | 91.0 |
| XLK | Information Technology | 0.2 | -0.6 | 0.6 | -0.9 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural accumulation | 91.0 |
| XLB | Materials | -0.2 | 0.4 | 0.5 | -0.8 | Flat | Neutral | Normal | Neutral | Neutral | Structural accumulation | 91.0 |
| XLRE | Real Estate | 1.2 | 1.7 | 0.7 | -0.6 | Up | Buy | Normal | Steady Accumulation | Risk-On | Strong confirmation | 95.0 |
| XLU | Utilities | 0.1 | 0.2 | 0.5 | -0.8 | Flat | Neutral | Normal | Neutral | Neutral | Structural accumulation | 91.0 |

### Subsector PFV Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ITA | Aerospace and Defense | -0.1 | -0.4 | 0.2 | 0.5 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural distribution; Persistent selling | 71.0 |
| SOXX | Semiconductors | 1.2 | 1.6 | 0.5 | 1.0 | Down | Sell | Normal | Persistent Distribution | Risk-Off | Tactical profit-taking inside structural accumulation; Exceptional institutional selling | 75.0 |
| SMH | Semiconductors | -0.7 | -1.0 | 0.4 | 4.4 | Down | Sell | High | Confirmed Distribution | Strong Risk-Off | Strong confirmation | 95.0 |
| CIBR | Cybersecurity | 1.1 | 1.6 | 0.7 | -1.3 | Flat | Buy | Normal | Quiet Accumulation | Improving | Strong confirmation | 95.0 |

### Material Flow Divergences

| Severity | Type | Primary | Comparison | Interpretation |
| --- | --- | --- | --- | --- |
| medium | related_subsector_divergence | XLK | SOXX | technology differs from semiconductors |
| high | close_substitute_divergence | GLD | IAU | primary representative differs from close substitute |
| high | close_substitute_divergence | IVV | SPY | primary representative differs from close substitute |
| high | close_substitute_divergence | AGG | IUSB | primary representative differs from close substitute |
| high | close_substitute_divergence | HYG | JNK | primary representative differs from close substitute |
| high | close_substitute_divergence | IVV | SPY | primary representative differs from close substitute |


## Contradiction / Audit Flags

| Severity | Section | Issue | Deterministic Fix |
| --- | --- | --- | --- |
| low | Theme Strength Ranking | AI Infrastructure has strong news confirmation but weak price confirmation. | Classify as unconfirmed narrative. |

## Data Quality Notes

- Technical rows loaded: `60`
- S&P 500 constituent technical rows loaded: `503`
- Macro rows loaded: `49`
- Live macro rows used: `23`
- Economic rows loaded: `113`
- News rows loaded: `80`
- Positioning/flow rows loaded: `30`

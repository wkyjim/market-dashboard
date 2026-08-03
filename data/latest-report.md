# Rule-Based Institutional Market Update

Generated at: 3 August 2026, 12:12:41 (HKT)
Window: 24h

## Executive Dashboard

- Regime score: **58.51 / 100** (Mild Risk-On)
- US equity strength: **59.0 / 100** (neutral)
- Evidence quality: **83.0 / 100**
- ETF flow contribution: **49.17 / 100**, reliability **66.71 / 100**
- Breadth: **narrow**; above 50DMA `50.0%`, above 200DMA `72.88%`
- Top sector score: **Healthcare** `65.74`
- Top theme score: **Energy** `60.9`

## Market Regime Score

| Metric | Value | Driver / Interpretation |
| --- | --- | --- |
| Overall regime | 58.51 | Mild Risk-On |
| equity_trend | 66.25 | risk-on support; Core equity ETFs versus moving averages. |
| equity_momentum | 49.4 | neutral / mixed; 5D/20D/60D return momentum across SPY, QQQ, IWM, and SMH. |
| market_breadth | 54.29 | neutral / mixed; Participation breadth from tracked equity/ETF rows. |
| volatility | 80.0 | risk-on support; VIX level and change; higher score means calmer volatility conditions. |
| rates_yield_curve | 58.0 | mild risk-on support; Treasury yield pressure and curve shape; higher score means less rates pressure. |
| credit_proxy | 50.0 | neutral / mixed; Credit-market proxy; currently neutral when no direct spread signal is available. |
| dollar_fx | 55.87 | mild risk-on support; Dollar move; higher score means less USD tightening pressure. |
| commodity_confirmation | 57.0 | mild risk-on support; Copper, silver, oil, and gold mix; higher score means better cyclical confirmation. |
| etf_flow | 49.45 | neutral / mixed; Grouped ETF flow contribution adjusted for reliability. |
| news_confirmation | 61.25 | mild risk-on support; Weighted headline/news confirmation score. |
| Positive contributors |  | volatility=80.0, equity_trend=66.25, news_confirmation=61.25 |
| Negative contributors |  | none |

## US Equity Strength Score

| Component | Score |
| --- | --- |
| indices_above_moving_averages | 66.25 |
| sp500_trend | 100.0 |
| nasdaq_trend | 55.0 |
| russell_participation | 55.0 |
| returns_momentum | 49.4 |
| rsi_zone | 40.0 |
| macd_confirmation | 35.0 |
| volume_confirmation | 65.0 |
| breadth | 54.29 |

## Evidence Quality / Confidence

- Confidence score: `83.0`
- Agreement ratio: `0.6`
- Contradiction count: `0`
- Missing indicators: none
- Warning flags: none

## Cross-Asset Confirmation

| Area | Signal | Interpretation |
| --- | --- | --- |
| Equities | S&P 500 rising; Nasdaq rising; Russell 2000 falling | Confirms risk appetite when broad indices rise together; weak small caps would narrow the signal. |
| Rates | 10Y Treasury rising; MOVE rising | Rising yields can pressure duration assets; falling MOVE supports calmer bond volatility. |
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
| ^GSPC | S&P 500 | 7489.72 | 0.7 | 2026-07-31 | closed |
| ^IXIC | NASDAQ Composite | 25373.85 | 1.0 | 2026-07-31 | closed |
| ^RUT | Russell 2000 Index | 2931.34 | -0.5 | 2026-07-31 | closed |
| ^VIX | CBOE Volatility Index | 15.99 | -6.44 | 2026-07-31 | closed |
| ^SKEW | CBOE SKEW Index | 141.23 | 0.95 | 2026-07-31 | closed |
| ^MOVE | ICE BofA MOVE Index | 76.82 | 8.38 | 2026-07-24 | closed |
| US2YT=X | United States 2-Year Treasury Yield | 4.25 | -0.96 | 2026-08-03 | live as of 3 August 2026, 12:00:37 (HKT) |
| US3YT=X | United States 3-Year Treasury Yield | 4.31 | -1.13 | 2026-08-03 | live as of 3 August 2026, 12:00:37 (HKT) |
| US5YT=X | United States 5-Year Treasury Yield | 4.41 | -1.2 | 2026-08-03 | live as of 3 August 2026, 12:00:37 (HKT) |
| US7YT=X | United States 7-Year Treasury Yield | 4.55 | -1.13 | 2026-08-03 | live as of 3 August 2026, 12:00:37 (HKT) |
| US10YT=X | United States 10-Year Treasury Yield | 4.7 | -1.01 | 2026-08-03 | live as of 3 August 2026, 12:00:37 (HKT) |
| US20YT=X | United States 20-Year Treasury Yield | 5.26 | -0.75 | 2026-08-03 | live as of 3 August 2026, 12:00:37 (HKT) |
| US30YT=X | United States 30-Year Treasury Yield | 5.24 | -0.64 | 2026-08-03 | live as of 3 August 2026, 12:00:37 (HKT) |
| HK50 | Hang Seng Futures | 25911.5 | -0.06 | 2026-08-03 | live as of 3 August 2026, 12:00:37 (HKT) |
| KOR200c1 | KOSPI 200 Futures | 978.4 | -5.07 | 2026-07-31 | closed |
| CIHc1 | SSE 50 Futures | 2914.2 | 0.38 | 2026-07-31 | closed |
| HYG | iShares iBoxx High Yield Corporate Bond ETF | 79.48 | 0.01 | 2026-07-31 | closed |
| LQD | iShares iBoxx Investment Grade Corporate Bond ETF | 106.25 | -0.15 | 2026-07-31 | closed |
| JNK | SPDR Bloomberg High Yield Bond ETF | 95.68 | 0.02 | 2026-07-31 | closed |
| RSP | Invesco S&P 500 Equal Weight ETF | 215.01 | -0.17 | 2026-07-31 | closed |
| IWF | iShares Russell 1000 Growth ETF | 118.32 | 0.76 | 2026-07-31 | closed |
| IWD | iShares Russell 1000 Value ETF | 251.82 | 0.44 | 2026-07-31 | closed |
| TLT | iShares 20+ Year Treasury Bond ETF | 82.25 | -0.66 | 2026-07-31 | closed |
| IEF | iShares 7-10 Year Treasury Bond ETF | 92.95 | -0.28 | 2026-07-31 | closed |
| SHY | iShares 1-3 Year Treasury Bond ETF | 82.0 | -0.01 | 2026-07-31 | closed |
| GC=F | Gold Future | 4121.7 | 1.79 | 2026-08-02 | closed |
| SI=F | Silver Future | 58.64 | 1.82 | 2026-08-02 | closed |
| CL=F | WTI Crude Oil Future | 81.09 | -4.23 | 2026-08-02 | closed |
| HG=F | Copper Future | 6.54 | 1.68 | 2026-08-02 | closed |

## Market Dispersion Analysis

- Sector ETF 20D dispersion: `14.98` points (high); leader `XLE` (Energy) `11.89`, laggard `XLU` (Utilities) `-3.08`
- Sector ETF 60D dispersion: `18.26` points (high); leader `XLV` (Health Care) `11.87`, laggard `XLC` (Communication Services) `-6.39`

| Comparison | Left | Right | 20D Spread | Signal |
| --- | --- | --- | --- | --- |
| Equal-weight vs cap-weight | RSP (Equal-weight S&P 500) | SPY (S&P 500) | -0.26 | balanced |
| Small-cap vs large-cap | IWM (Russell 2000) | SPY (S&P 500) | -2.45 | large-cap leadership |
| Growth vs value | IWF (Russell 1000 Growth) | IWD (Russell 1000 Value) | -4.37 | value leadership |
| Nasdaq vs S&P 500 | QQQ (Nasdaq 100) | SPY (S&P 500) | -3.76 | S&P 500 leadership |

## Sector Constituent Dispersion

- Breadth 50D / 200D: percentage of active S&P 500 constituents in the sector trading above the 50-day / 200-day moving average.
- Positive 20D: percentage of active sector constituents with positive 20-day return.
- Std 20D: cross-sectional standard deviation of constituent 20-day returns; higher means wider stock-level dispersion.

| Sector | Count | Breadth 50D | Breadth 200D | Positive 20D | 20D Dispersion | Std 20D | Label | Leaders | Laggards |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Information Technology | 74 | 40.54 | 61.64 | 50.0 | 62.2 | 13.16 | very high | CTSH, HPQ, ACN | INTC, GLW, SNDK |
| Financials | 76 | 87.67 | 80.0 | 65.79 | 49.03 | 7.28 | very high | PYPL, CBOE, WTW | PGR, COIN, HOOD |
| Health Care | 59 | 84.75 | 66.1 | 57.63 | 48.39 | 8.13 | very high | DXCM, REGN, BAX | ELV, ISRG, MRNA |
| Consumer Discretionary | 47 | 59.57 | 53.19 | 46.81 | 43.3 | 8.62 | very high | GRMN, ROST, HAS | CVNA, DHI, TSLA |
| Industrials | 81 | 59.49 | 67.53 | 44.44 | 39.87 | 8.6 | very high | CTAS, HII, ALLE | GNRC, CHRW, LII |
| Communication Services | 23 | 40.91 | 40.91 | 47.83 | 36.36 | 7.69 | very high | T, VZ, CHTR | NFLX, ECHO, PSKY |
| Materials | 26 | 57.69 | 73.08 | 46.15 | 29.77 | 9.04 | very high | NUE, LYB, STLD | MLM, LIN, ALB |
| Energy | 21 | 85.71 | 85.71 | 85.71 | 22.17 | 7.49 | very high | PSX, MPC, FANG | TPL, HAL, WMB |
| Utilities | 31 | 16.13 | 58.06 | 9.68 | 19.11 | 3.68 | high | CEG, PCG, AES | DTE, WEC, LNT |
| Consumer Staples | 34 | 66.67 | 59.38 | 47.06 | 17.51 | 4.23 | high | TGT, CASY, DG | STZ, MO, KDP |
| Real Estate | 31 | 58.06 | 80.65 | 45.16 | 15.91 | 3.93 | high | DLR, HST, WY | CPT, MAA, UDR |

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
| US dollar/Euro ECB reference exchange rate | 1.15 | USD | 0.0 USD vs prior | 2026-07-31 | EUR strengthened versus this currency. |
| Japanese yen/Euro ECB reference exchange rate | 184.03 | JPY | -2.96 JPY vs prior | 2026-07-31 | EUR weakened versus this currency. |
| Chinese yuan renminbi/Euro ECB reference exchange rate | 7.75 | CNY | 0.0 CNY vs prior | 2026-07-31 | EUR strengthened versus this currency. |
| Australian dollar/Euro ECB reference exchange rate | 1.64 | AUD | -0.01 AUD vs prior | 2026-07-31 | EUR weakened versus this currency. |

ABS Australia note: ABS rows are stored locally/Neon, but most series are dimension-coded; only curated series should be promoted into narrative report text.

## Sector and Theme Leadership

### Official Sector Strength

Supporting and detracting names are the top/bottom S&P 500 constituents by 20D return when constituent coverage is available; otherwise the report falls back to related ETFs.

| Rank | Sector | Score | Trend | Momentum | Stock Breadth | ETF Flow | Flow Reliability | 3M RS | Supporting / Leaders | Detracting / Laggards |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Healthcare | 65.74 | strong uptrend | neutral | broad | 74.38 | 65.0 | 52.85 | DXCM, REGN, BAX | ELV, ISRG, MRNA |
| 2 | Consumer Staples | 64.99 | strong uptrend | neutral | broad | 50.0 | 0.0 | 49.05 | TGT, CASY, DG | STZ, MO, KDP |
| 3 | Financials | 64.47 | strong uptrend | neutral | broad | 56.2 | 65.0 | 54.11 | PYPL, CBOE, WTW | PGR, COIN, HOOD |
| 4 | Cybersecurity | 63.79 | strong uptrend | positive | broad | 57.34 | 65.0 | 61.13 | CIBR | CIBR |
| 5 | Real Estate | 63.75 | strong uptrend | neutral | broad | 43.64 | 65.0 | 49.87 | DLR, HST, WY | CPT, MAA, UDR |
| 6 | Energy | 61.42 | uptrend | positive | broad | 60.24 | 65.0 | 55.74 | PSX, MPC, FANG | TPL, HAL, WMB |
| 7 | Consumer Discretionary | 59.35 | uptrend | neutral | broad | 50.0 | 0.0 | 47.33 | GRMN, ROST, HAS | CVNA, DHI, TSLA |
| 8 | Industrials | 55.65 | strong uptrend | neutral | broad | 50.0 | 0.0 | 48.93 | CTAS, HII, ALLE | GNRC, CHRW, LII |
| 9 | Crypto | 51.08 | neutral | neutral | mixed | 60.83 | 65.0 | 50.0 |  |  |
| 10 | Semiconductors | 46.57 | neutral | neutral | weak | 73.64 | 90.0 | 44.26 | SMH, SOXX | SOXX, SMH |
| 11 | Technology | 45.45 | neutral | neutral | weak | 38.08 | 65.0 | 47.99 | CTSH, HPQ, ACN | INTC, GLW, SNDK |
| 12 | Defense | 44.13 | downtrend | neutral | weak | 50.0 | 0.0 | 45.31 | XAR | XAR |
| 13 | Grid Infrastructure | 42.96 | downtrend | neutral | weak | 68.52 | 65.0 | 44.04 | GRID | GRID |
| 14 | Nuclear | 34.67 | strong downtrend | negative | weak | 50.0 | 0.0 | 34.53 | NLR | NLR |
| 15 | Utilities | 34.0 | strong downtrend | neutral | weak | 50.0 | 0.0 | 43.87 | CEG, PCG, AES | DTE, WEC, LNT |

### Thematic Strength

| Rank | Theme | Score | Setup | ETF Flow | Flow Reliability | Dispersion | Price | News |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Energy | 60.9 | Positive setup | 60.24 | 65.0 | 4.44 | True | False |
| 2 | Healthcare Innovation | 59.86 | Positive setup | 74.38 | 65.0 | 5.85 | False | False |
| 3 | Financials | 56.93 | Positive setup | 56.2 | 65.0 | 5.74 | False | False |
| 4 | Cybersecurity | 56.13 | Positive setup | 57.34 | 65.0 | 8.31 | False | False |
| 5 | AI Infrastructure | 52.95 | Neutral / watchlist | 73.64 | 90.0 | 29.86 | False | False |
| 6 | Quality Growth | 52.53 | Neutral / watchlist | 65.28 | 65.0 | 22.46 | False | False |
| 7 | Dividend Defensives | 51.65 | Neutral / watchlist | 61.06 | 65.0 | 3.15 | False | False |
| 8 | Defense | 50.36 | Neutral / watchlist | 50.0 | 0.0 | 29.77 | False | False |
| 9 | Semiconductors | 48.41 | Neutral / watchlist | 73.64 | 90.0 | 18.85 | False | False |
| 10 | Grid Infrastructure | 46.52 | Neutral / watchlist | 68.52 | 65.0 | 8.47 | False | False |
| 11 | Small Caps | 46.4 | Neutral / watchlist | 49.38 | 65.0 | 0.0 | False | False |
| 12 | Nuclear | 36.38 | Weak setup | 50.0 | 0.0 | 19.99 | False | False |
| 13 | Crypto Infrastructure | 32.48 | Underperformance risk | 60.83 | 65.0 | 4.18 | False | False |

- Top 5 improving themes: Cybersecurity, Healthcare Innovation, Financials, Semiconductors, Defense
- Top 5 deteriorating themes: Crypto Infrastructure, Nuclear, Grid Infrastructure, Energy, AI Infrastructure
- Strong news but weak price confirmation: none
- Strong price but weak news confirmation: Energy

### Sector / Theme Alignment

| Sector | Related Themes | Sector Score | Sector Signal | Theme Score | Theme Signal | Interpretation |
| --- | --- | --- | --- | --- | --- | --- |
| Healthcare | Healthcare Innovation | 65.74 | strong | 59.86 | positive | sector and theme confirmation |
| Consumer Staples | Dividend Defensives | 64.99 | positive | 51.65 | mixed | sector stronger than related themes |
| Financials | Financials | 64.47 | positive | 56.93 | positive | sector and theme confirmation |
| Cybersecurity | Cybersecurity | 63.79 | positive | 56.13 | positive | sector and theme confirmation |
| Real Estate | Dividend Defensives | 63.75 | positive | 51.65 | mixed | sector stronger than related themes |
| Energy | Energy | 61.42 | positive | 60.9 | positive | sector and theme confirmation |
| Consumer Discretionary | Small Caps | 59.35 | positive | 46.4 | mixed | sector stronger than related themes |
| Industrials | Defense, Grid Infrastructure | 55.65 | positive | 48.44 | mixed | sector stronger than related themes |
| Crypto | Crypto Infrastructure | 51.08 | mixed | 32.48 | very weak | mixed confirmation |
| Semiconductors | AI Infrastructure, Semiconductors | 46.57 | mixed | 50.68 | mixed | mixed confirmation |
| Technology | AI Infrastructure, Semiconductors, Quality Growth | 45.45 | mixed | 51.3 | mixed | mixed confirmation |
| Defense | Defense | 44.13 | weak | 50.36 | mixed | mixed confirmation |
| Grid Infrastructure | Grid Infrastructure | 42.96 | weak | 46.52 | mixed | mixed confirmation |
| Nuclear | Nuclear | 34.67 | very weak | 36.38 | weak | broad weakness across sector and themes |
| Utilities | Grid Infrastructure, Nuclear, Dividend Defensives | 34.0 | very weak | 44.85 | weak | broad weakness across sector and themes |

## Three-Month Outperformance Setup

| Rank | Theme | Score | Classification | Drivers | Invalidation Triggers |
| --- | --- | --- | --- | --- | --- |
| 1 | Healthcare Innovation | 65.39 | Positive setup | relative_strength_60d, trend_persistence, breadth, downside_volatility, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 2 | Financials | 62.74 | Positive setup | trend_persistence, breadth, downside_volatility, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 3 | Energy | 62.71 | Positive setup | relative_strength_20d, trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 4 | Cybersecurity | 60.59 | Positive setup | relative_strength_60d, trend_persistence, breadth, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 5 | Quality Growth | 55.66 | Neutral / watchlist | trend_persistence, breadth, volume_accumulation, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 6 | Dividend Defensives | 55.38 | Neutral / watchlist | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 7 | AI Infrastructure | 55.09 | Neutral / watchlist | trend_persistence, breadth, volume_accumulation | relative strength below SPY, breadth below 45%, news turns negative |
| 8 | Defense | 52.28 | Neutral / watchlist | trend_persistence, breadth | relative strength below SPY, breadth below 45%, news turns negative |
| 9 | Small Caps | 52.09 | Neutral / watchlist | volume_accumulation, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 10 | Semiconductors | 49.78 | Neutral / watchlist |  | relative strength below SPY, breadth below 45%, news turns negative |
| 11 | Grid Infrastructure | 48.05 | Neutral / watchlist | volume_accumulation, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 12 | Nuclear | 33.44 | Weak setup |  | relative strength below SPY, breadth below 45%, news turns negative |

## Breadth and Participation

- Above 50DMA: `50.0%`
- Above 200DMA: `72.88%`
- Positive 20D return: `40.0%`

## Volatility and Risk Signals

- VIX close=15.99 pct_chg=-6.44

## News Analytics

- Sentiment counts: {'positive': 42, 'negative': 24, 'neutral': 14}
- News confirmation score: `61.25`

### Top Market-Moving Headlines

**1. Oil drops over 4% as Middle East tensions ebb on diplomatic efforts**
- Source: CNBC Top News
- Importance / impact: High / Negative
- Relevance / horizon: macro / short-term
- Affected assets: U.S, oil_prices, geopolitical_risk
- Score: `72.67`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the short-term.

**2. CNBC Daily Open: Markets exhale as Trump steps back, OPEC+ steps up**
- Source: CNBC Technology
- Importance / impact: High / Mixed
- Relevance / horizon: macro / short-term
- Affected assets: OPEC, CNBC, politics, oil_market, geopolitical_risk
- Score: `54.0`
- Investment implication: Macro-relevant mixed signal; use as context for rates, volatility, and index confirmation over the short-term.

**3. Financial stocks are crushing it. These charts show why the ‘breakout’ rally may have just begun.**
- Source: MarketWatch Top Stories
- Importance / impact: Medium / Positive
- Relevance / horizon: sector_theme / short-term
- Affected assets: bank_stocks, earnings, valuations
- Score: `48.77`
- Investment implication: Theme or sector positive signal; requires price and volume confirmation before affecting rankings.

**4. Investors scored on Iran war's oil market boom. Staying long the trade will get trickier**
- Source: CNBC Top News
- Importance / impact: High / Positive
- Relevance / horizon: macro / short-term
- Affected assets: U.S, oil market, U.S.-Iran conflict
- Score: `48.45`
- Investment implication: Macro-relevant positive signal; use as context for rates, volatility, and index confirmation over the short-term.

**5. Investors are rotating into financial stocks. The Fed’s next move could determine how far the rally runs.**
- Source: MarketWatch Top Stories
- Importance / impact: Medium / Positive
- Relevance / horizon: macro / short-term
- Affected assets: financial stocks, Fed policy
- Score: `44.2`
- Investment implication: Macro-relevant positive signal; use as context for rates, volatility, and index confirmation over the short-term.

**6. Bomb carried by woman kills three, injures 21 near Moscow restaurant, authorities say**
- Source: CNBC Top News
- Importance / impact: Medium / Negative
- Relevance / horizon: sector_theme / short-term
- Affected assets: security
- Score: `40.84`
- Investment implication: Theme or sector negative signal; requires price and volume confirmation before affecting rankings.

**7. WestJet flight attendants go on strike after talks fall through, grounding flights**
- Source: CNBC Top News
- Importance / impact: Medium / Negative
- Relevance / horizon: single_name / short-term
- Affected assets: WEST, Labor Issues, Transportation
- Score: `37.05`
- Investment implication: Single-name negative signal; low weight unless it maps to a broader sector or theme.

**8. U.S., Japan confirm coordinated yen intervention, signal readiness for more**
- Source: CNBC Top News
- Importance / impact: Low / Mixed
- Relevance / horizon: macro / short-term
- Affected assets: USDJPY, U.S, currency intervention
- Score: `33.25`
- Investment implication: Macro-relevant mixed signal; use as context for rates, volatility, and index confirmation over the short-term.

**9. S&P 500 profit growth is getting even wilder as Amazon makes its mark**
- Source: MarketWatch Top Stories
- Importance / impact: Low / Positive
- Relevance / horizon: single_name / short-term
- Affected assets: AMZN, P, S, AI, Tech
- Score: `33.15`
- Investment implication: Single-name positive signal; low weight unless it maps to a broader sector or theme.

**10. OPEC, Allies Increase Oil Output for Sixth Time in a Row**
- Source: Dow Jones US Business
- Importance / impact: Low / Positive
- Relevance / horizon: macro / short-term
- Affected assets: OPEC, oil production
- Score: `33.15`
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
- Market flow score: `50.9 / 100`
- Equity risk flow: `46.1`
- Credit risk flow: `53.2`
- Sector cyclicality flow: `56.1`
- Duration/liquidity flow: `49.4`
- Alternatives: `defensive or uncertainty hedge`
- ETF flow reliability: `66.7 / 100`
- Dominant allocation direction: `defensive demand`

### Core Flow Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVV | U.S. Broad Equity | -1.0 | 0.4 | 0.3 | -0.5 | Flat | Neutral | Normal | Neutral | Neutral | Medium-term deterioration | 83.0 |
| ACWI | Global Equity | -1.9 | -1.4 | 0.0 | -0.1 | Flat | Sell | Normal | Quiet Distribution | Weakening | Strong confirmation; Persistent selling | 87.0 |
| EFA | Developed Markets ex-U.S. | -1.5 | -0.1 | 0.0 | 0.3 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Medium-term deterioration; Persistent selling | 75.0 |
| IEMG | Emerging Markets | 0.0 | -0.3 | 0.1 | 0.4 | Down | Buy | Normal | Contrarian Buying | Watch | Strong confirmation; Exceptional institutional buying, Persistent selling | 95.0 |
| IJH | U.S. Mid Cap | 0.4 | 0.6 | 0.7 | -0.4 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural accumulation | 91.0 |
| IWM | U.S. Small Cap | -0.1 | -0.2 | 0.5 | 0.4 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural distribution | 79.0 |
| LQD | Investment-Grade Credit | -0.6 | 0.6 | 0.4 | 1.7 | Down | Neutral | High | Heavy Selling Pressure | Cautious | Medium-term deterioration | 83.0 |
| HYG | High-Yield Credit | -0.3 | 1.0 | 0.4 | 0.5 | Flat | Buy | Normal | Quiet Accumulation | Improving | Medium-term deterioration; Exceptional institutional buying | 91.0 |
| SGOV | Treasury Bills / Cash | -0.2 | -0.8 | 0.9 | 1.4 | Flat | Sell | High | Distribution Before Breakdown | Early Bearish | Tactical profit-taking inside structural accumulation; Strong sponsorship | 91.0 |
| SHY | Short-Duration Treasuries | -1.2 | -1.0 | 0.2 | -0.1 | Flat | Sell | Normal | Quiet Distribution | Weakening | Strong confirmation; Persistent selling | 87.0 |
| IEF | Intermediate-Duration Treasuries | 0.4 | -0.5 | 0.7 | 0.7 | Down | Neutral | High | Heavy Selling Pressure | Cautious | Structural accumulation | 91.0 |
| TLT | Long-Duration Treasuries | 1.4 | 1.0 | 0.8 | 3.0 | Down | Buy | High | Aggressive Dip Buying | Recovery Candidate | Strong confirmation; Strong sponsorship | 100.0 |
| GLD | Gold | 1.2 | 1.1 | 0.4 | -0.1 | Down | Buy | Normal | Contrarian Buying | Watch | Strong confirmation | 95.0 |
| IBIT | Bitcoin | 0.4 | -1.4 | 0.6 | 0.7 | Flat | Neutral | Normal | Neutral | Neutral | Medium-term recovery | 87.0 |

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
| ITA | Aerospace and Defense | -0.1 | -0.7 | 0.2 | -1.6 | Flat | Neutral | Low | Dormant Market | Neutral | Structural distribution; Persistent selling | 71.0 |
| SOXX | Semiconductors | 2.7 | 2.0 | 0.6 | 0.7 | Down | Buy | Normal | Contrarian Buying | Watch | Strong confirmation; Exceptional institutional buying | 100.0 |
| SMH | Semiconductors | 1.6 | 1.1 | 0.6 | 0.4 | Down | Buy | Normal | Contrarian Buying | Watch | Strong confirmation | 95.0 |
| CIBR | Cybersecurity | 0.6 | 1.2 | 0.6 | -0.5 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural accumulation | 91.0 |

### Material Flow Divergences

| Severity | Type | Primary | Comparison | Interpretation |
| --- | --- | --- | --- | --- |
| high | close_substitute_divergence | GLD | IAU | primary representative differs from close substitute |
| high | close_substitute_divergence | AGG | IUSB | primary representative differs from close substitute |
| high | close_substitute_divergence | IWF | IVW | primary representative differs from close substitute |
| high | close_substitute_divergence | IWD | IVE | primary representative differs from close substitute |
| high | close_substitute_divergence | SOXX | SMH | primary representative differs from close substitute |


## Contradiction / Audit Flags

No contradiction flags were triggered by current deterministic rules.

## Data Quality Notes

- Technical rows loaded: `60`
- S&P 500 constituent technical rows loaded: `503`
- Macro rows loaded: `49`
- Live macro rows used: `15`
- Economic rows loaded: `113`
- News rows loaded: `80`
- Positioning/flow rows loaded: `30`

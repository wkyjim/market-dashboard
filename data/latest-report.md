# Rule-Based Institutional Market Update

Generated at: 8 August 2026, 01:04:43 (HKT)
Window: 24h

## Executive Dashboard

- Regime score: **65.42 / 100** (Moderate Risk-On)
- US equity strength: **76.85 / 100** (strong)
- Evidence quality: **83.0 / 100**
- ETF flow contribution: **51.54 / 100**, reliability **71.51 / 100**
- Breadth: **healthy**; above 50DMA `68.33%`, above 200DMA `72.88%`
- Top sector score: **Cybersecurity** `69.81`
- Top theme score: **Financials** `59.35`

## Market Regime Score

| Metric | Value | Driver / Interpretation |
| --- | --- | --- |
| Overall regime | 65.42 | Moderate Risk-On |
| equity_trend | 87.5 | risk-on support; Core equity ETFs versus moving averages. |
| equity_momentum | 51.24 | neutral / mixed; 5D/20D/60D return momentum across SPY, QQQ, IWM, and SMH. |
| market_breadth | 69.29 | risk-on support; Participation breadth from tracked equity/ETF rows. |
| volatility | 80.0 | risk-on support; VIX level and change; higher score means calmer volatility conditions. |
| rates_yield_curve | 58.0 | mild risk-on support; Treasury yield pressure and curve shape; higher score means less rates pressure. |
| credit_proxy | 50.0 | neutral / mixed; Credit-market proxy; currently neutral when no direct spread signal is available. |
| dollar_fx | 57.37 | mild risk-on support; Dollar move; higher score means less USD tightening pressure. |
| commodity_confirmation | 50.0 | neutral / mixed; Copper, silver, oil, and gold mix; higher score means better cyclical confirmation. |
| etf_flow | 51.1 | neutral / mixed; Grouped ETF flow contribution adjusted for reliability. |
| news_confirmation | 85.62 | risk-on support; Weighted headline/news confirmation score. |
| Positive contributors |  | equity_trend=87.5, news_confirmation=85.62, volatility=80.0, market_breadth=69.29 |
| Negative contributors |  | none |

## US Equity Strength Score

| Component | Score |
| --- | --- |
| indices_above_moving_averages | 87.5 |
| sp500_trend | 100.0 |
| nasdaq_trend | 75.0 |
| russell_participation | 100.0 |
| returns_momentum | 51.24 |
| rsi_zone | 72.5 |
| macd_confirmation | 70.0 |
| volume_confirmation | 50.0 |
| breadth | 69.29 |

## Evidence Quality / Confidence

- Confidence score: `83.0`
- Agreement ratio: `0.6`
- Contradiction count: `0`
- Missing indicators: none
- Warning flags: none

## Cross-Asset Confirmation

| Area | Signal | Interpretation |
| --- | --- | --- |
| Equities | S&P 500 rising; Nasdaq rising; Russell 2000 rising | Confirms risk appetite when broad indices rise together; weak small caps would narrow the signal. |
| Rates | 10Y Treasury falling; MOVE rising | Rising yields can pressure duration assets; falling MOVE supports calmer bond volatility. |
| Dollar | DXY proxy falling | A stronger dollar can tighten financial conditions and pressure commodities/emerging-market risk. |
| Credit | HYG stable | High-yield weakness would challenge equity risk-on confirmation. |
| Gold | Gold rising | Gold strength can indicate defensive demand, inflation hedging, or geopolitical concern. |
| Silver | Silver rising | Silver helps distinguish precious-metal demand from industrial/cyclical confirmation when data is available. |
| Copper | Copper falling | Copper strength supports cyclical growth confirmation; weakness would dilute risk-on breadth. |
| Oil | WTI crude rising | Oil spikes can be inflationary risk; falling oil can ease cost pressure but may also flag demand softness. |
| Volatility | VIX falling | Falling VIX supports risk appetite; a volatility spike would reduce confidence in broad risk-on. |

### Macro Snapshot

Live macro rows are intraday snapshots from `public.macro_live`; closed rows are official stored rows from `public.macro`.

| Symbol | Name | Close | Pct Chg | Market Date | Status |
| --- | --- | --- | --- | --- | --- |
| ^GSPC | S&P 500 | 7742.29 | 0.42 | 2026-08-07 | live as of 8 August 2026, 01:00:40 (HKT) |
| ^IXIC | NASDAQ Composite | 26593.1 | 0.93 | 2026-08-07 | live as of 8 August 2026, 01:00:40 (HKT) |
| ^RUT | Russell 2000 Index | 3030.31 | 0.96 | 2026-08-07 | live as of 8 August 2026, 01:00:40 (HKT) |
| ^VIX | CBOE Volatility Index | 14.95 | -1.32 | 2026-08-07 | live as of 8 August 2026, 01:00:40 (HKT) |
| ^SKEW | CBOE SKEW Index | 134.73 | 1.06 | 2026-08-06 | closed |
| ^MOVE | ICE BofA MOVE Index | 76.82 | 8.38 | 2026-07-24 | closed |
| US2YT=X | United States 2-Year Treasury Yield | 4.2 | -0.98 | 2026-08-07 | live as of 8 August 2026, 01:00:40 (HKT) |
| US3YT=X | United States 3-Year Treasury Yield | 4.26 | -0.9 | 2026-08-07 | live as of 8 August 2026, 01:00:40 (HKT) |
| US5YT=X | United States 5-Year Treasury Yield | 4.36 | -0.69 | 2026-08-07 | live as of 8 August 2026, 01:00:40 (HKT) |
| US7YT=X | United States 7-Year Treasury Yield | 4.5 | -0.53 | 2026-08-07 | live as of 8 August 2026, 01:00:40 (HKT) |
| US10YT=X | United States 10-Year Treasury Yield | 4.66 | -0.32 | 2026-08-07 | live as of 8 August 2026, 01:00:40 (HKT) |
| US20YT=X | United States 20-Year Treasury Yield | 5.21 | -0.15 | 2026-08-07 | live as of 8 August 2026, 01:00:40 (HKT) |
| US30YT=X | United States 30-Year Treasury Yield | 5.21 | -0.09 | 2026-08-07 | live as of 8 August 2026, 01:00:40 (HKT) |
| HK50 | Hang Seng Futures | 25670.0 | 0.45 | 2026-08-07 | closed |
| KOR200c1 | KOSPI 200 Futures | 985.35 | 0.43 | 2026-08-06 | closed |
| CIHc1 | SSE 50 Futures | 2909.0 | -0.19 | 2026-08-06 | closed |
| HYG | iShares iBoxx High Yield Corporate Bond ETF | 79.58 | 0.15 | 2026-08-07 | live as of 8 August 2026, 01:00:40 (HKT) |
| LQD | iShares iBoxx Investment Grade Corporate Bond ETF | 106.47 | 0.1 | 2026-08-07 | live as of 8 August 2026, 01:00:40 (HKT) |
| JNK | SPDR Bloomberg High Yield Bond ETF | 95.78 | 0.17 | 2026-08-07 | live as of 8 August 2026, 01:00:40 (HKT) |
| RSP | Invesco S&P 500 Equal Weight ETF | 220.12 | 0.71 | 2026-08-07 | live as of 8 August 2026, 01:00:40 (HKT) |
| IWF | iShares Russell 1000 Growth ETF | 124.23 | 0.59 | 2026-08-07 | live as of 8 August 2026, 01:00:40 (HKT) |
| IWD | iShares Russell 1000 Value ETF | 257.48 | 0.53 | 2026-08-07 | live as of 8 August 2026, 01:00:40 (HKT) |
| TLT | iShares 20+ Year Treasury Bond ETF | 82.58 | 0.07 | 2026-08-07 | live as of 8 August 2026, 01:00:40 (HKT) |
| IEF | iShares 7-10 Year Treasury Bond ETF | 93.11 | 0.17 | 2026-08-07 | live as of 8 August 2026, 01:00:40 (HKT) |
| SHY | iShares 1-3 Year Treasury Bond ETF | 81.9 | 0.12 | 2026-08-07 | live as of 8 August 2026, 01:00:40 (HKT) |
| GC=F | Gold Future | 4397.5 | 3.67 | 2026-08-07 | live as of 8 August 2026, 01:00:40 (HKT) |
| SI=F | Silver Future | 63.51 | 3.37 | 2026-08-07 | live as of 8 August 2026, 01:00:40 (HKT) |
| CL=F | WTI Crude Oil Future | 78.22 | 1.2 | 2026-08-07 | live as of 8 August 2026, 01:00:40 (HKT) |
| HG=F | Copper Future | 6.59 | -1.41 | 2026-08-07 | live as of 8 August 2026, 01:00:40 (HKT) |

## Market Dispersion Analysis

- Sector ETF 20D dispersion: `9.97` points (moderate); leader `XLE` (Energy) `6.09`, laggard `XLU` (Utilities) `-3.88`
- Sector ETF 60D dispersion: `18.87` points (high); leader `XLV` (Health Care) `14.97`, laggard `XLU` (Utilities) `-3.9`

| Comparison | Left | Right | 20D Spread | Signal |
| --- | --- | --- | --- | --- |
| Equal-weight vs cap-weight | RSP (Equal-weight S&P 500) | SPY (S&P 500) | 0.14 | balanced |
| Small-cap vs large-cap | IWM (Russell 2000) | SPY (S&P 500) | -1.9 | large-cap leadership |
| Growth vs value | IWF (Russell 1000 Growth) | IWD (Russell 1000 Value) | -3.79 | value leadership |
| Nasdaq vs S&P 500 | QQQ (Nasdaq 100) | SPY (S&P 500) | -3.43 | S&P 500 leadership |

## Sector Constituent Dispersion

- Breadth 50D / 200D: percentage of active S&P 500 constituents in the sector trading above the 50-day / 200-day moving average.
- Positive 20D: percentage of active sector constituents with positive 20-day return.
- Std 20D: cross-sectional standard deviation of constituent 20-day returns; higher means wider stock-level dispersion.

| Sector | Count | Breadth 50D | Breadth 200D | Positive 20D | 20D Dispersion | Std 20D | Label | Leaders | Laggards |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Information Technology | 73 | 54.79 | 69.44 | 54.79 | 71.56 | 14.44 | very high | IT, ZBRA, CTSH | IBM, WDC, SNDK |
| Industrials | 83 | 64.63 | 73.42 | 62.65 | 56.73 | 9.78 | very high | LDOS, ALLE, SWK | LII, CHRW, HONA |
| Financials | 76 | 89.04 | 85.71 | 76.32 | 53.1 | 7.2 | very high | PYPL, GPN, WTW | COIN, IBKR, HOOD |
| Communication Services | 23 | 59.09 | 40.91 | 47.83 | 52.69 | 11.12 | very high | CHTR, FOXA, FOX | TTD, ECHO, APP |
| Health Care | 59 | 81.36 | 74.58 | 64.41 | 49.91 | 9.13 | very high | BAX, BDX, REGN | PODD, DVA, MRNA |
| Consumer Discretionary | 47 | 68.09 | 57.45 | 65.96 | 46.11 | 9.44 | very high | GRMN, DPZ, HAS | YUM, TSLA, APTV |
| Materials | 25 | 72.0 | 76.0 | 76.0 | 30.72 | 7.82 | very high | NUE, STLD, MOS | CRH, LIN, CTVA |
| Energy | 21 | 52.38 | 80.95 | 71.43 | 21.63 | 5.77 | very high | XOM, APA, BKR | HAL, WMB, TPL |
| Utilities | 31 | 6.45 | 41.94 | 6.45 | 19.39 | 4.02 | high | CEG, AWK, AES | VST, SRE, NRG |
| Consumer Staples | 34 | 69.7 | 65.62 | 70.59 | 18.83 | 4.53 | high | CLX, TGT, DG | BG, KR, MO |
| Real Estate | 31 | 35.48 | 77.42 | 54.84 | 17.02 | 3.48 | high | WY, DLR, EXR | FRT, REG, UDR |

## Economic Data Snapshot

### U.S. Labor

| Indicator | Latest | Unit | Change | Date | Rule-Based Interpretation |
| --- | --- | --- | --- | --- | --- |
| All Employees, Total Nonfarm | 158858.0 | thousands | -23.0 thousands vs prior | 2026-07-01 | Lower reading signals softer activity or liquidity. |
| Unemployment Rate | 4.1 | percent | -0.1 pp vs prior | 2026-07-01 | Lower reading eases macro pressure. |
| Initial Claims | 215000.0 | number | -12000.0 number vs prior | 2026-06-20 | Lower claims indicate firmer labor-market conditions. |
| Continued Claims | 1821000.0 | number | 21000.0 number vs prior | 2026-06-13 | Higher claims indicate softer labor-market conditions. |
| Labor Force Participation Rate | 61.4 | percent | -0.1 pp vs prior | 2026-07-01 | Lower participation constrains labor supply. |

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
| US dollar/Euro ECB reference exchange rate | 1.15 | USD | -0.0 USD vs prior | 2026-08-07 | EUR weakened versus this currency. |
| Japanese yen/Euro ECB reference exchange rate | 182.64 | JPY | 0.47 JPY vs prior | 2026-08-07 | EUR strengthened versus this currency. |
| Chinese yuan renminbi/Euro ECB reference exchange rate | 7.78 | CNY | -0.01 CNY vs prior | 2026-08-07 | EUR weakened versus this currency. |
| Australian dollar/Euro ECB reference exchange rate | 1.64 | AUD | -0.0 AUD vs prior | 2026-08-07 | EUR weakened versus this currency. |

ABS Australia note: ABS rows are stored locally/Neon, but most series are dimension-coded; only curated series should be promoted into narrative report text.

## Sector and Theme Leadership

### Official Sector Strength

Supporting and detracting names are the top/bottom S&P 500 constituents by 20D return when constituent coverage is available; otherwise the report falls back to related ETFs.

| Rank | Sector | Score | Trend | Momentum | Stock Breadth | ETF Flow | Flow Reliability | 3M RS | Supporting / Leaders | Detracting / Laggards |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Cybersecurity | 69.81 | strong uptrend | positive | broad | 64.19 | 65.0 | 59.54 | CIBR | CIBR |
| 2 | Financials | 68.17 | strong uptrend | positive | broad | 68.14 | 100.0 | 54.71 | PYPL, GPN, WTW | COIN, IBKR, HOOD |
| 3 | Industrials | 66.54 | strong uptrend | neutral | broad | 58.46 | 65.0 | 50.5 | LDOS, ALLE, SWK | LII, CHRW, HONA |
| 4 | Healthcare | 65.48 | strong uptrend | positive | broad | 65.88 | 90.0 | 53.9 | BAX, BDX, REGN | PODD, DVA, MRNA |
| 5 | Defense | 65.13 | strong uptrend | neutral | broad | 50.63 | 65.0 | 51.05 | XAR | XAR |
| 6 | Consumer Staples | 60.71 | strong uptrend | neutral | broad | 59.71 | 65.0 | 49.28 | CLX, TGT, DG | BG, KR, MO |
| 7 | Technology | 60.48 | strong uptrend | neutral | mixed | 55.27 | 95.0 | 47.59 | IT, ZBRA, CTSH | IBM, WDC, SNDK |
| 8 | Consumer Discretionary | 60.32 | uptrend | neutral | broad | 69.46 | 65.0 | 47.29 | GRMN, DPZ, HAS | YUM, TSLA, APTV |
| 9 | Energy | 57.03 | uptrend | neutral | broad | 50.0 | 0.0 | 51.42 | XOM, APA, BKR | HAL, WMB, TPL |
| 10 | Real Estate | 56.35 | strong uptrend | neutral | broad | 55.99 | 95.0 | 48.07 | WY, DLR, EXR | FRT, REG, UDR |
| 11 | Grid Infrastructure | 56.25 | strong uptrend | neutral | weak | 68.67 | 65.0 | 44.69 | GRID | GRID |
| 12 | Semiconductors | 54.66 | strong uptrend | neutral | weak | 60.82 | 100.0 | 42.57 | SMH, SOXX | SOXX, SMH |
| 13 | Crypto | 51.63 | neutral | neutral | mixed | 66.34 | 65.0 | 50.0 |  |  |
| 14 | Nuclear | 42.7 | strong downtrend | negative | weak | 50.0 | 0.0 | 38.77 | NLR | NLR |
| 15 | Utilities | 33.6 | strong downtrend | neutral | weak | 50.92 | 65.0 | 41.84 | CEG, AWK, AES | VST, SRE, NRG |

### Thematic Strength

| Rank | Theme | Score | Setup | ETF Flow | Flow Reliability | Dispersion | Price | News |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Financials | 59.35 | Positive setup | 68.14 | 100.0 | 8.54 | False | False |
| 2 | Defense | 59.07 | Positive setup | 50.63 | 65.0 | 12.02 | False | False |
| 3 | Quality Growth | 58.75 | Positive setup | 62.43 | 65.0 | 31.25 | False | False |
| 4 | Small Caps | 58.48 | Positive setup | 45.1 | 65.0 | 0.0 | False | False |
| 5 | Healthcare Innovation | 57.64 | Positive setup | 65.88 | 90.0 | 9.06 | False | False |
| 6 | Cybersecurity | 56.96 | Neutral / watchlist | 64.19 | 65.0 | 12.73 | False | False |
| 7 | AI Infrastructure | 56.74 | Neutral / watchlist | 60.82 | 100.0 | 38.5 | False | False |
| 8 | Energy | 54.18 | Positive setup | 50.0 | 0.0 | 6.55 | False | False |
| 9 | Semiconductors | 50.91 | Neutral / watchlist | 60.82 | 100.0 | 18.5 | False | False |
| 10 | Dividend Defensives | 50.01 | Neutral / watchlist | 53.07 | 65.0 | 6.17 | False | False |
| 11 | Grid Infrastructure | 46.66 | Neutral / watchlist | 68.67 | 65.0 | 16.72 | False | False |
| 12 | Nuclear | 38.13 | Weak setup | 50.0 | 0.0 | 8.12 | False | False |
| 13 | Crypto Infrastructure | 30.62 | Underperformance risk | 66.34 | 65.0 | 11.38 | False | False |

- Top 5 improving themes: Cybersecurity, Financials, Healthcare Innovation, Defense, Quality Growth
- Top 5 deteriorating themes: Crypto Infrastructure, Nuclear, Grid Infrastructure, AI Infrastructure, Semiconductors
- Strong news but weak price confirmation: none
- Strong price but weak news confirmation: none

### Sector / Theme Alignment

| Sector | Related Themes | Sector Score | Sector Signal | Theme Score | Theme Signal | Interpretation |
| --- | --- | --- | --- | --- | --- | --- |
| Cybersecurity | Cybersecurity | 69.81 | strong | 56.96 | positive | sector and theme confirmation |
| Financials | Financials | 68.17 | strong | 59.35 | positive | sector and theme confirmation |
| Industrials | Defense, Grid Infrastructure | 66.54 | strong | 52.87 | mixed | sector stronger than related themes |
| Healthcare | Healthcare Innovation | 65.48 | strong | 57.64 | positive | sector and theme confirmation |
| Defense | Defense | 65.13 | strong | 59.07 | positive | sector and theme confirmation |
| Consumer Staples | Dividend Defensives | 60.71 | positive | 50.01 | mixed | sector stronger than related themes |
| Technology | AI Infrastructure, Semiconductors, Quality Growth | 60.48 | positive | 55.47 | positive | sector and theme confirmation |
| Consumer Discretionary | Small Caps | 60.32 | positive | 58.48 | positive | sector and theme confirmation |
| Energy | Energy | 57.03 | positive | 54.18 | mixed | sector stronger than related themes |
| Real Estate | Dividend Defensives | 56.35 | positive | 50.01 | mixed | sector stronger than related themes |
| Grid Infrastructure | Grid Infrastructure | 56.25 | positive | 46.66 | mixed | sector stronger than related themes |
| Semiconductors | AI Infrastructure, Semiconductors | 54.66 | mixed | 53.82 | mixed | mixed confirmation |
| Crypto | Crypto Infrastructure | 51.63 | mixed | 30.62 | very weak | mixed confirmation |
| Nuclear | Nuclear | 42.7 | weak | 38.13 | weak | broad weakness across sector and themes |
| Utilities | Grid Infrastructure, Nuclear, Dividend Defensives | 33.6 | very weak | 44.94 | weak | broad weakness across sector and themes |

## Three-Month Outperformance Setup

| Rank | Theme | Score | Classification | Drivers | Invalidation Triggers |
| --- | --- | --- | --- | --- | --- |
| 1 | Small Caps | 63.29 | Positive setup | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 2 | Healthcare Innovation | 63.15 | Positive setup | relative_strength_60d, trend_persistence, breadth, downside_volatility, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 3 | Financials | 63.03 | Positive setup | relative_strength_60d, trend_persistence, breadth, downside_volatility, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 4 | Quality Growth | 60.92 | Positive setup | trend_persistence, breadth | relative strength below SPY, breadth below 45%, news turns negative |
| 5 | Energy | 60.88 | Positive setup | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 6 | Defense | 60.68 | Positive setup | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 7 | Cybersecurity | 57.86 | Neutral / watchlist | relative_strength_60d, trend_persistence, breadth, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 8 | AI Infrastructure | 57.25 | Neutral / watchlist | trend_persistence, breadth | relative strength below SPY, breadth below 45%, news turns negative |
| 9 | Dividend Defensives | 55.48 | Neutral / watchlist | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 10 | Semiconductors | 51.13 | Neutral / watchlist | trend_persistence, breadth | relative strength below SPY, breadth below 45%, news turns negative |
| 11 | Grid Infrastructure | 45.2 | Neutral / watchlist | downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 12 | Nuclear | 33.46 | Weak setup |  | relative strength below SPY, breadth below 45%, news turns negative |

## Breadth and Participation

- Above 50DMA: `68.33%`
- Above 200DMA: `72.88%`
- Positive 20D return: `66.67%`

## Volatility and Risk Signals

- VIX close=14.95 pct_chg=-1.32

## News Analytics

- Sentiment counts: {'positive': 68, 'negative': 11, 'neutral': 1}
- News confirmation score: `85.62`

### Top Market-Moving Headlines

**1. Oil prices rise as as market waits on deal to open Strait of Hormuz**
- Source: CNBC Top News
- Importance / impact: High / Positive
- Relevance / horizon: macro / short-term
- Affected assets: oil prices, supply disruptions
- Score: `72.67`
- Investment implication: Macro-relevant positive signal; use as context for rates, volatility, and index confirmation over the short-term.

**2. Solar stocks shine after Trump extends China tariffs to polysilicon products**
- Source: CNBC Top News
- Importance / impact: High / Positive
- Relevance / horizon: macro / short-term
- Affected assets: trade policies, renewable energy
- Score: `57.0`
- Investment implication: Macro-relevant positive signal; use as context for rates, volatility, and index confirmation over the short-term.

**3. BP profit more than doubles as Trump blasts Big Oil for ‘making too much money’**
- Source: CNBC Business News
- Importance / impact: High / Positive
- Relevance / horizon: macro / short-term
- Affected assets: BP, U.S, energy, political, oil prices
- Score: `48.0`
- Investment implication: Macro-relevant positive signal; use as context for rates, volatility, and index confirmation over the short-term.

**4. China's super-rich 'in shock' and hunting for cash as Beijing issues surprise tax on offshore trusts**
- Source: CNBC Technology
- Importance / impact: Medium / Negative
- Relevance / horizon: sector_theme / short-term
- Affected assets: tax_policy, wealth_management
- Score: `45.9`
- Investment implication: Theme or sector negative signal; requires price and volume confirmation before affecting rankings.

**5. SK Hynix to invest $38 billion building new memory chip plants as demand soars**
- Source: CNBC Top News
- Importance / impact: Medium / Positive
- Relevance / horizon: single_name / short-term
- Affected assets: SK, investment, technology, manufacturing
- Score: `44.88`
- Investment implication: Single-name positive signal; low weight unless it maps to a broader sector or theme.

**6. China's exports growth beats estimates in July, as AI-driven shipments surge**
- Source: CNBC Technology
- Importance / impact: Medium / Positive
- Relevance / horizon: sector_theme / short-term
- Affected assets: AI, exports, global_economy
- Score: `43.89`
- Investment implication: Theme or sector positive signal; requires price and volume confirmation before affecting rankings.

**7. Copper jumps to its highest level ever. What the metal is telling us**
- Source: CNBC Top News
- Importance / impact: Medium / Positive
- Relevance / horizon: sector_theme / short-term
- Affected assets: commodities, economy
- Score: `41.18`
- Investment implication: Theme or sector positive signal; requires price and volume confirmation before affecting rankings.

**8. Optical stocks have a China problem that most investors are missing**
- Source: MarketWatch Top Stories
- Importance / impact: Medium / Negative
- Relevance / horizon: sector_theme / medium-term
- Affected assets: trade, geopolitics
- Score: `38.73`
- Investment implication: Theme or sector negative signal; requires price and volume confirmation before affecting rankings.

**9. Trade Desk shares tumble on earnings miss and weak outlook**
- Source: MarketWatch Top Stories
- Importance / impact: Medium / Negative
- Relevance / horizon: single_name / short-term
- Affected assets: TTD, earnings report, revenue miss, growth concerns
- Score: `37.29`
- Investment implication: Single-name negative signal; low weight unless it maps to a broader sector or theme.

**10. Applied Materials is about to report earnings. How to trade the AI picks-and-shovels play ahead of results**
- Source: CNBC Top News
- Importance / impact: Medium / Positive
- Relevance / horizon: single_name / short-term
- Affected assets: APPLM, AI, Earnings Report
- Score: `37.05`
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
- Market flow score: `49.7 / 100`
- Equity risk flow: `47.4`
- Credit risk flow: `61.5`
- Sector cyclicality flow: `44.4`
- Duration/liquidity flow: `45.7`
- Alternatives: `mixed alternative-asset demand`
- ETF flow reliability: `71.5 / 100`
- Dominant allocation direction: `mixed allocation`

### Core Flow Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVV | U.S. Broad Equity | -0.7 | 0.4 | 0.4 | -0.9 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Medium-term deterioration | 83.0 |
| ACWI | Global Equity | -1.9 | -1.4 | 0.0 | -1.0 | Up | Sell | Normal | Profit Taking | Slightly Bearish | Strong confirmation; Persistent selling | 87.0 |
| EFA | Developed Markets ex-U.S. | -0.5 | -0.1 | 0.0 | -1.5 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Medium-term deterioration; Persistent selling | 75.0 |
| IEMG | Emerging Markets | -0.0 | -0.3 | 0.1 | -0.5 | Flat | Neutral | Normal | Neutral | Neutral | Structural accumulation; Persistent selling | 83.0 |
| IJH | U.S. Mid Cap | 0.6 | 1.0 | 0.7 | -1.1 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural accumulation | 91.0 |
| IWM | U.S. Small Cap | -0.7 | 0.1 | 0.5 | -1.4 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural distribution | 79.0 |
| LQD | Investment-Grade Credit | -1.1 | 0.9 | 0.3 | 0.4 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Medium-term deterioration | 83.0 |
| HYG | High-Yield Credit | 1.0 | 1.7 | 0.5 | -0.9 | Flat | Buy | Normal | Quiet Accumulation | Improving | Strong confirmation | 95.0 |
| SGOV | Treasury Bills / Cash | -0.6 | -0.9 | 0.9 | -0.4 | Flat | Neutral | Normal | Neutral | Neutral | Structural accumulation; Strong sponsorship | 99.0 |
| SHY | Short-Duration Treasuries | -1.1 | -0.1 | 0.2 | 0.9 | Flat | Buy | Normal | Quiet Accumulation | Improving | Medium-term deterioration; Persistent selling | 75.0 |
| IEF | Intermediate-Duration Treasuries | 0.1 | -0.3 | 0.7 | -0.7 | Flat | Neutral | Normal | Neutral | Neutral | Structural accumulation | 91.0 |
| TLT | Long-Duration Treasuries | 0.2 | 0.2 | 0.6 | 0.1 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Medium-term recovery | 87.0 |
| GLD | Gold | 1.4 | 1.5 | 0.5 | 1.0 | Up | Buy | High | Confirmed Accumulation | Strong Risk-On | Strong confirmation | 95.0 |
| IBIT | Bitcoin | 0.6 | -1.4 | 0.7 | -0.9 | Up | Buy | Normal | Steady Accumulation | Risk-On | Medium-term recovery | 87.0 |

### Sector Flow Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| XLC | Communication Services | -0.6 | -1.0 | 0.3 | -1.2 | Flat | Buy | Normal | Quiet Accumulation | Improving | Tactical rebound inside structural distribution | 83.0 |
| XLY | Consumer Discretionary | 1.6 | 3.0 | 0.6 | -1.5 | Up | Buy | Normal | Steady Accumulation | Risk-On | Strong confirmation; Exceptional institutional buying | 100.0 |
| XLP | Consumer Staples | 0.6 | 1.5 | 0.5 | -1.1 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural accumulation | 91.0 |
| XLE | Energy | -0.6 | -1.2 | 0.3 | -1.0 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural distribution | 79.0 |
| XLF | Financials | 1.2 | 2.4 | 0.5 | -1.0 | Up | Buy | Normal | Steady Accumulation | Risk-On | Strong confirmation; Exceptional institutional buying | 100.0 |
| XLV | Health Care | 1.4 | 2.6 | 0.6 | -0.5 | Up | Buy | Normal | Steady Accumulation | Risk-On | Strong confirmation; Exceptional institutional buying | 100.0 |
| XLI | Industrials | -0.3 | 0.7 | 0.5 | -1.2 | Up | Buy | Normal | Steady Accumulation | Risk-On | Strong confirmation | 95.0 |
| XLK | Information Technology | 0.1 | -0.9 | 0.7 | -1.2 | Flat | Neutral | Normal | Neutral | Neutral | Medium-term recovery | 87.0 |
| XLB | Materials | -1.1 | -0.2 | 0.4 | -0.8 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Medium-term deterioration | 83.0 |
| XLRE | Real Estate | 0.4 | 1.6 | 0.6 | -0.1 | Flat | Neutral | Normal | Neutral | Neutral | Structural accumulation | 91.0 |
| XLU | Utilities | -0.2 | 0.7 | 0.3 | 1.3 | Down | Neutral | High | Heavy Selling Pressure | Cautious | Medium-term deterioration | 83.0 |

### Subsector PFV Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ITA | Aerospace and Defense | 0.2 | 0.1 | 0.3 | 1.5 | Up | Buy | High | Confirmed Accumulation | Strong Risk-On | Medium-term recovery; Exceptional institutional buying | 95.0 |
| SOXX | Semiconductors | -1.1 | 0.9 | 0.4 | -0.8 | Flat | Sell | Normal | Quiet Distribution | Weakening | Medium-term deterioration | 83.0 |
| SMH | Semiconductors | -0.1 | 0.9 | 0.5 | -1.0 | Flat | Neutral | Low | Dormant Market | Neutral | Structural accumulation | 91.0 |
| CIBR | Cybersecurity | 0.5 | 1.4 | 0.6 | -1.0 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural accumulation | 91.0 |

### Material Flow Divergences

| Severity | Type | Primary | Comparison | Interpretation |
| --- | --- | --- | --- | --- |
| medium | related_subsector_divergence | XLI | ITA | defense-specific demand differs from broad industrials |
| medium | related_subsector_divergence | XLK | SOXX | technology differs from semiconductors |
| high | close_substitute_divergence | GLD | IAU | primary representative differs from close substitute |
| high | close_substitute_divergence | IVV | SPY | primary representative differs from close substitute |
| high | close_substitute_divergence | IVV | SPY | primary representative differs from close substitute |
| high | close_substitute_divergence | IWF | IVW | primary representative differs from close substitute |


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

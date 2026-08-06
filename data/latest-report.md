# Rule-Based Institutional Market Update

Generated at: 6 August 2026, 21:09:34 (HKT)
Window: 24h

## Executive Dashboard

- Regime score: **66.18 / 100** (Moderate Risk-On)
- US equity strength: **82.03 / 100** (strong)
- Evidence quality: **83.0 / 100**
- ETF flow contribution: **51.8 / 100**, reliability **71.67 / 100**
- Breadth: **broad**; above 50DMA `76.67%`, above 200DMA `72.88%`
- Top sector score: **Cybersecurity** `70.05`
- Top theme score: **Financials** `62.37`

## Market Regime Score

| Metric | Value | Driver / Interpretation |
| --- | --- | --- |
| Overall regime | 66.18 | Moderate Risk-On |
| equity_trend | 93.75 | risk-on support; Core equity ETFs versus moving averages. |
| equity_momentum | 53.14 | neutral / mixed; 5D/20D/60D return momentum across SPY, QQQ, IWM, and SMH. |
| market_breadth | 75.4 | risk-on support; Participation breadth from tracked equity/ETF rows. |
| volatility | 70.0 | risk-on support; VIX level and change; higher score means calmer volatility conditions. |
| rates_yield_curve | 58.0 | mild risk-on support; Treasury yield pressure and curve shape; higher score means less rates pressure. |
| credit_proxy | 50.0 | neutral / mixed; Credit-market proxy; currently neutral when no direct spread signal is available. |
| dollar_fx | 54.5 | neutral / mixed; Dollar move; higher score means less USD tightening pressure. |
| commodity_confirmation | 55.0 | mild risk-on support; Copper, silver, oil, and gold mix; higher score means better cyclical confirmation. |
| etf_flow | 51.29 | neutral / mixed; Grouped ETF flow contribution adjusted for reliability. |
| news_confirmation | 77.5 | risk-on support; Weighted headline/news confirmation score. |
| Positive contributors |  | equity_trend=93.75, news_confirmation=77.5, market_breadth=75.4, volatility=70.0 |
| Negative contributors |  | none |

## US Equity Strength Score

| Component | Score |
| --- | --- |
| indices_above_moving_averages | 93.75 |
| sp500_trend | 100.0 |
| nasdaq_trend | 100.0 |
| russell_participation | 100.0 |
| returns_momentum | 53.14 |
| rsi_zone | 75.0 |
| macd_confirmation | 70.0 |
| volume_confirmation | 50.0 |
| breadth | 75.4 |

## Evidence Quality / Confidence

- Confidence score: `83.0`
- Agreement ratio: `0.6`
- Contradiction count: `0`
- Missing indicators: none
- Warning flags: none

## Cross-Asset Confirmation

| Area | Signal | Interpretation |
| --- | --- | --- |
| Equities | S&P 500 stable; Nasdaq falling; Russell 2000 falling | Confirms risk appetite when broad indices rise together; weak small caps would narrow the signal. |
| Rates | 10Y Treasury rising; MOVE rising | Rising yields can pressure duration assets; falling MOVE supports calmer bond volatility. |
| Dollar | DXY proxy stable | A stronger dollar can tighten financial conditions and pressure commodities/emerging-market risk. |
| Credit | HYG stable | High-yield weakness would challenge equity risk-on confirmation. |
| Gold | Gold rising | Gold strength can indicate defensive demand, inflation hedging, or geopolitical concern. |
| Silver | Silver falling | Silver helps distinguish precious-metal demand from industrial/cyclical confirmation when data is available. |
| Copper | Copper rising | Copper strength supports cyclical growth confirmation; weakness would dilute risk-on breadth. |
| Oil | WTI crude rising | Oil spikes can be inflationary risk; falling oil can ease cost pressure but may also flag demand softness. |
| Volatility | VIX rising | Falling VIX supports risk appetite; a volatility spike would reduce confidence in broad risk-on. |

### Macro Snapshot

Live macro rows are intraday snapshots from `public.macro_live`; closed rows are official stored rows from `public.macro`.

| Symbol | Name | Close | Pct Chg | Market Date | Status |
| --- | --- | --- | --- | --- | --- |
| ^GSPC | S&P 500 | 7723.55 | -0.17 | 2026-08-05 | closed |
| ^IXIC | NASDAQ Composite | 26363.44 | -0.83 | 2026-08-05 | closed |
| ^RUT | Russell 2000 Index | 3019.19 | -0.59 | 2026-08-05 | closed |
| ^VIX | CBOE Volatility Index | 15.96 | 0.95 | 2026-08-06 | live as of 6 August 2026, 21:00:24 (HKT) |
| ^SKEW | CBOE SKEW Index | 133.32 | 5.47 | 2026-08-05 | closed |
| ^MOVE | ICE BofA MOVE Index | 76.82 | 8.38 | 2026-07-24 | closed |
| US2YT=X | United States 2-Year Treasury Yield | 4.22 | 0.9 | 2026-08-06 | live as of 6 August 2026, 21:00:24 (HKT) |
| US3YT=X | United States 3-Year Treasury Yield | 4.27 | 0.85 | 2026-08-06 | live as of 6 August 2026, 21:00:24 (HKT) |
| US5YT=X | United States 5-Year Treasury Yield | 4.36 | 0.73 | 2026-08-06 | live as of 6 August 2026, 21:00:24 (HKT) |
| US7YT=X | United States 7-Year Treasury Yield | 4.49 | 0.62 | 2026-08-06 | live as of 6 August 2026, 21:00:24 (HKT) |
| US10YT=X | United States 10-Year Treasury Yield | 4.64 | 0.58 | 2026-08-06 | live as of 6 August 2026, 21:00:24 (HKT) |
| US20YT=X | United States 20-Year Treasury Yield | 5.2 | 0.44 | 2026-08-06 | live as of 6 August 2026, 21:00:24 (HKT) |
| US30YT=X | United States 30-Year Treasury Yield | 5.19 | 0.37 | 2026-08-06 | live as of 6 August 2026, 21:00:24 (HKT) |
| HK50 | Hang Seng Futures | 25536.5 | -0.56 | 2026-08-06 | closed |
| KOR200c1 | KOSPI 200 Futures | 1003.05 | -3.74 | 2026-08-05 | closed |
| CIHc1 | SSE 50 Futures | 2914.4 | 1.49 | 2026-08-05 | closed |
| HYG | iShares iBoxx High Yield Corporate Bond ETF | 79.52 | -0.04 | 2026-08-05 | closed |
| LQD | iShares iBoxx Investment Grade Corporate Bond ETF | 106.74 | -0.02 | 2026-08-05 | closed |
| JNK | SPDR Bloomberg High Yield Bond ETF | 95.67 | -0.08 | 2026-08-05 | closed |
| RSP | Invesco S&P 500 Equal Weight ETF | 219.73 | -0.23 | 2026-08-05 | closed |
| IWF | iShares Russell 1000 Growth ETF | 123.89 | -0.33 | 2026-08-05 | closed |
| IWD | iShares Russell 1000 Value ETF | 256.13 | -0.19 | 2026-08-05 | closed |
| TLT | iShares 20+ Year Treasury Bond ETF | 83.0 | 0.22 | 2026-08-05 | closed |
| IEF | iShares 7-10 Year Treasury Bond ETF | 93.31 | 0.06 | 2026-08-05 | closed |
| SHY | iShares 1-3 Year Treasury Bond ETF | 81.9 | 0.04 | 2026-08-05 | closed |
| GC=F | Gold Future | 4312.8 | 1.58 | 2026-08-06 | live as of 6 August 2026, 21:00:24 (HKT) |
| SI=F | Silver Future | 61.62 | -0.76 | 2026-08-06 | live as of 6 August 2026, 21:00:24 (HKT) |
| CL=F | WTI Crude Oil Future | 76.26 | 1.38 | 2026-08-06 | live as of 6 August 2026, 21:00:24 (HKT) |
| HG=F | Copper Future | 6.77 | 1.04 | 2026-08-06 | live as of 6 August 2026, 21:00:24 (HKT) |

## Market Dispersion Analysis

- Sector ETF 20D dispersion: `9.26` points (moderate); leader `XLF` (Financials) `5.51`, laggard `XLU` (Utilities) `-3.75`
- Sector ETF 60D dispersion: `19.6` points (high); leader `XLV` (Health Care) `14.41`, laggard `XLC` (Communication Services) `-5.19`

| Comparison | Left | Right | 20D Spread | Signal |
| --- | --- | --- | --- | --- |
| Equal-weight vs cap-weight | RSP (Equal-weight S&P 500) | SPY (S&P 500) | 0.28 | balanced |
| Small-cap vs large-cap | IWM (Russell 2000) | SPY (S&P 500) | -1.13 | large-cap leadership |
| Growth vs value | IWF (Russell 1000 Growth) | IWD (Russell 1000 Value) | -2.74 | value leadership |
| Nasdaq vs S&P 500 | QQQ (Nasdaq 100) | SPY (S&P 500) | -2.45 | S&P 500 leadership |

## Sector Constituent Dispersion

- Breadth 50D / 200D: percentage of active S&P 500 constituents in the sector trading above the 50-day / 200-day moving average.
- Positive 20D: percentage of active sector constituents with positive 20-day return.
- Std 20D: cross-sectional standard deviation of constituent 20-day returns; higher means wider stock-level dispersion.

| Sector | Count | Breadth 50D | Breadth 200D | Positive 20D | 20D Dispersion | Std 20D | Label | Leaders | Laggards |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Information Technology | 74 | 54.05 | 69.86 | 60.81 | 61.49 | 13.45 | very high | ZBRA, IT, CTSH | APP, SNDK, IBM |
| Financials | 76 | 93.15 | 85.71 | 81.58 | 48.35 | 7.25 | very high | PYPL, GPN, ARES | COIN, PGR, HOOD |
| Health Care | 59 | 84.75 | 71.19 | 67.8 | 48.11 | 9.01 | very high | BAX, CRL, SOLV | PODD, DVA, MRNA |
| Industrials | 82 | 67.5 | 73.08 | 69.51 | 44.02 | 8.44 | very high | ALLE, SWK, EMR | ROL, LII, CHRW |
| Consumer Discretionary | 47 | 70.21 | 61.7 | 72.34 | 43.97 | 9.54 | very high | GRMN, EXPE, DPZ | YUM, TSLA, APTV |
| Materials | 26 | 69.23 | 76.92 | 73.08 | 29.35 | 8.47 | very high | NUE, FCX, STLD | LIN, CTVA, ALB |
| Communication Services | 22 | 66.67 | 38.1 | 59.09 | 24.85 | 6.75 | very high | CHTR, NWS, FOXA | TTWO, ECHO, PSKY |
| Utilities | 31 | 16.13 | 48.39 | 12.9 | 20.61 | 4.13 | very high | CEG, AWK, PCG | VST, SRE, NRG |
| Consumer Staples | 34 | 66.67 | 62.5 | 61.76 | 20.18 | 4.6 | very high | CLX, TGT, DG | KR, MO, BG |
| Real Estate | 31 | 54.84 | 80.65 | 64.52 | 19.03 | 4.43 | high | WY, DLR, HST | MAA, UDR, CCI |
| Energy | 21 | 38.1 | 80.95 | 52.38 | 16.86 | 5.01 | high | PSX, XOM, BKR | WMB, TRGP, HAL |

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
| US dollar/Euro ECB reference exchange rate | 1.16 | USD | 0.0 USD vs prior | 2026-08-05 | EUR strengthened versus this currency. |
| Japanese yen/Euro ECB reference exchange rate | 182.08 | JPY | 0.82 JPY vs prior | 2026-08-05 | EUR strengthened versus this currency. |
| Chinese yuan renminbi/Euro ECB reference exchange rate | 7.8 | CNY | 0.02 CNY vs prior | 2026-08-05 | EUR strengthened versus this currency. |
| Australian dollar/Euro ECB reference exchange rate | 1.64 | AUD | 0.0 AUD vs prior | 2026-08-05 | EUR strengthened versus this currency. |

ABS Australia note: ABS rows are stored locally/Neon, but most series are dimension-coded; only curated series should be promoted into narrative report text.

## Sector and Theme Leadership

### Official Sector Strength

Supporting and detracting names are the top/bottom S&P 500 constituents by 20D return when constituent coverage is available; otherwise the report falls back to related ETFs.

| Rank | Sector | Score | Trend | Momentum | Stock Breadth | ETF Flow | Flow Reliability | 3M RS | Supporting / Leaders | Detracting / Laggards |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Cybersecurity | 70.05 | strong uptrend | positive | broad | 65.04 | 65.0 | 61.98 | CIBR | CIBR |
| 2 | Financials | 68.38 | strong uptrend | positive | broad | 59.84 | 90.0 | 54.88 | PYPL, GPN, ARES | COIN, PGR, HOOD |
| 3 | Industrials | 67.84 | strong uptrend | neutral | broad | 67.52 | 65.0 | 51.3 | ALLE, SWK, EMR | ROL, LII, CHRW |
| 4 | Technology | 66.57 | strong uptrend | neutral | broad | 63.82 | 100.0 | 48.64 | ZBRA, IT, CTSH | APP, SNDK, IBM |
| 5 | Healthcare | 66.0 | strong uptrend | neutral | broad | 82.8 | 100.0 | 52.74 | BAX, CRL, SOLV | PODD, DVA, MRNA |
| 6 | Grid Infrastructure | 65.67 | strong uptrend | neutral | broad | 64.04 | 65.0 | 45.51 | GRID | GRID |
| 7 | Defense | 64.34 | strong uptrend | neutral | broad | 43.18 | 65.0 | 50.61 | XAR | XAR |
| 8 | Consumer Staples | 62.55 | strong uptrend | neutral | broad | 55.09 | 65.0 | 47.51 | CLX, TGT, DG | KR, MO, BG |
| 9 | Consumer Discretionary | 60.59 | uptrend | neutral | broad | 69.9 | 65.0 | 47.51 | GRMN, EXPE, DPZ | YUM, TSLA, APTV |
| 10 | Real Estate | 58.18 | strong uptrend | neutral | broad | 44.62 | 90.0 | 48.43 | WY, DLR, HST | MAA, UDR, CCI |
| 11 | Semiconductors | 53.53 | uptrend | neutral | weak | 61.91 | 100.0 | 43.95 | SMH, SOXX | SOXX, SMH |
| 12 | Crypto | 51.44 | neutral | neutral | mixed | 64.44 | 65.0 | 50.0 |  |  |
| 13 | Energy | 48.59 | strong downtrend | neutral | broad | 44.27 | 95.0 | 49.29 | PSX, XOM, BKR | WMB, TRGP, HAL |
| 14 | Nuclear | 43.24 | strong downtrend | neutral | weak | 50.0 | 0.0 | 40.13 | NLR | NLR |
| 15 | Utilities | 32.73 | strong downtrend | neutral | weak | 47.96 | 65.0 | 41.74 | CEG, AWK, PCG | VST, SRE, NRG |

### Thematic Strength

| Rank | Theme | Score | Setup | ETF Flow | Flow Reliability | Dispersion | Price | News |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Financials | 62.37 | Positive setup | 59.84 | 90.0 | 5.67 | True | False |
| 2 | Healthcare Innovation | 62.04 | Positive setup | 82.8 | 100.0 | 5.64 | True | False |
| 3 | Quality Growth | 61.02 | Positive setup | 63.98 | 65.0 | 27.92 | True | False |
| 4 | Small Caps | 59.48 | Positive setup | 48.76 | 65.0 | 0.0 | False | False |
| 5 | AI Infrastructure | 58.56 | Neutral / watchlist | 61.91 | 100.0 | 32.74 | False | False |
| 6 | Cybersecurity | 58.53 | Neutral / watchlist | 65.04 | 65.0 | 8.39 | False | False |
| 7 | Defense | 57.23 | Neutral / watchlist | 43.18 | 65.0 | 11.79 | False | False |
| 8 | Energy | 54.48 | Positive setup | 44.27 | 95.0 | 4.36 | False | False |
| 9 | Semiconductors | 51.55 | Neutral / watchlist | 61.91 | 100.0 | 14.45 | False | False |
| 10 | Grid Infrastructure | 51.54 | Neutral / watchlist | 64.04 | 65.0 | 17.7 | False | False |
| 11 | Dividend Defensives | 51.3 | Neutral / watchlist | 54.13 | 65.0 | 4.89 | False | False |
| 12 | Nuclear | 39.28 | Weak setup | 50.0 | 0.0 | 13.2 | False | False |
| 13 | Crypto Infrastructure | 32.17 | Underperformance risk | 64.44 | 65.0 | 10.74 | False | False |

- Top 5 improving themes: Cybersecurity, Financials, Healthcare Innovation, Defense, Small Caps
- Top 5 deteriorating themes: Crypto Infrastructure, Nuclear, Grid Infrastructure, Semiconductors, AI Infrastructure
- Strong news but weak price confirmation: none
- Strong price but weak news confirmation: Financials, Healthcare Innovation, Quality Growth

### Sector / Theme Alignment

| Sector | Related Themes | Sector Score | Sector Signal | Theme Score | Theme Signal | Interpretation |
| --- | --- | --- | --- | --- | --- | --- |
| Cybersecurity | Cybersecurity | 70.05 | strong | 58.53 | positive | sector and theme confirmation |
| Financials | Financials | 68.38 | strong | 62.37 | positive | sector and theme confirmation |
| Industrials | Defense, Grid Infrastructure | 67.84 | strong | 54.39 | mixed | sector stronger than related themes |
| Technology | AI Infrastructure, Semiconductors, Quality Growth | 66.57 | strong | 57.04 | positive | sector and theme confirmation |
| Healthcare | Healthcare Innovation | 66.0 | strong | 62.04 | positive | sector and theme confirmation |
| Grid Infrastructure | Grid Infrastructure | 65.67 | strong | 51.54 | mixed | sector stronger than related themes |
| Defense | Defense | 64.34 | positive | 57.23 | positive | sector and theme confirmation |
| Consumer Staples | Dividend Defensives | 62.55 | positive | 51.3 | mixed | sector stronger than related themes |
| Consumer Discretionary | Small Caps | 60.59 | positive | 59.48 | positive | sector and theme confirmation |
| Real Estate | Dividend Defensives | 58.18 | positive | 51.3 | mixed | sector stronger than related themes |
| Semiconductors | AI Infrastructure, Semiconductors | 53.53 | mixed | 55.06 | positive | theme stronger than official sector |
| Crypto | Crypto Infrastructure | 51.44 | mixed | 32.17 | very weak | mixed confirmation |
| Energy | Energy | 48.59 | mixed | 54.48 | mixed | mixed confirmation |
| Nuclear | Nuclear | 43.24 | weak | 39.28 | weak | broad weakness across sector and themes |
| Utilities | Grid Infrastructure, Nuclear, Dividend Defensives | 32.73 | very weak | 47.37 | mixed | mixed confirmation |

## Three-Month Outperformance Setup

| Rank | Theme | Score | Classification | Drivers | Invalidation Triggers |
| --- | --- | --- | --- | --- | --- |
| 1 | Financials | 67.18 | Positive setup | relative_strength_60d, trend_persistence, breadth, downside_volatility, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 2 | Healthcare Innovation | 66.66 | Positive setup | relative_strength_60d, trend_persistence, breadth, volume_accumulation, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 3 | Small Caps | 63.93 | Positive setup | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 4 | Quality Growth | 63.73 | Positive setup | trend_persistence, breadth | relative strength below SPY, breadth below 45%, news turns negative |
| 5 | Energy | 60.28 | Positive setup | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 6 | AI Infrastructure | 59.54 | Neutral / watchlist | trend_persistence, breadth | relative strength below SPY, breadth below 45%, news turns negative |
| 7 | Cybersecurity | 59.4 | Neutral / watchlist | relative_strength_60d, trend_persistence, breadth, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 8 | Defense | 59.16 | Neutral / watchlist | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 9 | Dividend Defensives | 55.83 | Neutral / watchlist | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 10 | Semiconductors | 51.87 | Neutral / watchlist | trend_persistence, breadth | relative strength below SPY, breadth below 45%, news turns negative |
| 11 | Grid Infrastructure | 51.7 | Neutral / watchlist | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 12 | Nuclear | 34.76 | Weak setup |  | relative strength below SPY, breadth below 45%, news turns negative |

## Breadth and Participation

- Above 50DMA: `76.67%`
- Above 200DMA: `72.88%`
- Positive 20D return: `76.67%`

## Volatility and Risk Signals

- VIX close=15.96 pct_chg=0.95

## News Analytics

- Sentiment counts: {'positive': 62, 'negative': 18, 'neutral': 0}
- News confirmation score: `77.5`

### Top Market-Moving Headlines

**1. We're exiting our position in a spin-off play gone wrong**
- Source: CNBC Markets
- Importance / impact: Medium / Negative
- Relevance / horizon: sector_theme / short-term
- Affected assets: divestment, earnings_report
- Score: `54.51`
- Investment implication: Theme or sector negative signal; requires price and volume confirmation before affecting rankings.

**2. CNBC Daily Open: A super Thursday of earnings and hopes for Iran detente**
- Source: CNBC Technology
- Importance / impact: High / Positive
- Relevance / horizon: macro / short-term
- Affected assets: A, CNBC, U.S, earnings report, geopolitical
- Score: `54.0`
- Investment implication: Macro-relevant positive signal; use as context for rates, volatility, and index confirmation over the short-term.

**3. Sandisk is falling after earnings. Here’s what Wall Street says.**
- Source: MarketWatch Top Stories
- Importance / impact: Medium / Negative
- Relevance / horizon: single_name / short-term
- Affected assets: Sandisk, NAND, technology, earnings
- Score: `49.73`
- Investment implication: Single-name negative signal; low weight unless it maps to a broader sector or theme.

**4. E.l.f. Beauty sees $50 million windfall in tariff refunds as profits surge 100%**
- Source: CNBC Investing
- Importance / impact: High / Positive
- Relevance / horizon: macro / short-term
- Affected assets: E, profit_growth, tariff
- Score: `48.77`
- Investment implication: Macro-relevant positive signal; use as context for rates, volatility, and index confirmation over the short-term.

**5. Block slashed 40% of its workforce for AI — and its earnings suggest that’s paying off**
- Source: MarketWatch Top Stories
- Importance / impact: Medium / Positive
- Relevance / horizon: sector_theme / short-term
- Affected assets: AI, workforce reduction
- Score: `43.35`
- Investment implication: Theme or sector positive signal; requires price and volume confirmation before affecting rankings.

**6. SoftBank earnings exceed expectations, even without an OpenAI boost. This U.S. chip company saved the day.**
- Source: MarketWatch Top Stories
- Importance / impact: Medium / Positive
- Relevance / horizon: single_name / short-term
- Affected assets: INTC, U.S, technology, investment
- Score: `39.0`
- Investment implication: Single-name positive signal; low weight unless it maps to a broader sector or theme.

**7. Lilly’s revenue soars 48%, driven by demand for its GLP-1s**
- Source: MarketWatch Top Stories
- Importance / impact: Medium / Positive
- Relevance / horizon: single_name / short-term
- Affected assets: LLY, GLP, pharmaceuticals, diabetes, weight loss
- Score: `37.29`
- Investment implication: Single-name positive signal; low weight unless it maps to a broader sector or theme.

**8. SoftBank gets $8.2 billion boost from Intel as OpenAI takes a backseat**
- Source: CNBC Investing
- Importance / impact: Medium / Positive
- Relevance / horizon: single_name / short-term
- Affected assets: SOFTBANKG, profit, investment, technology
- Score: `37.29`
- Investment implication: Single-name positive signal; low weight unless it maps to a broader sector or theme.

**9. This drug researcher just reported earnings and could rally on biotech bounceback, JPMorgan says**
- Source: CNBC Markets
- Importance / impact: Medium / Positive
- Relevance / horizon: single_name / short-term
- Affected assets: A, biotech
- Score: `37.05`
- Investment implication: Single-name positive signal; low weight unless it maps to a broader sector or theme.

**10. Siemens Shares Fall as Digital Industries Order Growth Misses Expectations**
- Source: Dow Jones US Business
- Importance / impact: Medium / Positive
- Relevance / horizon: single_name / short-term
- Affected assets: SI, infrastructure, data center
- Score: `35.98`
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
- Equity risk flow: `47.1`
- Credit risk flow: `59.5`
- Sector cyclicality flow: `46.5`
- Duration/liquidity flow: `45.6`
- Alternatives: `defensive or uncertainty hedge`
- ETF flow reliability: `71.7 / 100`
- Dominant allocation direction: `mixed allocation`

### Core Flow Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVV | U.S. Broad Equity | -0.7 | 0.5 | 0.4 | -0.6 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Medium-term deterioration | 83.0 |
| ACWI | Global Equity | -2.0 | -1.4 | 0.0 | -0.6 | Up | Sell | Normal | Profit Taking | Slightly Bearish | Strong confirmation; Persistent selling | 87.0 |
| EFA | Developed Markets ex-U.S. | -0.5 | -0.1 | 0.0 | -1.1 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Medium-term deterioration; Persistent selling | 75.0 |
| IEMG | Emerging Markets | 0.0 | -0.3 | 0.1 | -0.3 | Flat | Buy | Normal | Quiet Accumulation | Improving | Strong confirmation; Exceptional institutional buying, Persistent selling | 95.0 |
| IJH | U.S. Mid Cap | 0.4 | 0.7 | 0.7 | -0.7 | Up | Buy | Normal | Steady Accumulation | Risk-On | Strong confirmation | 95.0 |
| IWM | U.S. Small Cap | -0.7 | 0.0 | 0.5 | -1.2 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural distribution | 79.0 |
| LQD | Investment-Grade Credit | -1.0 | 0.9 | 0.3 | -0.5 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Medium-term deterioration | 83.0 |
| HYG | High-Yield Credit | 0.7 | 1.5 | 0.5 | -0.9 | Flat | Buy | Normal | Quiet Accumulation | Improving | Strong confirmation; Exceptional institutional buying | 100.0 |
| SGOV | Treasury Bills / Cash | -0.7 | -0.9 | 0.9 | -0.0 | Flat | Neutral | Normal | Neutral | Neutral | Structural accumulation; Strong sponsorship | 99.0 |
| SHY | Short-Duration Treasuries | -1.1 | -0.4 | 0.2 | 1.6 | Flat | Neutral | High | High-Turnover Consolidation | Transition | Medium-term deterioration; Persistent selling | 75.0 |
| IEF | Intermediate-Duration Treasuries | 0.1 | -0.2 | 0.6 | -0.3 | Flat | Neutral | Normal | Neutral | Neutral | Structural accumulation | 91.0 |
| TLT | Long-Duration Treasuries | 0.5 | 0.5 | 0.7 | 0.4 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Medium-term recovery | 87.0 |
| GLD | Gold | 1.6 | 1.7 | 0.5 | 2.8 | Up | Buy | High | Confirmed Accumulation | Strong Risk-On | Strong confirmation; Exceptional institutional buying | 100.0 |
| IBIT | Bitcoin | 0.5 | -1.5 | 0.7 | -0.6 | Up | Buy | Normal | Steady Accumulation | Risk-On | Medium-term recovery | 87.0 |

### Sector Flow Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| XLC | Communication Services | -0.7 | -1.0 | 0.3 | -0.3 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural distribution | 79.0 |
| XLY | Consumer Discretionary | 1.2 | 3.1 | 0.6 | -0.9 | Up | Buy | Normal | Steady Accumulation | Risk-On | Strong confirmation; Exceptional institutional buying | 100.0 |
| XLP | Consumer Staples | 0.6 | 1.7 | 0.4 | -1.3 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural accumulation | 91.0 |
| XLE | Energy | -0.6 | -1.3 | 0.3 | -0.1 | Flat | Neutral | Normal | Neutral | Neutral | Structural distribution | 79.0 |
| XLF | Financials | 1.3 | 2.8 | 0.5 | -0.2 | Up | Buy | Normal | Steady Accumulation | Risk-On | Strong confirmation; Exceptional institutional buying | 100.0 |
| XLV | Health Care | 1.1 | 1.7 | 0.6 | 1.6 | Up | Buy | High | Confirmed Accumulation | Strong Risk-On | Strong confirmation | 95.0 |
| XLI | Industrials | -0.1 | 1.3 | 0.6 | -1.2 | Up | Buy | Normal | Steady Accumulation | Risk-On | Strong confirmation; Exceptional institutional buying | 100.0 |
| XLK | Information Technology | 0.4 | -0.7 | 0.7 | -1.1 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural accumulation | 91.0 |
| XLB | Materials | -0.9 | -0.3 | 0.4 | 0.1 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural accumulation | 91.0 |
| XLRE | Real Estate | 0.6 | 1.6 | 0.6 | 0.6 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural accumulation | 91.0 |
| XLU | Utilities | -0.2 | 0.6 | 0.3 | 1.2 | Down | Neutral | High | Heavy Selling Pressure | Cautious | Medium-term deterioration | 83.0 |

### Subsector PFV Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ITA | Aerospace and Defense | 0.1 | -0.0 | 0.3 | -0.1 | Up | Buy | Normal | Steady Accumulation | Risk-On | Tactical rebound inside structural distribution | 83.0 |
| SOXX | Semiconductors | 1.5 | 1.2 | 0.5 | -0.2 | Down | Sell | Normal | Persistent Distribution | Risk-Off | Tactical profit-taking inside structural accumulation | 83.0 |
| SMH | Semiconductors | 0.2 | 1.0 | 0.5 | -1.1 | Flat | Neutral | Low | Dormant Market | Neutral | Structural accumulation | 91.0 |
| CIBR | Cybersecurity | 0.7 | 1.3 | 0.6 | 0.2 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural accumulation | 91.0 |

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
- Live macro rows used: `26`
- Economic rows loaded: `113`
- News rows loaded: `80`
- Positioning/flow rows loaded: `30`

# Rule-Based Institutional Market Update

Generated at: 13 August 2026, 03:13:33 (HKT)
Window: 24h

## Executive Dashboard

- Regime score: **64.84 / 100** (Mild Risk-On)
- US equity strength: **80.6 / 100** (strong)
- Evidence quality: **76.0 / 100**
- ETF flow contribution: **48.94 / 100**, reliability **71.51 / 100**
- Breadth: **broad**; above 50DMA `73.33%`, above 200DMA `74.58%`
- Top sector score: **Healthcare** `68.69`
- Top theme score: **Energy** `62.71`

## Market Regime Score

| Metric | Value | Driver / Interpretation |
| --- | --- | --- |
| Overall regime | 64.84 | Mild Risk-On |
| equity_trend | 93.75 | risk-on support; Core equity ETFs versus moving averages. |
| equity_momentum | 50.57 | neutral / mixed; 5D/20D/60D return momentum across SPY, QQQ, IWM, and SMH. |
| market_breadth | 73.75 | risk-on support; Participation breadth from tracked equity/ETF rows. |
| volatility | 80.0 | risk-on support; VIX level and change; higher score means calmer volatility conditions. |
| rates_yield_curve | 58.0 | mild risk-on support; Treasury yield pressure and curve shape; higher score means less rates pressure. |
| credit_proxy | 50.0 | neutral / mixed; Credit-market proxy; currently neutral when no direct spread signal is available. |
| dollar_fx | 54.13 | neutral / mixed; Dollar move; higher score means less USD tightening pressure. |
| commodity_confirmation | 51.0 | neutral / mixed; Copper, silver, oil, and gold mix; higher score means better cyclical confirmation. |
| etf_flow | 49.24 | neutral / mixed; Grouped ETF flow contribution adjusted for reliability. |
| news_confirmation | 50.0 | neutral / mixed; Weighted headline/news confirmation score. |
| Positive contributors |  | equity_trend=93.75, volatility=80.0, market_breadth=73.75 |
| Negative contributors |  | none |

## US Equity Strength Score

| Component | Score |
| --- | --- |
| indices_above_moving_averages | 93.75 |
| sp500_trend | 100.0 |
| nasdaq_trend | 100.0 |
| russell_participation | 100.0 |
| returns_momentum | 50.57 |
| rsi_zone | 63.75 |
| macd_confirmation | 70.0 |
| volume_confirmation | 50.0 |
| breadth | 73.75 |

## Evidence Quality / Confidence

- Confidence score: `76.0`
- Agreement ratio: `0.4`
- Contradiction count: `0`
- Missing indicators: none
- Warning flags: none

## Cross-Asset Confirmation

| Area | Signal | Interpretation |
| --- | --- | --- |
| Equities | S&P 500 rising; Nasdaq rising; Russell 2000 rising | Confirms risk appetite when broad indices rise together; weak small caps would narrow the signal. |
| Rates | 10Y Treasury stable; MOVE rising | Rising yields can pressure duration assets; falling MOVE supports calmer bond volatility. |
| Dollar | DXY proxy stable | A stronger dollar can tighten financial conditions and pressure commodities/emerging-market risk. |
| Credit | HYG stable | High-yield weakness would challenge equity risk-on confirmation. |
| Gold | Gold rising | Gold strength can indicate defensive demand, inflation hedging, or geopolitical concern. |
| Silver | Silver rising | Silver helps distinguish precious-metal demand from industrial/cyclical confirmation when data is available. |
| Copper | Copper stable | Copper strength supports cyclical growth confirmation; weakness would dilute risk-on breadth. |
| Oil | WTI crude stable | Oil spikes can be inflationary risk; falling oil can ease cost pressure but may also flag demand softness. |
| Volatility | VIX falling | Falling VIX supports risk appetite; a volatility spike would reduce confidence in broad risk-on. |

### Macro Snapshot

Live macro rows are intraday snapshots from `public.macro_live`; closed rows are official stored rows from `public.macro`.

| Symbol | Name | Close | Pct Chg | Market Date | Status |
| --- | --- | --- | --- | --- | --- |
| ^GSPC | S&P 500 | 7755.52 | 0.35 | 2026-08-12 | live as of 13 August 2026, 03:00:32 (HKT) |
| ^IXIC | NASDAQ Composite | 26625.7 | 0.68 | 2026-08-12 | live as of 13 August 2026, 03:00:32 (HKT) |
| ^RUT | Russell 2000 Index | 3046.98 | 0.66 | 2026-08-12 | live as of 13 August 2026, 03:00:32 (HKT) |
| ^VIX | CBOE Volatility Index | 14.52 | -4.97 | 2026-08-12 | live as of 13 August 2026, 03:00:32 (HKT) |
| ^SKEW | CBOE SKEW Index | 135.59 | -1.12 | 2026-08-11 | closed |
| ^MOVE | ICE BofA MOVE Index | 76.82 | 8.38 | 2026-07-24 | closed |
| US2YT=X | United States 2-Year Treasury Yield | 4.2 | -0.45 | 2026-08-12 | live as of 13 August 2026, 03:00:32 (HKT) |
| US3YT=X | United States 3-Year Treasury Yield | 4.27 | -0.33 | 2026-08-12 | live as of 13 August 2026, 03:00:32 (HKT) |
| US5YT=X | United States 5-Year Treasury Yield | 4.37 | -0.24 | 2026-08-12 | live as of 13 August 2026, 03:00:32 (HKT) |
| US7YT=X | United States 7-Year Treasury Yield | 4.52 | -0.17 | 2026-08-12 | live as of 13 August 2026, 03:00:32 (HKT) |
| US10YT=X | United States 10-Year Treasury Yield | 4.68 | -0.06 | 2026-08-12 | live as of 13 August 2026, 03:00:32 (HKT) |
| US20YT=X | United States 20-Year Treasury Yield | 5.25 | 0.08 | 2026-08-12 | live as of 13 August 2026, 03:00:32 (HKT) |
| US30YT=X | United States 30-Year Treasury Yield | 5.25 | 0.22 | 2026-08-12 | live as of 13 August 2026, 03:00:32 (HKT) |
| HK50 | Hang Seng Futures | 25412.0 | -0.52 | 2026-08-12 | closed |
| KOR200c1 | KOSPI 200 Futures | 1012.1 | 2.25 | 2026-08-11 | closed |
| CIHc1 | SSE 50 Futures | 2927.4 | -0.91 | 2026-08-11 | closed |
| HYG | iShares iBoxx High Yield Corporate Bond ETF | 79.62 | 0.14 | 2026-08-12 | live as of 13 August 2026, 03:00:32 (HKT) |
| LQD | iShares iBoxx Investment Grade Corporate Bond ETF | 106.12 | 0.13 | 2026-08-12 | live as of 13 August 2026, 03:00:32 (HKT) |
| JNK | SPDR Bloomberg High Yield Bond ETF | 95.87 | 0.19 | 2026-08-12 | live as of 13 August 2026, 03:00:32 (HKT) |
| RSP | Invesco S&P 500 Equal Weight ETF | 221.16 | 0.21 | 2026-08-12 | live as of 13 August 2026, 03:00:32 (HKT) |
| IWF | iShares Russell 1000 Growth ETF | 124.64 | 0.84 | 2026-08-12 | live as of 13 August 2026, 03:00:32 (HKT) |
| IWD | iShares Russell 1000 Value ETF | 257.9 | -0.01 | 2026-08-12 | live as of 13 August 2026, 03:00:32 (HKT) |
| TLT | iShares 20+ Year Treasury Bond ETF | 82.12 | -0.08 | 2026-08-12 | live as of 13 August 2026, 03:00:32 (HKT) |
| IEF | iShares 7-10 Year Treasury Bond ETF | 92.97 | 0.11 | 2026-08-12 | live as of 13 August 2026, 03:00:32 (HKT) |
| SHY | iShares 1-3 Year Treasury Bond ETF | 81.93 | 0.07 | 2026-08-12 | live as of 13 August 2026, 03:00:32 (HKT) |
| GC=F | Gold Future | 4475.8 | 2.12 | 2026-08-12 | live as of 13 August 2026, 03:00:32 (HKT) |
| SI=F | Silver Future | 65.75 | 1.51 | 2026-08-12 | live as of 13 August 2026, 03:00:32 (HKT) |
| CL=F | WTI Crude Oil Future | 83.18 | -0.02 | 2026-08-12 | live as of 13 August 2026, 03:00:32 (HKT) |
| HG=F | Copper Future | 6.62 | 0.07 | 2026-08-12 | live as of 13 August 2026, 03:00:32 (HKT) |

## Market Dispersion Analysis

- Sector ETF 20D dispersion: `11.5` points (moderate); leader `XLE` (Energy) `6.99`, laggard `XLU` (Utilities) `-4.51`
- Sector ETF 60D dispersion: `19.57` points (high); leader `XLV` (Health Care) `14.58`, laggard `XLC` (Communication Services) `-4.99`

| Comparison | Left | Right | 20D Spread | Signal |
| --- | --- | --- | --- | --- |
| Equal-weight vs cap-weight | RSP (Equal-weight S&P 500) | SPY (S&P 500) | 0.9 | balanced |
| Small-cap vs large-cap | IWM (Russell 2000) | SPY (S&P 500) | -0.29 | balanced |
| Growth vs value | IWF (Russell 1000 Growth) | IWD (Russell 1000 Value) | -4.39 | value leadership |
| Nasdaq vs S&P 500 | QQQ (Nasdaq 100) | SPY (S&P 500) | -2.66 | S&P 500 leadership |

## Sector Constituent Dispersion

- Breadth 50D / 200D: percentage of active S&P 500 constituents in the sector trading above the 50-day / 200-day moving average.
- Positive 20D: percentage of active sector constituents with positive 20-day return.
- Std 20D: cross-sectional standard deviation of constituent 20-day returns; higher means wider stock-level dispersion.

| Sector | Count | Breadth 50D | Breadth 200D | Positive 20D | 20D Dispersion | Std 20D | Label | Leaders | Laggards |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Information Technology | 73 | 53.42 | 70.83 | 57.53 | 74.96 | 15.19 | very high | ZBRA, IT, CTSH | NXPI, WDC, SNDK |
| Consumer Staples | 34 | 57.58 | 56.25 | 58.82 | 67.79 | 10.56 | very high | CLX, TGT, EL | BG, MO, MNST |
| Industrials | 83 | 69.51 | 75.95 | 66.27 | 59.52 | 9.97 | very high | LDOS, ALLE, EMR | HONA, LII, CHRW |
| Communication Services | 23 | 68.18 | 40.91 | 65.22 | 52.3 | 12.03 | very high | CHTR, T, FOXA | META, TTD, APP |
| Health Care | 59 | 83.05 | 83.05 | 79.66 | 49.92 | 10.24 | very high | BAX, ABT, VEEV | MRNA, CVS, DVA |
| Consumer Discretionary | 47 | 63.83 | 55.32 | 74.47 | 44.27 | 10.46 | very high | GRMN, ABNB, HAS | CMG, APTV, TSLA |
| Financials | 76 | 82.19 | 87.14 | 68.42 | 41.36 | 7.14 | very high | PYPL, ARES, WTW | MSCI, GS, HOOD |
| Materials | 25 | 72.0 | 80.0 | 76.0 | 33.94 | 8.21 | very high | NEM, NUE, SW | MLM, LIN, CTVA |
| Energy | 21 | 76.19 | 80.95 | 71.43 | 29.89 | 7.62 | very high | APA, SLB, COP | WMB, TRGP, TPL |
| Utilities | 31 | 9.68 | 35.48 | 6.45 | 21.97 | 4.12 | very high | CEG, AWK, AES | NI, LNT, NRG |
| Real Estate | 31 | 22.58 | 77.42 | 29.03 | 19.27 | 4.95 | high | CSGP, CBRE, DLR | VTR, UDR, CCI |

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
| Headline CPI month-over-month inflation rate | 0.07 | percent | 0.5 pp vs prior | 2026-07-01 | Higher reading increases macro pressure. |
| Headline CPI year-over-year inflation rate | 3.54 | percent | -0.19 pp vs prior | 2026-07-01 | Lower reading eases macro pressure. |
| Core CPI month-over-month inflation rate | 0.22 | percent | 0.23 pp vs prior | 2026-07-01 | Higher reading increases macro pressure. |
| Core CPI year-over-year inflation rate | 2.79 | percent | -0.02 pp vs prior | 2026-07-01 | Lower reading eases macro pressure. |
| Headline CPI year-over-year inflation rate | 3.52 | percent | -0.36 pp vs prior | 2026-07-01 | Lower reading eases macro pressure. |
| Core CPI year-over-year inflation rate | 2.67 | percent | -0.19 pp vs prior | 2026-07-01 | Lower reading eases macro pressure. |
| Headline PCE Price Index month-over-month inflation rate | -0.11 | percent | -0.57 pp vs prior | 2026-06-01 | Lower reading eases macro pressure. |
| Headline PCE Price Index year-over-year inflation rate | 3.67 | percent | -0.41 pp vs prior | 2026-06-01 | Lower reading eases macro pressure. |
| Core PCE Price Index month-over-month inflation rate | 0.13 | percent | -0.2 pp vs prior | 2026-06-01 | Lower reading eases macro pressure. |
| Core PCE Price Index year-over-year inflation rate | 3.29 | percent | -0.14 pp vs prior | 2026-06-01 | Lower reading eases macro pressure. |
| Headline PPI Final Demand month-over-month inflation rate | -0.19 | percent | -0.79 pp vs prior | 2026-06-01 | Lower reading eases macro pressure. |
| Headline PPI Final Demand year-over-year inflation rate | 5.51 | percent | -0.49 pp vs prior | 2026-06-01 | Lower reading eases macro pressure. |
| Core PPI Final Demand Less Foods and Energy month-over-month inflation rate | 0.2 | percent | 0.11 pp vs prior | 2026-06-01 | Higher reading increases macro pressure. |
| Core PPI Final Demand Less Foods and Energy year-over-year inflation rate | 4.68 | percent | 0.09 pp vs prior | 2026-06-01 | Higher reading increases macro pressure. |
| Consumer Price Index for All Urban Consumers | 332.81 | index 1982-1984=100 | 0.25 index pts vs prior | 2026-07-01 | Higher reading increases macro pressure. |
| Core CPI | 336.79 | index 1982-1984=100 | 0.72 index pts vs prior | 2026-07-01 | Higher reading increases macro pressure. |
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
| US dollar/Euro ECB reference exchange rate | 1.15 | USD | 0.0 USD vs prior | 2026-08-12 | EUR strengthened versus this currency. |
| Japanese yen/Euro ECB reference exchange rate | 183.67 | JPY | -0.05 JPY vs prior | 2026-08-12 | EUR weakened versus this currency. |
| Chinese yuan renminbi/Euro ECB reference exchange rate | 7.79 | CNY | 0.0 CNY vs prior | 2026-08-12 | EUR strengthened versus this currency. |
| Australian dollar/Euro ECB reference exchange rate | 1.63 | AUD | -0.0 AUD vs prior | 2026-08-12 | EUR weakened versus this currency. |

ABS Australia note: ABS rows are stored locally/Neon, but most series are dimension-coded; only curated series should be promoted into narrative report text.

## Sector and Theme Leadership

### Official Sector Strength

Supporting and detracting names are the top/bottom S&P 500 constituents by 20D return when constituent coverage is available; otherwise the report falls back to related ETFs.

| Rank | Sector | Score | Trend | Momentum | Stock Breadth | ETF Flow | Flow Reliability | 3M RS | Supporting / Leaders | Detracting / Laggards |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Healthcare | 68.69 | strong uptrend | positive | broad | 67.2 | 100.0 | 56.82 | BAX, ABT, VEEV | MRNA, CVS, DVA |
| 2 | Energy | 67.91 | strong uptrend | neutral | broad | 60.14 | 100.0 | 53.47 | APA, SLB, COP | WMB, TRGP, TPL |
| 3 | Cybersecurity | 67.54 | strong uptrend | positive | broad | 58.47 | 65.0 | 61.6 | CIBR | CIBR |
| 4 | Defense | 66.71 | strong uptrend | positive | broad | 49.32 | 65.0 | 56.2 | XAR | XAR |
| 5 | Industrials | 66.45 | strong uptrend | neutral | broad | 54.02 | 65.0 | 51.62 | LDOS, ALLE, EMR | HONA, LII, CHRW |
| 6 | Grid Infrastructure | 65.6 | strong uptrend | neutral | broad | 61.61 | 65.0 | 46.51 | GRID | GRID |
| 7 | Technology | 65.39 | strong uptrend | neutral | broad | 54.4 | 95.0 | 48.36 | ZBRA, IT, CTSH | NXPI, WDC, SNDK |
| 8 | Financials | 64.37 | strong uptrend | positive | broad | 61.11 | 95.0 | 54.12 | PYPL, ARES, WTW | MSCI, GS, HOOD |
| 9 | Consumer Discretionary | 60.17 | uptrend | neutral | broad | 61.76 | 65.0 | 49.23 | GRMN, ABNB, HAS | CMG, APTV, TSLA |
| 10 | Consumer Staples | 59.97 | strong uptrend | neutral | broad | 64.53 | 65.0 | 48.09 | CLX, TGT, EL | BG, MO, MNST |
| 11 | Nuclear | 54.77 | neutral | neutral | broad | 50.0 | 0.0 | 46.93 | NLR | NLR |
| 12 | Crypto | 51.84 | neutral | neutral | mixed | 68.43 | 65.0 | 50.0 |  |  |
| 13 | Semiconductors | 51.25 | strong uptrend | neutral | weak | 50.0 | 0.0 | 44.13 | SMH, SOXX | SOXX, SMH |
| 14 | Real Estate | 47.26 | neutral | neutral | weak | 65.14 | 100.0 | 46.92 | CSGP, CBRE, DLR | VTR, UDR, CCI |
| 15 | Utilities | 34.33 | strong downtrend | neutral | weak | 53.06 | 65.0 | 42.84 | CEG, AWK, AES | NI, LNT, NRG |

### Thematic Strength

| Rank | Theme | Score | Setup | ETF Flow | Flow Reliability | Dispersion | Price | News |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Energy | 62.71 | Positive setup | 60.14 | 100.0 | 3.15 | True | False |
| 2 | Defense | 60.8 | Positive setup | 49.32 | 65.0 | 27.73 | True | False |
| 3 | Healthcare Innovation | 60.39 | Positive setup | 67.2 | 100.0 | 13.39 | True | False |
| 4 | Small Caps | 59.74 | Positive setup | 48.47 | 65.0 | 0.0 | False | False |
| 5 | Financials | 58.6 | Positive setup | 61.11 | 95.0 | 14.85 | False | False |
| 6 | Cybersecurity | 58.08 | Neutral / watchlist | 58.47 | 65.0 | 20.36 | False | False |
| 7 | Quality Growth | 55.47 | Neutral / watchlist | 56.96 | 65.0 | 35.25 | False | False |
| 8 | AI Infrastructure | 54.95 | Neutral / watchlist | 50.0 | 0.0 | 36.82 | False | False |
| 9 | Semiconductors | 51.44 | Neutral / watchlist | 50.0 | 0.0 | 20.4 | False | False |
| 10 | Dividend Defensives | 51.12 | Neutral / watchlist | 57.57 | 65.0 | 10.65 | False | False |
| 11 | Nuclear | 48.38 | Neutral / watchlist | 50.0 | 0.0 | 11.69 | False | False |
| 12 | Grid Infrastructure | 47.96 | Neutral / watchlist | 61.61 | 65.0 | 16.79 | False | False |
| 13 | Crypto Infrastructure | 30.81 | Underperformance risk | 68.43 | 65.0 | 6.47 | False | False |

- Top 5 improving themes: Financials, Cybersecurity, Defense, Healthcare Innovation, Small Caps
- Top 5 deteriorating themes: Crypto Infrastructure, Nuclear, Grid Infrastructure, AI Infrastructure, Semiconductors
- Strong news but weak price confirmation: none
- Strong price but weak news confirmation: Energy, Defense, Healthcare Innovation

### Sector / Theme Alignment

| Sector | Related Themes | Sector Score | Sector Signal | Theme Score | Theme Signal | Interpretation |
| --- | --- | --- | --- | --- | --- | --- |
| Healthcare | Healthcare Innovation | 68.69 | strong | 60.39 | positive | sector and theme confirmation |
| Energy | Energy | 67.91 | strong | 62.71 | positive | sector and theme confirmation |
| Cybersecurity | Cybersecurity | 67.54 | strong | 58.08 | positive | sector and theme confirmation |
| Defense | Defense | 66.71 | strong | 60.8 | positive | sector and theme confirmation |
| Industrials | Defense, Grid Infrastructure | 66.45 | strong | 54.38 | mixed | sector stronger than related themes |
| Grid Infrastructure | Grid Infrastructure | 65.6 | strong | 47.96 | mixed | sector stronger than related themes |
| Technology | AI Infrastructure, Semiconductors, Quality Growth | 65.39 | strong | 53.95 | mixed | sector stronger than related themes |
| Financials | Financials | 64.37 | positive | 58.6 | positive | sector and theme confirmation |
| Consumer Discretionary | Small Caps | 60.17 | positive | 59.74 | positive | sector and theme confirmation |
| Consumer Staples | Dividend Defensives | 59.97 | positive | 51.12 | mixed | sector stronger than related themes |
| Nuclear | Nuclear | 54.77 | mixed | 48.38 | mixed | mixed confirmation |
| Crypto | Crypto Infrastructure | 51.84 | mixed | 30.81 | very weak | mixed confirmation |
| Semiconductors | AI Infrastructure, Semiconductors | 51.25 | mixed | 53.2 | mixed | mixed confirmation |
| Real Estate | Dividend Defensives | 47.26 | mixed | 51.12 | mixed | mixed confirmation |
| Utilities | Grid Infrastructure, Nuclear, Dividend Defensives | 34.33 | very weak | 49.15 | mixed | mixed confirmation |

## Three-Month Outperformance Setup

| Rank | Theme | Score | Classification | Drivers | Invalidation Triggers |
| --- | --- | --- | --- | --- | --- |
| 1 | Small Caps | 64.01 | Positive setup | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 2 | Healthcare Innovation | 63.43 | Positive setup | relative_strength_60d, trend_persistence, breadth, downside_volatility, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 3 | Energy | 63.33 | Positive setup | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 4 | Financials | 62.77 | Positive setup | relative_strength_60d, trend_persistence, breadth, downside_volatility, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 5 | Defense | 62.52 | Positive setup | relative_strength_20d, relative_strength_60d, trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 6 | Cybersecurity | 58.9 | Neutral / watchlist | relative_strength_60d, trend_persistence, breadth, downside_volatility, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 7 | Quality Growth | 57.44 | Neutral / watchlist | trend_persistence, breadth | relative strength below SPY, breadth below 45%, news turns negative |
| 8 | AI Infrastructure | 56.76 | Neutral / watchlist | trend_persistence, breadth | relative strength below SPY, breadth below 45%, news turns negative |
| 9 | Dividend Defensives | 54.88 | Neutral / watchlist | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 10 | Semiconductors | 53.09 | Neutral / watchlist | trend_persistence, breadth | relative strength below SPY, breadth below 45%, news turns negative |
| 11 | Grid Infrastructure | 48.11 | Neutral / watchlist | downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 12 | Nuclear | 47.05 | Neutral / watchlist |  | relative strength below SPY, breadth below 45%, news turns negative |

## Breadth and Participation

- Above 50DMA: `73.33%`
- Above 200DMA: `74.58%`
- Positive 20D return: `73.33%`

## Volatility and Risk Signals

- VIX close=14.52 pct_chg=-4.97

## News Analytics

- Sentiment counts: {'positive': 1, 'negative': 1, 'neutral': 78}
- News confirmation score: `50.0`

### Top Market-Moving Headlines

**1. An active fund holding a whopping 800 stocks is beating major indexes. Here’s how.**
- Source: MarketWatch Top Stories
- Importance / impact: Low / Mixed
- Relevance / horizon: macro / nan
- Affected assets: Equities, Bonds, USD, Commodities
- Score: `25.0`
- Investment implication: Macro-relevant mixed signal; use as context for rates, volatility, and index confirmation over the nan.

**2. Treasurys in turmoil: What rising yields mean for your money**
- Source: MarketWatch Bulletins
- Importance / impact: Low / Mixed
- Relevance / horizon: macro / nan
- Affected assets: Equities, Bonds, USD, Commodities
- Score: `23.75`
- Investment implication: Macro-relevant mixed signal; use as context for rates, volatility, and index confirmation over the nan.

**3. S&P 500 opens in record territory, Dow and Nasdaq climb after CPI data**
- Source: MarketWatch Bulletins
- Importance / impact: Low / Mixed
- Relevance / horizon: macro / nan
- Affected assets: P, S
- Score: `23.75`
- Investment implication: Macro-relevant mixed signal; use as context for rates, volatility, and index confirmation over the nan.

**4. The $30 trillion Treasury market is facing a painful reckoning. How rising yields could squeeze your portfolio.**
- Source: MarketWatch Top Stories
- Importance / impact: Low / Mixed
- Relevance / horizon: macro / nan
- Affected assets: Equities, Bonds, USD, Commodities
- Score: `21.25`
- Investment implication: Macro-relevant mixed signal; use as context for rates, volatility, and index confirmation over the nan.

**5. S&P 500 rises after tame inflation data; AI-related shares jump: Live updates**
- Source: CNBC Top News
- Importance / impact: Low / Mixed
- Relevance / horizon: sector_theme / nan
- Affected assets: P, S
- Score: `20.19`
- Investment implication: Theme or sector mixed signal; requires price and volume confirmation before affecting rankings.

**6. Stocks making the biggest moves midday: Wendy's, H&R Block, Quantinuum, CoreWeave, Cava & more**
- Source: CNBC Top News
- Importance / impact: Low / Mixed
- Relevance / horizon: sector_theme / nan
- Affected assets: H, R
- Score: `20.19`
- Investment implication: Theme or sector mixed signal; requires price and volume confirmation before affecting rankings.

**7. AI capex could hit $1.6 trillion next year, says fund manager who sees more echoes of 1998 than the dot-com bust**
- Source: MarketWatch Top Stories
- Importance / impact: Low / Mixed
- Relevance / horizon: sector_theme / nan
- Affected assets: A, T
- Score: `18.06`
- Investment implication: Theme or sector mixed signal; requires price and volume confirmation before affecting rankings.

**8. ‘I unexpectedly came into some money’: Is putting $20,000 into CDs a smart move?**
- Source: MarketWatch Top Stories
- Importance / impact: Low / Mixed
- Relevance / horizon: single_name / nan
- Affected assets: I
- Score: `16.25`
- Investment implication: Single-name mixed signal; low weight unless it maps to a broader sector or theme.

**9. I found a $100 bill in the communal washer at my Airbnb. What should I do?**
- Source: MarketWatch Top Stories
- Importance / impact: Low / Mixed
- Relevance / horizon: single_name / nan
- Affected assets: I
- Score: `16.25`
- Investment implication: Single-name mixed signal; low weight unless it maps to a broader sector or theme.

**10. Can I claim 50% of my husband’s Social Security now — and switch to my higher benefit at 70?**
- Source: MarketWatch Top Stories
- Importance / impact: Low / Mixed
- Relevance / horizon: single_name / nan
- Affected assets: I
- Score: `16.25`
- Investment implication: Single-name mixed signal; low weight unless it maps to a broader sector or theme.


### Headline Quality Checks

Noisy headline list: Social Security recipients will get more money nex, Amazon shares appear stuck in a rut. Trader Mike K

## Positioning & Flow Dashboard

Positioning and flow data is used as confirmation only. FINRA short-sale volume is not short interest.

### Deferred Flow Sections

- Official ETF / fund flows: current report uses shares-outstanding-derived net fund flow estimates from free ETF metadata.
- Institutional Ownership: not available until SEC 13F ingestion is implemented.
- Crowding / Squeeze Risks: initial coverage uses CFTC crowded positioning and FINRA elevated short-sale volume only.
- Grouped exposure flow reliability: use issuer coverage and availability status before treating ETF flow as confirmation.

## Short Positioning Analytics

FINRA daily short-sale volume measures transaction activity; twice-monthly FINRA short interest measures outstanding positions. Funding-short classifications are behavioral likelihood scores, not proof of hedge-fund identity.

| Date | Ticker | Regime | Confidence | Funding | Position | Activity | Unwind | DTC | 3M Relative |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08-11 | DOW | Neutral Inconclusive | 99.6 | 49.6 | 46.18 | 99.76 | 47.24 | 3.1 | 0.0 |
| 2026-08-11 | ETHA | Structural Funding Short | 75.67 | 75.67 | 69.81 | 99.09 | 34.87 | 1.49 | -0.21 |
| 2026-08-11 | SMDV | Short Covering | 85.0 | 43.12 | 25.0 | 98.81 | 67.84 | 1.0 | 0.07 |
| 2026-08-11 | MARA | New Conviction Short | 58.42 | 80.43 | 75.68 | 98.73 | 23.5 | 2.48 | -0.3 |
| 2026-08-11 | LQDA | Short Pressure Failure | 83.67 | 48.77 | 82.3 | 98.61 | 87.65 | 9.18 | 0.45 |
| 2026-08-11 | CNTX | Neutral Inconclusive | 91.93 | 58.07 | 53.62 | 98.42 | 19.51 | 1.81 | -0.83 |
| 2026-08-11 | BOX | Neutral Inconclusive | 98.12 | 48.12 | 75.55 | 98.3 | 54.04 | 5.81 | 0.33 |
| 2026-08-11 | AEG | Neutral Inconclusive | 99.61 | 50.39 | 60.52 | 98.26 | 47.23 | 1.0 | 0.09 |
| 2026-08-11 | CDLR | Neutral Inconclusive | 98.54 | 51.46 | 63.64 | 97.9 | 46.36 | 8.6 | -0.24 |
| 2026-08-11 | OCC | Neutral Inconclusive | 84.78 | 34.78 | 60.18 | 97.86 | 43.31 | 2.35 | 0.18 |
| 2026-08-11 | ASO | Confirmed Funding Short Unwind | 74.51 | 70.59 | 67.61 | 97.82 | 78.43 | 5.16 | -0.06 |
| 2026-08-11 | NU | Structural Funding Short | 81.31 | 81.31 | 74.72 | 97.71 | 34.29 | 1.54 | 0.03 |
| 2026-08-11 | CHWY | Structural Funding Short | 79.25 | 79.25 | 79.48 | 97.64 | 52.15 | 3.09 | 0.02 |
| 2026-08-11 | CORZW | Neutral Inconclusive | 95.4 | 45.4 | 58.84 | 97.51 | 20.51 | 4.04 | -0.31 |
| 2026-08-11 | BRKL | Neutral Inconclusive | 98.66 | 48.66 | 27.67 | 97.21 | 38.51 | 1.0 | n/a |
| 2026-08-11 | B | Neutral Inconclusive | 94.43 | 55.57 | 64.11 | 97.15 | 51.99 | 2.04 | -0.1 |
| 2026-08-11 | PRM | Short Covering | 79.23 | 49.05 | 74.08 | 97.07 | 80.9 | 3.85 | -0.01 |
| 2026-08-11 | IMCG | Neutral Inconclusive | 88.27 | 38.27 | 39.42 | 97.0 | 42.94 | 1.0 | 0.06 |
| 2026-08-11 | LITS | Short Covering | 85.0 | 46.47 | 30.99 | 96.95 | 47.2 | 1.0 | -0.29 |
| 2026-08-11 | KJUL | Neutral Inconclusive | 86.76 | 36.76 | 54.09 | 96.9 | 42.8 | 6.28 | -0.01 |

- Potential funding-short unwind: none
- Confirmed funding-short unwind: ASO
- Short-pressure failure: LQDA, AUGO, KFY

## ETF Flows Analysis

- Market flow regime: `Mixed / Neutral`
- Market flow score: `50.6 / 100`
- Equity risk flow: `48.2`
- Credit risk flow: `64.6`
- Sector cyclicality flow: `45.3`
- Duration/liquidity flow: `43.2`
- Alternatives: `mixed alternative-asset demand`
- ETF flow reliability: `71.5 / 100`
- Dominant allocation direction: `defensive demand`

### Core Flow Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVV | U.S. Broad Equity | -0.7 | 0.3 | 0.3 | -0.4 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Medium-term deterioration | 83.0 |
| ACWI | Global Equity | -1.8 | -1.3 | 0.0 | -1.1 | Up | Sell | Normal | Profit Taking | Slightly Bearish | Strong confirmation; Persistent selling | 87.0 |
| EFA | Developed Markets ex-U.S. | -0.5 | -0.1 | 0.0 | -1.7 | Up | Neutral | Low | Fragile Rally | Low Confidence | Medium-term deterioration; Persistent selling | 75.0 |
| IEMG | Emerging Markets | 0.2 | -0.1 | 0.2 | -0.5 | Flat | Buy | Normal | Quiet Accumulation | Improving | Strong confirmation; Exceptional institutional buying, Persistent selling | 95.0 |
| IJH | U.S. Mid Cap | 0.8 | 1.0 | 0.8 | -1.3 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural accumulation; Strong sponsorship | 99.0 |
| IWM | U.S. Small Cap | -0.9 | 0.6 | 0.4 | -1.5 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural distribution | 79.0 |
| LQD | Investment-Grade Credit | -1.1 | 0.9 | 0.4 | -0.5 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Medium-term deterioration | 83.0 |
| HYG | High-Yield Credit | 2.0 | 1.4 | 0.6 | -1.6 | Flat | Buy | Low | Early Accumulation | Watch | Strong confirmation | 95.0 |
| SGOV | Treasury Bills / Cash | -0.6 | -1.0 | 0.9 | -1.0 | Flat | Neutral | Normal | Neutral | Neutral | Medium-term recovery; Strong sponsorship | 95.0 |
| SHY | Short-Duration Treasuries | -0.8 | -0.1 | 0.3 | -0.7 | Flat | Neutral | Normal | Neutral | Neutral | Medium-term deterioration | 83.0 |
| IEF | Intermediate-Duration Treasuries | -4.2 | -2.5 | 0.6 | -0.4 | Flat | Sell | Normal | Quiet Distribution | Weakening | Strong confirmation; Exceptional institutional selling | 87.0 |
| TLT | Long-Duration Treasuries | 1.7 | 2.4 | 0.6 | -0.4 | Down | Buy | Normal | Contrarian Buying | Watch | Strong confirmation; Exceptional institutional buying | 100.0 |
| GLD | Gold | 2.0 | 1.7 | 0.6 | 0.0 | Up | Buy | Normal | Steady Accumulation | Risk-On | Strong confirmation; Exceptional institutional buying | 100.0 |
| IBIT | Bitcoin | 0.8 | -1.3 | 0.7 | -0.8 | Down | Buy | Normal | Contrarian Buying | Watch | Medium-term recovery | 87.0 |

### Sector Flow Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| XLC | Communication Services | -0.1 | -1.0 | 0.3 | -1.4 | Flat | Buy | Normal | Quiet Accumulation | Improving | Tactical rebound inside structural distribution | 83.0 |
| XLY | Consumer Discretionary | 0.9 | 2.1 | 0.6 | -1.8 | Up | Neutral | Low | Fragile Rally | Low Confidence | Structural accumulation; Exceptional institutional buying | 99.0 |
| XLP | Consumer Staples | 0.8 | 1.2 | 0.5 | -1.3 | Flat | Neutral | Normal | Neutral | Neutral | Structural accumulation | 91.0 |
| XLE | Energy | -0.3 | -0.9 | 0.5 | -1.3 | Up | Buy | Normal | Steady Accumulation | Risk-On | Tactical rebound inside structural distribution | 83.0 |
| XLF | Financials | 1.3 | 2.2 | 0.5 | -1.8 | Up | Buy | Low | Quiet Accumulation | Mild Risk-On | Strong confirmation; Exceptional institutional buying | 100.0 |
| XLV | Health Care | 1.2 | 1.6 | 0.6 | -1.3 | Up | Buy | Normal | Steady Accumulation | Risk-On | Strong confirmation | 95.0 |
| XLI | Industrials | -0.4 | 1.1 | 0.5 | -1.4 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural accumulation | 91.0 |
| XLK | Information Technology | 0.1 | -0.8 | 0.6 | -1.3 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Mixed or neutral flow structure | 85.0 |
| XLB | Materials | -0.9 | 0.0 | 0.5 | -0.1 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Medium-term deterioration | 83.0 |
| XLRE | Real Estate | 0.2 | 1.3 | 0.5 | 0.3 | Flat | Neutral | Normal | Neutral | Neutral | Structural accumulation | 91.0 |
| XLU | Utilities | -0.1 | 0.9 | 0.4 | -0.2 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural accumulation | 91.0 |

### Subsector PFV Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ITA | Aerospace and Defense | 0.4 | 0.3 | 0.4 | -1.6 | Up | Buy | Low | Quiet Accumulation | Mild Risk-On | Medium-term recovery | 87.0 |
| SOXX | Semiconductors | -1.9 | 0.1 | 0.4 | -0.8 | Flat | Sell | Normal | Quiet Distribution | Weakening | Medium-term deterioration; Exceptional institutional selling | 75.0 |
| SMH | Semiconductors | 0.1 | 0.1 | 0.5 | -1.2 | Flat | Neutral | Low | Dormant Market | Neutral | Structural accumulation | 91.0 |
| CIBR | Cybersecurity | 0.6 | 1.4 | 0.6 | -0.6 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural accumulation | 91.0 |

### Material Flow Divergences

| Severity | Type | Primary | Comparison | Interpretation |
| --- | --- | --- | --- | --- |
| medium | related_subsector_divergence | XLI | ITA | defense-specific demand differs from broad industrials |
| medium | related_subsector_divergence | XLK | SOXX | technology differs from semiconductors |
| high | close_substitute_divergence | GLD | IAU | primary representative differs from close substitute |
| high | close_substitute_divergence | IVV | SPY | primary representative differs from close substitute |
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
- Short-positioning analytics rows loaded: `40`

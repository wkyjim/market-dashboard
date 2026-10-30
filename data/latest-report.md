# Rule-Based Institutional Market Update

Generated at: 31 October 2026, 00:09:46 (HKT)
Window: 24h

## Executive Dashboard

- Regime score: **48.66 / 100** (Mixed / Rotation)
- US equity strength: **52.05 / 100** (neutral)
- Evidence quality: **72.5 / 100**
- ETF flow contribution: **50.08 / 100**, reliability **71.4 / 100**
- Breadth: **healthy**; above 50DMA `51.67%`, above 200DMA `63.33%`
- Top sector score: **Healthcare** `70.91`
- Top theme score: **Energy** `68.39`

## Market Regime Score

| Metric | Value | Driver / Interpretation |
| --- | --- | --- |
| Overall regime | 48.66 | Mixed / Rotation |
| equity_trend | 51.25 | neutral / mixed; Core equity ETFs versus moving averages. |
| equity_momentum | 49.13 | neutral / mixed; 5D/20D/60D return momentum across SPY, QQQ, IWM, and SMH. |
| market_breadth | 56.67 | mild risk-on support; Participation breadth from tracked equity/ETF rows. |
| volatility | 20.0 | risk-off pressure; VIX level and change; higher score means calmer volatility conditions. |
| rates_yield_curve | 58.0 | mild risk-on support; Treasury yield pressure and curve shape; higher score means less rates pressure. |
| credit_proxy | 50.0 | neutral / mixed; Credit-market proxy; currently neutral when no direct spread signal is available. |
| dollar_fx | 55.59 | mild risk-on support; Dollar move; higher score means less USD tightening pressure. |
| commodity_confirmation | 42.0 | mild risk-off pressure; Copper, silver, oil, and gold mix; higher score means better cyclical confirmation. |
| etf_flow | 50.06 | neutral / mixed; Grouped ETF flow contribution adjusted for reliability. |
| news_confirmation | 50.0 | neutral / mixed; Weighted headline/news confirmation score. |
| Positive contributors |  | none |
| Negative contributors |  | volatility=20.0, commodity_confirmation=42.0 |

## US Equity Strength Score

| Component | Score |
| --- | --- |
| indices_above_moving_averages | 51.25 |
| sp500_trend | 80.0 |
| nasdaq_trend | 35.0 |
| russell_participation | 55.0 |
| returns_momentum | 49.13 |
| rsi_zone | 47.5 |
| macd_confirmation | 43.75 |
| volume_confirmation | 50.0 |
| breadth | 56.67 |

## Evidence Quality / Confidence

- Confidence score: `72.5`
- Agreement ratio: `0.3`
- Contradiction count: `2`
- Missing indicators: none
- Warning flags: none

## Cross-Asset Confirmation

| Area | Signal | Interpretation |
| --- | --- | --- |
| Equities | S&P 500 falling; Nasdaq falling; Russell 2000 falling | Confirms risk appetite when broad indices rise together; weak small caps would narrow the signal. |
| Rates | 10Y Treasury falling; MOVE rising | Rising yields can pressure duration assets; falling MOVE supports calmer bond volatility. |
| Dollar | DXY proxy stable | A stronger dollar can tighten financial conditions and pressure commodities/emerging-market risk. |
| Credit | HYG stable | High-yield weakness would challenge equity risk-on confirmation. |
| Gold | Gold falling | Gold strength can indicate defensive demand, inflation hedging, or geopolitical concern. |
| Silver | Silver falling | Silver helps distinguish precious-metal demand from industrial/cyclical confirmation when data is available. |
| Copper | Copper falling | Copper strength supports cyclical growth confirmation; weakness would dilute risk-on breadth. |
| Oil | WTI crude rising | Oil spikes can be inflationary risk; falling oil can ease cost pressure but may also flag demand softness. |
| Volatility | VIX rising | Falling VIX supports risk appetite; a volatility spike would reduce confidence in broad risk-on. |

### Macro Snapshot

Live macro rows are intraday snapshots from `public.macro_live`; closed rows are official stored rows from `public.macro`.

| Symbol | Name | Close | Pct Chg | Market Date | Status |
| --- | --- | --- | --- | --- | --- |
| ^GSPC | S&P 500 | 7596.83 | -1.6 | 2026-10-30 | live as of 31 October 2026, 00:00:21 (HKT) |
| ^IXIC | NASDAQ Composite | 25510.33 | -2.58 | 2026-10-30 | live as of 31 October 2026, 00:00:21 (HKT) |
| ^RUT | Russell 2000 Index | 2808.8 | -1.76 | 2026-10-30 | live as of 31 October 2026, 00:00:21 (HKT) |
| ^VIX | CBOE Volatility Index | 20.17 | 17.27 | 2026-10-30 | live as of 31 October 2026, 00:00:21 (HKT) |
| ^SKEW | CBOE SKEW Index | 151.03 | 1.54 | 2026-10-29 | closed |
| ^MOVE | ICE BofA MOVE Index | 97.82 | 4.58 | 2026-10-30 | live as of 31 October 2026, 00:00:21 (HKT) |
| US2YT=X | United States 2-Year Treasury Yield | 4.62 | -0.79 | 2026-10-30 | live as of 31 October 2026, 00:00:21 (HKT) |
| US3YT=X | United States 3-Year Treasury Yield | 4.69 | -0.87 | 2026-10-30 | live as of 31 October 2026, 00:00:21 (HKT) |
| US5YT=X | United States 5-Year Treasury Yield | 4.76 | -0.94 | 2026-10-30 | live as of 31 October 2026, 00:00:21 (HKT) |
| US7YT=X | United States 7-Year Treasury Yield | 4.85 | -0.78 | 2026-10-30 | live as of 31 October 2026, 00:00:21 (HKT) |
| US10YT=X | United States 10-Year Treasury Yield | 4.94 | -0.9 | 2026-10-30 | live as of 31 October 2026, 00:00:21 (HKT) |
| US20YT=X | United States 20-Year Treasury Yield | 5.36 | -0.2 | 2026-10-30 | live as of 31 October 2026, 00:00:21 (HKT) |
| US30YT=X | United States 30-Year Treasury Yield | 5.33 | -0.08 | 2026-10-30 | live as of 31 October 2026, 00:00:21 (HKT) |
| HK50 | Hang Seng Futures | 23367.0 | 1.13 | 2026-10-30 | live as of 31 October 2026, 00:00:21 (HKT) |
| KOR200c1 | KOSPI 200 Futures | 897.25 | -4.04 | 2026-10-29 | live as of 31 October 2026, 00:00:21 (HKT) |
| CIHc1 | SSE 50 Futures | 2738.8 | 0.18 | 2026-10-29 | live as of 31 October 2026, 00:00:21 (HKT) |
| HYG | iShares iBoxx High Yield Corporate Bond ETF | 77.44 | -0.17 | 2026-10-30 | live as of 31 October 2026, 00:00:21 (HKT) |
| LQD | iShares iBoxx Investment Grade Corporate Bond ETF | 104.1 | -0.12 | 2026-10-30 | live as of 31 October 2026, 00:00:21 (HKT) |
| JNK | SPDR Bloomberg High Yield Bond ETF | 92.98 | -0.23 | 2026-10-30 | live as of 31 October 2026, 00:00:21 (HKT) |
| RSP | Invesco S&P 500 Equal Weight ETF | 218.29 | -0.8 | 2026-10-30 | live as of 31 October 2026, 00:00:21 (HKT) |
| IWF | iShares Russell 1000 Growth ETF | 117.98 | -2.58 | 2026-10-30 | live as of 31 October 2026, 00:00:21 (HKT) |
| IWD | iShares Russell 1000 Value ETF | 258.85 | -0.73 | 2026-10-30 | live as of 31 October 2026, 00:00:21 (HKT) |
| TLT | iShares 20+ Year Treasury Bond ETF | 81.42 | -0.08 | 2026-10-30 | live as of 31 October 2026, 00:00:21 (HKT) |
| IEF | iShares 7-10 Year Treasury Bond ETF | 91.45 | 0.22 | 2026-10-30 | live as of 31 October 2026, 00:00:21 (HKT) |
| SHY | iShares 1-3 Year Treasury Bond ETF | 81.66 | 0.1 | 2026-10-30 | live as of 31 October 2026, 00:00:21 (HKT) |
| GC=F | Gold Future | 3907.0 | -3.09 | 2026-10-30 | live as of 31 October 2026, 00:00:21 (HKT) |
| SI=F | Silver Future | 49.3 | -5.54 | 2026-10-30 | live as of 31 October 2026, 00:00:21 (HKT) |
| CL=F | WTI Crude Oil Future | 104.05 | 2.01 | 2026-10-30 | live as of 31 October 2026, 00:00:21 (HKT) |
| HG=F | Copper Future | 6.49 | -1.46 | 2026-10-30 | live as of 31 October 2026, 00:00:21 (HKT) |

## Market Dispersion Analysis

- Sector ETF 20D dispersion: `18.67` points (high); leader `XLV` (Health Care) `10.73`, laggard `XLC` (Communication Services) `-7.94`
- Sector ETF 60D dispersion: `28.6` points (very high); leader `XLE` (Energy) `19.89`, laggard `XLC` (Communication Services) `-8.71`

| Comparison | Left | Right | 20D Spread | Signal |
| --- | --- | --- | --- | --- |
| Equal-weight vs cap-weight | RSP (Equal-weight S&P 500) | SPY (S&P 500) | 4.58 | broader participation |
| Small-cap vs large-cap | IWM (Russell 2000) | SPY (S&P 500) | 1.09 | small-cap leadership |
| Growth vs value | IWF (Russell 1000 Growth) | IWD (Russell 1000 Value) | -8.72 | value leadership |
| Nasdaq vs S&P 500 | QQQ (Nasdaq 100) | SPY (S&P 500) | -4.3 | S&P 500 leadership |

## Sector Constituent Dispersion

- Breadth 50D / 200D: percentage of active S&P 500 constituents in the sector trading above the 50-day / 200-day moving average.
- Positive 20D: percentage of active sector constituents with positive 20-day return.
- Std 20D: cross-sectional standard deviation of constituent 20-day returns; higher means wider stock-level dispersion.

| Sector | Count | Breadth 50D | Breadth 200D | Positive 20D | 20D Dispersion | Std 20D | Label | Leaders | Laggards |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Information Technology | 75 | 52.0 | 68.92 | 46.67 | 61.75 | 13.73 | very high | PTC, GEN, ROP | COHR, STX, TER |
| Industrials | 83 | 63.86 | 53.16 | 67.47 | 50.04 | 10.42 | very high | EFX, LMT, PNR | BE, FIX, CAT |
| Real Estate | 30 | 51.72 | 37.93 | 80.0 | 48.02 | 8.05 | very high | CCI, SBAC, AMT | ESS, DOC, ARE |
| Consumer Discretionary | 47 | 63.83 | 46.81 | 76.6 | 39.03 | 8.06 | very high | HAS, NCLH, ULTA | WYNN, MGM, BKNG |
| Health Care | 60 | 81.67 | 88.33 | 90.0 | 38.43 | 6.37 | very high | CRL, LH, LLY | BSX, SOLV, DXCM |
| Materials | 24 | 75.0 | 66.67 | 79.17 | 37.26 | 8.81 | very high | DOW, NUE, VMC | FCX, ALB, MOS |
| Financials | 76 | 62.67 | 72.22 | 85.53 | 36.28 | 6.67 | very high | SPGI, AON, AJG | SCHW, COIN, HOOD |
| Consumer Staples | 34 | 75.0 | 62.5 | 85.29 | 30.58 | 6.46 | very high | EL, KMB, WMT | TGT, ADM, BG |
| Communication Services | 22 | 19.05 | 35.0 | 45.45 | 26.75 | 8.53 | very high | ECHO, DIS, OMC | META, GOOG, GOOGL |
| Energy | 21 | 80.95 | 80.95 | 85.71 | 24.7 | 6.23 | very high | APA, COP, EOG | BKR, TPL, VLO |
| Utilities | 31 | 87.1 | 51.61 | 100.0 | 12.81 | 3.56 | high | EXC, CNP, NI | AES, VST, NRG |

## Economic Data Snapshot

### U.S. Labor

| Indicator | Latest | Unit | Change | Date | Rule-Based Interpretation |
| --- | --- | --- | --- | --- | --- |
| All Employees, Total Nonfarm | 159044.0 | thousands | 29.0 thousands vs prior | 2026-09-01 | Higher reading supports activity or liquidity. |
| Unemployment Rate | 4.2 | percent | 0.1 pp vs prior | 2026-09-01 | Higher reading increases macro pressure. |
| Initial Claims | 194000.0 | number | -6000.0 number vs prior | 2026-10-17 | Lower claims indicate firmer labor-market conditions. |
| Continued Claims | 1728000.0 | number | 25000.0 number vs prior | 2026-10-10 | Higher claims indicate softer labor-market conditions. |
| Labor Force Participation Rate | 61.8 | percent | 0.2 pp vs prior | 2026-09-01 | Higher participation expands labor supply. |

### U.S. Growth

| Indicator | Latest | Unit | Change | Date | Rule-Based Interpretation |
| --- | --- | --- | --- | --- | --- |
| Real Gross Domestic Product | 24611.08 | billions chained 2017 dollars | 203.07 billions chained 2017 dollars vs prior | 2026-07-01 | Higher reading supports activity or liquidity. |
| Industrial Production Index | 103.95 | index 2017=100 | 0.68 index pts vs prior | 2026-09-01 | Higher reading supports activity or liquidity. |
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
| Federal Funds Effective Rate | 3.88 | percent | 0.0 pp vs prior | 2026-10-23 | Stable reading. |
| Secured Overnight Financing Rate | 3.92 | percent | 0.02 pp vs prior | 2026-10-23 | Higher reading increases macro pressure. |
| Effective Federal Funds Rate | 3.75 | percent | 0.12 pp vs prior | 2026-09-01 | Higher reading increases macro pressure. |
| Assets: Total Assets: Federal Reserve | 6753604.0 | millions dollars | -2035.0 millions dollars vs prior | 2026-10-21 | Lower reading signals softer activity or liquidity. |
| M1 Money Stock | 19991.1 | billions dollars | 104.6 billions dollars vs prior | 2026-08-01 | Higher reading supports activity or liquidity. |
| M2 Money Stock | 23342.8 | billions dollars | 124.9 billions dollars vs prior | 2026-08-01 | Higher reading supports activity or liquidity. |
| ICE BofA US High Yield Option-Adjusted Spread | 3.38 | percent | -0.02 pp vs prior | 2026-10-23 | Lower reading eases macro pressure. |
| ICE BofA US Corporate Option-Adjusted Spread | 0.91 | percent | 0.02 pp vs prior | 2026-10-23 | Higher reading increases macro pressure. |

### Housing and Sentiment

| Indicator | Latest | Unit | Change | Date | Rule-Based Interpretation |
| --- | --- | --- | --- | --- | --- |
| Housing Starts | 1221.0 | thousands | -67.0 thousands vs prior | 2026-09-01 | Lower reading signals softer activity or liquidity. |
| New Privately-Owned Housing Units Authorized | 1400.0 | thousands | -3.0 thousands vs prior | 2026-09-01 | Lower reading signals softer activity or liquidity. |
| 30-Year Fixed Rate Mortgage Average | 7.32 | percent | -0.08 pp vs prior | 2026-10-22 | Lower reading eases macro pressure. |
| University of Michigan Consumer Sentiment | 48.1 | index 1966:Q1=100 | -3.6 index pts vs prior | 2026-09-01 | Lower reading signals softer activity or liquidity. |

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
| US dollar/Euro ECB reference exchange rate | 1.12 | USD | 0.0 USD vs prior | 2026-10-30 | EUR strengthened versus this currency. |
| Japanese yen/Euro ECB reference exchange rate | 175.68 | JPY | -0.24 JPY vs prior | 2026-10-30 | EUR weakened versus this currency. |
| Chinese yuan renminbi/Euro ECB reference exchange rate | 7.43 | CNY | 0.02 CNY vs prior | 2026-10-30 | EUR strengthened versus this currency. |
| Australian dollar/Euro ECB reference exchange rate | 1.59 | AUD | 0.01 AUD vs prior | 2026-10-30 | EUR strengthened versus this currency. |

ABS Australia note: ABS rows are stored locally/Neon, but most series are dimension-coded; only curated series should be promoted into narrative report text.

## Sector and Theme Leadership

### Official Sector Strength

Supporting and detracting names are the top/bottom S&P 500 constituents by 20D return when constituent coverage is available; otherwise the report falls back to related ETFs.

| Rank | Sector | Score | Trend | Momentum | Stock Breadth | ETF Flow | Flow Reliability | 3M RS | Supporting / Leaders | Detracting / Laggards |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Healthcare | 70.91 | strong uptrend | positive | broad | 66.06 | 90.0 | 60.89 | CRL, LH, LLY | BSX, SOLV, DXCM |
| 2 | Energy | 70.03 | strong uptrend | positive | broad | 62.96 | 95.0 | 63.31 | APA, COP, EOG | BKR, TPL, VLO |
| 3 | Consumer Staples | 68.45 | strong uptrend | positive | broad | 66.35 | 65.0 | 56.8 | EL, KMB, WMT | TGT, ADM, BG |
| 4 | Consumer Discretionary | 66.64 | strong uptrend | neutral | broad | 52.53 | 65.0 | 52.85 | HAS, NCLH, ULTA | WYNN, MGM, BKNG |
| 5 | Financials | 65.61 | strong uptrend | neutral | broad | 50.0 | 0.0 | 52.78 | SPGI, AON, AJG | SCHW, COIN, HOOD |
| 6 | Cybersecurity | 62.93 | strong uptrend | neutral | broad | 69.44 | 65.0 | 53.35 | CIBR | CIBR |
| 7 | Utilities | 57.81 | neutral | neutral | broad | 62.36 | 65.0 | 54.6 | EXC, CNP, NI | AES, VST, NRG |
| 8 | Real Estate | 55.91 | neutral | neutral | broad | 50.0 | 0.0 | 51.22 | CCI, SBAC, AMT | ESS, DOC, ARE |
| 9 | Crypto | 51.52 | neutral | neutral | mixed | 65.18 | 65.0 | 50.0 |  |  |
| 10 | Industrials | 46.6 | strong downtrend | neutral | weak | 68.1 | 65.0 | 46.65 | EFX, LMT, PNR | BE, FIX, CAT |
| 11 | Technology | 44.8 | neutral | neutral | weak | 62.96 | 100.0 | 47.4 | PTC, GEN, ROP | COHR, STX, TER |
| 12 | Defense | 42.97 | strong downtrend | neutral | weak | 39.86 | 65.0 | 43.92 | XAR | XAR |
| 13 | Semiconductors | 41.46 | downtrend | negative | weak | 60.53 | 90.0 | 42.71 | SMH, SOXX | SOXX, SMH |
| 14 | Nuclear | 35.43 | strong downtrend | negative | weak | 50.0 | 0.0 | 38.85 | NLR | NLR |
| 15 | Grid Infrastructure | 35.01 | strong downtrend | neutral | weak | 60.44 | 65.0 | 43.27 | GRID | GRID |

### Thematic Strength

| Rank | Theme | Score | Setup | ETF Flow | Flow Reliability | Dispersion | Price | News |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Energy | 68.39 | Positive setup | 62.96 | 95.0 | 2.3 | True | True |
| 2 | Healthcare Innovation | 64.48 | Positive setup | 66.06 | 90.0 | 17.72 | True | False |
| 3 | Dividend Defensives | 60.42 | Positive setup | 50.74 | 65.0 | 2.01 | True | False |
| 4 | Cybersecurity | 59.25 | Positive setup | 69.44 | 65.0 | 46.84 | False | False |
| 5 | Defense | 50.93 | Neutral / watchlist | 39.86 | 65.0 | 31.19 | False | False |
| 6 | Small Caps | 49.14 | Neutral / watchlist | 51.91 | 65.0 | 0.0 | False | False |
| 7 | Financials | 48.5 | Neutral / watchlist | 50.0 | 0.0 | 11.33 | False | False |
| 8 | Quality Growth | 48.05 | Neutral / watchlist | 50.62 | 65.0 | 21.72 | False | False |
| 9 | AI Infrastructure | 45.39 | Neutral / watchlist | 60.53 | 90.0 | 19.47 | False | False |
| 10 | Semiconductors | 45.0 | Neutral / watchlist | 60.53 | 90.0 | 11.23 | False | False |
| 11 | Grid Infrastructure | 44.29 | Neutral / watchlist | 60.44 | 65.0 | 18.68 | False | False |
| 12 | Crypto Infrastructure | 43.68 | Neutral / watchlist | 65.18 | 65.0 | 3.4 | False | False |
| 13 | Nuclear | 32.36 | Underperformance risk | 50.0 | 0.0 | 17.96 | False | False |

- Top 5 improving themes: Crypto Infrastructure, Energy, Cybersecurity, Healthcare Innovation, Dividend Defensives
- Top 5 deteriorating themes: Nuclear, Financials, Defense, Grid Infrastructure, Small Caps
- Strong news but weak price confirmation: none
- Strong price but weak news confirmation: Healthcare Innovation, Dividend Defensives

### Sector / Theme Alignment

| Sector | Related Themes | Sector Score | Sector Signal | Theme Score | Theme Signal | Interpretation |
| --- | --- | --- | --- | --- | --- | --- |
| Healthcare | Healthcare Innovation | 70.91 | strong | 64.48 | positive | sector and theme confirmation |
| Energy | Energy | 70.03 | strong | 68.39 | strong | sector and theme confirmation |
| Consumer Staples | Dividend Defensives | 68.45 | strong | 60.42 | positive | sector and theme confirmation |
| Consumer Discretionary | Small Caps | 66.64 | strong | 49.14 | mixed | sector stronger than related themes |
| Financials | Financials | 65.61 | strong | 48.5 | mixed | sector stronger than related themes |
| Cybersecurity | Cybersecurity | 62.93 | positive | 59.25 | positive | sector and theme confirmation |
| Utilities | Grid Infrastructure, Nuclear, Dividend Defensives | 57.81 | positive | 45.69 | mixed | sector stronger than related themes |
| Real Estate | Dividend Defensives | 55.91 | positive | 60.42 | positive | sector and theme confirmation |
| Crypto | Crypto Infrastructure | 51.52 | mixed | 43.68 | weak | mixed confirmation |
| Industrials | Defense, Grid Infrastructure | 46.6 | mixed | 47.61 | mixed | mixed confirmation |
| Technology | AI Infrastructure, Semiconductors, Quality Growth | 44.8 | weak | 46.15 | mixed | mixed confirmation |
| Defense | Defense | 42.97 | weak | 50.93 | mixed | mixed confirmation |
| Semiconductors | AI Infrastructure, Semiconductors | 41.46 | weak | 45.19 | mixed | mixed confirmation |
| Nuclear | Nuclear | 35.43 | weak | 32.36 | very weak | broad weakness across sector and themes |
| Grid Infrastructure | Grid Infrastructure | 35.01 | weak | 44.29 | weak | broad weakness across sector and themes |

## Three-Month Outperformance Setup

| Rank | Theme | Score | Classification | Drivers | Invalidation Triggers |
| --- | --- | --- | --- | --- | --- |
| 1 | Energy | 68.65 | Positive setup | relative_strength_20d, relative_strength_60d, trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 2 | Healthcare Innovation | 67.72 | Positive setup | relative_strength_60d, trend_persistence, breadth, volume_accumulation, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 3 | Dividend Defensives | 64.15 | Positive setup | trend_persistence, breadth, volume_accumulation, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 4 | Cybersecurity | 61.54 | Positive setup | relative_strength_60d, trend_persistence, breadth, volume_accumulation, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 5 | Quality Growth | 54.27 | Neutral / watchlist | trend_persistence, breadth, volume_accumulation, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 6 | Defense | 52.78 | Neutral / watchlist | volume_accumulation, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 7 | Small Caps | 50.27 | Neutral / watchlist | downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 8 | AI Infrastructure | 49.33 | Neutral / watchlist | volume_accumulation, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 9 | Financials | 49.21 | Neutral / watchlist | downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 10 | Semiconductors | 47.77 | Neutral / watchlist |  | relative strength below SPY, breadth below 45%, news turns negative |
| 11 | Grid Infrastructure | 46.63 | Neutral / watchlist | downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 12 | Crypto Infrastructure | 45.16 | Neutral / watchlist | relative_strength_60d, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |

## Breadth and Participation

- Above 50DMA: `51.67%`
- Above 200DMA: `63.33%`
- Positive 20D return: `55.0%`

## Volatility and Risk Signals

- VIX close=20.17 pct_chg=17.27

## News Analytics

- Sentiment counts: {'positive': 36, 'negative': 36, 'neutral': 8}
- News confirmation score: `50.0`

### Top Market-Moving Headlines

**1. AMD’s stock slides after Intel earnings reveal two big issues**
- Source: MarketWatch Top Stories
- Importance / impact: Medium / Negative
- Relevance / horizon: sector_theme / short-term
- Affected assets: AMD, PC, AI, PC market, Intel earnings
- Score: `52.02`
- Investment implication: Theme or sector negative signal; requires price and volume confirmation before affecting rankings.

**2. Intel heads for worst day on Wall Street in more than 50 years on weak guidance**
- Source: CNBC Markets
- Importance / impact: Medium / Negative
- Relevance / horizon: sector_theme / short-term
- Affected assets: AMZN, INTC, AI spending, earnings pressure, market volatility
- Score: `48.45`
- Investment implication: Theme or sector negative signal; requires price and volume confirmation before affecting rankings.

**3. BP’s third-quarter profit nearly quadruples to $8.5 billion as refining margins surge**
- Source: CNBC Top News
- Importance / impact: High / Positive
- Relevance / horizon: macro / quarterly
- Affected assets: BP, earnings, profit, energy
- Score: `47.24`
- Investment implication: Macro-relevant positive signal; use as context for rates, volatility, and index confirmation over the quarterly.

**4. American Oil Giants See Profits Soar as Wars Crimp Energy Supplies**
- Source: Dow Jones US Business
- Importance / impact: High / Positive
- Relevance / horizon: macro / quarterly
- Affected assets: XOM, CVX, U.S, earnings, energy_supply
- Score: `45.9`
- Investment implication: Macro-relevant positive signal; use as context for rates, volatility, and index confirmation over the quarterly.

**5. Alphabet earnings miss reflects first real sign that AI is taking a bite out of search**
- Source: CNBC Top News
- Importance / impact: Medium / Negative
- Relevance / horizon: sector_theme / short-term
- Affected assets: GOOGL, GOOG, AI, earnings miss, Alphabet
- Score: `41.18`
- Investment implication: Theme or sector negative signal; requires price and volume confirmation before affecting rankings.

**6. The U.S. is in a battle to lower the costs to build housing, but it’s losing—as factors including the Iran war and tariffs fuel rising expenses for home builders**
- Source: Dow Jones Economy
- Importance / impact: Medium / Negative
- Relevance / horizon: macro / short-term
- Affected assets: U.S, housing costs, inflation, tariffs
- Score: `38.67`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the short-term.

**7. Shell nearly doubles quarterly profit year-on-year as refining margins soar to record high**
- Source: CNBC Investing
- Importance / impact: Medium / Positive
- Relevance / horizon: macro / quarterly
- Affected assets: SHEL, earnings, refining margins, buyback
- Score: `35.4`
- Investment implication: Macro-relevant positive signal; use as context for rates, volatility, and index confirmation over the quarterly.

**8. Why Alphabet’s stock is on track for its worst day ever after the latest results**
- Source: MarketWatch Top Stories
- Importance / impact: Medium / Negative
- Relevance / horizon: sector_theme / short-term
- Affected assets: GOOGL, GOOG, A, AI, cloud revenue
- Score: `35.22`
- Investment implication: Theme or sector negative signal; requires price and volume confirmation before affecting rankings.

**9. ServiceNow shares plunge 27% to worst day ever after earnings revive AI disruption fears**
- Source: CNBC Investing
- Importance / impact: Low / Negative
- Relevance / horizon: single_name / short-term
- Affected assets: NOW, AI disruption, earnings miss, stock decline
- Score: `33.93`
- Investment implication: Single-name negative signal; low weight unless it maps to a broader sector or theme.

**10. Opinion | The U.S. Investment Boom Arrives**
- Source: Dow Jones US News
- Importance / impact: Low / Positive
- Relevance / horizon: macro / short-term
- Affected assets: U.S, GDP growth, tariffs, economic outlook
- Score: `30.94`
- Investment implication: Macro-relevant positive signal; use as context for rates, volatility, and index confirmation over the short-term.


### Headline Quality Checks

Noisy headline list: Memory Crunch Cements CXMT as China’s Chip Champio

## Positioning & Flow Dashboard

Positioning and flow data is used as confirmation only.

### Deferred Flow Sections

- Official ETF / fund flows: current report uses shares-outstanding-derived net fund flow estimates from free ETF metadata.
- Institutional Ownership: not available until SEC 13F ingestion is implemented.
- Grouped exposure flow reliability: use issuer coverage and availability status before treating ETF flow as confirmation.

## ETF Flows Analysis

- Market flow regime: `Mixed / Neutral`
- Market flow score: `48.9 / 100`
- Equity risk flow: `46.6`
- Credit risk flow: `52.7`
- Sector cyclicality flow: `47.1`
- Duration/liquidity flow: `49.8`
- Alternatives: `mixed alternative-asset demand`
- ETF flow reliability: `71.4 / 100`
- Dominant allocation direction: `mixed allocation`

### Core Flow Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVV | U.S. Broad Equity | -0.2 | -1.0 | 0.5 | -0.7 | Flat | Neutral | Normal | Neutral | Neutral | Structural distribution | 79.0 |
| ACWI | Global Equity | -0.6 | -0.7 | 0.0 | 0.1 | Flat | Neutral | Normal | Neutral | Neutral | Mixed or neutral flow structure; Persistent selling | 77.0 |
| EFA | Developed Markets ex-U.S. | 0.9 | 0.6 | 0.1 | 0.1 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural accumulation; Persistent selling | 83.0 |
| IEMG | Emerging Markets | -0.5 | -0.4 | 0.0 | 0.6 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Mixed or neutral flow structure; Persistent selling | 77.0 |
| IJH | U.S. Mid Cap | -1.3 | 0.3 | 0.5 | -0.4 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Medium-term deterioration | 83.0 |
| IWM | U.S. Small Cap | -0.8 | 0.9 | 0.6 | 0.0 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Mixed or neutral flow structure | 85.0 |
| LQD | Investment-Grade Credit | 0.9 | -0.7 | 0.7 | 2.3 | Up | Neutral | High | Momentum Rally | Watch | Medium-term recovery | 87.0 |
| HYG | High-Yield Credit | 0.2 | 0.3 | 0.6 | 0.2 | Flat | Neutral | Normal | Neutral | Neutral | Structural accumulation | 91.0 |
| SGOV | Treasury Bills / Cash | -0.5 | -0.4 | 0.9 | 0.0 | Flat | Sell | Normal | Quiet Distribution | Weakening | Tactical profit-taking inside structural accumulation; Strong sponsorship | 91.0 |
| SHY | Short-Duration Treasuries | 1.2 | 2.0 | 0.8 | -0.3 | Flat | Buy | Normal | Quiet Accumulation | Improving | Strong confirmation; Exceptional institutional buying, Strong sponsorship | 100.0 |
| IEF | Intermediate-Duration Treasuries | 0.6 | -0.8 | 0.5 | -0.2 | Up | Buy | Normal | Steady Accumulation | Risk-On | Medium-term recovery | 87.0 |
| TLT | Long-Duration Treasuries | -0.9 | 1.1 | 0.6 | -0.7 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Medium-term deterioration | 83.0 |
| GLD | Gold | -0.7 | 1.0 | 0.4 | -0.1 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Medium-term deterioration | 83.0 |
| IBIT | Bitcoin | 0.3 | 1.5 | 0.7 | -0.4 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural accumulation | 91.0 |

### Sector Flow Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| XLC | Communication Services | 1.6 | 2.9 | 0.6 | 2.6 | Down | Buy | High | Aggressive Dip Buying | Recovery Candidate | Strong confirmation; Exceptional institutional buying | 100.0 |
| XLY | Consumer Discretionary | -0.2 | -1.1 | 0.5 | 0.1 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural distribution | 79.0 |
| XLP | Consumer Staples | 1.0 | 0.4 | 0.6 | 1.0 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Medium-term recovery | 87.0 |
| XLE | Energy | 0.8 | 0.1 | 0.7 | -0.7 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural accumulation | 91.0 |
| XLF | Financials | 0.1 | -2.5 | 0.3 | 0.0 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural distribution; Exceptional institutional selling | 71.0 |
| XLV | Health Care | 1.7 | 0.9 | 0.6 | 3.1 | Up | Neutral | High | Momentum Rally | Watch | Structural accumulation | 91.0 |
| XLI | Industrials | 1.0 | -1.2 | 0.6 | 0.4 | Flat | Neutral | Normal | Neutral | Neutral | Medium-term recovery | 87.0 |
| XLK | Information Technology | 0.7 | -0.2 | 0.7 | 0.1 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural accumulation | 91.0 |
| XLB | Materials | -0.6 | -1.4 | 0.6 | 1.3 | Up | Buy | High | Confirmed Accumulation | Strong Risk-On | Tactical rebound inside structural distribution | 83.0 |
| XLRE | Real Estate | 0.2 | -1.4 | 0.5 | 0.2 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Medium-term recovery | 87.0 |
| XLU | Utilities | -0.3 | 1.1 | 0.5 | -0.1 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural accumulation | 91.0 |

### Subsector PFV Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ITA | Aerospace and Defense | 0.1 | 0.6 | 0.3 | 1.4 | Up | Neutral | High | Momentum Rally | Watch | Structural distribution | 79.0 |
| SOXX | Semiconductors | 0.6 | -0.8 | 0.7 | -0.4 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural accumulation | 91.0 |
| SMH | Semiconductors | 0.7 | -0.1 | 0.7 | -0.4 | Down | Buy | Normal | Contrarian Buying | Watch | Strong confirmation | 95.0 |
| CIBR | Cybersecurity | 0.4 | 1.6 | 0.8 | 2.1 | Flat | Neutral | High | High-Turnover Consolidation | Transition | Structural accumulation; Strong sponsorship | 99.0 |

### Material Flow Divergences

| Severity | Type | Primary | Comparison | Interpretation |
| --- | --- | --- | --- | --- |
| medium | related_subsector_divergence | XLI | ITA | defense-specific demand differs from broad industrials |
| high | close_substitute_divergence | GLD | IAU | primary representative differs from close substitute |
| high | close_substitute_divergence | AGG | IUSB | primary representative differs from close substitute |
| high | close_substitute_divergence | HYG | JNK | primary representative differs from close substitute |
| high | close_substitute_divergence | IWF | IVW | primary representative differs from close substitute |
| high | close_substitute_divergence | IWD | IVE | primary representative differs from close substitute |


## Contradiction / Audit Flags

No contradiction flags were triggered by current deterministic rules.

## Data Quality Notes

- Technical rows loaded: `60`
- S&P 500 constituent technical rows loaded: `503`
- Macro rows loaded: `48`
- Live macro rows used: `44`
- Economic rows loaded: `113`
- News rows loaded: `80`
- Positioning/flow rows loaded: `30`

## Cycle Metadata

- Report generated at: 31 October 2026, 00:09:46 (HKT)

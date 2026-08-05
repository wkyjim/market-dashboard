# Rule-Based Institutional Market Update

Generated at: 6 August 2026, 00:05:11 (HKT)
Window: 24h

## Executive Dashboard

- Regime score: **66.66 / 100** (Moderate Risk-On)
- US equity strength: **80.99 / 100** (strong)
- Evidence quality: **86.5 / 100**
- ETF flow contribution: **48.65 / 100**, reliability **71.05 / 100**
- Breadth: **broad**; above 50DMA `73.33%`, above 200DMA `72.88%`
- Top sector score: **Cybersecurity** `72.22`
- Top theme score: **Financials** `61.22`

## Market Regime Score

| Metric | Value | Driver / Interpretation |
| --- | --- | --- |
| Overall regime | 66.66 | Moderate Risk-On |
| equity_trend | 93.75 | risk-on support; Core equity ETFs versus moving averages. |
| equity_momentum | 54.05 | neutral / mixed; 5D/20D/60D return momentum across SPY, QQQ, IWM, and SMH. |
| market_breadth | 73.74 | risk-on support; Participation breadth from tracked equity/ETF rows. |
| volatility | 70.0 | risk-on support; VIX level and change; higher score means calmer volatility conditions. |
| rates_yield_curve | 58.0 | mild risk-on support; Treasury yield pressure and curve shape; higher score means less rates pressure. |
| credit_proxy | 50.0 | neutral / mixed; Credit-market proxy; currently neutral when no direct spread signal is available. |
| dollar_fx | 55.7 | mild risk-on support; Dollar move; higher score means less USD tightening pressure. |
| commodity_confirmation | 59.0 | mild risk-on support; Copper, silver, oil, and gold mix; higher score means better cyclical confirmation. |
| etf_flow | 49.04 | neutral / mixed; Grouped ETF flow contribution adjusted for reliability. |
| news_confirmation | 88.12 | risk-on support; Weighted headline/news confirmation score. |
| Positive contributors |  | equity_trend=93.75, news_confirmation=88.12, market_breadth=73.74, volatility=70.0 |
| Negative contributors |  | none |

## US Equity Strength Score

| Component | Score |
| --- | --- |
| indices_above_moving_averages | 93.75 |
| sp500_trend | 100.0 |
| nasdaq_trend | 100.0 |
| russell_participation | 100.0 |
| returns_momentum | 54.05 |
| rsi_zone | 66.25 |
| macd_confirmation | 61.25 |
| volume_confirmation | 60.0 |
| breadth | 73.74 |

## Evidence Quality / Confidence

- Confidence score: `86.5`
- Agreement ratio: `0.7`
- Contradiction count: `0`
- Missing indicators: none
- Warning flags: none

## Cross-Asset Confirmation

| Area | Signal | Interpretation |
| --- | --- | --- |
| Equities | S&P 500 stable; Nasdaq falling; Russell 2000 falling | Confirms risk appetite when broad indices rise together; weak small caps would narrow the signal. |
| Rates | 10Y Treasury stable; MOVE rising | Rising yields can pressure duration assets; falling MOVE supports calmer bond volatility. |
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
| ^GSPC | S&P 500 | 7730.19 | -0.08 | 2026-08-05 | live as of 6 August 2026, 00:00:37 (HKT) |
| ^IXIC | NASDAQ Composite | 26471.07 | -0.43 | 2026-08-05 | live as of 6 August 2026, 00:00:37 (HKT) |
| ^RUT | Russell 2000 Index | 3026.93 | -0.33 | 2026-08-05 | live as of 6 August 2026, 00:00:37 (HKT) |
| ^VIX | CBOE Volatility Index | 16.31 | -1.15 | 2026-08-05 | live as of 6 August 2026, 00:00:37 (HKT) |
| ^SKEW | CBOE SKEW Index | 126.41 | -9.68 | 2026-08-04 | closed |
| ^MOVE | ICE BofA MOVE Index | 76.82 | 8.38 | 2026-07-24 | closed |
| US2YT=X | United States 2-Year Treasury Yield | 4.21 | 0.49 | 2026-08-05 | live as of 6 August 2026, 00:00:37 (HKT) |
| US3YT=X | United States 3-Year Treasury Yield | 4.27 | 0.55 | 2026-08-05 | live as of 6 August 2026, 00:00:37 (HKT) |
| US5YT=X | United States 5-Year Treasury Yield | 4.35 | 0.44 | 2026-08-05 | live as of 6 August 2026, 00:00:37 (HKT) |
| US7YT=X | United States 7-Year Treasury Yield | 4.49 | 0.35 | 2026-08-05 | live as of 6 August 2026, 00:00:37 (HKT) |
| US10YT=X | United States 10-Year Treasury Yield | 4.64 | 0.19 | 2026-08-05 | live as of 6 August 2026, 00:00:37 (HKT) |
| US20YT=X | United States 20-Year Treasury Yield | 5.18 | -0.07 | 2026-08-05 | live as of 6 August 2026, 00:00:37 (HKT) |
| US30YT=X | United States 30-Year Treasury Yield | 5.18 | -0.16 | 2026-08-05 | live as of 6 August 2026, 00:00:37 (HKT) |
| HK50 | Hang Seng Futures | 25898.5 | -0.11 | 2026-08-05 | closed |
| KOR200c1 | KOSPI 200 Futures | 1050.2 | 5.02 | 2026-08-04 | closed |
| CIHc1 | SSE 50 Futures | 2871.6 | -0.09 | 2026-08-04 | closed |
| HYG | iShares iBoxx High Yield Corporate Bond ETF | 79.46 | -0.11 | 2026-08-05 | live as of 6 August 2026, 00:00:37 (HKT) |
| LQD | iShares iBoxx Investment Grade Corporate Bond ETF | 106.67 | -0.08 | 2026-08-05 | live as of 6 August 2026, 00:00:37 (HKT) |
| JNK | SPDR Bloomberg High Yield Bond ETF | 95.69 | -0.07 | 2026-08-05 | live as of 6 August 2026, 00:00:37 (HKT) |
| RSP | Invesco S&P 500 Equal Weight ETF | 219.35 | -0.4 | 2026-08-05 | live as of 6 August 2026, 00:00:37 (HKT) |
| IWF | iShares Russell 1000 Growth ETF | 124.47 | 0.14 | 2026-08-05 | live as of 6 August 2026, 00:00:37 (HKT) |
| IWD | iShares Russell 1000 Value ETF | 255.6 | -0.4 | 2026-08-05 | live as of 6 August 2026, 00:00:37 (HKT) |
| TLT | iShares 20+ Year Treasury Bond ETF | 82.88 | 0.07 | 2026-08-05 | live as of 6 August 2026, 00:00:37 (HKT) |
| IEF | iShares 7-10 Year Treasury Bond ETF | 93.16 | -0.1 | 2026-08-05 | live as of 6 August 2026, 00:00:37 (HKT) |
| SHY | iShares 1-3 Year Treasury Bond ETF | 81.84 | -0.03 | 2026-08-05 | live as of 6 August 2026, 00:00:37 (HKT) |
| GC=F | Gold Future | 4305.8 | 5.14 | 2026-08-05 | live as of 6 August 2026, 00:00:37 (HKT) |
| SI=F | Silver Future | 62.3 | 3.73 | 2026-08-05 | live as of 6 August 2026, 00:00:37 (HKT) |
| CL=F | WTI Crude Oil Future | 75.33 | -0.58 | 2026-08-05 | live as of 6 August 2026, 00:00:37 (HKT) |
| HG=F | Copper Future | 6.71 | 1.32 | 2026-08-05 | live as of 6 August 2026, 00:00:37 (HKT) |

## Market Dispersion Analysis

- Sector ETF 20D dispersion: `10.58` points (moderate); leader `XLE` (Energy) `7.1`, laggard `XLU` (Utilities) `-3.48`
- Sector ETF 60D dispersion: `16.83` points (high); leader `XLF` (Financials) `12.28`, laggard `XLC` (Communication Services) `-4.55`

| Comparison | Left | Right | 20D Spread | Signal |
| --- | --- | --- | --- | --- |
| Equal-weight vs cap-weight | RSP (Equal-weight S&P 500) | SPY (S&P 500) | -0.6 | balanced |
| Small-cap vs large-cap | IWM (Russell 2000) | SPY (S&P 500) | -1.3 | large-cap leadership |
| Growth vs value | IWF (Russell 1000 Growth) | IWD (Russell 1000 Value) | -1.16 | value leadership |
| Nasdaq vs S&P 500 | QQQ (Nasdaq 100) | SPY (S&P 500) | -1.13 | S&P 500 leadership |

## Sector Constituent Dispersion

- Breadth 50D / 200D: percentage of active S&P 500 constituents in the sector trading above the 50-day / 200-day moving average.
- Positive 20D: percentage of active sector constituents with positive 20-day return.
- Std 20D: cross-sectional standard deviation of constituent 20-day returns; higher means wider stock-level dispersion.

| Sector | Count | Breadth 50D | Breadth 200D | Positive 20D | 20D Dispersion | Std 20D | Label | Leaders | Laggards |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Information Technology | 74 | 54.05 | 69.86 | 67.57 | 62.55 | 12.2 | very high | ZBRA, IT, CTSH | FICO, APP, IBM |
| Health Care | 59 | 84.75 | 67.8 | 64.41 | 52.57 | 8.26 | very high | BAX, DXCM, SOLV | ELV, ISRG, MRNA |
| Financials | 76 | 91.78 | 87.14 | 67.11 | 45.41 | 7.05 | very high | PYPL, ARES, IVZ | COIN, PGR, HOOD |
| Consumer Discretionary | 47 | 61.7 | 57.45 | 63.83 | 42.51 | 9.52 | very high | GRMN, ULTA, HAS | YUM, TSLA, APTV |
| Industrials | 81 | 69.62 | 72.73 | 64.2 | 40.08 | 7.95 | very high | LDOS, ALLE, WAB | ROL, CHRW, LII |
| Materials | 26 | 69.23 | 73.08 | 65.38 | 30.46 | 7.87 | very high | NUE, STLD, FCX | CRH, CTVA, LIN |
| Utilities | 31 | 19.35 | 58.06 | 9.68 | 26.68 | 4.39 | very high | CEG, PCG, AES | SRE, LNT, NRG |
| Communication Services | 23 | 68.18 | 40.91 | 60.87 | 26.6 | 6.51 | very high | CHTR, T, VZ | ECHO, TTWO, PSKY |
| Consumer Staples | 34 | 72.73 | 65.62 | 50.0 | 22.82 | 4.62 | very high | TGT, DG, TAP | BG, PEP, MO |
| Energy | 21 | 71.43 | 85.71 | 71.43 | 22.13 | 6.82 | very high | MPC, VLO, PSX | TRGP, HAL, WMB |
| Real Estate | 31 | 54.84 | 80.65 | 41.94 | 17.43 | 4.49 | high | WY, DLR, IRM | CPT, MAA, UDR |

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
| 1 | Cybersecurity | 72.22 | strong uptrend | positive | broad | 62.71 | 65.0 | 63.22 | CIBR | CIBR |
| 2 | Financials | 67.83 | strong uptrend | positive | broad | 62.06 | 90.0 | 52.8 | PYPL, ARES, IVZ | COIN, PGR, HOOD |
| 3 | Grid Infrastructure | 67.57 | strong uptrend | neutral | broad | 68.74 | 65.0 | 46.11 | GRID | GRID |
| 4 | Technology | 67.38 | strong uptrend | neutral | broad | 48.78 | 90.0 | 50.69 | ZBRA, IT, CTSH | FICO, APP, IBM |
| 5 | Industrials | 66.94 | strong uptrend | neutral | broad | 50.15 | 65.0 | 50.1 | LDOS, ALLE, WAB | ROL, CHRW, LII |
| 6 | Consumer Staples | 65.94 | strong uptrend | neutral | broad | 62.42 | 65.0 | 46.95 | TGT, DG, TAP | BG, PEP, MO |
| 7 | Healthcare | 65.09 | strong uptrend | neutral | broad | 83.04 | 100.0 | 49.88 | BAX, DXCM, SOLV | ELV, ISRG, MRNA |
| 8 | Defense | 64.74 | strong uptrend | neutral | broad | 42.85 | 65.0 | 49.47 | XAR | XAR |
| 9 | Real Estate | 62.09 | strong uptrend | neutral | broad | 60.7 | 100.0 | 47.0 | WY, DLR, IRM | CPT, MAA, UDR |
| 10 | Energy | 61.06 | uptrend | neutral | broad | 46.63 | 95.0 | 52.03 | MPC, VLO, PSX | TRGP, HAL, WMB |
| 11 | Consumer Discretionary | 60.92 | uptrend | neutral | broad | 66.47 | 65.0 | 45.86 | GRMN, ULTA, HAS | YUM, TSLA, APTV |
| 12 | Crypto | 51.43 | neutral | neutral | mixed | 64.25 | 65.0 | 50.0 |  |  |
| 13 | Semiconductors | 50.91 | strong uptrend | neutral | weak | 59.07 | 90.0 | 48.46 | SMH, SOXX | SOXX, SMH |
| 14 | Nuclear | 43.02 | strong downtrend | neutral | weak | 50.0 | 0.0 | 39.22 | NLR | NLR |
| 15 | Utilities | 34.01 | strong downtrend | neutral | weak | 56.08 | 65.0 | 41.76 | CEG, PCG, AES | SRE, LNT, NRG |

### Thematic Strength

| Rank | Theme | Score | Setup | ETF Flow | Flow Reliability | Dispersion | Price | News |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Financials | 61.22 | Positive setup | 62.06 | 90.0 | 4.44 | True | False |
| 2 | Small Caps | 60.57 | Positive setup | 53.91 | 65.0 | 0.0 | True | False |
| 3 | Quality Growth | 59.85 | Positive setup | 58.4 | 65.0 | 27.15 | False | False |
| 4 | Cybersecurity | 59.06 | Positive setup | 62.71 | 65.0 | 3.11 | False | False |
| 5 | AI Infrastructure | 58.65 | Positive setup | 59.07 | 90.0 | 28.46 | False | False |
| 6 | Energy | 58.25 | Positive setup | 46.63 | 95.0 | 2.32 | False | False |
| 7 | Defense | 57.16 | Neutral / watchlist | 42.85 | 65.0 | 9.62 | False | False |
| 8 | Healthcare Innovation | 56.79 | Neutral / watchlist | 83.04 | 100.0 | 9.04 | False | False |
| 9 | Semiconductors | 53.56 | Neutral / watchlist | 59.07 | 90.0 | 16.34 | False | False |
| 10 | Grid Infrastructure | 52.45 | Neutral / watchlist | 68.74 | 65.0 | 17.4 | False | False |
| 11 | Dividend Defensives | 52.23 | Neutral / watchlist | 54.17 | 65.0 | 4.08 | False | False |
| 12 | Nuclear | 38.47 | Weak setup | 50.0 | 0.0 | 15.92 | False | False |
| 13 | Crypto Infrastructure | 31.87 | Underperformance risk | 64.25 | 65.0 | 8.11 | False | False |

- Top 5 improving themes: Cybersecurity, Financials, Healthcare Innovation, Defense, Semiconductors
- Top 5 deteriorating themes: Crypto Infrastructure, Nuclear, Grid Infrastructure, Dividend Defensives, Energy
- Strong news but weak price confirmation: none
- Strong price but weak news confirmation: Financials, Small Caps

### Sector / Theme Alignment

| Sector | Related Themes | Sector Score | Sector Signal | Theme Score | Theme Signal | Interpretation |
| --- | --- | --- | --- | --- | --- | --- |
| Cybersecurity | Cybersecurity | 72.22 | strong | 59.06 | positive | sector and theme confirmation |
| Financials | Financials | 67.83 | strong | 61.22 | positive | sector and theme confirmation |
| Grid Infrastructure | Grid Infrastructure | 67.57 | strong | 52.45 | mixed | sector stronger than related themes |
| Technology | AI Infrastructure, Semiconductors, Quality Growth | 67.38 | strong | 57.35 | positive | sector and theme confirmation |
| Industrials | Defense, Grid Infrastructure | 66.94 | strong | 54.81 | mixed | sector stronger than related themes |
| Consumer Staples | Dividend Defensives | 65.94 | strong | 52.23 | mixed | sector stronger than related themes |
| Healthcare | Healthcare Innovation | 65.09 | strong | 56.79 | positive | sector and theme confirmation |
| Defense | Defense | 64.74 | positive | 57.16 | positive | sector and theme confirmation |
| Real Estate | Dividend Defensives | 62.09 | positive | 52.23 | mixed | sector stronger than related themes |
| Energy | Energy | 61.06 | positive | 58.25 | positive | sector and theme confirmation |
| Consumer Discretionary | Small Caps | 60.92 | positive | 60.57 | positive | sector and theme confirmation |
| Crypto | Crypto Infrastructure | 51.43 | mixed | 31.87 | very weak | mixed confirmation |
| Semiconductors | AI Infrastructure, Semiconductors | 50.91 | mixed | 56.1 | positive | theme stronger than official sector |
| Nuclear | Nuclear | 43.02 | weak | 38.47 | weak | broad weakness across sector and themes |
| Utilities | Grid Infrastructure, Nuclear, Dividend Defensives | 34.01 | very weak | 47.71 | mixed | mixed confirmation |

## Three-Month Outperformance Setup

| Rank | Theme | Score | Classification | Drivers | Invalidation Triggers |
| --- | --- | --- | --- | --- | --- |
| 1 | Financials | 66.45 | Positive setup | relative_strength_60d, trend_persistence, breadth, downside_volatility, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 2 | Small Caps | 64.5 | Positive setup | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 3 | Quality Growth | 63.32 | Positive setup | trend_persistence, breadth, volume_accumulation | relative strength below SPY, breadth below 45%, news turns negative |
| 4 | Energy | 61.61 | Positive setup | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 5 | AI Infrastructure | 61.59 | Positive setup | trend_persistence, breadth | relative strength below SPY, breadth below 45%, news turns negative |
| 6 | Cybersecurity | 61.3 | Positive setup | relative_strength_60d, trend_persistence, breadth, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 7 | Healthcare Innovation | 59.85 | Neutral / watchlist | trend_persistence, breadth, volume_accumulation, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 8 | Defense | 59.78 | Neutral / watchlist | trend_persistence, breadth | relative strength below SPY, breadth below 45%, news turns negative |
| 9 | Semiconductors | 56.45 | Neutral / watchlist | trend_persistence, breadth | relative strength below SPY, breadth below 45%, news turns negative |
| 10 | Dividend Defensives | 55.98 | Neutral / watchlist | trend_persistence, breadth, volume_accumulation, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 11 | Grid Infrastructure | 52.84 | Neutral / watchlist | trend_persistence, breadth, volume_accumulation, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 12 | Nuclear | 34.9 | Weak setup |  | relative strength below SPY, breadth below 45%, news turns negative |

## Breadth and Participation

- Above 50DMA: `73.33%`
- Above 200DMA: `72.88%`
- Positive 20D return: `75.0%`

## Volatility and Risk Signals

- VIX close=16.31 pct_chg=-1.15

## News Analytics

- Sentiment counts: {'positive': 69, 'negative': 8, 'neutral': 3}
- News confirmation score: `88.12`

### Top Market-Moving Headlines

**1. Flutter CEO to Step Down as U.S. Sports-Betting Business Falters; Profit Outlook Cut**
- Source: Dow Jones US Business
- Importance / impact: High / Negative
- Relevance / horizon: macro / short-term
- Affected assets: FLTR.L, U.S, Leadership Change, Profit Warning
- Score: `57.38`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the short-term.

**2. Lilly’s revenue soars 48%, driven by demand for its GLP-1s**
- Source: MarketWatch Top Stories
- Importance / impact: Medium / Positive
- Relevance / horizon: single_name / short-term
- Affected assets: LLY, GLP, pharmaceuticals, diabetes, weight loss
- Score: `43.88`
- Investment implication: Single-name positive signal; low weight unless it maps to a broader sector or theme.

**3. Walt Disney’s stock climbs as company cites ‘Toy Story 5’ for earnings growth**
- Source: MarketWatch Top Stories
- Importance / impact: Medium / Positive
- Relevance / horizon: single_name / short-term
- Affected assets: DIS, entertainment, earnings
- Score: `43.88`
- Investment implication: Single-name positive signal; low weight unless it maps to a broader sector or theme.

**4. Lilly’s revenue soars 48%, driven by demand for its GLP-1s**
- Source: MarketWatch Bulletins
- Importance / impact: Medium / Positive
- Relevance / horizon: single_name / short-term
- Affected assets: Lilly, GLP, revenue_growth, pharmaceuticals
- Score: `41.68`
- Investment implication: Single-name positive signal; low weight unless it maps to a broader sector or theme.

**5. China's super-rich 'in shock' and hunting for cash as Beijing issues surprise tax on offshore trusts**
- Source: CNBC Technology
- Importance / impact: Medium / Negative
- Relevance / horizon: sector_theme / short-term
- Affected assets: tax_policy, wealth_management
- Score: `39.02`
- Investment implication: Theme or sector negative signal; requires price and volume confirmation before affecting rankings.

**6. Honda Doubles Profit, Lifts Guidance on Weak Yen**
- Source: Dow Jones US Business
- Importance / impact: Medium / Positive
- Relevance / horizon: single_name / quarterly
- Affected assets: HON, EV, Automotive, Profitability
- Score: `37.29`
- Investment implication: Single-name positive signal; low weight unless it maps to a broader sector or theme.

**7. CNBC Daily Open: Markets rally on hopes of Iran-U.S. Strait of Hormuz deal**
- Source: CNBC Top News
- Importance / impact: Medium / Positive
- Relevance / horizon: macro / short-term
- Affected assets: CNBC, U.S, Geopolitics, Energy
- Score: `36.74`
- Investment implication: Macro-relevant positive signal; use as context for rates, volatility, and index confirmation over the short-term.

**8. Chip Maker Infineon Forecasts Strong Revenue Growth on Booming AI Demand**
- Source: Dow Jones US Business
- Importance / impact: Medium / Positive
- Relevance / horizon: sector_theme / current fiscal year
- Affected assets: AI, semiconductor
- Score: `36.58`
- Investment implication: Theme or sector positive signal; requires price and volume confirmation before affecting rankings.

**9. Palantir stock skyrockets 29%, narrowly missing its best day ever after 'otherworldly' results**
- Source: CNBC Top News
- Importance / impact: Medium / Positive
- Relevance / horizon: single_name / short-term
- Affected assets: PAL, technology, AI
- Score: `35.43`
- Investment implication: Single-name positive signal; low weight unless it maps to a broader sector or theme.

**10. Eli Lilly easily tops quarterly estimates, raises outlook as Zepbound and Mounjaro sales surge**
- Source: CNBC Business
- Importance / impact: Medium / Positive
- Relevance / horizon: single_name / long-term
- Affected assets: LLY, earnings report, pharmaceuticals
- Score: `35.1`
- Investment implication: Single-name positive signal; low weight unless it maps to a broader sector or theme.


### Headline Quality Checks

Noisy headline list: Dow leaps 1,000 points fueled by earnings, hopes f, U.S. Stocks Jump, Oil Drops After Bessent Says Ira

## Positioning & Flow Dashboard

Positioning and flow data is used as confirmation only. FINRA short-sale volume is not short interest.

### Deferred Flow Sections

- Official ETF / fund flows: current report uses shares-outstanding-derived net fund flow estimates from free ETF metadata.
- Institutional Ownership: not available until SEC 13F ingestion is implemented.
- Crowding / Squeeze Risks: initial coverage uses CFTC crowded positioning and FINRA elevated short-sale volume only.
- Grouped exposure flow reliability: use issuer coverage and availability status before treating ETF flow as confirmation.

## ETF Flows Analysis

- Market flow regime: `Mixed / Neutral`
- Market flow score: `48.8 / 100`
- Equity risk flow: `46.7`
- Credit risk flow: `56.5`
- Sector cyclicality flow: `45.6`
- Duration/liquidity flow: `46.7`
- Alternatives: `defensive or uncertainty hedge`
- ETF flow reliability: `71.0 / 100`
- Dominant allocation direction: `defensive demand`

### Core Flow Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVV | U.S. Broad Equity | -0.8 | 0.4 | 0.3 | -0.5 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Medium-term deterioration | 83.0 |
| ACWI | Global Equity | -2.0 | -1.4 | 0.0 | 1.0 | Up | Sell | High | Distribution into Strength | Bearish Divergence | Strong confirmation; Persistent selling | 87.0 |
| EFA | Developed Markets ex-U.S. | -1.4 | -0.2 | 0.0 | -0.7 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Medium-term deterioration; Persistent selling | 75.0 |
| IEMG | Emerging Markets | 0.0 | -0.3 | 0.1 | -0.2 | Flat | Buy | Normal | Quiet Accumulation | Improving | Strong confirmation; Exceptional institutional buying, Persistent selling | 95.0 |
| IJH | U.S. Mid Cap | 0.1 | 0.6 | 0.7 | 0.4 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural accumulation | 91.0 |
| IWM | U.S. Small Cap | 0.0 | -0.1 | 0.5 | -0.8 | Flat | Neutral | Normal | Neutral | Neutral | Structural distribution | 79.0 |
| LQD | Investment-Grade Credit | -1.1 | 0.7 | 0.3 | 0.3 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Medium-term deterioration | 83.0 |
| HYG | High-Yield Credit | 0.2 | 1.5 | 0.4 | 1.4 | Flat | Buy | High | Strong Accumulation | Early Bullish | Medium-term deterioration; Exceptional institutional buying | 91.0 |
| SGOV | Treasury Bills / Cash | -0.7 | -0.9 | 0.9 | 0.8 | Flat | Sell | Normal | Quiet Distribution | Weakening | Tactical profit-taking inside structural accumulation; Strong sponsorship | 91.0 |
| SHY | Short-Duration Treasuries | -0.7 | -0.6 | 0.2 | 1.9 | Flat | Buy | High | Strong Accumulation | Early Bullish | Medium-term deterioration; Exceptional institutional buying, Persistent selling | 83.0 |
| IEF | Intermediate-Duration Treasuries | 0.2 | -0.4 | 0.7 | -0.4 | Flat | Neutral | Normal | Neutral | Neutral | Structural accumulation | 91.0 |
| TLT | Long-Duration Treasuries | 0.8 | 0.7 | 0.7 | 1.4 | Down | Neutral | High | Heavy Selling Pressure | Cautious | Structural accumulation | 91.0 |
| GLD | Gold | 1.2 | 1.4 | 0.4 | -0.5 | Flat | Buy | Normal | Quiet Accumulation | Improving | Strong confirmation | 95.0 |
| IBIT | Bitcoin | 0.5 | -1.5 | 0.7 | -0.6 | Flat | Neutral | Normal | Neutral | Neutral | Medium-term recovery | 87.0 |

### Sector Flow Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| XLC | Communication Services | -0.9 | -1.7 | 0.3 | -0.5 | Flat | Sell | Normal | Quiet Distribution | Weakening | Strong confirmation; Exceptional institutional selling | 87.0 |
| XLY | Consumer Discretionary | 0.9 | 2.9 | 0.5 | 1.0 | Flat | Buy | High | Strong Accumulation | Early Bullish | Strong confirmation; Exceptional institutional buying | 100.0 |
| XLP | Consumer Staples | 0.8 | 1.8 | 0.4 | 0.4 | Flat | Neutral | Normal | Neutral | Neutral | Structural accumulation | 91.0 |
| XLE | Energy | -0.6 | -1.3 | 0.3 | 0.4 | Up | Sell | Normal | Profit Taking | Slightly Bearish | Strong confirmation; Exceptional institutional selling | 87.0 |
| XLF | Financials | 1.4 | 2.4 | 0.5 | -0.5 | Up | Buy | Normal | Steady Accumulation | Risk-On | Strong confirmation; Exceptional institutional buying | 100.0 |
| XLV | Health Care | 0.1 | 1.5 | 0.5 | 1.6 | Flat | Neutral | High | High-Turnover Consolidation | Transition | Medium-term deterioration | 83.0 |
| XLI | Industrials | -0.9 | 0.1 | 0.5 | 1.7 | Up | Neutral | High | Momentum Rally | Watch | Medium-term deterioration | 83.0 |
| XLK | Information Technology | 0.4 | -0.7 | 0.7 | 0.3 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural accumulation | 91.0 |
| XLB | Materials | -1.1 | -0.7 | 0.3 | 1.5 | Flat | Sell | High | Distribution Before Breakdown | Early Bearish | Medium-term deterioration | 83.0 |
| XLRE | Real Estate | 0.4 | 1.8 | 0.6 | 0.8 | Flat | Neutral | Normal | Neutral | Neutral | Structural accumulation | 91.0 |
| XLU | Utilities | -0.0 | 0.7 | 0.4 | 1.3 | Down | Buy | High | Aggressive Dip Buying | Recovery Candidate | Strong confirmation | 95.0 |

### Subsector PFV Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ITA | Aerospace and Defense | 0.1 | -0.3 | 0.3 | -1.0 | Flat | Neutral | Normal | Neutral | Neutral | Structural distribution | 79.0 |
| SOXX | Semiconductors | 1.7 | 1.5 | 0.5 | 0.0 | Flat | Buy | Normal | Quiet Accumulation | Improving | Strong confirmation | 95.0 |
| SMH | Semiconductors | 0.6 | 1.2 | 0.6 | -0.5 | Flat | Neutral | Normal | Neutral | Neutral | Structural accumulation | 91.0 |
| CIBR | Cybersecurity | 0.5 | 1.2 | 0.6 | 0.3 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural accumulation | 91.0 |

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

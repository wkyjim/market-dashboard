# Rule-Based Institutional Market Update

Generated at: 13 September 2026, 03:15:21 (HKT)
Window: 24h

## Executive Dashboard

- Regime score: **56.66 / 100** (Mild Risk-On)
- US equity strength: **57.01 / 100** (neutral)
- Evidence quality: **79.5 / 100**
- ETF flow contribution: **47.97 / 100**, reliability **66.86 / 100**
- Breadth: **narrow**; above 50DMA `46.67%`, above 200DMA `69.49%`
- Top sector score: **Energy** `65.32`
- Top theme score: **Energy** `60.87`

## Market Regime Score

| Metric | Value | Driver / Interpretation |
| --- | --- | --- |
| Overall regime | 56.66 | Mild Risk-On |
| equity_trend | 62.5 | mild risk-on support; Core equity ETFs versus moving averages. |
| equity_momentum | 47.92 | neutral / mixed; 5D/20D/60D return momentum across SPY, QQQ, IWM, and SMH. |
| market_breadth | 44.83 | mild risk-off pressure; Participation breadth from tracked equity/ETF rows. |
| volatility | 80.0 | risk-on support; VIX level and change; higher score means calmer volatility conditions. |
| rates_yield_curve | 58.0 | mild risk-on support; Treasury yield pressure and curve shape; higher score means less rates pressure. |
| credit_proxy | 50.0 | neutral / mixed; Credit-market proxy; currently neutral when no direct spread signal is available. |
| dollar_fx | 54.97 | neutral / mixed; Dollar move; higher score means less USD tightening pressure. |
| commodity_confirmation | 61.0 | mild risk-on support; Copper, silver, oil, and gold mix; higher score means better cyclical confirmation. |
| etf_flow | 48.64 | neutral / mixed; Grouped ETF flow contribution adjusted for reliability. |
| news_confirmation | 61.88 | mild risk-on support; Weighted headline/news confirmation score. |
| Positive contributors |  | volatility=80.0, equity_trend=62.5, news_confirmation=61.88, commodity_confirmation=61.0 |
| Negative contributors |  | market_breadth=44.83 |

## US Equity Strength Score

| Component | Score |
| --- | --- |
| indices_above_moving_averages | 62.5 |
| sp500_trend | 80.0 |
| nasdaq_trend | 80.0 |
| russell_participation | 35.0 |
| returns_momentum | 47.92 |
| rsi_zone | 56.25 |
| macd_confirmation | 43.75 |
| volume_confirmation | 42.5 |
| breadth | 44.83 |

## Evidence Quality / Confidence

- Confidence score: `79.5`
- Agreement ratio: `0.5`
- Contradiction count: `1`
- Missing indicators: none
- Warning flags: none

## Cross-Asset Confirmation

| Area | Signal | Interpretation |
| --- | --- | --- |
| Equities | S&P 500 rising; Nasdaq rising; Russell 2000 rising | Confirms risk appetite when broad indices rise together; weak small caps would narrow the signal. |
| Rates | 10Y Treasury rising; MOVE stable | Rising yields can pressure duration assets; falling MOVE supports calmer bond volatility. |
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
| ^GSPC | S&P 500 | 7656.98 | 0.86 | 2026-09-11 | closed |
| ^IXIC | NASDAQ Composite | 26333.04 | 0.96 | 2026-09-11 | closed |
| ^RUT | Russell 2000 Index | 2903.94 | 0.45 | 2026-09-11 | closed |
| ^VIX | CBOE Volatility Index | 15.84 | -11.21 | 2026-09-11 | closed |
| ^SKEW | CBOE SKEW Index | 154.49 | 5.08 | 2026-09-11 | closed |
| ^MOVE | ICE BofA MOVE Index | 82.21 | 0.14 | 2026-09-11 | closed |
| US2YT=X | United States 2-Year Treasury Yield | 4.63 | 1.75 | 2026-09-11 | closed |
| US3YT=X | United States 3-Year Treasury Yield | 4.72 | 1.59 | 2026-09-11 | closed |
| US5YT=X | United States 5-Year Treasury Yield | 4.79 | 1.12 | 2026-09-11 | closed |
| US7YT=X | United States 7-Year Treasury Yield | 4.87 | 0.84 | 2026-09-11 | closed |
| US10YT=X | United States 10-Year Treasury Yield | 4.97 | 0.57 | 2026-09-11 | closed |
| US20YT=X | United States 20-Year Treasury Yield | 5.39 | 0.14 | 2026-09-11 | closed |
| US30YT=X | United States 30-Year Treasury Yield | 5.36 | -0.08 | 2026-09-11 | closed |
| HK50 | Hang Seng Futures | 24798.0 | 0.36 | 2026-09-11 | closed |
| KOR200c1 | KOSPI 200 Futures | 1098.85 | 0.97 | 2026-09-11 | closed |
| CIHc1 | SSE 50 Futures | 2863.6 | -1.23 | 2026-09-11 | closed |
| HYG | iShares iBoxx High Yield Corporate Bond ETF | 78.6 | -0.03 | 2026-09-11 | closed |
| LQD | iShares iBoxx Investment Grade Corporate Bond ETF | 104.32 | -0.04 | 2026-09-11 | closed |
| JNK | SPDR Bloomberg High Yield Bond ETF | 94.61 | -0.02 | 2026-09-11 | closed |
| RSP | Invesco S&P 500 Equal Weight ETF | 214.87 | 0.8 | 2026-09-11 | closed |
| IWF | iShares Russell 1000 Growth ETF | 122.27 | 0.78 | 2026-09-11 | closed |
| IWD | iShares Russell 1000 Value ETF | 255.58 | 0.89 | 2026-09-11 | closed |
| TLT | iShares 20+ Year Treasury Bond ETF | 80.87 | 0.11 | 2026-09-11 | closed |
| IEF | iShares 7-10 Year Treasury Bond ETF | 91.01 | -0.19 | 2026-09-11 | closed |
| SHY | iShares 1-3 Year Treasury Bond ETF | 81.37 | -0.06 | 2026-09-11 | closed |
| GC=F | Gold Future | 4390.0 | 0.58 | 2026-09-11 | closed |
| SI=F | Silver Future | 65.02 | 1.14 | 2026-09-11 | closed |
| CL=F | WTI Crude Oil Future | 99.99 | -2.43 | 2026-09-11 | closed |
| HG=F | Copper Future | 6.56 | 1.39 | 2026-09-11 | closed |

## Market Dispersion Analysis

- Sector ETF 20D dispersion: `13.91` points (high); leader `XLE` (Energy) `6.68`, laggard `XLI` (Industrials) `-7.22`
- Sector ETF 60D dispersion: `23.59` points (very high); leader `XLE` (Energy) `17.67`, laggard `XLU` (Utilities) `-5.93`

| Comparison | Left | Right | 20D Spread | Signal |
| --- | --- | --- | --- | --- |
| Equal-weight vs cap-weight | RSP (Equal-weight S&P 500) | SPY (S&P 500) | -1.78 | mega-cap concentration |
| Small-cap vs large-cap | IWM (Russell 2000) | SPY (S&P 500) | -3.07 | large-cap leadership |
| Growth vs value | IWF (Russell 1000 Growth) | IWD (Russell 1000 Value) | -1.49 | value leadership |
| Nasdaq vs S&P 500 | QQQ (Nasdaq 100) | SPY (S&P 500) | -0.6 | balanced |

## Sector Constituent Dispersion

- Breadth 50D / 200D: percentage of active S&P 500 constituents in the sector trading above the 50-day / 200-day moving average.
- Positive 20D: percentage of active sector constituents with positive 20-day return.
- Std 20D: cross-sectional standard deviation of constituent 20-day returns; higher means wider stock-level dispersion.

| Sector | Count | Breadth 50D | Breadth 200D | Positive 20D | 20D Dispersion | Std 20D | Label | Leaders | Laggards |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Health Care | 59 | 57.63 | 71.19 | 44.07 | 155.81 | 18.09 | very high | MRNA, IQV, HUM | BSX, SYK, COO |
| Information Technology | 73 | 60.27 | 64.38 | 34.25 | 76.02 | 10.35 | very high | SWKS, CRM, DELL | ADSK, CIEN, APH |
| Consumer Staples | 34 | 36.36 | 40.62 | 35.29 | 39.14 | 7.65 | very high | EL, BG, ADM | HRL, CLX, CASY |
| Consumer Discretionary | 47 | 25.53 | 36.17 | 12.77 | 35.2 | 7.01 | very high | CMG, TSLA, BBY | BKNG, CCL, NCLH |
| Industrials | 83 | 20.48 | 49.37 | 8.43 | 32.48 | 5.36 | very high | DE, RSG, EXPD | BLDR, HWM, AXON |
| Materials | 25 | 32.0 | 56.0 | 24.0 | 32.1 | 8.39 | very high | MOS, CF, NEM | SHW, SW, IP |
| Financials | 76 | 33.33 | 74.65 | 21.05 | 29.11 | 4.93 | very high | COIN, HOOD, PGR | FIS, BX, AON |
| Utilities | 31 | 9.68 | 16.13 | 12.9 | 23.16 | 4.83 | very high | CEG, VST, AWK | D, EIX, PCG |
| Energy | 21 | 80.95 | 80.95 | 80.95 | 20.76 | 5.51 | very high | VLO, DVN, APA | WMB, KMI, BKR |
| Communication Services | 24 | 66.67 | 52.17 | 45.83 | 19.85 | 4.98 | high | META, PSKY, T | LYV, OMC, TTWO |
| Real Estate | 30 | 17.24 | 48.28 | 10.0 | 16.74 | 3.83 | high | ARE, AMT, WELL | INVH, PSA, WY |

## Economic Data Snapshot

### U.S. Labor

| Indicator | Latest | Unit | Change | Date | Rule-Based Interpretation |
| --- | --- | --- | --- | --- | --- |
| All Employees, Total Nonfarm | 159075.0 | thousands | 162.0 thousands vs prior | 2026-08-01 | Higher reading supports activity or liquidity. |
| Unemployment Rate | 4.1 | percent | 0.0 pp vs prior | 2026-08-01 | Stable reading. |
| Initial Claims | 215000.0 | number | -12000.0 number vs prior | 2026-06-20 | Lower claims indicate firmer labor-market conditions. |
| Continued Claims | 1821000.0 | number | 21000.0 number vs prior | 2026-06-13 | Higher claims indicate softer labor-market conditions. |
| Labor Force Participation Rate | 61.6 | percent | 0.2 pp vs prior | 2026-08-01 | Higher participation expands labor supply. |

### U.S. Growth

| Indicator | Latest | Unit | Change | Date | Rule-Based Interpretation |
| --- | --- | --- | --- | --- | --- |
| Real Gross Domestic Product | 24269.61 | billions chained 2017 dollars | 89.19 billions chained 2017 dollars vs prior | 2026-04-01 | Higher reading supports activity or liquidity. |
| Industrial Production Index | 102.65 | index 2017=100 | 0.14 index pts vs prior | 2026-05-01 | Higher reading supports activity or liquidity. |
| Advance Retail Sales | 763602.0 | millions dollars | -4470.0 millions dollars vs prior | 2026-07-01 | Lower reading signals softer activity or liquidity. |

### U.S. Inflation

| Indicator | Latest | Unit | Change | Date | Rule-Based Interpretation |
| --- | --- | --- | --- | --- | --- |
| Headline CPI month-over-month inflation rate | 0.4 | percent | 0.32 pp vs prior | 2026-08-01 | Higher reading increases macro pressure. |
| Headline CPI year-over-year inflation rate | 3.71 | percent | 0.17 pp vs prior | 2026-08-01 | Higher reading increases macro pressure. |
| Core CPI month-over-month inflation rate | 0.29 | percent | 0.07 pp vs prior | 2026-08-01 | Higher reading increases macro pressure. |
| Core CPI year-over-year inflation rate | 2.76 | percent | -0.02 pp vs prior | 2026-08-01 | Lower reading eases macro pressure. |
| Headline CPI year-over-year inflation rate | 3.69 | percent | 0.17 pp vs prior | 2026-08-01 | Higher reading increases macro pressure. |
| Core CPI year-over-year inflation rate | 2.75 | percent | 0.08 pp vs prior | 2026-08-01 | Higher reading increases macro pressure. |
| Headline PCE Price Index month-over-month inflation rate | 0.16 | percent | 0.25 pp vs prior | 2026-07-01 | Higher reading increases macro pressure. |
| Headline PCE Price Index year-over-year inflation rate | 3.7 | percent | -0.02 pp vs prior | 2026-07-01 | Lower reading eases macro pressure. |
| Core PCE Price Index month-over-month inflation rate | 0.25 | percent | 0.1 pp vs prior | 2026-07-01 | Higher reading increases macro pressure. |
| Core PCE Price Index year-over-year inflation rate | 3.34 | percent | 0.0 pp vs prior | 2026-07-01 | Higher reading increases macro pressure. |
| Headline PPI Final Demand month-over-month inflation rate | 0.29 | percent | 0.28 pp vs prior | 2026-08-01 | Higher reading increases macro pressure. |
| Headline PPI Final Demand year-over-year inflation rate | 5.44 | percent | 0.6 pp vs prior | 2026-08-01 | Higher reading increases macro pressure. |
| Core PPI Final Demand Less Foods and Energy month-over-month inflation rate | 0.16 | percent | -0.1 pp vs prior | 2026-08-01 | Lower reading eases macro pressure. |
| Core PPI Final Demand Less Foods and Energy year-over-year inflation rate | 4.62 | percent | 0.37 pp vs prior | 2026-08-01 | Higher reading increases macro pressure. |
| Consumer Price Index for All Urban Consumers | 334.13 | index 1982-1984=100 | 1.32 index pts vs prior | 2026-08-01 | Higher reading increases macro pressure. |
| Core CPI | 337.76 | index 1982-1984=100 | 0.98 index pts vs prior | 2026-08-01 | Higher reading increases macro pressure. |
| Personal Consumption Expenditures Price Index | 131.66 | index 2017=100 | 0.2 index pts vs prior | 2026-07-01 | Higher reading increases macro pressure. |
| Core PCE Price Index | 130.66 | index 2017=100 | 0.32 index pts vs prior | 2026-07-01 | Higher reading increases macro pressure. |
| Producer Price Index: Final Demand | 157.6 | index Nov 2009=100 | 0.45 index pts vs prior | 2026-08-01 | Latest structural macro observation. |
| Producer Price Index: Final Demand Less Foods and Energy | 154.84 | index Apr 2010=100 | 0.25 index pts vs prior | 2026-08-01 | Latest structural macro observation. |

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
| Housing Starts | 1239.0 | thousands | -176.0 thousands vs prior | 2026-07-01 | Lower reading signals softer activity or liquidity. |
| New Privately-Owned Housing Units Authorized | 1433.0 | thousands | 59.0 thousands vs prior | 2026-07-01 | Higher reading supports activity or liquidity. |
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
| US dollar/Euro ECB reference exchange rate | 1.16 | USD | -0.0 USD vs prior | 2026-09-11 | EUR weakened versus this currency. |
| Japanese yen/Euro ECB reference exchange rate | 178.56 | JPY | -0.53 JPY vs prior | 2026-09-11 | EUR weakened versus this currency. |
| Chinese yuan renminbi/Euro ECB reference exchange rate | 7.78 | CNY | -0.01 CNY vs prior | 2026-09-11 | EUR weakened versus this currency. |
| Australian dollar/Euro ECB reference exchange rate | 1.62 | AUD | -0.0 AUD vs prior | 2026-09-11 | EUR weakened versus this currency. |

ABS Australia note: ABS rows are stored locally/Neon, but most series are dimension-coded; only curated series should be promoted into narrative report text.

## Sector and Theme Leadership

### Official Sector Strength

Supporting and detracting names are the top/bottom S&P 500 constituents by 20D return when constituent coverage is available; otherwise the report falls back to related ETFs.

| Rank | Sector | Score | Trend | Momentum | Stock Breadth | ETF Flow | Flow Reliability | 3M RS | Supporting / Leaders | Detracting / Laggards |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Energy | 65.32 | strong uptrend | positive | broad | 42.87 | 65.0 | 61.38 | VLO, DVN, APA | WMB, KMI, BKR |
| 2 | Technology | 61.43 | strong uptrend | neutral | broad | 50.2 | 65.0 | 48.83 | SWKS, CRM, DELL | ADSK, CIEN, APH |
| 3 | Cybersecurity | 56.86 | strong uptrend | neutral | broad | 61.57 | 65.0 | 50.11 | CIBR | CIBR |
| 4 | Financials | 56.78 | strong uptrend | neutral | broad | 56.04 | 65.0 | 51.4 | COIN, HOOD, PGR | FIS, BX, AON |
| 5 | Semiconductors | 52.34 | neutral | neutral | weak | 72.2 | 100.0 | 44.25 | SMH, SOXX | SOXX, SMH |
| 6 | Crypto | 51.23 | neutral | neutral | mixed | 62.33 | 65.0 | 50.0 |  |  |
| 7 | Grid Infrastructure | 48.95 | neutral | neutral | weak | 62.81 | 65.0 | 45.57 | GRID | GRID |
| 8 | Healthcare | 47.35 | neutral | neutral | weak | 57.16 | 65.0 | 52.48 | MRNA, IQV, HUM | BSX, SYK, COO |
| 9 | Consumer Staples | 41.43 | downtrend | neutral | weak | 50.0 | 0.0 | 47.44 | EL, BG, ADM | HRL, CLX, CASY |
| 10 | Industrials | 40.22 | downtrend | neutral | weak | 50.0 | 0.0 | 44.31 | DE, RSG, EXPD | BLDR, HWM, AXON |
| 11 | Real Estate | 39.3 | downtrend | neutral | weak | 32.42 | 65.0 | 46.55 | ARE, AMT, WELL | INVH, PSA, WY |
| 12 | Utilities | 39.08 | strong downtrend | neutral | weak | 50.0 | 0.0 | 45.36 | CEG, VST, AWK | D, EIX, PCG |
| 13 | Nuclear | 34.55 | strong downtrend | neutral | weak | 50.0 | 0.0 | 43.97 | NLR | NLR |
| 14 | Consumer Discretionary | 34.53 | strong downtrend | neutral | weak | 50.0 | 0.0 | 45.67 | CMG, TSLA, BBY | BKNG, CCL, NCLH |
| 15 | Defense | 31.19 | strong downtrend | negative | weak | 50.0 | 0.0 | 35.74 | XAR | XAR |

### Thematic Strength

| Rank | Theme | Score | Setup | ETF Flow | Flow Reliability | Dispersion | Price | News |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Energy | 60.87 | Positive setup | 42.87 | 65.0 | 3.62 | True | False |
| 2 | Quality Growth | 56.41 | Positive setup | 48.65 | 65.0 | 11.2 | False | False |
| 3 | Financials | 55.14 | Positive setup | 56.04 | 65.0 | 0.89 | False | False |
| 4 | AI Infrastructure | 54.95 | Neutral / watchlist | 72.2 | 100.0 | 4.05 | False | False |
| 5 | Crypto Infrastructure | 52.29 | Neutral / watchlist | 62.33 | 65.0 | 21.0 | False | False |
| 6 | Semiconductors | 51.9 | Neutral / watchlist | 72.2 | 100.0 | 20.22 | False | False |
| 7 | Healthcare Innovation | 50.65 | Neutral / watchlist | 57.16 | 65.0 | 13.9 | False | False |
| 8 | Grid Infrastructure | 48.06 | Neutral / watchlist | 62.81 | 65.0 | 2.87 | False | False |
| 9 | Cybersecurity | 47.01 | Neutral / watchlist | 61.57 | 65.0 | 10.84 | False | False |
| 10 | Small Caps | 45.06 | Neutral / watchlist | 53.96 | 65.0 | 0.0 | False | False |
| 11 | Dividend Defensives | 42.61 | Neutral / watchlist | 61.42 | 65.0 | 1.95 | False | False |
| 12 | Nuclear | 35.06 | Weak setup | 50.0 | 0.0 | 19.5 | False | False |
| 13 | Defense | 33.21 | Weak setup | 50.0 | 0.0 | 12.85 | False | False |

- Top 5 improving themes: Energy, Healthcare Innovation, Quality Growth, Crypto Infrastructure, Financials
- Top 5 deteriorating themes: Nuclear, Defense, Grid Infrastructure, Semiconductors, Small Caps
- Strong news but weak price confirmation: none
- Strong price but weak news confirmation: Energy

### Sector / Theme Alignment

| Sector | Related Themes | Sector Score | Sector Signal | Theme Score | Theme Signal | Interpretation |
| --- | --- | --- | --- | --- | --- | --- |
| Energy | Energy | 65.32 | strong | 60.87 | positive | sector and theme confirmation |
| Technology | AI Infrastructure, Semiconductors, Quality Growth | 61.43 | positive | 54.42 | mixed | sector stronger than related themes |
| Cybersecurity | Cybersecurity | 56.86 | positive | 47.01 | mixed | sector stronger than related themes |
| Financials | Financials | 56.78 | positive | 55.14 | positive | sector and theme confirmation |
| Semiconductors | AI Infrastructure, Semiconductors | 52.34 | mixed | 53.42 | mixed | mixed confirmation |
| Crypto | Crypto Infrastructure | 51.23 | mixed | 52.29 | mixed | mixed confirmation |
| Grid Infrastructure | Grid Infrastructure | 48.95 | mixed | 48.06 | mixed | mixed confirmation |
| Healthcare | Healthcare Innovation | 47.35 | mixed | 50.65 | mixed | mixed confirmation |
| Consumer Staples | Dividend Defensives | 41.43 | weak | 42.61 | weak | broad weakness across sector and themes |
| Industrials | Defense, Grid Infrastructure | 40.22 | weak | 40.64 | weak | broad weakness across sector and themes |
| Real Estate | Dividend Defensives | 39.3 | weak | 42.61 | weak | broad weakness across sector and themes |
| Utilities | Grid Infrastructure, Nuclear, Dividend Defensives | 39.08 | weak | 41.91 | weak | broad weakness across sector and themes |
| Nuclear | Nuclear | 34.55 | very weak | 35.06 | weak | broad weakness across sector and themes |
| Consumer Discretionary | Small Caps | 34.53 | very weak | 45.06 | mixed | mixed confirmation |
| Defense | Defense | 31.19 | very weak | 33.21 | very weak | broad weakness across sector and themes |

## Three-Month Outperformance Setup

| Rank | Theme | Score | Classification | Drivers | Invalidation Triggers |
| --- | --- | --- | --- | --- | --- |
| 1 | Energy | 69.43 | Positive setup | relative_strength_60d, trend_persistence, breadth, downside_volatility, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 2 | Quality Growth | 62.81 | Positive setup | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 3 | Financials | 61.31 | Positive setup | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 4 | AI Infrastructure | 58.14 | Neutral / watchlist | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 5 | Healthcare Innovation | 57.81 | Neutral / watchlist | trend_persistence, breadth, downside_volatility, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 6 | Crypto Infrastructure | 52.96 | Neutral / watchlist | relative_strength_20d | relative strength below SPY, breadth below 45%, news turns negative |
| 7 | Semiconductors | 52.46 | Neutral / watchlist | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 8 | Small Caps | 51.82 | Neutral / watchlist | volume_accumulation, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 9 | Cybersecurity | 48.59 | Neutral / watchlist | trend_persistence, breadth | relative strength below SPY, breadth below 45%, news turns negative |
| 10 | Grid Infrastructure | 48.13 | Neutral / watchlist | downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 11 | Dividend Defensives | 45.93 | Neutral / watchlist | downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 12 | Defense | 36.48 | Weak setup | downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |

## Breadth and Participation

- Above 50DMA: `46.67%`
- Above 200DMA: `69.49%`
- Positive 20D return: `18.33%`

## Volatility and Risk Signals

- VIX close=15.84 pct_chg=-11.21

## News Analytics

- Sentiment counts: {'positive': 47, 'negative': 28, 'neutral': 5}
- News confirmation score: `61.88`

### Top Market-Moving Headlines

**1. The Houthis have opened a new front in the Middle East oil war that’s pushing up prices**
- Source: MarketWatch Top Stories
- Importance / impact: High / Negative
- Relevance / horizon: macro / short-term
- Affected assets: A, geopolitical, oil, pipelines
- Score: `51.0`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the short-term.

**2. Trump's America-first world is pushing other powers to hedge their bets**
- Source: CNBC Business Headlines
- Importance / impact: High / Negative
- Relevance / horizon: macro / short-term
- Affected assets: BRICS, U.S, geopolitics, trade, international relations
- Score: `48.0`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the short-term.

**3. Why Dell and HPE were the S&P 500’s top-performing stocks today**
- Source: MarketWatch Top Stories
- Importance / impact: Medium / Positive
- Relevance / horizon: macro / short-term
- Affected assets: HPE, P, S, earnings, hardware
- Score: `44.2`
- Investment implication: Macro-relevant positive signal; use as context for rates, volatility, and index confirmation over the short-term.

**4. Investors have all but concluded the Federal Reserve will raise interest rates next week for the first time in three years. The harder question is what comes after that.**
- Source: Dow Jones Economy
- Importance / impact: Medium / Negative
- Relevance / horizon: macro / short-term
- Affected assets: Federal Reserve, interest rates, economic policy
- Score: `43.35`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the short-term.

**5. Saudi Arabia shut down East-West crude oil pipeline after multiple attacks by drones from Iraq**
- Source: CNBC Top News
- Importance / impact: Medium / Negative
- Relevance / horizon: macro / short-term
- Affected assets: SPY, DIA, oil pipeline, Saudi Arabia, attacks
- Score: `42.39`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the short-term.

**6. Oil prices fall Friday, but post sharp weekly gains as tensions in the Middle East rise**
- Source: CNBC Top News
- Importance / impact: Medium / Negative
- Relevance / horizon: macro / short-term
- Affected assets: WTI, oil, commodity, price_change
- Score: `38.76`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the short-term.

**7. The Fed could raise interest rates three times. Here’s where the market could face the stiffest test.**
- Source: MarketWatch Top Stories
- Importance / impact: Medium / Negative
- Relevance / horizon: macro / short-term
- Affected assets: central banking, economic policy
- Score: `38.67`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the short-term.

**8. For most Americans, oil-fueled inflation shows up most quickly in their gas tanks. The big question is whether fuel prices will eventually start increasing prices for other goods and services.**
- Source: Dow Jones Economy
- Importance / impact: Medium / Negative
- Relevance / horizon: macro / short-term
- Affected assets: inflation, oil_prices
- Score: `37.57`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the short-term.

**9. As the Houthis open a new front in the Middle East war, oil prices are rising**
- Source: MarketWatch Bulletins
- Importance / impact: Medium / Positive
- Relevance / horizon: macro / short-term
- Affected assets: CL=F, OIL, conflict, geo-political, oil_market
- Score: `36.74`
- Investment implication: Macro-relevant positive signal; use as context for rates, volatility, and index confirmation over the short-term.

**10. Stocks stumble on inflation fears, but 2 of our names give us reasons to stay bullish**
- Source: CNBC Markets
- Importance / impact: Medium / Negative
- Relevance / horizon: macro / short-term
- Affected assets: inflation
- Score: `36.58`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the short-term.


### Headline Quality Checks

No noisy headlines detected by current rules.

## Positioning & Flow Dashboard

Positioning and flow data is used as confirmation only.

### Deferred Flow Sections

- Official ETF / fund flows: current report uses shares-outstanding-derived net fund flow estimates from free ETF metadata.
- Institutional Ownership: not available until SEC 13F ingestion is implemented.
- Grouped exposure flow reliability: use issuer coverage and availability status before treating ETF flow as confirmation.

## ETF Flows Analysis

- Market flow regime: `Mixed / Neutral`
- Market flow score: `45.2 / 100`
- Equity risk flow: `45.4`
- Credit risk flow: `26.8`
- Sector cyclicality flow: `50.4`
- Duration/liquidity flow: `52.5`
- Alternatives: `barbell demand`
- ETF flow reliability: `66.9 / 100`
- Dominant allocation direction: `defensive demand`

### Core Flow Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVV | U.S. Broad Equity | -2.1 | -0.6 | 0.1 | 0.1 | Down | Sell | Normal | Persistent Distribution | Risk-Off | Medium-term deterioration; Exceptional institutional selling, Persistent selling | 67.0 |
| ACWI | Global Equity | -0.7 | -1.1 | 0.0 | -0.3 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Mixed or neutral flow structure; Persistent selling | 77.0 |
| EFA | Developed Markets ex-U.S. | -0.1 | -0.1 | 0.0 | -0.1 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Mixed or neutral flow structure; Persistent selling | 77.0 |
| IEMG | Emerging Markets | -0.0 | 0.3 | 0.2 | -1.0 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural accumulation; Persistent selling | 83.0 |
| IJH | U.S. Mid Cap | 1.2 | 1.5 | 0.9 | -0.2 | Down | Buy | Normal | Contrarian Buying | Watch | Strong confirmation; Strong sponsorship | 100.0 |
| IWM | U.S. Small Cap | 0.1 | -0.8 | 0.3 | 0.9 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural distribution | 79.0 |
| LQD | Investment-Grade Credit | -1.9 | -1.2 | 0.3 | -0.1 | Down | Sell | Normal | Persistent Distribution | Risk-Off | Strong confirmation; Exceptional institutional selling | 87.0 |
| HYG | High-Yield Credit | -2.5 | -1.5 | 0.1 | 0.8 | Down | Sell | Normal | Persistent Distribution | Risk-Off | Strong confirmation; Exceptional institutional selling, Persistent selling | 79.0 |
| SGOV | Treasury Bills / Cash | 0.4 | -0.9 | 0.9 | -0.1 | Flat | Buy | Normal | Quiet Accumulation | Improving | Strong confirmation; Strong sponsorship | 100.0 |
| SHY | Short-Duration Treasuries | 0.6 | -0.0 | 0.5 | 1.5 | Flat | Sell | High | Distribution Before Breakdown | Early Bearish | Tactical profit-taking inside structural accumulation | 83.0 |
| IEF | Intermediate-Duration Treasuries | -0.2 | -1.4 | 0.5 | 0.3 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural distribution | 79.0 |
| TLT | Long-Duration Treasuries | 0.8 | 2.8 | 0.6 | 0.3 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural accumulation; Exceptional institutional buying | 99.0 |
| GLD | Gold | 1.4 | 2.6 | 0.5 | 0.4 | Flat | Sell | Normal | Quiet Distribution | Weakening | Tactical profit-taking inside structural accumulation | 83.0 |
| IBIT | Bitcoin | 1.7 | 0.8 | 0.7 | 0.0 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural accumulation | 91.0 |

### Sector Flow Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| XLC | Communication Services | 0.9 | 0.2 | 0.4 | -0.4 | Flat | Neutral | Normal | Neutral | Neutral | Medium-term recovery | 87.0 |
| XLY | Consumer Discretionary | -2.0 | -0.3 | 0.2 | -0.5 | Down | Sell | Normal | Persistent Distribution | Risk-Off | Strong confirmation; Exceptional institutional selling, Persistent selling | 79.0 |
| XLP | Consumer Staples | -0.8 | 1.6 | 0.4 | -0.1 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Medium-term deterioration | 83.0 |
| XLE | Energy | -0.3 | -0.5 | 0.5 | 1.3 | Up | Neutral | High | Momentum Rally | Watch | Structural distribution | 79.0 |
| XLF | Financials | -1.1 | 0.3 | 0.4 | -0.8 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Medium-term deterioration | 83.0 |
| XLV | Health Care | -0.1 | 1.3 | 0.6 | -0.6 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Medium-term deterioration | 83.0 |
| XLI | Industrials | -1.8 | -0.5 | 0.3 | 0.5 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Medium-term deterioration | 83.0 |
| XLK | Information Technology | -0.4 | -1.0 | 0.5 | -1.0 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural distribution | 79.0 |
| XLB | Materials | -0.9 | -1.5 | 0.3 | -0.6 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural distribution | 79.0 |
| XLRE | Real Estate | -1.5 | -0.1 | 0.2 | -0.3 | Down | Sell | Normal | Persistent Distribution | Risk-Off | Medium-term deterioration; Persistent selling | 75.0 |
| XLU | Utilities | -0.1 | 0.4 | 0.5 | 0.1 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural accumulation | 91.0 |

### Subsector PFV Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ITA | Aerospace and Defense | -0.3 | 1.1 | 0.1 | -0.1 | Down | Sell | Normal | Persistent Distribution | Risk-Off | Medium-term deterioration; Persistent selling | 75.0 |
| SOXX | Semiconductors | 0.1 | -0.7 | 0.5 | -1.1 | Flat | Neutral | Normal | Neutral | Neutral | Structural accumulation | 91.0 |
| SMH | Semiconductors | -0.3 | 0.5 | 0.5 | -0.8 | Flat | Neutral | Normal | Neutral | Neutral | Structural accumulation | 91.0 |
| CIBR | Cybersecurity | 0.8 | 1.8 | 0.6 | -0.7 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural accumulation | 91.0 |

### Material Flow Divergences

| Severity | Type | Primary | Comparison | Interpretation |
| --- | --- | --- | --- | --- |
| high | close_substitute_divergence | GLD | IAU | primary representative differs from close substitute |
| high | close_substitute_divergence | AGG | IUSB | primary representative differs from close substitute |
| high | close_substitute_divergence | IWF | IVW | primary representative differs from close substitute |
| high | close_substitute_divergence | IWD | IVE | primary representative differs from close substitute |
| high | close_substitute_divergence | SOXX | SMH | primary representative differs from close substitute |
| high | close_substitute_divergence | IWM | IJR | primary representative differs from close substitute |


## Contradiction / Audit Flags

No contradiction flags were triggered by current deterministic rules.

## Data Quality Notes

- Technical rows loaded: `60`
- S&P 500 constituent technical rows loaded: `503`
- Macro rows loaded: `49`
- Live macro rows used: `2`
- Economic rows loaded: `113`
- News rows loaded: `80`
- Positioning/flow rows loaded: `30`

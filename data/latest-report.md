# Rule-Based Institutional Market Update

Generated at: 15 September 2026, 08:43:49 (HKT)
Window: 24h

## Executive Dashboard

- Regime score: **47.5 / 100** (Mixed / Rotation)
- US equity strength: **47.29 / 100** (neutral)
- Evidence quality: **69.0 / 100**
- ETF flow contribution: **47.26 / 100**, reliability **65.94 / 100**
- Breadth: **narrow**; above 50DMA `33.33%`, above 200DMA `69.49%`
- Top sector score: **Cybersecurity** `65.87`
- Top theme score: **Energy** `60.86`

## Market Regime Score

| Metric | Value | Driver / Interpretation |
| --- | --- | --- |
| Overall regime | 47.5 | Mixed / Rotation |
| equity_trend | 46.25 | neutral / mixed; Core equity ETFs versus moving averages. |
| equity_momentum | 46.4 | neutral / mixed; 5D/20D/60D return momentum across SPY, QQQ, IWM, and SMH. |
| market_breadth | 43.16 | mild risk-off pressure; Participation breadth from tracked equity/ETF rows. |
| volatility | 35.0 | risk-off pressure; VIX level and change; higher score means calmer volatility conditions. |
| rates_yield_curve | 58.0 | mild risk-on support; Treasury yield pressure and curve shape; higher score means less rates pressure. |
| credit_proxy | 50.0 | neutral / mixed; Credit-market proxy; currently neutral when no direct spread signal is available. |
| dollar_fx | 53.34 | neutral / mixed; Dollar move; higher score means less USD tightening pressure. |
| commodity_confirmation | 46.0 | neutral / mixed; Copper, silver, oil, and gold mix; higher score means better cyclical confirmation. |
| etf_flow | 48.19 | neutral / mixed; Grouped ETF flow contribution adjusted for reliability. |
| news_confirmation | 55.62 | mild risk-on support; Weighted headline/news confirmation score. |
| Positive contributors |  | none |
| Negative contributors |  | volatility=35.0, market_breadth=43.16 |

## US Equity Strength Score

| Component | Score |
| --- | --- |
| indices_above_moving_averages | 46.25 |
| sp500_trend | 80.0 |
| nasdaq_trend | 35.0 |
| russell_participation | 35.0 |
| returns_momentum | 46.4 |
| rsi_zone | 47.5 |
| macd_confirmation | 43.75 |
| volume_confirmation | 42.5 |
| breadth | 43.16 |

## Evidence Quality / Confidence

- Confidence score: `69.0`
- Agreement ratio: `0.2`
- Contradiction count: `2`
- Missing indicators: none
- Warning flags: none

## Cross-Asset Confirmation

| Area | Signal | Interpretation |
| --- | --- | --- |
| Equities | S&P 500 falling; Nasdaq falling; Russell 2000 falling | Confirms risk appetite when broad indices rise together; weak small caps would narrow the signal. |
| Rates | 10Y Treasury falling; MOVE rising | Rising yields can pressure duration assets; falling MOVE supports calmer bond volatility. |
| Dollar | DXY proxy rising | A stronger dollar can tighten financial conditions and pressure commodities/emerging-market risk. |
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
| ^GSPC | S&P 500 | 7619.98 | -0.48 | 2026-09-14 | closed |
| ^IXIC | NASDAQ Composite | 26186.41 | -0.56 | 2026-09-14 | closed |
| ^RUT | Russell 2000 Index | 2892.24 | -0.4 | 2026-09-14 | closed |
| ^VIX | CBOE Volatility Index | 17.1 | 7.95 | 2026-09-14 | closed |
| ^SKEW | CBOE SKEW Index | 152.09 | -1.55 | 2026-09-14 | closed |
| ^MOVE | ICE BofA MOVE Index | 83.9 | 2.06 | 2026-09-14 | closed |
| US2YT=X | United States 2-Year Treasury Yield | 4.65 | 0.09 | 2026-09-15 | live as of 15 September 2026, 08:30:22 (HKT) |
| US3YT=X | United States 3-Year Treasury Yield | 4.75 | 0.15 | 2026-09-15 | live as of 15 September 2026, 08:30:22 (HKT) |
| US5YT=X | United States 5-Year Treasury Yield | 4.82 | 0.15 | 2026-09-15 | live as of 15 September 2026, 08:30:22 (HKT) |
| US7YT=X | United States 7-Year Treasury Yield | 4.9 | 0.11 | 2026-09-15 | live as of 15 September 2026, 08:30:22 (HKT) |
| US10YT=X | United States 10-Year Treasury Yield | 4.99 | 0.19 | 2026-09-15 | live as of 15 September 2026, 08:30:22 (HKT) |
| US20YT=X | United States 20-Year Treasury Yield | 5.39 | 0.15 | 2026-09-15 | live as of 15 September 2026, 08:30:22 (HKT) |
| US30YT=X | United States 30-Year Treasury Yield | 5.35 | 0.14 | 2026-09-15 | live as of 15 September 2026, 08:30:22 (HKT) |
| HK50 | Hang Seng Futures | 24873.0 | 0.32 | 2026-09-14 | closed |
| KOR200c1 | KOSPI 200 Futures | 1098.85 | 0.97 | 2026-09-11 | closed |
| CIHc1 | SSE 50 Futures | 2863.6 | -1.23 | 2026-09-11 | closed |
| HYG | iShares iBoxx High Yield Corporate Bond ETF | 78.53 | -0.09 | 2026-09-14 | closed |
| LQD | iShares iBoxx Investment Grade Corporate Bond ETF | 104.3 | -0.02 | 2026-09-14 | closed |
| JNK | SPDR Bloomberg High Yield Bond ETF | 94.49 | -0.13 | 2026-09-14 | closed |
| RSP | Invesco S&P 500 Equal Weight ETF | 215.01 | 0.07 | 2026-09-14 | closed |
| IWF | iShares Russell 1000 Growth ETF | 121.26 | -0.83 | 2026-09-14 | closed |
| IWD | iShares Russell 1000 Value ETF | 255.37 | -0.08 | 2026-09-14 | closed |
| TLT | iShares 20+ Year Treasury Bond ETF | 80.93 | 0.07 | 2026-09-14 | closed |
| IEF | iShares 7-10 Year Treasury Bond ETF | 90.93 | -0.09 | 2026-09-14 | closed |
| SHY | iShares 1-3 Year Treasury Bond ETF | 81.34 | -0.04 | 2026-09-14 | closed |
| GC=F | Gold Future | 4340.0 | -1.56 | 2026-09-14 | closed |
| SI=F | Silver Future | 63.76 | -1.24 | 2026-09-14 | closed |
| CL=F | WTI Crude Oil Future | 102.68 | 0.51 | 2026-09-15 | live as of 15 September 2026, 08:30:22 (HKT) |
| HG=F | Copper Future | 6.4 | -1.11 | 2026-09-14 | closed |

## Market Dispersion Analysis

- Sector ETF 20D dispersion: `13.12` points (high); leader `XLE` (Energy) `4.23`, laggard `XLI` (Industrials) `-8.89`
- Sector ETF 60D dispersion: `23.97` points (very high); leader `XLE` (Energy) `18.04`, laggard `XLU` (Utilities) `-5.94`

| Comparison | Left | Right | 20D Spread | Signal |
| --- | --- | --- | --- | --- |
| Equal-weight vs cap-weight | RSP (Equal-weight S&P 500) | SPY (S&P 500) | -1.49 | mega-cap concentration |
| Small-cap vs large-cap | IWM (Russell 2000) | SPY (S&P 500) | -3.64 | large-cap leadership |
| Growth vs value | IWF (Russell 1000 Growth) | IWD (Russell 1000 Value) | -1.98 | value leadership |
| Nasdaq vs S&P 500 | QQQ (Nasdaq 100) | SPY (S&P 500) | -1.0 | S&P 500 leadership |

## Sector Constituent Dispersion

- Breadth 50D / 200D: percentage of active S&P 500 constituents in the sector trading above the 50-day / 200-day moving average.
- Positive 20D: percentage of active sector constituents with positive 20-day return.
- Std 20D: cross-sectional standard deviation of constituent 20-day returns; higher means wider stock-level dispersion.

| Sector | Count | Breadth 50D | Breadth 200D | Positive 20D | 20D Dispersion | Std 20D | Label | Leaders | Laggards |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Health Care | 59 | 67.8 | 74.58 | 49.15 | 160.48 | 18.53 | very high | MRNA, IQV, RVTY | ALGN, SYK, COO |
| Information Technology | 73 | 50.68 | 63.01 | 31.51 | 85.22 | 11.97 | very high | CRM, NOW, SWKS | TER, CIEN, APH |
| Financials | 76 | 34.67 | 80.28 | 19.74 | 41.4 | 5.94 | very high | COIN, HOOD, JKHY | FIS, PYPL, AON |
| Consumer Staples | 34 | 39.39 | 46.88 | 35.29 | 40.64 | 7.76 | very high | EL, MO, ADM | HRL, CLX, CASY |
| Industrials | 83 | 18.07 | 44.3 | 10.84 | 33.38 | 6.38 | very high | DE, CHRW, RSG | GNRC, AXON, HWM |
| Consumer Discretionary | 47 | 27.66 | 36.17 | 12.77 | 33.1 | 7.06 | very high | CMG, BBY, ULTA | BKNG, CCL, NCLH |
| Materials | 25 | 32.0 | 56.0 | 20.0 | 31.85 | 7.68 | very high | MOS, CF, CTVA | SW, ALB, IP |
| Utilities | 31 | 6.45 | 12.9 | 6.45 | 25.76 | 5.05 | very high | AWK, AES, AEP | NRG, EIX, PCG |
| Energy | 21 | 76.19 | 76.19 | 71.43 | 24.49 | 6.09 | very high | VLO, MPC, APA | WMB, KMI, BKR |
| Communication Services | 24 | 66.67 | 60.87 | 62.5 | 22.58 | 5.78 | very high | META, PSKY, T | RDDT, LYV, TTWO |
| Real Estate | 30 | 10.34 | 48.28 | 6.67 | 21.36 | 4.05 | very high | ARE, AMT, VMRK | WY, DLR, IRM |

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
| US dollar/Euro ECB reference exchange rate | 1.16 | USD | -0.0 USD vs prior | 2026-09-14 | EUR weakened versus this currency. |
| Japanese yen/Euro ECB reference exchange rate | 178.52 | JPY | -0.04 JPY vs prior | 2026-09-14 | EUR weakened versus this currency. |
| Chinese yuan renminbi/Euro ECB reference exchange rate | 7.75 | CNY | -0.03 CNY vs prior | 2026-09-14 | EUR weakened versus this currency. |
| Australian dollar/Euro ECB reference exchange rate | 1.62 | AUD | 0.0 AUD vs prior | 2026-09-14 | EUR strengthened versus this currency. |

ABS Australia note: ABS rows are stored locally/Neon, but most series are dimension-coded; only curated series should be promoted into narrative report text.

## Sector and Theme Leadership

### Official Sector Strength

Supporting and detracting names are the top/bottom S&P 500 constituents by 20D return when constituent coverage is available; otherwise the report falls back to related ETFs.

| Rank | Sector | Score | Trend | Momentum | Stock Breadth | ETF Flow | Flow Reliability | 3M RS | Supporting / Leaders | Detracting / Laggards |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Cybersecurity | 65.87 | strong uptrend | positive | broad | 50.0 | 0.0 | 57.9 | CIBR | CIBR |
| 2 | Energy | 64.49 | strong uptrend | positive | broad | 28.23 | 65.0 | 59.87 | VLO, MPC, APA | WMB, KMI, BKR |
| 3 | Healthcare | 58.48 | strong uptrend | neutral | broad | 65.55 | 65.0 | 54.78 | MRNA, IQV, RVTY | ALGN, SYK, COO |
| 4 | Crypto | 51.17 | neutral | neutral | mixed | 61.72 | 65.0 | 50.0 |  |  |
| 5 | Technology | 50.27 | neutral | neutral | mixed | 44.06 | 65.0 | 47.78 | CRM, NOW, SWKS | TER, CIEN, APH |
| 6 | Financials | 46.77 | neutral | neutral | weak | 55.49 | 65.0 | 51.16 | COIN, HOOD, JKHY | FIS, PYPL, AON |
| 7 | Semiconductors | 42.4 | downtrend | negative | weak | 63.06 | 65.0 | 38.81 | SMH, SOXX | SOXX, SMH |
| 8 | Consumer Staples | 42.08 | downtrend | neutral | weak | 50.0 | 0.0 | 49.31 | EL, MO, ADM | HRL, CLX, CASY |
| 9 | Utilities | 35.27 | strong downtrend | negative | weak | 50.0 | 0.0 | 43.02 | AWK, AES, AEP | NRG, EIX, PCG |
| 10 | Consumer Discretionary | 34.81 | strong downtrend | neutral | weak | 50.0 | 0.0 | 46.49 | CMG, BBY, ULTA | BKNG, CCL, NCLH |
| 11 | Industrials | 33.35 | strong downtrend | negative | weak | 50.0 | 0.0 | 42.63 | DE, CHRW, RSG | GNRC, AXON, HWM |
| 12 | Grid Infrastructure | 32.77 | strong downtrend | negative | weak | 50.0 | 0.0 | 41.59 | GRID | GRID |
| 13 | Nuclear | 32.68 | strong downtrend | negative | weak | 50.0 | 0.0 | 40.86 | NLR | NLR |
| 14 | Real Estate | 32.27 | strong downtrend | neutral | weak | 34.85 | 65.0 | 46.5 | ARE, AMT, VMRK | WY, DLR, IRM |
| 15 | Defense | 29.43 | strong downtrend | negative | weak | 50.0 | 0.0 | 33.23 | XAR | XAR |

### Thematic Strength

| Rank | Theme | Score | Setup | ETF Flow | Flow Reliability | Dispersion | Price | News |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Energy | 60.86 | Positive setup | 28.23 | 65.0 | 2.97 | True | False |
| 2 | Crypto Infrastructure | 60.8 | Positive setup | 61.72 | 65.0 | 18.24 | True | False |
| 3 | Cybersecurity | 60.68 | Positive setup | 50.0 | 0.0 | 11.18 | True | False |
| 4 | Quality Growth | 57.38 | Positive setup | 47.81 | 65.0 | 11.89 | False | False |
| 5 | Healthcare Innovation | 53.7 | Positive setup | 65.55 | 65.0 | 11.16 | False | False |
| 6 | AI Infrastructure | 52.37 | Neutral / watchlist | 63.06 | 65.0 | 11.65 | False | False |
| 7 | Financials | 47.52 | Neutral / watchlist | 55.49 | 65.0 | 5.84 | False | True |
| 8 | Semiconductors | 45.72 | Neutral / watchlist | 63.06 | 65.0 | 12.63 | False | False |
| 9 | Small Caps | 45.62 | Neutral / watchlist | 63.03 | 65.0 | 0.0 | False | False |
| 10 | Dividend Defensives | 45.14 | Neutral / watchlist | 55.13 | 65.0 | 5.85 | False | False |
| 11 | Grid Infrastructure | 38.36 | Weak setup | 50.0 | 0.0 | 7.3 | False | False |
| 12 | Defense | 34.07 | Weak setup | 50.0 | 0.0 | 10.46 | False | False |
| 13 | Nuclear | 31.92 | Weak setup | 50.0 | 0.0 | 18.5 | False | False |

- Top 5 improving themes: Energy, Crypto Infrastructure, Cybersecurity, Healthcare Innovation, Quality Growth
- Top 5 deteriorating themes: Nuclear, Semiconductors, Grid Infrastructure, Defense, Small Caps
- Strong news but weak price confirmation: Financials
- Strong price but weak news confirmation: Energy, Crypto Infrastructure, Cybersecurity

### Sector / Theme Alignment

| Sector | Related Themes | Sector Score | Sector Signal | Theme Score | Theme Signal | Interpretation |
| --- | --- | --- | --- | --- | --- | --- |
| Cybersecurity | Cybersecurity | 65.87 | strong | 60.68 | positive | sector and theme confirmation |
| Energy | Energy | 64.49 | positive | 60.86 | positive | sector and theme confirmation |
| Healthcare | Healthcare Innovation | 58.48 | positive | 53.7 | mixed | sector stronger than related themes |
| Crypto | Crypto Infrastructure | 51.17 | mixed | 60.8 | positive | theme stronger than official sector |
| Technology | AI Infrastructure, Semiconductors, Quality Growth | 50.27 | mixed | 51.82 | mixed | mixed confirmation |
| Financials | Financials | 46.77 | mixed | 47.52 | mixed | mixed confirmation |
| Semiconductors | AI Infrastructure, Semiconductors | 42.4 | weak | 49.04 | mixed | mixed confirmation |
| Consumer Staples | Dividend Defensives | 42.08 | weak | 45.14 | mixed | mixed confirmation |
| Utilities | Grid Infrastructure, Nuclear, Dividend Defensives | 35.27 | weak | 38.47 | weak | broad weakness across sector and themes |
| Consumer Discretionary | Small Caps | 34.81 | very weak | 45.62 | mixed | mixed confirmation |
| Industrials | Defense, Grid Infrastructure | 33.35 | very weak | 36.22 | weak | broad weakness across sector and themes |
| Grid Infrastructure | Grid Infrastructure | 32.77 | very weak | 38.36 | weak | broad weakness across sector and themes |
| Nuclear | Nuclear | 32.68 | very weak | 31.92 | very weak | broad weakness across sector and themes |
| Real Estate | Dividend Defensives | 32.27 | very weak | 45.14 | mixed | mixed confirmation |
| Defense | Defense | 29.43 | very weak | 34.07 | very weak | broad weakness across sector and themes |

## Three-Month Outperformance Setup

| Rank | Theme | Score | Classification | Drivers | Invalidation Triggers |
| --- | --- | --- | --- | --- | --- |
| 1 | Energy | 70.18 | Positive setup | relative_strength_60d, trend_persistence, breadth, volume_accumulation, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 2 | Cybersecurity | 66.27 | Positive setup | trend_persistence, breadth, volume_accumulation, drawdown_recovery, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 3 | Crypto Infrastructure | 65.67 | Positive setup | relative_strength_20d, relative_strength_60d, trend_persistence, breadth, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 4 | Quality Growth | 64.17 | Positive setup | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 5 | Healthcare Innovation | 60.32 | Positive setup | trend_persistence, breadth, downside_volatility, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 6 | AI Infrastructure | 55.96 | Neutral / watchlist | trend_persistence, breadth, volume_accumulation, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 7 | Dividend Defensives | 51.63 | Neutral / watchlist | downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 8 | Small Caps | 51.26 | Neutral / watchlist | volume_accumulation, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 9 | Financials | 50.19 | Neutral / watchlist | volume_accumulation, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 10 | Semiconductors | 46.29 | Neutral / watchlist | volume_accumulation, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 11 | Grid Infrastructure | 40.03 | Weak setup | volume_accumulation, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 12 | Defense | 36.46 | Weak setup | downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |

## Breadth and Participation

- Above 50DMA: `33.33%`
- Above 200DMA: `69.49%`
- Positive 20D return: `26.67%`

## Volatility and Risk Signals

- VIX close=17.1 pct_chg=7.95

## News Analytics

- Sentiment counts: {'positive': 42, 'negative': 33, 'neutral': 5}
- News confirmation score: `55.62`

### Top Market-Moving Headlines

**1. The Fed may be on the verge of a serious mistake, prominent economists warn**
- Source: MarketWatch Bulletins
- Importance / impact: High / Negative
- Relevance / horizon: macro / short-term
- Affected assets: Economic Policy, Federal Reserve
- Score: `72.67`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the short-term.

**2. Oil prices rise after Saudi Arabia shuts down critical pipeline that bypasses Strait of Hormuz**
- Source: CNBC Top News
- Importance / impact: High / Positive
- Relevance / horizon: macro / short-term
- Affected assets: oil, pipeline, Saudi Arabia
- Score: `72.67`
- Investment implication: Macro-relevant positive signal; use as context for rates, volatility, and index confirmation over the short-term.

**3. Saudi Arabia may be just days away from not being able to export much oil**
- Source: MarketWatch Top Stories
- Importance / impact: High / Negative
- Relevance / horizon: macro / short-term
- Affected assets: oil, pipeline shutdown, energy prices
- Score: `68.0`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the short-term.

**4. Up 3,600%, this freight fund has posted the biggest gains of all on Iran war oil shock**
- Source: CNBC Markets
- Importance / impact: High / Positive
- Relevance / horizon: macro / short-term
- Affected assets: U.S, oil, shipping, war
- Score: `61.77`
- Investment implication: Macro-relevant positive signal; use as context for rates, volatility, and index confirmation over the short-term.

**5. The oil market is sending an increasingly loud warning about gas prices at the pump**
- Source: MarketWatch Top Stories
- Importance / impact: High / Negative
- Relevance / horizon: macro / short-term
- Affected assets: oil market, gas prices, supply concerns
- Score: `60.0`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the short-term.

**6. 10-year Treasury yield hits 5% as oil prices jump and Fed meeting looms**
- Source: MarketWatch Top Stories
- Importance / impact: High / Negative
- Relevance / horizon: macro / short-term
- Affected assets: interest_rates, bond_market, economic_indicators
- Score: `60.0`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the short-term.

**7. CrowdStrike and Palo Alto Networks lead software stocks to a never-before-seen feat**
- Source: MarketWatch Top Stories
- Importance / impact: Medium / Positive
- Relevance / horizon: sector_theme / short-term
- Affected assets: CrowdStrike, Palo Alto Networks, AI, Software Sector Performance
- Score: `51.0`
- Investment implication: Theme or sector positive signal; requires price and volume confirmation before affecting rankings.

**8. 30-year mortgage rate jumps to 7.17% — a nearly 2-year high — in the latest blow to the housing market**
- Source: MarketWatch Top Stories
- Importance / impact: High / Negative
- Relevance / horizon: macro / short-term
- Affected assets: housing
- Score: `51.0`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the short-term.

**9. Trump administration repeals Biden era greenhouse gas requirements for power plants**
- Source: CNBC Top News
- Importance / impact: Medium / Negative
- Relevance / horizon: sector_theme / short
- Affected assets: environment, politics, energy
- Score: `48.45`
- Investment implication: Theme or sector negative signal; requires price and volume confirmation before affecting rankings.

**10. 30-year mortgage rate hits nearly 2-year high, in latest blow to housing market**
- Source: MarketWatch Bulletins
- Importance / impact: Medium / Negative
- Relevance / horizon: sector_theme / short
- Affected assets: mortgage, housing
- Score: `48.45`
- Investment implication: Theme or sector negative signal; requires price and volume confirmation before affecting rankings.


### Headline Quality Checks

Noisy headline list: Stock market today: Dow, S&P 500, Nasdaq fall as A

## Positioning & Flow Dashboard

Positioning and flow data is used as confirmation only.

### Deferred Flow Sections

- Official ETF / fund flows: current report uses shares-outstanding-derived net fund flow estimates from free ETF metadata.
- Institutional Ownership: not available until SEC 13F ingestion is implemented.
- Grouped exposure flow reliability: use issuer coverage and availability status before treating ETF flow as confirmation.

## ETF Flows Analysis

- Market flow regime: `Defensive Rotation`
- Market flow score: `44.5 / 100`
- Equity risk flow: `45.4`
- Credit risk flow: `23.3`
- Sector cyclicality flow: `50.2`
- Duration/liquidity flow: `52.9`
- Alternatives: `barbell demand`
- ETF flow reliability: `65.9 / 100`
- Dominant allocation direction: `defensive demand`

### Core Flow Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVV | U.S. Broad Equity | -2.2 | -1.1 | 0.1 | -0.5 | Down | Sell | Normal | Persistent Distribution | Risk-Off | Strong confirmation; Exceptional institutional selling, Persistent selling | 79.0 |
| ACWI | Global Equity | -0.7 | -1.2 | 0.0 | -0.8 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Mixed or neutral flow structure; Persistent selling | 77.0 |
| EFA | Developed Markets ex-U.S. | -0.1 | -4.0 | 0.0 | 0.3 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Mixed or neutral flow structure; Exceptional institutional selling, Persistent selling | 69.0 |
| IEMG | Emerging Markets | -0.0 | 0.3 | 0.2 | -0.4 | Flat | Neutral | Normal | Neutral | Neutral | Structural accumulation; Persistent selling | 83.0 |
| IJH | U.S. Mid Cap | 1.1 | 1.4 | 0.9 | 0.5 | Down | Buy | Normal | Contrarian Buying | Watch | Strong confirmation; Strong sponsorship | 100.0 |
| IWM | U.S. Small Cap | 1.1 | 0.7 | 0.3 | 0.8 | Down | Buy | Normal | Contrarian Buying | Watch | Medium-term recovery; Exceptional institutional buying | 95.0 |
| LQD | Investment-Grade Credit | -2.1 | -1.6 | 0.2 | 0.3 | Down | Sell | Normal | Persistent Distribution | Risk-Off | Strong confirmation; Exceptional institutional selling, Persistent selling | 79.0 |
| HYG | High-Yield Credit | -2.7 | -1.8 | 0.1 | 1.4 | Down | Sell | High | Confirmed Distribution | Strong Risk-Off | Strong confirmation; Exceptional institutional selling, Persistent selling | 79.0 |
| SGOV | Treasury Bills / Cash | 0.4 | -0.8 | 0.9 | 0.1 | Flat | Neutral | Normal | Neutral | Neutral | Structural accumulation; Strong sponsorship | 99.0 |
| SHY | Short-Duration Treasuries | 0.7 | 0.0 | 0.5 | 0.6 | Flat | Sell | Normal | Quiet Distribution | Weakening | Tactical profit-taking inside structural accumulation | 83.0 |
| IEF | Intermediate-Duration Treasuries | -0.1 | -1.4 | 0.6 | 0.3 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural distribution | 79.0 |
| TLT | Long-Duration Treasuries | 0.8 | 2.6 | 0.6 | 0.3 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural accumulation; Exceptional institutional buying | 99.0 |
| GLD | Gold | 1.3 | 2.4 | 0.4 | -0.4 | Down | Buy | Normal | Contrarian Buying | Watch | Strong confirmation; Exceptional institutional buying | 100.0 |
| IBIT | Bitcoin | 1.6 | 0.8 | 0.7 | -0.0 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural accumulation | 91.0 |

### Sector Flow Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| XLC | Communication Services | 0.6 | -0.5 | 0.4 | -0.8 | Flat | Neutral | Normal | Neutral | Neutral | Structural distribution | 79.0 |
| XLY | Consumer Discretionary | -2.1 | -0.5 | 0.2 | -1.0 | Down | Sell | Normal | Persistent Distribution | Risk-Off | Strong confirmation; Exceptional institutional selling, Persistent selling | 79.0 |
| XLP | Consumer Staples | 0.3 | 1.9 | 0.5 | 0.1 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Mixed or neutral flow structure | 85.0 |
| XLE | Energy | -0.2 | -0.5 | 0.5 | 0.3 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Mixed or neutral flow structure | 85.0 |
| XLF | Financials | -1.0 | 0.2 | 0.5 | 0.4 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Medium-term deterioration | 83.0 |
| XLV | Health Care | 0.1 | 1.5 | 0.6 | -1.0 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Mixed or neutral flow structure | 85.0 |
| XLI | Industrials | -1.6 | -0.9 | 0.4 | -0.7 | Down | Sell | Normal | Persistent Distribution | Risk-Off | Medium-term deterioration | 83.0 |
| XLK | Information Technology | -0.4 | -1.1 | 0.5 | -0.6 | Flat | Neutral | Normal | Neutral | Neutral | Structural distribution | 79.0 |
| XLB | Materials | -1.1 | -2.1 | 0.3 | -0.8 | Down | Sell | Normal | Persistent Distribution | Risk-Off | Strong confirmation; Exceptional institutional selling | 87.0 |
| XLRE | Real Estate | -1.4 | -0.1 | 0.2 | -0.5 | Down | Sell | Normal | Persistent Distribution | Risk-Off | Medium-term deterioration; Persistent selling | 75.0 |
| XLU | Utilities | -0.0 | 0.5 | 0.5 | -1.0 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural accumulation | 91.0 |

### Subsector PFV Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ITA | Aerospace and Defense | -0.4 | 0.9 | 0.1 | 1.9 | Down | Sell | High | Confirmed Distribution | Strong Risk-Off | Strong confirmation; Persistent selling | 87.0 |
| SOXX | Semiconductors | 0.1 | -0.6 | 0.5 | 0.6 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural accumulation | 91.0 |
| SMH | Semiconductors | -0.3 | 0.5 | 0.5 | -0.8 | Flat | Neutral | Normal | Neutral | Neutral | Structural accumulation | 91.0 |
| CIBR | Cybersecurity | 0.8 | 1.8 | 0.6 | -0.7 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural accumulation | 91.0 |

### Material Flow Divergences

| Severity | Type | Primary | Comparison | Interpretation |
| --- | --- | --- | --- | --- |
| high | close_substitute_divergence | GLD | IAU | primary representative differs from close substitute |
| high | close_substitute_divergence | AGG | IUSB | primary representative differs from close substitute |
| high | close_substitute_divergence | IWF | IVW | primary representative differs from close substitute |
| high | close_substitute_divergence | IWD | IVE | primary representative differs from close substitute |
| high | close_substitute_divergence | IWM | IJR | primary representative differs from close substitute |


## Contradiction / Audit Flags

| Severity | Section | Issue | Deterministic Fix |
| --- | --- | --- | --- |
| low | Theme Strength Ranking | Financials has strong news confirmation but weak price confirmation. | Classify as unconfirmed narrative. |

## Data Quality Notes

- Technical rows loaded: `60`
- S&P 500 constituent technical rows loaded: `503`
- Macro rows loaded: `49`
- Live macro rows used: `15`
- Economic rows loaded: `113`
- News rows loaded: `80`
- Positioning/flow rows loaded: `30`

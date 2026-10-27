# Rule-Based Institutional Market Update

Generated at: 27 October 2026, 19:08:33 (HKT)
Window: 24h

## Executive Dashboard

- Regime score: **48.99 / 100** (Mixed / Rotation)
- US equity strength: **37.67 / 100** (weak)
- Evidence quality: **72.5 / 100**
- ETF flow contribution: **48.2 / 100**, reliability **71.28 / 100**
- Breadth: **narrow**; above 50DMA `38.33%`, above 200DMA `53.33%`
- Top sector score: **Energy** `69.09`
- Top theme score: **Energy** `67.68`

## Market Regime Score

| Metric | Value | Driver / Interpretation |
| --- | --- | --- |
| Overall regime | 48.99 | Mixed / Rotation |
| equity_trend | 31.25 | risk-off pressure; Core equity ETFs versus moving averages. |
| equity_momentum | 47.48 | neutral / mixed; 5D/20D/60D return momentum across SPY, QQQ, IWM, and SMH. |
| market_breadth | 45.0 | mild risk-off pressure; Participation breadth from tracked equity/ETF rows. |
| volatility | 70.0 | risk-on support; VIX level and change; higher score means calmer volatility conditions. |
| rates_yield_curve | 58.0 | mild risk-on support; Treasury yield pressure and curve shape; higher score means less rates pressure. |
| credit_proxy | 50.0 | neutral / mixed; Credit-market proxy; currently neutral when no direct spread signal is available. |
| dollar_fx | 53.86 | neutral / mixed; Dollar move; higher score means less USD tightening pressure. |
| commodity_confirmation | 55.0 | mild risk-on support; Copper, silver, oil, and gold mix; higher score means better cyclical confirmation. |
| etf_flow | 48.72 | neutral / mixed; Grouped ETF flow contribution adjusted for reliability. |
| news_confirmation | 50.0 | neutral / mixed; Weighted headline/news confirmation score. |
| Positive contributors |  | volatility=70.0 |
| Negative contributors |  | equity_trend=31.25, market_breadth=45.0 |

## US Equity Strength Score

| Component | Score |
| --- | --- |
| indices_above_moving_averages | 31.25 |
| sp500_trend | 55.0 |
| nasdaq_trend | 35.0 |
| russell_participation | 0.0 |
| returns_momentum | 47.48 |
| rsi_zone | 37.5 |
| macd_confirmation | 43.75 |
| volume_confirmation | 50.0 |
| breadth | 45.0 |

## Evidence Quality / Confidence

- Confidence score: `72.5`
- Agreement ratio: `0.3`
- Contradiction count: `2`
- Missing indicators: none
- Warning flags: none

## Cross-Asset Confirmation

| Area | Signal | Interpretation |
| --- | --- | --- |
| Equities | S&P 500 rising; Nasdaq rising; Russell 2000 rising | Confirms risk appetite when broad indices rise together; weak small caps would narrow the signal. |
| Rates | 10Y Treasury stable; MOVE falling | Rising yields can pressure duration assets; falling MOVE supports calmer bond volatility. |
| Dollar | DXY proxy stable | A stronger dollar can tighten financial conditions and pressure commodities/emerging-market risk. |
| Credit | HYG stable | High-yield weakness would challenge equity risk-on confirmation. |
| Gold | Gold falling | Gold strength can indicate defensive demand, inflation hedging, or geopolitical concern. |
| Silver | Silver falling | Silver helps distinguish precious-metal demand from industrial/cyclical confirmation when data is available. |
| Copper | Copper rising | Copper strength supports cyclical growth confirmation; weakness would dilute risk-on breadth. |
| Oil | WTI crude falling | Oil spikes can be inflationary risk; falling oil can ease cost pressure but may also flag demand softness. |
| Volatility | VIX falling | Falling VIX supports risk appetite; a volatility spike would reduce confidence in broad risk-on. |

### Macro Snapshot

Live macro rows are intraday snapshots from `public.macro_live`; closed rows are official stored rows from `public.macro`.

| Symbol | Name | Close | Pct Chg | Market Date | Status |
| --- | --- | --- | --- | --- | --- |
| ^GSPC | S&P 500 | 7676.77 | 0.7 | 2026-10-26 | closed |
| ^IXIC | NASDAQ Composite | 26169.38 | 0.82 | 2026-10-26 | closed |
| ^RUT | Russell 2000 Index | 2786.42 | 0.38 | 2026-10-26 | closed |
| ^VIX | CBOE Volatility Index | 17.83 | -3.05 | 2026-10-27 | live as of 27 October 2026, 19:00:26 (HKT) |
| ^SKEW | CBOE SKEW Index | 150.97 | -0.55 | 2026-10-26 | closed |
| ^MOVE | ICE BofA MOVE Index | 102.19 | -1.1 | 2026-10-26 | closed |
| US2YT=X | United States 2-Year Treasury Yield | 4.71 | 0.0 | 2026-10-27 | live as of 27 October 2026, 19:00:26 (HKT) |
| US3YT=X | United States 3-Year Treasury Yield | 4.78 | 0.06 | 2026-10-27 | live as of 27 October 2026, 19:00:26 (HKT) |
| US5YT=X | United States 5-Year Treasury Yield | 4.83 | 0.04 | 2026-10-27 | live as of 27 October 2026, 19:00:26 (HKT) |
| US7YT=X | United States 7-Year Treasury Yield | 4.9 | 0.02 | 2026-10-27 | live as of 27 October 2026, 19:00:26 (HKT) |
| US10YT=X | United States 10-Year Treasury Yield | 4.99 | 0.0 | 2026-10-27 | live as of 27 October 2026, 19:00:26 (HKT) |
| US20YT=X | United States 20-Year Treasury Yield | 5.35 | 0.06 | 2026-10-27 | live as of 27 October 2026, 19:00:26 (HKT) |
| US30YT=X | United States 30-Year Treasury Yield | 5.3 | 0.06 | 2026-10-27 | live as of 27 October 2026, 19:00:26 (HKT) |
| HK50 | Hang Seng Futures | 23009.0 | -0.92 | 2026-10-27 | live as of 27 October 2026, 19:00:26 (HKT) |
| KOR200c1 | KOSPI 200 Futures | 889.25 | 4.62 | 2026-10-26 | live as of 27 October 2026, 19:00:26 (HKT) |
| CIHc1 | SSE 50 Futures | 2737.2 | 0.15 | 2026-10-26 | live as of 27 October 2026, 19:00:26 (HKT) |
| HYG | iShares iBoxx High Yield Corporate Bond ETF | 77.2 | 0.19 | 2026-10-26 | closed |
| LQD | iShares iBoxx Investment Grade Corporate Bond ETF | 104.02 | 0.16 | 2026-10-26 | closed |
| JNK | SPDR Bloomberg High Yield Bond ETF | 92.66 | 0.15 | 2026-10-26 | closed |
| RSP | Invesco S&P 500 Equal Weight ETF | 217.29 | 0.35 | 2026-10-26 | closed |
| IWF | iShares Russell 1000 Growth ETF | 120.89 | 1.07 | 2026-10-26 | closed |
| IWD | iShares Russell 1000 Value ETF | 258.35 | 0.36 | 2026-10-26 | closed |
| TLT | iShares 20+ Year Treasury Bond ETF | 81.68 | 0.42 | 2026-10-26 | closed |
| IEF | iShares 7-10 Year Treasury Bond ETF | 91.12 | 0.08 | 2026-10-26 | closed |
| SHY | iShares 1-3 Year Treasury Bond ETF | 81.48 | -0.02 | 2026-10-26 | closed |
| GC=F | Gold Future | 4023.8 | -0.36 | 2026-10-27 | live as of 27 October 2026, 19:00:26 (HKT) |
| SI=F | Silver Future | 53.47 | -1.19 | 2026-10-27 | live as of 27 October 2026, 19:00:26 (HKT) |
| CL=F | WTI Crude Oil Future | 101.13 | -0.62 | 2026-10-27 | live as of 27 October 2026, 19:00:26 (HKT) |
| HG=F | Copper Future | 6.61 | 1.57 | 2026-10-27 | live as of 27 October 2026, 19:00:26 (HKT) |

## Market Dispersion Analysis

- Sector ETF 20D dispersion: `18.39` points (high); leader `XLE` (Energy) `11.75`, laggard `XLK` (Technology) `-6.64`
- Sector ETF 60D dispersion: `25.31` points (very high); leader `XLE` (Energy) `17.59`, laggard `XLI` (Industrials) `-7.72`

| Comparison | Left | Right | 20D Spread | Signal |
| --- | --- | --- | --- | --- |
| Equal-weight vs cap-weight | RSP (Equal-weight S&P 500) | SPY (S&P 500) | 4.05 | broader participation |
| Small-cap vs large-cap | IWM (Russell 2000) | SPY (S&P 500) | -0.73 | balanced |
| Growth vs value | IWF (Russell 1000 Growth) | IWD (Russell 1000 Value) | -7.44 | value leadership |
| Nasdaq vs S&P 500 | QQQ (Nasdaq 100) | SPY (S&P 500) | -3.91 | S&P 500 leadership |

## Sector Constituent Dispersion

- Breadth 50D / 200D: percentage of active S&P 500 constituents in the sector trading above the 50-day / 200-day moving average.
- Positive 20D: percentage of active sector constituents with positive 20-day return.
- Std 20D: cross-sectional standard deviation of constituent 20-day returns; higher means wider stock-level dispersion.

| Sector | Count | Breadth 50D | Breadth 200D | Positive 20D | 20D Dispersion | Std 20D | Label | Leaders | Laggards |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Information Technology | 75 | 48.0 | 60.81 | 44.0 | 74.85 | 16.39 | very high | ACN, PTC, INTU | SNDK, STX, FLEX |
| Industrials | 83 | 48.19 | 40.51 | 57.83 | 56.17 | 10.49 | very high | EFX, PAYX, LMT | VRT, FIX, BE |
| Financials | 76 | 46.67 | 61.97 | 63.16 | 52.31 | 8.78 | very high | CBOE, FDS, BRO | BAC, COIN, HOOD |
| Consumer Discretionary | 47 | 51.06 | 34.04 | 63.83 | 47.19 | 9.01 | very high | HAS, CCL, ULTA | CVNA, CMG, MGM |
| Real Estate | 30 | 44.83 | 41.38 | 63.33 | 40.56 | 8.01 | very high | CCI, CSGP, AMT | PLD, CBRE, ARE |
| Materials | 24 | 66.67 | 62.5 | 70.83 | 38.85 | 9.44 | very high | DOW, LYB, BALL | NEM, ALB, MOS |
| Health Care | 60 | 85.0 | 88.33 | 81.67 | 27.96 | 5.76 | very high | CRL, MCK, VEEV | SOLV, INCY, DXCM |
| Consumer Staples | 34 | 75.0 | 65.62 | 85.29 | 27.35 | 5.64 | very high | STZ, CASY, EL | ADM, TGT, BG |
| Communication Services | 22 | 28.57 | 40.0 | 40.91 | 26.11 | 7.69 | very high | OMC, NWSA, NWS | META, APP, T |
| Energy | 21 | 85.71 | 76.19 | 90.48 | 24.84 | 5.93 | very high | APA, COP, MPC | SLB, TPL, BKR |
| Utilities | 31 | 80.65 | 38.71 | 93.55 | 23.44 | 4.68 | very high | PNW, ED, SO | AES, CEG, NRG |

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
| Real Gross Domestic Product | 24408.01 | billions chained 2017 dollars | 133.63 billions chained 2017 dollars vs prior | 2026-04-01 | Higher reading supports activity or liquidity. |
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
| US dollar/Euro ECB reference exchange rate | 1.12 | USD | -0.0 USD vs prior | 2026-10-26 | EUR weakened versus this currency. |
| Japanese yen/Euro ECB reference exchange rate | 176.15 | JPY | 0.64 JPY vs prior | 2026-10-26 | EUR strengthened versus this currency. |
| Chinese yuan renminbi/Euro ECB reference exchange rate | 7.46 | CNY | -0.01 CNY vs prior | 2026-10-26 | EUR weakened versus this currency. |
| Australian dollar/Euro ECB reference exchange rate | 1.59 | AUD | -0.0 AUD vs prior | 2026-10-26 | EUR weakened versus this currency. |

ABS Australia note: ABS rows are stored locally/Neon, but most series are dimension-coded; only curated series should be promoted into narrative report text.

## Sector and Theme Leadership

### Official Sector Strength

Supporting and detracting names are the top/bottom S&P 500 constituents by 20D return when constituent coverage is available; otherwise the report falls back to related ETFs.

| Rank | Sector | Score | Trend | Momentum | Stock Breadth | ETF Flow | Flow Reliability | 3M RS | Supporting / Leaders | Detracting / Laggards |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Energy | 69.09 | strong uptrend | positive | broad | 54.88 | 95.0 | 63.98 | APA, COP, MPC | SLB, TPL, BKR |
| 2 | Healthcare | 68.76 | strong uptrend | positive | broad | 71.96 | 100.0 | 56.77 | CRL, MCK, VEEV | SOLV, INCY, DXCM |
| 3 | Cybersecurity | 68.11 | strong uptrend | positive | broad | 64.06 | 65.0 | 60.13 | CIBR | CIBR |
| 4 | Consumer Staples | 66.03 | strong uptrend | neutral | broad | 50.67 | 65.0 | 55.74 | STZ, CASY, EL | ADM, TGT, BG |
| 5 | Utilities | 57.25 | neutral | neutral | broad | 64.21 | 65.0 | 52.43 | PNW, ED, SO | AES, CEG, NRG |
| 6 | Financials | 55.02 | strong uptrend | neutral | weak | 50.0 | 0.0 | 50.29 | CBOE, FDS, BRO | BAC, COIN, HOOD |
| 7 | Crypto | 51.11 | neutral | neutral | mixed | 61.15 | 65.0 | 50.0 |  |  |
| 8 | Consumer Discretionary | 45.32 | strong downtrend | neutral | weak | 40.23 | 65.0 | 51.53 | HAS, CCL, ULTA | CVNA, CMG, MGM |
| 9 | Real Estate | 44.73 | strong downtrend | neutral | weak | 50.0 | 0.0 | 48.95 | CCI, CSGP, AMT | PLD, CBRE, ARE |
| 10 | Technology | 41.73 | downtrend | neutral | weak | 52.41 | 95.0 | 47.75 | ACN, PTC, INTU | SNDK, STX, FLEX |
| 11 | Semiconductors | 41.52 | downtrend | negative | weak | 76.51 | 90.0 | 39.55 | SMH, SOXX | SOXX, SMH |
| 12 | Industrials | 35.93 | strong downtrend | neutral | weak | 65.83 | 65.0 | 44.77 | EFX, PAYX, LMT | VRT, FIX, BE |
| 13 | Grid Infrastructure | 34.24 | strong downtrend | negative | weak | 61.38 | 65.0 | 41.09 | GRID | GRID |
| 14 | Defense | 33.44 | strong downtrend | negative | weak | 45.63 | 65.0 | 37.62 | XAR | XAR |
| 15 | Nuclear | 31.08 | strong downtrend | negative | weak | 50.0 | 0.0 | 34.53 | NLR | NLR |

### Thematic Strength

| Rank | Theme | Score | Setup | ETF Flow | Flow Reliability | Dispersion | Price | News |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Energy | 67.68 | Positive setup | 54.88 | 95.0 | 2.34 | True | False |
| 2 | Cybersecurity | 63.08 | Positive setup | 64.06 | 65.0 | 30.62 | True | False |
| 3 | Healthcare Innovation | 61.83 | Positive setup | 71.96 | 100.0 | 13.38 | True | False |
| 4 | Dividend Defensives | 59.1 | Positive setup | 53.39 | 65.0 | 2.69 | False | False |
| 5 | Crypto Infrastructure | 47.83 | Neutral / watchlist | 61.15 | 65.0 | 7.77 | False | False |
| 6 | Quality Growth | 46.32 | Neutral / watchlist | 50.31 | 65.0 | 8.85 | False | False |
| 7 | AI Infrastructure | 45.32 | Neutral / watchlist | 76.51 | 90.0 | 18.11 | False | False |
| 8 | Defense | 43.58 | Weak setup | 45.63 | 65.0 | 35.23 | False | False |
| 9 | Semiconductors | 40.82 | Weak setup | 76.51 | 90.0 | 11.78 | False | False |
| 10 | Financials | 39.39 | Weak setup | 50.0 | 0.0 | 12.76 | False | False |
| 11 | Grid Infrastructure | 37.77 | Weak setup | 61.38 | 65.0 | 24.51 | False | False |
| 12 | Small Caps | 35.49 | Weak setup | 47.05 | 65.0 | 0.0 | False | False |
| 13 | Nuclear | 27.22 | Underperformance risk | 50.0 | 0.0 | 19.59 | False | False |

- Top 5 improving themes: Cybersecurity, Crypto Infrastructure, Energy, Healthcare Innovation, Quality Growth
- Top 5 deteriorating themes: Nuclear, Financials, Grid Infrastructure, Defense, Small Caps
- Strong news but weak price confirmation: none
- Strong price but weak news confirmation: Energy, Cybersecurity, Healthcare Innovation

### Sector / Theme Alignment

| Sector | Related Themes | Sector Score | Sector Signal | Theme Score | Theme Signal | Interpretation |
| --- | --- | --- | --- | --- | --- | --- |
| Energy | Energy | 69.09 | strong | 67.68 | strong | sector and theme confirmation |
| Healthcare | Healthcare Innovation | 68.76 | strong | 61.83 | positive | sector and theme confirmation |
| Cybersecurity | Cybersecurity | 68.11 | strong | 63.08 | positive | sector and theme confirmation |
| Consumer Staples | Dividend Defensives | 66.03 | strong | 59.1 | positive | sector and theme confirmation |
| Utilities | Grid Infrastructure, Nuclear, Dividend Defensives | 57.25 | positive | 41.36 | weak | sector stronger than related themes |
| Financials | Financials | 55.02 | positive | 39.39 | weak | sector stronger than related themes |
| Crypto | Crypto Infrastructure | 51.11 | mixed | 47.83 | mixed | mixed confirmation |
| Consumer Discretionary | Small Caps | 45.32 | mixed | 35.49 | weak | mixed confirmation |
| Real Estate | Dividend Defensives | 44.73 | weak | 59.1 | positive | theme stronger than official sector |
| Technology | AI Infrastructure, Semiconductors, Quality Growth | 41.73 | weak | 44.15 | weak | broad weakness across sector and themes |
| Semiconductors | AI Infrastructure, Semiconductors | 41.52 | weak | 43.07 | weak | broad weakness across sector and themes |
| Industrials | Defense, Grid Infrastructure | 35.93 | weak | 40.67 | weak | broad weakness across sector and themes |
| Grid Infrastructure | Grid Infrastructure | 34.24 | very weak | 37.77 | weak | broad weakness across sector and themes |
| Defense | Defense | 33.44 | very weak | 43.58 | weak | broad weakness across sector and themes |
| Nuclear | Nuclear | 31.08 | very weak | 27.22 | very weak | broad weakness across sector and themes |

## Three-Month Outperformance Setup

| Rank | Theme | Score | Classification | Drivers | Invalidation Triggers |
| --- | --- | --- | --- | --- | --- |
| 1 | Energy | 71.66 | Positive setup | relative_strength_20d, relative_strength_60d, trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 2 | Cybersecurity | 70.38 | Positive setup | relative_strength_20d, relative_strength_60d, trend_persistence, breadth, volume_accumulation | relative strength below SPY, breadth below 45%, news turns negative |
| 3 | Healthcare Innovation | 62.68 | Positive setup | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 4 | Dividend Defensives | 61.58 | Positive setup | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 5 | Quality Growth | 53.13 | Neutral / watchlist | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 6 | Crypto Infrastructure | 51.69 | Neutral / watchlist | relative_strength_60d, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 7 | AI Infrastructure | 49.09 | Neutral / watchlist | downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 8 | Defense | 44.28 | Weak setup | downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 9 | Semiconductors | 43.09 | Weak setup | downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 10 | Financials | 40.1 | Weak setup | downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 11 | Grid Infrastructure | 39.57 | Weak setup | downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 12 | Small Caps | 35.6 | Weak setup | downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |

## Breadth and Participation

- Above 50DMA: `38.33%`
- Above 200DMA: `53.33%`
- Positive 20D return: `43.33%`

## Volatility and Risk Signals

- VIX close=17.83 pct_chg=-3.05

## News Analytics

- Sentiment counts: {'positive': 0, 'negative': 0, 'neutral': 80}
- News confirmation score: `50.0`

### Top Market-Moving Headlines

**1. Oil prices seesaw amid renewed diplomatic efforts to end Mideast conflict**
- Source: CNBC Top News
- Importance / impact: Low / Mixed
- Relevance / horizon: macro / short-term
- Affected assets: U.S
- Score: `23.75`
- Investment implication: Macro-relevant mixed signal; use as context for rates, volatility, and index confirmation over the short-term.

**2. The impressive real estate portfolio of sitcom producer Chuck Lorre of ‘Big Bang Theory’ and ‘Two and a Half Men’ fame**
- Source: MarketWatch Top Stories
- Importance / impact: Low / Mixed
- Relevance / horizon: sector_theme / short-term
- Affected assets: A, TV
- Score: `21.25`
- Investment implication: Theme or sector mixed signal; requires price and volume confirmation before affecting rankings.

**3. Some Republicans are opposing Trump on tariffs. Maine’s Susan Collins just got him to back down on Canadian levies.**
- Source: MarketWatch Top Stories
- Importance / impact: Low / Mixed
- Relevance / horizon: macro / short-term
- Affected assets: GOP
- Score: `21.25`
- Investment implication: Macro-relevant mixed signal; use as context for rates, volatility, and index confirmation over the short-term.

**4. Stocks close higher as excitement over Anthropic IPO filing propels tech sector: Live updates**
- Source: CNBC Top News
- Importance / impact: Low / Mixed
- Relevance / horizon: macro / short-term
- Affected assets: IPO
- Score: `20.19`
- Investment implication: Macro-relevant mixed signal; use as context for rates, volatility, and index confirmation over the short-term.

**5. Options traders are seizing control of the S&P 500**
- Source: MarketWatch Top Stories
- Importance / impact: Low / Mixed
- Relevance / horizon: sector_theme / short-term
- Affected assets: P, S, UBS
- Score: `18.06`
- Investment implication: Theme or sector mixed signal; requires price and volume confirmation before affecting rankings.

**6. Why Lumentum’s stock led the S&P 500 higher on Monday**
- Source: MarketWatch Top Stories
- Importance / impact: Low / Mixed
- Relevance / horizon: sector_theme / short-term
- Affected assets: IPO, P, S
- Score: `18.06`
- Investment implication: Theme or sector mixed signal; requires price and volume confirmation before affecting rankings.

**7. We stopped helping our neighbors with free home repairs and our friendship cooled. Who’s to blame?**
- Source: MarketWatch Top Stories
- Importance / impact: Low / Mixed
- Relevance / horizon: sector_theme / short-term
- Affected assets: A, SUV
- Score: `18.06`
- Investment implication: Theme or sector mixed signal; requires price and volume confirmation before affecting rankings.

**8. The stock market’s biggest test in weeks is here**
- Source: MarketWatch Top Stories
- Importance / impact: Low / Mixed
- Relevance / horizon: sector_theme / short-term
- Affected assets: A, I
- Score: `18.06`
- Investment implication: Theme or sector mixed signal; requires price and volume confirmation before affecting rankings.

**9. Anthropic's IPO puts power in the hands of founders, giving everyday shareholders little voice**
- Source: CNBC Markets
- Importance / impact: Low / Mixed
- Relevance / horizon: sector_theme / short-term
- Affected assets: IPO, LLC, S
- Score: `17.16`
- Investment implication: Theme or sector mixed signal; requires price and volume confirmation before affecting rankings.

**10. Options traders are seizing control of the S&P 500. Here’s why that matters.**
- Source: MarketWatch Bulletins
- Importance / impact: Low / Mixed
- Relevance / horizon: sector_theme / short-term
- Affected assets: P, S
- Score: `17.16`
- Investment implication: Theme or sector mixed signal; requires price and volume confirmation before affecting rankings.


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
- Market flow score: `49.0 / 100`
- Equity risk flow: `44.6`
- Credit risk flow: `55.5`
- Sector cyclicality flow: `46.8`
- Duration/liquidity flow: `51.9`
- Alternatives: `mixed alternative-asset demand`
- ETF flow reliability: `71.3 / 100`
- Dominant allocation direction: `defensive demand`

### Core Flow Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVV | U.S. Broad Equity | -0.2 | -0.9 | 0.5 | n/a | Flat | Neutral | Normal | Neutral | Neutral | Structural distribution | 64.0 |
| ACWI | Global Equity | -0.6 | -0.8 | 0.0 | n/a | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Mixed or neutral flow structure; Persistent selling | 62.0 |
| EFA | Developed Markets ex-U.S. | 0.9 | 0.6 | 0.1 | n/a | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural accumulation; Persistent selling | 68.0 |
| IEMG | Emerging Markets | -0.8 | -0.3 | 0.0 | n/a | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Medium-term deterioration; Persistent selling | 60.0 |
| IJH | U.S. Mid Cap | -1.7 | 0.6 | 0.3 | n/a | Flat | Neutral | Normal | Neutral | Neutral | Medium-term deterioration | 68.0 |
| IWM | U.S. Small Cap | -1.0 | -0.0 | 0.6 | n/a | Down | Sell | Normal | Persistent Distribution | Risk-Off | Strong confirmation | 80.0 |
| LQD | Investment-Grade Credit | 1.1 | -0.9 | 0.7 | n/a | Up | Buy | Normal | Steady Accumulation | Risk-On | Medium-term recovery | 72.0 |
| HYG | High-Yield Credit | 0.8 | 0.4 | 0.6 | n/a | Flat | Neutral | Normal | Neutral | Neutral | Structural accumulation | 76.0 |
| SGOV | Treasury Bills / Cash | -0.6 | -0.1 | 0.8 | n/a | Flat | Sell | Normal | Quiet Distribution | Weakening | Tactical profit-taking inside structural accumulation; Strong sponsorship | 76.0 |
| SHY | Short-Duration Treasuries | 1.3 | 2.4 | 0.7 | n/a | Flat | Buy | Normal | Quiet Accumulation | Improving | Strong confirmation; Exceptional institutional buying | 88.0 |
| IEF | Intermediate-Duration Treasuries | 1.1 | -0.7 | 0.5 | n/a | Up | Buy | Normal | Steady Accumulation | Risk-On | Medium-term recovery; Exceptional institutional buying | 80.0 |
| TLT | Long-Duration Treasuries | -0.4 | 1.0 | 0.7 | n/a | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Medium-term deterioration | 68.0 |
| GLD | Gold | -0.8 | 1.2 | 0.3 | n/a | Down | Sell | Normal | Persistent Distribution | Risk-Off | Medium-term deterioration; Exceptional institutional selling | 60.0 |
| IBIT | Bitcoin | 0.1 | 1.6 | 0.6 | n/a | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural accumulation | 76.0 |

### Sector Flow Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| XLC | Communication Services | 2.1 | 3.3 | 0.6 | n/a | Down | Buy | Normal | Contrarian Buying | Watch | Strong confirmation; Exceptional institutional buying | 88.0 |
| XLY | Consumer Discretionary | -1.1 | -0.1 | 0.3 | n/a | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural distribution | 64.0 |
| XLP | Consumer Staples | 0.1 | 0.6 | 0.6 | n/a | Up | Sell | Normal | Profit Taking | Slightly Bearish | Strong confirmation; Exceptional institutional selling | 72.0 |
| XLE | Energy | 0.5 | 0.1 | 0.7 | n/a | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural accumulation | 76.0 |
| XLF | Financials | -0.9 | -2.9 | 0.3 | n/a | Up | Sell | Normal | Profit Taking | Slightly Bearish | Strong confirmation; Exceptional institutional selling | 72.0 |
| XLV | Health Care | 0.9 | 1.1 | 0.6 | n/a | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural accumulation | 76.0 |
| XLI | Industrials | 0.5 | -0.8 | 0.5 | n/a | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural accumulation | 76.0 |
| XLK | Information Technology | 0.7 | -0.4 | 0.6 | n/a | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural accumulation | 76.0 |
| XLB | Materials | -1.0 | -1.8 | 0.5 | n/a | Up | Sell | Normal | Profit Taking | Slightly Bearish | Strong confirmation | 80.0 |
| XLRE | Real Estate | 0.2 | -1.3 | 0.5 | n/a | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Medium-term recovery | 72.0 |
| XLU | Utilities | 0.7 | 1.1 | 0.5 | n/a | Up | Sell | Normal | Profit Taking | Slightly Bearish | Tactical profit-taking inside structural accumulation | 68.0 |

### Subsector PFV Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ITA | Aerospace and Defense | -0.1 | 0.7 | 0.3 | n/a | Flat | Buy | Normal | Quiet Accumulation | Improving | Tactical rebound inside structural distribution | 68.0 |
| SOXX | Semiconductors | 0.6 | -0.9 | 0.6 | n/a | Down | Buy | Normal | Contrarian Buying | Watch | Strong confirmation; Exceptional institutional buying | 88.0 |
| SMH | Semiconductors | 0.2 | -1.2 | 0.6 | n/a | Down | Buy | Normal | Contrarian Buying | Watch | Medium-term recovery | 72.0 |
| CIBR | Cybersecurity | 0.7 | 1.9 | 0.8 | n/a | Up | Sell | Normal | Profit Taking | Slightly Bearish | Tactical profit-taking inside structural accumulation; Strong sponsorship | 76.0 |

### Material Flow Divergences

| Severity | Type | Primary | Comparison | Interpretation |
| --- | --- | --- | --- | --- |
| medium | related_subsector_divergence | XLI | ITA | defense-specific demand differs from broad industrials |
| medium | related_subsector_divergence | XLK | SOXX | technology differs from semiconductors |
| high | close_substitute_divergence | GLD | IAU | primary representative differs from close substitute |
| high | close_substitute_divergence | AGG | IUSB | primary representative differs from close substitute |
| high | close_substitute_divergence | HYG | JNK | primary representative differs from close substitute |
| high | close_substitute_divergence | IWD | IVE | primary representative differs from close substitute |


## Contradiction / Audit Flags

No contradiction flags were triggered by current deterministic rules.

## Data Quality Notes

- Technical rows loaded: `60`
- S&P 500 constituent technical rows loaded: `503`
- Macro rows loaded: `48`
- Live macro rows used: `26`
- Economic rows loaded: `113`
- News rows loaded: `80`
- Positioning/flow rows loaded: `30`

## Cycle Metadata

- Report generated at: 27 October 2026, 19:08:33 (HKT)

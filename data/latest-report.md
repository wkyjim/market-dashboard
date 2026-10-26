# Rule-Based Institutional Market Update

Generated at: 27 October 2026, 01:10:52 (HKT)
Window: 24h

## Executive Dashboard

- Regime score: **49.52 / 100** (Mixed / Rotation)
- US equity strength: **37.67 / 100** (weak)
- Evidence quality: **72.5 / 100**
- ETF flow contribution: **48.43 / 100**, reliability **71.51 / 100**
- Breadth: **narrow**; above 50DMA `38.33%`, above 200DMA `53.33%`
- Top sector score: **Energy** `68.83`
- Top theme score: **Energy** `67.42`

## Market Regime Score

| Metric | Value | Driver / Interpretation |
| --- | --- | --- |
| Overall regime | 49.52 | Mixed / Rotation |
| equity_trend | 31.25 | risk-off pressure; Core equity ETFs versus moving averages. |
| equity_momentum | 47.48 | neutral / mixed; 5D/20D/60D return momentum across SPY, QQQ, IWM, and SMH. |
| market_breadth | 45.0 | mild risk-off pressure; Participation breadth from tracked equity/ETF rows. |
| volatility | 70.0 | risk-on support; VIX level and change; higher score means calmer volatility conditions. |
| rates_yield_curve | 58.0 | mild risk-on support; Treasury yield pressure and curve shape; higher score means less rates pressure. |
| credit_proxy | 50.0 | neutral / mixed; Credit-market proxy; currently neutral when no direct spread signal is available. |
| dollar_fx | 54.34 | neutral / mixed; Dollar move; higher score means less USD tightening pressure. |
| commodity_confirmation | 63.0 | mild risk-on support; Copper, silver, oil, and gold mix; higher score means better cyclical confirmation. |
| etf_flow | 48.88 | neutral / mixed; Grouped ETF flow contribution adjusted for reliability. |
| news_confirmation | 50.0 | neutral / mixed; Weighted headline/news confirmation score. |
| Positive contributors |  | volatility=70.0, commodity_confirmation=63.0 |
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
| ^GSPC | S&P 500 | 7682.73 | 0.77 | 2026-10-26 | live as of 27 October 2026, 01:00:18 (HKT) |
| ^IXIC | NASDAQ Composite | 26229.62 | 1.06 | 2026-10-26 | live as of 27 October 2026, 01:00:18 (HKT) |
| ^RUT | Russell 2000 Index | 2793.18 | 0.62 | 2026-10-26 | live as of 27 October 2026, 01:00:18 (HKT) |
| ^VIX | CBOE Volatility Index | 18.58 | -4.47 | 2026-10-26 | live as of 27 October 2026, 01:00:18 (HKT) |
| ^SKEW | CBOE SKEW Index | 151.8 | -0.39 | 2026-10-23 | closed |
| ^MOVE | ICE BofA MOVE Index | 104.42 | 1.07 | 2026-10-26 | live as of 27 October 2026, 01:00:18 (HKT) |
| US2YT=X | United States 2-Year Treasury Yield | 4.71 | 0.53 | 2026-10-26 | live as of 27 October 2026, 01:00:18 (HKT) |
| US3YT=X | United States 3-Year Treasury Yield | 4.77 | 0.42 | 2026-10-26 | live as of 27 October 2026, 01:00:18 (HKT) |
| US5YT=X | United States 5-Year Treasury Yield | 4.82 | 0.21 | 2026-10-26 | live as of 27 October 2026, 01:00:18 (HKT) |
| US7YT=X | United States 7-Year Treasury Yield | 4.89 | 0.08 | 2026-10-26 | live as of 27 October 2026, 01:00:18 (HKT) |
| US10YT=X | United States 10-Year Treasury Yield | 4.98 | -0.12 | 2026-10-26 | live as of 27 October 2026, 01:00:18 (HKT) |
| US20YT=X | United States 20-Year Treasury Yield | 5.35 | -0.15 | 2026-10-26 | live as of 27 October 2026, 01:00:18 (HKT) |
| US30YT=X | United States 30-Year Treasury Yield | 5.3 | -0.21 | 2026-10-26 | live as of 27 October 2026, 01:00:18 (HKT) |
| HK50 | Hang Seng Futures | 23258.0 | 0.64 | 2026-10-26 | live as of 27 October 2026, 01:00:18 (HKT) |
| KOR200c1 | KOSPI 200 Futures | 861.55 | -0.2 | 2026-10-23 | live as of 27 October 2026, 01:00:18 (HKT) |
| CIHc1 | SSE 50 Futures | 2733.0 | 1.03 | 2026-10-23 | live as of 27 October 2026, 01:00:18 (HKT) |
| HYG | iShares iBoxx High Yield Corporate Bond ETF | 77.2 | 0.19 | 2026-10-26 | live as of 27 October 2026, 01:00:18 (HKT) |
| LQD | iShares iBoxx Investment Grade Corporate Bond ETF | 104.1 | 0.24 | 2026-10-26 | live as of 27 October 2026, 01:00:18 (HKT) |
| JNK | SPDR Bloomberg High Yield Bond ETF | 92.69 | 0.19 | 2026-10-26 | live as of 27 October 2026, 01:00:18 (HKT) |
| RSP | Invesco S&P 500 Equal Weight ETF | 217.23 | 0.32 | 2026-10-26 | live as of 27 October 2026, 01:00:18 (HKT) |
| IWF | iShares Russell 1000 Growth ETF | 121.13 | 1.27 | 2026-10-26 | live as of 27 October 2026, 01:00:18 (HKT) |
| IWD | iShares Russell 1000 Value ETF | 258.26 | 0.33 | 2026-10-26 | live as of 27 October 2026, 01:00:18 (HKT) |
| TLT | iShares 20+ Year Treasury Bond ETF | 81.73 | 0.48 | 2026-10-26 | live as of 27 October 2026, 01:00:18 (HKT) |
| IEF | iShares 7-10 Year Treasury Bond ETF | 91.14 | 0.1 | 2026-10-26 | live as of 27 October 2026, 01:00:18 (HKT) |
| SHY | iShares 1-3 Year Treasury Bond ETF | 81.48 | -0.02 | 2026-10-26 | live as of 27 October 2026, 01:00:18 (HKT) |
| GC=F | Gold Future | 4032.3 | 0.61 | 2026-10-26 | live as of 27 October 2026, 01:00:18 (HKT) |
| SI=F | Silver Future | 54.16 | 0.83 | 2026-10-26 | live as of 27 October 2026, 01:00:18 (HKT) |
| CL=F | WTI Crude Oil Future | 102.91 | -0.35 | 2026-10-26 | live as of 27 October 2026, 01:00:18 (HKT) |
| HG=F | Copper Future | 6.54 | 0.98 | 2026-10-26 | live as of 27 October 2026, 01:00:18 (HKT) |

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
| Initial Claims | 215000.0 | number | -12000.0 number vs prior | 2026-06-20 | Lower claims indicate firmer labor-market conditions. |
| Continued Claims | 1821000.0 | number | 21000.0 number vs prior | 2026-06-13 | Higher claims indicate softer labor-market conditions. |
| Labor Force Participation Rate | 61.8 | percent | 0.2 pp vs prior | 2026-09-01 | Higher participation expands labor supply. |

### U.S. Growth

| Indicator | Latest | Unit | Change | Date | Rule-Based Interpretation |
| --- | --- | --- | --- | --- | --- |
| Real Gross Domestic Product | 24408.01 | billions chained 2017 dollars | 133.63 billions chained 2017 dollars vs prior | 2026-04-01 | Higher reading supports activity or liquidity. |
| Industrial Production Index | 102.65 | index 2017=100 | 0.14 index pts vs prior | 2026-05-01 | Higher reading supports activity or liquidity. |
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
| Housing Starts | 1221.0 | thousands | -67.0 thousands vs prior | 2026-09-01 | Lower reading signals softer activity or liquidity. |
| New Privately-Owned Housing Units Authorized | 1400.0 | thousands | -3.0 thousands vs prior | 2026-09-01 | Lower reading signals softer activity or liquidity. |
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
| 1 | Energy | 68.83 | strong uptrend | positive | broad | 52.25 | 100.0 | 63.98 | APA, COP, MPC | SLB, TPL, BKR |
| 2 | Cybersecurity | 68.52 | strong uptrend | positive | broad | 68.21 | 65.0 | 60.13 | CIBR | CIBR |
| 3 | Consumer Staples | 68.45 | strong uptrend | neutral | broad | 74.88 | 65.0 | 55.74 | STZ, CASY, EL | ADM, TGT, BG |
| 4 | Healthcare | 68.12 | strong uptrend | positive | broad | 65.59 | 90.0 | 56.77 | CRL, MCK, VEEV | SOLV, INCY, DXCM |
| 5 | Utilities | 57.21 | neutral | neutral | broad | 63.81 | 65.0 | 52.43 | PNW, ED, SO | AES, CEG, NRG |
| 6 | Financials | 55.02 | strong uptrend | neutral | weak | 50.0 | 0.0 | 50.29 | CBOE, FDS, BRO | BAC, COIN, HOOD |
| 7 | Crypto | 51.38 | neutral | neutral | mixed | 63.81 | 65.0 | 50.0 |  |  |
| 8 | Consumer Discretionary | 45.81 | strong downtrend | neutral | weak | 45.17 | 65.0 | 51.53 | HAS, CCL, ULTA | CVNA, CMG, MGM |
| 9 | Real Estate | 44.73 | strong downtrend | neutral | weak | 50.0 | 0.0 | 48.95 | CCI, CSGP, AMT | PLD, CBRE, ARE |
| 10 | Technology | 42.39 | downtrend | neutral | weak | 59.02 | 100.0 | 47.75 | ACN, PTC, INTU | SNDK, STX, FLEX |
| 11 | Semiconductors | 41.48 | downtrend | negative | weak | 76.08 | 90.0 | 39.55 | SMH, SOXX | SOXX, SMH |
| 12 | Industrials | 36.02 | strong downtrend | neutral | weak | 66.73 | 65.0 | 44.77 | EFX, PAYX, LMT | VRT, FIX, BE |
| 13 | Grid Infrastructure | 35.08 | strong downtrend | negative | weak | 69.75 | 65.0 | 41.09 | GRID | GRID |
| 14 | Defense | 32.88 | strong downtrend | negative | weak | 40.03 | 65.0 | 37.62 | XAR | XAR |
| 15 | Nuclear | 31.08 | strong downtrend | negative | weak | 50.0 | 0.0 | 34.53 | NLR | NLR |

### Thematic Strength

| Rank | Theme | Score | Setup | ETF Flow | Flow Reliability | Dispersion | Price | News |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Energy | 67.42 | Positive setup | 52.25 | 100.0 | 2.34 | True | False |
| 2 | Cybersecurity | 63.49 | Positive setup | 68.21 | 65.0 | 30.62 | True | False |
| 3 | Healthcare Innovation | 61.19 | Positive setup | 65.59 | 90.0 | 13.38 | True | False |
| 4 | Dividend Defensives | 59.67 | Positive setup | 59.11 | 65.0 | 2.69 | False | False |
| 5 | Crypto Infrastructure | 48.1 | Neutral / watchlist | 63.81 | 65.0 | 7.77 | False | False |
| 6 | Quality Growth | 46.93 | Neutral / watchlist | 56.41 | 65.0 | 8.85 | False | False |
| 7 | AI Infrastructure | 45.28 | Neutral / watchlist | 76.08 | 90.0 | 18.11 | False | False |
| 8 | Defense | 43.02 | Weak setup | 40.03 | 65.0 | 35.23 | False | False |
| 9 | Semiconductors | 40.78 | Weak setup | 76.08 | 90.0 | 11.78 | False | False |
| 10 | Financials | 39.39 | Weak setup | 50.0 | 0.0 | 12.76 | False | False |
| 11 | Grid Infrastructure | 38.6 | Weak setup | 69.75 | 65.0 | 24.51 | False | False |
| 12 | Small Caps | 35.61 | Weak setup | 48.21 | 65.0 | 0.0 | False | False |
| 13 | Nuclear | 27.22 | Underperformance risk | 50.0 | 0.0 | 19.59 | False | False |

- Top 5 improving themes: Cybersecurity, Crypto Infrastructure, Energy, Healthcare Innovation, Quality Growth
- Top 5 deteriorating themes: Nuclear, Financials, Grid Infrastructure, Defense, Small Caps
- Strong news but weak price confirmation: none
- Strong price but weak news confirmation: Energy, Cybersecurity, Healthcare Innovation

### Sector / Theme Alignment

| Sector | Related Themes | Sector Score | Sector Signal | Theme Score | Theme Signal | Interpretation |
| --- | --- | --- | --- | --- | --- | --- |
| Energy | Energy | 68.83 | strong | 67.42 | strong | sector and theme confirmation |
| Cybersecurity | Cybersecurity | 68.52 | strong | 63.49 | positive | sector and theme confirmation |
| Consumer Staples | Dividend Defensives | 68.45 | strong | 59.67 | positive | sector and theme confirmation |
| Healthcare | Healthcare Innovation | 68.12 | strong | 61.19 | positive | sector and theme confirmation |
| Utilities | Grid Infrastructure, Nuclear, Dividend Defensives | 57.21 | positive | 41.83 | weak | sector stronger than related themes |
| Financials | Financials | 55.02 | positive | 39.39 | weak | sector stronger than related themes |
| Crypto | Crypto Infrastructure | 51.38 | mixed | 48.1 | mixed | mixed confirmation |
| Consumer Discretionary | Small Caps | 45.81 | mixed | 35.61 | weak | mixed confirmation |
| Real Estate | Dividend Defensives | 44.73 | weak | 59.67 | positive | theme stronger than official sector |
| Technology | AI Infrastructure, Semiconductors, Quality Growth | 42.39 | weak | 44.33 | weak | broad weakness across sector and themes |
| Semiconductors | AI Infrastructure, Semiconductors | 41.48 | weak | 43.03 | weak | broad weakness across sector and themes |
| Industrials | Defense, Grid Infrastructure | 36.02 | weak | 40.81 | weak | broad weakness across sector and themes |
| Grid Infrastructure | Grid Infrastructure | 35.08 | weak | 38.6 | weak | broad weakness across sector and themes |
| Defense | Defense | 32.88 | very weak | 43.02 | weak | broad weakness across sector and themes |
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

- VIX close=18.58 pct_chg=-4.47

## News Analytics

- Sentiment counts: {'positive': 0, 'negative': 0, 'neutral': 80}
- News confirmation score: `50.0`

### Top Market-Moving Headlines

**1. Stocks rally to start the week, Nasdaq jumps 1% on Anthropic IPO enthusiasm: Live updates**
- Source: CNBC Markets
- Importance / impact: Low / Mixed
- Relevance / horizon: macro / short-term
- Affected assets: IPO
- Score: `23.75`
- Investment implication: Macro-relevant mixed signal; use as context for rates, volatility, and index confirmation over the short-term.

**2. Oil prices fall as Saudi defense minister travels to Iran for talks to de-escalate conflict**
- Source: CNBC Top News
- Importance / impact: Low / Mixed
- Relevance / horizon: macro / short-term
- Affected assets: Equities, Bonds, USD, Commodities
- Score: `23.75`
- Investment implication: Macro-relevant mixed signal; use as context for rates, volatility, and index confirmation over the short-term.

**3. Fanatics teams up with OpenAI for new AI-powered shopping suggestion feature**
- Source: CNBC Top News
- Importance / impact: Low / Mixed
- Relevance / horizon: macro / short-term
- Affected assets: Equities, Bonds, USD, Commodities
- Score: `23.75`
- Investment implication: Macro-relevant mixed signal; use as context for rates, volatility, and index confirmation over the short-term.

**4. Economic calendar: A busy week is capped by the Fed's decision**
- Source: MarketWatch Bulletins
- Importance / impact: Low / Mixed
- Relevance / horizon: macro / short-term
- Affected assets: A
- Score: `23.75`
- Investment implication: Macro-relevant mixed signal; use as context for rates, volatility, and index confirmation over the short-term.

**5. The stock market’s biggest test in weeks is here**
- Source: MarketWatch Top Stories
- Importance / impact: Low / Mixed
- Relevance / horizon: sector_theme / short-term
- Affected assets: A, I
- Score: `21.25`
- Investment implication: Theme or sector mixed signal; requires price and volume confirmation before affecting rankings.

**6. These four shocks could hand investors an unexpected buying window, strategists say**
- Source: MarketWatch Top Stories
- Importance / impact: Low / Mixed
- Relevance / horizon: macro / short-term
- Affected assets: Equities, Bonds, USD, Commodities
- Score: `21.25`
- Investment implication: Macro-relevant mixed signal; use as context for rates, volatility, and index confirmation over the short-term.

**7. Dow, S&P and Nasdaq climb in morning trading as Anthropic files for IPO**
- Source: MarketWatch Bulletins
- Importance / impact: Low / Mixed
- Relevance / horizon: sector_theme / short-term
- Affected assets: IPO, P, S
- Score: `20.19`
- Investment implication: Theme or sector mixed signal; requires price and volume confirmation before affecting rankings.

**8. We stopped helping our neighbors with free home repairs and our friendship cooled. Who’s to blame?**
- Source: MarketWatch Top Stories
- Importance / impact: Low / Mixed
- Relevance / horizon: sector_theme / short-term
- Affected assets: A, SUV
- Score: `18.06`
- Investment implication: Theme or sector mixed signal; requires price and volume confirmation before affecting rankings.

**9. My spouse was awarded $90,000 from my 401(k) in our divorce. How is that fair?**
- Source: MarketWatch Top Stories
- Importance / impact: Low / Mixed
- Relevance / horizon: single_name / short-term
- Affected assets: I
- Score: `16.25`
- Investment implication: Single-name mixed signal; low weight unless it maps to a broader sector or theme.

**10. Is getting a wedding band from Quince a bad idea? It’s a third of the price of a local jeweler.**
- Source: MarketWatch Top Stories
- Importance / impact: Low / Mixed
- Relevance / horizon: single_name / short-term
- Affected assets: I
- Score: `16.25`
- Investment implication: Single-name mixed signal; low weight unless it maps to a broader sector or theme.


### Headline Quality Checks

Noisy headline list: Investors are doing just as well this year by shun, Support for semiconductor stocks could be as much 

## Positioning & Flow Dashboard

Positioning and flow data is used as confirmation only.

### Deferred Flow Sections

- Official ETF / fund flows: current report uses shares-outstanding-derived net fund flow estimates from free ETF metadata.
- Institutional Ownership: not available until SEC 13F ingestion is implemented.
- Grouped exposure flow reliability: use issuer coverage and availability status before treating ETF flow as confirmation.

## ETF Flows Analysis

- Market flow regime: `Mixed / Neutral`
- Market flow score: `48.9 / 100`
- Equity risk flow: `45.8`
- Credit risk flow: `55.9`
- Sector cyclicality flow: `45.1`
- Duration/liquidity flow: `50.1`
- Alternatives: `mixed alternative-asset demand`
- ETF flow reliability: `71.5 / 100`
- Dominant allocation direction: `defensive demand`

### Core Flow Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVV | U.S. Broad Equity | -0.2 | -1.0 | 0.5 | -0.7 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural distribution | 79.0 |
| ACWI | Global Equity | -0.6 | -0.8 | 0.0 | 0.5 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Mixed or neutral flow structure; Persistent selling | 77.0 |
| EFA | Developed Markets ex-U.S. | 0.9 | 0.6 | 0.1 | -0.3 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural accumulation; Persistent selling | 83.0 |
| IEMG | Emerging Markets | -0.8 | -0.2 | 0.0 | 0.3 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Medium-term deterioration; Persistent selling | 75.0 |
| IJH | U.S. Mid Cap | -0.9 | 0.6 | 0.3 | -0.5 | Flat | Neutral | Normal | Neutral | Neutral | Structural accumulation | 91.0 |
| IWM | U.S. Small Cap | -0.6 | -0.1 | 0.6 | -0.2 | Down | Sell | Normal | Persistent Distribution | Risk-Off | Strong confirmation | 95.0 |
| LQD | Investment-Grade Credit | 1.0 | -0.9 | 0.7 | -0.1 | Flat | Buy | Normal | Quiet Accumulation | Improving | Medium-term recovery | 87.0 |
| HYG | High-Yield Credit | 0.8 | 0.5 | 0.6 | 0.5 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural accumulation | 91.0 |
| SGOV | Treasury Bills / Cash | -0.5 | -0.3 | 0.8 | -0.5 | Flat | Sell | Normal | Quiet Distribution | Weakening | Tactical profit-taking inside structural accumulation; Strong sponsorship | 91.0 |
| SHY | Short-Duration Treasuries | 1.1 | 2.2 | 0.7 | -0.4 | Flat | Buy | Normal | Quiet Accumulation | Improving | Strong confirmation; Exceptional institutional buying | 100.0 |
| IEF | Intermediate-Duration Treasuries | 0.1 | -1.2 | 0.5 | 3.0 | Up | Neutral | High | Momentum Rally | Watch | Structural distribution | 79.0 |
| TLT | Long-Duration Treasuries | -0.1 | 1.0 | 0.7 | -0.3 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural accumulation | 91.0 |
| GLD | Gold | -0.6 | 1.2 | 0.4 | 0.1 | Down | Sell | Normal | Persistent Distribution | Risk-Off | Medium-term deterioration; Exceptional institutional selling | 75.0 |
| IBIT | Bitcoin | 0.2 | 1.7 | 0.7 | -1.0 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural accumulation | 91.0 |

### Sector Flow Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| XLC | Communication Services | 2.3 | 3.4 | 0.6 | 0.1 | Down | Buy | Normal | Contrarian Buying | Watch | Strong confirmation; Exceptional institutional buying | 100.0 |
| XLY | Consumer Discretionary | -0.9 | -0.2 | 0.4 | -0.0 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural distribution | 79.0 |
| XLP | Consumer Staples | 1.2 | 0.8 | 0.6 | 2.2 | Up | Buy | High | Confirmed Accumulation | Strong Risk-On | Medium-term recovery; Exceptional institutional buying | 95.0 |
| XLE | Energy | 0.3 | 0.1 | 0.6 | 1.2 | Up | Neutral | High | Momentum Rally | Watch | Structural accumulation | 91.0 |
| XLF | Financials | -0.5 | -2.6 | 0.3 | -0.4 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural distribution; Exceptional institutional selling | 71.0 |
| XLV | Health Care | 1.4 | 1.2 | 0.6 | -0.2 | Up | Buy | Normal | Steady Accumulation | Risk-On | Strong confirmation | 95.0 |
| XLI | Industrials | 0.6 | -0.6 | 0.6 | 0.1 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural accumulation | 91.0 |
| XLK | Information Technology | 0.7 | -0.3 | 0.7 | -0.0 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural accumulation | 91.0 |
| XLB | Materials | -1.0 | -1.8 | 0.5 | -0.9 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural distribution | 79.0 |
| XLRE | Real Estate | 0.2 | -1.4 | 0.5 | 1.9 | Up | Neutral | High | Momentum Rally | Watch | Medium-term recovery | 87.0 |
| XLU | Utilities | 1.0 | 1.3 | 0.6 | -0.7 | Up | Sell | Normal | Profit Taking | Slightly Bearish | Tactical profit-taking inside structural accumulation; Exceptional institutional selling | 75.0 |

### Subsector PFV Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ITA | Aerospace and Defense | -0.1 | 0.9 | 0.3 | 0.4 | Down | Buy | Normal | Contrarian Buying | Watch | Tactical rebound inside structural distribution | 83.0 |
| SOXX | Semiconductors | 0.1 | -1.3 | 0.6 | 0.3 | Down | Buy | Normal | Contrarian Buying | Watch | Medium-term recovery; Exceptional institutional buying | 95.0 |
| SMH | Semiconductors | 0.3 | -0.9 | 0.6 | 0.0 | Down | Buy | Normal | Contrarian Buying | Watch | Mixed or neutral flow structure | 85.0 |
| CIBR | Cybersecurity | 0.9 | 2.0 | 0.8 | 1.8 | Up | Sell | High | Distribution into Strength | Bearish Divergence | Tactical profit-taking inside structural accumulation; Exceptional institutional selling, Strong sponsorship | 83.0 |

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
- Macro rows loaded: `48`
- Live macro rows used: `44`
- Economic rows loaded: `113`
- News rows loaded: `80`
- Positioning/flow rows loaded: `30`

## Cycle Metadata

- Report generated at: 27 October 2026, 01:10:52 (HKT)

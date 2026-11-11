# Rule-Based Institutional Market Update

Generated at: 11 November 2026, 19:09:32 (HKT)
Window: 24h

## Executive Dashboard

- Regime score: **49.71 / 100** (Mixed / Rotation)
- US equity strength: **36.63 / 100** (weak)
- Evidence quality: **72.5 / 100**
- ETF flow contribution: **55.78 / 100**, reliability **71.16 / 100**
- Breadth: **healthy**; above 50DMA `68.94%`, above 200DMA `62.99%`
- Top sector score: **Healthcare** `70.57`
- Top theme score: **Healthcare Innovation** `64.09`

## Market Regime Score

| Metric | Value | Driver / Interpretation |
| --- | --- | --- |
| Overall regime | 49.71 | Mixed / Rotation |
| equity_trend | 22.5 | risk-off pressure; Core equity ETFs versus moving averages. |
| equity_momentum | 43.32 | mild risk-off pressure; 5D/20D/60D return momentum across SPY, QQQ, IWM, and SMH. |
| market_breadth | 67.53 | risk-on support; S&P 500 constituent breadth using index membership as of the observation date. |
| volatility | 70.0 | risk-on support; VIX level and change; higher score means calmer volatility conditions. |
| rates_yield_curve | 46.0 | neutral / mixed; Treasury yield pressure and curve shape; higher score means less rates pressure. |
| credit_proxy | 50.0 | neutral / mixed; Credit-market proxy; currently neutral when no direct spread signal is available. |
| dollar_fx | 53.82 | neutral / mixed; Dollar move; higher score means less USD tightening pressure. |
| commodity_confirmation | 67.0 | risk-on support; Copper, silver, oil, and gold mix; higher score means better cyclical confirmation. |
| etf_flow | 54.11 | neutral / mixed; Grouped ETF flow contribution adjusted for reliability. |
| news_confirmation | 46.88 | neutral / mixed; Weighted headline/news confirmation score. |
| Positive contributors |  | volatility=70.0, market_breadth=67.53, commodity_confirmation=67.0 |
| Negative contributors |  | equity_trend=22.5, equity_momentum=43.32 |

## Forward Signal (Score → Expected Return)

Read-only mapping. The regime score is a *state* descriptor, not a forecast; this table states what that score level has historically implied for forward SPY returns.

| Horizon | Bucket | Historical mean | n | Direction |
| --- | --- | --- | --- | --- |
| 5D | 45-50 | 1.3% | 9 | up |
| 20D | 45-50 | 2.32% | 9 | up |
| 60D | 45-50 | 4.94% | 9 | up |

Sample: 2025-10-21 → 2026-08-03, 116 daily origins.
Bottom-vs-top spread at 60D: **6.75 pp** (block-bootstrap 95% CI [1.92, 10.76], P(spread<=0)=<0.0001)
Shape: contrarian across buckets at this horizon — higher score buckets have historically shown *lower* forward returns. The Direction column is the sign of the expected return for this specific bucket, not a statement that a high score is bullish.

Method: Analyst inference/estimate (historical bucket calibration).
- Limitation: sample covers a bull-market window (2025-10-21..2026-08-03); no bear-market stress test is possible with current data
- Limitation: 60D forward windows overlap heavily; bootstrap CI is block-adjusted but effective sample size is small
- Limitation: low-score buckets hold few observations (n=9 daily in the <40 bucket) so the contrarian edge is directionally clear but imprecise

## US Equity Strength Score

| Component | Score |
| --- | --- |
| indices_above_moving_averages | 22.5 |
| sp500_trend | 35.0 |
| nasdaq_trend | 0.0 |
| russell_participation | 55.0 |
| returns_momentum | 43.32 |
| rsi_zone | 48.75 |
| macd_confirmation | 43.75 |
| volume_confirmation | 50.0 |
| breadth | 67.53 |

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
| Rates | 10Y Treasury rising; MOVE rising | Rising yields can pressure duration assets; falling MOVE supports calmer bond volatility. |
| Dollar | DXY proxy stable | A stronger dollar can tighten financial conditions and pressure commodities/emerging-market risk. |
| Credit | HYG falling | High-yield weakness would challenge equity risk-on confirmation. |
| Gold | Gold rising | Gold strength can indicate defensive demand, inflation hedging, or geopolitical concern. |
| Silver | Silver rising | Silver helps distinguish precious-metal demand from industrial/cyclical confirmation when data is available. |
| Copper | Copper rising | Copper strength supports cyclical growth confirmation; weakness would dilute risk-on breadth. |
| Oil | WTI crude rising | Oil spikes can be inflationary risk; falling oil can ease cost pressure but may also flag demand softness. |
| Volatility | VIX falling | Falling VIX supports risk appetite; a volatility spike would reduce confidence in broad risk-on. |

### Macro Snapshot

Live macro rows are intraday snapshots from `public.macro_live`; closed rows are official stored rows from `public.macro`.

| Symbol | Name | Close | Pct Chg | Market Date | Status |
| --- | --- | --- | --- | --- | --- |
| ^GSPC | S&P 500 | 7520.93 | -0.38 | 2026-11-10 | closed |
| ^IXIC | NASDAQ Composite | 25065.88 | -0.74 | 2026-11-10 | closed |
| ^RUT | Russell 2000 Index | 2821.38 | -0.68 | 2026-11-10 | closed |
| ^VIX | CBOE Volatility Index | 18.62 | -4.32 | 2026-11-11 | live as of 11 November 2026, 19:00:20 (HKT) |
| ^SKEW | CBOE SKEW Index | 151.12 | 0.52 | 2026-11-10 | closed |
| ^MOVE | ICE BofA MOVE Index | 92.43 | 7.5 | 2026-11-10 | closed |
| US2YT=X | United States 2-Year Treasury Yield | 4.75 | 4.42 | 2026-11-10 | live as of 11 November 2026, 19:00:20 (HKT) |
| US3YT=X | United States 3-Year Treasury Yield | 4.79 | 4.11 | 2026-11-10 | live as of 11 November 2026, 19:00:20 (HKT) |
| US5YT=X | United States 5-Year Treasury Yield | 4.83 | 3.63 | 2026-11-10 | live as of 11 November 2026, 19:00:20 (HKT) |
| US7YT=X | United States 7-Year Treasury Yield | 4.9 | 3.22 | 2026-11-10 | live as of 11 November 2026, 19:00:20 (HKT) |
| US10YT=X | United States 10-Year Treasury Yield | 4.99 | 2.21 | 2026-11-10 | closed |
| US20YT=X | United States 20-Year Treasury Yield | 5.4 | 2.16 | 2026-11-10 | live as of 11 November 2026, 19:00:20 (HKT) |
| US30YT=X | United States 30-Year Treasury Yield | 5.36 | 1.94 | 2026-11-10 | live as of 11 November 2026, 19:00:20 (HKT) |
| HK50 | Hang Seng Futures | 24224.5 | -0.53 | 2026-11-11 | live as of 11 November 2026, 19:00:20 (HKT) |
| KOR200c1 | KOSPI 200 Futures | 825.3 | 1.63 | 2026-11-11 | live as of 11 November 2026, 19:00:20 (HKT) |
| CIHc1 | SSE 50 Futures | 2746.0 | -0.31 | 2026-11-11 | live as of 11 November 2026, 19:00:20 (HKT) |
| HYG | iShares iBoxx High Yield Corporate Bond ETF | 77.18 | -0.43 | 2026-11-10 | closed |
| LQD | iShares iBoxx Investment Grade Corporate Bond ETF | 103.88 | -0.75 | 2026-11-10 | closed |
| JNK | SPDR Bloomberg High Yield Bond ETF | 92.63 | -0.41 | 2026-11-10 | closed |
| RSP | Invesco S&P 500 Equal Weight ETF | 220.88 | -0.03 | 2026-11-10 | closed |
| IWF | iShares Russell 1000 Growth ETF | 114.02 | -0.86 | 2026-11-10 | closed |
| IWD | iShares Russell 1000 Value ETF | 262.64 | 0.01 | 2026-11-10 | closed |
| TLT | iShares 20+ Year Treasury Bond ETF | 80.88 | -1.32 | 2026-11-10 | closed |
| IEF | iShares 7-10 Year Treasury Bond ETF | 91.01 | -0.86 | 2026-11-10 | closed |
| SHY | iShares 1-3 Year Treasury Bond ETF | 81.32 | -0.33 | 2026-11-10 | closed |
| GC=F | Gold Future | 4059.1 | 0.72 | 2026-11-11 | live as of 11 November 2026, 19:00:20 (HKT) |
| SI=F | Silver Future | 52.97 | 3.66 | 2026-11-11 | live as of 11 November 2026, 19:00:20 (HKT) |
| CL=F | WTI Crude Oil Future | 87.14 | 1.28 | 2026-11-11 | live as of 11 November 2026, 19:00:20 (HKT) |
| HG=F | Copper Future | 6.31 | 1.39 | 2026-11-11 | live as of 11 November 2026, 19:00:20 (HKT) |

## Market Dispersion Analysis

- Sector ETF 20D dispersion: `25.27` points (very high); leader `XLV` (Health Care) `11.33`, laggard `XLK` (Technology) `-13.94`
- Sector ETF 60D dispersion: `24.32` points (very high); leader `XLV` (Health Care) `13.07`, laggard `XLK` (Technology) `-11.25`

| Comparison | Left | Right | 20D Spread | Signal |
| --- | --- | --- | --- | --- |
| Equal-weight vs cap-weight | RSP (Equal-weight S&P 500) | SPY (S&P 500) | 7.16 | broader participation |
| Small-cap vs large-cap | IWM (Russell 2000) | SPY (S&P 500) | 5.01 | small-cap leadership |
| Growth vs value | IWF (Russell 1000 Growth) | IWD (Russell 1000 Value) | -13.49 | value leadership |
| Nasdaq vs S&P 500 | QQQ (Nasdaq 100) | SPY (S&P 500) | -5.64 | S&P 500 leadership |

## Sector Constituent Dispersion

- Breadth 50D / 200D: percentage of active S&P 500 constituents in the sector trading above the 50-day / 200-day moving average.
- Positive 20D: percentage of active sector constituents with positive 20-day return.
- Std 20D: cross-sectional standard deviation of constituent 20-day returns; higher means wider stock-level dispersion.

| Sector | Count | Breadth 50D | Breadth 200D | Positive 20D | 20D Dispersion | Std 20D | Label | Leaders | Laggards |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Communication Services | 22 | 57.14 | 40.0 | 59.09 | 81.72 | 17.52 | very high | APP, CHTR, CMCSA | GOOG, GOOGL, RDDT |
| Information Technology | 76 | 31.58 | 50.67 | 31.58 | 72.25 | 17.92 | very high | ROP, GEN, TYL | SNDK, MRVL, INTC |
| Industrials | 83 | 68.67 | 58.23 | 66.27 | 63.46 | 13.82 | very high | PNR, SWK, EFX | AXON, BE, FIX |
| Financials | 76 | 78.67 | 77.78 | 82.89 | 63.02 | 10.07 | very high | FISV, CBOE, GPN | FIS, HOOD, COIN |
| Health Care | 60 | 93.33 | 91.67 | 93.33 | 54.64 | 8.23 | very high | IDXX, LLY, EW | DVA, DXCM, ILMN |
| Consumer Staples | 33 | 80.65 | 70.97 | 81.82 | 42.94 | 8.11 | very high | CLX, DLTR, HRL | VYLR, BG, ADM |
| Materials | 24 | 79.17 | 66.67 | 83.33 | 37.59 | 8.45 | very high | CRH, MOS, PPG | ALB, IFF, FCX |
| Consumer Discretionary | 47 | 82.98 | 57.45 | 89.36 | 37.57 | 8.51 | very high | HAS, LOW, CVNA | EXPE, DASH, APTV |
| Utilities | 31 | 87.1 | 48.39 | 80.65 | 34.82 | 7.01 | very high | AWK, ED, WEC | NRG, CEG, VST |
| Energy | 21 | 4.76 | 47.62 | 4.76 | 27.92 | 7.05 | very high | SLB, EOG, HAL | MPC, VLO, TPL |
| Real Estate | 30 | 83.33 | 51.72 | 93.33 | 22.18 | 5.37 | very high | EXR, SPG, PSA | CSGP, PLD, IRM |

## Economic Data Snapshot

### U.S. Labor

| Indicator | Latest | Unit | Change | Date | Rule-Based Interpretation |
| --- | --- | --- | --- | --- | --- |
| All Employees, Total Nonfarm | 159044.0 | thousands | 29.0 thousands vs prior | 2026-09-01 | Higher reading supports activity or liquidity. |
| Unemployment Rate | 4.2 | percent | 0.1 pp vs prior | 2026-09-01 | Higher reading increases macro pressure. |
| Initial Claims | 189000.0 | number | -6000.0 number vs prior | 2026-10-31 | Lower claims indicate firmer labor-market conditions. |
| Continued Claims | 1718000.0 | number | 23000.0 number vs prior | 2026-10-24 | Higher claims indicate softer labor-market conditions. |
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
| Headline PCE Price Index month-over-month inflation rate | 0.49 | percent | 0.17 pp vs prior | 2026-09-01 | Higher reading increases macro pressure. |
| Headline PCE Price Index year-over-year inflation rate | 3.65 | percent | 0.2 pp vs prior | 2026-09-01 | Higher reading increases macro pressure. |
| Core PCE Price Index month-over-month inflation rate | 0.32 | percent | 0.05 pp vs prior | 2026-09-01 | Higher reading increases macro pressure. |
| Core PCE Price Index year-over-year inflation rate | 3.12 | percent | 0.09 pp vs prior | 2026-09-01 | Higher reading increases macro pressure. |
| Headline PPI Final Demand month-over-month inflation rate | 1.11 | percent | 0.76 pp vs prior | 2026-09-01 | Higher reading increases macro pressure. |
| Headline PPI Final Demand year-over-year inflation rate | 6.34 | percent | 0.73 pp vs prior | 2026-09-01 | Higher reading increases macro pressure. |
| Core PPI Final Demand Less Foods and Energy month-over-month inflation rate | 0.68 | percent | 0.44 pp vs prior | 2026-09-01 | Higher reading increases macro pressure. |
| Core PPI Final Demand Less Foods and Energy year-over-year inflation rate | 4.98 | percent | 0.17 pp vs prior | 2026-09-01 | Higher reading increases macro pressure. |
| Consumer Price Index for All Urban Consumers | 336.3 | index 1982-1984=100 | 2.17 index pts vs prior | 2026-09-01 | Higher reading increases macro pressure. |
| Core CPI | 338.9 | index 1982-1984=100 | 1.13 index pts vs prior | 2026-09-01 | Higher reading increases macro pressure. |
| Personal Consumption Expenditures Price Index | 132.26 | index 2017=100 | 0.65 index pts vs prior | 2026-09-01 | Higher reading increases macro pressure. |
| Core PCE Price Index | 130.9 | index 2017=100 | 0.41 index pts vs prior | 2026-09-01 | Higher reading increases macro pressure. |
| Producer Price Index: Final Demand | 159.61 | index Nov 2009=100 | 1.76 index pts vs prior | 2026-09-01 | Latest structural macro observation. |
| Producer Price Index: Final Demand Less Foods and Energy | 156.17 | index Apr 2010=100 | 1.06 index pts vs prior | 2026-09-01 | Latest structural macro observation. |

### Policy, Liquidity, Credit

| Indicator | Latest | Unit | Change | Date | Rule-Based Interpretation |
| --- | --- | --- | --- | --- | --- |
| Federal Funds Effective Rate | 3.88 | percent | 0.0 pp vs prior | 2026-11-04 | Stable reading. |
| Secured Overnight Financing Rate | 3.94 | percent | -0.03 pp vs prior | 2026-11-04 | Lower reading eases macro pressure. |
| Effective Federal Funds Rate | 3.75 | percent | 0.12 pp vs prior | 2026-09-01 | Higher reading increases macro pressure. |
| Assets: Total Assets: Federal Reserve | 6753604.0 | millions dollars | -2035.0 millions dollars vs prior | 2026-10-21 | Lower reading signals softer activity or liquidity. |
| M1 Money Stock | 20061.2 | billions dollars | 93.9 billions dollars vs prior | 2026-09-01 | Higher reading supports activity or liquidity. |
| M2 Money Stock | 23413.9 | billions dollars | 113.0 billions dollars vs prior | 2026-09-01 | Higher reading supports activity or liquidity. |
| ICE BofA US High Yield Option-Adjusted Spread | 3.32 | percent | -0.08 pp vs prior | 2026-11-04 | Lower reading eases macro pressure. |
| ICE BofA US Corporate Option-Adjusted Spread | 0.91 | percent | -0.02 pp vs prior | 2026-11-04 | Lower reading eases macro pressure. |

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
| US dollar/Euro ECB reference exchange rate | 1.12 | USD | 0.0 USD vs prior | 2026-11-10 | EUR strengthened versus this currency. |
| Japanese yen/Euro ECB reference exchange rate | 177.38 | JPY | 0.59 JPY vs prior | 2026-11-10 | EUR strengthened versus this currency. |
| Chinese yuan renminbi/Euro ECB reference exchange rate | 7.48 | CNY | 0.01 CNY vs prior | 2026-11-10 | EUR strengthened versus this currency. |
| Australian dollar/Euro ECB reference exchange rate | 1.62 | AUD | 0.0 AUD vs prior | 2026-11-10 | EUR strengthened versus this currency. |

ABS Australia note: ABS rows are stored locally/Neon, but most series are dimension-coded; only curated series should be promoted into narrative report text.

## Sector and Theme Leadership

### Official Sector Strength

Supporting and detracting names are the top/bottom S&P 500 constituents by 20D return when constituent coverage is available; otherwise the report falls back to related ETFs.

| Rank | Sector | Score | Trend | Momentum | Stock Breadth | ETF Flow | Flow Reliability | 3M RS | Supporting / Leaders | Detracting / Laggards |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Healthcare | 70.57 | strong uptrend | positive | broad | 66.21 | 95.0 | 65.37 | IDXX, LLY, EW | DVA, DXCM, ILMN |
| 2 | Consumer Staples | 68.05 | strong uptrend | positive | broad | 46.89 | 65.0 | 61.22 | CLX, DLTR, HRL | VYLR, BG, ADM |
| 3 | Consumer Discretionary | 67.37 | strong uptrend | neutral | broad | 45.76 | 65.0 | 59.46 | HAS, LOW, CVNA | EXPE, DASH, APTV |
| 4 | Real Estate | 66.3 | strong uptrend | neutral | broad | 50.0 | 0.0 | 57.07 | EXR, SPG, PSA | CSGP, PLD, IRM |
| 5 | Financials | 66.11 | strong uptrend | neutral | broad | 38.71 | 90.0 | 57.64 | FISV, CBOE, GPN | FIS, HOOD, COIN |
| 6 | Utilities | 59.12 | uptrend | neutral | broad | 46.77 | 65.0 | 54.4 | AWK, ED, WEC | NRG, CEG, VST |
| 7 | Defense | 54.69 | neutral | neutral | broad | 50.0 | 0.0 | 49.14 | XAR | XAR |
| 8 | Crypto | 49.39 | neutral | neutral | mixed | 43.92 | 65.0 | 50.0 |  |  |
| 9 | Energy | 46.72 | neutral | neutral | weak | 67.52 | 95.0 | 48.65 | SLB, EOG, HAL | MPC, VLO, TPL |
| 10 | Industrials | 46.05 | strong downtrend | neutral | weak | 58.77 | 65.0 | 49.59 | PNR, SWK, EFX | AXON, BE, FIX |
| 11 | Cybersecurity | 40.32 | downtrend | negative | weak | 47.43 | 65.0 | 44.88 | CIBR | CIBR |
| 12 | Nuclear | 35.46 | strong downtrend | negative | weak | 50.0 | 0.0 | 39.16 | NLR | NLR |
| 13 | Semiconductors | 35.41 | strong downtrend | negative | weak | 93.61 | 100.0 | 34.28 | SMH, SOXX | SOXX, SMH |
| 14 | Technology | 35.3 | strong downtrend | negative | weak | 69.13 | 90.0 | 42.62 | ROP, GEN, TYL | SNDK, MRVL, INTC |
| 15 | Grid Infrastructure | 33.35 | strong downtrend | negative | weak | 54.1 | 65.0 | 40.39 | GRID | GRID |

### Thematic Strength

| Rank | Theme | Score | Setup | ETF Flow | Flow Reliability | Dispersion | Price | News |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Healthcare Innovation | 64.09 | Positive setup | 66.21 | 95.0 | 18.51 | True | False |
| 2 | Dividend Defensives | 59.43 | Positive setup | 52.87 | 65.0 | 6.89 | False | False |
| 3 | Small Caps | 49.6 | Neutral / watchlist | 61.44 | 65.0 | 0.0 | False | False |
| 4 | Defense | 49.37 | Neutral / watchlist | 50.0 | 0.0 | 22.52 | False | False |
| 5 | Financials | 46.47 | Neutral / watchlist | 38.71 | 90.0 | 12.41 | False | False |
| 6 | Energy | 46.41 | Neutral / watchlist | 67.52 | 95.0 | 4.44 | False | False |
| 7 | AI Infrastructure | 43.24 | Weak setup | 93.61 | 100.0 | 30.85 | False | True |
| 8 | Quality Growth | 42.17 | Neutral / watchlist | 58.1 | 65.0 | 20.89 | False | False |
| 9 | Cybersecurity | 38.93 | Weak setup | 47.43 | 65.0 | 23.27 | False | False |
| 10 | Grid Infrastructure | 38.14 | Weak setup | 54.1 | 65.0 | 21.74 | False | False |
| 11 | Semiconductors | 37.44 | Weak setup | 93.61 | 100.0 | 19.0 | False | False |
| 12 | Crypto Infrastructure | 31.03 | Weak setup | 43.92 | 65.0 | 6.87 | False | False |
| 13 | Nuclear | 30.68 | Underperformance risk | 50.0 | 0.0 | 9.88 | False | False |

- Top 5 improving themes: Healthcare Innovation, Dividend Defensives, Crypto Infrastructure, Energy, Quality Growth
- Top 5 deteriorating themes: Nuclear, Semiconductors, Defense, Grid Infrastructure, AI Infrastructure
- Strong news but weak price confirmation: AI Infrastructure
- Strong price but weak news confirmation: Healthcare Innovation

### Sector / Theme Alignment

| Sector | Related Themes | Sector Score | Sector Signal | Theme Score | Theme Signal | Interpretation |
| --- | --- | --- | --- | --- | --- | --- |
| Healthcare | Healthcare Innovation | 70.57 | strong | 64.09 | positive | sector and theme confirmation |
| Consumer Staples | Dividend Defensives | 68.05 | strong | 59.43 | positive | sector and theme confirmation |
| Consumer Discretionary | Small Caps | 67.37 | strong | 49.6 | mixed | sector stronger than related themes |
| Real Estate | Dividend Defensives | 66.3 | strong | 59.43 | positive | sector and theme confirmation |
| Financials | Financials | 66.11 | strong | 46.47 | mixed | sector stronger than related themes |
| Utilities | Grid Infrastructure, Nuclear, Dividend Defensives | 59.12 | positive | 42.75 | weak | sector stronger than related themes |
| Defense | Defense | 54.69 | mixed | 49.37 | mixed | mixed confirmation |
| Crypto | Crypto Infrastructure | 49.39 | mixed | 31.03 | very weak | mixed confirmation |
| Energy | Energy | 46.72 | mixed | 46.41 | mixed | mixed confirmation |
| Industrials | Defense, Grid Infrastructure | 46.05 | mixed | 43.76 | weak | mixed confirmation |
| Cybersecurity | Cybersecurity | 40.32 | weak | 38.93 | weak | broad weakness across sector and themes |
| Nuclear | Nuclear | 35.46 | weak | 30.68 | very weak | broad weakness across sector and themes |
| Semiconductors | AI Infrastructure, Semiconductors | 35.41 | weak | 40.34 | weak | broad weakness across sector and themes |
| Technology | AI Infrastructure, Semiconductors, Quality Growth | 35.3 | weak | 40.95 | weak | broad weakness across sector and themes |
| Grid Infrastructure | Grid Infrastructure | 33.35 | very weak | 38.14 | weak | broad weakness across sector and themes |

## Three-Month Outperformance Setup

| Rank | Theme | Score | Classification | Drivers | Invalidation Triggers |
| --- | --- | --- | --- | --- | --- |
| 1 | Healthcare Innovation | 69.06 | Positive setup | relative_strength_20d, relative_strength_60d, trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 2 | Dividend Defensives | 63.1 | Positive setup | relative_strength_20d, trend_persistence, breadth, downside_volatility, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 3 | Defense | 51.7 | Neutral / watchlist | relative_strength_20d, trend_persistence, breadth | relative strength below SPY, breadth below 45%, news turns negative |
| 4 | Energy | 51.29 | Neutral / watchlist | downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 5 | Small Caps | 50.37 | Neutral / watchlist | downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 6 | Financials | 49.32 | Neutral / watchlist | downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 7 | Quality Growth | 46.18 | Neutral / watchlist | downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 8 | Cybersecurity | 42.26 | Weak setup |  | relative strength below SPY, breadth below 45%, news turns negative |
| 9 | AI Infrastructure | 38.47 | Weak setup |  | relative strength below SPY, breadth below 45%, news turns negative |
| 10 | Grid Infrastructure | 38.37 | Weak setup |  | relative strength below SPY, breadth below 45%, news turns negative |
| 11 | Semiconductors | 33.92 | Weak setup |  | relative strength below SPY, breadth below 45%, news turns negative |
| 12 | Crypto Infrastructure | 33.18 | Weak setup | relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |

## Breadth and Participation

- Above 50DMA: `68.94%`
- Above 200DMA: `62.99%`
- Positive 20D return: `70.66%`

## Volatility and Risk Signals

- VIX close=18.62 pct_chg=-4.32

## News Analytics

- Sentiment counts: {'positive': 36, 'negative': 41, 'neutral': 3}
- News confirmation score: `46.88`

### Top Market-Moving Headlines

**1. Fed rate hike odds in December at 88% after hot CPI- CME Fedwatch**
- Source: Investing.com Economic Indicators
- Importance / impact: High / Negative
- Relevance / horizon: macro / short-term
- Affected assets: CME, monetary policy, inflation, interest rates
- Score: `51.48`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the short-term.

**2. Dow, S&P 500 and Nasdaq end lower; Treasury yields rise after hot inflation data**
- Source: MarketWatch Bulletins
- Importance / impact: High / Negative
- Relevance / horizon: macro / short-term
- Affected assets: P, S, inflation, Treasury yields, equity markets
- Score: `51.48`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the short-term.

**3. US Treasury yields surge as hot CPI revives Fed tightening bets**
- Source: Investing.com Economic Indicators
- Importance / impact: High / Negative
- Relevance / horizon: macro / short-term
- Affected assets: US, Inflation, Monetary Policy, Bond Market
- Score: `51.48`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the short-term.

**4. Stocks rally as CoreWeave soothes, bonds reel on rate hike fears**
- Source: Investing.com Economic Indicators
- Importance / impact: Medium / Negative
- Relevance / horizon: sector_theme / short-term
- Affected assets: inflation, monetary policy, bond market
- Score: `49.42`
- Investment implication: Theme or sector negative signal; requires price and volume confirmation before affecting rankings.

**5. October CPI sparks December Fed hike fears as yields surge and tech stocks slide**
- Source: Investing.com Economic Indicators
- Importance / impact: High / Negative
- Relevance / horizon: macro / short-term
- Affected assets: Inflation, Federal Reserve, Interest Rates
- Score: `49.42`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the short-term.

**6. India garment makers rethink reliance on US after tariff shock**
- Source: Investing.com World News
- Importance / impact: High / Negative
- Relevance / horizon: macro / short-term
- Affected assets: US, tariff_policy, trade_relations, supply_chain
- Score: `46.8`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the short-term.

**7. Yen Slumps to Over One-Month Low on Fed Hike Bets**
- Source: Dow Jones Economy
- Importance / impact: High / Negative
- Relevance / horizon: macro / short-term
- Affected assets: USD, JPY, U.S, currency, monetary policy
- Score: `46.06`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the short-term.

**8. 10-year Treasury yield back at 5% as inflation data point to more Fed rate hikes**
- Source: MarketWatch Bulletins
- Importance / impact: Medium / Negative
- Relevance / horizon: macro / short-term
- Affected assets: inflation, monetary policy, interest rates
- Score: `44.61`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the short-term.

**9. S&P 500 futures fall sharply after October inflation data**
- Source: Investing.com Economic Indicators
- Importance / impact: Medium / Negative
- Relevance / horizon: sector_theme / short-term
- Affected assets: P, S, inflation, equity_futures, market_outlook
- Score: `43.76`
- Investment implication: Theme or sector negative signal; requires price and volume confirmation before affecting rankings.

**10. Market spooked because now the Fed may need a supersized hike in December**
- Source: CNBC Markets
- Importance / impact: Medium / Negative
- Relevance / horizon: macro / short-term
- Affected assets: inflation, monetary policy, Federal Reserve
- Score: `43.6`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the short-term.


### Headline Quality Checks

Noisy headline list: Nvidia could soon face tougher export rules, makin

## Positioning & Flow Dashboard

Positioning and flow data is used as confirmation only.

### Deferred Flow Sections

- Official ETF / fund flows: current report uses shares-outstanding-derived net fund flow estimates from free ETF metadata.
- Institutional Ownership: not available until SEC 13F ingestion is implemented.
- Grouped exposure flow reliability: use issuer coverage and availability status before treating ETF flow as confirmation.

## ETF Flows Analysis

- Market flow regime: `Mixed / Neutral`
- Market flow score: `51.2 / 100`
- Equity risk flow: `50.3`
- Credit risk flow: `57.2`
- Sector cyclicality flow: `52.5`
- Duration/liquidity flow: `43.0`
- Alternatives: `mixed alternative-asset demand`
- ETF flow reliability: `71.2 / 100`
- Dominant allocation direction: `risk demand`

### Core Flow Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVV | U.S. Broad Equity | 0.1 | -0.6 | 0.6 | -1.0 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Medium-term recovery | 87.0 |
| ACWI | Global Equity | -0.6 | -0.7 | 0.0 | 0.8 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Mixed or neutral flow structure; Persistent selling | 77.0 |
| EFA | Developed Markets ex-U.S. | -0.2 | 0.6 | 0.0 | 0.1 | Flat | Neutral | Normal | Neutral | Neutral | Mixed or neutral flow structure; Persistent selling | 77.0 |
| IEMG | Emerging Markets | -0.4 | -0.5 | 0.0 | 0.0 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Mixed or neutral flow structure; Persistent selling | 77.0 |
| IJH | U.S. Mid Cap | -0.8 | -0.1 | 0.6 | -0.1 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural accumulation | 91.0 |
| IWM | U.S. Small Cap | 0.6 | 1.4 | 0.7 | -0.3 | Up | Buy | Normal | Steady Accumulation | Risk-On | Strong confirmation | 95.0 |
| LQD | Investment-Grade Credit | 1.1 | -0.3 | 0.7 | -0.4 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural accumulation | 91.0 |
| HYG | High-Yield Credit | 0.5 | 0.8 | 0.7 | -0.1 | Flat | Neutral | Normal | Neutral | Neutral | Structural accumulation | 91.0 |
| SGOV | Treasury Bills / Cash | -1.9 | -1.7 | 0.7 | 0.5 | Flat | Sell | Normal | Quiet Distribution | Weakening | Strong confirmation | 95.0 |
| SHY | Short-Duration Treasuries | 0.7 | 2.3 | 0.8 | -0.4 | Flat | Neutral | Normal | Neutral | Neutral | Structural accumulation; Exceptional institutional buying, Strong sponsorship | 100.0 |
| IEF | Intermediate-Duration Treasuries | 1.3 | 1.2 | 0.6 | 0.0 | Flat | Buy | Normal | Quiet Accumulation | Improving | Strong confirmation | 95.0 |
| TLT | Long-Duration Treasuries | -1.3 | -0.1 | 0.5 | 0.1 | Flat | Neutral | Normal | Neutral | Neutral | Medium-term deterioration | 83.0 |
| GLD | Gold | -0.5 | 0.5 | 0.4 | -0.4 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Medium-term deterioration | 83.0 |
| IBIT | Bitcoin | -0.6 | 0.9 | 0.5 | -0.4 | Down | Sell | Normal | Persistent Distribution | Risk-Off | Medium-term deterioration; Exceptional institutional selling | 75.0 |

### Sector Flow Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| XLC | Communication Services | -1.0 | 1.2 | 0.5 | -0.1 | Flat | Sell | Normal | Quiet Distribution | Weakening | Medium-term deterioration; Exceptional institutional selling | 75.0 |
| XLY | Consumer Discretionary | -0.7 | -1.2 | 0.5 | 0.1 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural distribution | 79.0 |
| XLP | Consumer Staples | -1.3 | -0.0 | 0.4 | -0.2 | Up | Buy | Normal | Steady Accumulation | Risk-On | Tactical rebound inside structural distribution; Exceptional institutional buying | 91.0 |
| XLE | Energy | 0.0 | 0.1 | 0.6 | 0.0 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural accumulation | 91.0 |
| XLF | Financials | -0.3 | -1.7 | 0.3 | -0.4 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural distribution | 79.0 |
| XLV | Health Care | 1.9 | 1.3 | 0.6 | -0.1 | Up | Buy | Normal | Steady Accumulation | Risk-On | Strong confirmation | 95.0 |
| XLI | Industrials | -0.2 | -1.2 | 0.5 | -1.0 | Flat | Neutral | Normal | Neutral | Neutral | Medium-term recovery | 87.0 |
| XLK | Information Technology | 0.5 | 0.5 | 0.6 | 0.3 | Down | Buy | Normal | Contrarian Buying | Watch | Strong confirmation | 95.0 |
| XLB | Materials | -0.4 | -1.5 | 0.5 | -1.0 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Medium-term recovery | 87.0 |
| XLRE | Real Estate | 0.7 | -1.0 | 0.5 | -0.2 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Medium-term recovery | 87.0 |
| XLU | Utilities | -1.5 | 1.2 | 0.3 | -0.9 | Up | Buy | Normal | Steady Accumulation | Risk-On | Medium-term deterioration; Exceptional institutional buying | 91.0 |

### Subsector PFV Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ITA | Aerospace and Defense | 6.5 | 5.8 | 0.3 | -1.1 | Up | Buy | Normal | Steady Accumulation | Risk-On | Strong confirmation; Exceptional institutional buying | 100.0 |
| SOXX | Semiconductors | 5.6 | 3.8 | 0.8 | 0.9 | Down | Buy | Normal | Contrarian Buying | Watch | Strong confirmation; Exceptional institutional buying, Strong sponsorship | 100.0 |
| SMH | Semiconductors | 1.7 | 1.1 | 0.6 | 0.4 | Down | Buy | Normal | Contrarian Buying | Watch | Strong confirmation | 95.0 |
| CIBR | Cybersecurity | -1.0 | 1.0 | 0.6 | -1.0 | Down | Sell | Low | Thin Distribution | Mild Risk-Off | Medium-term deterioration | 83.0 |

### Material Flow Divergences

| Severity | Type | Primary | Comparison | Interpretation |
| --- | --- | --- | --- | --- |
| medium | related_subsector_divergence | XLI | ITA | defense-specific demand differs from broad industrials |
| medium | related_subsector_divergence | XLK | SOXX | technology differs from semiconductors |
| high | close_substitute_divergence | GLD | IAU | primary representative differs from close substitute |
| high | close_substitute_divergence | IVV | SPY | primary representative differs from close substitute |
| high | close_substitute_divergence | AGG | IUSB | primary representative differs from close substitute |
| high | close_substitute_divergence | IVV | SPY | primary representative differs from close substitute |


## Contradiction / Audit Flags

| Severity | Section | Issue | Deterministic Fix |
| --- | --- | --- | --- |
| low | Theme Strength Ranking | AI Infrastructure has strong news confirmation but weak price confirmation. | Classify as unconfirmed narrative. |

## Data Quality Notes

- Technical rows loaded: `60`
- S&P 500 constituent technical rows loaded: `503`
- Macro rows loaded: `48`
- Live macro rows used: `25`
- Economic rows loaded: `113`
- News rows loaded: `80`
- Positioning/flow rows loaded: `30`

## Cycle Metadata

- Report generated at: 11 November 2026, 19:09:32 (HKT)

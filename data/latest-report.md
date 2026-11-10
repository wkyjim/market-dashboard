# Rule-Based Institutional Market Update

Generated at: 10 November 2026, 17:09:35 (HKT)
Window: 24h

## Executive Dashboard

- Regime score: **52.34 / 100** (Mixed / Rotation)
- US equity strength: **40.29 / 100** (weak)
- Evidence quality: **79.5 / 100**
- ETF flow contribution: **55.04 / 100**, reliability **71.16 / 100**
- Breadth: **healthy**; above 50DMA `69.28%`, above 200DMA `62.78%`
- Top sector score: **Healthcare** `70.32`
- Top theme score: **Healthcare Innovation** `64.5`

## Market Regime Score

| Metric | Value | Driver / Interpretation |
| --- | --- | --- |
| Overall regime | 52.34 | Mixed / Rotation |
| equity_trend | 28.75 | risk-off pressure; Core equity ETFs versus moving averages. |
| equity_momentum | 43.97 | mild risk-off pressure; 5D/20D/60D return momentum across SPY, QQQ, IWM, and SMH. |
| market_breadth | 67.33 | risk-on support; S&P 500 constituent breadth using index membership as of the observation date. |
| volatility | 70.0 | risk-on support; VIX level and change; higher score means calmer volatility conditions. |
| rates_yield_curve | 58.0 | mild risk-on support; Treasury yield pressure and curve shape; higher score means less rates pressure. |
| credit_proxy | 50.0 | neutral / mixed; Credit-market proxy; currently neutral when no direct spread signal is available. |
| dollar_fx | 55.69 | mild risk-on support; Dollar move; higher score means less USD tightening pressure. |
| commodity_confirmation | 53.0 | neutral / mixed; Copper, silver, oil, and gold mix; higher score means better cyclical confirmation. |
| etf_flow | 53.59 | neutral / mixed; Grouped ETF flow contribution adjusted for reliability. |
| news_confirmation | 67.5 | risk-on support; Weighted headline/news confirmation score. |
| Positive contributors |  | volatility=70.0, news_confirmation=67.5, market_breadth=67.33 |
| Negative contributors |  | equity_trend=28.75, equity_momentum=43.97 |

## Forward Signal (Score → Expected Return)

Read-only mapping. The regime score is a *state* descriptor, not a forecast; this table states what that score level has historically implied for forward SPY returns.

| Horizon | Bucket | Historical mean | n | Direction |
| --- | --- | --- | --- | --- |
| 5D | 50-55 | 0.69% | 13 | up |
| 20D | 50-55 | 1.5% | 13 | up |
| 60D | 50-55 | 4.7% | 13 | up |

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
| indices_above_moving_averages | 28.75 |
| sp500_trend | 35.0 |
| nasdaq_trend | 0.0 |
| russell_participation | 80.0 |
| returns_momentum | 43.97 |
| rsi_zone | 48.75 |
| macd_confirmation | 43.75 |
| volume_confirmation | 46.25 |
| breadth | 67.33 |

## Evidence Quality / Confidence

- Confidence score: `79.5`
- Agreement ratio: `0.5`
- Contradiction count: `2`
- Missing indicators: none
- Warning flags: none

## Cross-Asset Confirmation

| Area | Signal | Interpretation |
| --- | --- | --- |
| Equities | S&P 500 rising; Nasdaq rising; Russell 2000 rising | Confirms risk appetite when broad indices rise together; weak small caps would narrow the signal. |
| Rates | 10Y Treasury stable; MOVE falling | Rising yields can pressure duration assets; falling MOVE supports calmer bond volatility. |
| Dollar | DXY proxy stable | A stronger dollar can tighten financial conditions and pressure commodities/emerging-market risk. |
| Credit | HYG rising | High-yield weakness would challenge equity risk-on confirmation. |
| Gold | Gold rising | Gold strength can indicate defensive demand, inflation hedging, or geopolitical concern. |
| Silver | Silver rising | Silver helps distinguish precious-metal demand from industrial/cyclical confirmation when data is available. |
| Copper | Copper stable | Copper strength supports cyclical growth confirmation; weakness would dilute risk-on breadth. |
| Oil | WTI crude falling | Oil spikes can be inflationary risk; falling oil can ease cost pressure but may also flag demand softness. |
| Volatility | VIX falling | Falling VIX supports risk appetite; a volatility spike would reduce confidence in broad risk-on. |

### Macro Snapshot

Live macro rows are intraday snapshots from `public.macro_live`; closed rows are official stored rows from `public.macro`.

| Symbol | Name | Close | Pct Chg | Market Date | Status |
| --- | --- | --- | --- | --- | --- |
| ^GSPC | S&P 500 | 7549.94 | 2.35 | 2026-11-09 | closed |
| ^IXIC | NASDAQ Composite | 25253.14 | 2.74 | 2026-11-09 | closed |
| ^RUT | Russell 2000 Index | 2840.81 | 3.15 | 2026-11-09 | closed |
| ^VIX | CBOE Volatility Index | 19.8 | -0.6 | 2026-11-10 | live as of 10 November 2026, 17:00:22 (HKT) |
| ^SKEW | CBOE SKEW Index | 150.34 | -2.09 | 2026-11-09 | closed |
| ^MOVE | ICE BofA MOVE Index | 85.98 | -7.32 | 2026-11-09 | closed |
| US2YT=X | United States 2-Year Treasury Yield | 4.55 | 0.09 | 2026-11-10 | live as of 10 November 2026, 17:00:22 (HKT) |
| US3YT=X | United States 3-Year Treasury Yield | 4.61 | 0.13 | 2026-11-10 | live as of 10 November 2026, 17:00:22 (HKT) |
| US5YT=X | United States 5-Year Treasury Yield | 4.66 | -0.04 | 2026-11-10 | live as of 10 November 2026, 17:00:22 (HKT) |
| US7YT=X | United States 7-Year Treasury Yield | 4.74 | -0.11 | 2026-11-10 | live as of 10 November 2026, 17:00:22 (HKT) |
| US10YT=X | United States 10-Year Treasury Yield | 4.87 | 0.19 | 2026-11-10 | live as of 10 November 2026, 17:00:22 (HKT) |
| US20YT=X | United States 20-Year Treasury Yield | 5.29 | -0.02 | 2026-11-10 | live as of 10 November 2026, 17:00:22 (HKT) |
| US30YT=X | United States 30-Year Treasury Yield | 5.27 | 0.21 | 2026-11-10 | live as of 10 November 2026, 17:00:22 (HKT) |
| HK50 | Hang Seng Futures | 24576.0 | 0.26 | 2026-11-10 | live as of 10 November 2026, 17:00:22 (HKT) |
| KOR200c1 | KOSPI 200 Futures | 808.0 | 4.14 | 2026-11-10 | live as of 10 November 2026, 17:00:22 (HKT) |
| CIHc1 | SSE 50 Futures | 2787.2 | 0.48 | 2026-11-09 | live as of 10 November 2026, 17:00:22 (HKT) |
| HYG | iShares iBoxx High Yield Corporate Bond ETF | 77.51 | 0.36 | 2026-11-09 | closed |
| LQD | iShares iBoxx Investment Grade Corporate Bond ETF | 104.67 | 0.13 | 2026-11-09 | closed |
| JNK | SPDR Bloomberg High Yield Bond ETF | 93.01 | 0.33 | 2026-11-09 | closed |
| RSP | Invesco S&P 500 Equal Weight ETF | 220.95 | 2.27 | 2026-11-09 | closed |
| IWF | iShares Russell 1000 Growth ETF | 115.01 | 2.92 | 2026-11-09 | closed |
| IWD | iShares Russell 1000 Value ETF | 262.61 | 2.0 | 2026-11-09 | closed |
| TLT | iShares 20+ Year Treasury Bond ETF | 81.96 | 0.05 | 2026-11-09 | closed |
| IEF | iShares 7-10 Year Treasury Bond ETF | 91.8 | -0.07 | 2026-11-09 | closed |
| SHY | iShares 1-3 Year Treasury Bond ETF | 81.59 | -0.05 | 2026-11-09 | closed |
| GC=F | Gold Future | 4126.0 | 0.28 | 2026-11-10 | live as of 10 November 2026, 17:00:22 (HKT) |
| SI=F | Silver Future | 52.87 | 0.58 | 2026-11-10 | live as of 10 November 2026, 17:00:22 (HKT) |
| CL=F | WTI Crude Oil Future | 84.28 | -2.96 | 2026-11-10 | live as of 10 November 2026, 17:00:22 (HKT) |
| HG=F | Copper Future | 6.33 | 0.01 | 2026-11-10 | live as of 10 November 2026, 17:00:22 (HKT) |

## Market Dispersion Analysis

- Sector ETF 20D dispersion: `22.48` points (very high); leader `XLV` (Health Care) `9.5`, laggard `XLK` (Technology) `-12.98`
- Sector ETF 60D dispersion: `22.59` points (very high); leader `XLV` (Health Care) `12.52`, laggard `XLK` (Technology) `-10.07`

| Comparison | Left | Right | 20D Spread | Signal |
| --- | --- | --- | --- | --- |
| Equal-weight vs cap-weight | RSP (Equal-weight S&P 500) | SPY (S&P 500) | 6.91 | broader participation |
| Small-cap vs large-cap | IWM (Russell 2000) | SPY (S&P 500) | 4.92 | small-cap leadership |
| Growth vs value | IWF (Russell 1000 Growth) | IWD (Russell 1000 Value) | -12.66 | value leadership |
| Nasdaq vs S&P 500 | QQQ (Nasdaq 100) | SPY (S&P 500) | -5.67 | S&P 500 leadership |

## Sector Constituent Dispersion

- Breadth 50D / 200D: percentage of active S&P 500 constituents in the sector trading above the 50-day / 200-day moving average.
- Positive 20D: percentage of active sector constituents with positive 20-day return.
- Std 20D: cross-sectional standard deviation of constituent 20-day returns; higher means wider stock-level dispersion.

| Sector | Count | Breadth 50D | Breadth 200D | Positive 20D | 20D Dispersion | Std 20D | Label | Leaders | Laggards |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Communication Services | 22 | 57.14 | 40.0 | 54.55 | 88.34 | 17.31 | very high | APP, CMCSA, CHTR | GOOG, GOOGL, RDDT |
| Information Technology | 76 | 35.53 | 52.0 | 31.58 | 70.25 | 18.09 | very high | ROP, GEN, TYL | SNDK, INTC, MRVL |
| Industrials | 83 | 68.67 | 56.96 | 65.06 | 66.19 | 13.59 | very high | PNR, SWK, EFX | BE, AXON, FIX |
| Financials | 76 | 78.67 | 75.0 | 81.58 | 62.49 | 9.54 | very high | FISV, AON, ERIE | FIS, HOOD, COIN |
| Health Care | 60 | 91.67 | 91.67 | 91.67 | 55.07 | 8.55 | very high | IDXX, MRNA, ALGN | CVS, DXCM, ILMN |
| Consumer Staples | 33 | 83.87 | 70.97 | 81.82 | 38.27 | 6.92 | very high | CLX, DLTR, HRL | BG, PM, ADM |
| Consumer Discretionary | 47 | 85.11 | 59.57 | 89.36 | 36.5 | 8.75 | very high | CVNA, HAS, LOW | EXPE, DASH, APTV |
| Materials | 24 | 70.83 | 66.67 | 83.33 | 35.78 | 8.35 | very high | PPG, MOS, CRH | NUE, STLD, FCX |
| Utilities | 31 | 90.32 | 48.39 | 80.65 | 30.49 | 6.34 | very high | AWK, WEC, NEE | CEG, NRG, VST |
| Energy | 21 | 0.0 | 42.86 | 4.76 | 27.13 | 6.2 | very high | SLB, EOG, CVX | MPC, VLO, TPL |
| Real Estate | 30 | 82.76 | 55.17 | 90.0 | 23.17 | 5.36 | very high | EXR, PSA, SPG | DLR, PLD, IRM |

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
| US dollar/Euro ECB reference exchange rate | 1.12 | USD | 0.0 USD vs prior | 2026-11-09 | EUR strengthened versus this currency. |
| Japanese yen/Euro ECB reference exchange rate | 176.79 | JPY | 0.02 JPY vs prior | 2026-11-09 | EUR strengthened versus this currency. |
| Chinese yuan renminbi/Euro ECB reference exchange rate | 7.47 | CNY | 0.02 CNY vs prior | 2026-11-09 | EUR strengthened versus this currency. |
| Australian dollar/Euro ECB reference exchange rate | 1.62 | AUD | -0.0 AUD vs prior | 2026-11-09 | EUR weakened versus this currency. |

ABS Australia note: ABS rows are stored locally/Neon, but most series are dimension-coded; only curated series should be promoted into narrative report text.

## Sector and Theme Leadership

### Official Sector Strength

Supporting and detracting names are the top/bottom S&P 500 constituents by 20D return when constituent coverage is available; otherwise the report falls back to related ETFs.

| Rank | Sector | Score | Trend | Momentum | Stock Breadth | ETF Flow | Flow Reliability | 3M RS | Supporting / Leaders | Detracting / Laggards |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Healthcare | 70.32 | strong uptrend | positive | broad | 68.82 | 95.0 | 63.89 | IDXX, MRNA, ALGN | CVS, DXCM, ILMN |
| 2 | Consumer Staples | 68.0 | strong uptrend | positive | broad | 50.0 | 0.0 | 60.01 | CLX, DLTR, HRL | BG, PM, ADM |
| 3 | Real Estate | 67.35 | strong uptrend | neutral | broad | 50.0 | 0.0 | 56.51 | EXR, PSA, SPG | DLR, PLD, IRM |
| 4 | Financials | 66.81 | strong uptrend | neutral | broad | 50.0 | 0.0 | 56.27 | FISV, AON, ERIE | FIS, HOOD, COIN |
| 5 | Consumer Discretionary | 66.79 | strong uptrend | neutral | broad | 41.74 | 65.0 | 58.8 | CVNA, HAS, LOW | EXPE, DASH, APTV |
| 6 | Utilities | 57.24 | uptrend | neutral | broad | 40.57 | 65.0 | 54.68 | AWK, WEC, NEE | CEG, NRG, VST |
| 7 | Defense | 52.87 | neutral | neutral | broad | 35.6 | 65.0 | 47.92 | XAR | XAR |
| 8 | Crypto | 49.46 | neutral | neutral | mixed | 44.64 | 65.0 | 50.0 |  |  |
| 9 | Energy | 46.69 | neutral | neutral | weak | 64.12 | 90.0 | 49.5 | SLB, EOG, CVX | MPC, VLO, TPL |
| 10 | Nuclear | 42.74 | strong downtrend | negative | weak | 50.0 | 0.0 | 41.84 | NLR | NLR |
| 11 | Industrials | 41.99 | strong downtrend | neutral | weak | 46.83 | 65.0 | 49.31 | PNR, SWK, EFX | BE, AXON, FIX |
| 12 | Cybersecurity | 40.68 | downtrend | negative | weak | 53.79 | 65.0 | 43.9 | CIBR | CIBR |
| 13 | Technology | 39.48 | strong downtrend | negative | weak | 79.9 | 100.0 | 43.17 | ROP, GEN, TYL | SNDK, INTC, MRVL |
| 14 | Grid Infrastructure | 33.81 | strong downtrend | negative | weak | 54.97 | 65.0 | 41.48 | GRID | GRID |
| 15 | Semiconductors | 32.34 | strong downtrend | negative | weak | 65.81 | 100.0 | 34.74 | SMH, SOXX | SOXX, SMH |

### Thematic Strength

| Rank | Theme | Score | Setup | ETF Flow | Flow Reliability | Dispersion | Price | News |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Healthcare Innovation | 64.5 | Positive setup | 68.82 | 95.0 | 17.12 | True | False |
| 2 | Dividend Defensives | 60.38 | Positive setup | 57.96 | 65.0 | 4.31 | True | False |
| 3 | Small Caps | 60.07 | Positive setup | 54.28 | 65.0 | 0.0 | True | False |
| 4 | Financials | 48.03 | Neutral / watchlist | 50.0 | 0.0 | 12.72 | False | False |
| 5 | Energy | 47.05 | Neutral / watchlist | 64.12 | 90.0 | 4.2 | False | False |
| 6 | Defense | 46.92 | Neutral / watchlist | 35.6 | 65.0 | 18.37 | False | False |
| 7 | Quality Growth | 45.68 | Neutral / watchlist | 55.18 | 65.0 | 21.16 | False | False |
| 8 | AI Infrastructure | 41.61 | Weak setup | 65.81 | 100.0 | 23.91 | False | False |
| 9 | Cybersecurity | 40.44 | Weak setup | 53.79 | 65.0 | 24.68 | False | False |
| 10 | Grid Infrastructure | 38.95 | Weak setup | 54.97 | 65.0 | 20.98 | False | False |
| 11 | Semiconductors | 35.49 | Weak setup | 65.81 | 100.0 | 11.12 | False | False |
| 12 | Crypto Infrastructure | 33.32 | Weak setup | 44.64 | 65.0 | 6.81 | False | False |
| 13 | Nuclear | 32.55 | Underperformance risk | 50.0 | 0.0 | 8.08 | False | False |

- Top 5 improving themes: Crypto Infrastructure, Healthcare Innovation, Dividend Defensives, Energy, Quality Growth
- Top 5 deteriorating themes: Nuclear, Defense, Semiconductors, Grid Infrastructure, Financials
- Strong news but weak price confirmation: none
- Strong price but weak news confirmation: Healthcare Innovation, Dividend Defensives, Small Caps

### Sector / Theme Alignment

| Sector | Related Themes | Sector Score | Sector Signal | Theme Score | Theme Signal | Interpretation |
| --- | --- | --- | --- | --- | --- | --- |
| Healthcare | Healthcare Innovation | 70.32 | strong | 64.5 | positive | sector and theme confirmation |
| Consumer Staples | Dividend Defensives | 68.0 | strong | 60.38 | positive | sector and theme confirmation |
| Real Estate | Dividend Defensives | 67.35 | strong | 60.38 | positive | sector and theme confirmation |
| Financials | Financials | 66.81 | strong | 48.03 | mixed | sector stronger than related themes |
| Consumer Discretionary | Small Caps | 66.79 | strong | 60.07 | positive | sector and theme confirmation |
| Utilities | Grid Infrastructure, Nuclear, Dividend Defensives | 57.24 | positive | 43.96 | weak | sector stronger than related themes |
| Defense | Defense | 52.87 | mixed | 46.92 | mixed | mixed confirmation |
| Crypto | Crypto Infrastructure | 49.46 | mixed | 33.32 | very weak | mixed confirmation |
| Energy | Energy | 46.69 | mixed | 47.05 | mixed | mixed confirmation |
| Nuclear | Nuclear | 42.74 | weak | 32.55 | very weak | broad weakness across sector and themes |
| Industrials | Defense, Grid Infrastructure | 41.99 | weak | 42.93 | weak | broad weakness across sector and themes |
| Cybersecurity | Cybersecurity | 40.68 | weak | 40.44 | weak | broad weakness across sector and themes |
| Technology | AI Infrastructure, Semiconductors, Quality Growth | 39.48 | weak | 40.93 | weak | broad weakness across sector and themes |
| Grid Infrastructure | Grid Infrastructure | 33.81 | very weak | 38.95 | weak | broad weakness across sector and themes |
| Semiconductors | AI Infrastructure, Semiconductors | 32.34 | very weak | 38.55 | weak | broad weakness across sector and themes |

## Three-Month Outperformance Setup

| Rank | Theme | Score | Classification | Drivers | Invalidation Triggers |
| --- | --- | --- | --- | --- | --- |
| 1 | Healthcare Innovation | 68.87 | Positive setup | relative_strength_20d, relative_strength_60d, trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 2 | Small Caps | 64.78 | Positive setup | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 3 | Dividend Defensives | 63.9 | Positive setup | relative_strength_20d, trend_persistence, breadth, downside_volatility, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 4 | Energy | 52.35 | Neutral / watchlist | downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 5 | Defense | 51.6 | Neutral / watchlist | trend_persistence, breadth | relative strength below SPY, breadth below 45%, news turns negative |
| 6 | Quality Growth | 50.21 | Neutral / watchlist | downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 7 | Financials | 49.81 | Neutral / watchlist | downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 8 | AI Infrastructure | 42.95 | Weak setup |  | relative strength below SPY, breadth below 45%, news turns negative |
| 9 | Cybersecurity | 42.87 | Weak setup |  | relative strength below SPY, breadth below 45%, news turns negative |
| 10 | Grid Infrastructure | 40.16 | Weak setup |  | relative strength below SPY, breadth below 45%, news turns negative |
| 11 | Semiconductors | 35.17 | Weak setup | volume_accumulation | relative strength below SPY, breadth below 45%, news turns negative |
| 12 | Crypto Infrastructure | 35.15 | Weak setup | relative_strength_60d, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |

## Breadth and Participation

- Above 50DMA: `69.28%`
- Above 200DMA: `62.78%`
- Positive 20D return: `69.94%`

## Volatility and Risk Signals

- VIX close=19.8 pct_chg=-0.6

## News Analytics

- Sentiment counts: {'positive': 53, 'negative': 25, 'neutral': 2}
- News confirmation score: `67.5`

### Top Market-Moving Headlines

**1. Hot U.S. inflation hasn’t cooled off. Rising consumer prices to keep Fed rate hike on track.**
- Source: MarketWatch Top Stories
- Importance / impact: High / Negative
- Relevance / horizon: macro / short-term
- Affected assets: U.S, inflation, monetary policy, interest rates
- Score: `54.19`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the short-term.

**2. Dow ends 1,100 points higher, S&P 500 books best day since April as stocks surge**
- Source: MarketWatch Bulletins
- Importance / impact: Medium / Positive
- Relevance / horizon: sector_theme / short-term
- Affected assets: ^DJI, ^GSPC, P, S, stock market rally
- Score: `46.33`
- Investment implication: Theme or sector positive signal; requires price and volume confirmation before affecting rankings.

**3. Dow up 1,200 points in final hour, S&P and Nasdaq surge after last week's swoon**
- Source: MarketWatch Bulletins
- Importance / impact: Medium / Positive
- Relevance / horizon: sector_theme / short-term
- Affected assets: ^DJI, ^GSPC, ^IXIC, P, S
- Score: `46.33`
- Investment implication: Theme or sector positive signal; requires price and volume confirmation before affecting rankings.

**4. Dow's surge hits 1,000 points today; S&P 500 and Nasdaq also see big gains**
- Source: MarketWatch Bulletins
- Importance / impact: Medium / Positive
- Relevance / horizon: sector_theme / intraday
- Affected assets: P, S, market_movers, index_performance, AI
- Score: `36.03`
- Investment implication: Theme or sector positive signal; requires price and volume confirmation before affecting rankings.

**5. A failed trial for a heart drug casts shadow over rivals developing similar therapies**
- Source: MarketWatch Top Stories
- Importance / impact: Medium / Negative
- Relevance / horizon: single_name / short-term
- Affected assets: A, clinical trial, cardiovascular drug, Lp(a) reduction
- Score: `35.22`
- Investment implication: Single-name negative signal; low weight unless it maps to a broader sector or theme.

**6. SoftBank swings to $7 billion net loss in second quarter as tech selloff weighs on results**
- Source: CNBC Top News
- Importance / impact: Low / Negative
- Relevance / horizon: single_name / quarterly
- Affected assets: 2398.T, earnings, loss, tech selloff
- Score: `34.12`
- Investment implication: Single-name negative signal; low weight unless it maps to a broader sector or theme.

**7. TAG raises 2026 earnings guidance on strong rental growth**
- Source: Investing.com World News
- Importance / impact: Low / Positive
- Relevance / horizon: single_name / short-term
- Affected assets: TAG, earnings guidance, rental growth, corporate guidance
- Score: `32.32`
- Investment implication: Single-name positive signal; low weight unless it maps to a broader sector or theme.

**8. TSMC's October sales jump as global chip boom rolls on**
- Source: CNBC Top News
- Importance / impact: Low / Positive
- Relevance / horizon: single_name / short-term
- Affected assets: TSM, TSMC, earnings, semiconductor, market_outlook
- Score: `32.11`
- Investment implication: Single-name positive signal; low weight unless it maps to a broader sector or theme.

**9. The Trade Desk shares surge 21% after earnings crush Wall Street estimates**
- Source: Investing.com World News
- Importance / impact: Low / Positive
- Relevance / horizon: single_name / short-term
- Affected assets: TTD, earnings, stock surge, market reaction
- Score: `31.7`
- Investment implication: Single-name positive signal; low weight unless it maps to a broader sector or theme.

**10. Merck’s efinopegdutide shows positive results in MASH trial**
- Source: Investing.com Markets
- Importance / impact: Low / Positive
- Relevance / horizon: single_name / short-term
- Affected assets: MASH, drug-development, clinical-trial, hepatology
- Score: `29.94`
- Investment implication: Single-name positive signal; low weight unless it maps to a broader sector or theme.


### Headline Quality Checks

Noisy headline list: The wait is almost over for this blockbuster video

## Positioning & Flow Dashboard

Positioning and flow data is used as confirmation only.

### Deferred Flow Sections

- Official ETF / fund flows: current report uses shares-outstanding-derived net fund flow estimates from free ETF metadata.
- Institutional Ownership: not available until SEC 13F ingestion is implemented.
- Grouped exposure flow reliability: use issuer coverage and availability status before treating ETF flow as confirmation.

## ETF Flows Analysis

- Market flow regime: `Mixed / Neutral`
- Market flow score: `50.6 / 100`
- Equity risk flow: `48.9`
- Credit risk flow: `55.4`
- Sector cyclicality flow: `53.0`
- Duration/liquidity flow: `43.6`
- Alternatives: `mixed alternative-asset demand`
- ETF flow reliability: `71.2 / 100`
- Dominant allocation direction: `risk demand`

### Core Flow Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVV | U.S. Broad Equity | 0.1 | -0.6 | 0.6 | 0.0 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Medium-term recovery | 87.0 |
| ACWI | Global Equity | -0.6 | -0.7 | 0.0 | 1.1 | Down | Neutral | High | Heavy Selling Pressure | Cautious | Mixed or neutral flow structure; Persistent selling | 77.0 |
| EFA | Developed Markets ex-U.S. | -0.2 | 0.6 | 0.0 | 1.0 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Mixed or neutral flow structure; Persistent selling | 77.0 |
| IEMG | Emerging Markets | -0.4 | -0.5 | 0.0 | 0.6 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Mixed or neutral flow structure; Persistent selling | 77.0 |
| IJH | U.S. Mid Cap | -0.5 | 0.2 | 0.6 | 2.4 | Up | Neutral | High | Momentum Rally | Watch | Structural accumulation | 91.0 |
| IWM | U.S. Small Cap | -0.4 | 1.2 | 0.6 | 0.8 | Up | Buy | Normal | Steady Accumulation | Risk-On | Medium-term deterioration | 83.0 |
| LQD | Investment-Grade Credit | 0.9 | -0.3 | 0.7 | -1.2 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Medium-term recovery | 87.0 |
| HYG | High-Yield Credit | 0.3 | 0.7 | 0.6 | -0.5 | Flat | Neutral | Normal | Neutral | Neutral | Structural accumulation | 91.0 |
| SGOV | Treasury Bills / Cash | -1.9 | -1.6 | 0.7 | 0.5 | Flat | Sell | Normal | Quiet Distribution | Weakening | Strong confirmation | 95.0 |
| SHY | Short-Duration Treasuries | 0.5 | 1.8 | 0.8 | 0.2 | Flat | Neutral | Normal | Neutral | Neutral | Structural accumulation; Strong sponsorship | 99.0 |
| IEF | Intermediate-Duration Treasuries | 1.5 | 1.2 | 0.6 | -0.6 | Up | Buy | Normal | Steady Accumulation | Risk-On | Strong confirmation | 95.0 |
| TLT | Long-Duration Treasuries | -1.1 | 0.1 | 0.5 | -0.6 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Medium-term deterioration | 83.0 |
| GLD | Gold | -0.5 | 0.7 | 0.4 | -0.5 | Flat | Neutral | Normal | Neutral | Neutral | Medium-term deterioration | 83.0 |
| IBIT | Bitcoin | -0.5 | 0.9 | 0.5 | -0.7 | Down | Sell | Normal | Persistent Distribution | Risk-Off | Medium-term deterioration; Exceptional institutional selling | 75.0 |

### Sector Flow Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| XLC | Communication Services | -0.8 | 1.5 | 0.5 | 0.7 | Flat | Sell | Normal | Quiet Distribution | Weakening | Medium-term deterioration; Exceptional institutional selling | 75.0 |
| XLY | Consumer Discretionary | -0.9 | -1.4 | 0.5 | 0.4 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural distribution | 79.0 |
| XLP | Consumer Staples | -1.0 | -0.6 | 0.4 | 0.8 | Up | Sell | Normal | Profit Taking | Slightly Bearish | Strong confirmation; Exceptional institutional selling | 87.0 |
| XLE | Energy | 0.0 | 0.1 | 0.6 | 0.7 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural accumulation | 91.0 |
| XLF | Financials | -0.5 | -1.9 | 0.3 | 0.1 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural distribution | 79.0 |
| XLV | Health Care | 2.4 | 1.6 | 0.7 | 0.2 | Up | Buy | Normal | Steady Accumulation | Risk-On | Strong confirmation; Exceptional institutional buying | 100.0 |
| XLI | Industrials | -0.4 | -1.4 | 0.5 | 0.6 | Flat | Sell | Normal | Quiet Distribution | Weakening | Strong confirmation | 95.0 |
| XLK | Information Technology | 0.6 | 0.5 | 0.7 | 1.4 | Down | Buy | High | Aggressive Dip Buying | Recovery Candidate | Strong confirmation; Exceptional institutional buying | 100.0 |
| XLB | Materials | -0.1 | -1.4 | 0.6 | 0.1 | Up | Buy | Normal | Steady Accumulation | Risk-On | Medium-term recovery | 87.0 |
| XLRE | Real Estate | 0.5 | -0.9 | 0.5 | 1.7 | Up | Neutral | High | Momentum Rally | Watch | Medium-term recovery | 87.0 |
| XLU | Utilities | -2.1 | 0.5 | 0.3 | 0.1 | Up | Sell | Normal | Profit Taking | Slightly Bearish | Medium-term deterioration; Exceptional institutional selling | 75.0 |

### Subsector PFV Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ITA | Aerospace and Defense | 7.3 | 6.6 | 0.3 | -0.6 | Up | Buy | Normal | Steady Accumulation | Risk-On | Strong confirmation; Exceptional institutional buying | 100.0 |
| SOXX | Semiconductors | 5.4 | 3.5 | 0.8 | 1.2 | Down | Buy | High | Aggressive Dip Buying | Recovery Candidate | Strong confirmation; Exceptional institutional buying, Strong sponsorship | 100.0 |
| SMH | Semiconductors | 1.4 | 0.2 | 0.6 | 1.5 | Down | Neutral | High | Heavy Selling Pressure | Cautious | Structural accumulation | 91.0 |
| CIBR | Cybersecurity | -0.8 | 1.0 | 0.6 | -0.3 | Down | Sell | Normal | Persistent Distribution | Risk-Off | Medium-term deterioration | 83.0 |

### Material Flow Divergences

| Severity | Type | Primary | Comparison | Interpretation |
| --- | --- | --- | --- | --- |
| medium | related_subsector_divergence | XLI | ITA | defense-specific demand differs from broad industrials |
| medium | related_subsector_divergence | XLK | SOXX | technology differs from semiconductors |
| high | close_substitute_divergence | IVV | SPY | primary representative differs from close substitute |
| high | close_substitute_divergence | AGG | IUSB | primary representative differs from close substitute |
| high | close_substitute_divergence | HYG | JNK | primary representative differs from close substitute |
| high | close_substitute_divergence | IVV | SPY | primary representative differs from close substitute |


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

- Report generated at: 10 November 2026, 17:09:35 (HKT)

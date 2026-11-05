# Rule-Based Institutional Market Update

Generated at: 6 November 2026, 04:07:09 (HKT)
Window: 24h

## Executive Dashboard

- Regime score: **46.05 / 100** (Mixed / Rotation)
- US equity strength: **48.21 / 100** (neutral)
- Evidence quality: **72.5 / 100**
- ETF flow contribution: **52.11 / 100**, reliability **71.16 / 100**
- Breadth: **narrow**; above 50DMA `46.67%`, above 200DMA `55.0%`
- Top sector score: **Consumer Staples** `70.33`
- Top theme score: **Healthcare Innovation** `66.64`

## Market Regime Score

| Metric | Value | Driver / Interpretation |
| --- | --- | --- |
| Overall regime | 46.05 | Mixed / Rotation |
| equity_trend | 42.5 | mild risk-off pressure; Core equity ETFs versus moving averages. |
| equity_momentum | 44.41 | mild risk-off pressure; 5D/20D/60D return momentum across SPY, QQQ, IWM, and SMH. |
| market_breadth | 50.56 | neutral / mixed; Participation breadth from tracked equity/ETF rows. |
| volatility | 20.0 | risk-off pressure; VIX level and change; higher score means calmer volatility conditions. |
| rates_yield_curve | 58.0 | mild risk-on support; Treasury yield pressure and curve shape; higher score means less rates pressure. |
| credit_proxy | 50.0 | neutral / mixed; Credit-market proxy; currently neutral when no direct spread signal is available. |
| dollar_fx | 54.83 | neutral / mixed; Dollar move; higher score means less USD tightening pressure. |
| commodity_confirmation | 46.0 | neutral / mixed; Copper, silver, oil, and gold mix; higher score means better cyclical confirmation. |
| etf_flow | 51.5 | neutral / mixed; Grouped ETF flow contribution adjusted for reliability. |
| news_confirmation | 46.25 | neutral / mixed; Weighted headline/news confirmation score. |
| Positive contributors |  | none |
| Negative contributors |  | volatility=20.0, equity_trend=42.5, equity_momentum=44.41 |

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
| indices_above_moving_averages | 42.5 |
| sp500_trend | 55.0 |
| nasdaq_trend | 35.0 |
| russell_participation | 80.0 |
| returns_momentum | 44.41 |
| rsi_zone | 46.25 |
| macd_confirmation | 43.75 |
| volume_confirmation | 43.75 |
| breadth | 50.56 |

## Evidence Quality / Confidence

- Confidence score: `72.5`
- Agreement ratio: `0.3`
- Contradiction count: `1`
- Missing indicators: none
- Warning flags: none

## Cross-Asset Confirmation

| Area | Signal | Interpretation |
| --- | --- | --- |
| Equities | S&P 500 falling; Nasdaq falling; Russell 2000 falling | Confirms risk appetite when broad indices rise together; weak small caps would narrow the signal. |
| Rates | 10Y Treasury falling; MOVE rising | Rising yields can pressure duration assets; falling MOVE supports calmer bond volatility. |
| Dollar | DXY proxy stable | A stronger dollar can tighten financial conditions and pressure commodities/emerging-market risk. |
| Credit | HYG falling | High-yield weakness would challenge equity risk-on confirmation. |
| Gold | Gold rising | Gold strength can indicate defensive demand, inflation hedging, or geopolitical concern. |
| Silver | Silver rising | Silver helps distinguish precious-metal demand from industrial/cyclical confirmation when data is available. |
| Copper | Copper falling | Copper strength supports cyclical growth confirmation; weakness would dilute risk-on breadth. |
| Oil | WTI crude rising | Oil spikes can be inflationary risk; falling oil can ease cost pressure but may also flag demand softness. |
| Volatility | VIX rising | Falling VIX supports risk appetite; a volatility spike would reduce confidence in broad risk-on. |

### Macro Snapshot

Live macro rows are intraday snapshots from `public.macro_live`; closed rows are official stored rows from `public.macro`.

| Symbol | Name | Close | Pct Chg | Market Date | Status |
| --- | --- | --- | --- | --- | --- |
| ^GSPC | S&P 500 | 7413.45 | -3.58 | 2026-11-05 | live as of 6 November 2026, 04:00:21 (HKT) |
| ^IXIC | NASDAQ Composite | 24569.85 | -4.53 | 2026-11-05 | live as of 6 November 2026, 04:00:21 (HKT) |
| ^RUT | Russell 2000 Index | 2741.63 | -4.04 | 2026-11-05 | live as of 6 November 2026, 04:00:21 (HKT) |
| ^VIX | CBOE Volatility Index | 24.5 | 47.5 | 2026-11-05 | live as of 6 November 2026, 04:00:21 (HKT) |
| ^SKEW | CBOE SKEW Index | 150.9 | 0.59 | 2026-11-04 | closed |
| ^MOVE | ICE BofA MOVE Index | 99.84 | 6.35 | 2026-11-05 | live as of 6 November 2026, 04:00:21 (HKT) |
| US2YT=X | United States 2-Year Treasury Yield | 4.47 | -2.31 | 2026-11-05 | live as of 6 November 2026, 04:00:21 (HKT) |
| US3YT=X | United States 3-Year Treasury Yield | 4.54 | -2.09 | 2026-11-05 | live as of 6 November 2026, 04:00:21 (HKT) |
| US5YT=X | United States 5-Year Treasury Yield | 4.6 | -1.81 | 2026-11-05 | live as of 6 November 2026, 04:00:21 (HKT) |
| US7YT=X | United States 7-Year Treasury Yield | 4.7 | -1.59 | 2026-11-05 | live as of 6 November 2026, 04:00:21 (HKT) |
| US10YT=X | United States 10-Year Treasury Yield | 4.82 | -1.43 | 2026-11-05 | live as of 6 November 2026, 04:00:21 (HKT) |
| US20YT=X | United States 20-Year Treasury Yield | 5.27 | -0.7 | 2026-11-05 | live as of 6 November 2026, 04:00:21 (HKT) |
| US30YT=X | United States 30-Year Treasury Yield | 5.25 | -0.62 | 2026-11-05 | live as of 6 November 2026, 04:00:21 (HKT) |
| HK50 | Hang Seng Futures | 24507.0 | 0.31 | 2026-11-05 | live as of 6 November 2026, 04:00:21 (HKT) |
| KOR200c1 | KOSPI 200 Futures | 847.85 | -4.72 | 2026-11-05 | live as of 6 November 2026, 04:00:21 (HKT) |
| CIHc1 | SSE 50 Futures | 2797.8 | 0.04 | 2026-11-05 | live as of 6 November 2026, 04:00:21 (HKT) |
| HYG | iShares iBoxx High Yield Corporate Bond ETF | 77.28 | -0.31 | 2026-11-05 | live as of 6 November 2026, 04:00:21 (HKT) |
| LQD | iShares iBoxx Investment Grade Corporate Bond ETF | 104.58 | 0.08 | 2026-11-05 | live as of 6 November 2026, 04:00:21 (HKT) |
| JNK | SPDR Bloomberg High Yield Bond ETF | 92.72 | -0.33 | 2026-11-05 | live as of 6 November 2026, 04:00:21 (HKT) |
| RSP | Invesco S&P 500 Equal Weight ETF | 217.69 | -2.53 | 2026-11-05 | live as of 6 November 2026, 04:00:21 (HKT) |
| IWF | iShares Russell 1000 Growth ETF | 111.67 | -5.28 | 2026-11-05 | live as of 6 November 2026, 04:00:21 (HKT) |
| IWD | iShares Russell 1000 Value ETF | 259.6 | -2.15 | 2026-11-05 | live as of 6 November 2026, 04:00:21 (HKT) |
| TLT | iShares 20+ Year Treasury Bond ETF | 82.02 | 0.32 | 2026-11-05 | live as of 6 November 2026, 04:00:21 (HKT) |
| IEF | iShares 7-10 Year Treasury Bond ETF | 91.99 | 0.36 | 2026-11-05 | live as of 6 November 2026, 04:00:21 (HKT) |
| SHY | iShares 1-3 Year Treasury Bond ETF | 81.64 | 0.18 | 2026-11-05 | live as of 6 November 2026, 04:00:21 (HKT) |
| GC=F | Gold Future | 4124.9 | 1.27 | 2026-11-05 | live as of 6 November 2026, 04:00:21 (HKT) |
| SI=F | Silver Future | 52.59 | 0.91 | 2026-11-05 | live as of 6 November 2026, 04:00:21 (HKT) |
| CL=F | WTI Crude Oil Future | 90.57 | 2.78 | 2026-11-05 | live as of 6 November 2026, 04:00:21 (HKT) |
| HG=F | Copper Future | 6.26 | -2.16 | 2026-11-05 | live as of 6 November 2026, 04:00:21 (HKT) |

## Market Dispersion Analysis

- Sector ETF 20D dispersion: `24.89` points (very high); leader `XLP` (Consumer Staples) `12.53`, laggard `XLK` (Technology) `-12.36`
- Sector ETF 60D dispersion: `21.63` points (very high); leader `XLV` (Health Care) `12.89`, laggard `XLI` (Industrials) `-8.75`

| Comparison | Left | Right | 20D Spread | Signal |
| --- | --- | --- | --- | --- |
| Equal-weight vs cap-weight | RSP (Equal-weight S&P 500) | SPY (S&P 500) | 7.38 | broader participation |
| Small-cap vs large-cap | IWM (Russell 2000) | SPY (S&P 500) | 3.62 | small-cap leadership |
| Growth vs value | IWF (Russell 1000 Growth) | IWD (Russell 1000 Value) | -14.22 | value leadership |
| Nasdaq vs S&P 500 | QQQ (Nasdaq 100) | SPY (S&P 500) | -7.34 | S&P 500 leadership |

## Sector Constituent Dispersion

- Breadth 50D / 200D: percentage of active S&P 500 constituents in the sector trading above the 50-day / 200-day moving average.
- Positive 20D: percentage of active sector constituents with positive 20-day return.
- Std 20D: cross-sectional standard deviation of constituent 20-day returns; higher means wider stock-level dispersion.

| Sector | Count | Breadth 50D | Breadth 200D | Positive 20D | 20D Dispersion | Std 20D | Label | Leaders | Laggards |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Information Technology | 76 | 34.21 | 52.0 | 32.89 | 86.45 | 20.42 | very high | GEN, ROP, ACN | LITE, MRVL, INTC |
| Industrials | 83 | 66.27 | 56.96 | 75.9 | 75.34 | 14.42 | very high | PNR, EFX, SWK | CAT, BE, FIX |
| Financials | 76 | 81.33 | 84.72 | 85.53 | 57.13 | 9.9 | very high | FISV, ERIE, AON | FIS, COIN, HOOD |
| Health Care | 60 | 95.0 | 90.0 | 96.67 | 53.27 | 8.93 | very high | IDXX, GEHC, MRNA | TECH, CVS, ILMN |
| Communication Services | 22 | 52.38 | 40.0 | 59.09 | 51.95 | 12.53 | very high | CMCSA, OMC, DIS | GOOG, GOOGL, RDDT |
| Utilities | 31 | 90.32 | 61.29 | 87.1 | 45.32 | 10.44 | very high | AWK, ED, NEE | CEG, NRG, VST |
| Consumer Staples | 33 | 90.32 | 67.74 | 87.88 | 39.31 | 8.18 | very high | DLTR, STZ, CLX | VYLR, BG, ADM |
| Consumer Discretionary | 47 | 91.49 | 63.83 | 97.87 | 36.14 | 7.51 | very high | HAS, LOW, HD | TSLA, GPC, APTV |
| Materials | 24 | 79.17 | 66.67 | 87.5 | 34.83 | 8.74 | very high | VMC, CRH, PPG | CF, ALB, FCX |
| Real Estate | 30 | 89.66 | 65.52 | 100.0 | 32.27 | 7.15 | very high | CCI, EXR, PSA | EQIX, ARE, ESS |
| Energy | 21 | 14.29 | 57.14 | 47.62 | 24.32 | 6.46 | very high | SLB, CVX, COP | MPC, VLO, TPL |

## Economic Data Snapshot

### U.S. Labor

| Indicator | Latest | Unit | Change | Date | Rule-Based Interpretation |
| --- | --- | --- | --- | --- | --- |
| All Employees, Total Nonfarm | 159044.0 | thousands | 29.0 thousands vs prior | 2026-09-01 | Higher reading supports activity or liquidity. |
| Unemployment Rate | 4.2 | percent | 0.1 pp vs prior | 2026-09-01 | Higher reading increases macro pressure. |
| Initial Claims | 194000.0 | number | -6000.0 number vs prior | 2026-10-17 | Lower claims indicate firmer labor-market conditions. |
| Continued Claims | 1701000.0 | number | -21000.0 number vs prior | 2026-10-17 | Lower claims indicate firmer labor-market conditions. |
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
| Federal Funds Effective Rate | 3.88 | percent | 0.0 pp vs prior | 2026-10-29 | Stable reading. |
| Secured Overnight Financing Rate | 3.94 | percent | 0.0 pp vs prior | 2026-10-29 | Stable reading. |
| Effective Federal Funds Rate | 3.75 | percent | 0.12 pp vs prior | 2026-09-01 | Higher reading increases macro pressure. |
| Assets: Total Assets: Federal Reserve | 6753604.0 | millions dollars | -2035.0 millions dollars vs prior | 2026-10-21 | Lower reading signals softer activity or liquidity. |
| M1 Money Stock | 20061.2 | billions dollars | 93.9 billions dollars vs prior | 2026-09-01 | Higher reading supports activity or liquidity. |
| M2 Money Stock | 23413.9 | billions dollars | 113.0 billions dollars vs prior | 2026-09-01 | Higher reading supports activity or liquidity. |
| ICE BofA US High Yield Option-Adjusted Spread | 3.26 | percent | 0.12 pp vs prior | 2026-10-29 | Higher reading increases macro pressure. |
| ICE BofA US Corporate Option-Adjusted Spread | 0.89 | percent | 0.03 pp vs prior | 2026-10-29 | Higher reading increases macro pressure. |

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
| US dollar/Euro ECB reference exchange rate | 1.12 | USD | -0.0 USD vs prior | 2026-11-05 | EUR weakened versus this currency. |
| Japanese yen/Euro ECB reference exchange rate | 177.85 | JPY | -0.45 JPY vs prior | 2026-11-05 | EUR weakened versus this currency. |
| Chinese yuan renminbi/Euro ECB reference exchange rate | 7.48 | CNY | -0.03 CNY vs prior | 2026-11-05 | EUR weakened versus this currency. |
| Australian dollar/Euro ECB reference exchange rate | 1.6 | AUD | -0.0 AUD vs prior | 2026-11-05 | EUR weakened versus this currency. |

ABS Australia note: ABS rows are stored locally/Neon, but most series are dimension-coded; only curated series should be promoted into narrative report text.

## Sector and Theme Leadership

### Official Sector Strength

Supporting and detracting names are the top/bottom S&P 500 constituents by 20D return when constituent coverage is available; otherwise the report falls back to related ETFs.

| Rank | Sector | Score | Trend | Momentum | Stock Breadth | ETF Flow | Flow Reliability | 3M RS | Supporting / Leaders | Detracting / Laggards |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Consumer Staples | 70.33 | strong uptrend | positive | broad | 59.04 | 65.0 | 61.94 | DLTR, STZ, CLX | VYLR, BG, ADM |
| 2 | Healthcare | 70.31 | strong uptrend | positive | broad | 69.49 | 90.0 | 63.56 | IDXX, GEHC, MRNA | TECH, CVS, ILMN |
| 3 | Financials | 68.27 | strong uptrend | positive | broad | 50.0 | 0.0 | 58.05 | FISV, ERIE, AON | FIS, COIN, HOOD |
| 4 | Consumer Discretionary | 67.09 | strong uptrend | positive | broad | 39.3 | 65.0 | 57.95 | HAS, LOW, HD | TSLA, GPC, APTV |
| 5 | Real Estate | 65.7 | strong uptrend | positive | broad | 50.0 | 0.0 | 58.67 | CCI, EXR, PSA | EQIX, ARE, ESS |
| 6 | Utilities | 51.58 | neutral | neutral | broad | 39.31 | 65.0 | 51.66 | AWK, ED, NEE | CEG, NRG, VST |
| 7 | Crypto | 50.02 | neutral | neutral | mixed | 50.15 | 65.0 | 50.0 |  |  |
| 8 | Energy | 48.64 | neutral | neutral | weak | 74.02 | 95.0 | 52.85 | SLB, CVX, COP | MPC, VLO, TPL |
| 9 | Industrials | 45.98 | strong downtrend | neutral | weak | 47.23 | 65.0 | 48.08 | PNR, EFX, SWK | CAT, BE, FIX |
| 10 | Cybersecurity | 44.85 | neutral | negative | weak | 53.57 | 65.0 | 44.79 | CIBR | CIBR |
| 11 | Defense | 42.12 | strong downtrend | negative | weak | 40.85 | 65.0 | 41.56 | XAR | XAR |
| 12 | Technology | 40.36 | downtrend | negative | weak | 60.63 | 95.0 | 42.92 | GEN, ROP, ACN | LITE, MRVL, INTC |
| 13 | Grid Infrastructure | 33.24 | strong downtrend | negative | weak | 61.38 | 65.0 | 39.77 | GRID | GRID |
| 14 | Nuclear | 32.62 | strong downtrend | negative | weak | 50.0 | 0.0 | 30.93 | NLR | NLR |
| 15 | Semiconductors | 31.5 | strong downtrend | negative | weak | 66.33 | 90.0 | 32.85 | SMH, SOXX | SOXX, SMH |

### Thematic Strength

| Rank | Theme | Score | Setup | ETF Flow | Flow Reliability | Dispersion | Price | News |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Healthcare Innovation | 66.64 | Positive setup | 69.49 | 90.0 | 13.99 | True | False |
| 2 | Dividend Defensives | 61.92 | Positive setup | 50.65 | 65.0 | 6.56 | True | False |
| 3 | Small Caps | 61.5 | Positive setup | 53.21 | 65.0 | 0.0 | True | False |
| 4 | Energy | 59.92 | Positive setup | 74.02 | 95.0 | 5.5 | False | False |
| 5 | Financials | 50.73 | Neutral / watchlist | 50.0 | 0.0 | 13.67 | False | False |
| 6 | Defense | 48.5 | Neutral / watchlist | 40.85 | 65.0 | 37.65 | False | False |
| 7 | Quality Growth | 48.25 | Neutral / watchlist | 50.89 | 65.0 | 22.48 | False | False |
| 8 | Cybersecurity | 44.04 | Neutral / watchlist | 53.57 | 65.0 | 36.74 | False | False |
| 9 | AI Infrastructure | 43.63 | Neutral / watchlist | 66.33 | 90.0 | 27.63 | False | False |
| 10 | Crypto Infrastructure | 42.88 | Neutral / watchlist | 50.15 | 65.0 | 8.04 | False | False |
| 11 | Grid Infrastructure | 41.36 | Weak setup | 61.38 | 65.0 | 24.12 | False | False |
| 12 | Semiconductors | 34.94 | Weak setup | 66.33 | 90.0 | 10.77 | False | False |
| 13 | Nuclear | 27.79 | Underperformance risk | 50.0 | 0.0 | 20.93 | False | False |

- Top 5 improving themes: Crypto Infrastructure, Healthcare Innovation, Dividend Defensives, Energy, Cybersecurity
- Top 5 deteriorating themes: Nuclear, Defense, Semiconductors, Grid Infrastructure, Financials
- Strong news but weak price confirmation: none
- Strong price but weak news confirmation: Healthcare Innovation, Dividend Defensives, Small Caps

### Sector / Theme Alignment

| Sector | Related Themes | Sector Score | Sector Signal | Theme Score | Theme Signal | Interpretation |
| --- | --- | --- | --- | --- | --- | --- |
| Consumer Staples | Dividend Defensives | 70.33 | strong | 61.92 | positive | sector and theme confirmation |
| Healthcare | Healthcare Innovation | 70.31 | strong | 66.64 | strong | sector and theme confirmation |
| Financials | Financials | 68.27 | strong | 50.73 | mixed | sector stronger than related themes |
| Consumer Discretionary | Small Caps | 67.09 | strong | 61.5 | positive | sector and theme confirmation |
| Real Estate | Dividend Defensives | 65.7 | strong | 61.92 | positive | sector and theme confirmation |
| Utilities | Grid Infrastructure, Nuclear, Dividend Defensives | 51.58 | mixed | 43.69 | weak | mixed confirmation |
| Crypto | Crypto Infrastructure | 50.02 | mixed | 42.88 | weak | mixed confirmation |
| Energy | Energy | 48.64 | mixed | 59.92 | positive | theme stronger than official sector |
| Industrials | Defense, Grid Infrastructure | 45.98 | mixed | 44.93 | weak | mixed confirmation |
| Cybersecurity | Cybersecurity | 44.85 | weak | 44.04 | weak | broad weakness across sector and themes |
| Defense | Defense | 42.12 | weak | 48.5 | mixed | mixed confirmation |
| Technology | AI Infrastructure, Semiconductors, Quality Growth | 40.36 | weak | 42.27 | weak | broad weakness across sector and themes |
| Grid Infrastructure | Grid Infrastructure | 33.24 | very weak | 41.36 | weak | broad weakness across sector and themes |
| Nuclear | Nuclear | 32.62 | very weak | 27.79 | very weak | broad weakness across sector and themes |
| Semiconductors | AI Infrastructure, Semiconductors | 31.5 | very weak | 39.28 | weak | broad weakness across sector and themes |

## Three-Month Outperformance Setup

| Rank | Theme | Score | Classification | Drivers | Invalidation Triggers |
| --- | --- | --- | --- | --- | --- |
| 1 | Healthcare Innovation | 70.6 | Positive setup | relative_strength_20d, relative_strength_60d, trend_persistence, breadth, volume_accumulation | relative strength below SPY, breadth below 45%, news turns negative |
| 2 | Dividend Defensives | 66.54 | Positive setup | relative_strength_20d, trend_persistence, breadth, volume_accumulation, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 3 | Small Caps | 65.98 | Positive setup | trend_persistence, breadth, volume_accumulation, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 4 | Energy | 62.9 | Positive setup | trend_persistence, breadth, volume_accumulation, downside_volatility, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 5 | Quality Growth | 55.11 | Neutral / watchlist | trend_persistence, breadth, volume_accumulation, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 6 | Financials | 52.56 | Neutral / watchlist | volume_accumulation, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 7 | Defense | 49.98 | Neutral / watchlist | volume_accumulation, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 8 | Cybersecurity | 47.21 | Neutral / watchlist |  | relative strength below SPY, breadth below 45%, news turns negative |
| 9 | Crypto Infrastructure | 46.67 | Neutral / watchlist | relative_strength_60d, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 10 | AI Infrastructure | 46.24 | Neutral / watchlist | volume_accumulation, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 11 | Grid Infrastructure | 42.16 | Weak setup | volume_accumulation, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 12 | Semiconductors | 34.83 | Weak setup | volume_accumulation | relative strength below SPY, breadth below 45%, news turns negative |

## Breadth and Participation

- Above 50DMA: `46.67%`
- Above 200DMA: `55.0%`
- Positive 20D return: `50.0%`

## Volatility and Risk Signals

- VIX close=24.5 pct_chg=47.5

## News Analytics

- Sentiment counts: {'positive': 34, 'negative': 40, 'neutral': 6}
- News confirmation score: `46.25`

### Top Market-Moving Headlines

**1. Fed’s Hammack backs restrictive rates, cites persistent inflation pressures**
- Source: Investing.com Economic Indicators
- Importance / impact: High / Negative
- Relevance / horizon: macro / short-term
- Affected assets: monetary_policy, inflation, interest_rates
- Score: `60.56`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the short-term.

**2. Tankers hit in Hormuz as Iran keeps up pressure after US vote**
- Source: Investing.com Stock Market
- Importance / impact: High / Negative
- Relevance / horizon: macro / short-term
- Affected assets: US, geopolitical risk, energy supply, maritime security
- Score: `54.0`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the short-term.

**3. US tariffs squeeze Canadian cabinet makers facing doubling of Trump duty**
- Source: Investing.com Economic Indicators
- Importance / impact: High / Negative
- Relevance / horizon: macro / short-term
- Affected assets: US, tariffs, trade policy, manufacturing
- Score: `51.48`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the short-term.

**4. Dow soars 1,500 points for best day since April 2025 on clear-cut Democratic win, falling oil: Live updates**
- Source: CNBC Markets
- Importance / impact: High / Positive
- Relevance / horizon: macro / short-term
- Affected assets: U.S, election, political risk, stock market rally
- Score: `51.48`
- Investment implication: Macro-relevant positive signal; use as context for rates, volatility, and index confirmation over the short-term.

**5. World's largest olive oil company plummets 20% after rivals agree to takeover deal**
- Source: CNBC Business News
- Importance / impact: High / Negative
- Relevance / horizon: macro / short-term
- Affected assets: DEO, M&A, Takeover, Stock decline
- Score: `51.0`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the short-term.

**6. Dow scores its best day in 18 months in a broad relief rally after Democrats sweep to power in Congress**
- Source: MarketWatch Top Stories
- Importance / impact: Medium / Positive
- Relevance / horizon: macro / short-term
- Affected assets: Stock Market Rally, Political Shift, Oil Prices
- Score: `41.44`
- Investment implication: Macro-relevant positive signal; use as context for rates, volatility, and index confirmation over the short-term.

**7. European gas slips further as 20% weekly Oil crash overwhelms fresh Hormuz threats**
- Source: Investing.com Stock Market
- Importance / impact: Medium / Negative
- Relevance / horizon: macro / short-term
- Affected assets: BZ, NWG, OIL, energy markets, oil prices
- Score: `41.31`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the short-term.

**8. Micron, Sandisk and other AI stocks are falling hard: ‘Investors don’t like uncertainty’**
- Source: MarketWatch Top Stories
- Importance / impact: Medium / Negative
- Relevance / horizon: sector_theme / short-term
- Affected assets: MU, SNDK, AI, election, uncertainty
- Score: `38.67`
- Investment implication: Theme or sector negative signal; requires price and volume confirmation before affecting rankings.

**9. Interest rates could go ‘significantly higher’ if oil prices keep climbing — even if the Iran war ends soon**
- Source: MarketWatch Top Stories
- Importance / impact: Medium / Negative
- Relevance / horizon: macro / medium-term
- Affected assets: U.S, U.K, interest rates, oil prices, inflation
- Score: `38.67`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the medium-term.

**10. Japan exporter stocks rally as Democrats’ sweep fuels hopes of U.S. tariff relief**
- Source: Investing.com World News
- Importance / impact: Low / Positive
- Relevance / horizon: macro / short-term
- Affected assets: U.S, trade policy, tariffs, market rally
- Score: `34.81`
- Investment implication: Macro-relevant positive signal; use as context for rates, volatility, and index confirmation over the short-term.


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
- Market flow score: `47.8 / 100`
- Equity risk flow: `46.7`
- Credit risk flow: `52.1`
- Sector cyclicality flow: `45.2`
- Duration/liquidity flow: `47.5`
- Alternatives: `mixed alternative-asset demand`
- ETF flow reliability: `71.2 / 100`
- Dominant allocation direction: `mixed allocation`

### Core Flow Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVV | U.S. Broad Equity | -0.1 | -0.8 | 0.5 | -0.2 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Medium-term recovery | 87.0 |
| ACWI | Global Equity | -0.6 | -0.7 | 0.0 | 1.4 | Flat | Neutral | High | High-Turnover Consolidation | Transition | Mixed or neutral flow structure; Persistent selling | 77.0 |
| EFA | Developed Markets ex-U.S. | -0.2 | 0.6 | 0.0 | 0.5 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Mixed or neutral flow structure; Persistent selling | 77.0 |
| IEMG | Emerging Markets | -0.4 | -0.5 | 0.0 | 0.8 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Mixed or neutral flow structure; Persistent selling | 77.0 |
| IJH | U.S. Mid Cap | -0.8 | 0.1 | 0.6 | 0.2 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural accumulation | 91.0 |
| IWM | U.S. Small Cap | -0.9 | 0.9 | 0.6 | 2.0 | Up | Neutral | High | Momentum Rally | Watch | Mixed or neutral flow structure | 85.0 |
| LQD | Investment-Grade Credit | 0.9 | -0.4 | 0.7 | 1.2 | Up | Buy | High | Confirmed Accumulation | Strong Risk-On | Medium-term recovery | 87.0 |
| HYG | High-Yield Credit | -0.2 | 0.4 | 0.5 | 0.7 | Flat | Neutral | Normal | Neutral | Neutral | Medium-term deterioration | 83.0 |
| SGOV | Treasury Bills / Cash | -1.4 | -1.0 | 0.8 | 0.7 | Flat | Sell | Normal | Quiet Distribution | Weakening | Strong confirmation; Strong sponsorship | 100.0 |
| SHY | Short-Duration Treasuries | 0.5 | 1.8 | 0.8 | 0.4 | Flat | Neutral | Normal | Neutral | Neutral | Structural accumulation; Strong sponsorship | 99.0 |
| IEF | Intermediate-Duration Treasuries | 1.7 | 1.3 | 0.6 | -0.0 | Up | Buy | Normal | Steady Accumulation | Risk-On | Strong confirmation | 95.0 |
| TLT | Long-Duration Treasuries | -0.9 | 0.4 | 0.6 | 0.2 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Medium-term deterioration | 83.0 |
| GLD | Gold | -0.9 | 0.7 | 0.3 | 0.5 | Flat | Neutral | Normal | Neutral | Neutral | Medium-term deterioration | 83.0 |
| IBIT | Bitcoin | -0.3 | 1.2 | 0.5 | 0.5 | Down | Sell | High | Confirmed Distribution | Strong Risk-Off | Medium-term deterioration | 83.0 |

### Sector Flow Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| XLC | Communication Services | -0.1 | 1.8 | 0.5 | 2.4 | Down | Sell | High | Confirmed Distribution | Strong Risk-Off | Medium-term deterioration; Exceptional institutional selling | 75.0 |
| XLY | Consumer Discretionary | -1.3 | -1.6 | 0.4 | 4.3 | Up | Sell | High | Distribution into Strength | Bearish Divergence | Strong confirmation | 95.0 |
| XLP | Consumer Staples | 0.4 | 0.3 | 0.5 | 2.3 | Up | Neutral | High | Momentum Rally | Watch | Medium-term recovery | 87.0 |
| XLE | Energy | 0.4 | 0.0 | 0.6 | 4.3 | Flat | Neutral | High | High-Turnover Consolidation | Transition | Structural accumulation | 91.0 |
| XLF | Financials | 0.3 | -2.0 | 0.3 | 1.8 | Up | Buy | High | Confirmed Accumulation | Strong Risk-On | Medium-term recovery | 87.0 |
| XLV | Health Care | 3.0 | 1.8 | 0.7 | 2.8 | Up | Buy | High | Confirmed Accumulation | Strong Risk-On | Strong confirmation; Exceptional institutional buying | 100.0 |
| XLI | Industrials | -0.4 | -1.2 | 0.5 | 2.6 | Flat | Neutral | High | High-Turnover Consolidation | Transition | Mixed or neutral flow structure | 85.0 |
| XLK | Information Technology | 0.2 | 0.0 | 0.6 | 1.7 | Down | Neutral | High | Heavy Selling Pressure | Cautious | Structural accumulation | 91.0 |
| XLB | Materials | -0.1 | -1.4 | 0.7 | 2.9 | Up | Buy | High | Confirmed Accumulation | Strong Risk-On | Medium-term recovery | 87.0 |
| XLRE | Real Estate | 0.4 | -1.0 | 0.5 | 1.3 | Up | Neutral | High | Momentum Rally | Watch | Medium-term recovery | 87.0 |
| XLU | Utilities | -1.5 | 0.8 | 0.3 | 1.3 | Up | Sell | High | Distribution into Strength | Bearish Divergence | Medium-term deterioration | 83.0 |

### Subsector PFV Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ITA | Aerospace and Defense | -0.4 | -0.4 | 0.3 | 1.6 | Up | Sell | High | Distribution into Strength | Bearish Divergence | Strong confirmation; Exceptional institutional selling | 87.0 |
| SOXX | Semiconductors | 1.2 | 0.1 | 0.7 | 2.9 | Down | Neutral | High | Heavy Selling Pressure | Cautious | Structural accumulation | 91.0 |
| SMH | Semiconductors | 0.9 | 0.3 | 0.6 | 1.8 | Down | Neutral | High | Heavy Selling Pressure | Cautious | Structural accumulation | 91.0 |
| CIBR | Cybersecurity | -0.6 | 1.3 | 0.7 | -0.4 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural accumulation | 91.0 |

### Material Flow Divergences

| Severity | Type | Primary | Comparison | Interpretation |
| --- | --- | --- | --- | --- |
| medium | related_subsector_divergence | XLI | ITA | defense-specific demand differs from broad industrials |
| high | close_substitute_divergence | GLD | IAU | primary representative differs from close substitute |
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
- Live macro rows used: `44`
- Economic rows loaded: `113`
- News rows loaded: `80`
- Positioning/flow rows loaded: `30`

## Cycle Metadata

- Report generated at: 06 November 2026, 04:07:09 (HKT)

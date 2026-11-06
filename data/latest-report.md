# Rule-Based Institutional Market Update

Generated at: 6 November 2026, 14:17:56 (HKT)
Window: 24h

## Executive Dashboard

- Regime score: **38.24 / 100** (Mild Risk-Off)
- US equity strength: **24.5 / 100** (weak)
- Evidence quality: **76.0 / 100**
- ETF flow contribution: **52.59 / 100**, reliability **69.31 / 100**
- Breadth: **weak**; above 50DMA `30.0%`, above 200DMA `41.67%`
- Top sector score: **Healthcare** `72.44`
- Top theme score: **Healthcare Innovation** `66.13`

## Market Regime Score

| Metric | Value | Driver / Interpretation |
| --- | --- | --- |
| Overall regime | 38.24 | Mild Risk-Off |
| equity_trend | 8.75 | risk-off pressure; Core equity ETFs versus moving averages. |
| equity_momentum | 38.47 | mild risk-off pressure; 5D/20D/60D return momentum across SPY, QQQ, IWM, and SMH. |
| market_breadth | 36.67 | mild risk-off pressure; Participation breadth from tracked equity/ETF rows. |
| volatility | 20.0 | risk-off pressure; VIX level and change; higher score means calmer volatility conditions. |
| rates_yield_curve | 58.0 | mild risk-on support; Treasury yield pressure and curve shape; higher score means less rates pressure. |
| credit_proxy | 50.0 | neutral / mixed; Credit-market proxy; currently neutral when no direct spread signal is available. |
| dollar_fx | 53.94 | neutral / mixed; Dollar move; higher score means less USD tightening pressure. |
| commodity_confirmation | 51.0 | neutral / mixed; Copper, silver, oil, and gold mix; higher score means better cyclical confirmation. |
| etf_flow | 51.8 | neutral / mixed; Grouped ETF flow contribution adjusted for reliability. |
| news_confirmation | 51.25 | neutral / mixed; Weighted headline/news confirmation score. |
| Positive contributors |  | none |
| Negative contributors |  | equity_trend=8.75, volatility=20.0, market_breadth=36.67, equity_momentum=38.47 |

## Forward Signal (Score → Expected Return)

Read-only mapping. The regime score is a *state* descriptor, not a forecast; this table states what that score level has historically implied for forward SPY returns.

| Horizon | Bucket | Historical mean | n | Direction |
| --- | --- | --- | --- | --- |
| 5D | 0-40 | 0.75% | 9 | up |
| 20D | 0-40 | 6.49% | 9 | up |
| 60D | 0-40 | 9.78% | 9 | up |

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
| indices_above_moving_averages | 8.75 |
| sp500_trend | 35.0 |
| nasdaq_trend | 0.0 |
| russell_participation | 0.0 |
| returns_momentum | 38.47 |
| rsi_zone | 46.25 |
| macd_confirmation | 43.75 |
| volume_confirmation | 35.0 |
| breadth | 36.67 |

## Evidence Quality / Confidence

- Confidence score: `76.0`
- Agreement ratio: `0.4`
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
| Gold | Gold falling | Gold strength can indicate defensive demand, inflation hedging, or geopolitical concern. |
| Silver | Silver falling | Silver helps distinguish precious-metal demand from industrial/cyclical confirmation when data is available. |
| Copper | Copper falling | Copper strength supports cyclical growth confirmation; weakness would dilute risk-on breadth. |
| Oil | WTI crude rising | Oil spikes can be inflationary risk; falling oil can ease cost pressure but may also flag demand softness. |
| Volatility | VIX rising | Falling VIX supports risk appetite; a volatility spike would reduce confidence in broad risk-on. |

### Macro Snapshot

Live macro rows are intraday snapshots from `public.macro_live`; closed rows are official stored rows from `public.macro`.

| Symbol | Name | Close | Pct Chg | Market Date | Status |
| --- | --- | --- | --- | --- | --- |
| ^GSPC | S&P 500 | 7353.73 | -4.36 | 2026-11-05 | closed |
| ^IXIC | NASDAQ Composite | 24315.0 | -5.52 | 2026-11-05 | closed |
| ^RUT | Russell 2000 Index | 2729.89 | -4.45 | 2026-11-05 | closed |
| ^VIX | CBOE Volatility Index | 28.18 | 69.66 | 2026-11-05 | closed |
| ^SKEW | CBOE SKEW Index | 149.37 | -1.01 | 2026-11-05 | closed |
| ^MOVE | ICE BofA MOVE Index | 97.92 | 4.3 | 2026-11-05 | closed |
| US2YT=X | United States 2-Year Treasury Yield | 4.47 | -0.16 | 2026-11-06 | live as of 6 November 2026, 14:00:23 (HKT) |
| US3YT=X | United States 3-Year Treasury Yield | 4.55 | 0.11 | 2026-11-06 | live as of 6 November 2026, 14:00:23 (HKT) |
| US5YT=X | United States 5-Year Treasury Yield | 4.61 | 0.11 | 2026-11-06 | live as of 6 November 2026, 14:00:23 (HKT) |
| US7YT=X | United States 7-Year Treasury Yield | 4.71 | 0.09 | 2026-11-06 | live as of 6 November 2026, 14:00:23 (HKT) |
| US10YT=X | United States 10-Year Treasury Yield | 4.83 | -0.14 | 2026-11-06 | live as of 6 November 2026, 14:00:23 (HKT) |
| US20YT=X | United States 20-Year Treasury Yield | 5.28 | 0.09 | 2026-11-06 | live as of 6 November 2026, 14:00:23 (HKT) |
| US30YT=X | United States 30-Year Treasury Yield | 5.26 | 0.15 | 2026-11-06 | live as of 6 November 2026, 14:00:23 (HKT) |
| HK50 | Hang Seng Futures | 24520.5 | 0.06 | 2026-11-06 | live as of 6 November 2026, 14:00:23 (HKT) |
| KOR200c1 | KOSPI 200 Futures | 775.25 | -7.41 | 2026-11-06 | live as of 6 November 2026, 14:00:23 (HKT) |
| CIHc1 | SSE 50 Futures | 2797.8 | 0.04 | 2026-11-05 | live as of 6 November 2026, 14:00:23 (HKT) |
| HYG | iShares iBoxx High Yield Corporate Bond ETF | 77.28 | -0.31 | 2026-11-05 | closed |
| LQD | iShares iBoxx Investment Grade Corporate Bond ETF | 104.66 | 0.15 | 2026-11-05 | closed |
| JNK | SPDR Bloomberg High Yield Bond ETF | 92.78 | -0.27 | 2026-11-05 | closed |
| RSP | Invesco S&P 500 Equal Weight ETF | 216.87 | -2.89 | 2026-11-05 | closed |
| IWF | iShares Russell 1000 Growth ETF | 110.36 | -6.4 | 2026-11-05 | closed |
| IWD | iShares Russell 1000 Value ETF | 258.38 | -2.61 | 2026-11-05 | closed |
| TLT | iShares 20+ Year Treasury Bond ETF | 81.93 | 0.21 | 2026-11-05 | closed |
| IEF | iShares 7-10 Year Treasury Bond ETF | 91.97 | 0.34 | 2026-11-05 | closed |
| SHY | iShares 1-3 Year Treasury Bond ETF | 81.67 | 0.21 | 2026-11-05 | closed |
| GC=F | Gold Future | 4057.4 | -1.36 | 2026-11-06 | live as of 6 November 2026, 14:00:23 (HKT) |
| SI=F | Silver Future | 51.53 | -1.35 | 2026-11-06 | live as of 6 November 2026, 14:00:23 (HKT) |
| CL=F | WTI Crude Oil Future | 91.5 | 1.08 | 2026-11-06 | live as of 6 November 2026, 14:00:23 (HKT) |
| HG=F | Copper Future | 6.23 | -0.38 | 2026-11-06 | live as of 6 November 2026, 14:00:23 (HKT) |

## Market Dispersion Analysis

- Sector ETF 20D dispersion: `27.86` points (very high); leader `XLV` (Health Care) `9.96`, laggard `XLK` (Technology) `-17.9`
- Sector ETF 60D dispersion: `23.8` points (very high); leader `XLV` (Health Care) `9.78`, laggard `XLK` (Technology) `-14.02`

| Comparison | Left | Right | 20D Spread | Signal |
| --- | --- | --- | --- | --- |
| Equal-weight vs cap-weight | RSP (Equal-weight S&P 500) | SPY (S&P 500) | 7.65 | broader participation |
| Small-cap vs large-cap | IWM (Russell 2000) | SPY (S&P 500) | 2.91 | small-cap leadership |
| Growth vs value | IWF (Russell 1000 Growth) | IWD (Russell 1000 Value) | -15.71 | value leadership |
| Nasdaq vs S&P 500 | QQQ (Nasdaq 100) | SPY (S&P 500) | -8.16 | S&P 500 leadership |

## Sector Constituent Dispersion

- Breadth 50D / 200D: percentage of active S&P 500 constituents in the sector trading above the 50-day / 200-day moving average.
- Positive 20D: percentage of active sector constituents with positive 20-day return.
- Std 20D: cross-sectional standard deviation of constituent 20-day returns; higher means wider stock-level dispersion.

| Sector | Count | Breadth 50D | Breadth 200D | Positive 20D | 20D Dispersion | Std 20D | Label | Leaders | Laggards |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Information Technology | 76 | 25.0 | 34.67 | 27.63 | 86.19 | 21.78 | very high | ROP, GEN, TYL | INTC, MRVL, LITE |
| Industrials | 83 | 55.42 | 48.1 | 60.24 | 76.85 | 15.33 | very high | PNR, EFX, SWK | CAT, BE, FIX |
| Communication Services | 22 | 47.62 | 25.0 | 45.45 | 67.17 | 14.46 | very high | APP, CMCSA, CHTR | GOOG, GOOGL, RDDT |
| Financials | 76 | 66.67 | 72.22 | 80.26 | 63.31 | 10.34 | very high | FISV, ERIE, AON | IBKR, COIN, HOOD |
| Health Care | 60 | 88.33 | 90.0 | 95.0 | 52.09 | 8.45 | very high | IDXX, GEHC, MRNA | RVTY, CVS, ILMN |
| Utilities | 31 | 83.87 | 54.84 | 83.87 | 46.61 | 10.28 | very high | AWK, ED, WEC | CEG, NRG, VST |
| Real Estate | 30 | 79.31 | 51.72 | 83.33 | 38.63 | 7.55 | very high | CCI, EXR, PSA | ARE, EQIX, IRM |
| Consumer Discretionary | 47 | 82.98 | 61.7 | 89.36 | 37.58 | 7.68 | very high | HAS, LULU, LOW | DASH, APTV, TSLA |
| Materials | 24 | 66.67 | 62.5 | 83.33 | 35.5 | 7.92 | very high | PPG, CRH, VMC | ALB, STLD, FCX |
| Consumer Staples | 33 | 90.32 | 67.74 | 84.85 | 34.02 | 7.58 | very high | CLX, KDP, STZ | SYY, BG, ADM |
| Energy | 21 | 0.0 | 47.62 | 14.29 | 25.27 | 7.2 | very high | SLB, COP, CVX | MPC, VLO, TPL |

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
| 1 | Healthcare | 72.44 | strong uptrend | positive | broad | 68.6 | 90.0 | 65.11 | IDXX, GEHC, MRNA | RVTY, CVS, ILMN |
| 2 | Consumer Staples | 70.22 | strong uptrend | positive | broad | 50.75 | 65.0 | 63.75 | CLX, KDP, STZ | SYY, BG, ADM |
| 3 | Consumer Discretionary | 68.35 | strong uptrend | neutral | broad | 50.0 | 0.0 | 58.32 | HAS, LULU, LOW | DASH, APTV, TSLA |
| 4 | Financials | 67.45 | strong uptrend | neutral | broad | 39.69 | 95.0 | 58.55 | FISV, ERIE, AON | IBKR, COIN, HOOD |
| 5 | Real Estate | 67.19 | strong uptrend | neutral | broad | 39.23 | 65.0 | 60.11 | CCI, EXR, PSA | ARE, EQIX, IRM |
| 6 | Crypto | 50.01 | neutral | neutral | mixed | 50.11 | 65.0 | 50.0 |  |  |
| 7 | Utilities | 47.91 | downtrend | neutral | mixed | 41.52 | 65.0 | 54.94 | AWK, ED, WEC | CEG, NRG, VST |
| 8 | Energy | 46.64 | neutral | neutral | weak | 66.47 | 90.0 | 52.29 | SLB, COP, CVX | MPC, VLO, TPL |
| 9 | Cybersecurity | 38.8 | downtrend | negative | weak | 50.0 | 0.0 | 42.9 | CIBR | CIBR |
| 10 | Industrials | 37.05 | strong downtrend | negative | weak | 50.0 | 0.0 | 48.07 | PNR, EFX, SWK | CAT, BE, FIX |
| 11 | Defense | 34.94 | strong downtrend | negative | weak | 40.94 | 65.0 | 41.09 | XAR | XAR |
| 12 | Technology | 32.65 | strong downtrend | negative | weak | 62.42 | 65.0 | 40.89 | ROP, GEN, TYL | INTC, MRVL, LITE |
| 13 | Grid Infrastructure | 30.74 | strong downtrend | negative | weak | 50.0 | 0.0 | 38.57 | GRID | GRID |
| 14 | Nuclear | 29.15 | strong downtrend | negative | weak | 50.0 | 0.0 | 33.45 | NLR | NLR |
| 15 | Semiconductors | 25.63 | strong downtrend | negative | weak | 76.04 | 90.0 | 15.04 | SMH, SOXX | SOXX, SMH |

### Thematic Strength

| Rank | Theme | Score | Setup | ETF Flow | Flow Reliability | Dispersion | Price | News |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Healthcare Innovation | 66.13 | Positive setup | 68.6 | 90.0 | 13.48 | True | False |
| 2 | Dividend Defensives | 63.1 | Positive setup | 56.04 | 65.0 | 4.53 | True | False |
| 3 | Energy | 49.55 | Neutral / watchlist | 66.47 | 90.0 | 6.19 | False | False |
| 4 | Financials | 46.39 | Neutral / watchlist | 39.69 | 95.0 | 13.21 | False | False |
| 5 | Quality Growth | 44.75 | Neutral / watchlist | 60.99 | 65.0 | 21.42 | False | False |
| 6 | Small Caps | 41.71 | Weak setup | 58.3 | 65.0 | 0.0 | False | False |
| 7 | Defense | 40.42 | Weak setup | 40.94 | 65.0 | 39.26 | False | False |
| 8 | Cybersecurity | 40.15 | Weak setup | 50.0 | 0.0 | 29.25 | False | False |
| 9 | AI Infrastructure | 39.81 | Weak setup | 76.04 | 90.0 | 79.13 | False | False |
| 10 | Crypto Infrastructure | 37.01 | Weak setup | 50.11 | 65.0 | 5.82 | False | False |
| 11 | Grid Infrastructure | 36.78 | Weak setup | 50.0 | 0.0 | 31.15 | False | False |
| 12 | Semiconductors | 31.64 | Underperformance risk | 76.04 | 90.0 | 57.53 | False | False |
| 13 | Nuclear | 27.83 | Underperformance risk | 50.0 | 0.0 | 20.08 | False | False |

- Top 5 improving themes: Crypto Infrastructure, Healthcare Innovation, Dividend Defensives, Energy, Quality Growth
- Top 5 deteriorating themes: Nuclear, Semiconductors, Defense, AI Infrastructure, Grid Infrastructure
- Strong news but weak price confirmation: none
- Strong price but weak news confirmation: Healthcare Innovation, Dividend Defensives

### Sector / Theme Alignment

| Sector | Related Themes | Sector Score | Sector Signal | Theme Score | Theme Signal | Interpretation |
| --- | --- | --- | --- | --- | --- | --- |
| Healthcare | Healthcare Innovation | 72.44 | strong | 66.13 | strong | sector and theme confirmation |
| Consumer Staples | Dividend Defensives | 70.22 | strong | 63.1 | positive | sector and theme confirmation |
| Consumer Discretionary | Small Caps | 68.35 | strong | 41.71 | weak | sector stronger than related themes |
| Financials | Financials | 67.45 | strong | 46.39 | mixed | sector stronger than related themes |
| Real Estate | Dividend Defensives | 67.19 | strong | 63.1 | positive | sector and theme confirmation |
| Crypto | Crypto Infrastructure | 50.01 | mixed | 37.01 | weak | mixed confirmation |
| Utilities | Grid Infrastructure, Nuclear, Dividend Defensives | 47.91 | mixed | 42.57 | weak | mixed confirmation |
| Energy | Energy | 46.64 | mixed | 49.55 | mixed | mixed confirmation |
| Cybersecurity | Cybersecurity | 38.8 | weak | 40.15 | weak | broad weakness across sector and themes |
| Industrials | Defense, Grid Infrastructure | 37.05 | weak | 38.6 | weak | broad weakness across sector and themes |
| Defense | Defense | 34.94 | very weak | 40.42 | weak | broad weakness across sector and themes |
| Technology | AI Infrastructure, Semiconductors, Quality Growth | 32.65 | very weak | 38.73 | weak | broad weakness across sector and themes |
| Grid Infrastructure | Grid Infrastructure | 30.74 | very weak | 36.78 | weak | broad weakness across sector and themes |
| Nuclear | Nuclear | 29.15 | very weak | 27.83 | very weak | broad weakness across sector and themes |
| Semiconductors | AI Infrastructure, Semiconductors | 25.63 | very weak | 35.72 | weak | broad weakness across sector and themes |

## Three-Month Outperformance Setup

| Rank | Theme | Score | Classification | Drivers | Invalidation Triggers |
| --- | --- | --- | --- | --- | --- |
| 1 | Healthcare Innovation | 71.26 | Positive setup | relative_strength_20d, relative_strength_60d, trend_persistence, breadth, volume_accumulation | relative strength below SPY, breadth below 45%, news turns negative |
| 2 | Dividend Defensives | 68.67 | Positive setup | relative_strength_20d, relative_strength_60d, trend_persistence, breadth, volume_accumulation | relative strength below SPY, breadth below 45%, news turns negative |
| 3 | Energy | 53.36 | Neutral / watchlist | volume_accumulation, downside_volatility, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 4 | Quality Growth | 50.02 | Neutral / watchlist | volume_accumulation, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 5 | Financials | 49.83 | Neutral / watchlist | volume_accumulation, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 6 | Defense | 43.48 | Weak setup | volume_accumulation | relative strength below SPY, breadth below 45%, news turns negative |
| 7 | Cybersecurity | 42.88 | Weak setup | volume_accumulation | relative strength below SPY, breadth below 45%, news turns negative |
| 8 | Small Caps | 41.24 | Weak setup | volume_accumulation, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 9 | AI Infrastructure | 39.74 | Weak setup | volume_accumulation | relative strength below SPY, breadth below 45%, news turns negative |
| 10 | Grid Infrastructure | 39.67 | Weak setup | volume_accumulation | relative strength below SPY, breadth below 45%, news turns negative |
| 11 | Crypto Infrastructure | 38.78 | Weak setup | relative_strength_60d, volume_accumulation, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 12 | Nuclear | 28.71 | Underperformance risk | volume_accumulation | relative strength below SPY, breadth below 45%, news turns negative |

## Breadth and Participation

- Above 50DMA: `30.0%`
- Above 200DMA: `41.67%`
- Positive 20D return: `38.33%`

## Volatility and Risk Signals

- VIX close=28.18 pct_chg=69.66

## News Analytics

- Sentiment counts: {'positive': 39, 'negative': 37, 'neutral': 4}
- News confirmation score: `51.25`

### Top Market-Moving Headlines

**1. US tariffs squeeze Canadian cabinet makers facing doubling of Trump duty**
- Source: Investing.com Economic Indicators
- Importance / impact: High / Negative
- Relevance / horizon: macro / short-term
- Affected assets: US, tariffs, trade policy, manufacturing
- Score: `51.48`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the short-term.

**2. Fed’s Hammack backs restrictive rates, cites persistent inflation pressures**
- Source: Investing.com Economic Indicators
- Importance / impact: High / Negative
- Relevance / horizon: macro / short-term
- Affected assets: monetary_policy, inflation, interest_rates
- Score: `51.48`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the short-term.

**3. Unity shares jump on report of takeover interest from Silver Lake, PIF**
- Source: Investing.com World News
- Importance / impact: Medium / Positive
- Relevance / horizon: sector_theme / short-term
- Affected assets: U, PIF, M&A, Takeover, Stock Rally
- Score: `45.9`
- Investment implication: Theme or sector positive signal; requires price and volume confirmation before affecting rankings.

**4. Tankers hit in Hormuz as Iran keeps up pressure after US vote**
- Source: Investing.com Stock Market
- Importance / impact: High / Negative
- Relevance / horizon: macro / short-term
- Affected assets: US, geopolitical risk, energy supply, maritime security
- Score: `45.9`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the short-term.

**5. World's largest olive oil company plummets 20% after rivals agree to takeover deal**
- Source: CNBC Business News
- Importance / impact: Medium / Negative
- Relevance / horizon: macro / short-term
- Affected assets: DEO, M&A, Takeover, Stock decline
- Score: `43.35`
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

**8. Interest rates could go ‘significantly higher’ if oil prices keep climbing — even if the Iran war ends soon**
- Source: MarketWatch Top Stories
- Importance / impact: Medium / Negative
- Relevance / horizon: macro / medium-term
- Affected assets: U.S, U.K, interest rates, oil prices, inflation
- Score: `38.67`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the medium-term.

**9. Micron, Sandisk and other AI stocks see steep drops: ‘Investors don’t like uncertainty’**
- Source: MarketWatch Top Stories
- Importance / impact: Low / Negative
- Relevance / horizon: sector_theme / short-term
- Affected assets: MU, SNDK, AI, election, uncertainty
- Score: `32.87`
- Investment implication: Theme or sector negative signal; requires price and volume confirmation before affecting rankings.

**10. Rheinmetall shares plunge 17% after outlook cut as military contracts stall**
- Source: CNBC Business News
- Importance / impact: Low / Negative
- Relevance / horizon: sector_theme / short-term
- Affected assets: RHMEY, RHM, earnings_outlook, military_contracts, supply_chain_delays
- Score: `31.93`
- Investment implication: Theme or sector negative signal; requires price and volume confirmation before affecting rankings.


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
- Market flow score: `51.9 / 100`
- Equity risk flow: `49.7`
- Credit risk flow: `54.4`
- Sector cyclicality flow: `56.3`
- Duration/liquidity flow: `46.2`
- Alternatives: `mixed alternative-asset demand`
- ETF flow reliability: `69.3 / 100`
- Dominant allocation direction: `mixed allocation`

### Core Flow Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVV | U.S. Broad Equity | 0.0 | -0.7 | 0.6 | 2.3 | Down | Neutral | High | Heavy Selling Pressure | Cautious | Medium-term recovery | 87.0 |
| ACWI | Global Equity | -0.6 | -0.7 | 0.0 | 3.8 | Down | Neutral | High | Heavy Selling Pressure | Cautious | Mixed or neutral flow structure; Persistent selling | 77.0 |
| EFA | Developed Markets ex-U.S. | -0.2 | 0.6 | 0.0 | 2.3 | Flat | Neutral | High | High-Turnover Consolidation | Transition | Mixed or neutral flow structure; Persistent selling | 77.0 |
| IEMG | Emerging Markets | -0.4 | -0.5 | 0.0 | 1.4 | Down | Neutral | High | Heavy Selling Pressure | Cautious | Mixed or neutral flow structure; Persistent selling | 77.0 |
| IJH | U.S. Mid Cap | -0.7 | 0.2 | 0.6 | 2.7 | Down | Neutral | High | Heavy Selling Pressure | Cautious | Structural accumulation | 91.0 |
| IWM | U.S. Small Cap | -0.3 | 2.0 | 0.6 | 3.9 | Down | Buy | High | Aggressive Dip Buying | Recovery Candidate | Medium-term deterioration | 83.0 |
| LQD | Investment-Grade Credit | 0.9 | -0.3 | 0.7 | 2.4 | Up | Buy | High | Confirmed Accumulation | Strong Risk-On | Medium-term recovery | 87.0 |
| HYG | High-Yield Credit | 0.0 | 0.7 | 0.6 | 0.9 | Flat | Neutral | Normal | Neutral | Neutral | Structural accumulation | 91.0 |
| SGOV | Treasury Bills / Cash | -1.5 | -1.1 | 0.8 | 2.9 | Flat | Sell | High | Distribution Before Breakdown | Early Bearish | Strong confirmation; Strong sponsorship | 100.0 |
| SHY | Short-Duration Treasuries | 0.3 | 1.7 | 0.7 | 1.2 | Flat | Neutral | High | High-Turnover Consolidation | Transition | Structural accumulation | 91.0 |
| IEF | Intermediate-Duration Treasuries | 1.6 | 1.2 | 0.6 | 0.7 | Up | Buy | Normal | Steady Accumulation | Risk-On | Strong confirmation | 95.0 |
| TLT | Long-Duration Treasuries | -0.9 | 0.3 | 0.6 | 0.7 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Medium-term deterioration | 83.0 |
| GLD | Gold | -0.6 | 0.6 | 0.3 | 0.7 | Flat | Neutral | Normal | Neutral | Neutral | Medium-term deterioration | 83.0 |
| IBIT | Bitcoin | -0.3 | 1.1 | 0.5 | 0.8 | Down | Sell | High | Confirmed Distribution | Strong Risk-Off | Medium-term deterioration; Exceptional institutional selling | 75.0 |

### Sector Flow Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| XLC | Communication Services | -0.8 | 1.5 | 0.5 | 3.0 | Down | Sell | High | Confirmed Distribution | Strong Risk-Off | Medium-term deterioration; Exceptional institutional selling | 75.0 |
| XLY | Consumer Discretionary | -1.3 | -1.6 | 0.4 | 4.3 | Up | Sell | High | Distribution into Strength | Bearish Divergence | Strong confirmation | 95.0 |
| XLP | Consumer Staples | 0.1 | -0.7 | 0.5 | 4.1 | Up | Neutral | High | Momentum Rally | Watch | Structural distribution | 79.0 |
| XLE | Energy | 0.3 | -0.1 | 0.6 | 3.6 | Down | Neutral | High | Heavy Selling Pressure | Cautious | Medium-term recovery | 87.0 |
| XLF | Financials | 0.7 | -1.4 | 0.4 | 3.3 | Up | Buy | High | Confirmed Accumulation | Strong Risk-On | Medium-term recovery | 87.0 |
| XLV | Health Care | 2.9 | 2.2 | 0.7 | 4.4 | Up | Buy | High | Confirmed Accumulation | Strong Risk-On | Strong confirmation; Exceptional institutional buying | 100.0 |
| XLI | Industrials | -0.4 | -1.2 | 0.5 | 2.6 | Flat | Neutral | High | High-Turnover Consolidation | Transition | Mixed or neutral flow structure | 85.0 |
| XLK | Information Technology | 0.2 | 0.0 | 0.6 | 1.7 | Down | Neutral | High | Heavy Selling Pressure | Cautious | Structural accumulation | 91.0 |
| XLB | Materials | -0.1 | -1.4 | 0.7 | 2.9 | Up | Buy | High | Confirmed Accumulation | Strong Risk-On | Medium-term recovery | 87.0 |
| XLRE | Real Estate | 0.4 | -1.0 | 0.5 | 1.3 | Up | Neutral | High | Momentum Rally | Watch | Medium-term recovery | 87.0 |
| XLU | Utilities | -1.7 | 0.9 | 0.3 | 1.7 | Up | Neutral | High | Momentum Rally | Watch | Medium-term deterioration | 83.0 |

### Subsector PFV Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ITA | Aerospace and Defense | 11.0 | 10.4 | 0.3 | 5.5 | Down | Buy | High | Aggressive Dip Buying | Recovery Candidate | Strong confirmation; Exceptional institutional buying | 93.0 |
| SOXX | Semiconductors | 7.3 | 4.8 | 0.8 | 7.0 | Down | Buy | High | Aggressive Dip Buying | Recovery Candidate | Strong confirmation; Exceptional institutional buying, Strong sponsorship | 100.0 |
| SMH | Semiconductors | 1.2 | 0.4 | 0.6 | 5.0 | Down | Neutral | High | Heavy Selling Pressure | Cautious | Structural accumulation | 91.0 |
| CIBR | Cybersecurity | -0.6 | 1.3 | 0.7 | -0.4 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural accumulation | 91.0 |

### Material Flow Divergences

| Severity | Type | Primary | Comparison | Interpretation |
| --- | --- | --- | --- | --- |
| high | close_substitute_divergence | GLD | IAU | primary representative differs from close substitute |
| high | close_substitute_divergence | AGG | IUSB | primary representative differs from close substitute |
| high | close_substitute_divergence | IWF | IVW | primary representative differs from close substitute |
| high | close_substitute_divergence | SOXX | SMH | primary representative differs from close substitute |
| high | close_substitute_divergence | IWM | IJR | primary representative differs from close substitute |


## Contradiction / Audit Flags

No contradiction flags were triggered by current deterministic rules.

## Data Quality Notes

- Technical rows loaded: `60`
- S&P 500 constituent technical rows loaded: `503`
- Macro rows loaded: `48`
- Live macro rows used: `28`
- Economic rows loaded: `113`
- News rows loaded: `80`
- Positioning/flow rows loaded: `30`

## Cycle Metadata

- Report generated at: 06 November 2026, 14:17:56 (HKT)

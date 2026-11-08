# Rule-Based Institutional Market Update

Generated at: 8 November 2026, 08:18:55 (HKT)
Window: 24h

## Executive Dashboard

- Regime score: **39.68 / 100** (Mild Risk-Off)
- US equity strength: **24.83 / 100** (weak)
- Evidence quality: **79.5 / 100**
- ETF flow contribution: **52.85 / 100**, reliability **66.62 / 100**
- Breadth: **weak**; above 50DMA `33.33%`, above 200DMA `41.67%`
- Top sector score: **Consumer Staples** `69.59`
- Top theme score: **Healthcare Innovation** `64.32`

## Market Regime Score

| Metric | Value | Driver / Interpretation |
| --- | --- | --- |
| Overall regime | 39.68 | Mild Risk-Off |
| equity_trend | 8.75 | risk-off pressure; Core equity ETFs versus moving averages. |
| equity_momentum | 40.27 | mild risk-off pressure; 5D/20D/60D return momentum across SPY, QQQ, IWM, and SMH. |
| market_breadth | 36.11 | mild risk-off pressure; Participation breadth from tracked equity/ETF rows. |
| volatility | 35.0 | risk-off pressure; VIX level and change; higher score means calmer volatility conditions. |
| rates_yield_curve | 58.0 | mild risk-on support; Treasury yield pressure and curve shape; higher score means less rates pressure. |
| credit_proxy | 50.0 | neutral / mixed; Credit-market proxy; currently neutral when no direct spread signal is available. |
| dollar_fx | 51.59 | neutral / mixed; Dollar move; higher score means less USD tightening pressure. |
| commodity_confirmation | 58.0 | mild risk-on support; Copper, silver, oil, and gold mix; higher score means better cyclical confirmation. |
| etf_flow | 51.9 | neutral / mixed; Grouped ETF flow contribution adjusted for reliability. |
| news_confirmation | 42.5 | mild risk-off pressure; Weighted headline/news confirmation score. |
| Positive contributors |  | none |
| Negative contributors |  | equity_trend=8.75, volatility=35.0, market_breadth=36.11, equity_momentum=40.27, news_confirmation=42.5 |

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
| returns_momentum | 40.27 |
| rsi_zone | 45.0 |
| macd_confirmation | 43.75 |
| volume_confirmation | 38.75 |
| breadth | 36.11 |

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
| Rates | 10Y Treasury rising; MOVE falling | Rising yields can pressure duration assets; falling MOVE supports calmer bond volatility. |
| Dollar | DXY proxy rising | A stronger dollar can tighten financial conditions and pressure commodities/emerging-market risk. |
| Credit | HYG stable | High-yield weakness would challenge equity risk-on confirmation. |
| Gold | Gold falling | Gold strength can indicate defensive demand, inflation hedging, or geopolitical concern. |
| Silver | Silver rising | Silver helps distinguish precious-metal demand from industrial/cyclical confirmation when data is available. |
| Copper | Copper rising | Copper strength supports cyclical growth confirmation; weakness would dilute risk-on breadth. |
| Oil | WTI crude falling | Oil spikes can be inflationary risk; falling oil can ease cost pressure but may also flag demand softness. |
| Volatility | VIX falling | Falling VIX supports risk appetite; a volatility spike would reduce confidence in broad risk-on. |

### Macro Snapshot

Live macro rows are intraday snapshots from `public.macro_live`; closed rows are official stored rows from `public.macro`.

| Symbol | Name | Close | Pct Chg | Market Date | Status |
| --- | --- | --- | --- | --- | --- |
| ^GSPC | S&P 500 | 7376.86 | 0.31 | 2026-11-06 | closed |
| ^IXIC | NASDAQ Composite | 24579.42 | 1.09 | 2026-11-06 | closed |
| ^RUT | Russell 2000 Index | 2754.11 | 0.89 | 2026-11-06 | closed |
| ^VIX | CBOE Volatility Index | 25.64 | -9.01 | 2026-11-06 | closed |
| ^SKEW | CBOE SKEW Index | 153.55 | 2.8 | 2026-11-06 | closed |
| ^MOVE | ICE BofA MOVE Index | 92.77 | -5.26 | 2026-11-06 | closed |
| US2YT=X | United States 2-Year Treasury Yield | 4.52 | 1.01 | 2026-11-06 | live as of 8 November 2026, 08:00:20 (HKT) |
| US3YT=X | United States 3-Year Treasury Yield | 4.59 | 0.95 | 2026-11-06 | live as of 8 November 2026, 08:00:20 (HKT) |
| US5YT=X | United States 5-Year Treasury Yield | 4.65 | 0.87 | 2026-11-06 | live as of 8 November 2026, 08:00:20 (HKT) |
| US7YT=X | United States 7-Year Treasury Yield | 4.74 | 0.74 | 2026-11-06 | live as of 8 November 2026, 08:00:20 (HKT) |
| US10YT=X | United States 10-Year Treasury Yield | 4.86 | 0.45 | 2026-11-06 | live as of 8 November 2026, 08:00:20 (HKT) |
| US20YT=X | United States 20-Year Treasury Yield | 5.29 | 0.25 | 2026-11-06 | live as of 8 November 2026, 08:00:20 (HKT) |
| US30YT=X | United States 30-Year Treasury Yield | 5.26 | 0.17 | 2026-11-06 | live as of 8 November 2026, 08:00:20 (HKT) |
| HK50 | Hang Seng Futures | 24622.0 | 0.47 | 2026-11-06 | live as of 8 November 2026, 08:00:20 (HKT) |
| KOR200c1 | KOSPI 200 Futures | 782.95 | -6.49 | 2026-11-06 | live as of 8 November 2026, 08:00:20 (HKT) |
| CIHc1 | SSE 50 Futures | 2774.0 | -0.85 | 2026-11-06 | live as of 8 November 2026, 08:00:20 (HKT) |
| HYG | iShares iBoxx High Yield Corporate Bond ETF | 77.23 | -0.06 | 2026-11-06 | closed |
| LQD | iShares iBoxx Investment Grade Corporate Bond ETF | 104.53 | -0.12 | 2026-11-06 | closed |
| JNK | SPDR Bloomberg High Yield Bond ETF | 92.7 | -0.09 | 2026-11-06 | closed |
| RSP | Invesco S&P 500 Equal Weight ETF | 216.05 | -0.38 | 2026-11-06 | closed |
| IWF | iShares Russell 1000 Growth ETF | 111.75 | 1.26 | 2026-11-06 | closed |
| IWD | iShares Russell 1000 Value ETF | 257.45 | -0.36 | 2026-11-06 | closed |
| TLT | iShares 20+ Year Treasury Bond ETF | 81.92 | -0.01 | 2026-11-06 | closed |
| IEF | iShares 7-10 Year Treasury Bond ETF | 91.86 | -0.12 | 2026-11-06 | closed |
| SHY | iShares 1-3 Year Treasury Bond ETF | 81.63 | -0.05 | 2026-11-06 | closed |
| GC=F | Gold Future | 4079.5 | -0.45 | 2026-11-06 | closed |
| SI=F | Silver Future | 51.97 | 0.26 | 2026-11-06 | closed |
| CL=F | WTI Crude Oil Future | 90.34 | -0.94 | 2026-11-06 | closed |
| HG=F | Copper Future | 6.26 | 0.76 | 2026-11-06 | closed |

## Market Dispersion Analysis

- Sector ETF 20D dispersion: `25.31` points (very high); leader `XLV` (Health Care) `8.19`, laggard `XLK` (Technology) `-17.12`
- Sector ETF 60D dispersion: `23.4` points (very high); leader `XLV` (Health Care) `9.75`, laggard `XLK` (Technology) `-13.64`

| Comparison | Left | Right | 20D Spread | Signal |
| --- | --- | --- | --- | --- |
| Equal-weight vs cap-weight | RSP (Equal-weight S&P 500) | SPY (S&P 500) | 6.97 | broader participation |
| Small-cap vs large-cap | IWM (Russell 2000) | SPY (S&P 500) | 3.67 | small-cap leadership |
| Growth vs value | IWF (Russell 1000 Growth) | IWD (Russell 1000 Value) | -14.18 | value leadership |
| Nasdaq vs S&P 500 | QQQ (Nasdaq 100) | SPY (S&P 500) | -7.11 | S&P 500 leadership |

## Sector Constituent Dispersion

- Breadth 50D / 200D: percentage of active S&P 500 constituents in the sector trading above the 50-day / 200-day moving average.
- Positive 20D: percentage of active sector constituents with positive 20-day return.
- Std 20D: cross-sectional standard deviation of constituent 20-day returns; higher means wider stock-level dispersion.

| Sector | Count | Breadth 50D | Breadth 200D | Positive 20D | 20D Dispersion | Std 20D | Label | Leaders | Laggards |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Information Technology | 76 | 27.63 | 40.0 | 26.32 | 82.09 | 20.73 | very high | ROP, GEN, TYL | SNDK, MRVL, LITE |
| Communication Services | 22 | 47.62 | 25.0 | 54.55 | 81.74 | 15.99 | very high | APP, CMCSA, CHTR | GOOG, GOOGL, RDDT |
| Industrials | 83 | 57.83 | 45.57 | 60.24 | 70.75 | 14.72 | very high | EFX, PNR, SWK | CAT, BE, FIX |
| Financials | 76 | 60.0 | 68.06 | 78.95 | 63.59 | 9.99 | very high | FISV, ERIE, AON | FIS, COIN, HOOD |
| Health Care | 60 | 90.0 | 90.0 | 95.0 | 53.89 | 7.98 | very high | IDXX, GEHC, REGN | CVS, DXCM, ILMN |
| Utilities | 31 | 80.65 | 41.94 | 80.65 | 39.33 | 8.78 | very high | AWK, NEE, ED | CEG, NRG, VST |
| Materials | 24 | 70.83 | 62.5 | 79.17 | 38.68 | 8.33 | very high | MOS, PPG, CRH | IFF, STLD, FCX |
| Consumer Discretionary | 47 | 80.85 | 53.19 | 85.11 | 37.38 | 8.05 | very high | HAS, LOW, PHM | TSLA, DASH, APTV |
| Consumer Staples | 33 | 87.1 | 67.74 | 81.82 | 31.7 | 6.34 | very high | CLX, STZ, KDP | PM, BG, ADM |
| Energy | 21 | 0.0 | 42.86 | 14.29 | 26.53 | 7.14 | very high | SLB, COP, CVX | MPC, VLO, TPL |
| Real Estate | 30 | 68.97 | 41.38 | 83.33 | 25.2 | 5.91 | very high | EXR, PSA, KIM | PLD, DLR, IRM |

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
| US dollar/Euro ECB reference exchange rate | 1.12 | USD | -0.01 USD vs prior | 2026-11-06 | EUR weakened versus this currency. |
| Japanese yen/Euro ECB reference exchange rate | 176.77 | JPY | -1.08 JPY vs prior | 2026-11-06 | EUR weakened versus this currency. |
| Chinese yuan renminbi/Euro ECB reference exchange rate | 7.45 | CNY | -0.04 CNY vs prior | 2026-11-06 | EUR weakened versus this currency. |
| Australian dollar/Euro ECB reference exchange rate | 1.62 | AUD | 0.02 AUD vs prior | 2026-11-06 | EUR strengthened versus this currency. |

ABS Australia note: ABS rows are stored locally/Neon, but most series are dimension-coded; only curated series should be promoted into narrative report text.

## Sector and Theme Leadership

### Official Sector Strength

Supporting and detracting names are the top/bottom S&P 500 constituents by 20D return when constituent coverage is available; otherwise the report falls back to related ETFs.

| Rank | Sector | Score | Trend | Momentum | Stock Breadth | ETF Flow | Flow Reliability | 3M RS | Supporting / Leaders | Detracting / Laggards |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Consumer Staples | 69.59 | strong uptrend | positive | broad | 50.0 | 0.0 | 62.21 | CLX, STZ, KDP | PM, BG, ADM |
| 2 | Healthcare | 68.97 | strong uptrend | positive | broad | 66.2 | 65.0 | 64.34 | IDXX, GEHC, REGN | CVS, DXCM, ILMN |
| 3 | Financials | 67.02 | strong uptrend | neutral | broad | 51.68 | 65.0 | 57.43 | FISV, ERIE, AON | FIS, COIN, HOOD |
| 4 | Consumer Discretionary | 66.91 | strong uptrend | neutral | broad | 50.0 | 0.0 | 57.75 | HAS, LOW, PHM | TSLA, DASH, APTV |
| 5 | Real Estate | 65.51 | strong uptrend | neutral | broad | 42.31 | 65.0 | 57.98 | EXR, PSA, KIM | PLD, DLR, IRM |
| 6 | Utilities | 52.58 | downtrend | neutral | broad | 50.0 | 0.0 | 55.21 | AWK, NEE, ED | CEG, NRG, VST |
| 7 | Crypto | 49.97 | neutral | neutral | mixed | 49.7 | 65.0 | 50.0 |  |  |
| 8 | Energy | 48.1 | neutral | neutral | weak | 71.13 | 65.0 | 52.7 | SLB, COP, CVX | MPC, VLO, TPL |
| 9 | Defense | 39.91 | strong downtrend | negative | weak | 50.0 | 0.0 | 45.06 | XAR | XAR |
| 10 | Cybersecurity | 39.08 | downtrend | negative | weak | 51.27 | 65.0 | 40.82 | CIBR | CIBR |
| 11 | Industrials | 35.14 | strong downtrend | negative | weak | 50.0 | 0.0 | 48.22 | EFX, PNR, SWK | CAT, BE, FIX |
| 12 | Technology | 34.12 | strong downtrend | negative | weak | 69.51 | 65.0 | 41.78 | ROP, GEN, TYL | SNDK, MRVL, LITE |
| 13 | Grid Infrastructure | 32.25 | strong downtrend | negative | weak | 62.87 | 65.0 | 39.45 | GRID | GRID |
| 14 | Nuclear | 30.59 | strong downtrend | negative | weak | 50.0 | 0.0 | 36.72 | NLR | NLR |
| 15 | Semiconductors | 25.82 | strong downtrend | negative | weak | 73.06 | 90.0 | 16.58 | SMH, SOXX | SOXX, SMH |

### Thematic Strength

| Rank | Theme | Score | Setup | ETF Flow | Flow Reliability | Dispersion | Price | News |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Healthcare Innovation | 64.32 | Positive setup | 66.2 | 65.0 | 14.04 | True | False |
| 2 | Dividend Defensives | 61.17 | Positive setup | 56.95 | 65.0 | 4.04 | True | False |
| 3 | Energy | 48.69 | Neutral / watchlist | 71.13 | 65.0 | 5.61 | False | False |
| 4 | Financials | 45.22 | Neutral / watchlist | 51.68 | 65.0 | 13.46 | False | False |
| 5 | Quality Growth | 43.07 | Neutral / watchlist | 61.07 | 65.0 | 20.72 | False | False |
| 6 | Small Caps | 39.36 | Weak setup | 60.18 | 65.0 | 0.0 | False | False |
| 7 | AI Infrastructure | 39.32 | Weak setup | 73.06 | 90.0 | 74.76 | False | True |
| 8 | Grid Infrastructure | 39.21 | Weak setup | 62.87 | 65.0 | 27.53 | False | False |
| 9 | Defense | 38.76 | Weak setup | 50.0 | 0.0 | 29.04 | False | False |
| 10 | Cybersecurity | 37.25 | Weak setup | 51.27 | 65.0 | 23.55 | False | False |
| 11 | Crypto Infrastructure | 34.17 | Weak setup | 49.7 | 65.0 | 8.42 | False | False |
| 12 | Semiconductors | 32.78 | Weak setup | 73.06 | 90.0 | 58.42 | False | False |
| 13 | Nuclear | 29.23 | Underperformance risk | 50.0 | 0.0 | 12.14 | False | False |

- Top 5 improving themes: Crypto Infrastructure, Healthcare Innovation, Energy, Dividend Defensives, Quality Growth
- Top 5 deteriorating themes: Nuclear, Semiconductors, AI Infrastructure, Defense, Grid Infrastructure
- Strong news but weak price confirmation: AI Infrastructure
- Strong price but weak news confirmation: Healthcare Innovation, Dividend Defensives

### Sector / Theme Alignment

| Sector | Related Themes | Sector Score | Sector Signal | Theme Score | Theme Signal | Interpretation |
| --- | --- | --- | --- | --- | --- | --- |
| Consumer Staples | Dividend Defensives | 69.59 | strong | 61.17 | positive | sector and theme confirmation |
| Healthcare | Healthcare Innovation | 68.97 | strong | 64.32 | positive | sector and theme confirmation |
| Financials | Financials | 67.02 | strong | 45.22 | mixed | sector stronger than related themes |
| Consumer Discretionary | Small Caps | 66.91 | strong | 39.36 | weak | sector stronger than related themes |
| Real Estate | Dividend Defensives | 65.51 | strong | 61.17 | positive | sector and theme confirmation |
| Utilities | Grid Infrastructure, Nuclear, Dividend Defensives | 52.58 | mixed | 43.2 | weak | mixed confirmation |
| Crypto | Crypto Infrastructure | 49.97 | mixed | 34.17 | very weak | mixed confirmation |
| Energy | Energy | 48.1 | mixed | 48.69 | mixed | mixed confirmation |
| Defense | Defense | 39.91 | weak | 38.76 | weak | broad weakness across sector and themes |
| Cybersecurity | Cybersecurity | 39.08 | weak | 37.25 | weak | broad weakness across sector and themes |
| Industrials | Defense, Grid Infrastructure | 35.14 | weak | 38.98 | weak | broad weakness across sector and themes |
| Technology | AI Infrastructure, Semiconductors, Quality Growth | 34.12 | very weak | 38.39 | weak | broad weakness across sector and themes |
| Grid Infrastructure | Grid Infrastructure | 32.25 | very weak | 39.21 | weak | broad weakness across sector and themes |
| Nuclear | Nuclear | 30.59 | very weak | 29.23 | very weak | broad weakness across sector and themes |
| Semiconductors | AI Infrastructure, Semiconductors | 25.82 | very weak | 36.05 | weak | broad weakness across sector and themes |

## Three-Month Outperformance Setup

| Rank | Theme | Score | Classification | Drivers | Invalidation Triggers |
| --- | --- | --- | --- | --- | --- |
| 1 | Healthcare Innovation | 69.28 | Positive setup | relative_strength_20d, relative_strength_60d, trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 2 | Dividend Defensives | 65.35 | Positive setup | relative_strength_20d, trend_persistence, breadth, downside_volatility, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 3 | Energy | 53.85 | Neutral / watchlist | downside_volatility, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 4 | Quality Growth | 48.09 | Neutral / watchlist | volume_accumulation, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 5 | Financials | 46.77 | Neutral / watchlist | downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 6 | Grid Infrastructure | 40.93 | Weak setup | volume_accumulation | relative strength below SPY, breadth below 45%, news turns negative |
| 7 | Defense | 40.83 | Weak setup |  | relative strength below SPY, breadth below 45%, news turns negative |
| 8 | Cybersecurity | 39.69 | Weak setup |  | relative strength below SPY, breadth below 45%, news turns negative |
| 9 | Small Caps | 37.95 | Weak setup | downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 10 | AI Infrastructure | 36.48 | Weak setup | volume_accumulation | relative strength below SPY, breadth below 45%, news turns negative |
| 11 | Crypto Infrastructure | 35.62 | Weak setup | relative_strength_60d, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 12 | Semiconductors | 30.86 | Weak setup | volume_accumulation | relative strength below SPY, breadth below 45%, news turns negative |

## Breadth and Participation

- Above 50DMA: `33.33%`
- Above 200DMA: `41.67%`
- Positive 20D return: `33.33%`

## Volatility and Risk Signals

- VIX close=25.64 pct_chg=-9.01

## News Analytics

- Sentiment counts: {'positive': 21, 'negative': 33, 'neutral': 26}
- News confirmation score: `42.5`

### Top Market-Moving Headlines

**1. Russia pounds Kyiv as Ukraine strikes oil refinery ahead of peace talks**
- Source: Investing.com Economic Indicators
- Importance / impact: High / Negative
- Relevance / horizon: macro / short-term
- Affected assets: military conflict, geopolitical tension, energy markets
- Score: `58.34`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the short-term.

**2. Poland’s Domanski blames presidential vetoes as S&P cuts outlook to negative**
- Source: Investing.com Economic Indicators
- Importance / impact: Medium / Negative
- Relevance / horizon: sector_theme / short-term
- Affected assets: P, S, credit rating, outlook revision, political risk
- Score: `37.92`
- Investment implication: Theme or sector negative signal; requires price and volume confirmation before affecting rankings.

**3. Anthropic’s breakneck rise: What to know before the IPO**
- Source: CNBC Markets
- Importance / impact: Medium / Positive
- Relevance / horizon: sector_theme / 2027
- Affected assets: AAPL, MSFT, GOOGL, AMZN, CNBC
- Score: `36.03`
- Investment implication: Theme or sector positive signal; requires price and volume confirmation before affecting rankings.

**4. Berkshire shares surge as Wall Street swoons amid AI fears**
- Source: CNBC Markets
- Importance / impact: Low / Positive
- Relevance / horizon: sector_theme / short-term
- Affected assets: P, S, AI fears, market outperformance, Berkshire Hathaway
- Score: `33.63`
- Investment implication: Theme or sector positive signal; requires price and volume confirmation before affecting rankings.

**5. Russia pounds power facilities around Kyiv, damages major bridge**
- Source: CNBC Top News
- Importance / impact: Low / Negative
- Relevance / horizon: single_name / short-term
- Affected assets: U.S, conflict, military, energy
- Score: `33.46`
- Investment implication: Single-name negative signal; low weight unless it maps to a broader sector or theme.

**6. ASBISc Q3 2026 slides: AI infrastructure drives 135% revenue surge**
- Source: Investing.com Markets
- Importance / impact: Low / Positive
- Relevance / horizon: sector_theme / short-term
- Affected assets: AI infrastructure, revenue growth, Q3 2026
- Score: `32.24`
- Investment implication: Theme or sector positive signal; requires price and volume confirmation before affecting rankings.

**7. Risk of Iran war escalation remains high despite Democratic sweep in U.S. midterm elections**
- Source: CNBC Top News
- Importance / impact: Low / Negative
- Relevance / horizon: single_name / short-term
- Affected assets: U.S, geopolitical risk, Iran, U.S. midterm elections
- Score: `31.49`
- Investment implication: Single-name negative signal; low weight unless it maps to a broader sector or theme.

**8. MODIVO Platform Q3 2026 slides: gross margin tops 50%, EBITDA up 48%**
- Source: Investing.com Markets
- Importance / impact: Low / Positive
- Relevance / horizon: sector_theme / quarterly
- Affected assets: financial_results, profitability, platform_growth
- Score: `27.94`
- Investment implication: Theme or sector positive signal; requires price and volume confirmation before affecting rankings.

**9. Trump says U.S. carried out ‘minor strikes’ on Iran as missiles hit Qeshm Island**
- Source: CNBC Business Headlines
- Importance / impact: Low / Negative
- Relevance / horizon: single_name / short-term
- Affected assets: U.S, geopolitics, military conflict, energy markets
- Score: `26.52`
- Investment implication: Single-name negative signal; low weight unless it maps to a broader sector or theme.

**10. Emerging market central banks turn hawkish as inflation pressures mount, Citi says**
- Source: Investing.com Economic Indicators
- Importance / impact: Low / Negative
- Relevance / horizon: sector_theme / short-term
- Affected assets: central bank policy, inflation, monetary tightening
- Score: `25.44`
- Investment implication: Theme or sector negative signal; requires price and volume confirmation before affecting rankings.


### Headline Quality Checks

Noisy headline list: The S&P 500 could be dangerously exposed to AI. He

## Positioning & Flow Dashboard

Positioning and flow data is used as confirmation only.

### Deferred Flow Sections

- Official ETF / fund flows: current report uses shares-outstanding-derived net fund flow estimates from free ETF metadata.
- Institutional Ownership: not available until SEC 13F ingestion is implemented.
- Grouped exposure flow reliability: use issuer coverage and availability status before treating ETF flow as confirmation.

## ETF Flows Analysis

- Market flow regime: `Selective Risk-On`
- Market flow score: `56.8 / 100`
- Equity risk flow: `50.1`
- Credit risk flow: `56.2`
- Sector cyclicality flow: `75.0`
- Duration/liquidity flow: `44.1`
- Alternatives: `mixed alternative-asset demand`
- ETF flow reliability: `66.6 / 100`
- Dominant allocation direction: `mixed allocation`

### Core Flow Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVV | U.S. Broad Equity | 0.1 | -0.7 | 0.6 | 0.0 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Medium-term recovery | 87.0 |
| ACWI | Global Equity | -0.6 | -0.7 | 0.0 | 1.2 | Down | Neutral | High | Heavy Selling Pressure | Cautious | Mixed or neutral flow structure; Persistent selling | 77.0 |
| EFA | Developed Markets ex-U.S. | -0.2 | 0.6 | 0.0 | 1.1 | Down | Neutral | High | Heavy Selling Pressure | Cautious | Mixed or neutral flow structure; Persistent selling | 77.0 |
| IEMG | Emerging Markets | -0.4 | -0.5 | 0.0 | 1.2 | Down | Neutral | High | Heavy Selling Pressure | Cautious | Mixed or neutral flow structure; Persistent selling | 77.0 |
| IJH | U.S. Mid Cap | -0.6 | 0.2 | 0.6 | 1.2 | Down | Neutral | High | Heavy Selling Pressure | Cautious | Structural accumulation | 91.0 |
| IWM | U.S. Small Cap | -0.1 | 2.0 | 0.6 | 0.4 | Down | Buy | Normal | Contrarian Buying | Watch | Medium-term deterioration | 83.0 |
| LQD | Investment-Grade Credit | 1.3 | -0.2 | 0.7 | -0.5 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural accumulation | 91.0 |
| HYG | High-Yield Credit | 0.3 | 0.7 | 0.6 | -0.7 | Flat | Neutral | Normal | Neutral | Neutral | Structural accumulation | 91.0 |
| SGOV | Treasury Bills / Cash | -1.8 | -1.5 | 0.8 | 0.6 | Flat | Sell | Normal | Quiet Distribution | Weakening | Strong confirmation; Strong sponsorship | 100.0 |
| SHY | Short-Duration Treasuries | 0.3 | 1.7 | 0.8 | 1.6 | Flat | Neutral | High | High-Turnover Consolidation | Transition | Structural accumulation; Strong sponsorship | 99.0 |
| IEF | Intermediate-Duration Treasuries | 1.6 | 1.2 | 0.6 | -0.3 | Up | Buy | Normal | Steady Accumulation | Risk-On | Strong confirmation | 95.0 |
| TLT | Long-Duration Treasuries | -1.1 | 0.2 | 0.5 | -0.0 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Medium-term deterioration | 83.0 |
| GLD | Gold | -0.5 | 0.7 | 0.4 | -0.5 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Medium-term deterioration | 83.0 |
| IBIT | Bitcoin | -0.3 | 1.1 | 0.5 | -0.2 | Down | Sell | Normal | Persistent Distribution | Risk-Off | Medium-term deterioration; Exceptional institutional selling | 75.0 |

### Sector Flow Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| XLC | Communication Services | -0.8 | 1.5 | 0.5 | 3.0 | Down | Sell | High | Confirmed Distribution | Strong Risk-Off | Medium-term deterioration; Exceptional institutional selling | 75.0 |
| XLY | Consumer Discretionary | -0.1 | -0.7 | 0.5 | 4.3 | Up | Buy | High | Confirmed Accumulation | Strong Risk-On | Tactical rebound inside structural distribution; Exceptional institutional buying | 91.0 |
| XLP | Consumer Staples | 0.1 | -0.7 | 0.5 | 4.1 | Up | Neutral | High | Momentum Rally | Watch | Structural distribution | 79.0 |
| XLE | Energy | 0.3 | -0.1 | 0.6 | 3.6 | Down | Neutral | High | Heavy Selling Pressure | Cautious | Medium-term recovery | 87.0 |
| XLF | Financials | 0.7 | -1.4 | 0.4 | 3.3 | Up | Buy | High | Confirmed Accumulation | Strong Risk-On | Medium-term recovery | 87.0 |
| XLV | Health Care | 2.9 | 2.2 | 0.7 | 4.4 | Up | Buy | High | Confirmed Accumulation | Strong Risk-On | Strong confirmation; Exceptional institutional buying | 100.0 |
| XLI | Industrials | -0.2 | -1.6 | 0.5 | 4.8 | Down | Neutral | High | Heavy Selling Pressure | Cautious | Medium-term recovery | 87.0 |
| XLK | Information Technology | 0.2 | 0.2 | 0.6 | 5.7 | Down | Neutral | High | Heavy Selling Pressure | Cautious | Structural accumulation | 91.0 |
| XLB | Materials | -0.2 | -1.4 | 0.6 | 3.2 | Up | Buy | High | Confirmed Accumulation | Strong Risk-On | Medium-term recovery | 87.0 |
| XLRE | Real Estate | 0.3 | -1.1 | 0.5 | 2.6 | Up | Neutral | High | Momentum Rally | Watch | Medium-term recovery | 87.0 |
| XLU | Utilities | -1.7 | 0.9 | 0.3 | 1.7 | Up | Neutral | High | Momentum Rally | Watch | Medium-term deterioration | 83.0 |

### Subsector PFV Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ITA | Aerospace and Defense | 8.6 | 7.9 | 0.3 | 2.8 | Down | Buy | High | Aggressive Dip Buying | Recovery Candidate | Strong confirmation; Exceptional institutional buying | 100.0 |
| SOXX | Semiconductors | 6.6 | 4.3 | 0.8 | 4.7 | Down | Buy | High | Aggressive Dip Buying | Recovery Candidate | Strong confirmation; Exceptional institutional buying, Strong sponsorship | 100.0 |
| SMH | Semiconductors | 1.7 | 0.6 | 0.6 | 2.0 | Down | Buy | High | Aggressive Dip Buying | Recovery Candidate | Strong confirmation | 95.0 |
| CIBR | Cybersecurity | -0.7 | 1.1 | 0.6 | 0.4 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Medium-term deterioration | 83.0 |

### Material Flow Divergences

| Severity | Type | Primary | Comparison | Interpretation |
| --- | --- | --- | --- | --- |
| high | close_substitute_divergence | AGG | IUSB | primary representative differs from close substitute |
| high | close_substitute_divergence | IWF | IVW | primary representative differs from close substitute |
| high | close_substitute_divergence | SOXX | SMH | primary representative differs from close substitute |
| high | close_substitute_divergence | IWM | IJR | primary representative differs from close substitute |


## Contradiction / Audit Flags

| Severity | Section | Issue | Deterministic Fix |
| --- | --- | --- | --- |
| low | Theme Strength Ranking | AI Infrastructure has strong news confirmation but weak price confirmation. | Classify as unconfirmed narrative. |

## Data Quality Notes

- Technical rows loaded: `60`
- S&P 500 constituent technical rows loaded: `503`
- Macro rows loaded: `48`
- Live macro rows used: `12`
- Economic rows loaded: `113`
- News rows loaded: `80`
- Positioning/flow rows loaded: `30`

## Cycle Metadata

- Report generated at: 08 November 2026, 08:18:55 (HKT)

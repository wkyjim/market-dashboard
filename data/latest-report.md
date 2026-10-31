# Rule-Based Institutional Market Update

Generated at: 1 November 2026, 02:17:53 (HKT)
Window: 24h

## Executive Dashboard

- Regime score: **44.45 / 100** (Mild Risk-Off)
- US equity strength: **42.22 / 100** (weak)
- Evidence quality: **76.0 / 100**
- ETF flow contribution: **48.84 / 100**, reliability **66.57 / 100**
- Breadth: **narrow**; above 50DMA `40.0%`, above 200DMA `53.33%`
- Top sector score: **Healthcare** `71.29`
- Top theme score: **Energy** `69.6`

## Market Regime Score

| Metric | Value | Driver / Interpretation |
| --- | --- | --- |
| Overall regime | 44.45 | Mild Risk-Off |
| equity_trend | 40.0 | mild risk-off pressure; Core equity ETFs versus moving averages. |
| equity_momentum | 45.36 | neutral / mixed; 5D/20D/60D return momentum across SPY, QQQ, IWM, and SMH. |
| market_breadth | 45.0 | mild risk-off pressure; Participation breadth from tracked equity/ETF rows. |
| volatility | 20.0 | risk-off pressure; VIX level and change; higher score means calmer volatility conditions. |
| rates_yield_curve | 58.0 | mild risk-on support; Treasury yield pressure and curve shape; higher score means less rates pressure. |
| credit_proxy | 50.0 | neutral / mixed; Credit-market proxy; currently neutral when no direct spread signal is available. |
| dollar_fx | 54.46 | neutral / mixed; Dollar move; higher score means less USD tightening pressure. |
| commodity_confirmation | 46.0 | neutral / mixed; Copper, silver, oil, and gold mix; higher score means better cyclical confirmation. |
| etf_flow | 49.23 | neutral / mixed; Grouped ETF flow contribution adjusted for reliability. |
| news_confirmation | 40.62 | mild risk-off pressure; Weighted headline/news confirmation score. |
| Positive contributors |  | none |
| Negative contributors |  | volatility=20.0, equity_trend=40.0, news_confirmation=40.62, market_breadth=45.0 |

## US Equity Strength Score

| Component | Score |
| --- | --- |
| indices_above_moving_averages | 40.0 |
| sp500_trend | 35.0 |
| nasdaq_trend | 35.0 |
| russell_participation | 55.0 |
| returns_momentum | 45.36 |
| rsi_zone | 45.0 |
| macd_confirmation | 43.75 |
| volume_confirmation | 38.75 |
| breadth | 45.0 |

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
| Credit | HYG stable | High-yield weakness would challenge equity risk-on confirmation. |
| Gold | Gold falling | Gold strength can indicate defensive demand, inflation hedging, or geopolitical concern. |
| Silver | Silver falling | Silver helps distinguish precious-metal demand from industrial/cyclical confirmation when data is available. |
| Copper | Copper falling | Copper strength supports cyclical growth confirmation; weakness would dilute risk-on breadth. |
| Oil | WTI crude stable | Oil spikes can be inflationary risk; falling oil can ease cost pressure but may also flag demand softness. |
| Volatility | VIX rising | Falling VIX supports risk appetite; a volatility spike would reduce confidence in broad risk-on. |

### Macro Snapshot

Live macro rows are intraday snapshots from `public.macro_live`; closed rows are official stored rows from `public.macro`.

| Symbol | Name | Close | Pct Chg | Market Date | Status |
| --- | --- | --- | --- | --- | --- |
| ^GSPC | S&P 500 | 7580.07 | -1.82 | 2026-10-30 | closed |
| ^IXIC | NASDAQ Composite | 25437.0 | -2.86 | 2026-10-30 | closed |
| ^RUT | Russell 2000 Index | 2811.84 | -1.66 | 2026-10-30 | closed |
| ^VIX | CBOE Volatility Index | 19.42 | 12.91 | 2026-10-30 | closed |
| ^SKEW | CBOE SKEW Index | 149.76 | -0.84 | 2026-10-30 | closed |
| ^MOVE | ICE BofA MOVE Index | 100.2 | 7.12 | 2026-10-30 | closed |
| US2YT=X | United States 2-Year Treasury Yield | 4.58 | -1.61 | 2026-10-30 | live as of 1 November 2026, 02:00:21 (HKT) |
| US3YT=X | United States 3-Year Treasury Yield | 4.65 | -1.67 | 2026-10-30 | live as of 1 November 2026, 02:00:21 (HKT) |
| US5YT=X | United States 5-Year Treasury Yield | 4.72 | -1.67 | 2026-10-30 | live as of 1 November 2026, 02:00:21 (HKT) |
| US7YT=X | United States 7-Year Treasury Yield | 4.82 | -1.43 | 2026-10-30 | live as of 1 November 2026, 02:00:21 (HKT) |
| US10YT=X | United States 10-Year Treasury Yield | 4.93 | -1.2 | 2026-10-30 | live as of 1 November 2026, 02:00:21 (HKT) |
| US20YT=X | United States 20-Year Treasury Yield | 5.34 | -0.54 | 2026-10-30 | live as of 1 November 2026, 02:00:21 (HKT) |
| US30YT=X | United States 30-Year Treasury Yield | 5.31 | -0.38 | 2026-10-30 | live as of 1 November 2026, 02:00:21 (HKT) |
| HK50 | Hang Seng Futures | 23346.0 | 1.03 | 2026-10-30 | live as of 1 November 2026, 02:00:21 (HKT) |
| KOR200c1 | KOSPI 200 Futures | 873.1 | -2.93 | 2026-10-30 | live as of 1 November 2026, 02:00:21 (HKT) |
| CIHc1 | SSE 50 Futures | 2727.6 | -0.41 | 2026-10-30 | live as of 1 November 2026, 02:00:21 (HKT) |
| HYG | iShares iBoxx High Yield Corporate Bond ETF | 77.43 | -0.19 | 2026-10-30 | closed |
| LQD | iShares iBoxx Investment Grade Corporate Bond ETF | 104.27 | 0.05 | 2026-10-30 | closed |
| JNK | SPDR Bloomberg High Yield Bond ETF | 92.98 | -0.23 | 2026-10-30 | closed |
| RSP | Invesco S&P 500 Equal Weight ETF | 218.31 | -0.79 | 2026-10-30 | closed |
| IWF | iShares Russell 1000 Growth ETF | 117.61 | -2.89 | 2026-10-30 | closed |
| IWD | iShares Russell 1000 Value ETF | 258.65 | -0.81 | 2026-10-30 | closed |
| TLT | iShares 20+ Year Treasury Bond ETF | 81.84 | 0.43 | 2026-10-30 | closed |
| IEF | iShares 7-10 Year Treasury Bond ETF | 91.76 | 0.56 | 2026-10-30 | closed |
| SHY | iShares 1-3 Year Treasury Bond ETF | 81.7 | 0.15 | 2026-10-30 | closed |
| GC=F | Gold Future | 3884.9 | -3.8 | 2026-10-30 | closed |
| SI=F | Silver Future | 49.13 | -5.77 | 2026-10-30 | closed |
| CL=F | WTI Crude Oil Future | 102.95 | 0.09 | 2026-10-30 | closed |
| HG=F | Copper Future | 6.51 | -1.03 | 2026-10-30 | closed |

## Market Dispersion Analysis

- Sector ETF 20D dispersion: `21.62` points (very high); leader `XLE` (Energy) `11.46`, laggard `XLK` (Technology) `-10.16`
- Sector ETF 60D dispersion: `30.54` points (very high); leader `XLE` (Energy) `20.39`, laggard `XLC` (Communication Services) `-10.15`

| Comparison | Left | Right | 20D Spread | Signal |
| --- | --- | --- | --- | --- |
| Equal-weight vs cap-weight | RSP (Equal-weight S&P 500) | SPY (S&P 500) | 5.9 | broader participation |
| Small-cap vs large-cap | IWM (Russell 2000) | SPY (S&P 500) | 1.03 | small-cap leadership |
| Growth vs value | IWF (Russell 1000 Growth) | IWD (Russell 1000 Value) | -11.16 | value leadership |
| Nasdaq vs S&P 500 | QQQ (Nasdaq 100) | SPY (S&P 500) | -6.07 | S&P 500 leadership |

## Sector Constituent Dispersion

- Breadth 50D / 200D: percentage of active S&P 500 constituents in the sector trading above the 50-day / 200-day moving average.
- Positive 20D: percentage of active sector constituents with positive 20-day return.
- Std 20D: cross-sectional standard deviation of constituent 20-day returns; higher means wider stock-level dispersion.

| Sector | Count | Breadth 50D | Breadth 200D | Positive 20D | 20D Dispersion | Std 20D | Label | Leaders | Laggards |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Information Technology | 75 | 38.67 | 59.46 | 32.0 | 80.66 | 17.98 | very high | PTC, GEN, ROP | COHR, TER, INTC |
| Industrials | 83 | 60.24 | 48.1 | 57.83 | 61.59 | 12.51 | very high | EFX, LMT, PNR | CAT, FIX, BE |
| Real Estate | 30 | 44.83 | 37.93 | 80.0 | 48.62 | 8.3 | very high | CCI, SBAC, AMT | ESS, DOC, ARE |
| Financials | 76 | 57.33 | 61.11 | 75.0 | 48.51 | 9.52 | very high | FDS, CBOE, GPN | IBKR, COIN, HOOD |
| Communication Services | 22 | 19.05 | 35.0 | 50.0 | 47.55 | 11.1 | very high | OMC, DIS, CMCSA | GOOG, GOOGL, RDDT |
| Consumer Discretionary | 47 | 61.7 | 44.68 | 76.6 | 39.85 | 7.59 | very high | HAS, ULTA, HD | GPC, DASH, BKNG |
| Health Care | 60 | 75.0 | 85.0 | 91.67 | 39.78 | 7.05 | very high | REGN, LLY, CRL | DXCM, SOLV, ILMN |
| Materials | 24 | 75.0 | 62.5 | 83.33 | 37.35 | 9.94 | very high | DOW, BALL, LYB | MOS, ALB, FCX |
| Consumer Staples | 34 | 78.12 | 65.62 | 85.29 | 29.34 | 6.65 | very high | STZ, DLTR, EL | TGT, ADM, BG |
| Energy | 21 | 85.71 | 80.95 | 85.71 | 24.02 | 6.42 | very high | COP, APA, EOG | BKR, VLO, TPL |
| Utilities | 31 | 83.87 | 51.61 | 93.55 | 15.43 | 3.82 | high | WEC, EXC, NI | NRG, AES, VST |

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
| US dollar/Euro ECB reference exchange rate | 1.12 | USD | 0.0 USD vs prior | 2026-10-30 | EUR strengthened versus this currency. |
| Japanese yen/Euro ECB reference exchange rate | 175.68 | JPY | -0.24 JPY vs prior | 2026-10-30 | EUR weakened versus this currency. |
| Chinese yuan renminbi/Euro ECB reference exchange rate | 7.43 | CNY | 0.02 CNY vs prior | 2026-10-30 | EUR strengthened versus this currency. |
| Australian dollar/Euro ECB reference exchange rate | 1.59 | AUD | 0.01 AUD vs prior | 2026-10-30 | EUR strengthened versus this currency. |

ABS Australia note: ABS rows are stored locally/Neon, but most series are dimension-coded; only curated series should be promoted into narrative report text.

## Sector and Theme Leadership

### Official Sector Strength

Supporting and detracting names are the top/bottom S&P 500 constituents by 20D return when constituent coverage is available; otherwise the report falls back to related ETFs.

| Rank | Sector | Score | Trend | Momentum | Stock Breadth | ETF Flow | Flow Reliability | 3M RS | Supporting / Leaders | Detracting / Laggards |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Healthcare | 71.29 | strong uptrend | positive | broad | 64.42 | 65.0 | 63.47 | REGN, LLY, CRL | DXCM, SOLV, ILMN |
| 2 | Energy | 70.73 | strong uptrend | positive | broad | 61.46 | 65.0 | 66.79 | COP, APA, EOG | BKR, VLO, TPL |
| 3 | Consumer Staples | 68.89 | strong uptrend | positive | broad | 50.0 | 0.0 | 60.4 | STZ, DLTR, EL | TGT, ADM, BG |
| 4 | Financials | 65.59 | strong uptrend | neutral | broad | 40.77 | 65.0 | 54.24 | FDS, CBOE, GPN | IBKR, COIN, HOOD |
| 5 | Consumer Discretionary | 61.18 | uptrend | neutral | broad | 50.0 | 0.0 | 53.74 | HAS, ULTA, HD | GPC, DASH, BKNG |
| 6 | Utilities | 58.83 | neutral | neutral | broad | 50.0 | 0.0 | 56.99 | WEC, EXC, NI | NRG, AES, VST |
| 7 | Real Estate | 56.11 | neutral | neutral | broad | 47.04 | 65.0 | 53.76 | CCI, SBAC, AMT | ESS, DOC, ARE |
| 8 | Crypto | 50.89 | neutral | neutral | mixed | 58.92 | 65.0 | 50.0 |  |  |
| 9 | Cybersecurity | 48.51 | neutral | neutral | weak | 69.45 | 65.0 | 51.58 | CIBR | CIBR |
| 10 | Defense | 43.14 | strong downtrend | negative | weak | 50.0 | 0.0 | 42.43 | XAR | XAR |
| 11 | Industrials | 39.34 | strong downtrend | neutral | weak | 50.0 | 0.0 | 47.09 | EFX, LMT, PNR | CAT, FIX, BE |
| 12 | Technology | 39.06 | downtrend | negative | weak | 48.57 | 65.0 | 45.04 | PTC, GEN, ROP | COHR, TER, INTC |
| 13 | Nuclear | 34.7 | strong downtrend | negative | weak | 50.0 | 0.0 | 37.56 | NLR | NLR |
| 14 | Semiconductors | 34.58 | strong downtrend | negative | weak | 60.92 | 90.0 | 36.62 | SMH, SOXX | SOXX, SMH |
| 15 | Grid Infrastructure | 33.97 | strong downtrend | negative | weak | 60.65 | 65.0 | 41.17 | GRID | GRID |

### Thematic Strength

| Rank | Theme | Score | Setup | ETF Flow | Flow Reliability | Dispersion | Price | News |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Energy | 69.6 | Positive setup | 61.46 | 65.0 | 2.71 | True | False |
| 2 | Healthcare Innovation | 67.6 | Positive setup | 64.42 | 65.0 | 20.42 | True | False |
| 3 | Dividend Defensives | 62.76 | Positive setup | 55.03 | 65.0 | 2.21 | True | False |
| 4 | Cybersecurity | 53.36 | Neutral / watchlist | 69.45 | 65.0 | 45.77 | False | False |
| 5 | Defense | 50.38 | Neutral / watchlist | 50.0 | 0.0 | 36.47 | False | False |
| 6 | Quality Growth | 48.1 | Neutral / watchlist | 49.03 | 65.0 | 21.81 | False | False |
| 7 | Small Caps | 47.74 | Neutral / watchlist | 44.17 | 65.0 | 0.0 | False | False |
| 8 | Financials | 44.63 | Neutral / watchlist | 40.77 | 65.0 | 12.6 | False | False |
| 9 | AI Infrastructure | 43.35 | Neutral / watchlist | 60.92 | 90.0 | 20.78 | False | False |
| 10 | Semiconductors | 41.69 | Weak setup | 60.92 | 90.0 | 12.18 | False | False |
| 11 | Grid Infrastructure | 40.43 | Weak setup | 60.65 | 65.0 | 24.2 | False | False |
| 12 | Crypto Infrastructure | 38.43 | Weak setup | 58.92 | 65.0 | 3.13 | False | False |
| 13 | Nuclear | 31.87 | Underperformance risk | 50.0 | 0.0 | 16.13 | False | False |

- Top 5 improving themes: Energy, Crypto Infrastructure, Healthcare Innovation, Cybersecurity, Dividend Defensives
- Top 5 deteriorating themes: Nuclear, Financials, Defense, Semiconductors, AI Infrastructure
- Strong news but weak price confirmation: none
- Strong price but weak news confirmation: Energy, Healthcare Innovation, Dividend Defensives

### Sector / Theme Alignment

| Sector | Related Themes | Sector Score | Sector Signal | Theme Score | Theme Signal | Interpretation |
| --- | --- | --- | --- | --- | --- | --- |
| Healthcare | Healthcare Innovation | 71.29 | strong | 67.6 | strong | sector and theme confirmation |
| Energy | Energy | 70.73 | strong | 69.6 | strong | sector and theme confirmation |
| Consumer Staples | Dividend Defensives | 68.89 | strong | 62.76 | positive | sector and theme confirmation |
| Financials | Financials | 65.59 | strong | 44.63 | weak | sector stronger than related themes |
| Consumer Discretionary | Small Caps | 61.18 | positive | 47.74 | mixed | sector stronger than related themes |
| Utilities | Grid Infrastructure, Nuclear, Dividend Defensives | 58.83 | positive | 45.02 | mixed | sector stronger than related themes |
| Real Estate | Dividend Defensives | 56.11 | positive | 62.76 | positive | sector and theme confirmation |
| Crypto | Crypto Infrastructure | 50.89 | mixed | 38.43 | weak | mixed confirmation |
| Cybersecurity | Cybersecurity | 48.51 | mixed | 53.36 | mixed | mixed confirmation |
| Defense | Defense | 43.14 | weak | 50.38 | mixed | mixed confirmation |
| Industrials | Defense, Grid Infrastructure | 39.34 | weak | 45.4 | mixed | mixed confirmation |
| Technology | AI Infrastructure, Semiconductors, Quality Growth | 39.06 | weak | 44.38 | weak | broad weakness across sector and themes |
| Nuclear | Nuclear | 34.7 | very weak | 31.87 | very weak | broad weakness across sector and themes |
| Semiconductors | AI Infrastructure, Semiconductors | 34.58 | very weak | 42.52 | weak | broad weakness across sector and themes |
| Grid Infrastructure | Grid Infrastructure | 33.97 | very weak | 40.43 | weak | broad weakness across sector and themes |

## Three-Month Outperformance Setup

| Rank | Theme | Score | Classification | Drivers | Invalidation Triggers |
| --- | --- | --- | --- | --- | --- |
| 1 | Energy | 74.44 | Positive setup | relative_strength_20d, relative_strength_60d, trend_persistence, breadth, volume_accumulation | relative strength below SPY, breadth below 45%, news turns negative |
| 2 | Healthcare Innovation | 71.87 | Positive setup | relative_strength_20d, relative_strength_60d, trend_persistence, breadth, volume_accumulation | relative strength below SPY, breadth below 45%, news turns negative |
| 3 | Dividend Defensives | 67.05 | Positive setup | relative_strength_20d, trend_persistence, breadth, volume_accumulation, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 4 | Quality Growth | 55.61 | Neutral / watchlist | trend_persistence, breadth, volume_accumulation, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 5 | Cybersecurity | 55.41 | Neutral / watchlist | relative_strength_60d, trend_persistence, breadth, volume_accumulation, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 6 | Defense | 50.81 | Neutral / watchlist | downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 7 | Small Caps | 50.38 | Neutral / watchlist | downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 8 | AI Infrastructure | 47.42 | Neutral / watchlist | volume_accumulation, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 9 | Financials | 46.73 | Neutral / watchlist | downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 10 | Grid Infrastructure | 41.86 | Weak setup | downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 11 | Semiconductors | 41.6 | Weak setup | volume_accumulation | relative strength below SPY, breadth below 45%, news turns negative |
| 12 | Crypto Infrastructure | 39.64 | Weak setup | relative_strength_60d, volume_accumulation, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |

## Breadth and Participation

- Above 50DMA: `40.0%`
- Above 200DMA: `53.33%`
- Positive 20D return: `41.67%`

## Volatility and Risk Signals

- VIX close=19.42 pct_chg=12.91

## News Analytics

- Sentiment counts: {'positive': 15, 'negative': 30, 'neutral': 35}
- News confirmation score: `40.62`

### Top Market-Moving Headlines

**1. AMD’s stock slides after Intel earnings reveal two big issues**
- Source: MarketWatch Top Stories
- Importance / impact: Medium / Negative
- Relevance / horizon: sector_theme / short-term
- Affected assets: AMD, PC, AI, PC market, Intel earnings
- Score: `44.22`
- Investment implication: Theme or sector negative signal; requires price and volume confirmation before affecting rankings.

**2. Intel stock has worst day since 1970s, wiping about $12 billion off government's stake**
- Source: CNBC Top News
- Importance / impact: Medium / Negative
- Relevance / horizon: sector_theme / short-term
- Affected assets: AMZN, INTC, AI spending, earnings pressure, market volatility
- Score: `41.18`
- Investment implication: Theme or sector negative signal; requires price and volume confirmation before affecting rankings.

**3. The tech selloff shifts into overdrive as weak earnings bring a reality check**
- Source: MarketWatch Bulletins
- Importance / impact: Low / Negative
- Relevance / horizon: sector_theme / short-term
- Affected assets: tech selloff, earnings miss, market correction
- Score: `31.23`
- Investment implication: Theme or sector negative signal; requires price and volume confirmation before affecting rankings.

**4. Nasdaq logs worst month since March 2025 as weak tech earnings rattle investors**
- Source: MarketWatch Bulletins
- Importance / impact: Low / Negative
- Relevance / horizon: single_name / short-term
- Affected assets: NASDAQ, equity-market-decline, tech-sector-weakness, earnings-report
- Score: `27.29`
- Investment implication: Single-name negative signal; low weight unless it maps to a broader sector or theme.

**5. Fed officials are already saying they’ll need to get back to hiking rates**
- Source: CNBC Markets
- Importance / impact: Low / Mixed
- Relevance / horizon: macro / short-term
- Affected assets: Federal Reserve, monetary policy, interest rates
- Score: `21.8`
- Investment implication: Macro-relevant mixed signal; use as context for rates, volatility, and index confirmation over the short-term.

**6. Stock market rocked as investors dump tech shares; Nasdaq suffers worst day since June: Live updates**
- Source: CNBC Top News
- Importance / impact: Low / Negative
- Relevance / horizon: sector_theme / short-term
- Affected assets: AMZN, INTC, earnings, stock decline, technology
- Score: `21.62`
- Investment implication: Theme or sector negative signal; requires price and volume confirmation before affecting rankings.

**7. The S&P 500 isn’t the big winner you may think it is**
- Source: MarketWatch Top Stories
- Importance / impact: Low / Mixed
- Relevance / horizon: sector_theme / nan
- Affected assets: P, S
- Score: `21.25`
- Investment implication: Theme or sector mixed signal; requires price and volume confirmation before affecting rankings.

**8. Oil hits six-month highs as Hormuz attacks threaten Iran peace efforts**
- Source: Investing.com Economic Indicators
- Importance / impact: Low / Negative
- Relevance / horizon: macro / short-term
- Affected assets: CL=F, BZ=F, IRAN, geopolitical risk, energy markets
- Score: `19.45`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the short-term.

**9. Grand Theft Callout: ‘GTA 6’ fans are missing work on the game’s release day because they ‘don’t want to wait’ anymore**
- Source: MarketWatch Top Stories
- Importance / impact: Low / Mixed
- Relevance / horizon: sector_theme / nan
- Affected assets: GTA, VI
- Score: `18.06`
- Investment implication: Theme or sector mixed signal; requires price and volume confirmation before affecting rankings.

**10. This cybersecurity stock will be the next to join the S&P 500**
- Source: MarketWatch Top Stories
- Importance / impact: Low / Mixed
- Relevance / horizon: sector_theme / nan
- Affected assets: P, S
- Score: `18.06`
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
- Market flow score: `49.1 / 100`
- Equity risk flow: `45.5`
- Credit risk flow: `53.2`
- Sector cyclicality flow: `51.1`
- Duration/liquidity flow: `46.0`
- Alternatives: `mixed alternative-asset demand`
- ETF flow reliability: `66.6 / 100`
- Dominant allocation direction: `defensive demand`

### Core Flow Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVV | U.S. Broad Equity | -0.2 | -1.0 | 0.4 | -0.2 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural distribution | 79.0 |
| ACWI | Global Equity | -0.6 | -0.7 | 0.0 | 0.5 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Mixed or neutral flow structure; Persistent selling | 77.0 |
| EFA | Developed Markets ex-U.S. | 0.9 | 0.6 | 0.1 | 2.1 | Flat | Neutral | High | High-Turnover Consolidation | Transition | Structural accumulation; Persistent selling | 83.0 |
| IEMG | Emerging Markets | -0.5 | -0.3 | 0.0 | 1.6 | Down | Neutral | High | Heavy Selling Pressure | Cautious | Mixed or neutral flow structure; Persistent selling | 77.0 |
| IJH | U.S. Mid Cap | -1.0 | 0.2 | 0.5 | 0.4 | Flat | Neutral | Normal | Neutral | Neutral | Medium-term deterioration | 83.0 |
| IWM | U.S. Small Cap | -1.4 | 0.7 | 0.6 | 0.3 | Flat | Neutral | Normal | Neutral | Neutral | Structural distribution | 79.0 |
| LQD | Investment-Grade Credit | 1.7 | -0.3 | 0.7 | 0.9 | Up | Buy | Normal | Steady Accumulation | Risk-On | Medium-term recovery; Exceptional institutional buying | 95.0 |
| HYG | High-Yield Credit | -0.2 | 0.3 | 0.6 | 0.6 | Flat | Buy | Normal | Quiet Accumulation | Improving | Medium-term deterioration | 83.0 |
| SGOV | Treasury Bills / Cash | -1.1 | -0.7 | 0.8 | 2.8 | Flat | Sell | High | Distribution Before Breakdown | Early Bearish | Medium-term deterioration; Strong sponsorship | 91.0 |
| SHY | Short-Duration Treasuries | 0.5 | 1.6 | 0.7 | 0.3 | Flat | Neutral | Normal | Neutral | Neutral | Structural accumulation | 91.0 |
| IEF | Intermediate-Duration Treasuries | 0.7 | -0.7 | 0.5 | 1.7 | Up | Buy | High | Confirmed Accumulation | Strong Risk-On | Medium-term recovery | 87.0 |
| TLT | Long-Duration Treasuries | -1.2 | 1.1 | 0.6 | 0.1 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Medium-term deterioration | 83.0 |
| GLD | Gold | -0.6 | 1.0 | 0.5 | 1.7 | Down | Neutral | High | Heavy Selling Pressure | Cautious | Medium-term deterioration | 83.0 |
| IBIT | Bitcoin | 0.2 | 1.5 | 0.7 | 2.8 | Down | Neutral | High | Heavy Selling Pressure | Cautious | Structural accumulation | 91.0 |

### Sector Flow Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| XLC | Communication Services | 1.6 | 2.9 | 0.6 | 2.6 | Down | Buy | High | Aggressive Dip Buying | Recovery Candidate | Strong confirmation; Exceptional institutional buying | 100.0 |
| XLY | Consumer Discretionary | -0.2 | -1.1 | 0.5 | 0.1 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural distribution | 79.0 |
| XLP | Consumer Staples | 1.0 | 0.4 | 0.6 | 1.0 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Medium-term recovery | 87.0 |
| XLE | Energy | 0.8 | 0.1 | 0.7 | -0.7 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural accumulation | 91.0 |
| XLF | Financials | 0.1 | -2.5 | 0.3 | 0.0 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural distribution; Exceptional institutional selling | 71.0 |
| XLV | Health Care | 1.7 | 0.9 | 0.6 | 3.1 | Up | Neutral | High | Momentum Rally | Watch | Structural accumulation | 91.0 |
| XLI | Industrials | 1.0 | -1.2 | 0.6 | 0.4 | Flat | Neutral | Normal | Neutral | Neutral | Medium-term recovery | 87.0 |
| XLK | Information Technology | 0.7 | -0.2 | 0.7 | 0.1 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural accumulation | 91.0 |
| XLB | Materials | -0.6 | -1.4 | 0.6 | 1.3 | Up | Buy | High | Confirmed Accumulation | Strong Risk-On | Tactical rebound inside structural distribution | 83.0 |
| XLRE | Real Estate | 0.2 | -1.4 | 0.5 | 0.2 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Medium-term recovery | 87.0 |
| XLU | Utilities | -0.3 | 1.1 | 0.5 | -0.1 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural accumulation | 91.0 |

### Subsector PFV Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ITA | Aerospace and Defense | 0.1 | 0.3 | 0.3 | 1.9 | Flat | Neutral | High | High-Turnover Consolidation | Transition | Structural distribution | 79.0 |
| SOXX | Semiconductors | 0.9 | -0.6 | 0.7 | 3.8 | Down | Neutral | High | Heavy Selling Pressure | Cautious | Structural accumulation | 91.0 |
| SMH | Semiconductors | 0.3 | -0.2 | 0.6 | 3.3 | Down | Neutral | High | Heavy Selling Pressure | Cautious | Structural accumulation | 91.0 |
| CIBR | Cybersecurity | 0.3 | 1.6 | 0.8 | 1.2 | Down | Neutral | High | Heavy Selling Pressure | Cautious | Structural accumulation; Strong sponsorship | 99.0 |

### Material Flow Divergences

| Severity | Type | Primary | Comparison | Interpretation |
| --- | --- | --- | --- | --- |
| high | close_substitute_divergence | GLD | IAU | primary representative differs from close substitute |
| high | close_substitute_divergence | AGG | IUSB | primary representative differs from close substitute |
| high | close_substitute_divergence | IWF | IVW | primary representative differs from close substitute |
| high | close_substitute_divergence | IWD | IVE | primary representative differs from close substitute |
| high | close_substitute_divergence | IWM | IJR | primary representative differs from close substitute |


## Contradiction / Audit Flags

No contradiction flags were triggered by current deterministic rules.

## Data Quality Notes

- Technical rows loaded: `60`
- S&P 500 constituent technical rows loaded: `503`
- Macro rows loaded: `48`
- Live macro rows used: `12`
- Economic rows loaded: `113`
- News rows loaded: `80`
- Positioning/flow rows loaded: `30`

## Cycle Metadata

- Report generated at: 01 November 2026, 02:17:53 (HKT)

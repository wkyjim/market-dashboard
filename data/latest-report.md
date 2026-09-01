# Rule-Based Institutional Market Update

Generated at: 2 September 2026, 00:12:07 (HKT)
Window: 24h

## Executive Dashboard

- Regime score: **64.97 / 100** (Mild Risk-On)
- US equity strength: **81.44 / 100** (strong)
- Evidence quality: **79.5 / 100**
- ETF flow contribution: **47.39 / 100**, reliability **70.81 / 100**
- Breadth: **broad**; above 50DMA `80.0%`, above 200DMA `74.58%`
- Top sector score: **Cybersecurity** `70.5`
- Top theme score: **Small Caps** `61.8`

## Market Regime Score

| Metric | Value | Driver / Interpretation |
| --- | --- | --- |
| Overall regime | 64.97 | Mild Risk-On |
| equity_trend | 93.75 | risk-on support; Core equity ETFs versus moving averages. |
| equity_momentum | 54.24 | neutral / mixed; 5D/20D/60D return momentum across SPY, QQQ, IWM, and SMH. |
| market_breadth | 78.75 | risk-on support; Participation breadth from tracked equity/ETF rows. |
| volatility | 70.0 | risk-on support; VIX level and change; higher score means calmer volatility conditions. |
| rates_yield_curve | 58.0 | mild risk-on support; Treasury yield pressure and curve shape; higher score means less rates pressure. |
| credit_proxy | 50.0 | neutral / mixed; Credit-market proxy; currently neutral when no direct spread signal is available. |
| dollar_fx | 54.21 | neutral / mixed; Dollar move; higher score means less USD tightening pressure. |
| commodity_confirmation | 47.0 | neutral / mixed; Copper, silver, oil, and gold mix; higher score means better cyclical confirmation. |
| etf_flow | 48.15 | neutral / mixed; Grouped ETF flow contribution adjusted for reliability. |
| news_confirmation | 60.62 | mild risk-on support; Weighted headline/news confirmation score. |
| Positive contributors |  | equity_trend=93.75, market_breadth=78.75, volatility=70.0, news_confirmation=60.62 |
| Negative contributors |  | none |

## US Equity Strength Score

| Component | Score |
| --- | --- |
| indices_above_moving_averages | 93.75 |
| sp500_trend | 100.0 |
| nasdaq_trend | 100.0 |
| russell_participation | 100.0 |
| returns_momentum | 54.24 |
| rsi_zone | 62.5 |
| macd_confirmation | 70.0 |
| volume_confirmation | 50.0 |
| breadth | 78.75 |

## Evidence Quality / Confidence

- Confidence score: `79.5`
- Agreement ratio: `0.5`
- Contradiction count: `0`
- Missing indicators: none
- Warning flags: none

## Cross-Asset Confirmation

| Area | Signal | Interpretation |
| --- | --- | --- |
| Equities | S&P 500 falling; Nasdaq falling; Russell 2000 falling | Confirms risk appetite when broad indices rise together; weak small caps would narrow the signal. |
| Rates | 10Y Treasury stable; MOVE rising | Rising yields can pressure duration assets; falling MOVE supports calmer bond volatility. |
| Dollar | DXY proxy stable | A stronger dollar can tighten financial conditions and pressure commodities/emerging-market risk. |
| Credit | HYG falling | High-yield weakness would challenge equity risk-on confirmation. |
| Gold | Gold falling | Gold strength can indicate defensive demand, inflation hedging, or geopolitical concern. |
| Silver | Silver falling | Silver helps distinguish precious-metal demand from industrial/cyclical confirmation when data is available. |
| Copper | Copper stable | Copper strength supports cyclical growth confirmation; weakness would dilute risk-on breadth. |
| Oil | WTI crude rising | Oil spikes can be inflationary risk; falling oil can ease cost pressure but may also flag demand softness. |
| Volatility | VIX rising | Falling VIX supports risk appetite; a volatility spike would reduce confidence in broad risk-on. |

### Macro Snapshot

Live macro rows are intraday snapshots from `public.macro_live`; closed rows are official stored rows from `public.macro`.

| Symbol | Name | Close | Pct Chg | Market Date | Status |
| --- | --- | --- | --- | --- | --- |
| ^GSPC | S&P 500 | 7650.11 | -0.47 | 2026-09-01 | live as of 1 September 2026, 23:01:50 (HKT) |
| ^IXIC | NASDAQ Composite | 26172.95 | -0.75 | 2026-09-01 | live as of 1 September 2026, 23:01:50 (HKT) |
| ^RUT | Russell 2000 Index | 2941.34 | -0.51 | 2026-09-01 | live as of 1 September 2026, 23:01:50 (HKT) |
| ^VIX | CBOE Volatility Index | 15.34 | 2.81 | 2026-09-01 | live as of 1 September 2026, 23:01:50 (HKT) |
| ^SKEW | CBOE SKEW Index | 148.53 | 3.11 | 2026-08-31 | closed |
| ^MOVE | ICE BofA MOVE Index | 75.32 | 7.81 | 2026-08-31 | closed |
| US2YT=X | United States 2-Year Treasury Yield | 4.37 | 0.43 | 2026-09-01 | live as of 1 September 2026, 23:01:50 (HKT) |
| US3YT=X | United States 3-Year Treasury Yield | 4.43 | 0.45 | 2026-09-01 | live as of 1 September 2026, 23:01:50 (HKT) |
| US5YT=X | United States 5-Year Treasury Yield | 4.53 | 0.4 | 2026-09-01 | live as of 1 September 2026, 23:01:50 (HKT) |
| US7YT=X | United States 7-Year Treasury Yield | 4.64 | 0.35 | 2026-09-01 | live as of 1 September 2026, 23:01:50 (HKT) |
| US10YT=X | United States 10-Year Treasury Yield | 4.77 | 0.34 | 2026-09-01 | live as of 1 September 2026, 23:01:50 (HKT) |
| US20YT=X | United States 20-Year Treasury Yield | 5.25 | 0.05 | 2026-09-01 | live as of 1 September 2026, 23:01:50 (HKT) |
| US30YT=X | United States 30-Year Treasury Yield | 5.25 | 0.01 | 2026-09-01 | live as of 1 September 2026, 23:01:50 (HKT) |
| HK50 | Hang Seng Futures | 25173.5 | -0.72 | 2026-09-01 | closed |
| KOR200c1 | KOSPI 200 Futures | 1065.65 | -0.21 | 2026-08-31 | closed |
| CIHc1 | SSE 50 Futures | 2915.8 | 0.21 | 2026-08-31 | closed |
| HYG | iShares iBoxx High Yield Corporate Bond ETF | 79.24 | -0.71 | 2026-09-01 | live as of 1 September 2026, 23:01:50 (HKT) |
| LQD | iShares iBoxx Investment Grade Corporate Bond ETF | 105.53 | -0.64 | 2026-09-01 | live as of 1 September 2026, 23:01:50 (HKT) |
| JNK | SPDR Bloomberg High Yield Bond ETF | 95.38 | -0.71 | 2026-09-01 | live as of 1 September 2026, 23:01:50 (HKT) |
| RSP | Invesco S&P 500 Equal Weight ETF | 218.2 | -0.54 | 2026-09-01 | live as of 1 September 2026, 23:01:50 (HKT) |
| IWF | iShares Russell 1000 Growth ETF | 121.63 | -0.88 | 2026-09-01 | live as of 1 September 2026, 23:01:50 (HKT) |
| IWD | iShares Russell 1000 Value ETF | 256.43 | -0.19 | 2026-09-01 | live as of 1 September 2026, 23:01:50 (HKT) |
| TLT | iShares 20+ Year Treasury Bond ETF | 82.09 | -0.52 | 2026-09-01 | live as of 1 September 2026, 23:01:50 (HKT) |
| IEF | iShares 7-10 Year Treasury Bond ETF | 92.27 | -0.51 | 2026-09-01 | live as of 1 September 2026, 23:01:50 (HKT) |
| SHY | iShares 1-3 Year Treasury Bond ETF | 81.64 | -0.3 | 2026-09-01 | live as of 1 September 2026, 23:01:50 (HKT) |
| GC=F | Gold Future | 4413.9 | -0.39 | 2026-09-01 | live as of 1 September 2026, 23:01:50 (HKT) |
| SI=F | Silver Future | 65.39 | -1.25 | 2026-09-01 | live as of 1 September 2026, 23:01:50 (HKT) |
| CL=F | WTI Crude Oil Future | 87.97 | 2.58 | 2026-09-01 | live as of 1 September 2026, 23:01:50 (HKT) |
| HG=F | Copper Future | 6.6 | 0.06 | 2026-09-01 | live as of 1 September 2026, 23:01:50 (HKT) |

## Market Dispersion Analysis

- Sector ETF 20D dispersion: `10.61` points (moderate); leader `XLK` (Technology) `7.46`, laggard `XLU` (Utilities) `-3.14`
- Sector ETF 60D dispersion: `19.34` points (high); leader `XLV` (Health Care) `15.55`, laggard `XLC` (Communication Services) `-3.79`

| Comparison | Left | Right | 20D Spread | Signal |
| --- | --- | --- | --- | --- |
| Equal-weight vs cap-weight | RSP (Equal-weight S&P 500) | SPY (S&P 500) | -0.05 | balanced |
| Small-cap vs large-cap | IWM (Russell 2000) | SPY (S&P 500) | -0.94 | balanced |
| Growth vs value | IWF (Russell 1000 Growth) | IWD (Russell 1000 Value) | -0.02 | balanced |
| Nasdaq vs S&P 500 | QQQ (Nasdaq 100) | SPY (S&P 500) | 0.08 | balanced |

## Sector Constituent Dispersion

- Breadth 50D / 200D: percentage of active S&P 500 constituents in the sector trading above the 50-day / 200-day moving average.
- Positive 20D: percentage of active sector constituents with positive 20-day return.
- Std 20D: cross-sectional standard deviation of constituent 20-day returns; higher means wider stock-level dispersion.

| Sector | Count | Breadth 50D | Breadth 200D | Positive 20D | 20D Dispersion | Std 20D | Label | Leaders | Laggards |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Information Technology | 73 | 60.27 | 70.83 | 82.19 | 72.99 | 13.83 | very high | SMCI, ZBRA, WDAY | FICO, CDNS, NXPI |
| Consumer Staples | 34 | 81.82 | 62.5 | 58.82 | 64.2 | 9.97 | very high | TGT, CLX, HSY | HRL, MO, MNST |
| Industrials | 83 | 69.51 | 74.68 | 62.65 | 59.1 | 9.43 | very high | LDOS, HII, ALLE | ROL, LII, CHRW |
| Health Care | 59 | 86.44 | 79.66 | 76.27 | 51.44 | 8.44 | very high | VEEV, CRL, REGN | CVS, PODD, DVA |
| Communication Services | 24 | 78.26 | 65.22 | 70.83 | 45.44 | 11.1 | very high | CHTR, FOXA, FOX | RDDT, TTD, APP |
| Consumer Discretionary | 47 | 59.57 | 48.94 | 57.45 | 42.28 | 9.32 | very high | ABNB, GRMN, EXPE | TSLA, DECK, APTV |
| Materials | 25 | 72.0 | 80.0 | 64.0 | 38.25 | 8.72 | very high | NEM, NUE, FCX | CRH, LIN, CTVA |
| Energy | 21 | 90.48 | 85.71 | 71.43 | 33.27 | 8.3 | very high | APA, MPC, PSX | TRGP, HAL, TPL |
| Financials | 76 | 86.3 | 88.57 | 64.47 | 28.88 | 6.1 | very high | ARES, GPN, APO | TROW, SPGI, MSCI |
| Real Estate | 30 | 44.83 | 79.31 | 30.0 | 20.62 | 4.88 | very high | DLR, CSGP, EQIX | UDR, REG, DOC |
| Utilities | 31 | 19.35 | 51.61 | 6.45 | 20.47 | 3.79 | very high | CEG, AWK, PCG | NI, EIX, NRG |

## Economic Data Snapshot

### U.S. Labor

| Indicator | Latest | Unit | Change | Date | Rule-Based Interpretation |
| --- | --- | --- | --- | --- | --- |
| All Employees, Total Nonfarm | 158858.0 | thousands | -23.0 thousands vs prior | 2026-07-01 | Lower reading signals softer activity or liquidity. |
| Unemployment Rate | 4.1 | percent | -0.1 pp vs prior | 2026-07-01 | Lower reading eases macro pressure. |
| Initial Claims | 215000.0 | number | -12000.0 number vs prior | 2026-06-20 | Lower claims indicate firmer labor-market conditions. |
| Continued Claims | 1821000.0 | number | 21000.0 number vs prior | 2026-06-13 | Higher claims indicate softer labor-market conditions. |
| Labor Force Participation Rate | 61.4 | percent | -0.1 pp vs prior | 2026-07-01 | Lower participation constrains labor supply. |

### U.S. Growth

| Indicator | Latest | Unit | Change | Date | Rule-Based Interpretation |
| --- | --- | --- | --- | --- | --- |
| Real Gross Domestic Product | 24269.61 | billions chained 2017 dollars | 89.19 billions chained 2017 dollars vs prior | 2026-04-01 | Higher reading supports activity or liquidity. |
| Industrial Production Index | 102.65 | index 2017=100 | 0.14 index pts vs prior | 2026-05-01 | Higher reading supports activity or liquidity. |
| Advance Retail Sales | 763602.0 | millions dollars | -4470.0 millions dollars vs prior | 2026-07-01 | Lower reading signals softer activity or liquidity. |

### U.S. Inflation

| Indicator | Latest | Unit | Change | Date | Rule-Based Interpretation |
| --- | --- | --- | --- | --- | --- |
| Headline CPI month-over-month inflation rate | 0.07 | percent | 0.5 pp vs prior | 2026-07-01 | Higher reading increases macro pressure. |
| Headline CPI year-over-year inflation rate | 3.54 | percent | -0.19 pp vs prior | 2026-07-01 | Lower reading eases macro pressure. |
| Core CPI month-over-month inflation rate | 0.22 | percent | 0.23 pp vs prior | 2026-07-01 | Higher reading increases macro pressure. |
| Core CPI year-over-year inflation rate | 2.79 | percent | -0.02 pp vs prior | 2026-07-01 | Lower reading eases macro pressure. |
| Headline CPI year-over-year inflation rate | 3.52 | percent | -0.36 pp vs prior | 2026-07-01 | Lower reading eases macro pressure. |
| Core CPI year-over-year inflation rate | 2.67 | percent | -0.19 pp vs prior | 2026-07-01 | Lower reading eases macro pressure. |
| Headline PCE Price Index month-over-month inflation rate | 0.16 | percent | 0.25 pp vs prior | 2026-07-01 | Higher reading increases macro pressure. |
| Headline PCE Price Index year-over-year inflation rate | 3.7 | percent | -0.02 pp vs prior | 2026-07-01 | Lower reading eases macro pressure. |
| Core PCE Price Index month-over-month inflation rate | 0.25 | percent | 0.1 pp vs prior | 2026-07-01 | Higher reading increases macro pressure. |
| Core PCE Price Index year-over-year inflation rate | 3.34 | percent | 0.0 pp vs prior | 2026-07-01 | Higher reading increases macro pressure. |
| Headline PPI Final Demand month-over-month inflation rate | -0.1 | percent | -0.07 pp vs prior | 2026-07-01 | Lower reading eases macro pressure. |
| Headline PPI Final Demand year-over-year inflation rate | 4.69 | percent | -0.85 pp vs prior | 2026-07-01 | Lower reading eases macro pressure. |
| Core PPI Final Demand Less Foods and Energy month-over-month inflation rate | 0.24 | percent | -0.15 pp vs prior | 2026-07-01 | Lower reading eases macro pressure. |
| Core PPI Final Demand Less Foods and Energy year-over-year inflation rate | 4.16 | percent | -0.57 pp vs prior | 2026-07-01 | Lower reading eases macro pressure. |
| Consumer Price Index for All Urban Consumers | 332.81 | index 1982-1984=100 | 0.25 index pts vs prior | 2026-07-01 | Higher reading increases macro pressure. |
| Core CPI | 336.79 | index 1982-1984=100 | 0.72 index pts vs prior | 2026-07-01 | Higher reading increases macro pressure. |
| Personal Consumption Expenditures Price Index | 131.66 | index 2017=100 | 0.2 index pts vs prior | 2026-07-01 | Higher reading increases macro pressure. |
| Core PCE Price Index | 130.66 | index 2017=100 | 0.32 index pts vs prior | 2026-07-01 | Higher reading increases macro pressure. |
| Producer Price Index: Final Demand | 156.93 | index Nov 2009=100 | -0.16 index pts vs prior | 2026-07-01 | Latest structural macro observation. |
| Producer Price Index: Final Demand Less Foods and Energy | 154.45 | index Apr 2010=100 | 0.37 index pts vs prior | 2026-07-01 | Latest structural macro observation. |

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
| US dollar/Euro ECB reference exchange rate | 1.16 | USD | -0.0 USD vs prior | 2026-09-01 | EUR weakened versus this currency. |
| Japanese yen/Euro ECB reference exchange rate | 185.63 | JPY | 0.41 JPY vs prior | 2026-09-01 | EUR strengthened versus this currency. |
| Chinese yuan renminbi/Euro ECB reference exchange rate | 7.79 | CNY | -0.0 CNY vs prior | 2026-09-01 | EUR weakened versus this currency. |
| Australian dollar/Euro ECB reference exchange rate | 1.62 | AUD | 0.0 AUD vs prior | 2026-09-01 | EUR strengthened versus this currency. |

ABS Australia note: ABS rows are stored locally/Neon, but most series are dimension-coded; only curated series should be promoted into narrative report text.

## Sector and Theme Leadership

### Official Sector Strength

Supporting and detracting names are the top/bottom S&P 500 constituents by 20D return when constituent coverage is available; otherwise the report falls back to related ETFs.

| Rank | Sector | Score | Trend | Momentum | Stock Breadth | ETF Flow | Flow Reliability | 3M RS | Supporting / Leaders | Detracting / Laggards |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Cybersecurity | 70.5 | strong uptrend | positive | broad | 68.01 | 65.0 | 62.96 | CIBR | CIBR |
| 2 | Grid Infrastructure | 68.65 | strong uptrend | neutral | broad | 69.24 | 65.0 | 49.05 | GRID | GRID |
| 3 | Healthcare | 68.51 | strong uptrend | positive | broad | 71.72 | 100.0 | 54.37 | VEEV, CRL, REGN | CVS, PODD, DVA |
| 4 | Defense | 68.37 | strong uptrend | positive | broad | 58.12 | 65.0 | 57.75 | XAR | XAR |
| 5 | Energy | 65.96 | strong uptrend | neutral | broad | 50.0 | 0.0 | 50.27 | APA, MPC, PSX | TRGP, HAL, TPL |
| 6 | Technology | 65.5 | strong uptrend | neutral | broad | 50.09 | 90.0 | 51.68 | SMCI, ZBRA, WDAY | FICO, CDNS, NXPI |
| 7 | Industrials | 65.43 | strong uptrend | neutral | broad | 43.34 | 65.0 | 51.11 | LDOS, HII, ALLE | ROL, LII, CHRW |
| 8 | Financials | 62.91 | strong uptrend | positive | broad | 50.0 | 0.0 | 52.34 | ARES, GPN, APO | TROW, SPGI, MSCI |
| 9 | Consumer Staples | 61.31 | strong uptrend | neutral | broad | 47.22 | 65.0 | 45.88 | TGT, CLX, HSY | HRL, MO, MNST |
| 10 | Real Estate | 58.48 | strong uptrend | neutral | broad | 45.6 | 90.0 | 46.51 | DLR, CSGP, EQIX | UDR, REG, DOC |
| 11 | Consumer Discretionary | 56.2 | uptrend | neutral | broad | 51.54 | 65.0 | 47.0 | ABNB, GRMN, EXPE | TSLA, DECK, APTV |
| 12 | Semiconductors | 55.64 | strong uptrend | neutral | weak | 39.34 | 100.0 | 51.7 | SOXX, SMH | SMH, SOXX |
| 13 | Nuclear | 55.5 | neutral | neutral | broad | 50.0 | 0.0 | 50.82 | NLR | NLR |
| 14 | Crypto | 51.81 | neutral | neutral | mixed | 68.08 | 65.0 | 50.0 |  |  |
| 15 | Utilities | 34.76 | strong downtrend | neutral | weak | 51.17 | 65.0 | 43.97 | CEG, AWK, PCG | NI, EIX, NRG |

### Thematic Strength

| Rank | Theme | Score | Setup | ETF Flow | Flow Reliability | Dispersion | Price | News |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Small Caps | 61.8 | Positive setup | 58.98 | 65.0 | 0.0 | True | False |
| 2 | Healthcare Innovation | 61.73 | Positive setup | 71.72 | 100.0 | 11.95 | True | False |
| 3 | Cybersecurity | 60.19 | Neutral / watchlist | 68.01 | 65.0 | 25.61 | True | False |
| 4 | Defense | 60.06 | Positive setup | 58.12 | 65.0 | 16.07 | True | False |
| 5 | Energy | 59.12 | Positive setup | 50.0 | 0.0 | 1.59 | False | False |
| 6 | Financials | 57.96 | Positive setup | 50.0 | 0.0 | 10.64 | False | False |
| 7 | Quality Growth | 56.13 | Neutral / watchlist | 56.3 | 65.0 | 32.28 | False | False |
| 8 | Semiconductors | 55.88 | Neutral / watchlist | 39.34 | 100.0 | 15.16 | False | False |
| 9 | AI Infrastructure | 55.46 | Neutral / watchlist | 39.34 | 100.0 | 26.16 | False | False |
| 10 | Grid Infrastructure | 52.33 | Neutral / watchlist | 69.24 | 65.0 | 17.92 | False | False |
| 11 | Nuclear | 51.49 | Neutral / watchlist | 50.0 | 0.0 | 18.53 | False | False |
| 12 | Dividend Defensives | 51.21 | Neutral / watchlist | 50.84 | 65.0 | 7.21 | False | False |
| 13 | Crypto Infrastructure | 34.14 | Underperformance risk | 68.08 | 65.0 | 7.37 | False | False |

- Top 5 improving themes: Financials, Healthcare Innovation, Defense, Cybersecurity, Small Caps
- Top 5 deteriorating themes: Crypto Infrastructure, Nuclear, Energy, Grid Infrastructure, Quality Growth
- Strong news but weak price confirmation: none
- Strong price but weak news confirmation: Small Caps, Healthcare Innovation, Cybersecurity, Defense

### Sector / Theme Alignment

| Sector | Related Themes | Sector Score | Sector Signal | Theme Score | Theme Signal | Interpretation |
| --- | --- | --- | --- | --- | --- | --- |
| Cybersecurity | Cybersecurity | 70.5 | strong | 60.19 | positive | sector and theme confirmation |
| Grid Infrastructure | Grid Infrastructure | 68.65 | strong | 52.33 | mixed | sector stronger than related themes |
| Healthcare | Healthcare Innovation | 68.51 | strong | 61.73 | positive | sector and theme confirmation |
| Defense | Defense | 68.37 | strong | 60.06 | positive | sector and theme confirmation |
| Energy | Energy | 65.96 | strong | 59.12 | positive | sector and theme confirmation |
| Technology | AI Infrastructure, Semiconductors, Quality Growth | 65.5 | strong | 55.82 | positive | sector and theme confirmation |
| Industrials | Defense, Grid Infrastructure | 65.43 | strong | 56.2 | positive | sector and theme confirmation |
| Financials | Financials | 62.91 | positive | 57.96 | positive | sector and theme confirmation |
| Consumer Staples | Dividend Defensives | 61.31 | positive | 51.21 | mixed | sector stronger than related themes |
| Real Estate | Dividend Defensives | 58.48 | positive | 51.21 | mixed | sector stronger than related themes |
| Consumer Discretionary | Small Caps | 56.2 | positive | 61.8 | positive | sector and theme confirmation |
| Semiconductors | AI Infrastructure, Semiconductors | 55.64 | positive | 55.67 | positive | sector and theme confirmation |
| Nuclear | Nuclear | 55.5 | positive | 51.49 | mixed | sector stronger than related themes |
| Crypto | Crypto Infrastructure | 51.81 | mixed | 34.14 | very weak | mixed confirmation |
| Utilities | Grid Infrastructure, Nuclear, Dividend Defensives | 34.76 | very weak | 51.68 | mixed | mixed confirmation |

## Three-Month Outperformance Setup

| Rank | Theme | Score | Classification | Drivers | Invalidation Triggers |
| --- | --- | --- | --- | --- | --- |
| 1 | Small Caps | 64.31 | Positive setup | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 2 | Healthcare Innovation | 63.24 | Positive setup | relative_strength_60d, trend_persistence, breadth, downside_volatility, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 3 | Energy | 63.11 | Positive setup | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 4 | Financials | 62.65 | Positive setup | relative_strength_60d, trend_persistence, breadth, downside_volatility, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 5 | Defense | 61.76 | Positive setup | relative_strength_20d, trend_persistence, breadth, downside_volatility, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 6 | Semiconductors | 59.27 | Neutral / watchlist | trend_persistence, breadth | relative strength below SPY, breadth below 45%, news turns negative |
| 7 | Cybersecurity | 59.16 | Neutral / watchlist | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 8 | AI Infrastructure | 57.47 | Neutral / watchlist | trend_persistence, breadth | relative strength below SPY, breadth below 45%, news turns negative |
| 9 | Quality Growth | 56.9 | Neutral / watchlist | trend_persistence, breadth | relative strength below SPY, breadth below 45%, news turns negative |
| 10 | Dividend Defensives | 54.67 | Neutral / watchlist | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 11 | Grid Infrastructure | 52.12 | Neutral / watchlist | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 12 | Nuclear | 50.58 | Neutral / watchlist | relative_strength_20d | relative strength below SPY, breadth below 45%, news turns negative |

## Breadth and Participation

- Above 50DMA: `80.0%`
- Above 200DMA: `74.58%`
- Positive 20D return: `81.67%`

## Volatility and Risk Signals

- VIX close=15.34 pct_chg=2.81

## News Analytics

- Sentiment counts: {'positive': 47, 'negative': 30, 'neutral': 3}
- News confirmation score: `60.62`

### Top Market-Moving Headlines

**1. Global oil prices surge above $92 a barrel after report of strikes on two tankers in the Strait of Hormuz**
- Source: MarketWatch Top Stories
- Importance / impact: High / Positive
- Relevance / horizon: macro / short-term
- Affected assets: U.S, oil_prices, geo_political_risk
- Score: `68.0`
- Investment implication: Macro-relevant positive signal; use as context for rates, volatility, and index confirmation over the short-term.

**2. Global oil prices are surging after reports of more Hormuz trouble**
- Source: MarketWatch Bulletins
- Importance / impact: High / Negative
- Relevance / horizon: macro / short-term
- Affected assets: WFC, XOM, CVX, oil_prices, geopolitical_risk
- Score: `64.6`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the short-term.

**3. Global bond yields soar to multi-decade highs as Middle East turmoil reignites inflation fears**
- Source: CNBC Business News
- Importance / impact: High / Negative
- Relevance / horizon: macro / short-term
- Affected assets: U.K, U.S, inflation, geo-political, bond market
- Score: `54.4`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the short-term.

**4. Amazon’s stock slips as the FTC alleges billions of dollars in hidden ad fees**
- Source: MarketWatch Top Stories
- Importance / impact: High / Negative
- Relevance / horizon: macro / short-term
- Affected assets: AMZN, FTC, regulatory, advertising
- Score: `51.0`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the short-term.

**5. Global Bond Yields Surge as Oil Prices Fuel Inflation Worries**
- Source: Dow Jones Economy
- Importance / impact: High / Negative
- Relevance / horizon: macro / short-term
- Affected assets: U.S, inflation, geopolitical, interest_rates
- Score: `51.0`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the short-term.

**6. Oil prices extend move over $90 after report of two tankers struck in Hormuz**
- Source: MarketWatch Bulletins
- Importance / impact: High / Positive
- Relevance / horizon: macro / short-term
- Affected assets: oil, geopolitical
- Score: `48.45`
- Investment implication: Macro-relevant positive signal; use as context for rates, volatility, and index confirmation over the short-term.

**7. Tehran urges return to June deal, oil prices rise as Trump vows to hit Iran 'hard'**
- Source: CNBC Business Headlines
- Importance / impact: High / Negative
- Relevance / horizon: macro / short-term
- Affected assets: U.S, geopolitical risk, oil supply concerns
- Score: `47.6`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the short-term.

**8. Euro zone inflation is back above 3%. Higher interest rates are likely to follow**
- Source: CNBC Economy
- Importance / impact: Medium / Positive
- Relevance / horizon: sector_theme / short-term
- Affected assets: inflation, interest rates, central bank
- Score: `45.9`
- Investment implication: Theme or sector positive signal; requires price and volume confirmation before affecting rankings.

**9. PG&E, other utility stocks sink as California leaves investors exposed to wildfire liability**
- Source: MarketWatch Top Stories
- Importance / impact: Medium / Negative
- Relevance / horizon: sector_theme / short-term
- Affected assets: A, E, PG, wildfire liability, legislation
- Score: `43.35`
- Investment implication: Theme or sector negative signal; requires price and volume confirmation before affecting rankings.

**10. Eurozone Inflation Climbs to Near Three-Year High Ahead of ECB Meeting**
- Source: Dow Jones Economy
- Importance / impact: Medium / Positive
- Relevance / horizon: sector_theme / short-term
- Affected assets: Economic Policy, Inflation, Central Bank
- Score: `43.35`
- Investment implication: Theme or sector positive signal; requires price and volume confirmation before affecting rankings.


### Headline Quality Checks

Noisy headline list: The 10-year Treasury yield is breaking out and 5% , Oil Prices Rise as Renewed U.S.-Iran Fighting Deep, Why Dell’s stock stands to gain from developments , Broadcom reports earnings this week. Mike Khouw sa, Stock market today: Dow, S&P 500, Nasdaq drop as r

## Positioning & Flow Dashboard

Positioning and flow data is used as confirmation only.

### Deferred Flow Sections

- Official ETF / fund flows: current report uses shares-outstanding-derived net fund flow estimates from free ETF metadata.
- Institutional Ownership: not available until SEC 13F ingestion is implemented.
- Grouped exposure flow reliability: use issuer coverage and availability status before treating ETF flow as confirmation.

## ETF Flows Analysis

- Market flow regime: `Mixed / Neutral`
- Market flow score: `50.0 / 100`
- Equity risk flow: `51.8`
- Credit risk flow: `47.0`
- Sector cyclicality flow: `45.2`
- Duration/liquidity flow: `50.3`
- Alternatives: `barbell demand`
- ETF flow reliability: `70.8 / 100`
- Dominant allocation direction: `defensive demand`

### Core Flow Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVV | U.S. Broad Equity | -0.6 | -0.6 | 0.2 | n/a | Flat | Neutral | Normal | Neutral | Neutral | Medium-term deterioration; Persistent selling | 60.0 |
| ACWI | Global Equity | -0.7 | -1.2 | 0.0 | n/a | Flat | Neutral | Normal | Neutral | Neutral | Mixed or neutral flow structure; Persistent selling | 62.0 |
| EFA | Developed Markets ex-U.S. | -0.1 | -0.1 | 0.0 | n/a | Flat | Neutral | Normal | Neutral | Neutral | Mixed or neutral flow structure; Persistent selling | 62.0 |
| IEMG | Emerging Markets | -0.1 | 0.0 | 0.1 | n/a | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural accumulation; Persistent selling | 68.0 |
| IJH | U.S. Mid Cap | 2.0 | 2.1 | 0.9 | n/a | Down | Buy | Normal | Contrarian Buying | Watch | Strong confirmation; Exceptional institutional buying, Strong sponsorship | 96.0 |
| IWM | U.S. Small Cap | 1.0 | -0.0 | 0.4 | n/a | Flat | Neutral | Normal | Neutral | Neutral | Medium-term recovery | 72.0 |
| LQD | Investment-Grade Credit | -0.5 | 0.3 | 0.6 | n/a | Flat | Neutral | Normal | Neutral | Neutral | Medium-term deterioration | 68.0 |
| HYG | High-Yield Credit | -0.8 | 0.2 | 0.3 | n/a | Flat | Neutral | Normal | Neutral | Neutral | Medium-term deterioration | 68.0 |
| SGOV | Treasury Bills / Cash | 0.6 | -1.4 | 1.0 | n/a | Flat | Neutral | Normal | Neutral | Neutral | Medium-term recovery; Strong sponsorship | 80.0 |
| SHY | Short-Duration Treasuries | 1.3 | -0.3 | 0.6 | n/a | Flat | Buy | Normal | Quiet Accumulation | Improving | Strong confirmation; Exceptional institutional buying | 88.0 |
| IEF | Intermediate-Duration Treasuries | -3.1 | -1.9 | 0.5 | n/a | Flat | Sell | Normal | Quiet Distribution | Weakening | Strong confirmation; Exceptional institutional selling | 72.0 |
| TLT | Long-Duration Treasuries | 2.3 | 2.9 | 0.6 | n/a | Flat | Buy | Normal | Quiet Accumulation | Improving | Strong confirmation; Exceptional institutional buying | 88.0 |
| GLD | Gold | 2.4 | 2.7 | 0.7 | n/a | Up | Buy | Normal | Steady Accumulation | Risk-On | Strong confirmation; Exceptional institutional buying | 88.0 |
| IBIT | Bitcoin | 1.9 | 0.3 | 0.8 | n/a | Up | Buy | Normal | Steady Accumulation | Risk-On | Strong confirmation; Strong sponsorship | 88.0 |

### Sector Flow Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| XLC | Communication Services | 0.2 | -0.8 | 0.3 | n/a | Flat | Neutral | Normal | Neutral | Neutral | Structural distribution | 64.0 |
| XLY | Consumer Discretionary | -0.2 | 0.5 | 0.4 | n/a | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Medium-term deterioration | 68.0 |
| XLP | Consumer Staples | 0.1 | 1.5 | 0.5 | n/a | Flat | Neutral | Normal | Neutral | Neutral | Medium-term deterioration | 68.0 |
| XLE | Energy | -0.9 | -0.7 | 0.4 | n/a | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural distribution | 64.0 |
| XLF | Financials | -1.8 | 0.5 | 0.2 | n/a | Flat | Sell | Normal | Quiet Distribution | Weakening | Medium-term deterioration; Persistent selling | 60.0 |
| XLV | Health Care | 0.2 | 1.2 | 0.6 | n/a | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural accumulation | 76.0 |
| XLI | Industrials | -1.0 | 0.2 | 0.3 | n/a | Down | Sell | Normal | Persistent Distribution | Risk-Off | Medium-term deterioration | 68.0 |
| XLK | Information Technology | -0.8 | -0.9 | 0.5 | n/a | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural distribution | 64.0 |
| XLB | Materials | -0.3 | -1.1 | 0.5 | n/a | Flat | Neutral | Normal | Neutral | Neutral | Medium-term recovery | 72.0 |
| XLRE | Real Estate | -0.8 | 0.7 | 0.3 | n/a | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Medium-term deterioration | 68.0 |
| XLU | Utilities | -0.3 | 0.3 | 0.3 | n/a | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Medium-term deterioration | 68.0 |

### Subsector PFV Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ITA | Aerospace and Defense | 0.5 | 0.9 | 0.4 | n/a | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Medium-term recovery | 72.0 |
| SOXX | Semiconductors | -1.8 | 0.1 | 0.3 | n/a | Flat | Neutral | Normal | Neutral | Neutral | Medium-term deterioration | 68.0 |
| SMH | Semiconductors | -0.9 | -0.3 | 0.5 | n/a | Flat | Neutral | Normal | Neutral | Neutral | Medium-term deterioration | 68.0 |
| CIBR | Cybersecurity | 1.9 | 1.3 | 0.8 | n/a | Up | Buy | Normal | Steady Accumulation | Risk-On | Strong confirmation; Strong sponsorship | 88.0 |

### Material Flow Divergences

| Severity | Type | Primary | Comparison | Interpretation |
| --- | --- | --- | --- | --- |
| medium | related_subsector_divergence | XLI | ITA | defense-specific demand differs from broad industrials |
| medium | related_subsector_divergence | XLK | SOXX | technology differs from semiconductors |
| high | close_substitute_divergence | GLD | IAU | primary representative differs from close substitute |
| high | close_substitute_divergence | AGG | IUSB | primary representative differs from close substitute |
| high | close_substitute_divergence | HYG | JNK | primary representative differs from close substitute |
| high | close_substitute_divergence | IWM | IJR | primary representative differs from close substitute |


## Contradiction / Audit Flags

No contradiction flags were triggered by current deterministic rules.

## Data Quality Notes

- Technical rows loaded: `60`
- S&P 500 constituent technical rows loaded: `503`
- Macro rows loaded: `49`
- Live macro rows used: `40`
- Economic rows loaded: `113`
- News rows loaded: `80`
- Positioning/flow rows loaded: `50`

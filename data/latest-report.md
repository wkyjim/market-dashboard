# Rule-Based Institutional Market Update

Generated at: 14 August 2026, 06:14:23 (HKT)
Window: 24h

## Executive Dashboard

- Regime score: **64.83 / 100** (Mild Risk-On)
- US equity strength: **81.4 / 100** (strong)
- Evidence quality: **79.5 / 100**
- ETF flow contribution: **51.27 / 100**, reliability **65.0 / 100**
- Breadth: **broad**; above 50DMA `76.67%`, above 200DMA `76.27%`
- Top sector score: **Cybersecurity** `68.7`
- Top theme score: **Small Caps** `60.9`

## Market Regime Score

| Metric | Value | Driver / Interpretation |
| --- | --- | --- |
| Overall regime | 64.83 | Mild Risk-On |
| equity_trend | 93.75 | risk-on support; Core equity ETFs versus moving averages. |
| equity_momentum | 54.24 | neutral / mixed; 5D/20D/60D return momentum across SPY, QQQ, IWM, and SMH. |
| market_breadth | 78.2 | risk-on support; Participation breadth from tracked equity/ETF rows. |
| volatility | 70.0 | risk-on support; VIX level and change; higher score means calmer volatility conditions. |
| rates_yield_curve | 58.0 | mild risk-on support; Treasury yield pressure and curve shape; higher score means less rates pressure. |
| credit_proxy | 50.0 | neutral / mixed; Credit-market proxy; currently neutral when no direct spread signal is available. |
| dollar_fx | 55.21 | mild risk-on support; Dollar move; higher score means less USD tightening pressure. |
| commodity_confirmation | 45.0 | mild risk-off pressure; Copper, silver, oil, and gold mix; higher score means better cyclical confirmation. |
| etf_flow | 50.83 | neutral / mixed; Grouped ETF flow contribution adjusted for reliability. |
| news_confirmation | 53.75 | neutral / mixed; Weighted headline/news confirmation score. |
| Positive contributors |  | equity_trend=93.75, market_breadth=78.2, volatility=70.0 |
| Negative contributors |  | commodity_confirmation=45.0 |

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
| breadth | 78.2 |

## Evidence Quality / Confidence

- Confidence score: `79.5`
- Agreement ratio: `0.5`
- Contradiction count: `1`
- Missing indicators: none
- Warning flags: none

## Cross-Asset Confirmation

| Area | Signal | Interpretation |
| --- | --- | --- |
| Equities | S&P 500 rising; Nasdaq rising; Russell 2000 stable | Confirms risk appetite when broad indices rise together; weak small caps would narrow the signal. |
| Rates | 10Y Treasury falling; MOVE rising | Rising yields can pressure duration assets; falling MOVE supports calmer bond volatility. |
| Dollar | DXY proxy stable | A stronger dollar can tighten financial conditions and pressure commodities/emerging-market risk. |
| Credit | HYG stable | High-yield weakness would challenge equity risk-on confirmation. |
| Gold | Gold stable | Gold strength can indicate defensive demand, inflation hedging, or geopolitical concern. |
| Silver | Silver falling | Silver helps distinguish precious-metal demand from industrial/cyclical confirmation when data is available. |
| Copper | Copper stable | Copper strength supports cyclical growth confirmation; weakness would dilute risk-on breadth. |
| Oil | WTI crude falling | Oil spikes can be inflationary risk; falling oil can ease cost pressure but may also flag demand softness. |
| Volatility | VIX rising | Falling VIX supports risk appetite; a volatility spike would reduce confidence in broad risk-on. |

### Macro Snapshot

Live macro rows are intraday snapshots from `public.macro_live`; closed rows are official stored rows from `public.macro`.

| Symbol | Name | Close | Pct Chg | Market Date | Status |
| --- | --- | --- | --- | --- | --- |
| ^GSPC | S&P 500 | 7798.99 | 0.65 | 2026-08-13 | closed |
| ^IXIC | NASDAQ Composite | 26803.03 | 0.81 | 2026-08-13 | closed |
| ^RUT | Russell 2000 Index | 3052.85 | 0.24 | 2026-08-13 | closed |
| ^VIX | CBOE Volatility Index | 14.63 | 0.55 | 2026-08-13 | closed |
| ^SKEW | CBOE SKEW Index | 134.37 | -1.59 | 2026-08-13 | closed |
| ^MOVE | ICE BofA MOVE Index | 76.82 | 8.38 | 2026-07-24 | closed |
| US2YT=X | United States 2-Year Treasury Yield | 4.14 | -1.3 | 2026-08-13 | closed |
| US3YT=X | United States 3-Year Treasury Yield | 4.22 | -1.28 | 2026-08-13 | closed |
| US5YT=X | United States 5-Year Treasury Yield | 4.32 | -1.3 | 2026-08-13 | closed |
| US7YT=X | United States 7-Year Treasury Yield | 4.47 | -1.17 | 2026-08-13 | closed |
| US10YT=X | United States 10-Year Treasury Yield | 4.63 | -1.0 | 2026-08-13 | closed |
| US20YT=X | United States 20-Year Treasury Yield | 5.21 | -0.71 | 2026-08-13 | closed |
| US30YT=X | United States 30-Year Treasury Yield | 5.22 | -0.6 | 2026-08-13 | closed |
| HK50 | Hang Seng Futures | 25218.0 | -0.42 | 2026-08-13 | closed |
| KOR200c1 | KOSPI 200 Futures | 1074.3 | 3.77 | 2026-08-12 | closed |
| CIHc1 | SSE 50 Futures | 2931.8 | 0.15 | 2026-08-12 | closed |
| HYG | iShares iBoxx High Yield Corporate Bond ETF | 79.79 | 0.23 | 2026-08-13 | closed |
| LQD | iShares iBoxx Investment Grade Corporate Bond ETF | 106.55 | 0.41 | 2026-08-13 | closed |
| JNK | SPDR Bloomberg High Yield Bond ETF | 96.04 | 0.2 | 2026-08-13 | closed |
| RSP | Invesco S&P 500 Equal Weight ETF | 222.73 | 0.75 | 2026-08-13 | closed |
| IWF | iShares Russell 1000 Growth ETF | 125.66 | 1.0 | 2026-08-13 | closed |
| IWD | iShares Russell 1000 Value ETF | 258.7 | 0.36 | 2026-08-13 | closed |
| TLT | iShares 20+ Year Treasury Bond ETF | 82.59 | 0.58 | 2026-08-13 | closed |
| IEF | iShares 7-10 Year Treasury Bond ETF | 93.3 | 0.37 | 2026-08-13 | closed |
| SHY | iShares 1-3 Year Treasury Bond ETF | 82.03 | 0.13 | 2026-08-13 | closed |
| GC=F | Gold Future | 4407.1 | -0.04 | 2026-08-13 | closed |
| SI=F | Silver Future | 64.58 | -1.48 | 2026-08-13 | closed |
| CL=F | WTI Crude Oil Future | 81.21 | -2.47 | 2026-08-13 | closed |
| HG=F | Copper Future | 6.59 | -0.11 | 2026-08-13 | closed |

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
| Information Technology | 73 | 61.64 | 75.0 | 82.19 | 72.99 | 13.83 | very high | SMCI, ZBRA, WDAY | FICO, CDNS, NXPI |
| Consumer Staples | 34 | 78.79 | 62.5 | 58.82 | 64.2 | 9.97 | very high | TGT, CLX, HSY | HRL, MO, MNST |
| Industrials | 83 | 69.51 | 74.68 | 62.65 | 59.1 | 9.43 | very high | LDOS, HII, ALLE | ROL, LII, CHRW |
| Health Care | 59 | 88.14 | 84.75 | 76.27 | 51.44 | 8.44 | very high | VEEV, CRL, REGN | CVS, PODD, DVA |
| Communication Services | 23 | 77.27 | 59.09 | 73.91 | 45.44 | 10.82 | very high | CHTR, FOXA, FOX | META, TTD, APP |
| Consumer Discretionary | 47 | 57.45 | 51.06 | 57.45 | 42.28 | 9.32 | very high | ABNB, GRMN, EXPE | TSLA, DECK, APTV |
| Materials | 25 | 64.0 | 76.0 | 64.0 | 38.25 | 8.72 | very high | NEM, NUE, FCX | CRH, LIN, CTVA |
| Energy | 21 | 80.95 | 80.95 | 71.43 | 33.27 | 8.3 | very high | APA, MPC, PSX | TRGP, HAL, TPL |
| Financials | 76 | 86.3 | 90.0 | 64.47 | 28.88 | 6.1 | very high | ARES, GPN, APO | TROW, SPGI, MSCI |
| Real Estate | 31 | 45.16 | 80.65 | 29.03 | 20.62 | 4.94 | very high | DLR, CSGP, EQIX | UDR, REG, DOC |
| Utilities | 31 | 12.9 | 48.39 | 6.45 | 20.47 | 3.79 | very high | CEG, AWK, PCG | NI, EIX, NRG |

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
| Real Gross Domestic Product | 24270.6 | billions chained 2017 dollars | 90.18 billions chained 2017 dollars vs prior | 2026-04-01 | Higher reading supports activity or liquidity. |
| Industrial Production Index | 102.65 | index 2017=100 | 0.14 index pts vs prior | 2026-05-01 | Higher reading supports activity or liquidity. |
| Advance Retail Sales | 768553.0 | millions dollars | 1677.0 millions dollars vs prior | 2026-06-01 | Higher reading supports activity or liquidity. |

### U.S. Inflation

| Indicator | Latest | Unit | Change | Date | Rule-Based Interpretation |
| --- | --- | --- | --- | --- | --- |
| Headline CPI month-over-month inflation rate | 0.07 | percent | 0.5 pp vs prior | 2026-07-01 | Higher reading increases macro pressure. |
| Headline CPI year-over-year inflation rate | 3.54 | percent | -0.19 pp vs prior | 2026-07-01 | Lower reading eases macro pressure. |
| Core CPI month-over-month inflation rate | 0.22 | percent | 0.23 pp vs prior | 2026-07-01 | Higher reading increases macro pressure. |
| Core CPI year-over-year inflation rate | 2.79 | percent | -0.02 pp vs prior | 2026-07-01 | Lower reading eases macro pressure. |
| Headline CPI year-over-year inflation rate | 3.52 | percent | -0.36 pp vs prior | 2026-07-01 | Lower reading eases macro pressure. |
| Core CPI year-over-year inflation rate | 2.67 | percent | -0.19 pp vs prior | 2026-07-01 | Lower reading eases macro pressure. |
| Headline PCE Price Index month-over-month inflation rate | -0.11 | percent | -0.57 pp vs prior | 2026-06-01 | Lower reading eases macro pressure. |
| Headline PCE Price Index year-over-year inflation rate | 3.67 | percent | -0.41 pp vs prior | 2026-06-01 | Lower reading eases macro pressure. |
| Core PCE Price Index month-over-month inflation rate | 0.13 | percent | -0.2 pp vs prior | 2026-06-01 | Lower reading eases macro pressure. |
| Core PCE Price Index year-over-year inflation rate | 3.29 | percent | -0.14 pp vs prior | 2026-06-01 | Lower reading eases macro pressure. |
| Headline PPI Final Demand month-over-month inflation rate | -0.1 | percent | -0.07 pp vs prior | 2026-07-01 | Lower reading eases macro pressure. |
| Headline PPI Final Demand year-over-year inflation rate | 4.69 | percent | -0.85 pp vs prior | 2026-07-01 | Lower reading eases macro pressure. |
| Core PPI Final Demand Less Foods and Energy month-over-month inflation rate | 0.24 | percent | -0.15 pp vs prior | 2026-07-01 | Lower reading eases macro pressure. |
| Core PPI Final Demand Less Foods and Energy year-over-year inflation rate | 4.16 | percent | -0.57 pp vs prior | 2026-07-01 | Lower reading eases macro pressure. |
| Consumer Price Index for All Urban Consumers | 332.81 | index 1982-1984=100 | 0.25 index pts vs prior | 2026-07-01 | Higher reading increases macro pressure. |
| Core CPI | 336.79 | index 1982-1984=100 | 0.72 index pts vs prior | 2026-07-01 | Higher reading increases macro pressure. |
| Personal Consumption Expenditures Price Index | 131.39 | index 2017=100 | -0.14 index pts vs prior | 2026-06-01 | Lower reading eases macro pressure. |
| Core PCE Price Index | 130.27 | index 2017=100 | 0.17 index pts vs prior | 2026-06-01 | Higher reading increases macro pressure. |
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
| Housing Starts | 1427.0 | thousands | 228.0 thousands vs prior | 2026-06-01 | Higher reading supports activity or liquidity. |
| New Privately-Owned Housing Units Authorized | 1374.0 | thousands | -36.0 thousands vs prior | 2026-06-01 | Lower reading signals softer activity or liquidity. |
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
| US dollar/Euro ECB reference exchange rate | 1.15 | USD | -0.0 USD vs prior | 2026-08-13 | EUR weakened versus this currency. |
| Japanese yen/Euro ECB reference exchange rate | 183.77 | JPY | 0.1 JPY vs prior | 2026-08-13 | EUR strengthened versus this currency. |
| Chinese yuan renminbi/Euro ECB reference exchange rate | 7.78 | CNY | -0.01 CNY vs prior | 2026-08-13 | EUR weakened versus this currency. |
| Australian dollar/Euro ECB reference exchange rate | 1.64 | AUD | 0.0 AUD vs prior | 2026-08-13 | EUR strengthened versus this currency. |

ABS Australia note: ABS rows are stored locally/Neon, but most series are dimension-coded; only curated series should be promoted into narrative report text.

## Sector and Theme Leadership

### Official Sector Strength

Supporting and detracting names are the top/bottom S&P 500 constituents by 20D return when constituent coverage is available; otherwise the report falls back to related ETFs.

| Rank | Sector | Score | Trend | Momentum | Stock Breadth | ETF Flow | Flow Reliability | 3M RS | Supporting / Leaders | Detracting / Laggards |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Cybersecurity | 68.7 | strong uptrend | positive | broad | 50.0 | 0.0 | 62.96 | CIBR | CIBR |
| 2 | Defense | 67.56 | strong uptrend | positive | broad | 50.0 | 0.0 | 57.75 | XAR | XAR |
| 3 | Grid Infrastructure | 66.72 | strong uptrend | neutral | broad | 50.0 | 0.0 | 49.05 | GRID | GRID |
| 4 | Healthcare | 66.34 | strong uptrend | positive | broad | 50.0 | 0.0 | 54.37 | VEEV, CRL, REGN | CVS, PODD, DVA |
| 5 | Industrials | 66.1 | strong uptrend | neutral | broad | 50.0 | 0.0 | 51.11 | LDOS, HII, ALLE | ROL, LII, CHRW |
| 6 | Energy | 65.96 | strong uptrend | neutral | broad | 50.0 | 0.0 | 50.27 | APA, MPC, PSX | TRGP, HAL, TPL |
| 7 | Technology | 65.49 | strong uptrend | neutral | broad | 50.0 | 0.0 | 51.68 | SMCI, ZBRA, WDAY | FICO, CDNS, NXPI |
| 8 | Financials | 62.91 | strong uptrend | positive | broad | 50.0 | 0.0 | 52.34 | ARES, GPN, APO | TROW, SPGI, MSCI |
| 9 | Consumer Staples | 61.59 | strong uptrend | neutral | broad | 50.0 | 0.0 | 45.88 | TGT, CLX, HSY | HRL, MO, MNST |
| 10 | Semiconductors | 57.1 | strong uptrend | neutral | weak | 50.0 | 0.0 | 51.7 | SOXX, SMH | SMH, SOXX |
| 11 | Consumer Discretionary | 56.05 | uptrend | neutral | broad | 50.0 | 0.0 | 47.0 | ABNB, GRMN, EXPE | TSLA, DECK, APTV |
| 12 | Nuclear | 55.5 | neutral | neutral | broad | 50.0 | 0.0 | 50.82 | NLR | NLR |
| 13 | Real Estate | 55.32 | strong uptrend | neutral | broad | 50.0 | 0.0 | 46.51 | DLR, CSGP, EQIX | UDR, REG, DOC |
| 14 | Crypto | 50.0 | neutral | neutral | mixed | 50.0 | 0.0 | 50.0 |  |  |
| 15 | Utilities | 34.65 | strong downtrend | neutral | weak | 50.0 | 0.0 | 43.97 | CEG, AWK, PCG | NI, EIX, NRG |

### Thematic Strength

| Rank | Theme | Score | Setup | ETF Flow | Flow Reliability | Dispersion | Price | News |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Small Caps | 60.9 | Positive setup | 50.0 | 0.0 | 0.0 | True | False |
| 2 | Cybersecurity | 60.39 | Positive setup | 50.0 | 0.0 | 25.61 | True | False |
| 3 | Healthcare Innovation | 59.56 | Positive setup | 50.0 | 0.0 | 11.95 | False | False |
| 4 | Energy | 59.47 | Positive setup | 50.0 | 0.0 | 1.59 | False | False |
| 5 | Defense | 59.25 | Positive setup | 50.0 | 0.0 | 16.07 | False | False |
| 6 | Financials | 57.96 | Positive setup | 50.0 | 0.0 | 10.64 | False | False |
| 7 | Semiconductors | 57.02 | Neutral / watchlist | 50.0 | 0.0 | 15.16 | False | False |
| 8 | AI Infrastructure | 56.52 | Neutral / watchlist | 50.0 | 0.0 | 26.16 | False | False |
| 9 | Quality Growth | 55.5 | Neutral / watchlist | 50.0 | 0.0 | 32.28 | False | False |
| 10 | Nuclear | 51.49 | Neutral / watchlist | 50.0 | 0.0 | 18.53 | False | False |
| 11 | Dividend Defensives | 51.12 | Neutral / watchlist | 50.0 | 0.0 | 7.21 | False | False |
| 12 | Grid Infrastructure | 48.41 | Neutral / watchlist | 50.0 | 0.0 | 17.92 | False | False |
| 13 | Crypto Infrastructure | 32.33 | Underperformance risk | 50.0 | 0.0 | 7.37 | False | False |

- Top 5 improving themes: Financials, Healthcare Innovation, Defense, Cybersecurity, Small Caps
- Top 5 deteriorating themes: Crypto Infrastructure, Nuclear, Energy, Grid Infrastructure, Quality Growth
- Strong news but weak price confirmation: none
- Strong price but weak news confirmation: Small Caps, Cybersecurity

### Sector / Theme Alignment

| Sector | Related Themes | Sector Score | Sector Signal | Theme Score | Theme Signal | Interpretation |
| --- | --- | --- | --- | --- | --- | --- |
| Cybersecurity | Cybersecurity | 68.7 | strong | 60.39 | positive | sector and theme confirmation |
| Defense | Defense | 67.56 | strong | 59.25 | positive | sector and theme confirmation |
| Grid Infrastructure | Grid Infrastructure | 66.72 | strong | 48.41 | mixed | sector stronger than related themes |
| Healthcare | Healthcare Innovation | 66.34 | strong | 59.56 | positive | sector and theme confirmation |
| Industrials | Defense, Grid Infrastructure | 66.1 | strong | 53.83 | mixed | sector stronger than related themes |
| Energy | Energy | 65.96 | strong | 59.47 | positive | sector and theme confirmation |
| Technology | AI Infrastructure, Semiconductors, Quality Growth | 65.49 | strong | 56.35 | positive | sector and theme confirmation |
| Financials | Financials | 62.91 | positive | 57.96 | positive | sector and theme confirmation |
| Consumer Staples | Dividend Defensives | 61.59 | positive | 51.12 | mixed | sector stronger than related themes |
| Semiconductors | AI Infrastructure, Semiconductors | 57.1 | positive | 56.77 | positive | sector and theme confirmation |
| Consumer Discretionary | Small Caps | 56.05 | positive | 60.9 | positive | sector and theme confirmation |
| Nuclear | Nuclear | 55.5 | positive | 51.49 | mixed | sector stronger than related themes |
| Real Estate | Dividend Defensives | 55.32 | positive | 51.12 | mixed | sector stronger than related themes |
| Crypto | Crypto Infrastructure | 50.0 | mixed | 32.33 | very weak | mixed confirmation |
| Utilities | Grid Infrastructure, Nuclear, Dividend Defensives | 34.65 | very weak | 50.34 | mixed | mixed confirmation |

## Three-Month Outperformance Setup

| Rank | Theme | Score | Classification | Drivers | Invalidation Triggers |
| --- | --- | --- | --- | --- | --- |
| 1 | Small Caps | 64.3 | Positive setup | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 2 | Healthcare Innovation | 63.25 | Positive setup | relative_strength_60d, trend_persistence, breadth, downside_volatility, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 3 | Financials | 62.64 | Positive setup | relative_strength_60d, trend_persistence, breadth, downside_volatility, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 4 | Cybersecurity | 62.12 | Positive setup | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 5 | Defense | 61.59 | Positive setup | relative_strength_20d, trend_persistence, breadth, downside_volatility, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 6 | Energy | 61.04 | Positive setup | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 7 | AI Infrastructure | 57.53 | Neutral / watchlist | trend_persistence, breadth | relative strength below SPY, breadth below 45%, news turns negative |
| 8 | Quality Growth | 56.97 | Neutral / watchlist | trend_persistence, breadth | relative strength below SPY, breadth below 45%, news turns negative |
| 9 | Semiconductors | 55.96 | Neutral / watchlist | trend_persistence, breadth | relative strength below SPY, breadth below 45%, news turns negative |
| 10 | Dividend Defensives | 54.69 | Neutral / watchlist | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 11 | Nuclear | 50.61 | Neutral / watchlist | relative_strength_20d | relative strength below SPY, breadth below 45%, news turns negative |
| 12 | Grid Infrastructure | 49.46 | Neutral / watchlist | downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |

## Breadth and Participation

- Above 50DMA: `76.67%`
- Above 200DMA: `76.27%`
- Positive 20D return: `81.67%`

## Volatility and Risk Signals

- VIX close=14.63 pct_chg=0.55

## News Analytics

- Sentiment counts: {'positive': 36, 'negative': 30, 'neutral': 14}
- News confirmation score: `53.75`

### Top Market-Moving Headlines

**1. CNBC Daily Open: Middle East tensions send oil higher while Iran-U.S. tensions escalate**
- Source: CNBC Top News
- Importance / impact: High / Positive
- Relevance / horizon: macro / short-term
- Affected assets: CRUDE.OIL, CNBC, U.S, oil_prices, geopolitical_risk
- Score: `48.45`
- Investment implication: Macro-relevant positive signal; use as context for rates, volatility, and index confirmation over the short-term.

**2. Workday’s stock sees a record surge. Could a buyout spark a software revival?**
- Source: MarketWatch Top Stories
- Importance / impact: Medium / Positive
- Relevance / horizon: single_name / short-term
- Affected assets: HR, acquisition, software
- Score: `43.88`
- Investment implication: Single-name positive signal; low weight unless it maps to a broader sector or theme.

**3. Tariff refunds have begun rolling in to big U.S. companies—in some cases providing a solid boost to earnings**
- Source: Dow Jones Economy
- Importance / impact: Medium / Positive
- Relevance / horizon: macro / short-term
- Affected assets: AAPL, NKE, FDX, U.S, economic policy
- Score: `43.35`
- Investment implication: Macro-relevant positive signal; use as context for rates, volatility, and index confirmation over the short-term.

**4. Tariff Refunds Are Here—and Turbocharging Earnings**
- Source: Dow Jones US Business
- Importance / impact: Medium / Positive
- Relevance / horizon: macro / short-term
- Affected assets: tariff refunds, company earnings
- Score: `43.03`
- Investment implication: Macro-relevant positive signal; use as context for rates, volatility, and index confirmation over the short-term.

**5. These charts show why stocks keep rallying. Profit margins are the highest on record**
- Source: CNBC Markets
- Importance / impact: Medium / Positive
- Relevance / horizon: sector_theme / short-term
- Affected assets: Earnings, Profit Margins
- Score: `41.99`
- Investment implication: Theme or sector positive signal; requires price and volume confirmation before affecting rankings.

**6. Cerebras stock plunges 14% after second earnings report following IPO**
- Source: CNBC Business
- Importance / impact: Low / Negative
- Relevance / horizon: single_name / short-term
- Affected assets: Ceresb, IPO, AI
- Score: `33.15`
- Investment implication: Single-name negative signal; low weight unless it maps to a broader sector or theme.

**7. Applied Materials Posts Higher Profit, Revenue on Continued AI Demand**
- Source: Dow Jones US Business
- Importance / impact: Low / Positive
- Relevance / horizon: single_name / short-term
- Affected assets: AMAT, AI, semiconductor
- Score: `32.91`
- Investment implication: Single-name positive signal; low weight unless it maps to a broader sector or theme.

**8. The Iran war risks bringing the G7's fastest-growing economy to a halt**
- Source: CNBC Economy
- Importance / impact: Low / Negative
- Relevance / horizon: single_name / short-term
- Affected assets: U.K, Geopolitical Risk, Energy Prices
- Score: `29.84`
- Investment implication: Single-name negative signal; low weight unless it maps to a broader sector or theme.

**9. Adyen Shares Jump as Earnings Rise and Growth Accelerates**
- Source: Dow Jones US Business
- Importance / impact: Low / Positive
- Relevance / horizon: single_name / short-term
- Affected assets: ADYEN.AS, earnings, growth, stock_performance
- Score: `29.52`
- Investment implication: Single-name positive signal; low weight unless it maps to a broader sector or theme.

**10. JD.com Profit, Revenue Beat Expectations as Food-Delivery Losses Narrow**
- Source: Dow Jones US Business
- Importance / impact: Low / Positive
- Relevance / horizon: single_name / short-term
- Affected assets: JD, e-commerce, food delivery
- Score: `27.97`
- Investment implication: Single-name positive signal; low weight unless it maps to a broader sector or theme.


### Headline Quality Checks

Noisy headline list: OpenAI loses revenue chief Denise Dresser, second 

## Positioning & Flow Dashboard

Positioning and flow data is used as confirmation only.

### Deferred Flow Sections

- Official ETF / fund flows: current report uses shares-outstanding-derived net fund flow estimates from free ETF metadata.
- Institutional Ownership: not available until SEC 13F ingestion is implemented.
- Grouped exposure flow reliability: use issuer coverage and availability status before treating ETF flow as confirmation.

## ETF Flows Analysis

- Market flow regime: `Mixed / Neutral`
- Market flow score: `50.0 / 100`
- Equity risk flow: `50.0`
- Credit risk flow: `50.0`
- Sector cyclicality flow: `50.0`
- Duration/liquidity flow: `50.0`
- Alternatives: `mixed alternative-asset demand`
- ETF flow reliability: `65.0 / 100`
- Dominant allocation direction: `risk demand`

### Core Flow Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVV | U.S. Broad Equity | -0.7 | 0.2 | 0.3 | -0.7 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Medium-term deterioration | 83.0 |
| ACWI | Global Equity | -1.8 | -1.3 | 0.0 | -0.8 | Up | Sell | Normal | Profit Taking | Slightly Bearish | Strong confirmation; Persistent selling | 87.0 |
| EFA | Developed Markets ex-U.S. | -0.5 | -0.1 | 0.0 | -0.7 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Medium-term deterioration; Persistent selling | 75.0 |
| IEMG | Emerging Markets | 0.2 | -0.1 | 0.2 | -0.2 | Up | Buy | Normal | Steady Accumulation | Risk-On | Strong confirmation; Persistent selling | 87.0 |
| IJH | U.S. Mid Cap | 0.6 | 1.0 | 0.8 | -0.6 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural accumulation; Strong sponsorship | 99.0 |
| IWM | U.S. Small Cap | -0.5 | -0.0 | 0.4 | -1.4 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural distribution | 79.0 |
| LQD | Investment-Grade Credit | -0.9 | 1.0 | 0.5 | -0.8 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Medium-term deterioration | 83.0 |
| HYG | High-Yield Credit | 2.1 | 1.2 | 0.6 | -0.8 | Flat | Buy | Normal | Quiet Accumulation | Improving | Strong confirmation; Exceptional institutional buying | 100.0 |
| SGOV | Treasury Bills / Cash | -0.6 | -1.0 | 0.9 | 0.1 | Flat | Neutral | Normal | Neutral | Neutral | Medium-term recovery; Strong sponsorship | 95.0 |
| SHY | Short-Duration Treasuries | -0.7 | -0.1 | 0.3 | -1.2 | Flat | Neutral | Normal | Neutral | Neutral | Medium-term deterioration | 83.0 |
| IEF | Intermediate-Duration Treasuries | -3.9 | -2.5 | 0.6 | -0.4 | Flat | Sell | Normal | Quiet Distribution | Weakening | Strong confirmation; Exceptional institutional selling | 87.0 |
| TLT | Long-Duration Treasuries | 2.0 | 2.7 | 0.6 | -0.5 | Down | Buy | Normal | Contrarian Buying | Watch | Strong confirmation; Exceptional institutional buying | 100.0 |
| GLD | Gold | 2.4 | 2.1 | 0.6 | 1.0 | Up | Buy | Normal | Steady Accumulation | Risk-On | Strong confirmation; Exceptional institutional buying | 100.0 |
| IBIT | Bitcoin | 0.7 | -1.2 | 0.7 | -1.1 | Down | Buy | Normal | Contrarian Buying | Watch | Medium-term recovery | 87.0 |

### Sector Flow Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| XLC | Communication Services | 0.1 | -0.6 | 0.3 | -0.4 | Flat | Neutral | Normal | Neutral | Neutral | Structural distribution | 79.0 |
| XLY | Consumer Discretionary | 1.0 | 1.8 | 0.6 | -1.5 | Flat | Neutral | Normal | Neutral | Neutral | Structural accumulation | 91.0 |
| XLP | Consumer Staples | 2.0 | 2.1 | 0.6 | -1.5 | Flat | Buy | Normal | Quiet Accumulation | Improving | Strong confirmation; Exceptional institutional buying | 100.0 |
| XLE | Energy | -0.4 | -0.9 | 0.4 | -1.2 | Up | Buy | Normal | Steady Accumulation | Risk-On | Tactical rebound inside structural distribution | 83.0 |
| XLF | Financials | 1.0 | 1.8 | 0.5 | -1.9 | Up | Sell | Low | Weak Distribution | Neutral | Tactical profit-taking inside structural accumulation | 83.0 |
| XLV | Health Care | 1.1 | 1.2 | 0.6 | -1.2 | Up | Buy | Normal | Steady Accumulation | Risk-On | Strong confirmation | 95.0 |
| XLI | Industrials | -0.1 | 1.9 | 0.5 | -1.8 | Up | Neutral | Low | Fragile Rally | Low Confidence | Structural accumulation | 91.0 |
| XLK | Information Technology | -0.1 | -0.9 | 0.6 | -1.2 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Medium-term recovery | 87.0 |
| XLB | Materials | -0.8 | -0.1 | 0.5 | -0.6 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural accumulation | 91.0 |
| XLRE | Real Estate | 0.2 | 1.4 | 0.5 | -0.3 | Flat | Neutral | Normal | Neutral | Neutral | Structural accumulation | 91.0 |
| XLU | Utilities | -0.1 | 0.8 | 0.4 | -0.9 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural accumulation | 91.0 |

### Subsector PFV Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ITA | Aerospace and Defense | 0.4 | 0.4 | 0.4 | -1.7 | Up | Buy | Low | Quiet Accumulation | Mild Risk-On | Medium-term recovery | 87.0 |
| SOXX | Semiconductors | -1.7 | -0.0 | 0.4 | -0.8 | Flat | Sell | Normal | Quiet Distribution | Weakening | Medium-term deterioration | 83.0 |
| SMH | Semiconductors | -0.1 | -0.0 | 0.5 | -0.8 | Flat | Neutral | Normal | Neutral | Neutral | Structural accumulation | 91.0 |
| CIBR | Cybersecurity | 0.8 | 1.5 | 0.6 | -0.9 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural accumulation | 91.0 |

### Material Flow Divergences

| Severity | Type | Primary | Comparison | Interpretation |
| --- | --- | --- | --- | --- |
| medium | related_subsector_divergence | XLI | ITA | defense-specific demand differs from broad industrials |
| medium | related_subsector_divergence | XLK | SOXX | technology differs from semiconductors |
| high | close_substitute_divergence | GLD | IAU | primary representative differs from close substitute |
| high | close_substitute_divergence | HYG | JNK | primary representative differs from close substitute |
| high | close_substitute_divergence | IWF | IVW | primary representative differs from close substitute |
| high | close_substitute_divergence | IWD | IVE | primary representative differs from close substitute |


## Contradiction / Audit Flags

No contradiction flags were triggered by current deterministic rules.

## Data Quality Notes

- Technical rows loaded: `60`
- S&P 500 constituent technical rows loaded: `503`
- Macro rows loaded: `49`
- Live macro rows used: `2`
- Economic rows loaded: `113`
- News rows loaded: `80`
- Positioning/flow rows loaded: `30`

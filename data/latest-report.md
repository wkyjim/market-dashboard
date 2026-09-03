# Rule-Based Institutional Market Update

Generated at: 3 September 2026, 21:08:32 (HKT)
Window: 24h

## Executive Dashboard

- Regime score: **62.79 / 100** (Mild Risk-On)
- US equity strength: **68.66 / 100** (constructive)
- Evidence quality: **86.5 / 100**
- ETF flow contribution: **45.91 / 100**, reliability **65.91 / 100**
- Breadth: **healthy**; above 50DMA `51.67%`, above 200DMA `69.49%`
- Top sector score: **Cybersecurity** `65.1`
- Top theme score: **Energy** `58.14`

## Market Regime Score

| Metric | Value | Driver / Interpretation |
| --- | --- | --- |
| Overall regime | 62.79 | Mild Risk-On |
| equity_trend | 71.25 | risk-on support; Core equity ETFs versus moving averages. |
| equity_momentum | 54.24 | neutral / mixed; 5D/20D/60D return momentum across SPY, QQQ, IWM, and SMH. |
| market_breadth | 67.61 | risk-on support; Participation breadth from tracked equity/ETF rows. |
| volatility | 80.0 | risk-on support; VIX level and change; higher score means calmer volatility conditions. |
| rates_yield_curve | 58.0 | mild risk-on support; Treasury yield pressure and curve shape; higher score means less rates pressure. |
| credit_proxy | 50.0 | neutral / mixed; Credit-market proxy; currently neutral when no direct spread signal is available. |
| dollar_fx | 57.76 | mild risk-on support; Dollar move; higher score means less USD tightening pressure. |
| commodity_confirmation | 63.0 | mild risk-on support; Copper, silver, oil, and gold mix; higher score means better cyclical confirmation. |
| etf_flow | 47.3 | neutral / mixed; Grouped ETF flow contribution adjusted for reliability. |
| news_confirmation | 82.5 | risk-on support; Weighted headline/news confirmation score. |
| Positive contributors |  | news_confirmation=82.5, volatility=80.0, equity_trend=71.25, market_breadth=67.61, commodity_confirmation=63.0 |
| Negative contributors |  | none |

## US Equity Strength Score

| Component | Score |
| --- | --- |
| indices_above_moving_averages | 71.25 |
| sp500_trend | 100.0 |
| nasdaq_trend | 75.0 |
| russell_participation | 55.0 |
| returns_momentum | 54.24 |
| rsi_zone | 62.5 |
| macd_confirmation | 70.0 |
| volume_confirmation | 50.0 |
| breadth | 67.61 |

## Evidence Quality / Confidence

- Confidence score: `86.5`
- Agreement ratio: `0.7`
- Contradiction count: `0`
- Missing indicators: none
- Warning flags: none

## Cross-Asset Confirmation

| Area | Signal | Interpretation |
| --- | --- | --- |
| Equities | S&P 500 rising; Nasdaq rising; Russell 2000 rising | Confirms risk appetite when broad indices rise together; weak small caps would narrow the signal. |
| Rates | 10Y Treasury falling; MOVE rising | Rising yields can pressure duration assets; falling MOVE supports calmer bond volatility. |
| Dollar | DXY proxy falling | A stronger dollar can tighten financial conditions and pressure commodities/emerging-market risk. |
| Credit | HYG stable | High-yield weakness would challenge equity risk-on confirmation. |
| Gold | Gold rising | Gold strength can indicate defensive demand, inflation hedging, or geopolitical concern. |
| Silver | Silver rising | Silver helps distinguish precious-metal demand from industrial/cyclical confirmation when data is available. |
| Copper | Copper rising | Copper strength supports cyclical growth confirmation; weakness would dilute risk-on breadth. |
| Oil | WTI crude rising | Oil spikes can be inflationary risk; falling oil can ease cost pressure but may also flag demand softness. |
| Volatility | VIX falling | Falling VIX supports risk appetite; a volatility spike would reduce confidence in broad risk-on. |

### Macro Snapshot

Live macro rows are intraday snapshots from `public.macro_live`; closed rows are official stored rows from `public.macro`.

| Symbol | Name | Close | Pct Chg | Market Date | Status |
| --- | --- | --- | --- | --- | --- |
| ^GSPC | S&P 500 | 7666.6 | 0.46 | 2026-09-02 | closed |
| ^IXIC | NASDAQ Composite | 26217.83 | 0.45 | 2026-09-02 | closed |
| ^RUT | Russell 2000 Index | 2953.17 | 1.13 | 2026-09-02 | closed |
| ^VIX | CBOE Volatility Index | 15.12 | -0.53 | 2026-09-03 | live as of 3 September 2026, 21:01:57 (HKT) |
| ^SKEW | CBOE SKEW Index | 144.12 | -3.42 | 2026-09-02 | closed |
| ^MOVE | ICE BofA MOVE Index | 79.71 | 2.35 | 2026-09-02 | closed |
| US2YT=X | United States 2-Year Treasury Yield | 4.32 | -1.61 | 2026-09-03 | live as of 3 September 2026, 21:01:57 (HKT) |
| US3YT=X | United States 3-Year Treasury Yield | 4.38 | -1.54 | 2026-09-03 | live as of 3 September 2026, 21:01:57 (HKT) |
| US5YT=X | United States 5-Year Treasury Yield | 4.49 | -1.45 | 2026-09-03 | live as of 3 September 2026, 21:01:57 (HKT) |
| US7YT=X | United States 7-Year Treasury Yield | 4.6 | -1.3 | 2026-09-03 | live as of 3 September 2026, 21:01:57 (HKT) |
| US10YT=X | United States 10-Year Treasury Yield | 4.74 | -1.08 | 2026-09-03 | live as of 3 September 2026, 21:01:57 (HKT) |
| US20YT=X | United States 20-Year Treasury Yield | 5.23 | -0.87 | 2026-09-03 | live as of 3 September 2026, 21:01:57 (HKT) |
| US30YT=X | United States 30-Year Treasury Yield | 5.23 | -0.75 | 2026-09-03 | live as of 3 September 2026, 21:01:57 (HKT) |
| HK50 | Hang Seng Futures | 25145.0 | -0.86 | 2026-09-03 | closed |
| KOR200c1 | KOSPI 200 Futures | 1043.2 | 1.37 | 2026-09-02 | closed |
| CIHc1 | SSE 50 Futures | 2900.2 | -0.98 | 2026-09-02 | closed |
| HYG | iShares iBoxx High Yield Corporate Bond ETF | 79.11 | 0.01 | 2026-09-02 | closed |
| LQD | iShares iBoxx Investment Grade Corporate Bond ETF | 105.35 | 0.12 | 2026-09-02 | closed |
| JNK | SPDR Bloomberg High Yield Bond ETF | 95.21 | 0.0 | 2026-09-02 | closed |
| RSP | Invesco S&P 500 Equal Weight ETF | 218.6 | 0.46 | 2026-09-02 | closed |
| IWF | iShares Russell 1000 Growth ETF | 121.81 | 0.49 | 2026-09-02 | closed |
| IWD | iShares Russell 1000 Value ETF | 257.08 | 0.44 | 2026-09-02 | closed |
| TLT | iShares 20+ Year Treasury Bond ETF | 81.95 | 0.1 | 2026-09-02 | closed |
| IEF | iShares 7-10 Year Treasury Bond ETF | 92.18 | 0.09 | 2026-09-02 | closed |
| SHY | iShares 1-3 Year Treasury Bond ETF | 81.64 | 0.06 | 2026-09-02 | closed |
| GC=F | Gold Future | 4531.5 | 3.78 | 2026-09-03 | live as of 3 September 2026, 21:01:57 (HKT) |
| SI=F | Silver Future | 66.99 | 3.5 | 2026-09-03 | live as of 3 September 2026, 21:01:57 (HKT) |
| CL=F | WTI Crude Oil Future | 91.85 | 0.92 | 2026-09-03 | live as of 3 September 2026, 21:01:57 (HKT) |
| HG=F | Copper Future | 6.67 | 2.53 | 2026-09-03 | live as of 3 September 2026, 21:01:57 (HKT) |

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
| Information Technology | 73 | 45.21 | 69.44 | 82.19 | 72.99 | 13.83 | very high | SMCI, ZBRA, WDAY | FICO, CDNS, NXPI |
| Consumer Staples | 34 | 54.55 | 65.62 | 58.82 | 64.2 | 9.97 | very high | TGT, CLX, HSY | HRL, MO, MNST |
| Industrials | 83 | 30.49 | 53.16 | 62.65 | 59.1 | 9.43 | very high | LDOS, HII, ALLE | ROL, LII, CHRW |
| Health Care | 59 | 77.97 | 79.66 | 76.27 | 51.44 | 8.44 | very high | VEEV, CRL, REGN | CVS, PODD, DVA |
| Communication Services | 24 | 65.22 | 56.52 | 70.83 | 45.44 | 11.1 | very high | CHTR, FOXA, FOX | RDDT, TTD, APP |
| Consumer Discretionary | 47 | 38.3 | 40.43 | 57.45 | 42.28 | 9.32 | very high | ABNB, GRMN, EXPE | TSLA, DECK, APTV |
| Materials | 25 | 64.0 | 76.0 | 64.0 | 38.25 | 8.72 | very high | NEM, NUE, FCX | CRH, LIN, CTVA |
| Energy | 21 | 95.24 | 85.71 | 71.43 | 33.27 | 8.3 | very high | APA, MPC, PSX | TRGP, HAL, TPL |
| Financials | 76 | 68.49 | 87.14 | 64.47 | 28.88 | 6.1 | very high | ARES, GPN, APO | TROW, SPGI, MSCI |
| Real Estate | 30 | 17.24 | 65.52 | 30.0 | 20.62 | 4.88 | very high | DLR, CSGP, EQIX | UDR, REG, DOC |
| Utilities | 31 | 9.68 | 22.58 | 6.45 | 20.47 | 3.79 | very high | CEG, AWK, PCG | NI, EIX, NRG |

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
| US dollar/Euro ECB reference exchange rate | 1.16 | USD | -0.0 USD vs prior | 2026-09-02 | EUR weakened versus this currency. |
| Japanese yen/Euro ECB reference exchange rate | 184.78 | JPY | -0.85 JPY vs prior | 2026-09-02 | EUR weakened versus this currency. |
| Chinese yuan renminbi/Euro ECB reference exchange rate | 7.78 | CNY | -0.01 CNY vs prior | 2026-09-02 | EUR weakened versus this currency. |
| Australian dollar/Euro ECB reference exchange rate | 1.62 | AUD | -0.0 AUD vs prior | 2026-09-02 | EUR weakened versus this currency. |

ABS Australia note: ABS rows are stored locally/Neon, but most series are dimension-coded; only curated series should be promoted into narrative report text.

## Sector and Theme Leadership

### Official Sector Strength

Supporting and detracting names are the top/bottom S&P 500 constituents by 20D return when constituent coverage is available; otherwise the report falls back to related ETFs.

| Rank | Sector | Score | Trend | Momentum | Stock Breadth | ETF Flow | Flow Reliability | 3M RS | Supporting / Leaders | Detracting / Laggards |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Cybersecurity | 65.1 | strong uptrend | positive | broad | 50.0 | 0.0 | 62.96 | CIBR | CIBR |
| 2 | Energy | 64.98 | strong uptrend | neutral | broad | 40.23 | 65.0 | 50.27 | APA, MPC, PSX | TRGP, HAL, TPL |
| 3 | Healthcare | 64.27 | strong uptrend | positive | broad | 29.23 | 65.0 | 54.37 | VEEV, CRL, REGN | CVS, PODD, DVA |
| 4 | Consumer Staples | 61.59 | strong uptrend | neutral | broad | 50.0 | 0.0 | 45.88 | TGT, CLX, HSY | HRL, MO, MNST |
| 5 | Financials | 61.42 | strong uptrend | positive | broad | 35.09 | 65.0 | 52.34 | ARES, GPN, APO | TROW, SPGI, MSCI |
| 6 | Technology | 60.45 | strong uptrend | neutral | mixed | 43.3 | 65.0 | 51.68 | SMCI, ZBRA, WDAY | FICO, CDNS, NXPI |
| 7 | Nuclear | 55.5 | neutral | neutral | broad | 50.0 | 0.0 | 50.82 | NLR | NLR |
| 8 | Crypto | 51.62 | neutral | neutral | mixed | 66.24 | 65.0 | 50.0 |  |  |
| 9 | Semiconductors | 50.82 | neutral | neutral | weak | 41.57 | 65.0 | 51.7 | SOXX, SMH | SMH, SOXX |
| 10 | Grid Infrastructure | 50.02 | downtrend | neutral | weak | 50.0 | 0.0 | 49.05 | GRID | GRID |
| 11 | Industrials | 49.4 | downtrend | neutral | weak | 50.0 | 0.0 | 51.11 | LDOS, HII, ALLE | ROL, LII, CHRW |
| 12 | Defense | 44.56 | strong downtrend | positive | weak | 50.0 | 0.0 | 57.75 | XAR | XAR |
| 13 | Real Estate | 43.0 | downtrend | neutral | weak | 57.81 | 65.0 | 46.51 | DLR, CSGP, EQIX | UDR, REG, DOC |
| 14 | Consumer Discretionary | 39.35 | strong downtrend | neutral | weak | 50.0 | 0.0 | 47.0 | ABNB, GRMN, EXPE | TSLA, DECK, APTV |
| 15 | Utilities | 34.65 | strong downtrend | neutral | weak | 50.0 | 0.0 | 43.97 | CEG, AWK, PCG | NI, EIX, NRG |

### Thematic Strength

| Rank | Theme | Score | Setup | ETF Flow | Flow Reliability | Dispersion | Price | News |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Energy | 58.14 | Positive setup | 40.23 | 65.0 | 1.59 | False | False |
| 2 | Financials | 56.47 | Positive setup | 35.09 | 65.0 | 10.64 | False | False |
| 3 | Cybersecurity | 56.39 | Neutral / watchlist | 50.0 | 0.0 | 25.61 | False | False |
| 4 | Quality Growth | 55.8 | Neutral / watchlist | 52.99 | 65.0 | 32.28 | False | False |
| 5 | Healthcare Innovation | 55.48 | Positive setup | 29.23 | 65.0 | 11.95 | False | False |
| 6 | AI Infrastructure | 54.43 | Neutral / watchlist | 41.57 | 65.0 | 26.16 | False | False |
| 7 | Semiconductors | 52.91 | Neutral / watchlist | 41.57 | 65.0 | 15.16 | False | False |
| 8 | Dividend Defensives | 51.36 | Neutral / watchlist | 52.4 | 65.0 | 7.21 | False | False |
| 9 | Small Caps | 50.85 | Neutral / watchlist | 49.52 | 65.0 | 0.0 | False | False |
| 10 | Nuclear | 48.99 | Neutral / watchlist | 50.0 | 0.0 | 18.53 | False | False |
| 11 | Defense | 47.25 | Neutral / watchlist | 50.0 | 0.0 | 16.07 | False | False |
| 12 | Grid Infrastructure | 44.41 | Weak setup | 50.0 | 0.0 | 17.92 | False | False |
| 13 | Crypto Infrastructure | 43.95 | Weak setup | 66.24 | 65.0 | 7.37 | False | False |

- Top 5 improving themes: Financials, Healthcare Innovation, Defense, Cybersecurity, Small Caps
- Top 5 deteriorating themes: Crypto Infrastructure, Nuclear, Energy, Grid Infrastructure, Quality Growth
- Strong news but weak price confirmation: none
- Strong price but weak news confirmation: none

### Sector / Theme Alignment

| Sector | Related Themes | Sector Score | Sector Signal | Theme Score | Theme Signal | Interpretation |
| --- | --- | --- | --- | --- | --- | --- |
| Cybersecurity | Cybersecurity | 65.1 | strong | 56.39 | positive | sector and theme confirmation |
| Energy | Energy | 64.98 | positive | 58.14 | positive | sector and theme confirmation |
| Healthcare | Healthcare Innovation | 64.27 | positive | 55.48 | positive | sector and theme confirmation |
| Consumer Staples | Dividend Defensives | 61.59 | positive | 51.36 | mixed | sector stronger than related themes |
| Financials | Financials | 61.42 | positive | 56.47 | positive | sector and theme confirmation |
| Technology | AI Infrastructure, Semiconductors, Quality Growth | 60.45 | positive | 54.38 | mixed | sector stronger than related themes |
| Nuclear | Nuclear | 55.5 | positive | 48.99 | mixed | sector stronger than related themes |
| Crypto | Crypto Infrastructure | 51.62 | mixed | 43.95 | weak | mixed confirmation |
| Semiconductors | AI Infrastructure, Semiconductors | 50.82 | mixed | 53.67 | mixed | mixed confirmation |
| Grid Infrastructure | Grid Infrastructure | 50.02 | mixed | 44.41 | weak | mixed confirmation |
| Industrials | Defense, Grid Infrastructure | 49.4 | mixed | 45.83 | mixed | mixed confirmation |
| Defense | Defense | 44.56 | weak | 47.25 | mixed | mixed confirmation |
| Real Estate | Dividend Defensives | 43.0 | weak | 51.36 | mixed | mixed confirmation |
| Consumer Discretionary | Small Caps | 39.35 | weak | 50.85 | mixed | mixed confirmation |
| Utilities | Grid Infrastructure, Nuclear, Dividend Defensives | 34.65 | very weak | 48.25 | mixed | mixed confirmation |

## Three-Month Outperformance Setup

| Rank | Theme | Score | Classification | Drivers | Invalidation Triggers |
| --- | --- | --- | --- | --- | --- |
| 1 | Energy | 63.05 | Positive setup | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 2 | Financials | 62.68 | Positive setup | relative_strength_60d, trend_persistence, breadth, downside_volatility, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 3 | Healthcare Innovation | 60.72 | Positive setup | relative_strength_60d, trend_persistence, breadth, downside_volatility, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 4 | Quality Growth | 56.91 | Neutral / watchlist | trend_persistence, breadth | relative strength below SPY, breadth below 45%, news turns negative |
| 5 | Cybersecurity | 56.44 | Neutral / watchlist | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 6 | AI Infrastructure | 55.9 | Neutral / watchlist | trend_persistence, breadth | relative strength below SPY, breadth below 45%, news turns negative |
| 7 | Dividend Defensives | 54.69 | Neutral / watchlist | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 8 | Small Caps | 51.35 | Neutral / watchlist | downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 9 | Semiconductors | 51.03 | Neutral / watchlist | news_acceleration | relative strength below SPY, breadth below 45%, news turns negative |
| 10 | Nuclear | 47.39 | Neutral / watchlist | relative_strength_20d | relative strength below SPY, breadth below 45%, news turns negative |
| 11 | Defense | 45.99 | Neutral / watchlist | relative_strength_20d, downside_volatility, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 12 | Grid Infrastructure | 44.3 | Weak setup | downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |

## Breadth and Participation

- Above 50DMA: `51.67%`
- Above 200DMA: `69.49%`
- Positive 20D return: `81.67%`

## Volatility and Risk Signals

- VIX close=15.12 pct_chg=-0.53

## News Analytics

- Sentiment counts: {'positive': 66, 'negative': 14, 'neutral': 0}
- News confirmation score: `82.5`

### Top Market-Moving Headlines

**1. Snowflake is ripping after its earnings report. Two analysts say there's more upside to come**
- Source: CNBC Markets
- Importance / impact: High / Positive
- Relevance / horizon: macro / short-term
- Affected assets: SNFL, earnings report, performance, analyst opinion
- Score: `72.67`
- Investment implication: Macro-relevant positive signal; use as context for rates, volatility, and index confirmation over the short-term.

**2. Brent oil price above $95 as Iran retaliates with strikes on U.S. Gulf allies**
- Source: CNBC Top News
- Importance / impact: High / Positive
- Relevance / horizon: macro / short
- Affected assets: U.S, geo-political
- Score: `61.77`
- Investment implication: Macro-relevant positive signal; use as context for rates, volatility, and index confirmation over the short.

**3. Chevron to expand in Venezuela operations, doubling production through $7 billion investment**
- Source: CNBC Top News
- Importance / impact: High / Positive
- Relevance / horizon: macro / medium-term
- Affected assets: Chevron, U.S, energy, investment, production
- Score: `61.77`
- Investment implication: Macro-relevant positive signal; use as context for rates, volatility, and index confirmation over the medium-term.

**4. Thyme Care raises $125 million, pushing cancer care startup's valuation above $2 billion**
- Source: CNBC Markets
- Importance / impact: Medium / Positive
- Relevance / horizon: sector_theme / short-term
- Affected assets: venture capital, healthcare, AI
- Score: `52.51`
- Investment implication: Theme or sector positive signal; requires price and volume confirmation before affecting rankings.

**5. Chevron to Invest $7 Billion in Venezuela, Doubling Production**
- Source: Dow Jones US Business
- Importance / impact: High / Positive
- Relevance / horizon: macro / short-term
- Affected assets: Chevron, ENI, U.S, oil-and-gas, investment
- Score: `48.77`
- Investment implication: Macro-relevant positive signal; use as context for rates, volatility, and index confirmation over the short-term.

**6. 10-year U.S. Treasury yield hits highest level since November 2023**
- Source: CNBC Markets
- Importance / impact: High / Negative
- Relevance / horizon: macro / short-term
- Affected assets: U.S, bond market, inflation, interest rates
- Score: `48.45`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the short-term.

**7. Shipping stocks at a crossroads amid their best rally in decades**
- Source: CNBC Technology
- Importance / impact: High / Positive
- Relevance / horizon: macro / short-term
- Affected assets: A, shipping, trade, geopolitical
- Score: `45.9`
- Investment implication: Macro-relevant positive signal; use as context for rates, volatility, and index confirmation over the short-term.

**8. A jittery Treasury market and the prospect of Fed rate increases risk making life more expensive for already cost-pressured Americans**
- Source: Dow Jones Economy
- Importance / impact: Medium / Negative
- Relevance / horizon: macro / short-term
- Affected assets: A, Treasury market, Fed rate increases
- Score: `43.35`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the short-term.

**9. Snowflake’s stock soars as the company blows away estimates with its AI-fueled forecast**
- Source: MarketWatch Top Stories
- Importance / impact: Medium / Positive
- Relevance / horizon: single_name / short-term
- Affected assets: SNFL, AI, data management
- Score: `42.27`
- Investment implication: Single-name positive signal; low weight unless it maps to a broader sector or theme.

**10. Global bond rout gathers pace as inflation fears mount**
- Source: CNBC Top News
- Importance / impact: Medium / Negative
- Relevance / horizon: sector_theme / short-term
- Affected assets: inflation, bond market
- Score: `41.18`
- Investment implication: Theme or sector negative signal; requires price and volume confirmation before affecting rankings.


### Headline Quality Checks

Noisy headline list: Stock market today: Dow, S&P 500, Nasdaq drop as o

## Positioning & Flow Dashboard

Positioning and flow data is used as confirmation only.

### Deferred Flow Sections

- Official ETF / fund flows: current report uses shares-outstanding-derived net fund flow estimates from free ETF metadata.
- Institutional Ownership: not available until SEC 13F ingestion is implemented.
- Grouped exposure flow reliability: use issuer coverage and availability status before treating ETF flow as confirmation.

## ETF Flows Analysis

- Market flow regime: `Mixed / Neutral`
- Market flow score: `49.1 / 100`
- Equity risk flow: `51.0`
- Credit risk flow: `37.6`
- Sector cyclicality flow: `49.0`
- Duration/liquidity flow: `51.1`
- Alternatives: `barbell demand`
- ETF flow reliability: `65.9 / 100`
- Dominant allocation direction: `defensive demand`

### Core Flow Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVV | U.S. Broad Equity | -0.8 | -0.6 | 0.1 | 0.3 | Flat | Neutral | High | High-Turnover Consolidation | Transition | Medium-term deterioration; Persistent selling | 75.0 |
| ACWI | Global Equity | -0.7 | -1.1 | 0.0 | -0.8 | Flat | Neutral | Normal | Neutral | Neutral | Mixed or neutral flow structure; Persistent selling | 77.0 |
| EFA | Developed Markets ex-U.S. | -0.1 | -0.1 | 0.0 | -1.3 | Flat | Neutral | Normal | Neutral | Neutral | Mixed or neutral flow structure; Persistent selling | 77.0 |
| IEMG | Emerging Markets | 0.0 | 0.1 | 0.2 | -0.3 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural accumulation; Persistent selling | 83.0 |
| IJH | U.S. Mid Cap | 1.6 | 1.9 | 0.9 | -0.6 | Down | Buy | Normal | Contrarian Buying | Watch | Strong confirmation; Strong sponsorship | 100.0 |
| IWM | U.S. Small Cap | 0.5 | 0.6 | 0.3 | -0.2 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Medium-term recovery | 87.0 |
| LQD | Investment-Grade Credit | -0.8 | 0.2 | 0.6 | -0.4 | Down | Sell | Normal | Persistent Distribution | Risk-Off | Medium-term deterioration; Exceptional institutional selling | 75.0 |
| HYG | High-Yield Credit | -1.9 | -0.7 | 0.2 | 0.2 | Flat | Sell | Normal | Quiet Distribution | Weakening | Strong confirmation; Persistent selling | 87.0 |
| SGOV | Treasury Bills / Cash | 0.4 | -1.4 | 0.9 | 0.2 | Flat | Buy | Normal | Quiet Accumulation | Improving | Medium-term recovery; Exceptional institutional buying, Strong sponsorship | 100.0 |
| SHY | Short-Duration Treasuries | 1.2 | 0.3 | 0.6 | -0.5 | Flat | Buy | Normal | Quiet Accumulation | Improving | Strong confirmation; Exceptional institutional buying | 100.0 |
| IEF | Intermediate-Duration Treasuries | -2.7 | -1.8 | 0.5 | -0.1 | Down | Sell | Normal | Persistent Distribution | Risk-Off | Strong confirmation; Exceptional institutional selling | 87.0 |
| TLT | Long-Duration Treasuries | 2.5 | 2.8 | 0.7 | -0.5 | Down | Buy | Normal | Contrarian Buying | Watch | Strong confirmation; Exceptional institutional buying | 100.0 |
| GLD | Gold | 2.6 | 3.4 | 0.7 | 1.8 | Flat | Buy | High | Strong Accumulation | Early Bullish | Strong confirmation; Exceptional institutional buying | 100.0 |
| IBIT | Bitcoin | 1.6 | 0.4 | 0.7 | -0.8 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural accumulation | 91.0 |

### Sector Flow Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| XLC | Communication Services | 1.1 | -0.7 | 0.4 | -0.6 | Down | Buy | Normal | Contrarian Buying | Watch | Medium-term recovery | 87.0 |
| XLY | Consumer Discretionary | 0.8 | 1.9 | 0.4 | -0.8 | Down | Buy | Normal | Contrarian Buying | Watch | Strong confirmation; Exceptional institutional buying | 100.0 |
| XLP | Consumer Staples | -0.0 | 0.7 | 0.4 | -0.5 | Flat | Neutral | Normal | Neutral | Neutral | Structural distribution | 79.0 |
| XLE | Energy | -0.4 | -0.5 | 0.5 | 0.3 | Up | Buy | Normal | Steady Accumulation | Risk-On | Tactical rebound inside structural distribution | 83.0 |
| XLF | Financials | -1.7 | 0.1 | 0.3 | -0.1 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural distribution | 79.0 |
| XLV | Health Care | 0.3 | 1.3 | 0.6 | -0.8 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural accumulation | 91.0 |
| XLI | Industrials | -0.5 | 0.3 | 0.4 | 1.0 | Down | Neutral | High | Heavy Selling Pressure | Cautious | Structural accumulation | 91.0 |
| XLK | Information Technology | -0.6 | -1.0 | 0.5 | -0.6 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural distribution | 79.0 |
| XLB | Materials | -0.4 | -1.3 | 0.5 | 1.4 | Flat | Neutral | High | High-Turnover Consolidation | Transition | Medium-term recovery | 87.0 |
| XLRE | Real Estate | -1.2 | 0.6 | 0.2 | 1.0 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Medium-term deterioration; Persistent selling | 75.0 |
| XLU | Utilities | -0.3 | 0.6 | 0.3 | 2.3 | Down | Neutral | High | Heavy Selling Pressure | Cautious | Medium-term deterioration | 83.0 |

### Subsector PFV Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ITA | Aerospace and Defense | 0.2 | 0.5 | 0.3 | 0.5 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Medium-term recovery | 87.0 |
| SOXX | Semiconductors | -1.3 | -0.0 | 0.4 | -1.2 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Medium-term deterioration | 83.0 |
| SMH | Semiconductors | -0.9 | -2.6 | 0.4 | -0.8 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural distribution; Exceptional institutional selling | 71.0 |
| CIBR | Cybersecurity | 1.7 | 1.6 | 0.7 | 1.5 | Down | Buy | High | Aggressive Dip Buying | Recovery Candidate | Strong confirmation | 95.0 |

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
- Macro rows loaded: `49`
- Live macro rows used: `26`
- Economic rows loaded: `113`
- News rows loaded: `80`
- Positioning/flow rows loaded: `30`

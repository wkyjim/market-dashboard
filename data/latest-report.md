# Rule-Based Institutional Market Update

Generated at: 2 September 2026, 12:16:27 (HKT)
Window: 24h

## Executive Dashboard

- Regime score: **55.93 / 100** (Mild Risk-On)
- US equity strength: **68.7 / 100** (constructive)
- Evidence quality: **76.0 / 100**
- ETF flow contribution: **46.67 / 100**, reliability **66.88 / 100**
- Breadth: **healthy**; above 50DMA `51.67%`, above 200DMA `71.19%`
- Top sector score: **Cybersecurity** `68.7`
- Top theme score: **Cybersecurity** `58.39`

## Market Regime Score

| Metric | Value | Driver / Interpretation |
| --- | --- | --- |
| Overall regime | 55.93 | Mild Risk-On |
| equity_trend | 71.25 | risk-on support; Core equity ETFs versus moving averages. |
| equity_momentum | 54.24 | neutral / mixed; 5D/20D/60D return momentum across SPY, QQQ, IWM, and SMH. |
| market_breadth | 68.17 | risk-on support; Participation breadth from tracked equity/ETF rows. |
| volatility | 35.0 | risk-off pressure; VIX level and change; higher score means calmer volatility conditions. |
| rates_yield_curve | 58.0 | mild risk-on support; Treasury yield pressure and curve shape; higher score means less rates pressure. |
| credit_proxy | 50.0 | neutral / mixed; Credit-market proxy; currently neutral when no direct spread signal is available. |
| dollar_fx | 53.75 | neutral / mixed; Dollar move; higher score means less USD tightening pressure. |
| commodity_confirmation | 42.0 | mild risk-off pressure; Copper, silver, oil, and gold mix; higher score means better cyclical confirmation. |
| etf_flow | 47.77 | neutral / mixed; Grouped ETF flow contribution adjusted for reliability. |
| news_confirmation | 63.75 | mild risk-on support; Weighted headline/news confirmation score. |
| Positive contributors |  | equity_trend=71.25, market_breadth=68.17, news_confirmation=63.75 |
| Negative contributors |  | volatility=35.0, commodity_confirmation=42.0 |

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
| breadth | 68.17 |

## Evidence Quality / Confidence

- Confidence score: `76.0`
- Agreement ratio: `0.4`
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
| Gold | Gold falling | Gold strength can indicate defensive demand, inflation hedging, or geopolitical concern. |
| Silver | Silver falling | Silver helps distinguish precious-metal demand from industrial/cyclical confirmation when data is available. |
| Copper | Copper falling | Copper strength supports cyclical growth confirmation; weakness would dilute risk-on breadth. |
| Oil | WTI crude stable | Oil spikes can be inflationary risk; falling oil can ease cost pressure but may also flag demand softness. |
| Volatility | VIX rising | Falling VIX supports risk appetite; a volatility spike would reduce confidence in broad risk-on. |

### Macro Snapshot

Live macro rows are intraday snapshots from `public.macro_live`; closed rows are official stored rows from `public.macro`.

| Symbol | Name | Close | Pct Chg | Market Date | Status |
| --- | --- | --- | --- | --- | --- |
| ^GSPC | S&P 500 | 7631.47 | -0.71 | 2026-09-01 | closed |
| ^IXIC | NASDAQ Composite | 26099.77 | -1.03 | 2026-09-01 | closed |
| ^RUT | Russell 2000 Index | 2920.13 | -1.23 | 2026-09-01 | closed |
| ^VIX | CBOE Volatility Index | 16.34 | 9.52 | 2026-09-01 | closed |
| ^SKEW | CBOE SKEW Index | 149.23 | 0.47 | 2026-09-01 | closed |
| ^MOVE | ICE BofA MOVE Index | 77.88 | 3.39 | 2026-09-01 | closed |
| US2YT=X | United States 2-Year Treasury Yield | 4.4 | 0.23 | 2026-09-02 | live as of 2 September 2026, 12:01:48 (HKT) |
| US3YT=X | United States 3-Year Treasury Yield | 4.47 | 0.2 | 2026-09-02 | live as of 2 September 2026, 12:01:48 (HKT) |
| US5YT=X | United States 5-Year Treasury Yield | 4.56 | 0.11 | 2026-09-02 | live as of 2 September 2026, 12:01:48 (HKT) |
| US7YT=X | United States 7-Year Treasury Yield | 4.68 | 0.18 | 2026-09-02 | live as of 2 September 2026, 12:01:48 (HKT) |
| US10YT=X | United States 10-Year Treasury Yield | 4.81 | 0.21 | 2026-09-02 | live as of 2 September 2026, 12:01:48 (HKT) |
| US20YT=X | United States 20-Year Treasury Yield | 5.29 | 0.33 | 2026-09-02 | live as of 2 September 2026, 12:01:48 (HKT) |
| US30YT=X | United States 30-Year Treasury Yield | 5.28 | 0.29 | 2026-09-02 | live as of 2 September 2026, 12:01:48 (HKT) |
| HK50 | Hang Seng Futures | 25024.5 | -0.62 | 2026-09-02 | live as of 2 September 2026, 12:01:48 (HKT) |
| KOR200c1 | KOSPI 200 Futures | 1051.9 | -2.43 | 2026-09-01 | closed |
| CIHc1 | SSE 50 Futures | 2929.0 | 0.45 | 2026-09-01 | closed |
| HYG | iShares iBoxx High Yield Corporate Bond ETF | 79.1 | -0.89 | 2026-09-01 | closed |
| LQD | iShares iBoxx Investment Grade Corporate Bond ETF | 105.22 | -0.93 | 2026-09-01 | closed |
| JNK | SPDR Bloomberg High Yield Bond ETF | 95.21 | -0.88 | 2026-09-01 | closed |
| RSP | Invesco S&P 500 Equal Weight ETF | 217.59 | -0.82 | 2026-09-01 | closed |
| IWF | iShares Russell 1000 Growth ETF | 121.21 | -1.22 | 2026-09-01 | closed |
| IWD | iShares Russell 1000 Value ETF | 255.95 | -0.37 | 2026-09-01 | closed |
| TLT | iShares 20+ Year Treasury Bond ETF | 81.87 | -0.79 | 2026-09-01 | closed |
| IEF | iShares 7-10 Year Treasury Bond ETF | 92.1 | -0.69 | 2026-09-01 | closed |
| SHY | iShares 1-3 Year Treasury Bond ETF | 81.59 | -0.37 | 2026-09-01 | closed |
| GC=F | Gold Future | 4375.7 | -1.25 | 2026-09-01 | closed |
| SI=F | Silver Future | 64.66 | -2.36 | 2026-09-01 | closed |
| CL=F | WTI Crude Oil Future | 90.71 | -0.08 | 2026-09-02 | live as of 2 September 2026, 12:01:48 (HKT) |
| HG=F | Copper Future | 6.53 | -0.9 | 2026-09-01 | closed |

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
| Information Technology | 73 | 47.95 | 72.22 | 82.19 | 72.99 | 13.83 | very high | SMCI, ZBRA, WDAY | FICO, CDNS, NXPI |
| Consumer Staples | 34 | 48.48 | 62.5 | 58.82 | 64.2 | 9.97 | very high | TGT, CLX, HSY | HRL, MO, MNST |
| Industrials | 83 | 34.15 | 53.16 | 62.65 | 59.1 | 9.43 | very high | LDOS, HII, ALLE | ROL, LII, CHRW |
| Health Care | 59 | 79.66 | 79.66 | 76.27 | 51.44 | 8.44 | very high | VEEV, CRL, REGN | CVS, PODD, DVA |
| Communication Services | 24 | 60.87 | 52.17 | 70.83 | 45.44 | 11.1 | very high | CHTR, FOXA, FOX | RDDT, TTD, APP |
| Consumer Discretionary | 47 | 38.3 | 40.43 | 57.45 | 42.28 | 9.32 | very high | ABNB, GRMN, EXPE | TSLA, DECK, APTV |
| Materials | 25 | 60.0 | 68.0 | 64.0 | 38.25 | 8.72 | very high | NEM, NUE, FCX | CRH, LIN, CTVA |
| Energy | 21 | 95.24 | 85.71 | 71.43 | 33.27 | 8.3 | very high | APA, MPC, PSX | TRGP, HAL, TPL |
| Financials | 76 | 64.38 | 85.71 | 64.47 | 28.88 | 6.1 | very high | ARES, GPN, APO | TROW, SPGI, MSCI |
| Real Estate | 30 | 24.14 | 65.52 | 30.0 | 20.62 | 4.88 | very high | DLR, CSGP, EQIX | UDR, REG, DOC |
| Utilities | 31 | 9.68 | 25.81 | 6.45 | 20.47 | 3.79 | very high | CEG, AWK, PCG | NI, EIX, NRG |

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
| 1 | Cybersecurity | 68.7 | strong uptrend | positive | broad | 50.0 | 0.0 | 62.96 | CIBR | CIBR |
| 2 | Healthcare | 66.12 | strong uptrend | positive | broad | 47.8 | 65.0 | 54.37 | VEEV, CRL, REGN | CVS, PODD, DVA |
| 3 | Energy | 64.96 | strong uptrend | neutral | broad | 40.01 | 65.0 | 50.27 | APA, MPC, PSX | TRGP, HAL, TPL |
| 4 | Consumer Staples | 61.59 | strong uptrend | neutral | broad | 50.0 | 0.0 | 45.88 | TGT, CLX, HSY | HRL, MO, MNST |
| 5 | Financials | 61.41 | strong uptrend | positive | broad | 34.98 | 65.0 | 52.34 | ARES, GPN, APO | TROW, SPGI, MSCI |
| 6 | Technology | 61.39 | strong uptrend | neutral | mixed | 53.17 | 65.0 | 51.68 | SMCI, ZBRA, WDAY | FICO, CDNS, NXPI |
| 7 | Nuclear | 55.5 | neutral | neutral | broad | 50.0 | 0.0 | 50.82 | NLR | NLR |
| 8 | Crypto | 51.84 | neutral | neutral | mixed | 68.4 | 65.0 | 50.0 |  |  |
| 9 | Grid Infrastructure | 50.02 | downtrend | neutral | weak | 50.0 | 0.0 | 49.05 | GRID | GRID |
| 10 | Semiconductors | 49.59 | neutral | neutral | weak | 32.89 | 95.0 | 51.7 | SOXX, SMH | SMH, SOXX |
| 11 | Industrials | 49.4 | downtrend | neutral | weak | 50.0 | 0.0 | 51.11 | LDOS, HII, ALLE | ROL, LII, CHRW |
| 12 | Real Estate | 45.35 | neutral | neutral | weak | 45.3 | 65.0 | 46.51 | DLR, CSGP, EQIX | UDR, REG, DOC |
| 13 | Defense | 44.56 | strong downtrend | positive | weak | 50.0 | 0.0 | 57.75 | XAR | XAR |
| 14 | Consumer Discretionary | 39.35 | strong downtrend | neutral | weak | 50.0 | 0.0 | 47.0 | ABNB, GRMN, EXPE | TSLA, DECK, APTV |
| 15 | Utilities | 34.65 | strong downtrend | neutral | weak | 50.0 | 0.0 | 43.97 | CEG, AWK, PCG | NI, EIX, NRG |

### Thematic Strength

| Rank | Theme | Score | Setup | ETF Flow | Flow Reliability | Dispersion | Price | News |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Cybersecurity | 58.39 | Neutral / watchlist | 50.0 | 0.0 | 25.61 | False | False |
| 2 | Energy | 58.12 | Positive setup | 40.01 | 65.0 | 1.59 | False | False |
| 3 | Healthcare Innovation | 57.34 | Positive setup | 47.8 | 65.0 | 11.95 | False | False |
| 4 | Quality Growth | 56.47 | Neutral / watchlist | 59.7 | 65.0 | 32.28 | False | False |
| 5 | Financials | 56.46 | Positive setup | 34.98 | 65.0 | 10.64 | False | False |
| 6 | AI Infrastructure | 53.56 | Neutral / watchlist | 32.89 | 95.0 | 26.16 | False | False |
| 7 | Small Caps | 51.29 | Neutral / watchlist | 53.87 | 65.0 | 0.0 | False | False |
| 8 | Dividend Defensives | 51.28 | Neutral / watchlist | 51.57 | 65.0 | 7.21 | False | False |
| 9 | Semiconductors | 49.52 | Neutral / watchlist | 32.89 | 95.0 | 15.16 | False | False |
| 10 | Defense | 49.25 | Neutral / watchlist | 50.0 | 0.0 | 16.07 | False | False |
| 11 | Nuclear | 46.49 | Weak setup | 50.0 | 0.0 | 18.53 | False | False |
| 12 | Grid Infrastructure | 44.41 | Weak setup | 50.0 | 0.0 | 17.92 | False | False |
| 13 | Crypto Infrastructure | 44.17 | Weak setup | 68.4 | 65.0 | 7.37 | False | False |

- Top 5 improving themes: Financials, Healthcare Innovation, Defense, Cybersecurity, Small Caps
- Top 5 deteriorating themes: Crypto Infrastructure, Nuclear, Energy, Grid Infrastructure, Quality Growth
- Strong news but weak price confirmation: none
- Strong price but weak news confirmation: none

### Sector / Theme Alignment

| Sector | Related Themes | Sector Score | Sector Signal | Theme Score | Theme Signal | Interpretation |
| --- | --- | --- | --- | --- | --- | --- |
| Cybersecurity | Cybersecurity | 68.7 | strong | 58.39 | positive | sector and theme confirmation |
| Healthcare | Healthcare Innovation | 66.12 | strong | 57.34 | positive | sector and theme confirmation |
| Energy | Energy | 64.96 | positive | 58.12 | positive | sector and theme confirmation |
| Consumer Staples | Dividend Defensives | 61.59 | positive | 51.28 | mixed | sector stronger than related themes |
| Financials | Financials | 61.41 | positive | 56.46 | positive | sector and theme confirmation |
| Technology | AI Infrastructure, Semiconductors, Quality Growth | 61.39 | positive | 53.19 | mixed | sector stronger than related themes |
| Nuclear | Nuclear | 55.5 | positive | 46.49 | mixed | sector stronger than related themes |
| Crypto | Crypto Infrastructure | 51.84 | mixed | 44.17 | weak | mixed confirmation |
| Grid Infrastructure | Grid Infrastructure | 50.02 | mixed | 44.41 | weak | mixed confirmation |
| Semiconductors | AI Infrastructure, Semiconductors | 49.59 | mixed | 51.54 | mixed | mixed confirmation |
| Industrials | Defense, Grid Infrastructure | 49.4 | mixed | 46.83 | mixed | mixed confirmation |
| Real Estate | Dividend Defensives | 45.35 | mixed | 51.28 | mixed | mixed confirmation |
| Defense | Defense | 44.56 | weak | 49.25 | mixed | mixed confirmation |
| Consumer Discretionary | Small Caps | 39.35 | weak | 51.29 | mixed | mixed confirmation |
| Utilities | Grid Infrastructure, Nuclear, Dividend Defensives | 34.65 | very weak | 47.39 | mixed | mixed confirmation |

## Three-Month Outperformance Setup

| Rank | Theme | Score | Classification | Drivers | Invalidation Triggers |
| --- | --- | --- | --- | --- | --- |
| 1 | Energy | 63.16 | Positive setup | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 2 | Financials | 62.6 | Positive setup | relative_strength_60d, trend_persistence, breadth, downside_volatility, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 3 | Healthcare Innovation | 60.73 | Positive setup | relative_strength_60d, trend_persistence, breadth, downside_volatility, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 4 | Cybersecurity | 59.02 | Neutral / watchlist | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 5 | Quality Growth | 56.88 | Neutral / watchlist | trend_persistence, breadth | relative strength below SPY, breadth below 45%, news turns negative |
| 6 | AI Infrastructure | 55.77 | Neutral / watchlist | trend_persistence, breadth | relative strength below SPY, breadth below 45%, news turns negative |
| 7 | Dividend Defensives | 54.7 | Neutral / watchlist | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 8 | Semiconductors | 51.76 | Neutral / watchlist |  | relative strength below SPY, breadth below 45%, news turns negative |
| 9 | Small Caps | 51.21 | Neutral / watchlist | downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 10 | Defense | 48.55 | Neutral / watchlist | relative_strength_20d, downside_volatility, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 11 | Grid Infrastructure | 44.25 | Weak setup | downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 12 | Nuclear | 43.92 | Weak setup | relative_strength_20d | relative strength below SPY, breadth below 45%, news turns negative |

## Breadth and Participation

- Above 50DMA: `51.67%`
- Above 200DMA: `71.19%`
- Positive 20D return: `81.67%`

## Volatility and Risk Signals

- VIX close=16.34 pct_chg=9.52

## News Analytics

- Sentiment counts: {'positive': 50, 'negative': 28, 'neutral': 2}
- News confirmation score: `63.75`

### Top Market-Moving Headlines

**1. Global oil prices surge to a 6-week high after the U.S. strikes Iran in Hormuz**
- Source: MarketWatch Bulletins
- Importance / impact: High / Positive
- Relevance / horizon: macro / short-term
- Affected assets: U.S, oil_prices, geopolitical_risk
- Score: `65.21`
- Investment implication: Macro-relevant positive signal; use as context for rates, volatility, and index confirmation over the short-term.

**2. Dow ends 400 points down as stocks fall, oil spikes after new U.S.-Iran strikes**
- Source: MarketWatch Bulletins
- Importance / impact: High / Negative
- Relevance / horizon: macro / short-term
- Affected assets: U.S, geopolitical, oil_market
- Score: `61.77`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the short-term.

**3. Global oil prices surge to a 6-week high after the U.S. strikes Iran in Hormuz**
- Source: MarketWatch Top Stories
- Importance / impact: High / Positive
- Relevance / horizon: macro / short-term
- Affected assets: U.S, oil_prices, geo_political_risk
- Score: `57.8`
- Investment implication: Macro-relevant positive signal; use as context for rates, volatility, and index confirmation over the short-term.

**4. Global oil prices are surging after reports of more Hormuz trouble**
- Source: MarketWatch Bulletins
- Importance / impact: High / Negative
- Relevance / horizon: macro / short-term
- Affected assets: WFC, XOM, CVX, oil_prices, geopolitical_risk
- Score: `54.91`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the short-term.

**5. CNBC Daily Open: Groundhog Day in the Gulf**
- Source: CNBC Technology
- Importance / impact: High / Negative
- Relevance / horizon: macro / short-term
- Affected assets: CNBC, U.S, geopolitical, oil_market, central_bank_policy
- Score: `54.0`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the short-term.

**6. GoPro joins AI bonanza with pivot into data centers as shares skyrocket 40%**
- Source: CNBC Top News
- Importance / impact: Medium / Positive
- Relevance / horizon: sector_theme / medium-term
- Affected assets: GOOG, GOOGL, MSFT, AI, data center expansion
- Score: `52.51`
- Investment implication: Theme or sector positive signal; requires price and volume confirmation before affecting rankings.

**7. Dell’s AI servers drive a stellar earnings performance, and a raised outlook**
- Source: MarketWatch Top Stories
- Importance / impact: Medium / Positive
- Relevance / horizon: single_name / short
- Affected assets: DELL, AI, server, performance
- Score: `49.73`
- Investment implication: Single-name positive signal; low weight unless it maps to a broader sector or theme.

**8. Stocks sliding in final hour, oil prices spike as U.S.-Iran tensions escalate**
- Source: MarketWatch Bulletins
- Importance / impact: High / Negative
- Relevance / horizon: macro / short
- Affected assets: U.S, geopolitical, oil
- Score: `48.45`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the short.

**9. Oil prices extend move over $90 after report of two tankers struck in Hormuz**
- Source: MarketWatch Bulletins
- Importance / impact: High / Positive
- Relevance / horizon: macro / short-term
- Affected assets: oil, geopolitical
- Score: `48.45`
- Investment implication: Macro-relevant positive signal; use as context for rates, volatility, and index confirmation over the short-term.

**10. Global bond yields soar to multi-decade highs as Middle East turmoil reignites inflation fears**
- Source: CNBC Business News
- Importance / impact: High / Negative
- Relevance / horizon: macro / short-term
- Affected assets: U.K, U.S, inflation, geo-political, bond market
- Score: `46.24`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the short-term.


### Headline Quality Checks

Noisy headline list: This could be the 10-year Treasury’s tipping point, Oil Prices Rise as Renewed U.S.-Iran Fighting Deep, Stock market today: Dow, S&P 500, Nasdaq drop as r

## Positioning & Flow Dashboard

Positioning and flow data is used as confirmation only.

### Deferred Flow Sections

- Official ETF / fund flows: current report uses shares-outstanding-derived net fund flow estimates from free ETF metadata.
- Institutional Ownership: not available until SEC 13F ingestion is implemented.
- Grouped exposure flow reliability: use issuer coverage and availability status before treating ETF flow as confirmation.

## ETF Flows Analysis

- Market flow regime: `Mixed / Neutral`
- Market flow score: `49.5 / 100`
- Equity risk flow: `51.2`
- Credit risk flow: `42.6`
- Sector cyclicality flow: `49.1`
- Duration/liquidity flow: `46.7`
- Alternatives: `barbell demand`
- ETF flow reliability: `66.9 / 100`
- Dominant allocation direction: `defensive demand`

### Core Flow Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVV | U.S. Broad Equity | -0.7 | -0.6 | 0.2 | -0.4 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Medium-term deterioration; Persistent selling | 75.0 |
| ACWI | Global Equity | -0.7 | -1.2 | 0.0 | -0.4 | Flat | Neutral | Normal | Neutral | Neutral | Mixed or neutral flow structure; Persistent selling | 77.0 |
| EFA | Developed Markets ex-U.S. | -0.1 | -0.1 | 0.0 | -0.5 | Flat | Neutral | Normal | Neutral | Neutral | Mixed or neutral flow structure; Persistent selling | 77.0 |
| IEMG | Emerging Markets | 0.0 | 0.1 | 0.2 | -0.4 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural accumulation; Persistent selling | 83.0 |
| IJH | U.S. Mid Cap | 1.8 | 2.0 | 0.9 | -0.9 | Down | Buy | Normal | Contrarian Buying | Watch | Strong confirmation; Strong sponsorship | 100.0 |
| IWM | U.S. Small Cap | 0.3 | 0.4 | 0.3 | -0.2 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural distribution | 79.0 |
| LQD | Investment-Grade Credit | -0.3 | 0.5 | 0.6 | 0.8 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural accumulation | 91.0 |
| HYG | High-Yield Credit | -1.5 | -0.3 | 0.3 | 1.8 | Flat | Neutral | High | High-Turnover Consolidation | Transition | Structural distribution | 79.0 |
| SGOV | Treasury Bills / Cash | -0.3 | -1.9 | 0.9 | 3.7 | Flat | Sell | High | Distribution Before Breakdown | Early Bearish | Medium-term recovery; Exceptional institutional selling, Strong sponsorship | 87.0 |
| SHY | Short-Duration Treasuries | 0.5 | -0.4 | 0.6 | 3.8 | Flat | Neutral | High | High-Turnover Consolidation | Transition | Structural accumulation | 91.0 |
| IEF | Intermediate-Duration Treasuries | -2.8 | -1.8 | 0.5 | 0.1 | Down | Sell | Normal | Persistent Distribution | Risk-Off | Strong confirmation; Exceptional institutional selling | 87.0 |
| TLT | Long-Duration Treasuries | 2.5 | 2.9 | 0.7 | -0.2 | Down | Buy | Normal | Contrarian Buying | Watch | Strong confirmation; Exceptional institutional buying | 100.0 |
| GLD | Gold | 2.4 | 3.1 | 0.7 | 1.6 | Flat | Buy | High | Strong Accumulation | Early Bullish | Strong confirmation; Exceptional institutional buying | 100.0 |
| IBIT | Bitcoin | 1.9 | 0.5 | 0.8 | 0.5 | Up | Buy | High | Confirmed Accumulation | Strong Risk-On | Strong confirmation; Strong sponsorship | 100.0 |

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
| ITA | Aerospace and Defense | 0.4 | 0.8 | 0.3 | 1.5 | Down | Neutral | High | Heavy Selling Pressure | Cautious | Medium-term recovery | 87.0 |
| SOXX | Semiconductors | -1.7 | -0.0 | 0.3 | -0.6 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Medium-term deterioration | 83.0 |
| SMH | Semiconductors | -0.9 | -2.6 | 0.4 | -0.8 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural distribution; Exceptional institutional selling | 71.0 |
| CIBR | Cybersecurity | 1.9 | 1.3 | 0.8 | n/a | Up | Buy | Normal | Steady Accumulation | Risk-On | Strong confirmation; Strong sponsorship | 88.0 |

### Material Flow Divergences

| Severity | Type | Primary | Comparison | Interpretation |
| --- | --- | --- | --- | --- |
| high | close_substitute_divergence | GLD | IAU | primary representative differs from close substitute |
| high | close_substitute_divergence | AGG | IUSB | primary representative differs from close substitute |
| high | close_substitute_divergence | IWF | IVW | primary representative differs from close substitute |
| high | close_substitute_divergence | IWM | IJR | primary representative differs from close substitute |


## Contradiction / Audit Flags

No contradiction flags were triggered by current deterministic rules.

## Data Quality Notes

- Technical rows loaded: `60`
- S&P 500 constituent technical rows loaded: `503`
- Macro rows loaded: `49`
- Live macro rows used: `17`
- Economic rows loaded: `113`
- News rows loaded: `80`
- Positioning/flow rows loaded: `50`

# Rule-Based Institutional Market Update

Generated at: 2026-07-13T07:11:52.533575+00:00
Window: 24h

## Executive Dashboard

- Regime score: **65.0 / 100** (Mild Risk-On)
- Market strength: **75.76 / 100** (strong)
- Evidence quality: **83.0 / 100**
- ETF flow contribution: **51.44 / 100**, reliability **67.12 / 100**
- Breadth: **broad**; above 50DMA `60.0%`, above 200DMA `72.88%`
- Top sector score: **Cybersecurity** `71.02`
- Top theme score: **Semiconductors** `63.93`

## Market Regime Score

| Sub-score | Value |
| --- | --- |
| equity_trend | 90.0 |
| equity_momentum | 58.5 |
| market_breadth | 70.4 |
| volatility | 80.0 |
| rates_yield_curve | 58.0 |
| credit_proxy | 50.0 |
| dollar_fx | 54.2 |
| commodity_confirmation | 47.0 |
| etf_flow | 50.97 |
| news_confirmation | 59.38 |

Positive contributors: equity_trend=90.0, volatility=80.0, market_breadth=70.4
Negative contributors: none

## Market Strength Score

| Component | Score |
| --- | --- |
| indices_above_moving_averages | 90.0 |
| sp500_trend | 100.0 |
| nasdaq_trend | 100.0 |
| russell_participation | 80.0 |
| returns_momentum | 58.5 |
| rsi_zone | 57.5 |
| macd_confirmation | 43.75 |
| volume_confirmation | 50.0 |
| breadth | 70.4 |

## Evidence Quality / Confidence

- Confidence score: `83.0`
- Agreement ratio: `0.6`
- Contradiction count: `0`
- Missing indicators: none
- Warning flags: none

## Cross-Asset Confirmation

| Area | Signal | Interpretation |
| --- | --- | --- |
| Equities | S&P 500 rising; Nasdaq rising; Russell 2000 falling | Confirms risk appetite when broad indices rise together; weak small caps would narrow the signal. |
| Rates | 10Y Treasury rising; MOVE rising | Rising yields can pressure duration assets; falling MOVE supports calmer bond volatility. |
| Dollar | DXY proxy stable | A stronger dollar can tighten financial conditions and pressure commodities/emerging-market risk. |
| Credit | HYG stable | High-yield weakness would challenge equity risk-on confirmation. |
| Gold | Gold falling | Gold strength can indicate defensive demand, inflation hedging, or geopolitical concern. |
| Silver | Silver falling | Silver helps distinguish precious-metal demand from industrial/cyclical confirmation when data is available. |
| Copper | Copper rising | Copper strength supports cyclical growth confirmation; weakness would dilute risk-on breadth. |
| Oil | WTI crude rising | Oil spikes can be inflationary risk; falling oil can ease cost pressure but may also flag demand softness. |
| Volatility | VIX falling | Falling VIX supports risk appetite; a volatility spike would reduce confidence in broad risk-on. |

### Macro Snapshot

| Symbol | Name | Close | Pct Chg | Date |
| --- | --- | --- | --- | --- |
| ^GSPC | S&P 500 | 7575.39 | 0.42 | 2026-07-10 |
| ^IXIC | NASDAQ Composite | 26281.61 | 0.29 | 2026-07-10 |
| ^RUT | Russell 2000 Index | 2977.81 | -0.49 | 2026-07-10 |
| ^VIX | CBOE Volatility Index | 15.03 | -5.11 | 2026-07-10 |
| ^MOVE | ICE BofA MOVE Index | 69.55 | 6.34 | 2026-07-10 |
| ^FVX | Treasury Yield 5 Years | 4.31 | 0.91 | 2026-07-10 |
| ^TNX | Treasury Yield 10 Years | 4.57 | 0.66 | 2026-07-10 |
| ^TYX | Treasury Yield 30 Years | 5.07 | 0.36 | 2026-07-10 |
| DX-Y.NYB | US Dollar Index | 101.13 | 0.16 | 2026-07-12 |
| HYG | iShares iBoxx High Yield Corporate Bond ETF | 79.71 | -0.05 | 2026-07-10 |
| LQD | iShares iBoxx Investment Grade Corporate Bond ETF | 107.46 | -0.23 | 2026-07-10 |
| JNK | SPDR Bloomberg High Yield Bond ETF | 95.93 | -0.07 | 2026-07-10 |
| RSP | Invesco S&P 500 Equal Weight ETF | 214.3 | 0.37 | 2026-07-10 |
| IWF | iShares Russell 1000 Growth ETF | 123.95 | 0.53 | 2026-07-10 |
| IWD | iShares Russell 1000 Value ETF | 246.84 | 0.19 | 2026-07-10 |
| TLT | iShares 20+ Year Treasury Bond ETF | 84.47 | -0.02 | 2026-07-10 |
| IEF | iShares 7-10 Year Treasury Bond ETF | 93.63 | -0.09 | 2026-07-10 |
| SHY | iShares 1-3 Year Treasury Bond ETF | 81.88 | -0.04 | 2026-07-10 |
| GC=F | Gold Future | 4086.1 | -0.44 | 2026-07-12 |
| SI=F | Silver Future | 59.12 | -1.16 | 2026-07-12 |
| CL=F | WTI Crude Oil Future | 73.73 | 3.25 | 2026-07-12 |
| HG=F | Copper Future | 6.26 | 0.35 | 2026-07-12 |

## Market Dispersion Analysis

- Sector ETF 20D dispersion: `12.67` points (high); leader `XLI` (Industrials) `7.23`, laggard `XLE` (Energy) `-5.44`
- Sector ETF 60D dispersion: `29.8` points (very high); leader `XLK` (Technology) `25.58`, laggard `XLC` (Communication Services) `-4.22`

| Comparison | Left | Right | 20D Spread | Signal |
| --- | --- | --- | --- | --- |
| Equal-weight vs cap-weight | RSP (Equal-weight S&P 500) | SPY (S&P 500) | -0.31 | balanced |
| Small-cap vs large-cap | IWM (Russell 2000) | SPY (S&P 500) | 0.87 | balanced |
| Growth vs value | IWF (Russell 1000 Growth) | IWD (Russell 1000 Value) | -1.37 | value leadership |
| Nasdaq vs S&P 500 | QQQ (Nasdaq 100) | SPY (S&P 500) | 0.52 | balanced |

## Sector Constituent Dispersion

- Breadth 50D / 200D: percentage of active S&P 500 constituents in the sector trading above the 50-day / 200-day moving average.
- Positive 20D: percentage of active sector constituents with positive 20-day return.
- Std 20D: cross-sectional standard deviation of constituent 20-day returns; higher means wider stock-level dispersion.

| Sector | Count | Breadth 50D | Breadth 200D | Positive 20D | 20D Dispersion | Std 20D | Label | Leaders | Laggards |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Materials | 26 | 61.54 | 65.38 | 76.92 | 214.11 | 38.73 | very high | DD, IP, CTVA | ALB, STLD, DOW |
| Information Technology | 74 | 48.65 | 64.38 | 58.11 | 114.87 | 16.97 | very high | ZBRA, PANW, AMD | ORCL, CRWD, KLAC |
| Health Care | 59 | 91.53 | 61.02 | 89.83 | 55.83 | 8.74 | very high | MRNA, TECH, CRL | PFE, ZTS, BSX |
| Industrials | 81 | 74.03 | 71.43 | 81.48 | 41.14 | 6.94 | very high | AXON, GEV, UAL | LDOS, CPRT, FDXF |
| Financials | 76 | 88.89 | 70.0 | 88.16 | 40.62 | 6.39 | very high | HOOD, GPN, JKHY | APO, CME, CBOE |
| Communication Services | 23 | 36.36 | 45.45 | 52.17 | 37.62 | 9.3 | very high | META, TTWO, OMC | TKO, FOX, FOXA |
| Consumer Discretionary | 47 | 55.32 | 46.81 | 53.19 | 37.36 | 8.42 | very high | GPC, DASH, EXPE | APTV, LVS, TJX |
| Real Estate | 31 | 58.06 | 74.19 | 38.71 | 26.63 | 5.94 | very high | WELL, VTR, DOC | AMT, CCI, CSGP |
| Consumer Staples | 34 | 63.64 | 62.5 | 38.24 | 24.06 | 5.83 | very high | DLTR, KMB, DG | MDLZ, CASY, BG |
| Energy | 21 | 33.33 | 90.48 | 33.33 | 22.76 | 6.77 | very high | VLO, MPC, TPL | APA, HAL, SLB |
| Utilities | 31 | 87.1 | 80.65 | 100.0 | 16.03 | 3.45 | high | NRG, VST, ES | NI, PPL, DUK |

## Economic Data Snapshot

### U.S. Labor

| Indicator | Latest | Unit | Change | Date | Rule-Based Interpretation |
| --- | --- | --- | --- | --- | --- |
| All Employees, Total Nonfarm | 158984.0 | thousands | 57.0 thousands vs prior | 2026-06-01 | Higher reading supports activity or liquidity. |
| Unemployment Rate | 4.2 | percent | -0.1 pp vs prior | 2026-06-01 | Lower reading eases macro pressure. |
| Initial Claims | 215000.0 | number | -12000.0 number vs prior | 2026-06-20 | Lower claims indicate firmer labor-market conditions. |
| Continued Claims | 1821000.0 | number | 21000.0 number vs prior | 2026-06-13 | Higher claims indicate softer labor-market conditions. |
| Labor Force Participation Rate | 61.5 | percent | -0.3 pp vs prior | 2026-06-01 | Lower participation constrains labor supply. |

### U.S. Growth

| Indicator | Latest | Unit | Change | Date | Rule-Based Interpretation |
| --- | --- | --- | --- | --- | --- |
| Real Gross Domestic Product | 24180.42 | billions chained 2017 dollars | 124.67 billions chained 2017 dollars vs prior | 2026-01-01 | Higher reading supports activity or liquidity. |
| Industrial Production Index | 102.65 | index 2017=100 | 0.14 index pts vs prior | 2026-05-01 | Higher reading supports activity or liquidity. |
| Advance Retail Sales | 763705.0 | millions dollars | 6669.0 millions dollars vs prior | 2026-05-01 | Higher reading supports activity or liquidity. |

### U.S. Inflation

| Indicator | Latest | Unit | Change | Date | Rule-Based Interpretation |
| --- | --- | --- | --- | --- | --- |
| Headline CPI month-over-month inflation rate | 0.47 | percent | -0.17 pp vs prior | 2026-05-01 | Lower reading eases macro pressure. |
| Headline CPI year-over-year inflation rate | 4.27 | percent | 0.32 pp vs prior | 2026-05-01 | Higher reading increases macro pressure. |
| Core CPI month-over-month inflation rate | 0.21 | percent | -0.17 pp vs prior | 2026-05-01 | Lower reading eases macro pressure. |
| Core CPI year-over-year inflation rate | 2.96 | percent | -0.03 pp vs prior | 2026-05-01 | Lower reading eases macro pressure. |
| Headline CPI year-over-year inflation rate | 4.47 | percent | 0.33 pp vs prior | 2026-05-01 | Higher reading increases macro pressure. |
| Core CPI year-over-year inflation rate | 3.07 | percent | 0.04 pp vs prior | 2026-05-01 | Higher reading increases macro pressure. |
| Headline PCE Price Index month-over-month inflation rate | 0.45 | percent | 0.04 pp vs prior | 2026-05-01 | Higher reading increases macro pressure. |
| Headline PCE Price Index year-over-year inflation rate | 4.07 | percent | 0.28 pp vs prior | 2026-05-01 | Higher reading increases macro pressure. |
| Core PCE Price Index month-over-month inflation rate | 0.32 | percent | 0.07 pp vs prior | 2026-05-01 | Higher reading increases macro pressure. |
| Core PCE Price Index year-over-year inflation rate | 3.41 | percent | 0.09 pp vs prior | 2026-05-01 | Higher reading increases macro pressure. |
| Headline PPI Final Demand month-over-month inflation rate | 1.03 | percent | -0.09 pp vs prior | 2026-05-01 | Lower reading eases macro pressure. |
| Headline PPI Final Demand year-over-year inflation rate | 6.46 | percent | 0.79 pp vs prior | 2026-05-01 | Higher reading increases macro pressure. |
| Core PPI Final Demand Less Foods and Energy month-over-month inflation rate | 0.42 | percent | -0.27 pp vs prior | 2026-05-01 | Lower reading eases macro pressure. |
| Core PPI Final Demand Less Foods and Energy year-over-year inflation rate | 4.9 | percent | 0.03 pp vs prior | 2026-05-01 | Higher reading increases macro pressure. |
| Consumer Price Index for All Urban Consumers | 333.98 | index 1982-1984=100 | 1.57 index pts vs prior | 2026-05-01 | Higher reading increases macro pressure. |
| Core CPI | 336.12 | index 1982-1984=100 | 0.7 index pts vs prior | 2026-05-01 | Higher reading increases macro pressure. |
| Personal Consumption Expenditures Price Index | 131.53 | index 2017=100 | 0.59 index pts vs prior | 2026-05-01 | Higher reading increases macro pressure. |
| Core PCE Price Index | 130.08 | index 2017=100 | 0.41 index pts vs prior | 2026-05-01 | Higher reading increases macro pressure. |
| Producer Price Index: Final Demand | 158.01 | index Nov 2009=100 | 1.62 index pts vs prior | 2026-05-01 | Latest structural macro observation. |
| Producer Price Index: Final Demand Less Foods and Energy | 154.15 | index Apr 2010=100 | 0.64 index pts vs prior | 2026-05-01 | Latest structural macro observation. |

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
| Housing Starts | 1177.0 | thousands | -215.0 thousands vs prior | 2026-05-01 | Lower reading signals softer activity or liquidity. |
| New Privately-Owned Housing Units Authorized | 1410.0 | thousands | -13.0 thousands vs prior | 2026-05-01 | Lower reading signals softer activity or liquidity. |
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
| US dollar/Euro ECB reference exchange rate | 1.14 | USD | -0.0 USD vs prior | 2026-07-10 | EUR weakened versus this currency. |
| Japanese yen/Euro ECB reference exchange rate | 185.02 | JPY | -0.7 JPY vs prior | 2026-07-10 | EUR weakened versus this currency. |
| Chinese yuan renminbi/Euro ECB reference exchange rate | 7.74 | CNY | -0.03 CNY vs prior | 2026-07-10 | EUR weakened versus this currency. |
| Australian dollar/Euro ECB reference exchange rate | 1.64 | AUD | -0.0 AUD vs prior | 2026-07-10 | EUR weakened versus this currency. |

ABS Australia note: ABS rows are stored locally/Neon, but most series are dimension-coded; only curated series should be promoted into narrative report text.

## Sector and Theme Leadership

### Official Sector Strength

Supporting and detracting names are the top/bottom S&P 500 constituents by 20D return when constituent coverage is available; otherwise the report falls back to related ETFs.

| Rank | Sector | Score | Trend | Momentum | Stock Breadth | ETF Flow | Flow Reliability | 3M RS | Supporting / Leaders | Detracting / Laggards |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Cybersecurity | 71.02 | strong uptrend | positive | broad | 50.0 | 0.0 | 68.83 | CIBR | CIBR |
| 2 | Financials | 67.56 | strong uptrend | positive | broad | 68.55 | 65.0 | 51.11 | HOOD, GPN, JKHY | APO, CME, CBOE |
| 3 | Healthcare | 64.47 | strong uptrend | positive | broad | 41.07 | 65.0 | 50.44 | MRNA, TECH, CRL | PFE, ZTS, BSX |
| 4 | Semiconductors | 63.87 | strong uptrend | positive | broad | 75.28 | 100.0 | 64.4 | SOXX, SMH | SMH, SOXX |
| 5 | Industrials | 63.43 | strong uptrend | positive | broad | 50.0 | 0.0 | 50.39 | AXON, GEV, UAL | LDOS, CPRT, FDXF |
| 6 | Technology | 62.91 | strong uptrend | positive | broad | 59.18 | 65.0 | 55.2 | ZBRA, PANW, AMD | ORCL, CRWD, KLAC |
| 7 | Real Estate | 58.76 | strong uptrend | neutral | broad | 61.18 | 65.0 | 44.29 | WELL, VTR, DOC | AMT, CCI, CSGP |
| 8 | Utilities | 57.67 | uptrend | neutral | broad | 50.0 | 0.0 | 45.98 | NRG, VST, ES | NI, PPL, DUK |
| 9 | Consumer Staples | 57.66 | strong uptrend | neutral | broad | 50.0 | 0.0 | 44.41 | DLTR, KMB, DG | MDLZ, CASY, BG |
| 10 | Crypto | 49.4 | neutral | neutral | mixed | 44.0 | 65.0 | 50.0 |  |  |
| 11 | Consumer Discretionary | 49.04 | downtrend | neutral | weak | 50.0 | 0.0 | 46.33 | GPC, DASH, EXPE | APTV, LVS, TJX |
| 12 | Grid Infrastructure | 45.96 | neutral | neutral | weak | 50.0 | 0.0 | 45.97 | GRID | GRID |
| 13 | Energy | 44.31 | strong downtrend | neutral | weak | 63.74 | 65.0 | 40.19 | VLO, MPC, TPL | APA, HAL, SLB |
| 14 | Defense | 41.05 | downtrend | neutral | weak | 50.0 | 0.0 | 44.41 | XAR | XAR |
| 15 | Nuclear | 32.56 | strong downtrend | negative | weak | 50.0 | 0.0 | 35.91 | NLR | NLR |

### Thematic Strength

| Rank | Theme | Score | Setup | ETF Flow | Flow Reliability | Dispersion | Price | News |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Semiconductors | 63.93 | Positive setup | 75.28 | 100.0 | 19.68 | True | False |
| 2 | Financials | 61.29 | Positive setup | 68.55 | 65.0 | 4.02 | True | False |
| 3 | Healthcare Innovation | 59.94 | Positive setup | 41.07 | 65.0 | 12.01 | False | False |
| 4 | Small Caps | 58.24 | Positive setup | 68.98 | 65.0 | 0.0 | False | False |
| 5 | Cybersecurity | 55.63 | Neutral / watchlist | 50.0 | 0.0 | 94.92 | False | False |
| 6 | Dividend Defensives | 55.47 | Neutral / watchlist | 64.54 | 65.0 | 6.83 | False | False |
| 7 | AI Infrastructure | 55.41 | Neutral / watchlist | 75.28 | 100.0 | 10.44 | False | False |
| 8 | Quality Growth | 51.87 | Neutral / watchlist | 54.65 | 65.0 | 11.23 | False | False |
| 9 | Grid Infrastructure | 49.8 | Neutral / watchlist | 50.0 | 0.0 | 7.3 | False | False |
| 10 | Defense | 44.85 | Weak setup | 50.0 | 0.0 | 26.83 | False | False |
| 11 | Energy | 43.61 | Weak setup | 63.74 | 65.0 | 2.35 | False | False |
| 12 | Nuclear | 31.81 | Weak setup | 50.0 | 0.0 | 17.59 | False | False |
| 13 | Crypto Infrastructure | 30.86 | Underperformance risk | 44.0 | 65.0 | 21.27 | False | False |

- Top 5 improving themes: Cybersecurity, Semiconductors, Healthcare Innovation, AI Infrastructure, Quality Growth
- Top 5 deteriorating themes: Crypto Infrastructure, Nuclear, Defense, Energy, Grid Infrastructure
- Strong news but weak price confirmation: none
- Strong price but weak news confirmation: Semiconductors, Financials

### Sector / Theme Alignment

| Sector | Related Themes | Sector Score | Sector Signal | Theme Score | Theme Signal | Interpretation |
| --- | --- | --- | --- | --- | --- | --- |
| Cybersecurity | Cybersecurity | 71.02 | strong | 55.63 | positive | sector and theme confirmation |
| Financials | Financials | 67.56 | strong | 61.29 | positive | sector and theme confirmation |
| Healthcare | Healthcare Innovation | 64.47 | positive | 59.94 | positive | sector and theme confirmation |
| Semiconductors | AI Infrastructure, Semiconductors | 63.87 | positive | 59.67 | positive | sector and theme confirmation |
| Industrials | Defense, Grid Infrastructure | 63.43 | positive | 47.32 | mixed | sector stronger than related themes |
| Technology | AI Infrastructure, Semiconductors, Quality Growth | 62.91 | positive | 57.07 | positive | sector and theme confirmation |
| Real Estate | Dividend Defensives | 58.76 | positive | 55.47 | positive | sector and theme confirmation |
| Utilities | Grid Infrastructure, Nuclear, Dividend Defensives | 57.67 | positive | 45.69 | mixed | sector stronger than related themes |
| Consumer Staples | Dividend Defensives | 57.66 | positive | 55.47 | positive | sector and theme confirmation |
| Crypto | Crypto Infrastructure | 49.4 | mixed | 30.86 | very weak | mixed confirmation |
| Consumer Discretionary | Small Caps | 49.04 | mixed | 58.24 | positive | theme stronger than official sector |
| Grid Infrastructure | Grid Infrastructure | 45.96 | mixed | 49.8 | mixed | mixed confirmation |
| Energy | Energy | 44.31 | weak | 43.61 | weak | broad weakness across sector and themes |
| Defense | Defense | 41.05 | weak | 44.85 | weak | broad weakness across sector and themes |
| Nuclear | Nuclear | 32.56 | very weak | 31.81 | very weak | broad weakness across sector and themes |

## Three-Month Outperformance Setup

| Rank | Theme | Score | Classification | Drivers | Invalidation Triggers |
| --- | --- | --- | --- | --- | --- |
| 1 | Healthcare Innovation | 65.73 | Positive setup | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 2 | Semiconductors | 64.57 | Positive setup | relative_strength_60d, trend_persistence, breadth, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 3 | Financials | 63.85 | Positive setup | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 4 | Small Caps | 63.36 | Positive setup | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 5 | Dividend Defensives | 57.35 | Neutral / watchlist | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 6 | AI Infrastructure | 56.66 | Neutral / watchlist | trend_persistence, breadth | relative strength below SPY, breadth below 45%, news turns negative |
| 7 | Cybersecurity | 56.29 | Neutral / watchlist | relative_strength_60d, trend_persistence, breadth, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 8 | Quality Growth | 54.67 | Neutral / watchlist | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 9 | Grid Infrastructure | 53.96 | Neutral / watchlist | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 10 | Defense | 40.95 | Weak setup | news_acceleration | relative strength below SPY, breadth below 45%, news turns negative |
| 11 | Energy | 38.32 | Weak setup | downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 12 | Nuclear | 30.43 | Weak setup |  | relative strength below SPY, breadth below 45%, news turns negative |

## Breadth and Participation

- Above 50DMA: `60.0%`
- Above 200DMA: `72.88%`
- Positive 20D return: `78.33%`

## Volatility and Risk Signals

- VIX close=15.03 pct_chg=-5.11

## News Analytics

- Sentiment counts: {'positive': 43, 'negative': 28, 'neutral': 9}
- News confirmation score: `59.38`

### Top Market-Moving Headlines

**1. Oil prices rise, stock futures dip after latest flare-up of strikes between U.S. and Iran**
- Source: MarketWatch Top Stories
- Importance / impact: High / Negative
- Relevance / horizon: macro / short-term
- Affected assets: U.S, geopolitical_risk, oil_market
- Score: `60.0`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the short-term.

**2. Khosla family agrees to purchase defending Super Bowl champion Seattle Seahawks for $9.612 billion, sources say**
- Source: CNBC Markets
- Importance / impact: Medium / Positive
- Relevance / horizon: sector_theme / short-term
- Affected assets: sports, business
- Score: `52.51`
- Investment implication: Theme or sector positive signal; requires price and volume confirmation before affecting rankings.

**3. CNBC Daily Open: Mideast tensions on the boil again as U.S., Iran trade strikes**
- Source: CNBC Top News
- Importance / impact: High / Negative
- Relevance / horizon: macro / short-term
- Affected assets: CNBC, U.S, geopolitical_risk, oil_prices
- Score: `48.45`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the short-term.

**4. The stock-market rally now hinges more on AI than oil**
- Source: MarketWatch Bulletins
- Importance / impact: High / Positive
- Relevance / horizon: macro / short-term
- Affected assets: AI
- Score: `48.45`
- Investment implication: Macro-relevant positive signal; use as context for rates, volatility, and index confirmation over the short-term.

**5. Oil prices rise, stock futures dip after latest flare-up of U.S.-Iran strikes**
- Source: MarketWatch Bulletins
- Importance / impact: High / Mixed
- Relevance / horizon: macro / short-term
- Affected assets: U.S, oil_prices, geo_political
- Score: `48.45`
- Investment implication: Macro-relevant mixed signal; use as context for rates, volatility, and index confirmation over the short-term.

**6. Oil prices rise as U.S. and Iran fight for control of Strait of Hormuz**
- Source: CNBC Top News
- Importance / impact: High / Positive
- Relevance / horizon: macro / short-term
- Affected assets: U.S., U.S, geopolitical_risk, oil_market
- Score: `48.45`
- Investment implication: Macro-relevant positive signal; use as context for rates, volatility, and index confirmation over the short-term.

**7. The stock-market rally now hinges more on AI than oil**
- Source: MarketWatch Top Stories
- Importance / impact: Medium / Positive
- Relevance / horizon: macro / short-term
- Affected assets: AI
- Score: `44.2`
- Investment implication: Macro-relevant positive signal; use as context for rates, volatility, and index confirmation over the short-term.

**8. SK Hynix South Korean shares clock worst day on record, sink over 15%, after stellar Nasdaq debut**
- Source: CNBC Top News
- Importance / impact: Medium / Negative
- Relevance / horizon: single_name / 短期
- Affected assets: SK, technology, stocks
- Score: `41.68`
- Investment implication: Single-name negative signal; low weight unless it maps to a broader sector or theme.

**9. TSMC, the world's largest contract chipmaker, reports 68% surge in June revenue**
- Source: CNBC Technology
- Importance / impact: Medium / Positive
- Relevance / horizon: single_name / short-term
- Affected assets: TSMC, revenue growth, chipmaker
- Score: `39.49`
- Investment implication: Single-name positive signal; low weight unless it maps to a broader sector or theme.

**10. Next week brings earnings and inflation data amid resumption of U.S.-Iran hostilities. Here's what's ahead**
- Source: CNBC Business
- Importance / impact: Low / Mixed
- Relevance / horizon: sector_theme / short-term
- Affected assets: MSFT, AAPL, GOOGL, TSLA, U.S
- Score: `34.68`
- Investment implication: Theme or sector mixed signal; requires price and volume confirmation before affecting rankings.


### Headline Quality Checks

Noisy headline list: Why Lumentum (LITE) Could Benefit From AI Optical 

## Positioning & Flow Dashboard

Positioning and flow data is used as confirmation only. FINRA short-sale volume is not short interest.

### Deferred Flow Sections

- Official ETF / fund flows: current report uses shares-outstanding-derived net fund flow estimates from free ETF metadata.
- Institutional Ownership: not available until SEC 13F ingestion is implemented.
- Crowding / Squeeze Risks: initial coverage uses CFTC crowded positioning and FINRA elevated short-sale volume only.
- Grouped exposure flow reliability: use issuer coverage and availability status before treating ETF flow as confirmation.

## ETF Flows Analysis

- Market flow regime: `Selective Risk-On`
- Market flow score: `57.4 / 100`
- Equity risk flow: `61.6`
- Credit risk flow: `61.5`
- Sector cyclicality flow: `58.3`
- Duration/liquidity flow: `46.8`
- Alternatives: `mixed alternative-asset demand`
- ETF flow reliability: `67.1 / 100`
- Dominant allocation direction: `mixed allocation`

### Core Flow Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVV | U.S. Broad Equity | 1.6 | 1.6 | 0.5 | -0.6 | Up | Buy | Low | Quiet Accumulation | Mild Risk-On | Strong confirmation | 95.0 |
| ACWI | Global Equity | -0.3 | -1.1 | 0.1 | -0.8 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Medium-term recovery; Persistent selling | 79.0 |
| EFA | Developed Markets ex-U.S. | 0.6 | 0.2 | 0.1 | -1.6 | Up | Sell | Low | Weak Distribution | Neutral | Tactical profit-taking inside structural accumulation; Persistent selling | 75.0 |
| IEMG | Emerging Markets | -0.5 | -0.7 | 0.1 | -0.1 | Flat | Neutral | Normal | Neutral | Neutral | Structural distribution; Persistent selling | 71.0 |
| IJH | U.S. Mid Cap | 0.3 | 0.3 | 0.6 | -0.4 | Flat | Neutral | Normal | Neutral | Neutral | Structural accumulation | 91.0 |
| IWM | U.S. Small Cap | 1.8 | 2.0 | 0.5 | -1.7 | Up | Buy | Low | Quiet Accumulation | Mild Risk-On | Strong confirmation; Exceptional institutional buying | 100.0 |
| LQD | Investment-Grade Credit | 2.6 | 0.6 | 0.8 | 0.9 | Flat | Neutral | Normal | Neutral | Neutral | Structural accumulation; Exceptional institutional buying, Strong sponsorship | 100.0 |
| HYG | High-Yield Credit | 1.0 | 0.3 | 0.7 | -1.1 | Flat | Sell | Normal | Quiet Distribution | Weakening | Medium-term recovery; Exceptional institutional selling | 79.0 |
| SGOV | Treasury Bills / Cash | -0.7 | -1.8 | 0.8 | -0.9 | Flat | Buy | Normal | Quiet Accumulation | Improving | Medium-term recovery; Strong sponsorship | 95.0 |
| SHY | Short-Duration Treasuries | 0.2 | -1.2 | 0.3 | -0.9 | Flat | Buy | Normal | Quiet Accumulation | Improving | Medium-term recovery | 87.0 |
| IEF | Intermediate-Duration Treasuries | -0.5 | -1.0 | 0.3 | -0.1 | Flat | Neutral | Normal | Neutral | Neutral | Structural distribution | 79.0 |
| TLT | Long-Duration Treasuries | 2.2 | 1.9 | 0.7 | -1.4 | Flat | Buy | Normal | Quiet Accumulation | Improving | Strong confirmation; Exceptional institutional buying | 100.0 |
| GLD | Gold | 0.0 | -0.4 | 0.3 | -0.6 | Flat | Neutral | Normal | Neutral | Neutral | Structural distribution | 79.0 |
| IBIT | Bitcoin | -1.2 | -1.8 | 0.3 | -0.8 | Up | Sell | Normal | Profit Taking | Slightly Bearish | Strong confirmation | 95.0 |

### Sector Flow Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| XLC | Communication Services | -0.3 | 0.9 | 0.3 | 0.2 | Flat | Sell | Normal | Quiet Distribution | Weakening | Strong confirmation | 95.0 |
| XLY | Consumer Discretionary | 0.3 | 0.8 | 0.5 | 0.1 | Flat | Neutral | Normal | Neutral | Neutral | Mixed or neutral flow structure | 85.0 |
| XLP | Consumer Staples | 0.8 | 2.2 | 0.5 | -0.3 | Down | Buy | Normal | Contrarian Buying | Watch | Strong confirmation; Exceptional institutional buying | 100.0 |
| XLE | Energy | -0.8 | -0.8 | 0.4 | -1.4 | Flat | Neutral | Normal | Neutral | Neutral | Structural distribution | 79.0 |
| XLF | Financials | 0.8 | 0.6 | 0.7 | -1.1 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Medium-term recovery | 87.0 |
| XLV | Health Care | 1.1 | 0.3 | 0.6 | -0.3 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Medium-term recovery | 87.0 |
| XLI | Industrials | 1.6 | 1.0 | 0.7 | -1.4 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural accumulation | 91.0 |
| XLK | Information Technology | -0.8 | -0.3 | 0.5 | -1.2 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Medium-term deterioration | 83.0 |
| XLB | Materials | 0.2 | 0.3 | 0.6 | -0.3 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural accumulation | 91.0 |
| XLRE | Real Estate | 2.0 | 1.8 | 0.8 | -1.4 | Down | Buy | Normal | Contrarian Buying | Watch | Strong confirmation; Exceptional institutional buying, Strong sponsorship | 100.0 |
| XLU | Utilities | 1.0 | -1.0 | 0.7 | -0.2 | Up | Buy | Normal | Steady Accumulation | Risk-On | Medium-term recovery | 87.0 |

### Subsector PFV Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ITA | Aerospace and Defense | -0.2 | 0.3 | 0.5 | -1.2 | Flat | Neutral | Normal | Neutral | Neutral | Structural distribution | 79.0 |
| SOXX | Semiconductors | 2.5 | 2.7 | 0.6 | -0.9 | Flat | Buy | Normal | Quiet Accumulation | Improving | Strong confirmation; Exceptional institutional buying | 100.0 |
| SMH | Semiconductors | -2.0 | 0.6 | 0.4 | -1.3 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Medium-term deterioration | 83.0 |
| CIBR | Cybersecurity | n/a | n/a | 0.2 | n/a | Flat | Buy | Normal | Quiet Accumulation | Improving | Mixed or neutral flow structure; Persistent selling | 42.0 |

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
- Macro rows loaded: `38`
- Economic rows loaded: `113`
- News rows loaded: `80`
- Positioning/flow rows loaded: `30`

# Rule-Based Institutional Market Update

Generated at: 2026-07-11T10:11:54.111184+00:00
Window: 24h

## Executive Dashboard

- Regime score: **69.68 / 100** (Moderate Risk-On)
- Market strength: **75.76 / 100** (strong)
- Evidence quality: **90.0 / 100**
- Breadth: **broad**; above 50DMA `60.0%`, above 200DMA `72.88%`
- Top sector score: **Cybersecurity** `74.32`
- Top theme score: **Healthcare Innovation** `63.18`

## Market Regime Score

| Sub-score | Value |
| --- | --- |
| equity_trend | 90.0 |
| equity_momentum | 58.5 |
| market_breadth | 70.4 |
| volatility | 80.0 |
| rates_yield_curve | 58.0 |
| credit_proxy | 50.0 |
| dollar_fx | 54.88 |
| commodity_confirmation | 58.0 |
| news_confirmation | 60.62 |
| market_strength | 75.76 |

Positive contributors: equity_trend=90.0, volatility=80.0, market_strength=75.76, market_breadth=70.4, news_confirmation=60.62
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

- Confidence score: `90.0`
- Agreement ratio: `0.8`
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
| Gold | Gold stable | Gold strength can indicate defensive demand, inflation hedging, or geopolitical concern. |
| Silver | Silver stable | Silver helps distinguish precious-metal demand from industrial/cyclical confirmation when data is available. |
| Copper | Copper rising | Copper strength supports cyclical growth confirmation; weakness would dilute risk-on breadth. |
| Oil | WTI crude falling | Oil spikes can be inflationary risk; falling oil can ease cost pressure but may also flag demand softness. |
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
| DX-Y.NYB | US Dollar Index | 100.97 | 0.02 | 2026-07-10 |
| HYG | iShares iBoxx High Yield Corporate Bond ETF | 79.71 | -0.05 | 2026-07-10 |
| LQD | iShares iBoxx Investment Grade Corporate Bond ETF | 107.46 | -0.23 | 2026-07-10 |
| JNK | SPDR Bloomberg High Yield Bond ETF | 95.93 | -0.07 | 2026-07-10 |
| RSP | Invesco S&P 500 Equal Weight ETF | 214.3 | 0.37 | 2026-07-10 |
| IWF | iShares Russell 1000 Growth ETF | 123.95 | 0.53 | 2026-07-10 |
| IWD | iShares Russell 1000 Value ETF | 246.84 | 0.19 | 2026-07-10 |
| TLT | iShares 20+ Year Treasury Bond ETF | 84.47 | -0.02 | 2026-07-10 |
| IEF | iShares 7-10 Year Treasury Bond ETF | 93.63 | -0.09 | 2026-07-10 |
| SHY | iShares 1-3 Year Treasury Bond ETF | 81.88 | -0.04 | 2026-07-10 |
| GC=F | Gold Future | 4128.9 | -0.04 | 2026-07-10 |
| SI=F | Silver Future | 60.3 | -0.13 | 2026-07-10 |
| CL=F | WTI Crude Oil Future | 71.51 | -0.79 | 2026-07-10 |
| HG=F | Copper Future | 6.29 | 1.13 | 2026-07-10 |

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

| Rank | Sector | Score | Trend | Momentum | Breadth | 3M RS | Supporting / Leaders | Detracting / Laggards |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Cybersecurity | 74.32 | strong uptrend | positive | broad | 68.83 | CIBR | CIBR |
| 2 | Financials | 68.38 | strong uptrend | positive | broad | 51.11 | HOOD, GPN, JKHY | APO, CME, CBOE |
| 3 | Healthcare | 68.0 | strong uptrend | positive | broad | 50.44 | MRNA, TECH, CRL | PFE, ZTS, BSX |
| 4 | Industrials | 66.07 | strong uptrend | positive | broad | 50.39 | AXON, GEV, UAL | LDOS, CPRT, FDXF |
| 5 | Technology | 64.97 | strong uptrend | positive | broad | 55.2 | ZBRA, PANW, AMD | ORCL, CRWD, KLAC |
| 6 | Semiconductors | 63.77 | strong uptrend | positive | broad | 64.4 | SOXX, SMH | SMH, SOXX |
| 7 | Real Estate | 59.88 | strong uptrend | neutral | broad | 44.29 | WELL, VTR, DOC | AMT, CCI, CSGP |
| 8 | Consumer Staples | 59.64 | strong uptrend | neutral | broad | 44.41 | DLTR, KMB, DG | MDLZ, CASY, BG |
| 9 | Utilities | 59.6 | uptrend | neutral | broad | 45.98 | NRG, VST, ES | NI, PPL, DUK |
| 10 | Crypto | 50.0 | neutral | neutral | mixed | 50.0 |  |  |
| 11 | Consumer Discretionary | 47.32 | downtrend | neutral | weak | 46.33 | GPC, DASH, EXPE | APTV, LVS, TJX |
| 12 | Grid Infrastructure | 44.51 | neutral | neutral | weak | 45.97 | GRID | GRID |
| 13 | Energy | 40.87 | strong downtrend | neutral | weak | 40.19 | VLO, MPC, TPL | APA, HAL, SLB |
| 14 | Defense | 38.92 | downtrend | neutral | weak | 44.41 | XAR | XAR |
| 15 | Nuclear | 29.65 | strong downtrend | negative | weak | 35.91 | NLR | NLR |

### Thematic Strength

| Rank | Theme | Score | Setup | Dispersion | Price | News |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Healthcare Innovation | 63.18 | Positive setup | 12.01 | True | False |
| 2 | Semiconductors | 61.99 | Positive setup | 19.68 | True | False |
| 3 | Financials | 61.7 | Positive setup | 4.02 | True | False |
| 4 | Small Caps | 58.53 | Positive setup | 0.0 | False | False |
| 5 | Cybersecurity | 56.69 | Neutral / watchlist | 94.92 | False | False |
| 6 | Dividend Defensives | 55.31 | Neutral / watchlist | 6.83 | False | False |
| 7 | AI Infrastructure | 54.13 | Neutral / watchlist | 10.44 | False | False |
| 8 | Quality Growth | 52.38 | Neutral / watchlist | 11.23 | False | False |
| 9 | Grid Infrastructure | 50.57 | Neutral / watchlist | 7.3 | False | False |
| 10 | Defense | 41.71 | Weak setup | 26.83 | False | False |
| 11 | Energy | 40.51 | Weak setup | 2.35 | False | False |
| 12 | Nuclear | 29.43 | Weak setup | 17.59 | False | False |
| 13 | Crypto Infrastructure | 28.67 | Underperformance risk | 21.27 | False | False |

- Top 5 improving themes: Cybersecurity, Semiconductors, Healthcare Innovation, AI Infrastructure, Quality Growth
- Top 5 deteriorating themes: Crypto Infrastructure, Nuclear, Defense, Energy, Grid Infrastructure
- Strong news but weak price confirmation: none
- Strong price but weak news confirmation: Healthcare Innovation, Semiconductors, Financials

### Sector / Theme Alignment

| Sector | Related Themes | Sector Score | Sector Signal | Theme Score | Theme Signal | Interpretation |
| --- | --- | --- | --- | --- | --- | --- |
| Cybersecurity | Cybersecurity | 74.32 | strong | 56.69 | positive | sector and theme confirmation |
| Financials | Financials | 68.38 | strong | 61.7 | positive | sector and theme confirmation |
| Healthcare | Healthcare Innovation | 68.0 | strong | 63.18 | positive | sector and theme confirmation |
| Industrials | Defense, Grid Infrastructure | 66.07 | strong | 46.14 | mixed | sector stronger than related themes |
| Technology | AI Infrastructure, Semiconductors, Quality Growth | 64.97 | positive | 56.16 | positive | sector and theme confirmation |
| Semiconductors | AI Infrastructure, Semiconductors | 63.77 | positive | 58.06 | positive | sector and theme confirmation |
| Real Estate | Dividend Defensives | 59.88 | positive | 55.31 | positive | sector and theme confirmation |
| Consumer Staples | Dividend Defensives | 59.64 | positive | 55.31 | positive | sector and theme confirmation |
| Utilities | Grid Infrastructure, Nuclear, Dividend Defensives | 59.6 | positive | 45.1 | mixed | sector stronger than related themes |
| Crypto | Crypto Infrastructure | 50.0 | mixed | 28.67 | very weak | mixed confirmation |
| Consumer Discretionary | Small Caps | 47.32 | mixed | 58.53 | positive | theme stronger than official sector |
| Grid Infrastructure | Grid Infrastructure | 44.51 | weak | 50.57 | mixed | mixed confirmation |
| Energy | Energy | 40.87 | weak | 40.51 | weak | broad weakness across sector and themes |
| Defense | Defense | 38.92 | weak | 41.71 | weak | broad weakness across sector and themes |
| Nuclear | Nuclear | 29.65 | very weak | 29.43 | very weak | broad weakness across sector and themes |

## Three-Month Outperformance Setup

| Rank | Theme | Score | Classification | Drivers | Invalidation Triggers |
| --- | --- | --- | --- | --- | --- |
| 1 | Healthcare Innovation | 65.73 | Positive setup | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 2 | Semiconductors | 65.57 | Positive setup | relative_strength_60d, trend_persistence, breadth, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 3 | Financials | 63.85 | Positive setup | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 4 | Small Caps | 63.36 | Positive setup | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 5 | Dividend Defensives | 57.35 | Neutral / watchlist | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 6 | AI Infrastructure | 56.66 | Neutral / watchlist | trend_persistence, breadth | relative strength below SPY, breadth below 45%, news turns negative |
| 7 | Cybersecurity | 56.29 | Neutral / watchlist | relative_strength_60d, trend_persistence, breadth, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 8 | Quality Growth | 54.67 | Neutral / watchlist | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 9 | Grid Infrastructure | 53.96 | Neutral / watchlist | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 10 | Energy | 39.82 | Weak setup | downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 11 | Defense | 38.95 | Weak setup |  | relative strength below SPY, breadth below 45%, news turns negative |
| 12 | Nuclear | 30.43 | Weak setup |  | relative strength below SPY, breadth below 45%, news turns negative |

## Breadth and Participation

- Above 50DMA: `60.0%`
- Above 200DMA: `72.88%`
- Positive 20D return: `78.33%`

## Volatility and Risk Signals

- VIX close=15.03 pct_chg=-5.11

## News Analytics

- Sentiment counts: {'positive': 42, 'negative': 25, 'neutral': 13}
- News confirmation score: `60.62`

### Top Market-Moving Headlines

**1. The dot-com crash was a $5 trillion blip. Why the next financial crisis could hit 4 times harder.**
- Source: MarketWatch Top Stories
- Importance / impact: Medium / Negative
- Relevance / horizon: sector_theme / medium-term
- Affected assets: financial crisis, market outlook
- Score: `48.05`
- Investment implication: Theme or sector negative signal; requires price and volume confirmation before affecting rankings.

**2. Trump threatens to 'decimate' Iran if it tries to kill him, as Treasury sanctions alleged Iranian financier**
- Source: CNBC Business Headlines
- Importance / impact: High / Negative
- Relevance / horizon: macro / short-term
- Affected assets: U.S, geopolitical_risk, defense
- Score: `47.6`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the short-term.

**3. Buy these dividend-paying real estate stocks ahead of earnings, says UBS**
- Source: CNBC Markets
- Importance / impact: Medium / Positive
- Relevance / horizon: sector_theme / short-term
- Affected assets: UBS, senior housing stocks, skilled nursing facilities, real estate, dividends
- Score: `41.18`
- Investment implication: Theme or sector positive signal; requires price and volume confirmation before affecting rankings.

**4. Elon Musk speaks exclusively to CNBC about Grok, Tesla and the SpaceX IPO: Live updates**
- Source: CNBC Markets
- Importance / impact: Medium / Positive
- Relevance / horizon: sector_theme / short-term
- Affected assets: CNBC, IPO, AI
- Score: `41.18`
- Investment implication: Theme or sector positive signal; requires price and volume confirmation before affecting rankings.

**5. How Apple stock rode the AI rollercoaster to record highs in 1 chart**
- Source: CNBC Markets
- Importance / impact: Medium / Positive
- Relevance / horizon: single_name / long-term
- Affected assets: AAPL, AI, Apple
- Score: `40.15`
- Investment implication: Single-name positive signal; low weight unless it maps to a broader sector or theme.

**6. Meta’s stock roars back to life as it notches its best week in years**
- Source: MarketWatch Top Stories
- Importance / impact: Medium / Positive
- Relevance / horizon: single_name / short-term
- Affected assets: META, AI, Tech
- Score: `37.29`
- Investment implication: Single-name positive signal; low weight unless it maps to a broader sector or theme.

**7. Meta’s stock roars back to life as it notches its best week in years**
- Source: MarketWatch Bulletins
- Importance / impact: Medium / Positive
- Relevance / horizon: single_name / short-term
- Affected assets: META, technology, social media
- Score: `35.43`
- Investment implication: Single-name positive signal; low weight unless it maps to a broader sector or theme.

**8. Meta's stock has best week since early 2024 as optimism builds around AI strategy**
- Source: CNBC Markets
- Importance / impact: Medium / Positive
- Relevance / horizon: single_name / short-term
- Affected assets: META, AI, Meta
- Score: `35.43`
- Investment implication: Single-name positive signal; low weight unless it maps to a broader sector or theme.

**9. Stablecoin issuer Circle just got the greenlight to operate as a bank. The shares are up 5%**
- Source: CNBC Top News
- Importance / impact: Medium / Positive
- Relevance / horizon: single_name / short-term
- Affected assets: CRL, U.S, banking, cryptocurrency
- Score: `35.43`
- Investment implication: Single-name positive signal; low weight unless it maps to a broader sector or theme.

**10. Dow climbing over 200 points as U.S. stocks build on gains in final hour — live**
- Source: MarketWatch Bulletins
- Importance / impact: Medium / Positive
- Relevance / horizon: single_name / short term
- Affected assets: U.S, Stock Market
- Score: `35.43`
- Investment implication: Single-name positive signal; low weight unless it maps to a broader sector or theme.


### Headline Quality Checks

Noisy headline list: Slumping AI stocks could be really good news for y, The bar is high for S&P 500 earnings, but these as

## Positioning & Flow Dashboard

Positioning and flow data is used as confirmation only. FINRA short-sale volume is not short interest.

### ETF Fund Flows

Net fund flow is estimated from ETF shares outstanding changes multiplied by NAV. Flows are grouped into broad-market, fixed-income/macro, and sector/thematic ETFs.

**Broad Market ETF Flows**

| Date | ETF / Segment | 1D Net Flow | 5D Net Flow | Rule-Based Comment |
| --- | --- | --- | --- | --- |
| 2026-07-10 | IVV - Broad Equity | -$1,971,998,753 | -$5,878,073,207 | 1D outflow; 5D outflow. |
| 2026-07-10 | IWM - Small Caps | $1,109,200,189 | $1,138,778,860 | 1D inflow; 5D inflow. |
| 2026-07-09 | SPY - Broad Equity | -$2,443,000,852 | -$601,354,056 | 1D outflow; 5D outflow. |
| 2026-07-10 | IWD - Value | -$24,689,512 | $493,790,232 | 1D outflow; 5D inflow. |
| 2026-07-10 | IJH - Mid Caps | $0 | $416,066,607 | 1D flat; 5D inflow. |
| 2026-07-10 | IWF - Growth | $185,924,170 | -$371,848,341 | 1D inflow; 5D outflow. |
| 2026-07-10 | IXUS - International Equity | $0 | $341,915,566 | 1D flat; 5D inflow. |
| 2026-07-10 | EFA - Developed Markets ex-US | $0 | -$312,584,514 | 1D flat; 5D outflow. |
| 2026-07-09 | DIA - Dow Industrials | -$78,638,039 | $288,339,476 | 1D outflow; 5D inflow. |
| 2026-07-10 | ITOT - Total U.S. Equity | $33,106,189 | $273,126,063 | 1D inflow; 5D inflow. |

**Fixed Income / Macro ETF Flows**

| Date | ETF / Segment | 1D Net Flow | 5D Net Flow | Rule-Based Comment |
| --- | --- | --- | --- | --- |
| 2026-07-10 | SGOV - Treasury Bills | $653,269,090 | $2,864,333,704 | 1D inflow; 5D inflow. |
| 2026-07-10 | LQD - Investment Grade Credit | $483,685,168 | $1,752,015,166 | 1D inflow; 5D inflow. |
| 2026-07-10 | TLT - Long Duration Treasury | $591,121,713 | $1,596,028,625 | 1D inflow; 5D inflow. |
| 2026-07-10 | HYG - High Yield Credit | -$421,951,396 | -$1,027,013,776 | 1D outflow; 5D outflow. |
| 2026-07-10 | AGG - Core Bonds | $107,865,997 | $774,673,976 | 1D inflow; 5D inflow. |
| 2026-07-10 | SHY - Short Treasury | -$49,119,398 | $335,649,218 | 1D outflow; 5D inflow. |
| 2026-07-10 | IUSB - Core Bonds | $64,027,548 | $237,816,608 | 1D inflow; 5D inflow. |
| 2026-07-10 | GOVT - U.S. Treasuries | $88,056,423 | $207,722,844 | 1D inflow; 5D inflow. |
| 2026-07-10 | GLD - Gold | -$376,138,716 | $188,069,358 | 1D outflow; 5D inflow. |
| 2026-07-10 | IEF - Intermediate Treasury | -$9,361,177 | $159,140,011 | 1D outflow; 5D inflow. |

**Sector / Thematic ETF Flows**

| Date | ETF / Segment | 1D Net Flow | 5D Net Flow | Rule-Based Comment |
| --- | --- | --- | --- | --- |
| 2026-07-10 | SOXX - Semiconductors | -$1,191,479,588 | $5,986,458,416 | 1D outflow; 5D inflow. |
| 2026-07-09 | SMH - Semiconductors | $698,871,830 | $3,099,381,666 | 1D inflow; 5D inflow. |
| 2026-07-09 | XLP - Consumer Staples | -$24,967,242 | $607,536,222 | 1D outflow; 5D inflow. |
| 2026-07-09 | XLI - Industrials | $81,504,857 | $570,534,001 | 1D inflow; 5D inflow. |
| 2026-07-09 | XLF - Financials | -$16,662,784 | $547,094,738 | 1D outflow; 5D inflow. |
| 2026-07-09 | XLE - Energy | -$21,923,620 | -$465,876,934 | 1D outflow; 5D outflow. |
| 2026-07-10 | QUAL - Quality Factor | $32,951,485 | $461,320,786 | 1D inflow; 5D inflow. |
| 2026-07-10 | DYNF - Equity Factor Rotation | $119,217,483 | $435,995,366 | 1D inflow; 5D inflow. |
| 2026-07-09 | XLU - Utilities | -$11,280,378 | $419,630,071 | 1D outflow; 5D inflow. |
| 2026-07-09 | XLC - Communication Services | -$55,278,041 | -$370,362,875 | 1D outflow; 5D outflow. |

### Deferred Flow Sections

- Official ETF / fund flows: current report uses shares-outstanding-derived net fund flow estimates from free ETF metadata.
- Institutional Ownership: not available until SEC 13F ingestion is implemented.
- Crowding / Squeeze Risks: initial coverage uses CFTC crowded positioning and FINRA elevated short-sale volume only.
- Flow-Confirmed vs Price-Only Themes: partial coverage through ETF flow proxies; stronger coverage requires issuer/ICI adapters.

## Contradiction / Audit Flags

No contradiction flags were triggered by current deterministic rules.

## Data Quality Notes

- Technical rows loaded: `60`
- S&P 500 constituent technical rows loaded: `503`
- Macro rows loaded: `29`
- Economic rows loaded: `113`
- News rows loaded: `80`
- Positioning/flow rows loaded: `30`

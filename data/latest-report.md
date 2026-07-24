# Rule-Based Institutional Market Update

Generated at: 24 July 2026, 12:11:43 (HKT)
Window: 24h

## Executive Dashboard

- Regime score: **50.83 / 100** (Mixed / Rotation)
- US equity strength: **54.73 / 100** (neutral)
- Evidence quality: **76.0 / 100**
- ETF flow contribution: **46.79 / 100**, reliability **65.76 / 100**
- Breadth: **healthy**; above 50DMA `50.0%`, above 200DMA `69.49%`
- Top sector score: **Financials** `66.08`
- Top theme score: **Energy** `61.94`

## Market Regime Score

| Metric | Value | Driver / Interpretation |
| --- | --- | --- |
| Overall regime | 50.83 | Mixed / Rotation |
| equity_trend | 61.25 | mild risk-on support; Core equity ETFs versus moving averages. |
| equity_momentum | 51.24 | neutral / mixed; 5D/20D/60D return momentum across SPY, QQQ, IWM, and SMH. |
| market_breadth | 58.16 | mild risk-on support; Participation breadth from tracked equity/ETF rows. |
| volatility | 20.0 | risk-off pressure; VIX level and change; higher score means calmer volatility conditions. |
| rates_yield_curve | 58.0 | mild risk-on support; Treasury yield pressure and curve shape; higher score means less rates pressure. |
| credit_proxy | 50.0 | neutral / mixed; Credit-market proxy; currently neutral when no direct spread signal is available. |
| dollar_fx | 53.57 | neutral / mixed; Dollar move; higher score means less USD tightening pressure. |
| commodity_confirmation | 38.0 | mild risk-off pressure; Copper, silver, oil, and gold mix; higher score means better cyclical confirmation. |
| etf_flow | 47.89 | neutral / mixed; Grouped ETF flow contribution adjusted for reliability. |
| news_confirmation | 62.5 | mild risk-on support; Weighted headline/news confirmation score. |
| Positive contributors |  | news_confirmation=62.5, equity_trend=61.25 |
| Negative contributors |  | volatility=20.0, commodity_confirmation=38.0 |

## US Equity Strength Score

| Component | Score |
| --- | --- |
| indices_above_moving_averages | 61.25 |
| sp500_trend | 55.0 |
| nasdaq_trend | 55.0 |
| russell_participation | 80.0 |
| returns_momentum | 51.24 |
| rsi_zone | 40.0 |
| macd_confirmation | 35.0 |
| volume_confirmation | 46.25 |
| breadth | 58.16 |

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
| Dollar | DXY proxy rising | A stronger dollar can tighten financial conditions and pressure commodities/emerging-market risk. |
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
| ^GSPC | S&P 500 | 7408.3 | -1.21 | 2026-07-23 | closed |
| ^IXIC | NASDAQ Composite | 25137.69 | -2.15 | 2026-07-23 | closed |
| ^RUT | Russell 2000 Index | 2940.16 | -0.67 | 2026-07-23 | closed |
| ^VIX | CBOE Volatility Index | 18.7 | 12.38 | 2026-07-23 | closed |
| ^MOVE | ICE BofA MOVE Index | 80.08 | 12.98 | 2026-07-23 | closed |
| ^FVX | Treasury Yield 5 Years | 4.46 | 1.23 | 2026-07-23 | closed |
| ^TNX | Treasury Yield 10 Years | 4.7 | 0.99 | 2026-07-23 | closed |
| ^TYX | Treasury Yield 30 Years | 5.17 | 0.47 | 2026-07-23 | closed |
| DX-Y.NYB | US Dollar Index | 101.43 | 0.29 | 2026-07-23 | closed |
| HYG | iShares iBoxx High Yield Corporate Bond ETF | 79.23 | -0.36 | 2026-07-23 | closed |
| LQD | iShares iBoxx Investment Grade Corporate Bond ETF | 106.26 | -0.38 | 2026-07-23 | closed |
| JNK | SPDR Bloomberg High Yield Bond ETF | 95.4 | -0.37 | 2026-07-23 | closed |
| RSP | Invesco S&P 500 Equal Weight ETF | 211.92 | -0.37 | 2026-07-23 | closed |
| IWF | iShares Russell 1000 Growth ETF | 118.59 | -1.93 | 2026-07-23 | closed |
| IWD | iShares Russell 1000 Value ETF | 246.18 | -0.54 | 2026-07-23 | closed |
| TLT | iShares 20+ Year Treasury Bond ETF | 83.17 | -0.32 | 2026-07-23 | closed |
| IEF | iShares 7-10 Year Treasury Bond ETF | 92.85 | -0.27 | 2026-07-23 | closed |
| SHY | iShares 1-3 Year Treasury Bond ETF | 81.77 | -0.07 | 2026-07-23 | closed |
| GC=F | Gold Future | 4052.3 | -2.28 | 2026-07-23 | closed |
| SI=F | Silver Future | 57.9 | -3.54 | 2026-07-23 | closed |
| CL=F | WTI Crude Oil Future | 92.36 | 6.37 | 2026-07-23 | closed |
| HG=F | Copper Future | 6.34 | -1.76 | 2026-07-23 | closed |

## Market Dispersion Analysis

- Sector ETF 20D dispersion: `16.33` points (high); leader `XLE` (Energy) `10.85`, laggard `XLY` (Consumer Discretionary) `-5.48`
- Sector ETF 60D dispersion: `21.54` points (very high); leader `XLV` (Health Care) `12.53`, laggard `XLC` (Communication Services) `-9.01`

| Comparison | Left | Right | 20D Spread | Signal |
| --- | --- | --- | --- | --- |
| Equal-weight vs cap-weight | RSP (Equal-weight S&P 500) | SPY (S&P 500) | 0.06 | balanced |
| Small-cap vs large-cap | IWM (Russell 2000) | SPY (S&P 500) | -2.22 | large-cap leadership |
| Growth vs value | IWF (Russell 1000 Growth) | IWD (Russell 1000 Value) | -3.05 | value leadership |
| Nasdaq vs S&P 500 | QQQ (Nasdaq 100) | SPY (S&P 500) | -3.3 | S&P 500 leadership |

## Sector Constituent Dispersion

- Breadth 50D / 200D: percentage of active S&P 500 constituents in the sector trading above the 50-day / 200-day moving average.
- Positive 20D: percentage of active sector constituents with positive 20-day return.
- Std 20D: cross-sectional standard deviation of constituent 20-day returns; higher means wider stock-level dispersion.

| Sector | Count | Breadth 50D | Breadth 200D | Positive 20D | 20D Dispersion | Std 20D | Label | Leaders | Laggards |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Information Technology | 74 | 28.38 | 60.27 | 45.95 | 86.9 | 12.81 | very high | PANW, DDOG, AAPL | GLW, MRVL, CRWD |
| Industrials | 81 | 65.82 | 71.43 | 59.26 | 44.83 | 8.65 | very high | CTAS, UNP, CHRW | PNR, BLDR, GNRC |
| Materials | 26 | 42.31 | 61.54 | 42.31 | 43.83 | 8.45 | very high | CF, CTVA, LYB | MLM, CRH, ALB |
| Financials | 76 | 80.56 | 72.86 | 78.95 | 39.98 | 6.25 | very high | PYPL, TRV, GPN | PGR, ERIE, C |
| Health Care | 59 | 71.19 | 62.71 | 76.27 | 39.28 | 6.26 | very high | TECH, TMO, CRL | MRNA, EW, ISRG |
| Energy | 21 | 85.71 | 85.71 | 85.71 | 30.19 | 8.27 | very high | MPC, VLO, PSX | BKR, WMB, HAL |
| Consumer Discretionary | 47 | 25.53 | 38.3 | 21.28 | 27.26 | 5.93 | very high | DPZ, BBY, GPC | CCL, DHI, TSLA |
| Consumer Staples | 34 | 54.55 | 62.5 | 38.24 | 24.62 | 5.59 | very high | ADM, BG, KHC | HSY, WMT, STZ |
| Communication Services | 23 | 18.18 | 31.82 | 39.13 | 23.55 | 6.56 | very high | FOXA, META, FOX | ECHO, TKO, PSKY |
| Real Estate | 31 | 61.29 | 74.19 | 51.61 | 22.33 | 5.25 | very high | VTR, WELL, DOC | DLR, CSGP, CCI |
| Utilities | 31 | 96.77 | 87.1 | 67.74 | 10.36 | 2.28 | moderate | EIX, ES, VST | DTE, PEG, CMS |

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
| Advance Retail Sales | 768553.0 | millions dollars | 1677.0 millions dollars vs prior | 2026-06-01 | Higher reading supports activity or liquidity. |

### U.S. Inflation

| Indicator | Latest | Unit | Change | Date | Rule-Based Interpretation |
| --- | --- | --- | --- | --- | --- |
| Headline CPI month-over-month inflation rate | -0.42 | percent | -0.9 pp vs prior | 2026-06-01 | Lower reading eases macro pressure. |
| Headline CPI year-over-year inflation rate | 3.73 | percent | -0.54 pp vs prior | 2026-06-01 | Lower reading eases macro pressure. |
| Core CPI month-over-month inflation rate | -0.02 | percent | -0.22 pp vs prior | 2026-06-01 | Lower reading eases macro pressure. |
| Core CPI year-over-year inflation rate | 2.81 | percent | -0.15 pp vs prior | 2026-06-01 | Lower reading eases macro pressure. |
| Headline CPI year-over-year inflation rate | 3.88 | percent | -0.58 pp vs prior | 2026-06-01 | Lower reading eases macro pressure. |
| Core CPI year-over-year inflation rate | 2.86 | percent | -0.21 pp vs prior | 2026-06-01 | Lower reading eases macro pressure. |
| Headline PCE Price Index month-over-month inflation rate | 0.45 | percent | 0.04 pp vs prior | 2026-05-01 | Higher reading increases macro pressure. |
| Headline PCE Price Index year-over-year inflation rate | 4.07 | percent | 0.28 pp vs prior | 2026-05-01 | Higher reading increases macro pressure. |
| Core PCE Price Index month-over-month inflation rate | 0.32 | percent | 0.07 pp vs prior | 2026-05-01 | Higher reading increases macro pressure. |
| Core PCE Price Index year-over-year inflation rate | 3.41 | percent | 0.09 pp vs prior | 2026-05-01 | Higher reading increases macro pressure. |
| Headline PPI Final Demand month-over-month inflation rate | -0.19 | percent | -0.79 pp vs prior | 2026-06-01 | Lower reading eases macro pressure. |
| Headline PPI Final Demand year-over-year inflation rate | 5.51 | percent | -0.49 pp vs prior | 2026-06-01 | Lower reading eases macro pressure. |
| Core PPI Final Demand Less Foods and Energy month-over-month inflation rate | 0.2 | percent | 0.11 pp vs prior | 2026-06-01 | Higher reading increases macro pressure. |
| Core PPI Final Demand Less Foods and Energy year-over-year inflation rate | 4.68 | percent | 0.09 pp vs prior | 2026-06-01 | Higher reading increases macro pressure. |
| Consumer Price Index for All Urban Consumers | 332.57 | index 1982-1984=100 | -1.41 index pts vs prior | 2026-06-01 | Lower reading eases macro pressure. |
| Core CPI | 336.06 | index 1982-1984=100 | -0.06 index pts vs prior | 2026-06-01 | Lower reading eases macro pressure. |
| Personal Consumption Expenditures Price Index | 131.53 | index 2017=100 | 0.59 index pts vs prior | 2026-05-01 | Higher reading increases macro pressure. |
| Core PCE Price Index | 130.08 | index 2017=100 | 0.41 index pts vs prior | 2026-05-01 | Higher reading increases macro pressure. |
| Producer Price Index: Final Demand | 157.04 | index Nov 2009=100 | -0.3 index pts vs prior | 2026-06-01 | Latest structural macro observation. |
| Producer Price Index: Final Demand Less Foods and Energy | 154.0 | index Apr 2010=100 | 0.31 index pts vs prior | 2026-06-01 | Latest structural macro observation. |

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
| New Privately-Owned Housing Units Authorized | 1367.0 | thousands | -43.0 thousands vs prior | 2026-06-01 | Lower reading signals softer activity or liquidity. |
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
| US dollar/Euro ECB reference exchange rate | 1.14 | USD | -0.0 USD vs prior | 2026-07-23 | EUR weakened versus this currency. |
| Japanese yen/Euro ECB reference exchange rate | 186.23 | JPY | 0.2 JPY vs prior | 2026-07-23 | EUR strengthened versus this currency. |
| Chinese yuan renminbi/Euro ECB reference exchange rate | 7.71 | CNY | -0.01 CNY vs prior | 2026-07-23 | EUR weakened versus this currency. |
| Australian dollar/Euro ECB reference exchange rate | 1.63 | AUD | -0.0 AUD vs prior | 2026-07-23 | EUR weakened versus this currency. |

ABS Australia note: ABS rows are stored locally/Neon, but most series are dimension-coded; only curated series should be promoted into narrative report text.

## Sector and Theme Leadership

### Official Sector Strength

Supporting and detracting names are the top/bottom S&P 500 constituents by 20D return when constituent coverage is available; otherwise the report falls back to related ETFs.

| Rank | Sector | Score | Trend | Momentum | Stock Breadth | ETF Flow | Flow Reliability | 3M RS | Supporting / Leaders | Detracting / Laggards |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Financials | 66.08 | strong uptrend | neutral | broad | 72.19 | 65.0 | 53.77 | PYPL, TRV, GPN | PGR, ERIE, C |
| 2 | Real Estate | 65.56 | strong uptrend | neutral | broad | 51.36 | 65.0 | 50.24 | VTR, WELL, DOC | DLR, CSGP, CCI |
| 3 | Utilities | 61.72 | strong uptrend | neutral | broad | 50.0 | 0.0 | 48.43 | EIX, ES, VST | DTE, PEG, CMS |
| 4 | Industrials | 61.27 | strong uptrend | neutral | broad | 50.0 | 0.0 | 51.07 | CTAS, UNP, CHRW | PNR, BLDR, GNRC |
| 5 | Healthcare | 61.22 | strong uptrend | positive | broad | 43.66 | 65.0 | 56.49 | TECH, TMO, CRL | MRNA, EW, ISRG |
| 6 | Energy | 60.88 | uptrend | positive | broad | 55.82 | 65.0 | 56.66 | MPC, VLO, PSX | BKR, WMB, HAL |
| 7 | Cybersecurity | 60.17 | strong uptrend | positive | broad | 50.0 | 0.0 | 63.06 | CIBR | CIBR |
| 8 | Crypto | 49.49 | neutral | neutral | mixed | 44.89 | 65.0 | 50.0 |  |  |
| 9 | Semiconductors | 47.54 | neutral | neutral | weak | 57.73 | 65.0 | 51.05 | SMH, SOXX | SOXX, SMH |
| 10 | Defense | 46.49 | neutral | neutral | weak | 50.0 | 0.0 | 49.84 | XAR | XAR |
| 11 | Technology | 45.32 | neutral | neutral | weak | 34.73 | 65.0 | 49.83 | PANW, DDOG, AAPL | GLW, MRVL, CRWD |
| 12 | Consumer Staples | 42.29 | downtrend | neutral | weak | 50.0 | 0.0 | 47.86 | ADM, BG, KHC | HSY, WMT, STZ |
| 13 | Grid Infrastructure | 41.05 | downtrend | neutral | weak | 50.0 | 0.0 | 44.01 | GRID | GRID |
| 14 | Nuclear | 34.7 | strong downtrend | negative | weak | 50.0 | 0.0 | 34.61 | NLR | NLR |
| 15 | Consumer Discretionary | 32.78 | strong downtrend | negative | weak | 50.0 | 0.0 | 41.94 | DPZ, BBY, GPC | CCL, DHI, TSLA |

### Thematic Strength

| Rank | Theme | Score | Setup | ETF Flow | Flow Reliability | Dispersion | Price | News |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Energy | 61.94 | Positive setup | 55.82 | 65.0 | 3.76 | True | False |
| 2 | Financials | 61.91 | Positive setup | 72.19 | 65.0 | 6.35 | True | False |
| 3 | Healthcare Innovation | 58.62 | Positive setup | 43.66 | 65.0 | 4.09 | False | False |
| 4 | Small Caps | 56.56 | Positive setup | 52.48 | 65.0 | 0.0 | False | False |
| 5 | Semiconductors | 52.21 | Neutral / watchlist | 57.73 | 65.0 | 13.26 | False | False |
| 6 | Defense | 52.11 | Neutral / watchlist | 50.0 | 0.0 | 16.34 | False | False |
| 7 | Grid Infrastructure | 50.89 | Neutral / watchlist | 50.0 | 0.0 | 9.46 | False | False |
| 8 | Dividend Defensives | 50.71 | Neutral / watchlist | 57.21 | 65.0 | 6.73 | False | False |
| 9 | Cybersecurity | 49.7 | Neutral / watchlist | 50.0 | 0.0 | 86.9 | False | False |
| 10 | Quality Growth | 46.39 | Neutral / watchlist | 62.52 | 65.0 | 17.74 | False | False |
| 11 | AI Infrastructure | 43.01 | Weak setup | 57.73 | 65.0 | 13.26 | False | False |
| 12 | Crypto Infrastructure | 32.29 | Underperformance risk | 44.89 | 65.0 | 7.89 | False | False |
| 13 | Nuclear | 31.07 | Underperformance risk | 50.0 | 0.0 | 16.03 | False | False |

- Top 5 improving themes: Cybersecurity, Healthcare Innovation, Semiconductors, Financials, Small Caps
- Top 5 deteriorating themes: Crypto Infrastructure, Nuclear, Grid Infrastructure, Defense, AI Infrastructure
- Strong news but weak price confirmation: none
- Strong price but weak news confirmation: Energy, Financials

### Sector / Theme Alignment

| Sector | Related Themes | Sector Score | Sector Signal | Theme Score | Theme Signal | Interpretation |
| --- | --- | --- | --- | --- | --- | --- |
| Financials | Financials | 66.08 | strong | 61.91 | positive | sector and theme confirmation |
| Real Estate | Dividend Defensives | 65.56 | strong | 50.71 | mixed | sector stronger than related themes |
| Utilities | Grid Infrastructure, Nuclear, Dividend Defensives | 61.72 | positive | 44.22 | weak | sector stronger than related themes |
| Industrials | Defense, Grid Infrastructure | 61.27 | positive | 51.5 | mixed | sector stronger than related themes |
| Healthcare | Healthcare Innovation | 61.22 | positive | 58.62 | positive | sector and theme confirmation |
| Energy | Energy | 60.88 | positive | 61.94 | positive | sector and theme confirmation |
| Cybersecurity | Cybersecurity | 60.17 | positive | 49.7 | mixed | sector stronger than related themes |
| Crypto | Crypto Infrastructure | 49.49 | mixed | 32.29 | very weak | mixed confirmation |
| Semiconductors | AI Infrastructure, Semiconductors | 47.54 | mixed | 47.61 | mixed | mixed confirmation |
| Defense | Defense | 46.49 | mixed | 52.11 | mixed | mixed confirmation |
| Technology | AI Infrastructure, Semiconductors, Quality Growth | 45.32 | mixed | 47.2 | mixed | mixed confirmation |
| Consumer Staples | Dividend Defensives | 42.29 | weak | 50.71 | mixed | mixed confirmation |
| Grid Infrastructure | Grid Infrastructure | 41.05 | weak | 50.89 | mixed | mixed confirmation |
| Nuclear | Nuclear | 34.7 | very weak | 31.07 | very weak | broad weakness across sector and themes |
| Consumer Discretionary | Small Caps | 32.78 | very weak | 56.56 | positive | theme stronger than official sector |

## Three-Month Outperformance Setup

| Rank | Theme | Score | Classification | Drivers | Invalidation Triggers |
| --- | --- | --- | --- | --- | --- |
| 1 | Healthcare Innovation | 67.44 | Positive setup | relative_strength_60d, trend_persistence, breadth, downside_volatility, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 2 | Financials | 66.21 | Positive setup | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 3 | Small Caps | 65.38 | Positive setup | trend_persistence, breadth, volume_accumulation, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 4 | Energy | 63.41 | Positive setup | relative_strength_20d, trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 5 | Dividend Defensives | 55.22 | Neutral / watchlist | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 6 | Semiconductors | 54.95 | Neutral / watchlist | relative_strength_60d, trend_persistence, breadth, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 7 | Grid Infrastructure | 54.04 | Neutral / watchlist | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 8 | Cybersecurity | 53.22 | Neutral / watchlist | relative_strength_60d, trend_persistence, breadth, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 9 | Defense | 52.33 | Neutral / watchlist | volume_accumulation | relative strength below SPY, breadth below 45%, news turns negative |
| 10 | Quality Growth | 47.97 | Neutral / watchlist | downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 11 | AI Infrastructure | 44.43 | Weak setup | downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 12 | Nuclear | 28.12 | Underperformance risk |  | relative strength below SPY, breadth below 45%, news turns negative |

## Breadth and Participation

- Above 50DMA: `50.0%`
- Above 200DMA: `69.49%`
- Positive 20D return: `55.0%`

## Volatility and Risk Signals

- VIX close=18.7 pct_chg=12.38

## News Analytics

- Sentiment counts: {'positive': 50, 'negative': 30, 'neutral': 0}
- News confirmation score: `62.5`

### Top Market-Moving Headlines

**1. Brent crude crosses $100 after tankers reportedly struck off Saudi Arabia**
- Source: CNBC Markets
- Importance / impact: High / Positive
- Relevance / horizon: macro / short term
- Affected assets: U.S, Geopolitical Risk, Energy
- Score: `61.77`
- Investment implication: Macro-relevant positive signal; use as context for rates, volatility, and index confirmation over the short term.

**2. Stocks slump after earnings disappoint and oil hits $100 a barrel — live updates**
- Source: MarketWatch Bulletins
- Importance / impact: High / Negative
- Relevance / horizon: macro / short-term
- Affected assets: earnings_disappointments, oil_prices
- Score: `61.77`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the short-term.

**3. CNBC Daily Open: Brent crude is back at $100 — and Trump renews tariffs**
- Source: CNBC Technology
- Importance / impact: High / Negative
- Relevance / horizon: macro / short-term
- Affected assets: CNBC, oil prices, geo-political tensions, AI spending concerns
- Score: `54.0`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the short-term.

**4. Trump rolls out a new wave of global tariffs. Here are the latest rates.**
- Source: MarketWatch Top Stories
- Importance / impact: High / Negative
- Relevance / horizon: macro / short-term
- Affected assets: U.S, trade
- Score: `51.0`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the short-term.

**5. Japan’s $1.8 trillion pension giant might bring money home. That could jolt U.S. stocks and the Fed.**
- Source: MarketWatch Top Stories
- Importance / impact: High / Negative
- Relevance / horizon: macro / short-term
- Affected assets: U.S, foreign assets, pension funds, U.S. stocks
- Score: `51.0`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the short-term.

**6. Global oil prices top $100 after Houthis claim strikes on Saudi Arabian tankers**
- Source: MarketWatch Top Stories
- Importance / impact: High / Positive
- Relevance / horizon: macro / short-term
- Affected assets: commodity_market, geopolitical_risk
- Score: `51.0`
- Investment implication: Macro-relevant positive signal; use as context for rates, volatility, and index confirmation over the short-term.

**7. Brent Hits $100 Again as Houthi Attacks Threaten Further Supply Squeeze**
- Source: Dow Jones US Business
- Importance / impact: High / Positive
- Relevance / horizon: macro / short-term
- Affected assets: crude_oil_prices, geopolitical_risk
- Score: `48.77`
- Investment implication: Macro-relevant positive signal; use as context for rates, volatility, and index confirmation over the short-term.

**8. Odds of Federal Reserve rate hike surge as oil prices rip higher**
- Source: CNBC Markets
- Importance / impact: High / Positive
- Relevance / horizon: macro / short-term
- Affected assets: Federal Reserve policy, oil prices
- Score: `48.45`
- Investment implication: Macro-relevant positive signal; use as context for rates, volatility, and index confirmation over the short-term.

**9. Shortsighted stock market can no longer brush off war: 'It's too hard to ignore $100 oil'**
- Source: CNBC Top News
- Importance / impact: High / Negative
- Relevance / horizon: macro / short-term
- Affected assets: U.S, oil prices, geopolitical risk
- Score: `48.45`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the short-term.

**10. U.S. to see higher generic drug prices thanks to tariffs, CEO of leading India pharma firm warns**
- Source: CNBC Technology
- Importance / impact: High / Negative
- Relevance / horizon: macro / short-term
- Affected assets: DRRX, U.S, tariffs, pharmaceuticals
- Score: `46.8`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the short-term.


### Headline Quality Checks

No noisy headlines detected by current rules.

## Positioning & Flow Dashboard

Positioning and flow data is used as confirmation only. FINRA short-sale volume is not short interest.

### Deferred Flow Sections

- Official ETF / fund flows: current report uses shares-outstanding-derived net fund flow estimates from free ETF metadata.
- Institutional Ownership: not available until SEC 13F ingestion is implemented.
- Crowding / Squeeze Risks: initial coverage uses CFTC crowded positioning and FINRA elevated short-sale volume only.
- Grouped exposure flow reliability: use issuer coverage and availability status before treating ETF flow as confirmation.

## ETF Flows Analysis

- Market flow regime: `Mixed / Neutral`
- Market flow score: `50.2 / 100`
- Equity risk flow: `49.3`
- Credit risk flow: `46.5`
- Sector cyclicality flow: `54.2`
- Duration/liquidity flow: `51.6`
- Alternatives: `defensive or uncertainty hedge`
- ETF flow reliability: `65.8 / 100`
- Dominant allocation direction: `defensive demand`

### Core Flow Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVV | U.S. Broad Equity | 0.4 | 0.9 | 0.5 | -0.0 | Flat | Neutral | Normal | Neutral | Neutral | Structural accumulation | 91.0 |
| ACWI | Global Equity | -1.0 | -1.3 | 0.1 | -1.4 | Flat | Sell | Low | Weak Distribution | Neutral | Medium-term recovery; Exceptional institutional selling, Persistent selling | 71.0 |
| EFA | Developed Markets ex-U.S. | -2.5 | -0.1 | 0.0 | -0.2 | Flat | Neutral | Normal | Neutral | Neutral | Medium-term deterioration; Exceptional institutional selling, Persistent selling | 67.0 |
| IEMG | Emerging Markets | -0.3 | -0.6 | 0.1 | -0.6 | Down | Buy | Normal | Contrarian Buying | Watch | Medium-term recovery; Persistent selling | 79.0 |
| IJH | U.S. Mid Cap | -0.8 | -0.1 | 0.6 | -0.7 | Flat | Neutral | Normal | Neutral | Neutral | Structural accumulation | 91.0 |
| IWM | U.S. Small Cap | -0.4 | 1.4 | 0.5 | 0.3 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Medium-term deterioration | 83.0 |
| LQD | Investment-Grade Credit | 0.8 | 0.6 | 0.6 | 1.1 | Down | Neutral | High | Heavy Selling Pressure | Cautious | Structural accumulation | 91.0 |
| HYG | High-Yield Credit | -0.4 | -1.0 | 0.5 | 1.9 | Flat | Neutral | High | High-Turnover Consolidation | Transition | Structural distribution | 79.0 |
| SGOV | Treasury Bills / Cash | -0.7 | -0.5 | 0.8 | -0.2 | Flat | Neutral | Normal | Neutral | Neutral | Structural accumulation; Strong sponsorship | 99.0 |
| SHY | Short-Duration Treasuries | -0.2 | -1.2 | 0.3 | -0.2 | Flat | Neutral | Normal | Neutral | Neutral | Medium-term recovery | 87.0 |
| IEF | Intermediate-Duration Treasuries | 0.3 | -0.7 | 0.6 | -0.7 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Medium-term recovery | 87.0 |
| TLT | Long-Duration Treasuries | 2.4 | 1.6 | 0.8 | 0.6 | Down | Buy | Normal | Contrarian Buying | Watch | Strong confirmation; Exceptional institutional buying, Strong sponsorship | 100.0 |
| GLD | Gold | 0.5 | 0.5 | 0.4 | 1.0 | Flat | Buy | High | Strong Accumulation | Early Bullish | Tactical rebound inside structural distribution | 83.0 |
| IBIT | Bitcoin | -0.5 | -1.6 | 0.5 | -0.4 | Up | Buy | Normal | Steady Accumulation | Risk-On | Tactical rebound inside structural distribution | 83.0 |

### Sector Flow Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| XLC | Communication Services | -0.6 | -1.4 | 0.3 | -1.1 | Flat | Neutral | Normal | Neutral | Neutral | Structural distribution | 79.0 |
| XLY | Consumer Discretionary | 1.3 | 1.1 | 0.6 | -0.5 | Flat | Buy | Normal | Quiet Accumulation | Improving | Strong confirmation | 95.0 |
| XLP | Consumer Staples | 1.0 | 0.9 | 0.3 | -1.8 | Flat | Neutral | Low | Dormant Market | Neutral | Medium-term recovery | 87.0 |
| XLE | Energy | -0.5 | -1.0 | 0.3 | -0.6 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural distribution | 79.0 |
| XLF | Financials | 1.6 | 1.4 | 0.6 | -1.2 | Up | Buy | Normal | Steady Accumulation | Risk-On | Strong confirmation | 95.0 |
| XLV | Health Care | 2.7 | 0.8 | 0.6 | -1.8 | Flat | Buy | Low | Early Accumulation | Watch | Medium-term recovery; Exceptional institutional buying | 95.0 |
| XLI | Industrials | -0.4 | 0.4 | 0.5 | -1.9 | Flat | Sell | Low | Weak Distribution | Neutral | Tactical profit-taking inside structural accumulation | 83.0 |
| XLK | Information Technology | 0.0 | -0.9 | 0.6 | -1.6 | Down | Neutral | Low | Weak Downtrend | Neutral | Mixed or neutral flow structure | 85.0 |
| XLB | Materials | -0.4 | 0.1 | 0.4 | -0.3 | Flat | Neutral | Normal | Neutral | Neutral | Structural accumulation | 91.0 |
| XLRE | Real Estate | 1.1 | 1.9 | 0.7 | -0.7 | Flat | Buy | Normal | Quiet Accumulation | Improving | Strong confirmation | 95.0 |
| XLU | Utilities | 0.2 | -0.3 | 0.5 | -0.4 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Medium-term recovery | 87.0 |

### Subsector PFV Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ITA | Aerospace and Defense | -0.1 | -0.5 | 0.2 | -0.0 | Flat | Neutral | Normal | Neutral | Neutral | Structural distribution; Persistent selling | 71.0 |
| SOXX | Semiconductors | 2.0 | 1.3 | 0.6 | -0.8 | Down | Buy | Normal | Contrarian Buying | Watch | Strong confirmation; Exceptional institutional buying | 100.0 |
| SMH | Semiconductors | 0.6 | 0.4 | 0.5 | -1.4 | Down | Neutral | Low | Weak Downtrend | Neutral | Structural accumulation | 91.0 |
| CIBR | Cybersecurity | 1.2 | 1.7 | 0.7 | 0.9 | Flat | Buy | Normal | Quiet Accumulation | Improving | Strong confirmation | 95.0 |

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
- Macro rows loaded: `38`
- Live macro rows used: `8`
- Economic rows loaded: `113`
- News rows loaded: `80`
- Positioning/flow rows loaded: `30`

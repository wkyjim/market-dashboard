# Rule-Based Institutional Market Update

Generated at: 23 July 2026, 09:18:57 (HKT)
Window: 24h

## Executive Dashboard

- Regime score: **60.68 / 100** (Mild Risk-On)
- US equity strength: **63.87 / 100** (constructive)
- Evidence quality: **86.5 / 100**
- ETF flow contribution: **48.28 / 100**, reliability **67.19 / 100**
- Breadth: **healthy**; above 50DMA `55.0%`, above 200DMA `71.19%`
- Top sector score: **Real Estate** `65.4`
- Top theme score: **Financials** `61.72`

## Market Regime Score

| Metric | Value | Driver / Interpretation |
| --- | --- | --- |
| Overall regime | 60.68 | Mild Risk-On |
| equity_trend | 72.5 | risk-on support; Core equity ETFs versus moving averages. |
| equity_momentum | 52.09 | neutral / mixed; 5D/20D/60D return momentum across SPY, QQQ, IWM, and SMH. |
| market_breadth | 64.84 | mild risk-on support; Participation breadth from tracked equity/ETF rows. |
| volatility | 70.0 | risk-on support; VIX level and change; higher score means calmer volatility conditions. |
| rates_yield_curve | 58.0 | mild risk-on support; Treasury yield pressure and curve shape; higher score means less rates pressure. |
| credit_proxy | 50.0 | neutral / mixed; Credit-market proxy; currently neutral when no direct spread signal is available. |
| dollar_fx | 55.22 | mild risk-on support; Dollar move; higher score means less USD tightening pressure. |
| commodity_confirmation | 55.0 | mild risk-on support; Copper, silver, oil, and gold mix; higher score means better cyclical confirmation. |
| etf_flow | 48.85 | neutral / mixed; Grouped ETF flow contribution adjusted for reliability. |
| news_confirmation | 76.25 | risk-on support; Weighted headline/news confirmation score. |
| Positive contributors |  | news_confirmation=76.25, equity_trend=72.5, volatility=70.0, market_breadth=64.84 |
| Negative contributors |  | none |

## US Equity Strength Score

| Component | Score |
| --- | --- |
| indices_above_moving_averages | 72.5 |
| sp500_trend | 100.0 |
| nasdaq_trend | 55.0 |
| russell_participation | 80.0 |
| returns_momentum | 52.09 |
| rsi_zone | 48.75 |
| macd_confirmation | 35.0 |
| volume_confirmation | 50.0 |
| breadth | 64.84 |

## Evidence Quality / Confidence

- Confidence score: `86.5`
- Agreement ratio: `0.7`
- Contradiction count: `0`
- Missing indicators: none
- Warning flags: none

## Cross-Asset Confirmation

| Area | Signal | Interpretation |
| --- | --- | --- |
| Equities | S&P 500 stable; Nasdaq falling; Russell 2000 falling | Confirms risk appetite when broad indices rise together; weak small caps would narrow the signal. |
| Rates | 10Y Treasury rising; MOVE rising | Rising yields can pressure duration assets; falling MOVE supports calmer bond volatility. |
| Dollar | DXY proxy stable | A stronger dollar can tighten financial conditions and pressure commodities/emerging-market risk. |
| Credit | HYG stable | High-yield weakness would challenge equity risk-on confirmation. |
| Gold | Gold rising | Gold strength can indicate defensive demand, inflation hedging, or geopolitical concern. |
| Silver | Silver rising | Silver helps distinguish precious-metal demand from industrial/cyclical confirmation when data is available. |
| Copper | Copper falling | Copper strength supports cyclical growth confirmation; weakness would dilute risk-on breadth. |
| Oil | WTI crude rising | Oil spikes can be inflationary risk; falling oil can ease cost pressure but may also flag demand softness. |
| Volatility | VIX falling | Falling VIX supports risk appetite; a volatility spike would reduce confidence in broad risk-on. |

### Macro Snapshot

Live macro rows are intraday snapshots from `public.macro_live`; closed rows are official stored rows from `public.macro`.

| Symbol | Name | Close | Pct Chg | Market Date | Status |
| --- | --- | --- | --- | --- | --- |
| ^GSPC | S&P 500 | 7498.96 | -0.14 | 2026-07-22 | closed |
| ^IXIC | NASDAQ Composite | 25690.9 | -0.57 | 2026-07-22 | closed |
| ^RUT | Russell 2000 Index | 2959.94 | -0.92 | 2026-07-22 | closed |
| ^VIX | CBOE Volatility Index | 16.64 | -2.4 | 2026-07-22 | closed |
| ^MOVE | ICE BofA MOVE Index | 76.31 | 7.65 | 2026-07-22 | closed |
| ^FVX | Treasury Yield 5 Years | 4.41 | 0.85 | 2026-07-22 | closed |
| ^TNX | Treasury Yield 10 Years | 4.66 | 0.63 | 2026-07-22 | closed |
| ^TYX | Treasury Yield 30 Years | 5.15 | 0.33 | 2026-07-22 | closed |
| DX-Y.NYB | US Dollar Index | 101.14 | -0.04 | 2026-07-22 | closed |
| HYG | iShares iBoxx High Yield Corporate Bond ETF | 79.52 | -0.16 | 2026-07-22 | closed |
| LQD | iShares iBoxx Investment Grade Corporate Bond ETF | 106.67 | -0.17 | 2026-07-22 | closed |
| JNK | SPDR Bloomberg High Yield Bond ETF | 95.75 | -0.16 | 2026-07-22 | closed |
| RSP | Invesco S&P 500 Equal Weight ETF | 212.7 | -0.03 | 2026-07-22 | closed |
| IWF | iShares Russell 1000 Growth ETF | 120.92 | -0.34 | 2026-07-22 | closed |
| IWD | iShares Russell 1000 Value ETF | 247.52 | 0.03 | 2026-07-22 | closed |
| TLT | iShares 20+ Year Treasury Bond ETF | 83.44 | -0.26 | 2026-07-22 | closed |
| IEF | iShares 7-10 Year Treasury Bond ETF | 93.1 | -0.23 | 2026-07-22 | closed |
| SHY | iShares 1-3 Year Treasury Bond ETF | 81.83 | -0.07 | 2026-07-22 | closed |
| GC=F | Gold Future | 4135.0 | 1.57 | 2026-07-22 | closed |
| SI=F | Silver Future | 60.03 | 2.04 | 2026-07-22 | closed |
| CL=F | WTI Crude Oil Future | 86.48 | 1.85 | 2026-07-22 | closed |
| HG=F | Copper Future | 6.49 | -0.31 | 2026-07-22 | closed |

## Market Dispersion Analysis

- Sector ETF 20D dispersion: `10.83` points (moderate); leader `XLE` (Energy) `8.7`, laggard `XLK` (Technology) `-2.13`
- Sector ETF 60D dispersion: `18.0` points (high); leader `XLK` (Technology) `12.51`, laggard `XLC` (Communication Services) `-5.49`

| Comparison | Left | Right | 20D Spread | Signal |
| --- | --- | --- | --- | --- |
| Equal-weight vs cap-weight | RSP (Equal-weight S&P 500) | SPY (S&P 500) | -0.06 | balanced |
| Small-cap vs large-cap | IWM (Russell 2000) | SPY (S&P 500) | -2.4 | large-cap leadership |
| Growth vs value | IWF (Russell 1000 Growth) | IWD (Russell 1000 Value) | -1.8 | value leadership |
| Nasdaq vs S&P 500 | QQQ (Nasdaq 100) | SPY (S&P 500) | -3.05 | S&P 500 leadership |

## Sector Constituent Dispersion

- Breadth 50D / 200D: percentage of active S&P 500 constituents in the sector trading above the 50-day / 200-day moving average.
- Positive 20D: percentage of active sector constituents with positive 20-day return.
- Std 20D: cross-sectional standard deviation of constituent 20-day returns; higher means wider stock-level dispersion.

| Sector | Count | Breadth 50D | Breadth 200D | Positive 20D | 20D Dispersion | Std 20D | Label | Leaders | Laggards |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Materials | 26 | 57.69 | 61.54 | 50.0 | 220.9 | 38.98 | very high | DD, CF, CTVA | MLM, CRH, ALB |
| Information Technology | 74 | 31.08 | 60.27 | 47.3 | 89.81 | 13.55 | very high | GDDY, PANW, WDAY | ORCL, MRVL, CRWD |
| Health Care | 59 | 72.88 | 57.63 | 83.05 | 43.09 | 6.52 | very high | TECH, CRL, IQV | MRNA, BSX, ISRG |
| Financials | 76 | 80.56 | 74.29 | 84.21 | 41.98 | 6.38 | very high | PYPL, GPN, TRV | PGR, C, APO |
| Industrials | 81 | 60.76 | 68.83 | 61.73 | 41.55 | 7.21 | very high | CTAS, CHRW, AXON | FDXF, PNR, GNRC |
| Energy | 21 | 85.71 | 85.71 | 76.19 | 33.52 | 9.07 | very high | VLO, MPC, PSX | WMB, BKR, HAL |
| Communication Services | 23 | 40.91 | 40.91 | 47.83 | 26.08 | 7.2 | very high | FOXA, FOX, META | DIS, PSKY, TKO |
| Consumer Discretionary | 47 | 46.81 | 46.81 | 42.55 | 25.31 | 5.75 | very high | BBY, GPC, DPZ | DHI, CCL, WYNN |
| Consumer Staples | 34 | 69.7 | 62.5 | 67.65 | 23.98 | 5.5 | very high | KHC, ADM, BG | PEP, STZ, WMT |
| Real Estate | 31 | 58.06 | 74.19 | 51.61 | 22.34 | 5.8 | very high | VTR, WELL, DOC | CCI, CSGP, DLR |
| Utilities | 31 | 90.32 | 87.1 | 70.97 | 12.42 | 2.76 | high | EIX, PCG, AWK | NI, CMS, PEG |

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
| US dollar/Euro ECB reference exchange rate | 1.14 | USD | -0.0 USD vs prior | 2026-07-22 | EUR weakened versus this currency. |
| Japanese yen/Euro ECB reference exchange rate | 186.03 | JPY | 0.21 JPY vs prior | 2026-07-22 | EUR strengthened versus this currency. |
| Chinese yuan renminbi/Euro ECB reference exchange rate | 7.73 | CNY | 0.0 CNY vs prior | 2026-07-22 | EUR strengthened versus this currency. |
| Australian dollar/Euro ECB reference exchange rate | 1.63 | AUD | 0.0 AUD vs prior | 2026-07-22 | EUR strengthened versus this currency. |

ABS Australia note: ABS rows are stored locally/Neon, but most series are dimension-coded; only curated series should be promoted into narrative report text.

## Sector and Theme Leadership

### Official Sector Strength

Supporting and detracting names are the top/bottom S&P 500 constituents by 20D return when constituent coverage is available; otherwise the report falls back to related ETFs.

| Rank | Sector | Score | Trend | Momentum | Stock Breadth | ETF Flow | Flow Reliability | 3M RS | Supporting / Leaders | Detracting / Laggards |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Real Estate | 65.4 | strong uptrend | neutral | broad | 53.22 | 65.0 | 48.57 | VTR, WELL, DOC | CCI, CSGP, DLR |
| 2 | Consumer Staples | 64.9 | strong uptrend | neutral | broad | 50.0 | 0.0 | 48.02 | KHC, ADM, BG | PEP, STZ, WMT |
| 3 | Financials | 64.67 | strong uptrend | neutral | broad | 58.68 | 65.0 | 53.01 | PYPL, GPN, TRV | PGR, C, APO |
| 4 | Cybersecurity | 59.69 | strong uptrend | positive | broad | 50.0 | 0.0 | 63.78 | CIBR | CIBR |
| 5 | Utilities | 59.26 | strong uptrend | neutral | broad | 50.0 | 0.0 | 47.03 | EIX, PCG, AWK | NI, CMS, PEG |
| 6 | Energy | 58.18 | uptrend | positive | broad | 48.9 | 65.0 | 53.85 | VLO, MPC, PSX | WMB, BKR, HAL |
| 7 | Healthcare | 57.07 | strong uptrend | positive | broad | 43.95 | 65.0 | 54.08 | TECH, CRL, IQV | MRNA, BSX, ISRG |
| 8 | Industrials | 55.49 | strong uptrend | neutral | broad | 50.0 | 0.0 | 48.71 | CTAS, CHRW, AXON | FDXF, PNR, GNRC |
| 9 | Crypto | 49.51 | neutral | neutral | mixed | 45.13 | 65.0 | 50.0 |  |  |
| 10 | Semiconductors | 48.35 | neutral | neutral | weak | 66.77 | 100.0 | 50.17 | SMH, SOXX | SOXX, SMH |
| 11 | Technology | 45.55 | neutral | neutral | weak | 39.12 | 65.0 | 49.76 | GDDY, PANW, WDAY | ORCL, MRVL, CRWD |
| 12 | Grid Infrastructure | 40.89 | downtrend | neutral | weak | 50.0 | 0.0 | 42.93 | GRID | GRID |
| 13 | Defense | 40.46 | downtrend | neutral | weak | 50.0 | 0.0 | 45.82 | XAR | XAR |
| 14 | Consumer Discretionary | 35.14 | strong downtrend | neutral | weak | 50.0 | 0.0 | 45.56 | BBY, GPC, DPZ | DHI, CCL, WYNN |
| 15 | Nuclear | 34.19 | strong downtrend | negative | weak | 50.0 | 0.0 | 32.59 | NLR | NLR |

### Thematic Strength

| Rank | Theme | Score | Setup | ETF Flow | Flow Reliability | Dispersion | Price | News |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Financials | 61.72 | Positive setup | 58.68 | 65.0 | 6.06 | True | False |
| 2 | Energy | 59.63 | Positive setup | 48.9 | 65.0 | 1.83 | False | False |
| 3 | Healthcare Innovation | 57.35 | Positive setup | 43.95 | 65.0 | 1.82 | False | False |
| 4 | Small Caps | 55.61 | Positive setup | 53.82 | 65.0 | 0.0 | False | False |
| 5 | Dividend Defensives | 54.42 | Neutral / watchlist | 57.33 | 65.0 | 3.98 | False | False |
| 6 | Semiconductors | 53.59 | Neutral / watchlist | 66.77 | 100.0 | 14.18 | False | False |
| 7 | Cybersecurity | 51.77 | Neutral / watchlist | 50.0 | 0.0 | 87.58 | False | False |
| 8 | Grid Infrastructure | 48.17 | Neutral / watchlist | 50.0 | 0.0 | 10.33 | False | False |
| 9 | AI Infrastructure | 47.57 | Neutral / watchlist | 66.77 | 100.0 | 13.94 | False | False |
| 10 | Quality Growth | 47.28 | Neutral / watchlist | 57.25 | 65.0 | 12.86 | False | False |
| 11 | Defense | 41.51 | Weak setup | 50.0 | 0.0 | 8.56 | False | False |
| 12 | Nuclear | 34.19 | Weak setup | 50.0 | 0.0 | 15.19 | False | False |
| 13 | Crypto Infrastructure | 33.03 | Underperformance risk | 45.13 | 65.0 | 8.71 | False | False |

- Top 5 improving themes: Cybersecurity, Healthcare Innovation, Semiconductors, Financials, Small Caps
- Top 5 deteriorating themes: Crypto Infrastructure, Nuclear, Defense, Grid Infrastructure, Dividend Defensives
- Strong news but weak price confirmation: none
- Strong price but weak news confirmation: Financials

### Sector / Theme Alignment

| Sector | Related Themes | Sector Score | Sector Signal | Theme Score | Theme Signal | Interpretation |
| --- | --- | --- | --- | --- | --- | --- |
| Real Estate | Dividend Defensives | 65.4 | strong | 54.42 | mixed | sector stronger than related themes |
| Consumer Staples | Dividend Defensives | 64.9 | positive | 54.42 | mixed | sector stronger than related themes |
| Financials | Financials | 64.67 | positive | 61.72 | positive | sector and theme confirmation |
| Cybersecurity | Cybersecurity | 59.69 | positive | 51.77 | mixed | sector stronger than related themes |
| Utilities | Grid Infrastructure, Nuclear, Dividend Defensives | 59.26 | positive | 45.59 | mixed | sector stronger than related themes |
| Energy | Energy | 58.18 | positive | 59.63 | positive | sector and theme confirmation |
| Healthcare | Healthcare Innovation | 57.07 | positive | 57.35 | positive | sector and theme confirmation |
| Industrials | Defense, Grid Infrastructure | 55.49 | positive | 44.84 | weak | sector stronger than related themes |
| Crypto | Crypto Infrastructure | 49.51 | mixed | 33.03 | very weak | mixed confirmation |
| Semiconductors | AI Infrastructure, Semiconductors | 48.35 | mixed | 50.58 | mixed | mixed confirmation |
| Technology | AI Infrastructure, Semiconductors, Quality Growth | 45.55 | mixed | 49.48 | mixed | mixed confirmation |
| Grid Infrastructure | Grid Infrastructure | 40.89 | weak | 48.17 | mixed | mixed confirmation |
| Defense | Defense | 40.46 | weak | 41.51 | weak | broad weakness across sector and themes |
| Consumer Discretionary | Small Caps | 35.14 | weak | 55.61 | positive | theme stronger than official sector |
| Nuclear | Nuclear | 34.19 | very weak | 34.19 | very weak | broad weakness across sector and themes |

## Three-Month Outperformance Setup

| Rank | Theme | Score | Classification | Drivers | Invalidation Triggers |
| --- | --- | --- | --- | --- | --- |
| 1 | Financials | 66.41 | Positive setup | relative_strength_60d, trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 2 | Healthcare Innovation | 65.61 | Positive setup | relative_strength_60d, trend_persistence, breadth, downside_volatility, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 3 | Small Caps | 63.69 | Positive setup | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 4 | Energy | 60.92 | Positive setup | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 5 | Dividend Defensives | 58.8 | Neutral / watchlist | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 6 | Semiconductors | 56.27 | Neutral / watchlist | relative_strength_60d, trend_persistence, breadth, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 7 | Cybersecurity | 54.77 | Neutral / watchlist | relative_strength_60d, trend_persistence, breadth, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 8 | Grid Infrastructure | 53.23 | Neutral / watchlist | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 9 | Quality Growth | 49.84 | Neutral / watchlist | downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 10 | AI Infrastructure | 48.98 | Neutral / watchlist | downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 11 | Defense | 43.54 | Weak setup |  | relative strength below SPY, breadth below 45%, news turns negative |
| 12 | Nuclear | 31.98 | Weak setup |  | relative strength below SPY, breadth below 45%, news turns negative |

## Breadth and Participation

- Above 50DMA: `55.0%`
- Above 200DMA: `71.19%`
- Positive 20D return: `68.33%`

## Volatility and Risk Signals

- VIX close=16.64 pct_chg=-2.4

## News Analytics

- Sentiment counts: {'positive': 61, 'negative': 19, 'neutral': 0}
- News confirmation score: `76.25`

### Top Market-Moving Headlines

**1. Oil prices climb after tanker struck off Saudi Arabia, Trump escalates Iran threats**
- Source: CNBC Top News
- Importance / impact: High / Positive
- Relevance / horizon: macro / short term
- Affected assets: U.S, Geopolitical Risk, Energy
- Score: `72.67`
- Investment implication: Macro-relevant positive signal; use as context for rates, volatility, and index confirmation over the short term.

**2. Houthis deploy missiles and drones to attack ships in southern Red Sea, naval group says**
- Source: CNBC Markets
- Importance / impact: High / Negative
- Relevance / horizon: macro / short-term
- Affected assets: defense, geo-political, oil
- Score: `61.77`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the short-term.

**3. Global oil prices settle at 6-week high after topping $95 a barrel, as hopes dim for de-escalation of Iran war**
- Source: MarketWatch Top Stories
- Importance / impact: High / Positive
- Relevance / horizon: macro / short-term
- Affected assets: U.S, oil_prices, geopolitical_risk
- Score: `60.0`
- Investment implication: Macro-relevant positive signal; use as context for rates, volatility, and index confirmation over the short-term.

**4. Alphabet earnings takeaways: Q2 revenue beats, GOOGL stock sinks on 2026 capex hike**
- Source: CNBC Top News
- Importance / impact: Medium / Positive
- Relevance / horizon: sector_theme / short-term
- Affected assets: GOOGL, GOOG, AI, earnings
- Score: `48.45`
- Investment implication: Theme or sector positive signal; requires price and volume confirmation before affecting rankings.

**5. Stocks close mostly lower as Iran conflict pushes up oil prices and bond yields**
- Source: MarketWatch Bulletins
- Importance / impact: Medium / Negative
- Relevance / horizon: macro / short-term
- Affected assets: geopolitical_risk, oil_prices
- Score: `43.23`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the short-term.

**6. Equinor Hikes Buyback as Earnings Jump on Higher Energy Prices**
- Source: Dow Jones US Business
- Importance / impact: Medium / Positive
- Relevance / horizon: macro / short-term
- Affected assets: EQNR, buyback, earnings, energy_prices
- Score: `43.03`
- Investment implication: Macro-relevant positive signal; use as context for rates, volatility, and index confirmation over the short-term.

**7. Alphabet earnings: Google parent's capex doubles as AI spending boom continues**
- Source: MarketWatch Bulletins
- Importance / impact: Medium / Positive
- Relevance / horizon: sector_theme / short-term
- Affected assets: GOOGL, GOOG, AI, capex
- Score: `41.99`
- Investment implication: Theme or sector positive signal; requires price and volume confirmation before affecting rankings.

**8. Analysis: Iran war energy shock hits the U.S. economy as gas and diesel prices climb**
- Source: CNBC Business Headlines
- Importance / impact: Medium / Negative
- Relevance / horizon: sector_theme / short-term
- Affected assets: A, U.S, geopolitical_risk, energy_prices
- Score: `40.8`
- Investment implication: Theme or sector negative signal; requires price and volume confirmation before affecting rankings.

**9. ServiceNow’s stock rises as earnings show momentum in cybersecurity**
- Source: MarketWatch Top Stories
- Importance / impact: Medium / Positive
- Relevance / horizon: single_name / short-term
- Affected assets: SNOW, cybersecurity, technology
- Score: `38.02`
- Investment implication: Single-name positive signal; low weight unless it maps to a broader sector or theme.

**10. CSX Reports Higher Second-Quarter Profit, Sales**
- Source: Dow Jones US Business
- Importance / impact: Medium / Positive
- Relevance / horizon: single_name / short-term
- Affected assets: CSX, railroad, revenue
- Score: `37.29`
- Investment implication: Single-name positive signal; low weight unless it maps to a broader sector or theme.


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
- Market flow score: `51.2 / 100`
- Equity risk flow: `50.5`
- Credit risk flow: `50.2`
- Sector cyclicality flow: `54.5`
- Duration/liquidity flow: `51.1`
- Alternatives: `mixed alternative-asset demand`
- ETF flow reliability: `67.2 / 100`
- Dominant allocation direction: `defensive demand`

### Core Flow Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVV | U.S. Broad Equity | 0.9 | 1.0 | 0.5 | -0.7 | Flat | Neutral | Normal | Neutral | Neutral | Structural accumulation | 91.0 |
| ACWI | Global Equity | -1.0 | -1.3 | 0.1 | -1.6 | Flat | Sell | Low | Weak Distribution | Neutral | Medium-term recovery; Exceptional institutional selling, Persistent selling | 71.0 |
| EFA | Developed Markets ex-U.S. | -2.6 | -0.1 | 0.0 | 0.3 | Flat | Neutral | Normal | Neutral | Neutral | Medium-term deterioration; Exceptional institutional selling, Persistent selling | 67.0 |
| IEMG | Emerging Markets | -0.3 | -0.6 | 0.1 | -0.5 | Down | Buy | Normal | Contrarian Buying | Watch | Medium-term recovery; Persistent selling | 79.0 |
| IJH | U.S. Mid Cap | -0.9 | -0.0 | 0.5 | -0.7 | Flat | Neutral | Normal | Neutral | Neutral | Structural accumulation | 91.0 |
| IWM | U.S. Small Cap | -0.3 | 1.2 | 0.5 | -1.1 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Medium-term deterioration | 83.0 |
| LQD | Investment-Grade Credit | 0.9 | 0.5 | 0.6 | -1.0 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural accumulation | 91.0 |
| HYG | High-Yield Credit | -0.1 | -0.4 | 0.5 | -1.0 | Flat | Neutral | Normal | Neutral | Neutral | Structural distribution | 79.0 |
| SGOV | Treasury Bills / Cash | -0.6 | -0.4 | 0.8 | -1.4 | Flat | Neutral | Normal | Neutral | Neutral | Structural accumulation; Strong sponsorship | 99.0 |
| SHY | Short-Duration Treasuries | -0.1 | -1.3 | 0.3 | -0.1 | Flat | Neutral | Normal | Neutral | Neutral | Medium-term recovery | 87.0 |
| IEF | Intermediate-Duration Treasuries | 0.1 | -0.7 | 0.6 | -1.2 | Flat | Neutral | Normal | Neutral | Neutral | Medium-term recovery | 87.0 |
| TLT | Long-Duration Treasuries | 2.2 | 1.5 | 0.8 | -1.2 | Down | Buy | Normal | Contrarian Buying | Watch | Strong confirmation; Exceptional institutional buying, Strong sponsorship | 100.0 |
| GLD | Gold | 0.1 | 0.2 | 0.3 | 0.0 | Flat | Buy | Normal | Quiet Accumulation | Improving | Tactical rebound inside structural distribution | 83.0 |
| IBIT | Bitcoin | -0.6 | -1.6 | 0.5 | -1.2 | Up | Buy | Normal | Steady Accumulation | Risk-On | Tactical rebound inside structural distribution | 83.0 |

### Sector Flow Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| XLC | Communication Services | -0.5 | -1.5 | 0.3 | -1.1 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural distribution | 79.0 |
| XLY | Consumer Discretionary | 1.5 | -0.2 | 0.6 | -0.7 | Flat | Neutral | Normal | Neutral | Neutral | Medium-term recovery | 87.0 |
| XLP | Consumer Staples | 1.2 | 1.2 | 0.4 | -1.5 | Flat | Buy | Low | Early Accumulation | Watch | Strong confirmation | 95.0 |
| XLE | Energy | -0.6 | -1.1 | 0.3 | -1.6 | Up | Neutral | Low | Fragile Rally | Low Confidence | Structural distribution | 79.0 |
| XLF | Financials | 1.3 | 0.6 | 0.6 | -1.1 | Up | Buy | Normal | Steady Accumulation | Risk-On | Medium-term recovery | 87.0 |
| XLV | Health Care | 2.9 | 0.7 | 0.6 | -1.4 | Up | Buy | Normal | Steady Accumulation | Risk-On | Medium-term recovery; Exceptional institutional buying | 95.0 |
| XLI | Industrials | -0.2 | 0.8 | 0.5 | -1.7 | Down | Sell | Low | Thin Distribution | Mild Risk-Off | Tactical profit-taking inside structural accumulation | 83.0 |
| XLK | Information Technology | 0.1 | -1.0 | 0.6 | -1.1 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Medium-term recovery | 87.0 |
| XLB | Materials | -0.3 | 0.1 | 0.5 | -0.7 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural accumulation | 91.0 |
| XLRE | Real Estate | 1.2 | 2.0 | 0.7 | -1.2 | Up | Buy | Normal | Steady Accumulation | Risk-On | Strong confirmation | 95.0 |
| XLU | Utilities | 0.6 | -0.3 | 0.5 | -0.9 | Flat | Neutral | Normal | Neutral | Neutral | Medium-term recovery | 87.0 |

### Subsector PFV Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ITA | Aerospace and Defense | 0.0 | -0.5 | 0.3 | -1.6 | Down | Neutral | Low | Weak Downtrend | Neutral | Structural distribution | 79.0 |
| SOXX | Semiconductors | 1.6 | 1.7 | 0.6 | -1.0 | Down | Buy | Normal | Contrarian Buying | Watch | Strong confirmation | 95.0 |
| SMH | Semiconductors | 0.6 | 0.4 | 0.5 | -1.4 | Down | Neutral | Low | Weak Downtrend | Neutral | Structural accumulation | 91.0 |
| CIBR | Cybersecurity | 1.9 | 1.7 | 0.7 | 1.0 | Up | Buy | Normal | Steady Accumulation | Risk-On | Strong confirmation | 95.0 |

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
- Live macro rows used: `7`
- Economic rows loaded: `113`
- News rows loaded: `80`
- Positioning/flow rows loaded: `30`

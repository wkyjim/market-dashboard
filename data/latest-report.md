# Rule-Based Institutional Market Update

Generated at: 21 July 2026, 15:02:05 (HKT)
Window: 24h

## Executive Dashboard

- Regime score: **56.94 / 100** (Mild Risk-On)
- Market strength: **55.07 / 100** (neutral)
- Evidence quality: **83.0 / 100**
- ETF flow contribution: **50.49 / 100**, reliability **71.05 / 100**
- Breadth: **narrow**; above 50DMA `50.0%`, above 200DMA `67.8%`
- Top sector score: **Cybersecurity** `68.93`
- Top theme score: **Financials** `62.74`

## Market Regime Score

| Metric | Value | Driver / Interpretation |
| --- | --- | --- |
| Overall regime | 56.94 | Mild Risk-On |
| equity_trend | 61.25 | mild risk-on support; Core equity ETFs versus moving averages. |
| equity_momentum | 50.12 | neutral / mixed; 5D/20D/60D return momentum across SPY, QQQ, IWM, and SMH. |
| market_breadth | 54.27 | neutral / mixed; Participation breadth from tracked equity/ETF rows. |
| volatility | 70.0 | risk-on support; VIX level and change; higher score means calmer volatility conditions. |
| rates_yield_curve | 58.0 | mild risk-on support; Treasury yield pressure and curve shape; higher score means less rates pressure. |
| credit_proxy | 50.0 | neutral / mixed; Credit-market proxy; currently neutral when no direct spread signal is available. |
| dollar_fx | 55.44 | mild risk-on support; Dollar move; higher score means less USD tightening pressure. |
| commodity_confirmation | 59.0 | mild risk-on support; Copper, silver, oil, and gold mix; higher score means better cyclical confirmation. |
| etf_flow | 50.35 | neutral / mixed; Grouped ETF flow contribution adjusted for reliability. |
| news_confirmation | 62.5 | mild risk-on support; Weighted headline/news confirmation score. |
| Positive contributors |  | volatility=70.0, news_confirmation=62.5, equity_trend=61.25 |
| Negative contributors |  | none |

## Market Strength Score

| Component | Score |
| --- | --- |
| indices_above_moving_averages | 61.25 |
| sp500_trend | 55.0 |
| nasdaq_trend | 55.0 |
| russell_participation | 80.0 |
| returns_momentum | 50.12 |
| rsi_zone | 47.5 |
| macd_confirmation | 35.0 |
| volume_confirmation | 50.0 |
| breadth | 54.27 |

## Evidence Quality / Confidence

- Confidence score: `83.0`
- Agreement ratio: `0.6`
- Contradiction count: `0`
- Missing indicators: none
- Warning flags: none

## Cross-Asset Confirmation

| Area | Signal | Interpretation |
| --- | --- | --- |
| Equities | S&P 500 stable; Nasdaq stable; Russell 2000 falling | Confirms risk appetite when broad indices rise together; weak small caps would narrow the signal. |
| Rates | 10Y Treasury rising; MOVE rising | Rising yields can pressure duration assets; falling MOVE supports calmer bond volatility. |
| Dollar | DXY proxy stable | A stronger dollar can tighten financial conditions and pressure commodities/emerging-market risk. |
| Credit | HYG stable | High-yield weakness would challenge equity risk-on confirmation. |
| Gold | Gold rising | Gold strength can indicate defensive demand, inflation hedging, or geopolitical concern. |
| Silver | Silver rising | Silver helps distinguish precious-metal demand from industrial/cyclical confirmation when data is available. |
| Copper | Copper rising | Copper strength supports cyclical growth confirmation; weakness would dilute risk-on breadth. |
| Oil | WTI crude falling | Oil spikes can be inflationary risk; falling oil can ease cost pressure but may also flag demand softness. |
| Volatility | VIX falling | Falling VIX supports risk appetite; a volatility spike would reduce confidence in broad risk-on. |

### Macro Snapshot

Live macro rows are intraday snapshots from `public.macro_live`; closed rows are official stored rows from `public.macro`.

| Symbol | Name | Close | Pct Chg | Market Date | Status |
| --- | --- | --- | --- | --- | --- |
| ^GSPC | S&P 500 | 7443.28 | -0.19 | 2026-07-20 | closed |
| ^IXIC | NASDAQ Composite | 25508.07 | -0.05 | 2026-07-20 | closed |
| ^RUT | Russell 2000 Index | 2942.43 | -0.67 | 2026-07-20 | closed |
| ^VIX | CBOE Volatility Index | 18.65 | -0.64 | 2026-07-20 | closed |
| ^MOVE | ICE BofA MOVE Index | 72.66 | 2.51 | 2026-07-20 | closed |
| ^FVX | Treasury Yield 5 Years | 4.33 | 1.29 | 2026-07-20 | closed |
| ^TNX | Treasury Yield 10 Years | 4.6 | 1.26 | 2026-07-20 | closed |
| ^TYX | Treasury Yield 30 Years | 5.12 | 1.07 | 2026-07-20 | closed |
| DX-Y.NYB | US Dollar Index | 100.9 | -0.09 | 2026-07-21 | live as of 21 July 2026, 15:00:39 (HKT) |
| HYG | iShares iBoxx High Yield Corporate Bond ETF | 79.68 | 0.04 | 2026-07-20 | closed |
| LQD | iShares iBoxx Investment Grade Corporate Bond ETF | 107.15 | -0.38 | 2026-07-20 | closed |
| JNK | SPDR Bloomberg High Yield Bond ETF | 95.95 | -0.03 | 2026-07-20 | closed |
| RSP | Invesco S&P 500 Equal Weight ETF | 212.42 | -0.45 | 2026-07-20 | closed |
| IWF | iShares Russell 1000 Growth ETF | 119.47 | 0.08 | 2026-07-20 | closed |
| IWD | iShares Russell 1000 Value ETF | 246.96 | -0.43 | 2026-07-20 | closed |
| TLT | iShares 20+ Year Treasury Bond ETF | 83.89 | -0.75 | 2026-07-20 | closed |
| IEF | iShares 7-10 Year Treasury Bond ETF | 93.54 | -0.32 | 2026-07-20 | closed |
| SHY | iShares 1-3 Year Treasury Bond ETF | 81.95 | -0.04 | 2026-07-20 | closed |
| GC=F | Gold Future | 4084.2 | 1.84 | 2026-07-21 | live as of 21 July 2026, 15:00:39 (HKT) |
| SI=F | Silver Future | 59.1 | 4.05 | 2026-07-21 | live as of 21 July 2026, 15:00:39 (HKT) |
| CL=F | WTI Crude Oil Future | 82.08 | -1.38 | 2026-07-21 | live as of 21 July 2026, 15:00:39 (HKT) |
| HG=F | Copper Future | 6.47 | 2.65 | 2026-07-21 | live as of 21 July 2026, 15:00:39 (HKT) |

## Market Dispersion Analysis

- Sector ETF 20D dispersion: `15.97` points (high); leader `XLE` (Energy) `7.76`, laggard `XLK` (Technology) `-8.22`
- Sector ETF 60D dispersion: `17.15` points (high); leader `XLK` (Technology) `11.15`, laggard `XLC` (Communication Services) `-6.01`

| Comparison | Left | Right | 20D Spread | Signal |
| --- | --- | --- | --- | --- |
| Equal-weight vs cap-weight | RSP (Equal-weight S&P 500) | SPY (S&P 500) | 1.79 | broader participation |
| Small-cap vs large-cap | IWM (Russell 2000) | SPY (S&P 500) | -0.49 | balanced |
| Growth vs value | IWF (Russell 1000 Growth) | IWD (Russell 1000 Value) | -4.99 | value leadership |
| Nasdaq vs S&P 500 | QQQ (Nasdaq 100) | SPY (S&P 500) | -5.39 | S&P 500 leadership |

## Sector Constituent Dispersion

- Breadth 50D / 200D: percentage of active S&P 500 constituents in the sector trading above the 50-day / 200-day moving average.
- Positive 20D: percentage of active sector constituents with positive 20-day return.
- Std 20D: cross-sectional standard deviation of constituent 20-day returns; higher means wider stock-level dispersion.

| Sector | Count | Breadth 50D | Breadth 200D | Positive 20D | 20D Dispersion | Std 20D | Label | Leaders | Laggards |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Materials | 26 | 53.85 | 61.54 | 34.62 | 210.82 | 36.96 | very high | DD, CF, CTVA | NEM, FCX, ALB |
| Information Technology | 74 | 36.49 | 60.27 | 40.54 | 96.92 | 17.47 | very high | WDAY, GDDY, PANW | SNDK, MRVL, CRWD |
| Industrials | 81 | 58.23 | 70.13 | 46.91 | 48.19 | 8.63 | very high | AXON, CTAS, PAYX | FIX, PNR, GNRC |
| Financials | 76 | 87.5 | 77.14 | 81.58 | 47.67 | 7.53 | very high | PYPL, GPN, JKHY | HOOD, C, APO |
| Health Care | 59 | 79.66 | 59.32 | 84.75 | 41.95 | 7.41 | very high | VEEV, TECH, IQV | ALGN, MRNA, ISRG |
| Energy | 21 | 61.9 | 85.71 | 80.95 | 38.17 | 10.0 | very high | VLO, MPC, PSX | EQT, SLB, BKR |
| Consumer Discretionary | 47 | 42.55 | 42.55 | 34.04 | 29.56 | 6.26 | very high | BBY, GPC, EXPE | WYNN, APTV, CCL |
| Communication Services | 23 | 36.36 | 40.91 | 52.17 | 29.23 | 7.97 | very high | OMC, NWS, NWSA | TKO, NFLX, PSKY |
| Real Estate | 31 | 67.74 | 74.19 | 64.52 | 25.34 | 6.38 | very high | WELL, VTR, DOC | AMT, DLR, EQIX |
| Consumer Staples | 34 | 69.7 | 65.62 | 73.53 | 18.91 | 5.17 | high | ADM, KHC, DLTR | WMT, PEP, STZ |
| Utilities | 31 | 54.84 | 77.42 | 74.19 | 14.96 | 3.31 | high | EIX, AWK, ES | VST, NI, CEG |

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
| US dollar/Euro ECB reference exchange rate | 1.14 | USD | -0.0 USD vs prior | 2026-07-20 | EUR weakened versus this currency. |
| Japanese yen/Euro ECB reference exchange rate | 185.54 | JPY | -0.11 JPY vs prior | 2026-07-20 | EUR weakened versus this currency. |
| Chinese yuan renminbi/Euro ECB reference exchange rate | 7.73 | CNY | -0.02 CNY vs prior | 2026-07-20 | EUR weakened versus this currency. |
| Australian dollar/Euro ECB reference exchange rate | 1.63 | AUD | -0.01 AUD vs prior | 2026-07-20 | EUR weakened versus this currency. |

ABS Australia note: ABS rows are stored locally/Neon, but most series are dimension-coded; only curated series should be promoted into narrative report text.

## Sector and Theme Leadership

### Official Sector Strength

Supporting and detracting names are the top/bottom S&P 500 constituents by 20D return when constituent coverage is available; otherwise the report falls back to related ETFs.

| Rank | Sector | Score | Trend | Momentum | Stock Breadth | ETF Flow | Flow Reliability | 3M RS | Supporting / Leaders | Detracting / Laggards |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Cybersecurity | 68.93 | strong uptrend | positive | broad | 60.61 | 65.0 | 67.06 | CIBR | CIBR |
| 2 | Financials | 68.24 | strong uptrend | neutral | broad | 72.0 | 95.0 | 54.34 | PYPL, GPN, JKHY | HOOD, C, APO |
| 3 | Consumer Staples | 67.28 | strong uptrend | neutral | broad | 66.01 | 65.0 | 51.1 | ADM, KHC, DLTR | WMT, PEP, STZ |
| 4 | Real Estate | 65.28 | strong uptrend | neutral | broad | 42.2 | 100.0 | 52.14 | WELL, VTR, DOC | AMT, DLR, EQIX |
| 5 | Energy | 58.19 | uptrend | neutral | broad | 50.0 | 0.0 | 54.28 | VLO, MPC, PSX | EQT, SLB, BKR |
| 6 | Healthcare | 58.16 | strong uptrend | positive | broad | 50.0 | 0.0 | 56.11 | VEEV, TECH, IQV | ALGN, MRNA, ISRG |
| 7 | Industrials | 56.59 | strong uptrend | neutral | broad | 57.91 | 65.0 | 49.37 | AXON, CTAS, PAYX | FIX, PNR, GNRC |
| 8 | Crypto | 49.38 | neutral | neutral | mixed | 43.83 | 65.0 | 50.0 |  |  |
| 9 | Semiconductors | 47.24 | neutral | neutral | weak | 75.03 | 90.0 | 46.35 | SMH, SOXX | SOXX, SMH |
| 10 | Technology | 45.25 | neutral | neutral | weak | 45.69 | 90.0 | 47.85 | WDAY, GDDY, PANW | SNDK, MRVL, CRWD |
| 11 | Utilities | 42.01 | strong downtrend | neutral | mixed | 65.94 | 65.0 | 47.58 | EIX, AWK, ES | VST, NI, CEG |
| 12 | Grid Infrastructure | 41.06 | downtrend | negative | weak | 62.7 | 65.0 | 41.71 | GRID | GRID |
| 13 | Consumer Discretionary | 36.87 | strong downtrend | neutral | weak | 65.43 | 65.0 | 45.88 | BBY, GPC, EXPE | WYNN, APTV, CCL |
| 14 | Defense | 32.67 | strong downtrend | neutral | weak | 39.3 | 65.0 | 42.67 | XAR | XAR |
| 15 | Nuclear | 28.75 | strong downtrend | negative | weak | 50.0 | 0.0 | 26.66 | NLR | NLR |

### Thematic Strength

| Rank | Theme | Score | Setup | ETF Flow | Flow Reliability | Dispersion | Price | News |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Financials | 62.74 | Positive setup | 72.0 | 95.0 | 11.3 | True | False |
| 2 | Energy | 58.27 | Positive setup | 50.0 | 0.0 | 1.61 | False | False |
| 3 | Healthcare Innovation | 57.75 | Positive setup | 50.0 | 0.0 | 4.85 | False | False |
| 4 | Cybersecurity | 55.97 | Neutral / watchlist | 60.61 | 65.0 | 92.17 | False | False |
| 5 | Small Caps | 54.4 | Positive setup | 45.12 | 65.0 | 0.0 | False | False |
| 6 | Dividend Defensives | 53.56 | Neutral / watchlist | 51.25 | 65.0 | 6.19 | False | False |
| 7 | Semiconductors | 51.15 | Neutral / watchlist | 75.03 | 90.0 | 14.52 | False | False |
| 8 | Quality Growth | 49.31 | Neutral / watchlist | 55.38 | 65.0 | 17.81 | False | False |
| 9 | AI Infrastructure | 47.73 | Neutral / watchlist | 75.03 | 90.0 | 24.07 | False | False |
| 10 | Grid Infrastructure | 41.95 | Neutral / watchlist | 62.7 | 65.0 | 10.33 | False | False |
| 11 | Defense | 36.97 | Weak setup | 39.3 | 65.0 | 20.69 | False | False |
| 12 | Crypto Infrastructure | 30.9 | Underperformance risk | 43.83 | 65.0 | 11.34 | False | False |
| 13 | Nuclear | 25.89 | Underperformance risk | 50.0 | 0.0 | 4.5 | False | False |

- Top 5 improving themes: Cybersecurity, Semiconductors, Healthcare Innovation, Financials, Quality Growth
- Top 5 deteriorating themes: Crypto Infrastructure, Nuclear, Defense, Grid Infrastructure, Energy
- Strong news but weak price confirmation: none
- Strong price but weak news confirmation: Financials

### Sector / Theme Alignment

| Sector | Related Themes | Sector Score | Sector Signal | Theme Score | Theme Signal | Interpretation |
| --- | --- | --- | --- | --- | --- | --- |
| Cybersecurity | Cybersecurity | 68.93 | strong | 55.97 | positive | sector and theme confirmation |
| Financials | Financials | 68.24 | strong | 62.74 | positive | sector and theme confirmation |
| Consumer Staples | Dividend Defensives | 67.28 | strong | 53.56 | mixed | sector stronger than related themes |
| Real Estate | Dividend Defensives | 65.28 | strong | 53.56 | mixed | sector stronger than related themes |
| Energy | Energy | 58.19 | positive | 58.27 | positive | sector and theme confirmation |
| Healthcare | Healthcare Innovation | 58.16 | positive | 57.75 | positive | sector and theme confirmation |
| Industrials | Defense, Grid Infrastructure | 56.59 | positive | 39.46 | weak | sector stronger than related themes |
| Crypto | Crypto Infrastructure | 49.38 | mixed | 30.9 | very weak | mixed confirmation |
| Semiconductors | AI Infrastructure, Semiconductors | 47.24 | mixed | 49.44 | mixed | mixed confirmation |
| Technology | AI Infrastructure, Semiconductors, Quality Growth | 45.25 | mixed | 49.4 | mixed | mixed confirmation |
| Utilities | Grid Infrastructure, Nuclear, Dividend Defensives | 42.01 | weak | 40.47 | weak | broad weakness across sector and themes |
| Grid Infrastructure | Grid Infrastructure | 41.06 | weak | 41.95 | weak | broad weakness across sector and themes |
| Consumer Discretionary | Small Caps | 36.87 | weak | 54.4 | mixed | mixed confirmation |
| Defense | Defense | 32.67 | very weak | 36.97 | weak | broad weakness across sector and themes |
| Nuclear | Nuclear | 28.75 | very weak | 25.89 | very weak | broad weakness across sector and themes |

## Three-Month Outperformance Setup

| Rank | Theme | Score | Classification | Drivers | Invalidation Triggers |
| --- | --- | --- | --- | --- | --- |
| 1 | Healthcare Innovation | 66.37 | Positive setup | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 2 | Financials | 65.67 | Positive setup | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 3 | Small Caps | 64.16 | Positive setup | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 4 | Energy | 60.46 | Positive setup | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 5 | Dividend Defensives | 59.62 | Neutral / watchlist | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 6 | Cybersecurity | 57.92 | Neutral / watchlist | relative_strength_60d, trend_persistence, breadth, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 7 | Semiconductors | 52.89 | Neutral / watchlist | relative_strength_60d, trend_persistence, breadth, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 8 | Quality Growth | 52.58 | Neutral / watchlist | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 9 | AI Infrastructure | 48.35 | Neutral / watchlist | downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 10 | Grid Infrastructure | 45.14 | Neutral / watchlist | downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 11 | Defense | 38.4 | Weak setup |  | relative strength below SPY, breadth below 45%, news turns negative |
| 12 | Nuclear | 25.65 | Underperformance risk |  | relative strength below SPY, breadth below 45%, news turns negative |

## Breadth and Participation

- Above 50DMA: `50.0%`
- Above 200DMA: `67.8%`
- Positive 20D return: `45.0%`

## Volatility and Risk Signals

- VIX close=18.65 pct_chg=-0.64

## News Analytics

- Sentiment counts: {'positive': 49, 'negative': 29, 'neutral': 2}
- News confirmation score: `62.5`

### Top Market-Moving Headlines

**1. China's car market heads for worst year since 2021 as sales plunge 20%**
- Source: CNBC Top News
- Importance / impact: Medium / Negative
- Relevance / horizon: sector_theme / shortterm
- Affected assets: Economy, Automotive
- Score: `52.51`
- Investment implication: Theme or sector negative signal; requires price and volume confirmation before affecting rankings.

**2. U.S. hits Canada with stiff new tariffs, escalating trade tensions**
- Source: MarketWatch Bulletins
- Importance / impact: High / Negative
- Relevance / horizon: macro / short-term
- Affected assets: U.S, trade, tariffs
- Score: `48.45`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the short-term.

**3. Oil prices rise after Trump says Iran will pay for killing U.S. service members**
- Source: CNBC Top News
- Importance / impact: High / Negative
- Relevance / horizon: macro / short-term
- Affected assets: U.S, geopolitical_risk, oil_prices
- Score: `48.45`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the short-term.

**4. Iran's Houthi allies declare maritime embargo against Saudi Arabia, escalating threat to oil market**
- Source: CNBC Top News
- Importance / impact: High / Negative
- Relevance / horizon: macro / short-term
- Affected assets: geopolitical, oil_market
- Score: `48.45`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the short-term.

**5. Ships shun Strait of Hormuz as renewed fighting strains key oil corridor**
- Source: CNBC Business Headlines
- Importance / impact: High / Negative
- Relevance / horizon: macro / short-term
- Affected assets: U.S, geopolitical_risk, oil_market
- Score: `48.0`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the short-term.

**6. U.S. hits Canada with stiff new tariffs, escalating trade tensions**
- Source: MarketWatch Top Stories
- Importance / impact: High / Negative
- Relevance / horizon: macro / short-term
- Affected assets: U.S., U.S, trade policy, geopolitics
- Score: `47.6`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the short-term.

**7. Forget Nvidia. These 5 S&P 500 stocks are quietly going all in on AI.**
- Source: MarketWatch Top Stories
- Importance / impact: Medium / Positive
- Relevance / horizon: sector_theme / medium-term
- Affected assets: P, S, AI, S&P 500
- Score: `44.22`
- Investment implication: Theme or sector positive signal; requires price and volume confirmation before affecting rankings.

**8. SpaceX gave investors intense FOMO. Now the decade’s hottest IPO represents a brutal reality check.**
- Source: MarketWatch Top Stories
- Importance / impact: Medium / Negative
- Relevance / horizon: macro / short-term
- Affected assets: SpaceX, related_tickers, FOMO, IPO, initial public offering (IPO)
- Score: `44.2`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the short-term.

**9. Why cheap Chinese AI models could actually be a boon for Nvidia, Micron and other chip stocks**
- Source: MarketWatch Top Stories
- Importance / impact: Medium / Positive
- Relevance / horizon: sector_theme / long-term
- Affected assets: NVDA, MU, AI, Nvidia, Micron
- Score: `43.35`
- Investment implication: Theme or sector positive signal; requires price and volume confirmation before affecting rankings.

**10. Trump vows retaliation against Iran after U.S. deaths: 'They will pay'**
- Source: CNBC Business Headlines
- Importance / impact: Medium / Negative
- Relevance / horizon: macro / short-term
- Affected assets: U.S, geopolitical
- Score: `40.8`
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
- Market flow score: `49.2 / 100`
- Equity risk flow: `50.7`
- Credit risk flow: `54.9`
- Sector cyclicality flow: `43.5`
- Duration/liquidity flow: `50.9`
- Alternatives: `reduced alternative-asset allocation`
- ETF flow reliability: `71.0 / 100`
- Dominant allocation direction: `mixed allocation`

### Core Flow Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVV | U.S. Broad Equity | 1.6 | 1.2 | 0.6 | -0.5 | Flat | Buy | Normal | Quiet Accumulation | Improving | Strong confirmation | 95.0 |
| ACWI | Global Equity | -0.6 | -1.2 | 0.1 | 1.9 | Flat | Neutral | High | High-Turnover Consolidation | Transition | Medium-term recovery; Persistent selling | 79.0 |
| EFA | Developed Markets ex-U.S. | -2.8 | -0.1 | 0.0 | 0.4 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Medium-term deterioration; Exceptional institutional selling, Persistent selling | 67.0 |
| IEMG | Emerging Markets | -0.4 | -0.6 | 0.1 | -0.1 | Down | Buy | Normal | Contrarian Buying | Watch | Medium-term recovery; Exceptional institutional buying, Persistent selling | 87.0 |
| IJH | U.S. Mid Cap | -2.2 | 0.2 | 0.5 | -0.2 | Flat | Neutral | Normal | Neutral | Neutral | Medium-term deterioration; Exceptional institutional selling | 75.0 |
| IWM | U.S. Small Cap | -0.4 | 1.0 | 0.5 | -0.9 | Flat | Sell | Normal | Quiet Distribution | Weakening | Medium-term deterioration | 83.0 |
| LQD | Investment-Grade Credit | 1.0 | -0.1 | 0.6 | 0.3 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural accumulation | 91.0 |
| HYG | High-Yield Credit | 0.2 | 0.5 | 0.6 | -1.5 | Flat | Neutral | Low | Dormant Market | Neutral | Structural accumulation | 91.0 |
| SGOV | Treasury Bills / Cash | -0.6 | -0.3 | 0.8 | -0.3 | Flat | Neutral | Normal | Neutral | Neutral | Structural accumulation; Strong sponsorship | 99.0 |
| SHY | Short-Duration Treasuries | -0.3 | -1.4 | 0.3 | -0.3 | Flat | Neutral | Normal | Neutral | Neutral | Medium-term recovery | 87.0 |
| IEF | Intermediate-Duration Treasuries | 0.1 | -0.7 | 0.6 | -1.2 | Flat | Neutral | Normal | Neutral | Neutral | Medium-term recovery | 87.0 |
| TLT | Long-Duration Treasuries | 1.8 | 1.9 | 0.7 | -0.1 | Down | Buy | Normal | Contrarian Buying | Watch | Strong confirmation | 95.0 |
| GLD | Gold | -0.4 | -0.5 | 0.3 | -1.3 | Down | Buy | Normal | Contrarian Buying | Watch | Tactical rebound inside structural distribution; Exceptional institutional buying | 91.0 |
| IBIT | Bitcoin | -0.9 | -1.7 | 0.3 | -0.6 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural distribution | 79.0 |

### Sector Flow Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| XLC | Communication Services | -0.4 | -1.1 | 0.3 | -1.1 | Up | Buy | Normal | Steady Accumulation | Risk-On | Tactical rebound inside structural distribution | 83.0 |
| XLY | Consumer Discretionary | 1.1 | 2.1 | 0.6 | -0.1 | Down | Buy | Normal | Contrarian Buying | Watch | Strong confirmation; Exceptional institutional buying | 100.0 |
| XLP | Consumer Staples | 1.3 | 1.4 | 0.4 | -1.2 | Up | Buy | Normal | Steady Accumulation | Risk-On | Strong confirmation | 95.0 |
| XLE | Energy | -0.9 | -1.2 | 0.2 | -0.9 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural distribution; Persistent selling | 71.0 |
| XLF | Financials | 1.0 | 0.7 | 0.6 | 0.3 | Up | Buy | Normal | Steady Accumulation | Risk-On | Medium-term recovery; Exceptional institutional buying | 95.0 |
| XLV | Health Care | 2.0 | 0.4 | 0.6 | -1.5 | Flat | Buy | Normal | Quiet Accumulation | Improving | Medium-term recovery; Exceptional institutional buying | 95.0 |
| XLI | Industrials | -0.2 | 0.3 | 0.5 | -1.0 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural accumulation | 91.0 |
| XLK | Information Technology | -3.6 | -0.8 | 0.6 | -1.1 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Medium-term deterioration; Exceptional institutional selling | 75.0 |
| XLB | Materials | -0.5 | -0.3 | 0.4 | -0.2 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural accumulation | 91.0 |
| XLRE | Real Estate | 1.6 | 1.9 | 0.8 | -1.2 | Up | Buy | Normal | Steady Accumulation | Risk-On | Strong confirmation; Strong sponsorship | 100.0 |
| XLU | Utilities | 0.8 | -0.4 | 0.6 | -0.5 | Flat | Neutral | Normal | Neutral | Neutral | Medium-term recovery | 87.0 |

### Subsector PFV Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ITA | Aerospace and Defense | -0.1 | -0.3 | 0.2 | -0.3 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural distribution; Persistent selling | 71.0 |
| SOXX | Semiconductors | 3.1 | 2.6 | 0.6 | -0.9 | Down | Buy | Normal | Contrarian Buying | Watch | Strong confirmation; Exceptional institutional buying | 100.0 |
| SMH | Semiconductors | 0.7 | 0.6 | 0.5 | -1.1 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural accumulation | 91.0 |
| CIBR | Cybersecurity | -2.2 | 1.3 | 0.7 | -0.7 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Medium-term deterioration; Exceptional institutional selling | 75.0 |

### Material Flow Divergences

| Severity | Type | Primary | Comparison | Interpretation |
| --- | --- | --- | --- | --- |
| medium | related_subsector_divergence | XLK | SOXX | technology differs from semiconductors |
| high | close_substitute_divergence | GLD | IAU | primary representative differs from close substitute |
| high | close_substitute_divergence | IVV | SPY | primary representative differs from close substitute |
| high | close_substitute_divergence | AGG | IUSB | primary representative differs from close substitute |
| high | close_substitute_divergence | HYG | JNK | primary representative differs from close substitute |
| high | close_substitute_divergence | IVV | SPY | primary representative differs from close substitute |


## Contradiction / Audit Flags

No contradiction flags were triggered by current deterministic rules.

## Data Quality Notes

- Technical rows loaded: `60`
- S&P 500 constituent technical rows loaded: `503`
- Macro rows loaded: `38`
- Live macro rows used: `16`
- Economic rows loaded: `113`
- News rows loaded: `80`
- Positioning/flow rows loaded: `30`

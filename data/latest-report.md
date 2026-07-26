# Rule-Based Institutional Market Update

Generated at: 26 July 2026, 08:06:12 (HKT)
Window: 24h

## Executive Dashboard

- Regime score: **56.04 / 100** (Mild Risk-On)
- US equity strength: **51.24 / 100** (neutral)
- Evidence quality: **83.0 / 100**
- ETF flow contribution: **46.94 / 100**, reliability **66.86 / 100**
- Breadth: **healthy**; above 50DMA `51.67%`, above 200DMA `69.49%`
- Top sector score: **Healthcare** `65.71`
- Top theme score: **Energy** `61.12`

## Market Regime Score

| Metric | Value | Driver / Interpretation |
| --- | --- | --- |
| Overall regime | 56.04 | Mild Risk-On |
| equity_trend | 55.0 | mild risk-on support; Core equity ETFs versus moving averages. |
| equity_momentum | 50.51 | neutral / mixed; 5D/20D/60D return momentum across SPY, QQQ, IWM, and SMH. |
| market_breadth | 58.72 | mild risk-on support; Participation breadth from tracked equity/ETF rows. |
| volatility | 70.0 | risk-on support; VIX level and change; higher score means calmer volatility conditions. |
| rates_yield_curve | 58.0 | mild risk-on support; Treasury yield pressure and curve shape; higher score means less rates pressure. |
| credit_proxy | 50.0 | neutral / mixed; Credit-market proxy; currently neutral when no direct spread signal is available. |
| dollar_fx | 54.83 | neutral / mixed; Dollar move; higher score means less USD tightening pressure. |
| commodity_confirmation | 63.0 | mild risk-on support; Copper, silver, oil, and gold mix; higher score means better cyclical confirmation. |
| etf_flow | 47.95 | neutral / mixed; Grouped ETF flow contribution adjusted for reliability. |
| news_confirmation | 57.5 | mild risk-on support; Weighted headline/news confirmation score. |
| Positive contributors |  | volatility=70.0, commodity_confirmation=63.0 |
| Negative contributors |  | none |

## US Equity Strength Score

| Component | Score |
| --- | --- |
| indices_above_moving_averages | 55.0 |
| sp500_trend | 55.0 |
| nasdaq_trend | 55.0 |
| russell_participation | 55.0 |
| returns_momentum | 50.51 |
| rsi_zone | 38.75 |
| macd_confirmation | 35.0 |
| volume_confirmation | 55.0 |
| breadth | 58.72 |

## Evidence Quality / Confidence

- Confidence score: `83.0`
- Agreement ratio: `0.6`
- Contradiction count: `0`
- Missing indicators: none
- Warning flags: none

## Cross-Asset Confirmation

| Area | Signal | Interpretation |
| --- | --- | --- |
| Equities | S&P 500 stable; Nasdaq falling; Russell 2000 falling | Confirms risk appetite when broad indices rise together; weak small caps would narrow the signal. |
| Rates | 10Y Treasury falling; MOVE rising | Rising yields can pressure duration assets; falling MOVE supports calmer bond volatility. |
| Dollar | DXY proxy stable | A stronger dollar can tighten financial conditions and pressure commodities/emerging-market risk. |
| Credit | HYG stable | High-yield weakness would challenge equity risk-on confirmation. |
| Gold | Gold stable | Gold strength can indicate defensive demand, inflation hedging, or geopolitical concern. |
| Silver | Silver rising | Silver helps distinguish precious-metal demand from industrial/cyclical confirmation when data is available. |
| Copper | Copper rising | Copper strength supports cyclical growth confirmation; weakness would dilute risk-on breadth. |
| Oil | WTI crude falling | Oil spikes can be inflationary risk; falling oil can ease cost pressure but may also flag demand softness. |
| Volatility | VIX falling | Falling VIX supports risk appetite; a volatility spike would reduce confidence in broad risk-on. |

### Macro Snapshot

Live macro rows are intraday snapshots from `public.macro_live`; closed rows are official stored rows from `public.macro`.

| Symbol | Name | Close | Pct Chg | Market Date | Status |
| --- | --- | --- | --- | --- | --- |
| ^GSPC | S&P 500 | 7411.98 | 0.05 | 2026-07-24 | closed |
| ^IXIC | NASDAQ Composite | 24975.82 | -0.64 | 2026-07-24 | closed |
| ^RUT | Russell 2000 Index | 2930.0 | -0.35 | 2026-07-24 | closed |
| ^VIX | CBOE Volatility Index | 18.58 | -0.64 | 2026-07-24 | closed |
| ^MOVE | ICE BofA MOVE Index | 76.82 | 8.38 | 2026-07-24 | closed |
| ^FVX | Treasury Yield 5 Years | 4.43 | -0.78 | 2026-07-24 | closed |
| ^TNX | Treasury Yield 10 Years | 4.68 | -0.51 | 2026-07-24 | closed |
| ^TYX | Treasury Yield 30 Years | 5.16 | -0.17 | 2026-07-24 | closed |
| DX-Y.NYB | US Dollar Index | 101.47 | 0.03 | 2026-07-24 | closed |
| HYG | iShares iBoxx High Yield Corporate Bond ETF | 79.23 | 0.0 | 2026-07-24 | closed |
| LQD | iShares iBoxx Investment Grade Corporate Bond ETF | 106.23 | -0.03 | 2026-07-24 | closed |
| JNK | SPDR Bloomberg High Yield Bond ETF | 95.39 | -0.01 | 2026-07-24 | closed |
| RSP | Invesco S&P 500 Equal Weight ETF | 213.57 | 0.78 | 2026-07-24 | closed |
| IWF | iShares Russell 1000 Growth ETF | 117.65 | -0.79 | 2026-07-24 | closed |
| IWD | iShares Russell 1000 Value ETF | 248.24 | 0.84 | 2026-07-24 | closed |
| TLT | iShares 20+ Year Treasury Bond ETF | 83.25 | 0.1 | 2026-07-24 | closed |
| IEF | iShares 7-10 Year Treasury Bond ETF | 93.03 | 0.19 | 2026-07-24 | closed |
| SHY | iShares 1-3 Year Treasury Bond ETF | 81.85 | 0.1 | 2026-07-24 | closed |
| GC=F | Gold Future | 4055.7 | 0.22 | 2026-07-24 | closed |
| SI=F | Silver Future | 58.49 | 1.2 | 2026-07-24 | closed |
| CL=F | WTI Crude Oil Future | 90.47 | -1.87 | 2026-07-24 | closed |
| HG=F | Copper Future | 6.34 | 0.55 | 2026-07-24 | closed |

## Market Dispersion Analysis

- Sector ETF 20D dispersion: `14.93` points (high); leader `XLE` (Energy) `10.22`, laggard `XLK` (Technology) `-4.71`
- Sector ETF 60D dispersion: `21.19` points (very high); leader `XLV` (Health Care) `13.02`, laggard `XLC` (Communication Services) `-8.16`

| Comparison | Left | Right | 20D Spread | Signal |
| --- | --- | --- | --- | --- |
| Equal-weight vs cap-weight | RSP (Equal-weight S&P 500) | SPY (S&P 500) | 0.23 | balanced |
| Small-cap vs large-cap | IWM (Russell 2000) | SPY (S&P 500) | -3.22 | large-cap leadership |
| Growth vs value | IWF (Russell 1000 Growth) | IWD (Russell 1000 Value) | -1.95 | value leadership |
| Nasdaq vs S&P 500 | QQQ (Nasdaq 100) | SPY (S&P 500) | -5.12 | S&P 500 leadership |

## Sector Constituent Dispersion

- Breadth 50D / 200D: percentage of active S&P 500 constituents in the sector trading above the 50-day / 200-day moving average.
- Positive 20D: percentage of active sector constituents with positive 20-day return.
- Std 20D: cross-sectional standard deviation of constituent 20-day returns; higher means wider stock-level dispersion.

| Sector | Count | Breadth 50D | Breadth 200D | Positive 20D | 20D Dispersion | Std 20D | Label | Leaders | Laggards |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Information Technology | 74 | 28.38 | 60.27 | 50.0 | 94.03 | 17.3 | very high | AAPL, WDAY, GDDY | GLW, SNDK, CRWD |
| Industrials | 81 | 73.42 | 74.03 | 53.09 | 53.33 | 9.63 | very high | CTAS, PAYX, ADP | PNR, BLDR, GNRC |
| Financials | 76 | 84.72 | 74.29 | 80.26 | 41.31 | 7.41 | very high | PYPL, FDS, TRV | AXP, SYF, C |
| Materials | 26 | 57.69 | 61.54 | 46.15 | 37.14 | 7.62 | very high | CF, CTVA, IP | MLM, CRH, ALB |
| Health Care | 59 | 74.58 | 62.71 | 69.49 | 33.37 | 6.01 | very high | VEEV, TMO, BMY | EW, MRNA, ISRG |
| Consumer Discretionary | 47 | 44.68 | 44.68 | 38.3 | 33.2 | 6.26 | very high | DPZ, BBY, ROST | LEN, DHI, TSLA |
| Energy | 21 | 85.71 | 85.71 | 85.71 | 26.51 | 7.27 | very high | MPC, PSX, VLO | KMI, HAL, WMB |
| Communication Services | 23 | 31.82 | 31.82 | 43.48 | 26.14 | 7.14 | very high | FOXA, FOX, META | ECHO, TKO, PSKY |
| Consumer Staples | 34 | 69.7 | 62.5 | 44.12 | 22.15 | 4.7 | very high | ADM, CASY, KHC | WMT, KDP, STZ |
| Real Estate | 31 | 77.42 | 74.19 | 64.52 | 22.05 | 4.68 | very high | VTR, WELL, O | CSGP, CCI, WY |
| Utilities | 31 | 96.77 | 83.87 | 54.84 | 10.82 | 2.61 | moderate | EIX, PCG, FE | CMS, PEG, NRG |

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
| US dollar/Euro ECB reference exchange rate | 1.14 | USD | -0.0 USD vs prior | 2026-07-24 | EUR weakened versus this currency. |
| Japanese yen/Euro ECB reference exchange rate | 186.38 | JPY | 0.15 JPY vs prior | 2026-07-24 | EUR strengthened versus this currency. |
| Chinese yuan renminbi/Euro ECB reference exchange rate | 7.7 | CNY | -0.01 CNY vs prior | 2026-07-24 | EUR weakened versus this currency. |
| Australian dollar/Euro ECB reference exchange rate | 1.63 | AUD | -0.0 AUD vs prior | 2026-07-24 | EUR weakened versus this currency. |

ABS Australia note: ABS rows are stored locally/Neon, but most series are dimension-coded; only curated series should be promoted into narrative report text.

## Sector and Theme Leadership

### Official Sector Strength

Supporting and detracting names are the top/bottom S&P 500 constituents by 20D return when constituent coverage is available; otherwise the report falls back to related ETFs.

| Rank | Sector | Score | Trend | Momentum | Stock Breadth | ETF Flow | Flow Reliability | 3M RS | Supporting / Leaders | Detracting / Laggards |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Healthcare | 65.71 | strong uptrend | positive | broad | 59.36 | 65.0 | 55.97 | VEEV, TMO, BMY | EW, MRNA, ISRG |
| 2 | Financials | 65.64 | strong uptrend | positive | broad | 63.77 | 65.0 | 54.74 | PYPL, FDS, TRV | AXP, SYF, C |
| 3 | Real Estate | 65.22 | strong uptrend | neutral | broad | 46.52 | 65.0 | 51.78 | VTR, WELL, O | CSGP, CCI, WY |
| 4 | Cybersecurity | 61.79 | strong uptrend | positive | broad | 62.36 | 65.0 | 64.15 | CIBR | CIBR |
| 5 | Utilities | 61.39 | strong uptrend | neutral | broad | 50.0 | 0.0 | 47.47 | EIX, PCG, FE | CMS, PEG, NRG |
| 6 | Industrials | 59.79 | strong uptrend | neutral | broad | 50.0 | 0.0 | 50.35 | CTAS, PAYX, ADP | PNR, BLDR, GNRC |
| 7 | Energy | 59.33 | uptrend | positive | broad | 55.61 | 65.0 | 55.55 | MPC, PSX, VLO | KMI, HAL, WMB |
| 8 | Crypto | 49.31 | neutral | neutral | mixed | 43.14 | 65.0 | 50.0 |  |  |
| 9 | Consumer Staples | 49.06 | neutral | neutral | weak | 50.0 | 0.0 | 48.73 | ADM, CASY, KHC | WMT, KDP, STZ |
| 10 | Semiconductors | 47.16 | neutral | neutral | weak | 62.03 | 100.0 | 46.69 | SMH, SOXX | SOXX, SMH |
| 11 | Technology | 45.04 | neutral | neutral | weak | 39.71 | 65.0 | 48.43 | AAPL, WDAY, GDDY | GLW, SNDK, CRWD |
| 12 | Defense | 42.42 | downtrend | neutral | weak | 50.0 | 0.0 | 49.47 | XAR | XAR |
| 13 | Grid Infrastructure | 41.99 | downtrend | neutral | weak | 69.09 | 65.0 | 42.31 | GRID | GRID |
| 14 | Nuclear | 34.51 | strong downtrend | negative | weak | 50.0 | 0.0 | 33.99 | NLR | NLR |
| 15 | Consumer Discretionary | 34.22 | strong downtrend | neutral | weak | 50.0 | 0.0 | 43.41 | DPZ, BBY, ROST | LEN, DHI, TSLA |

### Thematic Strength

| Rank | Theme | Score | Setup | ETF Flow | Flow Reliability | Dispersion | Price | News |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Energy | 61.12 | Positive setup | 55.61 | 65.0 | 3.87 | True | False |
| 2 | Financials | 60.7 | Positive setup | 63.77 | 65.0 | 7.0 | True | False |
| 3 | Healthcare Innovation | 60.24 | Positive setup | 59.36 | 65.0 | 4.81 | True | False |
| 4 | Dividend Defensives | 51.98 | Neutral / watchlist | 62.69 | 65.0 | 4.23 | False | False |
| 5 | Semiconductors | 51.87 | Neutral / watchlist | 62.03 | 100.0 | 21.38 | False | False |
| 6 | Defense | 51.28 | Neutral / watchlist | 50.0 | 0.0 | 16.74 | False | False |
| 7 | Grid Infrastructure | 51.04 | Neutral / watchlist | 69.09 | 65.0 | 13.87 | False | False |
| 8 | Cybersecurity | 50.66 | Neutral / watchlist | 62.36 | 65.0 | 87.95 | False | False |
| 9 | Quality Growth | 46.01 | Neutral / watchlist | 64.01 | 65.0 | 28.01 | False | False |
| 10 | Small Caps | 44.95 | Neutral / watchlist | 51.71 | 65.0 | 0.0 | False | False |
| 11 | AI Infrastructure | 42.67 | Weak setup | 62.03 | 100.0 | 23.89 | False | False |
| 12 | Crypto Infrastructure | 32.37 | Underperformance risk | 43.14 | 65.0 | 3.64 | False | False |
| 13 | Nuclear | 31.35 | Underperformance risk | 50.0 | 0.0 | 11.37 | False | False |

- Top 5 improving themes: Cybersecurity, Healthcare Innovation, Semiconductors, Financials, Small Caps
- Top 5 deteriorating themes: Crypto Infrastructure, Nuclear, Grid Infrastructure, AI Infrastructure, Defense
- Strong news but weak price confirmation: none
- Strong price but weak news confirmation: Energy, Financials, Healthcare Innovation

### Sector / Theme Alignment

| Sector | Related Themes | Sector Score | Sector Signal | Theme Score | Theme Signal | Interpretation |
| --- | --- | --- | --- | --- | --- | --- |
| Healthcare | Healthcare Innovation | 65.71 | strong | 60.24 | positive | sector and theme confirmation |
| Financials | Financials | 65.64 | strong | 60.7 | positive | sector and theme confirmation |
| Real Estate | Dividend Defensives | 65.22 | strong | 51.98 | mixed | sector stronger than related themes |
| Cybersecurity | Cybersecurity | 61.79 | positive | 50.66 | mixed | sector stronger than related themes |
| Utilities | Grid Infrastructure, Nuclear, Dividend Defensives | 61.39 | positive | 44.79 | weak | sector stronger than related themes |
| Industrials | Defense, Grid Infrastructure | 59.79 | positive | 51.16 | mixed | sector stronger than related themes |
| Energy | Energy | 59.33 | positive | 61.12 | positive | sector and theme confirmation |
| Crypto | Crypto Infrastructure | 49.31 | mixed | 32.37 | very weak | mixed confirmation |
| Consumer Staples | Dividend Defensives | 49.06 | mixed | 51.98 | mixed | mixed confirmation |
| Semiconductors | AI Infrastructure, Semiconductors | 47.16 | mixed | 47.27 | mixed | mixed confirmation |
| Technology | AI Infrastructure, Semiconductors, Quality Growth | 45.04 | mixed | 46.85 | mixed | mixed confirmation |
| Defense | Defense | 42.42 | weak | 51.28 | mixed | mixed confirmation |
| Grid Infrastructure | Grid Infrastructure | 41.99 | weak | 51.04 | mixed | mixed confirmation |
| Nuclear | Nuclear | 34.51 | very weak | 31.35 | very weak | broad weakness across sector and themes |
| Consumer Discretionary | Small Caps | 34.22 | very weak | 44.95 | weak | broad weakness across sector and themes |

## Three-Month Outperformance Setup

| Rank | Theme | Score | Classification | Drivers | Invalidation Triggers |
| --- | --- | --- | --- | --- | --- |
| 1 | Healthcare Innovation | 66.81 | Positive setup | relative_strength_60d, trend_persistence, breadth, downside_volatility, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 2 | Financials | 66.19 | Positive setup | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 3 | Energy | 62.2 | Positive setup | relative_strength_20d, trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 4 | Dividend Defensives | 55.52 | Neutral / watchlist | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 5 | Semiconductors | 54.92 | Neutral / watchlist | relative_strength_60d, trend_persistence, breadth, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 6 | Defense | 53.83 | Neutral / watchlist | trend_persistence, breadth | relative strength below SPY, breadth below 45%, news turns negative |
| 7 | Cybersecurity | 52.73 | Neutral / watchlist | relative_strength_60d, trend_persistence, breadth, relative_vs_qqq | relative strength below SPY, breadth below 45%, news turns negative |
| 8 | Grid Infrastructure | 52.61 | Neutral / watchlist | trend_persistence, breadth, downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 9 | Small Caps | 50.82 | Neutral / watchlist | downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 10 | Quality Growth | 48.09 | Neutral / watchlist | downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 11 | AI Infrastructure | 44.32 | Weak setup | downside_volatility | relative strength below SPY, breadth below 45%, news turns negative |
| 12 | Crypto Infrastructure | 28.92 | Underperformance risk |  | relative strength below SPY, breadth below 45%, news turns negative |

## Breadth and Participation

- Above 50DMA: `51.67%`
- Above 200DMA: `69.49%`
- Positive 20D return: `55.0%`

## Volatility and Risk Signals

- VIX close=18.58 pct_chg=-0.64

## News Analytics

- Sentiment counts: {'positive': 39, 'negative': 27, 'neutral': 14}
- News confirmation score: `57.5`

### Top Market-Moving Headlines

**1. S&P 500 flashes sell signals — options traders are bracing for wild swings in Apple, Meta and Microsoft**
- Source: MarketWatch Top Stories
- Importance / impact: Medium / Negative
- Relevance / horizon: sector_theme / short-term
- Affected assets: AAPL, META, MSFT, P, S
- Score: `43.35`
- Investment implication: Theme or sector negative signal; requires price and volume confirmation before affecting rankings.

**2. Russian attack cuts power to around 150,000 in Ukraine’s north as Kyiv hits missile, oil facilities**
- Source: CNBC Business News
- Importance / impact: Medium / Negative
- Relevance / horizon: macro / short-term
- Affected assets: geo-political
- Score: `40.8`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the short-term.

**3. Morgan Stanley says buy these stocks ahead of their earnings, before it's too late**
- Source: CNBC Markets
- Importance / impact: Medium / Positive
- Relevance / horizon: sector_theme / short-term
- Affected assets: MS, AAPL, GOOGL, buy, earnings
- Score: `40.15`
- Investment implication: Theme or sector positive signal; requires price and volume confirmation before affecting rankings.

**4. Oil prices may fall, but gasoline prices won’t. Look at the trap we’re in.**
- Source: MarketWatch Top Stories
- Importance / impact: Low / Negative
- Relevance / horizon: macro / short term
- Affected assets: Oil Prices, Gasoline Prices, Iran
- Score: `31.5`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the short term.

**5. Tariffs and gas prices are intensifying the affordability crunch. These 3 products can help**
- Source: CNBC Markets
- Importance / impact: Low / Negative
- Relevance / horizon: macro / short-term
- Affected assets: economy, trade, energy
- Score: `31.09`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the short-term.

**6. Trump sued hours after new tariffs take effect, as experts say they may not hold up**
- Source: CNBC Business Headlines
- Importance / impact: Low / Negative
- Relevance / horizon: macro / short-term
- Affected assets: trade_policy, government_regulation
- Score: `30.94`
- Investment implication: Macro-relevant negative signal; use as context for rates, volatility, and index confirmation over the short-term.

**7. Oil set for more than 25% spike over two weeks as Middle East conflict escalates**
- Source: Investing.com Stock Market
- Importance / impact: Low / Positive
- Relevance / horizon: macro / short-term
- Affected assets: WCL, OIL, USO, oil prices, Middle East conflict
- Score: `28.86`
- Investment implication: Macro-relevant positive signal; use as context for rates, volatility, and index confirmation over the short-term.

**8. Is your index fund an accidental bet on AI? These two massive ETFs show why it might be.**
- Source: MarketWatch Top Stories
- Importance / impact: Low / Positive
- Relevance / horizon: sector_theme / short-term
- Affected assets: AI, ETFs
- Score: `26.77`
- Investment implication: Theme or sector positive signal; requires price and volume confirmation before affecting rankings.

**9. Investors are in the dark about the Fed’s decision this week — and that’s just how Warsh wants it**
- Source: MarketWatch Top Stories
- Importance / impact: Low / Mixed
- Relevance / horizon: macro / short-term
- Affected assets: Federal Reserve, Economic Policy
- Score: `26.77`
- Investment implication: Macro-relevant mixed signal; use as context for rates, volatility, and index confirmation over the short-term.

**10. SpaceX launches massive Starship rocket in first test flight since IPO**
- Source: CNBC Business
- Importance / impact: Low / Positive
- Relevance / horizon: single_name / short-term
- Affected assets: IPO, space exploration, rocket launch
- Score: `26.52`
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
- Market flow score: `49.6 / 100`
- Equity risk flow: `46.7`
- Credit risk flow: `48.9`
- Sector cyclicality flow: `53.2`
- Duration/liquidity flow: `51.8`
- Alternatives: `defensive or uncertainty hedge`
- ETF flow reliability: `66.9 / 100`
- Dominant allocation direction: `defensive demand`

### Core Flow Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IVV | U.S. Broad Equity | -0.2 | 0.8 | 0.4 | -0.7 | Flat | Neutral | Normal | Neutral | Neutral | Structural accumulation | 91.0 |
| ACWI | Global Equity | -1.5 | -1.5 | 0.1 | -0.8 | Flat | Sell | Normal | Quiet Distribution | Weakening | Strong confirmation; Exceptional institutional selling, Persistent selling | 79.0 |
| EFA | Developed Markets ex-U.S. | -2.4 | -0.1 | 0.0 | -1.2 | Flat | Neutral | Normal | Neutral | Neutral | Medium-term deterioration; Exceptional institutional selling, Persistent selling | 67.0 |
| IEMG | Emerging Markets | -0.4 | -0.6 | 0.1 | -0.6 | Down | Buy | Normal | Contrarian Buying | Watch | Medium-term recovery; Persistent selling | 79.0 |
| IJH | U.S. Mid Cap | -0.6 | -0.1 | 0.6 | -0.5 | Flat | Neutral | Normal | Neutral | Neutral | Structural accumulation | 91.0 |
| IWM | U.S. Small Cap | -0.5 | 0.6 | 0.5 | -1.0 | Down | Sell | Normal | Persistent Distribution | Risk-Off | Strong confirmation | 95.0 |
| LQD | Investment-Grade Credit | 0.6 | 1.1 | 0.5 | 0.0 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural accumulation | 91.0 |
| HYG | High-Yield Credit | -0.6 | -0.4 | 0.5 | 0.8 | Flat | Neutral | Normal | Neutral | Neutral | Structural distribution | 79.0 |
| SGOV | Treasury Bills / Cash | -0.6 | -0.4 | 0.8 | -1.0 | Flat | Neutral | Normal | Neutral | Neutral | Structural accumulation; Strong sponsorship | 99.0 |
| SHY | Short-Duration Treasuries | -0.8 | -1.2 | 0.2 | -0.3 | Flat | Neutral | Normal | Neutral | Neutral | Structural distribution; Persistent selling | 71.0 |
| IEF | Intermediate-Duration Treasuries | 0.6 | -0.7 | 0.6 | -0.6 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Medium-term recovery | 87.0 |
| TLT | Long-Duration Treasuries | 2.3 | 1.7 | 0.8 | -1.3 | Down | Buy | Normal | Contrarian Buying | Watch | Strong confirmation; Exceptional institutional buying, Strong sponsorship | 100.0 |
| GLD | Gold | 1.0 | 0.7 | 0.4 | -1.3 | Flat | Buy | Normal | Quiet Accumulation | Improving | Medium-term recovery; Exceptional institutional buying | 95.0 |
| IBIT | Bitcoin | -0.6 | -1.6 | 0.5 | -0.6 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural distribution | 79.0 |

### Sector Flow Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| XLC | Communication Services | 0.0 | -1.1 | 0.4 | 2.8 | Down | Neutral | High | Heavy Selling Pressure | Cautious | Structural distribution | 79.0 |
| XLY | Consumer Discretionary | 1.6 | 0.8 | 0.6 | 2.0 | Down | Neutral | High | Heavy Selling Pressure | Cautious | Structural accumulation | 91.0 |
| XLP | Consumer Staples | 1.1 | 0.9 | 0.3 | -0.5 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Medium-term recovery | 87.0 |
| XLE | Energy | -0.4 | -1.0 | 0.3 | 0.0 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Structural distribution | 79.0 |
| XLF | Financials | 1.8 | 1.5 | 0.6 | -1.4 | Up | Buy | Normal | Steady Accumulation | Risk-On | Strong confirmation | 95.0 |
| XLV | Health Care | 1.8 | 0.2 | 0.6 | -1.5 | Up | Sell | Normal | Profit Taking | Slightly Bearish | Medium-term recovery; Exceptional institutional selling | 79.0 |
| XLI | Industrials | -0.1 | 0.9 | 0.5 | 0.5 | Flat | Sell | Normal | Quiet Distribution | Weakening | Tactical profit-taking inside structural accumulation | 83.0 |
| XLK | Information Technology | 0.0 | -0.7 | 0.6 | -1.1 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural accumulation | 91.0 |
| XLB | Materials | -0.1 | 0.3 | 0.5 | -0.1 | Down | Neutral | Normal | Unconfirmed Weakness | Neutral Bearish | Structural accumulation | 91.0 |
| XLRE | Real Estate | 1.4 | 1.7 | 0.7 | -0.3 | Flat | Buy | Normal | Quiet Accumulation | Improving | Strong confirmation | 95.0 |
| XLU | Utilities | 0.3 | 0.1 | 0.5 | -1.3 | Up | Neutral | Normal | Price Leadership | Neutral Bullish | Mixed or neutral flow structure | 85.0 |

### Subsector PFV Signals

| Ticker | Exposure | 20D Flow Z | 60D Flow Z | Persistence | Volume Z | Price State | Flow State | Volume State | PFV State | Regime Bias | Flow Structure | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ITA | Aerospace and Defense | 0.1 | -0.5 | 0.2 | 0.9 | Up | Neutral | High | Momentum Rally | Watch | Structural distribution; Persistent selling | 71.0 |
| SOXX | Semiconductors | 1.3 | 1.2 | 0.5 | 0.3 | Down | Sell | Normal | Persistent Distribution | Risk-Off | Tactical profit-taking inside structural accumulation; Exceptional institutional selling | 75.0 |
| SMH | Semiconductors | 0.0 | 0.0 | 0.5 | 1.8 | Down | Neutral | High | Heavy Selling Pressure | Cautious | Structural accumulation | 91.0 |
| CIBR | Cybersecurity | 1.2 | 1.6 | 0.7 | -1.3 | Flat | Buy | Normal | Quiet Accumulation | Improving | Strong confirmation | 95.0 |

### Material Flow Divergences

| Severity | Type | Primary | Comparison | Interpretation |
| --- | --- | --- | --- | --- |
| high | close_substitute_divergence | AGG | IUSB | primary representative differs from close substitute |
| high | close_substitute_divergence | IWF | IVW | primary representative differs from close substitute |
| high | close_substitute_divergence | IWD | IVE | primary representative differs from close substitute |
| high | close_substitute_divergence | SOXX | SMH | primary representative differs from close substitute |
| high | close_substitute_divergence | IWM | IJR | primary representative differs from close substitute |


## Contradiction / Audit Flags

No contradiction flags were triggered by current deterministic rules.

## Data Quality Notes

- Technical rows loaded: `60`
- S&P 500 constituent technical rows loaded: `503`
- Macro rows loaded: `38`
- Live macro rows used: `2`
- Economic rows loaded: `113`
- News rows loaded: `80`
- Positioning/flow rows loaded: `30`

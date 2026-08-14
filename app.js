const API_BASE = "https://postgresql-us-equities-api.onrender.com";
const MARKET_TAPE_GROUPS = [
  {
    title: "U.S. Market Indices",
    key: "us",
    symbols: [
      ["^GSPC", "S&P 500"],
      ["^NDX", "Nasdaq 100"],
      ["^DJI", "DJIA"],
      ["^VIX", "VIX"],
      ["^SKEW", "CBOE SKEW"]
    ]
  },
  {
    title: "Asia Equity Indices",
    key: "asia",
    symbols: [
      ["^HSI", "Hang Seng"],
      ["^N225", "Nikkei 225"],
      ["^KS11", "KOSPI"],
      ["000001.SS", "SSE Composite"]
    ]
  },
  {
    title: "Index Futures",
    key: "futures",
    symbols: [
      ["ES=F", "S&P 500 Future"],
      ["NQ=F", "Nasdaq 100 Future"],
      ["YM=F", "Dow Future"],
      ["RTY=F", "Russell 2000 Future"],
      ["HK50", "Hang Seng Future"],
      ["NIY=F", "Nikkei Future"],
      ["KOR200c1", "KOSPI 200 Future"],
      ["CIHc1", "SSE 50 Future"]
    ]
  },
  {
    title: "Other Assets",
    key: "other",
    symbols: [
      ["DX-Y.NYB", "DXY"],
      ["JPY=X", "USD/JPY"],
      ["EURUSD=X", "EUR/USD"],
      ["GC=F", "Gold"],
      ["BZ=F", "Brent"],
      ["CL=F", "WTI"],
      ["BTC-USD", "Bitcoin"]
    ]
  },
  {
    title: "UST Yield Moves",
    key: "rates",
    symbols: [
      ["US2YT=X", "UST 2Y"],
      ["US3YT=X", "UST 3Y"],
      ["US5YT=X", "UST 5Y"],
      ["US7YT=X", "UST 7Y"],
      ["US10YT=X", "UST 10Y"],
      ["US20YT=X", "UST 20Y"],
      ["US30YT=X", "UST 30Y"]
    ]
  }
];
const MARKET_TAPE_SYMBOLS = MARKET_TAPE_GROUPS.flatMap((group) => group.symbols.map(([symbol]) => symbol));
const REPORT_PATH = "data/latest-report.md";
const INDICATOR_GROUPS = [
  {
    title: "Trend",
    fields: [
      ["ma_5", "5-day MA"], ["ma_20", "20-day MA"], ["ma_50", "50-day MA"],
      ["ma_100", "100-day MA"], ["ma_200", "200-day MA"],
      ["ema_12", "12-day EMA"], ["ema_26", "26-day EMA"]
    ]
  },
  {
    title: "Momentum",
    fields: [
      ["rsi_14", "RSI (14)"], ["macd", "MACD"], ["macd_signal", "MACD signal"],
      ["macd_hist", "MACD histogram"], ["return_5d", "5-day return", "%"],
      ["return_20d", "20-day return", "%"], ["return_60d", "60-day return", "%"]
    ]
  },
  {
    title: "Volume & Range",
    fields: [
      ["atr_14", "ATR (14)"], ["volume_ma_20", "20-day avg volume"],
      ["volume_ratio_20", "Volume ratio"], ["high_52w", "52-week high"],
      ["low_52w", "52-week low"]
    ]
  },
  {
    title: "Risk",
    fields: [
      ["volatility_20d", "20-day volatility", "%"], ["close", "Latest close"],
      ["pct_chg", "Daily change", "%"], ["amplitude", "Daily amplitude", "%"],
      ["turnover_rate", "Turnover rate", "%"]
    ]
  }
];

const $ = (selector) => document.querySelector(selector);
const escapeHtml = (value) => String(value ?? "").replace(/[&<>"']/g, (char) => ({
  "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#039;"
}[char]));
const formatNumber = (value, digits = 2) => value == null || Number.isNaN(Number(value))
  ? "n/a"
  : Number(value).toLocaleString(undefined, { maximumFractionDigits: digits });
const formatPercent = (value, digits = 2) => value == null ? "n/a" : `${formatNumber(Number(value) * 100, digits)}%`;
const shortState = { limit: 50, offset: 0, total: 0 };

async function apiFetch(path) {
  const response = await fetch(`${API_BASE}${path}`, { headers: { Accept: "application/json" } });
  if (!response.ok) throw new Error(`${response.status} ${response.statusText}`);
  return response.json();
}

function setApiStatus(ok, message) {
  const element = $("#api-status");
  element.className = `status ${ok ? "ok" : "error"}`;
  element.innerHTML = `<i></i><b>LIVE DATA</b><small>${escapeHtml(message)}</small>`;
}

async function loadMacroTape() {
  const payload = await apiFetch(`/macro/batch/latest?symbols=${encodeURIComponent(MARKET_TAPE_SYMBOLS.join(","))}`);
  const rows = payload.data || [];
  if (!rows.length) throw new Error("No macro rows returned");
  const rowsBySymbol = new Map(rows.map((row) => [row.symbol, row]));
  const macroTape = $("#macro-tape");
  if (!macroTape) return;
  macroTape.classList.remove("loading-block");
  macroTape.innerHTML = MARKET_TAPE_GROUPS.map((group) => {
    const items = group.symbols.map(([symbol, label]) => {
      const row = rowsBySymbol.get(symbol);
      if (!row) {
        return `<div class="tape-item missing"><span>${escapeHtml(label)}</span><strong>n/a</strong><small>No data</small></div>`;
      }
      const moveValue = group.key === "rates" && row.change != null ? Number(row.change) * 100 : Number(row.pct_chg);
      const moveSuffix = group.key === "rates" ? " bps" : "%";
      const changeClass = Number(moveValue) > 0 ? "positive" : Number(moveValue) < 0 ? "negative" : "";
      const sign = Number(moveValue) > 0 ? "+" : "";
      return `<div class="tape-item">
        <span>${escapeHtml(label)}${row.is_live ? '<small class="live-tag">LIVE</small>' : ""}</span>
        <strong>${formatNumber(row.close)}</strong>
        <small class="${changeClass}">${sign}${formatNumber(moveValue)}${moveSuffix}</small>
        <small>${escapeHtml(row.date)} · ${escapeHtml(row.data_source)}</small>
      </div>`;
    }).join("");
    return `<section class="tape-group">
      <h3>${escapeHtml(group.title)}</h3>
      <div class="tape-group-grid">${items}</div>
    </section>`;
  }).join("");
  const newest = rows.map((row) => row.observed_at || row.date).filter(Boolean).sort().at(-1);
  $("#as-of").textContent = `As of ${newest || "unavailable"}`;
  setApiStatus(true, "API Online");
}

function inlineMarkdown(value) {
  return escapeHtml(value)
    .replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>")
    .replace(/`(.+?)`/g, "<code>$1</code>");
}

function renderMarkdown(markdown) {
  const lines = markdown.split(/\r?\n/);
  const output = [];
  for (let i = 0; i < lines.length; i += 1) {
    const line = lines[i];
    if (/^\|/.test(line) && i + 1 < lines.length && /^\|\s*---/.test(lines[i + 1])) {
      const headers = line.split("|").slice(1, -1).map((cell) => cell.trim());
      i += 2;
      const rows = [];
      while (i < lines.length && /^\|/.test(lines[i])) {
        rows.push(lines[i].split("|").slice(1, -1).map((cell) => cell.trim()));
        i += 1;
      }
      i -= 1;
      output.push(`<div class="table-scroll"><table><thead><tr>${headers.map((cell) => `<th>${inlineMarkdown(cell)}</th>`).join("")}</tr></thead><tbody>${rows.map((row) => `<tr>${row.map((cell) => `<td>${inlineMarkdown(cell)}</td>`).join("")}</tr>`).join("")}</tbody></table></div>`);
    } else if (line.startsWith("# ")) output.push(`<h1>${inlineMarkdown(line.slice(2))}</h1>`);
    else if (line.startsWith("## ")) output.push(`<h2>${inlineMarkdown(line.slice(3))}</h2>`);
    else if (line.startsWith("### ")) output.push(`<h3>${inlineMarkdown(line.slice(4))}</h3>`);
    else if (line.startsWith("#### ")) output.push(`<h4>${inlineMarkdown(line.slice(5))}</h4>`);
    else if (line.startsWith("- ")) {
      const items = [line.slice(2)];
      while (i + 1 < lines.length && lines[i + 1].startsWith("- ")) items.push(lines[++i].slice(2));
      output.push(`<ul>${items.map((item) => `<li>${inlineMarkdown(item)}</li>`).join("")}</ul>`);
    } else if (line.trim()) output.push(`<p>${inlineMarkdown(line)}</p>`);
  }
  return output.join("");
}

function metric(markdown, pattern, fallback = "--") {
  return markdown.match(pattern)?.[1] ?? fallback;
}

function firstReportBullet(markdown) {
  const lines = markdown.split(/\r?\n/).map((line) => line.trim()).filter(Boolean);
  const bullet = lines.find((line) => line.startsWith("- ") && !/Generated at:/i.test(line));
  return bullet ? bullet.slice(2).replace(/\*\*/g, "") : "Latest rule-based report loaded. Review the market update for full evidence and risk notes.";
}

function parseReportMetrics(markdown) {
  const regimeScore = metric(markdown, /Regime score:\s+\*\*([\d.]+ \/ 100)\*\*/);
  const regimeLabel = metric(markdown, /Regime score:.*?\(([^)]+)\)/);
  $("#regime-score").textContent = regimeScore;
  $("#regime-label").textContent = regimeLabel;
  $("#strength-score").textContent = metric(markdown, /(?:US equity strength|Market strength):\s+\*\*([\d.]+ \/ 100)\*\*/);
  $("#strength-label").textContent = metric(markdown, /(?:US equity strength|Market strength):.*?\(([^)]+)\)/);
  $("#evidence-score").textContent = metric(markdown, /Evidence quality:\s+\*\*([\d.]+ \/ 100)\*\*/);
  const breadthAbove50 = metric(markdown, /above 50DMA [`\x27]?([\d.]+)%[`\x27]?/);
  $("#breadth-score").textContent = `${breadthAbove50}%`;
  $("#breadth-label").textContent = metric(markdown, /Breadth:\s+\*\*([^*]+)\*\*/);
  const generatedAt = metric(markdown, /Generated at:\s+([^\n]+)/, "Report timestamp unavailable");
  $("#report-time").textContent = generatedAt;
  const heroRegime = $("#hero-regime");
  const heroSummary = $("#hero-summary");
  const reportCoverage = $("#report-coverage");
  if (heroRegime) heroRegime.textContent = `${regimeLabel} - ${regimeScore}`;
  if (heroSummary) heroSummary.textContent = firstReportBullet(markdown);
  if (reportCoverage) reportCoverage.textContent = `Latest report - ${generatedAt}`;
}

async function loadReport() {
  const response = await fetch(REPORT_PATH);
  if (!response.ok) throw new Error("Published report not found");
  const markdown = await response.text();
  parseReportMetrics(markdown);
  const content = $("#report-content");
  if (!content) return;
  content.classList.remove("loading-block");
  content.innerHTML = renderMarkdown(markdown);
}

function shortQuery() {
  const fields = {
    ticker: $("#short-search")?.value.trim(), sector: $("#short-sector")?.value.trim(),
    industry: $("#short-industry")?.value.trim(), security_type: $("#short-security-type")?.value,
    regime: $("#short-regime")?.value, min_funding_short_score: $("#short-min-funding")?.value,
    min_funding_short_quality: $("#short-min-quality")?.value,
    min_short_activity_score: $("#short-min-activity")?.value,
    min_unwind_risk: $("#short-min-unwind")?.value,
    sort_by: $("#short-sort-by")?.value, sort_order: $("#short-sort-order")?.value,
    limit: shortState.limit, offset: shortState.offset
  };
  const params = new URLSearchParams();
  Object.entries(fields).forEach(([key, value]) => {
    if (value !== "" && value != null) params.set(key, value);
  });
  return params.toString();
}

function regimeLabel(value) {
  return String(value || "NEUTRAL_INCONCLUSIVE").replaceAll("_", " ").toLowerCase()
    .replace(/\b\w/g, (letter) => letter.toUpperCase());
}

function renderShortTable(payload) {
  const rows = payload.data || [];
  const table = $("#short-table");
  const empty = $("#short-empty");
  shortState.total = payload.total || 0;
  if (!rows.length) {
    table.hidden = true;
    empty.hidden = false;
  } else {
    table.hidden = false;
    empty.hidden = true;
  }
  const columns = [
    ["ticker", "Ticker"], ["name", "Name"], ["sector", "Sector"], ["latest_price", "Price"],
    ["si_change_pct_latest", "SI Change %"], ["days_to_cover", "DTC"], ["svr_20d", "SVR 20D"],
    ["svr_z20", "SVR Z20"], ["casv_10d", "CASV 10D"], ["short_position_score", "Position"],
    ["short_activity_score", "Activity"], ["funding_short_score", "Funding"],
    ["funding_short_quality_score", "Quality"], ["unwind_risk_score", "Unwind"],
    ["short_regime", "Regime"], ["regime_confidence", "Confidence"]
  ];
  table.querySelector("thead").innerHTML = `<tr>${columns.map(([, label]) => `<th>${escapeHtml(label)}</th>`).join("")}</tr>`;
  table.querySelector("tbody").innerHTML = rows.map((row) => `<tr>
    ${columns.map(([key]) => {
      if (key === "ticker") return `<td><button class="ticker-link" data-short-ticker="${escapeHtml(row.ticker)}">${escapeHtml(row.ticker)}</button></td>`;
      if (key === "short_regime") return `<td><span class="regime-badge">${escapeHtml(regimeLabel(row[key]))}</span></td>`;
      const value = key === "si_change_pct_latest" ? formatNumber(row[key]) : key === "name" || key === "sector" ? (row[key] ?? "n/a") : formatNumber(row[key]);
      return `<td>${escapeHtml(value)}</td>`;
    }).join("")}
  </tr>`).join("");
  table.querySelectorAll("[data-short-ticker]").forEach((button) => button.addEventListener("click", () => {
    loadSingleStock(button.dataset.shortTicker);
  }));
  const page = Math.floor(shortState.offset / shortState.limit) + 1;
  const pages = Math.max(1, Math.ceil(shortState.total / shortState.limit));
  $("#short-page").textContent = `Page ${page} of ${pages}`;
  $("#short-prev").disabled = shortState.offset === 0;
  $("#short-next").disabled = shortState.offset + shortState.limit >= shortState.total;
  $("#short-status").textContent = `${formatNumber(payload.total, 0)} latest ticker snapshots; values not reported remain n/a.`;
  const newest = rows[0];
  $("#short-freshness").textContent = newest
    ? `Short volume ${newest.latest_short_volume_date || "n/a"} · SI settlement ${newest.latest_si_settlement_date || "n/a"} · SI publication ${newest.latest_si_publication_date || "n/a"}`
    : "No matching snapshot dates";
}

async function loadShortAnalytics() {
  const payload = await apiFetch(`/short-analytics/latest?${shortQuery()}`);
  renderShortTable(payload);
}

function shortMetricRows(row, fields) {
  return fields.map(([key, label, kind]) => {
    const value = kind === "pct" ? formatPercent(row[key]) : kind === "rawpct" ? (row[key] == null ? "n/a" : `${formatNumber(row[key])}%`) : formatNumber(row[key]);
    return `<div class="indicator-row"><span>${escapeHtml(label)}</span><strong>${escapeHtml(value)}</strong></div>`;
  }).join("");
}

const REGIME_EVIDENCE = [
  ["flow_confirmation_signal", "Flow confirmation", "Relationship between published short-interest change, short activity and relative price action."],
  ["actual_si_change_1obs", "Latest published SI change", "Change from the prior published short-interest settlement."],
  ["short_position_score", "Short position score", "Persistence, percentile, days-to-cover and stability evidence."],
  ["short_activity_score", "Short activity score", "Current FINRA short-volume intensity versus the ticker's own history."],
  ["funding_short_score", "Funding-short likelihood", "Composite evidence for persistent short-positioning behavior."],
  ["funding_short_quality_score", "Funding-short quality", "Liquidity, stability, relative performance and squeeze-risk suitability."],
  ["unwind_risk_score", "Unwind risk", "Evidence that existing short positioning may be reversing."],
  ["short_interest_persistence", "SI persistence", "Share of observed periods supporting persistent short interest."],
  ["short_interest_trend", "SI trend", "Direction and statistical quality of the published short-interest trend."],
  ["short_interest_stability", "SI stability", "Consistency of short interest through time."],
  ["industry_relative_weakness", "Market-relative weakness", "Weakness versus SPY across medium and longer horizons."],
  ["pressure_effectiveness", "Pressure effectiveness", "Whether elevated short-volume periods historically coincided with relative weakness."],
  ["daily_short_activity", "Daily short activity", "Latest normalized short-volume activity score."],
  ["technical_compatibility", "Technical compatibility", "Price trend and momentum alignment with the short thesis."],
  ["capture_asymmetry", "Capture asymmetry", "Difference between downside and upside capture versus SPY."],
  ["institutional_liquidity", "Liquidity", "Trading-liquidity suitability; this does not identify who is trading."],
  ["evidence_completeness", "Evidence completeness", "Share of required model inputs available for classification."],
  ["evidence_fields_available", "Evidence fields", "Count of required model inputs available."],
];

function evidenceValue(key, value) {
  if (value == null) return "n/a";
  if (typeof value === "boolean") return value ? "Yes" : "No";
  if (key === "actual_si_change_1obs" || key === "evidence_completeness") return formatPercent(value);
  return typeof value === "number" ? formatNumber(value) : String(value).replaceAll("_", " ");
}

function renderRegimeReasons(value, row = {}) {
  if (!value || typeof value !== "object") return '<div class="empty-state">No structured regime evidence is available.</div>';
  const rows = REGIME_EVIDENCE.filter(([key]) => key in value);
  if (!rows.length) return '<div class="empty-state">No structured regime evidence is available.</div>';
  return `<div class="table-scroll"><table class="regime-evidence-table">
    <thead><tr><th>Evidence</th><th>Value</th><th>Role in classification</th></tr></thead>
    <tbody>${rows.map(([key, label, meaning]) => {
      const insufficientPressureHistory = key === "pressure_effectiveness" && row.short_pressure_effectiveness == null;
      const displayValue = insufficientPressureHistory ? "n/a" : evidenceValue(key, value[key]);
      const displayMeaning = insufficientPressureHistory
        ? `${meaning} Insufficient qualifying observations; the classifier uses a neutral prior.`
        : meaning;
      return `<tr><td>${escapeHtml(label)}</td><td>${escapeHtml(displayValue)}</td><td>${escapeHtml(displayMeaning)}</td></tr>`;
    }).join("")}</tbody>
  </table></div>`;
}

function renderShortDetail(row) {
  const groups = [
    ["Position State", [["short_interest", "Short interest"], ["previous_short_interest", "Previous SI"], ["si_change_pct_latest", "Latest SI change", "rawpct"], ["days_to_cover", "Days to cover"], ["si_slope_6m", "SI slope 6M"], ["si_slope_12m", "SI slope 12M"], ["si_persistence_12m", "SI persistence 12M", "pct"], ["own_si_percentile_3y", "Own SI percentile 3Y", "pct"], ["industry_si_percentile", "Industry SI percentile", "pct"]]],
    ["Daily Short Activity", [["short_volume_ratio", "SVR 1D", "pct"], ["svr_5d", "SVR 5D", "pct"], ["svr_20d", "SVR 20D", "pct"], ["svr_60d", "SVR 60D", "pct"], ["svr_z20", "SVR Z20"], ["svr_z60", "SVR Z60"], ["casv_5d", "CASV 5D"], ["casv_10d", "CASV 10D"], ["casv_20d", "CASV 20D"], ["short_activity_persistence", "Activity persistence", "pct"]]],
    ["Price / Relative", [["latest_price", "Latest price"], ["rel_return_1m", "Relative return 1M", "pct"], ["rel_return_3m", "Relative return 3M", "pct"], ["rel_return_6m", "Relative return 6M", "pct"], ["rel_return_12m", "Relative return 12M", "pct"], ["up_capture", "Upside capture"], ["down_capture", "Downside capture"], ["long_short_asymmetry", "Long/short asymmetry"], ["short_pressure_effectiveness", "Pressure effectiveness"]]],
    ["Technicals", [["ma20", "MA20"], ["ma50", "MA50"], ["ma100", "MA100"], ["ma200", "MA200"], ["price_vs_ma50_pct", "Price vs MA50", "rawpct"], ["price_vs_ma200_pct", "Price vs MA200", "rawpct"], ["rsi14", "RSI14"], ["macd", "MACD"], ["macd_signal", "MACD signal"], ["macd_histogram", "MACD histogram"]]],
    ["Scores", [["short_position_score", "Short position"], ["short_activity_score", "Short activity"], ["short_flow_confirmation_score", "Flow confirmation"], ["funding_short_score", "Funding likelihood"], ["funding_short_quality_score", "Funding quality"], ["unwind_risk_score", "Unwind risk"], ["regime_confidence", "Regime confidence"]]]
  ];
  $("#short-detail").innerHTML = `<div class="short-detail-head"><div><span class="eyebrow">${escapeHtml(row.security_type || "unknown")}</span><h3>${escapeHtml(row.ticker)} · ${escapeHtml(row.name || "Unnamed security")}</h3><p>${escapeHtml(row.sector || "Unclassified")} · ${escapeHtml(row.industry || "Unclassified")}</p></div><span class="regime-badge">${escapeHtml(regimeLabel(row.short_regime))}</span></div>
    <div class="freshness-strip"><span>Analytics ${escapeHtml(row.analytics_date || "n/a")}</span><span>Short volume ${escapeHtml(row.latest_short_volume_date || "n/a")}</span><span>SI settlement ${escapeHtml(row.latest_si_settlement_date || "n/a")}</span><span>SI publication ${escapeHtml(row.latest_si_publication_date || "n/a")}</span></div>
    <div class="short-detail-grid">${groups.map(([title, fields]) => `<section class="indicator-group"><h4>${escapeHtml(title)}</h4>${shortMetricRows(row, fields)}</section>`).join("")}</div>
    <section class="regime-reasons"><h4>Short-Positioning Regime Evidence</h4><p>These are the observable and calculated inputs behind this stock's deterministic short-positioning classification. They are separate from the dashboard's macro market regime.</p>${renderRegimeReasons(row.regime_reason_json, row)}</section>`;
}

async function loadShortTicker(ticker = $("#short-detail-ticker")?.value.trim()) {
  if (!ticker) return;
  const detail = $("#short-detail");
  detail.innerHTML = '<div class="skeleton">Loading the latest FINRA analytics.</div>';
  try {
    const payload = await apiFetch(`/short-analytics/latest/${encodeURIComponent(ticker.toUpperCase())}`);
    renderShortDetail(payload.data);
  } catch (error) {
    detail.innerHTML = `<div class="empty-state">No latest short-positioning snapshot is available for ${escapeHtml(ticker.toUpperCase())}.</div>`;
  }
}

async function loadSingleStock(ticker) {
  const symbol = String(ticker || "").trim().toUpperCase();
  if (!symbol) return;
  $("#short-detail-ticker").value = symbol;
  $("#asset-type").value = "equities";
  $("#symbol").value = symbol;
  $("#query-mode").value = "latest";
  updateQueryControls();
  await Promise.allSettled([loadShortTicker(symbol), runQuery()]);
}

function drawChart(rows, symbol, asset) {
  const svg = $("#history-chart");
  const ordered = [...rows].reverse().filter((row) =>
    ["open", "high", "low", "close"].every((key) => Number.isFinite(Number(row[key])))
  );
  if (ordered.length < 2) {
    svg.innerHTML = '<text x="500" y="160" text-anchor="middle" class="chart-label">Insufficient history</text>';
    return;
  }
  const width = 1000, height = 360, left = 58, right = 18, top = 20, priceBottom = 270, volumeTop = 292, bottom = 336;
  const highs = ordered.map((row) => Number(row.high));
  const lows = ordered.map((row) => Number(row.low));
  const volumes = ordered.map((row) => Number(row.volume)).filter(Number.isFinite);
  const min = Math.min(...lows), max = Math.max(...highs), range = max - min || 1;
  const maxVolume = Math.max(...volumes, 1);
  const chartWidth = width - left - right;
  const step = chartWidth / ordered.length;
  const bodyWidth = Math.max(3, Math.min(10, step * 0.58));
  const xFor = (index) => left + (index + 0.5) * step;
  const yFor = (value) => top + ((max - Number(value)) / range) * (priceBottom - top);
  const grids = [0, .25, .5, .75, 1].map((fraction) => {
    const y = top + fraction * (priceBottom - top);
    const label = max - fraction * range;
    return `<line x1="${left}" y1="${y}" x2="${width - right}" y2="${y}" class="chart-grid"/>
      <text x="${left - 8}" y="${y + 4}" text-anchor="end" class="chart-label">${formatNumber(label)}</text>`;
  }).join("");
  const candles = ordered.map((row, index) => {
    const x = xFor(index);
    const open = Number(row.open), high = Number(row.high), low = Number(row.low), close = Number(row.close);
    const up = close >= open;
    const bodyTop = yFor(Math.max(open, close));
    const bodyHeight = Math.max(1, Math.abs(yFor(open) - yFor(close)));
    return `<g class="${up ? "candle-up" : "candle-down"}">
      <line x1="${x}" x2="${x}" y1="${yFor(high)}" y2="${yFor(low)}" class="candle-wick"/>
      <rect x="${x - bodyWidth / 2}" y="${bodyTop}" width="${bodyWidth}" height="${bodyHeight}" class="candle-body"/>
    </g>`;
  }).join("");
  const volumeBars = ordered.map((row, index) => {
    const volume = Number(row.volume);
    if (!Number.isFinite(volume) || volume <= 0) return "";
    const x = xFor(index);
    const barHeight = (volume / maxVolume) * (bottom - volumeTop);
    const up = Number(row.close) >= Number(row.open);
    return `<rect x="${x - bodyWidth / 2}" y="${bottom - barHeight}" width="${bodyWidth}" height="${barHeight}" class="${up ? "volume-up" : "volume-down"}"/>`;
  }).join("");
  svg.innerHTML = `${grids}<line x1="${left}" y1="${volumeTop}" x2="${width - right}" y2="${volumeTop}" class="chart-grid"/>${volumeBars}${candles}`;
  const latest = ordered.at(-1), first = ordered[0];
  const periodChange = ((Number(latest.close) / Number(first.close)) - 1) * 100;
  $("#chart-summary").innerHTML = `<strong>${escapeHtml(symbol)}</strong> · ${escapeHtml(asset)} · OHLCV · ${ordered.length} sessions ·
    <span class="${periodChange >= 0 ? "positive" : "negative"}">${periodChange >= 0 ? "+" : ""}${formatNumber(periodChange)}%</span>
    · ${escapeHtml(first.date)} to ${escapeHtml(latest.date)}`;
}

async function loadChart() {
  const asset = $("#chart-asset").value;
  const symbol = $("#chart-symbol").value.trim().toUpperCase();
  if (!symbol) {
    $("#chart-summary").textContent = "Enter a symbol.";
    return;
  }
  $("#chart-summary").textContent = "Loading history...";
  const result = await apiFetch(`/${asset}/history/${encodeURIComponent(symbol)}?limit=90`);
  drawChart(result.data || [], symbol, asset);
}

function updateChartSymbols() {
  const asset = $("#chart-asset").value;
  const macroOptions = [
    ["^GSPC", "S&P 500"], ["^IXIC", "Nasdaq Composite"], ["^RUT", "Russell 2000"],
    ["^VIX", "VIX"], ["^SKEW", "CBOE SKEW"], ["US10YT=X", "10Y Treasury"], ["GC=F", "Gold"], ["SI=F", "Silver"],
    ["HG=F", "Copper"], ["CL=F", "WTI Oil"]
  ];
  const equityOptions = [
    ["SPY", "SPY"], ["QQQ", "QQQ"], ["IWM", "IWM"], ["SMH", "SMH"], ["SOXX", "SOXX"],
    ["CIBR", "CIBR"], ["XAR", "XAR"], ["NLR", "NLR"], ["GRID", "GRID"], ["XLV", "XLV"]
  ];
  const options = asset === "equities" ? equityOptions : macroOptions;
  $("#chart-symbol-options").innerHTML = options.map(([value, label]) => `<option value="${escapeHtml(value)}">${escapeHtml(label)}</option>`).join("");
  const current = $("#chart-symbol").value.trim().toUpperCase();
  if (!current || !options.some(([value]) => value === current)) {
    $("#chart-symbol").value = options[0][0];
  }
}

function updateQueryControls() {
  const mode = $("#query-mode").value;
  const asset = $("#asset-type").value;
  $("#date-field").style.display = mode === "date" ? "grid" : "none";
  $("#limit-field").style.display = mode === "history" ? "grid" : "none";
  const liveOption = [...$("#query-mode").options].find((option) => option.value === "live");
  liveOption.disabled = asset === "equities";
  if (asset === "equities" && mode === "live") $("#query-mode").value = "latest";
}

function renderResult(payload) {
  const rows = Array.isArray(payload.data) ? payload.data : payload.data ? [payload.data] : [];
  const table = $("#result-table");
  const empty = $("#result-empty");
  if (!rows.length) {
    table.style.display = "none";
    empty.style.display = "block";
    empty.textContent = payload.message || "No rows returned.";
    return;
  }
  const preferred = ["date", "observed_at", "ticker", "symbol", "name", "close", "change", "pct_chg", "volume", "rsi_14", "ma_20", "ma_50", "ma_200", "is_live", "data_source"];
  const keys = [...preferred.filter((key) => key in rows[0]), ...Object.keys(rows[0]).filter((key) => !preferred.includes(key))];
  table.style.display = "table";
  empty.style.display = "none";
  table.querySelector("thead").innerHTML = `<tr>${keys.map((key) => `<th>${escapeHtml(key)}</th>`).join("")}</tr>`;
  table.querySelector("tbody").innerHTML = rows.map((row) => `<tr>${keys.map((key) => `<td>${escapeHtml(row[key] ?? "")}</td>`).join("")}</tr>`).join("");
}

function indicatorValue(value, suffix = "") {
  if (value == null || value === "") return "n/a";
  return `${formatNumber(value)}${suffix}`;
}

function renderEquityIndicators(payload, asset) {
  const panel = $("#indicator-panel");
  const rows = Array.isArray(payload.data) ? payload.data : payload.data ? [payload.data] : [];
  const row = rows[0];
  if (asset !== "equities" || !row) {
    panel.hidden = true;
    panel.innerHTML = "";
    return;
  }
  const availableCount = INDICATOR_GROUPS.flatMap((group) => group.fields)
    .filter(([field]) => row[field] != null).length;
  panel.hidden = false;
  panel.innerHTML = `<div class="indicator-head">
      <h3>${escapeHtml(row.ticker || "")} Technical Map</h3>
      <span>Close ${escapeHtml(row.date || "unavailable")} · Indicators ${escapeHtml(row.indicator_date || "unavailable")}</span>
    </div>
    <div class="indicator-groups">${INDICATOR_GROUPS.map((group) => `<section class="indicator-group">
      <h4>${escapeHtml(group.title)}</h4>
      ${group.fields.map(([field, label, suffix = ""]) => `<div class="indicator-row">
        <span>${escapeHtml(label)}</span><strong>${indicatorValue(row[field], suffix)}</strong>
      </div>`).join("")}
    </section>`).join("")}</div>
    <p class="indicator-note">${availableCount
      ? `${availableCount} same-date fields available from public.us_equities_indicators.`
      : "No same-date indicator row is available; price data is shown without carried-forward or inferred technicals."}</p>`;
}

async function runQuery(event) {
  event?.preventDefault();
  const asset = $("#asset-type").value;
  const symbol = $("#symbol").value.trim().toUpperCase();
  const mode = $("#query-mode").value;
  const date = $("#query-date").value;
  const limit = $("#query-limit").value;
  let path;
  if (mode === "latest") path = `/${asset}/latest/${encodeURIComponent(symbol)}`;
  else if (mode === "live") path = `/macro/live/${encodeURIComponent(symbol)}`;
  else if (mode === "date") {
    if (!date) return ($("#query-status").textContent = "Select a custom date.");
    path = `/${asset}/date/${encodeURIComponent(symbol)}?date=${encodeURIComponent(date)}`;
  } else path = `/${asset}/history/${encodeURIComponent(symbol)}?limit=${encodeURIComponent(limit)}`;
  $("#query-endpoint").textContent = path;
  $("#query-status").textContent = "Loading...";
  try {
    const payload = await apiFetch(path);
    renderResult(payload);
    renderEquityIndicators(payload, asset);
    $("#query-status").textContent = `${payload.count ?? (payload.found ? 1 : 0)} row(s) returned`;
  } catch (error) {
    renderEquityIndicators({}, asset);
    $("#query-status").textContent = `Request failed: ${error.message}`;
  }
}

async function runSingleSymbolQuery(event) {
  event.preventDefault();
  const asset = $("#asset-type").value;
  const symbol = $("#symbol").value.trim().toUpperCase();
  await runQuery();
  if (asset === "equities" && symbol) {
    $("#short-detail-ticker").value = symbol;
    await loadShortTicker(symbol);
  }
}

async function refreshDashboard() {
  setApiStatus(false, "Connecting");
  const [macroOutcome, reportOutcome, , shortOutcome] = await Promise.allSettled([loadMacroTape(), loadReport(), loadChart(), loadShortAnalytics(), loadSingleStock("AMD")]);
  if (macroOutcome.status === "rejected") {
    setApiStatus(false, "Unavailable");
    const macroTape = $("#macro-tape");
    if (macroTape) macroTape.innerHTML = `<div class="empty-state">API unavailable. Retry after the market data service recovers.<br>${escapeHtml(macroOutcome.reason.message)}</div>`;
  }
  if (reportOutcome.status === "rejected") {
    const reportContent = $("#report-content");
    if (reportContent) reportContent.innerHTML = `<div class="empty-state">Market report unavailable.<br>${escapeHtml(reportOutcome.reason.message)}</div>`;
  }
  if (shortOutcome.status === "rejected") $("#short-status").textContent = `Short analytics unavailable: ${shortOutcome.reason.message}`;
}

$("#refresh").addEventListener("click", refreshDashboard);
$("#hero-refresh")?.addEventListener("click", refreshDashboard);
$("#chart-asset").addEventListener("change", () => {
  updateChartSymbols();
  loadChart();
});
$("#load-chart").addEventListener("click", loadChart);
$("#asset-type").addEventListener("change", updateQueryControls);
$("#query-mode").addEventListener("change", updateQueryControls);
$("#data-form").addEventListener("submit", runSingleSymbolQuery);
$("#short-filter-form")?.addEventListener("submit", (event) => { event.preventDefault(); shortState.offset = 0; loadShortAnalytics(); });
$("#short-reset")?.addEventListener("click", () => { $("#short-filter-form").reset(); shortState.offset = 0; loadShortAnalytics(); });
$("#short-prev")?.addEventListener("click", () => { shortState.offset = Math.max(0, shortState.offset - shortState.limit); loadShortAnalytics(); });
$("#short-next")?.addEventListener("click", () => { shortState.offset += shortState.limit; loadShortAnalytics(); });
$("#short-detail-form")?.addEventListener("submit", (event) => { event.preventDefault(); loadSingleStock($("#short-detail-ticker").value); });
$("#toggle-report").addEventListener("click", () => {
  const content = $("#report-content");
  content.classList.toggle("expanded");
  $("#toggle-report").textContent = content.classList.contains("expanded") ? "Collapse report" : "Expand report";
});
function syncActiveNav() {
  const hash = window.location.hash || "#overview";
  document.querySelectorAll(".sidebar a, .topnav a").forEach((item) => {
    item.classList.toggle("active", item.getAttribute("href") === hash);
  });
}

document.querySelectorAll(".sidebar a, .topnav a").forEach((link) => link.addEventListener("click", () => {
  window.setTimeout(syncActiveNav, 0);
}));
window.addEventListener("hashchange", syncActiveNav);

updateQueryControls();
updateChartSymbols();
refreshDashboard();
syncActiveNav();

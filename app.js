const API_BASE = "https://postgresql-us-equities-api.onrender.com";
const MARKET_TAPE_GROUPS = [
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
      ["RTY=F", "Russell 2000 Future"]
    ]
  },
  {
    title: "UST Yield Moves",
    key: "rates",
    symbols: [
      ["^FVX", "UST 5Y"],
      ["^TNX", "UST 10Y"],
      ["^TYX", "UST 30Y"]
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

async function apiFetch(path) {
  const response = await fetch(`${API_BASE}${path}`, { headers: { Accept: "application/json" } });
  if (!response.ok) throw new Error(`${response.status} ${response.statusText}`);
  return response.json();
}

function setApiStatus(ok, message) {
  const element = $("#api-status");
  element.className = `status ${ok ? "ok" : "error"}`;
  element.innerHTML = `<i></i>${escapeHtml(message)}`;
}

async function loadMacroTape() {
  const payload = await apiFetch(`/macro/batch/latest?symbols=${encodeURIComponent(MARKET_TAPE_SYMBOLS.join(","))}`);
  const rows = payload.data || [];
  if (!rows.length) throw new Error("No macro rows returned");
  const rowsBySymbol = new Map(rows.map((row) => [row.symbol, row]));
  $("#macro-tape").classList.remove("loading-block");
  $("#macro-tape").innerHTML = MARKET_TAPE_GROUPS.map((group) => {
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

function parseReportMetrics(markdown) {
  $("#regime-score").textContent = metric(markdown, /Regime score:\s+\*\*([\d.]+ \/ 100)\*\*/);
  $("#regime-label").textContent = metric(markdown, /Regime score:.*?\(([^)]+)\)/);
  $("#strength-score").textContent = metric(markdown, /Market strength:\s+\*\*([\d.]+ \/ 100)\*\*/);
  $("#strength-label").textContent = metric(markdown, /Market strength:.*?\(([^)]+)\)/);
  $("#evidence-score").textContent = metric(markdown, /Evidence quality:\s+\*\*([\d.]+ \/ 100)\*\*/);
  $("#breadth-score").textContent = `${metric(markdown, /above 50DMA `([\d.]+)%`/)}%`;
  $("#breadth-label").textContent = metric(markdown, /Breadth:\s+\*\*([^*]+)\*\*/);
  $("#report-time").textContent = metric(markdown, /Generated at:\s+([^\n]+)/, "Report timestamp unavailable");

  const subscoreBlock = markdown.match(/## Market Regime Score\s+\| Sub-score[\s\S]*?(?=\n\nPositive contributors:)/)?.[0] || "";
  const rows = [...subscoreBlock.matchAll(/\|\s*([a-z_]+)\s*\|\s*([\d.]+)\s*\|/g)].slice(0, 9);
  $("#regime-bars").classList.remove("loading-block");
  $("#regime-bars").innerHTML = rows.map(([, label, value]) => `<div class="bar-row">
    <div class="bar-label"><span>${escapeHtml(label.replaceAll("_", " "))}</span><strong>${escapeHtml(value)}</strong></div>
    <div class="bar-track"><div class="bar-fill" style="width:${Math.min(100, Number(value))}%"></div></div>
  </div>`).join("");
}

async function loadReport() {
  const response = await fetch(REPORT_PATH);
  if (!response.ok) throw new Error("Published report not found");
  const markdown = await response.text();
  parseReportMetrics(markdown);
  const content = $("#report-content");
  content.classList.remove("loading-block");
  content.innerHTML = renderMarkdown(markdown);
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
  const symbol = $("#chart-symbol").value;
  $("#chart-summary").textContent = "Loading history...";
  const result = await apiFetch(`/${asset}/history/${encodeURIComponent(symbol)}?limit=90`);
  drawChart(result.data || [], symbol, asset);
}

function updateChartSymbols() {
  const asset = $("#chart-asset").value;
  const macroOptions = [
    ["^GSPC", "S&P 500"], ["^IXIC", "Nasdaq Composite"], ["^RUT", "Russell 2000"],
    ["^VIX", "VIX"], ["^TNX", "10Y Treasury"], ["GC=F", "Gold"], ["SI=F", "Silver"],
    ["HG=F", "Copper"], ["CL=F", "WTI Oil"]
  ];
  const equityOptions = [
    ["SPY", "SPY"], ["QQQ", "QQQ"], ["IWM", "IWM"], ["SMH", "SMH"], ["SOXX", "SOXX"],
    ["CIBR", "CIBR"], ["XAR", "XAR"], ["NLR", "NLR"], ["GRID", "GRID"], ["XLV", "XLV"]
  ];
  const options = asset === "equities" ? equityOptions : macroOptions;
  $("#chart-symbol").innerHTML = options.map(([value, label]) => `<option value="${escapeHtml(value)}">${escapeHtml(label)}</option>`).join("");
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
  event.preventDefault();
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

async function refreshDashboard() {
  setApiStatus(false, "Connecting");
  const outcomes = await Promise.allSettled([loadMacroTape(), loadReport(), loadChart()]);
  if (outcomes[0].status === "rejected") {
    setApiStatus(false, "API Unavailable");
    $("#macro-tape").textContent = outcomes[0].reason.message;
  }
  if (outcomes[1].status === "rejected") $("#report-content").textContent = outcomes[1].reason.message;
}

$("#refresh").addEventListener("click", refreshDashboard);
$("#chart-asset").addEventListener("change", () => {
  updateChartSymbols();
  loadChart();
});
$("#load-chart").addEventListener("click", loadChart);
$("#asset-type").addEventListener("change", updateQueryControls);
$("#query-mode").addEventListener("change", updateQueryControls);
$("#data-form").addEventListener("submit", runQuery);
$("#toggle-report").addEventListener("click", () => {
  const content = $("#report-content");
  content.classList.toggle("expanded");
  $("#toggle-report").textContent = content.classList.contains("expanded") ? "Collapse report" : "Expand report";
});
document.querySelectorAll(".sidebar a").forEach((link) => link.addEventListener("click", () => {
  document.querySelectorAll(".sidebar a").forEach((item) => item.classList.remove("active"));
  link.classList.add("active");
}));

updateQueryControls();
updateChartSymbols();
refreshDashboard();

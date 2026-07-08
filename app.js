const API_BASE = "https://postgresql-us-equities-api.onrender.com";
const MACRO_SYMBOLS = ["^GSPC", "^IXIC", "^RUT", "^VIX", "^TNX", "GC=F", "SI=F", "HG=F", "CL=F", "HYG", "BTC-USD", "DX-Y.NYB"];
const REPORT_PATH = "data/latest-report.md";

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
  const results = await Promise.allSettled(
    MACRO_SYMBOLS.map((symbol) => apiFetch(`/macro/latest/${encodeURIComponent(symbol)}`))
  );
  const rows = results
    .filter((result) => result.status === "fulfilled" && result.value.found)
    .map((result) => result.value.data);
  if (!rows.length) throw new Error("No macro rows returned");
  $("#macro-tape").classList.remove("loading-block");
  $("#macro-tape").innerHTML = rows.map((row) => {
    const changeClass = Number(row.pct_chg) > 0 ? "positive" : Number(row.pct_chg) < 0 ? "negative" : "";
    return `<div class="tape-item">
      <span>${escapeHtml(row.name || row.symbol)}${row.is_live ? '<small class="live-tag">LIVE</small>' : ""}</span>
      <strong>${formatNumber(row.close)}</strong>
      <small class="${changeClass}">${Number(row.pct_chg) > 0 ? "+" : ""}${formatNumber(row.pct_chg)}%</small>
      <small>${escapeHtml(row.date)} · ${escapeHtml(row.data_source)}</small>
    </div>`;
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

function drawChart(rows, symbol) {
  const svg = $("#history-chart");
  const values = rows.map((row) => Number(row.close)).filter(Number.isFinite);
  if (values.length < 2) {
    svg.innerHTML = '<text x="500" y="160" text-anchor="middle" class="chart-label">Insufficient history</text>';
    return;
  }
  const width = 1000, height = 320, left = 58, right = 18, top = 20, bottom = 36;
  const min = Math.min(...values), max = Math.max(...values), range = max - min || 1;
  const ordered = [...rows].reverse();
  const points = ordered.map((row, index) => {
    const x = left + (index / (ordered.length - 1)) * (width - left - right);
    const y = top + ((max - Number(row.close)) / range) * (height - top - bottom);
    return [x, y];
  });
  const line = points.map(([x, y]) => `${x.toFixed(1)},${y.toFixed(1)}`).join(" ");
  const area = `${left},${height - bottom} ${line} ${width - right},${height - bottom}`;
  const grids = [0, .25, .5, .75, 1].map((fraction) => {
    const y = top + fraction * (height - top - bottom);
    const label = max - fraction * range;
    return `<line x1="${left}" y1="${y}" x2="${width - right}" y2="${y}" class="chart-grid"/>
      <text x="${left - 8}" y="${y + 4}" text-anchor="end" class="chart-label">${formatNumber(label)}</text>`;
  }).join("");
  svg.innerHTML = `${grids}<polygon points="${area}" class="chart-area"/><polyline points="${line}" class="chart-line"/>`;
  const latest = ordered.at(-1), first = ordered[0];
  const periodChange = ((Number(latest.close) / Number(first.close)) - 1) * 100;
  $("#chart-summary").innerHTML = `<strong>${escapeHtml(symbol)}</strong> · ${ordered.length} sessions · 
    <span class="${periodChange >= 0 ? "positive" : "negative"}">${periodChange >= 0 ? "+" : ""}${formatNumber(periodChange)}%</span>
    · ${escapeHtml(first.date)} to ${escapeHtml(latest.date)}`;
}

async function loadChart() {
  const symbol = $("#chart-symbol").value;
  $("#chart-summary").textContent = "Loading history...";
  const result = await apiFetch(`/macro/history/${encodeURIComponent(symbol)}?limit=90`);
  drawChart(result.data || [], symbol);
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
    $("#query-status").textContent = `${payload.count ?? (payload.found ? 1 : 0)} row(s) returned`;
  } catch (error) {
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
refreshDashboard();

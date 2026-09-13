import fs from "node:fs";

const marketApiBaseUrl = (process.env.MARKET_API_BASE_URL || "").replace(/\/+$/, "");

if (!marketApiBaseUrl) {
  throw new Error("MARKET_API_BASE_URL is required");
}

const config = `window.MARKET_DASHBOARD_CONFIG = Object.freeze({ marketApiBaseUrl: ${JSON.stringify(marketApiBaseUrl)} });\n`;
fs.writeFileSync("config.js", config, "utf8");

# Market Intelligence Dashboard

Static GitHub Pages dashboard for the Market Intelligence ecosystem.

Live site: https://wkyjim.github.io/market-dashboard/#overview
Repository: https://github.com/wkyjim/market-dashboard
Local path: `C:\Users\User\OneDrive\Coding\DB_builder\market-dashboard`

## Purpose

Market Intelligence presents deterministic market analytics from the PostgreSQL / Neon-backed market data stack. It combines a cross-asset macro tape, OHLCV price-history charting, the latest rule-based market update, and unified single-stock short-positioning, price, technical and historical analytics.

Aegis is the dashboard identity: the Market Intelligence Sentinel. The visual system is designed to feel institutional, calm, precise, risk-aware, and data-driven.

Primary message: See clearly. Decide precisely. Act with discipline.

## Project Structure

```text
market-dashboard/
|-- index.html
|-- styles.css
|-- app.js
|-- assets/
|   `-- images/
|       `-- aegis/
|           |-- aegis-avatar.png
|           |-- aegis-hero.png
|           `-- aegis-hero-mobile.png
|-- data/
|   `-- latest-report.md
|-- .github/
|   `-- workflows/
|       `-- pages.yml
|-- .gitignore
|-- .nojekyll
`-- README.md
```

The site intentionally remains a lightweight static application. CSS and JavaScript were kept in root files to preserve the existing GitHub Pages deployment and reduce risk to the working API integration.

## Data Sources

- Public API base URL: `https://postgresql-us-equities-api.onrender.com`
- Published report path: `data/latest-report.md`
- Live dashboard URL: `https://wkyjim.github.io/market-dashboard/#overview`

The API is consumed directly by `app.js`. Do not commit API tokens, database URLs, Neon credentials, Telegram tokens, or private config files.

## Main Navigation

The dashboard preserves these hash routes:

```text
#overview
#cross-asset
#report
#explorer
```

These routes are used by the page shell, sidebar, top navigation, browser history, and linked Telegram/dashboard references.

## Aegis Assets

Image assets live under:

```text
assets/images/aegis/aegis-avatar.png
assets/images/aegis/aegis-hero.png
assets/images/aegis/aegis-hero-mobile.png
```

Usage:

- `aegis-avatar.png`: header identity, sidebar sentinel marker, favicon.
- `aegis-hero.png`: desktop overview hero.
- `aegis-hero-mobile.png`: mobile and narrow-tablet overview hero.

Keep the PNG originals in the repository. Optional optimized WebP variants may be added later, but do not remove the supplied PNG files unless all references are updated and visually verified.

## Local Preview

From this folder:

```powershell
python -m http.server 8000
```

Open:

```text
http://localhost:8000
```

Useful checks:

- `http://localhost:8000/#overview`
- `http://localhost:8000/#cross-asset`
- `http://localhost:8000/#report`
- `http://localhost:8000/#explorer`

## GitHub Pages Deployment

The site deploys from the `main` branch using `.github/workflows/pages.yml`.

The workflow uploads the static repository contents as a GitHub Pages artifact. Preserve relative asset paths so the site works under:

```text
https://wkyjim.github.io/market-dashboard/
```

## Report Publishing

The generated deterministic report is expected at:

```text
data/latest-report.md
```

The broader DB_builder report process should update this file and push the dashboard repository. The dashboard then renders the report and exposes it to the Telegram bot through the public GitHub Pages URL.

## Ecosystem Architecture

```text
Market data ingestion / PostgreSQL / Neon
-> Render market API
-> rule-based report generation
-> market-dashboard/data/latest-report.md
-> GitHub Pages dashboard
-> Telegram bot report links and commands
```

Related local projects under `C:\Users\User\OneDrive\Coding\DB_builder` include the database/report generator workspace, the Market Dashboard repository, and the standalone Telegram bot repository. Keep independent Git repositories separate.

## Security Notes

- Do not commit `.env` files.
- Do not commit Neon connection strings.
- Do not commit Telegram credentials.
- Do not expose private Render or database configuration in static files.
- Public URLs already used by the dashboard and Telegram bot are safe to document.

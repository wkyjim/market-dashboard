# Market Intelligence Dashboard

Static institutional market dashboard for GitHub Pages.

## Data

- Live and historical market data: Neon-backed Render API
- Market update: latest published deterministic rule-based report
- Equities are close-only
- Macro latest endpoints prefer live snapshots and fall back to latest close

## Local preview

```powershell
python -m http.server 8000
```

Open `http://localhost:8000`.

## GitHub Pages

The site is deployed from the `main` branch using `.github/workflows/pages.yml`.

The published report is stored at `data/latest-report.md`. Replace that file with a newer generated rule-based report and push to publish an update.

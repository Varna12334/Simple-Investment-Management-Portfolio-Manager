# Simple Investment Management — Portfolio Manager

A small tool to manage investments (stocks / mutual funds), calculate total invested value, compute profit or loss, and show a portfolio summary.

---

![Hero illustration]
https://acrobat.adobe.com/id/urn:aaid:sc:AP:c9ea9f42-541f-4678-8713-bd72b2c2a10b


Quick visual guide below will help viewers understand the app at a glance — what you do (add investments), what the app calculates, and what it shows.

## Features (visual)
- Add investments (stock / mutual fund) — docs/images/add.png
- Calculate total investment — docs/images/total.png
- Calculate profit or loss — docs/images/profit.png
- Show portfolio summary (table + charts) — https://acrobat.adobe.com/id/urn:aaid:sc:AP:c9ea9f42-541f-4678-8713-bd72b2c2a10b



## Workflow (diagram)
https://acrobat.adobe.com/id/urn:aaid:sc:AP:4aabf1d6-a50c-4283-9aaf-ed814f44c886
```mermaid
flowchart LR
  A[User: Add investment] --> B[Store investment record]
  B --> C[Calculate totals & current value]
  C --> D[Compute profit / loss]
  D --> E[Show portfolio summary (table & charts)]
  E --> F[Export / Reports (CSV, PDF)]
```

## Example visuals to include
Add the following images to `docs/images/` and reference them in the README:

- `hero.png` — a simple banner or mockup showing portfolio + charts.
- `add.png` — small illustration of adding an investment (form or plus icon).
- `total.png` — icon or tiny bar showing "Total Invested".
- `profit.png` — simple up/down arrows showing profit/loss.
- `summary.png` — screenshot or mockup of the portfolio summary with a pie chart and a table.
- `portfolio_chart.png` — example pie or line chart produced by the app for a sample portfolio.

Each image should have a short caption / alt text so the README remains accessible.

## Example: generate a portfolio pie chart (Python)
Use this script to create a sample chart to include in the README:

```python
import matplotlib.pyplot as plt

labels = ['AAPL', 'MSFT', 'Vanguard 500', 'Cash']
sizes = [30, 25, 35, 10]
colors = ['#2ca02c', '#1f77b4', '#ff7f0e', '#7f7f7f']

plt.figure(figsize=(6,6))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title('Sample Portfolio Allocation')
plt.savefig('docs/images/portfolio_chart.png', bbox_inches='tight', dpi=150)
```

## How to add images to the repo
1. Create folder `docs/images/`.
2. Put images there (PNG/SVG recommended).
3. Commit and push.
4. Reference them in the README with: `![Alt text](docs/images/portfolio_chart.png)`.

## Recommended tools to make images
- Diagrams & flowcharts: draw.io / diagrams.net, Figma, Lucidchart, or Mermaid (embedded).
- Icons & illustrations: https://iconmonstr.com, https://undraw.co, or use simple SVGs.
- Charts: Matplotlib, Plotly, or Excel → export PNG.

---

If you want, I can:
- generate the Mermaid diagram as an SVG,
- create example chart images (PNG) from your sample data,
- or produce ready-to-commit image files and update the README for you.

Tell me which images you'd like me to create first (diagram, chart, or mockup screenshot) and — if relevant — paste a small sample of your portfolio data (ticker, quantity, buy price, current price) so I can make realistic charts.

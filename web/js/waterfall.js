/**
 * Waterfall view — cost pool flow chart for a single year.
 */
import { fmtPLN, getAllEvents } from './data.js';
import { createCanvas, drawWaterfallChart } from './charts.js';

export function renderWaterfall(app, yearData, year) {
  const events = getAllEvents(yearData);
  const costsPrior = parseFloat(yearData.costs_prior_years_pln) || 0;
  const revenue = parseFloat(yearData.revenue_pln) || 0;
  const costsCurrent = parseFloat(yearData.costs_current_year_pln) || 0;
  const carryForward = parseFloat(yearData.carry_forward_pln) || 0;

  let html = `
    <a href="#/year/${year}" class="back-btn">← Back to ${year} Events</a>
    <div class="section-header">
      <h2 class="section-title">${year} — Cost Pool Waterfall</h2>
      <span class="section-subtitle">Visualizing how each event changes the cost pool</span>
    </div>

    <div class="waterfall-legend">
      <div class="legend-item"><div class="legend-swatch" style="background:#10b981"></div>Carry Forward</div>
      <div class="legend-item"><div class="legend-swatch" style="background:#818cf8"></div>Salary USDC</div>
      <div class="legend-item"><div class="legend-swatch" style="background:#14b8a6"></div>Purchases</div>
      <div class="legend-item"><div class="legend-swatch" style="background:#f59e0b"></div>Sales (Revenue)</div>
    </div>

    <div class="chart-container" id="waterfall-chart"></div>

    <div class="year-grid" style="grid-template-columns:repeat(4,1fr)">
      <div class="card">
        <div class="metric-label">Prior Carry-Forward</div>
        <div class="metric-value metric-cost" style="font-size:1.1rem;margin-top:8px">${fmtPLN(costsPrior)}</div>
      </div>
      <div class="card">
        <div class="metric-label">Costs This Year</div>
        <div class="metric-value metric-cost" style="font-size:1.1rem;margin-top:8px">${fmtPLN(costsCurrent)}</div>
      </div>
      <div class="card">
        <div class="metric-label">Revenue</div>
        <div class="metric-value metric-revenue" style="font-size:1.1rem;margin-top:8px">${fmtPLN(revenue)}</div>
      </div>
      <div class="card">
        <div class="metric-label">New Carry-Forward</div>
        <div class="metric-value metric-carry" style="font-size:1.1rem;margin-top:8px">${fmtPLN(carryForward)}</div>
      </div>
    </div>
  `;

  app.innerHTML = html;

  // Draw chart
  const container = document.getElementById('waterfall-chart');
  const containerWidth = container.clientWidth - 48; // subtract padding
  const { ctx } = createCanvas(container, containerWidth, 400);
  drawWaterfallChart(ctx, containerWidth, 400, events, costsPrior);
}

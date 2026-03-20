/**
 * Timeline view — multi-year carry-forward area chart.
 */
import { fmtPLN, getCarryChain } from './data.js';
import { createCanvas, drawTimelineChart } from './charts.js';

export function renderTimeline(app, data) {
  const chain = getCarryChain(data);
  const totalRevenue = chain.reduce((s, c) => s + c.revenue, 0);
  const totalCosts = chain.reduce((s, c) => s + c.costsCurrent, 0);
  const totalDisposals = chain.reduce((s, c) => s + c.disposals, 0);
  const finalCarry = chain[chain.length - 1]?.carryForward || 0;

  let html = `
    <a href="#/" class="back-btn">← Back to Dashboard</a>
    <div class="section-header">
      <h2 class="section-title">Carry-Forward Timeline (2020–2025)</h2>
      <span class="section-subtitle">Shows how the cost pool balance evolves across all years</span>
    </div>

    <div class="chart-container" id="timeline-chart"></div>

    <div class="year-grid" style="grid-template-columns:repeat(4,1fr)">
      <div class="card">
        <div class="metric-label">Total Revenue (all years)</div>
        <div class="metric-value metric-revenue" style="font-size:1.1rem;margin-top:8px">${fmtPLN(totalRevenue)}</div>
      </div>
      <div class="card">
        <div class="metric-label">Total Costs (all years)</div>
        <div class="metric-value metric-cost" style="font-size:1.1rem;margin-top:8px">${fmtPLN(totalCosts)}</div>
      </div>
      <div class="card">
        <div class="metric-label">Total Disposals</div>
        <div class="metric-value" style="font-size:1.1rem;margin-top:8px">${totalDisposals}</div>
      </div>
      <div class="card">
        <div class="metric-label">Current Carry-Forward</div>
        <div class="metric-value metric-carry" style="font-size:1.1rem;margin-top:8px">${fmtPLN(finalCarry)}</div>
      </div>
    </div>

    <div class="card" style="margin-top:16px">
      <h3 style="font-size:0.85rem;font-weight:700;text-transform:uppercase;letter-spacing:0.5px;color:var(--text-muted);margin-bottom:12px">Annual Breakdown</h3>
      <table class="data-table">
        <thead>
          <tr>
            <th>Year</th>
            <th>Disposals</th>
            <th>Revenue</th>
            <th>Costs (Current)</th>
            <th>Costs (Prior)</th>
            <th>Income</th>
            <th>Tax</th>
            <th>Carry-Forward</th>
          </tr>
        </thead>
        <tbody>
          ${chain.map(c => `<tr onclick="location.hash='#/year/${c.year}'" style="cursor:pointer">
            <td><strong>${c.year}</strong></td>
            <td class="cell-mono cell-right">${c.disposals}</td>
            <td class="cell-pln metric-revenue">${fmtPLN(c.revenue)}</td>
            <td class="cell-pln metric-cost">${fmtPLN(c.costsCurrent)}</td>
            <td class="cell-pln metric-cost">${fmtPLN(c.costsPrior)}</td>
            <td class="cell-pln">${fmtPLN(c.income)}</td>
            <td class="cell-pln ${c.tax > 0 ? 'metric-tax' : 'metric-zero'}">${c.tax > 0 ? fmtPLN(c.tax) : '0.00 PLN ✓'}</td>
            <td class="cell-pln metric-carry">${fmtPLN(c.carryForward)}</td>
          </tr>`).join('')}
        </tbody>
      </table>
    </div>
  `;

  app.innerHTML = html;

  // Draw chart
  const container = document.getElementById('timeline-chart');
  const containerWidth = container.clientWidth - 48;
  const { ctx } = createCanvas(container, containerWidth, 350);
  drawTimelineChart(ctx, containerWidth, 350, chain);
}

/**
 * Dashboard view — year overview cards with carry-forward chain.
 */
import { fmtPLN, fmtNum, getYears, getCarryChain } from './data.js';

export function renderDashboard(app, data) {
  const years = getYears(data);
  const chain = getCarryChain(data);
  const maxCarry = Math.max(...chain.map(c => c.carryForward), 1);

  let html = '<div class="animate-in">';

  // Carry-forward chain
  html += '<div class="section-header"><h2 class="section-title">Cost Pool Carry-Forward Chain</h2>';
  html += '<span class="section-subtitle">Art. 22 ust. 16 — unlimited carry-forward</span></div>';
  html += '<div class="card carry-chain">';
  chain.forEach((c, i) => {
    if (i > 0) html += '<span class="carry-arrow">→</span>';
    html += `<div class="carry-node">
      <span class="carry-node-year">${c.year}</span>
      <span class="carry-node-value">${fmtPLN(c.carryForward)}</span>
    </div>`;
  });
  html += '</div>';

  // Year cards
  html += '<div class="section-header"><h2 class="section-title">Annual PIT-38 Summary</h2>';
  html += '<span class="section-subtitle">Click any year for detailed breakdown</span></div>';
  html += '<div class="year-grid">';

  chain.forEach((c, i) => {
    const totalCosts = c.costsCurrent + c.costsPrior;
    const carryPct = Math.min((c.carryForward / maxCarry) * 100, 100);

    html += `<div class="card card-clickable animate-in" onclick="location.hash='#/year/${c.year}'">
      <div class="year-card-header">
        <span class="year-label">${c.year}</span>
        <span class="disposal-count">${c.disposals} disposal${c.disposals !== 1 ? 's' : ''}</span>
      </div>
      <div class="year-card-metrics">
        <div class="metric-row">
          <span class="metric-label">Revenue (przychód)</span>
          <span class="metric-value metric-revenue">${fmtPLN(c.revenue)}</span>
        </div>
        <div class="metric-row">
          <span class="metric-label">Costs this year</span>
          <span class="metric-value metric-cost">${fmtPLN(c.costsCurrent)}</span>
        </div>
        <div class="metric-row">
          <span class="metric-label">Costs from prior years</span>
          <span class="metric-value metric-cost">${fmtPLN(c.costsPrior)}</span>
        </div>
        <div class="metric-row" style="padding-top:8px;border-top:1px solid var(--border)">
          <span class="metric-label"><strong>Tax due</strong></span>
          <span class="metric-value ${c.tax > 0 ? 'metric-tax' : 'metric-zero'}">
            <strong>${c.tax > 0 ? fmtPLN(c.tax) : '0.00 PLN ✓'}</strong>
          </span>
        </div>
        <div class="metric-row">
          <span class="metric-label">Carry-forward → ${parseInt(c.year) + 1}</span>
          <span class="metric-value metric-carry">${fmtPLN(c.carryForward)}</span>
        </div>
      </div>
      <div class="carry-bar">
        <div class="carry-bar-fill" style="width:${carryPct}%"></div>
      </div>
    </div>`;
  });

  html += '</div></div>';
  app.innerHTML = html;
}

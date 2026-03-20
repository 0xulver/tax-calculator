/**
 * App entry point — hash-based router and initialization.
 */
import { loadDetail } from './data.js';
import { renderDashboard } from './dashboard.js';
import { renderEvents, resetFilters } from './events.js';
import { renderDrilldown } from './drilldown.js';
import { renderWaterfall } from './waterfall.js';
import { renderTimeline } from './timeline.js';

let data = null;

async function init() {
  data = await loadDetail();
  document.getElementById('loading').style.display = 'none';
  route();
}

function route() {
  const hash = location.hash || '#/';
  const app = document.getElementById('app');

  // Update nav active state
  document.querySelectorAll('.nav-link').forEach(link => {
    link.classList.remove('active');
    if (link.getAttribute('href') === hash ||
        (hash.startsWith('#/year') && link.dataset.view === 'dashboard') ||
        (hash.startsWith('#/event') && link.dataset.view === 'dashboard') ||
        (hash.startsWith('#/waterfall') && link.dataset.view === 'dashboard')) {
      link.classList.add('active');
    }
    if (hash === '#/' && link.dataset.view === 'dashboard') link.classList.add('active');
    if (hash === '#/timeline' && link.dataset.view === 'timeline') link.classList.add('active');
  });

  // Route matching
  if (hash === '#/' || hash === '') {
    renderDashboard(app, data);
  } else if (hash === '#/timeline') {
    renderTimeline(app, data);
  } else if (hash.startsWith('#/waterfall/')) {
    const year = hash.split('/')[2];
    const yearData = data.yearly_results[year];
    if (yearData) renderWaterfall(app, yearData, year);
    else renderDashboard(app, data);
  } else if (hash.startsWith('#/event/')) {
    const parts = hash.split('/');
    const year = parts[2];
    const idx = parseInt(parts[3]);
    const yearData = data.yearly_results[year];
    if (yearData && !isNaN(idx)) renderDrilldown(app, yearData, year, idx);
    else renderDashboard(app, data);
  } else if (hash.startsWith('#/year/')) {
    const year = hash.split('/')[2];
    const yearData = data.yearly_results[year];
    if (yearData) {
      resetFilters();
      const rerender = () => renderEvents(app, yearData, year, rerender);
      rerender();
    } else {
      renderDashboard(app, data);
    }
  } else {
    renderDashboard(app, data);
  }
}

// Listen for hash changes
window.addEventListener('hashchange', route);

// Boot
init().catch(err => {
  console.error('Failed to load data:', err);
  document.getElementById('app').innerHTML = `
    <div class="card" style="text-align:center;margin-top:40px">
      <h2 style="color:var(--rose)">Failed to load data</h2>
      <p style="color:var(--text-muted);margin-top:8px">Run <code>python web/export_data.py</code> first to generate the data files.</p>
      <p style="color:var(--text-muted);margin-top:8px">${err.message}</p>
    </div>
  `;
});

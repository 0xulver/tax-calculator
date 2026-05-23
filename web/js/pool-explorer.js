/**
 * Pool Explorer — cross-year transaction-level cost pool visualization.
 *
 * Flattens every revenue + cost event across all years into one timeline,
 * computes a running cost pool balance, and renders:
 *   1. An interactive SVG area chart
 *   2. A synchronised scrollable event table
 */
import { fmtPLN, fmtNum, getYears } from './data.js';

/* ------------------------------------------------------------------ */
/*  Data helpers                                                       */
/* ------------------------------------------------------------------ */

/** Flatten all events across all years into a single sorted timeline. */
export function buildPoolTimeline(data) {
  const years = getYears(data);
  const all = [];

  years.forEach(year => {
    const yr = data.yearly_results[year];
    (yr.revenue_events || []).forEach(e =>
      all.push({ ...e, _type: 'revenue', _year: year }));
    (yr.cost_events || []).forEach(e =>
      all.push({ ...e, _type: 'cost', _year: year }));
  });

  // Sort chronologically; ties broken: costs first (they add to pool before revenue removes)
  all.sort((a, b) => {
    const dc = a.date.localeCompare(b.date);
    if (dc !== 0) return dc;
    if (a._type === 'cost' && b._type === 'revenue') return -1;
    if (a._type === 'revenue' && b._type === 'cost') return 1;
    return 0;
  });

  // Compute running pool balance
  let pool = 0;
  let totalCosts = 0;
  let totalRevenue = 0;
  all.forEach((e, i) => {
    const val = parseFloat(e.pln_value) || 0;
    if (e._type === 'cost') {
      pool += val;
      totalCosts += val;
      e._delta = val;
    } else {
      pool -= val;
      totalRevenue += val;
      e._delta = -val;
    }
    e._pool = Math.max(pool, 0);
    e._rawPool = pool;
    e._index = i;
  });

  return { events: all, totalCosts, totalRevenue, finalPool: Math.max(pool, 0) };
}

/* ------------------------------------------------------------------ */
/*  Render helpers                                                     */
/* ------------------------------------------------------------------ */

function eventBadge(e) {
  if (e._type === 'revenue') return '<span class="badge badge-revenue">SELL</span>';
  if (e.source === 'polygon_salary') return '<span class="badge badge-salary">SALARY</span>';
  if (e.price_method && e.price_method.includes('fee')) return '<span class="badge badge-fee">FEE</span>';
  if (e.price_method && e.price_method.includes('stablecoin')) return '<span class="badge badge-deposit">DEP</span>';
  return '<span class="badge badge-cost">BUY</span>';
}

function eventCategory(e) {
  if (e._type === 'revenue') return 'revenue';
  if (e.source === 'polygon_salary') return 'salary';
  if (e.price_method && e.price_method.includes('fee')) return 'fee';
  return 'cost';
}

/** Get unique assets across timeline events */
function getUniqueAssets(events) {
  const s = new Set(events.map(e => e.asset));
  return [...s].sort();
}

/* ------------------------------------------------------------------ */
/*  SVG Chart                                                          */
/* ------------------------------------------------------------------ */

function renderSvgChart(events, containerId) {
  const container = document.getElementById(containerId);
  if (!container || events.length === 0) return;

  const rect = container.getBoundingClientRect();
  const W = rect.width - 48; // padding
  const H = 380;
  const pad = { top: 30, right: 30, bottom: 55, left: 85 };
  const plotW = W - pad.left - pad.right;
  const plotH = H - pad.top - pad.bottom;

  const maxPool = Math.max(...events.map(e => e._pool), 1);
  const minDate = new Date(events[0].date);
  const maxDate = new Date(events[events.length - 1].date);
  const dateRange = maxDate - minDate || 1;

  const x = (date) => pad.left + ((new Date(date) - minDate) / dateRange) * plotW;
  const y = (val) => pad.top + plotH - (val / maxPool) * plotH;

  // Build SVG
  let svg = `<svg class="pool-svg" viewBox="0 0 ${W} ${H}" width="${W}" height="${H}" xmlns="http://www.w3.org/2000/svg">`;

  // Defs — gradient fill
  svg += `<defs>
    <linearGradient id="pool-area-grad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#10b981" stop-opacity="0.35"/>
      <stop offset="100%" stop-color="#10b981" stop-opacity="0.02"/>
    </linearGradient>
    <linearGradient id="pool-line-grad" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#818cf8"/>
      <stop offset="100%" stop-color="#10b981"/>
    </linearGradient>
  </defs>`;

  // Grid lines
  const gridSteps = 6;
  for (let i = 0; i <= gridSteps; i++) {
    const gy = pad.top + (plotH / gridSteps) * i;
    const val = maxPool - (maxPool / gridSteps) * i;
    svg += `<line x1="${pad.left}" y1="${gy}" x2="${W - pad.right}" y2="${gy}" stroke="rgba(255,255,255,0.05)" stroke-width="1"/>`;
    svg += `<text x="${pad.left - 10}" y="${gy + 4}" fill="rgba(255,255,255,0.4)" font-size="10" font-family="JetBrains Mono" text-anchor="end">${chartPLN(val)}</text>`;
  }

  // Year boundary lines
  const years = [...new Set(events.map(e => e._year))];
  years.forEach(yr => {
    const yearStart = new Date(`${yr}-01-01`);
    if (yearStart > minDate && yearStart < maxDate) {
      const bx = x(yearStart.toISOString().slice(0, 10));
      svg += `<line x1="${bx}" y1="${pad.top}" x2="${bx}" y2="${pad.top + plotH}" stroke="rgba(129,140,248,0.15)" stroke-width="1" stroke-dasharray="4,4"/>`;
      svg += `<text x="${bx}" y="${pad.top + plotH + 18}" fill="rgba(129,140,248,0.5)" font-size="11" font-family="Inter" font-weight="600" text-anchor="middle">${yr}</text>`;
    }
  });
  // Label first and last year
  svg += `<text x="${pad.left + 5}" y="${pad.top + plotH + 18}" fill="rgba(129,140,248,0.5)" font-size="11" font-family="Inter" font-weight="600" text-anchor="start">${years[0]}</text>`;
  svg += `<text x="${W - pad.right - 5}" y="${pad.top + plotH + 18}" fill="rgba(129,140,248,0.5)" font-size="11" font-family="Inter" font-weight="600" text-anchor="end">${years[years.length - 1]}</text>`;

  // Area fill path
  let areaPath = `M ${x(events[0].date)} ${pad.top + plotH}`;
  events.forEach(e => { areaPath += ` L ${x(e.date)} ${y(e._pool)}`; });
  areaPath += ` L ${x(events[events.length - 1].date)} ${pad.top + plotH} Z`;
  svg += `<path d="${areaPath}" fill="url(#pool-area-grad)"/>`;

  // Pool line
  let linePath = '';
  events.forEach((e, i) => {
    const px = x(e.date);
    const py = y(e._pool);
    linePath += i === 0 ? `M ${px} ${py}` : ` L ${px} ${py}`;
  });
  svg += `<path d="${linePath}" fill="none" stroke="url(#pool-line-grad)" stroke-width="2" stroke-linejoin="round"/>`;

  // Event dots — group for interactivity
  events.forEach((e, i) => {
    const px = x(e.date);
    const py = y(e._pool);
    const cat = eventCategory(e);
    let color;
    switch (cat) {
      case 'revenue': color = '#f59e0b'; break;
      case 'salary': color = '#818cf8'; break;
      case 'fee': color = '#64748b'; break;
      default: color = '#14b8a6'; break;
    }
    // Larger invisible hit area
    svg += `<circle class="pool-event-dot" cx="${px}" cy="${py}" r="12" fill="transparent" data-idx="${i}" style="cursor:pointer"/>`;
    // Visible dot
    svg += `<circle cx="${px}" cy="${py}" r="${events.length > 200 ? 2.5 : 3.5}" fill="${color}" opacity="0.85" pointer-events="none"/>`;
  });

  // Title
  svg += `<text x="${pad.left}" y="18" fill="rgba(255,255,255,0.7)" font-size="12" font-family="Inter" font-weight="700">Cost Pool Balance Over Time</text>`;

  // Axis labels
  svg += `<text x="${W / 2}" y="${H - 5}" fill="rgba(255,255,255,0.3)" font-size="10" font-family="Inter" text-anchor="middle">Timeline (${events[0].date} → ${events[events.length - 1].date})</text>`;

  svg += '</svg>';

  // Tooltip element
  svg += '<div class="pool-tooltip" id="pool-tooltip"></div>';

  container.innerHTML = svg;

  // Bind interactions
  bindChartInteractions(container, events, x, y);
}

function chartPLN(v) {
  if (Math.abs(v) >= 1000000) return (v / 1000000).toFixed(1) + 'M';
  if (Math.abs(v) >= 1000) return (v / 1000).toFixed(0) + 'K';
  return v.toFixed(0);
}

function bindChartInteractions(container, events, xFn, yFn) {
  const tooltip = container.querySelector('#pool-tooltip');
  const dots = container.querySelectorAll('.pool-event-dot');

  dots.forEach(dot => {
    dot.addEventListener('mouseenter', (ev) => {
      const idx = parseInt(dot.dataset.idx);
      const e = events[idx];
      if (!e) return;

      const isRev = e._type === 'revenue';
      const deltaSign = isRev ? '−' : '+';
      const deltaColor = isRev ? 'var(--amber)' : 'var(--green)';

      tooltip.innerHTML = `
        <div style="font-weight:700;margin-bottom:4px">${e.date}</div>
        <div>${e._type === 'revenue' ? 'SELL' : (e.source === 'polygon_salary' ? 'SALARY' : 'BUY')} ${e.asset} — ${fmtNum(parseFloat(e.amount), 4)}</div>
        <div style="color:${deltaColor}">${deltaSign}${fmtPLN(Math.abs(parseFloat(e.pln_value)))}</div>
        <div style="margin-top:4px;color:var(--green);font-weight:600">Pool: ${fmtPLN(e._pool)}</div>
      `;
      tooltip.classList.add('visible');

      const cr = container.getBoundingClientRect();
      const cx = parseFloat(dot.getAttribute('cx'));
      const cy = parseFloat(dot.getAttribute('cy'));
      // Position tooltip near the dot
      const svgEl = container.querySelector('svg');
      const svgRect = svgEl.getBoundingClientRect();
      const scale = svgRect.width / svgEl.viewBox.baseVal.width;

      let ttLeft = cx * scale + 16;
      let ttTop = cy * scale - 20;
      // Flip if near edge
      if (ttLeft + 200 > svgRect.width) ttLeft = cx * scale - 220;
      if (ttTop < 10) ttTop = cy * scale + 16;
      tooltip.style.left = ttLeft + 'px';
      tooltip.style.top = ttTop + 'px';
    });

    dot.addEventListener('mouseleave', () => {
      tooltip.classList.remove('visible');
    });

    dot.addEventListener('click', () => {
      const idx = parseInt(dot.dataset.idx);
      scrollToEvent(idx);
    });
  });
}

function scrollToEvent(idx) {
  const row = document.querySelector(`tr[data-event-idx="${idx}"]`);
  if (!row) return;
  // Remove previous highlight
  document.querySelectorAll('.pool-row-highlight').forEach(r => r.classList.remove('pool-row-highlight'));
  row.classList.add('pool-row-highlight');
  row.scrollIntoView({ behavior: 'smooth', block: 'center' });
}

/* ------------------------------------------------------------------ */
/*  Main render                                                        */
/* ------------------------------------------------------------------ */

let _filter = { search: '', asset: '', type: '' };

export function renderPoolExplorer(app, data) {
  const { events, totalCosts, totalRevenue, finalPool } = buildPoolTimeline(data);
  const assets = getUniqueAssets(events);

  // Apply filters
  const filtered = events.filter(e => {
    if (_filter.type && e._type !== _filter.type) return false;
    if (_filter.asset && e.asset !== _filter.asset) return false;
    if (_filter.search) {
      const s = _filter.search.toLowerCase();
      const h = `${e.date} ${e.asset} ${e.source} ${e.notes || ''} ${e.counterparty_asset || ''} ${e.price_method || ''}`.toLowerCase();
      if (!h.includes(s)) return false;
    }
    return true;
  });

  const revenueCount = events.filter(e => e._type === 'revenue').length;
  const costCount = events.filter(e => e._type === 'cost').length;
  const peakPool = Math.max(...events.map(e => e._pool));

  let html = `<div class="animate-in">
    <a href="#/" class="back-btn">← Back to Dashboard</a>

    <div class="section-header">
      <h2 class="section-title">Pool Explorer</h2>
      <span class="section-subtitle">Every event from ${events[0]?.date || '—'} to ${events[events.length - 1]?.date || '—'} — ${events.length} events total</span>
    </div>

    <!-- Summary cards -->
    <div class="pool-summary-grid">
      <div class="card pool-stat-card">
        <div class="pool-stat-label">Total Events</div>
        <div class="pool-stat-value">${events.length}</div>
        <div class="pool-stat-detail">${costCount} costs · ${revenueCount} disposals</div>
      </div>
      <div class="card pool-stat-card">
        <div class="pool-stat-label">Total Costs Added</div>
        <div class="pool-stat-value metric-cost">${fmtPLN(totalCosts)}</div>
        <div class="pool-stat-detail">Acquisitions + salary + fees</div>
      </div>
      <div class="card pool-stat-card">
        <div class="pool-stat-label">Total Revenue Consumed</div>
        <div class="pool-stat-value metric-revenue">${fmtPLN(totalRevenue)}</div>
        <div class="pool-stat-detail">All crypto→fiat disposals</div>
      </div>
      <div class="card pool-stat-card">
        <div class="pool-stat-label">Peak Pool Balance</div>
        <div class="pool-stat-value" style="color:var(--indigo)">${fmtPLN(peakPool)}</div>
        <div class="pool-stat-detail">Highest cost pool balance</div>
      </div>
      <div class="card pool-stat-card">
        <div class="pool-stat-label">Current Pool Balance</div>
        <div class="pool-stat-value metric-carry">${fmtPLN(finalPool)}</div>
        <div class="pool-stat-detail">Carry-forward → 2026</div>
      </div>
    </div>

    <!-- Chart -->
    <div class="pool-chart-wrap" id="pool-chart-container"></div>

    <!-- Legend -->
    <div class="pool-legend">
      <div class="legend-item"><div class="legend-swatch" style="background:#14b8a6"></div>Purchases</div>
      <div class="legend-item"><div class="legend-swatch" style="background:#818cf8"></div>Salary USDC</div>
      <div class="legend-item"><div class="legend-swatch" style="background:#f59e0b"></div>Sales (Revenue)</div>
      <div class="legend-item"><div class="legend-swatch" style="background:#64748b"></div>Fees</div>
      <div class="legend-item"><div class="legend-swatch" style="background:linear-gradient(90deg,#818cf8,#10b981);border-radius:2px"></div>Pool Balance Line</div>
    </div>

    <!-- Filters -->
    <div class="section-header" style="margin-top:24px">
      <h2 class="section-title">Event Log</h2>
      <span class="section-subtitle">${filtered.length} of ${events.length} events</span>
    </div>

    <div class="tab-bar">
      <button class="tab-btn ${_filter.type === '' ? 'active' : ''}" data-type="">All</button>
      <button class="tab-btn ${_filter.type === 'cost' ? 'active' : ''}" data-type="cost">Costs (${costCount})</button>
      <button class="tab-btn ${_filter.type === 'revenue' ? 'active' : ''}" data-type="revenue">Revenue (${revenueCount})</button>
    </div>

    <div class="filter-bar">
      <input class="search-input" type="text" placeholder="Search events..." value="${_filter.search}" id="pool-search" />
      <select class="filter-select" id="pool-filter-asset">
        <option value="">All Assets</option>
        ${assets.map(a => `<option value="${a}" ${_filter.asset === a ? 'selected' : ''}>${a}</option>`).join('')}
      </select>
    </div>

    <!-- Table -->
    <div class="card" style="padding:0;overflow-x:auto">
      <table class="data-table pool-table" id="pool-event-table">
        <thead>
          <tr>
            <th>#</th>
            <th>Date</th>
            <th>Type</th>
            <th>Asset</th>
            <th>Amount</th>
            <th>PLN Value</th>
            <th>Pool Δ</th>
            <th>Pool Balance</th>
            <th>Source</th>
          </tr>
        </thead>
        <tbody>`;

  let prevYear = null;
  filtered.forEach((e, fi) => {
    // Year separator
    if (e._year !== prevYear) {
      prevYear = e._year;
      html += `<tr class="pool-year-separator">
        <td colspan="9">${e._year}</td>
      </tr>`;
    }

    const isRev = e._type === 'revenue';
    const deltaVal = parseFloat(e.pln_value) || 0;
    const deltaSign = isRev ? '−' : '+';
    const deltaClass = isRev ? 'pool-delta-negative' : 'pool-delta-positive';

    html += `<tr data-event-idx="${e._index}" class="pool-event-row" title="${e.notes || ''}">
      <td class="cell-mono" style="color:var(--text-muted)">${e._index + 1}</td>
      <td class="cell-mono">${e.date}</td>
      <td>${eventBadge(e)}</td>
      <td><strong>${e.asset}</strong></td>
      <td class="cell-mono cell-right">${fmtNum(parseFloat(e.amount), 6)}</td>
      <td class="cell-pln">${fmtPLN(deltaVal)}</td>
      <td class="cell-pln ${deltaClass}">${deltaSign}${fmtPLN(deltaVal)}</td>
      <td class="cell-pln pool-running-value">${fmtPLN(e._pool)}</td>
      <td>${e.source || '—'}</td>
    </tr>`;
  });

  html += `</tbody>
        <tfoot>
          <tr>
            <td colspan="5" class="cell-right">Totals:</td>
            <td class="cell-pln">${fmtPLN(totalCosts + totalRevenue)}</td>
            <td class="cell-pln metric-carry">Net: ${fmtPLN(totalCosts - totalRevenue)}</td>
            <td class="cell-pln metric-carry">${fmtPLN(finalPool)}</td>
            <td></td>
          </tr>
        </tfoot>
      </table>
    </div>
  </div>`;

  app.innerHTML = html;

  // Render chart (needs DOM present)
  requestAnimationFrame(() => {
    renderSvgChart(events, 'pool-chart-container');
  });

  // Bind filter events
  const rerender = () => renderPoolExplorer(app, data);

  app.querySelectorAll('.tab-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      _filter.type = btn.dataset.type;
      rerender();
    });
  });

  const searchInput = app.querySelector('#pool-search');
  if (searchInput) {
    searchInput.addEventListener('input', (ev) => {
      _filter.search = ev.target.value;
      rerender();
    });
    // Restore cursor position
    requestAnimationFrame(() => {
      searchInput.focus();
      searchInput.selectionStart = searchInput.selectionEnd = searchInput.value.length;
    });
  }

  app.querySelector('#pool-filter-asset')?.addEventListener('change', (ev) => {
    _filter.asset = ev.target.value;
    rerender();
  });

  // Table row click → highlight on chart
  app.querySelectorAll('.pool-event-row').forEach(row => {
    row.addEventListener('click', () => {
      const idx = parseInt(row.dataset.eventIdx);
      // Highlight this row
      document.querySelectorAll('.pool-row-highlight').forEach(r => r.classList.remove('pool-row-highlight'));
      row.classList.add('pool-row-highlight');

      // Pulse the chart dot
      const dot = document.querySelector(`.pool-event-dot[data-idx="${idx}"]`);
      if (dot) {
        dot.classList.add('pool-dot-pulse');
        setTimeout(() => dot.classList.remove('pool-dot-pulse'), 1200);
        // Scroll chart into view
        const chart = document.getElementById('pool-chart-container');
        if (chart) chart.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }
    });
  });
}

export function resetPoolFilters() {
  _filter = { search: '', asset: '', type: '' };
}

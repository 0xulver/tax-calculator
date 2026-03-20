/**
 * Events table view — sortable, filterable table of revenue/cost events.
 */
import { fmtPLN, fmtNum, getAllEvents, getUniqueAssets, getUniqueSources } from './data.js';

let _sortCol = 'date';
let _sortAsc = true;
let _filter = { search: '', asset: '', source: '', type: '' };

function sortEvents(events) {
  return [...events].sort((a, b) => {
    let va = a[_sortCol] || '';
    let vb = b[_sortCol] || '';
    if (_sortCol === 'pln_value' || _sortCol === 'amount' || _sortCol === 'counterparty_amount') {
      va = parseFloat(va) || 0;
      vb = parseFloat(vb) || 0;
    }
    if (va < vb) return _sortAsc ? -1 : 1;
    if (va > vb) return _sortAsc ? 1 : -1;
    return 0;
  });
}

function filterEvents(events) {
  return events.filter(e => {
    if (_filter.type && e._type !== _filter.type) return false;
    if (_filter.asset && e.asset !== _filter.asset) return false;
    if (_filter.source && e.source !== _filter.source) return false;
    if (_filter.search) {
      const s = _filter.search.toLowerCase();
      const haystack = `${e.date} ${e.asset} ${e.source} ${e.notes} ${e.counterparty_asset} ${e.price_method}`.toLowerCase();
      if (!haystack.includes(s)) return false;
    }
    return true;
  });
}

export function renderEvents(app, yearData, year, rerender) {
  const allEvents = getAllEvents(yearData);
  const assets = getUniqueAssets(allEvents);
  const sources = getUniqueSources(allEvents);
  const filtered = filterEvents(allEvents);
  const sorted = sortEvents(filtered);

  const revenueTotal = sorted.filter(e => e._type === 'revenue').reduce((s, e) => s + (parseFloat(e.pln_value) || 0), 0);
  const costTotal = sorted.filter(e => e._type === 'cost').reduce((s, e) => s + (parseFloat(e.pln_value) || 0), 0);

  const sortIcon = (col) => {
    if (_sortCol !== col) return '';
    return _sortAsc ? ' sorted-asc' : ' sorted-desc';
  };

  let html = `
    <a href="#/" class="back-btn">← Back to Dashboard</a>
    <div class="section-header">
      <h2 class="section-title">${year} — All Events</h2>
      <span class="section-subtitle">${sorted.length} of ${allEvents.length} events shown</span>
    </div>

    <div class="tab-bar">
      <button class="tab-btn ${_filter.type === '' ? 'active' : ''}" data-type="">All</button>
      <button class="tab-btn ${_filter.type === 'revenue' ? 'active' : ''}" data-type="revenue">Revenue</button>
      <button class="tab-btn ${_filter.type === 'cost' ? 'active' : ''}" data-type="cost">Costs</button>
    </div>

    <div class="filter-bar">
      <input class="search-input" type="text" placeholder="Search events..." value="${_filter.search}" id="event-search" />
      <select class="filter-select" id="filter-asset">
        <option value="">All Assets</option>
        ${assets.map(a => `<option value="${a}" ${_filter.asset === a ? 'selected' : ''}>${a}</option>`).join('')}
      </select>
      <select class="filter-select" id="filter-source">
        <option value="">All Sources</option>
        ${sources.map(s => `<option value="${s}" ${_filter.source === s ? 'selected' : ''}>${s}</option>`).join('')}
      </select>
    </div>

    <div class="card" style="padding:0;overflow-x:auto">
      <table class="data-table">
        <thead>
          <tr>
            <th class="${sortIcon('_type')}" data-col="_type">Type</th>
            <th class="${sortIcon('date')}" data-col="date">Date</th>
            <th class="${sortIcon('asset')}" data-col="asset">Asset</th>
            <th class="${sortIcon('amount')}" data-col="amount">Amount</th>
            <th class="${sortIcon('counterparty_asset')}" data-col="counterparty_asset">Counter</th>
            <th class="${sortIcon('counterparty_amount')}" data-col="counterparty_amount">CP Amt</th>
            <th class="${sortIcon('pln_value')}" data-col="pln_value">PLN Value</th>
            <th class="${sortIcon('price_method')}" data-col="price_method">Method</th>
            <th class="${sortIcon('source')}" data-col="source">Source</th>
          </tr>
        </thead>
        <tbody>`;

  sorted.forEach((e, idx) => {
    const badge = e._type === 'revenue' ? 'badge-revenue' : (e.source === 'polygon_salary' ? 'badge-salary' : 'badge-cost');
    const label = e._type === 'revenue' ? 'SELL' : (e.source === 'polygon_salary' ? 'SALARY' : 'BUY');
    html += `<tr onclick="location.hash='#/event/${year}/${idx}'" title="${e.notes}">
      <td><span class="badge ${badge}">${label}</span></td>
      <td class="cell-mono">${e.date}</td>
      <td><strong>${e.asset}</strong></td>
      <td class="cell-mono cell-right">${fmtNum(parseFloat(e.amount), 6)}</td>
      <td>${e.counterparty_asset || '—'}</td>
      <td class="cell-mono cell-right">${e.counterparty_amount && e.counterparty_amount !== '0' ? fmtNum(parseFloat(e.counterparty_amount), 2) : '—'}</td>
      <td class="cell-pln">${fmtPLN(parseFloat(e.pln_value))}</td>
      <td><span class="badge badge-fee">${e.price_method}</span></td>
      <td>${e.source}</td>
    </tr>`;
  });

  html += `</tbody>
        <tfoot>
          <tr>
            <td colspan="6" class="cell-right">Revenue Total:</td>
            <td class="cell-pln metric-revenue">${fmtPLN(revenueTotal)}</td>
            <td colspan="2"></td>
          </tr>
          <tr>
            <td colspan="6" class="cell-right">Cost Total:</td>
            <td class="cell-pln metric-cost">${fmtPLN(costTotal)}</td>
            <td colspan="2"></td>
          </tr>
        </tfoot>
      </table>
    </div>`;

  app.innerHTML = html;

  // Bind events
  app.querySelectorAll('.tab-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      _filter.type = btn.dataset.type;
      rerender();
    });
  });

  const searchInput = app.querySelector('#event-search');
  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      _filter.search = e.target.value;
      rerender();
    });
  }

  app.querySelector('#filter-asset')?.addEventListener('change', (e) => {
    _filter.asset = e.target.value;
    rerender();
  });

  app.querySelector('#filter-source')?.addEventListener('change', (e) => {
    _filter.source = e.target.value;
    rerender();
  });

  app.querySelectorAll('.data-table thead th[data-col]').forEach(th => {
    th.addEventListener('click', () => {
      const col = th.dataset.col;
      if (_sortCol === col) {
        _sortAsc = !_sortAsc;
      } else {
        _sortCol = col;
        _sortAsc = true;
      }
      rerender();
    });
  });
}

export function resetFilters() {
  _filter = { search: '', asset: '', source: '', type: '' };
  _sortCol = 'date';
  _sortAsc = true;
}

/**
 * Drilldown view — single event detail with price trace and pool impact.
 */
import { fmtPLN, fmtNum, getAllEvents } from './data.js';

export function renderDrilldown(app, yearData, year, eventIndex) {
  const events = getAllEvents(yearData);
  const event = events[eventIndex];

  if (!event) {
    app.innerHTML = `<a href="#/year/${year}" class="back-btn">← Back to ${year}</a>
      <div class="card"><p>Event not found.</p></div>`;
    return;
  }

  // Compute pool impact: running total before and after this event
  const costsPrior = parseFloat(yearData.costs_prior_years_pln) || 0;
  let runningPool = costsPrior;
  let poolBefore = 0;
  let poolAfter = 0;
  let revenueAccum = 0;
  let costAccum = 0;

  events.forEach((e, i) => {
    if (i === eventIndex) poolBefore = costAccum + costsPrior - revenueAccum;
    const val = parseFloat(e.pln_value) || 0;
    if (e._type === 'cost') costAccum += val;
    else revenueAccum += val;
    if (i === eventIndex) poolAfter = costAccum + costsPrior - revenueAccum;
  });

  const delta = parseFloat(event.pln_value) || 0;
  const isRevenue = event._type === 'revenue';
  const badge = isRevenue ? 'badge-revenue' : (event.source === 'polygon_salary' ? 'badge-salary' : 'badge-cost');
  const label = isRevenue ? 'REVENUE (Disposal)' : (event.source === 'polygon_salary' ? 'COST (Salary USDC)' : 'COST (Acquisition)');

  let html = `
    <a href="#/year/${year}" class="back-btn">← Back to ${year} Events</a>

    <div class="section-header">
      <h2 class="section-title">Event Drilldown</h2>
      <span class="badge ${badge}" style="font-size:0.85rem;padding:6px 14px">${label}</span>
    </div>

    <div class="drilldown-grid">
      <div class="card detail-section">
        <h3>Transaction Details</h3>
        <div class="detail-row"><span class="detail-label">Date</span><span class="detail-value">${event.date}</span></div>
        <div class="detail-row"><span class="detail-label">Asset</span><span class="detail-value">${event.asset}</span></div>
        <div class="detail-row"><span class="detail-label">Amount</span><span class="detail-value">${fmtNum(parseFloat(event.amount), 8)}</span></div>
        <div class="detail-row"><span class="detail-label">Counterparty Asset</span><span class="detail-value">${event.counterparty_asset || '—'}</span></div>
        <div class="detail-row"><span class="detail-label">Counterparty Amount</span><span class="detail-value">${event.counterparty_amount && event.counterparty_amount !== '0' ? fmtNum(parseFloat(event.counterparty_amount), 2) : '—'}</span></div>
        <div class="detail-row"><span class="detail-label">Source</span><span class="detail-value">${event.source}</span></div>
        <div class="detail-row"><span class="detail-label">Notes</span><span class="detail-value" style="max-width:250px;white-space:normal;text-align:right">${event.notes || '—'}</span></div>
      </div>

      <div class="card detail-section">
        <h3>Price Resolution Trace</h3>
        <div class="detail-row"><span class="detail-label">PLN Value</span><span class="detail-value" style="color:var(--green);font-size:1.1rem"><strong>${fmtPLN(delta)}</strong></span></div>
        <div class="detail-row"><span class="detail-label">Method</span><span class="detail-value"><span class="badge badge-fee">${event.price_method}</span></span></div>
        ${renderPriceTrace(event)}
      </div>
    </div>

    <div class="card pool-impact">
      <h3 style="color:var(--text-muted);font-size:0.85rem;text-transform:uppercase;letter-spacing:0.5px;margin-bottom:16px">
        Impact on Cost Pool
      </h3>
      <div class="pool-bar-container">
        <div class="pool-segment">
          <span class="pool-segment-label">Pool Before</span>
          <span class="pool-segment-value pool-before">${fmtPLN(Math.max(poolBefore, 0))}</span>
        </div>
        <span class="pool-operator">${isRevenue ? '−' : '+'}</span>
        <div class="pool-segment">
          <span class="pool-segment-label">This Event</span>
          <span class="pool-segment-value ${isRevenue ? 'pool-delta-revenue' : 'pool-delta-cost'}">${fmtPLN(delta)}</span>
        </div>
        <span class="pool-operator">=</span>
        <div class="pool-segment">
          <span class="pool-segment-label">Pool After</span>
          <span class="pool-segment-value pool-after">${fmtPLN(Math.max(poolAfter, 0))}</span>
        </div>
      </div>
      <p style="margin-top:16px;color:var(--text-muted);font-size:0.8rem">
        ${isRevenue
          ? 'Revenue events reduce the cost pool. If total costs still exceed total revenue, no tax is due.'
          : 'Cost events increase the cost pool, shielding future revenue from taxation.'}
      </p>
    </div>

    ${eventIndex > 0 || eventIndex < events.length - 1 ? `
    <div style="display:flex;gap:12px;margin-top:12px">
      ${eventIndex > 0 ? `<a href="#/event/${year}/${eventIndex - 1}" class="back-btn">← Previous Event</a>` : ''}
      ${eventIndex < events.length - 1 ? `<a href="#/event/${year}/${eventIndex + 1}" class="back-btn">Next Event →</a>` : ''}
    </div>` : ''}
  `;

  app.innerHTML = html;
}

function renderPriceTrace(event) {
  const method = event.price_method || '';
  let trace = '';

  if (method.startsWith('nbp_') && event.counterparty_asset && event.counterparty_amount !== '0') {
    const cpAmt = parseFloat(event.counterparty_amount) || 0;
    const plnVal = parseFloat(event.pln_value) || 0;
    const impliedRate = cpAmt > 0 ? (plnVal / cpAmt) : 0;
    const currency = method.replace('nbp_', '').replace('_fee', '').replace('_via_usdc', '').replace('_via_usdt', '').toUpperCase();

    trace += `<div class="detail-row"><span class="detail-label">Step 1</span><span class="detail-value">Counterparty: ${fmtNum(cpAmt, 2)} ${event.counterparty_asset}</span></div>`;
    trace += `<div class="detail-row"><span class="detail-label">Step 2</span><span class="detail-value">NBP ${currency}/PLN rate: ~${fmtNum(impliedRate, 4)}</span></div>`;
    trace += `<div class="detail-row"><span class="detail-label">Result</span><span class="detail-value">${fmtNum(cpAmt, 2)} × ${fmtNum(impliedRate, 4)} = ${fmtPLN(plnVal)}</span></div>`;
  } else if (method === 'coingecko_pln') {
    const amt = parseFloat(event.amount) || 0;
    const plnVal = parseFloat(event.pln_value) || 0;
    const impliedPrice = amt > 0 ? (plnVal / amt) : 0;

    trace += `<div class="detail-row"><span class="detail-label">Step 1</span><span class="detail-value">CoinGecko historical PLN price</span></div>`;
    trace += `<div class="detail-row"><span class="detail-label">Step 2</span><span class="detail-value">1 ${event.asset} = ~${fmtPLN(impliedPrice)}</span></div>`;
    trace += `<div class="detail-row"><span class="detail-label">Result</span><span class="detail-value">${fmtNum(amt, 6)} × ${fmtNum(impliedPrice, 2)} = ${fmtPLN(plnVal)}</span></div>`;
  } else if (method === 'direct_pln') {
    trace += `<div class="detail-row"><span class="detail-label">Step 1</span><span class="detail-value">Direct PLN amount</span></div>`;
    trace += `<div class="detail-row"><span class="detail-label">Result</span><span class="detail-value">${fmtPLN(parseFloat(event.pln_value))}</span></div>`;
  } else if (method.includes('stablecoin') || method.includes('salary')) {
    const amt = parseFloat(event.amount) || 0;
    const plnVal = parseFloat(event.pln_value) || 0;
    const impliedRate = amt > 0 ? (plnVal / amt) : 0;

    trace += `<div class="detail-row"><span class="detail-label">Step 1</span><span class="detail-value">Stablecoin treated as 1:1 USD</span></div>`;
    trace += `<div class="detail-row"><span class="detail-label">Step 2</span><span class="detail-value">NBP USD/PLN rate: ~${fmtNum(impliedRate, 4)}</span></div>`;
    trace += `<div class="detail-row"><span class="detail-label">Result</span><span class="detail-value">${fmtNum(amt, 2)} × ${fmtNum(impliedRate, 4)} = ${fmtPLN(plnVal)}</span></div>`;
  } else {
    trace += `<div class="detail-row"><span class="detail-label">Method</span><span class="detail-value">${method}</span></div>`;
  }

  trace += `<div class="detail-row" style="margin-top:12px;border-top:1px solid var(--border);padding-top:12px">
    <span class="detail-label" style="font-size:0.75rem;color:var(--text-muted)">NBP rate is from last business day <em>before</em> transaction date (Art. 11a ust. 1-2)</span>
  </div>`;

  return trace;
}

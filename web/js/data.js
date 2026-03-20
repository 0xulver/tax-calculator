/**
 * Data loading and indexing for the tax dashboard.
 */

let _detailData = null;
let _transactions = null;

/** Format a number as PLN currency string */
export function fmtPLN(v) {
  const n = typeof v === 'string' ? parseFloat(v) : v;
  if (isNaN(n)) return '0.00 PLN';
  return n.toLocaleString('pl-PL', { minimumFractionDigits: 2, maximumFractionDigits: 2 }) + ' PLN';
}

/** Format a number with commas */
export function fmtNum(v, decimals = 2) {
  const n = typeof v === 'string' ? parseFloat(v) : v;
  if (isNaN(n)) return '0';
  return n.toLocaleString('en-US', { minimumFractionDigits: decimals, maximumFractionDigits: decimals });
}

/** Load and cache the enriched PIT-38 detail data */
export async function loadDetail() {
  if (_detailData) return _detailData;
  const resp = await fetch('/data/pit38_detail.json');
  _detailData = await resp.json();
  return _detailData;
}

/** Load and cache the normalized transaction ledger */
export async function loadTransactions() {
  if (_transactions) return _transactions;
  const resp = await fetch('/data/transactions.json');
  _transactions = await resp.json();
  return _transactions;
}

/** Get sorted year keys from the detail data */
export function getYears(data) {
  return Object.keys(data.yearly_results).sort();
}

/** Get all events for a year (revenue + cost), sorted by date */
export function getAllEvents(yearData) {
  const revenue = (yearData.revenue_events || []).map(e => ({ ...e, _type: 'revenue' }));
  const cost = (yearData.cost_events || []).map(e => ({ ...e, _type: 'cost' }));
  return [...revenue, ...cost].sort((a, b) => a.date.localeCompare(b.date));
}

/** Get unique assets from events */
export function getUniqueAssets(events) {
  const assets = new Set(events.map(e => e.asset));
  return [...assets].sort();
}

/** Get unique sources from events */
export function getUniqueSources(events) {
  const sources = new Set(events.map(e => e.source).filter(Boolean));
  return [...sources].sort();
}

/** Compute the carry-forward chain across all years */
export function getCarryChain(data) {
  const years = getYears(data);
  return years.map(y => ({
    year: y,
    carryForward: parseFloat(data.yearly_results[y].carry_forward_pln) || 0,
    revenue: parseFloat(data.yearly_results[y].revenue_pln) || 0,
    costsCurrent: parseFloat(data.yearly_results[y].costs_current_year_pln) || 0,
    costsPrior: parseFloat(data.yearly_results[y].costs_prior_years_pln) || 0,
    income: parseFloat(data.yearly_results[y].income_pln) || 0,
    tax: parseFloat(data.yearly_results[y].tax_due_pln) || 0,
    disposals: data.yearly_results[y].disposal_count || 0,
  }));
}

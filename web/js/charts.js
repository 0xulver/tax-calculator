/**
 * Chart rendering utilities using Canvas 2D API.
 */

const COLORS = {
  salary: '#818cf8',     // indigo
  buy: '#14b8a6',        // teal
  deposit: '#3b82f6',    // blue
  fee: '#64748b',        // slate
  sell: '#f59e0b',       // amber
  carry: '#10b981',      // green
  revenue: '#f59e0b',
  cost: '#3b82f6',
  grid: 'rgba(255,255,255,0.05)',
  axis: 'rgba(255,255,255,0.2)',
  text: 'rgba(255,255,255,0.5)',
  textBright: 'rgba(255,255,255,0.8)',
};

/** Create a canvas with proper DPI scaling */
export function createCanvas(container, width, height) {
  const canvas = document.createElement('canvas');
  const dpr = window.devicePixelRatio || 1;
  canvas.width = width * dpr;
  canvas.height = height * dpr;
  canvas.style.width = width + 'px';
  canvas.style.height = height + 'px';
  const ctx = canvas.getContext('2d');
  ctx.scale(dpr, dpr);
  container.appendChild(canvas);
  return { canvas, ctx, width, height, dpr };
}

/** Format PLN value for chart labels */
function chartPLN(v) {
  if (Math.abs(v) >= 1000000) return (v / 1000000).toFixed(1) + 'M';
  if (Math.abs(v) >= 1000) return (v / 1000).toFixed(0) + 'K';
  return v.toFixed(0);
}

/** Draw a horizontal bar chart (waterfall-style) */
export function drawWaterfallChart(ctx, w, h, events, costsPrior) {
  const pad = { top: 30, right: 20, bottom: 40, left: 80 };
  const plotW = w - pad.left - pad.right;
  const plotH = h - pad.top - pad.bottom;

  // Build bars: start with carry-forward, then each event changes the running total
  const bars = [];
  let running = costsPrior;

  bars.push({ label: 'Prior CF', value: running, delta: running, type: 'carry', start: 0 });

  events.forEach(e => {
    const val = parseFloat(e.pln_value) || 0;
    const prev = running;
    if (e._type === 'cost') {
      running += val;
      bars.push({ label: `${e.asset}`, value: running, delta: val, type: e.source === 'polygon_salary' ? 'salary' : 'buy', start: prev, date: e.date });
    } else {
      running -= val;
      bars.push({ label: `${e.asset}`, value: running, delta: -val, type: 'sell', start: prev, date: e.date });
    }
  });

  bars.push({ label: 'End CF', value: Math.max(running, 0), delta: Math.max(running, 0), type: 'carry', start: 0 });

  // Find scale
  const maxVal = Math.max(...bars.map(b => Math.max(b.value, b.start, b.start + Math.abs(b.delta))), 1);
  const yScale = plotH / maxVal;

  // Skip drawing if too many bars — aggregate by type instead
  const drawBars = bars.length > 60 ?
    aggregateBars(bars) : bars;

  const barWidth = Math.max(2, Math.min(20, (plotW - 10) / drawBars.length - 2));
  const barGap = Math.max(1, (plotW - drawBars.length * barWidth) / (drawBars.length + 1));

  // Grid lines
  ctx.strokeStyle = COLORS.grid;
  ctx.lineWidth = 1;
  const gridSteps = 5;
  for (let i = 0; i <= gridSteps; i++) {
    const y = pad.top + (plotH / gridSteps) * i;
    ctx.beginPath();
    ctx.moveTo(pad.left, y);
    ctx.lineTo(w - pad.right, y);
    ctx.stroke();

    ctx.fillStyle = COLORS.text;
    ctx.font = '11px Inter';
    ctx.textAlign = 'right';
    const val = maxVal - (maxVal / gridSteps) * i;
    ctx.fillText(chartPLN(val), pad.left - 8, y + 4);
  }

  // Draw bars
  drawBars.forEach((bar, i) => {
    const x = pad.left + barGap + i * (barWidth + barGap);
    const color = COLORS[bar.type] || COLORS.cost;

    if (bar.type === 'carry') {
      // Full height from 0
      const barH = bar.value * yScale;
      const y = pad.top + plotH - barH;
      ctx.fillStyle = color;
      ctx.globalAlpha = 0.8;
      ctx.fillRect(x, y, barWidth, barH);
      ctx.globalAlpha = 1;
    } else {
      // Delta bar
      const startY = pad.top + plotH - bar.start * yScale;
      const deltaH = Math.abs(bar.delta) * yScale;
      const y = bar.delta > 0 ? startY - deltaH : startY;
      ctx.fillStyle = color;
      ctx.globalAlpha = 0.7;
      ctx.fillRect(x, y, barWidth, deltaH);
      ctx.globalAlpha = 1;
    }

    // Label (only for aggregated or few bars)
    if (drawBars.length <= 30 || bar.type === 'carry') {
      ctx.fillStyle = COLORS.text;
      ctx.font = '9px Inter';
      ctx.textAlign = 'center';
      ctx.fillText(bar.label, x + barWidth / 2, h - pad.bottom + 14);
    }
  });

  // Running total line
  ctx.beginPath();
  ctx.strokeStyle = COLORS.carry;
  ctx.lineWidth = 2;
  ctx.globalAlpha = 0.6;
  drawBars.forEach((bar, i) => {
    const x = pad.left + barGap + i * (barWidth + barGap) + barWidth / 2;
    const y = pad.top + plotH - bar.value * yScale;
    if (i === 0) ctx.moveTo(x, y);
    else ctx.lineTo(x, y);
  });
  ctx.stroke();
  ctx.globalAlpha = 1;

  // Title
  ctx.fillStyle = COLORS.textBright;
  ctx.font = 'bold 12px Inter';
  ctx.textAlign = 'left';
  ctx.fillText('Cost Pool Waterfall', pad.left, 18);
}

function aggregateBars(bars) {
  // Keep first and last (carry bars), aggregate middle by type chunks
  const result = [bars[0]];
  const middle = bars.slice(1, -1);

  // Group by asset
  const groups = {};
  middle.forEach(b => {
    const key = `${b.type}_${b.label}`;
    if (!groups[key]) groups[key] = { ...b };
    else {
      groups[key].delta += b.delta;
      groups[key].value = groups[key].start + groups[key].delta;
    }
  });

  let running = bars[0].value;
  Object.values(groups).sort((a, b) => b.type === 'sell' ? -1 : 1).forEach(g => {
    g.start = running;
    g.value = running + g.delta;
    running = g.value;
    result.push(g);
  });

  const lastBar = bars[bars.length - 1];
  lastBar.value = Math.max(running, 0);
  result.push(lastBar);
  return result;
}

/** Draw multi-year area chart for carry-forward timeline */
export function drawTimelineChart(ctx, w, h, chainData) {
  const pad = { top: 30, right: 30, bottom: 50, left: 80 };
  const plotW = w - pad.left - pad.right;
  const plotH = h - pad.top - pad.bottom;

  const maxVal = Math.max(
    ...chainData.map(c => Math.max(c.carryForward, c.costsCurrent + c.costsPrior, c.revenue)),
    1
  );
  const yScale = plotH / maxVal;
  const xStep = plotW / (chainData.length - 1 || 1);

  // Grid
  ctx.strokeStyle = COLORS.grid;
  ctx.lineWidth = 1;
  for (let i = 0; i <= 5; i++) {
    const y = pad.top + (plotH / 5) * i;
    ctx.beginPath();
    ctx.moveTo(pad.left, y);
    ctx.lineTo(w - pad.right, y);
    ctx.stroke();
    ctx.fillStyle = COLORS.text;
    ctx.font = '11px Inter';
    ctx.textAlign = 'right';
    ctx.fillText(chartPLN(maxVal - (maxVal / 5) * i), pad.left - 8, y + 4);
  }

  // Revenue bars
  const barW = Math.min(40, xStep * 0.3);
  chainData.forEach((c, i) => {
    const x = pad.left + i * xStep;
    const revH = c.revenue * yScale;
    const costH = (c.costsCurrent + c.costsPrior) * yScale;

    // Cost bar
    ctx.fillStyle = COLORS.cost;
    ctx.globalAlpha = 0.4;
    ctx.fillRect(x - barW - 1, pad.top + plotH - costH, barW, costH);

    // Revenue bar
    ctx.fillStyle = COLORS.revenue;
    ctx.globalAlpha = 0.4;
    ctx.fillRect(x + 1, pad.top + plotH - revH, barW, revH);
    ctx.globalAlpha = 1;

    // Year label
    ctx.fillStyle = COLORS.textBright;
    ctx.font = 'bold 12px Inter';
    ctx.textAlign = 'center';
    ctx.fillText(c.year, x, h - pad.bottom + 20);
  });

  // Carry-forward area fill
  ctx.beginPath();
  ctx.moveTo(pad.left, pad.top + plotH);
  chainData.forEach((c, i) => {
    const x = pad.left + i * xStep;
    const y = pad.top + plotH - c.carryForward * yScale;
    ctx.lineTo(x, y);
  });
  ctx.lineTo(pad.left + (chainData.length - 1) * xStep, pad.top + plotH);
  ctx.closePath();
  const grad = ctx.createLinearGradient(0, pad.top, 0, pad.top + plotH);
  grad.addColorStop(0, 'rgba(16, 185, 129, 0.3)');
  grad.addColorStop(1, 'rgba(16, 185, 129, 0.02)');
  ctx.fillStyle = grad;
  ctx.fill();

  // Carry-forward line
  ctx.beginPath();
  ctx.strokeStyle = COLORS.carry;
  ctx.lineWidth = 3;
  chainData.forEach((c, i) => {
    const x = pad.left + i * xStep;
    const y = pad.top + plotH - c.carryForward * yScale;
    if (i === 0) ctx.moveTo(x, y);
    else ctx.lineTo(x, y);
  });
  ctx.stroke();

  // Dots + labels
  chainData.forEach((c, i) => {
    const x = pad.left + i * xStep;
    const y = pad.top + plotH - c.carryForward * yScale;
    ctx.beginPath();
    ctx.arc(x, y, 5, 0, Math.PI * 2);
    ctx.fillStyle = COLORS.carry;
    ctx.fill();

    ctx.fillStyle = COLORS.textBright;
    ctx.font = 'bold 11px JetBrains Mono';
    ctx.textAlign = 'center';
    ctx.fillText(chartPLN(c.carryForward), x, y - 12);
  });

  // Legend
  const legendY = 16;
  ctx.font = 'bold 12px Inter';
  ctx.textAlign = 'left';
  ctx.fillStyle = COLORS.textBright;
  ctx.fillText('Carry-Forward Timeline', pad.left, legendY);

  [
    { color: COLORS.carry, label: 'Carry-forward' },
    { color: COLORS.cost, label: 'Total costs' },
    { color: COLORS.revenue, label: 'Revenue' },
  ].forEach((item, i) => {
    const x = w - pad.right - 200 + i * 100;
    ctx.fillStyle = item.color;
    ctx.fillRect(x, legendY - 8, 10, 10);
    ctx.fillStyle = COLORS.text;
    ctx.font = '10px Inter';
    ctx.fillText(item.label, x + 14, legendY);
  });
}

# Agent Onboarding

This repo is a personal tax-calculation workspace for Polish filings involving
crypto, self-employment income, pre-JDG service income, and cross-border
Sweden-to-Poland residency issues. It combines code, generated reports, legal
research notes, and private evidence. Treat it as a high-sensitivity tax
evidence repo.

## Current Filing State

Start with the working summaries in `docs/todo/`:

- `docs/todo/readiness-assessment.md` - current status, blockers, and evidence gaps.
- `docs/todo/filing-summary.md` - current filing plan and values that are ready.
- `docs/todo/pit38-filing-guide.md` - PIT-38 caveats and historical values.

Important current posture:

- PIT-36 2025 and PIT-28 2025 are arithmetically ready but still have evidence
  caveats.
- PIT-38 is blocked until the `2023-04-12` move-date imported-basis ledger is
  rebuilt. Optimism and Arbitrum both have pre-residency activity and must be
  included. Mantle, Mode, and Scroll are post-residency in current evidence but
  still matter for 2024-2025 normalization.
- Topic 17 is the current PIT-38 legal policy. Topic 16 is superseded for
  PIT-38 mechanics.

## Repository Map

- `src/tax_calc/` - Python package.
  - `cli.py` - command entry point for normalization, PIT-38, reports, and full runs.
  - `cost_pool.py` - PIT-38 annual cost-pool engine and split-year policy modes.
  - `pit38.py` - PIT-38 markdown report generation.
  - `pit36.py` - pre-JDG USDC service-income calculator.
  - `pit28.py` - JDG ryczalt calculator.
  - `normalizers/` - Binance, Kraken, Coinbase, FTX, and salary parsers.
  - `nbp.py`, `prices.py` - exchange-rate and price lookup/cache logic.
- `tests/` - pytest coverage for normalizers, NBP, salary parsing, FIFO, and cost pool.
- `outputs/` - generated tax reports and normalized datasets. These are working
  outputs, not automatically final filing values.
- `docs/todo/` - current operational filing guidance.
- `docs/tax-law/` - legal research topics. Start with:
  - `16-implementation-audit/filing-policy.md`
  - `17-pre-residency-usdc-basis/synthesis-pre-residency-usdc-basis.md`
- `docs/crypto-transactions/` - wallet lists, manual purchase/salary inputs,
  on-chain helper scripts, and crypto-transaction docs.
- `docs/invoices/` - business invoice evidence used by PIT-28 and related checks.
- `web/` - Vite dashboard for inspecting generated PIT-38 data.
- `data/` - NBP and CoinGecko caches.
- `private/` - ignored private evidence and raw archives. Do not expose,
  summarize only at the level needed for the user, and do not commit it.

## Private Evidence

`private/` is intentionally gitignored and contains sensitive tax evidence,
Koinly exports, on-chain raw archives, and working evidence summaries. Useful
current private docs include:

- `private/evidence/onchain/archive-summary-2026-04-25.md`
- `private/evidence/onchain/chain-migration-timeline-2026-04-25.md`

Do not move private files into tracked folders unless the user explicitly asks
and understands the privacy impact. If a task needs evidence from `private/`,
read it locally and write only the necessary derived summary to tracked docs.

## Common Commands

Run tests:

```bash
python -m pytest tests/ -q
```

Run the main PIT-38 flow:

```bash
PYTHONPATH=src python -m tax_calc full --policy all --primary-policy split_year_conservative
```

Run PIT-38 only with explicit imported-basis inputs:

```bash
PYTHONPATH=src python -m tax_calc pit38 \
  --policy all \
  --primary-policy split_year_conservative \
  --polish-residency-start 2023-04-12 \
  --imported-fiat-costs 0 \
  --imported-salary-usdc-costs 0 \
  --imported-successor-costs 0
```

Run the wallet tracker from `docs/crypto-transactions/`:

```bash
python3 crypto_wallet_tracker.py --wallets-file wallets.txt --config config.json --discover-only
python3 crypto_wallet_tracker.py --wallets-file wallets.txt --config config.json --year 2025 --output-dir outputs
```

Run the web dashboard:

```bash
cd web
npm run dev
```

## Engineering Notes

- Use `rg` / `rg --files` for repo search.
- Prefer existing normalizer and tax-model patterns over new ad hoc parsing.
- Keep legal-policy changes separate from arithmetic/code changes when possible.
- Generated reports can be stale. Always check the current docs in `docs/todo/`
  before treating an output file as filing-source.
- If changing calculations, update or add tests and regenerate affected reports
  when practical.
- Do not revert unrelated dirty work. This repo often has multiple concurrent
  edits and private evidence updates.

## Tax-Specific Cautions

- This is decision support, not formal tax advice. Preserve uncertainty in docs
  where the research is unresolved.
- PIT-38 uses Polish annual cost pooling, not FIFO, for Polish reporting. FIFO
  may still be useful for reconstruction or foreign evidence.
- Split-year PIT-38 policy starts Polish revenue from `2023-04-12`.
- Pre-residency imported basis must be reconstructed from move-date inventory
  and Swedish surviving basis, not from a synthetic full-history Polish pool.
- For PIT-28, health insurance deduction reduces revenue, not tax.
- For PIT-36 2025, the working model is personal-services income with 20% costs,
  but classification remains fact-sensitive.

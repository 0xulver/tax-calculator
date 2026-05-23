# Claude Code Guide

Read `../AGENTS.md` first. It is the canonical onboarding guide for this repo.

Fast orientation:

- Current operational docs are in `docs/todo/`.
- Current PIT-38 legal policy is topic 17:
  `docs/tax-law/17-pre-residency-usdc-basis/synthesis-pre-residency-usdc-basis.md`.
- PIT-38 is blocked on the `2023-04-12` imported-basis ledger. Optimism and
  Arbitrum pre-residency activity must be included.
- PIT-36 and PIT-28 2025 are arithmetically ready, with evidence caveats in
  `docs/todo/readiness-assessment.md`.
- `private/` is ignored sensitive evidence. Do not move it into tracked files
  or quote it unnecessarily.

Useful commands:

```bash
python -m pytest tests/ -q
PYTHONPATH=src python -m tax_calc full --policy all --primary-policy split_year_conservative
cd web && npm run dev
```

When editing, keep changes scoped, preserve existing uncertainty in tax docs,
and update tests/reports when calculation behavior changes.

# Crypto wallet tracker

This folder now contains a command line tracker for wallet discovery and transaction export.

## Files

- `wallets.txt` - your wallet list (`label address`, one per line).
- `config.json` - chain and API configuration.
- `crypto_wallet_tracker.py` - script to discover chains and fetch normalized transactions.
- `outputs/` - generated CSV files.

## Setup

Set RPC/API credentials you want to use as environment variables.

- `ETHERSCAN_API_KEY`

EVM chains in this tracker use Etherscan V2, which expects a single `ETHERSCAN_API_KEY` plus a per-chain `chainid`.

## Quick commands

Run from `docs/crypto-transactions`:

- Discover active chains only (no full pulls):
  - `python3 crypto_wallet_tracker.py --wallets-file wallets.txt --config config.json --discover-only`
- Export 2025 data (default fetch scope = 2025):
  - `python3 crypto_wallet_tracker.py --wallets-file wallets.txt --config config.json --year 2025 --output-dir outputs`
- Export 2025 + backfill from config history start:
  - `python3 crypto_wallet_tracker.py --wallets-file wallets.txt --config config.json --year 2025 --full-history --output-dir outputs`
- Limit to one wallet label:
  - `python3 crypto_wallet_tracker.py --wallets-file wallets.txt --wallet-filter "Reaper"`
- Limit to one chain:
  - `python3 crypto_wallet_tracker.py --wallets-file wallets.txt --chain-filter polygon --year 2025`

## Output files

- `outputs/wallet_chain_activity.csv` - wallet-chain discovered and whether provider returned data.
- `outputs/all_transactions.csv` - normalized transactions for the selected fetch window.
- `outputs/transactions_<YEAR>.csv` - year-filtered view (e.g. `transactions_2025.csv`).
- `outputs/monthly_summary_<YEAR>.csv` - month aggregated totals by wallet/chain/token/direction.
- `outputs/salary_candidates_<YEAR>.csv` - optional file if salary filter is enabled in config.

## Notes

- The script is intentionally conservative and uses only public JSON-RPC / explorer endpoints.
- Some providers can rate-limit heavily. Increase `request_delay_seconds` in `config.json` if needed.
- Polygon/EVM scanners use Etherscan-compatible APIs and are chain-configurable through `config.json`.
- Sui parsing currently relies on transaction block balance changes; this gives good coverage for wallet balance movement, but may still miss full semantic context of complex contracts.

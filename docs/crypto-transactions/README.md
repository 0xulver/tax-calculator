# Crypto wallet tracker

This folder now contains a command line tracker for wallet discovery and transaction export.

## Files

- `wallets.txt` - your wallet list (`label address`, one per line).
- `config.json` - chain and API configuration.
- `crypto_wallet_tracker.py` - script to discover chains and fetch normalized transactions.
- `archive_evm_explorer_transactions.py` - raw Etherscan-compatible archive for supported EVM chains.
- `archive_blockscout_v2_transactions.py` - raw Blockscout v2 archive for chains like Optimism/Mode.
- `archive_oklink_transactions.py` - raw OKLink archive for Fantom.
- `archive_evm_transfer_logs.py` - raw EVM RPC `Transfer` log archive by wallet address.
- `archive_evm_traces.py` - raw EVM `trace_filter` archive for native/internal value traces.
- `archive_evm_transaction_traces.py` - raw EVM `trace_transaction` archive for tx hashes already discovered from transfer logs.
- `build_move_date_inventory.py` - reconstructs the `2023-04-12` on-chain asset snapshot from archived evidence.
- `build_move_date_cost_provenance.py` - creates the Layer A/B/C/D/E imported-basis review ledger from the move-date inventory and Koinly evidence.
- `build_move_date_basis_decision.py` - traces the highest-impact Layer C positions and quantifies the remaining imported-basis threshold gap.
- `build_move_date_unwind_traces.py` - verifies post-move exits/current zero balances for the highest-impact Layer C positions.
- `build_move_date_cdp_positions.py` - queries protocol-state CDP collateral/debt at the `2023-04-12` move-date block, including positions not visible as wallet token balances.
- `build_wbtc_cdp_basis_trace.py` - traces the Ethos WBTC CDP collateral top-ups and cross-chain predecessor transactions.
- `build_wbtc_swedish_evidence_checklist.py` - checks the WBTC CDP trace against available Koinly transaction-history exports and lists remaining self-calculation rows.
- `build_wbtc_basis_rollforward.py` - scales the WBTC CDP trace to the actual top-up quantities and separates exact Koinly anchors from source-open stablecoin proxy legs.
- `build_wbtc_stablecoin_source_workpaper.py` - isolates the WBTC stablecoin source-open rows and their immediate on-chain evidence.
- `build_wbtc_fantom_usdc_sender_scan.py` - scans the external Fantom USDC sender behind the WBTC source-open row.
- `build_reaper_multistrategy_hack_thread.py` - isolates the Reaper multi-strategy vault hack/compensation evidence thread behind the Fantom USDC source-open row.
- `build_wbtc_reaper_recovery_link.py` - links direct and forward-traced Reaper recovery rows to the WBTC predecessor trace and separates the March 2023 source-open USDC leg.
- `outputs/` - generated CSV files.

## Setup

Set RPC/API credentials you want to use as environment variables.

- `ETHERSCAN_API_KEY`
- `OKLINK_API_KEY`

EVM chains in this tracker use Etherscan V2, which expects a single `ETHERSCAN_API_KEY` plus a per-chain `chainid`.
Fantom is configured for OKLink instead, because the Etherscan V2 account API rejected Fantom `chainid=250` during the April 25 archive attempt.

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
- Archive Fantom raw history through OKLink:
  - `python3 archive_oklink_transactions.py --wallets-file wallets.txt --config config.json --chain-filter fantom --output-dir ../../private/evidence/onchain/raw/oklink`
- Archive Fantom token-transfer logs through public RPC:
  - `python3 archive_evm_transfer_logs.py --wallets-file wallets.txt --config config.json --chain-filter fantom --start-date 2020-04-24 --output-dir ../../private/evidence/onchain/raw/rpc-transfer-logs`
- Archive Fantom address traces through Fantom tracing RPC:
  - `python3 archive_evm_traces.py --wallets-file wallets.txt --config config.json --chain-filter fantom --start-date 2020-04-24 --output-dir ../../private/evidence/onchain/raw/rpc-traces`
- Archive Fantom transaction traces for pre-move token-movement transactions:
  - `python3 archive_evm_transaction_traces.py --config config.json --chain fantom --source-dir ../../private/evidence/onchain/raw/rpc-transfer-logs/fantom --output-dir ../../private/evidence/onchain/raw/rpc-transaction-traces --before-date 2023-04-12`
- Build the move-date inventory snapshot:
  - `python3 build_move_date_inventory.py --wallets-file wallets.txt --raw-dir ../../private/evidence/onchain/raw --output-dir ../../private/evidence/onchain/move-date-inventory-2023-04-12 --cutoff 2023-04-12T00:00:00Z`
- Build the move-date cost-provenance workpaper:
  - `python3 build_move_date_cost_provenance.py`
- Build the move-date CDP protocol-state workpaper:
  - `python3 build_move_date_cdp_positions.py`
- Build the Ethos WBTC CDP basis trace:
  - `python3 build_wbtc_cdp_basis_trace.py`
- Build the Ethos WBTC Swedish/Koinly evidence checklist:
  - `python3 build_wbtc_swedish_evidence_checklist.py`
- Build the Ethos WBTC scaled basis roll-forward:
  - `python3 build_wbtc_basis_rollforward.py`
- Build the Ethos WBTC source-open stablecoin workpaper:
  - `python3 build_wbtc_stablecoin_source_workpaper.py`
- Scan the external Fantom USDC sender behind the WBTC source-open row:
  - `python3 build_wbtc_fantom_usdc_sender_scan.py`
- Build the Reaper multi-strategy hack/compensation thread:
  - `python3 build_reaper_multistrategy_hack_thread.py`
- Build the Reaper recovery to WBTC link workpaper:
  - `python3 build_wbtc_reaper_recovery_link.py`
- Build the move-date basis decision workpaper:
  - `python3 build_move_date_basis_decision.py`
- Build the move-date unwind workpaper:
  - `python3 build_move_date_unwind_traces.py`

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
- The main normalized tracker does not yet normalize OKLink responses, RPC transfer-log archives, or transaction-trace archives; use `archive_evm_transfer_logs.py` for Fantom token movements and `archive_oklink_transactions.py` for Fantom normal/internal address history once an OKLink key exists.
- RPC `Transfer` logs capture ERC-20/ERC-721 token movements but do not capture native-token transfers, non-transfer contract calls, or position state by themselves.
- `trace_transaction` archives capture full trace trees for known transaction hashes. This is the preferred Fantom trace path for transactions already found from token logs.
- Broad address-level `trace_filter` scans can discover native/internal value traces, but historical Fantom ranges were slow and could fail on the public tracing endpoint. Treat `archive_evm_traces.py` as experimental for small ranges unless an indexed source is available.
- The move-date inventory is an asset-position reconstruction, not a cost-basis calculation. Run `build_move_date_cost_provenance.py` to create the review ledger, then `build_move_date_cdp_positions.py` to add protocol-state collateral/debt that token-transfer balances can miss, `build_wbtc_cdp_basis_trace.py` to trace the main WBTC CDP collateral path, `build_wbtc_swedish_evidence_checklist.py` to check available Koinly evidence for that path, `build_wbtc_basis_rollforward.py` to scale that path into exact/proxy/open buckets, `build_wbtc_stablecoin_source_workpaper.py` to isolate the remaining stablecoin source-open judgment, `build_wbtc_fantom_usdc_sender_scan.py` to scan the external Fantom USDC sender if that row is needed, `build_reaper_multistrategy_hack_thread.py` to isolate the Reaper multi-strategy vault hack/compensation path, `build_wbtc_reaper_recovery_link.py` to link direct and forward-traced Reaper recovery rows to the WBTC path, `build_move_date_basis_decision.py` to generate the max supportable no-debt candidate ledger and threshold scenarios, and `build_move_date_unwind_traces.py` to verify post-move exits and current zero balances for the priority positions. Rows still need final Swedish acquisition/replacement-basis tracing, no-double-counting review, and PLN conversion before they become imported PIT-38 costs.
- Sui parsing currently relies on transaction block balance changes; this gives good coverage for wallet balance movement, but may still miss full semantic context of complex contracts.

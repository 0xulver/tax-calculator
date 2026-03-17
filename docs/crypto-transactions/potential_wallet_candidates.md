# Potential Wallet Candidates

This note is a review list of wallet families that may be missing from [wallets.txt](/home/ulver/code/ai/tax-calculator/docs/crypto-transactions/wallets.txt), based on Binance and Kraken exchange exports from `2020` through `2025`.

Important limitation:
- The exchange exports reviewed here do **not** contain explicit destination/source wallet addresses.
- Because of that, this is a list of **candidate wallet families or chains**, not confirmed wallet addresses.
- Nothing here has been added to `wallets.txt`.

Current wallet families already in `wallets.txt`:
- EVM (`0x...`)
- Solana
- Sui

## High Confidence Candidates

| Candidate | Why it looks likely | Evidence from exchange history | Confidence | Confirmed? |
| --- | --- | --- | --- | --- |
| Bitcoin wallet(s) | You have both BTC withdrawals and later BTC deposits across exchanges, but no BTC wallet in `wallets.txt`. | Kraken BTC withdrawals in `2020-12-01 09:36:59`, `2021-01-04 11:20:00`, `2022-12-10 19:11:41`, `2023-01-12 06:24:03`. Binance BTC deposits in `2021-08-11 11:41:14`, `2021-08-11 11:53:06`, `2021-08-11 14:27:12`. | High | `[ ]` |
| Terra wallet(s) | You moved `LUNA` and `UST`, and there is no Terra wallet in `wallets.txt`. | Binance `LUNA` withdrawals in `2021-08-11 14:38:41`, `2021-08-12 07:00:52`, and many more in `2021-2022`. Binance `UST` withdrawals in `2022-01-05 16:02:42`, `2022-01-07 16:53:42`, `2022-01-23 11:08:42`. | High | `[ ]` |
| Polkadot / Kusama / Substrate wallet(s) | You moved `DOT`, `KSM`, `ACA`, `KAR`, which strongly suggests at least one Substrate-style wallet not listed. | Binance `DOT` withdrawal `2021-12-26 23:17:41`; Binance `KSM` withdrawals `2021-12-09 22:09:42`, `2022-01-23 12:13:42`; Binance `ACA` withdrawals `2022-01-31 13:21:40`, `2022-01-31 13:35:40`. Kraken `DOT`, `KSM`, and `KAR` withdrawals in `2021`. | High | `[ ]` |
| Cosmos wallet(s) | You withdrew `ATOM`, but there is no Cosmos wallet in `wallets.txt`. | Binance `ATOM` withdrawals `2022-01-31 11:33:41`, `2022-01-31 11:36:42`, `2022-02-06 11:59:41`, `2022-02-06 12:46:40`. Kraken `ATOM` deposits in `2022-05-27 13:56:46`, `2022-05-27 14:08:14`, `2022-06-04 17:47:04`. | High | `[ ]` |
| Monero wallet(s) | You withdrew `XMR`, and there is no Monero wallet in `wallets.txt`. | Kraken `XMR` withdrawals `2022-11-21 13:53:36` and `2022-11-21 14:29:36`. | High | `[ ]` |

## Medium Confidence Candidates

| Candidate | Why it looks possible | Evidence from exchange history | Confidence | Confirmed? |
| --- | --- | --- | --- | --- |
| Additional EVM wallet(s) | Many `ETH`, `LINK`, `AAVE`, `SNX`, `USDC`, `USDT`, `MATIC`, `FTM` transfers could map to your known EVM wallets, but could also point to older or separate EVM addresses not listed. | Kraken `ETH`, `LINK`, `AAVE`, `SNX` withdrawals in `2020-2021`; Binance `FTM` withdrawals in `2021-2022`; Kraken `USDC` and `USDT` deposits in `2021-2024`; Kraken `MATIC` deposits in `2022-2023`. | Medium | `[ ]` |
| Additional Solana wallet(s) | You already have one Solana wallet listed, but exchange flows suggest there may have been another Solana address as well. | Binance `SOL` withdrawals `2021-08-27 12:23:42`, `2021-08-27 12:29:42`, `2025-03-02 17:26:43`, `2025-03-02 17:28:43`. Kraken `SOL` withdrawals `2021-09-13 10:40:38`, `2021-09-13 10:43:38`, `2021-09-15 12:09:03`. | Medium | `[ ]` |
| Additional Sui wallet(s) | You already have two Sui wallets listed, but the exchange withdrawals may have gone to one of those or to a separate Sui address. | Binance `SUI` withdrawals `2024-11-19 17:18:42`, `2024-12-01 20:13:41`, `2024-12-17 09:34:43`. Kraken `SUI` withdrawals `2025-08-07 19:48:09`, `2025-08-18 13:17:42`. | Medium | `[ ]` |

## Lower Confidence / Maybe Already Covered

| Candidate | Why it is weaker | Evidence from exchange history | Confidence | Confirmed? |
| --- | --- | --- | --- | --- |
| Existing known EVM wallet reuse | Some exchange deposit patterns may simply be funds returning from wallets you already listed. | Binance `USDC` deposits in `2024-2025`; Kraken `USDC` deposits in `2020-2025`; Binance `ETH` deposits in `2024-2025`; Kraken `ETH` deposits in `2022`, `2024`. | Low | `[ ]` |
| Existing known Solana wallet reuse | Your current Solana wallet may already account for some of the Solana exchange movements. | Binance `SOL` deposits in `2021`; Kraken `SOL` withdrawals in `2021`; Binance `SOL` withdrawals in `2025`. | Low | `[ ]` |
| Existing known Sui wallet reuse | Your current Sui wallets may already explain the `SUI` withdrawals. | Binance `SUI` withdrawals in `2024`; Kraken `SUI` withdrawals in `2025`. | Low | `[ ]` |

## Practical Interpretation

The strongest likely omissions from `wallets.txt` are:
- Bitcoin
- Terra
- Polkadot / Kusama / broader Substrate
- Cosmos
- Monero

The weaker candidates are not about a new chain family, but about whether you used an additional wallet on a chain family you already track:
- another EVM wallet
- another Solana wallet
- another Sui wallet

## Best Next Step

To turn these from chain-level candidates into actual wallet addresses, the best source is:
- Binance withdrawal/deposit export with destination address and network
- Kraken withdrawal/deposit export with destination address and method/network

If you export those, I can compare the actual addresses against `wallets.txt` and produce a much cleaner confirmed/unconfirmed candidate list.

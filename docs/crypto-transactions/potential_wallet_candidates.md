# Potential Wallet Candidates

Updated analysis of wallets that may be missing from [wallets.txt](file:///home/ulver/code/ai/tax-calculator/docs/crypto-transactions/wallets.txt), based on comprehensive review of Binance and Kraken exchange exports from `2020` through `2025`.

> [!IMPORTANT]
> The exchange CSV exports **do not contain destination/source wallet addresses**. To get actual addresses, use the **exchange web UI** withdrawal history (Binance: Wallet → Transaction History → Withdrawals; Kraken: History → Withdrawals) or check **email confirmations** which include destination addresses.

Current wallets in `wallets.txt`:
- 4 EVM (`0x...`) — Reaper, Metamask2, Metamask3, Reaper strategist
- 1 Solana — Old Solana `4QjwQQ...`
- 2 Sui — Ulver Stashed, m.brantheim stashed

---

## High Confidence — Missing Wallet Families

### 1. ✅ Polkadot / Kusama — CONFIRMED

| Detail | DOT | KSM |
| --- | --- | --- |
| **Withdrawn from exchanges** | ~2,919 DOT (16 txs) | ~696 KSM (16 txs across Kraken+Binance) |
| **Deposited back** | ~3,045 DOT (7 deposits) | ~226 KSM (9 deposits) |
| **Withdrawal period** | Apr 2021 — May 2022 | Jul 2021 — Jul 2023 |
| **Deposit period** | Jul 2021 — May 2022 | Oct 2021 — May 2022 |
| **Pattern** | Staking (large out, partial return) | Crowdloans + staking (heavy accumulation) |

**3 DOT addresses found from Kraken saved withdrawal addresses:**

| Label | Address | Type |
| --- | --- | --- |
| Fearless Wallet DOT | `16Q2CwF7mBoQd7ay6YyrBG9eryjvSmyZVjgHzLpFCq5S5Hb3` | Self-custody |
| Celsius Polkadot | `12cH7rXQPZkwy5KbbNvGqgnmS75CSn1EUjrHno6ymBP9KYUq` | Defunct platform (funds stuck) |
| Chloe Celsius DOT | `15iv67DkPLWdBpFSWz1tzsJfjpz5mgr46sDBpaD6j4zNYyDF` | Third-party (ex-girlfriend's wallet, gifted crypto) |

> [!NOTE]
> Chloe's Celsius wallet represents crypto gifts. In Sweden (Skatteverket) and Poland, gifting crypto is generally not a taxable disposal for the giver, but the cost basis transfers. However, verify with your tax advisor. Celsius is defunct — same warning as BTC Celsius.

**Related parachain tokens also withdrawn:**
- **ACA** (Acala): 2 Binance withdrawals on 2022-01-31 (~556 ACA total)
- **KAR** (Karura): 1 Kraken withdrawal on 2021-10-08 (6 KAR)

**KSM address also found (same Fearless Wallet seed):**

| Label | Address | Type |
| --- | --- | --- |
| Fearless Wallet KSM | `DdpP9Qtic67emirWfRBA4NNbwqBp4UEbqgpSvNyfh6yyQ37` | Self-custody |

| Confirmed? |
| --- |
| DOT: `[x]` / KSM: `[x]` |

---

### 2. Cosmos (ATOM)

| Detail | Value |
| --- | --- |
| **Withdrawn (Binance)** | ~297 ATOM (4 txs: 2022-01-31, 2022-02-06) |
| **Deposited (Kraken)** | ~353 ATOM (3 txs: 2022-05-27, 2022-06-04) |
| **Pattern** | Binance → self-custody (staking ~4 months) → Kraken |

**Evidence strength:** Very strong. Clear flow: bought ATOM on Binance, withdrew to self-custody wallet for ~4 months (likely staking on-chain), then deposited to Kraken and sold.

**Likely wallet software:** Keplr browser extension or Cosmostation.

| Confirmed? |
| --- |
| `[ ]` |

---

### 3. Terra (LUNA / UST)

| Detail | LUNA | UST |
| --- | --- | --- |
| **Withdrawn** | ~3,459 LUNA (23 Binance txs) | ~44,016 UST (4 Binance txs) |
| **Deposited back** | ~4,862 LUNA (17 Binance deposits) | ~2,500 UST (1 deposit) |
| **Active period** | Aug 2021 — Feb 2022 | Jan 2022 |
| **Also deposited to Kraken** | LUNA2: 69 (May 2022 — post-collapse airdrop) | — |

**Evidence strength:** Very strong. Heavy DeFi activity (27 withdrawals, 18 deposits). The massive UST withdrawals (~$44K) strongly suggest Anchor Protocol usage for the ~20% APY yield. The LUNA2 Kraken deposit confirms you received the post-collapse airdrop, meaning you held LUNA in a Terra wallet at the snapshot.

**Likely wallet software:** Terra Station.

> [!NOTE]
> Terra Classic collapsed in May 2022. The wallet still exists on Terra Classic chain but is likely near-worthless. The LUNA2 airdrop was distributed to a new Terra 2.0 address derived from the same key. For tax purposes, the acquisition dates and disposals in 2021-2022 are the relevant events.

| Confirmed? |
| --- |
| `[ ]` |

---

### 4. ✅ Bitcoin (BTC) — CONFIRMED

| Detail | Value |
| --- | --- |
| **Withdrawn (Kraken)** | ~0.62 BTC (13 txs: Dec 2020 — Jan 2023) |
| **Deposited (Binance)** | ~0.31 BTC (3 txs: Aug 2021) |
| **Pattern** | Kraken → BTC wallet → partially moved to Binance |

**6 BTC addresses found from Kraken saved withdrawal addresses:**

| Label | Address | Type |
| --- | --- | --- |
| Electrum | `bc1qjd8pnqhkla4fsj0kt7rw96kd0drvqkugstn2z7` | Self-custody |
| Electrum 2 | `bc1qlkjyugnzkyfp7snhkh5przhwz8xcv7kmypy9yl` | Self-custody |
| Electrum 3 | `bc1qjllxk2j2n029pakreue07x3agsfkjkm3ufuzqs` | Self-custody |
| Electrum withdraw | `bc1q7sxfz3yuq0crvza7wj9de628fnykl575k5e3hj` | Self-custody |
| Celsius BTC | `bc1qvvreqkvs03l86eheelqs8j3wvy6mx2ul0rjz7r` | Defunct platform (funds stuck) |
| BlockFi BTC | `3GV34TNcQUS53MimCWd8rMjKLxJF3C6Qoj` | Defunct platform (funds stuck) |

> [!WARNING]
> Celsius and BlockFi are no longer operational. Funds sent to those addresses may be stuck or subject to bankruptcy proceedings. For tax purposes, the withdrawal from Kraken to those addresses is still a reportable event, but any loss of funds may be claimable as a capital loss depending on jurisdiction.

| Confirmed? |
| --- |
| `[x]` |

---

### 5. Monero (XMR)

| Detail | Value |
| --- | --- |
| **Withdrawn (Kraken)** | ~0.42 XMR (2 txs: 2022-11-21) |
| **Deposited back** | None |

**Evidence strength:** Moderate. Only 2 withdrawals on the same day, small amount. Still, this confirms a Monero wallet exists somewhere.

> [!NOTE]
> Monero is privacy-focused. On-chain tracing is not possible. The wallet address can only be found from Kraken withdrawal history, email confirmations, or the wallet software itself.

| Confirmed? |
| --- |
| `[ ]` |

---

## Medium Confidence — Additional Wallets on Known Chains

### 6. Second Solana Wallet (NEW)

| Detail | Value |
| --- | --- |
| **Known wallet** | `4QjwQQ4gny4YZbpZtj6aThtRKSz4ALmtxUBS3tY7BpSC` (active through Nov 2025) |
| **Binance SOL withdrawals (2021)** | 2 txs on 2021-08-27 (~51 SOL) — could be same wallet |
| **Binance SOL withdrawals (2025)** | 2 txs on 2025-03-02 (~138 SOL) — **4 years later** |
| **Kraken SOL withdrawals (2021)** | 4 txs on 2021-09-13/15 (~35 SOL) |

**Evidence strength:** Medium-High. The **2025 withdrawals** are 4 years after the 2021 ones. If you set up a new wallet (Phantom, Backpack) in the intervening years, the 2025 SOL likely went to a different address. The known "Old Solana" wallet name itself suggests you consider it old.

| Confirmed? |
| --- |
| `[ ]` |

---

### 7. Additional EVM Wallets

| Detail | Value |
| --- | --- |
| **Kraken ETH withdrawals** | 12 txs (~66 ETH) in Dec 2020 — Jan 2021 |
| **Kraken ETH deposits back** | 6 txs (~3.9 ETH) in 2022-2024 |
| **Kraken LINK** | 7 withdrawals (~253 LINK), 1 deposit (199 LINK) |
| **Kraken SNX** | 5 withdrawals (~487 SNX) |
| **Kraken AAVE** | 6 withdrawals (~7.4 AAVE) |
| **Kraken FTM deposits** | 12 deposits (~130K FTM) |
| **Kraken MATIC deposits** | 11 deposits (~52K MATIC) |

**Evidence strength:** Medium. These could all map to your 4 known EVM wallets. However, the early 2020 withdrawals predate some DeFi activity and might have gone to an older wallet.

| Confirmed? |
| --- |
| `[ ]` |

---

### 8. Additional Sui Wallets

| Detail | Value |
| --- | --- |
| **Binance SUI withdrawals** | 6 txs in Nov-Dec 2024 |
| **Kraken SUI withdrawals** | 2 txs in Aug 2025 (~2,555 SUI) |

**Evidence strength:** Low-Medium. You have 2 Sui wallets already. The Binance withdrawals (2024) and Kraken withdrawals (2025) may go to your known Stashed wallets, or to a third wallet.

| Confirmed? |
| --- |
| `[ ]` |

---

## Summary: Priority Action Items

| Priority | Chain | Estimated Wallet Count | Best Way to Find Address |
| --- | --- | --- | --- |
| 🔴 **Critical** | Polkadot/Kusama (DOT/KSM/ACA/KAR) | 1-2 Substrate wallets | Polkadot.js extension, Ledger, or exchange withdrawal history |
| 🔴 **Critical** | Cosmos (ATOM) | 1 Cosmos wallet | Keplr extension or exchange withdrawal history |
| 🔴 **Critical** | Terra (LUNA/UST) | 1 Terra wallet | Terra Station or exchange withdrawal history |
| 🟡 **Important** | Bitcoin (BTC) | 1 BTC wallet | Electrum/Wasabi/Ledger or exchange withdrawal emails |
| 🟡 **Important** | Solana (new) | Likely 1 additional | Phantom/Backpack or Binance 2025 withdrawal history |
| 🟠 **Moderate** | Monero (XMR) | 1 XMR wallet | Monero GUI/CLI or Kraken withdrawal email |
| ⚪ **Low** | EVM / Sui | Possibly 1+ more | Already tracked partially |

## Fastest Way to Resolve All of These

1. **Check Binance withdrawal history** in the web UI (Wallet → Spot → Transaction History → Withdrawals) — filter by DOT, KSM, ATOM, LUNA, BTC, SOL, XMR. **Each withdrawal shows the destination address.**
2. **Check Kraken withdrawal history** in the web UI (History → Exports → Withdrawals export) — same approach.
3. **Search email** for "withdrawal" + coin name — confirmation emails from Binance/Kraken contain destination addresses.
4. **Check browser extensions** — Polkadot.js, Keplr, Phantom, Terra Station may still have the accounts.
5. **Check Ledger Live** if you used a hardware wallet — accounts tab will show all chains.

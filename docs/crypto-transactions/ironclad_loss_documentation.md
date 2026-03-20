# Ironclad Finance — Loss Documentation (Ionic Money Hack)

## Summary

On **February 4, 2025**, the Ionic Money protocol on Mode Network was exploited via a social engineering attack. The attacker used stolen MBTC tokens as collateral on Ironclad Finance's lending pool to borrow all available ETH. Merlin (MBTC issuer) subsequently burned the MBTC, rendering the collateral worthless and creating permanent bad debt in Ironclad's lending pool. All user funds deposited in the lending pool are irrecoverable.

**Affected wallet**: `0xB573f01f2901c0dB3E14Ec80C6E12e4868DEC864` (Metamask3)

**Loss**: ~22.6 ETH locked as Trove collateral (ic-ETH vault tokens backed by the drained lending pool) + ~27,195 iUSD outstanding debt

---

## Timeline of Events

### 1. Trove Opening and Deposits (Oct 26, 2024 — Jan 2025)

| Date | Action | ETH Amount | Tx Hash |
|------|--------|-----------|---------|
| 2024-10-26 09:09 | **openTrove** (initial deposit) | ~8.99 ETH | `0x6018acc3b0624707...` |
| 2024-10-26 09:21-09:33 | adjustTrove (add collateral) | +3.0 ETH × 2 | `0xfd49cde615273049...`, `0xe6cdeee9d6886c6d...` |
| 2024-10-28 12:23-13:35 | adjustTrove (add collateral) | +3.0 ETH × 4 | `0x859c46d9e9eadb8a...`, `0x9ae7e96099a0ecab...`, `0x9e7ba9bc4e113655...`, `0x42ebbc423b14b048...` |
| 2024-10-29 11:17 | adjustTrove (add collateral) | +3.0 ETH | `0x46e7c73907f26042...` |
| 2024-10-31 08:16 | adjustTrove (add collateral) | +3.0 ETH | `0xf735371f4cb38287...` |
| 2024-11-04 — 2024-12-12 | Multiple adjustTrove calls | various | see on-chain |
| 2024-12-19 — 2025-02-03 | adjustTrove (ongoing management) | various | see on-chain |

**Deposit mechanism**: ETH → wrapped to WETH → deposited into ic-ETH Vault (Ironclad ETH Vault) → ic-ETH used as Trove collateral → iUSD borrowed

### 2. The Hack — February 4, 2025

**Attack flow (Ionic Money exploit):**
1. Attackers impersonated Lombard Finance team members
2. Social-engineered Ionic Money into listing a counterfeit LBTC token
3. Minted 250 fake LBTC tokens → used as collateral on Ionic
4. Borrowed ~$8.6M in real tokens from Ionic (including MBTC and iBTC)
5. Swapped borrowed tokens to MBTC
6. **Deposited stolen MBTC as collateral on Ironclad Finance lending pool**
7. **Borrowed ALL available ETH from Ironclad lending pool** (~460.85 ETH)
8. Bridged ~1,204 ETH to Ethereum mainnet → laundered through Tornado Cash

**Attacker address**: `0x9E34d89C013Da3BF65fc02b59B6F27D710850430`
**Fake LBTC contract**: `0x964dd444e3192f636322229080a576077b06fba3`

### 3. MBTC Burn by Merlin (post-hack)

Merlin (the MBTC token issuer) used a **pre-exploit snapshot** to protect MBTC holders. This effectively:
- Made all MBTC held by Ironclad's lending pool **worthless**
- The 30.4 MBTC deposited as collateral by the hacker was burned/invalidated
- Created **permanent bad debt** in Ironclad's lending pool
- Ironclad could not liquidate the worthless MBTC to recover the borrowed ETH

### 4. Post-Hack: Markets Frozen

Ironclad Finance froze all markets immediately after the exploit. The protocol was marked as "dead" on DefiLlama starting February 5, 2025.

### 5. Attempted Debt Repayment (Feb 21 — Apr 3, 2025)

After the hack, the wallet owner made numerous `adjustTrove` calls to repay iUSD debt, purchasing iUSD on DEXes (Odos Router) and sending to the BorrowerHelper contract. This was an attempt to reduce the Trove position and potentially extract remaining collateral.

---

## On-Chain Proof of Loss

### Current Trove Position (as of March 2026)

Verified via direct smart contract reads:

| Parameter | Value | Contract |
|-----------|-------|----------|
| Trove Status | 1 (Active) | TroveManager `0x829746b34F624fdB03171AA4cF4D2675B0F2A2e6` |
| Collateral | **22,600,604,469,927,607,879 wei** (~22.60 ic-ETH) | TroveManager |
| Debt | **27,194,821,387,709,259,041,425 wei** (~27,194.82 iUSD) | TroveManager |
| Collateral type | ic-ETH Vault `0x3117c7854d11cB0216c82B81934CAaFe0722BB44` | — |

### Lending Pool Status (proof of bad debt)

| Parameter | Value | Contract |
|-----------|-------|----------|
| ironETH total supply (depositor claims) | **460,852,706,081,878,943,222 wei** (~460.85 ETH) | ironETH `0x9c29a8eC901DBec4fFf165cD57D4f9E03D4838f7` |
| variableDebtETH (outstanding borrows) | **460,855,123,226,125,826,232 wei** (~460.85 ETH) | variableDebtETH `0x06D38c309d1dC541a23b0025B35d163c25754288` |
| Actual WETH in lending pool | **0** | LendingPool `0xB702cE183b4E1Faa574834715E5D4a6378D0eEd3` |
| Actual WETH held by ironETH contract | **0** | WETH `0x4200000000000000000000000000000000000006` |
| ironMBTC (worthless collateral) | **30,401,097,006,800,163,723 wei** (~30.4 MBTC) | ironMBTC `0xC17312076F48764d6b4D263eFdd5A30833E311DC` |
| MBTC underlying | `0x59889b7021243dB5B1e065385F918316cD90D46c` | burned/invalidated by Merlin |

**Key finding**: 100% of ETH was borrowed from the lending pool (460.85 ETH borrowed vs 460.85 ETH in depositor claims). The pool holds 0 WETH. The MBTC collateral used by the hacker is worthless.

### ic-ETH Vault Status

| Parameter | Value |
|-----------|-------|
| Vault address | `0x3117c7854d11cB0216c82B81934CAaFe0722BB44` |
| Underlying asset | WETH `0x4200000000000000000000000000000000000006` |
| Total supply | 35,441,842,646,759,349,039 (~35.44 ic-ETH) |
| Reported totalAssets | 35,441,842,646,759,349,039 (~35.44 WETH) |
| Actual WETH held by vault | **0** |
| Actual ironETH held by vault | **0** |

The vault reports a 1:1 exchange rate, but the underlying assets are inaccessible because the lending pool is drained. **The ic-ETH tokens are effectively worthless.**

---

## Loss Calculation

### ETH Price Data (Binance ETHUSDT)

| Date | Open | High | Low | Close |
|------|------|------|-----|-------|
| **2024-10-26** (Trove opened) | $2,440.63 | $2,508.00 | $2,430.12 | $2,482.51 |
| 2024-10-28 (major deposits) | $2,507.80 | $2,589.67 | $2,471.67 | $2,567.48 |
| 2024-10-29 | $2,567.49 | $2,681.86 | $2,561.20 | $2,638.80 |
| 2024-10-31 | $2,659.19 | $2,669.00 | $2,503.00 | $2,518.61 |
| **2025-02-04** (hack date) | $2,879.89 | $2,888.50 | $2,632.60 | **$2,731.19** |

### 1. Locked Collateral (irrecoverable)

| Item | Amount |
|------|--------|
| ic-ETH locked in Trove | 22.60 ic-ETH |
| Nominal ETH value (pre-hack) | ~22.60 ETH |
| Actual recoverable ETH | **0 ETH** |
| **Value at hack date** (22.6 × $2,731.19) | **$61,724.89** |

### 2. Post-Hack iUSD Debt Repayments (wasted expenditure)

After the hack (Feb 4, 2025), the wallet owner purchased iUSD on DEXes (Odos Router) and repaid Trove debt via `adjustTrove` calls. Since the collateral backing is irrecoverable, these repayments are an additional loss.

| Period | iUSD Repaid | Notes |
|--------|-------------|-------|
| Feb 4, 2025 (day of hack) | 19,987.92 | Largest single repayment |
| Feb 21–23, 2025 | 5,019.31 | Multiple small repayments |
| Feb 24–28, 2025 | 7,513.56 | Daily repayments |
| Mar 1–4, 2025 | 2,034.69 | Continued repayments |
| Apr 1–3, 2025 | 3,044.65 | Final repayments |
| **Total post-hack repayments** | **~38,303 iUSD** | **≈ $38,303 USD** (iUSD ~$1 peg) |

### 3. Remaining Debt

| Item | Amount |
|------|--------|
| Current Trove debt | ~27,195 iUSD |
| Status | Likely unrecoverable by protocol (dead) |

### Total Loss Estimate

**Debt at time of hack** (before post-hack repayments): ~27,195 + ~38,303 = **~65,498 iUSD**

| Scenario | Loss |
|----------|------|
| **A. Locked ETH only** (ignore debt — it was already a liability) | 22.6 ETH = **$61,725** |
| **B. ETH + post-hack iUSD repayments** (money spent after hack that couldn't recover collateral) | $61,725 + $38,303 = **$100,028** |
| **C. Net position loss** (ETH value minus forgiven remaining debt) | $61,725 + $38,303 − $27,195 = **$72,833** |

> **Recommended framing for tax purposes**: The loss of the 22.6 ETH collateral is the primary capital loss event ($61,725 at FMV on Feb 4, 2025). The post-hack iUSD repayments of ~$38,303 represent additional economic damage — money spent attempting to close a position against worthless collateral. Consult tax advisor on whether these repayments are deductible as part of the same loss event or separately.

### ETH Price During Repayment Period

For reference, ETH price dropped significantly during the repayment period:

| Date | ETH Close Price |
|------|----------------|
| Feb 4, 2025 (hack) | $2,731.19 |
| Feb 21 | $2,663.00 |
| Feb 28 | $2,237.59 |
| Mar 10 | $1,865.10 |
| Mar 29 | $1,828.08 |
| Apr 3 (last repayment) | $1,817.23 |

The 22.6 ETH locked would be worth only ~$41,069 at Apr 3 prices — a 33% decline from hack date.

---

## Key Contracts Reference

| Contract | Address | Purpose |
|----------|---------|---------|
| Ironclad LendingPool (proxy) | `0xB702cE183b4E1Faa574834715E5D4a6378D0eEd3` | Main lending pool |
| ironETH (aToken for ETH deposits) | `0x9c29a8eC901DBec4fFf165cD57D4f9E03D4838f7` | Deposit receipt token |
| variableDebtETH | `0x06D38c309d1dC541a23b0025B35d163c25754288` | Borrow debt tracking |
| ironMBTC (worthless collateral) | `0xC17312076F48764d6b4D263eFdd5A30833E311DC` | Hacker's deposited collateral |
| MBTC token (burned by Merlin) | `0x59889b7021243dB5B1e065385F918316cD90D46c` | Underlying MBTC |
| ic-ETH Vault | `0x3117c7854d11cB0216c82B81934CAaFe0722BB44` | ETH vault (user's collateral type) |
| TroveManager | `0x829746b34F624fdB03171AA4cF4D2675B0F2A2e6` | CDP position tracking |
| BorrowerHelper | `0x5454891FddbcCe91A79777205A173618634a623F` | User interaction contract |
| BorrowerOperations | `0x9571873B4Df31D317d4ED4FE4689915A2F3fF7d4` | Core borrowing logic |
| Attacker address | `0x9E34d89C013Da3BF65fc02b59B6F27D710850430` | Ionic Money exploiter |

---

## External References

- [Halborn: Explained — The Ionic Money Hack (February 2025)](https://www.halborn.com/blog/post/explained-the-ionic-money-hack-february-2025)
- [Rekt News: Ionic Money — Rekt](https://rekt.news/ionic-money-rekt)
- [Ionic Mode Main Market Exploit Post Mortem (Feb 8, 2025)](https://postmortem.s3.us-east-1.amazonaws.com/postmortem.pdf)
- [Ironclad Finance — DefiLlama](https://defillama.com/protocol/ironclad-finance) (marked dead from Feb 5, 2025)
- [Ironclad Finance X/Twitter](https://x.com/IroncladFinance)
- [Mode Block Explorer — User wallet](https://explorer.mode.network/address/0xB573f01f2901c0dB3E14Ec80C6E12e4868DEC864)

---

## How to Verify (Reproducible Commands)

All on-chain data can be verified using `cast` (from Foundry) with Mode RPC:

```bash
# Check Trove status (1 = active)
cast call 0x829746b34F624fdB03171AA4cF4D2675B0F2A2e6 \
  "getTroveStatus(address,address)(uint256)" \
  0xB573f01f2901c0dB3E14Ec80C6E12e4868DEC864 \
  0x3117c7854d11cB0216c82B81934CAaFe0722BB44 \
  --rpc-url https://mainnet.mode.network

# Check Trove collateral
cast call 0x829746b34F624fdB03171AA4cF4D2675B0F2A2e6 \
  "getTroveColl(address,address)(uint256)" \
  0xB573f01f2901c0dB3E14Ec80C6E12e4868DEC864 \
  0x3117c7854d11cB0216c82B81934CAaFe0722BB44 \
  --rpc-url https://mainnet.mode.network

# Check lending pool has 0 WETH
cast call 0x4200000000000000000000000000000000000006 \
  "balanceOf(address)(uint256)" \
  0x9c29a8eC901DBec4fFf165cD57D4f9E03D4838f7 \
  --rpc-url https://mainnet.mode.network

# Check total ETH borrowed (bad debt)
cast call 0x06D38c309d1dC541a23b0025B35d163c25754288 \
  "totalSupply()(uint256)" \
  --rpc-url https://mainnet.mode.network
```

---

## Tax Implications (Poland)

> ⚠️ Consult with a Polish tax advisor for definitive guidance.

Under Polish crypto tax law (PIT-38):
- Crypto losses from hacks/protocol failures may be claimable as capital losses
- The loss event date is **February 4, 2025** (date the hack occurred and funds became irrecoverable)
- Cost basis: The acquisition cost of the ETH originally deposited (tracked via FIFO from exchange purchases)
- The loss needs to be documented with on-chain evidence (this document)
- Protocol insolvency/bad debt is analogous to platform failure (similar to Celsius/BlockFi precedent)

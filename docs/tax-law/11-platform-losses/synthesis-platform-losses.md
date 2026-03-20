# Synthesis: Tax Treatment of Losses from Collapsed Platforms (Celsius, BlockFi)

Sources: ChatGPT 5.4 Pro, ChatGPT Deep Research, Perplexity, Gemini 3.1 Deep Research

---

## Full Consensus (All 4 agree)

### Bankruptcy itself is NOT a taxable event in Poland
The withdrawal freeze, bankruptcy filing, court proceedings — none of these trigger a "disposal" under Art. 17 ust. 1f. Polish crypto tax only recognizes exchanges for fiat/goods/services/property rights. A platform going bankrupt is simply not on the list.

### There is no "loss deduction" for platform collapses
Polish crypto has no mechanism for claiming a stand-alone bankruptcy loss. Art. 9 ust. 3a pkt 2 excludes crypto from the standard loss carry-forward. The Ministry of Finance says "a crypto tax loss never occurs." Only unused acquisition costs carry forward through the cost pool.

### Original acquisition costs survive and remain in the cost pool
The fiat originally spent to buy the BTC/DOT deposited to Celsius/BlockFi stays in the Polish cost pool. It doesn't disappear because the platform collapsed. These costs can offset future crypto disposal revenue indefinitely. This is the primary economic relief mechanism.

### Do NOT book a fictitious "sale at 0 PLN"
All 4 sources explicitly warn: do not create a fake disposal event at zero value. Polish law taxes actual disposals, not theoretical ones. Booking a zero-value sale invents a taxable event that didn't happen and is legally indefensible.

### Move frozen assets to a separate "claim/frozen" bucket in the tracker
The correct approach: remove the coins from spendable inventory but don't delete them or book them as sold. Keep them in a separate insolvency claim bucket with their original acquisition cost preserved.

### No dedicated PIT-38 field for platform bankruptcy losses
Celsius/BlockFi effects flow through the ordinary crypto Section E fields (revenue/costs/carry-forward). There's no special insolvency line.

### Recovery distributions have different tax treatments by type

| Distribution Type | Polish Tax Treatment | All agree? |
|---|---|---|
| **Crypto received back** (BTC/ETH) | NOT taxable at receipt — taxed only when later sold for fiat | Yes |
| **Fiat received** (USD) | Taxable as crypto disposal revenue in the year received | Yes |
| **Equity received** (Ionic Digital shares) | Taxable as disposal for property rights (19%) at receipt FMV | Yes (Gemini adds most detail) |

### These events occurred while you were a Swedish resident — complicates things
Since Celsius froze in June 2022 and BlockFi in November 2022, you were a Swedish tax resident. The deposits were also made while Swedish. Polish law generally cannot reach pre-residency events. The acquisition COSTS are available in Poland (per WSA 2024 ruling), but a stand-alone "loss" from 2022 belongs to Swedish jurisdiction.

---

## The One Meaningful Disagreement: Was the Deposit Itself a Disposal?

This is the most interesting question and sources diverge on how risky it is:

### The issue
Celsius Earn and BlockFi Interest Accounts **transferred title** of deposited crypto to the platform. You became an unsecured creditor with a claim, not an owner of specific coins. Under Art. 17 ust. 1f, exchanging crypto for a "property right other than virtual currency" (a claim against the platform) IS a taxable disposal.

| Source | Position |
|---|---|
| ChatGPT 5.4 Pro | Flags this as the hardest question. If the deposit was a disposal, the tax moment was the deposit date (pre-Poland). Recommends individual ruling for material amounts. |
| ChatGPT Deep Research | Extensively analyzes both sides. Compares to Swedish approach (Skatteverket treats lending deposits as disposals). Says Polish law doesn't explicitly address this. |
| Perplexity | Takes the simpler view: "depositing to a custodial platform does NOT constitute a taxable disposal" under Polish law. Relies on the fact that the official disposal definition is limited to fiat/goods exchanges. |
| **Gemini** | **Most definitive**: Claims Polish tax code "heavily prioritizes the economic substance" over strict civil law. Despite Celsius transferring legal title, Polish tax law treats the deposit as a tax-neutral transfer, NOT a disposal. "The act of depositing was definitively not a taxable disposal." |

### Assessment
Gemini and Perplexity give a clear "no disposal" answer. ChatGPT sources are more cautious, flagging the title-transfer issue as a genuine risk. The practical impact for your case is limited since the deposits were made while Swedish resident anyway — but if you were to use the custody vs lending distinction in a Polish context, Gemini's view is more favorable.

### Swedish angle (Perplexity adds unique value)
Perplexity highlights that **Skatteverket explicitly treats Celsius lending deposits as disposals** — the depositor is deemed to have sold the crypto and holds a claim instead. This means:
- You may have had a Swedish tax reporting obligation at the deposit date
- The Celsius "claim" is a separate financial instrument under Swedish law
- The claim loss can only be deducted in Sweden when the claim is formally disposed of (requires final bankruptcy, not Chapter 11)
- Swedish crypto losses cannot be carried forward to future years (70% same-year offset only)

---

## Practical Guidance for Our Calculator / Cost Pool

### What the cost pool should show

For Celsius/BlockFi assets:
1. The **original fiat purchase costs** (from when you bought BTC/DOT) remain in the Polish cost pool as documented acquisition costs
2. These costs were incurred while Swedish resident, so they enter the Polish system as pre-residency costs (per WSA 2024 ruling) — provided they weren't already deducted in Sweden
3. The coins themselves should be in a **frozen/claim bucket** — not in active inventory, not booked as sold

### When distributions arrive

| Event | In the calculator |
|---|---|
| Receive BTC/ETH back from bankruptcy | Transfer from "claim" bucket to active inventory. NOT a revenue event. Original cost basis carries through. |
| Receive USD from bankruptcy | Record as crypto disposal revenue in the year received. Offset by costs from the pool. |
| Receive equity (Ionic Digital shares) | Record as crypto disposal revenue at FMV. Creates a new cost basis for the shares. |
| Unrecovered remainder (final) | Non-taxable write-off in inventory. Cost stays in the pool. |

### Gemini's Celsius distribution breakdown

| Component | Allocation | Tax Status |
|---|---|---|
| Liquid crypto (BTC) | 28.95% | Tax neutral at receipt |
| Liquid crypto (ETH) | 28.95% | Tax neutral at receipt |
| Corporate equity (Ionic Digital) | 14.90% | **Taxable** — disposal for property rights |
| Fiat recovery (USD) | 6.40% | **Taxable** — fiat realization |

---

## Action Items

### 1. Check if you received any Celsius/BlockFi distributions
If you were a creditor and received distributions in 2024 or later:
- Crypto distributions: not immediately taxable, but track them
- Fiat distributions: taxable revenue in the year received
- Equity distributions: taxable at FMV on receipt date

### 2. Keep original purchase costs in the cost pool
Your BTC/DOT purchase costs from 2020-2022 remain valid for Polish PIT-38, provided they weren't deducted in Swedish K4. These are part of your pre-residency cost base.

### 3. Do NOT book any "loss" or "sale at 0" in the calculator
The calculator should treat Celsius/BlockFi assets as frozen/non-spendable — not as disposed of. The cost stays in the pool.

### 4. Consider Swedish filing obligations
Perplexity raises an important point: if Skatteverket treats the Celsius deposit as a disposal, you may have had a Swedish K4 reporting obligation for the year of deposit. Worth consulting a Swedish tax specialist if amounts are material.

### 5. For material amounts, get a KIS interpretacja indywidualna
Two specific questions worth ruling on:
- Was the Celsius Earn deposit itself a taxable disposal under Polish law?
- How should the Celsius bankruptcy distribution (mix of crypto + fiat + equity) be classified?

### 6. Document everything
Keep: original purchase records, blockchain tx hashes to Celsius/BlockFi addresses, platform statements before freeze, proof of claim, all distribution notices, and any court orders. KAS accepts exchange reports + bank confirmations as tax evidence.

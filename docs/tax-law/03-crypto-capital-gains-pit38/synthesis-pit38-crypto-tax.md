# Synthesis: Crypto Capital Gains and PIT-38 in Poland

Sources: ChatGPT 5.4 Pro, ChatGPT Deep Research, Perplexity, Gemini 3.1 Deep Research

---

## Full Consensus (All 4 agree)

### Core framework
- **19% flat tax** on "odplatne zbycie walut wirtualnych" (paid disposal of virtual currencies) under Art. 30b ust. 1a
- Reported on **PIT-38, Section E** (separate from stocks/securities in Section C)
- Filing deadline: **15 Feb - 30 April** of the following year
- Crypto income is **completely segregated** from other income — cannot offset stocks, business income, or anything else

### Taxable events
- Crypto -> fiat (EUR, PLN): **taxable**
- USDC -> EUR via Binance Convert: **taxable**
- Crypto -> goods/services: **taxable**
- Crypto -> settle liabilities: **taxable**

### Non-taxable events
- Crypto -> crypto swaps (BTC->ETH, USDT->USDC): **NOT taxable** (since 2019 reform)
- Own wallet transfers (Binance -> MetaMask): **NOT taxable**
- Buying crypto with fiat: **NOT taxable** (creates cost only)
- Holding crypto: **NOT taxable**
- Gifting crypto: **NOT taxable** for donor (gift tax may apply to recipient)

### Stablecoins = virtual currency
- USDC, USDT remain classified as "waluta wirtualna" under Polish law
- KIS confirmed this post-MiCA (early 2026 interpretation)
- Swapping BTC -> USDC = non-taxable crypto-to-crypto
- Selling USDC -> EUR = taxable disposal

### NBP exchange rate rules
- Revenue: NBP mid-rate from **last business day BEFORE** the revenue date (Art. 11a ust. 1)
- Costs: NBP mid-rate from **last business day BEFORE** the cost date (Art. 11a ust. 2)
- Applies to all EUR/USD amounts on both sides

### PIT-38 reports aggregated totals only
- Total annual revenue from all taxable disposals
- Total costs incurred in the year
- Prior-year carried costs
- Resulting income (or excess costs to carry forward)
- **No individual transaction listing** on the form

### Cost carry-forward (not "loss")
- If costs > revenue: income = 0, excess costs carry forward to next year
- Polish crypto has **no traditional "loss"** (strata) — only undeducted costs
- Carry-forward is **unlimited in time** (no 5-year cap, no 50% annual limit)
- **Must file PIT-38 even with zero revenue** to register costs for carry-forward

### Pre-residency costs (Sweden -> Poland)
- Original acquisition costs from Sweden **ARE deductible** in Polish PIT-38
- Use **original purchase price** converted to PLN at NBP rate for the original date
- **No step-up** to market value on migration
- Condition: costs were not already deducted in Sweden
- KIS interpretation and WSA Warsaw ruling (III SA/Wa 1290/24, Aug 2024) both support this

### Platform collapses (Celsius, BlockFi, Terra)
- Collapse itself is **NOT** a taxable event (no "odplatne zbycie" occurred)
- **Cannot claim a deductible loss** at the time of collapse
- BUT: original acquisition costs **remain in the cost pool** and carry forward
- If partial recovery received (bankruptcy distribution), that IS taxable revenue
- To crystallize a loss on worthless tokens, sell them for a nominal amount

### Deductible costs

| Cost | Deductible? |
|---|---|
| Purchase price (fiat -> crypto) | Yes |
| Exchange trading fees (buy/sell) | Yes |
| Withdrawal fees tied to disposal | Likely yes (cautious) |
| Network gas fees tied to disposal | Likely yes (cautious) |
| Crypto-to-crypto swap fees | **No** (Art. 23 ust. 1 pkt 38d) |
| Mining equipment / electricity | **No** |
| Loan interest for crypto purchases | **No** |
| Hardware wallet costs | **No** |

### Documentation
- No formal "ewidencja walut wirtualnych" template required
- Must keep evidence to substantiate costs and revenue
- Exchange CSVs + bank statements + wallet tx hashes
- Retain for at least 5 years (statute of limitations)
- DAC8 (from 2026): Binance/Kraken will report to Polish authorities

---

## The Big Disagreement: FIFO

This is the most consequential finding for our tax calculator.

### Poland does NOT use FIFO for crypto

| Source | Position |
|---|---|
| **ChatGPT 5.4 Pro** | "I would NOT confirm FIFO for Polish crypto PIT." Art. 30b ust. 7-7a (FIFO) does NOT apply to Art. 30b ust. 1a (crypto). Crypto uses the annual aggregate formula. |
| **ChatGPT Deep Research** | "Poland does not require FIFO" — the model is pooled annual costs and revenues. KIS interpretation confirms no need to match specific costs to specific revenues. |
| **Perplexity** | "No legal basis for applying FIFO" — cites KIS official guidance explicitly stating FIFO doesn't apply. Uses "annual cost pool approach." Costs carry forward without per-lot matching. |
| **Gemini** | "The FIFO Myth" — calls it a "widespread misconception." KAS guidelines explicitly clarify no FIFO for individual crypto investors. Uses "global cash-flow pooling mechanism." |

**All 4 sources unanimously agree: Poland does NOT use FIFO for crypto.** Instead it uses an **annual cost pooling** approach:

1. Sum ALL fiat spent acquiring crypto during the year = total costs
2. Sum ALL fiat received from selling crypto during the year = total revenue
3. Revenue - (costs + carry-forward) = income (or 0 if negative, with excess carrying forward)

**You never need to identify which specific coins were sold.** You only need total fiat in (purchases) and total fiat out (sales) for the year.

### Impact on our tax calculator

Our FIFO-based calculator (`src/tax_calc/fifo.py`) produces per-transaction gains/losses by matching specific lots to sales. **This is useful for economic analysis but is NOT how Polish PIT-38 works.**

For the actual PIT-38 filing, we need a simpler calculation:
- Poz. 34/36: Sum of all crypto->fiat revenue (in PLN)
- Poz. 35/37: Sum of all fiat->crypto costs (in PLN) + salary USDC at receipt value
- Poz. 36/38: Prior year carry-forward
- Result: annual aggregate, no per-transaction matching needed

---

## Other Disagreement: Staking/Airdrop Taxation

Active dispute between tax authority (KIS) and courts:

| | KIS Position | Court Position |
|---|---|---|
| **When taxed** | At receipt (PIT-36, progressive 12%/32%) | At disposal only (PIT-38, 19%) |
| **Cost basis** | Market value at receipt | Zero |
| **Form** | PIT-36 at receipt + PIT-38 at disposal | PIT-38 only at disposal |
| **Risk** | Low (follows authority) | Medium (requires court defense if challenged) |

Key rulings cited:
- **KIS**: 0112-KDIL2-2.4011.146.2024.2.IM, 0112-KDIL2-2.4011.234.2025.3.AA — staking = property rights income at receipt
- **Courts**: WSA Wroclaw I SA/Wr 413/23 (Dec 2023), WSA Poznan I SA/Po 434/24 (Apr 2024), NSA II FSK 1688/19 (Mar 2022) — staking taxed only at disposal

**Practical impact for you**: Your staking rewards (DOT, ETH, SOL on Kraken) are small relative to the salary USDC. Under either approach, the amounts are modest. The conservative KIS approach (tax at receipt) gives you a cost basis for later disposal; the court approach gives zero cost basis but no tax at receipt. For small amounts, following KIS is simpler.

---

## Minor Disagreements

### Withdrawal/gas fees
- All sources say exchange trading fees are deductible
- Withdrawal and gas fees: "likely yes" but cautious, must be directly tied to taxable disposal
- Crypto-to-crypto swap fees: unanimously **not deductible** (Art. 23 ust. 1 pkt 38d)

### Whether PIT/ZG needed with PIT-38
- ChatGPT 5.4 Pro: PIT/ZG needed if foreign tax was paid on crypto
- Others: mention it only in the context of foreign tax credits
- Since no foreign crypto tax was paid, PIT/ZG likely not needed specifically for PIT-38

---

## Action Items for Us

### 1. Rethink the calculator's output for Polish filing

Our FIFO calculator is useful for tracking economic gains, but for the actual PIT-38 we need a **cost pool report**:
- Total PLN revenue from all crypto->fiat events in the year
- Total PLN costs from all crypto acquisitions (purchases + salary USDC) in the year
- Carry-forward from prior year
- Net: income or excess costs

Consider adding a `--poland-pit38` output mode that produces these aggregated numbers instead of per-transaction FIFO gains.

### 2. Pre-residency costs from Sweden (2020-2022)

We should calculate the total PLN value of all crypto purchased with fiat while in Sweden. This amount enters the cost pool for the first Polish PIT-38 (2023) as prior-year costs. **This is free money** — it increases the cost pool and reduces any taxable income.

To do this:
- Extract all fiat->crypto purchases from Binance/Kraken for 2020-2022
- Convert each to PLN using NBP rate from day before purchase
- Sum = pre-residency cost pool

### 3. File PIT-38 even for years with no sales

If crypto was purchased in a year but not sold, PIT-38 should still be filed to register the costs. This preserves the carry-forward chain.

### 4. Staking rewards: pick an approach

For your DOT/ETH/SOL staking on Kraken, decide:
- **Conservative (KIS)**: declare at receipt on PIT-36, use as cost basis on PIT-38 later
- **Taxpayer-friendly (courts)**: ignore until disposal, accept zero cost basis

Given the amounts are small and you already have massive cost carry-forward from salary USDC, the choice has minimal tax impact. The conservative approach avoids any dispute.

### 5. Celsius/BlockFi costs

Your original acquisition costs for crypto deposited to Celsius/BlockFi remain in the cost pool. Document the original purchases and include those costs — they carry forward indefinitely and shield future gains.

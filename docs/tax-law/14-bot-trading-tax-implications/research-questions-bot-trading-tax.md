# Research: Tax Implications of Automated Crypto Bot Trading (Liquidations, DEX Arbitrage) Under Polish JDG

## Context

A Polish tax resident operates a JDG (sole proprietorship) under ryczalt 12% for software development (PKD 62.01.B). Separately, the developer is building and running automated trading bots that perform:

1. **Lending market liquidations** (e.g., Aave, Compound, Morpho, Ironclad-style protocols): The bot monitors under-collateralized positions on DeFi lending platforms and executes liquidation calls, earning a liquidation bonus (typically 5-10% of the liquidated collateral). This involves:
   - Receiving a liquidation bonus in crypto (e.g., ETH, WBTC)
   - Sometimes using flash loans to fund the liquidation
   - Transactions can be very small (e.g., $0.50 profit) or significant ($500+)
   - The bot pays gas fees on each transaction

2. **DEX-to-DEX arbitrage**: The bot detects price discrepancies between decentralized exchanges (e.g., Uniswap on Ethereum vs SushiSwap on Arbitrum, or between different AMM pools) and executes atomic or cross-chain arbitrage trades. This involves:
   - Buying low on one DEX, selling high on another
   - Often using flash loans or flash swaps
   - All transactions are crypto-to-crypto (no fiat involved in the trade itself)
   - Very high frequency: potentially hundreds or thousands of transactions per day
   - Gas fees on every transaction
   - Sometimes MEV (Maximal Extractable Value) strategies

3. **Multi-chain operation**: The bots may run on multiple chains (Ethereum, Arbitrum, Base, Mode, Polygon, etc.) and the developer may host the bot infrastructure in different countries (e.g., a server in Germany, or using cloud infrastructure in Japan/US).

The developer's existing tax research has established:
- Crypto-to-crypto swaps are non-taxable under Polish PIT (Art. 17 ust. 1f)
- Only crypto-to-fiat conversion triggers PIT-38 tax
- Art. 17 ust. 1g keeps crypto disposal in PIT-38 even within business activity
- The annual cost pool method is used (not FIFO)
- Polish tax residency means worldwide income is taxed in Poland

## Critical Questions

### Classification: Business Income or Capital Gains?

1. Under Polish law, does running automated liquidation/arbitrage bots constitute:
   a) Personal crypto trading (PIT-38 at 19%)?
   b) Non-agricultural business activity (dzialalnosc gospodarcza) that could be reported as JDG business income?
   c) A regulated crypto-service activity under AML Art. 2 ust. 1 pkt 12 (which IS treated as business income)?

2. Art. 17 ust. 1g says crypto disposal stays in PIT-38 even within business activity — EXCEPT for activities under AML Art. 2 ust. 1 pkt 12. Does running liquidation bots or arbitrage bots fall under any of the AML-defined crypto service activities (exchange, intermediation, wallet/account services)?

3. If the bot activity is classified as business (dzialalnosc gospodarcza), can it be registered under the existing JDG? What PKD code would apply? Would this affect the ryczalt 12% rate for the software development part?

4. If the bot profits stay in PIT-38 (capital gains at 19%), can the bot's operational costs (server hosting, gas fees, flash loan fees) be deducted? Or are gas fees on crypto-to-crypto transactions non-deductible under Art. 23 ust. 1 pkt 38d?

### The Crypto-to-Crypto Problem

5. If ALL bot transactions are crypto-to-crypto (e.g., buy ETH on DEX A, sell ETH on DEX B for USDC), does this mean:
   - No taxable event occurs at ANY point during the bot's operation?
   - Tax only occurs when the accumulated profits are eventually converted to fiat (EUR/PLN)?
   - The cost pool includes all fiat originally used to fund the bot wallet?

6. For liquidation bonuses: the bot receives crypto (e.g., ETH) as a bonus for performing a liquidation. Is this:
   a) A "free" receipt like an airdrop/staking reward (disputed: KIS says tax at receipt, courts say tax at disposal)?
   b) Income from a service performed (liquidation service)?
   c) A crypto acquisition with zero cost basis?

7. Flash loans: the bot borrows crypto, uses it, and repays in the same transaction (atomic). Are flash loan fees deductible costs? Since the entire operation is crypto-to-crypto, are the fees non-deductible under Art. 23 ust. 1 pkt 38d?

### Volume and Reporting

8. If the bot executes 1,000 transactions per day (365,000/year), how is this reported on PIT-38? The form only requires annual aggregates — but what documentation must be maintained?

9. Is there a practical threshold where high-frequency bot trading gets reclassified from personal capital gains (PIT-38) to business activity? Polish law defines business as "gainful activity carried out in an organized and continuous way" — automated bots running 24/7 seem to meet this definition.

10. If the activity IS reclassified as business, and it falls under the AML Art. 2 ust. 1 pkt 12 exception, what changes:
    - Tax form (PIT-36/PIT-36L instead of PIT-38)?
    - Tax rate (progressive 12%/32% or linear 19% instead of capital gains 19%)?
    - Deductible costs (server costs, gas, flash loan fees become deductible)?
    - ZUS obligations?
    - AML registration requirements?

### Multi-Jurisdiction: Bot Location

11. If the bot runs on a server in Germany (e.g., Hetzner data center), does Germany have any tax claim on the bot's profits? Or does Polish tax residency mean all worldwide income (including bot income) is taxed exclusively in Poland?

12. If the bot runs on cloud infrastructure in Japan (e.g., AWS Tokyo region), does Japan have any claim?

13. Does the physical location of the server matter at all for Polish tax purposes? Or is the tax obligation determined solely by the developer's tax residency?

14. Under the Poland-Germany DTT and Poland-Japan DTT, how are "business profits" from automated trading allocated? Is there a PE (permanent establishment) risk from having a server in another country?

15. For DeFi bots that interact with protocols "located" on specific blockchains — does the "location" of the smart contract matter for tax purposes? (E.g., Uniswap is "on Ethereum" but has no physical location.)

### Gas Fees and Operational Costs

16. The bot pays gas fees (in ETH or the native token) on every transaction. Under Polish crypto tax rules:
    - Are gas fees on crypto-to-crypto arbitrage transactions deductible? (Art. 23 ust. 1 pkt 38d excludes crypto-to-crypto swap costs)
    - Are gas fees on liquidation transactions deductible? (These could be "costs of disposal" if the liquidation itself is a disposal)
    - What about gas fees for failed transactions (the bot paid gas but the transaction reverted)?

17. Server hosting costs (e.g., Hetzner VPS at 50 EUR/month): Are these deductible under PIT-38 crypto capital gains? (Likely not — indirect costs similar to mining equipment.) Could they be deductible under JDG business expenses if the bot activity is classified as business?

18. Can the developer deduct the cost of developing the bot software? (E.g., time spent coding, which is "performed within the JDG".)

### Practical Reporting Example

19. Walk through a concrete example:
    - Bot starts with 10 ETH (purchased for 25,000 EUR)
    - Over 1 year, performs 50,000 arbitrage trades (all crypto-to-crypto)
    - Net result: bot now holds 12 ETH + 500 USDC
    - Developer converts 500 USDC to EUR (the "profit taking")
    - What goes on PIT-38? What goes on PIT-28? What documentation is needed?

20. For the liquidation scenario:
    - Bot liquidates a position and receives 0.1 ETH bonus
    - This ETH is later swapped to USDC (crypto-to-crypto, non-taxable)
    - USDC is later converted to EUR on Kraken
    - What is the cost basis of the 0.1 ETH? What is the revenue on the EUR conversion?

### Are There KIS Interpretations on Bot Trading?

21. Has KIS issued any interpretacje indywidualne specifically about:
    - Automated crypto trading bots?
    - DeFi liquidation profits?
    - DEX arbitrage?
    - High-frequency crypto trading by individuals?
    - MEV/flash loan strategies?

22. Are there any Polish court rulings (WSA/NSA) that address automated or algorithmic crypto trading?

## Desired Output

A comprehensive analysis covering:
1. Classification of bot trading under Polish tax law (PIT-38 vs business income)
2. The crypto-to-crypto neutrality question for high-frequency arbitrage
3. Deductibility of gas fees and operational costs
4. Multi-jurisdiction analysis (server location irrelevance or PE risk)
5. Practical reporting methodology for high-volume transactions
6. Risk assessment for each classification approach
7. Specific legal references and KIS interpretations if available

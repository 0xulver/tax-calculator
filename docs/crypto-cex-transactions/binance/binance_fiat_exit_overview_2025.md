# 2025 CEX Fiat Exit Overview

This note summarizes the `2025` CEX transactions that look like exits into fiat.

For the purpose of this overview, the important event is:
- a trade where `EUR` was received.

That is the event I am treating as the main taxable event from a Polish perspective.

`Fiat Withdraw` or `withdrawal` rows are included only as context, to show when the EUR later left the exchange.

Sources:
- `binance_transactions_2025.csv`
- `kraken_stocks_etfs_ledgers_2024-12-31-2025-12-31.csv`

## High-Level Summary

- Total fiat-exit trade events: `15`
- Binance fiat-exit trade events: `13`
- Kraken fiat-exit trade events: `2`
- Gross EUR received from fiat-exit trades: `63,980.97971139`
- EUR trading fees on those trades: `65.440255`
- Net EUR after trading fees: `63,915.53945639`
- Follow-up EUR withdrawal rows recorded: `13`
- Total EUR withdrawn after those trades: `63,907.78`

Assets sold into EUR:
- `USDC`: `58,511.97727100`
- `USDT`: `11,999.93409000`
- `DOT`: `2.1009309200`

Main observations:
- Most fiat-exit events happened on Binance and were stablecoin-to-EUR conversions.
- Kraken adds one larger `USDC -> EUR` fiat-exit in January and one small `DOT -> EUR` fiat-exit in August.
- The recorded EUR withdrawals almost fully match the net EUR received from fiat-exit trades.
- Small differences are expected because of rounding, leftover EUR dust, and one tiny Binance conversion that did not have its own separate withdrawal row.

## Monthly Summary

| Month | Net EUR from fiat-exit trades | EUR withdrawn |
| --- | ---: | ---: |
| 2025-01 | 4,846.41 | 4,845.41 |
| 2025-02 | 5,752.53 | 5,752.52 |
| 2025-03 | 16,712.75 | 16,712.75 |
| 2025-04 | 25,992.88 | 25,992.89 |
| 2025-05 | 7,979.31 | 7,979.31 |
| 2025-06 | 2,624.90 | 2,624.90 |
| 2025-08 | 6.75 | 0.00 |

## Fiat-Exit Trade Events

| Exchange | Time | Asset sold | EUR gross | EUR fee | EUR net | Follow-up EUR withdraw |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| Kraken | 2025-01-16 08:48:23 | USDC 4000.00000100 | 3883.60 | 7.7672 | 3875.8328 | 3874.83 |
| Binance | 2025-01-16 09:41:12 | USDC 1000.64500000 | 971.50 | 0.922925 | 970.577075 | 970.58 |
| Binance | 2025-02-04 11:26:36 | USDC 2998.14111000 | 2901.20 | 2.756140 | 2898.443860 | 2898.54 |
| Binance | 2025-02-04 11:27:13 | USDC 0.10334000 | 0.09921139 | 0.000000 | 0.09921139 | - |
| Binance | 2025-02-14 20:18:49 | USDC 3000.20099000 | 2856.70 | 2.713865 | 2853.986135 | 2853.98 |
| Binance | 2025-03-04 15:37:47 | USDT 3999.96099000 | 3799.40 | 3.799400 | 3795.600600 | 3795.61 |
| Binance | 2025-03-20 22:42:23 | USDC 6000.16896000 | 5529.60 | 5.253120 | 5524.346880 | 5524.34 |
| Binance | 2025-03-25 14:03:08 | USDT 1999.94160000 | 1847.70 | 1.847700 | 1845.852300 | 1845.85 |
| Binance | 2025-03-27 16:38:08 | USDT 6000.03150000 | 5552.50 | 5.552500 | 5546.947500 | 5546.95 |
| Binance | 2025-04-11 14:32:10 | USDC 6321.96090000 | 5548.50 | 5.271075 | 5543.228925 | 5543.23 |
| Binance | 2025-04-23 20:29:57 | USDC 23190.65552000 | 20469.10 | 19.445645 | 20449.654355 | 20449.66 |
| Binance | 2025-05-06 10:58:34 | USDC 2999.92400000 | 2654.80 | 2.522060 | 2652.277940 | 2652.27 |
| Binance | 2025-05-19 15:54:42 | USDC 6000.21213000 | 5332.10 | 5.065495 | 5327.034505 | 5327.04 |
| Binance | 2025-06-05 08:42:22 | USDC 2999.96532000 | 2627.40 | 2.496030 | 2624.903970 | 2624.90 |
| Kraken | 2025-08-07 19:43:53 | DOT 2.1009309200 | 6.7805 | 0.0271 | 6.7534 | - |

## Follow-Up EUR Withdrawal Rows

These are not the main taxable event in this note. They are included so you can see when the EUR later left the exchange.

| Exchange | Time | EUR withdrawn |
| --- | --- | ---: |
| Kraken | 2025-01-16 08:50:09 | 3874.83 |
| Binance | 2025-01-16 09:42:49 | 970.58 |
| Binance | 2025-02-04 11:49:55 | 2898.54 |
| Binance | 2025-02-14 20:54:43 | 2853.98 |
| Binance | 2025-03-04 15:39:56 | 3795.61 |
| Binance | 2025-03-20 22:45:44 | 5524.34 |
| Binance | 2025-03-25 14:27:07 | 1845.85 |
| Binance | 2025-03-27 16:40:58 | 5546.95 |
| Binance | 2025-04-11 14:33:50 | 5543.23 |
| Binance | 2025-04-23 20:31:35 | 20449.66 |
| Binance | 2025-05-06 11:00:30 | 2652.27 |
| Binance | 2025-05-19 15:56:11 | 5327.04 |
| Binance | 2025-06-05 08:43:36 | 2624.90 |

## Interpretation

At a high level, your `2025` fiat-exit pattern looks straightforward:
- on Binance, most taxable fiat-exit events were stablecoin-to-EUR conversions followed by EUR withdrawals;
- on Kraken, there was one larger `USDC -> EUR` fiat-exit in January and one small `DOT -> EUR` fiat-exit in August;
- the withdrawal data broadly lines up with the EUR received from those trades.

This is much easier to read than the raw exchange ledgers because each multi-line trade has been collapsed into one fiat-exit event.

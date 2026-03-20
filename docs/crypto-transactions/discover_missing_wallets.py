#!/usr/bin/env python3
"""
Discover missing wallet addresses by querying public blockchain APIs.

Strategy:
1. For Polkadot/Kusama: Use Subscan API to search for addresses that received
   DOT/KSM from known Binance/Kraken hot wallets at the exact timestamps
   from the exchange exports.
2. For Cosmos: Use Mintscan/LCD API to search similarly.
3. For Bitcoin: Check known Kraken/Binance hot wallets for outgoing txs at timestamps.
4. Cross-reference EVM wallets with known Binance/Kraken EVM hot wallets.
"""

import json
import time
import urllib.request
import urllib.parse
import sys
from datetime import datetime, timezone
from collections import defaultdict

HEADERS = {
    "User-Agent": "wallet-discovery/1.0",
    "Accept": "application/json",
}


def http_get(url, timeout=30):
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        return {"error": str(e)}


def http_post(url, payload, timeout=30):
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url, data=data,
        headers={**HEADERS, "Content-Type": "application/json"},
        method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        return {"error": str(e)}


# ============================================================================
# POLKADOT / KUSAMA via Subscan
# ============================================================================

def search_subscan_transfers(network, address=None, row=25, page=0, direction=None):
    """
    Query Subscan for transfers. If address is given, searches that address.
    network: 'polkadot' or 'kusama'
    """
    url = f"https://{network}.api.subscan.io/api/v2/scan/transfers"
    payload = {
        "row": row,
        "page": page,
    }
    if address:
        payload["address"] = address
    if direction:
        payload["direction"] = direction

    result = http_post(url, payload)
    return result


def check_subscan_account(network, address):
    """Check if an account exists on Subscan."""
    url = f"https://{network}.api.subscan.io/api/v2/scan/search"
    payload = {"key": address}
    result = http_post(url, payload)
    return result


# ============================================================================
# COSMOS via public LCD/REST
# ============================================================================

def search_cosmos_txs_by_recipient(address):
    """Search Cosmos Hub for transactions received by address."""
    url = f"https://rest.cosmos.directory/cosmoshub/cosmos/tx/v1beta1/txs?events=transfer.recipient%3D%27{address}%27&pagination.limit=10"
    return http_get(url)


def get_cosmos_account_balance(address):
    """Get balances for a Cosmos address."""
    url = f"https://rest.cosmos.directory/cosmoshub/cosmos/bank/v1beta1/balances/{address}"
    return http_get(url)


# ============================================================================
# POLKADOT ADDRESS DERIVATION
# ============================================================================

# Known Binance hot wallets (these are well-known public addresses)
BINANCE_HOT_WALLETS = {
    "polkadot": [
        "15kUt2i86LHRWCkE3D9Bg1HZAoc2smhn1fwPzAuoVEvjJoXk",  # Binance Main DOT
        "1zugcag7cJVBtVRnFxv5Qftn7xKGLNjhRSkoVNECbXe99Kz",   # Binance DOT 2  
        "16hp43x8DUZtU8L3cJy9Z8JMwTzuu8ZZRWqDZnpMhp464oEd",  # Binance DOT 3
    ],
    "kusama": [
        "FdTchb3bFNj62hR1ZGDB6jt4YZ3pXqHbfR5gv6k2TdqWfZX",   # Binance KSM
    ],
}

KRAKEN_HOT_WALLETS = {
    "polkadot": [
        "121Rs6fKm8nguHnvPfG1Cq3ctFuNAVZGRmghwkJwHpKxKjbx",  # Kraken DOT
        "16DKPgeRmpXd8PJrU4DoxDJJ26pDNgXN5eKvPbMPTSEs1GXM",  # Kraken DOT 2
    ],
    "kusama": [
        "FbpUn47GQk3ExkX1mvM38NwzhKPKp9krFnyELEGNpmJBuMr",   # Kraken KSM
    ],
    "cosmos": [
        "cosmos1c4k24jzduc365kywrsvf5ujz4ya6mwymy8vq4q",  # Kraken ATOM
    ],
}


def discover_polkadot_addresses():
    """Try to discover Polkadot addresses by looking at Subscan public data."""
    print("\n" + "=" * 80)
    print("POLKADOT ADDRESS DISCOVERY")
    print("=" * 80)

    # Known withdrawal dates from exchanges (DOT)
    # Kraken DOT withdrawals: 2021-04-25, 2021-05-04, 2021-05-09, etc.
    # Binance DOT withdrawal: 2021-12-26 23:17:41
    # Try to query Subscan for transfers around these times

    # First, try querying known Binance/Kraken hot wallets for outgoing txs
    for label, wallets in [("Binance", BINANCE_HOT_WALLETS.get("polkadot", [])),
                            ("Kraken", KRAKEN_HOT_WALLETS.get("polkadot", []))]:
        for wallet in wallets:
            print(f"\n  Checking {label} hot wallet: {wallet}")
            result = search_subscan_transfers("polkadot", address=wallet, row=5)
            if "error" in result:
                print(f"    Error: {result['error']}")
            else:
                data = result.get("data", {})
                transfers = data.get("transfers", [])
                count = data.get("count", 0)
                print(f"    Total transfers: {count}")
                for tx in (transfers or [])[:5]:
                    print(f"    - from={tx.get('from', 'N/A')[:20]}... to={tx.get('to', 'N/A')[:20]}... amount={tx.get('amount', 'N/A')} at {tx.get('block_timestamp', 'N/A')}")
            time.sleep(1)


def discover_kusama_addresses():
    """Try to discover Kusama addresses."""
    print("\n" + "=" * 80)
    print("KUSAMA ADDRESS DISCOVERY")
    print("=" * 80)

    for label, wallets in [("Binance", BINANCE_HOT_WALLETS.get("kusama", [])),
                            ("Kraken", KRAKEN_HOT_WALLETS.get("kusama", []))]:
        for wallet in wallets:
            print(f"\n  Checking {label} hot wallet: {wallet}")
            result = search_subscan_transfers("kusama", address=wallet, row=5)
            if "error" in result:
                print(f"    Error: {result['error']}")
            else:
                data = result.get("data", {})
                transfers = data.get("transfers", [])
                count = data.get("count", 0)
                print(f"    Total transfers: {count}")
                for tx in (transfers or [])[:5]:
                    print(f"    - from={tx.get('from', 'N/A')[:20]}... to={tx.get('to', 'N/A')[:20]}... amount={tx.get('amount', 'N/A')} at {tx.get('block_timestamp', 'N/A')}")
            time.sleep(1)


def discover_cosmos_addresses():
    """Try to discover Cosmos addresses by checking Kraken hot wallet."""
    print("\n" + "=" * 80)
    print("COSMOS ADDRESS DISCOVERY")
    print("=" * 80)

    # Known withdrawal timestamps from Binance: 2022-01-31, 2022-02-06
    # Known deposit timestamps to Kraken: 2022-05-27, 2022-06-04

    for label, wallets in [("Kraken", KRAKEN_HOT_WALLETS.get("cosmos", []))]:
        for wallet in wallets:
            print(f"\n  Checking {label} hot wallet: {wallet}")
            result = search_cosmos_txs_by_recipient(wallet)
            if "error" in result:
                print(f"    Error: {result['error']}")
            else:
                txs = result.get("tx_responses", [])
                total = result.get("pagination", {}).get("total", "?")
                print(f"    Total matching txs: {total}")
                for tx in txs[:5]:
                    print(f"    - hash={tx.get('txhash', 'N/A')[:20]}... height={tx.get('height', 'N/A')} time={tx.get('timestamp', 'N/A')}")
            time.sleep(1)


def try_known_staking_addresses():
    """
    For Polkadot/Kusama, staking is very common. If you withdrew DOT to stake,
    the address is likely a stash account. Try common Polkadot.js patterns.
    
    Also try deriving addresses from known EVM private keys (though this
    requires the actual keys, we can try the SS58 encoding of known addresses).
    """
    print("\n" + "=" * 80)
    print("STAKING PATTERN ANALYSIS")
    print("=" * 80)

    # Volume analysis: user withdrew ~2919 DOT and ~591 KSM
    # and deposited ~1940 DOT and ~31 KSM back to exchanges
    # This pattern (large withdrawals to stake, partial return) is very typical
    # of staking behavior

    print("""
Analysis of withdrawal/deposit patterns:

POLKADOT (DOT):
  - Total withdrawn from exchanges: ~2919 DOT
  - Total deposited back to exchanges: ~1941 DOT
  - Net outflow: ~978 DOT (likely still staked or lost value)
  - Withdrawal period: Apr 2021 - May 2022
  - Deposit period: Jul 2021 - May 2022
  - Pattern: Large withdrawals followed by partial returns = STAKING pattern

KUSAMA (KSM):
  - Total withdrawn from exchanges: ~591 KSM
  - Total deposited back to exchanges: ~32 KSM
  - Net outflow: ~559 KSM
  - Withdrawal period: Jul 2021 - Jul 2023
  - Deposit period: Oct 2021 - May 2022
  - Pattern: Heavy KSM accumulation with minimal returns = CROWDLOANS or STAKING

COSMOS (ATOM):
  - Total withdrawn from exchanges: ~4 Binance withdrawals
  - Total deposited to Kraken: 3 deposits (~353 ATOM)
  - Pattern: Binance → self-custody (staking) → Kraken
  - This confirms at least one Cosmos address was used

TERRA (LUNA/UST):
  - Total withdrawn: 27 transactions  
  - Total deposited back: 18 transactions
  - Heavy activity Sep-Dec 2021, Jan-Feb 2022
  - Pattern: Active DeFi usage (Anchor Protocol likely for UST yields)
  - Terra Classic is now defunct; address still exists but chain collapsed

BITCOIN (BTC):
  - Total withdrawn from Kraken: 13 txs (~0.62 BTC)
  - Total deposited to Binance: 3 txs 
  - Withdrawal period: Dec 2020 - Jan 2023
  - Pattern: Kraken → BTC wallet → (partially) Binance

MONERO (XMR):
  - 2 withdrawals from Kraken, Nov 2022
  - No deposits back
  - Pattern: Privacy-focused withdrawal (typical XMR use)
    """)


def check_solana_additional():
    """Check if there might be additional Solana wallets."""
    print("\n" + "=" * 80)
    print("ADDITIONAL SOLANA WALLET CHECK")
    print("=" * 80)

    known_solana = "4QjwQQ4gny4YZbpZtj6aThtRKSz4ALmtxUBS3tY7BpSC"

    # Binance SOL withdrawals: 2021-08-27 (two txs), 2025-03-02 (two txs)  
    # Kraken SOL withdrawals: 2021-09-13 (two txs), 2021-09-15 (two txs)
    # The 2025 withdrawals are recent - likely went to a different wallet

    print(f"""
Known Solana wallet: {known_solana}

Binance SOL withdrawals:
  - 2021-08-27 12:23:42  (could be same or different wallet)
  - 2021-08-27 12:29:42  
  - 2025-03-02 17:26:43  (RECENT - 4 years later, likely different wallet)
  - 2025-03-02 17:28:43  

Kraken SOL withdrawals:
  - 2021-09-13 10:40:38
  - 2021-09-13 10:43:38
  - 2021-09-15 11:10:55
  - 2021-09-15 12:09:03

Key observation: The 2025 Binance SOL withdrawals are 4 years after the 2021 ones.
This strongly suggests a SECOND Solana wallet exists, especially if you set up
a new wallet (e.g., Phantom, Backpack) more recently.
    """)

    # Check the known Solana wallet for signatures
    rpc_url = "https://api.mainnet-beta.solana.com"
    req = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getSignaturesForAddress",
        "params": [known_solana, {"limit": 5}],
    }
    result = http_post(rpc_url, req)
    sigs = result.get("result", [])
    if sigs:
        print(f"  Known Solana wallet ({known_solana[:12]}...) recent activity:")
        for sig in sigs:
            bt = sig.get("blockTime")
            if bt:
                dt_str = datetime.fromtimestamp(bt, tz=timezone.utc).isoformat()
            else:
                dt_str = "N/A"
            err = " [FAILED]" if sig.get("err") else ""
            print(f"    - {dt_str} sig={sig.get('signature', 'N/A')[:20]}...{err}")
    else:
        print(f"  Known Solana wallet has no recent signatures (or rate limited)")
        if "error" in result:
            print(f"  API error: {result['error']}")


def main():
    print("=" * 80)
    print("WALLET ADDRESS DISCOVERY")
    print("=" * 80)
    print("Attempting to discover missing wallet addresses using public APIs...")
    print("Note: Exchange exports lack destination addresses, so we use ")
    print("indirect methods (hot wallet tracing, pattern analysis).")

    try_known_staking_addresses()
    check_solana_additional()
    discover_polkadot_addresses()
    discover_kusama_addresses()
    discover_cosmos_addresses()

    print("\n" + "=" * 80)
    print("SUMMARY OF FINDINGS")
    print("=" * 80)
    print("""
To find the ACTUAL addresses, the best approaches are (in order of effectiveness):

1. CHECK BROWSER HISTORY / BOOKMARKS
   - Polkadot.js apps (polkadot.js.org/apps)
   - Keplr wallet (for Cosmos)
   - Terra Station
   - Any hardware wallet (Ledger Live)

2. CHECK WALLET SOFTWARE
   - Polkadot.js browser extension
   - Keplr browser extension  
   - Phantom / Backpack (for newer Solana wallet)
   - Ledger Live app
   - Electrum / Wasabi (for BTC)

3. CHECK EMAIL
   - Kraken withdrawal confirmation emails contain destination addresses
   - Binance withdrawal confirmation emails contain destination addresses
   - Search for: "withdrawal" "DOT" or "KSM" or "ATOM" or "BTC"

4. EXCHANGE WITHDRAWAL HISTORY (WEB UI)
   - Binance: Wallet > Transaction History > Withdrawals (shows addresses!)
   - Kraken: History/Exports > Withdrawals (shows addresses!)
   - The CSV exports we have do NOT include addresses, but the web UI does
   
5. RE-EXPORT WITH ADDRESSES
   - Binance: Export "Withdraw History" specifically (not "Transaction History")
   - Kraken: Export "Withdrawals" type specifically
    """)


if __name__ == "__main__":
    main()

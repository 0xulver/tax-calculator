from __future__ import annotations

FIAT = frozenset({"EUR", "USD", "GBP", "PLN", "SEK", "JPY", "CAD", "AUD"})

STABLECOINS = frozenset({"USDC", "USDT", "UST", "DAI", "BUSD", "TUSD", "PYUSD", "FDUSD"})

KRAKEN_ASSET_MAP = {
    "XXBT": "BTC", "XBT": "BTC", "XBTC": "BTC",
    "XETH": "ETH", "XXRP": "XRP", "XLTC": "LTC",
    "XXLM": "XLM", "XDOGE": "DOGE", "XZEC": "ZEC",
    "XXMR": "XMR", "XREP": "REP", "XETC": "ETC",
    "XICN": "ICN", "XMLN": "MLN",
    "ZUSD": "USD", "ZEUR": "EUR", "ZGBP": "GBP",
    "ZJPY": "JPY", "ZCAD": "CAD", "ZAUD": "AUD",
    "DOT.S": "DOT", "DOT28.S": "DOT",
    "KSM.S": "KSM",
    "ATOM.S": "ATOM", "ATOM21.S": "ATOM",
    "ETH2.S": "ETH", "ETH.S": "ETH",
    "SOL.S": "SOL",
    "XTZ.S": "XTZ",
    "FLOW.S": "FLOW", "FLOWH.S": "FLOW",
    "KAVA.S": "KAVA",
    "MINA.S": "MINA",
    "TRX.S": "TRX",
    "ADA.S": "ADA",
    "LUNA2": "LUNA2",
}

COINGECKO_ID_MAP = {
    "BTC": "bitcoin", "ETH": "ethereum", "SOL": "solana",
    "DOT": "polkadot", "KSM": "kusama", "ATOM": "cosmos",
    "LINK": "chainlink", "AAVE": "aave", "SNX": "havven",
    "MATIC": "matic-network", "FTM": "fantom",
    "SUI": "sui", "XMR": "monero",
    "LUNA": "terra-luna", "UST": "terrausd",
    "LUNA2": "terra-luna-2",
    "ACA": "acala", "KAR": "karura",
    "USDC": "usd-coin", "USDT": "tether",
    "XRP": "ripple", "ADA": "cardano",
    "AVAX": "avalanche-2", "NEAR": "near",
    "ALGO": "algorand", "XTZ": "tezos",
    "FLOW": "flow", "MINA": "mina-protocol",
    "KAVA": "kava", "TRX": "tron",
}

IGNORED_TX_TYPES = frozenset({
    "internal_transfer", "earn_allocation", "earn_other",
    "fiat_deposit", "fiat_withdrawal", "adjustment", "recovery",
    "unknown",
})


def is_fiat(asset: str) -> bool:
    return asset.upper() in FIAT


def is_stablecoin(asset: str) -> bool:
    return asset.upper() in STABLECOINS

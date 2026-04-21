from core.cache import memoize

COINS = {
    "BTC": {
        "symbol": "BTC",
        "name": "Bitcoin",
        "max_supply": 21000000,
        "launched": 2009,
    },
    "ETH": {
        "symbol": "ETH",
        "name": "Ethereum",
        "max_supply": None,
        "launched": 2015,
    },
    "SOL": {
        "symbol": "SOL",
        "name": "Solana",
        "max_supply": None,
        "launched": 2020,
    },
    "BNB": {
        "symbol": "BNB",
        "name": "Binance Coin",
        "max_supply": 200000000,
        "launched": 2017,
    },
    "CRPR": {
        "symbol": "CRPR",
        "name": "Creeper",
        "max_supply": None,
        "launched": 2222,
    },
}


@memoize
def get_coin_info(symbol):
    return COINS.get(symbol.upper())
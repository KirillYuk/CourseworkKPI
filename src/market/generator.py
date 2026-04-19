import random


def price_generator(symbol="CRPR", start_price=50000.0, volatility=10):
    price = start_price
    
    while True:
        price = price + random.uniform(-volatility, volatility)
        change_24h = round(random.uniform(-10, 10), 2)
        rsi = round(random.uniform(20, 80), 1)



        yield {
            "symbol": symbol,
            "price": round(price, 2),
            "change_24h": change_24h,
            "market_cap": round(price * 19000000, 2),
            "volume": round(random.uniform(30000000000, 60000000000), 2),
            "technical": {
                "rsi": rsi,
                "signal": "BUY" if rsi < 30 else "SELL" if rsi > 70 else "NEUTRAL",
            }
        }
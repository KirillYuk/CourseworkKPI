import random


def price_generator(symbol="CRPR", start_price=50000.0, volatility=10):
    price = start_price
    rsi = 50.0
    
    while True:
        price = price + random.uniform(-volatility, volatility)
        change_24h = round(random.uniform(-10, 10), 2)
        rsi = rsi + random.uniform(-5, 5)
        rsi = max(10, min(90, rsi))
        rsi = round(rsi, 1)
        
        if rsi < 30:
            signal = "BUY"
        elif rsi > 70:
            signal = "SELL"
        else:
            signal = "NEUTRAL"



        yield {
            "symbol": symbol,
            "price": round(price, 2),
            "change_24h": change_24h,
            "market_cap": round(price * 19000000, 2),
            "volume": round(random.uniform(30000000000, 60000000000), 2),
            "technical": {
                "rsi": rsi,
                "signal": signal,
            }
        }

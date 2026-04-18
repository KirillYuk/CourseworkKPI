import random


def price_generator(symbol="CRPR", start_price=50000.0, volatility=10):
    price = start_price
    
    while True:
        price = price + random.uniform(-volatility, volatility)
        yield {
            "symbol": symbol,
            "price": round(price, 2)
        }
import random


def price_generator(start_price=50000.0, volatility=100):
    price = start_price
    while True:
        price = price + random.uniform(-volatility, volatility)
        yield price
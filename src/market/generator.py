import random


def price_generator():
    price = 50000.0
    while True:
        price = price + random.uniform(-100, 100)
        yield price
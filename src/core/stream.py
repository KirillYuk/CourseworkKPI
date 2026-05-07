import csv
import random


def generate_csv(filename, symbol="BTC", days=30):
    price = 50000.0

    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["symbol", "price", "day"])

        for day in range(1, days + 1):
            price = round(price + random.uniform(-500, 500), 2)
            writer.writerow([symbol, price, day])


def read_csv(filename):
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield row
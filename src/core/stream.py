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
            
def filter_by_symbol(filename, symbol):
    for row in read_csv(filename):
        if row["symbol"] == symbol:
            yield row
            
def history_stats(filename, symbol):
    count = 0
    total = 0
    max_price = None
    min_price = None
    
    for row in filter_by_symbol(filename, symbol):
        price = float(row["price"])
        
        count+=1
        total+=price
        
        if min_price is None or price < min_price:
            min_price = price
            
        if max_price is None or price > max_price:
            max_price = price
            
        avg = round(total/count, 2)
        
        yield {
            "day": row["day"],
            "symbol": row["symbol"],
            "price": price,
            "avg": avg,
            "min": min_price,
            "max": max_price,  
        }
        
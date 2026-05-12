import asyncio
from market.generator import price_generator, async_price_generator
from market.coins import get_coin_info 
from core.runtime import run
from core.async_runtime import async_run
from core.stream import generate_csv, history_stats
from api.api import get_real_price


command = input("command (stream/async_stream/info): ")
symbol = input("symbol: ").strip().upper()


if command == "stream":
    info = get_coin_info(symbol)
    if not info:
        print("coin not found", symbol)
    else:
        seconds = float(input("seconds: "))
        gen = price_generator(symbol=symbol, start_price=50000.0, volatility=10)
        run(gen, seconds)
        
        
elif command == "async_stream":
    info = get_coin_info(symbol)
    if not info:
        print("coin not found:", symbol)
    else:
        seconds = float(input("seconds: "))
        threshold = input("price threshold(enter to skip): ")
        threshold = float(threshold) if threshold else None
        
        enable_logs = input("enable event logs? (y/n): ").strip().lower() == "y"
        enable_notifications = input("enable notifications? (y/n): ").strip().lower() == "y"
        
        gen = async_price_generator(symbol=symbol, start_price=50000.0, volatility=100)
        asyncio.run(async_run(gen, seconds, price_threshold=threshold, enable_logs=enable_logs, enable_notifications=enable_notifications))


elif command == "info":
    info = get_coin_info(symbol)
    if info:
        for key, value in info.items():
            print(key + ":", value)
    else:
        print("coin not found", symbol)
        
        
elif command == "history":
    filename = "history.csv"
    days = int(input("days: "))
    
    generate_csv(filename, symbol=symbol, days=days)
    
    for row in history_stats(filename, symbol):
        print(
            "day: ", row["day"],
            "symbol: ", row["symbol"],
            "price: ", row["price"],
            "avg: ", row["avg"],
            "min: ", row["min"],
            "max: ", row["max"],
        )
        
        
elif command == "price":
    data = get_real_price(symbol)
    if data:
        for key, value in data.items():
            print(key, value)
    else:
        print("coin not found", symbol)
        
        
else:
    print("unknown command:", command)

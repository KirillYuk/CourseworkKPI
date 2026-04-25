from market.generator import price_generator
from core.runtime import run
from market.coins import get_coin_info 


command = input("command (stream/info): ")
symbol = input("symbol: ")

if command == "stream":
    seconds = float(input("seconds: "))
    gen = price_generator(symbol=symbol, start_price=50000.0, volatility=10)
    run(gen, seconds)

elif command == "info":
    info = get_coin_info(symbol)
    if info:
        for key, value in info.items():
            print(key + ":", value)
    else:
        print("coin not found", symbol)
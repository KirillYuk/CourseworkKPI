from market.generator import price_generator
from core.runtime import run
 

symbol = input("symbol: ")
seconds = float(input("seconds: "))
gen = price_generator(symbol="CRPR", start_price=50000.0, volatility=10)
run(gen, seconds)
 
from market.generator import price_generator
from core.runtime import run
 

seconds = float(input("seconds: "))
gen = price_generator(symbol="CRPR", start_price=10, volatility=1)
run(gen, seconds)
 
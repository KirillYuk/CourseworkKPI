import time
from rich import print


def run(iterator, seconds):
    end_time = time.time() + seconds
    count = 0
    total = 0
    min_price = None
    max_price = None


    for symbol, price in iterator:
        if time.time() > end_time:
            break

        count+=1
        total +=price

        if min_price is None or price < min_price:
            min_price = price
        if max_price is None or price > max_price:
            max_price = price

        avg = round(total/count, 2)


        print(f"[white]{count}[/white] [red]{symbol}[/red] [green]{round(price, 2)}[green]", "   avg: ", avg, "   min: ", min_price, "   max: ", max_price)
        
        time.sleep(0.3)
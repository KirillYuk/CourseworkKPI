import time
from rich import print


def run(iterator, seconds):
    end_time = time.time() + seconds
    count = 0
    total = 0
    min_price = None
    max_price = None


    for tick in iterator:
        if time.time() > end_time:
            break

        count+=1
        total += tick["price"]

        if min_price is None or tick["price"] < min_price:
            min_price = tick["price"]
        if max_price is None or tick["price"] > max_price:
            max_price = tick["price"]

        avg = round(total/count, 2)


        print(f"[white]{count}[/white] [red]{tick["symbol"]}[/red] [green]{round(tick["price"], 2)}[green]", "   avg: ", avg, "   min: ", min_price, "   max: ", max_price)
        
        time.sleep(0.01)
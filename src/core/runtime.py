import time
from rich import print


def run(iterator, seconds):
    end_time = time.time() + seconds
    count = 0
    total = 0

    for price in iterator:
        if time.time() > end_time:
            break
        count+=1
        total +=price
        avg = round(total/count, 2)
        print(f"[white]{count}[/white] [green]{round(price, 2)}[green]", avg)
        time.sleep(0.1)
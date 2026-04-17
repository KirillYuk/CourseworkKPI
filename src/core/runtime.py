import time
from rich import print


def run(iterator, seconds):
    end_time = time.time() + seconds
    count = 0

    for price in iterator:
        if time.time() > end_time:
            break
        count+=1
        print(f"[white]{count}[/white] [green]{price}[green]")
        time.sleep(0.1)
import time
from rich import print
from market.alerts import BiQueue


def run(iterator, seconds):
    end_time = time.time() + seconds
    count = 0
    total = 0
    min_price = None
    max_price = None
    alert_queue = BiQueue()


    for tick in iterator:
        if time.time() > end_time:
            break

        count += 1
        total += tick["price"]

        if min_price is None or tick["price"] < min_price:
            min_price = tick["price"]
        if max_price is None or tick["price"] > max_price:
            max_price = tick["price"]

        avg = round(total/count, 2)

        rsi = tick["technical"]["rsi"]
        signal = tick["technical"]["signal"]
        
        
        print(f"[white]{count}[/white] [red]{tick["symbol"]}[/red] [green]{round(tick["price"], 2)}[green]", "   avg: ", avg, "   min: ", min_price, "   max: ", max_price)
        
        
        if signal == "BUY":
            alert_queue.enqueue(
                {"symbol": tick["symbol"],
                 "rsi": rsi,
                 "signal": signal},
                priority=3
            )
            print(f"[green]BUY {tick["symbol"]} RSI: {rsi}[/green]")
        
        elif signal == "SELL":
            alert_queue.enqueue(
                {"symbol": tick["symbol"],
                 "rsi": rsi,
                 "signal": signal},
                priority=2
            )
            print(f"[red]SELL {tick["symbol"]} RSI: {rsi}[/red]")
        
        
        time.sleep(1)
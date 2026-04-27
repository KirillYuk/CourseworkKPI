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

        count+=1
        total += tick["price"]

        if min_price is None or tick["price"] < min_price:
            min_price = tick["price"]
        if max_price is None or tick["price"] > max_price:
            max_price = tick["price"]

        avg = round(total/count, 2)

        rsi = tick["technical"]["rsi"]
        signal = tick["technical"]["signal"]
        
        if signal == "BUY":
            alert_queue.enqueue(
                {"symbol": tick["symbol"],
                 "rsi": rsi,
                 "signal": signal},
                priority=3
            )
        
        elif signal == "SELL":
            alert_queue.enqueue(
                {"symbol": tick["symbol"],
                 "rsi": rsi,
                 "signal": signal},
                priority=2
            )
        
        print(f"[white]{count}[/white] [red]{tick["symbol"]}[/red] [green]{round(tick["price"], 2)}[green]", "   avg: ", avg, "   min: ", min_price, "   max: ", max_price)
        
        time.sleep(0.01)
        
    print("\n[bold yellow]ALERTS[/bold yellow]")
    alert = alert_queue.dequeue("highest")
    while alert != None:
        print(f"[red]{alert["signal"]}[/red] {alert["symbol"]} RSI: {alert["rsi"]}")
        alert = alert_queue.dequeue("highest")
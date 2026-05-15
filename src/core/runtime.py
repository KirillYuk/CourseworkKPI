import time
from core.display import print_tick, print_signal, show_startup
from market.alerts import BiQueue


def run(iterator, seconds):
    end_time = time.time() + seconds
    count = 0
    total = 0
    min_price = None
    max_price = None
    alert_queue = BiQueue()
    
    show_startup("Starting sync market stream...")

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
        
        
        print_tick(count, tick, avg, min_price, max_price)
        
        
        if signal == "BUY":
            alert = {"symbol": tick["symbol"],
                 "rsi": rsi,
                 "signal": signal
                 }
            alert_queue.enqueue(alert, priority=3)
            print_signal("BUY", alert)
        
        elif signal == "SELL":
            alert = {"symbol": tick["symbol"],
                 "rsi": rsi,
                 "signal": signal
                 }
            alert_queue.enqueue(alert, priority=2)
            print_signal("SELL", alert)
        
        
        time.sleep(3)

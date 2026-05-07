import asyncio
from rich import print
from market.alerts import BiQueue
from events.events import EventEmitter, on_buy_signal, on_sell_signal, on_price_threshold


async def async_run(iterator, seconds, price_threshold=None):
    end_time = asyncio.get_event_loop().time() + seconds
    count = 0
    total = 0
    min_price = None
    max_price = None
    alert_queue = BiQueue()

    emitter = EventEmitter()
    emitter.subscribe("buy_signal", on_buy_signal)
    emitter.subscribe("sell_signal", on_sell_signal)
    if price_threshold is not None:
        emitter.subscribe("price_threshold", on_price_threshold)
        

    async for tick in iterator:
        if asyncio.get_event_loop().time() > end_time:
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
            emitter.emit("buy_signal", {"symbol": tick["symbol"], "rsi": rsi})
        
        elif signal == "SELL":
            alert_queue.enqueue(
                {"symbol": tick["symbol"],
                 "rsi": rsi,
                 "signal": signal},
                priority=2
            )
            emitter.emit("sell_signal", {"symbol": tick["symbol"], "rsi": rsi})
            
        if price_threshold is not None and tick["price"] > price_threshold:
            emitter.emit("price_threshold", {"symbol": tick["symbol"], "price": tick["price"]})
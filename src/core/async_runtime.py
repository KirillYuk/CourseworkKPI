import asyncio
from rich import print
from market.alerts import BiQueue
from events.events import EventEmitter, on_buy_signal, on_sell_signal, on_price_threshold


async def handle_commands(emitter, stop_event):
    while not stop_event.is_set():
        try:
            command = await asyncio.get_event_loop().run_in_executor(None, input, "> ")
            
            if command == "unsubscribe price_threshold":
                emitter.unsubscribe("price_threshold", on_price_threshold)
                print("unsubscribed from price_threshold")
            elif command == "stop":
                stop_event.set()
        except Exception:
            break


async def async_run(iterator, seconds, price_threshold=None):
    end_time = asyncio.get_event_loop().time() + seconds
    count = 0
    total = 0
    min_price = None
    max_price = None
    alert_queue = BiQueue()
    stop_event = asyncio.Event()

    emitter = EventEmitter()
    emitter.subscribe("buy_signal", on_buy_signal)
    emitter.subscribe("sell_signal", on_sell_signal)
    if price_threshold is not None:
        emitter.subscribe("price_threshold", on_price_threshold)
        
    command_task = asyncio.create_task(handle_commands(emitter, stop_event))
        

    async for tick in iterator:
        if asyncio.get_event_loop().time() > end_time or stop_event.is_set():
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
            
    command_task.cancel()
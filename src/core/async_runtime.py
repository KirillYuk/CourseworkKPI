import asyncio
from pynput import keyboard
from rich import print
from market.alerts import BiQueue
from events.events import (EventEmitter,
                           on_buy_signal,
                           on_sell_signal,
                           on_price_threshold,
                           log_market_event,
                           notify_user) 


PRICE_LISTENERS = [on_price_threshold, log_market_event, notify_user]

def listen_keys(emitter, stop_event, price_subscribed):
    def on_press(key):
        try:
            if key.char == "q":
                stop_event.set()
                
            elif key.char == "s":
                if price_subscribed[0]:
                    for listener in PRICE_LISTENERS:
                        emitter.unsubscribe("price_threshold", listener)
                    price_subscribed[0] = False
                    print("unsubscribed from price_threshold")
                    
                else:
                    for listener in PRICE_LISTENERS:
                        emitter.subscribe("price_threshold", listener)
                    price_subscribed[0] = True
                    print("subscribed to price_threshold")
                    
        except AttributeError:
            pass
        
    return keyboard.Listener(on_press=on_press)


async def async_run(iterator, seconds, price_threshold=None):
    end_time = asyncio.get_event_loop().time() + seconds
    count = 0
    total = 0
    min_price = None
    max_price = None
    alert_queue = BiQueue()
    stop_event = asyncio.Event()
    price_subscribed = [price_threshold is not None]

    emitter = EventEmitter()
    
    emitter.subscribe("buy_signal", on_buy_signal)
    emitter.subscribe("buy_signal", log_market_event)
    
    emitter.subscribe("sell_signal", on_sell_signal)
    emitter.subscribe("sell_signal", log_market_event)
    
    if price_threshold is not None:
        for listener in PRICE_LISTENERS:
            emitter.subscribe("price_threshold", listener)
        
    print("Controls: q - stop, s - toogle price alerts")
    
    listener = listen_keys(emitter, stop_event, price_subscribed)
    listener.start()
        

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
        
        
        print(f"[white]{count}[/white]"
              f"[red]{tick["symbol"]}[/red]"
              f"[green]{round(tick["price"], 2)}[green]",
              "   avg: ", avg,
              "   min: ", min_price,
              "   max: ", max_price)
        
        
        if signal == "BUY":
            alert = {
                "symbol": tick["symbol"],
                "rsi": rsi,
                "signal": signal},
            
            alert_queue.enqueue(alert, priority=3)
            emitter.emit("buy_signal", alert)
        
        elif signal == "SELL":
            alert = {
                "symbol": tick["symbol"],
                "rsi": rsi,
                "signal": signal},
            alert_queue.enqueue(alert, priority=2)
            emitter.emit("sell_signal", alert)
            
        if price_threshold is not None and tick["price"] > price_threshold:
            emitter.emit("price_threshold", {
                "symbol": tick["symbol"],
                "price": tick["price"]})
            
    listener.stop()

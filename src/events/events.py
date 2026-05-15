from core.display import console

class EventEmitter:
    def __init__(self):
        self.listeners = {}
        
    def subscribe(self, event, callback):
        if event not in self.listeners:
            self.listeners[event] = []
        self.listeners[event].append(callback)
        
    def unsubscribe(self, event, callback):
        if event in self.listeners and callback in self.listeners[event]:
            self.listeners[event].remove(callback)
            
    def emit(self, event, data):
        if event in self.listeners:
            for callback in self.listeners[event]:
                callback(data)
                
                
def on_buy_signal(data):
    console.print(f"[event] [green]BUY[/] {data["symbol"]} RSI: {data["rsi"]}")
        
def on_sell_signal(data):
    console.print(f"[event] [red]SELL[/] {data["symbol"]} RSI: {data["rsi"]}")
        
def on_price_threshold(data):
    console.print(f"[event] [yellow]PRICE[/] {data["symbol"]} price: {data["price"]}")
    
def log_market_event(data):
    console.print(f"[log] {data}")
    
def notify_user(data):
    console.print(f"[notify] Important market event for {data['symbol']}")
class EventEmitter:
    def __init__(self):
        self.listeners = {}
        
    def subscribe(self, event, callback):
        if event not in self.listeners:
            self.listeners[event] = []
        self.listeners[event].append(callback)
        
    def unsubscribe(self, event, callback):
        if event in self.listeners:
            self.listeners[event].remove(callback)
            
    def emit(self, event, data):
        if event in self.listeners:
            for callback in self.listeners[event]:
                callback(data)
                
                
def on_buy_signal(data):
    print(f"[event] BUY signal {data["symbol"]} RSI: {data["rsi"]}")
        
def on_sell_signal(data):
        print(f"[event] SELL signal {data["symbol"]} RSI: {data["rsi"]}")
        
def on_price_threshold(data):
    print(f"[event] PRICE signal {data["symbol"]} price: {data["price"]}")
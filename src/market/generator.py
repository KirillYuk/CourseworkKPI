import random
import asyncio


def calculate_rsi(prices):
    if len(prices) < 14:
        return None
    
    gains = []
    losses = []
    
    for i in range(1, 14):
        change = prices[i] - prices[i - 1]
        if change > 0:
            gains.append(change)
            losses.append(0)
        else:
            gains.append(0)
            losses.append(abs(change))
            
    avg_gain = sum(gains) / 14
    avg_loss = sum(losses) / 14
    
    if avg_loss == 0:
        return 100
    
    rs = avg_gain / avg_loss
    rsi = round(100 - (100 / (1+ rs)), 1)
    return rsi

def price_generator(symbol="CRPR", start_price=50000.0, volatility=10):
    price = start_price
    prices = []
    
    while True:
        price = price + random.uniform(-volatility, volatility)
        prices.append(price)
        
        change_24h = round(random.uniform(-10, 10), 2)
        rsi = calculate_rsi(prices[-14:])
        if rsi == None:
            signal = "NEUTRAL"
        elif rsi < 30:
            signal = "BUY"
        elif rsi > 70:
            signal = "SELL"
        else:
            signal = "NEUTRAL"



        yield {
            "symbol": symbol,
            "price": round(price, 2),
            "change_24h": change_24h,
            "market_cap": round(price * 19000000, 2),
            "volume": round(random.uniform(30000000000, 60000000000), 2),
            "technical": {
                "rsi": rsi,
                "signal": signal,
            }
        }


async def async_price_generator(symbol="CRPR", start_price=50000.0, volatility=10):
    price = start_price
    prices = []
    
    while True:
        price = price + random.uniform(-volatility, volatility)
        prices.append(price)
        
        change_24h = round(random.uniform(-10, 10), 2)
        rsi = calculate_rsi(prices[-14:])
        if rsi == None:
            signal = "NEUTRAL"
        elif rsi < 30:
            signal = "BUY"
        elif rsi > 70:
            signal = "SELL"
        else:
            signal = "NEUTRAL"



        yield {
            "symbol": symbol,
            "price": round(price, 2),
            "change_24h": change_24h,
            "market_cap": round(price * 19000000, 2),
            "volume": round(random.uniform(30000000000, 60000000000), 2),
            "technical": {
                "rsi": rsi,
                "signal": signal,
            }
        }
        
        await asyncio.sleep(1)

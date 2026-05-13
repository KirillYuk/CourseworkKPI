import os
from dotenv import load_dotenv
from core.proxy import AuthProxy

load_dotenv()

base_url = "https://api.freecryptoapi.com/v1"
proxy = AuthProxy(method="api_key", key=os.getenv("API_KEY"))


def normalize_symbol(symbol):
    return symbol.strip().upper()


def get_real_price(symbol):
    symbol = normalize_symbol(symbol)
    data = proxy.get(base_url + "/getData", params={"symbol": symbol})
    return data

def get_real_info(symbol):
    data = get_real_price(symbol)
    
    if not data.get("status", True):
        return data
    
    return data

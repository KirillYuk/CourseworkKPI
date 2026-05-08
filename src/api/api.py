import os
from dotenv import load_dotenv
from core.proxy import AuthProxy

load_dotenv()

base_url = "https://api.freecryptoapi.com/v1"
proxy = AuthProxy(method="api_key", key=os.getenv("API_KEY"))

def get_real_price(symbol):
    data = proxy.get(base_url + "/getData?symbol=" + symbol)
    return data
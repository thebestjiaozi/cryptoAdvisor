import requests
from config import CRYPTOPANIC_TOKEN

def fetch_news():
    url = "https://cryptopanic.com/api/v1/posts/"
    params = {
        "auth_token": CRYPTOPANIC_TOKEN,
        "currencies": "BTC,ETH",
        "public": "true"
    }
    res = requests.get(url, params=params)
    return res.json()["results"]
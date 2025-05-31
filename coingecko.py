import requests
import datetime

def fetch_coin_data(coin_id="bitcoin", vs_currency="usd", days=1):
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart"
    params = {"vs_currency": vs_currency, "days": days}
    res = requests.get(url, params=params)
    data = res.json()
    
    prices = data.get("prices", [])
    formatted = [
        {"timestamp": datetime.datetime.fromtimestamp(p[0] / 1000), "price": p[1]}
        for p in prices
    ]
    return formatted

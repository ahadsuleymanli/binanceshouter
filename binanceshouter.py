import time
import datetime
import requests
from playsound import playsound


def check_price(pair: str = "ADAUSDT") -> float:
    response = requests.get(f"https://api.binance.com/api/v3/avgPrice?symbol={pair}")
    price = float(response.json()["price"])
    print(f"checked price for {pair}: {price}")
    return price


def handle_price(price: float, low_limit: float, pair: str) -> None:
    if price < low_limit:
        response(price, low_limit, pair)

def response(price, low_limit, pair):
    playsound('you_suffer.mp3')
    print(f"{datetime.datetime.now()}: {pair}: price{price}")

if __name__ == "__main__":
    while True:
        pair = "ADAUSDT"
        price = check_price(pair)
        handle_price(price, 1.7, pair)
        time.sleep(1)

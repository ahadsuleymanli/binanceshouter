import time
import datetime
import sys
from os import system, name
import requests
from playsound import playsound
from collections import deque

def check_price(pair: str = "ADAUSDT") -> float:
    response = requests.get(f"https://api.binance.com/api/v3/avgPrice?symbol={pair}")
    price = float(response.json()["price"])
    # print(f"checked price for {pair}: {price}")
    return price


def handle_price(price: float, low_limit: float, pair: str) -> None:
    if price < low_limit:
        response(price, low_limit, pair)

def response(price, low_limit, pair):
    playsound('you_suffer.mp3')
    print(f"{datetime.datetime.now()}: {pair}: price: {price}")

def everynowandthen_generator(every_x_secs: int = 100):
    secs_passed = -1
    while True:
        yield True if (secs_passed := (secs_passed + 1) % every_x_secs) == 0 else False

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

if __name__ == "__main__":
    prices_list = deque(maxlen=10)

    history_gen = everynowandthen_generator(100)
    shout_gen = everynowandthen_generator(60)

    while True:
        pair = "ADAUSDT"
        outstring = ""
        
        price = check_price(pair)
        if next(history_gen):
            prices_list.append(f"{datetime.datetime.now()}: {price}")
        for x in prices_list:
            outstring += x + "\n"
        outstring += f"checked price for {pair}: {price}"

        clear()
        print(outstring)

        if next(shout_gen):
            handle_price(price, 1.7, pair)

        time.sleep(1)

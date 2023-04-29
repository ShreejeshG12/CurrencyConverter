import requests
import json

main_currency = (input()).lower()
cache = {}
r = requests.get("http://www.floatrates.com/daily/{}.json".format(main_currency))

response = r.json()



for key, value in response.items():
    if main_currency == "usd":
        cache |= {'usd' : 1, 'eur': 1.0995170805676}
    elif main_currency == "eur":
        cache |= {'eur' : 1, 'usd' : 0.90949019135178}
    else:
        cache |= {'usd' : response['usd']['inverseRate']}
        cache |= {'eur' : response['eur']['inverseRate']}

while True:
    ex_currency = input().lower()
    if ex_currency == "":
        break

    money = float(input())

    if ex_currency in cache.keys():
        total = money / cache[ex_currency]
        print("Checking the cache...")
        print("Oh! It is in the cache!")
        print("You received {} {}.".format(total, ex_currency.upper()))

    else:
        rate = response[ex_currency]['inverseRate']
        cache |= {ex_currency : rate}
        total =  money / rate
        print("Checking the cache...")
        print("Sorry, but it is not in the cache!")
        print("You received {} {}.".format(total, ex_currency.upper()))




git
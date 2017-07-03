import json

import requests


def get_btce_data(first_stock, second_stock):
    # code which takes 2 stocks and returns btc data
    stocks_to_search = first_stock + "_" + second_stock
    url = "https://btc-e.com/api/3/ticker/" + stocks_to_search
    url_data = requests.get(url).content
    raw_data = url_data
    try:
        stocks_to_search = second_stock + "_" + first_stock
        url = "https://btc-e.com/api/3/ticker/" + stocks_to_search
        url_data = requests.get(url).content
        raw_data = url_data
        try:
            print(json.loads(raw_data)["error"])
            return -1
        except:
            return raw_data
    except:
        return raw_data

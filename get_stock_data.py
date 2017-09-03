import json
import requests

'''
This module goes to the bitfinex API and gets the stock information
'''


def get_btce_data(first_stock, second_stock):
    # code which takes 2 stocks and returns btc data
    stocks_to_search = first_stock + second_stock
    print(stocks_to_search)
    url = "https://api.bitfinex.com/v1/pubticker/" + stocks_to_search
    try:
        url_data = requests.get(url).content
        raw_data = url_data
        try:
            message = (json.loads(raw_data)['message'])
            print(message)
            stocks_to_search = second_stock + first_stock
            url = "https://api.bitfinex.com/v1/pubticker/" + stocks_to_search
            url_data = requests.get(url).content
            raw_data = url_data
            try:
                print(json.loads(raw_data)['message'])
                return -1
            except:
                print(raw_data)
                return raw_data
        except:
                return raw_data
    except:
        print("Unable to reach url")
        return -1

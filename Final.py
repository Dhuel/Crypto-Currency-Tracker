import threading
import get_csv_data as get
import json


def f():
    # Function used to get sell price every second
    threading.Timer(1, f).start()
    btc_ltc = get.get_btc_ltc()
    d = json.loads(btc_ltc)
    print(d["ltc_btc"]['last'])
    if d["ltc_btc"]['last'] < 0.01049:
        print("ALERT-Sell time")

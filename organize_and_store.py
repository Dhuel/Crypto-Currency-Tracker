import json
import sqlite3
import threading

import get_stock_data as get


def get_stock_data(first_stock, second_stock, frequency, go):
    # Function used to get Stock information
    if go:
        stock_data = get.get_btce_data(first_stock, second_stock)
        if stock_data == -1:
            go = False
            return 0
        d = json.loads(stock_data)
        print(d)
        name = next(iter(d))
        values = [(d[name]['updated'], d[name]['high'], d[name]['low'], d[name]['avg'],
                   d[name]['vol'], d[name]['vol_cur'], d[name]['last'], d[name]['buy'],
                   d[name]['sell'])]
        store_to_db(name, values)
        threading.Timer(frequency, get_stock_data, [first_stock, second_stock, frequency, go]).start()


def store_to_db(table, values):
    # Function used to store information to db
    conn = sqlite3.connect('Stock.db')
    c = conn.cursor()
    # c.execute('delete from btc_ltc')
    # Create table if it doesn't exist
    c.execute(
        "CREATE TABLE IF NOT EXISTS " + table + " (date text, high real, low real, avg real, vol real, vol_cur real," +
        "last real, buy real, sell real)")

    # Insert a row of data
    c.executemany("INSERT INTO " + table + " VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", values)

    # Save (commit) the changes and close db connection
    conn.commit()
    conn.close()

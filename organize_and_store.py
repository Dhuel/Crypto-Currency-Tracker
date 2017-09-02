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
        values = [(d['mid'], d['bid'], d['ask'], d['last_price'], d['low'], d['high'], d['volume'], d['timestamp'])]
        print(d['last_price'])
        store_to_db("btc_usd", values)
        threading.Timer(frequency, get_stock_data, [first_stock, second_stock, frequency, go]).start()


def store_to_db(table, values):
    # Function used to store information to db
    conn = sqlite3.connect('Records.db')
    c = conn.cursor()
    # c.execute('delete from btc_ltc')
    # Create table if it doesn't exist
    c.execute(
        "CREATE TABLE IF NOT EXISTS " + table + " (mid real, bid real, ask real, last_price real, low real, high real," +
        "volume real, timestamp text)")

    # Insert a row of data
    c.executemany("INSERT INTO " + table + " VALUES ( ?, ?, ?, ?, ?, ?, ?, ?)", values)

    # Save (commit) the changes and close db connection
    conn.commit()
    conn.close()

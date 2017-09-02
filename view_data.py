import sqlite3

if __name__ == "__main__":
    # This function is used to ensure the database is pulling and storing records
    conn = sqlite3.connect('Records.db')
    cursor = conn.execute("SELECT * from btc_usd")
    for row in cursor:
        print("mid = ", row[0])
        print("bid = ", row[1])
        print("ask = ", row[2])
        print("last price = ", row[3])
        print("low = ", row[4])
        print("high = ", row[5])
        print("volume = ", row[6])
        print("time = ", row[7], "\n")

    conn.close()

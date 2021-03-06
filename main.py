import organize_and_store as org


if __name__ == "__main__":
    ''' This is the main function of the entire code structure.
         It is the starting point for pulling the stock data which will then be stored to a database.
         This function takes two crypto currency icons, a time variable and a True value.
         These values are then checked against bitfinex's API.
     '''
    org.get_stock_data("usd", 'btc', 60, True)

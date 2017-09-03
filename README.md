# PythonFinance
This is a python module which uses the bitfinex API to pull and store crypto currency records locally using python.

The required modules are:

json, sqlite3, threading, requests

It may be started by running main.py through python
```
$ python main.py
```
The current version of the code allows for data to be pulled every 60 seconds. This may be edited by changing the time parameter in the main.py file.

```
e.g. org.get_stock_data("usd", 'btc', 90, True)
```
Bitfinex limits thee amount of times an API can be called so read their documentation before editing the time value
https://bitfinex.readme.io/v2/docs/getting-started

To ensure that data is correctly being entered in the database, you may use the view_data.py
```
$ python view_data.py
```






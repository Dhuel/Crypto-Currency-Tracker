import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
import time

dfStock = pd.read_csv("table.csv")


def plot_selected(df, columns, start_index, end_index):
    """Plot the desired columns over index values in the given range. Uses indices in column field"""
    plot_data(df.ix[start_index:end_index, columns], title="Selected data")


def normalize_data(df):
    """Normalizes data"""
    return df / df.ix[0, :]


def symbol_to_path(symbol, base_dir=""):
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))
    # returns csv file with update col name values


def get_data(stocks, dates):
    """Read stock data for given symbols from CSV file"""
    df = pd.DataFrame(index=dates)
    if 'Google' not in stocks:  # Add google for reference
        stocks.insert(0, 'Google')
    for symbol in stocks:
        df_temp = pd.read_csv(symbol_to_path(symbol), index_col='Date', parse_dates=True, usecols=['Date',
                                                                                                   'Adj Close'],
                              na_values=['nan'])
        df_temp = df_temp.rename(columns={'Adj Close': symbol + ' ADJ'})
        df = df.join(df_temp)
        # Drops everything that had  nan in google
        if symbol == 'Google':
            # 01-02 quiz 12
            # df = df.dropna(subset=['Google'])
            df = df.dropna()
    return df


def plot_data(df, title="Stock prices"):
    ax = df.plot(title=title)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.show()


def test_run():
    dates = pd.date_range('2017-03-29', '2017-04-26')
    stocks = ['AAPL', 'IBM', 'GLD']
    df = get_data(stocks, dates)
    # df = normalize_data(df)
    # plot_data(df)
    # plot_selected(df, [2 , 3], '2017-03-29', '2017-04-26')
    print(df)


def get_max_index(a):
    return a.argmax()


def check_time(a, b):
    print("The time taken is ", b-a, " seconds.")


def num_tut():
    # print(np.array([(2, 3, 4), (5, 6, 7)]))
    # Creates 2d empty array
    """
    print(np.empty((5, 4)))
    # Creates 2d array filled with ones with integers
    print(np.ones((5, 4), dtype=np.int))
    # Creates randomly generated numbers in array
    print(np.random.rand(5, 4))
    # Sample numbers from a Gaussian distribution
    print(np.random.normal(50, 10, size=(2, 3)))  # sets mean to 50 and s.d to 10
    """

    # Generating random integers
    '''print(np.random.randint(10))  # Single integer between 0 and 10
    print(np.random.randint(0, 10))  # Same as above but explicitly
    print(np.random.randint(0, 10, size=5))  # 5 random integers as array
    print(np.random.randint(0, 10, size=(2, 3)))  # 2x3 array'''
    # Getting array size and data type
    '''
    a = np.random.rand(5, 4)
    print(a)
    print(a.shape)
    # a.shape(0) returns rows, can also be used for columns
    print(len(a.shape))  # Tells dimensions
    print(a.size)  # Tells how many values are in the array
    print(a.dtype)  # Tells the data type
    '''
    # Seeding and printing rows and column sums
    '''   
    np.random.seed(693)  # seed the random number generator This makes the numbers remain the same
    a = np.random.randint(0, 10, size=(5, 4))
    print("Array:\n", a)


    # Sum of all elements in array
    print("Sum of all elements: ", a.sum())

    # Sum of each column
    print("Sum of each column:\n", a.sum(axis=0))

    # Sum of each row
    print("Sum of each row:\n", a.sum(axis=1))
    '''

    # Getting min, max and average
    '''
    np.random.seed(693)  # seed the random number generator This makes the numbers remain the same
    a = np.random.randint(0, 10, size=(5, 4))
    print("Array:\n", a)
    print("Minimum of each column:\n", a.min(axis=0))
    print("Maximum of each row:\n", a.max(axis=1))
    print("Mean of all elements:\n", a.mean())
    '''

    '''
    # Find the maximum and its index in array
    print("Maximum value:", a.max())
    print("Index of max.:", get_max_index(a))
    '''
    # Checking timing
    '''
    t1 = time.time()
    t2 = time.time()
    check_time(t1, t2)
    '''
    # Slicing and dicing
    '''
    # Element at position
    element = a[3, 2]
    print(element)
    # Element in range
    print("Range:\n", a[0, 1:3])
    # Getting corner
    print(a[0:2, 0:2])
    # Slicing
    # slices n:m:t. it starts at n but stops before m. It will select column 0,2 of every row
    # DON'T  UNDERSTAND THIS 01-03 - 15
    print("Slicing: \n", a[:, 0:3:2])
    '''
    # Assigning values
    '''
    a[0, 0] = 1
    a[0:2] = 2
    a[:, 3] = [1, 2, 3, 4, 5]
    '''
    # Accessing using indices
    '''
    indices = np.array([1, 1, 2, 3])
    print(a[indices])
    '''
    # Masking
    '''
    a = np.array([(20, 25, 10, 23, 26, 32, 10, 5, 0), (0, 2, 50, 20, 0, 1, 28, 5, 0)])
    print("Array: \n", a)
    mean = a.mean()
    # mask
    print(a[a < mean])
    a[a < mean] = mean
    print("New a \n", a)
    '''
    # Arithmetic operations
    a = np.array([(1, 2, 3, 4, 5), (10, 20, 30, 40, 50)])
    print("Original array \n", a)
    # Multiply by 2
    print("\n Multiply a by 2:\n", 2*a)
    # Can be used to add arrays as well
    # Does element wise algorithm

if __name__ == "__main__":
    num_tut()
    # test_run()




















# Original test run
# def test_run():
#     start_date = '2017-03-29'
#     end_date = '2017-04-26'
#     # Used to set the range of dates being searched
#     dates = pd.date_range(start_date, end_date)
#
#     # Creates a new dataframe containing only those dates as their indeces
#     df1 = pd.DataFrame(index=dates)
#
#     '''
#     index_col - Used to set index to be matched against when joining
#     parse_dates - Converts the date to be a date time index object
#     usecols - Pulls only those columns
#     na_values -used to specify which rows to drop in dropna() function
#     '''
#     dfGOOG = pd.read_csv("google.csv", index_col="Date", parse_dates=True, usecols=['Date', 'Open', 'Adj Close'],
#                          na_values=['nan'])
#     # Rename column names
#     dfGOOG = dfGOOG.rename(columns={'Adj Close': 'SPY ADJ'})
#     dfGOOG = dfGOOG.rename(columns={'Open': 'SPY Open'})
#
#     '''
#     # Join two data frames
#     df1 = df1.join(dfGOOG)
#     # Drop unneeded fields (NaN)
#     df1 = df1.dropna()
#
#     '''
#     # Joins dataframes without the need for multiple calls, ie join and dropna
#     df1 = df1.join(dfGOOG, how='inner')
#
#     # Reading in multiple data sets
#     Stocks = ['IBM', 'GLD', 'AAPL']
#     for symbol in Stocks:
#         # Stores temporary values to be joined to data
#         df_temp = pd.read_csv("{}.csv".format(symbol), index_col='Date', parse_dates=True, usecols=['Date', 'Open',
#                                                                                                     'Adj Close'],
#                               na_values=['nan'])
#         # Renaming columns to prevent clashes
#         df_temp = df_temp.rename(columns={'Adj Close': symbol + ' ADJ'})
#         df_temp = df_temp.rename(columns={'Open': symbol + ' Open'})
#         df1 = df1.join(df_temp)  # uses default left join
#     print(df1)

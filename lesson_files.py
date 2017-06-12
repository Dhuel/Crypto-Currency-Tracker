import numpy as np
import time
import pandas as pd
import get_csv_data as ob
import plotting_data as plotter
import parse_data as parser
import matplotlib.pyplot as plt


def check_time(a, b):
    print("The time taken is ", b - a, " seconds.")


def lesson4():
    def num_tut():
        # Creates 2d empty array
        print(np.empty((5, 4)))
        # Creates 2d array filled with ones with integers
        print(np.ones((5, 4), dtype=np.int))
        # Creates randomly generated numbers in array
        print(np.random.rand(5, 4))
        # Sample numbers from a Gaussian distribution
        print(np.random.normal(50, 10, size=(2, 3)))  # sets mean to 50 and s.d to 10

        # Generating random integers
        print(np.random.randint(10))  # Single integer between 0 and 10
        print(np.random.randint(0, 10))  # Same as above but explicitly
        print(np.random.randint(0, 10, size=5))  # 5 random integers as array
        print(np.random.randint(0, 10, size=(2, 3)))  # 2x3 array'''
        # Getting array size and data type

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
        print("Slicing: \n", a[:, 0:3:2])
        '''
        gives  you 0 - (3 - 2 and then umps(2 - 1) columns
        '''
        # Assigning values

        a[0, 0] = 1
        a[0:2] = 2
        a[:, 3] = [1, 2, 3, 4, 5]

        # Accessing using indices

        indices = np.array([1, 1, 2, 3])
        print(a[indices])

        # Masking

        a = np.array([(20, 25, 10, 23, 26, 32, 10, 5, 0), (0, 2, 50, 20, 0, 1, 28, 5, 0)])
        print("Array: \n", a)
        mean = a.mean()
        # mask
        print(a[a < mean])
        a[a < mean] = mean
        print("New a \n", a)

        # Arithmetic operations

        a = np.array([(1, 2, 3, 4, 5), (10, 20, 30, 40, 50)])
        print("Original array \n", a)
        # Multiply by 2
        print("\n Multiply a by 2:\n", 2 * a)

        # Can be used to add arrays as well
        # Does element wise algorithm


def get_max_index(a):
    return a.argmax()


def lesson4_1():
    stocks = ['AAPL', 'IBM', 'GLD']
    dates = pd.date_range('2017-03-29', '2017-04-26')
    df = ob.get_data(stocks, dates)
    df = parser.normalize_data(df)
    plotter.plot_data(df)
    plotter.plot_selected(df, [2, 3], '2017-03-29', '2017-04-26')


def lesson5_1():
    # Global Statistics
    # Global statistics that can be used - mean, median, std, sum, prod, mode
    dates = pd.date_range('2017-03-29', '2017-04-26')
    stocks = ['AAPL', 'IBM', 'GLD']
    df = ob.get_data(stocks, dates)
    plotter.plot_data(df)
    print(df.mean())


def lesson5_2():
    # Rolling  statistics - mean of set windows of the data (simple moving average)
    # Suggestion for stock purchase, whenever stock falls below rolling mean, buy stock
    stocks = ['Google']
    dates = pd.date_range('2017-03-29', '2017-04-26')
    df = ob.get_data(stocks, dates)

    # Plot google data, retain matplotlib axis object
    ax = df['Google'].plot(title='Google Rolling mean', label="Google")
    # Complete Rolling mean using 4 day window
    # Switched to version that isn't being removed
    rm_google = pd.Series.rolling(df['Google'], window=4, center=False).mean()
    print(rm_google)
    rm_google.plot(label="Rolling mean", ax=ax)
    ax.set_xlabel("Date")
    ax.set_ylabel('Price')
    ax.legend(loc="upper left")
    # Used to actually show plot
    plt.show()
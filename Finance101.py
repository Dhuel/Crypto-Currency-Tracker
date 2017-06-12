import pandas as pd
import Final as final
import os
import matplotlib.pyplot as plt
import time
import get_csv_data as get
import plotting_data as plotter
import parse_data as parser
# from util import get_data, plot_data


def main():
    dates = pd.date_range('2015-05-28', '2017-05-28')
    stocks = ['AAPL','GLD','IBM','SPY']
    df = get.get_data(stocks, dates)
    parser.calculate_sharpe_ratio(df)
    # parser.test_run()
    # print(df)
    # plotter.plot_data(df)
    # plotter.plot_daily_returns(df)
    # plotter.plot_kurtosis(df, "SPY price")


if __name__ == "__main__":
    # final.f()
    main()

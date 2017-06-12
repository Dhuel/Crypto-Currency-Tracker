import pandas as pd
import get_csv_data as ob
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as spo


def normalize_data(df):
    """Normalizes data"""
    # print(df.ix[1, :])
    return df / df.ix[0, :]


def get_rolling_mean(values, window):
    """Return rolling mean of given values, using specified window size."""
    return pd.Series.rolling(values, window=window, center=False).mean()


def get_rolling_std(values, window):
    """Return rolling standard deviation of given values, using specified window size."""
    return pd.Series.rolling(values, window=window, center=False).std()


def get_bollinger_bands(rm, rstd):
    """Return upper and lower Bollinger Bands."""
    upper_band = (2 * rstd) + rm
    lower_band = (-1 * 2 * rstd) + rm
    return upper_band, lower_band


def compute_daily_returns(df):
    """Compute and return the daily return values."""
    daily_returns = df.copy()
    # NOTE values threw me off but it was explained
    daily_returns[1:] = (daily_returns[1:] / daily_returns[:-1].values) - 1
    # May need some clarification on this
    # # OR daily_returns = (df/df.shift(1))-1  still have to set first row to 0
    daily_returns.ix[0, :] = 0
    # print(daily_returns)
    return daily_returns


def bollinger_band(n):
    # Compute Bollinger Bands
    stocks = [n]
    dates = pd.date_range('2017-03-29', '2017-04-26')
    df = ob.get_data(stocks, dates)
    # 1. Compute rolling mean
    rm_goog = get_rolling_mean(df[n], window=4)

    # 2. Compute rolling standard deviation
    rstd_goog = get_rolling_std(df[n], window=4)

    # 3. Compute upper and lower bands
    upper_band, lower_band = get_bollinger_bands(rm_goog, rstd_goog)

    # Plot raw SPY values, rolling mean and Bollinger Bands
    ax = df[n].plot(title="Bollinger Bands", label=n)
    rm_goog.plot(label='Rolling mean', ax=ax)
    upper_band.plot(label='upper band', ax=ax)
    lower_band.plot(label='lower band', ax=ax)

    # Add axis labels and legend
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend(loc='upper left')
    plt.show()


def plot_scatter(df, n, m):
    # n was "GLD ADJ and m was IBM ADJ
    daily_returns = compute_daily_returns(df)
    daily_returns.plot(kind="scatter", x=n, y=m)
    beta_XOM, alpha_XOM = np.polyfit(daily_returns[n], daily_returns[m], 1)
    print(daily_returns.corr(method='pearson'))
    plt.plot(daily_returns[n], beta_XOM * daily_returns[n] + alpha_XOM, '-', color='r')
    plt.show()


def f(x):
    y = (x - 1.5) ** 2 + 0.5
    print("X = {}, Y ={}".format(x, y))
    return y


def test_run():
    # Cant install scipy
    Xguess = 2.0
    min_result = spo.minimize(f, Xguess, method='BFGS', options={'disp': True})
    print("Minima found at:")
    print("X = {}, Y = {}".format(min_result.x, min_result.fun))

    # Xplot = np.linspace(0.5, 2.5, 21)
    # Yplot = f(Xplot)
    # plt.plot(Xplot, Yplot)
    # plt.plot(min_result.x, min_result.fun, 'ro')
    # plt.title("Minima of an objective function")
    # plt.show()


def error(line, data):
    err = np.sum((data[:, 1]-(line[0] * data[:, 0] + line[1]))**2)
    return err

'''
was not clear Lesson 9 - video 9
def test_run2():
    # Define original line
    l_orig = np.float32([4, 2])
    print("Original line: C0 = {}, C1 = {}".format(l_orig[0], l_orig[1]))
    Xorig = np.linspace(0, 10, 21)
    Yorig = l_orig[0] * Xorig + l_orig[1]
    plt.plot(Xorig, Yorig, 'b--', linewidth=2.0, label="Original line")

    # Generate noisy data points
    noise_sigma = 3.0
    noise = np.random.normal(0, noise_sigma, Yorig.shape)
    data = np.asarray(Xorig, Yorig + noise]).T
    plt.plot(data[:,0], data[:,1], 'go', label="Data points")
'''


def daily_portfolio_value(df, alloc, start_val):
    # print(alloc)
    normed = normalize_data(compute_daily_returns(df)[1:])
    # print(normed)
    normed.ix[:, 0] = normed.ix[:, 0] * alloc[0]
    normed.ix[:, 1] = normed.ix[:, 1] * alloc[1]
    normed.ix[:, 2] = normed.ix[:, 2] * alloc[2]
    normed.ix[:, 3] = normed.ix[:, 3] * alloc[3]
    alloc = normed
    pos_val = alloc*start_val
    port_val = pos_val.sum(axis=1)
    return port_val


def cum_ret(df):
    return (df[-1]/df[0])-1

'''
def avg_daily_ret(df):
    return compute_daily_returns(df)[1:].mean()


def std_daily_ret(df):
    return compute_daily_returns(df)[1:].std()

'''


'''
Determines the risk and return of a  stock
'''


def sharpe(df, daily_rfr):
    # Lesson 8 - sharpe ratio
    df[1:] = (df[1:] / df[:-1].values) - 1
    daily_ret = df[1:]
    sharpe_ratio = ((daily_ret - daily_rfr).mean())/((daily_ret - daily_rfr).std())
    return sharpe_ratio


def calculate_sharpe_ratio(df):
    q = 0.4
    w = 0.4
    e = 0.2
    r = 0.2
    min_result = spo.minimize(full_sharpe_eqn(df, 0, q, w, e, r, 100), [q, w, e, r], method='SLSQP', options={'disp': True})
    print(min_result)


def minimize_sharpe(q, w, e, r, df):
    daily_port = daily_portfolio_value(df, [q, w, e, r], start_val=100)
    sharpe_ratio = sharpe(daily_port, 0)
    return sharpe_ratio-1


def full_sharpe_eqn(df, daily_rfr, q, w, e, r, start_val):
    # print("start of minimize_sharpe section")
    # print("start of daily portfolio value section")
    # print("start of normalize section")
    # print("start of compute daily returns section")
    daily_returns = df.copy()
    daily_returns[1:] = (daily_returns[1:] / daily_returns[:-1].values) - 1
    daily_returns.ix[0, :] = 0
    normed = daily_returns[1:]
    print("end of compute daily returns section \n", normed)
    normed = normed / normed.ix[0, :]
    print("end of normalize section\n", normed)
    normed.ix[:, 0] = normed.ix[:, 0] * q
    normed.ix[:, 1] = normed.ix[:, 1] * w
    normed.ix[:, 2] = normed.ix[:, 2] * e
    normed.ix[:, 3] = normed.ix[:, 3] * r
    alloc = normed
    pos_val = alloc * start_val
    port_val = pos_val.sum(axis=1)
    print("end of  daily portfolio value section\n", port_val)
    # print("start of sharpe section")
    port_val[1:] = (port_val[1:] / port_val[:-1].values) - 1
    daily_ret = port_val[1:]
    sharpe_ratio = ((daily_ret - daily_rfr).mean()) / ((daily_ret - daily_rfr).std())
    print("end of sharpe section", sharpe_ratio)
    sharpe_ratio = sharpe_ratio - 1
    return sharpe_ratio
    # print("end of minimize_sharpe section")


def full_sharpe_eqn2(df, daily_rfr, q, w, e, r, start_val):
    # print("start of minimize_sharpe section")
    # print("start of daily portfolio value section")
    # print("start of normalize section")
    # print("start of compute daily returns section")
    daily_returns = df.copy()
    daily_returns[1:] = (daily_returns[1:] / daily_returns[:-1].values) - 1
    daily_returns.ix[0, :] = 0
    normed = daily_returns[1:]
    normed = normed / normed.ix[0, :]
    normed.ix[:, 0] = normed.ix[:, 0] * q
    normed.ix[:, 1] = normed.ix[:, 1] * w
    normed.ix[:, 2] = normed.ix[:, 2] * e
    normed.ix[:, 3] = normed.ix[:, 3] * r
    sharpe_ratio = ((((normed * start_val)(axis=1)[1:] / (normed * start_val).sum(axis=1)[:-1].values)
                     - 1 - daily_rfr).mean()) / ((((normed * start_val).sum(axis=1)[1:] /
                                                   (normed * start_val).sum(axis=1)[:-1].values) -
                                                  1 - daily_rfr).std()) - 1
    return sharpe_ratio
    # print("end of minimize_sharpe section")

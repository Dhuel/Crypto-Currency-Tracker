import matplotlib.pyplot as plt
import parse_data as parser


def plot_selected(df, columns, start_index, end_index):
    """Plot the desired columns over index values in the given range. Uses indices in column field"""
    plot_data(df.ix[start_index:end_index, columns], title="Selected data")


def plot_data(df, title="Stock prices", xlabel="Date", ylabel="Price"):
    """Plot stock prices with a custom title and meaningful axis labels."""
    ax = df.plot(title=title, fontsize=12)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.show()


def plot_daily_returns(df):
    daily_returns = parser.compute_daily_returns(df)
    plot_data(daily_returns, title="Daily returns", ylabel="Daily returns")


def plot_kurtosis(df, n):
    # Lesson 7 - Unable to get util
    # positive kurtosis = fat tail - more likely to give back positive returns=
    # negative kurtosis - skinny tails
    # daily returns
    daily_returns = parser.compute_daily_returns(df)

    # plot_data(daily_returns, title='Daily returns', ylabel='Daily returns', xlabel='Dates')
    # Doesnt look right
    daily_returns.hist()

    # plt.show()
    mean = daily_returns[n].mean()
    print("mean = ", mean)
    std = daily_returns[n].std()
    print("std = ", std)
    plt.axvline(mean, color='w', linestyle='dashed', linewidth=2)
    plt.axvline(std, color='r', linestyle='dashed', linewidth=2)
    plt.axvline(-std, color='r', linestyle='dashed', linewidth=2)
    plt.show()
    print(daily_returns.kurtosis())


def plot_daily_returns(df):
    daily_returns = parser.compute_daily_returns(df)
    # plot_data(daily_returns, title='Daily returns', ylabel='Daily returns', xlabel='Dates')
    # daily_returns['IBM ADJ'].hist(label="IBM")
    # daily_returns['GLD ADJ'].hist(label="GLD")
    daily_returns.hist()
    plt.legend(loc='upper right')
    plt.show()
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from statistics import Statistics
from computereturns import ComputeReturns


base_dir = os.getcwd()
def symbol_to_path(symbol):
    """Return CSV file path given feature."""
    base_dir = os.getcwd()
    return os.path.join(base_dir, "BitcoinData", (str(symbol)))


def get_data(symbols, dates):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    df = pd.DataFrame(index=dates)

    for symbol in symbols:
        location = os.path.join(base_dir, "BitcoinData", symbol)
        df_temp = pd.read_csv(location, index_col=0, parse_dates=True, \
                            infer_datetime_format=True, dayfirst=True, \
                            na_values=['nan'], header=None,
                          names=['date', symbol.replace('.csv', '')])
        df_temp.dropna()
        df_temp.index = df_temp.index.normalize()
        df_temp = normalize_data(df_temp)
        df = df.join(df_temp)
        df.dropna()

    return df


def get_btc(location, btc_file):
    df_btc = pd.read_csv(location, index_col=0, parse_dates=True, \
                        infer_datetime_format=True, dayfirst=True, \
                        na_values=['nan'], header=None,
                      names=['date', btc_file.replace('.csv', '')])
    df_btc.dropna()
    df_btc.index = df_btc.index.normalize()
    return df_btc


def normalize_data(df):
  """Normalize data using the first row of the dataframe."""
  return df / df.ix[0, :]


def plot_data(df, title="Stock prices", xlabel="Date", ylabel="Price"):
    """Plot stock prices with a custom title and meaningful axis labels."""
    title = title.strip('.csv')
    ax = df.plot(title=title, fontsize=12)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.show()


def plot_selected(df, columns, start_index, end_index):
    """Plot the desired columns over index values in the given range."""
    df = normalize_data(df)
    plot_data(df.ix[start_index:end_index, columns], "Bitcoin")


def test_run():
    # Define a date range
    dates = pd.date_range('2015-04-02', '2016-04-01')

    # Choose feature symbols to read
    location = os.path.join(base_dir, "BitcoinData")
    symbols = os.listdir(location)

    #build dataframe consisting of all features
    df = get_data(symbols, dates)

    for index in range(len(symbols)):
        symbols[index] = symbols[index].strip('.csv')

    #plot dataframe in selected range and given features list
    #plot_selected(df, symbols, '2015-05-01', '2015-06-01')
    #plot dataframe for all given data
    #plot_data(df, "Bitcoin")

    btc_file = "bitcoin-market-price.csv"
    location = os.path.join(base_dir, btc_file)
    df_btc = get_btc(location, btc_file)
    stats = Statistics(df, symbols)
    rmean = stats.get_rolling_mean(df_btc['bitcoin-market-price'], window=20)
    rstd = stats.get_rolling_std(df_btc.ix[:, 'bitcoin-market-price'], window=20)
    upper_band, lower_band = stats.get_bollinger_bands(rmean, rstd)

    # Plot raw SPY values, rolling mean and Bollinger Bands
    ax = df_btc['bitcoin-market-price'].plot(title="Bollinger Bands", \
                                            label='bitcoin-market-price')
    rmean.plot(label='Rolling mean', ax=ax)
    upper_band.plot(label='upper band', ax=ax)
    lower_band.plot(label='lower band', ax=ax)

    # Add axis labels and legend
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend(loc='upper left')
    plt.show()

    #compute daily returns
    returns = ComputeReturns(df)
    daily_returns = returns.compute_daily_returns(df)
    plot_data(daily_returns, title="Daily returns", ylabel="Daily returns")


if __name__ == "__main__":
    test_run()

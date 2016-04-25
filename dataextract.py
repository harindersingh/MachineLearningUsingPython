import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


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


def normalize_data(df):
  """Normalize data using the first row of the dataframe."""
  return df / df.ix[0, :]


def plot_data(df, title):
    """Plot stock prices with a custom title and meaningful axis labels."""
    title = title.strip('csv')
    ax = df.plot(title=title, fontsize=12)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
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
    plot_selected(df, symbols, '2015-05-01', '2015-06-01')
    #plot dataframe for all given data
    plot_data(df, "Bitcoin")


if __name__ == "__main__":
    test_run()

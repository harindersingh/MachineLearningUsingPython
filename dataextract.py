import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


def symbol_to_path(symbol):
    """Return CSV file path given feature."""
    base_dir = os.getcwd()
    return os.path.join(base_dir, "BitcoinData", (str(symbol)))


def get_data(symbols, dates):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    df = pd.DataFrame()

    for symbol in symbols:
        df_temp = pd.read_csv(symbol_to_path(symbol), index_col=0, parse_dates=True, \
                            infer_datetime_format=True, na_values=['nan'])
        print df_temp.head()
        df = df.join(df_temp)
        df = df.dropna()

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

    base_dir = os.getcwd()

    # Choose feature symbols to read
    #symbols = ['avg_block_size', 'block_size', 'hash_rate', 'difficulty']
    location = os.path.join(base_dir, "BitcoinData")
    symbols = os.listdir(location)

    #df = get_data(symbols, dates)

    #plot_selected(df, symbols, '2015-05-01', '2015-06-01')
    df = pd.DataFrame(index=dates)
    for symbol in symbols:
        location = os.path.join(base_dir, "BitcoinData", symbol)
        df_temp = pd.read_csv(location, index_col=0, parse_dates=True, infer_datetime_format=True, dayfirst=True, na_values=['nan'])
        df_temp.dropna()
        df_temp.index = df_temp.index.normalize()
        #have to drop first row in the final dataframe because of no naming present
        df_temp = normalize_data(df_temp)
        #print df_temp.index
        #plot_data(df_temp, symbol)
        df = df.join(df_temp)
        #plot_data(df_temp, symbol)
        #Get stock data
        #df = get_data(symbols, dates)

    print df.head()
    df.dropna()
    plot_data(df, "Bitcoin")
    for symbol in symbols:
        symbol.strip('.csv')
    # Slice and plot
    #plot_selected(df, symbols, '', '')

if __name__ == "__main__":
    test_run()

import pandas as pd
import os


class DataReader(object):
    base_dir = os.getcwd()
    def __init__(self):
        pass


    def symbol_to_path(symbol):
        """Return CSV file path given feature."""
        base_dir = os.getcwd()
        return os.path.join(base_dir, "BitcoinData", (str(symbol)))


    def get_data(self, location, symbols, dates):
        """Read stock data (adjusted close) for given symbols from CSV files."""
        df = pd.DataFrame(index=dates)

        for symbol in symbols:
            templocation = os.path.join(location, symbol)
            df_temp = pd.read_csv(templocation, index_col=0, parse_dates=True, \
                                infer_datetime_format=True, dayfirst=True, \
                                na_values=['nan'], header=None,
                              names=['date', symbol.replace('.csv', '')])
            df_temp.dropna()
            df_temp.index = df_temp.index.normalize()
            df = df.join(df_temp)
            df.dropna()

        return df


    def get_btc(self, location, btc_file):
        df_btc = pd.read_csv(location, index_col=0, parse_dates=True, \
                            infer_datetime_format=True, dayfirst=True, \
                            na_values=['nan'], header=None,
                          names=['date', btc_file.replace('.csv', '')])
        df_btc.dropna()
        df_btc.index = df_btc.index.normalize()
        return df_btc

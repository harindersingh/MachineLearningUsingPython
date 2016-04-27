import pandas as pd
import os

class Statistics:
    def __init__(self, dataframe):
        self.dataframe = dataframe


    def compute_daily_returns(self, df):
        """
        1. Daily returns
            daily_ret[t] = (price[t]/price[t-1]) - 1
        2. Cumulative returns
            cumret[t] = (price[t]/price[0]) - 1
        """
        """Compute and return the daily return values."""
        # daily_returns = df.pct_change()
        # Daily return values for the first date cannot be calculated. Set these to zero.
        # daily_returns.ix[0, :] = 0

        # Alternative method
        # daily_returns = (df / df.shift(1)) - 1
        daily_returns = df.copy()
        daily_returns[1:] = (df[1:] / df[:-1].values)
        daily_returns.ix[0, :] = 0
        return daily_returns


    def get_rolling_mean(self, values, window):
        """Return rolling mean of given values, using specified window size."""
        return values.rolling(window, center=False).mean()


    def get_rolling_std(self, values, window):
        """Return rolling standard deviation of given values, using specified window size."""
        return values.rolling(window, center=False).std()


    def get_bollinger_bands(self, rmean, rstd):
        """Return upper and lower Bollinger Bands."""
        upper_band = rmean + 2*rstd
        lower_band = rmean - 2*rstd
        return upper_band, lower_band

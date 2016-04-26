import pandas as pd
import os

class Statistics:
    def __init__(self, dataframe, columns):
        self.dataframe = dataframe
        self.columns = columns


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

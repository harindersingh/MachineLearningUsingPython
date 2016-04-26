import pandas as pd
import os


class Utility:
    def __init__(self):
        pass


    def timing(func, *args):
        # Timing Python operations
        pass


    def normalize_data(self, df):
      """Normalize data using the first row of the dataframe."""
      return df / df.ix[0, :]


    def fill_missing_values(self, df_data):
        """
        Dealing with missing data:
        1. Fill forward (to avoid peeking into the future)
        2. Fill backward
        """
        """Fill missing values in data frame, in place."""
        df_data.fillna(method='ffill', inplace=True)
        df_data.fillna(method='bfill', inplace=True)
        return df_data

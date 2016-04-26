"""
Daily returns
daily_ret[t] = (price[t]/price[t-1]) - 1
Cumulative returns
cumret[t] = (price[t]/price[0]) - 1
"""


import pandas as pd


class ComputeReturns():

    def __init__(self, df):
        self.df = df


    def compute_daily_returns(self, df):
        """Compute and return the daily return values."""
        daily_returns = df.pct_change()
        # Daily return values for the first date cannot be calculated. Set these to zero.
        daily_returns.ix[0, :] = 0

        # Alternative method
        # daily_returns = (df / df.shift(1)) - 1
        # daily_returns.ix[0, :] = 0
        return daily_returns

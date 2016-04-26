import pandas as pd
import matplotlib.pyplot as plt
import os
from utility import Utility
"""
kurtosis (quantifies whether the shape of the data distribution matches the Gaussian distribution)
  + fat tails
  - skinny tails

Scatterplots
  slope (Beta): how reactive a stock is to the market - higher Beta means
the stock is more reactive to the market
NOTE: slope != correlation
correlation is a measure of how tightly do the individual points fit the line

  intercept (alpha): +ve --> the stock on avg is performing a little bit better
than the market
In many cases in financial research we assume the daily returns are normally distributed,
but this can be dangerous because it ignores kurtosis or the probability in the
tails.
"""

class Plotting(object):
    def __init__(self):
        pass


    def plot_data(self, df, title="Bitcoin Data", xlabel="Date", ylabel="Price"):
        """Plot stock prices with a custom title and meaningful axis labels."""
        title = title.strip('.csv')
        ax = df.plot(title=title, fontsize=12)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        plt.show()


    def plot_selected(self, df, columns, start_index, end_index):
        """Plot the desired columns over index values in the given range."""
        util = Utility()
        df = util.normalize_data(df)
        self.plot_data(df.ix[start_index:end_index, columns], "Bitcoin")

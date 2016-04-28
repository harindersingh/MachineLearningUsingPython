import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datareader import DataReader
from statistics import Statistics
from dataplotting import DataPlotting
from utility import Utility


base_dir = os.getcwd()


def test_run():
    # Define a date range
    dates = pd.date_range('2015-04-02', '2016-04-01')

    # Choose feature symbols to read
    location = os.path.join(base_dir, "BitcoinData")
    symbols = os.listdir(location)

    #build dataframe consisting of all features
    dfreader = DataReader()
    util = Utility()
    location = os.path.join(base_dir, "BitcoinData")
    df = dfreader.get_data(location, symbols, dates)
    df = util.normalize_data(df)

    for index in range(len(symbols)):
        symbols[index] = symbols[index].strip('.csv')

    plotter = DataPlotting()
    #plot dataframe in selected range and given features list
    #plotter.plot_selected(df, symbols, '2015-05-01', '2015-06-01')
    #plot dataframe for all given data
    #plotter.plot_data(df, "Bitcoin")

    dates = pd.date_range('2010-01-01', '2016-01-01')
    btc_file = "bitcoin-market-price.csv"
    location = os.path.join(base_dir, btc_file)
    df_btc = dfreader.get_btc(location, btc_file, dates)

    stats = Statistics(df)
    rmean = stats.get_rolling_mean(df_btc['bitcoin-market-price'], window=20)
    rstd = stats.get_rolling_std(df_btc.ix[:, 'bitcoin-market-price'], window=20)
    upper_band, lower_band = stats.get_bollinger_bands(rmean, rstd)

    # Plot raw values, rolling mean and Bollinger Bands
    ax = df_btc['bitcoin-market-price'].plot(title="Bollinger Bands", \
                                            label='bitcoin-market-price')
    rmean.plot(label='Rolling mean', ax=ax)
    upper_band.plot(label='upper band', ax=ax)
    lower_band.plot(label='lower band', ax=ax)

    # Add axis labels and legend
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend(loc='upper left')
    #plt.show()

    #compute daily returns
    daily_returns = stats.compute_daily_returns(df_btc)
    #plotter.plot_data(daily_returns, title="Daily returns", ylabel="Daily returns")

    daily_returns.replace(to_replace=np.inf, value=np.NaN, inplace=True)
    # Plot a histogram
    daily_returns.hist(bins=21)

    # Get mean as standard deviation
    mean = daily_returns.mean()
    std = daily_returns.std()

    #print type(mean)
    plt.axvline(mean[0], color='w', linestyle='dashed', linewidth=2)
    plt.axvline(std[0], color='r', linestyle='dashed', linewidth=2)
    plt.axvline(-std[0], color='r', linestyle='dashed', linewidth=2)
    plt.show()

    # Scatterplots
    df.plot(kind='scatter', x='hash_rate', y='market_cap')
    beta_XOM, alpha_XOM = np.polyfit(df['hash_rate'], df['market_cap'], 1)  # fit poly degree 1
    #plt.plot(df['hash_rate'], beta_XOM*df['market_cap'] + alpha_XOM, '-', color='r')
    plt.show()

    # Calculate correlation coefficient
    daily_returns.corr(method='pearson')


if __name__ == "__main__":
    test_run()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.style as style
style.use('ggplot')

import pandas_datareader as web
import datetime as dt
import mplfinance as mpf

class Analysis:

    def __init__(self, ticker, start):
        
        data = pd.read_csv('data/{}_{}.csv'.format(ticker, start), index_col='Date')
        data.index = pd.to_datetime(data.index)

        outlier_data = pd.read_csv('data/{}_{}_CLEANED_OUTLIERS.csv'.format(ticker, start))
        self.outlier_data = outlier_data

        self.ticker = ticker
        self.data = data
        self.start = start
    
    # basic line plot
    def adj_close(self):
        data = self.data
        date = data.index
        adj_close = data['Adj Close']

        fig = plt.figure(figsize=(12,6))
        plt.plot(date, adj_close, c='r')
        plt.title('{} Adj Close Price'.format(self.ticker))
        plt.show()

    # candlistick charts
    def candlestick(self):
        data = self.data

        colors = mpf.make_marketcolors(up='#00ff00',
                                    down='#ff0000',
                                    wick='inherit',
                                    edge='inherit',
                                    volume='in')

        mpf_style = mpf.make_mpf_style(base_mpf_style='mike', marketcolors=colors)
        mpf.plot(data, type='line', style=mpf_style, volume=True)

    # average of past n values to today
    def moving_average(self):
        data = self.data
        date = data.index

        adj_cl = data['Adj Close']
        moving_avg = adj_cl.rolling(window=7).mean() # the window decides the number of trading days

        fig = plt.figure(figsize=(12,6))
        plt.plot(date, moving_avg, c='blue', label='Moving Average')
        plt.plot(date, adj_cl, c='red', label='Adj Close')
        # plt.title('{} Moving Avg vs Adj Close'.format(self.ticker))
        plt.legend()
        plt.show()

    def plot_outliers(self):
        outlier_data = self.outlier_data
        outliers = outlier_data[outlier_data['Outlier'] == -1] 

        days = 20
        moving_avg = outlier_data['Adj Close'].rolling(window=days).mean() # the window decides the number of trading days
        
        fig = plt.figure(figsize=(16,8))
        ax = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # main axes
        
        ax.plot(outlier_data['Date'], outlier_data['Adj Close'], label='Adjusted Close', c='g')
        ax.scatter(outliers['Date'], outliers['Adj Close'], label='Outliers', c='b')
        ax.plot( moving_avg, label='Moving Average {}'.format(days), c='r')
        ax.legend()
        ax.set_xticks(outlier_data['Date'][::5])
        
        plt.title('{} Outliers'.format(self.ticker)) 
        plt.savefig('graphs/{}_{}_Outliers'.format(self.ticker, self.start))
        plt.show()
        

    
    
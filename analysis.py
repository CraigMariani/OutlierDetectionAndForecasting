import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.style as style
style.use('ggplot')

import pandas_datareader as web
import datetime as dt
import mplfinance as mpf

class Analysis:

    def __init__(self, ticker):
        
        data = pd.read_csv('data/{}.csv'.format(ticker), index_col='Date')
        data.index = pd.to_datetime(data.index)

        self.ticker = ticker
        self.data = data
    
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

    # draws vetical lines on x axis for adj Close price
    def season_comparison(self):
        data = self.data
        date = pd.Series(data.index).astype(str)
        

        years = date.str.split('-').str[0]
        
        adj_close = data['Adj Close']

        

        fig = plt.figure(figsize=(12,6))
        plt.plot(date, adj_close, c='r')
        plt.title('{} Adj Close Price (With Seasonal Comparison)'.format(self.ticker))
        for yr in years:
            # plt.axvline(pd.to_datetime(str(time)+'-01-01'), color='k', linestyle='--', alpha=0.2)
            time_period = pd.to_datetime(str(yr)+'-01-27').year
            plt.axvline(time_period, color='k', linestyle='--', alpha=0.2)
        plt.show()
    
    # average of past n values to today
    def moving_average(self):
        data = self.data
        date = data.index

        adj_cl = data['Adj Close']
        moving_avg = adj_cl.rolling(window=7).mean() # the window decides the number of trading days

        fig = plt.figure(figsize=(12,6))
        plt.plot(date, moving_avg, c='blue', label='Moving Average')
        plt.plot(date, adj_cl, c='red', label='Adj Close')
        plt.title('{} Moving Avg vs Adj Close'.format(self.ticker))
        plt.legend()
        plt.show()

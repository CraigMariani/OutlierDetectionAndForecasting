import datetime
import mplfinance as mpf
import numpy as np
import pandas as pd
import pandas_datareader as web


class Extract:

    def __init__(self, ticker):
        # looking two months back
        self.start = datetime.datetime(2020, 10, 10)
        self.end = datetime.datetime.now()
        # print(self.end)
        self.ticker = ticker

    def  read_data(self):
        ticker_data = web.DataReader(self.ticker, 'yahoo', self.start, self.end)
        ticker_data.index = pd.to_datetime(ticker_data.index)
        return ticker_data

    def convert_csv(self, ticker_data):
        ticker_data.to_csv('data/{}.csv'.format(self.ticker))

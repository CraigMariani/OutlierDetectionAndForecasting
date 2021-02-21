import pandas as pd

from extract import Extract
from analysis import Analysis


def main():

    # ticker = 'GME'
    ticker = 'BTC-USD'

    # ext = Extract(ticker=ticker)
    # data = ext.read_data()
    # ext.convert_csv(data)

    ans = Analysis(ticker=ticker)
    # ans.adj_close()
    # ans.candlestick()
    # ans.season_comparison()
    ans.moving_average()

if __name__ == '__main__':
    main()
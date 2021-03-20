import pandas as pd
import datetime

from extract import Extract
from analysis import Analysis
from isolation_forests import Forest

def main():

    ticker = 'GME' # Gamestop
    # ticker = 'BTC-USD' # Bitcoin 
    # ticker = '^GSPC' # S&P 500 index

    start = datetime.date(2021, 1, 1) # start looking at the stock
    ext = Extract(ticker=ticker, start=start)
    data = ext.read_data()
    ext.convert_csv(data)
    
    fst = Forest(ticker=ticker, start=start)
    fst.model_outliers()

    ans = Analysis(ticker=ticker, start=start)
    ans.plot_outliers()
    

if __name__ == '__main__':
    main()
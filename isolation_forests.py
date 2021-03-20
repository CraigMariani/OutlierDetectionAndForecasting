import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split 
from sklearn.pipeline import make_pipeline
from sklearn.ensemble import IsolationForest

'''
Isolation Forest:
after training the model, the output will be either 
    -1 : outlier 
    1  : inlier
'''

class Forest:

    def __init__(self, ticker, start):
        data = pd.read_csv('data/{}_{}.csv'.format(ticker, start), index_col='Date')
        data.index = pd.to_datetime(data.index)

        self.ticker = ticker
        self.data = data
        self.start = start
    
    
    def model_outliers(self):
        train_data = self.data
        # isolation forest model, it has 100 estimators
        iso_model = IsolationForest(n_estimators=)


        train_adj_close = np.array(train_data['Adj Close']).reshape(-1, 1)
        iso_model.fit(train_adj_close)

        # looking for outliers by testing the already trained data outliers (-1) and inliers (1)
        results = iso_model.predict(train_adj_close)
        train_data2 = train_data.copy()
        train_data2['Outlier'] = results
        
        outliers = train_data2.loc[train_data2['Outlier'] == -1]
        norms = train_data2.loc[train_data2['Outlier'] == 1]
        
        # see how many outliers
        # print(train_data2['Outlier'].value_counts())

        # determine intensity of outliers
        intensity = iso_model.decision_function(train_adj_close) 
        train_data2['Outlier_Intensity'] = intensity

        
        train_data2.to_csv('data/{}_{}_CLEANED_OUTLIERS.csv'.format(self.ticker, self.start))
    
    def model_novelties(self):
        pass



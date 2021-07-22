import pandas as pd
import matplotlib.pyplot as plt
import os
import glob
import datetime as dt


data = pd.read_csv('downstairs_train.csv')

data = data[(data != 0).all(1)]
data = data[(data != 0.0).all(1)]
data = data[(data != -0.0).all(1)]
data = data.round(decimals=4).astype(object)

data['x-axis'] = data['x-axis'].apply(lambda x: "{:.2f}".format(x))
data['y-axis'] = data['y-axis'].apply(lambda x: "{:.2f}".format(x))
data['z-axis'] = data['z-axis'].apply(lambda x: "{:.2f}".format(x))

data['timestamp'] = pd.to_timedelta(data['timestamp'].astype(str)).diff(-1).dt.total_seconds().div(60)

data.to_csv('downstairs-no-zeros.csv', index=False)


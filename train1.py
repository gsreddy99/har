import pandas as pd
import matplotlib.pyplot as plt
import os
import glob
from sklearn.preprocessing import MinMaxScaler
from pandas import DataFrame
import numpy as np

# data.to_csv('new.csv')

def convert_to_float(x):
    try:
        return np.float(x)
    except:
        return np.nan

for x in range(1,11):
    csv_file = 'NEWD/'+str(x)+'.csv'
    data = pd.read_csv(csv_file, encoding='utf-8', low_memory=False)
    # data.rename(columns={0: 'user-id', 1: 'timestamp', 2: 'accX', 3: 'accY', 4: 'accZ', 5: 'ActivityEncoded'}, inplace=True)
    data["ActivityEncoded"].replace(
        {0: "Downstairs", 1: "Jogging", 2: "Sitting", 3: "Standing", 4: "Upstairs", 5: "Walking"},
        inplace=True)



    for (classification), group in data.groupby(['ActivityEncoded']):
        group.to_csv(f'NEWC/{x}_{classification}.csv', index=False)


classList = ['Downstairs', 'Jogging', 'Sitting', 'Standing', 'Upstairs', 'Walking']

for x in classList:

    df = pd.concat(map(pd.read_csv, glob.glob(f'NEWC/*{x}.csv')),ignore_index=True)
    df.reset_index(drop=True, inplace=True)
    timestamp_col = df[['timestamp']]

    del df['ActivityEncoded']
    del df['user-id']
    del df['timestamp']


    df = df[df.accX != 0]
    df = df[df.accY != 0]
    df = df[df.accZ != 0]

    #trans = MinMaxScaler()
   # df = trans.fit_transform(df)
    #df = df.values[:, :-1]
    dataset = DataFrame(df)
    #dataset['timestamp'] = timestamp_col['timestamp']
    #dataset.rename(columns={0: 'X (mg)', 1: 'Y (mg)', 2: 'Z (mg)'}, inplace=True)
    dataset = dataset.apply(pd.to_numeric)
    dataset['accZ'] = df['accZ'].astype(float)

    dataset.astype(float).round(2)
    dataset.insert(0, 'timestamp', timestamp_col['timestamp'])
    print(x)
    print(df.head())
    dataset.to_csv(f'CONCAT_NEW/{x}.csv',index=False, index_label=False)
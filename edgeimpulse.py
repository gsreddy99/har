import pandas as pd
import os
import glob

files = os.listdir('EDGED/')
#print(files)

for file in files:
    fileName = f'EDGED/{file}'
    df = pd.read_csv(fileName, skiprows=4, encoding="cp1252")

    df.drop(df.columns[[0, 2, 3, 4]], axis = 1, inplace = True)
    df.columns.values[0] = "timestamp"
    #print(df.head)
    df.to_csv(f'EDGEC/{file}',index=False , index_label=False)


activityList = ['sitting', 'standing', 'walking', 'jogging', 'upstairs', 'downstairs']

for x in activityList:
    activity_df = pd.concat(map(pd.read_csv, glob.glob(f'EDGEC/*{x}*.csv')),ignore_index=True)
    activity_df.dropna(axis=0,how='any',thresh=None,subset=None,inplace=True)
    activity_df.to_csv(f'EDGE/{x}.csv', index=False, index_label=False)

files = os.listdir('EDGED-TEST/')
#print(files)

for file in files:
    fileName = f'EDGED-TEST/{file}'
    df = pd.read_csv(fileName, skiprows=4, encoding="cp1252")

    df.drop(df.columns[[0, 2, 3, 4]], axis = 1, inplace = True)
    df.columns.values[0] = "timestamp"
    #print(df.head)
    df.to_csv(f'EDGEC-TEST/{file}',index=False , index_label=False)


activityList = ['sitting', 'standing', 'walking', 'upstairs', 'downstairs']

for x in activityList:
    print(x)
    activity_df = pd.concat(map(pd.read_csv, glob.glob(f'EDGEC-TEST/*{x}*.csv')),ignore_index=True)
    activity_df.dropna(axis=0,how='any',thresh=None,subset=None,inplace=True)
    activity_df.to_csv(f'EDGE-TEST/{x}.csv', index=False, index_label=False)
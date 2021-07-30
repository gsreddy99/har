import pandas as pd
import os
import glob

# Define the folder location for training and test data directories
trainBaseFolder = 'EDGEIMPULSE-TRAIN'
testBaseFolder = 'EDGEIMPULSE-TEST'

# Read data from training data set.
files = os.listdir(f'{trainBaseFolder}-RAW/')

# Read all the files from training data folder
for file in files:
    fileName = f'{trainBaseFolder}-RAW/{file}'
    df = pd.read_csv(fileName, skiprows=4, encoding="cp1252")
    # drop the columns which are not required for edgeimpulse
    df.drop(df.columns[[0, 2, 3, 4]], axis = 1, inplace = True)
    # populate timestamp in the data set as required by edgeimpulse
    df.columns.values[0] = "timestamp"
    df.to_csv(f'{trainBaseFolder}-CONCAT/{file}',index=False , index_label=False)

# List of all the activities that are being measured
activityList = ['sitting', 'standing', 'walking', 'jogging', 'upstairs', 'downstairs']

# Read the multiple files for each activity and concatinate for each activity
for x in activityList:
    activity_df = pd.concat(map(pd.read_csv, glob.glob(f'{trainBaseFolder}-CONCAT/*{x}*.csv')), ignore_index=True)
    activity_df.dropna(axis=0,how='any',thresh=None,subset=None,inplace=True)
    activity_df.to_csv(f'{trainBaseFolder}/{x}.csv', index=False, index_label=False)
files = os.listdir(f'{testBaseFolder}-RAW/')

# Read data from test data set.

for file in files:
    fileName = f'{testBaseFolder}-RAW/{file}'
    df = pd.read_csv(fileName, skiprows=4, encoding="cp1252")

    df.drop(df.columns[[0, 2, 3, 4]], axis = 1, inplace = True)
    df.columns.values[0] = "timestamp"
    df.to_csv(f'{testBaseFolder}-CONCAT/{file}',index=False , index_label=False)

# List of all the activities that are being measured
activityList = ['sitting', 'standing', 'walking', 'jogging', 'upstairs', 'downstairs']

# Read the multiple files for each activity and concatinate for each activity
for x in activityList:
    activity_df = pd.concat(map(pd.read_csv, glob.glob(f'{testBaseFolder}-CONCAT/*{x}*.csv')), ignore_index=True)
    activity_df.dropna(axis=0,how='any',thresh=None,subset=None,inplace=True)
    activity_df.to_csv(f'{testBaseFolder}/{x}.csv', index=False, index_label=False)
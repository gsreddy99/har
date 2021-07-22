import pandas as pd
import matplotlib.pyplot as plt
import os
import glob

'''
for x in range(1,16):
    csv_file = 'HAR/'+str(x)+'.csv'
    df = pd.read_csv(csv_file, header=None)
    df.rename(columns={0: 'timestamp', 1: 'accX', 2: 'accY',3: 'accZ',4: 'class'}, inplace=True)
    df.to_csv(csv_file, index=False)


for x in range(1,16):
    csv_file = 'HAR/'+str(x)+'.csv'
    data_category_range = csv_file['class'].unique()
    data_category_range = data_category_range.tolist()
    for i,value in enumerate(data_category_range):
        csv_file[csv_file['class'] == value].to_csv(str(x)+'_'+str(value)+'.csv',index = False, na_rep = 'N/A')


csv_file = '1.csv'
df = pd.read_csv(csv_file, header=None)
for i, x in df.groupby('class'):
    p = os.path.join(os.getcwd(), "data_{}.csv".format(i.lower()))
    x.to_csv(p, index=False)
'''

csv_file = 'NEWD/1.csv'
df = pd.read_csv(csv_file, header=None)
'''
df.rename(columns={ 0: 'index', 1: 'class', 2: 'timestamp', 3: 'accX', 4: 'accY', 5: 'accZ'}, inplace=True)
df.to_csv(csv_file, index=False)

'''
for i, x in df.groupby('class'):
    p = os.path.join(os.getcwd(), "data_{}.csv".format(i.lower()))
    x.to_csv(p, index=False)


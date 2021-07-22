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


# data.to_csv('new.csv')

for x in range(1,16):
    csv_file = 'HAR/'+str(x)+'.csv'
    data = pd.read_csv(csv_file)
    data["class"].replace(
        {1: "computer", 2: "standing-up", 3: "standing", 4: "walking", 5: "stairs", 6: "walk-talk", 7: "stand-talk"},
        inplace=True)
    for (classification), group in data.groupby(['class']):
        group.to_csv(f'HARC/{x}_{classification}.csv', index=False)


classList = ['computer', 'standing-up', 'standing', 'walking', 'stairs', 'walk-talk', 'stand-talk']

for x in classList:
    print(x)
    df = pd.concat(map(pd.read_csv, glob.glob(f'HARC/*{x}.csv')),ignore_index=True)
    df["class"].replace(
        {"computer": 1, "standing-up": 2, "standing": 3, "walking": 4, "stairs": 5, "walk-talk": 6, "stand-talk": 7},
        inplace=True)
    df.reset_index(drop=True, inplace=True)
    df.to_csv(f'CONCAT/{x}.csv',index=False)

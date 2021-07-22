import pandas as pd
import matplotlib.pyplot as plt
import os
import glob

# data.to_csv('new.csv')

for x in range(1,6):
    csv_file = 'TESTD/'+str(x)+'.csv'
    data = pd.read_csv(csv_file)
    data["class"].replace(
        {1: "computer", 2: "standing-up", 3: "standing", 4: "walking", 5: "stairs", 6: "walk-talk", 7: "stand-talk"},
        inplace=True)
    for (classification), group in data.groupby(['class']):
        group.to_csv(f'TESTC/{x}_{classification}.csv', index=False)


classList = ['computer', 'standing-up', 'standing', 'walking', 'stairs', 'walk-talk', 'stand-talk']

for x in classList:
    print(x)
    df = pd.concat(map(pd.read_csv, glob.glob(f'TESTC/*{x}.csv')),ignore_index=True)
    df["class"].replace(
        {"computer": 1, "standing-up": 2, "standing": 3, "walking": 4, "stairs": 5, "walk-talk": 6, "stand-talk": 7},
        inplace=True)
    df.reset_index(drop=True, inplace=True)
    df.to_csv(f'TEST/{x}.csv',index=False)

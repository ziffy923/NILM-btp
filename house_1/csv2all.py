import pandas as pd
import os

path = '/home/ziffy/low_freq_copy/house_1/Data_csv/'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.dat' in file:
            files.append(file)
names_col = ["timestamp", "value"]

df0 =  pd.read_csv(path+files[0],names=names_col,header=0)
print(df0)

for i in range(1,len(files)):
    print(files[i])
    df =  pd.read_csv(path+files[i],names=names_col,header=0)

    df0 = df0.join(df0,on=df.index,rsuffix=files[i])#uffixes=('',files[i]))

finaldata = df0.to_csv("all_appliances_merged.csv")
    # timestamp=[]
    # value=[]
    # f=open(files[i],'r')
    # data=f.readlines()
    # for line in data:
    #     word=line.split()
    #     timestamp.append(int(word[0]))
    #     value.append(float(word[1]))
    # df=pd.DataFrame({'value':value_stove},index=utc_timestamp_stove)
    # df.to_csv(files[i]+".csv")
    # f.close()
    # print('completed',files[i])

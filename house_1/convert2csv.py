import os
import pandas as pd
# al=os.system('ls')
# print(al)
print('hshshshshshsh')
os.system('ls')

path = 'D:/BTP Project/low_freq/low_freq/house_1'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.dat' in file:
            files.append(file)

data_dict={}

for i in range(len(files)):
    timestamp=[]
    value=[]
    f=open(files[i],'r')
    data=f.readlines()
    for line in data:
        word=line.split()
        timestamp.append(int(word[0]))
        value.append(float(word[1]))
    df=pd.DataFrame({'value':value},index=timestamp)
    df.to_csv('Data_csv/'+files[i]+".csv")
    f.close()
    print('completed',files[i])

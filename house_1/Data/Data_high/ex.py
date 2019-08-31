import time
import os
import pandas as pd
f=open('D:/BTP Project/high_freq/high_freq/house_3/current_1.dat','r')
g = open('D:/BTP Project/high_freq/high_freq/house_3/voltage.dat','r')
h = open('D:/BTP Project/high_freq/high_freq/house_3/current_2.dat','r')

# files = []
# # r=root, d=directories, f = files
# for r, d, f in os.walk(path):
#     for file in f:
#         if '.dat' in file:
#             files.append(file)


data = f.readlines()
datav = g.readlines()
datac2 = h.readlines()
# for i in range(len(files)):


timestamp=[]
current_1=[]
voltage = []
current_2=[]

print(len(data))
print(len(datav))
print(len(datac2))

for i in range(52926):
    words=data[i].split()
    words2=datac2[i].split()
    words3=datav[i].split()

    utc=float(words[0])
    cycle=float(words[1])
    timestamp.append(utc)
    current_1.append(float(words[2]))
    current_2.append(float(words2[2]))
    voltage.append(float(words3[2]))

    fraction_base=utc-int(utc)
    fraction_base = 60*(1-fraction_base)
    i=1
    while (fraction_base<cycle):

        index_base=fraction_base*275/cycle
        timestamp.append(int(utc)+i)
        current_1.append(float(words[int(index_base)+2]))
        current_2.append(float(words2[int(index_base)+2]))
        voltage.append(float(words3[int(index_base)+2]))
        #print(int(utc)+i,' -> ',float(words[int(index_base)+2]))
        i=i+1
        fraction_base=fraction_base+60
    print('cycle complete')

df=pd.DataFrame({'current':current_1,'current2':current_2,'voltage':voltage},index=timestamp)

df.to_csv('Data_csv/'+"alldatahigh"+".csv")
# f.close()
print('completed csv')


print(timestamp==set(timestamp))
print('timestamp', len(timestamp))
print('set',len(set(timestamp)))
# print(timestamp)
# print("its me")
# print(current_1)




# data_dict={}

# for i in range(len(files)):
#     timestamp=[]
#     value=[]
#     f=open(files[i],'r')
#     data=f.readlines()
#     for line in data:
#         word=line.split()
#         timestamp.append(int(word[0]))
#         value.append(float(word[1]))
#     df=pd.DataFrame({'value':value},index=timestamp)
#     df.to_csv('Data_csv/'+files[i]+".csv")
#     f.close()
#     print('completed',files[i])

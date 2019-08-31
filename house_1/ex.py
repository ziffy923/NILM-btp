import time
f=open('current_1.dat','r')

data=f.readlines()
timestamp=[]
current_1=[]

for line in data:
    words=line.split()
    utc=float(words[0])
    cycle=float(words[1])
    timestamp.append(utc)
    current_1.append(words[2])

    fraction_base=utc-int(utc)
    fraction_base=60*(1-fraction_base)
    i=1
    while (fraction_base<cycle):
        index_base=fraction_base*275/cycle
        timestamp.append(int(utc)+i)
        current_1.append(float(words[int(index_base)+2]))
        #print(int(utc)+i,' -> ',float(words[int(index_base)+2]))
        i=i+1
        fraction_base=fraction_base+60
    print('cycle complete')
print(timestamp==set(timestamp))
print('timestamp', len(timestamp))
print('set',len(set(timestamp)))

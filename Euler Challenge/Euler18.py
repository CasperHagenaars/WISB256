import sys
import time
import re
import math
T1 = time.time()

f = open('euler18', 'r')
a = []
for line in f:
    h = line
    wordList = re.sub("[^\w]", " ",  h).split()
    a.append(wordList)

for i in range(1,100):
    for j in range(0,len(a[i])):
        if(int(j) == 0):
            a[i][j] = int(a[i][j]) + int(a[i-1][j])
        else:
            if(int(j) == len(a[i])-1):
                a[i][j] = int(a[i][j]) + int(a[i-1][j-1])
            else:
                    if(int(a[i-1][j]) > int(a[i-1][j-1])):
                        a[i][j] = int(a[i-1][j]) + int(a[i][j])
                    else:
                        a[i][j] = int(a[i-1][j-1]) + int(a[i][j])

record = 0
for getal in a[99]:
    if getal > record:
        record = getal
print(record)
f.close()
T2 = time.time()
print(str(T2-T1) + " seconds have passed.")
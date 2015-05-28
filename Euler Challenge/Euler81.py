import sys
import time
import re
import math
T1 = time.time()
def bestand(naam):
    f = open(str(naam), 'r')
    a = []
    for line in f:
        h = line
        wordList = re.sub("[^\w]", "\n",  h).split()
        a.append(wordList)
    f.close()
    return a
a = bestand('matrices.txt')

for i in range(80):
    for j in range(80):
        a[i][j] = int(a[i][j])
        
def doe(a):
    for i in range(80):
        for j in range(80):
            if(i == 0 and j ==0):
                continue
            if(i == 0):
                a[0][j] += a[0][j-1]
                continue
            if(j==0):
                a[i][0] += a[i-1][0]
                continue
            
            if a[i][j-1] < a[i-1][j]:
                a[i][j] += a[i][j-1]
            else:
                a[i][j] += a[i-1][j]
    return a
    
matrix = doe(a)
print(matrix[79][79])
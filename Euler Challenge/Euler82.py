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
a = bestand('matrices82.txt')
b = bestand('matrices82.txt')
for i in range(80):
    for j in range(80):
        a[i][j] = int(a[i][j])
        b[i][j] = int(b[i][j])

tesing = [[131,673,234,103,18],[201,96,342,965,150],[630,803,746,422,111],[537,699,497,121,956],[805,732,524,37,331]]
tesing2 = [[131,673,234,103,18],[201,96,342,965,150],[630,803,746,422,111],[537,699,497,121,956],[805,732,524,37,331]]
def doe(a,b,lengte):
    for kolom in range(1,lengte):
        for rij in range(lengte):
            a[rij][kolom] += a[rij][kolom-1]
        for rij in range(lengte):
            if(rij == 0):
                if(a[rij+1][kolom] + b[rij][kolom] < a[rij][kolom]):
                    a[rij][kolom] = a[rij+1][kolom]+b[rij][kolom]
            else:
                if(rij == lengte-1):
                    if(a[rij-1][kolom] + b[rij][kolom] < a[rij][kolom]):
                        a[rij][kolom] = a[rij-1][kolom]+b[rij][kolom]
                else:
                    if(a[rij-1][kolom] + b[rij][kolom] < a[rij][kolom]):
                        a[rij][kolom] = a[rij-1][kolom]+b[rij][kolom]
                        rij -=5
                    if(a[rij+1][kolom] + b[rij][kolom] < a[rij][kolom]):
                        a[rij][kolom] = a[rij+1][kolom]+b[rij][kolom]
                        rij -= 5
    return a
def calc(a,b,lengte):
    record = 100000000
    matrix = doe(a,b,lengte)
    for i in range(lengte):
        if matrix[i][lengte-1] < record:
            record = matrix[i][lengte-1]
    return record
print(calc(tesing,tesing2,5))
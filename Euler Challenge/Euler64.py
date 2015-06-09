import math
from decimal import *
import time
T1 = time.time()
getcontext().prec = 100000

def cont(x):
    repeat = []
    for i in range(25):
        y = int(x)
        repeat.append(y)
        x = 1/(x-y)
    return repeat

def check(n):
    i = ''.join(str(a) for a in n)
    lengte = 1
    print(i)
    while(i[3:3+lengte] != i[3+lengte:3+2*lengte]):
        lengte += 1
        print(lengte)
        if(len(i)<50):
            return 0
    return lengte
count = 0
verz = []
for i in range(2,101):
    sqrt = math.sqrt(i)
    if int(sqrt) == sqrt:
        continue
    aantal = check(cont(sqrt))
    if aantal % 2 == 1:
        verz.append((str(i),aantal))
        count += 1
print(count)
print(verz)
print(len(verz))
T2 = time.time()
print(T2-T1)
input()
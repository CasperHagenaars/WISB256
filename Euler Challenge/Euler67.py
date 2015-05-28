import math
from time import time
T1 = time()
voldoen = []
machten = set()
for i in range(1,10000):
    for j in range(1,30):
        macht = i**j
        if len(str(macht)) == j:
            voldoen.append(int(macht))
            machten.add(j)
            
T2 = time()
print(voldoen)
print(len(voldoen))
print(machten)
print(T2-T1)
input()
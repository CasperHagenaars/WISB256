import time
import math
import sys
T1 = time.time()
n = 1
m = 2
v = 0
fib = [1,2]
verzameling = []

while(m < 4000000):
    if(float(m)/2 == round(m/2)):
        verzameling.append(m)
    v = m
    m = m + n
    n = v

T2 = time.time()
time = str(T2 - T1)
print("Found "+ str(n)+", "+ str(m)+ ", " +str(verzameling)+ ", " +str(sum(verzameling)) + " in under " + time + ".")
print("-------------------------------------------- ")
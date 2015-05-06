import time
import math
import sys
T1 = time.time()
n = 1
m = 1
v = 0
fib = [1,2]
verzameling = []
counter = 2
while(len(str(m)) < 1000):
    v = m
    m = m + n
    n = v
    counter += 1
    
print(counter)
T2 = time.time()
time = str(T2 - T1)
print("Found "+ str(n)+", "+ str(m)+ ", " +str(verzameling)+ ", " +str(sum(verzameling)) + " in under " + time + ".")
print("-------------------------------------------- ")
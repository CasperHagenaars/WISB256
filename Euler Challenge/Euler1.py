import time
import math
import sys
T1 = time.time()
notprimes = set()
for i in range(1000):
    if(i % 3 == 0 or i % 5 == 0):
        notprimes.add(i)
print(sum(notprimes))

T2 = time.time()
time = str(T2 - T1)
print(time)
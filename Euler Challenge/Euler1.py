import time
import math
import sys
T1 = time.time()
n = 1000
counter3 = 1
counter5 = 1
notprimes = set()
while(counter3*3<n):
    notprimes.add(counter3*3)
    counter3 += 1
while(counter5*5<n):
    notprimes.add(counter5*5)
    counter5 += 1
T2 = time.time()
time = str(T2 - T1)
print("Found "+ str(sum(notprimes))+" Prime numbers smaller than "+ str(n)+ " in under " + time + ".")
print("-------------------------------------------- ")
import time
import math
import sys
T1 = time.time()
n = int(2000000)
notprimes = set()
primes = []
for counter in range(2,n):
    if counter in notprimes: 
        continue
        
    for j in range(counter*counter,n+1,counter):
            notprimes.add(j)
            
    primes.append(counter)
T2 = time.time()
time = str(T2 - T1)
print("Found "+ str(sum(primes))+" Prime numbers smaller than "+ str(n)+ " in under " + time + ".")
print("-------------------------------------------- ")
import time
import math
import sys
T1 = time.time()
n = int(1000000)
bestand = open("test.dat", 'w')
notprimes = set()
primes = []
for counter in range(2,n):
    if counter in notprimes: 
        continue
        
    for j in range(counter*counter,n+1,counter):
            notprimes.add(j)
    if(len(primes)<10001):
        primes.append(counter)

bestand.write("\n".join(map(str,primes)))
bestand.close()
T2 = time.time()
time = str(T2 - T1)
print("Found "+ str(len(primes))+" Prime numbers smaller than "+ str(primes[-1])+ " in under " + time + ".")
print("-------------------------------------------- ")
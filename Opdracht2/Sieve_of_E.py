import time
import math
import sys
T1 = time.time()
n = int(sys.argv[1])
bestand = open(sys.argv[2], 'w')
notprimes = set()
primes = []
for counter in range(2,n+1):
    if counter in notprimes: 
        continue
        
    for j in range(counter*counter,n+1,counter):
            notprimes.add(j)
            
    primes.append(counter)
bestand.write("\n".join(map(str,primes)))
bestand.close()
T2 = time.time()
time = str(T2 - T1)
time = time[:19]
print("Found "+ str(len(primes))+" Prime numbers smaller than "+ str(n)+ " in " + time + " sec.")
print("--------------------------------------------")

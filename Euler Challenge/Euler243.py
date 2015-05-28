from fractions import *
import time
import math
from decimal import *
getcontext().prec = 5
T1 = time.time()
def primenumbers(L):
    notprimes = set()
    primes = []
    for counter in range(2,L):
        if counter in notprimes: 
            continue
        
        for j in range(counter*counter,L+1,counter):
            notprimes.add(j)
                    
        primes.append(counter)
    return primes 
priem = primenumbers(1000)
begin = 1 
priems = set()
for i in priem:
    if(93744*begin < 15499):
        print(priems)
    else:
        begin *= (1-1/i)
        priems.add(i)
        print(begin)


T2 = time.time()
print(str(T2-T1) + " seconden.")
input()
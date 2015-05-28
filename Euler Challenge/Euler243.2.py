from fractions import *
import time
import math
from decimal import *
getcontext().prec = 2
cons1 = Decimal(15499)/Decimal(94744)
cons = 15499/94744
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
priem = primenumbers(50000)

T2 = time.time()
print(T2-T1)
def totient(a):
    getal = a
    priemdelers = set()
    for i in priem:
        if i < int(math.sqrt(a)+1):
            if((a/i) % 1 == 0):
                priemdelers.add(i)
                continue
        else:
            break
    for x in priemdelers:
        getal *= (1-1/x)
    return int(getal)
def finder():
    i = 5105100
    record = 1
    while(True):
        if(totient(i)*94744 < (i-1)*15499):
            return i
        else:
            i += 1
    
print(finder())

T3 = time.time()
print(T3-T2)
input()
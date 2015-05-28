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
priem = primenumbers(10000000)
T2 = time.time()

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

def finder(begin,aantal):
    i = begin
    record = 1
    while(i-begin < aantal):
        if(totient(i)*94744 < (i-1)*15499):
            return i
        else:
            if(r12 < record):
                record = r12
                print(record)
                print(i)
            i += 1
    return (str(record)+ str(aantal))
    
print(finder(223092869,10))

T3 = time.time()
print(T3-T2)
input()
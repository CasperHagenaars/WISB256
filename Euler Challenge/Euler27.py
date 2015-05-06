import time
import math
import sys
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
priem = set(primenumbers(1000000))

def calc(a,b,n):
    return (n*n + a*n + b)
awin = 0
bwin = 0
record = 0
n = 0
for a in range(-999,999):
    for b in range(-999,999):
        print(str(a) + ", " + str(b) + ", " + str(n) + ", record: "+ str(record))
        n = 0
        while(calc(a,b,n) in priem):
            n += 1
            print(str(n))
            if(n>record):
                record = n
                awin = a
                bwin = b
print(str(record)+ ", " + str(awin) + ", " + str(bwin))
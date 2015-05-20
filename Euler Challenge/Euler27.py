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
record = 0
arec  = 0
brec = 0
print("huh")
for i in range(-1000,1000):
    for j in range(-1000,1000):
        n = 0
        while(calc(i,j,n) in priem):
            n += 1
        if n > record:
            record = n 
            arec = i
            brec = j
print(record)
print(arec)
print(brec)
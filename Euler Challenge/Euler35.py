import time
import itertools
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

priem = primenumbers(100)
spiegel = set()
priem = set(priem)


def swap(n):
    y = itertools.permutations(str(n))
    x = map(list,y)
    return x
    
def bin(n):
    m = 1
    while(n>1):
        m = n*m
        n -= 1
    return m

def circular(n):
    temp = []
    circ = []
    for j in swap(n):
        if(int(j) in priem):
            temp =+ j
    if(len(temp) == bin(n)):
        circ.append(i)
    return circ
    
print(swap(circular(234)))

for i in priem:
    temp = []
    for i in range(0,len(str(i))):
        i = str(i)
        i = i + i[0]
        i = i[1:]
        if(int(i) in priem):
            temp.append(i)
            print(temp)
        if(len(temp) == len(str(i))):
            spiegel.add(i)
        

T2 = time.time()
time = str(T2 - T1)

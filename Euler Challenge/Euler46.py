import math
import sys
import time
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
    
priem = primenumbers(1000000)
priem1 = set(priem)

def calc(a,b):
    return a + 2*(b**2)

def probeer(n):
    while(n in priem1):
        n +=2
    for b in range(1,int(math.sqrt(n))):
        for a in priem:
            if a < n:
                if(calc(a,b) == n):
                   return True

def vind(n):
    for i in range(13,n):
        while(probeer(i) == True):
            i += 2
            print(i)
        return i

print(vind(1000))
print(int(math.sqrt(57)/2)+1)
T2 = time.time()
print(str(T2-T2))
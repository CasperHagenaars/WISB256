import math
import time
from multiprocessing import Pool
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

def totient(a):
    getal = 1
    priemdelers = set()
    if a in priem:
        return int(a-1)
    for i in priem:
        if a != 1:
            if(a % i == 0):
                while(a/i % 1 == 0):
                    a /= i
                    getal *= i
                priemdelers.add(i)
                continue
        else:
            break
    for x in priemdelers:
        getal *= (x-1)
    return int(getal)
    
total = 0
print(totient(8))
for i in range(2,2):
    total += totient(i)
print(total)

T2 = time.time()
print(T2-T1)
input()
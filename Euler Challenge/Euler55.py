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

def check(n):
    n = str(n)
    temp = n
    record = 0
    if(len(set(n)) < len(n)):
        for i in list(n):
            count = 0
            if(n.count(i) > 1):
                for j in range(10):
                    n = temp.replace(i,str(j))
                    if(int(n) in priem):
                        if(len(list(str(n))) == len(str(int(n)))):
                            count += 1
                        if(count > record):
                            record = count
    return record

record = 0
record_getal = 0  
for i in range(1,1000000):
    new = check(i)
    if new > 7:
        record = new
        record_getal = i
        print(record)
        print(record_getal)
        break

T2 = time.time()
print(str(T2-T1) + " seconden.")
input()
import sys
import math
import time
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

a = set()
priem = set(primenumbers(1000000))
priemlaag = {2,3,5,7}
T1 = time.time()
def links(n):
    a =set()
    for i in n:
        j = i
        print(str(i))
        while j in priem:
            if len(str(j)) == 1 :
                if(j in priemlaag):
                    a.add(i)
                    print(j)
                    break
                break
            j = str(j)
            j = j[1:]
            j = int(j)
    return (a - priemlaag)
    
def rechts(n):
    a= set()
    for i in n:
        j = i
        while(j in priem):
            if(len(str(j)) == 1):
                if(j in priemlaag):
                    a.add(i)
                    break
                break
            j = str(j)
            j = j[:-1]
            j = int(j)
    return a
som = links(rechts(priem))
print(str(som))
T2 = time.time()
print(str(sum(som)))
print(str(T2-T1) + " seconden")


def newlinks(n):
    a = set()
    for i in n:
        for j in priemlaag:
            ij = str(i) + str(j)
            if(int(ij) in priem):
                a.add(int(ij))
    return a
    
def driel(n):
    b = n.copy()
    for i in n:
        for j in priemlaag:
            ij = int(str(i)+str(j))
            if(ij in priem):
                b.add(ij)
    return b

def drier(n):
    b = n.copy()
    for i in n:
        for j in priemlaag:
            ij = int(str(j)+str(i))
            if(ij in priem):
                b.add(ij)
    return b

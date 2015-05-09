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
priem = primenumbers(1000000)

def function(a):
    priemdelers = {}
    getal = a
    for i in priem:
        if i < (a+1):
            x = 0
            while(((a/i) % 1) == 0.0):
                x += 1
                priemdelers[int(i)] = int(x)
                a = a/i
        else:
            break
    return priemdelers
    
def divisorfunction(a):
    begin = 1
    for x in a:
        begin *= (a[x]+1)
    return begin
    
triangle = 1   
i = 2

while(2>1):
    if(divisorfunction(function(triangle))>500):
        print("Gevonden: " + str(triangle))
        T2 = time.time()
        print("In: "+ str(T2-T1)+ " seconden")
        break
    else:
        triangle += i
        i +=  1
        print(triangle)


snelstetijd = 9.613641023635864
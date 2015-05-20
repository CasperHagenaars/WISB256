import math

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

def dis(n,c):
    count = 0
    for p in priem:
        if n / p == int(n/p):
            count += 1
            if count == c:
                return True
    return False
    
def fourdis(n,x,c):
    count = 0
    for i in range(n,x+n):
        if(dis(i,c) == True):
            count += 1
            if(count == c):
                return True
        else:
            count = 0
    return False
print(fourdis(600,200,3))
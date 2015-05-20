import itertools
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
    
priem = set(primenumbers(1000000))

def cycle(n):
    lijst = {n}
    x = str(n)
    x = x[1:] + x[0]
    while(x != str(n)):
        lijst.add(int(x))
        x = x[1:] + x[0]
    return lijst

antwoord = []

for i in priem:
    counter = 0
    n = cycle(i)
    for j in n:
        if j in priem:
            counter += 1
        if counter == len(n):
            antwoord.append(i)

print(antwoord)
print(len(antwoord))
T2 = time.time()
print(str(T2-T1))
input()
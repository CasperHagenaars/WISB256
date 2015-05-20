import itertools
import time
import sys
import math
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
    
priem = primenumbers(int(math.sqrt(float(987654321))))
priem_num = len(priem)
T2 = time.time()
def perms(n):
    ans = []
    x = list(itertools.permutations(str(n)))
    for verz in x:
        getal = ""
        for num in verz:
            getal += num
        ans.append(int(getal))
    return list(reversed(ans))
x = perms(1234567)

print(T2-T1)

for i in x:
    for j in priem:
        if(i / j == int(i/j)):
            print(i)
            break
        if(j > math.sqrt(float(i))):
            print(i / j)
            print(i)
            sys.exit(0)
        
T3 = time.time()
print(T3-T2)
import time
import itertools

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
    
priems = set(primenumbers(10000))
T2 = time.time()
print(T2-T1)

def checker(n):
    perm = list(itertools.permutations(list(str(n))))
    temp = n
    for i in range(1000,10000):
        count = 0
        n = temp
        while(n in priems):
            count += 1
            if(tuple(list(str(n))) not in perm):
                break
            if(count == 3):
                return ((str(n-2*i)+str(n-i)+str(n)),i)
            n += i
    return False
    
getallen = []
teller = 0
for priem in priems:
    if(checker(priem) != False):
        getallen.append(checker(priem))

print(sorted(getallen))
T3 = time.time()
print(str(T3-T2))
input()
import itertools
import time
import Functions

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

priem = primenumbers(4000)
priem2 = set(priem)

T1 = time.time()
def perm(n,m):
    m1 = list(str(m))
    n1 = list(str(n))
    for digit in m1:
        if(m1.count(digit) != n1.count(digit)):
            return False
    return True


record = 2
record_num = 2
for i in priem:
    for j in priem:
        num = i*j
        if (num > 10**7):
            break
        tot = (i-1)*(j-1)
        ratio = num/tot
        if(ratio < record):
            if(perm(num,tot) == True):
                record = ratio
                record_num = num
print(record_num)
        
T2 = time.time()
print(T2-T1)
input()
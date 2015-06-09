import fractions
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
priem = primenumbers(1000000)
T1 = time.time()

def totient(n, prime_facts = None):
    '''Euler's totient function, phi(n), counts the numbers less than n
    that are coprime with n. Input an integer. Optionally input list
    of prime factors to avoid double work.'''
    result = n
    for prime in priem:
        result *= (prime-1)
        result /= prime
    return result
    
count = 0
for i in range(2,10001):
    count += phi(i)
print(count)

T2 = time.time()
print(T2-T1)
def totient(a):
    getal = a
    priemdelers = set()
    if a in priem:
        return int(a-1)
    for i in priem:
        if a != 1:
            if(a % i == 0):
                while(a/i % 1 == 0):
                    a /= i
                priemdelers.add(i)
                continue
        else:
            break
    for x in priemdelers:
        getal *= (1-1/x)
    return int(getal)

count2 = 0
for j in range(2,10001):
    count2 += totient(j)
print(count2)

T3 = time.time()
print(T3-T2)

def totient2(n, prime_facts = None):
    '''Euler's totient function, phi(n), counts the numbers less than n
    that are coprime with n. Input an integer. Optionally input list
    of prime factors to avoid double work.'''
    result = n
    if not prime_facts:
        prime_facts = priem(n)
    for prime in prime_facts:
        result *= (prime-1)
        result /= prime
    return result
    

input()
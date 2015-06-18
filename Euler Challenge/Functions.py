import time
import math
from math import sqrt
from itertools import count, islice

def isPrime(n):
    if n < 2: return False
    return all(n%i for i in islice(count(2), int(sqrt(n)-1)))

def base2(x):
    return int(bin(x)[2:])
    

def fac(n):
    m = 1
    while(n>1):
        m = n*m
        n -= 1
    return m
    
def isqrt(n):  
    'isqrt(n)\n\nReturn floor(sqrt(n)).'  
  
    if not isinstance(n, int):  
        raise TypeError('an int is required')  
    if n < 0:  
        raise ValueError('math domain error')  
  
    guess = (n >> n.bit_length() // 2) + 1  
    result = (guess + n // guess) // 2  
    while abs(result - guess) > 1:  
        guess = result  
        result = (guess + n // guess) // 2  
    while result * result > n:  
        result -= 1  
    return result  
    
def primenumbers(n):
  sieve=[True]*(n+1)
  sieve[:2]=[False, False]
  sqrtn=int(n**0.5)
  for i in range(2,sqrtn+1):
    if sieve[i]:
      sieve[2*i::i]=[False]*(n//i-1)
  return sieve

priem = primenumbers(10**7)
priem2 = set(priem)
def priemdelers(a):
    priems = set()
    for i in priem:
        if a != 1:
            if(a % i == 0):
                while(a/i % 1 == 0):
                    a /= i
                priems.add(i)
                continue
        else:
            break
    return priems
def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x
def totient(a):
    if a == 0 or a == 1:
        return 1
    getal = a
    if a in priem2:
        return int(a-1)
    primes = priemdelers(a)
    for x in primes:
        getal *= (1-1/x)
    return int(getal)
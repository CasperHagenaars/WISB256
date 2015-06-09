import math
from time import time
T1 = time()

def bin(n):
    m = 1
    while(n>1):
        m = n*m
        n -= 1
    return m
    
def fact(n):
    n = list(str(n))
    count = 0
    for digit in n:
        count += bin(int(digit))
    return count

def check(n):
    count = 0
    for tel in range(n):
        chains = set()
        while(getal not in chains):
            chains.add(getal)
            getal = fact(getal)
            if(len(chains)>60):
                continue
        if(len(chains) == 60):
            count += 1
    return count
        
print(check(10000))

T2 = time()
print(T2-T1)
input()
import math
import Functions
import time
from multiprocessing import Pool
p = Pool(4)

T1 = time.time()
volgorde = []
def div(n):
    for i in range(3, int(math.sqrt(n))+1,1):
        if n%i==0:
            if not Functions.isPrime((n+i*i)/i):
                return False
    return True

def finder(n):
    som = 1
    for getal in range(2,n+1,4):
        if Functions.isPrime((getal+4)/2):
            if Functions.isPrime(getal+1):
                if div(getal) != False:
                    som += getal
    return som
    
print(finder(10**6))
T2 = time.time()

print(T2-T1)
input()
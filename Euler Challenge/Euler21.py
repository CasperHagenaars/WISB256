import math
import time
T1 = time.time()

def sumdivisors(n):
    delers = 0
    for i in range(1,int(n/2)+1):
        if(n % i == 0):
            delers += i
    return delers

def testam(n):
    m = sumdivisors(n)
    if sumdivisors(m) == n:
        if (m != n):
            return n
    return None

def calc(n):
    total = 0
    for tel in range(1,n+1):
        if testam(tel) != None:
            total += tel
    return total
    
print(calc(10000))

T2 = time.time()
print(str(T2-T1) + " seconden have passed.")
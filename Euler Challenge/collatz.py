import math
import time
T1 = time.time()

def collatz(n):
    if(n % 2 == 0):
        return int(n/2)
    else:
        return int(3*n+1)

for i in range(0,1000001):
    record = 0
    tel = 0
    t = collatz(i)
    while(t > 1):
        t = collatz(t)
        tel += 1
    if(tel > record):
        record = tel

T2 = time.time()
print(record)
print(str(T2-T1))


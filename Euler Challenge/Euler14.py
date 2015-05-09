import time
import math
import sys
T1 = time.time()

a = {1:0, 2:1}

def collatz(n):
    try:
        return a[n]
    except:
        if(n % 2 == 0):
            return int(n/2)
        else:
            return int(3*n+1)
        a[n] = collatz(n)+1
        
def aantal(n):
    i = 0
    m = n
    while(m > 0):
        if m in a:
            a[n] = a[m] + i
            return a[n]
        else:
            m = collatz(m)
            i += 1
    return i
        
record = 1
recordhouder = 17

for i in range(1,1000001):
    check = aantal(i)
    if(check > record):
        record = check
        recordhouder = i
    print(str(check) + ", " + str(i)+ ", record: "+ str(record))

    
T2 = time.time()
time = str(T2 - T1)

print(str(time))
print(int(recordhouder))
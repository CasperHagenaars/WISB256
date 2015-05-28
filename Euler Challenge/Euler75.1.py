import math
from time import time
T1 = time()
pyth = set()
notpyth = set()
def check(maxim):
    a,b,c= 0,0,0
    for n in range(1,maxim):
        for m in range(n,maxim):
            a = m*m-n*n
            b = 2*m*n
            c = m*m + n*n
            if(a+b+c > 1500000):
                break
            if (a+b+c) not in pyth:
                pyth.add(a+b+c)
            else:
                notpyth.add(a+b+c)
                
for i in range(2,920):
    check(i)
    print(i)
    
result = pyth-notpyth
print(result)
print(len(result))
    
T2 = time()
print(T2-T1)
input()
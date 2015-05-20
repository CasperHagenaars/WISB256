import math
import time

record = 0
def cpan(n):
    x = len(str(n))
    i = 2
    ans = str(n)
    while(x != 9):
        if(x>9):
            break
        nex = str(n*i)
        x += len(nex)
        i += 1
        ans += nex
    return ans
def pan(n):
    a = set()
    b = []
    for i in list(str(n)):
        a.add(i)
        b.append(i)
    if('0' not in a):
        if(len(a) == len(b)):
            return True
    return False
    
for i in range(20,10000):
    nu = cpan(i)
    if pan(nu) == True:
        if int(nu) > int(record):
            record = nu
print(record)
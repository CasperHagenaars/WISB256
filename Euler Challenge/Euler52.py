import math
import sys
import time

def intoset(n):
    n = set(str(n))
    return n
    
def checker(n):
    m = intoset(n)
    i = 2
    while(m == intoset(i*n)):
        i += 1
        if(i>6):
            return True
    print(str(n) + " werkt niet")
    return False
    
for i in range(1,1000000):
    x = checker(i)
    if(x == True):
        print(x)
        sys.exit(0)
        
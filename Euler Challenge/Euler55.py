import time
import math
import sys
T1 = time.time()
def palin(n):
    x = str(n)
    return int(x[::-1])
    
def checker(n):
    for x in range(0,50):
        m = palin(n) + n
        if(m == palin(m)):
            return True
        else:
            n = m
    return False
            
def lychrel(n):
    i = 0
    print("Nummer test: " + str(n))
    for y in range(1,n+1):
        if(checker(y) == False):
            i += 1
            print("Great succes for: "+ str(y))
    return i
    
print("checker: "+ str(checker(196)))
print("lychrel nummers: "+ str(lychrel(10000)))
T2 = time.time()
print(str(T2-T1) + " seconden.")
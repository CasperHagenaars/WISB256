import time
import math
import sys
T1 = time.time()
a = {3:2,6:3}
triangle = 0

def divisors(L):
    divisor = []
    if(L == 0):
        return []
    for i in range(1,L):
        if(float(L)/float(i) == round(L/i)):
            divisor.append(i)
    return divisor

for counter in range(0,1000):
    if(len(divisors(triangle))>50):
        print("Triangle nummer: "+ str(counter)+ ". Gelijk aan: " + str(triangle)+ " met priemdelers: #" + str(len(divisors(triangle))))
        triangle += counter
    else:
        triangle += counter 
    
    
T2 = time.time()
time = str(T2 - T1)
print("Found "+ str(1000)+" Prime numbers smaller than "+ str(45)+ " in under " + time + ".")
print("-------------------------------------------- ")
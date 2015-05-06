import time
import math
import sys
T1 = time.time()
def bin(n):
    m = 1
    while(n>1):
        m = n*m
        n -= 1
    return m

print(str(bin(10)))
getal = str(bin(100))
antwoord = 0
for i in range(0,len(getal)):
    antwoord += int(getal[i])


print(str(antwoord))
T2 = time.time()
time = str(T2 - T1)
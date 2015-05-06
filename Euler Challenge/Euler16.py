import time
import math
import sys
T1 = time.time()
getal = 2**1000
antwoord = 0
for i in range(0,len(getal)):
    antwoord += int(getal[i])

T2 = time.time()
time = str(T2 - T1)

import sys
import time
import Functions
import math
priems = 0
side = 0
getal = 1
diag = 1
i = 2
totaal =1002001

while( i < 100):  
    for j in range(0,4):
        getal += i
        diag += getal
        if getal in Functions.priem2:
            priems += 1
    print(getal)
    print(priems)
    i += 2
    side += 1
    print("____")
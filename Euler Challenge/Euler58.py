import sys
import time
import Functions
import math
priems = 0
diags = 1
side = 1
getal = 1
i = 2
totaal =1002001

while(True):  
    for j in range(0,4):
        getal += i
        if getal in Functions.priem2:
            priems += 1
            print(getal)
        diags += 1
    side += 2
    if(priems/diags < 0.1):
        print(priems)
        print(diags)
        print(side)
        print("EINDE")
        break
    i += 2
input()
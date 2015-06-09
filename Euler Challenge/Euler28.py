import sys
import time
import math
diag = 1
getal = 1
i = 2
totaal =1002001
while(i<51):
    for j in range(0,4):
        getal += i
        diag += getal
        print(getal)
    i += 2
print(diag)
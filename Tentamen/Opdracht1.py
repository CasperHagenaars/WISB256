import math
import time

tekst = input()

lijn = "Ug"
try:
    if(int(tekst) > 1):
        for i in range(1,int(tekst)):
            lijn += " ug"
        lijn += "!"
        lijn = str(lijn)
    else:
        lijn = "Ug!"
except:
    lengte = (len(tekst) / 3)
    lijn = int(lengte)
print(lijn)
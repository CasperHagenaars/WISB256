from decimal import *
import math

getcontext().prec = 110
result = 0
for getal in range(1,101):
    if(math.sqrt(getal) != int(math.sqrt(getal))):
        sqrt = Decimal(getal)**Decimal(0.5)
        decimals = str(sqrt)[:101]
        print(decimals)
        for i in decimals:
            try:
                if(len(decimals) > 50):
                    result += int(i)
            except:
                continue
print(result)
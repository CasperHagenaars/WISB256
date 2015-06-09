import math
import fractions
from time import time
from decimal import *
T1 = time()
getcontext().prec = 30




def ordfrac(n):
    count = 0
    for denom in range(2,n+1):
        curr_num = int(denom/3)+1
        while(curr_num*3 > denom and curr_num*2 < denom):
            if(fractions.gcd(curr_num,denom)==1):
                count += 1
            curr_num += 1
            
    return count

print(ordfrac(1200))
T2 = time()
print(T2-T1)
input()
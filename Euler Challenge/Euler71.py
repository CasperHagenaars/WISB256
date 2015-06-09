import math
import fractions
from time import time
from decimal import *
T1 = time()
getcontext().prec = 17




def ordfrac():
    frac = Decimal(3/7)
    record = 1   
    record_num = 9
    for denom in range(1,1000000):
        curr_num = Decimal(int(frac*denom))
        difference = frac - curr_num/denom
        if(difference < record):
            record = difference
            record_num = curr_num
    return record_num


print(ordfrac())
T2 = time()
print(T2-T1)
input()
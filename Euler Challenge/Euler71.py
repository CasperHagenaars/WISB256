import math
import fractions
from time import time
from decimal import *
T1 = time()
getcontext().prec = 50
cons = Decimal(2/7)
eind = Decimal(3/7)
def div(n):
    getal = Decimal(int(cons*n))/n
    stap = Decimal(1/n)
    while(getal < eind):
        getal += stap
    getal -= stap
    return getal
record = 1   
record_breuk = 9
for i in range(999900,1000001):
    verschil = eind - div(i)
    if(verschil > 0):
        if(verschil < record):
            record = verschil
            print(verschil)
            print(i)
            record_breuk = fractions.Fraction(div(i)).limit_denominator(1000000)
T2 = time()
print(record_breuk)
print(T2-T1)
input()
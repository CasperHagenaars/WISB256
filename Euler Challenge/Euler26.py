import math
from decimal import *
getcontext().prec = 100000
def check(n):
    i = str(1/Decimal(n))
    lengte = 1
    while(i[10:10+lengte] != i[10+lengte:10+2*lengte]):
        lengte += 1
        if(len(i)<50):
            return 0
    return lengte
record = 0
record_number = 2
for i in range(2,1001):
    aantal = check(i)
    if aantal >record:
        record = aantal
        record_number = i
    print(str(aantal) + ", "+ str(i))
print(record)
print(record_number)

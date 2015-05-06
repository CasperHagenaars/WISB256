import time
import math
import sys
T1 = time.time()
sums = 0
ssum = 0
verzameling = []

for counter in range(0,101):
    sums = sums + counter*counter
for counter2 in range(0,101):
    ssum += counter2
print(math.fabs(sums-ssum*ssum))
    
        
T2 = time.time()
time = str(T2 - T1)
print("Found "+ str(n)+", "+ str(n)+ ", " +str(verzameling)+ ", " +str(sum(verzameling)) + " in under " + time + ".")
print("-------------------------------------------- ")
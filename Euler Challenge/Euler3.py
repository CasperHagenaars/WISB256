import time
import math
import sys
T1 = time.time()
n = 600851475143
verzameling = []

for counter in range(2,int(math.sqrt(n))+1): 
    if(float(n)/counter == round(n/counter)):
        verzameling.append(counter)
        n = n / counter
T2 = time.time()
time = str(T2 - T1)
print("Found "+ str(n)+", "+ str(n)+ ", " +str(verzameling)+ ", " +str(sum(verzameling)) + " in under " + time + ".")
print("-------------------------------------------- ")
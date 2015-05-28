import bisection
import math
import time
T1 = time.time()
root = bisection.findAllRoots(lambda x:math.sin(x),0.1,2.9,.0001)
for i in range(len(root)):
    root[i] = round(root[i],5)
print(root)
T2 = time.time()

print("In " + str(T2-T1)+ " seconden.")
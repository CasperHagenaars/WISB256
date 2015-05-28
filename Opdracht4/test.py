import bisection
import math
import time
T1 = time.time()
root = bisection.findAllRoots(lambda x:math.cos(x),0.1,2.9,.0001)
print(root)
T2 = time.time()

print("In " + str(T2-T1)+ " seconden.")
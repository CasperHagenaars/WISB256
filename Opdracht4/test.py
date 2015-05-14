import bisection
import math
import time
T1 = time.time()
root = bisection.findAllRoots(lambda x:math.sin(x),0,9,.1)
print(root)
T2 = time.time()

print("In " + str(T2-T1)+ " seconden.")
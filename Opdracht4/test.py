import bisection
import math
import time
T1 = time.time()
root = bisection.findRoot(lambda x:math.cos(x),0,3,.00001)
print(str(root/(.5*math.pi)))
T2 = time.time()

print("In " + str(T2-T1)+ " seconden.")

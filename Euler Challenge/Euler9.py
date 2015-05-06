import time
import math
import sys
T1 = time.time()
for a in range(1,1000):
    for b in range(a,1000):
        for c in range(b,1000):
            if(a*a+b*b == c*c):
                if(a+b+c == 1000):
                    print(str(a) + ", " + str(b)+ ", " + str(c) + ", " +str(a*b*c))
                    sys.exit(0)
T2 = time.time()
time = str(T2 - T1)
print("-------------------------------------------- ")
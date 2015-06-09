import math
import time
T1 = time.time()
def dio(d):
    for x in range(int(math.sqrt(d)),500000000):
        gebied = int(math.sqrt((x*x-1)/d))
        for y in range(gebied,gebied+1):
            n = x*x-d*y*y
            if(n == 1):
                return (x,y)

            

for d in range(2,1001):
    if(math.sqrt(d) != int(math.sqrt(d))):
        a = dio(d)
        print(str(a) + ", " +str(d))
        T2 = time.time()
        print(T2-T1)

input()
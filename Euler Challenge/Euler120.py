import math
import time
T1 = time.time()
def sqr(a,n):
    return (((a-1)**n+(a+1)**n) % (a*a))
def maxsq(a):
    r_record = 0
    for n in range(2,2*a+20):
        r = sqr(a,n)
        if(r > r_record):
            r_record = r
            n_hoogst = n
    return (a,r_record,n_hoogst)
r_sum = 0
for a in range(3,1001):
    r_max = maxsq(a)
    r_sum += r_max[1]
    print(r_max)
print(r_sum)
T2 = time.time()
print(T2-T1)
input()
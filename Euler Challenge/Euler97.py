import math
import time
T1 = time.time()
sq = '1234567890'
sqq = '1_2_3_4_5_6_7_8_9_0'
def check(n):
    a = str(n)
    for i in range(0,10):
        if a[2*i] != sq[i]:
            return False
    return True
    
for i in range(1010101010,1389026624,10):
    if(check(i*i) == True):
        print(i)
        
T2 = time.time()
print(T2-T1)
input()
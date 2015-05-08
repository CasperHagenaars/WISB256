import time
import math
import sys
T1 = time.time()
reca = 0
recb = 0
rec = {0:0}
for i in range(50,1000):
    for a in range(1,i):
        for b in range(a,i):
            if(a+b+math.sqrt(a*a+b*b)== i):
                if(a==20):
                    print(str(i) + ", "+ str(a)+ ", " + str(b))
                if(a==24):
                    print(str(i) + ", "+ str(a)+ ", " + str(b))
                if(a==30):
                    print(str(i) + ", "+ str(a)+ ", " + str(b))
                if(i in rec):
                    temp = rec[i]
                    rec[i] += 1
                else:
                    rec[i] = 1
print(rec)
T2 = time.time()
time = str(T2 - T1)
print("-------------------------------------------- ")
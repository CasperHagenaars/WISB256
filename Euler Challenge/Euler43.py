import time
import math
T1 = time.time()
pan = set()
for i in range(0,10):
    for j in range(0,10):
        for k in range(0,10):
            if((i*100+j*10+k) % 2 == 0):
                for l in range(0,10):
                    if((j*100+k*10+l) % 3 == 0):
                        for m in range(0,10):
                            if((k*100+l*10+m) % 5 == 0):
                                for n in range(0,10):
                                    if((l*100+m*10+n) % 7 == 0):
                                        for o in range(0,10):
                                            if((m*100+n*10+o) % 11 == 0):
                                                for p in range(0,10):
                                                    if((n*100+o*10+p) % 13 == 0):
                                                        for q in range(0,10):
                                                            if((o*100+p*10+q) % 17 == 0):
                                                                getal = str(i)+str(j)+str(k)+str(l)+str(m)+str(n)+str(o)+str(p)+str(q)
                                                                getalset = set(list(getal))
                                                                if(len(getalset) == 9):
                                                                    pan.add(getal)

pan2 = set()
for x in pan:
    for y in range(1,10):
        if str(y) not in list(x):
            x = str(y) + str(x)
            pan2.add(int(x))
            
print(pan2)
print(sum(pan2))
T2 = time.time()
print("In "+str(T2-T1)+ " seconden.")
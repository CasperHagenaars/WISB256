import time
import math
import sys
T1 = time.time()
nummer = 1
def checkpalin(n):
    if(len(str(n))<6):
        return False
    else:
        checkpalindroom1 = False
        checkpalindroom2 = False
        checkpalindroom3 = False
        if((n/100000) == (n - (n/10)*10)):
            checkpalindroom1 = True
        if(((n-n/100000*100000)/10000) == (n - (n/100)*100)/10):
            checkpalindroom2 = True
        if((n/1000 - (n/10000)*10) == (n/100 - (n/1000)*10)):
            checkpalindroom3 = True
        if(checkpalindroom1 == True and checkpalindroom2 == True and checkpalindroom3 == True):
            return True
for x in range(1,1000):
    for y in range(1,1000):
        if(nummer < x*y):
            if(checkpalin(x*y) == True):
                nummer = x*y
print(checkpalin(998001))
print(str(nummer))
T2 = time.time()
time = str(T2 - T1)
print("Found "+str((998001/100000))+", "+str((998001 - (998001/10)*10))+ ", " +str(3)+ ", " +str(4) + ", " +str(5) + " in under " + time + ".")
print("-------------------------------------------- ")


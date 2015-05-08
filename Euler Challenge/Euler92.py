import sys
import math
import time
T1 = time.time()

def form(n):
    x = 0
    n = list(str(n))
    for i in n:
        x += int(i)**2
    return x
    

c1 = 1
c89 = 0

def under600(m):
    a = {1:1,44:87,32:1,13:1,10:1,85:89,145:89,42:89,20:89,4:89,16:89,37:89,58:89,89:89}
    for i in range(1,m+1):
        n = i
        while(n>1):
            if(n>567):
                n = form(n)
            else:
                n = form(n)
                if n in a:
                    a[i] = a[n]
                    if(a[n] == 1):
                        global c1 
                        c1 += 1
                        print(str(i) +" getal en 1:"+str(c1))
                        n = 0
                    else:
                        global c89 
                        c89 += 1
                        print(str(i)+ " getal en 89:"+ str(c89))
                        n = 0
                else:
                    print(str(i) + " gaat nu naar: " + str(n))
    return a

a = under600(600)
print(a)
print(c1)
print(c89)
for i in range(601,10000001):
    i = a[form(i)]
    if(i == 89):
        c89 += 1
print(c89)
T2 = time.time()
print(T2-T1)

ans = 8581146
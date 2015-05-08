import math
import sys
import time

def bin(n):
    m = 1
    while(n>1):
        m = n*m
        n -= 1
    return m
    
def c(n,r):
    return bin(n)/(bin(r)*bin(n-r))
cn = []
cr = []
for i in range(22,101):
    for j in range(1,i+1):
        if(c(i,j) > 1000000):
            cn.append(i)
            cr.append(j)
        else:
            print("c = " + str(i) + ", r = " + str(j))
print(cn)
print(cr)
print(len(cn))
print(len(cr))
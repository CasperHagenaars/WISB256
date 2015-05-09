import time
import math

def findRoot(f,a,b,epsilon):
    m = (a+b)/2
    if(math.fabs(a-b) < epsilon):
        return m
    if(f(a)<f(b)):
        l = a
        h = b
    else:
        l = b
        h = a
    if(f(m)>0):
        return findRoot(f,l,m,epsilon)
    else:
        return findRoot(f,m,h,epsilon)
        
def findAllRoots(f,a,b,epsilon):
    return a

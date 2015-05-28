import time
import math

def findRoot(f,a,b,epsilon):
    m = (a+b)/2
    if(f(a) == 0):
        return a
    if(f(a)*f(b) > 0):
        return None
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
roots = []

def findAllRoots(f,a,b,epsilon):
    while a + 0.00001 <= b:
        root = findRoot(f,a,a+0.00001,epsilon)
        if root != None:
            roots.append(root)
        a += 0.00001
    return roots
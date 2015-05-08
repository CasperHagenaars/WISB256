import time
import math
import sys

def triangle(n):
    return (n*(n+1)/2)
def pentagon(n):
    return n*(3*n-1)/2
def hexagon(n):
    return n*(2*n-1)

t = 285
p = 165
h = 143
for t in range(286,1000000):
    tr = triangle(t)
    while(tr > pentagon(p)):
        p +=1
    while(tr > hexagon(h)):
        h += 1
    if(tr == hexagon(h)):
        if(tr==pentagon(p)):
            print(str(int(tr)))
            sys.exit(0)
            
print(str(t)+", "+ str(p)+ ", "+ str(h))
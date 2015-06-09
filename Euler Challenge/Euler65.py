import math
from fractions import *

def elist(n):
    e = [2]
    for i in range(1,n):
        e.append(1)
        e.append(2*i)
        e.append(1)
    return e
    
def cont(lengte,n):
    n = n[:lengte]
    count = n.pop()
    for i in range(lengte-1):
        count = n.pop() + 1/count
    return count

a = list(str(cont(100,elist(150))))
tel = 0
for i in a:
    if i == '/':
        break
    tel += int(i)
print(tel)
input()
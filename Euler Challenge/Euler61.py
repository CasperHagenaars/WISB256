import math
import time
T1 = time.time()
def polygonal(f):
    verzameling = set()
    for n in range(1000):
        num = f(n)
        if num > 999:
            verzameling.add(int(num))
        if num > 9999:
            return verzameling
            
triangle = polygonal(lambda n: n*(n+1)/2)
square = polygonal(lambda n: n*n)
pentagon = polygonal(lambda n: n*(3*n-1)/2)
hexagonal = polygonal(lambda n: n*(2*n-1))
heptagonal = polygonal(lambda n: n*(5*n-3)/2)
octagonal = polygonal(lambda n: n*(3*n-2))

def check(n,m1):
    verz = set()
    for m in m1:
        if str(n)[:2] == str(m)[2:] or str(n)[2:] == str(m)[:2]:
            verz.add(m)
    return verz
def reken(a,b,c,d,e):
    result = set()
    for i in a:
        result = result.union(check(i,b))
    temp = result
    result = set()
    for j in temp:
        result = result.union(check(j,c))
    temp = result
    result = set()
    for k in temp:
        result = result.union(check(j,d))
    temp = result
    result = set()
    for m in temp:
        result = result.union(check(j,e))  
    temp = result
    result = set()
    for l in temp:
        result = result.union(check(j,a))
    return result
print(reken(square,triangle,pentagon,hexagonal,pentagon))

T2 = time.time()
print(T2-T1)
input()
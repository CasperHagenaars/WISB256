import math
import itertools
import time
T1 = time.time()
def polygonal(f):
    verzameling = []
    for n in range(1000):
        num = f(n)
        if num > 9999:
            return verzameling
        if num > 999:
            verzameling.append(int(num))

            
triangle = polygonal(lambda n: n*(n+1)/2)
square = polygonal(lambda n: n*n)
pentagon = polygonal(lambda n: n*(3*n-1)/2)
hexagonal = polygonal(lambda n: n*(2*n-1))
heptagonal = polygonal(lambda n: n*(5*n-3)/2)
octagonal = polygonal(lambda n: n*(3*n-2))

def check(eerste,tweede):
    verz = set()
    for n in eerste:
        for m in tweede:
            n1 = str(n)[2:]
            n2 = str(m)[:2]
            if n1 == n2:
                if str(m)[2] != '0':
                    verz.add(m)
    return verz
    
def reken(lijst):
    temp = square
    result = set()
    verz = set()
    for i in lijst:
        result = set()
        result = result.union(check(temp,i))
        temp = result
    return result
    
antwoord = set()
lijst = [triangle,pentagon,hexagonal,octagonal,pentagon]

for i in list(itertools.permutations(lijst)):
    temp = i
    if(reken(temp) != set()):
        test = check(reken(temp),square)
        for elem in test:
            antwoord.add(elem)
    
print(antwoord)
T2 = time.time()
print(T2-T1)
input()
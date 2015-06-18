import math
import itertools
cubes = []
dic = {}
i = 1
def cube(n):
    return int(n**3)
print(cube(5027))
while(True):
    geordend = sorted(list(str(cube(i))))
    cubes.append(geordend)
    if(geordend == sorted(list(str(cube(5027))))):
        print(i)
        print(geordend)
    if(cubes.count(geordend) == 5):
        print(i)
        break
    i+=1

input()
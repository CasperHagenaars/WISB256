import math
import itertools
cubes = []
dic = {}
i = 1
while(i< 100):
    cube = i**3
    cubes.append(cube)
    print(i)
    if(cubes.count(cube) == 4):
        print(i)
    i+=1
print(cubes)
input()
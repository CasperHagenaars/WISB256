import math
import re

f = open('Euler22.dat', 'r')
names = []

for line in f:
    h = line
    wordList = re.sub("[^\w]", " ",  h).split()
    names.append(wordList)
names = names[0]

def tri(n):
    return int(n*(n+1)/2)
triangles = set()
for i in range(0,30):
    triangles.add(tri(i))

def length(naam):
    naam = list(naam)
    count = 0
    for i in naam:
        count += ord(i) - 64
    return count

print(triangles)
print(names)
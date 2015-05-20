import math
import time
import re
f = open('Euler22.dat', 'r')
a = []
for line in f:
    h = line
    wordList = re.sub("[^\w]", " ",  h).split()
    a.append(wordList)

a = a[0]

def length(naam):
    naam = list(naam)
    count = 0
    for i in naam:
        count += ord(i) - 64
    return count

def calc(lijst):
    count = 0
    teller = 1
    for i in sorted(lijst):
        count += length(i) * teller
        teller += 1 
    return count
print(calc(a))
f.close()
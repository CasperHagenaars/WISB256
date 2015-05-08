import time
import math
import sys

def bin(n):
    m = 1
    while(n>1):
        m = n*m
        n -= 1
    return m
x = set()
getal = str(bin(100))
antwoord = 0
for i in range(0,len(getal)):
    antwoord += int(getal[i])
    
for i in range(3,1000000):
    getal = str(i)
    antw = 0
    for j in range(0,len(getal)):
        antw += bin(int(getal[j]))
    if(antw == int(getal)):
        x.add(int(getal))
print(getal)
print(len(getal))
print(str(antw))
print(x)

import sys
import time
import re
import math
f = open('collatz.dat', 'r')
a = []
for line in f:
    h = line
    wordList = re.sub("[^\w]", " ",  h).split()
    a.append(wordList)
     
def vert(n):
    record = 1
    for i in range(0,20):
        for j in range(0,16):
            x = 1
            for k in range(0,4):
                x *= int(n[i][j+k])
                if(x > record):
                    record = x
    return record
    
def horz(n):
    record = 1
    for i in range(0,20):
        for j in range(0,16):
            x = 1
            for k in range(0,4):
                x *= int(n[j+k][i])
                if(x > record):
                    record = x
    return record
def diag1(n):
    record = 1
    for i in range(0,16):
        for j in range(0,16):
            x = 1
            for k in range(0,4):
                x *= int(n[i+k][j+k])
                if(x > record):
                    record = x
    return record
def diag2(n):
    record = 1
    for i in range(0,16):
        for j in range(4,20):
            x = 1
            for k in range(0,4):
                x *= int(n[i+k][j-k])
                if(x > record):
                    record = x
    return record
print(vert(a))
print(horz(a))
print(diag1(a))
print(diag2(a))
f.close()

import time
import math
import re
import sys
T1 = time.time()
f = open('problem13.dat', 'r')
a = []
for line in f:
    h = line
    wordList = re.sub("[^\w]", " ",  h).split()
    a.append(wordList)

x = 0
for line in a:
    x += int(line[0])
print(x)
print(len(x))


f.close()
    
T2 = time.time()
time = str(T2 - T1)
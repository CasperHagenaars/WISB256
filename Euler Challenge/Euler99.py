from time import time
import math
import re
t1 = time()
f = open('machten.txt', 'r')
a = []
print(len(str(5.19432**525806)))
input()
for line in f:
    h = line
    wordList = re.sub("[^\w]", " ",  h).split()
    a.append(wordList)
def checklen(a,b):
    a1 = len(str(a))-1
    print(a)
    print(b)
    a2 = len(str(int((a/(10**a1))**b)))-1
    print(a2)
    b1 = len(str((10**a1)**b))-1
    return (a2+b1)
    
for i in range(0,1000):
    print(checklen(int(a[i][0]),int(a[i][1])))
f.close()
t2 = time()
print(t2-t1)
input()
from time import time
import math
import re
t1 = time()
f = open('machten.txt', 'r')
a = []
for line in f:
    h = line
    wordList = re.sub("[^\w]", " ",  h).split()
    a.append(wordList)
def checklen(a,b):
    getal = a
    count = 0
    while(b > 1):
        getal *= a
        if(getal > 10**20):
            getal /= 10**6
            count += 6
        b -= 1
    return (count + len(str(int(getal))))
record = 0
for i in range(0,10):
    getal = checklen(int(a[i][0]),int(a[i][1]))
    if(getal >= record):
        record = getal
        print(getal)
        print(i)
        print(record)
        print("____")
f.close()
t2 = time()
print(t2-t1)
input()
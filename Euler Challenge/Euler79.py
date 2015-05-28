import sys
import time
import re
import math
T1 = time.time()
f = open('pass.txt', 'r')
a = []
for line in f:
    h = line
    wordList = re.sub("[^\w]", " ",  h).split()
    a.append(wordList)

for i in range(100000890,900000000,1000):
    i = list('73'+ str(i))
    
    if('4' in i or '5' in i):
        continue
    for wacht in a:
        try:
            password = list(wacht[0])
            a1 = password[0]
            a2 = password[1]
            a3 = password[2]
            if(i.index(a1)<i.index(a2) and i.index(a2) < i.index(a)):
                print("huh")
                print(i)
        except:
            print(i)
            break

f.close()
T2 = time.time()
print(str(T2-T1) + " seconds have passed.")
input()
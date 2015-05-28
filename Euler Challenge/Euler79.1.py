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
eerste = {'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
laatste = {'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
b = a
print(a)
for i in a:
    i = i[0]
    i = list(str(i))
    if(i[0] in eerste):
        eerste[i[0]] += 1
    else:
        eerste[i[0]] = 1
        
for j in a:
    j = j[0]
    j = list(str(j))
    if(j[-1] in laatste):
        laatste[j[-1]] += 1
    else:
        laatste[j[-1]] = 1
        
print(laatste)
print(eerste)
f.close()
T2 = time.time()
print(str(T2-T1) + " seconds have passed.")
input()
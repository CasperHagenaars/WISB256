import math
import sys
import time
T1 = time.time()
x = 0 
i=0
while(x<1000100):
    x += len(str(i))
    i +=1
a = []
for x in range(1,i+1):
    a.append(x)

tekst = ""
for line in a:
    tekst += str(line)
getallen = list(str(tekst))

print(int(getallen[0])*int(getallen[9])*int(getallen[99])*int(getallen[999])*int(getallen[9999])*int(getallen[99999])*int(getallen[999999]))
T2 = time.time()
print(str(T2-T1))
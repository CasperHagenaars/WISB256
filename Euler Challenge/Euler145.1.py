from time import time
import math
import sys
T1 = time()
oneven = {'1','3','5','7','9'}

def rev(n):
    x = str(n)
    if(x[-1] == '0'):
        return False
    y = x[::-1]
    if (set(str(int(x)+int(y))) <= oneven):
        return True
    return False
    

counter = 0
lijst = []
for i in range(1,10**7):
    if(rev(i) == True):
        counter += 1
        
print(lijst)
print(str(counter))

T2 = time()
print(T2-T1)
input()
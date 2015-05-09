import time
import math
import sys

def rev(n):
    x = str(n)
    y = x[::-1]
    if(y[0] == '0'):
        return '0'
    return str((int(x)+int(y)))

oneven = {'1','3','5','7','9'}

def check(n):
    if(set(n) | oneven == oneven):
        return True
    else:
        return False
counter = 0
for i in range(1,1000000001):
    i = str(i)

    if(check(rev(i)) == True):
        counter += 1
        print(str(counter) + " getal: "+ str(i))
print(str(counter))
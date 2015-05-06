import time
import math
import sys
T1 = time.time()
n1 = 3
n2 = 3
n3 = 5
n4 = 4
n5 = 4
n6 = 3
n7 = 5
n8 = 5
n9 = 4
n10 = 3
n11 = 6
n12 = 6
n13 = 8
n14 = 8
n15 = 7
n16 = 7
n17 = 9
n18 = 8
n19 = 8
n20 = 6
n30 = 6
n40 = 5
n50 = 5
n60 = 5
n70 = 7
n80 = 6
n90 = 6
n100 = 7


def under100(n):
    if(n<20):
        return 0
    n = n%100/10
    if(n == 2):
        return n20
    if(n == 3):
        return n30
    if(n == 4):
        return n40
    if(n == 5):
        return n50
    if(n == 6):
        return n60
    if(n == 7):
        return n70
    if(n == 8):
        return n80
    if(n == 9):
        return n90
    else: 
        return 0
def under20(n):
    if(n%100>20):
        n = n%10
    else:
        n = n%20
    if(n == 1):
        return n1
    if(n == 2):
        return n2
    if(n == 3):
        return n3
    if(n == 4):
        return n4
    if(n == 5):
        return n5
    if(n == 6):
        return n6
    if(n == 7):
        return n7
    if(n == 8):
        return n8
    if(n == 9):
        return n9
    if(n == 10):
        return n10
    if(n == 11):
        return n11
    if(n == 12):
        return n12
    if(n == 13):
        return n13
    if(n == 14):
        return n14
    if(n == 15):
        return n15
    if(n == 16):
        return n16
    if(n == 17):
        return n17
    if(n == 18):
        return n18
    if(n == 19):
        return n19
    if(n == 20):
        return n20
    else: 
        return 0
        
def above100(n):
    if(n>99):
        if(n%100 == 0):
            return (under20(n/100)+7)
        else:
            return (under20(n/100)+10)   
    else:
        return 0
        
def calculate(n):
        return(above100(n)+under100(n)+under20(n))
antwoord = 0

for i in range(1,1000):
    antwoord += calculate(i)
    print(str(i)+", "+ str(calculate(i))+ ", " + str(antwoord))
print(str(antwoord+11))
         
         
T2 = time.time()
time = str(T2 - T1)

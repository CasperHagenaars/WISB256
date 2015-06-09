import math
from time import time
T1 = time()
def pan(n):
    for i in range(1,10):
        if str(i) not in n:
            return False
    return True

def fib1():
    stop = False
    count = 2
    n_1 = 1
    n_2 = 1
    n_3 = 1
    n_4 = 1
    while(stop == False):
        temp = n_2
        temp2 = n_4
        n_2 += n_1
        n_4 += n_3 % 1000000000
        n_1 = temp
        n_3 = temp2 % 1000000000
        count += 1
        if(len(str(n_2))>25):
            if(len(str(n_2))==len(str(n_1))):
                n_1 = int(str(n_1)[:15])
                n_2 = int(str(n_2)[:15])
        if(pan(list(str(n_2))[:9]) == True):
            if(pan(list(str(n_4))[-9:]) == True):
                stop = True
    return (count)
    
print(fib1())

    
T2 = time()
print(T2-T1)
input()
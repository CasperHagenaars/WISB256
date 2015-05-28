import math
from time import time
T1 = time()


dic = {0:0}
def check(n):
    count_max = int(n/2) + 1
    for i in range(1,count_max):
        for j in range(i+1,count_max):
            k = math.sqrt(i*i+j*j)
            if(i+j+k > 1500000):
                break
            if(round(k) == k):
                tot = int(i+j+k)
                if tot in dic:
                    dic[tot] += 1
                else:
                    dic[tot] = 1
        

check(5000)
a = list(dic.values())

print(a.count(1))



T2 = time()
print(T2-T1)
input()
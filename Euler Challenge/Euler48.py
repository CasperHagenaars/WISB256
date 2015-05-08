import time
import math
import sys
ans = 0
def base2(x):
    return int(bin(x)[2:])
    
for i in range(1,1000000):
    if(str(i)[::-1] == str(i)):
        if(str(base2(i))[::-1] == str(base2(i))):
            ans += i
print(ans)
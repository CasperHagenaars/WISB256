import math
import time
import re
T1 = time.time()
f = open('priems.txt', 'r')
priem = f.readline()
print(priem)


f.close()
T2 = time.time()
print(T2-T1)
input()
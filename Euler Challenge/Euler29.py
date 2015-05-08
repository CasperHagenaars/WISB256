import sys
import time
import math
a = set()
for i in range(2,101):
    for j in range(2,101):
        x = i**j
        a.add(x)
print(len(a))
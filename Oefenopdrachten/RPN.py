import math
import time
invoer = str(input())
invoer = invoer.split(" ")
x = []
for i in range(0,3):
    x.append(invoer[i])
if(x[2] == '+'):
    result = int(x[0]) + int(x[1])
if(x[2] == '*'):
    result = int(x[0]) * int(x[1])
if(x[2] == '-'):
    result = int(x[0]) - int(x[1])
if(x[2] == '/'):
    result = int(x[0]) / int(x[1])
    
    
print(str("{0:.3f}".format(result)))
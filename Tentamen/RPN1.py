import math
import time
invoer = str(input())
invoer = invoer.split(" ")
x = []
for i in range(0,len(invoer)):
    x.append(invoer[i])

def calc(first,second,operator):
    try:
        if(operator == '+'):
            return (float(first) + float(second))
        if(operator == '*'):
            return (float(first) * float(second))
        if(operator == '-'):
            return (float(first) - float(second))
        if(operator == '/'):
            return (float(first) / float(second))
    except:
        return None
    
i = 0
while(len(x)>2):
    ans = calc(x[i],x[i+1],x[i+2])
    if ans != None:
        x[i] = ans
        del x[i+1]
        del x[i+1]
        i = 0
    else: 
        i += 1

    
print(str("{0:.3f}".format(float(x[0]))))
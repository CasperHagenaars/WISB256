import time
T1 = time.time()
abun = []
def propdiv(n):
    count = 0
    for i in range(1,int(n/2)+1):
        if(n % i == 0):
            count += i
    
    return count
for i in range(1,30000):
    if propdiv(i) > i:
        abun.append(i)
    
T2 = time.time()
print(str(T2-T1))

verz = set()
for a in abun:
    for b in abun:
        c = a + b
        verz.add(c)

getallen = set()
for d in range(0,28124):
    if d not in verz:
        getallen.add(d)
print(str(sum(getallen)))
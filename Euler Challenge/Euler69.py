import math

def primenumbers(L):
    notprimes = set()
    primes = []
    for counter in range(2,L):
        if counter in notprimes: 
            continue
        
        for j in range(counter*counter,L+1,counter):
            notprimes.add(j)
                    
        primes.append(counter)
    return primes 
    


priem = primenumbers(1000000)
def totient(a):
    getal = a
    priemdelers = set()
    if a in priem:
        return int(a-1)
    for i in priem:
        if a != 1:
            if(a % i == 0):
                while(a/i % 1 == 0):
                    a /= i
                priemdelers.add(i)
                continue
        else:
            break
    for x in priemdelers:
        getal *= (1-1/x)
    return int(getal)
record = 1
for i in range(1,1000000):
    temp = 1000000 - i
    if(temp/totient(temp) > record):
        record = temp/totient(temp)
        print(temp/totient(temp))
        print(temp)
input()
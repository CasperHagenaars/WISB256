def base2(x):
    return int(bin(x)[2:])
    
def bin(n):
    m = 1
    while(n>1):
        m = n*m
        n -= 1
    return m
    
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
    
priem = set(primenumbers(100000000))
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
    
priem = primenumbers(1100000)
import time
T1 = time.time()

def check():
    record = 5
    i = 0
    som_record = 0
    priem_record = 0
    begin_record = 0
    for beginpriem in range(0,80000):
        i = beginpriem
        som = 0
        while(som < 1000000):
            if((i-beginpriem) > record):
                if som in priem:
                    record = (i-beginpriem)
                    begin_record = beginpriem
                    som_record = som
                    priem_record = priem[i]
            som += priem[i]
            i += 1
    return (som_record, begin_record, priem_record, record)
    
print(check())


T2 = time.time()
print(T2-T1)
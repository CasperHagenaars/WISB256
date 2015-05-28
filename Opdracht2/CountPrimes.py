import math
import sys
import re
import time
T1 = time.time()
bestandnaam = sys.argv[0]
f = open(str(bestandnaam), 'r')
primes = []
for line in f:
    wordList = int(re.sub("[^\w]", "\n",  line).split()[0])
    primes.append(wordList)


def twins():
    count = 0
    for i in range(len(primes)):
        try:
            if(primes[i] + 2 == primes[i+1]):
                count += 1
        except:
            return count
    
c = 0.6601618
largest = primes[-1]
aantal = len(primes)
nlog = largest/math.log(largest)
ratio = aantal*math.log(largest)/largest
c2 = 2*c*largest/(math.log(largest)**2)
hardy = twins()*math.log(largest)**2/(2*c*largest)

print("Largest Prime =  " + str(largest))
print("--------------------------------")
print("pi(N)         =  " + str(aantal))
print("N/log(N)      =  " + str(nlog))
print("ratio         =  " + str(ratio))
print("--------------------------------")
print("pi_2(N)       =  " + str(twins()))
print("2CN/log(N)^2  =  " +str(c2))
print("ratio         =  " + str(hardy))
import math
import Functions
def som(n):
    


def harshad(n):
    som = 0
    getal = int(n/10)
    n = list(str(getal))
    for i in range(len(n)):
        som += int(n[i])
    if(getal % som != 0):
        return False
    if(Functions.isprime(getal/som)):
        while(
print(harshad(2011))
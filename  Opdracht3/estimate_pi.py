import random
import math
import sys

if len(sys.argv) < 4:
    print("Use: estimate_pi.py N L F")
    sys.exit(0)
    
aantal = int(sys.argv[1])
lengte = float(sys.argv[2])
random.seed(sys.argv[3])
hits = 0

def drop_needle(L):
    y = random.uniform(0,0.5)
    a = random.uniform(0,math.pi/2)
    if lengte*math.cos(a)/2 > y:
        return True
    else:
        return False
        
for i in range(0,aantal):
    if drop_needle(lengte) == True:
        hits += 1

if lengte > 1:
    schatting_pi = round(((2*lengte-2*(math.sqrt(lengte*lengte-1) + math.asin(1/lengte)))/(hits/aantal-1)),6)
else:
    schatting_pi = round(2*lengte*aantal/hits,6)

print(str(hits) +" hits in "+ str(aantal) + " tries \nPi = "+ str(schatting_pi))

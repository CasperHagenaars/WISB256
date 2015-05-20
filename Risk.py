import random
import time
T1 = time.time()

def worp(n):
    stenen = []
    i = 0
    while(i < n):
        y = int(random.randint(1,6))
        stenen.append(y)
        i += 1
    return (sorted(stenen))
    
def resultaat(aanval,verdediging):
    wins = 0
    if(verdediging[-1] >= aanval[-1]):
        wins += 1
    else:
        wins += -1
    if(len(verdediging) == 1):
        return wins
    else:
        if(verdediging[-2] >= aanval[-2]):
            wins += 1
        else:
            wins += -1
    return wins
    
def beter(n):
    stand = 0
    for i in range(n):
        aanval = worp(3)
        if aanval[-2] < 4:
            stand += resultaat(aanval,worp(2))
        else:
            stand += resultaat(aanval,worp(1))
    return stand
    

def simul(aanval, n):
    wins2 = 0
    wins1 = 0
    for i in range(n):
        wins2 += resultaat(aanval,worp(2))
    for i in range(n):
        wins1 += resultaat(aanval,worp(1))
    if wins1 > wins2:
        return "1"
    else:
        return "2"

    
def vaaksim(aanval,n):
    win1 = 0
    win2 = 0
    for i in range(n):
        x = simul(aanval,n)
        if x == "1":
            win1 += 1
        else:
            win2 += 1
    return "een: "+ str(win1), "twee: "+ str(win2)

aanval = 0
verd = 0
for a in range(100):
    if(int(beter(100)) > 0):
        verd += 1
    else:
        aanval += 1

print(aanval)
print(verd)

T2 = time.time()
print(T2-T1)
input()
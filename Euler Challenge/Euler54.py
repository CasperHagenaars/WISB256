import time
import math
import re

f = open('poker.dat', 'r')
speler1 = []
speler2 = []
testhand = ['8C', 'TS', 'KC', '9H', '4S']
testhand2 = ['8C', 'TC', 'KC', '9C', '4C']
teststraight = ['5C', '4C', '3C', 'AC', '2C']
testfour = ['KC', 'KS', 'KC', '9H', 'KS']
testhouse = ['KC', 'KS', 'KC', '9H', '9S']
for line in f:
    h = line
    wordList = re.sub("[^\w]", " ",  h).split()
    speler1.append(wordList[:5])
    speler2.append(wordList[5:])

def flush(n):
    kleur = str(n[0])[1]
    for i in range(len(n)):
        if str(n[i])[1] != kleur:
            return False
    return True
def sort(n):
    getallen = []
    for i in range(5):
        hoogte = (str(n[i])[0])
        try:
            getallen.append(int(hoogte))
        except:
            if(hoogte == 'T'):
                getallen.append(10)
            if(hoogte == 'J'):
                getallen.append(11)
            if(hoogte == 'Q'):
                getallen.append(12)
            if(hoogte == 'K'):
                getallen.append(13)
            if(hoogte == 'A'):
                getallen.append(1)
                getallen.append(14)
    return sorted(getallen)
        
        
def straight(n):
    getallen = n
    count = 0
    for j in range(len(getallen)-1):
        if(getallen[j+1]-getallen[j] == 1):
            count += 1
            if count == 4:
                return getallen[j+1]
        else: count = 0
    return False

def straightflush(n):
    if(flush(n) != False):
        n = sort(n)
        return straight(n)
    return False
    
def four(n):
    for i in n:
        if n.count(i) == 4:
            return i
    return False
    
def pairs(n):
    two_nums = [] 
    twocount = 0
    for i in n:
        if(n.count(i) == 2):
            twocount -= 1
        if n.count(i) == 3:
            return (3,i)
        if n.count(i) == 2:
            twocount += 1
            two_nums.append(i)
    if twocount == 2 or twocount == 1:
        return (twocount,two_nums)
    if twocount == 0:
        return (0,n[-1])
    
def fullhouse(n):
    three = False
    three_num = 0
    two = False
    two_num = 0
    for i in n:
        if n.count(i) == 3:
            three = True
            three_num = i
        if n.count(i) == 2:
            two = True
            two_num = i
    if(three and two):
        return (three_num,two_num)
    return False

def value(n):
    unsort = n
    n = sort(n)
    if(straightflush(unsort) != False):
        return (8,straightflush(unsort))
    if(four(n) != False):
        return (7,four(n))
    if(fullhouse(n) != False):
        return (6,fullhouse(n))
    if(flush(unsort) != False):
        return (5,flush(unsort))
    if(straight(n) != False):
        return (4,straight(n))
    if(pairs(n) != False):
        return pairs(n)
        
def winnaar(speler1,speler2):
    if(value(speler1)[0] > value(speler2)[0]):
        return "Speler 1"
    if(value(speler1)[0] < value(speler2)[0]):
        return "Speler 2"
    else:
        if(value(speler1)[1] > value(speler2)[1]):
            return "Speler 1"
        if(value(speler1)[1] < value(speler2)[1]):
            return "Speler 2"
    return None
player = 0
for i in range(1000):
    if winnaar(speler1[i],speler2[i]) == "Speler 1":
        print("Speler 1")
        player +=1
    else:
        print("Speler 2")
print(player)
input()
import time
import math
import re

f = open('poker.dat', 'r')
speler1 = []
speler2 = []
testhand = ['8C', 'TS', 'KC', '9H', '4S']
for line in f:
    h = line
    wordList = re.sub("[^\w]", " ",  h).split()
    speler1.append(wordList[:5])
    speler2.append(wordList[5:])

def waardehand(hand):
    for i in hand:
        
import sys
import time
import re
import math
from Binary import XOR
T1 = time.time()
def bestand(naam):
    f = open(str(naam), 'r')
    a = []
    for line in f:
        h = line
        wordList = re.sub("[^\w]", "\n",  h).split()
        a.append(wordList)
    f.close()
    return a
waarden = 0
a = bestand('code.txt')[0]
eerste = 103
tweede = 111
derde = 100
tekst = ""
for code in range(len(a)):
    if code % 3 == 0:
        char = XOR(eerste,int(a[code]))
    if code % 3 == 1:
        char = XOR(tweede,int(a[code]))
    if code % 3 == 2:
        char = XOR(derde,int(a[code]))
    tekst += chr(char)

for symbol in tekst:
    waarden += ord(symbol)
print(waarden)
print(tekst)
input()
import time
import math
n = int(input())
berichten = []
for i in range(0,n):
    add = input()
    berichten.append(add)
    
for i in range(0,n):
    tekst = berichten[i].split(' ')
    if(len(tekst) > 4):
        print("Crackers!")
    else:
        print(str(berichten[i]) + " krAh!")
import math
import time
n = int(input())
berichten = []
for i in range(0,n):
    add = input()
    berichten.append(add)
    
count = 0
for i in range(0,n):
    for j in range(0,len(berichten[i])):
        if (berichten[i][j] == '#'):
            count += 1
count *= 5
print("Om de hekjes in dit weiland te verven heb je " + str(count) + " liter verf nodig")
            
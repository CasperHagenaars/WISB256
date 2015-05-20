import math
count = int(input())


def tetra(n):
    i = 0
    j = 0
    k = 0
    l = 1
    for tel in range(0,n-3):
        temp = l
        l = l + k + j + i
        i = j
        j = k
        k = temp
    return l

if count < 3:
    print("0")
else:
    if count == 3:
        print("1")
    else:
        print(tetra(count))
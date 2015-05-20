a = set()
num = 1
den = 1
for i in range(10,100):
    for j in range(i,100):
        i2 = list(str(i))
        j2 = list(str(j))
        try:
            if((i/j == float(i2[0])/float(j2[1])) and (i2[1] == j2[0]) and (i2[0] != i2[1]) and (j2[0] !=j2[1])):
                num *= i
                den *= j
                print("("+str(i) + ", " +str(j)+ ") ")
        except:
            continue
print(str(num) + ", "+ str(den))

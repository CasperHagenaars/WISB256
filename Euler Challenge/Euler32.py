import time
T1 = time.time()
def check(n):
    ans = []
    for i in range(n,50000):
        if(len(str(n)) + len(str(i)) + len(str(n*i)) != 9):
            continue
        test = set()
        testlijst = []
        nlist = list(str(n))
        ilist = list(str(i))
        nilist = list(str(n*i))
        for q in nlist:
            test.add(q)
            testlijst.append(q)
        for j in ilist:
            test.add(j)
            testlijst.append(j)
        for k in nilist:
            test.add(k)
            testlijst.append(k)
        if(len(test) == len(testlijst) and len(test) == 9):
            if '0' not in test:
                ans.append(n*i)
                print(str(ans) + ", " + str(n) + ", " +str(i))
    return ans

antwoord = set()
for i in range(1,100):
    x = check(i)
    if(x != []):
       for pan in x:
        antwoord.add(pan)
print(antwoord)
print(sum(antwoord))
T2 = time.time()
print(str(T2-T1)+ " seconds have passed")
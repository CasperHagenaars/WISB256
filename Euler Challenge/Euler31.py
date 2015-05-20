import time
T1 = time.time()
count = 2
for penny100 in range(0,2):
    for penny50 in range(0,5):
        for penny20 in range(0,11):
            for penny10 in range(0,21):
                if(10*penny10 + 20*penny20 + 50 * penny50 + 100*penny100 < 201):
                    for penny in range(0,201):
                        for penny2 in range(0,101):
                                for penny5 in range(0,41):
                                    if penny + 2*penny2 + 5*penny5 + 10*penny10 + 20*penny20 + 50 * penny50 + 100*penny100 == 200:
                                        count +=1


print(count)
T2 = time.time()
print(str(T2-T1))
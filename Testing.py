import Functions
import time
T1 = time.time()
count = 0
for i in range(100):
    count += Functions.totient(i)
T2 = time.time()
print(T2-T1)
input()
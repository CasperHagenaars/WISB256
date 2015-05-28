import math
maanden = [31,28,31,30,31,30,31,31,30,31,30,31]
dagen = [0,0,0,0,0,0,1]
naamdagen = ["maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag"]
naammaanden = ["jan", "feb", "maart", "april", "mei","juni","juli", "aug", "sept", "okt", "nov", "dec"]
jaar = 1901
start = "dinsdag 1 januari 1901"
dag = 1
def check(d,jaar):
    count = 0
    maanden[1] = 28
    if(jaar % 4 == 0):
        maanden[1] = 29
        
    for i in range(12):
        print(str(naamdagen[d])+ ", " + str(naammaanden[i])+ ","+ str(jaar))
        zon = dagen[d]
        count += zon
        d = (d + maanden[i]) % 7
        
    return [count,d]
count = 0
for i in range(1901,2001):
    result = check(dag,i)
    count += result[0]
    dag = result[1]
print(count)
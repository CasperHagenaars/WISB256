import math
import fractions
import decimal
decimal.getcontext().prec = 1000
def it(n):
    tel = decimal.Decimal(0)
    for i in range(n):
        tel = 1/(2+tel) 
    return 1 + tel        

def check(nomdomlijst):
    if len(nomdomlijst[0]) > len(nomdomlijst[1]):
        return True
    else:
        return False
        
def fractionmaker(n):
    temp = fractions.Fraction(n).limit_denominator(10**500)
    return str(temp).split('/')

print(fractionmaker(it(5)))
print(fractionmaker(it(1000)))

counter = 0
s = ""
for i in range(1,1001):
    if check(fractionmaker(it(i))) == True:
        counter +=1
    if(i%100 == 0):
        print(i)
print(counter)
input()
import math
v = int(input())
z = int(input())
h = int(input())

result = math.asin(z*h/v/v)/2
print(str("{0:.2f}".format(result)))
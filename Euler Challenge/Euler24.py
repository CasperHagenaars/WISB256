import itertools
import math

a = list(itertools.permutations(list(str(1234567890))))
a = sorted(a)
print(a[999999])
input()
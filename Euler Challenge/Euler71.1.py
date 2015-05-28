import math
import fractions
from time import time
print(fractions.Fraction(3.0/7-0.000001).limit_denominator(1000000))
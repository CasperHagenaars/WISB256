import math
record = 1
record_a = 0
record_b = 0
def rec(a,b):
    power = str(a**b)
    som = 0
    for digit in power:
        som += int(digit)
    return som
    
for eerste in range(1,100):
    for tweede in range(1,100):
        if rec(eerste,tweede) > record:
            record = rec(eerste,tweede)
            record_a = eerste
            record_b = tweede
print(record)
print(record_a)
print(record_b)
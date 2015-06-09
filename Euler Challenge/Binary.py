def base2(x):
    return int(bin(x)[2:])
def base10(x):
    return int(str(x),2)
def XOR(a,b):
    result = ""
    a = str(base2(a))
    b = str(base2(b))
    if(len(a) < len(b)):
        a = '0'*(len(b)-len(a))+a
    else:
        b = '0'*(len(a)-len(b))+b
    for i in range(len(a)):
        result += str((int(a[i])+int(b[i])) % 2)
    return base10(result)

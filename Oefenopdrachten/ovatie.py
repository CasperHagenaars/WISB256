n = input()
lijst = list(str(input()))
vrienden = 0
staand = 0
for i in range(0,len(lijst)):
    if(int(lijst[i]) > 0):
        var = i - staand
        if(var <= 0):
            staand += int(lijst[i])
        else:
            vrienden += var
            staand += var + int(lijst[i])
print(vrienden)
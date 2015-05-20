n = input()
lijst = list(str(input()))
vrienden = 0
staand = 0
for i in range(0,len(lijst)):
    nummer = int(lijst[i])
    if(nummer > 0):
        var = i - staand
        if(var <= 0):
            staand += nummer
        else:
            vrienden += var
            staand += var + nummer
print(vrienden)
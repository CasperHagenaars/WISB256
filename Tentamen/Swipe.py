import math

def start():
    wboek = int(input())
    woordenboek = []
    for i in range(0,wboek):
        add = input()
        woordenboek.append(add)
    return woordenboek
    
woordenboek = list(start())
swipe = start()
probeer = list(swipe)
gevonden = []
for j in probeer:
    for i in woordenboek:
        mislukt = 0
        if(len(i)>len(j)):
            mislukt = 1
            break
        tel = 0
        indexnu = 0
        while(tel < len(i)):
            if(tel == len(j)):
                break
            try:
                indexnu = j.find(i[tel],indexnu)
                if(indexnu > -1):
                    tel += 1
                else:
                    mislukt = 1
                    break
            except:
                mislukt = 1
                break
        if mislukt == 0:
            gevonden.append(i)
            break
    if mislukt == 1:
        gevonden.append("?")
        break
                
string = ""
for i in gevonden:
    string += i 
    string += "\n"
print(string)

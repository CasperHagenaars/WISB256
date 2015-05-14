n = int(input())
zetten = []
for i in range(n):
    zetten.append(str(input()))

dobbelsteen = ['1','2','3','4','5','6']

def omlaag(lijst):
    temp = lijst[5]
    lijst[5] = lijst[2]
    lijst[2] = lijst[0]
    lijst[0] = lijst[3]
    lijst[3] = temp
    return lijst

def omhoog(lijst):
    temp = lijst[5]
    lijst[5] = lijst[3]
    lijst[3] = lijst[0]
    lijst[0] = lijst[2]
    lijst[2] = temp
    return lijst

def rechts(lijst):
    temp = lijst[5]
    lijst[5] = lijst[1]
    lijst[1] = lijst[0]
    lijst[0] = lijst[4]
    lijst[4] = temp
    return lijst

def links(lijst):
    temp = lijst[5]
    lijst[5] = lijst[4]
    lijst[4] = lijst[0]
    lijst[0] = lijst[1]
    lijst[1] = temp
    return lijst

for i in range(0,n):
    zet = zetten[i]
    if(zet == 'omlaag'):
        dobbelsteen = omlaag(dobbelsteen)
    if(zet == 'omhoog'):
        dobbelsteen = omhoog(dobbelsteen)
    if(zet == 'links'):
        dobbelsteen = links(dobbelsteen)
    if(zet == 'rechts'):
        dobbelsteen = rechts(dobbelsteen)

print(dobbelsteen[5])

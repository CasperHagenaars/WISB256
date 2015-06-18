oplossingen = []
def summations(limit = 100,verz = [],getal=0):
        if sum(verz) > limit:
            verz = []
        if sum(verz) == limit:
            print("Debug")
            oplossingen.append(verz)
            verz = []
        getal += 1
        if getal < limit:
            summations(limit,verz,getal)
            verz.append(getal)
            summations(limit,verz,getal)
        
summations(10)
print(oplossingen)
print("HUH")
input()
rij1 = list(str(input()))
rij2 = list(str(input()))
rij3 = list(str(input()))
spel = [rij1,rij2,rij3]

def win(a,b,c):
    if a == b:
        if b == c:
            if a == '1':
                return "Player 1 wins"
            if a == '2':
                return "Player 2 wins"
    return None
def horz(spel):
    for i in range(0,3):
        result = win(spel[i][0],spel[i][1],spel[i][2])
        if(result != None):
            return result
    return None
    
def vert(spel):
    for i in range(0,3):
        result = win(spel[0][i],spel[1][i],spel[2][i])
        if(result != None):
            return result
    return None
    
def diag(spel):
    diag1 = win(spel[0][0],spel[1][1],spel[2][2])
    diag2 = win(spel[2][0],spel[1][1],spel[0][2])
    if(diag1 != None):
        return diag1
    if(diag2 != None):
        return diag2
    return None
    
def bereken(spel):
    if(horz(spel) != None):
        return horz(spel)
    if(vert(spel) != None):
        return vert(spel)    
    if(diag(spel) != None):
        return diag(spel)
    return "No winner"

print(bereken(spel))
import math
class Vector:
    def __init__(self, n, waarde = 0.0):
        a = []
        if(type(waarde) == type([])):
            a = waarde
        else:
            for i in range(n):
                a.append(waarde)
        self.vectors = a
        self.lengte = len(a)

    def __str__(self):
        st = ""
        for i in self.vectors:
            rounded = format(i, '.6f')
            st += str(rounded) + "\n"
        st = st[:-1]
        return st

    def lincomb(self,other,alpha,beta):
        vec = Vector(other.lengte)
        for i in range(other.lengte):
            vec.vectors[i] = beta * other.vectors[i] + self.vectors[i] * alpha
        return vec

    def scalar(self,alpha):
        vec = Vector(self.lengte)
        for i in range(self.lengte):
            vec.vectors[i] = float(alpha)*self.vectors[i]
        return vec

    def norm(self):
        dist = 0
        for i in range(self.lengte):
            dist += self.vectors[i]*self.vectors[i]
        return math.sqrt(dist)

    def inner(self,other):
        dist = 0
        for i in range(self.lengte):
            dist += self.vectors[i]*other.vectors[i]
        return dist
    
    def proj(self, other):
        sc = self.inner(other)/self.inner(self)
        projection = self.scalar(sc)
        return projection 

        
def GrammSchmidt(vectoren):
    orth = []
    for x in vectoren:
        som = Vector(x.lengte)
        for y in orth:
            som = som.lincomb(y.proj(x),1,1)
        orth.append(x.lincomb(som,1,-1))
    for i in orth:
        inner = i.inner(i)
        for j in range(i.lengte):
            i.vectors[j] /= math.sqrt(inner)
    return orth
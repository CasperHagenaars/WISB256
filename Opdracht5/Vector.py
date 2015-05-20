import math
class Vector:
    def __init__(self, n, waarde = 0.00000):
        a = []
        global aantal 
        aantal = n
        if(type(waarde) == type([])):
            for i in waarde:
                a.append(i)
        else:
            for i in range(n):
                a.append(waarde)
        self.vectors = a
        self.lengte = len(a)
            
    def __str__(self):
        st = ""
        for i in self.vectors:
            st += str(i) + "\n"
        st = st[:-1]
        return st
        
    def lincomb(self,other,alpha,beta):
        vec = Vector(other.lengte,3)
        for i in range(aantal):
            vec.vectors[i] = beta * other.vectors[i] + self.vectors[i] * alpha
        return vec
    
    def scalar(self,alpha):
        vec = Vector(self.lengte)
        for i in range(aantal):
            vec.vectors[i] = int(alpha)*self.vectors[i]
        return vec
        
    def norm(self):
        dist = 0
        for i in range(aantal):
            dist += self.vectors[i]*self.vectors[i]
        return math.sqrt(dist)

    def inner(self,other):
        dist = 0
        for i in range(aantal):
            dist += self.vectors[i]*other.vectors[i]
        return dist
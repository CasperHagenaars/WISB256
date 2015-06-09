from scipy.integrate import odeint
import numpy as np

class Lorenz:
        def __init__(self, positie, sigma=10, rho=28, beta=8/3):
            self.startpositie = positie
            self.sigma = sigma
            self.rho = rho
            self.beta = beta
                
        def lorenz(self,positie,tijd):
                x_dot = self.sigma*(positie[1] - positie[0])
                y_dot = positie[0]*(self.rho - positie[2]) - positie[1]
                z_dot = positie[0]*positie[1] - self.beta*positie[2]
                return [x_dot, y_dot, z_dot]
                
        def solve(self,T,dt):
            tijd = np.arange(0, T+dt, dt)
            func = odeint(self.lorenz, [self.startpositie[0],self.startpositie[1],self.startpositie[2]], tijd)
            return func
        
        def jacobian(self,positie):
            return nd.Jacobian(positie)
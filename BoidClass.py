## AERO 470 Team Project Boid Class

from vpython import *

import random as rand
import numpy as np
import math as m

class Boid:

    def __init__(self, simulationArea = [ [0, 100], [0, 100], [0, 100] ], makeTrails = False):
        
        x = rand.uniform(simulationArea[0][0], simulationArea[0][1])
        y = rand.uniform(simulationArea[1][0], simulationArea[1][1])
        z = rand.uniform(simulationArea[2][0], simulationArea[2][1])

        self.position = vec(x, y, z)
        self.velocity = vec(0, 0, 0)

        self.birb = cone(pos = self.position, axis = vec(1, 0, 0), make_trail = makeTrails)

    def rule1(self,flock):
        N = flock.nBoids
        flock = flock.members
        birb = Boid.birb
        pcj = 0
        for birb in flock:
            if birb == self.birb:
                pass
            else:
                pcj = pcj + birb.pos
    
        pcj = pcj/(N - 1)
        v1 = (pcj - self.birb.pos)/100
        return v1

    def rule2(self,flock):
        flock = flock.members
        birb = Boid.birb
        c = vector(0,0,0)
        boidProx = 5

        for birb in flock:
            if birb == self.birb:
                pass
            else:
                check = birb.pos - self.birb.pos
                if check.mag < boidProx:
                    c = c - check
                else:
                    pass
        return c

    def rule3(self,flock):
        N = flock.nBoids
        flock = flock.members
        birb = Boid.birb
        pvj = vector(0,0,0)
        for birb in flock:
            if birb == self.birb:
                pass
            else:
                pvj = pvj + birb.velocity
        pvj = pvj/(N-1)
        v3 = (pvj - self.velocity)/8
        return v3

class Flock:

    def __init__(self, nBoids = 10):

        self.members = [Boid() for i in range(nBoids)]
        self.nBoids = nBoids


    def moveAllBoids(self):

        boid: Boid
        for boid in self.members:

            v1 = boid.rule1(self)
            v2 = boid.rule2(self)
            v3 = boid.rule3(self)
            
            boid.velocity = boid.velocity + v1 + v2 + v3
            boid.position = boid.position + boid.velocity
            boid.birb.pos = boid.position



    
        

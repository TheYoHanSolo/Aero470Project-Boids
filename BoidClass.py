## AERO 470 Team Project Boid Class

from vpython import *

import random as rand
import numpy as np
import math as m

class Boid:

    def __init__(self, simulationArea = [ [0, 10], [0, 10], [0, 10] ], makeTrails = False):
        
        x = rand.uniform(simulationArea[0][0], simulationArea[0][1])
        y = rand.uniform(simulationArea[1][0], simulationArea[1][1])
        z = rand.uniform(simulationArea[2][0], simulationArea[2][1])

        self.position = vec(x, y, z)
        self.velocity = vec(0, 0, 0)

        self.birb = cone(pos = self.position, axis = vec(1, 0, 0), make_trail = makeTrails)

    def rule1(self,flock,numBirds):
        flock = flock.members
        birb = Boid.birb
        pcj = 0
        for birb in flock:
            if birb == self.birb:
                pass
            else:
                pcj = pcj + birb.pos
    
        pcj = pcj/(numBirds - 1)
        v1 = (pcj - self.birb.pos)/100
        return v1

    def rule2(self):
        flock = flock.members
        birb = Boid.birb
        c = vector(0,0,0)
        for birb in flock:
            if birb == self.birb:
                pass
            else:
                pcj = pcj + birb.pos

class Flock:

    def __init__(self, nBoids = 10):

        self.members = [Boid() for i in range(nBoids)]
        

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
        self.birb = cone(pos = self.position, axis = vec(1, 0, 0), make_trail = makeTrails)



    def Rule1(self):
        pass

class Flock:

    def __init__(self):
        pass

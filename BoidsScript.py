# Initial Boids script file

from vpython import *

import numpy as np
import matplotlib.pyplot as plt
import random as rand

import BoidClass as Boid


flock = Boid.Flock()
limits = [-100,100,-100,100,-100,100,0.5]

while 1:

    rate(100)
    flock.moveAllBoids(limits)

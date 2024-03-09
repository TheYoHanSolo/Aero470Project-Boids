# Initial Boids script file

from vpython import *

import numpy as np
import matplotlib.pyplot as plt
import random as rand

import BoidClass as Boid


flock = Boid.Flock(nBoids = 30)
limits = [-100,100,-100,100,-100,100,0.75]

while 1:

    rate(100)
    flock.moveAllBoids(limits)
    #scene.camera.pos(flock.members[0].birb.pos)

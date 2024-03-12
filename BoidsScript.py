# Initial Boids script file

from vpython import *

import numpy as np
import matplotlib.pyplot as plt
import random as rand

import BoidClass as Boid


flock = Boid.Flock(nBoids = 30)
limits = [-100,100,-100,100,-100,100, 0.8]

hawk1 = Boid.Hawk(killDistance=3)

while 1:

    rate(100)

    if hawk1.followingFlag == False:
        hawk1.findNearestBoid(flock)

    else:
       hawk1.huntTargetedBoid(flock)

    flock.moveAllBoids(limits, hawk1)

    #scene.camera.pos = flock.members[0].birb.pos

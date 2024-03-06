#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 16:49:28 2024

@author: johangovaars
"""

from vpython import *
import math

# Initial States of the bodies
rME = vec(0, 0.2, 0)
vME = vec(-1, 0, 0)
vE = vec(0, 0.5, 0)
rE = vec(0.75, 0, 0)

# Defines the locations and sizes of the bodies
sun = sphere(pos = vec(0, 0, 0), radius = 0.1, color = color.yellow)
earth = sphere(pos = rE, radius = 0.05, color = color.blue)

# Moon is relative to the Earth
moon = sphere(pos = earth.pos + rME, radius = 0.01, color = color.white)


#earth.velocity = vec(0, 0.1, 0)
#moon.velocity = earth.velocity + vME

#v = earth.velocity
v = vE
r = earth.pos

vM = vME
rM = rME

# Parametric representation of orbit using angular velocity
angVel = v.mag/r.mag
angVelM = vM.mag/rM.mag

# Initial angular location and time step
theta0 = 0
theta0M = 0
dt = 0.01

scene.autoscale = False
#scene.camera.axis.z = -scene.camera.axis.z

#scene.camera.pos = moon.pos

# Runs the simulation
while 1:
    
    rate(100)
    
    # Angular position given initial position and angular velocity
    theta = theta0 + angVel*dt
    thetaM = theta0M + angVelM*dt
    
    # Makes sure the angle is between 0 and 2pi
    theta = theta%(2*math.pi)
    
    # Parametric curve for the Earth and Moon
    earth.pos.y = rE.mag*math.sin(theta)
    earth.pos.x = rE.mag*math.cos(theta)
    
    # Moon's position is relative to Earth
    moon.pos.y = rME.mag*math.sin(thetaM) + earth.pos.y
    moon.pos.x = rME.mag*math.cos(thetaM) + earth.pos.x
    
    
    #
    #scene.camera.pos = earth.pos + vec(rME.mag*math.cos(thetaM), rME.mag*math.sin(thetaM), 0);
    scene.camera.follow(moon)

    
    #earth.velocity.y = v.mag*math.cos(theta)
    #earth.velocity.x = v.mag*math.sin(theta)
    
    theta0 = theta
    theta0M = thetaM
    
    #print(earth.pos.mag)
    
    
    
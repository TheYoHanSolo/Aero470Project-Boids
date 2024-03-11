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
        self.oob = False

        self.birb = cone(pos = self.position, axis = vec(-1, 0, 0), make_trail = makeTrails)

    def rule1(self,flock):
        N = flock.nBoids
        flock = flock.members
        Birb_i: Boid
        pcj = vector(0,0,0)
        for Birb_i in flock:
            if Birb_i == self.birb:
                pass
            else:
                pcj = pcj + Birb_i.birb.pos
    
        pcj = pcj/(N - 1)
        v1 = (pcj - self.birb.pos)/100
        return v1

    def rule2(self,flock):
        flock = flock.members
        Birb_i: Boid
        c = vector(0,0,0)
        boidProx = 20

        for Birb_i in flock:
            if Birb_i == self.birb:
                pass
            else:
                check = Birb_i.birb.pos - self.birb.pos
                if check.mag < boidProx:
                    c = c - check
                    #c = c.norm()

                    c = c*0.01
                    
                else:
                    pass
        return c

    def rule3(self,flock):
        N = flock.nBoids
        flock = flock.members
        Birb_i: Boid
        pvj = vector(0,0,0)
        for Birb_i in flock:
            if Birb_i == self.birb:
                pass
            else:
                pvj = pvj + Birb_i.velocity
        pvj = pvj/(N-1)
        v3 = (pvj - self.velocity)/16
        return v3
    
    def rule4(self, hawk):

        v4 = -(hawk.velocity)*0.005

        return v4

    def BoundPosition(self,xmin,xmax,ymin,ymax,zmin,zmax):
        if self.birb.pos.x < xmin:
            self.velocity.x = 10
            self.oob = True
            #self.velocity.x = -self.velocity.x

        elif self.birb.pos.x > xmax:
            self.velocity.x = -10
            self.oob = True
            #self.velocity.x = -self.velocity.x

        if self.birb.pos.y < ymin:
            self.velocity.y = 10
            self.oob = True
            #self.velocity.y = -self.velocity.y
        elif self.birb.pos.y > ymax:
            self.velocity.y = -10
            self.oob = True
            #self.velocity.y = -self.velocity.y

        if self.birb.pos.z < zmin:
            self.velocity.z = 10
            self.oob = True
            #self.velocity.z = -self.velocity.z
        elif self.birb.pos.z > zmax:
            self.velocity.z = -10
            self.oob = True
            #self.velocity.z = -self.velocity.z

        else:
            self.oob = False

    def LimitSpeed(self,vlim):
        if self.velocity.mag > vlim:
            self.velocity = (self.velocity/self.velocity.mag)*vlim

class Flock:

    def __init__(self, nBoids = 10):

        self.members = [Boid() for i in range(nBoids)]
        self.nBoids = nBoids
        self.vLim = 0


    def moveAllBoids(self, limits, hawk):
        xmin = limits[0]
        xmax = limits[1]
        ymin = limits[2]
        ymax = limits[3]
        zmin = limits[4]
        zmax = limits[5]
        vlim = limits[6]
        self.vLim = vlim

        boid: Boid
        for boid in self.members:

            v1 = boid.rule1(self)
            v2 = boid.rule2(self)
            v3 = boid.rule3(self)
            v4 = boid.rule4(hawk)
            boid.velocity = boid.velocity + v1 + v2 + v3 + v4
            boid.LimitSpeed(vlim)            
            
            boid.position = boid.position + boid.velocity
            boid.birb.pos = boid.position
            boid.birb.axis = boid.velocity.norm()
            boid.BoundPosition(xmin,xmax,ymin,ymax,zmin,zmax)



class Hawk:

    def __init__(self, simulationArea = [ [0, 100], [0, 100], [0, 100] ], makeTrails = False, maxSpeed = 0.1, killDistance = 10):
        
        x = rand.uniform(simulationArea[0][0], simulationArea[0][1])
        y = rand.uniform(simulationArea[1][0], simulationArea[1][1])
        z = rand.uniform(simulationArea[2][0], simulationArea[2][1])

        self.position = vec(x, y, z)
        self.velocity = vec(0, 0, 0)
        self.oob = False
        self.maxSpeed = maxSpeed
        self.followingFlag = False
        self.targetedBoid = 0
        self.killDistance = killDistance
        self.huntAttempts = 0

        self.hawk = cone(pos = self.position, axis = vec(-1, 0, 0), make_trail = makeTrails)
        self.hawk.color = color.red


    def findNearestBoid(self, flock):

        boid: Boid
        vect: vec
        relDist = []
        dist = []

        if len(flock.members) == 0:

            self.velocity = vec(0, 0, 0)

        else:


            for boid in flock.members:

                relDist.append(boid.position - self.position)


            for vect in relDist:

                dist.append(vect.mag)

            minDist = dist.index(min(dist))

            #relVel = (relDist[minDist].norm())*self.maxSpeed
            self.followingFlag = True
            #self.velocity = relVel
            self.targetedBoid = minDist

            #print('Test')

    def huntTargetedBoid(self, flock):

        relDist = flock.members[self.targetedBoid].position - self.position

        relVel = (relDist.norm())*self.maxSpeed

        if relDist.mag < self.killDistance:

            flock.members[self.targetedBoid].birb.color = color.magenta
            flock.members.remove(flock.members[self.targetedBoid])
            self.followingFlag = False
            self.targetedBoid = 0

        else:

            self.velocity = self.velocity + relVel
            self.LimitSpeed(flock.vLim)
            self.position = self.position + self.velocity
            self.hawk.pos = self.position
            self.hawk.axis = self.velocity.norm()
            self.huntAttempts += 1

        if self.huntAttempts > 400:

            self.followingFlag = False


    def LimitSpeed(self,vlim):

        hawkVLim = vlim*1.3
        if self.velocity.mag > hawkVLim:
            self.velocity = (self.velocity/self.velocity.mag)*hawkVLim
        


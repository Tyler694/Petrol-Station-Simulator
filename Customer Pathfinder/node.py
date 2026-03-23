import math
from settings import *

class Node:

    def __init__(self, pos, start, end, previousFCost, nodeBeginning):
        self.pos = pos
        self.start = start
        self.end = end
        self.previousFCost = previousFCost
        self.nodeBeginning = nodeBeginning

        self.colour = (150, 150, 150)

        self.boundary = False

        self.G_COST = 0
        self.H_COST = 0
        self.F_COST = 0

        self.boundaryCheck()
        self.calculateDistances()

    def boundaryCheck(self):
        if (self.pos[0]*TILESIZE,self.pos[1]*TILESIZE) in BOUNDARIES:
            self.boundary = True

    def calculateDistances(self):
        #H_COST is the distance to the end
        #F_COST is the distance to the start
        #G_COST is the total distance
        
        self.H_COST = ((abs(self.pos[0] - self.end[0]) + abs(self.pos[1] - self.end[1])) * 10)
        self.F_COST = ((math.sqrt(abs(self.pos[0] - self.nodeBeginning[0])**2 + abs(self.pos[1] - self.nodeBeginning[1])**2) * 10) // 1) + self.previousFCost

        self.G_COST = self.H_COST + self.F_COST
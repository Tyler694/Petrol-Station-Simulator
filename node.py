import math
from settings import *

class Node:

    def __init__(self, pos, end, previousNode):
        self.pos = pos
        self.end = end
        self.previousNodePos = previousNode.pos
        self.previousNodeG_COST = previousNode.G_COST
        self.parentNode = previousNode

        self.G_COST = 0
        self.H_COST = 0
        self.F_COST = 0

        self.calculateCosts()

    def calculateCosts(self):
        self.G_COST = ((math.sqrt((abs(self.pos[0]-self.previousNodePos[0])**2)+(abs(self.pos[1]-self.previousNodePos[1])**2))*10) // 1) + self.previousNodeG_COST
        self.H_COST = (abs(self.pos[0]-self.end[0]) + abs(self.pos[1]-self.end[1])) * 10
        self.F_COST = self.G_COST + self.H_COST


class StartNode(Node):
    def __init__(self, pos, end):
        self.pos = pos
        self.end = end

        self.G_COST = 0
        self.H_COST = 0
        self.F_COST = 0

        self.calculateCosts()


    def calculateCosts(self):
        self.H_COST = (abs(self.pos[0]-self.end[0]) + abs(self.pos[1]-self.end[1])) * 10
        self.F_COST = self.G_COST + self.H_COST

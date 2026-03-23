import pygame
from settings import *
from node import *

class Pathfind:

    def __init__(self):
        self.nodes = []

        self.start = (1, 2)
        self.end = (10,1)

        self.i = 0

        self.currentNodes = []
        self.nodePositions = []

        self.LOWEST_H_COST = 5000
        self.LOWEST_G_COST = 5000

        self.screen = pygame.display.get_surface()

        self.currentTile(self.start, 0)

    def drawNodes(self):
        for node in self.nodes:
            pygame.draw.rect(self.screen, node.colour, (node.pos[0]*TILESIZE,node.pos[1]*TILESIZE,TILESIZE-1,TILESIZE-1))

        pygame.draw.rect(self.screen, (255, 100, 100), (self.start[0]*TILESIZE,self.start[1]*TILESIZE,TILESIZE-1,TILESIZE-1))
        pygame.draw.rect(self.screen, (100, 100, 255), (self.end[0]*TILESIZE,self.end[1]*TILESIZE,TILESIZE-1,TILESIZE-1))

    def currentTile(self, pos, previousFCost):
        for i in range(3):
            for j in range(3):
                x = (pos[0] - 1) + j
                y = (pos[1] - 1) + i

                if (x,y) not in self.nodePositions and (j,i) != (1,1):
                    self.nodes.append(Node((x,y), self.start, self.end, previousFCost, pos))
                    self.nodePositions.append((x,y))

        for node in self.nodes:
            if node.pos == self.end:
                return
            if node.boundary:
                self.nodes.remove(node)

        self.findLowestGCost()
        self.findLowestHCost()

        self.next_tile()

    def findLowestGCost(self):
        self.LOWEST_G_COST = self.nodes[0].G_COST
        for node in self.nodes:
            if node.G_COST < self.LOWEST_G_COST:
                self.LOWEST_G_COST = node.G_COST

        for node in self.nodes:
            if node.G_COST == self.LOWEST_G_COST:
                self.currentNodes.append(node)

        
    def findLowestHCost(self):
        self.LOWEST_H_COST = self.nodes[0].H_COST
        for node in self.currentNodes:
            if node.H_COST < self.LOWEST_H_COST:
                self.LOWEST_H_COST = node.H_COST


    def next_tile(self):
        print("====")
        for node in self.nodes:
            print(node.H_COST, node.F_COST, node.G_COST)
            if node.G_COST == self.LOWEST_G_COST and node.H_COST == self.LOWEST_H_COST and  self.i != 6:
                node.colour = (75 ,75, 75)
                self.i += 1
                self.currentTile(node.pos, node.F_COST)
                return
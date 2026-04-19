import pygame
from settings import *
from node import *

class Pathfind:

    def __init__(self, start, end):
        self.start = start
        self.end = end

        self.nodePos = []
        self.openNodes = []
        self.closedNodes = []
        self.path = []
        self.i = 0

        self.finished = False

        self.screen = pygame.display.get_surface()

        self.startNode = StartNode(self.start,self.end)
        self.openNodes.append(self.startNode)

        self.createChildren(self.startNode)
        self.reconstructPath()

    def reconstructPath(self):
        node = self.closedNodes[-1]

        while node != self.startNode:
            self.path.append(node)
            node = node.parentNode

    def drawNodes(self):
        for node in self.path:
            pygame.draw.rect(self.screen, (100,100,150), (node.pos[0]*TILESIZE,node.pos[1]*TILESIZE,TILESIZE-1,TILESIZE-1))

        pygame.draw.rect(self.screen, (255, 100, 100), (self.start[0]*TILESIZE,self.start[1]*TILESIZE,TILESIZE-1,TILESIZE-1))
        pygame.draw.rect(self.screen, (100, 100, 255), (self.end[0]*TILESIZE,self.end[1]*TILESIZE,TILESIZE-1,TILESIZE-1))

    def createChildren(self, previousNode):
        for node in self.openNodes:
            self.nodePos.append(node.pos)

        for i in range(3):
            for j in range(3):
                if previousNode != self.startNode:
                    x = (previousNode.pos[0] - 1) + j
                    y = (previousNode.pos[1] - 1) + i
                else:
                    x = (self.startNode.pos[0] - 1) + j
                    y = (self.startNode.pos[1] - 1) + i

                if (x*TILESIZE,y*TILESIZE) not in BOUNDARIES and (j,i) != (1,1) and (x,y) not in self.nodePos:
                    tempNode = Node((x,y), self.end, previousNode)

                    if tempNode.H_COST < self.startNode.H_COST:
                        self.openNodes.append(tempNode)

                if (x,y) == self.end:
                    return
                
        self.next_node()


    def next_node(self):
        currentNode = self.findLowestF()
        
        self.openNodes.remove(currentNode)
        self.closedNodes.append(currentNode)

        self.nodePos.clear()

        self.createChildren(currentNode)

    def findLowestF(self):
        currentNode = self.openNodes[0]
        for node in self.openNodes:
            if node.F_COST < currentNode.F_COST:
                currentNode = node
        return currentNode






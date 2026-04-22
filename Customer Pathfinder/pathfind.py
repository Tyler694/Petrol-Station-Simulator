from node import *
import pygame

class Pathfind:

    def __init__(self, start, end):
        self.screen = pygame.display.get_surface()

        self.start = start
        self.end = end

        self.openList = []
        self.closedList = []
        self.path = []
        self.evaluatedNodes = []

        self.startNode = Node(self.start, self.end, None)
        self.openList.append(self.startNode)
        self.evaluatedNodes.append(self.startNode.pos)

        self.search = True

        self.i = 0

    def reconstruct_path(self):
        node = self.closedList[-1]
        while node != None:
            self.path.append(node)
            node = node.parentNode

    def drawPath(self):
        for node in self.path:
            pygame.draw.rect(self.screen, (255,100,100), (node.pos[0]*TILESIZE, node.pos[1]*TILESIZE, TILESIZE-1, TILESIZE-1))

        pygame.draw.rect(self.screen, (100,255,100), (self.end[0]*TILESIZE, self.end[1]*TILESIZE, TILESIZE-1, TILESIZE-1))
        pygame.draw.rect(self.screen, (100,100,255), (self.start[0]*TILESIZE, self.start[1]*TILESIZE, TILESIZE-1, TILESIZE-1))

    def createPath(self):
        while len(self.openList) > 0 and self.search != False:
            currentNode = self.findLowestFCost()

            self.openList.remove(currentNode)
            self.closedList.append(currentNode)

            self.generateSuccessor(currentNode)

            self.i += 1

    def generateSuccessor(self, previousNode):
        for i in range(3):
            for j in range(3):
                if (i,j) != (1,1):
                    x = (previousNode.pos[0] - 1) + j
                    y = (previousNode.pos[1] - 1) + i

                    if (x,y) == self.end:
                        self.search = False
                        self.reconstruct_path()
                        return

                    if (x*TILESIZE,y*TILESIZE) not in BOUNDARIES and (x,y) not in self.evaluatedNodes:
                        succesor = Node((x,y), self.end, previousNode)

                        succesor.calculateCosts()
                        self.openList.append(succesor)
                        self.evaluatedNodes.append(succesor.pos)

    def findLowestFCost(self):
        currentNode = self.openList[0]
        for node in self.openList:
            if node.F_COST < currentNode.F_COST:
                currentNode = node
        
        return currentNode
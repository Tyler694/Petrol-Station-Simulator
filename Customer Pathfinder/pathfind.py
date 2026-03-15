import pygame
from settings import *
from node import *
import random

class Pathfind:

    def __init__(self):
        self.Start_Pos = (15, 5)
        self.End_Pos = (20, 5)

        self.nodes = []
        self.route = []

        self.i = 0

        self.screen = pygame.display.get_surface()

        self.next_node(self.Start_Pos)

    def draw(self):
        pygame.draw.rect(self.screen, (255, 50, 50), (self.Start_Pos[0] * TILESIZE, self.Start_Pos[1] * TILESIZE, TILESIZE-1, TILESIZE-1))
        pygame.draw.rect(self.screen, (50, 50, 255), (self.End_Pos[0] * TILESIZE, self.End_Pos[1] * TILESIZE, TILESIZE-1, TILESIZE-1))

        for node in self.route:
            pygame.draw.rect(self.screen, (200, 200, 200), (node.pos[0]*TILESIZE, node.pos[1]*TILESIZE, TILESIZE-1, TILESIZE-1))

    def next_node(self, pos):
        for i in range(3):
            for j in range(3):
                x = (pos[0] - 1) + j
                y = (pos[1] - 1) + i

                if (i,j) != (1,1) and (x*TILESIZE,y*TILESIZE) not in BOUNDARIES:
                    self.nodes.append(Node((x,y), self.Start_Pos, self.End_Pos))

        #Find Lowest Total Dist
        LOWEST_TOTAL_DIST_ARRAY = []
        for index, node in enumerate(self.nodes):
            LOWEST_TOTAL_DIST_ARRAY.append([node.TotalDist, index])
        
        LOWEST_TOTAL_DIST_ARRAY = self.findLowestValue(LOWEST_TOTAL_DIST_ARRAY)

        self.nodes.append(LOWEST_TOTAL_DIST_ARRAY[0])

        LOWEST_END_DIST_ARRAY = []
        for index, node in enumerate(self.nodes):
            LOWEST_END_DIST_ARRAY.append([node.DistToEnd, index])


        self.route.append(self.nodes[LOWEST_END_DIST_ARRAY[0][1]])

        if self.i != 5:
            self.i+=1
            self.next_node(self.route[0].pos)

    def findLowestValue(self, array):
        array.sort()
        i=1
        while len(array) != i:
            if array[i][0] != array[0][0]:
                array.pop(i)
            else:
                i+=1
        
        return array


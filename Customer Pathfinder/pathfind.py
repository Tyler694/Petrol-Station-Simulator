import pygame
from settings import *
from node import *

class Pathfind:

    def __init__(self):
        self.start_pos = (12,5)
        self.end_pos = (15, 0)

        self.nodes = []
        self.TILES = []

        self.screen = pygame.display.get_surface()

        self.next_node(self.start_pos[0], self.start_pos[1])



    def draw(self):
        for tile in self.TILES:
            tile.draw()

        pygame.draw.rect(self.screen, (255, 50, 50), (self.start_pos[0] * TILESIZE, self.start_pos[1] * TILESIZE, TILESIZE-1, TILESIZE-1))
        pygame.draw.rect(self.screen, (50, 50, 255), (self.end_pos[0] * TILESIZE, self.end_pos[1] * TILESIZE, TILESIZE-1, TILESIZE-1))

    def next_node(self, startX, startY):
        self.nodes.clear()

        for i in range(3):
            for j in range(3):
                x = (startX - 1) + j
                y = (startY - 1) + i
                
                if (j,i) != (1,1) and (x*TILESIZE,y*TILESIZE) not in BOUNDARIES:
                    self.nodes.append(Node(x, y, self.start_pos, self.end_pos))

                if (x,y) == self.end_pos:
                    return

        self.nodes[0].get_values()
        LOWEST_TOTAL_DIST = self.nodes[0].TOTAL_DIST
        for node in self.nodes:
            node.get_values()

            if node.TOTAL_DIST < LOWEST_TOTAL_DIST:
                LOWEST_TOTAL_DIST = node.TOTAL_DIST

        LOWEST_DISTS = []
        for node in self.nodes:
            if node.TOTAL_DIST == LOWEST_TOTAL_DIST:
                LOWEST_DISTS.append(node)

        if len(LOWEST_DISTS) > 1:
            LOWEST_END_DIST = LOWEST_DISTS[0].END_DIST
            for node in LOWEST_DISTS:
                if node.END_DIST < LOWEST_END_DIST:
                    LOWEST_END_DIST = node.END_DIST
        
            LOWEST_DISTS.clear()
            for node in self.nodes:
                if node.END_DIST == LOWEST_END_DIST:
                    self.TILES.append(node)
                    self.next_node(node.x, node.y)
        else:
            self.TILES.append(LOWEST_DISTS[0])
            self.next_node(LOWEST_DISTS[0].x, LOWEST_DISTS[0].y) 
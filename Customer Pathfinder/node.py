import pygame
from settings import *

class Node:
    def __init__(self, x, y, start_pos, end_pos):
        self.x = x
        self.y = y

        self.start_pos = start_pos
        self.end_pos = end_pos

        self.G = 0
        self.F = 0
        self.H = 0

        self.LOWEST_INDEX = False

        self.screen = pygame.display.get_surface()

    def draw(self):
        pygame.draw.rect(self.screen, (250, 250, 250), (self.x * TILESIZE, self.y * TILESIZE, TILESIZE, TILESIZE))
        pygame.draw.rect(self.screen, (255, 50, 50), (self.start_pos[0] * TILESIZE, self.start_pos[1] * TILESIZE, TILESIZE, TILESIZE))
        pygame.draw.rect(self.screen, (50, 50, 255), (self.end_pos[0] * TILESIZE, self.end_pos[1] * TILESIZE, TILESIZE, TILESIZE))

    def calculate_weights(self):
        self.G = abs(self.x - self.start_pos[0]) + abs(self.y - self.start_pos[1])
        self.F = abs(self.x - self.end_pos[0]) + abs(self.y - self.end_pos[1])  
        self.H = self.G + self.F

    def Get_New_Nodes(self):
        self.LOWEST_INDEX = False

        Nodes = []

        for i in range(3):
            for j in range(3):
                Nodes.append(Node((self.x - 1 + j), (self.y - 1 + i), self.start_pos, self.end_pos))

        LOWEST_H = Nodes[0].H
        LOWEST_INDEX = 0
        for index, node in enumerate(Nodes):
            node.calculate_weights()    

            if node.H < LOWEST_H:
                LOWEST_H = node.H
                LOWEST_INDEX = index

        LOWEST_F = Nodes[LOWEST_INDEX].F
        for node in Nodes:
            if node.H == LOWEST_H:
                if node.F < LOWEST_F:
                    LOWEST_F = node.F
                    LOWEST_INDEX = index

        Nodes[LOWEST_INDEX].LOWEST_INDEX = True

        if Nodes[LOWEST_INDEX].LOWEST_INDEX != (Nodes[LOWEST_INDEX].x, Nodes[LOWEST_INDEX].y) != Nodes[LOWEST_INDEX].end_pos:
            Nodes[LOWEST_INDEX].draw()
            #Nodes[LOWEST_INDEX].Get_New_Nodes()
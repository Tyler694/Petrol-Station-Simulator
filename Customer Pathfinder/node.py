import pygame
from settings import *

class Node:

    def __init__(self, x, y, startPos, endPos):
        self.x = x
        self.y = y

        self.startPos = startPos
        self.endPos = endPos

        self.G = 0
        self.F = 0
        self.H = self.G + self.F
        
        self.screen = pygame.display.get_surface()

    def draw(self):
        pygame.draw.rect(self.screen, (250, 250, 250), (self.x * TILESIZE, self.y * TILESIZE, TILESIZE-1, TILESIZE-1))

    def calculate_weight(self):
        self.F = abs(self.x - self.startPos[0]) + abs(self.y - self.startPos[1])
        self.G = abs(self.x - self.endPos[0]) + abs(self.y - self.endPos[1])
        self.H = self.G + self.F

        for boundary in BOUNDARIES:
            if (self.x * TILESIZE, self.y * TILESIZE) == boundary:
                self.H += 50
        print(self.H)

        
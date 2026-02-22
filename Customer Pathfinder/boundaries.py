import pygame
from settings import *

class BoundariesClass():
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.boundaryPositions = []

        for i in range(90):
            for j in range(160):
                if BOUNDARIES[(i*160)+j] == 1:
                    self.boundaryPositions.append((j*TILESIZE, i*TILESIZE))

    def drawBoundaries(self):
        #LEVEL COLLISIONS
        for boundary in self.boundaryPositions:
            pygame.draw.rect(self.screen, (255,0,0), (boundary[0], boundary[1], TILESIZE, TILESIZE))

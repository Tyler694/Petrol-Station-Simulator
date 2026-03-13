import pygame
from settings import *

class BoundariesClass():
    def __init__(self):
        self.screen = pygame.display.get_surface()

    def drawBoundaries(self):
        for i in range(HEIGHT // TILESIZE):
            for j in range(WIDTH // TILESIZE):
                pygame.draw.rect(self.screen, (50, 50, 50), (j*TILESIZE, i*TILESIZE, TILESIZE-1, TILESIZE-1))

        #LEVEL COLLISIONS
        for boundary in BOUNDARIES:
            pygame.draw.rect(self.screen, (255,0,0), (boundary[0], boundary[1], TILESIZE-1, TILESIZE-1))


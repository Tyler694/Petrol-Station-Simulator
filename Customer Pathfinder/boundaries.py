import pygame
from settings import *

class BoundariesClass():
    def __init__(self):
        self.screen = pygame.display.get_surface()

    def drawBoundaries(self):
        #LEVEL COLLISIONS
        for boundary in BOUNDARIES:
            pygame.draw.rect(self.screen, (255,0,0), (boundary[0], boundary[1], TILESIZE, TILESIZE))

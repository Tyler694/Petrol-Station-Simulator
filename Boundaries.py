import pygame
from settings import *

class Boundary:

    def __init__(self,x,y):
        self.screen = pygame.display.get_surface()
        self.TILESIZE = 10
        self.x = x
        self.y = y

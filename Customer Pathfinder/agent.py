import pygame
from settings import *

class Agent:

    def __init__(self):
        self.x = 3
        self.y = 4

        self.dx = 20
        self.dy = 4

        self.screen = pygame.display.get_surface()

    def draw(self):
        pygame.draw.rect(self.screen, (255,50,50), (self.x * TILESIZE, self.y * TILESIZE, TILESIZE-1, TILESIZE-1))
        pygame.draw.rect(self.screen, (50,50,255), (self.dx * TILESIZE, self.dy * TILESIZE, TILESIZE-1, TILESIZE-1))
        
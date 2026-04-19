import pygame
from settings import *

class Player():
    def __init__(self):
        #PLAYER INITIALISATION
        self.screen = pygame.display.get_surface()
        self.px, self.py = 800, 750
        self.speed = 5
        self.playerTileSize = 20
        self.boundaryTileSize = 10
    
    def draw(self):
        #PLAYER DRAWING
        pygame.draw.rect(self.screen, (255,0,0), (self.px,self.py,self.playerTileSize,self.playerTileSize))

    def move(self, boundaries):
        keys = pygame.key.get_pressed()
        vx,vy = 0,0
        #WASD MOVEMNT
        if keys[pygame.K_w]:
            vy += -1
        if keys[pygame.K_s]:
            vy += 1
        if keys[pygame.K_a]:
            vx += -1
        if keys[pygame.K_d]:
            vx += 1
        
        #COLLISIONS
        for boundary in BOUNDARIES:
            if (((self.px + self.playerTileSize) + (vx * self.speed)) > boundary[0]
                 and ((self.px) + (vx * self.speed)) < (boundary[0])+self.boundaryTileSize
                   and ((self.py + self.playerTileSize) + (vy * self.speed)) > boundary[1]
                     and ((self.py) + (vy * self.speed)) < (boundary[1])+self.boundaryTileSize):
                self.speed = 0

        self.py += vy * self.speed
        self.px += vx * self.speed

        self.speed = 5

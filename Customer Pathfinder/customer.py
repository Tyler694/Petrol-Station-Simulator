import pygame
from settings import *

class Customer:

    def __init__(self):
        self.x = 100
        self.y = 200
        self.screen = pygame.display.get_surface()

        self.destinationX = 1000
        self.destinationY = 800

        self.speedX = 0
        self.speedY = 0

        self.boundaryPositions = []

        self.set_speed()

    def draw(self):
        pygame.draw.rect(self.screen, (255,0,0), (self.x, self.y, TILESIZE, TILESIZE))

    def set_speed(self):
        if self.y < self.destinationY:
            self.speedY = 5
        elif self.y > self.destinationY:
            self.speedY = -5
        else:
            self.speedY = 0

        if self.x < self.destinationX:
            self.speedX = 5
        elif self.x > self.destinationX:
            self.speedX = -5
        else:
            self.speedX = 0

    def findDestinationPositionY(self):
        if self.y != self.destinationY:
            for boundary in self.boundaryPositions:
                if self.x == boundary[0] and self.y + TILESIZE == boundary[1]:
                    self.x += TILESIZE
                    print("Working")
                    if self.x > WIDTH:
                        self.speedX *= -1
                    elif self.x < 0:
                        self.speedX *= -1
                    break
            self.y += self.speedY

    def findDestinationPosition(self):
        if self.x != self.destinationX:
            for boundary in self.boundaryPositions:
                if self.x + TILESIZE == boundary[0] and self.y == boundary[1]:
                    self.y += TILESIZE
                    return
            self.x += self.speedX
        else:
            self.findDestinationPositionY()
    
        
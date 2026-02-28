import pygame
from settings import *

class Customer:

    def __init__(self):
        self.x = 100
        self.y = 200
        self.screen = pygame.display.get_surface()

        self.destinationX = 1000
        self.destinationY = 800

        self.hitBoundary = False

        self.speedX = 0
        self.speedY = 0

        self.boundaryPositions = []
        self.checkpoints = []

        self.set_speedX()
        self.set_speedY()

    def draw(self):
        pygame.draw.rect(self.screen, (255,0,0), (self.x, self.y, TILESIZE, TILESIZE))

    def set_speedX(self):
        if self.x > self.destinationX:
            self.speedX = -TILESIZE
        elif self.x < self.destinationX:
            self.speedX = TILESIZE

        if self.x > WIDTH:
            self.speedX = -TILESIZE
        elif self.x < 0:
            self.speedX = TILESIZE

    def set_speedY(self):
        if self.y > self.destinationY:
            self.speedY = -TILESIZE
        elif self.y < self.destinationY:
            self.speedY = TILESIZE

        if self.y > HEIGHT:
            self.speedY = -TILESIZE
        elif self.y < 0:
            self.speedY = TILESIZE


    def next_x_pos(self):
        boundaryFound = False

        if self.x != self.destinationX:
            for boundary in self.boundaryPositions:
                if (self.x + self.speedX, self.y) == boundary:
                    boundaryFound = True
            if boundaryFound:
                self.y += self.speedY
            else:
                self.x += self.speedX
        else:
            self.next_y_pos()

    def next_y_pos(self):
        boundaryFound = False

        if self.y != self.destinationY:
            for boundary in self.boundaryPositions:
                if (self.x, self.y + self.speedY) == boundary:
                    boundaryFound = True
            if boundaryFound:
                self.x += self.speedX
                print("Working")
                if self.x > WIDTH:
                    self.set_speedX()
            else:
                self.y += self.speedY
        else:
            self.next_x_pos()

        

        
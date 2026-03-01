import pygame
from settings import *

class Customer:

    def __init__(self):
        self.x, self.y = (190, 100)

        self.screen = pygame.display.get_surface()

        self.destinationX, self.destinationY = (1020, 200)

        self.ReachedX = False
        self.ReachedY = False

        self.speedX = TILESIZE
        self.speedY = TILESIZE

        self.set_speedX()
        self.set_speedY()

        self.checkpoints = []


    def draw(self):
        pygame.draw.rect(self.screen, (50,50,255), (self.destinationX, self.destinationY, TILESIZE, TILESIZE))
        pygame.draw.rect(self.screen, (255,0,0), (self.x, self.y, TILESIZE, TILESIZE))

    def pathfind(self):
        if self.ReachedX:
            self.next_y_pos()
        else:
            self.next_x_pos()
        
        if self.ReachedX and self.ReachedY:
            self.drawRoute()

    def set_speedX(self):
        if self.x > self.destinationX:
            self.speedX = -TILESIZE
        else:
            self.speedX = TILESIZE

    def set_speedY(self):
        if self.y > self.destinationY:
            self.speedY = -TILESIZE
        else:
            self.speedY = TILESIZE

    def next_x_pos(self):
        while self.x != self.destinationX:
            for boundary in BOUNDARIES:
                if self.x + self.speedX == boundary[0] and self.y == boundary[1]:
                    self.find_x_gap()
                self.checkpoints.append((self.x, self.y))
            self.x += self.speedX

        self.ReachedX = True

        if self.y != self.destinationY:
            self.ReachedY = False
            self.set_speedY()

    def find_x_gap(self):
        if self.y + self.speedY >= HEIGHT:
            self.speedY = -TILESIZE
        if self.y + self.speedY <= 0:
            self.speedY = TILESIZE

        self.checkpoints.append((self.x, self.y))
        self.y += self.speedY

    def next_y_pos(self):
        while self.y != self.destinationY:
            for boundary in BOUNDARIES:
                while self.x == boundary[0] and self.y + self.speedY == boundary[1]:
                    self.find_y_gap()
            self.checkpoints.append((self.x, self.y))
            self.y += self.speedY

        self.ReachedY = True

        if self.x != self.destinationX:
            self.ReachedX = False
            self.set_speedX()

    def find_y_gap(self):
        if self.x + self.speedX >= WIDTH:
            self.speedX = -TILESIZE
        if self.x + self.speedX <= 0:
            self.speedX = TILESIZE
    
        self.checkpoints.append((self.x, self.y))
        self.x += self.speedX

    def drawRoute(self):
        for tile in self.checkpoints:
            pygame.draw.rect(self.screen, (50,255,50), (tile[0],tile[1],TILESIZE-1, TILESIZE-1))



        

        
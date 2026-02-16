import pygame
from player import *
from settings import *
from assets import *
from Boundaries import *

class Game:
    def __init__(self):
        #SETUP INITIALISATION
        pygame.display.set_caption("Petrol Station Simulator - TSNF")
        self.screen = pygame.display.set_mode(RES)
        self.clock = pygame.time.Clock()
        self.running = True
        #PLAYER SETUP
        self.player = Player()
        #PETROLSTATION SETUP
        self.station = pygame.image.load(PETROLSTATION)
        self.boundaries = [] #COLLISIONS

    def playerInit(self):
        self.player.draw()
        self.player.move(self.boundaries)

    def LevelBoundaries(self):
        for i in range(90):
            for j in range(160):
                if BOUNDARIES[(i*160)+j] == 14401:
                    self.boundaries.append(Boundary(j,i))

    def run(self):
        #SETUP DISPLAY
        while self.running == True:
            self.screen.blit(self.station, (0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            #LEVEL COLLISIONS
            self.LevelBoundaries()
            #PLAYER MOVEMENT AND DRAWING
            self.playerInit()

            self.boundaries.clear()
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    game = Game()
    game.run()
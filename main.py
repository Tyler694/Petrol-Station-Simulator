import pygame
from player import *
from settings import *
from assets import *
from customer import *
from business import *

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

        self.business = Business()
        #CUSTOMERS
        self.customers = [Customer(1)]

    def playerInit(self):
        #DRAWS PLAYER AND IF NO GUI IS OPEN IT MOVES THE PLAYER
        self.player.draw()
        self.player.move(self.boundaries)

    def customerInit(self):
        for customer in self.customers:
            customer.drawCustomer()


    def run(self):
        #SETUP DISPLAY
        while self.running == True:
            self.screen.blit(self.station, (0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            #PLAYER MOVEMENT AND DRAWING
            self.playerInit()

            self.customerInit()

            self.boundaries.clear()
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    game = Game()
    game.run()
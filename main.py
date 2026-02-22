import pygame
from player import *
from settings import *
from assets import *
from Boundaries import *
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
        #CUSTOMER
        self.customerWaitTime = 5

        self.business = Business()
        
        self.customers = []

    def playerInit(self):
        #DRAWS PLAYER AND IF NO GUI IS OPEN IT MOVES THE PLAYER
        self.player.draw()
        for customer in self.customers:
            if customer.GUIOpen == False:
                self.player.move(self.boundaries)

    def LevelBoundaries(self):
        #LEVEL COLLISIONS
        for i in range(90):
            for j in range(160):
                if BOUNDARIES[(i*160)+j] == 1:
                    self.boundaries.append(Boundary(j,i))

    def customerLogic(self):
        #IF THERES NO CUSTOMER AND THERE HAS BEEN A DELAY IT CREATES A NEW CUSTOMER
        if self.SpawnTimer():
            if self.business.pumpsInUse != [True,True,True,True]:
                self.customers.append(Customer(self.clock, self.business.choosePump()))
                self.newCustomer(self.customers[0])
        else:
            for customer in self.customers:
                customer.drawCustomer()
                customer.pay(self.player.px,self.player.py)

    def newCustomer(self, customer):
        #CREATES A NEW CUSTOMER
        self.business.money += customer.total
        customer.paid = False

    def SpawnTimer(self):
        #CUSTOMER SPAWN DELAY
        self.customerWaitTime -= self.clock.get_time() / 1000

        if self.customerWaitTime < 0:
            self.customerWaitTime = 5
            return True


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

            #CUSTOMER LOGIC
            self.customerLogic()

            self.boundaries.clear()
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    game = Game()
    game.run()
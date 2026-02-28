import pygame
from settings import *
from customer import *
from boundaries import *

screen = pygame.display.set_mode(RES)
clock = pygame.time.Clock()
running = True

customer = Customer()
boundaries = BoundariesClass()

while running:
    screen.fill((50,50,50))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    boundaries.drawBoundaries()

    customer.boundaryPositions = boundaries.boundaryPositions

    customer.draw()
    customer.next_x_pos()
    
    clock.tick(60)
    pygame.display.flip()
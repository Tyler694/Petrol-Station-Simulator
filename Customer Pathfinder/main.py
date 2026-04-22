import pygame
from settings import *
from boundaries import *
from pathfind import *

screen = pygame.display.set_mode(RES)
clock = pygame.time.Clock()
running = True

pygame.display.set_caption("Pathfinding Algorithm - Tyler694")

boundaries = BoundariesClass()
pathfind = Pathfind((5,5), (64, 59))
pathfind.createPath()

while running:
    screen.fill((10,10,10))

    boundaries.drawBoundaries()
    pathfind.drawPath()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(60)
    pygame.display.flip()
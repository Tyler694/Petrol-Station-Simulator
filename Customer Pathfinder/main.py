import pygame
from settings import *
from boundaries import *
from pathfind import *

screen = pygame.display.set_mode(RES)
clock = pygame.time.Clock()
running = True

pygame.display.set_caption("Pathfinding Algorithm - Tyler694")

boundaries = BoundariesClass()
#pathfind = Pathfind((3, 25), (107, 47))
#pathfind = Pathfind((20, 31), (117, 31))
pathfind = Pathfind((6, 4), (66, 82))

while running:
    screen.fill((10,10,10))

    pathfind.createPath()

    boundaries.drawBoundaries()
    pathfind.drawPath()

    pathfind.reconstruct_path()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(165)
    pygame.display.flip()
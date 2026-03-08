import pygame
from settings import *
from boundaries import *
from pathfind import *
from agent import *

screen = pygame.display.set_mode(RES)
clock = pygame.time.Clock()
running = True

pygame.display.set_caption("Pathfinding Algorithm - Tyler694")

boundaries = BoundariesClass()
agent = Agent()

pathfind = Pathfind(agent)

while running:
    screen.fill((10,10,10))

    boundaries.drawBoundaries()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pathfind.draw()
    agent.draw()

    clock.tick(60)
    pygame.display.flip()
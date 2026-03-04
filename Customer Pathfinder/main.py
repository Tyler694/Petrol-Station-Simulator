import pygame
from settings import *
from boundaries import *
from node import *

screen = pygame.display.set_mode(RES)
clock = pygame.time.Clock()
running = True

pygame.display.set_caption("Pathfinding Algorithm - Tyler694")

boundaries = BoundariesClass()

nodes = []

for i in range(3):
    for j in range(3):
        nodes.append(Node((9 + j), (2 + i), (10,3), (5,5)))

while running:
    screen.fill((10,10,10))

    boundaries.drawBoundaries()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    LOWEST_H = nodes[0].H
    LOWEST_INDEX = 0
    for index, node in enumerate(nodes):
        node.calculate_weights()    

        if node.H < LOWEST_H:
            LOWEST_H = node.H
            LOWEST_INDEX = index

    LOWEST_F = nodes[LOWEST_INDEX].F
    for node in nodes:
        if node.H == LOWEST_H:
            if node.F < LOWEST_F:
                LOWEST_F = node.F
                LOWEST_INDEX = index

    nodes[LOWEST_INDEX].LOWEST_INDEX = True

    if nodes[LOWEST_INDEX].LOWEST_INDEX and (nodes[LOWEST_INDEX].x, nodes[LOWEST_INDEX].y) != nodes[LOWEST_INDEX].end_pos:
        nodes[LOWEST_INDEX].draw()
        #nodes[LOWEST_INDEX].Get_New_Nodes()


    

    clock.tick(60)
    pygame.display.flip()
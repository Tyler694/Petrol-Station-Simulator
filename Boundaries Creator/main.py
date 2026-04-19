import pygame
import pyperclip
from settings import *

screen = pygame.display.set_mode((RES))
pygame.display.set_caption("Boundaries Creator - Tyler694")
running = True

bg = pygame.image.load(BG)

mouseX = 0
mouseY = 0

index = 0

tiles = []

def findTile():
    mouse_pos = pygame.mouse.get_pos()

    mouseX = (mouse_pos[0] // TILESIZE) * TILESIZE
    mouseY = (mouse_pos[1] // TILESIZE) * TILESIZE

    pygame.draw.rect(screen, (255,255,255), (mouseX, mouseY, TILESIZE, TILESIZE))

    return mouseX, mouseY

def drawTile(mouseX, mouseY):
    mouse = pygame.mouse.get_pressed()
    mouse = mouse[0]
    if mouse:
        if len(tiles) == 0:
            tiles.append((mouseX, mouseY))
        elif tiles[len(tiles)-1] != (mouseX, mouseY):
            tiles.append((mouseX, mouseY))

def removeTile(mouseX,mouseY):
    mouse = pygame.mouse.get_pressed()
    mouse = mouse[2]
    if mouse:
        for tile in tiles:
            if tile == (mouseX, mouseY):
                tiles.remove(tile)



    

def drawMap():

    for tile in tiles:
        if tile != 0:
            pygame.draw.rect(screen, (255,0,0), (tile[0], tile[1], TILESIZE, TILESIZE))

while running:
    screen.blit(bg, (0,0))

    mouseX, mouseY = findTile()
    
    drawMap()
    drawTile(mouseX,mouseY)
    removeTile(mouseX, mouseY)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pyperclip.copy(tiles)
            print(tiles) 
            running = False

    pygame.display.flip()
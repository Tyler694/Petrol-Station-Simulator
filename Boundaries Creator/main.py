import pygame
from settings import *

screen = pygame.display.set_mode((RES))
running = True

bg = pygame.image.load(BG)

mouseX = 0
mouseY = 0

index = 0

tiles = []

def createMapArray():
    for i in range((HEIGHT//10)):
        for j in range((WIDTH//10)):
            tiles.append(0)

def findTile():
    mouse_pos = pygame.mouse.get_pos()

    mouseX = (mouse_pos[0] // 10) * 10
    mouseY = (mouse_pos[1] // 10) * 10

    pygame.draw.rect(screen, (255,255,255), (mouseX, mouseY, TILESIZE, TILESIZE))

    return mouseX, mouseY

def drawTile(mouseX, mouseY):
    mouse_pressed = pygame.mouse.get_pressed()
    mouse_left_pressed = mouse_pressed[2]
    mouse_right_pressed = mouse_pressed[0]

    index = ((mouseY * (WIDTH // 10)) + mouseX) // 10

    if mouse_right_pressed:
        tiles[index] = (mouseX,mouseY)
    if mouse_left_pressed:
        tiles[index] = 0
    

def drawMap():
    for tile in tiles:
        if tile != 0:
            pygame.draw.rect(screen, (255,0,0), (tile[0], tile[1], TILESIZE, TILESIZE))


createMapArray()

while running:
    screen.blit(bg, (0,0))

    mouseX, mouseY = findTile()
    drawTile(mouseX, mouseY)
    
    drawMap()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            for index, tile in enumerate(tiles):
                if tile != 0:
                    tiles[index] = 1
            print(tiles) 
            running = False

    pygame.display.flip()
import pygame
from settings import *

class Node:

    def __init__(self, x, y, start_pos, end_pos):
        self.x = x
        self.y = y

        self.start_pos = start_pos
        self.end_pos = end_pos

        self.PLAYER_DIST = 0
        self.END_DIST = 0
        self.TOTAL_DIST = 0

        self.screen = pygame.display.get_surface()

    def draw(self):
        pygame.draw.rect(self.screen, (200, 200, 200), (self.x * TILESIZE, self.y * TILESIZE, TILESIZE-1, TILESIZE-1))

    def get_values(self):
        self.PLAYER_DIST = (abs(self.x - self.start_pos[0]) + abs(self.y - self.start_pos[1])) * 10
        self.END_DIST = (abs(self.x - self.end_pos[0]) + abs(self.y - self.end_pos[1])) * 10

        self.TOTAL_DIST = self.PLAYER_DIST + self.END_DIST

        if self.PLAYER_DIST == 20:
            self.PLAYER_DIST = 14
import pygame

class Player():
    def __init__(self):
        #PLAYER INITIALISATION
        self.screen = pygame.display.get_surface()
        self.px, self.py = 300, 100
        self.speed = 2
    
    def draw(self):
        #PLAYER DRAWING
        pygame.draw.rect(self.screen, (255,0,0), (self.px,self.py,20,20))

    def move(self, boundaries):
        keys = pygame.key.get_pressed()
        vx,vy = 0,0
        #WASD MOVEMNT
        if keys[pygame.K_w]:
            vy += -1
        if keys[pygame.K_s]:
            vy += 1
        if keys[pygame.K_a]:
            vx += -1
        if keys[pygame.K_d]:
            vx += 1
        
        for boundary in boundaries:
            if (((self.px + 20) + (vx * self.speed)) > boundary.x*10 and ((self.px) + (vx * self.speed)) < (boundary.x*10)+10 and ((self.py + 20) + (vy * self.speed)) > boundary.y*10 and ((self.py) + (vy * self.speed)) < (boundary.y*10)+10):
                self.speed = 0
        print(vx * self.speed)
        self.py += vy * self.speed
        self.px += vx * self.speed

        self.speed = 2

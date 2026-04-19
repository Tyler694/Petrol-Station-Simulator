import pygame
import random
from assets import *
from pathfind import *

class Customer:

    def __init__(self, pump):
        self.screen = pygame.display.get_surface()

        #CUSTOMER ITEMS
        self.items = []
        self.total = 0
        self.PETROLPRICE = random.randint(10,50)

        #CUSTOMER LOGIC
        #self.x,self.y = 690,640
        self.x,self.y = 100,100
        self.paid = False

        #CHECKOUT GUI
        self.GUIOpen = False
        self.checkoutGUI = pygame.image.load(CHECKOUTGUI)

        #ITEM IMAGES
        self.crisps = pygame.image.load(CRISPS)
        self.water = pygame.image.load(WATER)
        self.coffee = pygame.image.load(COFFEE)
        self.gum = pygame.image.load(GUM)
        self.chocolate = pygame.image.load(CHOCOLATE)
        self.sweets = pygame.image.load(SWEETS)
        self.money = pygame.image.load(MONEY)
        self.car = pygame.image.load(CAR)

        self.pump = pump

        #PUMP NUMBER TEXT

        self.PETROLPRICETEXT = "PETROL PRICE:"
        self.NUMBER_PRESSED = ""

        pygame.font.init()
        self.pumpNumberTextFont = pygame.font.Font("Assets\FONTS\Roboto-VariableFont_wdth,wght.ttf", 15)
        self.pumpNumberText = self.pumpNumberTextFont.render(f"£{self.PETROLPRICE} on pump {self.pump} please", True, (0,0,0))
        self.pumpNumberTextRect = self.pumpNumberText.get_rect()
        self.pumpNumberTextRect.move_ip(477,455)

        self.pumpNumberSelectedFont = pygame.font.Font("Assets\FONTS\Roboto-VariableFont_wdth,wght.ttf", 30)
        self.pumpNumberSelectedText = self.pumpNumberSelectedFont.render(f"{self.PETROLPRICETEXT} {str(self.NUMBER_PRESSED)}", True, (0,0,0))
        self.pumpNumberSelectedTextRect = self.pumpNumberSelectedText.get_rect()
        self.pumpNumberSelectedTextRect.move_ip(496, 511)

        self.TOTALTEXT = "Total: "
        self.totalTextFont = pygame.font.Font("Assets\FONTS\Roboto-VariableFont_wdth,wght.ttf", 50)
        self.totalText_TEXT = self.pumpNumberSelectedFont.render(f"{self.TOTALTEXT} {str(self.total)}", True, (0,0,0))
        self.totalTextRect = self.totalText_TEXT.get_rect()
        
        #KEYPAD VARIABLES
        self.clicking = False
        self.FINISHED = False
        self.clicked = False
        self.OverCharging = False
        self.petrolPaid = False

        self.closeDelay = 3

        self.Cx,self.Cy = 350, -300
        self.Tx, self.Ty = 957, 151
        
        #CUSTOMER ARRIVAL ANIMATION
        self.FinishedKeyFrame1 = False
        self.FinishedKeyFrame2 = True
        self.FinishedKeyFrame3 = True

        self.CustomerArrivalAnimation = []
        self.FirstFrame = True
        
        self.chooseItems()

        pathfind = Pathfind((self.x // TILESIZE, self.y // TILESIZE), (690//TILESIZE,640//TILESIZE))
        
    def chooseItems(self):
        #Chooses a random number, this is the number of items the customer will have.
        #Choose a random item, this will be the item the customer will have.
        #Puts the items into a list.
        itemCount = random.randint(0, 5)
        for i in range(itemCount):
            index = random.randint(0,len(ITEMS)-1)
            self.items.append(ITEMS[index])

        #Calculate Total
        for item in self.items:
            self.total += item[1]

    def drawCustomer(self):
        pygame.draw.rect(self.screen, (255,0,0), (self.x, self.y,20,20))
    
    def payGUI(self):
        #BLITING GUI
        self.screen.blit(self.checkoutGUI, (0,0))
        self.screen.blit(self.pumpNumberText, self.pumpNumberTextRect)
        
        if self.petrolPaid == False:
            self.keypad()
        else:
            pygame.draw.rect(self.screen, (91, 167, 255), (463, 483, 299, 293))
            #IF OVERCHARGED THE CUSTOMER YOU DONT GET PAID AND A SHORT DELAY BEFORE CLOSING THE GUI
            if self.OverCharging:
                self.paid = True
                self.GUIOpen = False
                self.petrolPaid = False
                self.FINISHED = False
            #PUTS A MONEY IMAGE ON THE SCREEN
            if self.OverCharging == False:
                self.screen.blit(self.money, (563, 551))
                #CHECKS TO SEE IF YOU ARE CLICKING ON THE MONEY
                if pygame.mouse.get_pressed() == (1,0,0):
                    self.clicking = True

                mouse_pos = pygame.mouse.get_pos()
                if self.clicking and pygame.mouse.get_pressed() == (0,0,0) and mouse_pos[0] > 563 and mouse_pos[0] < 563 + 115 and mouse_pos[1] > 551 and mouse_pos[1] < 551 + 193:
                    self.paid = True
                    self.GUIOpen = False
                    self.petrolPaid = False
                    self.FINISHED = False
        #WHERE THE TOTAL AND ITEMS ARE POSITIONED ON SCREEN
        self.totalText()
        self.Tx += 30
        self.Ty -= 10
        #BLITING ITEMS
        for item in self.items:
            if item[0] == "Chocolate Bar":
                self.screen.blit(self.chocolate, (self.Tx,self.Ty-22))
                self.Ty -= 32
            if item[0] == "Gum":
                self.screen.blit(self.gum, (self.Tx,self.Ty-23))
                self.Ty -= 33
            if item[0] == "Water":
                self.screen.blit(self.water, (self.Tx,self.Ty-93))
                self.Ty -= 103
            if item[0] == "Crisps":
                self.screen.blit(self.crisps, (self.Tx,self.Ty-120))
                self.Ty -= 130
            if item[0] == "Coffee":
                self.screen.blit(self.coffee, (self.Tx,self.Ty-123))
                self.Ty -= 133
            if item[0] == "Sweets":
                self.screen.blit(self.sweets, (self.Tx,self.Ty-111))
                self.Ty -= 121

    #THE BLACK BAR AND THE TEXT ON THE ITEMS SIDE OF THE GUI
    def totalText(self):     
        self.Tx,self.Ty = 917, 700
        pygame.draw.rect(self.screen, (0,0,0), (self.Tx, self.Ty, 341, 19))

        self.totalTextRect.x = self.Tx + 20
        self.totalTextRect.y = self.Ty + 40

        self.totalText_TEXT = self.pumpNumberSelectedFont.render(f"{self.TOTALTEXT} £{str(self.total)}", True, (0,0,0))
        self.screen.blit(self.totalText_TEXT,self.totalTextRect)

    #KEYPAD LOGIC
    def keypad(self):
        mouse_pos = pygame.mouse.get_pos()

        numLength = 2
        #BUTTON LOGIC
        if pygame.mouse.get_pressed() == (1,0,0):
            self.clicking = True

        for i in range(4):
            for j in range(3):
                if mouse_pos[0] > 535 + (55 * j) and mouse_pos[0] < (535 + 50) + (55 * j) and mouse_pos[1] > 554 + (55 * i) and mouse_pos[1] < 603 + (55 * i):

                    pygame.draw.rect(self.screen, (80,80,80,), (535 + (55 * j), 554 + (55 * i), 50, 50))

                    BUTTON_NUMBER = (j+1)+(i*3)

                    if self.clicking and pygame.mouse.get_pressed() == (0,0,0):
                        #NUMBER BUTTONS
                        if  (BUTTON_NUMBER != 12) and (BUTTON_NUMBER != 10) and len(self.NUMBER_PRESSED) < numLength:
                            if BUTTON_NUMBER == 11:
                                self.NUMBER_PRESSED = self.NUMBER_PRESSED + "0"
                                self.clicking = False
                                self.pumpNumberSelectedText = self.pumpNumberSelectedFont.render(f"{self.PETROLPRICETEXT} {str(self.NUMBER_PRESSED)}", True, (0,0,0))
                                break

                            self.clicking = False
                            self.NUMBER_PRESSED = self.NUMBER_PRESSED + str(BUTTON_NUMBER)
                            self.pumpNumberSelectedText = self.pumpNumberSelectedFont.render(f"{self.PETROLPRICETEXT} {str(self.NUMBER_PRESSED)}", True, (0,0,0))

                        #X BUTTON
                        if  BUTTON_NUMBER == 10:
                            self.clicking = False
                            
                            self.NUMBER_PRESSED = ""
                            self.pumpNumberSelectedText = self.pumpNumberSelectedFont.render(f"{self.PETROLPRICETEXT} {str(self.NUMBER_PRESSED)}", True, (0,0,0))
                        #TICK BUTTON
                        if BUTTON_NUMBER == 12 and self.NUMBER_PRESSED != "" and len(self.NUMBER_PRESSED) == 2:
                            self.clicking = False

                            if int(self.NUMBER_PRESSED) > self.PETROLPRICE:
                                self.pumpNumberText = self.pumpNumberTextFont.render(f"Hey Your Overcharging me!", True, (0,0,0))
                                self.petrolPaid = True
                                self.OverCharging = True
                            else:
                                self.total += self.PETROLPRICE
                    
                            self.petrolPaid = True
                            
        self.screen.blit(self.pumpNumberSelectedText, self.pumpNumberSelectedTextRect)

    def pay(self,px,py):
        #PLAYER INTERACTION ZONE
        collisionBoundsX = 634
        collisionBoundsY = 720
        collisionBoundsLength = 136
        collisionBoundsWidth = 59

        if self.x == 690 and self.y == 640:
            pygame.draw.rect(self.screen, (255,0,0), (634, 720, 136,59))

            if ((px + 20) > collisionBoundsX and ((px)) < (collisionBoundsX)+collisionBoundsLength and ((py + 20)) > collisionBoundsY and ((py)) < (collisionBoundsY)+collisionBoundsWidth):
                keys = pygame.key.get_pressed()
                #E TO OPEN
                if keys[pygame.K_e]:
                    self.GUIOpen = True

                if self.GUIOpen:
                    self.payGUI()
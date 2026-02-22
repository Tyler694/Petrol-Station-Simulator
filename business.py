import random

class Business:
    #CONTROLS ALL THE DATA ABOUT THE BUSINESS
    def __init__(self):
        self.money = 0
        self.pumpsInUse = [False,False,False,False]

    def choosePump(self):
        pump = random.randint(1,4)
        if self.pumpsInUse[pump-1] == False:
            self.pumpsInUse[pump-1] = True
            return pump
        else:
            self.choosePump()
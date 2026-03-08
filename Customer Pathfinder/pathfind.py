from settings import *
from node import *

class Pathfind:

    def __init__(self, agent):
        self.agent = agent

        self.start_pos = (agent.x, agent.y)
        self.end_pos = (agent.dx, agent.dy)

        self.start_H = abs(agent.x - self.start_pos[0]) + abs(agent.y - self.start_pos[1]) + abs(agent.x - self.end_pos[0]) + abs(agent.y - self.end_pos[1])
        self.last_G = 0

        self.PERFECT_TILES = []

        self.i = 0

        self.first_tile()


    def first_tile(self):
        for i in range(3):
            for j in range(3):
                self.x = (self.agent.x - 1) + j
                self.y = (self.agent.y - 1) + i

                if (j,i) != (1,1):
                    NODE.append(Node(self.x, self.y, self.start_pos, self.end_pos))

        LOWEST_H = NODE[0].H
        for node in NODE:

            node.calculate_weight()

            if node.H < LOWEST_H:
                LOWEST_H = node.H
    
        for node in NODE:
            if node.H != LOWEST_H and node.H > self.start_H:
                NODE.remove(node)

        while len(NODE) != 1:
            LOWEST_G = NODE[0].G
            for node in NODE:
                if node.G < LOWEST_G:
                    LOWEST_G = node.G
        
            for node in NODE:
                if node.G != LOWEST_G:
                    NODE.remove(node)

        self.x = NODE[0].x
        self.y = NODE[0].y

        self.last_G = NODE[0].G

        self.PERFECT_TILES.append(NODE[0])
        self.next_tile(self.x, self.y)

    def next_tile(self, x, y):
        NODE.clear()

        for i in range(3):
            for j in range(3):
                self.x = (x - 1) + j
                self.y = (y - 1) + i

                if (j,i) != (1,1):
                    NODE.append(Node(self.x, self.y, self.start_pos, self.end_pos))
                    
                
            LOWEST_H = NODE[0].H
            for node in NODE:
                node.calculate_weight()

                if node.H < LOWEST_H :
                    LOWEST_H = node.H
        
            for node in NODE:
                if node.H != LOWEST_H:
                    NODE.remove(node)


        while len(NODE) != 1:
            LOWEST_G = NODE[0].G
            for node in NODE:
                if node.G < LOWEST_G and node.G < self.last_G:
                    LOWEST_G = node.G
        
            for node in NODE:
                if node.G != LOWEST_G:
                    NODE.remove(node)

        self.x = NODE[0].x
        self.y = NODE[0].y
        
        self.last_G = NODE[0].G

        if (self.x,self.y) != self.end_pos:
            self.i += 1
            self.PERFECT_TILES.append(NODE[0])
            self.next_tile(self.x, self.y)


                
                    

    def draw(self):
        for tile in self.PERFECT_TILES:
            tile.draw()
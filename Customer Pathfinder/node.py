class Node:

    def __init__(self, pos, start_pos, end_pos):
        self.DistToStart = 0
        self.DistToEnd = 0
        self.TotalDist = 0

        self.pos = pos
        self.start_pos = start_pos
        self.end_pos = end_pos

        self.calculateDists()

    def calculateDists(self):
        self.DistToStart = (abs(self.pos[0]-self.start_pos[0]) + abs(self.pos[1]-self.start_pos[1])) * 10
        self.DistToEnd = (abs(self.pos[0]-self.end_pos[0]) + abs(self.pos[1]-self.end_pos[1])) * 10

        if self.DistToStart == 20:
            self.DistToStart = 14

        self.TotalDist = self.DistToStart + self.DistToEnd
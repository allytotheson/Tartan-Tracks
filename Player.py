from constants import *

class Player:

    def __init__(self, name, track):
        self.gameName = name
        self.name = f"images/{name}.png"
        self.coinCount = 0
        self.distance = 0
        self.speed = 20
        self.track = track
        self.location = (200, TRACK_1_MIDDLE + TRACK_DIFFERENCE*self.track) 

        self.isJump = False
        self.jumpCount = 8

    def __repr__(self):
        return f"Player {self.name}"
    
    def __hash__(self):
        return str(self.name)
    
    def __eq__(self, other):
        return ((isinstance(other, Player)) and (self.name == other.name))

    def addCoins(self):
        self.coinCount += 1
    
    def addDistance(self):
        self.distance += speed
    
    def switchLanes(self, direction):
        if 0<= self.track + direction <= 2:
            self.track+=direction
            self.location = (200, TRACK_1_MIDDLE + TRACK_DIFFERENCE*self.track) 
        #animation for bouncing back
    def jump(self):
        if self.jumpCount >= -8:
            y = self.location[1]
            dy = (self.jumpCount * abs(self.jumpCount)) * 0.5
            self.location = (200, y - dy)
            self.jumpCount -= 1
        else:
            self.jumpCount = 8
            self.isJump = False
        
    
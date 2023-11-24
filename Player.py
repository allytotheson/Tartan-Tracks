from constants import *

class Player:
    def __init__(self, num, img):
        self.num = num
        self.img = img
        self.coinCount = 0
    
    def __repr__(self):
        return f"Player {self.num}"
    
    def __hash__(self):
        return str(self.num)
    
    def __eq__(self, other):
        return ((isinstance(other, Player)) and (self.num == other.num)
                 and (self.img == other.img))

    def addCoins(self):
        self.coinCount += 1
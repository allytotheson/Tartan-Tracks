from constants import *
import random
class Coin:
    def __init__(self, track, count):
        self.name = "images/coin.png"
        self.track = track
        self.count = count
        self.trackDy = TRACK_DIFFERENCE*track
        self.width = 100
        self.height = 87
        self.location = (WIDTH, TRACK_1_BOTTOM + self.trackDy - self.height - 30)
    

    def __repr__(self):
        return str(self.location)

    def __eq__(self, other):
        return (isinstance(other, Coin)
                and (self.location == other.location))
    def __hash__(self):
        return str(self)

    def updateLocation(self, speed):
        x, y = self.location
        self.location = (x-speed, y)
        return (self.location)
    
def isLegalCoin(curC, newC):
    for coin in curC:
        endX = coin.location[0] + coin.count*coin.width #current coin chains
        #end location

        if newC.location[0] <= endX and newC.track == coin.track:
            return False
    return True
            
def loadCoin(coinList):
    randomTrack = random.randrange(0,3) #thats weird
    randomCount = random.randrange(3,6)
    newCoins = Coin(randomTrack, randomCount)
    if isLegalCoin(coinList, newCoins):
        return newCoins
    else:
        return loadCoin(coinList)


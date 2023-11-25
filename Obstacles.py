import random
from constants import *
from cmu_graphics import *
from PIL import Image, ImageDraw

class Obstacle:
    def __init__(self, track):
        self.track = track #note that tracks go from 0-2 instead of 1-3

        self.trackDy = TRACK_DIFFERENCE*track
        middleOfTrackY = TRACK_1_MIDDLE + self.trackDy

        #this is for collisons
        #self.middleHeight = obstacleHeight + middleOfTrackY 

    def __repr__(self):
        return str(self.location)
    def __eq__(self, other):
        return ((isinstance(other, Obstacle)) and 
            (self.track == other.track))
    def __hash__(self):
        return hash(str(self))

    def updateLocation(self, speed):
        x, y = self.location
        self.location = (x-speed, y)
        return (self.location)
    



class Train(Obstacle):
    def __init__(self, track, color):
        super().__init__(track)
        self.length = 300
        self.height = 180
        self.color = color

        self.location = (WIDTH, TRACK_1_BOTTOM + self.trackDy - self.height)
        self.name = f"images/{self.color}Train.png"

class Fence(Obstacle):
    def __init__(self, track, fill):
        super().__init__(track)
        self.length = 60
        self.height = 200
        self.fill = fill

        self.location = (WIDTH, TRACK_1_BOTTOM + self.trackDy - self.height)
        self.name = f"images/{self.fill}Fence.png"

#maybe clean up by putting inside class
def isLegal(curO, newO):
    for obstacle in curO:
        if ((obstacle.location[0] + obstacle.length >= newO.location[0]) and
            (obstacle.track == newO.track)): #if any obstacle is off-screen
            #and the tracks are same, they overlap
            return False
        #if cannot switch lanes without dying
    
    return True

def loadObstacle(curObstacles):
    randomType = choice(OBSTACLES)
    randomTrack = randrange(0,3)
    randomCustomization = choice(CUSTOMIZATION[randomType])

    if randomType == "Train":
        newObstacle = Train(randomTrack, randomCustomization)
    elif randomType == "Fence":
        newObstacle = Fence(randomTrack, randomCustomization)
    #return newObstacle

    if isLegal(curObstacles, newObstacle):
        return newObstacle
    else:
        return loadObstacle(curObstacles)#is this okay

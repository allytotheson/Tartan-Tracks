import random
from constants import *

class Obstacle:
    obstacleSizes = {"train":(300,150), "solid fence": (20,100),
                     "hollow fence":(20,100)} #length, height

    def __init__(self, typeObstacle, track):
        self.typeObstacle = typeObstacle
        self.track = track #note that tracks go from 0-2 instead of 1-3

        obstacleLength = Obstacle.obstacleSizes[typeObstacle][0]
        obstacleHeight = Obstacle.obstacleSizes[typeObstacle][1]
        middleOfTrackY = TRACK_1_MIDDLE + TRACK_DIFFERENCE*track

        #these are for updating locations
        self.startLocation = (WIDTH, TRACK_1_BOTTOM + obstacleHeight)
        self.endLocation = (WIDTH+ obstacleLength,
                            TRACK_1_BOTTOM + obstacleHeight)
        #this is for collisons
        self.middleHeight = obstacleHeight + middleOfTrackY 

    def __repr__(self):
        return str(self.location)
    def __eq__(self, other):
        return ((isinstance(other, Obstacle)) and 
            (self.typeObstacle == other.typeObstacle) and 
            (self.track == other.track))
    def __hash__(self):
        return hash(str(self))



#note for future : when adding obstacles to list, add their locations in

def loadObstacle():
    possibleObstacles = ["train", "solid fence", "hollow fence"]
    randomTrack = random.randrange(0,3)

    newObstacle = Obstacle(randomTrack, random.choice(possibleObstacles))
    if isLegal(newObstacle):
        pass
        #return newObstacle
    else:
        loadObstacle() #is this okay


def isLegal():
    pass
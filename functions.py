from cmu_graphics import *
from PIL import Image, ImageDraw
from constants import * 
import random 

from Obstacles import Obstacle, Train, Fence
from Player import Player
import Obstacles as OBS

def loadImage(image):
    if isinstance(image, Train):
        train = Image.open(image.name)
        train = train.resize((train.size[0]//2, train.size[1]//2))
        return train
    if isinstance(image, Fence):
        fence = Image.open(image.name)
        fence = fence.resize((fence.size[0]//5,fence.size[1]//5))
        return fence
    if isinstance(image, Player):
        player = Image.open(image.name)
        player = player.resize((player.size[0]//5, player.size[1]//5))
        return player
    
def removeObstacles(obstacleList):
    new = obstacleList[:]

    for obstacle in obstacleList:
        if obstacle.location[0] >= 0:
            new.append(obstacle)
    return new
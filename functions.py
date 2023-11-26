from cmu_graphics import *
from PIL import Image, ImageDraw
from constants import * 
import random 

from Obstacle import Obstacle, Train, Fence
from Player import Player
from Coin import Coin
import Obstacle as OBS

def loadImage(image):
    if isinstance(image, Train):
        train = Image.open(image.name)
        #train = train.resize((train.size[0]//2, train.size[1]//2))
        return train
    if isinstance(image, Fence):
        fence = Image.open(image.name)
        fence = fence.resize((fence.size[0]//5,fence.size[1]//5))
        return fence
    if isinstance(image, Player):
        player = Image.open(image.name)
        player = player.resize((player.size[0]//2, player.size[1]//2))
        return player
    if isinstance(image, Coin):
        coin = Image.open(image.name)
        #coin = coin.resize((coin.size[0]*4, coin.size[1]*4))
        return coin

def removeObstacles(obstacleList):
    new = obstacleList[:]

    for obstacle in obstacleList:
        if obstacle.location[0] >= 0:
            new.append(obstacle)
    return new

def drawSpritesInOrder(l): #sorts obstacles into smaller lists
    #based on track
    trackList = [[] for i in range(3)] 
    for sprite in l:
        if sprite.location[0] + sprite.width < 0:
            continue
        else:
            trackList[sprite.track].append(sprite)
    
    return trackList

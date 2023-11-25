from cmu_graphics import *
from PIL import Image, ImageDraw
from constants import * 
import random 

from Obstacles import Obstacle, Train, Fence
from Player import Player
import Obstacles as OBS
import functions as func

def onAppStart(app):
    app.width = WIDTH
    app.height = HEIGHT
    app.stepCount = 0

    app.bg = Image.open(BACKGROUND)

    app.curObstacles = []
    app.nextObstacle = OBS.loadObstacle(app.curObstacles)

    app.players = [Player("pikachu", 1)] #will be chosen in start screen
    app.player1 = app.players[0]
    #app.player2 = app.players[1]

#--------------------#
#----START SCREEN----#
#--------------------#


#-------------------#
#----GAME SCREEN----#
#-------------------#

def game_redrawAll(app):
    drawImage(CMUImage(app.bg), 0,0)

    for obstacle in app.curObstacles:
        x, y = obstacle.location
        img = func.loadImage(obstacle)
        drawImage(CMUImage(img), x, y)
    
    for player in app.players:
        x, y = player.location
        img = func.loadImage(player)
        drawImage(CMUImage(img), x, y-50)

def game_onStep(app):
    app.stepsPerSecond = 10
    app.stepCount += 1
    #load piece
    if app.stepCount%15 == 0:
        app.nextObstacle = OBS.loadObstacle(app.curObstacles)
        app.curObstacles.append(app.nextObstacle)
    #delete gone objects
    
    #increase position of each piece on board
    for i in range(len(app.curObstacles)):
        app.curObstacles[i].updateLocation(20)
    
    if app.player1.isJump:
        app.player1.jump()

    #update player image
def game_onKeyPress(app, key):
    #if key != None:
        #for i in range(len(app.curObstacles)):
            #app.curObstacles[i].updateLocation(10)
    
    if key == "left":
        app.player1.switchLanes(-1)
    if key == "right":
        app.player1.switchLanes(+1)
    # if key == "up":
    #     app.player1.isJump = True
    #     app.player1.jump()

def game_onKeyHold(app,keys):
    if "up" in keys:
        app.player1.isJump = True
        

def game_onKeyRelease(app, key):
    pass




#--------------------#
#----PAUSE SCREEN----#
#--------------------#

#-------------------#
#----HELP SCREEN----#
#-------------------#


#---------------------#
#----CUSTOMIZATION----#
#---------------------#

def main():
    runAppWithScreens(initialScreen = "game")


main()
from cmu_graphics import *
from PIL import Image, ImageDraw
from constants import * 
import random 

from Obstacle import Obstacle, Train, Fence
from Player import Player
from Coin import Coin
import Obstacle as OBS
import functions as func
import Coin as C

def onAppStart(app):
    app.width = WIDTH
    app.height = HEIGHT
    app.stepCount = 0

    app.bg = Image.open(BACKGROUND)
    app.coin = Image.open(COIN)

    app.curObstacles = []
    app.curCoins = []

    app.spritesList = [] #the sorted version, 

    app.players = [Player("bluePlayer", 1)] #will be chosen in start screen
    app.player1 = app.players[0]
    #app.player2 = app.players[1]

    app.gameOver = False


    app.speed = 20
#--------------------#
#----START SCREEN----#
#--------------------#


#-------------------#
#----GAME SCREEN----#
#-------------------#

def game_redrawAll(app):
    drawImage(CMUImage(app.bg), 0,0)
    drawImage(CMUImage(app.coin), 950, 10)
    drawLabel(f"{app.player1.coinCount}", 1050, 60, size = 32)

    for l in app.spritesList:
        for sprite in l: #wait is this an mvc violation . . .
            if isinstance(sprite, Coin):
                for i in range(sprite.count):
                    x, y = sprite.location[0] + i*sprite.width, sprite.location[1]
                    img = func.loadImage(sprite)
                    drawImage(CMUImage(img), x, y)
            else:
                x, y = sprite.location
                img = func.loadImage(sprite)
                drawImage(CMUImage(img), x, y)

    for player in app.players:
        x, y = player.location
        img = func.loadImage(player)
        drawImage(CMUImage(img), x, y-50)


def game_onStep(app):
    app.stepsPerSecond = 20
    app.stepCount += 1
    if not app.gameOver:
        if app.stepCount%15 == 0:
            #new obstacle
            app.curObstacles.append(OBS.loadObstacle(app.curObstacles))

            #new coins
            app.curCoins.append(C.loadCoin(app.curCoins))
        #delete gone objects
        app.spritesList = func.drawSpritesInOrder(app.curObstacles + app.curCoins)
        #increase position of each piece on board
        for i in range(len(app.curObstacles)):
            app.curObstacles[i].updateLocation(app.speed)
        for i in range(len(app.curCoins)):
            app.curCoins[i].updateLocation(app.speed)
        
        if app.player1.isJump:
            app.player1.jump()
    
    if app.player1.isObstacleCollision(app.spritesList):
        app.gameOver = True
    
    app.player1.isCoinCollision(app.curCoins)



    #update player image
def game_onKeyPress(app, key):
    #if key != None:
        #for i in range(len(app.curObstacles)):
            #app.curObstacles[i].updateLocation(10)
    
    if key == "left" and not app.player1.isJump:
        app.player1.switchLanes(-1)
    elif key == "right" and not app.player1.isJump:
        app.player1.switchLanes(+1)
    elif key == "up":
        app.player1.isJump = True
    #     app.player1.jump()
    elif key == "space":
        if app.gameOver == True:
            print("collide")
            print(app.spritesList)

def game_onKeyHold(app,keys):
    pass
    # if "up" in keys:
    #     app.player1.isJump = True
        

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
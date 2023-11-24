from cmu_graphics import *
from PIL import Image, ImageDraw
from constants import * 
def onAppStart(app):
    app.width = WIDTH
    app.height = HEIGHT

    loadImages(app)


def loadImages(app):
    app.bg = Image.open(BACKGROUND)
    app.redTrain = Image.open(RED_TRAIN)
    app.redTrain = app.redTrain.resize((app.redTrain.size[0]//2,
                                        app.redTrain.size[1]//2))
    app.solidFence = Image.open(SOLID_FENCE)
    app.solidFence = app.solidFence.resize((app.solidFence.size[0]//5,
                                            app.solidFence.size[1]//5))


#--------------------#
#----START SCREEN----#
#--------------------#


#-------------------#
#----GAME SCREEN----#
#-------------------#

def game_redrawAll(app):
    drawImage(CMUImage(app.bg), 0,0)
    drawImage(CMUImage(app.redTrain), 400,165)
    drawImage(CMUImage(app.solidFence), 800,135)
    drawCircle(80,280,40, fill = "red")
def game_onStep(app):
    #load piece

    #increase position of each piece on board

    #update player image
    pass
def game_onKeyPress(app, key):
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
    print((app.redTrain.size[0]//2, app.redTrain.size[1]//2))
    print((app.solidFence.size[0]//5, app.solidFence.size[1]//5))

main()
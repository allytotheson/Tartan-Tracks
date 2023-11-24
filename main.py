from cmu_graphics import *
from PIL import Image, ImageDraw
from constants import * 
def onAppStart(app):
    app.width = WIDTH
    app.height = HEIGHT

    loadImages(app)


def loadImages(app):
    app.bg = Image.open(BACKGROUND)
    


#--------------------#
#----START SCREEN----#
#--------------------#


#-------------------#
#----GAME SCREEN----#
#-------------------#

def game_redrawAll(app):
    drawImage(CMUImage(app.bg), 0,0)

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

main()
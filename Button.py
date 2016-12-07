
## basically the button for splash screen

from tkinter import *
from Precious import Rock, Gold

import random



class Button(object):
    def __init__(self, x0, y0, x1, y1, color, text):
        self.x0, self.y0 = x0, y0
        self.x1, self.y1 = x1, y1
        self.color = color
        self.text = text
        self.name = text
        self.regularImage = PhotoImage(
                    file="image/button/emptyButton240.gif")
        self.highlightImage = PhotoImage(
                    file="image/button/emptyButtonHigh240.gif")

    def drawButton(self, canvas, motionPosn):
        # check if it's highlight
        if self.clickInButton(motionPosn[0], motionPosn[1]):
            currImage = self.highlightImage
        else: currImage = self.regularImage

        imageX = (self.x0 + self.x1)/2
        imageY = (self.y0 + self.y1)/2
        canvas.create_image(imageX, imageY, image= currImage)

        textX = (self.x0 + self.x1) / 2
        textY = (self.y0 + self.y1) / 2
        canvas.create_text(textX, textY, text = self.text, 
                                font = "Corbel 26 bold", fill = "yellow")

    def clickInButton(self, x, y):
        if ((x > self.x0) and (x < self.x1) and 
            (y > self.y0) and (y < self.y1)):
            return True
        return False

    def __repr__(self):
        return "(x0=%d,y0=%d),(x1=%d,y1=%d)"%(self.x0,self.y0,self.x1,self.y1)











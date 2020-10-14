import pygame

#TILES
class TileSet(object):
    def __init__(self, tiles, initX, initY, win):
        self.tileSet = tiles
        self.initX = initX
        self.initY = initY
        self.win = win
        self.xOff = 0

    def baseTile(self, x, y):
        self.win.blit(self.tileSet[0], (x + self.xOff, y))
        self.win.blit(self.tileSet[1], (x+128 + self.xOff, y))
        self.win.blit(self.tileSet[2], (x + 256 + self.xOff, y))
    
    def thickTile(self, x, y):
        self.win.blit(self.tileSet[0], (x + self.xOff, y))
        self.win.blit(self.tileSet[1], (x+128 + self.xOff, y))
        self.win.blit(self.tileSet[2], (x + 256 + self.xOff, y))
        self.win.blit(self.tileSet[3], (x + self.xOff, y+128))
        self.win.blit(self.tileSet[4], (x+128 + self.xOff, y+128))
        self.win.blit(self.tileSet[5], (x+256 + self.xOff, y+128))

    def thinSuspendedTile(self, x, y):
        self.win.blit(self.tileSet[12], (x + self.xOff, y))
        self.win.blit(self.tileSet[13], (x + 128 + self.xOff, y))
        self.win.blit(self.tileSet[14], (x + 256 + self.xOff, y))
    
    def customBaseTile(self, x, y, width, height=0):
        try:
            # To check if any error is there
            if type(width) == float:
                # To check if provided width is float
                raise FloatingPointError
            elif type(width) == int:
                # IF it is an integer then draw the image
                self.win.blit(self.tileSet[0], (x + self.xOff, y))
                # The first tile
                for i in range(1, width + 1):
                    # The mid tiles which decide the width
                    self.win.blit(self.tileSet[1], (x + (128 * i) + self.xOff, y))
                #The last block
                self.win.blit(self.tileSet[2], (x + (128*(width+1)) + self.xOff, y))
        except ZeroDivisionError:
            self.win.blit(self.tileSet[0], (x, y))
            for i in range(1, 1 + 1):
                self.win.blit(self.tileSet[1], (x + (128 * i) + self.xOff, y))
            self.win.blit(self.tileSet[2], (x + (128*(1+1)) + self.xOff, y))
    
    def moveForward(self, vel):
        # To move the platform
        self.xOff -= vel
    
    def moveBackward(self, vel):
        # To move the platform
        if  self.xOff < 0:
            self.xOff += vel
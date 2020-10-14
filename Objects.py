import pygame

class Objects(object):
    def __init__(self, win):
        self.images = {}
        self.win = win
        self.objectsTotal = len(self.images)
        self.count = 0

    def draw(self, name, x, y):
        self.win.blit(self.images[name], (x + self.count , y))
    
    def addObject(self, img, name):
        self.images[name] = img
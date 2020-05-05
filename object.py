import pygame

class ball(object):
    def __init__(self,x,y,r,color):
        self.x = x
        self.y = y
        self.radius = r
        self.color = color

    def draw(self, win):
        pygame.draw.circle(win, (0,0,0), (self.x,self.y), self.radius)
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius-1)

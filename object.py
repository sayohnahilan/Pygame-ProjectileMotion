import pygame

# ball
class ball(object):
    # create a ball
    def __init__(self,x,y,r,color):
        self.x = x
        self.y = y
        self.radius = r
        self.color = color

    # draw the ball and a small shadow behind it
    def draw(self, win):
        pygame.draw.circle(win, (0,0,0), (self.x,self.y), self.radius)
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius-1)

import pygame
import math
from object import ball
from util import findAngle, goBall

#tinker with these settings
width = 1600
height = 900
ballRadius = 6
timeInc = 0.05
powerDivider = 10

win = pygame.display.set_mode((width,height))
pygame.display.set_caption('Projectile Motion with Pygame')

def updateScreen():
    win.fill((64, 64, 64))
    myBall.draw(win)
    pygame.draw.line(win, (0, 255, 0), project[0], project[1])
    pygame.display.update()

playing = True
time = 0
power = 0
angle = 0
clock = pygame.time.Clock()
inProgress = False

myBall = ball(round(width/2), (height - ballRadius - 1), ballRadius, (255, 0, 0))

while playing:
    clock.tick(200)
    if inProgress:
        if (myBall.y < (height - ballRadius)):
            time += timeInc
            new = goBall(xCurrent, yCurrent, power, angle, time)
            myBall.x = new[0]
            myBall.y = new[1]
        else:
            inProgress = False
            time = 0
            myBall.y = (height - ballRadius - 1)

    project = [(myBall.x, myBall.y), pygame.mouse.get_pos()]
    updateScreen()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if not inProgress:
                inProgress = True
                xCurrent = myBall.x
                yCurrent = myBall.y
                mouse = pygame.mouse.get_pos()
                angle = findAngle(mouse, myBall)
                power = math.sqrt((project[1][1]-project[0][1])**2 +(project[1][0]-project[0][1])**2) / powerDivider

pygame.quit()
quit()

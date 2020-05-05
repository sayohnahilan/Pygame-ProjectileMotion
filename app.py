import pygame
import math
from object import ball
from util import findAngle, goBall

width = 1600
height = 900

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
myBall = ball(800, 450, 6, (255, 0, 0))

while playing:
    clock.tick(250)
    if inProgress:
        time += 0.10
        new = goBall(myBall.x, myBall.y, power, angle, time)
        myBall.x = new[0]
        myBall.y = new[1]

    project = [(myBall.x, myBall.y), pygame.mouse.get_pos()]
    updateScreen()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            inProgress = True
            mouse = pygame.mouse.get_pos()
            angle = findAngle(mouse, myBall)
            power = math.sqrt((project[1][1]-project[0][1])**2 +(project[1][0]-project[0][1])**2)

pygame.quit()
quit()

import pygame
import math
from object import ball
from util import findAngle, goBall

# tinker with these settings
width = 1600
height = 900
ballRadius = 6
timeInc = 0.05
powerDivider = 10

# start pygame window
win = pygame.display.set_mode((width, height))
pygame.display.set_caption('Projectile Motion with Pygame')


# call to update elements on window
def updateScreen():
    win.fill((64, 64, 64))
    myBall.draw(win)
    pygame.draw.line(win, (0, 255, 0), project[0], project[1])
    pygame.display.update()


# initial variables
playing = True
time = 0
power = 0
angle = 0
clock = pygame.time.Clock()
inProgress = False

# draw ball
myBall = ball(round(width / 2), (height - ballRadius - 1), ballRadius, (255, 0, 0))

while playing:
    clock.tick(200)
    # if ball is moving
    if inProgress:
        # if in boundary
        if (myBall.y < (height - ballRadius)):
            time += timeInc
            new = goBall(xCurrent, yCurrent, power, angle, time)
            myBall.x = new[0]
            myBall.y = new[1]
        # stop moving
        else:
            inProgress = False
            time = 0
            myBall.y = (height - ballRadius - 1)

    # constantly draw line between mouse and ball and update screen
    project = [(myBall.x, myBall.y), pygame.mouse.get_pos()]
    updateScreen()

    # pygame event
    for event in pygame.event.get():
        # quit
        if event.type == pygame.QUIT:
            playing = False

        # if mousedown
        if event.type == pygame.MOUSEBUTTONDOWN:
            # if ball is not already moving
            if not inProgress:
                # get data and start moving ball
                inProgress = True
                xCurrent = myBall.x
                yCurrent = myBall.y
                mouse = pygame.mouse.get_pos()
                angle = findAngle(mouse, myBall)
                power = math.sqrt(
                    (project[1][1] - project[0][1]) ** 2 + (project[1][0] - project[0][1]) ** 2) / powerDivider

# end game
pygame.quit()
quit()

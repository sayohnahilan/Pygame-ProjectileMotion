import math

def findAngle(mouse, myBall):
    mouseX = mouse[0]
    mouseY = mouse[1]
    ballX = myBall.x
    ballY = myBall.y
    try:
        angle = math.atan((ballY - mouseY) / (ballX - mouseX))
    except:
        angle = math.pi / 2

    # Mouse is above and to the right of ball
    if mouseY < ballY and mouseX > ballX:
        angle = abs(angle)
    # Mouse is above and to the left of ball
    elif mouseY < ballY and mouseX < ballX:
        angle = math.pi - angle

    return angle
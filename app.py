import pygame
from object import ball

width = 1600
height = 900

win = pygame.display.set_mode((width,height))
pygame.display.set_caption('Projectile Motion with Pygame')

def updateScreen():
    win.fill((64, 64, 64))
    myBall.draw(win)
    pygame.display.update()

playing = True
time = 0
power = 0
angle = 0
clock = pygame.time.Clock()

myBall = ball(800, 450, 6, (255, 0, 0))

while playing:
    clock.tick(200)
    updateScreen()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

pygame.quit()
quit()

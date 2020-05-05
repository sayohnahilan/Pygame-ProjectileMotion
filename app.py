import pygame

width = 1200
height = 500

win = pygame.display.set_mode((width,height))
pygame.display.set_caption('Projectile Motion with Pygame')

playing = True
time = 0
power = 0
angle = 0
clock = pygame.time.Clock()

while playing:
    clock.tick(200)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

pygame.quit()
quit()

import pygame
import random




pygame.init()

SCREEN_WIDTH = 2400
SCREEN_HEIGHT = 1600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill((0, 0, 0))

pygame.display.set_caption('Jakobs Game')

run = True
while run: 

    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)

    x = random.randint(0, SCREEN_WIDTH)
    y = random.randint(0, SCREEN_HEIGHT)

    radius = random.randint(1, 3)

    pygame.draw.circle(screen, (red, green, blue), (x, y), radius)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
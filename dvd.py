import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill((200, 200, 200))

pygame.display.set_caption('Jakobs Game')

#Variables
x= random.randint(0, 800)
y= random.randint(0, 600)
speedX = random.uniform(-0.5, 0.5)
speedY = random.uniform(-0.5, 0.5)
r = 200
g = 200
b = 200

run = True
while run:
    screen.fill((200, 200, 200))

    pygame.draw.circle(screen, (r, g, b), [x,y], 30)
    
    if x+30 > 800 or x-30 < 0:
        speedX = -speedX
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        speedX = random.uniform(-0.5, 0.5)
        speedY = random.uniform(-0.5, 0.5)
    
    x = x + speedX

    if y+30 > 600 or y-30 < 0:
        speedY = -speedY
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        speedX = random.uniform(-0.5, 0.5)
        speedY = random.uniform(-0.5, 0.5)

    y = y + speedY

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
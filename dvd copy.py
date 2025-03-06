import pygame
import random



pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill((200, 200, 200))

pygame.display.set_caption('Jakobs Game')

#Variables
x= 300
y= 300
speedX = 0
speedY = 0
r = 200
g = 200
b = 200

run = True
while run:

    pygame.draw.circle(screen, (250, 0, 0), [x,y], 30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print('Left key pressed')
                speedX = -0.2
            if event.key == pygame.K_RIGHT:
                print('Right key pressed')
                speedX = 0.2
            if event.key == pygame.K_UP:
                print('Up key pressed')
                speedY = -0.2
            if event.key == pygame.K_DOWN:
                print('Down key pressed')
                speedY = 0.2

    x = x + speedX
    y = y + speedY

    pygame.display.update()

pygame.quit()
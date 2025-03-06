import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill((200, 200, 200))

pygame.display.set_caption('Jakobs Game')

x = 0
y = 300
speed = 0.1
rad = 5

run = True
while run:
    screen.fill((200, 200, 200))

    pygame.draw.circle(screen, (255, 255, 0), [x,y], 30)
    
    
    if x > 800:
        speed = -speed

    if x < 0:
        speed = -speed

    x = x + speed


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
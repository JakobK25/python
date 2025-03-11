import pygame
import random
import pyfirmata
import time

port = 'COM3'
board = pyfirmata.Arduino(port)
#led = board.get_pin('d:3:o')
tSensor = board.get_pin('a:0:i')

it = pyfirmata.util.Iterator(board)
it.start()

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill((200, 200, 200))

pygame.display.set_caption('Jakobs Game')

#Variables

run = True
while run:
    screen.fill((200, 200, 200))

    temp = tSensor.read()
    
    if temp is not None:
        print(temp)

        height = int(temp * 400)
        
        pygame.draw.rect(screen, (0, 255, 0), [100, SCREEN_HEIGHT - height, 50, height])

        if temp > 0.8000 :
            pygame.draw.rect(screen, (255, 0, 0), [100, SCREEN_HEIGHT - height, 50, height * 2])

    else:
        print("Reading sensor...")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
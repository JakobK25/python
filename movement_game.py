import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill((200, 200, 200))

pygame.display.set_caption('Jakobs Game')

run = True
while run:



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                print('Left key pressed')
            if event.key == pygame.K_RIGHT:
                print('Right key pressed')
            if event.key == pygame.K_UP:
                print('Up key pressed')
            if event.key == pygame.K_DOWN:
                print('Down key pressed')

    pygame.display.update()

pygame.quit()
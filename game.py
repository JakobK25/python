import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill((200, 200, 200))

pygame.display.set_caption('Jakobs Game')

run = True
while run:

    pygame.draw.circle(screen, (255, 255, 0), [400,300], 275)
    pygame.draw.circle(screen, (255, 255, 0), [150,100], 50)
    pygame.draw.circle(screen, (255, 255, 0), [650,100], 50)

    pygame.draw.circle(screen, (0, 0, 0), [150,100], 10)
    pygame.draw.circle(screen, (0, 0, 0), [650,100], 10)

    pygame.draw.circle(screen, (0, 0, 0), [300,250], 25)
    pygame.draw.circle(screen, (0, 0, 0), [500,250], 25)

    pygame.draw.circle(screen, (255, 255, 255), [300,250], 10)
    pygame.draw.circle(screen, (255, 255, 255), [500,250], 10)

    pygame.draw.arc(screen, (255, 0, 0), [300, 325, 200, 150], 3.14, 6.28, 10)    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
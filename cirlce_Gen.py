import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill((200, 200, 200))

pygame.display.set_caption('Jakobs Game')

run = True
while run: 

    for i in range(10):
        pygame.draw.circle(screen, (0, 0, 0), (400, 300), 50 * i, 5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
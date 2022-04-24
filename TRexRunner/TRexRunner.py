import pygame, sys
pygame.init()

# init pygame window
screen = pygame.display.set_mode((1200, 400))
pygame.display.set_caption("TRex Runner")
clock = pygame.time.Clock()
FPS = 60


while True:
    for event in pygame.event.get():
        # exit game
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(FPS)
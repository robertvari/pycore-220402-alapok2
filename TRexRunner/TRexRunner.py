from utilities.settings import *
import pygame, sys
pygame.init()

# init pygame window
screen = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption(GAMETITLE)
clock = pygame.time.Clock()


def check_events():
    for event in pygame.event.get():
        # handle exit game
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()

        # handle jump key
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            print("Jump")


def game_loop():
    while True:
        check_events()

        screen.fill(BACKGROUND_COLOR)
        pygame.display.update()
        clock.tick(FPS)

game_loop()
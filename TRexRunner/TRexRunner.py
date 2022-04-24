from utilities.settings import *
import pygame, sys
pygame.init()

from game_assets.start_screen import draw_start_screen
from game_assets.game_over_screen import draw_game_over_screen
from game_assets.main_game import main_game_screen

# init pygame window
screen = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption(GAMETITLE)
clock = pygame.time.Clock()

start_screen = False
game_over = False


def main():
    game_loop()


def check_events():
    for event in pygame.event.get():
        # handle exit game
        if event.type == pygame.QUIT:
            exit_game()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            exit_game()


def exit_game():
    pygame.quit()
    sys.exit()


def game_loop():
    while True:
        check_events()
        screen.fill(BACKGROUND_COLOR)

        if not game_over:
            if start_screen:
                draw_start_screen(screen)
            else:
                main_game_screen(screen)
        else:
            draw_game_over_screen(screen)

        pygame.display.update()
        clock.tick(FPS)


# start game
main()

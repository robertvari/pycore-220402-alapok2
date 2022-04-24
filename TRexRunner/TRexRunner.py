from utilities.settings import *
import pygame, sys
from pygame import mixer
pygame.init()
mixer.init()

from game_assets.start_screen import draw_start_screen
from game_assets.game_over_screen import draw_game_over_screen
from game_assets.main_game import main_game_screen
from game_assets.t_rex import get_trex_rect
from game_assets.cactus import get_cactus_rect
from utilities.resources import get_resource

# init pygame window
screen = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption(GAMETITLE)
clock = pygame.time.Clock()

start_screen = False
game_over = False
game_over_sound = pygame.mixer.Sound(get_resource("death.wav"))
game_over_sound.set_volume(0.2)


def main():
    game_loop()


def check_events():
    for event in pygame.event.get():
        # handle exit game
        if event.type == pygame.QUIT:
            exit_game()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            exit_game()

        # if game over and space pressed


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
                check_collisions()
        else:
            draw_game_over_screen(screen)

        pygame.display.update()
        clock.tick(FPS)


def check_collisions():
    global game_over

    cactus_rect = get_cactus_rect()
    trex_rect = get_trex_rect()

    if trex_rect.colliderect(cactus_rect):
        game_over = True
        game_over_sound.play()

# start game
main()

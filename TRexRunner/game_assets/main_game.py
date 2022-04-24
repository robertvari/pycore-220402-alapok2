import pygame
from utilities.resources import get_resource

from game_assets.sky import draw_sky

# load background image
background_image = pygame.image.load(get_resource("mountains.png"))


def main_game_screen(screen):
    screen.blit(background_image, (-400, -100))

    # sky
    draw_sky(screen)

    # ground

    # T-Rex

    # Cactus

    # Birds
import pygame
from utilities.resources import get_resource

from game_assets.clouds import draw_clouds

# load background image
background_image = pygame.image.load(get_resource("mountains.png"))


def main_game_screen(screen):
    screen.blit(background_image, (-400, -100))

    draw_clouds(screen)

    # ground

    # T-Rex

    # Cactus

    # Birds
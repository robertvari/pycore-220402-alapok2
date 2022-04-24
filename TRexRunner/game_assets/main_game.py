import pygame
from utilities.resources import get_resource

from game_assets.clouds import draw_clouds
from game_assets.ground import draw_ground
from game_assets.t_rex import draw_trex
from game_assets.cactus import draw_cactus

# load background image
background_image = pygame.image.load(get_resource("mountains.png"))


def main_game_screen(screen):
    screen.blit(background_image, (-400, -70))

    draw_clouds(screen)
    draw_ground(screen)

    draw_trex(screen)

    # Cactus
    draw_cactus(screen)

    # Birds
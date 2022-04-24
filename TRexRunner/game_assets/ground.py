import pygame
from utilities.resources import get_resource

ground_image = pygame.image.load(get_resource("ground.png"))


def draw_ground(screen):
    screen.blit(ground_image, (0, -30))
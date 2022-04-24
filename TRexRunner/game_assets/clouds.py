import pygame
from utilities.resources import get_resource

cloud_image = pygame.image.load(get_resource("clouds.png"))


def draw_clouds(screen):
    screen.blit(cloud_image, (0, 0))
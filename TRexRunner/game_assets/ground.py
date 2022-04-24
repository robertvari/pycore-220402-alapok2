import pygame
from utilities.resources import get_resource

ground_speed = 20
ground_image = pygame.image.load(get_resource("ground.png"))
ground_rect = ground_image.get_rect(bottomleft=(0, 400))


def draw_ground(screen):
    ground_rect.x -= ground_speed
    screen.blit(ground_image, ground_rect)
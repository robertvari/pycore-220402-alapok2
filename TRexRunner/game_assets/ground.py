import pygame
from utilities.resources import get_resource

ground_speed = 20
ground_image1 = pygame.image.load(get_resource("ground.png"))
ground_rect1 = ground_image1.get_rect(bottomleft=(0, 400))

ground_image2 = pygame.image.load(get_resource("ground.png"))
ground_rect2 = ground_image2.get_rect(bottomleft=ground_rect1.bottomright)


def draw_ground(screen):
    if ground_rect1.right < 0:
        ground_rect1.bottomleft = ground_rect2.bottomright

    ground_rect1.x -= ground_speed
    screen.blit(ground_image1, ground_rect1)

    if ground_rect2.right < 0:
        ground_rect2.bottomleft = ground_rect1.bottomright

    ground_rect2.x -= ground_speed
    screen.blit(ground_image2, ground_rect2)
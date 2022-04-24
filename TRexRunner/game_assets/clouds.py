import pygame
from utilities.resources import get_resource

cloud_speed = 5

cloud_image1 = pygame.image.load(get_resource("clouds.png"))
cloud_rect_1 = cloud_image1.get_rect(x=0, y=0)

cloud_image2 = pygame.image.load(get_resource("clouds.png"))
cloud_rect_2 = cloud_image1.get_rect(midleft=cloud_rect_1.midright)


def draw_clouds(screen):
    if cloud_rect_1.right < 0:
        cloud_rect_1.midleft = cloud_rect_2.midright

    cloud_rect_1.x -= cloud_speed
    screen.blit(cloud_image1, cloud_rect_1)

    if cloud_rect_2.right < 0:
        cloud_rect_2.midleft = cloud_rect_1.midright

    cloud_rect_2.x -= cloud_speed
    screen.blit(cloud_image2, cloud_rect_2)
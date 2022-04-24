import pygame
from utilities.resources import get_resource
from utilities.settings import SCREENSIZE


cactus_image = pygame.image.load(get_resource("cactus_01.png"))
cactus_rect = cactus_image.get_rect(x=SCREENSIZE[0], y=250)


def draw_cactus(screen):
    cactus_rect.x -= 20
    if cactus_rect.right < 0:
        cactus_rect.x = SCREENSIZE[0]

    screen.blit(cactus_image, cactus_rect)
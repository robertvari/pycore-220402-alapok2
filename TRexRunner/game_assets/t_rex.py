import pygame
from utilities.resources import get_resource

ground_pos = 250

trex_image = pygame.image.load(get_resource("trex_run_01.png"))
trex_rect = trex_image.get_rect(x=50, y=ground_pos)


def draw_trex(screen):
    screen.blit(trex_image, trex_rect)
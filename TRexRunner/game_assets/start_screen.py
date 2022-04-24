import pygame

trex_image = pygame.image.load("resources/trex_idle.png")


def draw_start_screen(screen):
    """
    This is the function which draws the game start screen.
    :param screen: This is the game window
    :return: None
    """
    screen.blit(trex_image, (0, 0))

import pygame
from utilities.settings import GAMETITLE

# setup game title
title_font = pygame.font.Font("resources/dogicabold.ttf", 40)
title = title_font.render(GAMETITLE, True, "white")

# press space to start
press_space_font = pygame.font.Font("resources/dogica.ttf", 25)
press_space_text = press_space_font.render("Press Space to Start", True, "white")

trex_image = pygame.image.load("resources/trex_idle.png")


def draw_start_screen(screen):
    """
    This is the function which draws the game start screen.
    :param screen: This is the game window
    :return: None
    """
    screen.blit(trex_image, (0, 0))
    screen.blit(title, (0, 300))
    screen.blit(press_space_text, (0, 150))

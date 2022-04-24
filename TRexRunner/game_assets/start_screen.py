import pygame
from utilities.settings import GAMETITLE, SCREENSIZE

# setup game title
title_font = pygame.font.Font("resources/dogicabold.ttf", 40)
title = title_font.render(GAMETITLE, True, "white")
title_rect = title.get_rect(midtop=(SCREENSIZE[0]/2, 100))

# load trex image
trex_image = pygame.image.load("resources/trex_idle.png")
trex_rect = trex_image.get_rect(midtop=(title_rect.midbottom[0], title_rect.midbottom[1]))

# press space to start
press_space_font = pygame.font.Font("resources/dogica.ttf", 25)
press_space_text = press_space_font.render("Press Space to Start", True, "white")
press_space_rect = press_space_text.get_rect(midtop=(trex_rect.midbottom[0], trex_rect.midbottom[1] + 10))


def draw_start_screen(screen):
    """
    This is the function which draws the game start screen.
    :param screen: This is the game window
    :return: None
    """
    screen.blit(title, title_rect)
    screen.blit(trex_image, trex_rect)
    screen.blit(press_space_text, press_space_rect)

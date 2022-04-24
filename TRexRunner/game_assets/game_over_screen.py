import pygame
from utilities.settings import SCREENSIZE
from utilities.resources import get_resource

# setup game title
title_font = pygame.font.Font(get_resource("dogicabold.ttf"), 40)
title = title_font.render("Game Over", True, "white")
title_rect = title.get_rect(midtop=(SCREENSIZE[0]/2, 100))

# load trex image
dead_trex_frames = [
    pygame.image.load(get_resource("trex_dead_02.png")),
    pygame.image.load(get_resource("trex_dead_03.png")),
]
trex_rect = dead_trex_frames[0].get_rect(midtop=(title_rect.midbottom[0], title_rect.midbottom[1]))
frame_index = 0

# press space to start
press_space_font = pygame.font.Font(get_resource("dogica.ttf"), 25)
press_space_text = press_space_font.render("Press Space to Restart Game", True, "white")
press_space_rect = press_space_text.get_rect(midtop=(trex_rect.midbottom[0], trex_rect.midbottom[1] + 10))


def draw_game_over_screen(screen):
    global frame_index

    screen.blit(title, title_rect)

    frame_index += 0.2
    if frame_index >= len(dead_trex_frames):
        frame_index = 0

    screen.blit(dead_trex_frames[int(frame_index)], trex_rect)

    screen.blit(press_space_text, press_space_rect)
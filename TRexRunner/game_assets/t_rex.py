import pygame
from utilities.resources import get_resource

ground_pos = 250

trex_frames = [
    pygame.image.load(get_resource("trex_run_01.png")),
    pygame.image.load(get_resource("trex_run_02.png"))
]
frame_index = 0
trex_rect = trex_frames[frame_index].get_rect(x=50, y=ground_pos - 150)

gravity = 0
on_ground = True


def draw_trex(screen):
    global frame_index, gravity, on_ground

    # handle jump
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        jump()

    frame_index += 0.3
    if frame_index >= len(trex_frames):
        frame_index = 0

    gravity += 1
    trex_rect.y += gravity

    if trex_rect.y >= ground_pos:
        gravity = 0
        trex_rect.y = ground_pos
        on_ground = True

    screen.blit(trex_frames[int(frame_index)], trex_rect)


def jump():
    global gravity, on_ground

    if not on_ground:
        return

    gravity -= 20
    on_ground = False

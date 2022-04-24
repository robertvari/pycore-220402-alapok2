import pygame
from utilities.resources import get_resource

ground_pos = 250

trex_frames = [
    pygame.image.load(get_resource("trex_run_01.png")),
    pygame.image.load(get_resource("trex_run_02.png"))
]
frame_index = 0
trex_rect = trex_frames[frame_index].get_rect(x=50, y=ground_pos)


def draw_trex(screen):
    global frame_index

    frame_index += 0.3
    if frame_index >= len(trex_frames):
        frame_index = 0

    screen.blit(trex_frames[int(frame_index)], trex_rect)
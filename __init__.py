import os.path
import pygame

import src.block as block

project_dir = os.path.join(os.path.dirname(__file__), '..')
assets_dir = os.path.join(project_dir, 'assets')

cell_size = 64
cols = 10
rows = 20

# Interval in frames when the game checks for input
frames_interval = 0

width = cell_size*cols
height = cell_size*rows

bg_color = (20,20,20)

pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True

player = block.Block(screen, [0,0], cell_size, "red")

def validate_position(position: list) -> list:
    p_x, p_y = position
    if p_x <= 0:
        p_x = 0
    elif p_x > cols-1:
        p_x = cols-1
    return [p_x,p_y]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    p_x, p_y = player.get_position()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if frames_interval == 0:
            frames_interval = 10
            player.set_position(validate_position([p_x-1,p_y]))
    elif keys[pygame.K_RIGHT]:
        if frames_interval == 0:
            frames_interval = 10
            player.set_position(validate_position([p_x+1,p_y]))



    screen.fill(bg_color)

    # RENDER YOUR GAME HERE
    player.draw()

    pygame.display.flip()

    if frames_interval > 0: frames_interval -= 1
    clock.tick(60)  # limits FPS to 60

pygame.quit()
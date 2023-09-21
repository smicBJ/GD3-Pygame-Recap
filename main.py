import sys
import pygame as py

from assets.models.player import Player

# Screen Settings
py.init()
screen_dimensions = (854, 480)
screen = py.display.set_mode(screen_dimensions)
clock = py.time.Clock()

# Misc Setup
py.display.set_caption("Pygame 3 Game")

# Sprites and Graphics setup
bg = py.image.load("assets/graphics/bg_space.png").convert()

ship_group = py.sprite.GroupSingle()

player = Player(group=ship_group)

# Game Loop
while True:
    # Event Loop
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()

    # Time, Updates, Graphics
    delta_time = clock.tick(120) / 1000

    ship_group.update()

    screen.blit(bg, (0, 0))
    ship_group.draw(screen)

    # Screen Update
    py.display.update()

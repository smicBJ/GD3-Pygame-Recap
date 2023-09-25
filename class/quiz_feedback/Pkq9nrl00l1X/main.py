# Standard libraries should be imported before external ones
import pygame as py
import sys

# Screen Setting
py.init()
screen_dimensions = (1280, 720)
screen = py.display.set_mode(screen_dimensions)
clock = py.time.Clock()

from player import Player

# Misc Setup, fun fact I literally just realized misc stood for miscellaneous
py.display.set_caption("Pygame Review")

# Graphics Setup,
bg = py.image.load("assets/map.png")

ship_group = py.sprite.GroupSingle()

player = Player(group=ship_group)


# Lame Goop
while True:
    # Event Loop
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()

    # Time Updates, Graphics
    delta_time = clock.tick(120) / 1000

    ship_group.update()

    screen.blit(bg, (0, 0))
    ship_group.draw(screen)

    # Screen Updates
    py.display.update()

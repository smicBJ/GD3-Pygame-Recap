import sys
import pygame as py

# Screen Settings
py.init()
screen_dimensions = (854, 480)
screen = py.display.set_mode(screen_dimensions)
clock = py.time.Clock()

# Misc Setup
py.display.set_caption("Pygame 3 Game")

# Sprites and Graphics setup
bg = py.image.load("assets/graphics/bg_space.png").convert()

# Game Loop
while True:
    # Event Loop
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()

    # Time, Updates, Graphics
    delta_time = clock.tick(120) / 1000

    screen.blit(bg, (0, 0))

    # Screen Update
    py.display.update()

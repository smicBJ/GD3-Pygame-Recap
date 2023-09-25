# external libraries should be imported after standard ones
import pygame as py
import sys



#Screen Settings
py.init()
screen_dimensions = (1280, 720)
screen = py.display.set_mode(screen_dimensions)
clock = py.time.Clock()

from graphics.player import Player

#Misc Setup
py.display.set_caption("pygame 3 Game")

#Sprites and Graphics setup
bg = py.image.load("graphics/map.png").convert()

player_group = py.sprite.GroupSingle()

player = Player(group=player_group)

#Game loop
while True:
    #Event loop
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit
    #Time, Update, Graphics
    delta_time = clock.tick(120) / 1000

    player_group.update()

    screen.blit(bg, (0, 0))
    player_group.draw(screen)

    #Screen Update
    py.display.update()

import pygame as py
import sys


py.init()
screen_dimension = (1280,720)
screen = py.display.set_mode(screen_dimension)
clock = py.time.Clock()

from player import Player

player_group = py.sprite.GroupSingle()
player = Player(group=player_group)

py.display.set_caption("My pygame")
bg = py.image.load("Unit 2 Quiz - assets/map.png").convert()

while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()

    delta_time = clock.tick(120)/1000

    player_group.update()

    screen.blit(bg,(0,0))
    player_group.draw(screen)

    py.display.update()
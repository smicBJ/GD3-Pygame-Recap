import sys

import pygame as py

from player_r1 import Player

# -1: You are missing the import of the Player class here
# for the above issue, I added the missing import of player

# Put spaces between your import, variables and function definitions
#initializing game
py.init()
screen_dimensions = (720,480)
# -1: Do not put spaces between methods
#deleted the spaces
screen = py.display.set_mode(screen_dimensions)
clock = py.time.Clock()

# -1: Why are you flipping the display here? This line seems irrelevant
#py.display.flip()
# for above issue, I removed the line. I wanted to refresh the page at the time.
clock.tick(60)

#misc setup
py.display.set_caption("trial")

# -1: You are missing the group being created here
# created the group, name as "characters".
characters = py.sprite.GroupSingle()

player = Player(group=characters)
# -1: You should create the player instance here and add it to the group
#created the missing player
# added the player into the group "characters"

#spirit and graphic set up
bg = py.image.load("Unit 2 Quiz - assets/map.png").convert()

#game loop
while true
    #events
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()



while true
    delta_time = clock.tick(100)/1200
    screen.blit(bg, (0, 0))


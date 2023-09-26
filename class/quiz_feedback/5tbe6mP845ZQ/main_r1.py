import sys

import pygame as py

from player_r1 import Player

# ✅: You are missing the import of the Player class here
# for the above issue, I added the missing import of player

# Put spaces between your import, variables and function definitions
#initializing game
py.init()
screen_dimensions = (720,480)
# ✅: Do not put spaces between methods
#deleted the spaces
screen = py.display.set_mode(screen_dimensions)
clock = py.time.Clock()

# ✅: Why are you flipping the display here? This line seems irrelevant
#py.display.flip()
# for above issue, I removed the line. I wanted to refresh the page at the time.
clock.tick(60)

#misc setup
py.display.set_caption("trial")

# ✅: You are missing the group being created here
# created the group, name as "characters".
characters = py.sprite.GroupSingle()

player = Player(group=characters)
# ✅: You should create the player instance here and add it to the group
#created the missing player
# added the player into the group "characters"

#spirit and graphic set up
bg = py.image.load("Unit 2 Quiz - assets/map.png").convert()

#game loop
# -1: You are missing the colon after the true, which should be with a capital T
while true
    #events
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()
    # -1: This loop is missing the group update and draw method being called and then the screen being updated

# -1: You do not need two while loops so this second one will be irrelevant
while true
    delta_time = clock.tick(100)/1200
    screen.blit(bg, (0, 0))


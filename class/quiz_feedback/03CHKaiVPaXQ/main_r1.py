# Standard libraries should be imported before the external libraries
import pygame
import sys
from player import Player
# ✅: irrelevant import
#from pygame.locals import *
#deleeted the irrelevant import

# ✅: You call the init method twice, making one of the lines redundant
#pygame.init()
#deleted one init so it is not as redundant
# Initialize Pygame
pygame.init()



screensize = (1280, 720)
screen = pygame.display.set_mode(screensize)
clock = pygame.time.Clock()
# ✅: This should be in the game loop and why is it indented?
#    screen.blit(background, (0, 0))
# I moved it down into the game loop

pygame.display.set_caption("Unit2 Quiz")


bg = pygame.image.load("graphics/map.png").convert()

player_group = pygame.sprite.GroupSingle()

player = Player(group=player_group)

#Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit
    delta_time = clock.tick(120) / 1000

    player_group.update()

    screen.blit(bg,(0,0))
    player_group.draw(screen)






    pygame.display.update()




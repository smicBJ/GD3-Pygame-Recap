# Standard libraries should be imported before the external libraries
import pygame
import sys
# -1: irrelevant import
from pygame.locals import *

# -1: You call the init method twice, making one of the lines redundant
pygame.init()

# Initialize Pygame
pygame.init()



WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("unit2quiz")
background = pygame.image.load("assets/map.png")
running = True
clock = pygame.time.Clock()
# -2: This should be in the game loop and why is it indented?
    screen.blit(background, (0, 0))



pygame.quit()
sys.exit()

# -1: You have an import for time that is not being used here, and you are mixing import types

#REMOVED OLD IMPORT
#import pygame, time, player
import sys
import pygame
#USED FROM IMPORT TO CLEAN UP LATER CODE
from player import Player

# pygame setup
pygame.init()
screen = pygame.display.set_mode((396, 480))
pygame.display.set_caption("Unit 2 Quiz")
clock = pygame.time.Clock()
background_img = pygame.image.load("unit2_quiz_assets/assets/map.png").convert()
background_img = pygame.transform.scale(background_img, (396, 480))
# -1: This blit must be done in the game loop
#BLIT MOVED TO GAME LOOP
#screen.blit(background_img, (0, 0))
#SPRITE GROUP RENAMED FROM "PLAYERS" TO "SPRITES" SINCE THERE WILL ONLY BE ONE PLAYER
sprites = pygame.sprite.Group()
# -1: Missing the instance of the player sprite being created
# -1: Missing adding the player sprite to the group
#CREATING & ADDING PLAYER INSTANCE TO SPRITE GROUP MOVED HERE FROM GAME LOOP
player = Player()
sprites.add(player)
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # -1: The first thing in the changes section should be the creation of delta time

    # -1: This is not only not the right place to create an instance and add it to the group, but also the wrong cond.
    # SPRITE INSTANCE MOVED TO PROPER LOCATION & REMOVED
    # mouse = pygame.mouse.get_pressed()
    # if mouse[0]:
    #     player = sprite.Player()
    #     players.add(player)

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    screen.blit(background_img, (0, 0))
    for sprite in sprites:
        screen.blit(sprite.image, (sprite.rect.x, sprite.rect.y))
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
sys.exit()
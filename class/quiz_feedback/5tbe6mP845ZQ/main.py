import sys
import pygame as py
# -1: You are missing the import of the Player class here

# Put spaces between your import, variables and function definitions
#initializing game
py.init()
screen_dimensions = (720,480)
# -1: Do not put spaces between methods
screen = py.display. set_mode(screen_dimensions)
clock = py.time.Clock()

# -1: Why are you flipping the display here? This line seems irrelevant
py.display.flip()
clock.tick(60)

#misc setup
py.display.set_caption("trial")

# -1: You are missing the group being created here
# -1: You should create the player instance here and add it to the group

#spirit and graphic set up
bg = py.image.load("Unit 2 Quiz - assets/map.png").convert()

#game loop
while true
    #events
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()

class Player(pygame.sprite.Sprite):
    def _init_ (player_img, player_rect,player_pos)
        pygame.sprite.Sprite.__init__(self)
        self.image = ("Unit 2 Quiz - assets/0.png")
        self.rect = player_rect (0)



while true
    delta_time = clock.tick(100)/1200
    screen.blit(bg, (0, 0))


import pygame as py
from player_r1 import Player

py.init()
# ✅: When setting the mode, you are setting the screen size. Anything would have worked except 0 by 0 pixels
# You're wrong
screen = py.display.set_mode((0, 0))
clock = py.time.Clock()
running = True
dt = 0

all_sprites_list = py.sprite.Group()
a = Player()

all_sprites_list.add(a)

bg = py.image.load('ass/map.png').convert()
while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False

    dt = clock.tick(60) / 1000

    # -1: Where is the update call on the sprite group?
    
    screen.blit(py.transform.scale(bg, screen.get_size()), (0, 0))
    all_sprites_list.draw(screen), (100, 100)
    py.display.flip()
py.quit()

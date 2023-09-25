import pygame as py
# -1: The following import is irrelevant to the task
from PIL import Image

from player import Player

py.init()
# -1: When setting the mode, you are setting the screen size. Anything would have worked except 0 by 0 pixels
screen = py.display.set_mode((0, 0))
clock = py.time.Clock()
running = True
dt = 0

all_sprites_list = py.sprite.Group()
a = Player(screen.get_size()[1])

all_sprites_list.add(a)

bg = [py.image.load('ass/map.png').convert(), Image.open("ass/map.png").size]
while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
    keys = py.key.get_pressed()
    mouse = py.mouse.get_pos()

    dt = clock.tick(60) / 1000

    all_sprites_list.update(keys=keys, mouse=mouse, action=1, dt=dt)

    screen.blit(py.transform.scale(bg[0], screen.get_size()), (0, 0))
    all_sprites_list.draw(screen), (100, 100)
    py.display.flip()
py.quit()

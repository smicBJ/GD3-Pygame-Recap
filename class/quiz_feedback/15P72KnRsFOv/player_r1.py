# This does not pertain to the quiz but the filenames in python should always be lowercase
# I changed your "player.py" to "player.py"

import pygame as py

# You do not need these variables here since you are creating them in the class
SCREEN_W = py.display.get_window_size()[0]
SCREEN_H = py.display.get_window_size()[1]


class Player(py.sprite.Sprite):

    def __init__(self, group):
        super().__init__(group)

        # -1: For this type of image, a convert_alpha is more appropriate
        self.image = py.image.load("graphics/0.png").convert_alpha()
        #it should be convert_alpha() because of the transparent background and without the _alpha, it would just have a black background which would not look nice or meet the standard.
    
        SCREEN_W = py.display.get_window_size()[0]
        SCREEN_H = py.display.get_window_size()[1]
        self.rect = self.image.get_rect(center=(SCREEN_W / 2, SCREEN_H / 30))

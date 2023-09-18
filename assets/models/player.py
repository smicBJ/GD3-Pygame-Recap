import pygame as py
SCREEN_W = py.display.get_window_size()[0]
SCREEN_H = py.display.get_window_size()[1]


class Player(py.sprite.Sprite):

    def __init__(self, group):
        # Call the parents init
        super().__init__(group)

        # Create an image
        self.image = py.image.load("assets/graphics/player_ship.png").convert_alpha()

        # It needs a rect
        self.rect = self.image.get_rect(center=(SCREEN_W / 2, SCREEN_H - 80))
import pygame as py


class Player(py.sprite.Sprite):

    def __init__(self, group):
        # call parent class, I hope it picks up the call
        super().__init__(group)

        self.image = py.image.load("assets/0.png").convert_alpha()

        SCREEN_W = py.display.get_window_size()[0]
        SCREEN_H = py.display.get_window_size()[1]
        # GET RECT LOL 
        self.rect = self.image.get_rect(center=(SCREEN_W/2, SCREEN_H-80))

        # -1: The following lines are not needed
        # The following lines do not exist anymore

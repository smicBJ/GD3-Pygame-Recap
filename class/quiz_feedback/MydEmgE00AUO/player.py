import pygame as py

SCREEN_W = py.display.get_window_size()[0]
SCREEN_H = py.display.get_window_size()[1]


class Player(py.sprite.Sprite):
    def __init__(self,group):
        # Call the parents init
        super().__init__(group)

        self.image = py.image.load("Unit 2 Quiz - assets/0.png").convert_alpha()

        self.rect = self.image.get_rect(center=(SCREEN_W/2, SCREEN_H-80))

        # -1: For the quiz we do not need the following lines and method
        # Vector base movement Vector needs 2 value to create an actual verctor
        self.position = py.math.Vector2(self.rect.center)
        self.direction = py.math.Vector2()
        self.speed = 250

    def input(self):
        keys = py.key.get_pressed()

        if keys(py.K_w):
            self.direction.y = -1
        else:
            self.direction.y = 0
            #WHY DO WE SET IT BACK




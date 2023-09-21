import pygame as py


class Player(py.sprite.Sprite):

    def __init__(self, group):
        # Call the parents init
        super().__init__(group)

        # Create an image
        self.image = py.image.load("assets/graphics/player_ship.png").convert_alpha()

        # It needs a rect
        SCREEN_W = py.display.get_window_size()[0]
        SCREEN_H = py.display.get_window_size()[1]
        self.rect = self.image.get_rect(center=(SCREEN_W / 2, SCREEN_H - 80))

        # Vector based movement
        self.position = py.math.Vector2(self.rect.center)
        self.direction = py.math.Vector2()
        self.speed = 250

    def input(self):
        keys = py.key.get_pressed()

        if keys[py.K_w]:
            self.direction.y = -1
        else:
            self.direction.y = 0

    def move(self, delta_time):
        self.position += self.speed * self.direction * delta_time

    def update(self):
        self.input()

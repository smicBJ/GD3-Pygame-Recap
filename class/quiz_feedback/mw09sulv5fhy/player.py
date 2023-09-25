import pygame as py
# -1: These following 3 imports are irrelevant to the task
from PIL import Image
from random import randint, choice
import math

class Player(py.sprite.Sprite):
    def __init__(self, Y):
        super().__init__()
        # -1: This is an improper way to load the image
        self.image = py.Surface(Image.open("ass/0.png").size)
        # -1: This fill is not required
        self.image.fill((255, 255, 255))
        # -1: This blit is premature as the group will draw the graphics
        self.image.blit(py.image.load('ass/0.png').convert_alpha(), (0, 0))
        # -1: The quiz did not require you to scale the image
        self.image = py.transform.scale(self.image, (50, 400))
        self.rect = self.image.get_rect()
        # -1: The following 5 lines are irrelevant to the quiz
        self.image.set_colorkey((255, 255, 255))
        self.rect.y = Y - self.image.get_size()[1]
        self.position = py.math.Vector2(self.rect.center)
        self.direction = py.math.Vector2()
        self.speed = 250

    # -1: This method is irrelevant to the quiz
    def movement(self,  mouse, dt):
        distancex = self.rect.centerx - mouse[0] if self.rect.centerx > mouse[0] else mouse[0] - self.rect.centerx
        speedx = (100 / distancex) * 1.25 if distancex != 0 else 1
        self.rect.centerx += ((1 if self.rect.centerx < mouse[0] else (-1 if self.rect.centerx > mouse[0] else 0))
                              * dt * 600 ) / speedx

    # -1: This method is irrelevant to the quiz
    def update(self, keys, mouse, action, dt):
        self.movement(mouse, dt)
        if keys[py.MOUSEBUTTONDOWN]:
            print('hi')


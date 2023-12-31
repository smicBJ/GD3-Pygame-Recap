# ✅: Missing pygame import
# added the missing import
import pygame as py


class Player(py.sprite.Sprite):
    # ✅: Missing the self argument
    # change to self argument
    # def __init__(player_img, player_rect, player_pos)
    def __init__(self, group):
        # ✅: Use the parent call instead
        # ok, change to using parent call.
        super().__init__(group)
        # added a super, to link it to parent.
        # py.sprite.Sprite.__init__(self)
        # ✅: Improper image import
        # added py.image.load, and .convert alpha
        self.image = py.image.load("Unit 2 Quiz - assets/0.png").convert_alpha()
        # ✅: Improper rect creation
        # self.rect = player_rect(0)
        # change to proper self.image.get_rect
        # ✅: You forgot to create the variables before using them, so first create SCREEN_W and SCREEN_H
        # create the variables:
        SCREEN_W = py.display.get_window_size()[0]
        SCREEN_H = py.display.get_window_size()[1]
        self.rect = self.image.get_rect(center=(SCREEN_W / 2, SCREEN_H - 100))
        # self.rect.topLeft = init_pos


# ✅: Missing pygame import
#added the missing import
import pygame as py


class Player(py.sprite.Sprite):
    # ✅: Missing the self argument
    #change to self argument
    #def __init__(player_img, player_rect, player_pos)
    def __init__(self, group):
        # ✅: Use the parent call instead
        # ok, change to using parent call.
        super().__init__(group)
        #added a super, to link it to parent.
        # py.sprite.Sprite.__init__(self)
        # ✅: Improper image import
        #added py.image.load, and .convert alpha
        self.image = py.image.load("Unit 2 Quiz - assets/0.png").convert_alpha()
        # ✅: Improper rect creation
        #self.rect = player_rect(0)
        # change to proper self.image.get_rect
        # -1: You forgot to create the variables before using them, so first create SCREEN_W and SCREEN_H
        self.rect = self.image.get_rect(center=(SCREEN_W / 2, SCREEN_H / 2))
        # self.rect.topleft = init_pos


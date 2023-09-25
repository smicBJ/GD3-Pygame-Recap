# -1: Missing pygame import
#added the missing import
import pygame as py


class Player(py.sprite.Sprite):
    # -1: Missing the self argument
    #change to self argument
    #def __init__(player_img, player_rect, player_pos)
    def __init__(self, group):
        # -1: Use the parent call instead
        # ok, change to using parent call.
        super().__init__(group)
        #added a super, to link it to parent.
        # py.sprite.Sprite.__init__(self)
        # -1: Improper image import
        #added py.image.load, and .convert alpha
        self.image = py.image.load("Unit 2 Quiz - assets/0.png").convert_alpha()
        # -1: Improper rect creation
        #self.rect = player_rect(0)
        # change to proper self.image.get_rect
        self.rect = self.image.get_rect(center=(SCREEN_W / 2, SCREEN_H / 2))
        # self.rect.topleft = init_pos


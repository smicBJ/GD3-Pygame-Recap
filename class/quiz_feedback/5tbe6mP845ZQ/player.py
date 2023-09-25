# -1: Missing pygame import
class Player(pygame.sprite.Sprite):
    # -1: Missing the self argument
    def _init_(player_img, player_rect, player_pos)
        # -1: Use the parent call instead
        pygame.sprite.Sprite.__init__(self)
        # -1: Improper image import
        self.image = ("Unit 2 Quiz - assets/0.png")
        # -1: Improper rect creation
        self.rect = player_rect(0)
        self.rect.topleft = init_pos


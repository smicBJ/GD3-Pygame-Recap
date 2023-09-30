import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        # -1: Use the parent class otherwise the inheritance is irrelevant
        # INIT FROM PARENT CLASS
        super(Player, self).__init__()
        #pygame.sprite.Sprite.__init__(self)
        # -1: The following lines can be condensed into one line and needs to properly import the image
        self.image = pygame.image.load("unit2_quiz_assets/assets/0.png").convert_alpha()
        # REMOVED CODE FOR RESIZING IMAGE
        # self.image_size = self.rootimage.get_size()
        # self.image = pygame.transform.scale(self.rootimage, (int(self.image_size[0]/5), int(self.image_size[1]/5)))
        # -1: Missing rect
        self.rect = self.image.get_rect()

    # -1: The following 2 methods are not needed for this assignment
    # REMOVED UNNEEDED METHODS
    # def update(self, dt):
    #     key = pygame.key.get_pressed()
    #     mouse = pygame.mouse.get_pressed()

    # def display(self, surface):
    #     surface.blit(self.image, (0, 0))
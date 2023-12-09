# -6: Missing the entire player sprite file
#added a sprite file
import pygame
class Player(pygame.sprite.Sprite):

    def __init__(self, group):
        super().__init__(group)
        self.image = pygame.image.load("graphics/0.png").convert_alpha()
        SCREEN_W = pygame.display.get_window_size()[0]
        SCREEN_H = pygame.display.get_window_size()[1]
        self.rect = self.image.get_rect(center=(SCREEN_W / 2, SCREEN_H / 30))
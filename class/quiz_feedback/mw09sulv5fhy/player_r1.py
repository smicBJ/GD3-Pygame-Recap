import pygame as py
# -1: These following 3 imports are irrelevant to the task
# r1: removed unnecessary imports
class Player(py.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # -1: This is an improper way to load the image
        # r1: removed surface of image size

        # -1: This fill is not required
        # r1: removed unnecessary fill and replaced with revised image load

        # -1: This blit is premature as the group will draw the graphics
        # r1: replaced with image load

        self.image = py.image.load('ass/0.png').convert_alpha()
        # -1: The quiz did not require you to scale the image
        # r1: removed image scaling

        self.rect = self.image.get_rect()
        # -1: The following 5 lines are irrelevant to the quiz
        # r1: removed irrelevant image configurations and movement variables

    # -1: This method is irrelevant to the quiz X 2
    # r1: removed unnecessary methods that relate to image updates and movement X 2

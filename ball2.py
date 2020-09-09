import pygame
from pygame.sprite import Sprite

class Ball2(Sprite):
    """A class to represent a single ball2 in the fleet."""

    def __init__(self, ss_game):
        """Initialize the ball2 and set its starting position."""
        super().__init__()
        self.screen = ss_game.screen

        # Load the ball2 image and set its rect attribute
        self.image = pygame.image.load('images/ycircle.bmp')
        self.rect = self.image.get_rect()

        # Start each new ball2 near the top right of the screen.
        self.rect.x = self.rect.width * 39.5
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

import pygame
from pygame.sprite import Sprite

class Ball(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ss_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ss_game.screen

        # Load the ball image and set its rect attribute.
        self.image = pygame.image.load('images/rbcircle.bmp')
        self.rect = self.image.get_rect()

        # Start each new ball near the top right of the screen.
        self.rect.y = self.rect.height 
        self.rect.x = self.rect.width * 39.5 

        # Store the ball's exact horizontal position
        self.x = float(self.rect.x)

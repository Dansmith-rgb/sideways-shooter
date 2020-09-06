import pygame
from pygame.sprite import Sprite

class Bulletb(Sprite):
    """A class to manage bullets fired from the shooter."""
    def __init__(self, ss_game):
        super().__init__()
        self.screen = ss_game.screen
        self.settings = ss_game.settings
        self.color = self.settings.bulletb_color


        # Create a bullet rect at (0,0) and then set the correct position.
        self.rect = pygame.Rect(0,0, self.settings.bulletb_width, self.settings.bulletb_height)
        self.rect.midright = ss_game.shooter.rect.midright

        # Store the bullet's position as a decimal place
        self.x = float(self.rect.x)

    def update(self):
        """Move the bullet up the screen."""
        # Move the decimal position of the bullet.
        self.x += self.settings.bulletb_speed
        # Update the rect position
        self.rect.x = self.x

    def draw_bulletb(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)


import pygame
from pygame.sprite import Sprite

class Shooter(Sprite):
    """A class to manage the shooter"""

    def __init__(self, ss_game):
        """Initialize the shooter and set its starting position."""
        super().__init__()
        self.screen = ss_game.screen
        self.settings = ss_game.settings
        self.screen_rect = ss_game.screen.get_rect()

        # Load the shooter image in and get its rect.
        # Its rect is its rectangle which you detect collisions for
        self.image = pygame.image.load('images/shooter.bmp')
        self.rect = self.image.get_rect()

        # Start each new shooter at the mid left of the screen.
        self.rect.midleft = self.screen_rect.midleft

        # Store a decimal value for the shooters
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the shooter's position based on the movement flags."""
        # Update the shooter's y value, not the rect.
        if self.moving_right and self.rect.bottom < self.screen_rect.height:
            self.y += self.settings.shooter_speed
        if self.moving_left and self.rect.top > 0:
            self.y -= self.settings.shooter_speed

        
        # Moving the shooter very slowly forward
        """Move the shooter forward."""
        self.x += self.settings.shooter_speed2
        # Update rect object from self.y
        self.rect.y = self.y
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship and its current location."""
        self.screen.blit(self.image, self.rect)

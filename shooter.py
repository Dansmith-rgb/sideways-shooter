import pygame

class Shooter:
    """A class to manage the shooter"""

    def __init__(self, ss_game):
        """Initialize the shooter and set its starting position."""
        self.screen = ss_game.screen
        self.screen_rect = ss_game.screen.get_rect()

        # Load the shooter image in and get its rect.
        # Its rect is its rectangle which you detect collisions for
        self.image = pygame.image.load('images/shooter.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midleft = self.screen_rect.midleft

    def blitme(self):
        """Draw the ship and its current location."""
        self.screen.blit(self.image, self.rect)

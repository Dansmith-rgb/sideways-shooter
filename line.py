import pygame
from pygame.sprite import Sprite

class Line(Sprite):
    """A class to manage the line."""

    def __init__(self, ss_game):
        """Create a line object at the shooter's current position."""
        super().__init__()
        self.screen = ss_game.screen
        self.settings = ss_game.settings
        self.color = self.settings.line_color

        # Create a line rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.line_width, self.settings.line_height)
        self.midleft = ss_game.shooter.rect.midleft

        # Store the lines position as a decimal value.
        self.x = float(self.rect.x)

    def update(self):
        """"Move the line along the screen."""
        # Update the decimal position of the bullet
        self.x += self.settings.line_speed
        # Update the rect position.
        self.rect.x = self.x

    def draw_line(self):
        """Draw the line to the screen ."""
        pygame.draw.rect(self.screen, self.color, self.rect)

        

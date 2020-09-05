import sys

import pygame

from settings import Settings
from shooter import Shooter

class SidewaysShooter:

    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Sideways Shooter")

        self.shooter = Shooter(self)
        
    def run_game(self):
        """Start the main game loop."""
        while True:
            self._check_events()
            self.shooter.update()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    # Move the shooter to the right
                    self.shooter.moving_right = True
                elif event.key == pygame.K_c:
                    self.shooter.moving_left = True
            
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_x:
                    self.shooter.moving_right = False
                elif event.key == pygame.K_c:
                    self.shooter.moving_left = False

    def _update_screen(self):
        """Update images on the csreen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.shooter.blitme()
            
        pygame.display.flip()

if __name__ == '__main__':
        #Make a game instance, and run the game
        ss = SidewaysShooter()
        ss.run_game()
        

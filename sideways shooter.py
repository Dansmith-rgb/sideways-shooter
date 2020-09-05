import sys

import pygame


class SidewaysShooter:

    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()

        self.screen = pygame.display.set_mode((1800,800))
        pygame.display.set_caption("Sideways Shooter")

        # Set the background color
        self.bg_color = (0,255,255)

    def run_game(self):
        """Start the main game loop."""
        while True:
            # WATCH FOR KEYBOARD AND MOUSE EVENTS.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass through the loop
            self.screen.fill(self.bg_color)
            
            pygame.display.flip()

if __name__ == '__main__':
        #Make a game instance, and run the game
        ss = SidewaysShooter()
        ss.run_game()
        

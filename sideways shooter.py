import sys

import pygame

from settings import Settings
from shooter import Shooter
from bullet import Bullet
from bulletb import Bulletb


class SidewaysShooter:

    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Sideways Shooter")

        self.shooter = Shooter(self)
        self.bullets = pygame.sprite.Group()
        self.bulletbs = pygame.sprite.Group()
        
    def run_game(self):
        """Start the main game loop."""
        while True:
            self._check_events()
            self.shooter.update()
            self.bullets.update()
            self.bulletbs.update()

            # Get rid of bullets that have disappeared.
            for bullet in self.bullets.copy():
                if bullet.rect.right >= self.settings.screen_width:
                    self.bullets.remove(bullet)

            for bulletb in self.bulletbs.copy():
                if bulletb.rect.right >= self.settings.screen_width:
                    self.bulletbs.remove(bulletb)
            
            self._update_screen()

    def _check_events(self):
        LEFT = 1
        RIGHT = 3
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                self._fire_bullet()
                
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT:
                self._fire_bulletb()
                
    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_x:
            self.shooter.moving_right = True
        elif event.key == pygame.K_c:
            self.shooter.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_x:
            self.shooter.moving_right = False
        elif event.key == pygame.K_c:
            self.shooter.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the group."""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _fire_bulletb(self):
        """Create a new bullet and add it to the group."""
        new_bulletb = Bulletb(self)
        self.bulletbs.add(new_bulletb)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.shooter.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
            

        for bulletb in self.bulletbs.sprites():
            bulletb.draw_bulletb()
            
        pygame.display.flip()

if __name__ == '__main__':
        #Make a game instance, and run the game
        ss = SidewaysShooter()
        ss.run_game()
        

import sys

import pygame

from settings import Settings
from shooter import Shooter
from bullet import Bullet
from bulletb import Bulletb
from ball import Ball
from ball2 import Ball2


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
        self.balls = pygame.sprite.Group()
        self.ball2s = pygame.sprite.Group()

        self._create_fleet()
        self._create_fleet2()
        
    def run_game(self):
        """Start the main game loop."""
        while True:
            self._check_events()
            self.shooter.update()
            self._update_bullets()
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
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _fire_bulletb(self):
        """Create a new bullet and add it to the group."""
        if len(self.bulletbs) < self.settings.bulletbs_allowed:
            new_bulletb = Bulletb(self)
            self.bulletbs.add(new_bulletb)

    def _update_bullets(self):
        """Update position of bullerts and get rid of old bullets."""
        # Update bullet positions
        self.bullets.update()
        self.bulletbs.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.right >= self.settings.screen_width:
                self.bullets.remove(bullet)

        for bulletb in self.bulletbs.copy():
            if bulletb.rect.right >= self.settings.screen_width:
                self.bulletbs.remove(bulletb)

    def _create_fleet(self):
        """Create the fleet of balls."""
        # Create a ball and find the number of balls in one row.
        # Spacing between ball is equal to one balls width.
        ball = Ball(self)
        ball_width = ball.rect.height
        available_space_x = self.settings.screen_width
        number_balls_x = available_space_x // (6 * ball_width)
        
        # Create the first row of aliens.
        for ball_number in range(number_balls_x):
            # Create a ball and place it in the row.
            ball = Ball(self)
            ball.y = 3 * ball_width + (6 * ball_width * ball_number) 
            ball.rect.y = ball.y
            self.balls.add(ball)

    def _create_fleet2(self):
        """Create the fleet of ball2s."""
        # Create a yellow ball and find the number of balls in a row.
        # Spacing between each ball is equal to one ball width.
        ball2 = Ball2(self)
        ball_width2 = ball2.rect.height
        available_space_x2 = self.settings.screen_width
        number_ball2s_x = available_space_x2 // (6 * ball_width2 )

        # Create the first row of balls.
        for ball2_number in range(number_ball2s_x):
            # Create a ball and place it in the row.
            ball2 = Ball2(self)
            ball2.y =  6 * ball_width2 * ball2_number 
            ball2.rect.y = ball2.y
            self.ball2s.add(ball2)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.shooter.blitme()
        
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
            

        for bulletb in self.bulletbs.sprites():
            bulletb.draw_bulletb()

        self.balls.draw(self.screen)
        self.ball2s.draw(self.screen)
            
        pygame.display.flip()

if __name__ == '__main__':
        #Make a game instance, and run the game
        ss = SidewaysShooter()
        ss.run_game()
        

import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from line import Line
from play_button import PlayButton
from settings_button import SettingsButton, SettingsMenu
from shooter import Shooter
from bullet import Bullet
from bulletb import Bulletb
from ball import Ball
from ball2 import Ball2

#flag = False
pause = False
class SidewaysShooter:

    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Sideways Shooter")

        # Create an instance to store game statistics.
        self.stats = GameStats(self)
        self.shooter = Shooter(self)
        self.lines = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.bulletbs = pygame.sprite.Group()
        self.balls = pygame.sprite.Group()
        self.ball2s = pygame.sprite.Group()

        self._create_fleet()
        self._create_fleet2()

        # Make the play button.
        self.play_button = PlayButton(self, "Right wheel to play")

        # Make the Settings button.
        self.settings_button = SettingsButton(self, "Settings")

        # Make the setttings menu
        self.settings_menu = SettingsMenu(self, "fast or slow press y or n")
        
    def run_game(self):
        """Start the main game loop."""
        Running, Pause = 0, 1
        state = Running
        while True:
            self._check_events()
            if self.stats.game_active:
                self._check_events()
                self.shooter.update()
                self._update_bullets()
                self._update_shooter()
                self.check_if_empty()

                        
            self._update_screen()

    def _check_events(self):
        LEFT = 1
        MIDDLE = 2
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
                #mouse_pos2 = pygame.mouse.get_pos()
                #self._check_play_button(mouse_pos2)
                #None
                self._fire_bullet()

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == MIDDLE:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
                #pause
                
                #self._check_settings_button(mouse_pos)

            #elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos2 = pygame.mouse.get_pos()
                self.settings_button.flag = True
                #self._check_settings_button(mouse_pos2)
                
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT:
                #mouse_pos = pygame.mouse.get_pos()
                #self._check_play_button(mouse_pos) 
                self._fire_bulletb()
                
    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        
        if button_clicked and not self.stats.game_active:
            # Reset the game statistics.
            self.stats.reset_stats()
            self.stats.game_active = True

            # Get rid of any remaining balss and aliens
            self.balls.empty()
            self.ball2s.empty()
            self.bullets.empty()
            self.bulletbs.empty()
            self.lines.empty()
            self.shooter3()

            # Create a new fleet.
            self._create_fleet()
            self._create_fleet2()

            # Hide the mouse cursor.
            pygame.mouse.set_visible(False)
        

    def _check_settings_button(self, mouse_pos2):
        """load the settings when the player clicks settings"""
        if self.settings_button.rect.collidepoint(mouse_pos2):
            #self.settings_button.flag = True
            #self.settings_menu.check_image()
            self.settings_menu.draw_button()

    
        
                        
    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_x:
            self.shooter.moving_right = True
        elif event.key == pygame.K_c:
            self.shooter.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_line()
        elif event.key == pygame.K_RIGHT:
            self.settings_button.flag = True
        elif event.key == pygame.K_LEFT:
            self.settings_button.flag = False
            self.settings_menu.draw_button()
            pygame.mouse.set_visible(True)
        elif event.key == pygame.K_y:
            self.settings.shooter_speed2 = 0.09
        elif event.key == pygame.K_n:
            self.settings.shooter_speed2 = 0.01
        elif event.key == pygame.K_p:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)
            self.settings_button.flag = False
            #self.settings_button()
            self.balls.empty()
            self.ball2s.empty()
            self.bullets.empty()
            self.bulletbs.empty()
            self.lines.empty()
            self.shooter3()
            self._create_fleet()
            self._create_fleet2()
        elif event.key == pygame.K_q:
            sys.exit()

    def shooter3(self):
        self.shooter = Shooter(self)

    def check_if_empty(self):
        if len(self.balls) == 0:
            pass

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
        self.lines.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.right >= self.settings.screen_width:
                self.bullets.remove(bullet)

        for bulletb in self.bulletbs.copy():
            if bulletb.rect.right >= self.settings.screen_width:
                self.bulletbs.remove(bulletb)

        self._check_bullet_ball_collisions()
        
    def _check_bullet_ball_collisions(self):
        """Respond to bullet-ball collisions."""
        # Remove any bullets and balls that have collided.
        # Check for any bullets that have hit any balls
        #  If so, get rid of the bullets and the ball
        collisions = pygame.sprite.groupcollide(self.bullets, self.balls, True, True)
        colllision2 = pygame.sprite.groupcollide(self.bulletbs, self.ball2s, True, True)
        collisions3 = pygame.sprite.groupcollide(self.lines, self.balls, True, True)
        collisions4 = pygame.sprite.groupcollide(self.lines, self.ball2s, True, True)

        if collisions3 or collisions4 == True:
            self._shooter_hit()
            
    def _update_shooter(self):
        """Update the position of the shooter."""
        self.shooter.update()

        # Look for ball-shooter collisions.
        if pygame.sprite.spritecollideany(self.shooter, self.balls):
            self._shooter_hit()

        if pygame.sprite.spritecollideany(self.shooter, self.ball2s):
            self._shooter_hit()

    
    def _shooter_hit(self):
        """Respond to the shooter being hit."""
        if self.stats.shooters_left > 0:
            self.stats.shooters_left -= 1

            # Get rid of any remaining balls and bullets.
            self.balls.empty()
            self.ball2s.empty()
            self.bullets.empty()
            self.bulletbs.empty()
            self.lines.empty()

            # Create a new fleet
            self.shooter3()
            self._create_fleet()
            self._create_fleet2()

            # Pause.
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)
                
    def _create_fleet(self):
        """Create the fleet of balls."""
        # Create a ball and find the number of balls in one row.
        # Spacing between ball is equal to one balls width.
        ball = Ball(self)
        ball_width = ball.rect.height
        ball_width, ball_height = ball.rect.size
        available_space_x = self.settings.screen_width 
        number_balls_x = available_space_x // (6 * ball_width)
 
        # Determine the number of rows of aliens that fit on the screen.
        ship_height = self.shooter.rect.height
        available_space_y = self.settings.screen_height 
        number_rows = available_space_y // (2 * ball_height)
        
        # Create the first fleet of aliens.
        for row_number in range(number_rows):
            for ball_number in range(number_balls_x):
                # Create a ball and place it in the row.
                ball = Ball(self)
                ball_width, ball_height = ball.rect.size
                ball.y = 2 * ball_width + (5 * ball_width * ball_number) 
                ball.rect.y = ball.y
                ball.rect.x =  19 *  ball_width  + (2 * ball_width * row_number) 
                self.balls.add(ball)

    def _create_fleet2(self):
        """Create the fleet of ball2s."""
        # Create a yellow ball and find the number of balls in a row.
        # Spacing between each ball is equal to one ball width.
        ball2 = Ball2(self)
        ball_width2 = ball2.rect.height
        ball_width2, ball_height2  = ball2.rect.size
        available_space_x2 = self.settings.screen_width
        number_ball2s_x = available_space_x2 // (6 * ball_width2)

        # Determine the number of balls that fit on the screen
        shooter_height = self.shooter.rect.height
        available_space_y2 = self.settings.screen_width
        number_rows2 = available_space_y2 // (2 * ball_height2)

        # Create the first fleet of balls.
        for row_number2 in range(number_rows2):
            for ball2_number in range(number_ball2s_x):
                # Create a ball and place it in the row.
                ball2 = Ball2(self)
                ball_width2, ball_height2 = ball2.rect.size
                ball2.y =  5 * ball_width2 * ball2_number
                ball2.rect.y = ball2.y
                ball2.rect.x =  19 * ball_width2 + (2 * ball_width2 * row_number2)
                self.ball2s.add(ball2)

    def _fire_line(self):
        """Create a new line and add it to the lines group."""
        for i in range(1):
            new_line = Line(self)
            self.lines.add(new_line)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
         # Draw the play button if the game is inactive.
        #if not self.stats.game_active:
            #self.play_button.draw_button()
            
        self.screen.fill(self.settings.bg_color)
        self.shooter.blitme()
        #self._fire_line()
        
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
            

        for bulletb in self.bulletbs.sprites():
            bulletb.draw_bulletb()

        for line in self.lines.sprites():
            #self._fire_line()
            line.draw_line()
            
            
        self.balls.draw(self.screen)
        self.ball2s.draw(self.screen)

        # Draw the play button if the game is inactive.
        if not self.stats.game_active:
            self.play_button.draw_button()

        # Draw the settings if the game is inactive.
        if not self.stats.game_active:
            self.settings_button.draw_button()

        if self.settings_button.flag == True and not self.stats.game_active:
            #self.settings_menu.check_image()
            self.settings_menu.draw_button()
            
        pygame.display.flip()

if __name__ == '__main__':
        #Make a game instance, and run the game
        ss = SidewaysShooter()
        ss.run_game()
        

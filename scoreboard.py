import pygame.font
from pygame.sprite import Group
from shooter import Shooter

class Scoreboard:
    """A class to report scoring information."""

    def __init__(self, ss_game):
        """Initialize scorekeeping attributes."""
        self.ss_game = ss_game
        self.screen = ss_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ss_game.settings
        self.stats = ss_game.stats

        # Font settings for scoring information.
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare the initial score images.
        self.prep_score()
        self.prep_high_score()
        self.prep_shooters()

    def prep_score(self):
        """Turn the score into a rendered image."""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # Display the score at the top left of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.left = self.screen_rect.left + 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Turn the high score in to a rendered image."""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)

        # Center the high score at the top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_shooters(self):
        """Show how many shooters are left."""
        self.shooters = Group()
        for shooter_number in range(self.stats.shooters_left):
            shooter = Shooter(self.ss_game)
            shooter.rect.x = 10 + shooter_number * shooter.rect.width
            shooter.rect.y = 100
            self.shooters.add(shooter)
    

    def check_high_score(self):
        """Check to see if there's a neew high score."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def show_score(self):
        """Draw scores and shooters to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.shooters.draw(self.screen)
      





        

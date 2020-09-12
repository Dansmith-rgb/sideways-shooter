class Settings:
    """A class to store all the settings for Sideways Shooter."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1800
        self.screen_height = 800
        self.bg_color = (0, 255, 255)
        
        # Shooter settings
        self.shooter_speed = 2.5
        self.shooter_limit = 3

        # Bullet settings
        self.bullet_speed = 2
        self.bullet_width = 15
        self.bullet_height = 50
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 4

        # Bulletb settings
        self.bulletb_speed = 2
        self.bulletb_width = 15
        self.bulletb_height = 50
        self.bulletb_color = (255, 255, 0)
        self.bulletbs_allowed = 4

        # Ball speed
        self.shooter_speed2 = 0.06

        # Follow up line
        self.line_speed = 0.12
        self.line_width = 5
        self.line_height = 800
        self.line_color = (255, 0, 0)

        
 

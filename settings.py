class Settings:
    """A class to store all the settings for Sideways Shooter."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1800
        self.screen_height = 800
        self.bg_color = (0, 255, 255)
        
        # Shooter settings
        self.shooter_speed = 1.5

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3

        # Bulletb settings
        self.bulletb_speed = 1.0
        self.bulletb_width = 15
        self.bulletb_height = 3
        self.bulletb_color = (255, 255, 0)

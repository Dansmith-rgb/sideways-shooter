class GameStats:
    """Track statistics for Sideways Shooter."""

    def __init__(self, ss_game):
        """Initialize statistics."""
        self.settings = ss_game.settings
        self.reset_stats()

        # Start Sideways Shooter in an active state.
        self.game_active = False

        # High score should never be reset.
        self.high_score = 0

    def reset_stats(self):
        "Initialzie statistics that can change during the game."""
        self.shooters_left = self.settings.shooter_limit
        self.score = 0
    

class GameStats:
    """Track statistics for Alien Invasion"""

    def __init__(self, ai_settings):
        """Initialize statistics"""
        self.ai_settings = ai_settings
        # Start game in an inactive state
        self.game_active = False
        # High score should never be reset
        self.high_score = 0

        # Variables to be initialized outside of __init__
        self.ships_left = None
        self.score = None
        self.level = None

        self.reset_stats()

    def reset_stats(self):
        """Initialize statistics that can change throughout the game"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1


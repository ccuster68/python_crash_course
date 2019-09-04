import json


class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()
        # Start game in an inactive state.
        self.game_active = False
        # High score should never be reset.
        # Get High Score
        try:
            with open('high_score.json') as high_score:
                self.high_score = int(json.load(high_score))
        except:
            with open('high_score.json', 'w') as high_score:
                json.dump('0', high_score)

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

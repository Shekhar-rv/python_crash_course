# All the setting required for pygame will be stored here


class Settings:
    """A class to store all the settings for Alien Invasion"""

    def __init__(self) -> None:
        """Initialize the game settings."""
        # Screen settings
        self.screen_width = 1920
        self.screen_height = 1080
        self.bg_color = (12, 22, 79)
        self.image_width = 60
        self.image_height = 120

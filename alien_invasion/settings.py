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
        # Ship settings
        self.ship_speed_factor = 1.5
        # Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 57, 255, 20 # Neon Green

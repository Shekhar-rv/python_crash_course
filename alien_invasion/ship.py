import pygame


class Ship:
    """This class manages most of the behaviour of the player's ship"""

    def __init__(self, ai_settings, screen) -> None:
        """Initialize the ship and set its starting position."""
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ship image and get its rect.
        self.image = pygame.image.load("images/ship.bmp")
        self.image = pygame.transform.scale(
            self.image, (ai_settings.image_width, ai_settings.image_height)
        )
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start the ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)
        self.bottom = float(self.rect.bottom)

        # Set moving flag.
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the ship's position based on the movement of the flag."""
        # Update the ship's center value, not the rect and make sure the ship doesn't go over the edges of the screen.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.bottom -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.bottom += self.ai_settings.ship_speed_factor

        # Update rect object from self.center.
        self.rect.centerx = self.center
        self.rect.bottom = self.bottom

    def blitme(self) -> None:
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

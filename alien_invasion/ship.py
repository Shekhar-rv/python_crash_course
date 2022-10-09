import pygame
from settings import Settings


class Ship:
    """This class manages most of the behaviour of the player's ship"""

    def __init__(self, screen) -> None:
        """Initialize the ship and set its starting position."""
        self.screen = screen
        ai_settings = Settings()

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
        # Set moving flag.
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement of the flag."""
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1

    def blitme(self) -> None:
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

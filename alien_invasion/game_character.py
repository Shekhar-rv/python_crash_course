import pygame
from settings import Settings

class Character():
    """This class manages most of the behaviour of the player's character"""

    def __init__(self, screen) -> None:
        """Initialize the character and set its starting position."""
        self.screen = screen
        ai_settings = Settings()

        # Load the character image and get its rect.
        self.image = pygame.image.load("images/game_character.bmp")
        self.image = pygame.transform.scale(self.image, (ai_settings.image_width, ai_settings.image_height))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start the character at the bottom center of the screen.
        # self.rect.centerx = self.screen_rect.centerx
        self.rect.center = self.screen_rect.center

    def blitme(self) -> None:
        """Draw the character at its current location"""
        self.screen.blit(self.image, self.rect)
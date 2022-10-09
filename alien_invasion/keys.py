import pygame
from os import sys
from settings import Settings


def run_game():
    # Initialise game, settings and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Print keys pressed")

    # Start the main loop for the game.
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print(event.key)


if __name__ == "__main__":
    run_game()

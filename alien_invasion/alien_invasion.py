from numpy import character
import pygame
from settings import Settings
from ship import Ship
from game_functions import check_events, update_screen
from game_character import Character

def run_game():
    # Initialise game, settings and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship.
    ship = Ship(screen=screen)
    # Make a game character
    character = Character(screen=screen)


    # Start the main loop for the game.
    while True:
        # Call the check events fn to watch for keyboard and mouse events.
        check_events()
        # Redraw the screen during each pass through the loop.
        update_screen(ai_settings=ai_settings, screen=screen,ship=ship, character=character)


if __name__ == "__main__":
    run_game()
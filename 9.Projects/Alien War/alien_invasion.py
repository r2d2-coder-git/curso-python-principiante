import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien

def run_game():
 # Initialize game and create a screen object.
    pygame.init()
    bg_color = (230,230,230)
    screen_width = 1200
    screen_height = 800
    game_settings = Settings(screen_width, screen_height, bg_color)
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(screen,'.\imgs\ship.png',game_settings)
    alien = Alien(game_settings,screen)
    bullets = Group()
    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        gf.check_events(game_settings, screen, ship, bullets)
        gf.update_bullets(bullets)
        gf.update_screen(game_settings,screen, ship, alien, bullets)
run_game()
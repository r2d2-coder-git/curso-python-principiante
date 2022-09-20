import pygame
import sys

def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            if event.key == pygame.K_LEFT:
                ship.moving_left = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right =False
            if event.key == pygame.K_LEFT:
                ship.moving_left = False
def update_screen(game_settings, screen, ship):
    screen.fill(game_settings.bg_color)
    ship.update() #first update events 
    ship.blitme() #second draw in the screen
    pygame.display.flip()
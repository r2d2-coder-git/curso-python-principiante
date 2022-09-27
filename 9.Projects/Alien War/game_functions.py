import pygame
import sys
from bullet import Bullet

def check_events(ai_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        #KEY DOWN
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT: #Move ship to right
                ship.moving_right = True
            elif event.key == pygame.K_LEFT: #Move ship to left
                ship.moving_left = True
            elif event.key == pygame.K_SPACE and len(bullets) < ai_settings.bullets_allowed: #Shot
                fire_bullet(ai_settings, screen, ship ,bullets)     
        #KEY UP
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right =False
            if event.key == pygame.K_LEFT:
                ship.moving_left = False
def update_screen(game_settings, screen, ship, alien, bullets):
    screen.fill(game_settings.bg_color)
    ship.update() #first update events 
    ship.blitme() #second draw in the screen
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    alien.blitme()
    pygame.display.flip()

def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy(): #To delete the bullets that dissapear from the screen.
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    print(len(bullets))

def fire_bullet(ai_settings, screen, ship, bullets):
    new_bullet = Bullet(ai_settings,screen,ship)
    bullets.add(new_bullet)
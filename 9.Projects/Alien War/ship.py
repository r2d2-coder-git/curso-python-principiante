import pygame

class Ship():
    def __init__(self, screen:pygame.Surface,path_to_img:str):
        #Take the screen and load the image, it also loads position of screen and image
        self.screen = screen 
        self.image = pygame.image.load(path_to_img)
        self.image = pygame.transform.scale(self.image,(self.screen.get_height()*20/100, self.screen.get_width()*20/100)) #Ship resize to 20% of the screen
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        #We assign to the image the positions from the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self._moving_right = False
        self._moving_left = False
    def blitme(self):
        self.screen.blit(self.image, self.rect) #Draw the ship into the screen.
    def update(self):
        if self.moving_left:
            self.rect.centerx -= 1
        if self.moving_right:
            self.rect.centerx += 1
    @property
    def moving_right(self):
        return self._moving_right
    @property
    def moving_left(self):
        return self._moving_left
    @moving_right.setter
    def moving_right(self, status):
        self._moving_right = status
    @moving_left.setter
    def moving_left(self, status):
        self._moving_left = status


        


import pygame
from pygame.sprite import Sprite


class Square(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        # load alien assets and set rect attribute
        self.image = pygame.image.load('images/target.bmp')
        self.rect = self.image.get_rect() 
        


        

        self.rect.midleft = self.screen_rect.midleft

        # store position
        self.y = float(self.rect.y) 

    
    def update(self):
        # move square to right initially. direction is dependent on fleet direction (-1 = go left, 1 = go right)
        self.y -= self.settings.alien_speed * self.settings.fleet_direction
        self.rect.y = self.y
        

    def check_if_hit_edge(self):
        # returns true if alien is at edge
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom or self.rect.top <= 0:
            return True
            



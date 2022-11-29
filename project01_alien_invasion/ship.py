import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        # init ship and its position
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # load the ship image and get its rect
        self.image = pygame.image.load("images/ship.bmp")
        IMAGE_SMALL = pygame.transform.scale(self.image, (5, 50))
        self.rect = self.image.get_rect()
        
        # start at bottom
        self.rect.midbottom = self.screen_rect.midbottom

        # position (convert to float, because rect values only store integers)
        self.x = float(self.rect.x)

        # controls
        self.moving_right = False
        self.moving_left = False
        self.ship_speed = 1.5

    # update self
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        elif self.moving_left and self.rect.left > 0: 
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)
    
    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
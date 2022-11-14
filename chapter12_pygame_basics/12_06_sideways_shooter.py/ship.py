import pygame


class Ship():
    def __init__(self, ai_game):

        # init ship and its position
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # load the ship image and get its rect
        self.image = pygame.image.load("images/ship.bmp")
        img_with_flip = pygame.transform.flip(self.image, True, False)
        self.rect = img_with_flip.get_rect()
        
        # start at bottom
        
        #rectXpos = 550
        #rectYpos = 750
        #self.rect = pygame.rect.Rect(rectXpos, rectYpos, 50, 50)
        
        self.rect.midright = self.screen_rect.midright

        # position (convert to float, because rect values only store integers)
        self.y = float(self.rect.y)

        # controls
        self.moving_up = False
        self.moving_down = False
        self.ship_speed = 1.5

    # update self
    def update(self):
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        elif self.moving_up and self.rect.top  > 0: 
            self.y -= self.settings.ship_speed

        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)

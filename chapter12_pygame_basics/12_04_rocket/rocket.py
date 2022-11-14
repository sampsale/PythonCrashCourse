import pygame


class Rocket:
    def __init__(self, rocketgame):

        # init: screen from rocketgame.py
        self.screen = rocketgame.screen
        self.screen_rect = rocketgame.screen.get_rect()

        # image from bitmap
        self.image = pygame.image.load("dude.bmp")
        self.rect = self.image.get_rect()

        # controls
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.speed = 1.5

        # placing
        self.rect.center = self.screen_rect.center



    # place self
    def place_me(self):
        self.screen.blit(self.image, self.rect)
    # update self
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += 1
        elif self.moving_left and self.rect.left > 0:
            self.rect.x -= 1
        elif self.moving_up and self.rect.top > 0:
            self.rect.y -= 1
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += 1

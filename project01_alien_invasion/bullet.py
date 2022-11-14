import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # create bullet rect at 0,0 and then set position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # speed will be float 
        self.y = float(self.rect.y)

    def update(self):
        # update y based on speed
        self.y -= self.settings.bullet_speed
        # update the rect position
        self.rect.y = self.y

    # draw the bullet
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
import pygame
from pygame.sprite import Sprite


class AlienBomb(Sprite):
    def __init__(self, ai_game, alien):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bomb_color

        # create bomb rect at 0,0 and then set position
        self.rect = pygame.Rect(0, 0, self.settings.bomb_width, self.settings.bomb_height)
        self.rect.midbottom = alien.rect.midbottom

        # speed will be float 
        self.y = float(self.rect.y)

        # direction
        self.direction = 'UP'

    def update(self):
        # update y based on speed
        self.y += self.settings.bomb_speed
        # update the rect position
        self.rect.y = self.y

    # draw the bomb
    def draw_bomb(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
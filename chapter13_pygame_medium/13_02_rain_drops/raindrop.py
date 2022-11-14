import pygame
from pygame.sprite import Sprite


class RainDrop(Sprite):
    def __init__(self, star_display):
        super().__init__()
        self.screen = star_display.screen
        self.image = pygame.image.load('star.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width - 500
        self.rect.y = self.rect.height 
    
        self.x = float(self.rect.x)

    def update(self):
        self.rect.y += 1

    def check_if_hit_edge(self):
        screen_rect = self.screen.get_rect()
        if self.rect.bottom > 800:
            return True
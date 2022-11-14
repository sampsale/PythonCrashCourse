import pygame
import sys


class GameCharacter():
    def __init__(self, background):
        # init ship and its position
        self.screen = background.screen
        self.screen_rect = background.screen.get_rect()

        # load the ship image and get its rect
        self.image = pygame.image.load("stickman.bmp")
        self.rect = self.image.get_rect()
        # start at bottom
        self.rect.center = self.screen_rect.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)

class Screen():

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        self.bg_color = (3, 157, 252)
        pygame.display.set_caption('Blue Sky')
        self.character = GameCharacter(self)

    def run_game(self):
        self.screen.fill(self.bg_color)
        while True:
            self.screen.fill(self.bg_color)
            self.character.blitme()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.flip()

if __name__ == '__main__':
    # make a game instance and run the game
    bluesky = Screen()
    bluesky.run_game()
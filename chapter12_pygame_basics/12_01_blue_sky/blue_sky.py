import pygame
import sys

class BlueSky():

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        self.bg_color = (3, 157, 252)
        pygame.display.set_caption('Blue Sky')

    def run_game(self):
        self.screen.fill(self.bg_color)
        while True:
            self.screen.fill(self.bg_color)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.flip()

if __name__ == '__main__':
    # make a game instance and run the game
    bluesky = BlueSky()
    bluesky.run_game()
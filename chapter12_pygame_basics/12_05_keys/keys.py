import sys
import pygame


class Keys:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))


    # just print event keys
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    print(event)

if __name__ == '__main__':
    keys = Keys()
    keys.run_game()

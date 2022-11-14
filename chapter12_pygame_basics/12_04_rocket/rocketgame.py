import sys
import pygame
from rocket import Rocket


class RocketGame:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        self.bg_color = (3, 157, 252)
        pygame.display.set_caption('Rocket')

        self.rocket = Rocket(self)

    def run_game(self):
        self.screen.fill(self.bg_color)

        while True:
            # fill background
            self.screen.fill(self.bg_color)
            # place rocket
            self.rocket.place_me()
            # update rocket
            self.rocket.update()
            # check for keys
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self.check_down_events(event)
                elif event.type == pygame.KEYUP:
                    self.check_up_events(event)

            pygame.display.flip()

    def check_down_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = True
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = True

    def check_up_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = False
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = False


if __name__ == '__main__':
    rocket = RocketGame()
    rocket.run_game()

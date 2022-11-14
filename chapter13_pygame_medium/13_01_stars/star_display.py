import sys
import pygame
from star import Star
from random import randint

class StarDisplay():
    # init
    def __init__(self):
        self.screen = pygame.display.set_mode((1500, 800))
        pygame.display.set_caption('Stars in the sky')

        self.stars = pygame.sprite.Group()

        self.create_star_sky()
    # run
    def run_star_sky(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.flip()
            self.screen.fill((0, 0, 0))
            self.stars.draw(self.screen)
    # create star sky
    def create_star_sky(self):
        star = Star(self)
        star_width = star.rect.width
        star_height = star.rect.height
        # available space is screen width - star_width for x and for y screen height
        available_space_x = 1500 - (star_width)
        available_space_y = 800

        number_rows = available_space_y // (2*star_height)
        number_stars_per_row = available_space_x // (2*star_width)

        for row_number in range(number_rows):
            for number_star in range(number_stars_per_row):
                self.create_star(number_star, row_number)
    # create stars
    def create_star(self, number_star, row_number):
        # add randomness to position
        randomness = randint(-40, 40)
        star = Star(self)
        star_width = star.rect.width
        star_height = star.rect.height
        star.rect.x = (star_width + 2 * star_width * number_star) + randomness
        star.rect.y = (star_height + 2 * star_height * row_number) + randomness
        self.stars.add(star)


star_display = StarDisplay()
star_display.run_star_sky()

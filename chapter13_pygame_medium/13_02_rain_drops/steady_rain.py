import sys
import pygame
from raindrop import RainDrop
from random import randint


class SteadyRain():

    def __init__(self):

        pygame.init()
        self.screen = pygame.display.set_mode((1500, 800))
        pygame.display.set_caption('Rain drops')

        self.raindrops = pygame.sprite.Group()
        self.create_rain()

    def run_rain_drops(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.flip()
            self.screen.fill((3, 152, 252))
            self.raindrops.draw(self.screen)
            self.raindrops.update()
            self.check_if_raindrop_hit_edge()
            self.create_rain()

    # create rain
    def create_rain(self):

        raindrop = RainDrop(self)
        raindrop_width = raindrop.rect.width
        raindrop_height = raindrop.rect.height
        # available space is screen width - raindrop_width for x and for y screen height
        # ADD 200 TO HEIGHT, that will be added to raindrop spawn height
        w, h = pygame.display.get_surface().get_size()

        available_space_x = w - (raindrop_width)
        available_space_y = h + 200 

        

        number_rows = available_space_y // (2*raindrop_height)
        number_raindrops_per_row = available_space_x // (2*raindrop_width)
        
        # first time print all rows
        if (len(self.raindrops) == 0):
            for row_number in range(number_rows):
                for number_raindrop in range(number_raindrops_per_row):
                    self.create_raindrop(number_raindrop, row_number)
        
        # if total raindrops = total raindrops - 1 row, make 1 extra row
        elif (len(self.raindrops) < (number_rows-1)*number_raindrops_per_row):
            for number_raindrop in range(number_raindrops_per_row):
                self.create_raindrop(number_raindrop, 0)

    # create raindrops
    def create_raindrop(self, number_raindrop, row_number):
        # add randomness to position
        randomness = randint(-40, 40)
        raindrop = RainDrop(self)
        raindrop_width = raindrop.rect.width
        raindrop_height = raindrop.rect.height
        raindrop.rect.x = (raindrop_width + 2 *
                           raindrop_width * number_raindrop) + randomness

        # DEDUCT 200 FROM Y SO THEY SPAWN OUTSIDE OF SCREEN
        raindrop.rect.y = (
            (raindrop_height + 2 * raindrop_height * row_number) + randomness) - 200
        self.raindrops.add(raindrop)

    def check_if_raindrop_hit_edge(self):
        for raindrop in self.raindrops:
            if raindrop.check_if_hit_edge():
                self.raindrops.remove(raindrop)


raining = SteadyRain()
raining.run_rain_drops()

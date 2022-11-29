import pygame
from alien import Alien
from bomb import AlienBomb
from random import randint, choice

def update_aliens(self):
    check_fleet_edges(self)
    self.aliens.update()
    roll_for_drop_bomb(self)
    if pygame.sprite.spritecollideany(self.ship, self.aliens):
        self.ship_hit()

    # make aliens fleet
def create_fleet(self):
    # determine alien
    alien = Alien(self)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    # determine ship
    ship_height = self.ship.rect.height
    #print(f"Alien width: {alien_width} Alien height: {alien_height}")
    # available space x is screen width - 2*alien width
    available_space_x = self.settings.screen_width - (2*alien_width)
    # number of aliens per row available space divided by (2 * alien_width). Use // to make in an integer and remove the reminder
    aliens_per_row = available_space_x // (2*alien_width)
    # available space y == number of rows
    available_space_y = self.settings.screen_height - \
        (3*alien_height) - ship_height
    number_rows = available_space_y // (2*alien_height)

    #print(f"Rows: {number_rows} Aliens per row: {aliens_per_row}")
        # do as many times as number of rows
    for row_number in range(number_rows):
        # do as many times as number of aliens per row
        for alien_number in range(aliens_per_row):
                create_alien(self, alien_number, row_number)

# create aliens
def create_alien(self, alien_number, row_number):
    randomness = randint(0,20)
    alien = Alien(self)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    # assign position
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x + randomness
    alien.rect.y = (alien_height + 2 * alien_height * row_number) + randomness
    # print(
    #        f"Alien {alien_number+1} on row {row_number+1} X position: {alien.rect.x} Y position: {alien.rect.y}")
    self.aliens.add(alien)

# check if has hit edge
def check_fleet_edges(self):
    for alien in self.aliens.sprites():
        if alien.check_if_hit_edge():
            change_fleet_direction(self)
            break

# changes direction from left to right, also drops down
def change_fleet_direction(self):
    for alien in self.aliens.sprites():
        alien.rect.y += self.settings.fleet_drop_speed
    self.settings.fleet_direction *= -1


# alien drops boms
def roll_for_drop_bomb(self):
    random_alien = choice(self.aliens.sprites())

    # make magic math happen to calculate drop rate. the length of aliens is relevant, because the drop rate should always be the same
    bomb_drop_rate = int(self.settings.bomb_frequency*(len(self.aliens))/(len(self.aliens)))


    if randint(0, bomb_drop_rate) <1:
        newbomb = AlienBomb(self, random_alien)
        self.bombs.add(newbomb)

